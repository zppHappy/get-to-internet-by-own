# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-24 00:38:41+0800`

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
| 抓取链接 | 19252 |
| 去重后节点 | 7977 |
| TCP 预筛剔除 | 3874 |
| 真连接测试 | 7977 |
| 测试通过 | 534 |
| **最终保留** | **534** |
| 耗时 | 310.8 秒 |

> 解析阶段跳过：重复 11250、协议未启用 0、无法解析 25

## 协议分布

vless 268 · ss 139 · vmess 85 · trojan 38 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 534 个节点中，有 **432** 个能经代理访问到国内目标站，**102** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.167:443` | 40 ms | 812 ms | - |
| 2 | EPODONIOS | vless | `188.114.98.0:443` | 76 ms | 1587 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.170:443` | 82 ms | 843 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.169:443` | 86 ms | 795 ms | - |
| 5 | EPODONIOS | ss | `95.215.201.18:19999` | 95 ms | 944 ms | - |
| 6 | EPODONIOS | vless | `104.18.37.127:443` | 97 ms | 1140 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 741 | vless | `172.64.150.28:2082` | 97 ms | 2227 ms | - |
| 8 | ⚡ b2n.ir/v2ray-configs / 879 | vless | `188.114.96.6:443` | 102 ms | 1646 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 287 | vless | `104.18.20.69:443` | 102 ms | 958 ms | - |
| 10 | EPODONIOS | vless | `188.114.98.0:443` | 107 ms | 926 ms | - |
| 11 | EPODONIOS | vless | `188.114.98.0:443` | 108 ms | 921 ms | - |
| 12 | EPODONIOS | vless | `172.66.0.162:443` | 109 ms | 915 ms | - |
| 13 | EPODONIOS | vless | `188.114.98.0:443` | 110 ms | 2232 ms | - |
| 14 | EPODONIOS | vless | `172.64.150.43:443` | 111 ms | 1078 ms | - |
| 15 | EPODONIOS | vless | `104.18.33.97:443` | 112 ms | 1003 ms | - |
| 16 | EPODONIOS | vless | `188.114.98.0:443` | 114 ms | 955 ms | - |
| 17 | EPODONIOS | vless | `172.64.152.241:443` | 114 ms | 991 ms | - |
| 18 | EPODONIOS | vless | `172.64.150.28:2082` | 115 ms | 1091 ms | - |
| 19 | EPODONIOS | vless | `162.159.135.234:443` | 116 ms | 1106 ms | - |
| 20 | EPODONIOS | vless | `188.114.97.6:443` | 116 ms | 1677 ms | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 118 ms | 949 ms | - |
| 22 | EPODONIOS | vless | `cf.130519.xyz:443` | 120 ms | 941 ms | - |
| 23 | EPODONIOS | vless | `104.18.0.181:2082` | 122 ms | 1209 ms | - |
| 24 | ⚡ b2n.ir/v2ray-configs / 125 | vless | `104.18.32.47:443` | 123 ms | 1536 ms | - |
| 25 | EPODONIOS | vless | `188.114.98.0:443` | 127 ms | 1034 ms | - |
| 26 | EPODONIOS | vless | `188.114.98.0:443` | 127 ms | 1575 ms | - |
| 27 | EPODONIOS | vless | `cf.877774.xyz:443` | 127 ms | 991 ms | - |
| 28 | EPODONIOS | vless | `188.114.98.0:443` | 128 ms | 943 ms | - |
| 29 | EPODONIOS | ss | `37.19.198.243:443` | 131 ms | 1075 ms | - |
| 30 | EPODONIOS | vless | `172.64.158.170:443` | 131 ms | 3300 ms | - |
| 31 | EPODONIOS | vless | `104.18.35.86:8080` | 132 ms | 1038 ms | - |
| 32 | EPODONIOS | ss | `37.19.198.236:443` | 133 ms | 1029 ms | - |
| 33 | EPODONIOS | vless | `cf.090227.xyz:443` | 134 ms | 1117 ms | - |
| 34 | EPODONIOS | vless | `188.114.98.0:443` | 136 ms | 915 ms | - |
| 35 | EPODONIOS | vless | `188.114.98.0:443` | 139 ms | 1426 ms | - |
| 36 | EPODONIOS | ss | `173.244.56.9:443` | 143 ms | 860 ms | - |
| 37 | EPODONIOS | ss | `156.146.38.168:443` | 146 ms | 807 ms | - |
| 38 | EPODONIOS | vless | `45.32.69.110:443` | 150 ms | 957 ms | - |
| 39 | EPODONIOS | vless | `www.speedtest.net:443` | 152 ms | 982 ms | - |
| 40 | EPODONIOS | vless | `172.64.154.211:443` | 155 ms | 1685 ms | - |
| 41 | EPODONIOS | vless | `188.114.98.0:443` | 155 ms | 1560 ms | - |
| 42 | EPODONIOS | ss | `173.244.56.6:443` | 159 ms | 860 ms | - |
| 43 | EPODONIOS | ss | `37.19.198.244:443` | 167 ms | 1044 ms | - |
| 44 | EPODONIOS | vless | `45.63.53.81:443` | 167 ms | 970 ms | - |
| 45 | EPODONIOS | vless | `45.76.172.197:443` | 170 ms | 846 ms | - |
| 46 | EPODONIOS | vmess | `67.220.95.3:18000` | 172 ms | 1311 ms | - |
| 47 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 175 ms | 1821 ms | - |
| 48 | EPODONIOS | vless | `104.18.0.181:2082` | 176 ms | 2203 ms | - |
| 49 | EPODONIOS | ss | `15.204.233.41:8882` | 183 ms | 1513 ms | - |
| 50 | EPODONIOS | vmess | `84.17.41.2:18000` | 183 ms | 1145 ms | - |

> 仅展示前 50 个，共 534 个；完整列表见 `sub/nodes.txt`。
