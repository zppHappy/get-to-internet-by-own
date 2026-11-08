# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-09 03:27:37+0800`

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
| 抓取链接 | 12599 |
| 去重后节点 | 8215 |
| TCP 预筛剔除 | 3908 |
| 真连接测试 | 8215 |
| 测试通过 | 848 |
| **最终保留** | **848** |
| 耗时 | 331.6 秒 |

> 解析阶段跳过：重复 4357、协议未启用 0、无法解析 27

## 协议分布

vless 378 · ss 203 · vmess 145 · trojan 122

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 848 个节点中，有 **705** 个能经代理访问到国内目标站，**143** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | 84.17.41.2:18000 | vmess | `84.17.41.2:18000` | 30 ms | 不可达 | - |
| 2 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 30 ms | 不可达 | - |
| 3 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 31 ms | 不可达 | - |
| 4 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 31 ms | 不可达 | - |
| 5 | US 🇺🇸 / @Raydikalx / 964397 | vmess | `84.17.41.2:18000` | 36 ms | 不可达 | - |
| 6 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | ss | `149.22.95.183:443` | 48 ms | 776 ms | - |
| 7 | ⏳35@ConfigV2RayNG | trojan | `216.106.186.32:443` | 57 ms | 703 ms | - |
| 8 | @V2ray_confiig | vless | `15.204.97.216:23576` | 58 ms | 不可达 | - |
| 9 | @i10VPN⁷ | vless | `15.204.97.206:23576` | 61 ms | 936 ms | - |
| 10 | 13 | vless | `15.204.97.206:23576` | 61 ms | 1706 ms | - |
| 11 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.198:23576` | 61 ms | 不可达 | - |
| 12 | @ConfigV2RayNG | vless | `15.204.97.198:23576` | 61 ms | 不可达 | - |
| 13 | @ConfigV2RayNG | vless | `15.204.97.198:23576` | 62 ms | 不可达 | - |
| 14 | @ConfigV2RayNG | trojan | `216.106.186.46:443` | 62 ms | 654 ms | - |
| 15 | 🇺🇸210349 / ⚡️Telegram = t.me/SOSkeyNET | vless | `15.204.97.214:23576` | 63 ms | 不可达 | - |
| 16 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.214:23576` | 63 ms | 不可达 | - |
| 17 | Tel@MARAMBASHI 🇫🇷 | vless | `15.204.97.219:23576` | 63 ms | 不可达 | - |
| 18 | @FXxNET⚡️ | trojan | `216.106.186.32:443` | 63 ms | 761 ms | - |
| 19 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `216.106.186.82:443` | 63 ms | 941 ms | - |
| 20 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 65 ms | 不可达 | - |
| 21 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.209:23576` | 74 ms | 1035 ms | - |
| 22 | @FXxNET⚡️ | vless | `15.204.97.219:23576` | 74 ms | 不可达 | - |
| 23 | @ConfigV2RayNG | trojan | `216.106.186.66:443` | 75 ms | 1103 ms | - |
| 24 | >>@freeland8::US | vless | `ww13.levikogjgfdd.ir:23576` | 90 ms | 不可达 | - |
| 25 | @fastkanfig / سرور 3 | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 92 ms | 797 ms | - |
| 26 | @ConfigV2RayNG | ss | `169.197.142.68:19999` | 94 ms | 875 ms | - |
| 27 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `137.175.73.178:35678` | 96 ms | 933 ms | - |
| 28 | United States | trojan | `216.106.186.33:443` | 98 ms | 665 ms | - |
| 29 | US 🇺🇸 / @Raydikalx / D17CE8 | vmess | `169.197.142.22:18000` | 101 ms | 890 ms | - |
| 30 | United States | trojan | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | 106 ms | 1061 ms | - |
| 31 | 11602@proxy_online_net | vmess | `169.197.142.22:18000` | 111 ms | 887 ms | - |
| 32 | @Nexus_Panell چنل تلگرام | trojan | `104.17.10.171:443` | 111 ms | 1646 ms | - |
| 33 | @Shh_Proxy-New⁷ | trojan | `188.114.98.0:443` | 117 ms | 764 ms | - |
| 34 | @VPNConnectd | trojan | `104.25.95.49:443` | 118 ms | 710 ms | - |
| 35 | 🇪🇺  @EXPRESSVPN_420 | ss | `95.215.201.18:19999` | 123 ms | 851 ms | - |
| 36 | @ConfigV2RayNG | ss | `38.145.220.193:8443` | 125 ms | 747 ms | - |
| 37 | Telegram 👉🏼 @planB_net  • 09 | trojan | `167.88.61.193:443` | 128 ms | 779 ms | - |
| 38 | 🔰 @ConfigV2RayNG (تلگرام) - 172 | trojan | `167.88.61.193:443` | 131 ms | 741 ms | - |
| 39 | United States | trojan | `167.88.61.198:443` | 131 ms | 942 ms | - |
| 40 | @ConfigV2RayNG | trojan | `167.88.61.52:443` | 131 ms | 757 ms | - |
| 41 | @V2rayNGVPN > کانفیگ رایگان | trojan | `104.25.95.49:443` | 132 ms | 1302 ms | - |
| 42 | US 🇺🇸 / @Raydikalx / A46964 | vmess | `169.197.142.68:1270` | 132 ms | 1147 ms | - |
| 43 | @VPNConnectd | vless | `199.232.78.159:443` | 133 ms | 851 ms | - |
| 44 | ⏳41@ConfigV2RayNG | trojan | `167.88.61.85:443` | 133 ms | 733 ms | - |
| 45 | @FXxNET⚡️ | trojan | `167.88.61.193:443` | 134 ms | 770 ms | - |
| 46 | Tel@MARAMBASHI 🇫🇷 | trojan | `167.88.61.52:443` | 134 ms | 769 ms | - |
| 47 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `47.251.108.158:443` | 136 ms | 783 ms | - |
| 48 | 🇺🇸US-173.244.56.6-0208 | ss | `173.244.56.6:443` | 137 ms | 867 ms | - |
| 49 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `173.244.56.9:443` | 139 ms | 837 ms | - |
| 50 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `167.88.62.203:19999` | 139 ms | 964 ms | - |

> 仅展示前 50 个，共 848 个；完整列表见 `sub/nodes.txt`。
