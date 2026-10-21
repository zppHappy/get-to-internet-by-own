# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-22 05:23:46+0800`

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
| 抓取链接 | 19571 |
| 去重后节点 | 7951 |
| TCP 预筛剔除 | 3840 |
| 真连接测试 | 7951 |
| 测试通过 | 761 |
| **最终保留** | **761** |
| 耗时 | 301.6 秒 |

> 解析阶段跳过：重复 11593、协议未启用 0、无法解析 27

## 协议分布

vless 406 · ss 144 · vmess 117 · trojan 88 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 761 个节点中，有 **654** 个能经代理访问到国内目标站，**107** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 35 ms | 833 ms | - |
| 2 | EPODONIOS | vless | `86.109.75.183:443` | 53 ms | 1151 ms | - |
| 3 | EPODONIOS | vless | `45.78.7.153:443` | 63 ms | 732 ms | - |
| 4 | EPODONIOS | vless | `188.114.97.6:443` | 68 ms | 1050 ms | - |
| 5 | EPODONIOS | vless | `188.114.98.0:443` | 70 ms | 769 ms | - |
| 6 | EPODONIOS | vless | `188.114.98.0:443` | 70 ms | 944 ms | - |
| 7 | EPODONIOS | vless | `188.114.98.0:443` | 71 ms | 876 ms | - |
| 8 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 71 ms | 955 ms | - |
| 9 | EPODONIOS | vless | `188.114.97.6:443` | 72 ms | 692 ms | - |
| 10 | EPODONIOS | vless | `188.114.98.0:443` | 72 ms | 915 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 425 | vless | `188.114.97.6:443` | 72 ms | 741 ms | - |
| 12 | EPODONIOS | ss | `95.215.201.18:19999` | 73 ms | 783 ms | - |
| 13 | EPODONIOS | vless | `162.159.135.234:443` | 74 ms | 705 ms | - |
| 14 | EPODONIOS | vless | `172.64.150.43:443` | 77 ms | 682 ms | - |
| 15 | EPODONIOS | vless | `172.64.150.28:2082` | 77 ms | 727 ms | - |
| 16 | US 🇺🇸 / @Raydikalx / CE2CEA | vmess | `rib9jxayoqjgn2kw.v.3dns.vip:443` | 78 ms | 652 ms | - |
| 17 | EPODONIOS | vless | `172.67.75.172:443` | 79 ms | 788 ms | - |
| 18 | EPODONIOS | vless | `104.21.91.244:443` | 79 ms | 865 ms | - |
| 19 | EPODONIOS | vless | `188.114.98.0:443` | 81 ms | 719 ms | - |
| 20 | EPODONIOS | vless | `188.114.98.0:443` | 82 ms | 718 ms | - |
| 21 | EPODONIOS | vless | `104.21.91.244:443` | 82 ms | 1153 ms | - |
| 22 | ⚡ b2n.ir/v2ray-configs / 563 | vless | `188.114.97.6:443` | 82 ms | 846 ms | - |
| 23 | EPODONIOS | vless | `188.114.98.0:443` | 84 ms | 675 ms | - |
| 24 | ⚡ b2n.ir/v2ray-configs / 288 | vless | `188.114.97.6:443` | 86 ms | 892 ms | - |
| 25 | EPODONIOS | vless | `15.204.97.206:23576` | 87 ms | 不可达 | - |
| 26 | EPODONIOS | vless | `15.204.97.219:23576` | 87 ms | 不可达 | - |
| 27 | EPODONIOS | vless | `15.204.97.206:23576` | 88 ms | 不可达 | - |
| 28 | EPODONIOS | vless | `15.204.97.197:23576` | 89 ms | 不可达 | - |
| 29 | EPODONIOS | vmess | `129.146.77.248:39495` | 90 ms | 1046 ms | - |
| 30 | EPODONIOS | vless | `188.114.97.6:443` | 92 ms | 852 ms | - |
| 31 | ⚡ b2n.ir/v2ray-configs / 229 | vless | `b2n.ir:443` | 93 ms | 708 ms | - |
| 32 | EPODONIOS | vless | `15.204.97.219:23576` | 98 ms | 不可达 | - |
| 33 | EPODONIOS | vless | `104.21.91.244:443` | 98 ms | 840 ms | - |
| 34 | EPODONIOS | vless | `15.204.97.216:23576` | 99 ms | 不可达 | - |
| 35 | EPODONIOS | vless | `104.21.91.244:443` | 103 ms | 706 ms | - |
| 36 | ⚡ b2n.ir/v2ray-configs / 865 | vless | `www.speedtest.net:443` | 103 ms | 696 ms | - |
| 37 | EPODONIOS | vless | `172.66.47.10:443` | 104 ms | 942 ms | - |
| 38 | ⚡ b2n.ir/v2ray-configs / 938 | vless | `188.114.97.6:443` | 104 ms | 915 ms | - |
| 39 | EPODONIOS | vless | `cf.877774.xyz:443` | 106 ms | 726 ms | - |
| 40 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 107 ms | 不可达 | - |
| 41 | ⚡ b2n.ir/v2ray-configs / 380 | vless | `172.67.155.65:8443` | 108 ms | 755 ms | - |
| 42 | EPODONIOS | ss | `173.244.56.6:443` | 117 ms | 808 ms | - |
| 43 | EPODONIOS | vless | `104.18.0.181:2082` | 119 ms | 683 ms | - |
| 44 | CA 🇨🇦 / @Raydikalx / 8BB1EE | vmess | `us16-4.998998.best:443` | 123 ms | 769 ms | - |
| 45 | EPODONIOS | vless | `172.64.152.241:443` | 124 ms | 712 ms | - |
| 46 | EPODONIOS | vless | `104.18.0.181:2082` | 130 ms | 709 ms | - |
| 47 | EPODONIOS | vless | `188.114.98.0:443` | 131 ms | 686 ms | - |
| 48 | ⚡ b2n.ir/v2ray-configs / 300 | vless | `104.21.91.244:443` | 131 ms | 706 ms | - |
| 49 | EPODONIOS | ss | `156.146.38.167:443` | 133 ms | 925 ms | - |
| 50 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 133 ms | 不可达 | - |

> 仅展示前 50 个，共 761 个；完整列表见 `sub/nodes.txt`。
