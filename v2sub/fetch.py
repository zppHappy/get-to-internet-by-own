"""订阅抓取：支持 http(s) 链接、本地文件、base64 订阅、明文链接列表。"""
from __future__ import annotations

import base64
import binascii
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path
from typing import List, Tuple

UA = "v2rayN/6.42 (v2sub-filter)"
SCHEMES = ("vmess://", "vless://", "trojan://", "ss://", "ssr://", "hysteria2://", "hy2://", "tuic://")


class FetchError(RuntimeError):
    pass


def _http_get(url: str, timeout: float = 20.0) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": UA,
            "Accept": "*/*",
            "Accept-Encoding": "identity",
        },
    )
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
            raw = resp.read()
    except urllib.error.HTTPError as exc:
        raise FetchError(f"HTTP {exc.code}") from exc
    except Exception as exc:
        raise FetchError(str(exc)) from exc
    return raw.decode("utf-8", "replace")


def _maybe_b64(text: str) -> str:
    """订阅内容如果整体是 base64，就解开。"""
    stripped = re.sub(r"\s+", "", text)
    if not stripped:
        return ""
    # 已经是明文链接列表
    lowered = stripped.lower()
    if any(s in lowered for s in ("vmess://", "vless://", "trojan://", "ss://", "hysteria2://", "tuic://")):
        return text
    if stripped.startswith("proxies:") or "proxy-groups:" in stripped:
        return text  # clash yaml，交给上层判断
    try:
        stripped = stripped.replace("-", "+").replace("_", "/")
        stripped += "=" * (-len(stripped) % 4)
        decoded = base64.b64decode(stripped, validate=True).decode("utf-8", "replace")
        return decoded
    except (binascii.Error, UnicodeDecodeError, ValueError):
        return text


def split_links(text: str) -> List[str]:
    text = _maybe_b64(text)
    links: List[str] = []
    for line in text.replace("\r", "\n").split("\n"):
        line = line.strip()
        if not line:
            continue
        low = line.lower()
        if any(low.startswith(s) for s in SCHEMES):
            links.append(line)
    return links


def fetch_source(src: str, timeout: float = 20.0) -> Tuple[str, List[str], str]:
    """返回 (来源标签, 链接列表, 错误信息)。"""
    src = src.strip()
    if not src:
        return "", [], "空来源"

    if src.startswith(("http://", "https://")):
        label = src.split("?")[0][-48:]
        try:
            text = _http_get(src, timeout)
        except FetchError as exc:
            return label, [], f"{exc}"
        if "proxy-groups:" in text or text.lstrip().startswith("proxies:"):
            return label, [], "clash yaml 订阅暂不支持，请换成 base64/明文订阅"
        links = split_links(text)
        return label, links, "" if links else "未解析到节点（订阅可能是空的或格式不支持）"

    path = Path(src[5:]) if src.startswith("file:") else Path(src)
    label = path.name
    if not path.is_file():
        return label, [], "文件不存在"
    text = path.read_text(encoding="utf-8", errors="replace")
    links = split_links(text)
    return label, links, "" if links else "文件中没有可用节点"


def fetch_all(sources: List[str], timeout: float = 20.0, log=None) -> Tuple[List[Tuple[str, str]], List[Tuple[str, str]]]:
    """抓取全部订阅。返回 ([(link, source)], [(source, error)])"""
    all_links: List[Tuple[str, str]] = []
    errors: List[Tuple[str, str]] = []
    for src in sources:
        label, links, err = fetch_source(src, timeout)
        if err:
            errors.append((label or src[:40], err))
            if log:
                log(f"  ✗ {label or src[:40]}: {err}")
        else:
            if log:
                log(f"  ✓ {label}: {len(links)} 个节点")
        for ln in links:
            all_links.append((ln, label))
    return all_links, errors
