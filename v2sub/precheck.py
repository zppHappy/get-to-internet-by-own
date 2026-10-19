"""TCP 预筛：先把端口都连不上的节点剔掉，再进入昂贵的真连接测试。

真连接测试要为每个节点冷启动一个内核（0.3~1.5s）再发一次 HTTP 请求。
上万个节点里绝大多数其实端口根本连不上，先花 1~2 秒做一次 TCP 探活，
能省掉大部分时间，而且不会误杀：TCP 都连不上，代理一定不可用。

注意：
1. 只对 TCP 系协议做（vmess / vless / trojan / ss）。
   hysteria2、tuic 走 UDP，端口不通不代表节点挂了，直接跳过预筛。
2. 同一个 server:port 只探一次，结果套用到该端点上的所有节点。
3. 预筛只是「剔除确定死的」，活下来的仍然要过真连接测试。
"""
from __future__ import annotations

import socket
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import List, Tuple

from .tester import TestResult

UDP_PROTOS = {"hysteria2", "tuic"}


def _tcp_probe(host: str, port: int, timeout: float) -> Tuple[bool, str]:
    if not host or not port:
        return False, "tcp: 地址或端口为空"
    try:
        with socket.create_connection((host, int(port)), timeout=timeout):
            return True, ""
    except socket.timeout:
        return False, f"tcp: 连接超时 {timeout}s"
    except OSError as exc:
        return False, f"tcp: {exc.__class__.__name__}"


def precheck(nodes: List, timeout: float = 2.0, concurrency: int = 200, log=None):
    """返回 (存活节点, 预筛失败的 TestResult 列表, 实际探测的端点数)。"""
    endpoints = {}
    for n in nodes:
        if n.proto in UDP_PROTOS:
            continue
        endpoints.setdefault((n.server.lower(), n.port), None)

    if not endpoints:
        return list(nodes), [], 0

    results = {}
    total = len(endpoints)
    with ThreadPoolExecutor(max_workers=max(1, min(concurrency, total))) as pool:
        futures = {
            pool.submit(_tcp_probe, host, port, timeout): (host, port)
            for (host, port) in endpoints
        }
        done = 0
        for fut in as_completed(futures):
            ep = futures[fut]
            try:
                results[ep] = fut.result()
            except Exception as exc:  # 单个探测异常不影响整体
                results[ep] = (False, f"tcp: {exc.__class__.__name__}")
            done += 1
            if log and total >= 1000 and done % 1000 == 0:
                log(f"    预筛 {done}/{total} 个端点")

    alive, dead = [], []
    for n in nodes:
        if n.proto in UDP_PROTOS:
            alive.append(n)
            continue
        ok, err = results.get((n.server.lower(), n.port), (False, "tcp: 未探测"))
        if ok:
            alive.append(n)
        else:
            dead.append(TestResult(node=n, ok=False, error=err))
    return alive, dead, total
