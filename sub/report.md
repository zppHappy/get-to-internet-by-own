# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-01 05:08:11+0800`

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
| 抓取链接 | 12418 |
| 去重后节点 | 8095 |
| TCP 预筛剔除 | 3699 |
| 真连接测试 | 8095 |
| 测试通过 | 924 |
| **最终保留** | **924** |
| 耗时 | 319.0 秒 |

> 解析阶段跳过：重复 4289、协议未启用 0、无法解析 34

## 协议分布

vless 470 · ss 160 · trojan 157 · vmess 137

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 924 个节点中，有 **767** 个能经代理访问到国内目标站，**157** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | @VEGAAS_VPN🇩🇪 | ss | `95.215.201.18:19999` | 24 ms | 917 ms | - |
| 2 | Channel id: ConfigV2RayNG@ 🇺🇸 | vmess | `129.146.77.248:39495` | 26 ms | 1270 ms | - |
| 3 | Channel id: ConfigV2RayNG 🇺🇸 | vmess | `129.146.77.248:39495` | 40 ms | 1226 ms | - |
| 4 | 🇺🇸US-173.244.56.6-0129 | ss | `173.244.56.6:443` | 53 ms | 728 ms | - |
| 5 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.13:443` | 61 ms | 704 ms | - |
| 6 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.142:443` | 63 ms | 720 ms | - |
| 7 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.147:443` | 65 ms | 724 ms | - |
| 8 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.121:443` | 66 ms | 738 ms | - |
| 9 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.242:443` | 66 ms | 699 ms | - |
| 10 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.76:443` | 67 ms | 720 ms | - |
| 11 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.171:443` | 69 ms | 1554 ms | - |
| 12 | @v2ray313 کانالمون 🫶🏻 | vless | `172.64.150.28:2082` | 71 ms | 921 ms | - |
| 13 | @B2Hub | vless | `172.64.150.28:2082` | 75 ms | 810 ms | - |
| 14 | Tel@MARAMBASHI 🇹🇷 | vless | `104.21.221.158:443` | 78 ms | 745 ms | - |
| 15 | Channel : @Daily_Configs | vless | `104.18.40.100:443` | 80 ms | 718 ms | - |
| 16 | @V2ray_confiig | vless | `104.21.221.158:443` | 80 ms | 708 ms | - |
| 17 | @MARAMBASHI 🇫🇷 | vless | `chatgpt.com:443` | 81 ms | 734 ms | - |
| 18 | @GozargahAzad/🏁 | vless | `104.18.37.247:443` | 82 ms | 740 ms | - |
| 19 | Channel id: @ConfigV2RayNG (118) | vless | `104.19.247.67:443` | 82 ms | 731 ms | - |
| 20 | configprxy | vless | `172.64.150.28:2082` | 82 ms | 746 ms | - |
| 21 | @Tarkshodeh 🇧🇲 | ss | `156.146.38.167:443` | 82 ms | 870 ms | - |
| 22 | Tel@MARAMBASHI 🇫🇮 | vless | `104.18.40.100:443` | 83 ms | 764 ms | - |
| 23 | @hex_proxy ⁴ | vless | `172.64.146.66:443` | 83 ms | 750 ms | - |
| 24 | Tel@MARAMBASHI 🇫🇷 | vless | `172.66.0.162:443` | 83 ms | 752 ms | - |
| 25 | Channel : @Daily_Configs | vless | `104.21.221.158:443` | 84 ms | 751 ms | - |
| 26 | @VPsave | vless | `104.25.95.31:443` | 84 ms | 729 ms | - |
| 27 | ♾️𝗝𝗼𝗶𝗻➠🆔️@ATLAS_V2VPN🆓️📶‎🛰️644🌐🆕 | vless | `chatgpt.com:443` | 85 ms | 934 ms | - |
| 28 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `173.244.56.9:443` | 85 ms | 740 ms | - |
| 29 | @Tarkahodeh 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | ss | `156.146.38.169:443` | 85 ms | 893 ms | - |
| 30 | 🇺🇸US-156.146.38.170-0185 | ss | `156.146.38.170:443` | 85 ms | 1264 ms | - |
| 31 | ⚡ b2n.ir/v2ray-configs / 624 | vless | `104.18.45.38:443` | 85 ms | 726 ms | - |
| 32 | ⚡ b2n.ir/v2ray-configs / 721 | vless | `104.21.221.158:443` | 85 ms | 725 ms | - |
| 33 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `156.146.38.168:443` | 86 ms | 861 ms | - |
| 34 | ⚡ b2n.ir/v2ray-configs / 922 | vless | `104.21.221.158:443` | 86 ms | 719 ms | - |
| 35 | @vmesskhodam | vless | `104.21.221.158:443` | 87 ms | 756 ms | - |
| 36 | 11445@proxy_online_net | vless | `172.66.0.162:443` | 87 ms | 736 ms | - |
| 37 | @VPsave | vless | `104.17.96.84:443` | 88 ms | 752 ms | - |
| 38 | Channel : @Daily_Configs | vless | `104.18.47.73:443` | 88 ms | 760 ms | - |
| 39 | Tel@MARAMBASHI 🇨🇦 | vless | `104.21.221.158:443` | 88 ms | 815 ms | - |
| 40 | @ConfigV2RayNG | vless | `104.18.35.15:443` | 89 ms | 745 ms | - |
| 41 | TELEGRAM--MARAMBASHI--MARAMBASHI--MARAMB | vless | `172.64.152.241:443` | 89 ms | 725 ms | - |
| 42 | @V2ray_confiig | vless | `172.64.152.241:443` | 89 ms | 722 ms | - |
| 43 | Channel : @Daily_Configs | vless | `88.216.69.253:443` | 89 ms | 887 ms | - |
| 44 | @VPsave | vless | `104.16.195.204:443` | 90 ms | 732 ms | - |
| 45 | @VPsave | vless | `104.17.245.250:443` | 90 ms | 722 ms | - |
| 46 | 11355@proxy_online_net | vless | `172.64.158.170:443` | 90 ms | 730 ms | - |
| 47 | @hex_proxy ² | vless | `104.18.37.247:443` | 91 ms | 759 ms | - |
| 48 | @VPsave | vless | `104.18.41.188:443` | 91 ms | 726 ms | - |
| 49 | Telegram---PLANB_NET---PLANB_NET---PLANB | vless | `172.64.152.241:443` | 91 ms | 754 ms | - |
| 50 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `cf.090227.xyz:443` | 91 ms | 768 ms | - |

> 仅展示前 50 个，共 924 个；完整列表见 `sub/nodes.txt`。
