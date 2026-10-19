"""配置加载与默认值。"""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any, Dict

DEFAULTS: Dict[str, Any] = {
    "sources": [],
    "settings": {
        "concurrency": 8,
        "startup_timeout": 6.0,
        "fetch_timeout": 20,
        # TCP 预筛：先剔掉端口都不通的节点，避免为它们冷启动内核（只对 TCP 系协议生效）
        "tcp_precheck": True,
        "precheck_timeout": 2.0,
        "precheck_concurrency": 200,
        # 真连接测试（和 v2rayN 的「真连接延迟」一致：通过代理真的请求一次）
        "delay_test_url": "https://www.gstatic.com/generate_204",
        "delay_timeout": 5,
        "delay_retries": 2,
        "accept_any_status": True,
        "accept_status": [200, 204, 301, 302],
        # 测速（和 v2rayN 的「下载速度」一致：通过代理真的下载一段数据）
        "speed_test": True,
        "speed_test_url": "https://cachefly.cachefly.net/10mb.test",
        "speed_timeout": 8,
        "speed_max_bytes": 0,
        # 筛选条件
        "max_delay_ms": 2500,
        "min_speed_mbps": 0.0,
        "require_speed": False,
        "max_nodes": 0,
        "protocols": ["vmess", "vless", "trojan", "ss", "hysteria2", "tuic"],
        "dedupe": True,
        # 命名
        "rename": True,
        "rename_template": "{name} | {delay}ms | {speed}",
        "core_dir": "./bin",
    },
    "output": {
        "dir": "./sub",
        "base64": "base64.txt",
        "plain": "nodes.txt",
        "report": "report.json",
        "markdown": "report.md",
        "include_links_in_report": False,
    },
    "github": {
        "enabled": False,
        "token_env": "GITHUB_TOKEN",
        "mode": "repo",  # repo | gist
        "owner": "",
        "repo": "",
        "path": "sub/base64.txt",
        "branch": "main",
        "commit_message": "chore: update filtered subscription",
        "upload_plain": False,
        "plain_path": "sub/nodes.txt",
        "gist_id": "",
        "gist_filename": "sub.txt",
        "gist_description": "v2sub filtered subscription",
        "gist_public": False,
    },
}


def _merge(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    out = copy.deepcopy(base)
    for k, v in (override or {}).items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _merge(out[k], v)
        else:
            out[k] = v
    return out


def load_config(path: str) -> Dict[str, Any]:
    p = Path(path)
    if not p.is_file():
        raise SystemExit(f"配置文件不存在: {path}")
    text = p.read_text(encoding="utf-8")
    if p.suffix.lower() in (".yaml", ".yml"):
        try:
            import yaml
        except ImportError:
            raise SystemExit("需要 PyYAML：pip install pyyaml")
        data = yaml.safe_load(text) or {}
    else:
        data = json.loads(text or "{}")
    cfg = _merge(DEFAULTS, data)
    # 相对路径按配置文件所在目录解析
    base = p.resolve().parent
    for key, sub in (("dir", "output"),):
        val = cfg["output"].get(key, "")
        if val and not Path(val).is_absolute():
            cfg["output"][key] = str(base / val)
    cd = cfg["settings"].get("core_dir", "")
    if cd and not Path(cd).is_absolute():
        cfg["settings"]["core_dir"] = str(base / cd)
    cfg["_config_dir"] = str(base)
    return cfg
