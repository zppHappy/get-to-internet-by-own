"""代理内核管理：为每个节点临时拉起一个 xray / sing-box 实例，暴露本地 socks5 端口。

和 v2rayN 的做法一致——不是 TCP 探活，而是真的把节点跑起来，再通过它发 HTTP 请求。
"""
from __future__ import annotations

import json
import os
import platform
import shutil
import socket
import stat
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Optional

BIN_DIR = Path(__file__).resolve().parent.parent / "bin"


class CoreError(RuntimeError):
    pass


def _is_windows() -> bool:
    return os.name == "nt"


def find_core(name: str, core_dir: Optional[Path] = None) -> Optional[str]:
    """按 配置目录 → ./bin → PATH 的顺序找内核可执行文件。"""
    exe = f"{name}.exe" if _is_windows() else name
    candidates = []
    if core_dir:
        candidates += [Path(core_dir) / exe, Path(core_dir) / name / exe]
    candidates += [BIN_DIR / exe, BIN_DIR / name / exe]
    for c in candidates:
        if c.is_file():
            try:
                c.chmod(c.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)
            except OSError:
                pass
            return str(c)
    found = shutil.which(name)
    return found


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def _wait_port(port: int, proc: subprocess.Popen, timeout: float) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        if proc.poll() is not None:
            return False
        try:
            with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                return True
        except OSError:
            time.sleep(0.05)
    return False


class CoreProcess:
    """一次性的内核进程，with 语句结束后自动清理。"""

    def __init__(self, binary: str, config: dict, core: str = "xray", startup_timeout: float = 6.0):
        self.binary = binary
        self.config = config
        self.core = core
        self.startup_timeout = startup_timeout
        self.port = 0
        self.proc: Optional[subprocess.Popen] = None
        self.tmpdir: Optional[tempfile.TemporaryDirectory] = None
        self.stderr_tail = ""

    def __enter__(self) -> "CoreProcess":
        self.start()
        return self

    def __exit__(self, *exc) -> None:
        self.stop()

    def start(self) -> None:
        self.tmpdir = tempfile.TemporaryDirectory(prefix="v2sub-")
        cfg_path = Path(self.tmpdir.name) / "config.json"
        cfg_path.write_text(json.dumps(self.config, ensure_ascii=False), encoding="utf-8")
        args = [self.binary, "run", "-c", str(cfg_path)]
        if self.core == "xray":
            args = [self.binary, "run", "-c", str(cfg_path)]
        try:
            self.proc = subprocess.Popen(
                args,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,  # xray 的报错走 stdout，必须一起收
                cwd=self.tmpdir.name,
                env={**os.environ, "XRAY_LOCATION_ASSET": str(Path(self.binary).parent)},
            )
        except OSError as exc:
            raise CoreError(f"无法启动内核 {self.binary}: {exc}") from exc

        if not _wait_port(self.port, self.proc, self.startup_timeout):
            self.stderr_tail = self._read_err()
            self.stop()
            raise CoreError(f"内核未能监听 127.0.0.1:{self.port} {self.stderr_tail}".strip())

    def _read_err(self) -> str:
        if not self.proc:
            return ""
        try:
            out, _ = self.proc.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            return ""
        except Exception:
            return ""
        text = (out or b"").decode("utf-8", "replace").strip()
        # 只留最后一行有用信息
        lines = [l for l in text.splitlines() if l.strip()]
        return (" | ".join(lines[-2:]))[-300:] if lines else ""

    def stop(self) -> None:
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                self.proc.kill()
                try:
                    self.proc.wait(timeout=1)
                except subprocess.TimeoutExpired:
                    pass
        if self.tmpdir:
            try:
                self.tmpdir.cleanup()
            except Exception:
                pass
            self.tmpdir = None


def build_xray_config(outbound: dict, socks_port: int) -> dict:
    return {
        "log": {"loglevel": "none", "error": ""},
        "inbounds": [
            {
                "tag": "socks-in",
                "listen": "127.0.0.1",
                "port": socks_port,
                "protocol": "socks",
                "settings": {"auth": "noauth", "udp": False},
                "sniffing": {"enabled": False},
            }
        ],
        "outbounds": [outbound],
        "routing": {"domainStrategy": "AsIs", "rules": []},
    }


def build_singbox_config(outbound: dict, socks_port: int) -> dict:
    return {
        "log": {"level": "error", "timestamp": True},
        "inbounds": [
            {
                "type": "socks",
                "tag": "socks-in",
                "listen": "127.0.0.1",
                "listen_port": socks_port,
            }
        ],
        "outbounds": [outbound],
        "route": {"final": outbound.get("tag", "proxy")},
    }


def make_core(node, core_dir: Optional[Path] = None, startup_timeout: float = 6.0, core: str = "") -> CoreProcess:
    """根据节点类型创建对应的内核进程（尚未启动）。

    core 可强制指定 xray / sing-box（用于一个内核不支持某节点时换另一个重试）。
    """
    core = core or node.core
    outbound = node.to_outbound(core)
    if outbound is None:
        raise CoreError(f"{core} 不支持该节点（{node.proto}）")

    binary = find_core(core, core_dir)
    if not binary:
        raise CoreError(f"未找到 {core} 内核，请先运行 ./install_core.sh 或配置 core_dir")

    port = free_port()
    if core == "xray":
        cfg = build_xray_config(outbound, port)
    else:
        cfg = build_singbox_config(outbound, port)

    proc = CoreProcess(binary, cfg, core=core, startup_timeout=startup_timeout)
    proc.port = port
    return proc
