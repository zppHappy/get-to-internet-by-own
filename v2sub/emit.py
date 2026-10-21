"""结果筛选与输出：base64 订阅、明文列表、报告。"""
from __future__ import annotations

import base64
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .parse import Node, rename_link


def _now(settings) -> datetime:
    """按配置时区取当前时间。GitHub Actions 的 runner 是 UTC，
    直接 strftime 会和用户本地时钟差 8 小时，所以这里显式换算。"""
    try:
        offset = float(settings.get("stamp_tz", 8) or 0)
    except (TypeError, ValueError):
        offset = 8.0
    return datetime.now(timezone(timedelta(hours=offset)))


def _speed_str(res) -> str:
    if not res.ok or res.speed_mbps <= 0:
        return "-"
    return f"{res.speed_mbps:.1f}MB/s"


def _cn_str(res) -> str:
    """节点名里显示的国内方向延迟：CN45 / CN- 。"""
    if getattr(res, "cn_ok", False) and res.cn_delay_ms > 0:
        return f"CN{res.cn_delay_ms}"
    return "CN-"


def select_working(results, settings) -> List[Any]:
    """按阈值筛选出可用节点，并做去重/排序/截断。"""
    max_delay = int(settings.get("max_delay_ms", 0) or 0)
    min_speed = float(settings.get("min_speed_mbps", 0) or 0)
    require_speed = bool(settings.get("require_speed", False))
    require_cn = bool(settings.get("cn_test_required", False))

    keep = []
    for r in results:
        if not r.ok:
            continue
        if max_delay and r.delay_ms > max_delay:
            continue
        if require_speed and r.speed_mbps <= 0:
            continue
        if min_speed and r.speed_mbps and r.speed_mbps < min_speed:
            continue
        if require_cn and not getattr(r, "cn_ok", False):
            continue
        keep.append(r)

    if settings.get("dedupe", True):
        best: Dict[tuple, Any] = {}
        for r in keep:
            k = r.node.key
            cur = best.get(k)
            if cur is None:
                best[k] = r
                continue
            better = (r.delay_ms < cur.delay_ms) or (
                r.delay_ms == cur.delay_ms and r.speed_mbps > cur.speed_mbps
            )
            if better:
                best[k] = r
        keep = list(best.values())

    if settings.get("cn_sort", True):
        # 先按「到国内的延迟」升序（越小越靠中国），再按普通延迟
        keep.sort(
            key=lambda r: (
                0 if getattr(r, "cn_ok", False) else 1,
                r.cn_delay_ms if getattr(r, "cn_ok", False) else 10 ** 6,
                r.delay_ms,
            )
        )
    else:
        keep.sort(key=lambda r: (-r.speed_mbps, r.delay_ms))
    limit = int(settings.get("max_nodes", 0) or 0)
    if limit > 0:
        keep = keep[:limit]
    return keep


def render_name(res, index: int, template: str, stamp: str = "") -> str:
    node: Node = res.node
    name = (node.name or f"{node.server}:{node.port}").strip()
    # 名字里已有的 "|" 会让模板看着乱，统一压缩空白
    name = " ".join(name.split())
    try:
        return template.format(
            index=index,
            name=name,
            delay=res.delay_ms,
            speed=_speed_str(res),
            proto=node.proto,
            server=node.server,
            port=node.port,
            # {time} 是「本轮筛选时间」，MMDD-HHMM，方便在客户端一眼看出新旧
            time=stamp,
            # {cn} 是经该节点访问国内目标的延迟，形如 CN45 / CN-
            cn=_cn_str(res),
        ).strip()
    except (KeyError, IndexError, ValueError):
        return f"{name} | {res.delay_ms}ms | {_speed_str(res)}"


def build_links(keep, settings, stamp: str = "") -> List[str]:
    template = settings.get("rename_template") or "{name}"
    do_rename = bool(settings.get("rename", True))
    links = []
    for i, r in enumerate(keep, 1):
        link = r.node.link
        if do_rename:
            link = rename_link(link, render_name(r, i, template, stamp))
        links.append(link)
    return links


def build_files(keep, all_results, cfg, stats) -> Dict[str, str]:
    """生成待写入/上传的文件内容。key 是逻辑名，value 是文本内容。"""
    settings = cfg["settings"]
    out_cfg = cfg["output"]
    now = _now(settings)
    stamp = now.strftime("%m%d-%H%M")
    links = build_links(keep, settings, stamp)
    plain = "\n".join(links) + ("\n" if links else "")
    b64 = base64.b64encode(plain.encode("utf-8")).decode("ascii")

    files: Dict[str, str] = {
        "base64": b64,
        "plain": plain,
    }

    report = {
        "generated_at": now.strftime("%Y-%m-%d %H:%M:%S%z"),
        "stats": stats,
        "nodes": [
            {
                "index": i,
                "name": r.node.name,
                "proto": r.node.proto,
                "server": r.node.server,
                "port": r.node.port,
                "source": r.node.source,
                "ok": r.ok,
                "delay_ms": r.delay_ms,
                "speed_mbps": r.speed_mbps,
                "cn_ok": getattr(r, "cn_ok", False),
                "cn_delay_ms": getattr(r, "cn_delay_ms", 0),
                "cn_error": getattr(r, "cn_error", ""),
                "error": r.error,
                **({"link": r.node.link} if out_cfg.get("include_links_in_report") else {}),
            }
            for i, r in enumerate(keep, 1)
        ],
        "failed": [
            {
                "name": r.node.name,
                "proto": r.node.proto,
                "server": r.node.server,
                "port": r.node.port,
                "error": r.error or "unknown",
            }
            for r in all_results
            if not r.ok
        ],
    }
    files["report"] = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    files["markdown"] = _markdown(report, keep, stats, cfg)
    return files


