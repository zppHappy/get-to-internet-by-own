# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-02 08:23:08+0800`

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
| 抓取链接 | 12706 |
| 去重后节点 | 8139 |
| TCP 预筛剔除 | 3753 |
| 真连接测试 | 8139 |
| 测试通过 | 987 |
| **最终保留** | **987** |
| 耗时 | 292.9 秒 |

> 解析阶段跳过：重复 4539、协议未启用 0、无法解析 28

## 协议分布

vless 533 · ss 189 · vmess 162 · trojan 103

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 987 个节点中，有 **859** 个能经代理访问到国内目标站，**128** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | @Tarkahodeh 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | ss | `156.146.38.169:443` | 53 ms | 878 ms | - |
| 2 | @Tarkshodeh 🇧🇲 | ss | `156.146.38.167:443` | 56 ms | 835 ms | - |
| 3 | 🇺🇸 / @ELiV2Ray | vless | `38.107.232.36:80` | 65 ms | 1047 ms | - |
| 4 | @V2raySaman | trojan | `216.152.155.158:443` | 75 ms | 837 ms | - |
| 5 | @FXxNET⚡️ | ss | `156.146.38.170:443` | 79 ms | 850 ms | - |
| 6 | @FarazV2ray | ss | `156.146.38.168:443` | 83 ms | 925 ms | - |
| 7 | @V2raySaman | trojan | `216.152.155.59:443` | 84 ms | 857 ms | - |
| 8 | @i10VPN⁶ | trojan | `216.152.155.176:443` | 87 ms | 1115 ms | - |
| 9 | @v2ray_configs_pools 🌍 ⚡️ | vless | `3h-unitedstates1.09vpn.com:80` | 92 ms | 885 ms | - |
| 10 | 11598@proxy_online_net | vmess | `67.220.85.46:18000` | 103 ms | 1523 ms | - |
| 11 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `37.19.198.243:443` | 104 ms | 1000 ms | - |
| 12 | @filembad | ss | `185.215.132.18:19999` | 104 ms | 963 ms | - |
| 13 | Channel id: @ConfigV2RayNG 🇺🇸 | ss | `185.215.132.9:19999` | 104 ms | 938 ms | - |
| 14 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `37.19.198.160:443` | 109 ms | 1818 ms | - |
| 15 | کانال تلگرام 🪐 MTMVPN | vmess | `104.21.7.133:80` | 110 ms | 848 ms | - |
| 16 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vmess | `67.220.85.46:18000` | 111 ms | 1805 ms | - |
| 17 | Channel : @Daily_Configs | vless | `88.216.69.253:443` | 112 ms | 910 ms | - |
| 18 | @ICV2RAY | ss | `198.98.53.130:443` | 112 ms | 907 ms | - |
| 19 | ⚡ b2n.ir/v2ray-configs / 668 | vless | `104.21.221.158:443` | 112 ms | 1013 ms | - |
| 20 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `37.19.198.236:443` | 113 ms | 1001 ms | - |
| 21 | @i10VPN¹⁰ | trojan | `216.152.155.131:443` | 114 ms | 868 ms | - |
| 22 | @hex_proxy ⁴ | vless | `172.64.146.66:443` | 115 ms | 986 ms | - |
| 23 | [84265] - Telegram : @V2All | vmess | `172.67.187.145:80` | 116 ms | 867 ms | - |
| 24 | CA 🇨🇦 / @Raydikalx / 4EC4EF | vmess | `cf.090227.xyz:443` | 120 ms | 898 ms | - |
| 25 | @hex_proxy ¹ | vless | `cf.877774.xyz:443` | 121 ms | 904 ms | - |
| 26 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `37.19.198.244:443` | 122 ms | 1045 ms | - |
| 27 | Telegram @mtmvpn 🚨 | trojan | `216.152.147.89:443` | 122 ms | 1040 ms | - |
| 28 | @ConfigV2RayNG | trojan | `216.152.147.85:443` | 122 ms | 1176 ms | - |
| 29 | 🇨🇦CA-216.152.147.48-3164 | trojan | `216.152.147.48:443` | 122 ms | 1084 ms | - |
| 30 | Tel@MARAMBASHI 🇳🇱 | vless | `chatgpt.com:443` | 123 ms | 943 ms | - |
| 31 | 🏁RELAY-104.17.147.222-1361 | vmess | `104.17.147.222:80` | 124 ms | 878 ms | - |
| 32 | 11611@proxy_online_net | vless | `104.20.17.210:443` | 124 ms | 1006 ms | - |
| 33 | @V2ray_confiig | vless | `104.21.221.158:443` | 124 ms | 956 ms | - |
| 34 | [84237] - Telegram : @V2All | vless | `195.211.98.43:443` | 126 ms | 896 ms | - |
| 35 | Tel@MARAMBASHI 🇸🇬 | vless | `172.64.153.153:443` | 126 ms | 967 ms | - |
| 36 | ⚡ b2n.ir/v2ray-configs / 814 | vless | `cf.090227.xyz:443` | 126 ms | 968 ms | - |
| 37 | CA 🇨🇦 / @Raydikalx / CD5754 | vmess | `134.195.196.211:18000` | 126 ms | 1391 ms | - |
| 38 | 🇨🇦204742 / ⚡️Telegram = t.me/SOSkeyNET | vmess | `23.162.200.198:18000` | 127 ms | 1456 ms | - |
| 39 | @FXxNET⚡️ | vless | `104.21.221.158:443` | 127 ms | 946 ms | - |
| 40 | @FXxNET⚡️ | vless | `88.216.69.253:443` | 127 ms | 933 ms | - |
| 41 | @FarazV2ray  | vmess | `134.195.196.211:18000` | 128 ms | 1526 ms | - |
| 42 | @i10VPN⁶ | vless | `47.253.226.114:443` | 128 ms | 1052 ms | - |
| 43 | @ConfigV2RayNG | trojan | `216.152.155.23:443` | 128 ms | 891 ms | - |
| 44 | @meliproxyy | vless | `188.164.248.216:443` | 129 ms | 928 ms | - |
| 45 | @pass_net🎃🕸️🎃 | vless | `47.253.226.114:443` | 130 ms | 1042 ms | - |
| 46 | Tel@MARAMBASHI 🇹🇷 | vless | `195.211.98.43:443` | 130 ms | 920 ms | - |
| 47 | @FXxNET⚡️ | vless | `172.64.150.28:2082` | 130 ms | 921 ms | - |
| 48 | CA 🇨🇦 / @Raydikalx / A1CD58 | vmess | `cf.0sm.com:80` | 130 ms | 891 ms | - |
| 49 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `216.152.155.54:443` | 131 ms | 925 ms | - |
| 50 | Channel id: @ConfigV2RayNG 🇺🇸 | vless | `47.253.226.114:443` | 132 ms | 1037 ms | - |

> 仅展示前 50 个，共 987 个；完整列表见 `sub/nodes.txt`。
