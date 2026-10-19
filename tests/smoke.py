"""冒烟测试：把 filter.main() 全流程打桩跑一遍。

内核、网络、文件写入全部替换成假实现，只验证主流程和统计段的逻辑。
目的是在 CI 里几秒内发现「统计字段拼错、变量名写错」这类会让正式运行白跑
二十分钟的低级错误。

用法：python3 tests/smoke.py
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

import filter as F  # noqa: E402
from v2sub.config import DEFAULTS  # noqa: E402
from v2sub.tester import TestResult  # noqa: E402

LINKS = [
    "vless://11111111-1111-1111-1111-111111111111@1.2.3.4:443?security=reality&pbk=x#节点A",
    "vmess://eyJ2IjoiMiIsInBzIjoi6IqC54K5QiIsImFkZCI6IjUuNi43LjgiLCJwb3J0IjoiODAiLCJpZCI6IjExMTExMTExLTExMTEtMTExMS0xMTExLTExMTExMTExMTExMSIsIm5ldCI6IndzIiwicGF0aCI6Ii8ifQ==",
]
# 补到 60 条，让 TCP 预筛分支（阈值 50）也跑到
LINKS += [
    f"vless://22222222-2222-2222-2222-222222222222@10.0.0.{i}:443?security=tls&sni=a.com#节点{i}"
    for i in range(1, 59)
]


def main() -> int:
    cfg = copy.deepcopy(DEFAULTS)
    cfg["sources"] = ["http://example.com/sub"]
    cfg["settings"].update({"speed_test": False, "tcp_precheck": True, "max_delay_ms": 5000})
    cfg["output"]["dir"] = str(ROOT / "sub")
    cfg["github"]["enabled"] = False
    cfg["_config_dir"] = str(ROOT)

    F.load_config = lambda p: cfg
    F.fetch_all = lambda sources, timeout, log=None: ([(l, "fake") for l in LINKS], [])
    F.find_core = lambda name, d=None: "xray"
    F.precheck = lambda nodes, timeout=2.0, concurrency=200, log=None: (
        nodes[:1],
        [TestResult(node=n, ok=False, error="tcp: 连接超时 2.0s") for n in nodes[1:]],
        2,
    )
    F.test_nodes = lambda nodes, st, core_dir=None, progress=None: [
        TestResult(node=n, ok=True, delay_ms=100 + i * 50) for i, n in enumerate(nodes)
    ]
    F.write_files = lambda files, cfg: []

    sys.argv = ["filter.py", "-c", "config.yaml"]
    rc = F.main()
    if rc != 0:
        print(f"✗ main() 返回 {rc}")
        return 1
    print("✓ 冒烟测试通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
