# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-26 20:26:24+0800`

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
| 抓取链接 | 20094 |
| 去重后节点 | 8427 |
| TCP 预筛剔除 | 3911 |
| 真连接测试 | 8427 |
| 测试通过 | 725 |
| **最终保留** | **725** |
| 耗时 | 329.5 秒 |

> 解析阶段跳过：重复 11637、协议未启用 0、无法解析 30

## 协议分布

vless 402 · ss 151 · vmess 109 · trojan 60 · hysteria2 3

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 725 个节点中，有 **603** 个能经代理访问到国内目标站，**122** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `138.199.42.68:8080` | 34 ms | 757 ms | - |
| 2 | EPODONIOS | vless | `104.18.40.100:443` | 61 ms | 825 ms | - |
| 3 | EPODONIOS | vless | `172.64.152.241:443` | 69 ms | 1040 ms | - |
| 4 | EPODONIOS | vless | `cf.877774.xyz:443` | 69 ms | 1599 ms | - |
| 5 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 69 ms | 1175 ms | - |
| 6 | EPODONIOS | vless | `172.66.0.162:443` | 72 ms | 975 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 308 | vless | `8.47.69.60:443` | 72 ms | 1008 ms | - |
| 8 | EPODONIOS | vless | `cf.877774.xyz:443` | 73 ms | 1029 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 168 | vless | `172.66.1.36:443` | 73 ms | 1010 ms | - |
| 10 | EPODONIOS | ss | `37.19.198.160:443` | 75 ms | 970 ms | - |
| 11 | EPODONIOS | ss | `37.19.198.244:443` | 75 ms | 967 ms | - |
| 12 | ⚡ b2n.ir/v2ray-configs / 740 | vless | `104.21.221.158:443` | 75 ms | 1147 ms | - |
| 13 | EPODONIOS | ss | `37.19.198.236:443` | 76 ms | 958 ms | - |
| 14 | EPODONIOS | vless | `cf.090227.xyz:443` | 76 ms | 911 ms | - |
| 15 | EPODONIOS | ss | `37.19.198.243:443` | 77 ms | 976 ms | - |
| 16 | EPODONIOS | vless | `88.216.69.253:443` | 80 ms | 899 ms | - |
| 17 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 80 ms | 1172 ms | - |
| 18 | EPODONIOS | vless | `188.164.248.216:443` | 82 ms | 1134 ms | - |
| 19 | EPODONIOS | ss | `156.146.38.167:443` | 84 ms | 889 ms | - |
| 20 | EPODONIOS | ss | `156.146.38.169:443` | 84 ms | 1036 ms | - |
| 21 | ⚡ b2n.ir/v2ray-configs / 97 | vless | `88.216.69.253:443` | 84 ms | 962 ms | - |
| 22 | 🇺🇸 Join+Telegram:@Farah_VPN 🇺🇸 | vless | `cf.130519.xyz:443` | 92 ms | 762 ms | - |
| 23 | US 🇺🇸 / @Raydikalx / BA43A3 | vmess | `67.220.85.46:18000` | 92 ms | 1573 ms | - |
| 24 | @Qara_atayi / 🇮🇷 | vless | `172.64.158.170:443` | 94 ms | 958 ms | - |
| 25 | EPODONIOS | ss | `137.184.174.93:8080` | 97 ms | 1785 ms | - |
| 26 | EPODONIOS | ss | `156.146.38.170:443` | 102 ms | 878 ms | - |
| 27 | @VPsave | vmess | `67.220.95.3:18000` | 106 ms | 1672 ms | - |
| 28 | EPODONIOS | vless | `172.64.150.28:2082` | 107 ms | 915 ms | - |
| 29 | EPODONIOS | vmess | `67.220.95.3:18000` | 107 ms | 1243 ms | - |
| 30 | EPODONIOS | vless | `172.64.150.28:2082` | 110 ms | 982 ms | - |
| 31 | CA 🇨🇦 / @Raydikalx / CD5754 | vmess | `134.195.196.211:18000` | 110 ms | 1114 ms | - |
| 32 | EPODONIOS | ss | `51.222.200.165:5000` | 113 ms | 1352 ms | - |
| 33 | EPODONIOS | vless | `169.40.42.35:443` | 115 ms | 1195 ms | - |
| 34 | EPODONIOS | vless | `159.89.87.21:28190` | 116 ms | 1023 ms | - |
| 35 | EPODONIOS | ss | `185.230.230.18:19999` | 118 ms | 961 ms | - |
| 36 | EPODONIOS | vless | `169.40.42.89:443` | 118 ms | 1269 ms | - |
| 37 | EPODONIOS | vless | `169.40.42.235:443` | 119 ms | 1193 ms | - |
| 38 | EPODONIOS | vless | `169.40.42.35:443` | 119 ms | 1226 ms | - |
| 39 | EPODONIOS | vmess | `38.91.107.49:18000` | 119 ms | 1856 ms | - |
| 40 | EPODONIOS | vmess | `67.220.95.3:18000` | 119 ms | 1282 ms | - |
| 41 | EPODONIOS | vmess | `67.220.95.3:18000` | 120 ms | 不可达 | - |
| 42 | EPODONIOS | ss | `156.146.38.168:443` | 122 ms | 900 ms | - |
| 43 | EPODONIOS | vless | `169.40.42.74:443` | 127 ms | 992 ms | - |
| 44 | EPODONIOS | vless | `169.40.42.104:443` | 128 ms | 1229 ms | - |
| 45 | EPODONIOS | ss | `51.222.136.236:8882` | 129 ms | 1327 ms | - |
| 46 | EPODONIOS | vless | `3h-unitedstates1.09vpn.com:80` | 129 ms | 948 ms | - |
| 47 | EPODONIOS | vless | `185.95.231.156:443` | 134 ms | 1404 ms | - |
| 48 | EPODONIOS | vless | `195.123.235.177:443` | 134 ms | 889 ms | - |
| 49 | EPODONIOS | ss | `15.204.246.132:7307` | 135 ms | 1381 ms | - |
| 50 | EPODONIOS | vless | `159.89.87.21:28190` | 138 ms | 1204 ms | - |

> 仅展示前 50 个，共 725 个；完整列表见 `sub/nodes.txt`。
