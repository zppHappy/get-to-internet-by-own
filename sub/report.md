# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-24 05:08:33+0800`

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
| 抓取链接 | 19907 |
| 去重后节点 | 8100 |
| TCP 预筛剔除 | 3979 |
| 真连接测试 | 8100 |
| 测试通过 | 652 |
| **最终保留** | **652** |
| 耗时 | 288.4 秒 |

> 解析阶段跳过：重复 11776、协议未启用 0、无法解析 31

## 协议分布

vless 339 · ss 149 · vmess 110 · trojan 50 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 652 个节点中，有 **538** 个能经代理访问到国内目标站，**114** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `37.19.198.244:443` | 36 ms | 942 ms | - |
| 2 | EPODONIOS | ss | `37.19.198.236:443` | 38 ms | 1031 ms | - |
| 3 | EPODONIOS | vless | `69.46.46.91:443` | 39 ms | 860 ms | - |
| 4 | EPODONIOS | ss | `37.19.198.243:443` | 41 ms | 919 ms | - |
| 5 | EPODONIOS | vless | `47.253.226.114:443` | 48 ms | 1171 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 69 | vless | `104.18.37.127:443` | 52 ms | 946 ms | - |
| 7 | EPODONIOS | vless | `159.89.87.21:28190` | 53 ms | 1126 ms | - |
| 8 | EPODONIOS | vless | `172.66.0.162:443` | 54 ms | 1164 ms | - |
| 9 | EPODONIOS | vless | `47.253.226.114:443` | 57 ms | 920 ms | - |
| 10 | EPODONIOS | vless | `172.64.154.211:443` | 57 ms | 969 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 763 | vless | `104.24.197.20:443` | 57 ms | 965 ms | - |
| 12 | EPODONIOS | vless | `162.159.135.234:443` | 59 ms | 1617 ms | - |
| 13 | EPODONIOS | vless | `47.253.226.114:443` | 61 ms | 924 ms | - |
| 14 | US 🇺🇸 / @Raydikalx / DE08A7 | vmess | `67.220.95.3:18000` | 61 ms | 1222 ms | - |
| 15 | EPODONIOS | vless | `172.64.150.28:2082` | 63 ms | 1622 ms | - |
| 16 | EPODONIOS | vmess | `67.220.95.3:18000` | 64 ms | 1431 ms | - |
| 17 | EPODONIOS | vless | `172.64.150.43:443` | 65 ms | 976 ms | - |
| 18 | EPODONIOS | ss | `37.19.198.160:443` | 66 ms | 892 ms | - |
| 19 | EPODONIOS | vless | `185.95.231.156:443` | 68 ms | 1385 ms | - |
| 20 | EPODONIOS | vmess | `67.220.95.3:18000` | 68 ms | 不可达 | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 69 ms | 1037 ms | - |
| 22 | EPODONIOS | vless | `cf.877774.xyz:443` | 70 ms | 1009 ms | - |
| 23 | EPODONIOS | vless | `195.123.235.177:443` | 73 ms | 922 ms | - |
| 24 | EPODONIOS | vless | `169.40.42.35:443` | 73 ms | 900 ms | - |
| 25 | EPODONIOS | vless | `169.40.42.235:443` | 73 ms | 1160 ms | - |
| 26 | EPODONIOS | vless | `169.40.42.74:443` | 73 ms | 971 ms | - |
| 27 | EPODONIOS | vless | `www.speedtest.net:443` | 75 ms | 1010 ms | - |
| 28 | EPODONIOS | vless | `169.40.42.235:443` | 75 ms | 1211 ms | - |
| 29 | EPODONIOS | vless | `169.40.42.35:443` | 76 ms | 1029 ms | - |
| 30 | EPODONIOS | vless | `104.18.0.181:2082` | 77 ms | 1230 ms | - |
| 31 | EPODONIOS | vless | `169.40.42.225:443` | 81 ms | 954 ms | - |
| 32 | EPODONIOS | vless | `169.40.42.89:443` | 81 ms | 1170 ms | - |
| 33 | EPODONIOS | vless | `188.114.98.0:443` | 82 ms | 1027 ms | - |
| 34 | EPODONIOS | vless | `188.114.96.6:443` | 84 ms | 984 ms | - |
| 35 | EPODONIOS | vless | `104.18.0.181:2082` | 84 ms | 1120 ms | - |
| 36 | EPODONIOS | vless | `169.40.42.235:443` | 85 ms | 889 ms | - |
| 37 | EPODONIOS | vless | `169.40.42.225:443` | 85 ms | 1270 ms | - |
| 38 | EPODONIOS | vless | `188.114.98.0:443` | 91 ms | 1041 ms | - |
| 39 | EPODONIOS | vless | `172.64.158.170:443` | 92 ms | 1210 ms | - |
| 40 | EPODONIOS | ss | `51.222.136.236:8882` | 93 ms | 1054 ms | - |
| 41 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 98 ms | 1521 ms | - |
| 42 | EPODONIOS | vless | `172.64.152.241:443` | 102 ms | 968 ms | - |
| 43 | EPODONIOS | vless | `188.114.98.0:443` | 103 ms | 1105 ms | - |
| 44 | EPODONIOS | vless | `188.114.98.0:443` | 111 ms | 1118 ms | - |
| 45 | EPODONIOS | vless | `188.114.98.0:443` | 112 ms | 1095 ms | - |
| 46 | EPODONIOS | vless | `cf.877774.xyz:443` | 117 ms | 964 ms | - |
| 47 | EPODONIOS | ss | `156.146.38.169:443` | 118 ms | 1061 ms | - |
| 48 | EPODONIOS | vless | `169.40.42.104:443` | 119 ms | 1132 ms | - |
| 49 | EPODONIOS | vless | `188.114.97.6:443` | 120 ms | 1076 ms | - |
| 50 | EPODONIOS | vless | `188.114.98.0:443` | 120 ms | 1217 ms | - |

> 仅展示前 50 个，共 652 个；完整列表见 `sub/nodes.txt`。
