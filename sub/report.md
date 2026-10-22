# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-22 11:34:56+0800`

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
| 抓取链接 | 19736 |
| 去重后节点 | 8018 |
| TCP 预筛剔除 | 3843 |
| 真连接测试 | 8018 |
| 测试通过 | 877 |
| **最终保留** | **877** |
| 耗时 | 288.3 秒 |

> 解析阶段跳过：重复 11688、协议未启用 0、无法解析 30

## 协议分布

vless 502 · ss 159 · vmess 114 · trojan 96 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 877 个节点中，有 **798** 个能经代理访问到国内目标站，**79** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.167:443` | 50 ms | 886 ms | - |
| 2 | EPODONIOS | ss | `156.146.38.168:443` | 52 ms | 822 ms | - |
| 3 | EPODONIOS | ss | `138.199.42.68:8080` | 60 ms | 835 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.169:443` | 88 ms | 872 ms | - |
| 5 | EPODONIOS | vmess | `104.21.7.133:80` | 90 ms | 916 ms | - |
| 6 | EPODONIOS | ss | `156.146.38.170:443` | 92 ms | 871 ms | - |
| 7 | EPODONIOS | ss | `37.19.198.160:443` | 95 ms | 980 ms | - |
| 8 | EPODONIOS | vless | `104.18.0.181:2082` | 98 ms | 979 ms | - |
| 9 | CA 🇨🇦 / @Raydikalx / F65B9D | vmess | `104.17.147.222:80` | 99 ms | 964 ms | - |
| 10 | EPODONIOS | vless | `172.67.155.65:8443` | 100 ms | 1025 ms | - |
| 11 | EPODONIOS | ss | `37.19.198.244:443` | 101 ms | 1039 ms | - |
| 12 | EPODONIOS | vless | `104.18.35.86:8080` | 102 ms | 1004 ms | - |
| 13 | EPODONIOS | ss | `37.19.198.236:443` | 102 ms | 988 ms | - |
| 14 | EPODONIOS | vless | `172.67.155.65:8443` | 106 ms | 1006 ms | - |
| 15 | EPODONIOS | vmess | `67.220.95.3:18000` | 107 ms | 1741 ms | - |
| 16 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 107 ms | 1505 ms | - |
| 17 | EPODONIOS | vless | `104.18.0.181:2082` | 109 ms | 1015 ms | - |
| 18 | EPODONIOS | vmess | `67.220.95.3:18000` | 112 ms | 1691 ms | - |
| 19 | EPODONIOS | ss | `37.19.198.243:443` | 112 ms | 995 ms | - |
| 20 | EPODONIOS | vless | `172.64.154.211:443` | 113 ms | 961 ms | - |
| 21 | EPODONIOS | vless | `45.138.100.248:10443` | 114 ms | 1170 ms | - |
| 22 | EPODONIOS | vless | `88.216.69.30:8880` | 116 ms | 1003 ms | - |
| 23 | EPODONIOS | vless | `chat.openai.com:8880` | 117 ms | 956 ms | - |
| 24 | EPODONIOS | vless | `172.67.155.65:8443` | 117 ms | 984 ms | - |
| 25 | EPODONIOS | vless | `172.64.147.91:443` | 119 ms | 926 ms | - |
| 26 | EPODONIOS | vless | `172.64.150.28:2082` | 119 ms | 969 ms | - |
| 27 | EPODONIOS | vless | `195.211.98.43:443` | 122 ms | 908 ms | - |
| 28 | EPODONIOS | vless | `162.120.94.30:8880` | 124 ms | 978 ms | - |
| 29 | EPODONIOS | vless | `45.12.30.30:8880` | 124 ms | 965 ms | - |
| 30 | EPODONIOS | vless | `172.67.155.65:8443` | 124 ms | 977 ms | - |
| 31 | EPODONIOS | vless | `172.67.155.65:2053` | 125 ms | 1005 ms | - |
| 32 | EPODONIOS | vless | `47.253.226.114:443` | 126 ms | 1055 ms | - |
| 33 | US 🇺🇸 / @Raydikalx / DE08A7 | vmess | `67.220.95.3:18000` | 126 ms | 1694 ms | - |
| 34 | EPODONIOS | vless | `172.64.150.43:443` | 127 ms | 997 ms | - |
| 35 | EPODONIOS | vless | `e33xr.qzz.io:80` | 127 ms | 928 ms | - |
| 36 | EPODONIOS | vless | `172.67.155.65:2053` | 127 ms | 1191 ms | - |
| 37 | EPODONIOS | vless | `162.159.135.234:443` | 128 ms | 1155 ms | - |
| 38 | EPODONIOS | vless | `172.64.158.170:443` | 128 ms | 929 ms | - |
| 39 | EPODONIOS | vless | `172.67.155.65:8443` | 128 ms | 974 ms | - |
| 40 | EPODONIOS | vless | `172.66.0.162:443` | 129 ms | 934 ms | - |
| 41 | EPODONIOS | vless | `188.114.98.0:443` | 130 ms | 838 ms | - |
| 42 | EPODONIOS | vless | `172.67.155.65:8443` | 131 ms | 952 ms | - |
| 43 | EPODONIOS | vless | `172.67.155.65:8443` | 132 ms | 944 ms | - |
| 44 | EPODONIOS | vless | `188.114.98.0:443` | 132 ms | 982 ms | - |
| 45 | EPODONIOS | vless | `3h-unitedstates1.09vpn.com:80` | 133 ms | 955 ms | - |
| 46 | EPODONIOS | vless | `104.21.91.244:443` | 133 ms | 1061 ms | - |
| 47 | EPODONIOS | vless | `162.159.135.234:443` | 134 ms | 1107 ms | - |
| 48 | EPODONIOS | vless | `154.197.64.30:8880` | 134 ms | 991 ms | - |
| 49 | EPODONIOS | vless | `188.164.248.216:443` | 134 ms | 1084 ms | - |
| 50 | EPODONIOS | vless | `172.67.155.65:2053` | 134 ms | 948 ms | - |

> 仅展示前 50 个，共 877 个；完整列表见 `sub/nodes.txt`。
