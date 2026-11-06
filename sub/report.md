# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-06 09:28:29+0800`

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
| 抓取链接 | 13135 |
| 去重后节点 | 8151 |
| TCP 预筛剔除 | 3773 |
| 真连接测试 | 8151 |
| 测试通过 | 941 |
| **最终保留** | **941** |
| 耗时 | 308.8 秒 |

> 解析阶段跳过：重复 4957、协议未启用 0、无法解析 27

## 协议分布

vless 477 · ss 176 · vmess 172 · trojan 116

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 941 个节点中，有 **823** 个能经代理访问到国内目标站，**118** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 27 ms | 4351 ms | - |
| 2 | US 🇺🇸 / @Raydikalx / 98D357 | vmess | `84.17.41.2:18000` | 29 ms | 不可达 | - |
| 3 | 84.17.41.2:18000 | vmess | `84.17.41.2:18000` | 30 ms | 920 ms | - |
| 4 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 31 ms | 949 ms | - |
| 5 | US 🇺🇸 / @Raydikalx / B723A6 | vmess | `84.17.41.2:18000` | 37 ms | 不可达 | - |
| 6 | United States | trojan | `216.106.186.32:443` | 42 ms | 656 ms | - |
| 7 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | ss | `149.22.95.183:443` | 49 ms | 761 ms | - |
| 8 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.82:443` | 51 ms | 677 ms | - |
| 9 | Telegram 👉🏼 @planB_net  • 10 | vless | `15.204.97.219:23576` | 59 ms | 1497 ms | - |
| 10 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 60 ms | 不可达 | - |
| 11 | Channel : @Daily_Configs | vless | `15.204.97.219:23576` | 60 ms | 不可达 | - |
| 12 | @filembad | vless | `15.204.97.214:23576` | 61 ms | 不可达 | - |
| 13 | @pass_net🎃🕸️🎃 | vless | `15.204.97.216:23576` | 61 ms | 不可达 | - |
| 14 | @ConfigV2RayNG | vless | `15.204.97.197:23576` | 64 ms | 不可达 | - |
| 15 | Telegram 👉🏼 @planB_net  • 02 | vless | `15.204.97.216:23576` | 65 ms | 不可达 | - |
| 16 | @FXxNET⚡️ | vless | `15.204.97.198:23576` | 66 ms | 1490 ms | - |
| 17 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.198:23576` | 66 ms | 不可达 | - |
| 18 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.214:23576` | 66 ms | 不可达 | - |
| 19 | @Net2ray 🔥 | vless | `15.204.97.197:23576` | 69 ms | 不可达 | - |
| 20 | 11994@proxy_online_net | vless | `15.204.97.197:23576` | 69 ms | 不可达 | - |
| 21 | Channel : @Daily_Configs | vless | `15.204.97.206:23576` | 70 ms | 不可达 | - |
| 22 | @i10VPN⁷ | vless | `15.204.97.206:23576` | 70 ms | 不可达 | - |
| 23 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.195:23576` | 73 ms | 不可达 | - |
| 24 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.209:23576` | 73 ms | 不可达 | - |
| 25 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 73 ms | 799 ms | - |
| 26 | @meliproxyy | vless | `chat.openai.com:8880` | 74 ms | 629 ms | - |
| 27 | Tel@MARAMBASHI 🇺🇸 | vless | `15.204.97.219:23576` | 75 ms | 1135 ms | - |
| 28 | United States | trojan | `www.findlocaljobnetworkandbuildcommunityconnections.com:443` | 77 ms | 666 ms | - |
| 29 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.33:443` | 79 ms | 681 ms | - |
| 30 | @v2ray313 کانالمون 🌙 | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 82 ms | 671 ms | - |
| 31 | ⚡ b2n.ir/v2ray-configs / 305 | vless | `188.114.97.3:443` | 91 ms | 687 ms | - |
| 32 | @Tarkshodeh 🇺🇲 | vless | `chat.openai.com:8880` | 94 ms | 899 ms | - |
| 33 | US 🇺🇸 / @Raydikalx / 4D7399 | vmess | `169.197.142.22:18000` | 97 ms | 1020 ms | - |
| 34 | US 🇺🇸 / @Raydikalx / B79C28 | vmess | `169.197.142.22:18000` | 97 ms | 1298 ms | - |
| 35 | [132144] | vless | `104.26.4.57:2087` | 101 ms | 671 ms | - |
| 36 | @IRAN_V2PING | vless | `www.speedtest.net:443` | 101 ms | 650 ms | - |
| 37 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 105 ms | 1215 ms | - |
| 38 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `8.34.70.30:8880` | 107 ms | 1106 ms | - |
| 39 | @Tarkshodeh 🇺🇲 | vless | `154.197.75.40:8880` | 108 ms | 771 ms | - |
| 40 | @VPsave | trojan | `208.103.161.16:2096` | 110 ms | 1812 ms | - |
| 41 | @FXxNET⚡️ | vless | `188.114.97.3:443` | 116 ms | 685 ms | - |
| 42 | @fastkanfig / سرور 3 | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 116 ms | 691 ms | - |
| 43 | 11871@proxy_online_net | ss | `49.51.39.148:443` | 119 ms | 721 ms | - |
| 44 | @Tarkshodeh 🇺🇲 | vless | `154.197.64.30:8880` | 120 ms | 657 ms | - |
| 45 | United States | trojan | `167.88.61.198:443` | 124 ms | 757 ms | - |
| 46 | ✰𝗝𝗼𝗶𝗻 ➠ @v2raymelliii✰ | trojan | `167.88.61.20:443` | 124 ms | 762 ms | - |
| 47 | ⏳41@ConfigV2RayNG | trojan | `167.88.61.85:443` | 124 ms | 762 ms | - |
| 48 | @VPNConnectd | trojan | `167.88.61.193:443` | 125 ms | 741 ms | - |
| 49 | 🇺🇸US-167.88.61.52-0166 | trojan | `167.88.61.52:443` | 125 ms | 769 ms | - |
| 50 | Fast Deploy Your Own Worker For Creation | vless | `medium.com:443` | 126 ms | 672 ms | - |

> 仅展示前 50 个，共 941 个；完整列表见 `sub/nodes.txt`。
