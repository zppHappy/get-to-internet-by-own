# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-29 04:12:18+0800`

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
| 抓取链接 | 12157 |
| 去重后节点 | 8228 |
| TCP 预筛剔除 | 3835 |
| 真连接测试 | 8228 |
| 测试通过 | 670 |
| **最终保留** | **670** |
| 耗时 | 344.4 秒 |

> 解析阶段跳过：重复 3903、协议未启用 0、无法解析 26

## 协议分布

vless 346 · ss 141 · trojan 95 · vmess 88

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 670 个节点中，有 **499** 个能经代理访问到国内目标站，**171** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / 24BE22 | vmess | `47.88.79.34:443` | 53 ms | 649 ms | - |
| 2 | @FarazV2ray | vless | `172.64.152.241:443` | 62 ms | 905 ms | - |
| 3 | @ConfigV2RayNG | vless | `104.17.154.123:443` | 70 ms | 673 ms | - |
| 4 | ⚡ b2n.ir/v2ray-configs / 929 | vless | `172.64.150.28:2082` | 70 ms | 700 ms | - |
| 5 | 🔵@chillguy_vpn | vmess | `43.130.35.53:10087` | 71 ms | 825 ms | - |
| 6 | @hex_proxy ⁵ | vless | `172.64.158.170:443` | 71 ms | 730 ms | - |
| 7 | 11229@proxy_online_net | vless | `88.216.69.253:443` | 71 ms | 858 ms | - |
| 8 | @B2Hub | vless | `104.17.154.123:443` | 72 ms | 682 ms | - |
| 9 | @hex_proxy ⁴ | vless | `104.18.40.100:443` | 72 ms | 684 ms | - |
| 10 | 🇺🇸US-173.244.56.9-0135 | ss | `173.244.56.9:443` | 72 ms | 765 ms | - |
| 11 | @VPsave | vless | `172.96.141.206:8443` | 73 ms | 714 ms | - |
| 12 | ✰𝗝𝗼𝗶𝗻 ➠ @v2raymelliii✰ | vless | `104.18.47.73:443` | 75 ms | 769 ms | - |
| 13 | 🇺🇸US-173.244.56.6-0136 | ss | `173.244.56.6:443` | 75 ms | 991 ms | - |
| 14 | @hex_proxy ¹ | vless | `172.64.158.170:443` | 78 ms | 682 ms | - |
| 15 | @hex_proxy ² | vless | `104.18.37.127:443` | 80 ms | 697 ms | - |
| 16 | vpnsal | vless | `172.66.0.162:443` | 80 ms | 672 ms | - |
| 17 | @VEGAAS_VPN🇩🇪 | ss | `95.215.201.18:19999` | 81 ms | 954 ms | - |
| 18 | Channel id: ConfigV2RayNG@ 🇺🇸 | vmess | `129.146.77.248:39495` | 84 ms | 1204 ms | - |
| 19 | @FarazV2ray | vless | `104.18.47.73:443` | 84 ms | 681 ms | - |
| 20 | Channel : @Daily_Configs | vless | `172.66.154.57:443` | 84 ms | 759 ms | - |
| 21 | ⚡ b2n.ir/v2ray-configs / 256 | vless | `104.21.221.158:443` | 85 ms | 898 ms | - |
| 22 | ⚡ b2n.ir/v2ray-configs / 81 | vless | `172.66.1.36:443` | 85 ms | 1005 ms | - |
| 23 | Channel id: @ConfigV2RayNG 🇺🇸 | vmess | `129.146.77.248:39495` | 87 ms | 1339 ms | - |
| 24 | @FarazV2ray | vless | `cf.877774.xyz:443` | 88 ms | 748 ms | - |
| 25 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `23.95.222.127:8443` | 89 ms | 934 ms | - |
| 26 | کانال تلگرام ⭐️ MTMVPN | vless | `172.64.152.241:443` | 91 ms | 853 ms | - |
| 27 | @VPsave | trojan | `66.163.112.13:443` | 91 ms | 800 ms | - |
| 28 | @hex_proxy ⁸ | vless | `104.18.37.247:443` | 92 ms | 671 ms | - |
| 29 | @VPsave | trojan | `66.163.112.31:443` | 94 ms | 790 ms | - |
| 30 | @hex_proxy ⁷ | vless | `88.216.69.253:443` | 95 ms | 662 ms | - |
| 31 | @ConfigV2RayNG | vless | `chatgpt.com:443` | 95 ms | 679 ms | - |
| 32 | 11195@proxy_online_net | vless | `104.21.221.158:443` | 97 ms | 814 ms | - |
| 33 | @ConfigV2RayNG | trojan | `66.163.112.171:443` | 98 ms | 792 ms | - |
| 34 | @VPsave | trojan | `66.163.112.242:443` | 98 ms | 803 ms | - |
| 35 | 🇨🇦CA-149.22.95.183-0144 | ss | `149.22.95.183:443` | 99 ms | 839 ms | - |
| 36 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.121:443` | 100 ms | 796 ms | - |
| 37 | 🇺🇸201905 / ⚡️Telegram = t.me/SOSkeyNET | vless | `15.204.97.197:23576` | 103 ms | 不可达 | - |
| 38 | Channel : @Daily_Configs | vless | `104.18.40.100:443` | 104 ms | 693 ms | - |
| 39 | @Qara_atayi / 🇬🇧 | trojan | `66.163.112.76:443` | 104 ms | 814 ms | - |
| 40 | 🇺🇸201903 / ⚡️Telegram = t.me/SOSkeyNET | vless | `15.204.97.206:23576` | 105 ms | 不可达 | - |
| 41 | @hex_proxy ² | vless | `188.164.248.216:443` | 109 ms | 676 ms | - |
| 42 | Channel id: @ConfigV2RayNG 🇨🇦 | vmess | `guanwang.awsno.com:443` | 110 ms | 不可达 | - |
| 43 | Tel@MARAMBASHI 🇬🇧 | vless | `51.81.203.63:443` | 113 ms | 829 ms | - |
| 44 | @meliproxyy | trojan | `216.106.186.66:443` | 113 ms | 834 ms | - |
| 45 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `15.204.97.195:23576` | 114 ms | 不可达 | - |
| 46 | @B2Hub | vless | `cf.877774.xyz:443` | 114 ms | 759 ms | - |
| 47 | @v2ray_phoenix | vless | `172.64.152.241:443` | 115 ms | 705 ms | - |
| 48 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `cf.877774.xyz:443` | 123 ms | 866 ms | - |
| 49 | @VPsave | vless | `195.123.240.65:443` | 125 ms | 745 ms | - |
| 50 | configprxy | vless | `172.64.150.28:2082` | 127 ms | 755 ms | - |

> 仅展示前 50 个，共 670 个；完整列表见 `sub/nodes.txt`。
