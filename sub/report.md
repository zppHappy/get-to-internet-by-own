# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-11-01 00:59:00+0800`

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
| 抓取链接 | 12472 |
| 去重后节点 | 8200 |
| TCP 预筛剔除 | 3751 |
| 真连接测试 | 8200 |
| 测试通过 | 870 |
| **最终保留** | **870** |
| 耗时 | 343.0 秒 |

> 解析阶段跳过：重复 4256、协议未启用 0、无法解析 16

## 协议分布

vless 471 · ss 163 · trojan 129 · vmess 107

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 870 个节点中，有 **697** 个能经代理访问到国内目标站，**173** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | @VEGAAS_VPN🇩🇪 | ss | `95.215.201.18:19999` | 23 ms | 705 ms | - |
| 2 | Channel id: ConfigV2RayNG 🇺🇸 | vmess | `129.146.77.248:39495` | 24 ms | 892 ms | - |
| 3 | Channel id: ConfigV2RayNG@ 🇺🇸 | vmess | `129.146.77.248:39495` | 28 ms | 1852 ms | - |
| 4 | @Nexus_Panell چنل تلگرام | vless | `67.209.184.133:443` | 55 ms | 708 ms | - |
| 5 | Channel id: @ConfigV2RayNG 🇺🇸 | ss | `45.207.207.25:443` | 56 ms | 不可达 | - |
| 6 | @V2ray_confiig | vless | `185.168.208.190:47443` | 62 ms | 747 ms | - |
| 7 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.242:443` | 62 ms | 702 ms | - |
| 8 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.76:443` | 62 ms | 875 ms | - |
| 9 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.171:443` | 63 ms | 727 ms | - |
| 10 | @tootffarangi🍓 | trojan | `66.163.112.31:443` | 63 ms | 722 ms | - |
| 11 | @V2ray_confiig | vless | `185.168.208.190:47443` | 64 ms | 735 ms | - |
| 12 | 🇨🇦 Join+Telegram:@Farah_VPN 🇨🇦 | vless | `172.64.150.28:2082` | 64 ms | 741 ms | - |
| 13 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.13:443` | 69 ms | 703 ms | - |
| 14 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.142:443` | 71 ms | 715 ms | - |
| 15 | Channel : @Daily_Configs | vless | `104.18.35.15:443` | 76 ms | 738 ms | - |
| 16 | Tel@MARAMBASHI 🇨🇦 | vless | `104.21.221.158:443` | 76 ms | 773 ms | - |
| 17 | Channel id: @ConfigV2RayNG 🇺🇸 | trojan | `66.163.112.121:443` | 76 ms | 737 ms | - |
| 18 | @VPsave | vless | `104.17.245.250:443` | 77 ms | 780 ms | - |
| 19 | Tel@MARAMBASHI 🇫🇷 | vless | `172.66.0.162:443` | 80 ms | 717 ms | - |
| 20 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | ss | `156.146.38.170:443` | 81 ms | 884 ms | - |
| 21 | 🇺🇸US-156.146.38.168-0187 | ss | `156.146.38.168:443` | 81 ms | 886 ms | - |
| 22 | @hex_proxy ⁴ | vless | `172.64.152.241:443` | 82 ms | 743 ms | - |
| 23 | @VPsave | vless | `104.25.95.31:443` | 83 ms | 762 ms | - |
| 24 | @Tarkshodeh 🇧🇲 | ss | `156.146.38.167:443` | 83 ms | 871 ms | - |
| 25 | 11354@proxy_online_net | vless | `104.18.37.247:443` | 84 ms | 735 ms | - |
| 26 | @tootffarangi🍓 | vless | `104.18.49.85:443` | 85 ms | 777 ms | - |
| 27 | Tel@MARAMBASHI 🇹🇷 | vless | `104.21.221.158:443` | 85 ms | 749 ms | - |
| 28 | 🇺🇸US-173.244.56.6-0129 | ss | `173.244.56.6:443` | 85 ms | 728 ms | - |
| 29 | @B2Hub | vless | `104.17.154.123:443` | 86 ms | 746 ms | - |
| 30 | Channel : @Daily_Configs | vless | `88.216.69.253:443` | 86 ms | 769 ms | - |
| 31 | @ConfigV2RayNG | vless | `104.18.35.15:443` | 87 ms | 763 ms | - |
| 32 | Channel id: @ConfigV2RayNG (118) | vless | `104.19.247.67:443` | 87 ms | 726 ms | - |
| 33 | @V2ray_confiig | vless | `104.21.221.158:443` | 87 ms | 766 ms | - |
| 34 | @B2Hub | vless | `172.64.152.241:443` | 87 ms | 735 ms | - |
| 35 | 🇨🇦204084 / ⚡️Telegram = t.me/SOSkeyNET | vless | `172.64.153.153:443` | 87 ms | 816 ms | - |
| 36 | Channel : @Daily_Configs | vless | `188.164.248.216:443` | 87 ms | 775 ms | - |
| 37 | configprxy | vless | `172.64.150.28:2082` | 87 ms | 913 ms | - |
| 38 | ⚡ b2n.ir/v2ray-configs / 490 | vless | `104.21.221.158:443` | 87 ms | 901 ms | - |
| 39 | @vmesskhodam | vless | `172.64.152.241:443` | 88 ms | 733 ms | - |
| 40 | @hex_proxy ⁷ | vless | `172.64.158.170:443` | 88 ms | 726 ms | - |
| 41 | @Tarkahodeh 🏴󠁧󠁢󠁷󠁬󠁳󠁿 | ss | `156.146.38.169:443` | 88 ms | 871 ms | - |
| 42 | @VPsave | vless | `104.24.173.112:443` | 89 ms | 737 ms | - |
| 43 | Channel : @Daily_Configs | vless | `172.66.154.57:443` | 89 ms | 765 ms | - |
| 44 | @VPsave | vless | `104.18.41.188:443` | 90 ms | 732 ms | - |
| 45 | @tootffarangi🍓 | vless | `104.18.8.74:443` | 90 ms | 718 ms | - |
| 46 | Tel@MARAMBASHI 🇫🇷 | vless | `88.216.69.253:443` | 90 ms | 775 ms | - |
| 47 | ⚡ b2n.ir/v2ray-configs / 840 | vless | `104.18.45.38:443` | 90 ms | 756 ms | - |
| 48 | @tootffarangi🍓 | vless | `172.64.152.241:443` | 91 ms | 757 ms | - |
| 49 | @hex_proxy ⁴ | vless | `172.66.0.162:443` | 91 ms | 736 ms | - |
| 50 | @pass_net🎃🕸️🎃🇨🇦 | vless | `cf.877774.xyz:443` | 91 ms | 752 ms | - |

> 仅展示前 50 个，共 870 个；完整列表见 `sub/nodes.txt`。
