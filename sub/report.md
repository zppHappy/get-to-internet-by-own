# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-23 11:39:22+0800`

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
| 抓取链接 | 19584 |
| 去重后节点 | 7986 |
| TCP 预筛剔除 | 3867 |
| 真连接测试 | 7986 |
| 测试通过 | 809 |
| **最终保留** | **809** |
| 耗时 | 270.9 秒 |

> 解析阶段跳过：重复 11594、协议未启用 0、无法解析 4

## 协议分布

vless 452 · ss 159 · vmess 115 · trojan 77 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 809 个节点中，有 **726** 个能经代理访问到国内目标站，**83** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vless | `47.253.226.114:443` | 33 ms | 910 ms | - |
| 2 | ⚡ b2n.ir/v2ray-configs / 510 | vless | `172.64.150.28:2082` | 46 ms | 1169 ms | - |
| 3 | EPODONIOS | vless | `47.253.226.114:443` | 47 ms | 937 ms | - |
| 4 | EPODONIOS | ss | `37.19.198.244:443` | 49 ms | 929 ms | - |
| 5 | US 🇺🇸 / @Raydikalx / F2583B | vmess | `67.220.85.46:18000` | 49 ms | 1922 ms | - |
| 6 | EPODONIOS | vless | `172.64.150.43:443` | 54 ms | 964 ms | - |
| 7 | EPODONIOS | ss | `37.19.198.243:443` | 55 ms | 898 ms | - |
| 8 | EPODONIOS | vless | `188.114.98.0:443` | 55 ms | 1327 ms | - |
| 9 | EPODONIOS | vless | `172.66.0.162:443` | 55 ms | 1106 ms | - |
| 10 | US 🇺🇸 / @Raydikalx / 46741C | vmess | `67.220.85.46:18000` | 55 ms | 1358 ms | - |
| 11 | EPODONIOS | ss | `64.42.181.102:12996` | 57 ms | 1160 ms | - |
| 12 | EPODONIOS | vless | `104.18.36.29:443` | 57 ms | 1058 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 401 | vless | `188.114.96.6:443` | 58 ms | 978 ms | - |
| 14 | EPODONIOS | vless | `47.253.226.114:443` | 60 ms | 939 ms | - |
| 15 | EPODONIOS | vless | `188.114.97.6:443` | 60 ms | 981 ms | - |
| 16 | EPODONIOS | vless | `188.114.97.6:443` | 60 ms | 984 ms | - |
| 17 | EPODONIOS | vless | `www.speedtest.net:443` | 60 ms | 998 ms | - |
| 18 | EPODONIOS | vless | `195.123.235.177:443` | 60 ms | 924 ms | - |
| 19 | EPODONIOS | vless | `172.64.152.241:443` | 60 ms | 1004 ms | - |
| 20 | EPODONIOS | vless | `172.66.0.162:443` | 60 ms | 978 ms | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 60 ms | 1005 ms | - |
| 22 | EPODONIOS | vless | `172.64.154.211:443` | 61 ms | 1051 ms | - |
| 23 | EPODONIOS | vless | `188.114.98.0:443` | 61 ms | 982 ms | - |
| 24 | EPODONIOS | vless | `cf.877774.xyz:443` | 61 ms | 943 ms | - |
| 25 | EPODONIOS | vless | `104.21.91.244:443` | 61 ms | 1688 ms | - |
| 26 | EPODONIOS | vmess | `67.220.95.3:18000` | 61 ms | 1398 ms | - |
| 27 | EPODONIOS | vless | `188.114.97.6:443` | 62 ms | 970 ms | - |
| 28 | EPODONIOS | vmess | `67.220.95.3:18000` | 62 ms | 1612 ms | - |
| 29 | EPODONIOS | ss | `37.19.198.236:443` | 63 ms | 1429 ms | - |
| 30 | EPODONIOS | vless | `188.114.98.0:443` | 63 ms | 999 ms | - |
| 31 | EPODONIOS | vless | `188.114.98.0:443` | 63 ms | 990 ms | - |
| 32 | EPODONIOS | vless | `104.21.91.244:443` | 63 ms | 1027 ms | - |
| 33 | EPODONIOS | vless | `104.21.91.244:443` | 63 ms | 1208 ms | - |
| 34 | EPODONIOS | vless | `159.89.87.21:28190` | 65 ms | 1262 ms | - |
| 35 | EPODONIOS | vless | `104.21.91.244:443` | 65 ms | 1666 ms | - |
| 36 | EPODONIOS | vless | `188.114.97.6:443` | 65 ms | 980 ms | - |
| 37 | EPODONIOS | vless | `172.64.158.170:443` | 66 ms | 1027 ms | - |
| 38 | EPODONIOS | vless | `104.21.91.244:443` | 66 ms | 990 ms | - |
| 39 | EPODONIOS | vless | `courses.mftplus.qzz.io:2096` | 68 ms | 1014 ms | - |
| 40 | EPODONIOS | vless | `cf.130519.xyz:443` | 68 ms | 2378 ms | - |
| 41 | EPODONIOS | vless | `188.114.97.6:443` | 68 ms | 960 ms | - |
| 42 | EPODONIOS | vless | `188.114.98.0:443` | 68 ms | 986 ms | - |
| 43 | EPODONIOS | trojan | `172.67.131.217:443` | 69 ms | 1057 ms | - |
| 44 | EPODONIOS | vless | `188.114.97.6:443` | 69 ms | 973 ms | - |
| 45 | EPODONIOS | vless | `188.114.98.0:443` | 70 ms | 974 ms | - |
| 46 | EPODONIOS | vless | `188.114.98.0:443` | 71 ms | 1257 ms | - |
| 47 | EPODONIOS | vless | `188.114.97.6:443` | 72 ms | 959 ms | - |
| 48 | EPODONIOS | vless | `188.114.97.6:443` | 72 ms | 959 ms | - |
| 49 | EPODONIOS | vless | `169.40.42.90:443` | 73 ms | 1288 ms | - |
| 50 | EPODONIOS | vless | `104.21.91.244:443` | 73 ms | 1022 ms | - |

> 仅展示前 50 个，共 809 个；完整列表见 `sub/nodes.txt`。
