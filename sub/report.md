# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-27 08:20:38+0800`

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
| 抓取链接 | 19620 |
| 去重后节点 | 8041 |
| TCP 预筛剔除 | 3817 |
| 真连接测试 | 8041 |
| 测试通过 | 827 |
| **最终保留** | **827** |
| 耗时 | 294.4 秒 |

> 解析阶段跳过：重复 11549、协议未启用 0、无法解析 30

## 协议分布

vless 441 · ss 165 · vmess 138 · trojan 73 · hysteria2 10

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 827 个节点中，有 **690** 个能经代理访问到国内目标站，**137** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vless | `172.64.146.66:443` | 63 ms | 959 ms | - |
| 2 | EPODONIOS | vless | `172.64.147.91:443` | 69 ms | 1154 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.167:443` | 72 ms | 1011 ms | - |
| 4 | EPODONIOS | vless | `172.64.152.241:443` | 79 ms | 950 ms | - |
| 5 | EPODONIOS | vless | `47.253.226.114:443` | 82 ms | 978 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 453 | vless | `104.18.45.38:443` | 82 ms | 989 ms | - |
| 7 | EPODONIOS | ss | `156.146.38.170:443` | 84 ms | 861 ms | - |
| 8 | EPODONIOS | ss | `37.19.198.160:443` | 84 ms | 966 ms | - |
| 9 | EPODONIOS | vless | `47.253.226.114:443` | 84 ms | 989 ms | - |
| 10 | EPODONIOS | ss | `156.146.38.168:443` | 86 ms | 852 ms | - |
| 11 | EPODONIOS | ss | `37.19.198.236:443` | 86 ms | 971 ms | - |
| 12 | EPODONIOS | ss | `15.204.247.206:4444` | 86 ms | 1275 ms | - |
| 13 | EPODONIOS | ss | `156.146.38.169:443` | 87 ms | 884 ms | - |
| 14 | EPODONIOS | ss | `37.19.198.243:443` | 87 ms | 973 ms | - |
| 15 | EPODONIOS | vless | `188.114.97.6:443` | 88 ms | 1051 ms | - |
| 16 | EPODONIOS | ss | `37.19.198.244:443` | 90 ms | 959 ms | - |
| 17 | US 🇺🇸 / @Raydikalx / F2583B | vmess | `67.220.85.46:18000` | 90 ms | 1760 ms | - |
| 18 | EPODONIOS | vless | `38.107.232.36:80` | 91 ms | 不可达 | - |
| 19 | EPODONIOS | vmess | `38.110.1.246:18000` | 91 ms | 1453 ms | - |
| 20 | CA 🇨🇦 / @Raydikalx / A1CD58 | vmess | `cf.0sm.com:80` | 92 ms | 955 ms | - |
| 21 | EPODONIOS | vless | `103.169.142.30:8880` | 93 ms | 977 ms | - |
| 22 | EPODONIOS | vless | `154.197.75.40:8880` | 93 ms | 1016 ms | - |
| 23 | EPODONIOS | vmess | `67.220.85.46:18000` | 95 ms | 1497 ms | - |
| 24 | US 🇺🇸 / @Raydikalx / 46741C | vmess | `67.220.85.46:18000` | 95 ms | 1439 ms | - |
| 25 | EPODONIOS | vless | `172.66.0.162:443` | 96 ms | 966 ms | - |
| 26 | EPODONIOS | vless | `cf.877774.xyz:443` | 96 ms | 952 ms | - |
| 27 | EPODONIOS | vless | `172.64.152.241:443` | 99 ms | 940 ms | - |
| 28 | EPODONIOS | vmess | `67.220.95.3:18000` | 99 ms | 1563 ms | - |
| 29 | EPODONIOS | vless | `104.18.35.15:443` | 100 ms | 1625 ms | - |
| 30 | ⚡ b2n.ir/v2ray-configs / 975 | ss | `138.199.42.68:8080` | 103 ms | 888 ms | - |
| 31 | EPODONIOS | vless | `104.18.41.190:443` | 104 ms | 961 ms | - |
| 32 | EPODONIOS | vless | `172.67.130.187:2083` | 107 ms | 949 ms | - |
| 33 | EPODONIOS | vless | `188.114.96.9:443` | 107 ms | 973 ms | - |
| 34 | EPODONIOS | vless | `104.19.145.193:443` | 113 ms | 1045 ms | - |
| 35 | EPODONIOS | vmess | `38.91.107.49:18000` | 114 ms | 1297 ms | - |
| 36 | EPODONIOS | vless | `185.193.29.30:8880` | 115 ms | 996 ms | - |
| 37 | EPODONIOS | vless | `cf.877774.xyz:443` | 115 ms | 1188 ms | - |
| 38 | EPODONIOS | vless | `216.24.57.30:8880` | 116 ms | 1120 ms | - |
| 39 | CA 🇨🇦 / @Raydikalx / 0AD519 | vmess | `172.67.187.145:80` | 120 ms | 867 ms | - |
| 40 | EPODONIOS | vless | `172.64.150.28:8880` | 121 ms | 973 ms | - |
| 41 | EPODONIOS | vless | `195.123.235.177:443` | 121 ms | 919 ms | - |
| 42 | EPODONIOS | vless | `cf.877774.xyz:443` | 122 ms | 978 ms | - |
| 43 | EPODONIOS | vless | `188.114.97.6:443` | 122 ms | 974 ms | - |
| 44 | EPODONIOS | vmess | `cf.0sm.com:443` | 122 ms | 872 ms | - |
| 45 | EPODONIOS | trojan | `69.164.240.85:50875` | 123 ms | 1648 ms | - |
| 46 | ⚡ b2n.ir/v2ray-configs / 925 | vless | `8.47.69.60:443` | 123 ms | 1156 ms | - |
| 47 | EPODONIOS | vless | `3h-unitedstates1.09vpn.com:80` | 124 ms | 不可达 | - |
| 48 | EPODONIOS | vless | `130.250.137.30:8880` | 125 ms | 1046 ms | - |
| 49 | EPODONIOS | vmess | `67.220.95.3:18000` | 125 ms | 1406 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 125 ms | 1449 ms | - |

> 仅展示前 50 个，共 827 个；完整列表见 `sub/nodes.txt`。
