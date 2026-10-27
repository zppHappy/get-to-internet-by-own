# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-27 23:15:14+0800`

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
| 抓取链接 | 19661 |
| 去重后节点 | 8058 |
| TCP 预筛剔除 | 3880 |
| 真连接测试 | 8058 |
| 测试通过 | 564 |
| **最终保留** | **564** |
| 耗时 | 329.1 秒 |

> 解析阶段跳过：重复 11575、协议未启用 0、无法解析 28

## 协议分布

vless 265 · ss 139 · vmess 105 · trojan 52 · hysteria2 3

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 564 个节点中，有 **407** 个能经代理访问到国内目标站，**157** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 32 ms | 1237 ms | - |
| 2 | EPODONIOS | trojan | `216.106.186.66:443` | 54 ms | 757 ms | - |
| 3 | EPODONIOS | trojan | `216.106.186.33:443` | 60 ms | 不可达 | - |
| 4 | EPODONIOS | vless | `15.204.97.219:23576` | 63 ms | 1511 ms | - |
| 5 | EPODONIOS | vless | `15.204.97.197:23576` | 66 ms | 不可达 | - |
| 6 | EPODONIOS | vless | `15.204.97.206:23576` | 66 ms | 不可达 | - |
| 7 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 66 ms | 不可达 | - |
| 8 | EPODONIOS | vless | `15.204.97.206:23576` | 67 ms | 不可达 | - |
| 9 | EPODONIOS | vless | `172.66.0.162:443` | 68 ms | 644 ms | - |
| 10 | EPODONIOS | ss | `149.22.95.183:443` | 68 ms | 765 ms | - |
| 11 | EPODONIOS | vless | `172.64.152.241:443` | 71 ms | 647 ms | - |
| 12 | EPODONIOS | vless | `15.204.97.216:23576` | 73 ms | 770 ms | - |
| 13 | EPODONIOS | vless | `cf.877774.xyz:443` | 73 ms | 633 ms | - |
| 14 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 74 ms | 不可达 | - |
| 15 | EPODONIOS | vless | `104.18.40.100:443` | 74 ms | 649 ms | - |
| 16 | EPODONIOS | vless | `172.64.150.28:2082` | 75 ms | 652 ms | - |
| 17 | EPODONIOS | vless | `cf.877774.xyz:443` | 76 ms | 692 ms | - |
| 18 | EPODONIOS | vless | `172.64.152.241:443` | 76 ms | 1610 ms | - |
| 19 | ⚡ b2n.ir/v2ray-configs / 308 | vless | `104.18.45.38:443` | 76 ms | 657 ms | - |
| 20 | EPODONIOS | vless | `51.81.203.63:443` | 77 ms | 1343 ms | - |
| 21 | EPODONIOS | vless | `chatgpt.com:443` | 81 ms | 635 ms | - |
| 22 | EPODONIOS | vless | `172.64.150.28:2082` | 82 ms | 659 ms | - |
| 23 | EPODONIOS | vless | `104.18.47.73:443` | 84 ms | 663 ms | - |
| 24 | EPODONIOS | vless | `172.64.146.66:443` | 84 ms | 850 ms | - |
| 25 | EPODONIOS | vless | `188.164.248.216:443` | 85 ms | 643 ms | - |
| 26 | EPODONIOS | vless | `172.64.158.170:443` | 87 ms | 661 ms | - |
| 27 | EPODONIOS | vless | `104.18.41.190:443` | 88 ms | 643 ms | - |
| 28 | EPODONIOS | vless | `172.64.152.241:443` | 90 ms | 650 ms | - |
| 29 | EPODONIOS | vless | `88.216.69.253:443` | 90 ms | 659 ms | - |
| 30 | EPODONIOS | vless | `cf.877774.xyz:443` | 101 ms | 656 ms | - |
| 31 | EPODONIOS | vless | `188.164.248.216:443` | 102 ms | 634 ms | - |
| 32 | EPODONIOS | trojan | `resources.findlocaljobnetworkandbuildcommunityconnections.com:443` | 103 ms | 1762 ms | - |
| 33 | EPODONIOS | vless | `172.64.150.28:2082` | 108 ms | 666 ms | - |
| 34 | EPODONIOS | vless | `104.17.154.123:443` | 115 ms | 1022 ms | - |
| 35 | EPODONIOS | vmess | `43.130.35.53:10087` | 118 ms | 不可达 | - |
| 36 | EPODONIOS | ss | `95.215.201.18:19999` | 126 ms | 1250 ms | - |
| 37 | ⚡ b2n.ir/v2ray-configs / 246 | vless | `8.47.69.60:443` | 127 ms | 655 ms | - |
| 38 | EPODONIOS | vless | `47.251.25.74:443` | 129 ms | 756 ms | - |
| 39 | EPODONIOS | vless | `172.67.76.40:443` | 134 ms | 1233 ms | - |
| 40 | EPODONIOS | vless | `172.64.150.28:2082` | 136 ms | 637 ms | - |
| 41 | US 🇺🇸 / @Raydikalx / 18811D | vmess | `129.146.143.80:48111` | 138 ms | 1002 ms | - |
| 42 | EPODONIOS | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 141 ms | 3815 ms | - |
| 43 | CA 🇨🇦 / @Raydikalx / A1CD58 | vmess | `cf.0sm.com:80` | 142 ms | 968 ms | - |
| 44 | EPODONIOS | vless | `188.164.248.91:443` | 144 ms | 1568 ms | - |
| 45 | EPODONIOS | vless | `188.164.248.246:443` | 145 ms | 756 ms | - |
| 46 | EPODONIOS | vless | `8.35.211.169:443` | 150 ms | 719 ms | - |
| 47 | EPODONIOS | vless | `188.164.248.181:443` | 152 ms | 766 ms | - |
| 48 | EPODONIOS | vless | `188.164.248.246:443` | 156 ms | 708 ms | - |
| 49 | EPODONIOS | ss | `156.146.38.169:443` | 161 ms | 1063 ms | - |
| 50 | EPODONIOS | ss | `173.244.56.6:443` | 163 ms | 944 ms | - |

> 仅展示前 50 个，共 564 个；完整列表见 `sub/nodes.txt`。
