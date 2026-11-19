# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-19 10:23:33+0800`

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
| 抓取链接 | 12961 |
| 去重后节点 | 8324 |
| TCP 预筛剔除 | 3975 |
| 真连接测试 | 8324 |
| 测试通过 | 1023 |
| **最终保留** | **1023** |
| 耗时 | 310.7 秒 |

> 解析阶段跳过：重复 4608、协议未启用 0、无法解析 29

## 协议分布

vless 459 · ss 262 · vmess 172 · trojan 130

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 1023 个节点中，有 **865** 个能经代理访问到国内目标站，**158** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `137.184.89.151:19999` | 29 ms | 790 ms | - |
| 2 | ⚜️𝗝𝗼𝗶𝗻 ➠ @tik7net_vpn | ss | `169.197.142.68:19999` | 31 ms | 643 ms | - |
| 3 | US 🇺🇸 / @Raydikalx / A46964 | vmess | `169.197.142.68:1270` | 38 ms | 648 ms | - |
| 4 | @cnetvpn 🇹🇷 | trojan | `167.88.61.20:443` | 39 ms | 652 ms | - |
| 5 | @ConfigV2RayNG | trojan | `167.88.61.52:443` | 45 ms | 645 ms | - |
| 6 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `104.21.227.134:80` | 51 ms | 721 ms | - |
| 7 | @Nexus_Panell چنل تلگرام | ss | `38.145.220.193:8443` | 59 ms | 703 ms | - |
| 8 | 🇺🇸US-23.150.152.38-0125 | ss | `23.150.152.38:19999` | 65 ms | 956 ms | - |
| 9 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vmess | `129.146.143.80:48111` | 68 ms | 768 ms | - |
| 10 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 70 ms | 1163 ms | - |
| 11 | ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ = @ꜰxxɴᴇᴛ🍉 | vless | `45.32.70.42:443` | 71 ms | 859 ms | - |
| 12 | ⚡04 / ⚡Telegram = t.me/ex_proxies | vless | `45.63.53.81:443` | 71 ms | 828 ms | - |
| 13 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `188.114.98.112:80` | 72 ms | 795 ms | - |
| 14 | 🇺🇸218763 / ⚡️Telegram = t.me/SOSkeyNET | vless | `172.235.49.52:443` | 73 ms | 726 ms | - |
| 15 | @sora1co | vless | `188.114.97.6:443` | 75 ms | 771 ms | - |
| 16 | @networld_vpn | vmess | `129.146.143.80:48111` | 76 ms | 772 ms | - |
| 17 | @V2rayNPVTConfig | ss | `173.244.56.9:443` | 80 ms | 791 ms | - |
| 18 | 🇺🇸218762 / ⚡️Telegram = t.me/SOSkeyNET | vless | `172.233.129.187:443` | 81 ms | 779 ms | - |
| 19 | @vmesskhodam | vless | `15.204.97.214:23576` | 87 ms | 不可达 | - |
| 20 | 🧬96@oneclickvpnkeys | vless | `45.76.172.197:443` | 87 ms | 678 ms | - |
| 21 | @hopev2ray🤍 | vless | `15.204.97.197:23576` | 88 ms | 2947 ms | - |
| 22 | @hopev2ray🩶 | vless | `15.204.97.206:23576` | 88 ms | 不可达 | - |
| 23 | 🇺🇸03 / ⚡Telegram = t.me/ex_proxies | vmess | `84.17.41.2:18000` | 89 ms | 954 ms | - |
| 24 | 12966@proxy_online_net | vless | `15.204.97.195:23576` | 89 ms | 不可达 | - |
| 25 | @Tarkshodeh 🇨🇵 | vless | `188.114.96.9:443` | 92 ms | 1354 ms | - |
| 26 | Channel : @Daily_Configs | vless | `15.204.97.195:23576` | 95 ms | 不可达 | - |
| 27 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `ww13.levikogjgfdd.ir:23576` | 95 ms | 不可达 | - |
| 28 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.209:23576` | 96 ms | 不可达 | - |
| 29 | @Net2ray 🔥 | vless | `15.204.97.197:23576` | 97 ms | 2591 ms | - |
| 30 | TEL;Father_vpn | vless | `188.114.97.6:443` | 97 ms | 950 ms | - |
| 31 | 🇺🇸US_104_@Surfboardv2ray | vless | `15.204.97.195:23576` | 98 ms | 不可达 | - |
| 32 | @TEHRANARGO | vless | `15.204.97.198:23576` | 98 ms | 不可达 | - |
| 33 | @V2ray_confiig | vless | `15.204.97.216:23576` | 98 ms | 不可达 | - |
| 34 | @Napsternetvirani | vless | `15.204.97.219:23576` | 98 ms | 不可达 | - |
| 35 | TEL;Father_vpn | vless | `188.114.97.6:443` | 98 ms | 726 ms | - |
| 36 | 🇺🇸218618 / ⚡️Telegram = t.me/SOSkeyNET | ss | `173.244.56.6:443` | 98 ms | 804 ms | - |
| 37 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `95.215.201.18:19999` | 98 ms | 760 ms | - |
| 38 | 🇺🇸218607 / ⚡️Telegram = t.me/SOSkeyNET | vless | `15.204.97.198:23576` | 99 ms | 不可达 | - |
| 39 | @hopev2ray🤎 | vless | `15.204.97.206:23576` | 101 ms | 不可达 | - |
| 40 | @V2rayNPVTConfig | vless | `15.204.97.214:23576` | 101 ms | 不可达 | - |
| 41 | ✰𝗝𝗼𝗶𝗻 ➠ @v2raymelliii✰ | vless | `15.204.97.219:23576` | 101 ms | 不可达 | - |
| 42 | >>@freeland8::US | vless | `ww13.levikogjgfdd.ir:23576` | 101 ms | 不可达 | - |
| 43 | @Nexus_Panell چنل تلگرام | trojan | `216.106.186.82:443` | 101 ms | 819 ms | - |
| 44 | تو کانال نتورلد نباشید قطع میشن
@networl | vmess | `169.197.142.22:18000` | 102 ms | 1364 ms | - |
| 45 | 12980@proxy_online_net | vless | `15.204.97.214:23576` | 102 ms | 不可达 | - |
| 46 | @ConfigV2RayNG | trojan | `104.20.26.192:2053` | 102 ms | 1011 ms | - |
| 47 | @fastkanfig / سرور 4 | trojan | `66.163.112.121:443` | 103 ms | 812 ms | - |
| 48 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vmess | `84.17.41.2:18000` | 104 ms | 1223 ms | - |
| 49 | 🇺🇸218761 / ⚡️Telegram = t.me/SOSkeyNET | vless | `172.235.63.167:443` | 104 ms | 711 ms | - |
| 50 | @ConfigV2RayNG | trojan | `216.106.186.46:443` | 104 ms | 824 ms | - |

> 仅展示前 50 个，共 1023 个；完整列表见 `sub/nodes.txt`。
