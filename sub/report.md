# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-23 05:19:57+0800`

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
| 抓取链接 | 19671 |
| 去重后节点 | 8004 |
| TCP 预筛剔除 | 3920 |
| 真连接测试 | 8004 |
| 测试通过 | 731 |
| **最终保留** | **731** |
| 耗时 | 294.6 秒 |

> 解析阶段跳过：重复 11660、协议未启用 0、无法解析 7

## 协议分布

vless 393 · ss 147 · vmess 123 · trojan 62 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 731 个节点中，有 **629** 个能经代理访问到国内目标站，**102** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / B79C28 | vmess | `169.197.142.22:18000` | 36 ms | 905 ms | - |
| 2 | EPODONIOS | vless | `47.251.108.158:443` | 61 ms | 651 ms | - |
| 3 | EPODONIOS | vless | `172.64.150.43:443` | 65 ms | 901 ms | - |
| 4 | EPODONIOS | vless | `172.66.0.162:443` | 67 ms | 1097 ms | - |
| 5 | EPODONIOS | vless | `104.21.91.244:443` | 68 ms | 1193 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 474 | vless | `172.64.150.43:8080` | 68 ms | 1321 ms | - |
| 7 | EPODONIOS | vless | `www.speedtest.net:443` | 69 ms | 1009 ms | - |
| 8 | EPODONIOS | vless | `188.114.98.0:443` | 70 ms | 707 ms | - |
| 9 | US 🇺🇸 / @Raydikalx / 18811D | vmess | `129.146.143.80:48111` | 70 ms | 920 ms | - |
| 10 | EPODONIOS | vless | `104.18.32.47:443` | 71 ms | 700 ms | - |
| 11 | EPODONIOS | vless | `162.159.135.234:443` | 71 ms | 705 ms | - |
| 12 | EPODONIOS | vless | `188.114.97.6:443` | 74 ms | 697 ms | - |
| 13 | EPODONIOS | vless | `188.114.98.0:443` | 74 ms | 880 ms | - |
| 14 | EPODONIOS | vless | `cf.130519.xyz:443` | 74 ms | 938 ms | - |
| 15 | EPODONIOS | ss | `95.215.201.18:19999` | 75 ms | 1166 ms | - |
| 16 | EPODONIOS | vless | `188.114.98.0:443` | 75 ms | 739 ms | - |
| 17 | EPODONIOS | vless | `172.67.155.65:2053` | 75 ms | 1568 ms | - |
| 18 | ⚡ b2n.ir/v2ray-configs / 807 | vless | `188.114.97.6:443` | 76 ms | 1202 ms | - |
| 19 | EPODONIOS | vless | `188.114.97.6:443` | 78 ms | 794 ms | - |
| 20 | EPODONIOS | vless | `172.64.152.241:443` | 78 ms | 743 ms | - |
| 21 | EPODONIOS | vless | `188.114.98.0:443` | 79 ms | 708 ms | - |
| 22 | EPODONIOS | vless | `188.114.97.6:443` | 80 ms | 906 ms | - |
| 23 | EPODONIOS | vless | `188.114.98.0:443` | 80 ms | 882 ms | - |
| 24 | EPODONIOS | vless | `172.67.155.65:2053` | 80 ms | 746 ms | - |
| 25 | EPODONIOS | vless | `188.114.98.0:443` | 81 ms | 741 ms | - |
| 26 | EPODONIOS | vless | `172.66.0.162:443` | 83 ms | 1142 ms | - |
| 27 | EPODONIOS | vless | `cf.877774.xyz:443` | 83 ms | 922 ms | - |
| 28 | ⚡ b2n.ir/v2ray-configs / 350 | vless | `104.20.6.134:443` | 83 ms | 806 ms | - |
| 29 | EPODONIOS | vless | `172.64.150.28:2082` | 84 ms | 743 ms | - |
| 30 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 84 ms | 1110 ms | - |
| 31 | EPODONIOS | vless | `104.21.91.244:443` | 88 ms | 757 ms | - |
| 32 | EPODONIOS | vless | `172.67.155.65:2053` | 89 ms | 867 ms | - |
| 33 | EPODONIOS | vless | `188.114.98.0:443` | 90 ms | 1828 ms | - |
| 34 | EPODONIOS | vless | `188.114.98.0:443` | 91 ms | 740 ms | - |
| 35 | EPODONIOS | vless | `172.67.155.65:2053` | 92 ms | 752 ms | - |
| 36 | US 🇺🇸 / @Raydikalx / CE2CEA | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 92 ms | 698 ms | - |
| 37 | EPODONIOS | vless | `188.114.98.0:443` | 93 ms | 772 ms | - |
| 38 | EPODONIOS | vless | `15.204.97.216:23576` | 95 ms | 不可达 | - |
| 39 | EPODONIOS | vless | `15.204.97.195:23576` | 96 ms | 不可达 | - |
| 40 | EPODONIOS | vless | `15.204.97.209:23576` | 96 ms | 不可达 | - |
| 41 | EPODONIOS | vless | `15.204.97.219:23576` | 98 ms | 不可达 | - |
| 42 | US 🇺🇸 / @Raydikalx / 452ED5 | vmess | `129.146.77.248:39495` | 98 ms | 1142 ms | - |
| 43 | EPODONIOS | vless | `15.204.97.206:23576` | 99 ms | 不可达 | - |
| 44 | EPODONIOS | vless | `15.204.97.216:23576` | 99 ms | 不可达 | - |
| 45 | EPODONIOS | vless | `172.64.155.209:443` | 104 ms | 756 ms | - |
| 46 | EPODONIOS | vless | `cf.090227.xyz:443` | 104 ms | 768 ms | - |
| 47 | EPODONIOS | vless | `188.114.98.0:443` | 107 ms | 838 ms | - |
| 48 | EPODONIOS | vless | `172.66.47.10:443` | 108 ms | 731 ms | - |
| 49 | EPODONIOS | vless | `188.114.98.0:443` | 109 ms | 741 ms | - |
| 50 | EPODONIOS | vless | `188.114.97.6:443` | 109 ms | 758 ms | - |

> 仅展示前 50 个，共 731 个；完整列表见 `sub/nodes.txt`。
