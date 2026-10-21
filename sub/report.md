# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-22 00:47:31+0800`

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
| 抓取链接 | 19702 |
| 去重后节点 | 8003 |
| TCP 预筛剔除 | 3876 |
| 真连接测试 | 8003 |
| 测试通过 | 708 |
| **最终保留** | **708** |
| 耗时 | 311.2 秒 |

> 解析阶段跳过：重复 11674、协议未启用 0、无法解析 25

## 协议分布

vless 377 · ss 153 · vmess 101 · trojan 72 · hysteria2 5

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 708 个节点中，有 **603** 个能经代理访问到国内目标站，**105** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `129.146.77.248:39495` | 26 ms | 1157 ms | - |
| 2 | EPODONIOS | ss | `95.215.201.18:19999` | 28 ms | 722 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.167:443` | 85 ms | 859 ms | - |
| 4 | EPODONIOS | vless | `172.64.150.28:2082` | 85 ms | 789 ms | - |
| 5 | EPODONIOS | vless | `104.18.0.181:2082` | 87 ms | 802 ms | - |
| 6 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 88 ms | 718 ms | - |
| 7 | EPODONIOS | ss | `156.146.38.169:443` | 91 ms | 893 ms | - |
| 8 | EPODONIOS | vless | `188.114.98.0:443` | 91 ms | 976 ms | - |
| 9 | EPODONIOS | vless | `188.114.98.0:443` | 91 ms | 739 ms | - |
| 10 | EPODONIOS | vless | `188.114.97.6:443` | 94 ms | 920 ms | - |
| 11 | EPODONIOS | vless | `172.64.150.28:2082` | 98 ms | 759 ms | - |
| 12 | US 🇺🇸 / @Raydikalx / E38DDB | vmess | `169.197.142.22:18000` | 98 ms | 1523 ms | - |
| 13 | EPODONIOS | vless | `188.114.98.0:443` | 100 ms | 979 ms | - |
| 14 | ⚡ b2n.ir/v2ray-configs / 196 | vless | `104.18.35.86:2082` | 102 ms | 736 ms | - |
| 15 | EPODONIOS | vless | `188.114.98.0:443` | 104 ms | 762 ms | - |
| 16 | EPODONIOS | vless | `188.114.98.0:443` | 109 ms | 784 ms | - |
| 17 | EPODONIOS | vless | `188.114.98.0:443` | 111 ms | 751 ms | - |
| 18 | EPODONIOS | vless | `188.114.98.0:443` | 111 ms | 801 ms | - |
| 19 | EPODONIOS | vless | `172.66.0.162:443` | 111 ms | 843 ms | - |
| 20 | EPODONIOS | vless | `104.18.0.181:2082` | 112 ms | 793 ms | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 113 ms | 784 ms | - |
| 22 | EPODONIOS | vless | `www.speedtest.net:443` | 113 ms | 890 ms | - |
| 23 | EPODONIOS | vless | `104.18.35.86:8080` | 117 ms | 764 ms | - |
| 24 | EPODONIOS | vless | `162.159.135.234:443` | 118 ms | 746 ms | - |
| 25 | EPODONIOS | vless | `188.114.97.6:443` | 120 ms | 773 ms | - |
| 26 | EPODONIOS | vless | `172.67.155.65:2053` | 126 ms | 830 ms | - |
| 27 | US 🇺🇸 / @Raydikalx / FC15CE | vmess | `84.17.41.2:18000` | 127 ms | 1208 ms | - |
| 28 | EPODONIOS | vless | `172.64.152.241:443` | 128 ms | 756 ms | - |
| 29 | EPODONIOS | ss | `156.146.38.170:443` | 128 ms | 865 ms | - |
| 30 | ⚡ b2n.ir/v2ray-configs / 82 | vless | `162.159.130.234:443` | 129 ms | 782 ms | - |
| 31 | EPODONIOS | vless | `172.67.75.172:443` | 130 ms | 748 ms | - |
| 32 | ⚡ b2n.ir/v2ray-configs / 137 | vless | `188.114.97.6:443` | 135 ms | 837 ms | - |
| 33 | ⚡ b2n.ir/v2ray-configs / 565 | vless | `188.114.97.6:443` | 136 ms | 802 ms | - |
| 34 | EPODONIOS | vless | `188.114.98.0:443` | 138 ms | 791 ms | - |
| 35 | EPODONIOS | vless | `104.18.43.174:443` | 138 ms | 823 ms | - |
| 36 | EPODONIOS | vless | `104.18.43.174:443` | 141 ms | 809 ms | - |
| 37 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 142 ms | 1151 ms | - |
| 38 | ⚡ b2n.ir/v2ray-configs / 278 | vless | `104.21.91.244:443` | 144 ms | 764 ms | - |
| 39 | EPODONIOS | vless | `15.204.97.197:23576` | 145 ms | 1497 ms | - |
| 40 | EPODONIOS | vless | `104.21.91.244:443` | 145 ms | 758 ms | - |
| 41 | EPODONIOS | vless | `15.204.97.206:23576` | 147 ms | 不可达 | - |
| 42 | EPODONIOS | vless | `15.204.97.219:23576` | 147 ms | 不可达 | - |
| 43 | EPODONIOS | vless | `104.18.41.190:443` | 147 ms | 800 ms | - |
| 44 | EPODONIOS | vless | `172.64.150.43:443` | 148 ms | 741 ms | - |
| 45 | ⚡ b2n.ir/v2ray-configs / 97 | vless | `188.114.97.6:443` | 148 ms | 789 ms | - |
| 46 | ⚡ b2n.ir/v2ray-configs / 845 | vless | `104.18.41.190:443` | 149 ms | 800 ms | - |
| 47 | EPODONIOS | vless | `188.114.97.6:2053` | 150 ms | 808 ms | - |
| 48 | EPODONIOS | vless | `188.114.97.6:443` | 150 ms | 826 ms | - |
| 49 | EPODONIOS | vless | `104.21.91.244:443` | 151 ms | 826 ms | - |
| 50 | EPODONIOS | vless | `15.204.97.206:23576` | 153 ms | 不可达 | - |

> 仅展示前 50 个，共 708 个；完整列表见 `sub/nodes.txt`。
