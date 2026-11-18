# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-18 10:50:00+0800`

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
| 抓取链接 | 12839 |
| 去重后节点 | 8197 |
| TCP 预筛剔除 | 3861 |
| 真连接测试 | 8197 |
| 测试通过 | 955 |
| **最终保留** | **955** |
| 耗时 | 307.5 秒 |

> 解析阶段跳过：重复 4611、协议未启用 0、无法解析 31

## 协议分布

vless 424 · ss 235 · vmess 179 · trojan 117

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 955 个节点中，有 **825** 个能经代理访问到国内目标站，**130** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / 964397 | vmess | `84.17.41.2:18000` | 31 ms | 不可达 | - |
| 2 | US 🇺🇸 / @Raydikalx / B723A6 | vmess | `84.17.41.2:18000` | 31 ms | 不可达 | - |
| 3 | 84.17.41.2:18000 | vmess | `84.17.41.2:18000` | 38 ms | 不可达 | - |
| 4 | US 🇺🇸 / @Raydikalx / 4ABB27 | vmess | `84.17.41.2:18000` | 40 ms | 1285 ms | - |
| 5 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 41 ms | 1094 ms | - |
| 6 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.66:443` | 49 ms | 737 ms | - |
| 7 | @ConfigV2RayNG | trojan | `216.106.186.155:443` | 49 ms | 1956 ms | - |
| 8 | @ConfigV2RayNG | trojan | `216.106.186.46:443` | 50 ms | 648 ms | - |
| 9 | @ConfigV2RayNG | trojan | `216.106.186.155:443` | 51 ms | 769 ms | - |
| 10 | @ConfigV2RayNG | trojan | `216.106.186.32:443` | 56 ms | 643 ms | - |
| 11 | @ConfigV2RayNG | trojan | `216.106.186.33:443` | 56 ms | 748 ms | - |
| 12 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `216.106.186.66:443` | 56 ms | 766 ms | - |
| 13 | @ConfigV2RayNG | trojan | `216.106.186.155:443` | 57 ms | 749 ms | - |
| 14 | 12747@proxy_online_net | vless | `15.204.97.216:23576` | 58 ms | 1132 ms | - |
| 15 | @ConfigV2RayNG | trojan | `216.106.186.32:443` | 58 ms | 729 ms | - |
| 16 | @hopev2ray🩶 | vless | `15.204.97.206:23576` | 59 ms | 不可达 | - |
| 17 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `15.204.97.195:23576` | 60 ms | 1121 ms | - |
| 18 | @filembad | vless | `15.204.97.197:23576` | 61 ms | 2905 ms | - |
| 19 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 61 ms | 不可达 | - |
| 20 | @GozargahAzad/🇺🇸 | vless | `15.204.97.214:23576` | 62 ms | 不可达 | - |
| 21 | 12717@proxy_online_net | vless | `15.204.97.198:23576` | 64 ms | 1070 ms | - |
| 22 | Tel@MARAMBASHI 🇮🇹 | vless | `15.204.97.198:23576` | 64 ms | 1091 ms | - |
| 23 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `15.204.97.209:23576` | 65 ms | 1140 ms | - |
| 24 | 🇺🇲 𝐔𝐒 @Fear_Config | vless | `15.204.97.198:23576` | 67 ms | 1146 ms | - |
| 25 | @V2ray_confiig | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 68 ms | 687 ms | - |
| 26 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `15.204.97.198:23576` | 69 ms | 773 ms | - |
| 27 | @V2ray_confiig | vless | `15.204.97.216:23576` | 70 ms | 1098 ms | - |
| 28 | Telegram:@v2rayng3 | vless | `ww13.levikogjgfdd.ir:23576` | 71 ms | 不可达 | - |
| 29 | @Napsternetvirani | vless | `15.204.97.219:23576` | 73 ms | 766 ms | - |
| 30 | @V2ray_confiig | vless | `15.204.97.216:23576` | 73 ms | 1151 ms | - |
| 31 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.209:23576` | 77 ms | 760 ms | - |
| 32 | Telegram 👉🏼 @planB_net  • 10 | vless | `15.204.97.198:23576` | 77 ms | 不可达 | - |
| 33 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `15.204.97.214:23576` | 77 ms | 不可达 | - |
| 34 | ✰𝗝𝗼𝗶𝗻 ➠ @v2raymelliii✰ | vless | `15.204.97.219:23576` | 78 ms | 769 ms | - |
| 35 | @Net2ray 🔥 | vless | `15.204.97.197:23576` | 78 ms | 2797 ms | - |
| 36 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.82:443` | 82 ms | 731 ms | - |
| 37 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.33:443` | 85 ms | 735 ms | - |
| 38 | @ConfigV2RayNG | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 88 ms | 785 ms | - |
| 39 | [97903] - Telegram : @V2All | ss | `137.184.89.151:19999` | 93 ms | 880 ms | - |
| 40 | ⚜️𝗝𝗼𝗶𝗻 ➠ @tik7net_vpn | ss | `169.197.142.68:19999` | 98 ms | 740 ms | - |
| 41 | US 🇺🇸 / @Raydikalx / D17CE8 | vmess | `169.197.142.22:18000` | 100 ms | 730 ms | - |
| 42 | @Nexus_Panell چنل تلگرام | ss | `38.145.220.193:8443` | 103 ms | 776 ms | - |
| 43 | 🇭🇰 Join+Telegram:@Farah_VPN 🇭🇰 | vmess | `206.237.11.17:50376` | 104 ms | 1131 ms | - |
| 44 | Channel : @Daily_Configs | vmess | `84.17.41.2:18000` | 105 ms | 不可达 | - |
| 45 | @meliproxyy | vless | `104.27.204.44:443` | 106 ms | 986 ms | - |
| 46 | @ConfigV2RayNG | vless | `172.64.144.240:443` | 108 ms | 719 ms | - |
| 47 | 🇺🇸US-23.150.152.38-0110 | ss | `23.150.152.38:19999` | 110 ms | 不可达 | - |
| 48 | @Nexus_Panell چنل تلگرام | trojan | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | 110 ms | 790 ms | - |
| 49 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `188.114.98.112:80` | 113 ms | 1017 ms | - |
| 50 | 🇸🇬 Join+Telegram:@Farah_VPN 🇸🇬 | vless | `172.67.65.56:2053` | 116 ms | 673 ms | - |

> 仅展示前 50 个，共 955 个；完整列表见 `sub/nodes.txt`。
