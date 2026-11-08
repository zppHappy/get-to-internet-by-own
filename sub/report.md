# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-08 20:55:51+0800`

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
| 抓取链接 | 12607 |
| 去重后节点 | 8229 |
| TCP 预筛剔除 | 3904 |
| 真连接测试 | 8229 |
| 测试通过 | 901 |
| **最终保留** | **901** |
| 耗时 | 323.4 秒 |

> 解析阶段跳过：重复 4349、协议未启用 0、无法解析 29

## 协议分布

vless 411 · ss 207 · vmess 148 · trojan 135

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 901 个节点中，有 **737** 个能经代理访问到国内目标站，**164** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / B723A6 | vmess | `84.17.41.2:18000` | 25 ms | 不可达 | - |
| 2 | US 🇺🇸 / @Raydikalx / 98D357 | vmess | `84.17.41.2:18000` | 27 ms | 不可达 | - |
| 3 | 84.17.41.2:18000 | vmess | `84.17.41.2:18000` | 29 ms | 655 ms | - |
| 4 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 31 ms | 1048 ms | - |
| 5 | US 🇺🇸 / @Raydikalx / 964397 | vmess | `84.17.41.2:18000` | 31 ms | 3902 ms | - |
| 6 | @ConfigV2RayNG | trojan | `216.106.186.66:443` | 37 ms | 668 ms | - |
| 7 | United States | trojan | `216.106.186.33:443` | 38 ms | 761 ms | - |
| 8 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `216.106.186.82:443` | 41 ms | 663 ms | - |
| 9 | ⏳35@ConfigV2RayNG | trojan | `216.106.186.32:443` | 41 ms | 675 ms | - |
| 10 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | ss | `149.22.95.183:443` | 43 ms | 700 ms | - |
| 11 | @V2rayNGVPN > کانفیگ رایگان | trojan | `216.106.186.46:443` | 48 ms | 747 ms | - |
| 12 | United States | trojan | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | 52 ms | 745 ms | - |
| 13 | @ConfigV2RayNG | vless | `15.204.97.198:23576` | 56 ms | 不可达 | - |
| 14 | @i10VPN⁷ | vless | `15.204.97.206:23576` | 56 ms | 不可达 | - |
| 15 | @V2ray_confiig | vless | `15.204.97.216:23576` | 56 ms | 不可达 | - |
| 16 | @v2ray313 کانالمون 🌙 | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 56 ms | 693 ms | - |
| 17 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 57 ms | 983 ms | - |
| 18 | @Net2ray 🔥 | vless | `15.204.97.197:23576` | 57 ms | 不可达 | - |
| 19 | @ConfigV2RayNG | vless | `15.204.97.198:23576` | 57 ms | 不可达 | - |
| 20 | Channel : @Daily_Configs | vless | `15.204.97.219:23576` | 57 ms | 不可达 | - |
| 21 | @fastkanfig / سرور 3 | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 57 ms | 820 ms | - |
| 22 | @ConfigV2RayNG | vless | `15.204.97.198:23576` | 58 ms | 不可达 | - |
| 23 | 13 | vless | `15.204.97.206:23576` | 58 ms | 不可达 | - |
| 24 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.209:23576` | 58 ms | 不可达 | - |
| 25 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.198:23576` | 59 ms | 不可达 | - |
| 26 | Tel@MARAMBASHI 🇫🇷 | vless | `15.204.97.219:23576` | 59 ms | 不可达 | - |
| 27 | Tel@MARAMBASHI 🇸🇪 | vless | `15.204.97.197:23576` | 61 ms | 不可达 | - |
| 28 | @hopev2ray🤍 | vless | `15.204.97.197:23576` | 62 ms | 1127 ms | - |
| 29 | Tel@MARAMBASHI 🇫🇷 | vless | `15.204.97.214:23576` | 62 ms | 不可达 | - |
| 30 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 63 ms | 697 ms | - |
| 31 | 🇨🇦210110 / ⚡️Telegram = t.me/SOSkeyNET | trojan | `4okhrijuyjytflnvowhl3zfw5wsgi34o.pages.dev:443` | 70 ms | 3108 ms | - |
| 32 | >>@freeland8::US | vless | `ww13.levikogjgfdd.ir:23576` | 71 ms | 不可达 | - |
| 33 | @i10VPN³ | vless | `ww13.levikogjgfdd.ir:23576` | 73 ms | 不可达 | - |
| 34 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `137.184.89.151:19999` | 89 ms | 856 ms | - |
| 35 | @ConfigV2RayNG | ss | `169.197.142.68:19999` | 91 ms | 752 ms | - |
| 36 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `137.175.73.178:35678` | 93 ms | 900 ms | - |
| 37 | 11602@proxy_online_net | vmess | `169.197.142.22:18000` | 101 ms | 2042 ms | - |
| 38 | 🇺🇸US-23.150.152.38-0227 | ss | `23.150.152.38:19999` | 102 ms | 1109 ms | - |
| 39 | @Shh_Proxy-New⁷ | trojan | `188.114.98.0:443` | 102 ms | 1462 ms | - |
| 40 | Telegram 👉🏼 @planB_net  • 07 | trojan | `104.25.95.49:443` | 103 ms | 671 ms | - |
| 41 | @Nexus_Panell چنل تلگرام | trojan | `104.17.10.171:443` | 104 ms | 不可达 | - |
| 42 | @ConfigV2RayNG | ss | `38.145.220.193:8443` | 105 ms | 774 ms | - |
| 43 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vmess | `84.17.41.2:18000` | 108 ms | 不可达 | - |
| 44 | @ConfigV2RayNG | trojan | `167.88.61.52:443` | 117 ms | 950 ms | - |
| 45 | Telegram 👉🏼 @planB_net  • 09 | trojan | `167.88.61.193:443` | 118 ms | 741 ms | - |
| 46 | @ConfigV2RayNG | trojan | `167.88.61.52:443` | 118 ms | 753 ms | - |
| 47 | @VPNConnectd | vless | `199.232.78.159:443` | 119 ms | 1125 ms | - |
| 48 | 🔰 @ConfigV2RayNG (تلگرام) - 172 | trojan | `167.88.61.193:443` | 119 ms | 808 ms | - |
| 49 | 🇺🇸US-167.88.61.175-0149 | trojan | `167.88.61.175:443` | 119 ms | 737 ms | - |
| 50 | @ConfigV2RayNG | trojan | `167.88.61.20:443` | 121 ms | 858 ms | - |

> 仅展示前 50 个，共 901 个；完整列表见 `sub/nodes.txt`。
