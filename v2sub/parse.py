"""订阅链接解析：把 vmess/vless/trojan/ss/hysteria2/tuic 链接转成内核可用的 outbound。

设计原则：
1. 保留原始链接字符串（输出的订阅里仍然写原始链接，保证客户端兼容）；
2. 解析出的字段只用于「起内核 + 真连接测试」；
3. 解析不了的节点不丢弃，标记 unsupported，最后单独统计。
"""
from __future__ import annotations

import base64
import binascii
import json
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from urllib.parse import unquote

SUPPORTED_PROTOCOLS = ("vmess", "vless", "trojan", "ss", "hysteria2", "tuic")

# 这些协议 xray 能跑；hysteria2 / tuic 需要 sing-box
XRAY_PROTOS = {"vmess", "vless", "trojan", "ss"}
SINGBOX_PROTOS = {"hysteria2", "tuic"}

# xray v25+ 移除了非 AEAD 的 shadowsocks 加密，这类节点要交给 sing-box
AEAD_METHODS = {
    "aes-128-gcm",
    "aes-192-gcm",
    "aes-256-gcm",
    "chacha20-poly1305",
    "chacha20-ietf-poly1305",
    "xchacha20-poly1305",
    "xchacha20-ietf-poly1305",
}
# xray v25+ 移除了 h2（net=http）传输，这类节点也要交给 sing-box
SINGBOX_ONLY_NETS = {"http", "h2"}


def _needs_singbox(proto: str, params: Dict[str, Any]) -> bool:
    if proto in SINGBOX_PROTOS:
        return True
    if proto == "ss":
        m = (params.get("method") or "").lower()
        return not (m in AEAD_METHODS or m.startswith("2022-"))
    if (params.get("net") or "").lower() in SINGBOX_ONLY_NETS:
        return True
    return False


def b64decode_any(s: str) -> bytes:
    """宽松 base64 解码：兼容 url-safe、缺 padding、含换行。"""
    s = re.sub(r"\s+", "", s)
    s = s.replace("-", "+").replace("_", "/")
    s += "=" * (-len(s) % 4)
    return base64.b64decode(s, validate=False)


def b64encode_str(s: str) -> str:
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


def _split_host_port(hp: str):
    """处理 host:port，兼容 [IPv6]:port。"""
    hp = hp.strip()
    if hp.startswith("["):
        end = hp.find("]")
        host = hp[1:end]
        rest = hp[end + 1 :]
        port = rest.lstrip(":")
        return host, int(port) if port else 0
    if ":" in hp:
        host, port = hp.rsplit(":", 1)
        try:
            return host, int(port)
        except ValueError:
            return host, 0
    return hp, 0


