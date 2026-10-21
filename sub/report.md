# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-21 17:42:24+0800`

## 订阅地址

```
https://raw.githubusercontent.com/zppHappy/get-to-internet-by-own/main/sub/base64.txt
```

国内直连 raw 经常不通，用 jsDelivr 镜像（约 12 小时缓存，加 `?t=时间戳` 可强制刷新）：

```
https://cdn.jsdelivr.net/gh/zppHappy/get-to-internet-by-own@main/sub/base64.txt
```

## 本次统计

| 项目 | 数量 |
|---|---|
| 抓取链接 | 19783 |
| 去重后节点 | 7966 |
| TCP 预筛剔除 | 3837 |
| 真连接测试 | 7966 |
| 测试通过 | 756 |
| **最终保留** | **756** |
| 耗时 | 306.1 秒 |

> 解析阶段跳过：重复 11789、协议未启用 0、无法解析 28

## 协议分布

vless 417 · ss 150 · vmess 120 · trojan 64 · hysteria2 5

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 756 个节点中，有 **626** 个能经代理访问到国内目标站，**130** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `95.215.201.18:19999` | 23 ms | 714 ms | - |
| 2 | EPODONIOS | vmess | `129.146.77.248:39495` | 26 ms | 992 ms | - |
| 3 | EPODONIOS | vless | `104.18.0.181:2082` | 65 ms | 725 ms | - |
| 4 | ⚡ b2n.ir/v2ray-configs / 782 | vless | `172.64.150.43:8080` | 66 ms | 1009 ms | - |
| 5 | EPODONIOS | vless | `104.18.35.86:8080` | 68 ms | 762 ms | - |
| 6 | EPODONIOS | vless | `172.64.150.28:2082` | 68 ms | 758 ms | - |
| 7 | EPODONIOS | vless | `104.18.0.181:2082` | 69 ms | 737 ms | - |
| 8 | ⚡ b2n.ir/v2ray-configs / 747 | vless | `104.18.0.181:2082` | 72 ms | 758 ms | - |
| 9 | EPODONIOS | vless | `188.114.98.0:443` | 79 ms | 756 ms | - |
| 10 | US 🇺🇸 / @Raydikalx / B79C28 | vmess | `169.197.142.22:18000` | 80 ms | 732 ms | - |
| 11 | EPODONIOS | vless | `172.64.150.28:2082` | 81 ms | 753 ms | - |
| 12 | EPODONIOS | vless | `188.114.97.6:443` | 85 ms | 764 ms | - |
| 13 | EPODONIOS | ss | `156.146.38.167:443` | 86 ms | 879 ms | - |
| 14 | EPODONIOS | vless | `188.114.97.6:443` | 86 ms | 834 ms | - |
| 15 | EPODONIOS | vless | `188.114.98.0:443` | 86 ms | 726 ms | - |
| 16 | EPODONIOS | vless | `188.114.98.0:443` | 87 ms | 839 ms | - |
| 17 | EPODONIOS | vless | `172.64.150.43:443` | 88 ms | 833 ms | - |
| 18 | EPODONIOS | vless | `188.114.98.0:443` | 88 ms | 754 ms | - |
| 19 | EPODONIOS | vless | `162.159.135.234:443` | 89 ms | 781 ms | - |
| 20 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 90 ms | 992 ms | - |
| 21 | EPODONIOS | ss | `156.146.38.170:443` | 91 ms | 889 ms | - |
| 22 | EPODONIOS | ss | `156.146.38.168:443` | 92 ms | 942 ms | - |
| 23 | EPODONIOS | ss | `156.146.38.169:443` | 92 ms | 不可达 | - |
| 24 | ⚡ b2n.ir/v2ray-configs / 379 | vless | `188.114.97.6:443` | 92 ms | 768 ms | - |
| 25 | EPODONIOS | vless | `188.114.98.0:443` | 93 ms | 758 ms | - |
| 26 | EPODONIOS | vless | `188.114.98.0:443` | 94 ms | 761 ms | - |
| 27 | EPODONIOS | vless | `104.18.43.174:443` | 95 ms | 792 ms | - |
| 28 | ⚡ b2n.ir/v2ray-configs / 260 | vless | `188.114.97.6:443` | 96 ms | 765 ms | - |
| 29 | EPODONIOS | vless | `188.114.98.0:443` | 97 ms | 892 ms | - |
| 30 | EPODONIOS | trojan | `172.67.131.217:443` | 98 ms | 779 ms | - |
| 31 | ⚡ b2n.ir/v2ray-configs / 240 | vless | `104.18.41.190:443` | 98 ms | 781 ms | - |
| 32 | EPODONIOS | vless | `188.114.97.6:443` | 99 ms | 796 ms | - |
| 33 | EPODONIOS | vless | `cf.877774.xyz:443` | 99 ms | 780 ms | - |
| 34 | EPODONIOS | vless | `104.18.43.174:443` | 99 ms | 772 ms | - |
| 35 | EPODONIOS | vless | `172.67.155.65:8443` | 99 ms | 781 ms | - |
| 36 | EPODONIOS | vless | `188.114.97.6:443` | 99 ms | 793 ms | - |
| 37 | ⚡ b2n.ir/v2ray-configs / 683 | vless | `b2n.ir:443` | 99 ms | 744 ms | - |
| 38 | CA 🇨🇦 / @Raydikalx / B52D10 | vmess | `us16-4.998998.best:443` | 100 ms | 764 ms | - |
| 39 | EPODONIOS | vless | `172.64.158.170:443` | 101 ms | 769 ms | - |
| 40 | EPODONIOS | vless | `188.114.97.6:443` | 101 ms | 777 ms | - |
| 41 | EPODONIOS | ss | `173.244.56.9:443` | 101 ms | 749 ms | - |
| 42 | ⚡ b2n.ir/v2ray-configs / 411 | vless | `b2n.ir:443` | 101 ms | 941 ms | - |
| 43 | EPODONIOS | vless | `104.18.41.190:443` | 103 ms | 752 ms | - |
| 44 | EPODONIOS | vless | `104.18.43.174:443` | 104 ms | 1148 ms | - |
| 45 | ⚡ b2n.ir/v2ray-configs / 567 | vless | `188.114.97.6:443` | 104 ms | 856 ms | - |
| 46 | EPODONIOS | vless | `188.114.98.0:443` | 105 ms | 833 ms | - |
| 47 | EPODONIOS | vless | `104.21.91.244:443` | 107 ms | 754 ms | - |
| 48 | EPODONIOS | vless | `104.21.91.244:443` | 107 ms | 744 ms | - |
| 49 | EPODONIOS | vless | `188.114.98.0:443` | 108 ms | 769 ms | - |
| 50 | EPODONIOS | vless | `188.114.97.6:443` | 108 ms | 853 ms | - |

> 仅展示前 50 个，共 756 个；完整列表见 `sub/nodes.txt`。
