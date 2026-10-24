# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-24 11:33:59+0800`

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
| 抓取链接 | 19873 |
| 去重后节点 | 8048 |
| TCP 预筛剔除 | 3853 |
| 真连接测试 | 8048 |
| 测试通过 | 744 |
| **最终保留** | **744** |
| 耗时 | 286.6 秒 |

> 解析阶段跳过：重复 11797、协议未启用 0、无法解析 28

## 协议分布

vless 414 · ss 152 · vmess 115 · trojan 58 · hysteria2 5

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 744 个节点中，有 **652** 个能经代理访问到国内目标站，**92** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.168:443` | 60 ms | 866 ms | - |
| 2 | EPODONIOS | ss | `156.146.38.170:443` | 64 ms | 860 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.169:443` | 76 ms | 1015 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.167:443` | 84 ms | 872 ms | - |
| 5 | EPODONIOS | ss | `37.19.198.236:443` | 95 ms | 1161 ms | - |
| 6 | EPODONIOS | ss | `37.19.198.243:443` | 98 ms | 992 ms | - |
| 7 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 98 ms | 1505 ms | - |
| 8 | EPODONIOS | vless | `104.18.35.86:8080` | 100 ms | 1032 ms | - |
| 9 | EPODONIOS | ss | `37.19.198.160:443` | 103 ms | 982 ms | - |
| 10 | EPODONIOS | ss | `37.19.198.244:443` | 103 ms | 1070 ms | - |
| 11 | EPODONIOS | vless | `188.114.96.6:443` | 109 ms | 1062 ms | - |
| 12 | EPODONIOS | vless | `154.197.64.30:8880` | 110 ms | 1013 ms | - |
| 13 | EPODONIOS | vmess | `67.220.85.46:18000` | 111 ms | 1271 ms | - |
| 14 | EPODONIOS | vless | `172.64.152.241:443` | 113 ms | 1194 ms | - |
| 15 | EPODONIOS | vless | `cf.877774.xyz:443` | 115 ms | 1012 ms | - |
| 16 | EPODONIOS | vless | `www.speedtest.net:443` | 119 ms | 983 ms | - |
| 17 | EPODONIOS | vless | `188.114.98.0:443` | 119 ms | 1642 ms | - |
| 18 | EPODONIOS | trojan | `ca.tronsg.com:443` | 121 ms | 906 ms | - |
| 19 | EPODONIOS | vless | `172.64.150.43:443` | 123 ms | 984 ms | - |
| 20 | EPODONIOS | vless | `cf.877774.xyz:443` | 124 ms | 991 ms | - |
| 21 | ⚡ b2n.ir/v2ray-configs / 79 | vless | `104.18.33.97:443` | 125 ms | 995 ms | - |
| 22 | CA 🇨🇦 / @Raydikalx / CD5754 | vmess | `134.195.196.211:18000` | 127 ms | 1965 ms | - |
| 23 | EPODONIOS | vless | `47.253.226.114:443` | 128 ms | 1029 ms | - |
| 24 | EPODONIOS | vless | `172.64.150.43:8080` | 128 ms | 1688 ms | - |
| 25 | EPODONIOS | vless | `154.197.75.40:8880` | 129 ms | 1066 ms | - |
| 26 | EPODONIOS | ss | `138.199.42.68:8080` | 129 ms | 862 ms | - |
| 27 | CA 🇨🇦 / @Raydikalx / 874860 | vmess | `134.195.196.211:18000` | 129 ms | 1481 ms | - |
| 28 | EPODONIOS | vless | `47.253.226.114:443` | 130 ms | 1042 ms | - |
| 29 | EPODONIOS | vless | `188.114.97.6:443` | 131 ms | 997 ms | - |
| 30 | EPODONIOS | vless | `172.64.150.28:2082` | 132 ms | 959 ms | - |
| 31 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 133 ms | 1217 ms | - |
| 32 | EPODONIOS | vless | `47.253.226.114:443` | 134 ms | 1048 ms | - |
| 33 | EPODONIOS | vless | `172.64.154.211:443` | 134 ms | 1733 ms | - |
| 34 | EPODONIOS | vless | `104.18.0.181:2082` | 134 ms | 1195 ms | - |
| 35 | EPODONIOS | ss | `95.215.201.18:19999` | 135 ms | 1149 ms | - |
| 36 | EPODONIOS | vless | `154.218.15.250:2083` | 135 ms | 不可达 | - |
| 37 | EPODONIOS | vless | `104.20.5.134:443` | 135 ms | 1227 ms | - |
| 38 | EPODONIOS | vless | `188.114.97.6:443` | 135 ms | 1029 ms | - |
| 39 | ⚡ b2n.ir/v2ray-configs / 661 | vless | `104.24.197.20:443` | 136 ms | 1301 ms | - |
| 40 | EPODONIOS | vless | `188.114.98.0:443` | 137 ms | 1660 ms | - |
| 41 | EPODONIOS | vless | `188.114.97.6:443` | 138 ms | 996 ms | - |
| 42 | EPODONIOS | vless | `188.114.98.0:443` | 138 ms | 1011 ms | - |
| 43 | EPODONIOS | vless | `188.114.98.0:443` | 138 ms | 963 ms | - |
| 44 | EPODONIOS | vless | `172.64.158.170:443` | 139 ms | 966 ms | - |
| 45 | EPODONIOS | vless | `188.114.98.0:443` | 140 ms | 1003 ms | - |
| 46 | EPODONIOS | vless | `188.114.98.0:443` | 140 ms | 962 ms | - |
| 47 | @V2ray_Alpha💎 11 | vmess | `134.195.196.211:18000` | 140 ms | 1511 ms | - |
| 48 | EPODONIOS | vless | `162.159.135.234:443` | 141 ms | 1134 ms | - |
| 49 | EPODONIOS | vmess | `67.220.95.3:18000` | 142 ms | 1074 ms | - |
| 50 | EPODONIOS | vless | `172.64.150.28:2082` | 143 ms | 1299 ms | - |

> 仅展示前 50 个，共 744 个；完整列表见 `sub/nodes.txt`。
