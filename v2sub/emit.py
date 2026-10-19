"""结果筛选与输出：base64 订阅、明文列表、报告。"""
from __future__ import annotations

import base64
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

from .parse import Node, rename_link


def _speed_str(res) -> str:
    if not res.ok or res.speed_mbps <= 0:
        return "-"
    return f"{res.speed_mbps:.1f}MB/s"


def select_working(results, settings) -> List[Any]:
    """按阈值筛选出可用节点，并做去重/排序/截断。"""
    max_delay = int(settings.get("max_delay_ms", 0) or 0)
    min_speed = float(settings.get("min_speed_mbps", 0) or 0)
    require_speed = bool(settings.get("require_speed", False))

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

    keep.sort(key=lambda r: (-r.speed_mbps, r.delay_ms))
    limit = int(settings.get("max_nodes", 0) or 0)
    if limit > 0:
        keep = keep[:limit]
    return keep


def render_name(res, index: int, template: str) -> str:
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
        ).strip()
    except (KeyError, IndexError, ValueError):
        return f"{name} | {res.delay_ms}ms | {_speed_str(res)}"


def build_links(keep, settings) -> List[str]:
    template = settings.get("rename_template") or "{name}"
    do_rename = bool(settings.get("rename", True))
    links = []
    for i, r in enumerate(keep, 1):
        link = r.node.link
        if do_rename:
            link = rename_link(link, render_name(r, i, template))
        links.append(link)
    return links


def build_files(keep, all_results, cfg, stats) -> Dict[str, str]:
    """生成待写入/上传的文件内容。key 是逻辑名，value 是文本内容。"""
    settings = cfg["settings"]
    out_cfg = cfg["output"]
    links = build_links(keep, settings)
    plain = "\n".join(links) + ("\n" if links else "")
    b64 = base64.b64encode(plain.encode("utf-8")).decode("ascii")

    files: Dict[str, str] = {
        "base64": b64,
        "plain": plain,
    }

    report = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S%z"),
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
    files["markdown"] = _markdown(report, keep, stats)
    return files


def _markdown(report, keep, stats) -> str:
    lines = [
        "# 订阅筛选报告",
        "",
        f"- 生成时间：`{report['generated_at']}`",
        f"- 抓取节点：**{stats['total']}** 个（来自 {stats['sources']} 个订阅）",
        f"- 测试通过：**{stats['ok']}** 个",
        f"- 最终保留：**{stats['kept']}** 个",
        "",
        "| # | 名称 | 协议 | 服务器 | 延迟 | 速度 |",
        "|---|------|------|--------|------|------|",
    ]
    for i, r in enumerate(keep[:50], 1):
        name = (r.node.name or "").replace("|", "/")[:40]
        lines.append(
            f"| {i} | {name} | {r.node.proto} | `{r.node.server}:{r.node.port}` | {r.delay_ms} ms | {_speed_str(r)} |"
        )
    if len(keep) > 50:
        lines.append(f"\n> 仅展示前 50 个，完整数据见 report.json")
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
