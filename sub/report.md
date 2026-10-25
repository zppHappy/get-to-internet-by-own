# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-25 23:43:34+0800`

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
| 抓取链接 | 20014 |
| 去重后节点 | 8076 |
| TCP 预筛剔除 | 3974 |
| 真连接测试 | 8076 |
| 测试通过 | 604 |
| **最终保留** | **604** |
| 耗时 | 312.1 秒 |

> 解析阶段跳过：重复 11913、协议未启用 0、无法解析 25

## 协议分布

vless 288 · ss 151 · vmess 120 · trojan 41 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 604 个节点中，有 **482** 个能经代理访问到国内目标站，**122** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | ⚡ b2n.ir/v2ray-configs / 980 | vless | `104.18.45.38:443` | 52 ms | 860 ms | - |
| 2 | EPODONIOS | vless | `cf.877774.xyz:443` | 56 ms | 796 ms | - |
| 3 | EPODONIOS | vless | `cf.877774.xyz:443` | 58 ms | 695 ms | - |
| 4 | EPODONIOS | vless | `172.64.152.241:443` | 60 ms | 1034 ms | - |
| 5 | ⚡ b2n.ir/v2ray-configs / 343 | vless | `88.216.69.253:443` | 62 ms | 727 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 310 | vless | `88.216.69.253:443` | 67 ms | 688 ms | - |
| 7 | EPODONIOS | vmess | `Rib9JXAYoqjGN2KW.v.3dns.vip:443` | 72 ms | 689 ms | - |
| 8 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 72 ms | 不可达 | - |
| 9 | EPODONIOS | vless | `172.64.158.170:443` | 74 ms | 801 ms | - |
| 10 | EPODONIOS | vless | `104.18.0.181:2082` | 74 ms | 697 ms | - |
| 11 | US 🇺🇸 / @Raydikalx / CE2CEA | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 76 ms | 654 ms | - |
| 12 | EPODONIOS | ss | `95.215.201.18:19999` | 77 ms | 789 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 466 | vless | `104.21.221.158:443` | 79 ms | 718 ms | - |
| 14 | US 🇺🇸 / @Raydikalx / FC15CE | vmess | `84.17.41.2:18000` | 82 ms | 4539 ms | - |
| 15 | ⚡ b2n.ir/v2ray-configs / 351 | vless | `8.47.69.60:443` | 83 ms | 965 ms | - |
| 16 | EPODONIOS | vless | `172.66.0.162:443` | 86 ms | 919 ms | - |
| 17 | EPODONIOS | vmess | `129.146.77.248:39495` | 87 ms | 1178 ms | - |
| 18 | EPODONIOS | vless | `15.204.97.197:23576` | 88 ms | 不可达 | - |
| 19 | EPODONIOS | vless | `15.204.97.197:23576` | 88 ms | 不可达 | - |
| 20 | US 🇺🇸 / @Raydikalx / 452ED5 | vmess | `129.146.77.248:39495` | 88 ms | 937 ms | - |
| 21 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 90 ms | 1200 ms | - |
| 22 | EPODONIOS | vless | `15.204.97.206:23576` | 91 ms | 不可达 | - |
| 23 | EPODONIOS | ss | `149.22.95.183:443` | 92 ms | 854 ms | - |
| 24 | EPODONIOS | vless | `15.204.97.216:23576` | 95 ms | 不可达 | - |
| 25 | EPODONIOS | vless | `172.64.150.28:2082` | 97 ms | 708 ms | - |
| 26 | EPODONIOS | vless | `172.64.150.43:8080` | 97 ms | 840 ms | - |
| 27 | EPODONIOS | vless | `15.204.97.206:23576` | 98 ms | 不可达 | - |
| 28 | EPODONIOS | vless | `15.204.97.219:23576` | 108 ms | 793 ms | - |
| 29 | US 🇺🇸 / @Raydikalx / CE19FB | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 120 ms | 669 ms | - |
| 30 | EPODONIOS | vless | `172.64.150.28:2082` | 130 ms | 729 ms | - |
| 31 | EPODONIOS | ss | `156.146.38.167:443` | 131 ms | 958 ms | - |
| 32 | EPODONIOS | ss | `173.244.56.9:443` | 131 ms | 856 ms | - |
| 33 | EPODONIOS | ss | `156.146.38.168:443` | 133 ms | 948 ms | - |
| 34 | EPODONIOS | vless | `172.64.150.28:2082` | 133 ms | 676 ms | - |
| 35 | EPODONIOS | ss | `156.146.38.170:443` | 135 ms | 957 ms | - |
| 36 | EPODONIOS | ss | `156.146.38.169:443` | 136 ms | 951 ms | - |
| 37 | EPODONIOS | vless | `15.204.97.219:23576` | 159 ms | 793 ms | - |
| 38 | EPODONIOS | ss | `173.244.56.6:443` | 163 ms | 780 ms | - |
| 39 | ⚡ b2n.ir/v2ray-configs / 417 | vless | `104.18.45.38:443` | 164 ms | 3243 ms | - |
| 40 | EPODONIOS | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 198 ms | 1279 ms | - |
| 41 | CA 🇨🇦 / @Raydikalx / 0940F6 | vmess | `23.162.200.198:18000` | 203 ms | 1582 ms | - |
| 42 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 203 ms | 1723 ms | - |
| 43 | EPODONIOS | ss | `37.19.198.243:443` | 207 ms | 1147 ms | - |
| 44 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 208 ms | 3987 ms | - |
| 45 | EPODONIOS | ss | `37.19.198.236:443` | 211 ms | 1136 ms | - |
| 46 | CA 🇨🇦 / @Raydikalx / A4F840 | vmess | `cf.877771.xyz:443` | 213 ms | 995 ms | - |
| 47 | EPODONIOS | vless | `172.64.150.28:2082` | 215 ms | 698 ms | - |
| 48 | EPODONIOS | vmess | `38.110.1.246:18000` | 225 ms | 1809 ms | - |
| 49 | EPODONIOS | ss | `37.19.198.160:443` | 225 ms | 1374 ms | - |
| 50 | EPODONIOS | ss | `193.151.163.18:19999` | 232 ms | 1138 ms | - |

> 仅展示前 50 个，共 604 个；完整列表见 `sub/nodes.txt`。
