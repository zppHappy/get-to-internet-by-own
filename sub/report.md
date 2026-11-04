# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-04 09:09:26+0800`

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
| 抓取链接 | 13032 |
| 去重后节点 | 8210 |
| TCP 预筛剔除 | 3718 |
| 真连接测试 | 8210 |
| 测试通过 | 1049 |
| **最终保留** | **1049** |
| 耗时 | 300.2 秒 |

> 解析阶段跳过：重复 4794、协议未启用 0、无法解析 28

## 协议分布

vless 582 · ss 197 · vmess 158 · trojan 112

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 1049 个节点中，有 **918** 个能经代理访问到国内目标站，**131** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | 🇺🇸US-138.199.42.68-6035 | ss | `138.199.42.68:8080` | 25 ms | 1134 ms | - |
| 2 | @V2rayng_market_1378_bot | trojan | `216.152.155.59:443` | 34 ms | 794 ms | - |
| 3 | @i10VPN¹⁰ | trojan | `216.152.155.131:443` | 39 ms | 818 ms | - |
| 4 | 🍪99@oneclickvpnkeys | trojan | `216.152.155.59:443` | 46 ms | 790 ms | - |
| 5 | @i10VPN⁶ | trojan | `216.152.155.176:443` | 48 ms | 997 ms | - |
| 6 | @v2ray313 کانالمون 💚 | trojan | `216.152.155.158:443` | 48 ms | 1673 ms | - |
| 7 | @ConfigV2RayNG | trojan | `216.152.155.23:443` | 54 ms | 788 ms | - |
| 8 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `216.152.155.54:443` | 57 ms | 784 ms | - |
| 9 | Tel@MARAMBASHI 🇸🇪 | vless | `172.64.153.153:443` | 65 ms | 951 ms | - |
| 10 | CA 🇨🇦 / @Raydikalx / 22A83C | vmess | `104.21.7.133:80` | 67 ms | 816 ms | - |
| 11 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `104.25.238.196:443` | 70 ms | 961 ms | - |
| 12 | @pass_net🎃🕸️🎃 | ss | `193.151.163.18:19999` | 72 ms | 939 ms | - |
| 13 | CA 🇨🇦 / @Raydikalx / F25C32 | vmess | `104.17.147.222:80` | 72 ms | 816 ms | - |
| 14 | US 🇺🇸 / @Raydikalx / F2583B | vmess | `67.220.85.46:18000` | 72 ms | 1535 ms | - |
| 15 | Tel@MARAMBASHI 🇸🇪 | vless | `104.21.221.158:443` | 75 ms | 902 ms | - |
| 16 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `37.19.198.236:443` | 75 ms | 1013 ms | - |
| 17 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `104.18.35.15:443` | 76 ms | 909 ms | - |
| 18 | @FarazV2ray | vless | `172.67.76.40:443` | 76 ms | 961 ms | - |
| 19 | @FXxNET⚡️ | vless | `88.216.69.253:443` | 76 ms | 894 ms | - |
| 20 | 156.146.38.168:443 | ss | `156.146.38.168:443` | 76 ms | 846 ms | - |
| 21 | kurdconfig | vless | `104.27.74.207:443` | 77 ms | 936 ms | - |
| 22 | @Capoit | vless | `172.64.152.241:443` | 77 ms | 1112 ms | - |
| 23 | @Tarkshodeh 🇧🇲 | ss | `156.146.38.167:443` | 77 ms | 877 ms | - |
| 24 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `156.146.38.170:443` | 77 ms | 881 ms | - |
| 25 | @VPsave | vmess | `cf.0sm.com:80` | 78 ms | 855 ms | - |
| 26 | 11598@proxy_online_net | vmess | `67.220.85.46:18000` | 78 ms | 1200 ms | - |
| 27 | @i10VPN⁶ | ss | `198.98.53.130:443` | 78 ms | 824 ms | - |
| 28 | 67.220.85.46:18000 | vmess | `67.220.85.46:18000` | 79 ms | 1121 ms | - |
| 29 | 11599@proxy_online_net | vmess | `23.162.200.198:18000` | 79 ms | 1435 ms | - |
| 30 | @hex_proxy ² | vless | `104.17.154.123:443` | 79 ms | 1149 ms | - |
| 31 | @FarazV2ray | vless | `104.18.40.100:443` | 79 ms | 999 ms | - |
| 32 | @hex_proxy ³ | vless | `104.18.37.127:443` | 80 ms | 948 ms | - |
| 33 | Channel : @Daily_Configs | vless | `104.21.221.158:443` | 80 ms | 926 ms | - |
| 34 | @FarazV2ray | vless | `104.26.4.2:443` | 80 ms | 938 ms | - |
| 35 | @ConfigV2RayNG | vless | `104.26.4.2:443` | 80 ms | 991 ms | - |
| 36 | US 🇺🇸 / @Raydikalx / C88267 | vmess | `67.220.85.46:18000` | 81 ms | 1179 ms | - |
| 37 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `104.20.61.103:443` | 82 ms | 886 ms | - |
| 38 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `104.18.40.100:443` | 83 ms | 999 ms | - |
| 39 | 🇺🇸US-37.19.198.160-0144 | ss | `37.19.198.160:443` | 83 ms | 917 ms | - |
| 40 | @VPsave | vless | `172.67.115.132:443` | 85 ms | 959 ms | - |
| 41 | @Tarkahodeh 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | ss | `156.146.38.169:443` | 85 ms | 876 ms | - |
| 42 | @ConfigV2RayNG | vless | `104.18.41.190:443` | 87 ms | 901 ms | - |
| 43 | @hex_proxy ⁶ | vless | `104.18.41.190:443` | 87 ms | 1103 ms | - |
| 44 | @V2raySaman | vless | `104.25.231.228:443` | 87 ms | 989 ms | - |
| 45 | Telegram 👉🏼 @planB_net  • 04 | vless | `cf.877774.xyz:443` | 87 ms | 916 ms | - |
| 46 | 🇨🇦206119 / ⚡️Telegram = t.me/SOSkeyNET | vmess | `23.162.200.198:18000` | 88 ms | 1395 ms | - |
| 47 | 🏁RELAY-104.17.136.198-1960 | vmess | `104.17.136.198:443` | 88 ms | 861 ms | - |
| 48 | @FXxNET⚡️ | vless | `88.216.69.253:443` | 88 ms | 990 ms | - |
| 49 | @FXxNET⚡️ | vless | `chatgpt.com:443` | 88 ms | 936 ms | - |
| 50 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `104.18.40.100:443` | 90 ms | 907 ms | - |

> 仅展示前 50 个，共 1049 个；完整列表见 `sub/nodes.txt`。
