#!/usr/bin/env python3
"""v2sub —— 订阅自动筛选工具

流程：抓取多个订阅 → 解析节点 → 逐个起内核做真连接测试 + 测速 → 只保留可用节点
      → 生成新的 base64 订阅 → 上传到 GitHub（仓库文件 / Gist）。

用法：
    python3 filter.py -c config.yaml
    python3 filter.py -c config.yaml --no-speed --no-upload
    python3 filter.py -c config.yaml --sub https://xxx/sub
"""
from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from v2sub.config import load_config  # noqa: E402
from v2sub.core import find_core  # noqa: E402
from v2sub.emit import build_files, select_working, write_files  # noqa: E402
from v2sub.fetch import fetch_all  # noqa: E402
from v2sub.parse import parse_link  # noqa: E402
from v2sub.precheck import precheck  # noqa: E402
from v2sub.tester import test_nodes  # noqa: E402
from v2sub.upload import UploadError, upload  # noqa: E402

BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"

MARKS = "①②③④⑤⑥⑦⑧⑨"


def _color(s: str, c: str) -> str:
    if not sys.stdout.isatty() and os.environ.get("FORCE_COLOR") != "1":
        return s
    return f"{c}{s}{RESET}"


def log(msg: str = "") -> None:
    print(msg, flush=True)


def step(title: str) -> None:
    """带序号的阶段标题，序号随实际执行的步骤自动递增。"""
    step.n += 1
    mark = MARKS[step.n - 1] if step.n <= len(MARKS) else f"({step.n})"
    log(_color(f"{mark} {title}", BOLD))


step.n = 0