def _query(q: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    if not q:
        return out
    for part in q.split("&"):
        if not part:
            continue
        if "=" in part:
            k, v = part.split("=", 1)
        else:
            k, v = part, ""
        out[unquote(k).lower()] = unquote(v)
    return out


@dataclass
class Node:
    link: str
    proto: str
    name: str
    server: str
    port: int
    params: Dict[str, Any] = field(default_factory=dict)
    source: str = ""
    core: str = "xray"
    error: str = ""

    @property
    def key(self) -> tuple:
        """去重键：同协议同服务器同端口同凭据同传输层视为同一节点。"""
        p = self.params
        cred = p.get("id") or p.get("password") or p.get("uuid") or ""
        return (
            self.proto,
            self.server.lower(),
            self.port,
            cred,
            p.get("net", ""),
            p.get("path", ""),
            p.get("host", ""),
            p.get("sni", ""),
        )

    def to_outbound(self, target: str = "") -> Optional[Dict[str, Any]]:
        """生成 outbound。target 可强制指定内核：xray / sing-box。"""
        target = target or self.core
        if target == "sing-box":
            return to_singbox_outbound(self)
        fn = {
            "vmess": _out_vmess,
            "vless": _out_vless,
            "trojan": _out_trojan,
            "ss": _out_ss,
            "hysteria2": _out_hy2,
            "tuic": _out_tuic,
        }.get(self.proto)
        if not fn:
            return None
        return fn(self)


# ---------------------------------------------------------------- stream 设置
def _xray_stream(p: Dict[str, Any]) -> Dict[str, Any]:
    net = (p.get("net") or "tcp").lower()
    if net not in {"tcp", "raw", "ws", "grpc", "h2", "http", "xhttp", "splithttp", "httpupgrade", "kcp", "quic"}:
        net = "tcp"  # none / udp / 空值等异常写法，按 tcp 处理
    security = (p.get("security") or "none").lower()
    stream: Dict[str, Any] = {"network": net}

    if net == "tcp" and (p.get("header_type") or "").lower() == "http":
        stream["network"] = "tcp"
        stream["tcpSettings"] = {
            "header": {
                "type": "http",
                "request": {
                    "path": [p.get("path") or "/"],
                    "headers": {"Host": [p.get("host") or p.get("sni") or ""]},
                },
            }
        }

    if net == "ws":
        stream["wsSettings"] = {"path": p.get("path") or "/"}
        host = p.get("host")
        if host:
            stream["wsSettings"]["headers"] = {"Host": host}
    elif net == "grpc":
        stream["grpcSettings"] = {"serviceName": p.get("service_name") or p.get("path") or ""}
        if p.get("multi_mode"):
            stream["grpcSettings"]["multiMode"] = True
    elif net in ("h2", "http"):
        stream["network"] = "h2"
        hs: Dict[str, Any] = {"path": p.get("path") or "/"}
        if p.get("host"):
            hs["host"] = [h.strip() for h in str(p["host"]).split(",") if h.strip()]
        stream["httpSettings"] = hs
    elif net in ("xhttp", "splithttp"):
        stream["network"] = "xhttp"
        xs: Dict[str, Any] = {"path": p.get("path") or "/"}
        if p.get("host"):
            xs["host"] = p["host"]
        if p.get("mode"):
            xs["mode"] = p["mode"]
        stream["xhttpSettings"] = xs
    elif net in ("httpupgrade",):
        stream["network"] = "httpupgrade"
        hu: Dict[str, Any] = {"path": p.get("path") or "/"}
        if p.get("host"):
            hu["host"] = p["host"]
        stream["httpupgradeSettings"] = hu
    elif net == "kcp":
        ks: Dict[str, Any] = {"header": {"type": p.get("header_type") or "none"}}
        if p.get("seed"):
            ks["seed"] = p["seed"]
        stream["kcpSettings"] = ks
    elif net == "quic":
        qs: Dict[str, Any] = {"security": p.get("quic_security") or "none", "key": p.get("quic_key") or ""}
        if p.get("quic_header"):
            qs["header"] = {"type": p["quic_header"]}
        stream["quicSettings"] = qs

    # TLS / REALITY
    if security in ("tls", "xtls"):
        tls: Dict[str, Any] = {}
        sni = p.get("sni") or p.get("host") or ""
        if sni:
            tls["serverName"] = sni
        if p.get("alpn"):
            tls["alpn"] = [a.strip() for a in str(p["alpn"]).split(",") if a.strip()]
        if p.get("fp"):
            tls["fingerprint"] = p["fp"]
        if str(p.get("allow_insecure", "")).lower() in ("1", "true"):
            tls["allowInsecure"] = True
        stream["security"] = "tls"
        stream["tlsSettings"] = tls
    elif security == "reality":
        rl: Dict[str, Any] = {}
        if p.get("sni"):
            rl["serverName"] = p["sni"]
        if p.get("pbk"):
            rl["publicKey"] = p["pbk"]
        if p.get("sid"):
            rl["shortId"] = p["sid"]
        if p.get("fp"):
            rl["fingerprint"] = p["fp"]
        if p.get("spx"):
            rl["spiderX"] = p["spx"]
        stream["security"] = "reality"
        stream["realitySettings"] = rl
    else:
        stream["security"] = "none"

    return stream


def _out_vmess(n: Node) -> Dict[str, Any]:
    p = n.params
    return {
        "tag": "proxy",
        "protocol": "vmess",
        "settings": {
            "vnext": [
                {
                    "address": n.server,
                    "port": n.port,
                    "users": [
                        {
                            "id": p.get("id", ""),
                            "alterId": int(p.get("aid") or 0),
                            "security": p.get("scy") or "auto",
                        }
                    ],
                }
            ]
        },
        "streamSettings": _xray_stream(p),
    }


def _out_vless(n: Node) -> Dict[str, Any]:
    p = n.params
    user: Dict[str, Any] = {"id": p.get("id", ""), "encryption": p.get("encryption") or "none"}
    if p.get("flow"):
        user["flow"] = p["flow"]
    return {
        "tag": "proxy",
        "protocol": "vless",
        "settings": {"vnext": [{"address": n.server, "port": n.port, "users": [user]}]},
        "streamSettings": _xray_stream(p),
    }


def _out_trojan(n: Node) -> Dict[str, Any]:
    p = n.params
    return {
        "tag": "proxy",
        "protocol": "trojan",
        "settings": {"servers": [{"address": n.server, "port": n.port, "password": p.get("password", "")}]},
        "streamSettings": _xray_stream(p),
    }


def _out_ss(n: Node) -> Dict[str, Any]:
    p = n.params
    return {
        "tag": "proxy",
        "protocol": "shadowsocks",
        "settings": {
            "servers": [
                {
                    "address": n.server,
                    "port": n.port,
                    "method": p.get("method", ""),
                    "password": p.get("password", ""),
                    "uot": False,
                }
            ]
        },
        "streamSettings": {"network": "tcp", "security": "none"},
    }


def _singbox_tls(p: Dict[str, Any], default_sni: str = "") -> Dict[str, Any]:
    tls: Dict[str, Any] = {"enabled": True}
    sni = p.get("sni") or p.get("host") or default_sni
    if sni:
        tls["server_name"] = sni
    if str(p.get("allow_insecure", "")).lower() in ("1", "true"):
        tls["insecure"] = True
    if p.get("alpn"):
        tls["alpn"] = [a.strip() for a in str(p["alpn"]).split(",") if a.strip()]
    return tls


def _out_hy2(n: Node) -> Dict[str, Any]:
    p = n.params
    ob: Dict[str, Any] = {
        "type": "hysteria2",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "password": p.get("password", ""),
        "tls": _singbox_tls(p, n.server),
    }
    if p.get("obfs"):
        ob["obfs"] = {"type": p["obfs"], "password": p.get("obfs_password", "")}
    if p.get("upmbps"):
        ob["up_mbps"] = int(float(p["upmbps"]))
    if p.get("downmbps"):
        ob["down_mbps"] = int(float(p["downmbps"]))
    return ob


def _out_tuic(n: Node) -> Dict[str, Any]:
    p = n.params
    ob: Dict[str, Any] = {
        "type": "tuic",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "uuid": p.get("uuid") or p.get("id") or "",
        "password": p.get("password", ""),
        "tls": _singbox_tls(p, n.server),
        "congestion_control": p.get("congestion_control") or "bbr",
        "udp_relay_mode": p.get("udp_relay_mode") or "native",
    }
    return ob


# --------------------------------------------------- sing-box 通用协议转换
def _sb_tls(p: Dict[str, Any], default_sni: str = "") -> Dict[str, Any]:
    """sing-box 的 TLS 段，含 reality / utls。"""
    security = (p.get("security") or "none").lower()
    tls: Dict[str, Any] = {"enabled": True}
    sni = p.get("sni") or p.get("host") or default_sni
    if sni:
        tls["server_name"] = sni
    if str(p.get("allow_insecure", "")).lower() in ("1", "true"):
        tls["insecure"] = True
    if p.get("alpn"):
        tls["alpn"] = [a.strip() for a in str(p["alpn"]).split(",") if a.strip()]
    if p.get("fp"):
        tls["utls"] = {"enabled": True, "fingerprint": p["fp"]}
    if security == "reality":
        reality: Dict[str, Any] = {"enabled": True}
        if p.get("pbk"):
            reality["public_key"] = p["pbk"]
        if p.get("sid"):
            reality["short_id"] = p["sid"]
        tls["reality"] = reality
        tls.setdefault("utls", {"enabled": True, "fingerprint": p.get("fp") or "chrome"})
    return tls


def _sb_transport(p: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    net = (p.get("net") or "tcp").lower()
    if net in ("tcp", "raw", "none", "", "udp"):
        return None
    if net == "ws":
        t: Dict[str, Any] = {"type": "ws", "path": p.get("path") or "/"}
        if p.get("host"):
            t["headers"] = {"Host": p["host"]}
        return t
    if net == "grpc":
        return {"type": "grpc", "service_name": p.get("service_name") or p.get("path") or ""}
    if net in ("http", "h2"):
        t = {"type": "http", "path": p.get("path") or "/"}
        hosts = [h.strip() for h in str(p.get("host") or "").split(",") if h.strip()]
        if hosts:
            t["host"] = hosts
        return t
    if net == "httpupgrade":
        t = {"type": "httpupgrade", "path": p.get("path") or "/"}
        if p.get("host"):
            t["host"] = p["host"]
        return t
    if net == "quic":
        return {"type": "quic"}
    # xhttp / kcp 等 sing-box 不支持
    raise ValueError(f"sing-box 不支持传输层: {net}")


def _sb_out_vmess(n: Node) -> Dict[str, Any]:
    p = n.params
    ob: Dict[str, Any] = {
        "type": "vmess",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "uuid": p.get("id", ""),
        "security": p.get("scy") or "auto",
        "alter_id": int(p.get("aid") or 0),
    }
    if (p.get("security") or "none").lower() in ("tls", "reality"):
        ob["tls"] = _sb_tls(p, n.server)
    t = _sb_transport(p)
    if t:
        ob["transport"] = t
    return ob


def _sb_out_vless(n: Node) -> Dict[str, Any]:
    p = n.params
    ob: Dict[str, Any] = {
        "type": "vless",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "uuid": p.get("id", ""),
    }
    if p.get("flow"):
        ob["flow"] = p["flow"]
    if (p.get("security") or "none").lower() in ("tls", "reality"):
        ob["tls"] = _sb_tls(p, n.server)
    t = _sb_transport(p)
    if t:
        ob["transport"] = t
    return ob


def _sb_out_trojan(n: Node) -> Dict[str, Any]:
    p = n.params
    ob: Dict[str, Any] = {
        "type": "trojan",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "password": p.get("password", ""),
    }
    if (p.get("security") or "tls").lower() in ("tls", "reality", "none"):
        ob["tls"] = _sb_tls(p, n.server)
    t = _sb_transport(p)
    if t:
        ob["transport"] = t
    return ob


def _sb_out_ss(n: Node) -> Dict[str, Any]:
    p = n.params
    return {
        "type": "shadowsocks",
        "tag": "proxy",
        "server": n.server,
        "server_port": n.port,
        "method": p.get("method", ""),
        "password": p.get("password", ""),
    }


def to_singbox_outbound(node: Node) -> Optional[Dict[str, Any]]:
    fn = {
        "vmess": _sb_out_vmess,
        "vless": _sb_out_vless,
        "trojan": _sb_out_trojan,
        "ss": _sb_out_ss,
        "hysteria2": _out_hy2,
        "tuic": _out_tuic,
    }.get(node.proto)
    if not fn:
        return None
    try:
        return fn(node)
    except ValueError:
        return None


# ------------------------------------------------------------------- 解析入口
def parse_link(link: str, source: str = "") -> Optional[Node]:
    link = link.strip()
    if not link or link.startswith("#") or link.startswith("//"):
        return None
    if "://" not in link:
        return None

    scheme = link.split("://", 1)[0].lower()
    node: Optional[Node]
    try:
        if scheme == "vmess":
            node = _parse_vmess(link, source)
        elif scheme == "vless":
            node = _parse_vless(link, source)
        elif scheme == "trojan":
            node = _parse_trojan(link, source)
        elif scheme == "ss":
            node = _parse_ss(link, source)
        elif scheme in ("hysteria2", "hy2"):
            node = _parse_hy2(link, source)
        elif scheme == "tuic":
            node = _parse_tuic(link, source)
        else:
            return None  # ssr / hysteria / juicity 等直接忽略
    except Exception as exc:  # 单条解析失败不影响整体
        return Node(link=link, proto=scheme, name="", server="", port=0, source=source, error=f"parse: {exc}")

    if node is not None and not node.error and _needs_singbox(node.proto, node.params):
        node.core = "sing-box"
    return node


def _body_and_name(link: str):
    body = link.split("://", 1)[1]
    name = ""
    if "#" in body:
        body, name = body.split("#", 1)
        name = unquote(name).strip()
    query = ""
    if "?" in body:
        body, query = body.split("?", 1)
    return body, unquote(name), query


def _parse_vmess(link: str, source: str) -> Node:
    body, name, _ = _body_and_name(link)
    raw = body.strip()
    # 少数订阅里 vmess 是明文 JSON（不带 base64）
    if raw.startswith("{"):
        obj = json.loads(raw)
    else:
        txt = b64decode_any(raw).decode("utf-8", "replace")
        obj = json.loads(txt)

    p = {
        "id": obj.get("id", ""),
        "aid": obj.get("aid") or obj.get("alterId") or 0,
        "scy": obj.get("scy") or obj.get("security") or "auto",
        "net": (obj.get("net") or "tcp").lower(),
        "header_type": (obj.get("type") or "").lower(),
        "host": obj.get("host") or "",
        "path": obj.get("path") or "",
        "sni": obj.get("sni") or obj.get("host") or "",
        "alpn": obj.get("alpn") or "",
        "fp": obj.get("fp") or "",
        "security": (obj.get("tls") or "none").lower() if obj.get("tls") else "none",
        "service_name": obj.get("path") if (obj.get("net") or "").lower() == "grpc" else "",
        "allow_insecure": obj.get("allowInsecure") or obj.get("verify_cert") is False,
    }
    if p["security"] in ("tls", "reality", "xtls"):
        pass
    else:
        p["security"] = "none"
    return Node(
        link=link,
        proto="vmess",
        name=name or obj.get("ps") or f"{obj.get('add')}:{obj.get('port')}",
        server=str(obj.get("add", "")),
        port=int(obj.get("port") or 0),
        params=p,
        source=source,
        core="xray",
    )


def _parse_vless(link: str, source: str) -> Node:
    body, name, query = _body_and_name(link)
    if "@" not in body:
        raise ValueError("missing uuid@host")
    userinfo, hp = body.rsplit("@", 1)
    host, port = _split_host_port(hp)
    q = _query(query)
    p = {
        "id": unquote(userinfo),
        "encryption": q.get("encryption", "none"),
        "flow": q.get("flow", ""),
        "net": (q.get("type") or "tcp").lower(),
        "security": (q.get("security") or "none").lower(),
        "sni": q.get("sni") or q.get("peer") or "",
        "host": q.get("host") or "",
        "path": q.get("path") or "",
        "service_name": q.get("servicename") or q.get("service_name") or "",
        "mode": q.get("mode") or "",
        "alpn": q.get("alpn") or "",
        "fp": q.get("fp") or "",
        "pbk": q.get("pbk") or "",
        "sid": q.get("sid") or "",
        "spx": q.get("spx") or "",
        "header_type": (q.get("headertype") or "").lower(),
        "allow_insecure": q.get("allowinsecure") or q.get("insecure") or "",
    }
    if p["net"] == "grpc" and not p["service_name"]:
        p["service_name"] = p["path"]
    return Node(
        link=link,
        proto="vless",
        name=name or f"{host}:{port}",
        server=host,
        port=port,
        params=p,
        source=source,
        core="xray",
    )


def _parse_trojan(link: str, source: str) -> Node:
    body, name, query = _body_and_name(link)
    if "@" not in body:
        raise ValueError("missing password@host")
    password, hp = body.rsplit("@", 1)
    host, port = _split_host_port(hp)
    q = _query(query)
    p = {
        "password": unquote(password),
        "net": (q.get("type") or "tcp").lower(),
        # trojan 默认走 TLS，但链接里显式写了 security=none 就尊重它
        "security": (q.get("security") or "tls").lower(),
        "sni": q.get("sni") or q.get("peer") or "",
        "host": q.get("host") or "",
        "path": q.get("path") or "",
        "service_name": q.get("servicename") or "",
        "alpn": q.get("alpn") or "",
        "fp": q.get("fp") or "",
        "allow_insecure": q.get("allowinsecure") or q.get("insecure") or "",
        "header_type": (q.get("headertype") or "").lower(),
    }
    return Node(
        link=link,
        proto="trojan",
        name=name or f"{host}:{port}",
        server=host,
        port=port,
        params=p,
        source=source,
        core="xray",
    )


def _parse_ss(link: str, source: str) -> Node:
    body, name, query = _body_and_name(link)
    plugin = ""
    if "@" in body:
        userinfo, hp = body.rsplit("@", 1)
        try:
            decoded = b64decode_any(userinfo).decode("utf-8", "replace")
            method, password = decoded.split(":", 1)
        except (binascii.Error, ValueError):
            method, password = unquote(userinfo).split(":", 1)
    else:
        decoded = b64decode_any(body).decode("utf-8", "replace")
        if "@" not in decoded:
            raise ValueError("bad ss link")
        userinfo, hp = decoded.rsplit("@", 1)
        method, password = userinfo.split(":", 1)
    host, port = _split_host_port(hp)
    q = _query(query)
    plugin = q.get("plugin", "")
    p = {"method": method, "password": password, "plugin": plugin, "net": "tcp"}
    node = Node(
        link=link,
        proto="ss",
        name=name or f"{host}:{port}",
        server=host,
        port=port,
        params=p,
        source=source,
        core="xray",
    )
    if plugin:
        # xray 不支持 ss 插件（obfs / v2ray-plugin），标记为不可测
        node.error = f"ss plugin unsupported: {plugin.split(';')[0]}"
    return node


def _parse_hy2(link: str, source: str) -> Node:
    body, name, query = _body_and_name(link)
    userinfo, hp = body.rsplit("@", 1)
    host, port = _split_host_port(hp)
    q = _query(query)
    p = {
        "password": unquote(userinfo),
        "sni": q.get("sni") or "",
        "allow_insecure": q.get("insecure") or q.get("allowinsecure") or "",
        "obfs": q.get("obfs") or "",
        "obfs_password": q.get("obfs-password") or q.get("obfs_password") or "",
        "alpn": q.get("alpn") or "",
        "upmbps": q.get("upmbps") or "",
        "downmbps": q.get("downmbps") or "",
    }
    return Node(
        link=link,
        proto="hysteria2",
        name=name or f"{host}:{port}",
        server=host,
        port=port,
        params=p,
        source=source,
        core="sing-box",
    )


def _parse_tuic(link: str, source: str) -> Node:
    body, name, query = _body_and_name(link)
    userinfo, hp = body.rsplit("@", 1)
    host, port = _split_host_port(hp)
    q = _query(query)
    uuid, _, password = userinfo.partition(":")
    p = {
        "uuid": unquote(uuid),
        "password": unquote(password),
        "sni": q.get("sni") or "",
        "allow_insecure": q.get("allow_insecure") or q.get("insecure") or "",
        "alpn": q.get("alpn") or "",
        "congestion_control": q.get("congestion_control") or "bbr",
        "udp_relay_mode": q.get("udp_relay_mode") or "native",
    }
    return Node(
        link=link,
        proto="tuic",
        name=name or f"{host}:{port}",
        server=host,
        port=port,
        params=p,
        source=source,
        core="sing-box",
    )


def rename_link(link: str, new_name: str) -> str:
    """把链接里的节点名改成 new_name（vmess 改 JSON 的 ps，其余改 fragment）。"""
    if link.lower().startswith("vmess://"):
        try:
            body, _, _ = _body_and_name(link)
            raw = body.strip()
            obj = json.loads(raw) if raw.startswith("{") else json.loads(b64decode_any(raw).decode("utf-8"))
            obj["ps"] = new_name
            return "vmess://" + b64encode_str(json.dumps(obj, ensure_ascii=False, separators=(",", ":")))
        except Exception:
            return link
    base = link.split("#", 1)[0]
    # fragment 里出现 # 会截断链接，用全角符号替换；中文保持原样，客户端可直接显示
    safe = new_name.replace("#", "＃")
    return base + "#" + safe


def parse_many(links: List[str], source: str = "") -> List[Node]:
    out: List[Node] = []
    for line in links:
        n = parse_link(line, source)
        if n is not None:
            out.append(n)
    return out
