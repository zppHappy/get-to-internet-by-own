# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-23 19:11:18+0800`

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
| 抓取链接 | 19522 |
| 去重后节点 | 7974 |
| TCP 预筛剔除 | 3868 |
| 真连接测试 | 7974 |
| 测试通过 | 558 |
| **最终保留** | **558** |
| 耗时 | 290.6 秒 |

> 解析阶段跳过：重复 11519、协议未启用 0、无法解析 29

## 协议分布

vless 269 · ss 142 · vmess 81 · trojan 60 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 558 个节点中，有 **451** 个能经代理访问到国内目标站，**107** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `15.204.233.41:8882` | 30 ms | 1208 ms | - |
| 2 | EPODONIOS | ss | `37.19.198.160:443` | 39 ms | 927 ms | - |
| 3 | US 🇺🇸 / @Raydikalx / BA43A3 | vmess | `67.220.85.46:18000` | 48 ms | 1100 ms | - |
| 4 | EPODONIOS | vless | `172.64.152.241:443` | 50 ms | 1185 ms | - |
| 5 | EPODONIOS | vless | `162.159.135.234:443` | 52 ms | 997 ms | - |
| 6 | EPODONIOS | vless | `188.114.97.6:443` | 53 ms | 957 ms | - |
| 7 | EPODONIOS | vless | `cf.130519.xyz:443` | 53 ms | 1315 ms | - |
| 8 | EPODONIOS | vless | `188.114.98.0:443` | 54 ms | 1333 ms | - |
| 9 | EPODONIOS | vless | `104.18.36.29:443` | 55 ms | 1706 ms | - |
| 10 | EPODONIOS | vless | `188.114.97.6:443` | 55 ms | 1011 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 939 | vless | `172.64.150.43:8080` | 56 ms | 1145 ms | - |
| 12 | EPODONIOS | vless | `188.114.98.0:443` | 57 ms | 1715 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 832 | vless | `104.18.32.47:443` | 57 ms | 1682 ms | - |
| 14 | EPODONIOS | vless | `188.114.98.0:443` | 58 ms | 1009 ms | - |
| 15 | EPODONIOS | vless | `188.114.97.6:443` | 58 ms | 1211 ms | - |
| 16 | EPODONIOS | vless | `172.64.154.211:443` | 58 ms | 2449 ms | - |
| 17 | EPODONIOS | vless | `172.64.158.170:443` | 58 ms | 984 ms | - |
| 18 | EPODONIOS | vmess | `67.220.95.3:18000` | 58 ms | 1365 ms | - |
| 19 | EPODONIOS | vless | `188.114.99.0:443` | 59 ms | 1041 ms | - |
| 20 | EPODONIOS | vless | `www.speedtest.net:443` | 60 ms | 1178 ms | - |
| 21 | EPODONIOS | vless | `195.123.235.177:443` | 60 ms | 915 ms | - |
| 22 | EPODONIOS | ss | `37.19.198.244:443` | 61 ms | 1203 ms | - |
| 23 | EPODONIOS | vless | `172.64.150.43:443` | 61 ms | 981 ms | - |
| 24 | EPODONIOS | vless | `188.114.98.0:443` | 61 ms | 982 ms | - |
| 25 | EPODONIOS | vless | `188.114.98.0:443` | 61 ms | 992 ms | - |
| 26 | EPODONIOS | vmess | `67.220.95.3:18000` | 61 ms | 1334 ms | - |
| 27 | EPODONIOS | vless | `188.114.98.0:443` | 64 ms | 1181 ms | - |
| 28 | EPODONIOS | vless | `cf.877774.xyz:443` | 71 ms | 967 ms | - |
| 29 | EPODONIOS | vless | `169.40.42.35:443` | 73 ms | 2250 ms | - |
| 30 | EPODONIOS | vless | `104.18.35.86:8080` | 73 ms | 971 ms | - |
| 31 | EPODONIOS | vless | `172.64.150.28:2082` | 74 ms | 975 ms | - |
| 32 | EPODONIOS | vless | `188.114.98.0:443` | 75 ms | 967 ms | - |
| 33 | EPODONIOS | vless | `172.66.0.162:443` | 75 ms | 977 ms | - |
| 34 | EPODONIOS | vless | `169.40.42.231:443` | 75 ms | 1026 ms | - |
| 35 | EPODONIOS | vless | `169.40.42.90:443` | 77 ms | 1314 ms | - |
| 36 | EPODONIOS | vless | `169.40.42.231:443` | 77 ms | 3169 ms | - |
| 37 | EPODONIOS | vless | `188.114.98.0:443` | 78 ms | 1197 ms | - |
| 38 | EPODONIOS | vless | `188.114.98.0:443` | 79 ms | 1288 ms | - |
| 39 | EPODONIOS | vless | `104.18.35.86:8080` | 82 ms | 954 ms | - |
| 40 | EPODONIOS | vless | `188.114.98.0:443` | 83 ms | 1163 ms | - |
| 41 | EPODONIOS | vless | `cf.877774.xyz:443` | 83 ms | 1046 ms | - |
| 42 | EPODONIOS | vless | `172.66.0.162:443` | 85 ms | 976 ms | - |
| 43 | EPODONIOS | vless | `188.114.98.0:443` | 86 ms | 1931 ms | - |
| 44 | EPODONIOS | ss | `37.19.198.236:443` | 90 ms | 1059 ms | - |
| 45 | EPODONIOS | vless | `66.70.179.198:2053` | 90 ms | 1057 ms | - |
| 46 | EPODONIOS | vless | `172.64.150.28:2082` | 90 ms | 1037 ms | - |
| 47 | EPODONIOS | vless | `159.89.87.21:28190` | 93 ms | 954 ms | - |
| 48 | EPODONIOS | vless | `104.18.0.181:2082` | 93 ms | 1849 ms | - |
| 49 | EPODONIOS | vless | `104.18.0.181:2082` | 94 ms | 1699 ms | - |
| 50 | EPODONIOS | vless | `169.40.42.163:443` | 98 ms | 1391 ms | - |

> 仅展示前 50 个，共 558 个；完整列表见 `sub/nodes.txt`。