def main() -> int:
    ap = argparse.ArgumentParser(description="V2RayN 订阅自动筛选（真连接测试 + 测速）")
    ap.add_argument("-c", "--config", default="config.yaml", help="配置文件路径")
    ap.add_argument("--sub", action="append", default=[], help="临时追加订阅地址（可多次）")
    ap.add_argument("--no-speed", action="store_true", help="只测延迟，不测速")
    ap.add_argument("--no-precheck", action="store_true", help="关闭 TCP 预筛（所有节点都做真连接测试）")
    ap.add_argument("--no-upload", action="store_true", help="只生成文件，不上传 GitHub")
    ap.add_argument("--dry-run", action="store_true", help="抓取+解析后只打印统计，不测试")
    ap.add_argument("--limit", type=int, default=0, help="最多保留多少个节点（覆盖配置）")
    ap.add_argument("--concurrency", type=int, default=0, help="并发数（覆盖配置）")
    ap.add_argument("--proto", default="", help="只测这些协议，逗号分隔，如 vmess,vless")
    ap.add_argument("--max-delay", type=int, default=0, help="延迟上限 ms（覆盖配置）")
    ap.add_argument("-q", "--quiet", action="store_true", help="只输出汇总")
    args = ap.parse_args()

    cfg = load_config(args.config)
    st = cfg["settings"]
    if args.no_speed:
        st["speed_test"] = False
    if args.no_precheck:
        st["tcp_precheck"] = False
    if args.limit:
        st["max_nodes"] = args.limit
    if args.concurrency:
        st["concurrency"] = args.concurrency
    if args.max_delay:
        st["max_delay_ms"] = args.max_delay
    if args.proto:
        st["protocols"] = [p.strip() for p in args.proto.split(",") if p.strip()]

    sources = list(cfg.get("sources") or [])
    # 隐私隔离：订阅地址可以放在 config 同目录的 sources.txt（每行一个，# 开头为注释）
    src_file = Path(cfg.get("_config_dir", ".")) / "sources.txt"
    if src_file.is_file():
        for line in src_file.read_text(encoding="utf-8", errors="replace").splitlines():
            line = line.strip()
            if line and not line.startswith("#"):
                sources.append(line)
    env_subs = os.environ.get("V2SUB_SOURCES", "")
    if env_subs.strip():
        for chunk in env_subs.replace(",", "\n").split("\n"):
            chunk = chunk.strip()
            if chunk:
                sources.append(chunk)
    sources += list(args.sub or [])

    # 去重且保序
    seen_src, uniq = set(), []
    for s in sources:
        if s not in seen_src:
            seen_src.add(s)
            uniq.append(s)
    sources = uniq

    if not sources:
        log(_color("✗ 没有配置订阅源：写进 sources.txt、或用 V2SUB_SOURCES 环境变量、或 --sub 指定", RED))
        return 2

    step("抓取订阅")
    t0 = time.time()
    raw_links, fetch_errors = fetch_all(sources, timeout=float(st.get("fetch_timeout", 20)), log=None if args.quiet else log)
    if not raw_links:
        log(_color("✗ 所有订阅都没取到节点", RED))
        for s, e in fetch_errors:
            log(f"  - {s}: {e}")
        return 2

    step(f"解析节点（共 {len(raw_links)} 条链接）")
    nodes, seen, skipped = [], set(), {"parse": 0, "proto": 0, "dup": 0}
    for link, src in raw_links:
        node = parse_link(link, src)
        if node is None:
            skipped["parse"] += 1
            continue
        if node.proto not in st["protocols"]:
            skipped["proto"] += 1
            continue
        if st.get("dedupe", True):
            if node.key in seen:
                skipped["dup"] += 1
                continue
            seen.add(node.key)
        nodes.append(node)

    by_proto = {}
    for n in nodes:
        by_proto[n.proto] = by_proto.get(n.proto, 0) + 1
    log(f"  可测节点 {len(nodes)} 个 " + _color("(" + ", ".join(f"{k}:{v}" for k, v in sorted(by_proto.items())) + ")", DIM))
    parsed_nodes = len(nodes)
    if any(skipped.values()):
        log(_color(f"  跳过：重复 {skipped['dup']}、协议未启用 {skipped['proto']}、无法解析 {skipped['parse']}", DIM))

    if not nodes:
        log(_color("✗ 没有可测试的节点", RED))
        return 2
    if args.dry_run:
        log(_color("--dry-run：跳过测试", YELLOW))
        return 0

    # TCP 预筛：先把端口都连不上的节点剔掉，省掉为它们冷启动内核的开销。
    # 只剔除「确定死的」，活下来的仍然要过真连接测试。
    pre_dead = []
    if st.get("tcp_precheck", True) and len(nodes) > 50:
        step("TCP 预筛（只剔除端口不通的）")
        t_pre = time.time()
        alive, pre_dead, n_ep = precheck(
            nodes,
            timeout=float(st.get("precheck_timeout", 2)),
            concurrency=int(st.get("precheck_concurrency", 200)),
            log=None if args.quiet else log,
        )
        log(
            f"  {n_ep} 个端点 → 可连 {len(alive)} / {len(nodes)} 个节点"
            + _color(f"，剔除 {len(pre_dead)}（{time.time() - t_pre:.1f}s）", DIM)
        )
        nodes = alive
        if not nodes:
            log(_color("✗ 所有节点端口都不通：检查本机网络，或订阅里的地址已全部失效", RED))
            return 1

    core_dir = st.get("core_dir") or None
    need = {n.core for n in nodes}
    missing = [c for c in sorted(need) if not find_core(c, core_dir)]
    if missing:
        log(_color(f"✗ 缺少内核：{', '.join(missing)}", RED))
        log("  先执行：./install_core.sh   （或把内核放到 ./bin 下）")
        return 2

    step(f"真连接测试{' + 测速' if st.get('speed_test') else ''}（并发 {st['concurrency']}）")
    log(_color(f"  延迟测试 URL: {st['delay_test_url']}", DIM))
    if st.get("speed_test"):
        log(_color(f"  测速 URL: {st['speed_test_url']}", DIM))

    started = time.time()

    def progress(done: int, total: int, r) -> None:
        if args.quiet:
            return
        name = (r.node.name or f"{r.node.server}:{r.node.port}")[:34]
        head = f"[{done:>3}/{total}]"
        if r.ok:
            sp = f"{r.speed_mbps:.1f}MB/s" if r.speed_mbps else "-"
            log(f"  {head} {_color('✓', GREEN)} {name:<34} {r.delay_ms:>5}ms  {sp:>9}")
        elif total > 500 and done % 25:
            return  # 节点多时失败项抽样打印，避免刷屏
        else:
            log(f"  {head} {_color('✗', RED)} {name:<34} {_color((r.error or '')[:46], DIM)}")

    results = test_nodes(nodes, st, core_dir=core_dir, progress=progress)
    results.extend(pre_dead)
    ok_count = sum(1 for r in results if r.ok)

    step("筛选结果")
    keep = select_working(results, st)
    stats = {
        "total": len(raw_links),
        "parsed": parsed_nodes,
        "precheck_dropped": len(pre_dead),
        "tested": len(results),
        "ok": ok_count,
        "kept": len(keep),
        "sources": len(sources),
        "elapsed_sec": round(time.time() - started, 1),
        "skipped": skipped,
    }
    log(f"  测试通过 {_color(str(ok_count), GREEN)} / {len(results)}，最终保留 {_color(str(len(keep)), BOLD)}")
    log(_color(f"  耗时 {stats['elapsed_sec']}s", DIM))

    if not keep:
        log(_color("✗ 没有节点通过筛选，检查一下 max_delay_ms / min_speed_mbps 或换测试 URL", YELLOW))
        return 1

    files = build_files(keep, results, cfg, stats)
    written = write_files(files, cfg)
    step("生成订阅文件")
    for p in written:
        size = p.stat().st_size
        log(f"  ✓ {p}  ({size} B)")

    if cfg.get("github", {}).get("enabled") and not args.no_upload:
        step("上传到 GitHub")
        try:
            info = upload(cfg, files, log=log)
        except UploadError as exc:
            log(_color(f"  ✗ 上传失败：{exc}", RED))
            log(_color("  （只想要本地文件可以加 --no-upload）", DIM))
            return 1
        if info.get("sub_url"):
            log("")
            log(_color("  新订阅地址（直接粘进 V2RayN）：", BOLD))
            log(f"  {info['sub_url']}")
            mirror = info["sub_url"].replace("https://raw.githubusercontent.com/", "https://cdn.jsdelivr.net/gh/")
            if mirror != info["sub_url"]:
                log(_color(f"  国内镜像：{mirror}", DIM))
    elif not cfg.get("github", {}).get("enabled"):
        log(_color("  （未启用 GitHub 上传，如需自动发布请配置 config.yaml 的 github 段）", DIM))

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n已中断")
        sys.exit(130)
