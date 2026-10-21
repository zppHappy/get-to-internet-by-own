"""真连接测试 + 测速。

和 v2rayN 的「真连接延迟」/「下载速度」同一套逻辑：
  起内核 → 本地 socks5 → 通过代理真的发一个 HTTP 请求 → 记延迟
  → 通过代理真的下载一段数据 → 记速度（MB/s）
而不是简单的 TCP 端口探活。
"""
from __future__ import annotations

import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field
from typing import List, Optional

from .core import CoreError, make_core


@dataclass
class TestResult:
    node: object
    ok: bool = False
    delay_ms: int = 0
    speed_mbps: float = 0.0
    bytes_downloaded: int = 0
    # 经节点访问「国内目标站」（默认 baidu.com）的结果。
    # 只代表「节点能到中国」，不等于「中国能到节点」，见 README 说明。
    cn_ok: bool = False
    cn_delay_ms: int = 0
    cn_error: str = ""
    error: str = ""
    attempts: int = 0
    tested_at: float = field(default_factory=time.time)


def _run_curl(args: List[str], timeout: float) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["curl", "-sS", "--no-keepalive", *args],
        capture_output=True,
        text=True,
        timeout=timeout + 5,
    )


def http_via_socks(port: int, url: str, timeout: float) -> tuple:
    """通过本地 socks5 发一个请求，返回 (http_code, seconds, bytes, err)。"""
    args = [
        "-o",
        "/dev/null" if not _is_windows() else "NUL",
        "-x",
        f"socks5h://127.0.0.1:{port}",
        "--connect-timeout",
        str(timeout),
        "-m",
        str(timeout),
        "-w",
        "%{http_code} %{time_total} %{size_download}",
        url,
    ]
    try:
        p = _run_curl(args, timeout)
    except subprocess.TimeoutExpired:
        return 0, 0.0, 0, "curl timeout"
    out = (p.stdout or "").strip().split()
    if p.returncode != 0 or len(out) < 2:
        err = (p.stderr or "").strip().splitlines()
        return 0, 0.0, 0, (err[-1] if err else f"curl exit {p.returncode}")
    try:
        code = int(out[0])
        secs = float(out[1])
        size = int(float(out[2])) if len(out) > 2 else 0
    except ValueError:
        return 0, 0.0, 0, f"bad curl output: {p.stdout!r}"
    return code, secs, size, ""


def _is_windows() -> bool:
    import os

    return os.name == "nt"


def test_node(node, settings, core_dir=None) -> TestResult:
    """单个节点完整测试：起内核 → 延迟（带重试）→ 可选测速。

    内核启动失败（并发下端口被抢占 / 机器瞬时负载高）时换一个端口重来一次，
    避免把「本机起不来内核」误判成「节点不可用」。
    """
    res = TestResult(node=node)

    if getattr(node, "error", ""):
        res.error = node.error
        return res

    # 先用节点默认内核；如果内核拒绝这份配置（旧加密、已移除的传输层），换另一个内核再试
    other = "sing-box" if node.core == "xray" else "xray"
    last_err = ""
    for core in (node.core, other):
        for attempt in range(2):
            try:
                out = _test_once(node, settings, core_dir, core)
                out.attempts = attempt + 1
                return out
            except CoreError as exc:
                # 端口被抢占 / 瞬时负载高：换端口重来
                last_err = f"[{core}] {exc}"
                if "未找到" in str(exc):
                    break
                time.sleep(0.15)

    return TestResult(node=node, error=f"内核启动失败: {last_err}")


