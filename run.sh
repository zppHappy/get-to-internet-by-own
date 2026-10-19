#!/usr/bin/env bash
# 一键运行：建虚拟环境 → 装依赖 → 装内核（缺了才装）→ 筛选
set -euo pipefail
cd "$(dirname "$0")"

PY="${PYTHON:-python3}"

if [ ! -d .venv ]; then
  echo "==> 创建虚拟环境 .venv"
  "$PY" -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
pip install -q --disable-pip-version-check -r requirements.txt

if [ ! -x bin/xray ] || [ ! -x bin/sing-box ]; then
  echo "==> 下载代理内核"
  chmod +x install_core.sh
  ./install_core.sh
fi

if [ ! -f sources.txt ] && [ -z "${V2SUB_SOURCES:-}" ]; then
  cp -n sources.example.txt sources.txt
  echo
  echo "!! 还没有订阅：请把订阅地址填进 sources.txt（一行一个），然后重新运行 ./run.sh"
  exit 1
fi

exec python filter.py -c config.yaml "$@"
