# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-23 09:30:47+0800`

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
| 抓取链接 | 13064 |
| 去重后节点 | 8530 |
| TCP 预筛剔除 | 4020 |
| 真连接测试 | 8530 |
| 测试通过 | 1091 |
| **最终保留** | **1091** |
| 耗时 | 299.4 秒 |

> 解析阶段跳过：重复 4506、协议未启用 0、无法解析 28

## 协议分布

vless 523 · ss 277 · vmess 206 · trojan 85

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 1091 个节点中，有 **948** 个能经代理访问到国内目标站，**143** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | @V2ray_confiig | vless | `47.253.226.114:443` | 26 ms | 927 ms | - |
| 2 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `40.160.86.43:8388` | 26 ms | 1834 ms | - |
| 3 | @B2Hub | vless | `47.253.226.114:443` | 28 ms | 914 ms | - |
| 4 | [131512] | ss | `37.19.198.243:443` | 37 ms | 918 ms | - |
| 5 | @ConfigV2RayNG - 187 | ss | `37.19.198.160:443` | 37 ms | 1119 ms | - |
| 6 | 🇪🇺 @EXPRESSVPN_420 | ss | `193.151.163.18:19999` | 37 ms | 898 ms | - |
| 7 | ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ = @ꜰxxɴᴇᴛ🏉 | ss | `37.19.198.244:443` | 38 ms | 896 ms | - |
| 8 | 13364@proxy_online_net | ss | `37.19.198.236:443` | 38 ms | 890 ms | - |
| 9 | @VPsave | vless | `104.26.13.31:8080` | 40 ms | 1049 ms | - |
| 10 | 🇺🇸US-🚀@VPNine1 | ss | `38.91.100.39:19999` | 40 ms | 1198 ms | - |
| 11 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `45.138.100.248:10443` | 41 ms | 1346 ms | - |
| 12 | Tel@MARAMBASHI 🇧🇷 | vless | `188.114.98.0:443` | 43 ms | 936 ms | - |
| 13 | @V2ray_confiig | vless | `104.21.227.134:80` | 44 ms | 973 ms | - |
| 14 | @i10VPN² | ss | `138.197.89.234:28960` | 46 ms | 不可达 | - |
| 15 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `104.21.227.134:80` | 47 ms | 1051 ms | - |
| 16 | ⚡01 / ⚡Telegram = t.me/ex_proxies | ss | `98.98.79.198:8080` | 48 ms | 875 ms | - |
| 17 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | trojan | `69.164.240.85:50875` | 48 ms | 1726 ms | - |
| 18 | %F0%9F%87%BA%F0%9F%87%B8US_6_@Surfboardv | vmess | `67.220.85.46:18000` | 49 ms | 1349 ms | - |
| 19 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `159.89.87.21:28190` | 50 ms | 1147 ms | - |
| 20 | Tel@MARAMBASHI 🇸🇪 | vless | `159.89.87.21:28190` | 50 ms | 1150 ms | - |
| 21 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vmess | `142.202.48.87:1270` | 52 ms | 1140 ms | - |
| 22 | @V2ray_confiig | vless | `159.89.87.21:28190` | 52 ms | 1079 ms | - |
| 23 | 🇺🇸 / تلگرام: @IRJetConfig #RK | vless | `45.138.100.248:10443` | 52 ms | 1592 ms | - |
| 24 | 🇺🇲 𝐔𝐒¹ @Fear_Config | vmess | `67.220.95.3:18000` | 53 ms | 861 ms | - |
| 25 | @ConfigV2RayNG - 205 | ss | `45.86.51.18:19999` | 55 ms | 883 ms | - |
| 26 | ⚡ b2n.ir/v2ray-configs / 803 | vless | `fast-route-279ca1-gw.staging-api-c694f6.workers.dev:443` | 55 ms | 932 ms | - |
| 27 | @VPsave | vless | `indiegogo.com:443` | 56 ms | 952 ms | - |
| 28 | @ConfigV2RayNG - 224 | ss | `198.98.53.130:443` | 57 ms | 813 ms | - |
| 29 | @vasl_bashim | vmess | `67.220.95.3:18000` | 58 ms | 1208 ms | - |
| 30 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `149.40.57.134:19999` | 58 ms | 904 ms | - |
| 31 | 🇺🇸 / تلگرام: @IRJetConfig #RK | ss | `185.230.230.18:19999` | 58 ms | 873 ms | - |
| 32 | @ConfigV2RayNG - 247 | ss | `149.40.57.138:19999` | 58 ms | 1119 ms | - |
| 33 | @Nexus_Panell چنل تلگرام | ss | `149.40.57.135:19999` | 58 ms | 1267 ms | - |
| 34 | @VPsave | vless | `104.18.109.147:8080` | 60 ms | 953 ms | - |
| 35 | @VPsave | vless | `icook.tw:8080` | 60 ms | 942 ms | - |
| 36 | تو کانال نتورلد نباشید قطع میشن@networld | ss | `172.111.38.72:19999` | 61 ms | 890 ms | - |
| 37 | @v2ray313 کانالمون 💦 | vmess | `67.220.95.3:18000` | 62 ms | 1212 ms | - |
| 38 | @pass_net 1 | trojan | `66.163.122.25:443` | 63 ms | 888 ms | - |
| 39 | Channel id: ConfigV2RayNG 🇺🇸 | vmess | `67.220.95.3:18000` | 64 ms | 1086 ms | - |
| 40 | @i10VPN⁴ | trojan | `66.163.122.113:443` | 64 ms | 901 ms | - |
| 41 | @pass_net 3 | trojan | `66.163.122.30:443` | 64 ms | 892 ms | - |
| 42 | @i10VPN⁶ | trojan | `66.163.122.46:443` | 64 ms | 872 ms | - |
| 43 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `188.114.98.112:80` | 65 ms | 937 ms | - |
| 44 | @VPsave | vless | `188.114.98.112:80` | 65 ms | 1005 ms | - |
| 45 | @ConfigV2RayNG | vless | `188.114.98.5:443` | 65 ms | 939 ms | - |
| 46 | @VPsave | vless | `workers.dev:443` | 65 ms | 980 ms | - |
| 47 | Tel-@ProxyMtAlpha🐺 3 | ss | `200.102.179.179:8388` | 65 ms | 877 ms | - |
| 48 | US 🇺🇸 / @Raydikalx / BA43A3 | vmess | `67.220.85.46:18000` | 65 ms | 1505 ms | - |
| 49 | 🇺🇸US_132_@Surfboardv2ray | vless | `104.20.30.179:2096` | 66 ms | 952 ms | - |
| 50 | @i10VPN¹⁰ | trojan | `66.163.122.26:443` | 66 ms | 895 ms | - |

> 仅展示前 50 个，共 1091 个；完整列表见 `sub/nodes.txt`。
