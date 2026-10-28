# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-28 20:18:24+0800`

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
| 抓取链接 | 20788 |
| 去重后节点 | 8265 |
| TCP 预筛剔除 | 3865 |
| 真连接测试 | 8265 |
| 测试通过 | 760 |
| **最终保留** | **760** |
| 耗时 | 345.2 秒 |

> 解析阶段跳过：重复 12496、协议未启用 0、无法解析 27

## 协议分布

vless 347 · ss 167 · vmess 134 · trojan 110 · hysteria2 2

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 760 个节点中，有 **596** 个能经代理访问到国内目标站，**164** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `84.17.41.2:18000` | 40 ms | 1276 ms | - |
| 2 | EPODONIOS | trojan | `216.106.186.32:443` | 43 ms | 757 ms | - |
| 3 | EPODONIOS | trojan | `216.106.186.33:443` | 47 ms | 1817 ms | - |
| 4 | EPODONIOS | ss | `149.22.95.183:443` | 56 ms | 766 ms | - |
| 5 | EPODONIOS | vless | `15.204.97.197:23576` | 61 ms | 不可达 | - |
| 6 | EPODONIOS | vless | `15.204.97.195:23576` | 64 ms | 不可达 | - |
| 7 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 71 ms | 不可达 | - |
| 8 | EPODONIOS | vless | `172.66.0.162:443` | 72 ms | 684 ms | - |
| 9 | EPODONIOS | vless | `104.18.35.15:443` | 75 ms | 695 ms | - |
| 10 | EPODONIOS | vless | `172.64.152.241:443` | 77 ms | 695 ms | - |
| 11 | EPODONIOS | vless | `104.17.154.123:443` | 80 ms | 676 ms | - |
| 12 | ⚡ b2n.ir/v2ray-configs / 915 | vless | `88.216.69.253:443` | 82 ms | 695 ms | - |
| 13 | EPODONIOS | vless | `cf.877774.xyz:443` | 83 ms | 730 ms | - |
| 14 | EPODONIOS | vless | `15.204.97.198:23576` | 84 ms | 800 ms | - |
| 15 | EPODONIOS | vless | `172.64.152.241:443` | 85 ms | 699 ms | - |
| 16 | EPODONIOS | vless | `172.64.153.153:443` | 85 ms | 722 ms | - |
| 17 | EPODONIOS | vless | `172.66.0.162:443` | 86 ms | 1987 ms | - |
| 18 | EPODONIOS | vless | `104.18.37.127:443` | 88 ms | 695 ms | - |
| 19 | EPODONIOS | vless | `172.64.152.241:443` | 92 ms | 690 ms | - |
| 20 | EPODONIOS | vless | `172.64.158.170:443` | 92 ms | 703 ms | - |
| 21 | EPODONIOS | vless | `172.64.158.170:443` | 93 ms | 812 ms | - |
| 22 | EPODONIOS | vless | `104.17.154.123:443` | 95 ms | 823 ms | - |
| 23 | EPODONIOS | vless | `104.18.37.247:443` | 99 ms | 702 ms | - |
| 24 | EPODONIOS | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 100 ms | 3003 ms | - |
| 25 | EPODONIOS | vless | `172.64.152.241:443` | 102 ms | 686 ms | - |
| 26 | EPODONIOS | vless | `104.18.47.73:443` | 106 ms | 876 ms | - |
| 27 | EPODONIOS | vless | `188.164.248.216:443` | 109 ms | 714 ms | - |
| 28 | EPODONIOS | vless | `104.18.47.73:443` | 110 ms | 689 ms | - |
| 29 | EPODONIOS | vless | `88.216.69.253:443` | 113 ms | 875 ms | - |
| 30 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 114 ms | 969 ms | - |
| 31 | ⚡ b2n.ir/v2ray-configs / 664 | vless | `104.21.221.158:443` | 120 ms | 1018 ms | - |
| 32 | EPODONIOS | vless | `104.18.41.190:443` | 121 ms | 930 ms | - |
| 33 | EPODONIOS | vless | `172.66.154.57:443` | 122 ms | 707 ms | - |
| 34 | EPODONIOS | vless | `chatgpt.com:443` | 126 ms | 714 ms | - |
| 35 | EPODONIOS | ss | `95.215.201.18:19999` | 127 ms | 1232 ms | - |
| 36 | EPODONIOS | vless | `vl.cocopon.top:443` | 127 ms | 1406 ms | - |
| 37 | EPODONIOS | vless | `47.251.25.74:443` | 128 ms | 1752 ms | - |
| 38 | EPODONIOS | vless | `104.18.40.100:443` | 131 ms | 885 ms | - |
| 39 | EPODONIOS | vless | `15.204.97.206:23576` | 135 ms | 不可达 | - |
| 40 | EPODONIOS | vless | `cf.877774.xyz:443` | 136 ms | 833 ms | - |
| 41 | EPODONIOS | vless | `104.18.0.181:2082` | 136 ms | 682 ms | - |
| 42 | EPODONIOS | ss | `173.244.56.6:443` | 137 ms | 936 ms | - |
| 43 | EPODONIOS | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 142 ms | 1215 ms | - |
| 44 | EPODONIOS | vless | `172.64.150.28:2082` | 143 ms | 1588 ms | - |
| 45 | EPODONIOS | vless | `188.164.248.216:443` | 145 ms | 707 ms | - |
| 46 | EPODONIOS | ss | `173.244.56.9:443` | 148 ms | 1376 ms | - |
| 47 | EPODONIOS | vless | `172.64.150.28:2082` | 150 ms | 705 ms | - |
| 48 | EPODONIOS | trojan | `66.163.114.126:443` | 153 ms | 904 ms | - |
| 49 | EPODONIOS | trojan | `66.163.114.166:443` | 155 ms | 880 ms | - |
| 50 | US 🇺🇸 / @Raydikalx / 18811D | vmess | `129.146.143.80:48111` | 156 ms | 1230 ms | - |

> 仅展示前 50 个，共 760 个；完整列表见 `sub/nodes.txt`。
