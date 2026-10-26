# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-26 11:31:44+0800`

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
| 抓取链接 | 20270 |
| 去重后节点 | 8133 |
| TCP 预筛剔除 | 3833 |
| 真连接测试 | 8133 |
| 测试通过 | 806 |
| **最终保留** | **806** |
| 耗时 | 291.0 秒 |

> 解析阶段跳过：重复 12101、协议未启用 0、无法解析 36

## 协议分布

vless 457 · ss 161 · vmess 121 · trojan 63 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 806 个节点中，有 **700** 个能经代理访问到国内目标站，**106** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | ⚡ b2n.ir/v2ray-configs / 713 | vless | `88.216.69.253:443` | 39 ms | 961 ms | - |
| 2 | US 🇺🇸 / @Raydikalx / 46741C | vmess | `67.220.85.46:18000` | 39 ms | 1350 ms | - |
| 3 | EPODONIOS | ss | `15.204.233.41:8882` | 43 ms | 1187 ms | - |
| 4 | EPODONIOS | vless | `172.66.0.162:443` | 46 ms | 1002 ms | - |
| 5 | EPODONIOS | vless | `47.253.226.114:443` | 52 ms | 935 ms | - |
| 6 | EPODONIOS | ss | `37.19.198.243:443` | 52 ms | 932 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 795 | vless | `188.114.97.6:8080` | 52 ms | 962 ms | - |
| 8 | EPODONIOS | ss | `37.19.198.244:443` | 53 ms | 934 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 327 | vless | `172.66.1.36:443` | 55 ms | 1016 ms | - |
| 10 | ⚡ b2n.ir/v2ray-configs / 392 | vless | `104.18.45.38:443` | 56 ms | 1060 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 658 | vless | `104.18.45.38:443` | 57 ms | 954 ms | - |
| 12 | @VPsave | vmess | `67.220.95.3:18000` | 61 ms | 1481 ms | - |
| 13 | EPODONIOS | vmess | `67.220.95.3:18000` | 61 ms | 1201 ms | - |
| 14 | EPODONIOS | vless | `cf.130519.xyz:443` | 62 ms | 983 ms | - |
| 15 | EPODONIOS | vmess | `67.220.95.3:18000` | 63 ms | 1609 ms | - |
| 16 | EPODONIOS | vless | `172.64.150.28:2082` | 66 ms | 971 ms | - |
| 17 | ⚡ b2n.ir/v2ray-configs / 885 | vless | `104.19.173.68:8080` | 66 ms | 979 ms | - |
| 18 | EPODONIOS | ss | `37.19.198.160:443` | 67 ms | 920 ms | - |
| 19 | ⚡ b2n.ir/v2ray-configs / 675 | vless | `104.21.221.158:443` | 67 ms | 1192 ms | - |
| 20 | EPODONIOS | vless | `188.114.98.112:80` | 68 ms | 971 ms | - |
| 21 | EPODONIOS | vless | `172.64.150.28:2082` | 68 ms | 932 ms | - |
| 22 | EPODONIOS | vmess | `67.220.95.3:18000` | 68 ms | 1502 ms | - |
| 23 | EPODONIOS | vless | `172.64.147.91:443` | 69 ms | 982 ms | - |
| 24 | EPODONIOS | vless | `195.123.235.177:443` | 69 ms | 936 ms | - |
| 25 | EPODONIOS | vless | `169.40.42.104:443` | 69 ms | 1232 ms | - |
| 26 | ⚡ b2n.ir/v2ray-configs / 991 | vless | `8.47.69.60:443` | 70 ms | 955 ms | - |
| 27 | EPODONIOS | vless | `192.65.217.30:8880` | 72 ms | 997 ms | - |
| 28 | EPODONIOS | vless | `172.64.158.170:443` | 72 ms | 969 ms | - |
| 29 | EPODONIOS | vless | `47.253.226.114:443` | 73 ms | 921 ms | - |
| 30 | EPODONIOS | vless | `169.40.42.104:443` | 73 ms | 1092 ms | - |
| 31 | EPODONIOS | vless | `cf.877774.xyz:443` | 74 ms | 959 ms | - |
| 32 | EPODONIOS | vless | `169.40.42.90:443` | 74 ms | 1143 ms | - |
| 33 | EPODONIOS | vless | `188.114.97.6:443` | 74 ms | 978 ms | - |
| 34 | EPODONIOS | vless | `169.40.42.235:443` | 76 ms | 1796 ms | - |
| 35 | EPODONIOS | vless | `172.64.150.28:2082` | 76 ms | 1069 ms | - |
| 36 | EPODONIOS | vless | `188.114.97.6:8080` | 77 ms | 968 ms | - |
| 37 | EPODONIOS | vless | `185.158.133.30:8880` | 77 ms | 1007 ms | - |
| 38 | EPODONIOS | vless | `172.64.152.241:443` | 77 ms | 966 ms | - |
| 39 | EPODONIOS | vless | `169.40.42.35:443` | 77 ms | 1151 ms | - |
| 40 | EPODONIOS | vless | `216.24.57.30:8880` | 78 ms | 1011 ms | - |
| 41 | EPODONIOS | vless | `185.95.231.156:443` | 82 ms | 1521 ms | - |
| 42 | EPODONIOS | vless | `173.245.49.50:8880` | 82 ms | 1168 ms | - |
| 43 | ⚡ b2n.ir/v2ray-configs / 730 | vless | `104.21.221.158:443` | 82 ms | 956 ms | - |
| 44 | EPODONIOS | vless | `cf.877774.xyz:443` | 85 ms | 1034 ms | - |
| 45 | EPODONIOS | vless | `185.225.195.30:8880` | 90 ms | 1032 ms | - |
| 46 | EPODONIOS | vless | `159.89.87.21:28190` | 91 ms | 898 ms | - |
| 47 | EPODONIOS | ss | `37.19.198.236:443` | 92 ms | 910 ms | - |
| 48 | EPODONIOS | ss | `51.222.200.165:5000` | 93 ms | 1375 ms | - |
| 49 | EPODONIOS | vless | `159.89.87.21:28190` | 93 ms | 1727 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 93 ms | 1482 ms | - |

> 仅展示前 50 个，共 806 个；完整列表见 `sub/nodes.txt`。
