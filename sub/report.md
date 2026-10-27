# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-28 05:56:52+0800`

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
| 抓取链接 | 19680 |
| 去重后节点 | 8076 |
| TCP 预筛剔除 | 3840 |
| 真连接测试 | 8076 |
| 测试通过 | 723 |
| **最终保留** | **723** |
| 耗时 | 291.9 秒 |

> 解析阶段跳过：重复 11578、协议未启用 0、无法解析 26

## 协议分布

vless 329 · ss 156 · vmess 156 · trojan 79 · hysteria2 3

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 723 个节点中，有 **623** 个能经代理访问到国内目标站，**100** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vless | `47.253.226.114:443` | 37 ms | 926 ms | - |
| 2 | EPODONIOS | ss | `198.98.53.130:443` | 41 ms | 1059 ms | - |
| 3 | EPODONIOS | vless | `47.253.226.114:443` | 45 ms | 933 ms | - |
| 4 | EPODONIOS | vless | `88.216.69.253:443` | 50 ms | 1354 ms | - |
| 5 | EPODONIOS | vless | `172.64.150.28:2082` | 56 ms | 1576 ms | - |
| 6 | EPODONIOS | vless | `172.64.150.28:2082` | 57 ms | 1032 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 177 | vless | `104.18.45.38:443` | 59 ms | 2547 ms | - |
| 8 | EPODONIOS | vless | `172.64.150.28:2082` | 60 ms | 1054 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 205 | vless | `8.47.69.60:443` | 62 ms | 1373 ms | - |
| 10 | EPODONIOS | vless | `188.164.248.216:443` | 63 ms | 2755 ms | - |
| 11 | EPODONIOS | vless | `188.164.248.216:443` | 64 ms | 1251 ms | - |
| 12 | ⚡ b2n.ir/v2ray-configs / 519 | vless | `104.21.221.158:443` | 64 ms | 1156 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 191 | vless | `104.18.45.38:443` | 64 ms | 1109 ms | - |
| 14 | EPODONIOS | vless | `172.64.152.241:443` | 66 ms | 1317 ms | - |
| 15 | EPODONIOS | vless | `cf.877774.xyz:443` | 67 ms | 1556 ms | - |
| 16 | EPODONIOS | trojan | `66.163.122.7:443` | 71 ms | 914 ms | - |
| 17 | EPODONIOS | vless | `195.123.235.177:443` | 71 ms | 807 ms | - |
| 18 | EPODONIOS | vless | `104.18.41.190:443` | 71 ms | 1632 ms | - |
| 19 | EPODONIOS | vless | `172.64.146.66:443` | 73 ms | 2026 ms | - |
| 20 | EPODONIOS | vless | `185.95.231.156:443` | 74 ms | 1340 ms | - |
| 21 | EPODONIOS | vless | `104.18.47.73:443` | 74 ms | 2509 ms | - |
| 22 | EPODONIOS | vless | `169.40.42.89:443` | 74 ms | 1316 ms | - |
| 23 | ⚡ b2n.ir/v2ray-configs / 989 | vless | `172.66.1.36:443` | 74 ms | 1114 ms | - |
| 24 | EPODONIOS | vless | `cf.877774.xyz:443` | 75 ms | 1262 ms | - |
| 25 | EPODONIOS | vless | `cf.877774.xyz:443` | 75 ms | 1569 ms | - |
| 26 | EPODONIOS | vmess | `67.220.95.3:18000` | 75 ms | 1140 ms | - |
| 27 | EPODONIOS | vless | `104.18.40.100:443` | 77 ms | 3114 ms | - |
| 28 | 🇺🇸US-66.163.122.81-0570 | trojan | `66.163.122.81:443` | 77 ms | 890 ms | - |
| 29 | EPODONIOS | vless | `169.40.42.225:443` | 79 ms | 1117 ms | - |
| 30 | EPODONIOS | vless | `169.40.42.235:443` | 79 ms | 1330 ms | - |
| 31 | EPODONIOS | vmess | `67.220.95.3:18000` | 80 ms | 1054 ms | - |
| 32 | EPODONIOS | vless | `172.64.152.241:443` | 85 ms | 1336 ms | - |
| 33 | EPODONIOS | vless | `169.40.42.168:443` | 85 ms | 1157 ms | - |
| 34 | EPODONIOS | vless | `172.66.0.162:443` | 90 ms | 不可达 | - |
| 35 | EPODONIOS | vless | `169.40.42.225:443` | 91 ms | 1138 ms | - |
| 36 | EPODONIOS | vless | `169.40.42.231:443` | 92 ms | 1195 ms | - |
| 37 | EPODONIOS | vless | `104.17.154.123:443` | 93 ms | 1077 ms | - |
| 38 | CA 🇨🇦 / @Raydikalx / BA5E42 | vmess | `23.162.200.198:18000` | 93 ms | 1488 ms | - |
| 39 | EPODONIOS | vless | `172.67.76.40:443` | 95 ms | 1760 ms | - |
| 40 | EPODONIOS | vless | `172.64.158.170:443` | 97 ms | 1476 ms | - |
| 41 | CA 🇨🇦 / @Raydikalx / 8F8AB8 | vmess | `134.195.196.211:18000` | 98 ms | 1514 ms | - |
| 42 | EPODONIOS | vless | `172.64.152.241:443` | 99 ms | 1368 ms | - |
| 43 | EPODONIOS | vless | `chatgpt.com:443` | 99 ms | 1055 ms | - |
| 44 | 未知48 3.0MB/s | vmess | `23.162.200.198:18000` | 99 ms | 1212 ms | - |
| 45 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 100 ms | 1181 ms | - |
| 46 | EPODONIOS | ss | `37.19.198.236:443` | 101 ms | 953 ms | - |
| 47 | 🇺🇸US-216.152.155.176-0538 | trojan | `216.152.155.176:443` | 103 ms | 907 ms | - |
| 48 | EPODONIOS | vmess | `134.195.196.211:18000` | 105 ms | 1440 ms | - |
| 49 | EPODONIOS | ss | `185.215.132.18:19999` | 108 ms | 不可达 | - |
| 50 | EPODONIOS | ss | `185.215.132.9:19999` | 110 ms | 1956 ms | - |

> 仅展示前 50 个，共 723 个；完整列表见 `sub/nodes.txt`。
