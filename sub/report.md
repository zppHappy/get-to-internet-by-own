# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-23 00:48:31+0800`

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
| 抓取链接 | 19648 |
| 去重后节点 | 8034 |
| TCP 预筛剔除 | 3960 |
| 真连接测试 | 8034 |
| 测试通过 | 714 |
| **最终保留** | **714** |
| 耗时 | 309.1 秒 |

> 解析阶段跳过：重复 11587、协议未启用 0、无法解析 27

## 协议分布

vless 388 · ss 143 · vmess 100 · trojan 76 · hysteria2 7

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 714 个节点中，有 **576** 个能经代理访问到国内目标站，**138** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `129.146.77.248:39495` | 24 ms | 1490 ms | - |
| 2 | EPODONIOS | ss | `95.215.201.18:19999` | 26 ms | 705 ms | - |
| 3 | EPODONIOS | vless | `104.18.35.86:8080` | 72 ms | 1320 ms | - |
| 4 | EPODONIOS | vless | `172.64.150.28:2082` | 78 ms | 789 ms | - |
| 5 | EPODONIOS | ss | `173.244.56.6:443` | 82 ms | 930 ms | - |
| 6 | EPODONIOS | ss | `156.146.38.167:443` | 90 ms | 893 ms | - |
| 7 | EPODONIOS | ss | `156.146.38.168:443` | 90 ms | 1037 ms | - |
| 8 | EPODONIOS | ss | `156.146.38.169:443` | 90 ms | 1035 ms | - |
| 9 | ⚡ b2n.ir/v2ray-configs / 150 | vless | `188.114.98.0:443` | 94 ms | 871 ms | - |
| 10 | EPODONIOS | vless | `188.114.97.6:443` | 97 ms | 790 ms | - |
| 11 | EPODONIOS | vless | `104.18.0.181:2082` | 97 ms | 758 ms | - |
| 12 | EPODONIOS | vless | `162.159.135.234:443` | 98 ms | 787 ms | - |
| 13 | EPODONIOS | vless | `104.18.20.69:443` | 100 ms | 770 ms | - |
| 14 | EPODONIOS | vless | `188.114.97.6:443` | 100 ms | 784 ms | - |
| 15 | EPODONIOS | ss | `156.146.38.170:443` | 100 ms | 862 ms | - |
| 16 | EPODONIOS | vless | `188.114.96.6:443` | 101 ms | 864 ms | - |
| 17 | EPODONIOS | vless | `172.66.0.162:443` | 101 ms | 786 ms | - |
| 18 | EPODONIOS | vless | `104.20.6.134:443` | 106 ms | 792 ms | - |
| 19 | EPODONIOS | vless | `188.114.98.0:443` | 106 ms | 788 ms | - |
| 20 | EPODONIOS | vless | `104.18.41.190:443` | 106 ms | 798 ms | - |
| 21 | EPODONIOS | vless | `188.114.98.0:443` | 108 ms | 1594 ms | - |
| 22 | EPODONIOS | vless | `188.114.98.0:443` | 111 ms | 800 ms | - |
| 23 | EPODONIOS | vless | `172.67.155.65:2053` | 112 ms | 915 ms | - |
| 24 | EPODONIOS | vless | `172.64.152.241:443` | 113 ms | 835 ms | - |
| 25 | EPODONIOS | vless | `104.18.0.181:2082` | 114 ms | 1859 ms | - |
| 26 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 115 ms | 1312 ms | - |
| 27 | EPODONIOS | vless | `104.18.43.174:443` | 116 ms | 811 ms | - |
| 28 | EPODONIOS | vless | `188.114.98.0:443` | 117 ms | 837 ms | - |
| 29 | EPODONIOS | vless | `cf.877774.xyz:443` | 118 ms | 798 ms | - |
| 30 | EPODONIOS | vless | `86.109.75.183:443` | 119 ms | 1264 ms | - |
| 31 | EPODONIOS | vless | `172.64.150.43:443` | 119 ms | 791 ms | - |
| 32 | EPODONIOS | vless | `104.21.91.244:443` | 119 ms | 775 ms | - |
| 33 | EPODONIOS | vless | `188.114.98.0:443` | 119 ms | 820 ms | - |
| 34 | EPODONIOS | vless | `172.67.155.65:8443` | 120 ms | 778 ms | - |
| 35 | EPODONIOS | vless | `172.66.0.162:443` | 121 ms | 781 ms | - |
| 36 | EPODONIOS | vless | `104.21.91.244:443` | 121 ms | 805 ms | - |
| 37 | EPODONIOS | vless | `172.67.155.65:2053` | 121 ms | 788 ms | - |
| 38 | EPODONIOS | vless | `188.114.98.0:443` | 122 ms | 991 ms | - |
| 39 | EPODONIOS | vless | `188.114.97.6:443` | 122 ms | 837 ms | - |
| 40 | EPODONIOS | vless | `188.114.98.0:443` | 125 ms | 800 ms | - |
| 41 | EPODONIOS | vless | `188.114.97.6:443` | 127 ms | 791 ms | - |
| 42 | EPODONIOS | vless | `172.64.150.43:8080` | 127 ms | 784 ms | - |
| 43 | EPODONIOS | vless | `188.114.97.6:443` | 128 ms | 1022 ms | - |
| 44 | EPODONIOS | vless | `188.114.98.0:443` | 128 ms | 804 ms | - |
| 45 | ⚡ b2n.ir/v2ray-configs / 737 | vless | `188.114.97.6:443` | 128 ms | 893 ms | - |
| 46 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 128 ms | 3876 ms | - |
| 47 | EPODONIOS | vless | `172.67.155.65:8443` | 129 ms | 822 ms | - |
| 48 | EPODONIOS | vless | `172.67.155.65:8443` | 130 ms | 777 ms | - |
| 49 | EPODONIOS | vless | `cf.090227.xyz:443` | 131 ms | 808 ms | - |
| 50 | EPODONIOS | vless | `cf.877774.xyz:443` | 133 ms | 767 ms | - |

> 仅展示前 50 个，共 714 个；完整列表见 `sub/nodes.txt`。
