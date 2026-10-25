# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-26 04:32:06+0800`

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
| 抓取链接 | 20407 |
| 去重后节点 | 8145 |
| TCP 预筛剔除 | 3869 |
| 真连接测试 | 8145 |
| 测试通过 | 660 |
| **最终保留** | **660** |
| 耗时 | 328.3 秒 |

> 解析阶段跳过：重复 12234、协议未启用 0、无法解析 28

## 协议分布

vless 338 · ss 142 · vmess 122 · trojan 53 · hysteria2 5

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 660 个节点中，有 **530** 个能经代理访问到国内目标站，**130** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / FC15CE | vmess | `84.17.41.2:18000` | 31 ms | 1151 ms | - |
| 2 | EPODONIOS | vmess | `84.17.41.2:18000` | 32 ms | 1140 ms | - |
| 3 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 44 ms | 不可达 | - |
| 4 | EPODONIOS | vless | `15.204.97.219:23576` | 60 ms | 不可达 | - |
| 5 | EPODONIOS | vless | `15.204.97.197:23576` | 63 ms | 不可达 | - |
| 6 | EPODONIOS | vless | `15.204.97.219:23576` | 64 ms | 不可达 | - |
| 7 | EPODONIOS | vless | `15.204.97.216:23576` | 65 ms | 不可达 | - |
| 8 | EPODONIOS | vless | `15.204.97.206:23576` | 67 ms | 不可达 | - |
| 9 | EPODONIOS | vless | `15.204.97.214:23576` | 68 ms | 937 ms | - |
| 10 | EPODONIOS | vless | `15.204.97.198:23576` | 69 ms | 不可达 | - |
| 11 | EPODONIOS | ss | `149.22.95.183:443` | 71 ms | 761 ms | - |
| 12 | EPODONIOS | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 77 ms | 758 ms | - |
| 13 | EPODONIOS | vless | `cf.877774.xyz:443` | 77 ms | 696 ms | - |
| 14 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 82 ms | 不可达 | - |
| 15 | EPODONIOS | vless | `172.64.150.28:2082` | 82 ms | 809 ms | - |
| 16 | EPODONIOS | vless | `15.204.97.206:23576` | 88 ms | 不可达 | - |
| 17 | ⚡ b2n.ir/v2ray-configs / 425 | vless | `8.47.69.60:443` | 90 ms | 641 ms | - |
| 18 | EPODONIOS | vless | `172.64.158.170:443` | 92 ms | 842 ms | - |
| 19 | US 🇺🇸 / @Raydikalx / B79C28 | vmess | `169.197.142.22:18000` | 96 ms | 不可达 | - |
| 20 | ⚡ b2n.ir/v2ray-configs / 121 | vless | `88.216.69.253:443` | 97 ms | 857 ms | - |
| 21 | EPODONIOS | vless | `172.64.150.28:2082` | 100 ms | 620 ms | - |
| 22 | ⚡ b2n.ir/v2ray-configs / 832 | vless | `104.21.221.158:443` | 109 ms | 854 ms | - |
| 23 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 111 ms | 1125 ms | - |
| 24 | EPODONIOS | vless | `cf.877774.xyz:443` | 117 ms | 655 ms | - |
| 25 | EPODONIOS | vless | `51.81.203.63:443` | 119 ms | 1530 ms | - |
| 26 | EPODONIOS | vmess | `169.197.142.22:18000` | 119 ms | 884 ms | - |
| 27 | EPODONIOS | vless | `172.64.152.241:443` | 123 ms | 661 ms | - |
| 28 | EPODONIOS | vless | `172.66.0.162:443` | 123 ms | 649 ms | - |
| 29 | EPODONIOS | ss | `95.215.201.18:19999` | 134 ms | 1065 ms | - |
| 30 | EPODONIOS | ss | `173.244.56.6:443` | 145 ms | 858 ms | - |
| 31 | EPODONIOS | vless | `195.123.240.65:443` | 154 ms | 836 ms | - |
| 32 | EPODONIOS | ss | `156.146.38.169:443` | 159 ms | 1014 ms | - |
| 33 | EPODONIOS | vmess | `129.146.77.248:39495` | 166 ms | 1642 ms | - |
| 34 | EPODONIOS | ss | `156.146.38.168:443` | 167 ms | 980 ms | - |
| 35 | EPODONIOS | vless | `172.64.150.28:2082` | 171 ms | 684 ms | - |
| 36 | EPODONIOS | ss | `156.146.38.170:443` | 172 ms | 985 ms | - |
| 37 | CA 🇨🇦 / @Raydikalx / F25C32 | vmess | `104.17.147.222:80` | 179 ms | 998 ms | - |
| 38 | EPODONIOS | ss | `156.146.38.167:443` | 180 ms | 984 ms | - |
| 39 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 202 ms | 1606 ms | - |
| 40 | @VPsave | vmess | `cf.0sm.com:443` | 203 ms | 1161 ms | - |
| 41 | EPODONIOS | ss | `37.19.198.243:443` | 206 ms | 1153 ms | - |
| 42 | @VPsave | vmess | `cf.090227.xyz:443` | 209 ms | 1001 ms | - |
| 43 | EPODONIOS | ss | `37.19.198.160:443` | 210 ms | 1146 ms | - |
| 44 | EPODONIOS | ss | `37.19.198.236:443` | 212 ms | 1296 ms | - |
| 45 | EPODONIOS | ss | `37.19.198.244:443` | 213 ms | 1119 ms | - |
| 46 | EPODONIOS | vless | `172.64.150.28:2082` | 220 ms | 662 ms | - |
| 47 | CA 🇨🇦 / @Raydikalx / C6C15A | vmess | `cf.090227.xyz:443` | 223 ms | 1001 ms | - |
| 48 | EPODONIOS | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 228 ms | 754 ms | - |
| 49 | US 🇺🇸 / @Raydikalx / DE08A7 | vmess | `67.220.95.3:18000` | 233 ms | 1664 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / 7C97A1 | vmess | `104.21.7.133:80` | 234 ms | 1034 ms | - |

> 仅展示前 50 个，共 660 个；完整列表见 `sub/nodes.txt`。
