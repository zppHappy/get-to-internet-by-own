# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-24 23:32:50+0800`

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
| 抓取链接 | 19920 |
| 去重后节点 | 8093 |
| TCP 预筛剔除 | 3963 |
| 真连接测试 | 8093 |
| 测试通过 | 616 |
| **最终保留** | **616** |
| 耗时 | 291.4 秒 |

> 解析阶段跳过：重复 11805、协议未启用 0、无法解析 22

## 协议分布

vless 335 · ss 141 · vmess 103 · trojan 34 · hysteria2 3

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 616 个节点中，有 **515** 个能经代理访问到国内目标站，**101** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `37.19.198.236:443` | 41 ms | 1036 ms | - |
| 2 | EPODONIOS | ss | `37.19.198.244:443` | 41 ms | 924 ms | - |
| 3 | EPODONIOS | ss | `37.19.198.243:443` | 43 ms | 1029 ms | - |
| 4 | US 🇺🇸 / @Raydikalx / F2583B | vmess | `67.220.85.46:18000` | 48 ms | 1258 ms | - |
| 5 | EPODONIOS | vless | `172.64.150.43:443` | 50 ms | 981 ms | - |
| 6 | EPODONIOS | vless | `188.114.96.6:443` | 50 ms | 1003 ms | - |
| 7 | EPODONIOS | vless | `172.64.152.241:443` | 53 ms | 962 ms | - |
| 8 | EPODONIOS | vless | `172.66.1.36:443` | 53 ms | 969 ms | - |
| 9 | EPODONIOS | vless | `172.64.154.211:443` | 54 ms | 993 ms | - |
| 10 | EPODONIOS | vless | `188.114.98.0:443` | 54 ms | 1172 ms | - |
| 11 | EPODONIOS | vless | `162.159.135.234:443` | 55 ms | 1002 ms | - |
| 12 | EPODONIOS | vless | `172.66.0.162:443` | 55 ms | 1144 ms | - |
| 13 | EPODONIOS | vless | `188.114.96.6:443` | 56 ms | 960 ms | - |
| 14 | EPODONIOS | vless | `188.114.97.6:443` | 56 ms | 971 ms | - |
| 15 | US 🇺🇸 / @Raydikalx / 46741C | vmess | `67.220.85.46:18000` | 56 ms | 2182 ms | - |
| 16 | EPODONIOS | vless | `104.24.197.20:443` | 57 ms | 975 ms | - |
| 17 | EPODONIOS | vless | `104.18.45.38:443` | 57 ms | 1035 ms | - |
| 18 | EPODONIOS | trojan | `69.164.240.85:50875` | 57 ms | 1254 ms | - |
| 19 | EPODONIOS | vless | `172.64.150.28:2082` | 58 ms | 935 ms | - |
| 20 | EPODONIOS | vless | `159.89.87.21:28190` | 58 ms | 1244 ms | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 58 ms | 981 ms | - |
| 22 | EPODONIOS | vless | `172.64.150.43:443` | 60 ms | 966 ms | - |
| 23 | EPODONIOS | vmess | `67.220.95.3:18000` | 60 ms | 2395 ms | - |
| 24 | EPODONIOS | vless | `159.89.87.21:28190` | 61 ms | 1275 ms | - |
| 25 | EPODONIOS | vless | `188.164.248.216:443` | 61 ms | 1116 ms | - |
| 26 | EPODONIOS | vless | `104.24.197.20:443` | 62 ms | 944 ms | - |
| 27 | EPODONIOS | vmess | `67.220.95.3:18000` | 62 ms | 1453 ms | - |
| 28 | EPODONIOS | vless | `104.21.221.158:443` | 63 ms | 1158 ms | - |
| 29 | EPODONIOS | ss | `15.204.247.206:4444` | 63 ms | 1502 ms | - |
| 30 | ⚡ b2n.ir/v2ray-configs / 124 | vless | `172.64.153.61:443` | 63 ms | 967 ms | - |
| 31 | EPODONIOS | vless | `167.17.69.171:443` | 64 ms | 1039 ms | - |
| 32 | EPODONIOS | vless | `162.159.130.234:443` | 65 ms | 985 ms | - |
| 33 | EPODONIOS | vless | `195.123.235.177:443` | 65 ms | 991 ms | - |
| 34 | EPODONIOS | vless | `cf.877774.xyz:443` | 65 ms | 983 ms | - |
| 35 | US 🇺🇸 / @Raydikalx / 602935 | vmess | `67.220.95.3:18000` | 65 ms | 1492 ms | - |
| 36 | EPODONIOS | vless | `188.114.98.0:443` | 68 ms | 953 ms | - |
| 37 | EPODONIOS | vless | `104.20.5.134:443` | 69 ms | 1117 ms | - |
| 38 | EPODONIOS | vless | `169.40.42.235:443` | 69 ms | 2805 ms | - |
| 39 | EPODONIOS | vless | `162.159.130.234:443` | 70 ms | 1219 ms | - |
| 40 | EPODONIOS | vless | `88.216.69.253:443` | 70 ms | 938 ms | - |
| 41 | EPODONIOS | vless | `cf.877774.xyz:443` | 71 ms | 973 ms | - |
| 42 | EPODONIOS | vless | `185.95.231.156:443` | 72 ms | 1250 ms | - |
| 43 | EPODONIOS | vless | `169.40.42.104:443` | 72 ms | 1214 ms | - |
| 44 | EPODONIOS | vless | `169.40.42.224:443` | 73 ms | 1426 ms | - |
| 45 | EPODONIOS | vless | `169.40.42.89:443` | 73 ms | 1043 ms | - |
| 46 | EPODONIOS | vless | `www.speedtest.net:443` | 76 ms | 1594 ms | - |
| 47 | EPODONIOS | vless | `162.159.135.234:443` | 77 ms | 980 ms | - |
| 48 | EPODONIOS | vless | `169.40.42.168:443` | 77 ms | 1574 ms | - |
| 49 | EPODONIOS | vless | `169.40.42.231:443` | 80 ms | 1335 ms | - |
| 50 | EPODONIOS | vless | `172.64.150.43:8080` | 80 ms | 1042 ms | - |

> 仅展示前 50 个，共 616 个；完整列表见 `sub/nodes.txt`。
