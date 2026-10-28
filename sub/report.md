# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-28 12:20:27+0800`

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
| 抓取链接 | 20738 |
| 去重后节点 | 8213 |
| TCP 预筛剔除 | 3870 |
| 真连接测试 | 8213 |
| 测试通过 | 855 |
| **最终保留** | **855** |
| 耗时 | 313.0 秒 |

> 解析阶段跳过：重复 12503、协议未启用 0、无法解析 22

## 协议分布

vless 439 · ss 169 · vmess 128 · trojan 113 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 855 个节点中，有 **716** 个能经代理访问到国内目标站，**139** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `129.146.77.248:39495` | 28 ms | 1437 ms | - |
| 2 | EPODONIOS | vmess | `129.146.77.248:39495` | 36 ms | 1564 ms | - |
| 3 | EPODONIOS | ss | `95.215.201.18:19999` | 38 ms | 714 ms | - |
| 4 | EPODONIOS | trojan | `66.163.112.76:443` | 38 ms | 718 ms | - |
| 5 | EPODONIOS | ss | `216.105.168.18:443` | 46 ms | 2404 ms | - |
| 6 | EPODONIOS | trojan | `66.163.112.242:443` | 48 ms | 731 ms | - |
| 7 | EPODONIOS | ss | `216.105.168.18:443` | 49 ms | 917 ms | - |
| 8 | EPODONIOS | ss | `173.244.56.9:443` | 59 ms | 858 ms | - |
| 9 | EPODONIOS | trojan | `66.163.112.142:443` | 73 ms | 735 ms | - |
| 10 | EPODONIOS | vless | `195.123.240.65:443` | 79 ms | 769 ms | - |
| 11 | EPODONIOS | vless | `172.64.150.28:2082` | 83 ms | 920 ms | - |
| 12 | EPODONIOS | vless | `172.64.150.28:2082` | 84 ms | 763 ms | - |
| 13 | EPODONIOS | ss | `156.146.38.169:443` | 91 ms | 873 ms | - |
| 14 | EPODONIOS | ss | `156.146.38.170:443` | 93 ms | 892 ms | - |
| 15 | EPODONIOS | ss | `156.146.38.167:443` | 94 ms | 898 ms | - |
| 16 | EPODONIOS | vmess | `169.197.142.22:18000` | 95 ms | 928 ms | - |
| 17 | EPODONIOS | vless | `172.66.154.57:443` | 97 ms | 1044 ms | - |
| 18 | EPODONIOS | ss | `156.146.38.168:443` | 100 ms | 1172 ms | - |
| 19 | EPODONIOS | vless | `172.64.153.153:443` | 100 ms | 806 ms | - |
| 20 | EPODONIOS | vless | `172.66.0.162:443` | 104 ms | 747 ms | - |
| 21 | EPODONIOS | vless | `172.64.152.241:443` | 105 ms | 773 ms | - |
| 22 | EPODONIOS | trojan | `66.163.112.13:443` | 108 ms | 731 ms | - |
| 23 | EPODONIOS | vless | `172.64.158.170:443` | 110 ms | 786 ms | - |
| 24 | EPODONIOS | vless | `104.18.26.94:8080` | 112 ms | 751 ms | - |
| 25 | EPODONIOS | vless | `38.107.232.36:80` | 115 ms | 不可达 | - |
| 26 | ⚡ b2n.ir/v2ray-configs / 640 | vless | `8.47.69.60:443` | 116 ms | 921 ms | - |
| 27 | EPODONIOS | vless | `154.197.75.40:8880` | 119 ms | 812 ms | - |
| 28 | EPODONIOS | vless | `172.67.76.40:443` | 119 ms | 719 ms | - |
| 29 | EPODONIOS | vless | `104.18.47.73:443` | 121 ms | 796 ms | - |
| 30 | EPODONIOS | vless | `172.64.152.241:443` | 121 ms | 950 ms | - |
| 31 | EPODONIOS | vless | `172.64.150.28:2082` | 121 ms | 788 ms | - |
| 32 | EPODONIOS | vless | `188.114.96.9:443` | 123 ms | 815 ms | - |
| 33 | EPODONIOS | vless | `23.227.60.30:8880` | 124 ms | 745 ms | - |
| 34 | EPODONIOS | vless | `172.64.146.66:443` | 126 ms | 916 ms | - |
| 35 | EPODONIOS | vless | `cf.877774.xyz:443` | 126 ms | 790 ms | - |
| 36 | EPODONIOS | vless | `104.18.0.181:2082` | 126 ms | 772 ms | - |
| 37 | EPODONIOS | vless | `104.21.94.161:443` | 127 ms | 984 ms | - |
| 38 | EPODONIOS | vless | `172.64.152.241:443` | 130 ms | 789 ms | - |
| 39 | EPODONIOS | vless | `172.64.150.28:2082` | 132 ms | 745 ms | - |
| 40 | ⚡ b2n.ir/v2ray-configs / 732 | vless | `104.18.45.38:443` | 132 ms | 912 ms | - |
| 41 | ⚡ b2n.ir/v2ray-configs / 112 | vless | `104.18.45.38:443` | 133 ms | 781 ms | - |
| 42 | ⚡ b2n.ir/v2ray-configs / 207 | vless | `104.21.221.158:443` | 133 ms | 784 ms | - |
| 43 | EPODONIOS | vless | `172.64.158.170:443` | 135 ms | 753 ms | - |
| 44 | EPODONIOS | ss | `173.244.56.6:443` | 137 ms | 814 ms | - |
| 45 | EPODONIOS | vless | `154.83.2.50:8880` | 138 ms | 775 ms | - |
| 46 | EPODONIOS | vless | `cf-socks.caoyuwu.eu.org:443` | 138 ms | 796 ms | - |
| 47 | EPODONIOS | vless | `154.218.15.50:8880` | 139 ms | 805 ms | - |
| 48 | EPODONIOS | vless | `188.164.248.216:443` | 139 ms | 780 ms | - |
| 49 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 139 ms | 不可达 | - |
| 50 | EPODONIOS | vless | `104.17.154.123:443` | 140 ms | 982 ms | - |

> 仅展示前 50 个，共 855 个；完整列表见 `sub/nodes.txt`。