def _test_once(node, settings, core_dir, core: str) -> TestResult:
    """跑一次完整测试；内核起不来时抛 CoreError（交给上层换内核/端口重试）。"""
    res = TestResult(node=node)

    try:
        proc = make_core(node, core_dir, startup_timeout=float(settings.get("startup_timeout", 8.0)), core=core)
    except CoreError as exc:
        raise CoreError(str(exc)) from exc

    try:
        try:
            proc.start()
        except CoreError as exc:
            raise CoreError(str(exc)) from exc

        url = settings["delay_test_url"]
        timeout = float(settings.get("delay_timeout", 5))
        retries = int(settings.get("delay_retries", 2))
        accept = settings.get("accept_status") or [200, 204, 301, 302]
        accept_any = bool(settings.get("accept_any_status", True))

        best = None
        for i in range(retries):
            code, secs, size, err = http_via_socks(proc.port, url, timeout)
            if err:
                res.error = err
                continue
            if not (accept_any or code in accept) or code == 0:
                res.error = f"HTTP {code}"
                continue
            ms = max(1, int(round(secs * 1000)))
            if best is None or ms < best:
                best = ms
            # 第一次成功就够了，和 v2rayN 一致（失败才重试）
            break

        if best is None:
            res.ok = False
            return res

        res.delay_ms = best
        res.ok = True

        # 额外：经这个节点访问国内目标站（默认 baidu.com）。
        # 注意方向是「节点 → 中国」，只能说明节点到中国的路径通不通、有多近，
        # 不能证明「中国 → 节点」也通（后者才是你实际使用的方向）。
        cn_url = (settings.get("cn_test_url") or "").strip()
        if cn_url:
            cn_timeout = float(settings.get("cn_test_timeout", 5))
            cn_code, cn_secs, _cn_size, cn_err = http_via_socks(proc.port, cn_url, cn_timeout)
            if cn_err or cn_code == 0:
                res.cn_error = cn_err or f"HTTP {cn_code}"
            elif not (accept_any or cn_code in accept):
                res.cn_error = f"HTTP {cn_code}"
            else:
                res.cn_ok = True
                res.cn_delay_ms = max(1, int(round(cn_secs * 1000)))
            if settings.get("cn_test_required") and not res.cn_ok:
                res.ok = False
                res.error = f"国内目标不可达: {res.cn_error}"
                return res

        if settings.get("speed_test", True):
            sp_url = settings.get("speed_test_url")
            sp_timeout = float(settings.get("speed_timeout", 8))
            max_bytes = int(settings.get("speed_max_bytes", 0))
            args = [
                "-o",
                "/dev/null" if not _is_windows() else "NUL",
                "-x",
                f"socks5h://127.0.0.1:{proc.port}",
                "--connect-timeout",
                str(min(5.0, sp_timeout)),
                "-m",
                str(sp_timeout),
                "-w",
                "%{http_code} %{time_total} %{size_download} %{speed_download}",
            ]
            if max_bytes > 0:
                args += ["-r", f"0-{max_bytes - 1}"]
            args.append(sp_url)
            try:
                p = _run_curl(args, sp_timeout)
                parts = (p.stdout or "").strip().split()
                if len(parts) >= 4:
                    size = int(float(parts[2]))
                    bps = float(parts[3])
                    res.bytes_downloaded = size
                    res.speed_mbps = round(bps / 1024 / 1024, 2)
                    if size < 1024 or bps <= 0:
                        res.error = "speed test: no data"
                else:
                    res.error = (p.stderr or "").strip()[-160:] or "speed test failed"
            except subprocess.TimeoutExpired:
                res.error = "speed test timeout"
            except Exception as exc:  # 测速失败不影响节点可用性
                res.error = f"speed: {exc}"

        return res
    finally:
        proc.stop()


def test_nodes(nodes, settings, core_dir=None, progress=None) -> List[TestResult]:
    concurrency = max(1, int(settings.get("concurrency", 8)))
    results: List[TestResult] = []
    total = len(nodes)
    done = 0

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(test_node, n, settings, core_dir): n for n in nodes}
        for fut in as_completed(futures):
            node = futures[fut]
            try:
                r = fut.result()
            except Exception as exc:
                r = TestResult(node=node, error=f"worker: {exc}")
            results.append(r)
            done += 1
            if progress:
                progress(done, total, r)

    results.sort(key=lambda r: (not r.ok, r.delay_ms if r.ok else 999999, -r.speed_mbps))
    return results
