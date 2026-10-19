#!/usr/bin/env python3
"""下载代理内核（xray / sing-box）到 ./bin，跨平台：Windows / macOS / Linux。

和 install_core.sh 的区别：这个脚本在 Windows 上也能用（bash 脚本只支持 macOS/Linux）。

用法：
    python install_core.py              # 两个都装
    python install_core.py xray         # 只装 xray
    python install_core.py sing-box     # 只装 sing-box
    python install_core.py all --dest D:\\mybin
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import stat
import sys
import tarfile
import tempfile
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
UA = {"User-Agent": "v2sub-installer"}


def _get(url: str, timeout: float = 60) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _latest_tag(repo: str) -> str:
    data = json.loads(_get(f"https://api.github.com/repos/{repo}/releases/latest").decode())
    tag = data.get("tag_name", "")
    if not tag:
        raise RuntimeError(f"拿不到 {repo} 的最新版本号")
    return tag


def _os_arch() -> tuple[str, str]:
    """返回 (os, arch)，arch 统一成 amd64 / arm64。"""
    if sys.platform.startswith("win"):
        osname = "windows"
    elif sys.platform == "darwin":
        osname = "darwin"
    else:
        osname = "linux"
    m = platform.machine().lower()
    if m in ("x86_64", "amd64", "x64"):
        arch = "amd64"
    elif m in ("aarch64", "arm64"):
        arch = "arm64"
    else:
        raise RuntimeError(f"不支持的架构: {platform.machine()}")
    return osname, arch


def _download(url: str, dest: Path) -> None:
    print(f"  ↓ {url.rsplit('/', 1)[-1]}")
    data = _get(url, timeout=300)
    dest.write_bytes(data)
    print(f"    {len(data) / 1024 / 1024:.1f} MB")


def install_xray(dest: Path) -> None:
    osname, arch = _os_arch()
    # xray 的命名习惯：windows/linux/macos + 64 / arm64-v8a
    xray_arch = "64" if arch == "amd64" else "arm64-v8a"
    asset = f"Xray-{osname}-{xray_arch}.zip"
    tag = _latest_tag("XTLS/Xray-core")
    print(f"==> Xray {tag} ({asset})")
    with tempfile.TemporaryDirectory() as tmp:
        zp = Path(tmp) / "x.zip"
        _download(f"https://github.com/XTLS/Xray-core/releases/download/{tag}/{asset}", zp)
        with zipfile.ZipFile(zp) as z:
            z.extractall(tmp)
        src = next(p for p in Path(tmp).rglob("*") if p.name in ("xray.exe", "xray") and p.is_file())
        out = dest / ("xray.exe" if osname == "windows" else "xray")
        shutil.copy2(src, out)
        out.chmod(out.stat().st_mode | stat.S_IEXEC)
    print(f"    ✓ {out}")


def install_singbox(dest: Path) -> None:
    osname, arch = _os_arch()
    tag = _latest_tag("SagerNet/sing-box")
    ver = tag.lstrip("v")
    ext = "zip" if osname == "windows" else "tar.gz"
    asset = f"sing-box-{ver}-{osname}-{arch}.{ext}"
    print(f"==> sing-box {tag} ({asset})")
    with tempfile.TemporaryDirectory() as tmp:
        fp = Path(tmp) / f"sb.{ext}"
        _download(f"https://github.com/SagerNet/sing-box/releases/download/{tag}/{asset}", fp)
        if ext == "zip":
            with zipfile.ZipFile(fp) as z:
                z.extractall(tmp)
        else:
            with tarfile.open(fp) as t:
                t.extractall(tmp)
        src = next(p for p in Path(tmp).rglob("*") if p.name in ("sing-box.exe", "sing-box") and p.is_file())
        out = dest / ("sing-box.exe" if osname == "windows" else "sing-box")
        shutil.copy2(src, out)
        out.chmod(out.stat().st_mode | stat.S_IEXEC)
    print(f"    ✓ {out}")


def main() -> int:
    ap = argparse.ArgumentParser(description="下载 xray / sing-box 内核到 ./bin")
    ap.add_argument("what", nargs="?", default="all", choices=["all", "xray", "sing-box", "singbox"])
    ap.add_argument("--dest", default=str(HERE / "bin"), help="安装目录，默认 ./bin")
    args = ap.parse_args()

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    print(f"系统: {sys.platform} / {platform.machine()} → {dest}")

    try:
        if args.what in ("all", "xray"):
            install_xray(dest)
        if args.what in ("all", "sing-box", "singbox"):
            install_singbox(dest)
    except urllib.error.HTTPError as exc:
        print(f"✗ 下载失败 HTTP {exc.code}：{exc.url}")
        print("  GitHub Releases 在国内经常连不上，挂个代理或换个网络再试")
        return 1
    except Exception as exc:
        print(f"✗ {exc}")
        return 1

    print(f"\n完成，内核位于 {dest}")
    print("现在可以运行： python filter.py -c config.yaml")
    return 0


if __name__ == "__main__":
    sys.exit(main())
