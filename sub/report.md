# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-25 04:04:08+0800`

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
| 抓取链接 | 12590 |
| 去重后节点 | 8217 |
| TCP 预筛剔除 | 4024 |
| 真连接测试 | 8217 |
| 测试通过 | 817 |
| **最终保留** | **817** |
| 耗时 | 334.8 秒 |

> 解析阶段跳过：重复 4348、协议未启用 0、无法解析 25

## 协议分布

vless 382 · ss 242 · vmess 141 · trojan 52

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 817 个节点中，有 **610** 个能经代理访问到国内目标站，**207** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `169.197.142.68:19999` | 32 ms | 1045 ms | - |
| 2 | @vmesskhodam | vmess | `169.197.142.22:18000` | 37 ms | 1126 ms | - |
| 3 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vmess | `169.197.142.22:18000` | 42 ms | 928 ms | - |
| 4 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `panel.apexkey.store:2053` | 42 ms | 681 ms | - |
| 5 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `104.238.140.45:11051` | 43 ms | 641 ms | - |
| 6 | US 🇺🇸 / @Raydikalx / D17CE8 | vmess | `169.197.142.22:18000` | 44 ms | 1148 ms | - |
| 7 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 44 ms | 784 ms | - |
| 8 | 🇺🇸US-23.150.152.38-0172 | ss | `23.150.152.38:19999` | 45 ms | 不可达 | - |
| 9 | @pass_net 3 | trojan | `167.88.61.175:443` | 49 ms | 671 ms | - |
| 10 | US 🇺🇸 / @Raydikalx / 481678 | vmess | `23.150.152.65:1270` | 55 ms | 915 ms | - |
| 11 | 🇸🇬 Join+Telegram:@Farah_VPN 🇸🇬 | vless | `172.64.154.113:8443` | 67 ms | 733 ms | - |
| 12 | US 🇺🇸 / @Raydikalx / 8C331C | vmess | `129.146.143.80:48111` | 67 ms | 不可达 | - |
| 13 | 📗92@oneclickvpnkeys | vless | `172.236.231.45:443` | 68 ms | 828 ms | - |
| 14 | 84.17.41.2:18000 | vmess | `84.17.41.2:18000` | 70 ms | 1080 ms | - |
| 15 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `172.64.154.113:8443` | 70 ms | 752 ms | - |
| 16 | Tel@MARAMBASHI 🇧🇷 | vless | `172.64.154.113:8443` | 75 ms | 730 ms | - |
| 17 | @VPNConnectd | vless | `172.64.154.113:8443` | 77 ms | 699 ms | - |
| 18 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 77 ms | 1234 ms | - |
| 19 | Telegram 👉🏼 @planB_net  • 07 | vless | `216.106.185.158:443` | 78 ms | 944 ms | - |
| 20 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `199.7.140.201:443` | 79 ms | 881 ms | - |
| 21 | 13375@proxy_online_net | ss | `173.244.56.6:443` | 80 ms | 790 ms | - |
| 22 | Channel : @Daily_Configs | vless | `172.64.154.113:8443` | 81 ms | 728 ms | - |
| 23 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 81 ms | 1727 ms | - |
| 24 | @VPsave | ss | `38.143.66.146:19999` | 82 ms | 不可达 | - |
| 25 | Tel@MARAMBASHI 🇧🇷 | ss | `173.244.56.9:443` | 83 ms | 745 ms | - |
| 26 | @hopev2ray🩶 | vless | `15.204.97.206:23576` | 85 ms | 不可达 | - |
| 27 | 🇺🇸US_66_@Surfboardv2ray | vless | `15.204.97.209:23576` | 86 ms | 不可达 | - |
| 28 | @V2ray_confiig | vless | `15.204.97.195:23576` | 87 ms | 不可达 | - |
| 29 | 🇺🇲 𝐔𝐒 @Fear_Config | vless | `15.204.97.198:23576` | 87 ms | 不可达 | - |
| 30 | US 🇺🇸 / @Raydikalx / 4ABB27 | vmess | `84.17.41.2:18000` | 87 ms | 1030 ms | - |
| 31 | @hopev2ray🤍 | vless | `15.204.97.197:23576` | 88 ms | 1326 ms | - |
| 32 | Tel@MARAMBASHI 🇮🇹 | vless | `15.204.97.216:23576` | 88 ms | 不可达 | - |
| 33 | 🇺🇸229699 / ⚡️Telegram = t.me/SOSkeyNET | vless | `15.204.97.219:23576` | 88 ms | 不可达 | - |
| 34 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `147.224.54.25:2053` | 88 ms | 658 ms | - |
| 35 | @FarazV2ray | vless | `15.204.97.216:23576` | 89 ms | 804 ms | - |
| 36 | Channel : @Daily_Configs | vless | `15.204.97.195:23576` | 89 ms | 不可达 | - |
| 37 | vpnbaz | vless | `15.204.97.198:23576` | 89 ms | 不可达 | - |
| 38 | @V2ray_confiig | vless | `15.204.97.214:23576` | 89 ms | 不可达 | - |
| 39 | @VPNConnectd | vless | `188.114.98.0:443` | 89 ms | 686 ms | - |
| 40 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 90 ms | 不可达 | - |
| 41 | @V2ray_confiig | vless | `15.204.97.214:23576` | 94 ms | 不可达 | - |
| 42 | 🇺🇸US_46_@Surfboardv2ray | vless | `15.204.97.214:23576` | 96 ms | 不可达 | - |
| 43 | 🇺🇸US_75_@Surfboardv2ray | vless | `15.204.97.209:23576` | 98 ms | 不可达 | - |
| 44 | 🇺🇸US_76_@Surfboardv2ray | vless | `15.204.97.214:23576` | 98 ms | 不可达 | - |
| 45 | Tel@MARAMBASHI 🇮🇹 | vless | `188.114.98.0:443` | 99 ms | 1426 ms | - |
| 46 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 100 ms | 1118 ms | - |
| 47 | Tel@MARAMBASHI 🇸🇪 | vless | `15.204.97.214:23576` | 100 ms | 不可达 | - |
| 48 | تو کانال نتورلد نباشید قطع میشن@networld | ss | `149.22.95.183:443` | 100 ms | 744 ms | - |
| 49 | kurdconfig | vless | `15.204.97.195:23576` | 101 ms | 不可达 | - |
| 50 | Telegram:@v2rayng3 | vless | `ww13.levikogjgfdd.ir:23576` | 101 ms | 不可达 | - |

> 仅展示前 50 个，共 817 个；完整列表见 `sub/nodes.txt`。
