"""上传到 GitHub：仓库文件（Contents API）或 Gist。

用标准库 urllib，不需要额外依赖。
"""
from __future__ import annotations

import base64
import json
import os
import ssl
import urllib.error
import urllib.request
from typing import Dict, Optional, Tuple

API = "https://api.github.com"


class UploadError(RuntimeError):
    pass


def _request(method: str, url: str, token: str, payload: Optional[dict] = None) -> dict:
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "v2sub-filter")
    if data:
        req.add_header("Content-Type", "application/json")
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body.strip() else {}
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:400]
        raise UploadError(f"{exc.code} {detail}") from exc
    except Exception as exc:
        raise UploadError(str(exc)) from exc


def _get_sha(owner: str, repo: str, path: str, branch: str, token: str) -> Optional[str]:
    url = f"{API}/repos/{owner}/{repo}/contents/{path}?ref={branch}"
    try:
        info = _request("GET", url, token)
        return info.get("sha")
    except UploadError as exc:
        if "404" in str(exc):
            return None
        raise


def upload_repo_file(token: str, owner: str, repo: str, path: str, branch: str, content: str, message: str) -> str:
    path = path.lstrip("/")
    sha = _get_sha(owner, repo, path, branch, token)
    payload = {
        "message": message,
        "content": base64.b64encode(content.encode("utf-8")).decode("ascii"),
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha
    url = f"{API}/repos/{owner}/{repo}/contents/{path}"
    info = _request("PUT", url, token, payload)
    html = (info.get("content") or {}).get("html_url", "")
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}", html


def update_gist(token: str, gist_id: str, filename: str, content: str, description: str = "") -> Tuple[str, str]:
    payload = {"files": {filename: {"content": content}}}
    if description:
        payload["description"] = description
    info = _request("PATCH", f"{API}/gists/{gist_id}", token, payload)
    files = info.get("files") or {}
    entry = files.get(filename) or {}
    return entry.get("raw_url", ""), info.get("html_url", "")


def create_gist(token: str, filename: str, content: str, description: str = "", public: bool = False) -> Tuple[str, str]:
    payload = {"description": description, "public": bool(public), "files": {filename: {"content": content}}}
    info = _request("POST", f"{API}/gists", token, payload)
    files = info.get("files") or {}
    entry = files.get(filename) or {}
    return entry.get("raw_url", ""), info.get("html_url", "")


def upload(cfg: dict, files: Dict[str, str], log=print) -> Dict[str, str]:
    """按配置上传，返回 {'sub_url':..., 'html_url':...}。"""
    gh = cfg.get("github") or {}
    if not gh.get("enabled"):
        return {}

    token_env = gh.get("token_env") or "GITHUB_TOKEN"
    token = os.environ.get(token_env, "").strip()
    if not token:
        raise UploadError(f"环境变量 {token_env} 为空，无法上传（GitHub Token 需要 repo/gist 权限）")

    mode = (gh.get("mode") or "repo").lower()
    out: Dict[str, str] = {}

    if mode == "gist":
        gist_id = (gh.get("gist_id") or "").strip()
        fname = gh.get("gist_filename") or "sub.txt"
        desc = gh.get("gist_description") or "v2sub filtered subscription"
        if gist_id:
            raw, html = update_gist(token, gist_id, fname, files["base64"], desc)
            log(f"  ✓ 已更新 Gist: {html}")
        else:
            raw, html = create_gist(token, fname, files["base64"], desc, bool(gh.get("gist_public")))
            log(f"  ✓ 已创建 Gist: {html}")
            log(f"    ⚠️ 请把 gist_id 填进配置，下次就会更新同一个 Gist：{html.rsplit('/', 1)[-1]}")
        out["sub_url"] = raw
        out["html_url"] = html
        return out

    owner = (gh.get("owner") or "").strip()
    repo = (gh.get("repo") or "").strip()
    if not owner or not repo:
        # GitHub Actions 里 GITHUB_REPOSITORY = "owner/repo"
        env_repo = os.environ.get("GITHUB_REPOSITORY", "")
        if "/" in env_repo:
            e_owner, e_repo = env_repo.split("/", 1)
            owner = owner or e_owner
            repo = repo or e_repo
    if not owner or not repo:
        raise UploadError("github.owner / github.repo 未配置")
    branch = gh.get("branch") or "main"
    path = gh.get("path") or "sub/base64.txt"
    msg = gh.get("commit_message") or "chore: update filtered subscription"

    raw, html = upload_repo_file(token, owner, repo, path, branch, files["base64"], msg)
    log(f"  ✓ 已上传订阅: {path}")
    out["sub_url"] = raw
    out["html_url"] = html

    if gh.get("upload_plain"):
        plain_path = gh.get("plain_path") or "sub/nodes.txt"
        upload_repo_file(token, owner, repo, plain_path, branch, files["plain"], msg)
        log(f"  ✓ 已上传明文列表: {plain_path}")

    # 人看的页面：GitHub 会把 .md 渲染成表格，订阅地址变化后立刻能刷出来
    if gh.get("upload_markdown", True) and files.get("markdown"):
        md_path = gh.get("markdown_path") or "sub/report.md"
        upload_repo_file(token, owner, repo, md_path, branch, files["markdown"], msg)
        log(f"  ✓ 已更新可读报告: {md_path}")

    return out
