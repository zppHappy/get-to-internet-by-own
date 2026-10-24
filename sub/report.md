# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-25 07:00:32+0800`

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
| 抓取链接 | 19744 |
| 去重后节点 | 8041 |
| TCP 预筛剔除 | 3888 |
| 真连接测试 | 8041 |
| 测试通过 | 634 |
| **最终保留** | **634** |
| 耗时 | 288.8 秒 |

> 解析阶段跳过：重复 11680、协议未启用 0、无法解析 23

## 协议分布

vless 314 · ss 151 · vmess 114 · trojan 51 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 634 个节点中，有 **545** 个能经代理访问到国内目标站，**89** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.167:443` | 45 ms | 813 ms | - |
| 2 | EPODONIOS | ss | `156.146.38.168:443` | 46 ms | 811 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.169:443` | 48 ms | 813 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.170:443` | 57 ms | 813 ms | - |
| 5 | EPODONIOS | vless | `172.64.150.28:2082` | 85 ms | 898 ms | - |
| 6 | EPODONIOS | vless | `172.64.150.28:2082` | 87 ms | 920 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 118 | vless | `88.216.69.253:443` | 92 ms | 938 ms | - |
| 8 | EPODONIOS | vmess | `129.146.143.80:48111` | 93 ms | 1119 ms | - |
| 9 | EPODONIOS | vless | `172.64.158.170:443` | 100 ms | 930 ms | - |
| 10 | EPODONIOS | vless | `104.18.0.181:2082` | 101 ms | 937 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 350 | vless | `104.21.221.158:443` | 103 ms | 1028 ms | - |
| 12 | ⚡ b2n.ir/v2ray-configs / 465 | vless | `8.47.69.60:443` | 103 ms | 925 ms | - |
| 13 | EPODONIOS | vless | `172.64.152.241:443` | 113 ms | 950 ms | - |
| 14 | US 🇺🇸 / @Raydikalx / 18811D | vmess | `129.146.143.80:48111` | 115 ms | 1136 ms | - |
| 15 | ⚡ b2n.ir/v2ray-configs / 821 | vless | `88.216.69.253:443` | 117 ms | 962 ms | - |
| 16 | EPODONIOS | ss | `95.215.201.18:19999` | 118 ms | 1197 ms | - |
| 17 | EPODONIOS | vless | `cf.877774.xyz:443` | 118 ms | 930 ms | - |
| 18 | EPODONIOS | vless | `104.18.35.86:8080` | 120 ms | 971 ms | - |
| 19 | EPODONIOS | vmess | `129.146.77.248:39495` | 123 ms | 1230 ms | - |
| 20 | EPODONIOS | vless | `172.66.0.162:443` | 124 ms | 893 ms | - |
| 21 | EPODONIOS | ss | `37.19.198.236:443` | 133 ms | 1033 ms | - |
| 22 | EPODONIOS | ss | `37.19.198.244:443` | 134 ms | 1044 ms | - |
| 23 | EPODONIOS | vless | `cf.877774.xyz:443` | 138 ms | 920 ms | - |
| 24 | EPODONIOS | ss | `37.19.198.243:443` | 141 ms | 1055 ms | - |
| 25 | EPODONIOS | ss | `216.105.168.18:443` | 145 ms | 921 ms | - |
| 26 | ⚡ b2n.ir/v2ray-configs / 34 | vless | `104.18.45.38:443` | 149 ms | 977 ms | - |
| 27 | EPODONIOS | vless | `172.64.150.28:2082` | 150 ms | 916 ms | - |
| 28 | EPODONIOS | vmess | `67.220.85.46:18000` | 150 ms | 1377 ms | - |
| 29 | EPODONIOS | ss | `37.19.198.160:443` | 152 ms | 1052 ms | - |
| 30 | US 🇺🇸 / @Raydikalx / BA43A3 | vmess | `67.220.85.46:18000` | 154 ms | 1516 ms | - |
| 31 | EPODONIOS | vmess | `23.254.194.215:8080` | 155 ms | 836 ms | - |
| 32 | US 🇺🇸 / @Raydikalx / DE08A7 | vmess | `67.220.95.3:18000` | 157 ms | 1486 ms | - |
| 33 | EPODONIOS | vmess | `38.110.1.246:18000` | 158 ms | 1485 ms | - |
| 34 | EPODONIOS | vmess | `67.220.95.3:18000` | 160 ms | 1547 ms | - |
| 35 | US 🇺🇸 / @Raydikalx / EDC608 | vmess | `23.254.194.215:8080` | 161 ms | 815 ms | - |
| 36 | EPODONIOS | ss | `15.204.233.41:8882` | 162 ms | 1531 ms | - |
| 37 | EPODONIOS | vmess | `67.220.95.3:18000` | 163 ms | 1557 ms | - |
| 38 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 163 ms | 1292 ms | - |
| 39 | EPODONIOS | vmess | `67.220.95.3:18000` | 166 ms | 1480 ms | - |
| 40 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 166 ms | 1275 ms | - |
| 41 | EPODONIOS | vless | `cf.090227.xyz:443` | 169 ms | 972 ms | - |
| 42 | EPODONIOS | ss | `193.151.160.18:19999` | 172 ms | 1331 ms | - |
| 43 | CA 🇨🇦 / @Raydikalx / 0940F6 | vmess | `23.162.200.198:18000` | 172 ms | 1559 ms | - |
| 44 | EPODONIOS | vless | `159.89.87.21:28190` | 177 ms | 1080 ms | - |
| 45 | EPODONIOS | vmess | `38.110.1.246:18000` | 178 ms | 1533 ms | - |
| 46 | EPODONIOS | ss | `198.98.53.130:443` | 179 ms | 1287 ms | - |
| 47 | EPODONIOS | vless | `195.123.235.177:443` | 180 ms | 1073 ms | - |
| 48 | CA 🇨🇦 / @Raydikalx / 22A83C | vmess | `104.21.7.133:80` | 180 ms | 974 ms | - |
| 49 | CA 🇨🇦 / @Raydikalx / 8B1289 | vmess | `172.64.229.21:443` | 180 ms | 955 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / E87E7A | vmess | `cf.0sm.com:80` | 182 ms | 999 ms | - |

> 仅展示前 50 个，共 634 个；完整列表见 `sub/nodes.txt`。
