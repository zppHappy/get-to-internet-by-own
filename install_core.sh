#!/usr/bin/env bash
# 下载代理内核到 ./bin：xray（vmess/vless/trojan/ss）+ sing-box（hysteria2/tuic）
# 用法： ./install_core.sh            # 两个都装
#        ./install_core.sh xray       # 只装 xray
#        ./install_core.sh sing-box   # 只装 sing-box
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p bin

OS_RAW="$(uname -s)"
ARCH_RAW="$(uname -m)"
WANT="${1:-all}"

api_latest() { # $1=repo
  local json
  json="$(curl -fsSL --retry 3 "https://api.github.com/repos/$1/releases/latest")" || return 1
  printf '%s' "$json" | sed -n 's/.*"tag_name":[[:space:]]*"\([^"]*\)".*/\1/p'
}

install_xray() {
  local os arch asset tag
  case "$OS_RAW" in
    Darwin) os="macos" ;;
    Linux)  os="linux" ;;
    *) echo "!! 不支持的系统: $OS_RAW"; return 1 ;;
  esac
  case "$ARCH_RAW" in
    arm64|aarch64) arch="arm64-v8a" ;;
    x86_64|amd64)  arch="64" ;;
    *) echo "!! 不支持的架构: $ARCH_RAW"; return 1 ;;
  esac
  asset="Xray-${os}-${arch}.zip"
  tag="$(api_latest XTLS/Xray-core)"
  [ -z "$tag" ] && { echo "!! 获取 Xray 版本失败"; return 1; }
  echo "==> 下载 Xray ${tag} (${asset})"
  tmp="$(mktemp -d)"
  curl -fL --retry 3 -o "$tmp/xray.zip" "https://github.com/XTLS/Xray-core/releases/download/${tag}/${asset}"
  unzip -oq "$tmp/xray.zip" -d "$tmp/x"
  cp "$tmp/x/xray" bin/xray
  chmod +x bin/xray
  rm -rf "$tmp"
  ./bin/xray version | sed -n '1p'
}

install_singbox() {
  local os arch asset tag
  case "$OS_RAW" in
    Darwin) os="darwin" ;;
    Linux)  os="linux" ;;
    *) echo "!! 不支持的系统: $OS_RAW"; return 1 ;;
  esac
  case "$ARCH_RAW" in
    arm64|aarch64) arch="arm64" ;;
    x86_64|amd64)  arch="amd64" ;;
    *) echo "!! 不支持的架构: $ARCH_RAW"; return 1 ;;
  esac
  tag="$(api_latest SagerNet/sing-box)"
  [ -z "$tag" ] && { echo "!! 获取 sing-box 版本失败"; return 1; }
  local ver="${tag#v}"
  asset="sing-box-${ver}-${os}-${arch}.tar.gz"
  echo "==> 下载 sing-box ${tag} (${asset})"
  tmp="$(mktemp -d)"
  curl -fL --retry 3 -o "$tmp/sb.tar.gz" "https://github.com/SagerNet/sing-box/releases/download/${tag}/${asset}"
  tar -xzf "$tmp/sb.tar.gz" -C "$tmp"
  cp "$tmp"/sing-box-*/sing-box bin/sing-box
  chmod +x bin/sing-box
  rm -rf "$tmp"
  ./bin/sing-box version | sed -n '1p'
}

case "$WANT" in
  all) install_xray; install_singbox ;;
  xray) install_xray ;;
  sing-box|singbox) install_singbox ;;
  *) echo "用法: $0 [all|xray|sing-box]"; exit 1 ;;
esac

echo "==> 完成，内核位于 $(pwd)/bin"
