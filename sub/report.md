# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-24 18:28:08+0800`

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
| 抓取链接 | 19879 |
| 去重后节点 | 8056 |
| TCP 预筛剔除 | 3922 |
| 真连接测试 | 8056 |
| 测试通过 | 626 |
| **最终保留** | **626** |
| 耗时 | 308.5 秒 |

> 解析阶段跳过：重复 11795、协议未启用 0、无法解析 28

## 协议分布

vless 330 · ss 141 · vmess 113 · trojan 38 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 626 个节点中，有 **515** 个能经代理访问到国内目标站，**111** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `169.197.142.22:18000` | 33 ms | 931 ms | - |
| 2 | US 🇺🇸 / @Raydikalx / B79C28 | vmess | `169.197.142.22:18000` | 33 ms | 674 ms | - |
| 3 | EPODONIOS | vless | `172.64.150.43:8080` | 49 ms | 741 ms | - |
| 4 | EPODONIOS | vless | `172.64.150.28:2082` | 50 ms | 753 ms | - |
| 5 | ⚡ b2n.ir/v2ray-configs / 163 | vless | `172.64.153.61:443` | 51 ms | 867 ms | - |
| 6 | US 🇺🇸 / @Raydikalx / CE2CEA | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 52 ms | 663 ms | - |
| 7 | EPODONIOS | vless | `188.114.97.6:443` | 54 ms | 712 ms | - |
| 8 | EPODONIOS | vless | `172.66.0.162:443` | 55 ms | 721 ms | - |
| 9 | EPODONIOS | vless | `162.159.135.234:443` | 56 ms | 956 ms | - |
| 10 | EPODONIOS | vless | `188.114.97.6:443` | 56 ms | 695 ms | - |
| 11 | EPODONIOS | vless | `188.114.98.0:443` | 57 ms | 704 ms | - |
| 12 | EPODONIOS | vless | `172.64.158.170:443` | 57 ms | 823 ms | - |
| 13 | EPODONIOS | vless | `188.114.97.6:443` | 58 ms | 719 ms | - |
| 14 | EPODONIOS | vless | `cf.877774.xyz:443` | 58 ms | 734 ms | - |
| 15 | EPODONIOS | vless | `104.20.5.134:443` | 59 ms | 856 ms | - |
| 16 | EPODONIOS | vless | `172.64.154.211:443` | 59 ms | 716 ms | - |
| 17 | EPODONIOS | vless | `188.114.98.0:443` | 59 ms | 855 ms | - |
| 18 | EPODONIOS | vless | `172.64.150.43:443` | 60 ms | 714 ms | - |
| 19 | EPODONIOS | vless | `188.114.98.0:443` | 60 ms | 708 ms | - |
| 20 | EPODONIOS | vless | `cf.877774.xyz:443` | 60 ms | 751 ms | - |
| 21 | ⚡ b2n.ir/v2ray-configs / 897 | vless | `104.24.197.20:443` | 61 ms | 688 ms | - |
| 22 | EPODONIOS | vless | `188.114.96.6:443` | 63 ms | 751 ms | - |
| 23 | EPODONIOS | vless | `45.63.53.81:443` | 66 ms | 821 ms | - |
| 24 | ⚡ b2n.ir/v2ray-configs / 73 | vless | `104.18.33.97:443` | 67 ms | 694 ms | - |
| 25 | ⚡ b2n.ir/v2ray-configs / 524 | vless | `104.18.37.127:443` | 67 ms | 1024 ms | - |
| 26 | EPODONIOS | vless | `45.32.69.110:443` | 69 ms | 674 ms | - |
| 27 | EPODONIOS | vless | `www.speedtest.net:443` | 70 ms | 1049 ms | - |
| 28 | EPODONIOS | vmess | `84.17.41.2:18000` | 71 ms | 1012 ms | - |
| 29 | EPODONIOS | ss | `95.215.201.18:19999` | 72 ms | 1001 ms | - |
| 30 | EPODONIOS | vless | `188.114.98.0:443` | 75 ms | 733 ms | - |
| 31 | EPODONIOS | vless | `23.95.222.127:8443` | 76 ms | 828 ms | - |
| 32 | EPODONIOS | vless | `154.40.55.185:443` | 76 ms | 732 ms | - |
| 33 | EPODONIOS | vless | `188.114.98.0:443` | 78 ms | 707 ms | - |
| 34 | EPODONIOS | vless | `172.64.152.241:443` | 80 ms | 685 ms | - |
| 35 | US 🇺🇸 / @Raydikalx / 110621 | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 81 ms | 653 ms | - |
| 36 | EPODONIOS | vless | `188.114.98.0:443` | 83 ms | 735 ms | - |
| 37 | EPODONIOS | vmess | `129.146.77.248:39495` | 84 ms | 1405 ms | - |
| 38 | US 🇺🇸 / @Raydikalx / 452ED5 | vmess | `129.146.77.248:39495` | 84 ms | 1025 ms | - |
| 39 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 85 ms | 不可达 | - |
| 40 | EPODONIOS | vless | `15.204.97.197:23576` | 87 ms | 不可达 | - |
| 41 | EPODONIOS | vless | `15.204.97.206:23576` | 87 ms | 不可达 | - |
| 42 | EPODONIOS | vless | `15.204.97.206:23576` | 89 ms | 不可达 | - |
| 43 | EPODONIOS | vless | `104.18.35.86:8080` | 91 ms | 812 ms | - |
| 44 | EPODONIOS | vless | `15.204.97.197:23576` | 92 ms | 不可达 | - |
| 45 | EPODONIOS | vless | `188.114.98.0:443` | 93 ms | 874 ms | - |
| 46 | EPODONIOS | vless | `144.202.126.147:443` | 97 ms | 704 ms | - |
| 47 | EPODONIOS | vless | `188.114.98.0:443` | 97 ms | 736 ms | - |
| 48 | EPODONIOS | vless | `15.204.97.209:23576` | 99 ms | 不可达 | - |
| 49 | EPODONIOS | vless | `15.204.97.214:23576` | 103 ms | 不可达 | - |
| 50 | EPODONIOS | vless | `45.76.172.197:443` | 103 ms | 844 ms | - |

> 仅展示前 50 个，共 626 个；完整列表见 `sub/nodes.txt`。
