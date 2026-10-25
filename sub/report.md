# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-25 11:29:52+0800`

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
| 抓取链接 | 19704 |
| 去重后节点 | 8074 |
| TCP 预筛剔除 | 3899 |
| 真连接测试 | 8074 |
| 测试通过 | 711 |
| **最终保留** | **711** |
| 耗时 | 289.4 秒 |

> 解析阶段跳过：重复 11600、协议未启用 0、无法解析 30

## 协议分布

vless 370 · ss 149 · vmess 135 · trojan 53 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 711 个节点中，有 **624** 个能经代理访问到国内目标站，**87** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `15.204.233.41:8882` | 43 ms | 1256 ms | - |
| 2 | EPODONIOS | vmess | `67.220.85.46:18000` | 51 ms | 1405 ms | - |
| 3 | EPODONIOS | vmess | `67.220.85.46:18000` | 53 ms | 1204 ms | - |
| 4 | ⚡ b2n.ir/v2ray-configs / 354 | vless | `104.18.45.38:443` | 58 ms | 975 ms | - |
| 5 | ⚡ b2n.ir/v2ray-configs / 604 | vless | `172.64.150.43:8080` | 64 ms | 1145 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 595 | vless | `172.66.1.36:443` | 66 ms | 1951 ms | - |
| 7 | EPODONIOS | vless | `172.64.150.28:2082` | 67 ms | 956 ms | - |
| 8 | ⚡ b2n.ir/v2ray-configs / 907 | vless | `8.47.69.60:443` | 68 ms | 986 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 60 | vless | `88.216.69.253:443` | 69 ms | 975 ms | - |
| 10 | EPODONIOS | vless | `wwww.qarvian.ir:443` | 70 ms | 1014 ms | - |
| 11 | EPODONIOS | vless | `104.26.4.2:443` | 70 ms | 1028 ms | - |
| 12 | EPODONIOS | vmess | `67.220.95.3:18000` | 70 ms | 2209 ms | - |
| 13 | US 🇺🇸 / @Raydikalx / DE08A7 | vmess | `67.220.95.3:18000` | 71 ms | 1440 ms | - |
| 14 | ⚡ b2n.ir/v2ray-configs / 828 | vless | `88.216.69.253:443` | 72 ms | 964 ms | - |
| 15 | EPODONIOS | vless | `159.89.87.21:28190` | 74 ms | 925 ms | - |
| 16 | EPODONIOS | vmess | `67.220.95.3:18000` | 74 ms | 1449 ms | - |
| 17 | EPODONIOS | vless | `172.64.152.241:443` | 76 ms | 991 ms | - |
| 18 | EPODONIOS | vless | `cf.877774.xyz:443` | 76 ms | 1004 ms | - |
| 19 | EPODONIOS | vless | `104.21.221.158:443` | 78 ms | 1031 ms | - |
| 20 | EPODONIOS | vmess | `67.220.95.3:18000` | 78 ms | 1496 ms | - |
| 21 | EPODONIOS | vless | `172.67.75.172:8080` | 81 ms | 1000 ms | - |
| 22 | EPODONIOS | vless | `cf.877774.xyz:443` | 82 ms | 1659 ms | - |
| 23 | EPODONIOS | vless | `154.197.64.30:8880` | 87 ms | 1031 ms | - |
| 24 | EPODONIOS | vless | `146.75.59.186:443` | 87 ms | 1845 ms | - |
| 25 | EPODONIOS | vless | `169.40.42.224:443` | 90 ms | 1264 ms | - |
| 26 | EPODONIOS | vless | `172.66.0.162:443` | 92 ms | 984 ms | - |
| 27 | EPODONIOS | vless | `169.40.42.168:443` | 92 ms | 1211 ms | - |
| 28 | EPODONIOS | vless | `159.89.87.21:28190` | 93 ms | 924 ms | - |
| 29 | EPODONIOS | vless | `169.40.42.225:443` | 93 ms | 1068 ms | - |
| 30 | EPODONIOS | vless | `169.40.42.89:443` | 93 ms | 945 ms | - |
| 31 | EPODONIOS | vless | `169.40.42.104:443` | 94 ms | 1279 ms | - |
| 32 | EPODONIOS | vless | `172.64.150.28:2082` | 95 ms | 1003 ms | - |
| 33 | EPODONIOS | ss | `51.222.155.113:5601` | 96 ms | 1194 ms | - |
| 34 | EPODONIOS | vless | `172.64.158.170:443` | 96 ms | 972 ms | - |
| 35 | EPODONIOS | vless | `169.40.42.104:443` | 96 ms | 1238 ms | - |
| 36 | EPODONIOS | vless | `172.64.150.28:2082` | 96 ms | 964 ms | - |
| 37 | EPODONIOS | vmess | `38.110.1.246:18000` | 104 ms | 1515 ms | - |
| 38 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 104 ms | 1476 ms | - |
| 39 | EPODONIOS | vless | `47.253.226.114:443` | 108 ms | 2635 ms | - |
| 40 | ⚡ b2n.ir/v2ray-configs / 695 | vless | `172.67.141.182:443` | 110 ms | 1030 ms | - |
| 41 | EPODONIOS | ss | `156.146.38.169:443` | 112 ms | 938 ms | - |
| 42 | EPODONIOS | vless | `154.218.15.250:2083` | 113 ms | 1664 ms | - |
| 43 | EPODONIOS | ss | `156.146.38.167:443` | 115 ms | 903 ms | - |
| 44 | EPODONIOS | ss | `51.79.64.198:8119` | 115 ms | 1173 ms | - |
| 45 | EPODONIOS | ss | `37.19.198.244:443` | 116 ms | 933 ms | - |
| 46 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 116 ms | 1534 ms | - |
| 47 | EPODONIOS | vless | `chat.openai.com:8880` | 118 ms | 1090 ms | - |
| 48 | EPODONIOS | ss | `37.19.198.243:443` | 119 ms | 923 ms | - |
| 49 | EPODONIOS | vless | `154.197.75.40:8880` | 125 ms | 1835 ms | - |
| 50 | EPODONIOS | ss | `37.19.198.236:443` | 125 ms | 957 ms | - |

> 仅展示前 50 个，共 711 个；完整列表见 `sub/nodes.txt`。