def _markdown(report, keep, stats, cfg=None) -> str:
    """给人和 GitHub 网页看的页面：统计 + 可读的节点表格。"""
    gh = (cfg or {}).get("github") or {}
    owner, repo = (gh.get("owner") or "").strip(), (gh.get("repo") or "").strip()
    branch = gh.get("branch") or "main"
    has_repo = bool(owner and repo)

    skipped = stats.get("skipped") or {}
    lines = [
        "# 可用节点（自动生成）",
        "",
        f"> 每次筛选后自动重写，最后更新：`{report['generated_at']}`",
        "",
    ]

    if has_repo:
        raw = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/sub/base64.txt"
        mirror = f"https://cdn.jsdelivr.net/gh/{owner}/{repo}@{branch}/sub/base64.txt"
        lines += [
            "## 订阅地址",
            "",
            "```",
            raw,
            "```",
            "",
            "国内直连 raw 经常不通，用 jsDelivr 镜像（约 12 小时缓存，加 `?t=时间戳` 可强制刷新）：",
            "",
            "```",
            mirror,
            "```",
            "",
        ]

    lines += [
        "## 本次统计",
        "",
        "| 项目 | 数量 |",
        "|---|---|",
        f"| 抓取链接 | {stats.get('total', 0)} |",
        f"| 去重后节点 | {stats.get('parsed', 0)} |",
        f"| TCP 预筛剔除 | {stats.get('precheck_dropped', 0)} |",
        f"| 真连接测试 | {stats.get('tested', 0)} |",
        f"| 测试通过 | {stats.get('ok', 0)} |",
        f"| **最终保留** | **{stats.get('kept', 0)}** |",
        f"| 耗时 | {stats.get('elapsed_sec', 0)} 秒 |",
        "",
    ]
    if any(skipped.values()):
        lines += [
            f"> 解析阶段跳过：重复 {skipped.get('dup', 0)}、协议未启用 {skipped.get('proto', 0)}、"
            f"无法解析 {skipped.get('parse', 0)}",
            "",
        ]

    # 协议分布
    by_proto: Dict[str, int] = {}
    for r in keep:
        by_proto[r.node.proto] = by_proto.get(r.node.proto, 0) + 1
    if by_proto:
        lines += [
            "## 协议分布",
            "",
            " · ".join(f"{k} {v}" for k, v in sorted(by_proto.items(), key=lambda x: -x[1])),
            "",
        ]

    cn_ok = sum(1 for r in keep if getattr(r, "cn_ok", False))
    if any(getattr(r, "cn_delay_ms", 0) or getattr(r, "cn_error", "") for r in keep):
        lines += [
            "## 国内方向探测（节点 → 中国，非中国 → 节点）",
            "",
            f"保留的 {len(keep)} 个节点中，有 **{cn_ok}** 个能经代理访问到国内目标站，"
            f"**{len(keep) - cn_ok}** 个访问不到。",
            "",
            "> 两个必须说清楚的点：",
            "> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——"
            "后者才是你实际使用的方向，必须在国内机器上测才算数。",
            "> 2. 这个延迟值被「测试机 → 节点」那段主导，"
            "**不反映节点离中国有多近**（实测香港节点比美国节点还高），"
            "所以不参与排序。只能当「能不能到」的参考。",
            "",
        ]

    lines += [
        "## 节点明细（按延迟升序）",
        "",
        "| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |",
        "|---|------|------|--------|------|------------|------|",
    ]
    for i, r in enumerate(keep[:50], 1):
        name = (r.node.name or "").replace("|", "/")[:40]
        cn_cell = f"{r.cn_delay_ms} ms" if getattr(r, "cn_ok", False) else "不可达"
        lines.append(
            f"| {i} | {name} | {r.node.proto} | `{r.node.server}:{r.node.port}` | {r.delay_ms} ms | {cn_cell} | {_speed_str(r)} |"
        )
    if len(keep) > 50:
        lines.append(f"\n> 仅展示前 50 个，共 {len(keep)} 个；完整列表见 `sub/nodes.txt`。")
    lines.append("")
    return "\n".join(lines)


def write_files(files: Dict[str, str], cfg) -> List[Path]:
    out_dir = Path(cfg["output"]["dir"])
    out_dir.mkdir(parents=True, exist_ok=True)
    name_map = {
        "base64": cfg["output"].get("base64", "base64.txt"),
        "plain": cfg["output"].get("plain", "nodes.txt"),
        "report": cfg["output"].get("report", "report.json"),
        "markdown": cfg["output"].get("markdown", "report.md"),
    }
    written = []
    for key, filename in name_map.items():
        if key not in files or not filename:
            continue
        p = out_dir / filename
        p.write_text(files[key], encoding="utf-8")
        written.append(p)
    return written
