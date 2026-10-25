# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-26 07:07:30+0800`

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
| 抓取链接 | 20312 |
| 去重后节点 | 8173 |
| TCP 预筛剔除 | 3845 |
| 真连接测试 | 8173 |
| 测试通过 | 754 |
| **最终保留** | **754** |
| 耗时 | 292.7 秒 |

> 解析阶段跳过：重复 12114、协议未启用 0、无法解析 25

## 协议分布

vless 403 · ss 167 · vmess 122 · trojan 59 · hysteria2 3

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 754 个节点中，有 **664** 个能经代理访问到国内目标站，**90** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vless | `47.253.226.114:443` | 53 ms | 932 ms | - |
| 2 | EPODONIOS | vless | `185.95.231.156:443` | 54 ms | 1301 ms | - |
| 3 | ⚡ b2n.ir/v2ray-configs / 730 | vless | `88.216.69.253:443` | 54 ms | 955 ms | - |
| 4 | ⚡ b2n.ir/v2ray-configs / 203 | vless | `104.18.45.38:443` | 55 ms | 1025 ms | - |
| 5 | EPODONIOS | vless | `172.64.152.241:443` | 57 ms | 1000 ms | - |
| 6 | EPODONIOS | vless | `47.253.226.114:443` | 58 ms | 925 ms | - |
| 7 | EPODONIOS | vless | `172.64.158.170:443` | 59 ms | 973 ms | - |
| 8 | EPODONIOS | vless | `cf.877774.xyz:443` | 59 ms | 979 ms | - |
| 9 | EPODONIOS | vmess | `67.220.95.3:18000` | 60 ms | 1241 ms | - |
| 10 | EPODONIOS | ss | `15.204.246.132:7307` | 61 ms | 1189 ms | - |
| 11 | EPODONIOS | vmess | `67.220.85.46:18000` | 62 ms | 894 ms | - |
| 12 | ⚡ b2n.ir/v2ray-configs / 966 | vless | `8.47.69.60:443` | 62 ms | 965 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 791 | vless | `104.21.221.158:443` | 64 ms | 980 ms | - |
| 14 | EPODONIOS | ss | `37.19.198.160:443` | 65 ms | 932 ms | - |
| 15 | EPODONIOS | vless | `159.89.87.21:28190` | 68 ms | 921 ms | - |
| 16 | EPODONIOS | ss | `37.19.198.243:443` | 69 ms | 923 ms | - |
| 17 | EPODONIOS | vless | `169.40.42.231:443` | 70 ms | 976 ms | - |
| 18 | ⚡ b2n.ir/v2ray-configs / 294 | vless | `172.66.1.36:443` | 71 ms | 964 ms | - |
| 19 | EPODONIOS | vless | `169.40.42.35:443` | 75 ms | 1103 ms | - |
| 20 | EPODONIOS | vless | `169.40.42.90:443` | 75 ms | 1182 ms | - |
| 21 | EPODONIOS | vless | `cf.130519.xyz:443` | 76 ms | 982 ms | - |
| 22 | EPODONIOS | vless | `169.40.42.235:443` | 76 ms | 1135 ms | - |
| 23 | EPODONIOS | vless | `169.40.42.163:443` | 81 ms | 1312 ms | - |
| 24 | EPODONIOS | vless | `159.89.87.21:28190` | 83 ms | 902 ms | - |
| 25 | EPODONIOS | vless | `cf.877774.xyz:443` | 83 ms | 1017 ms | - |
| 26 | EPODONIOS | vless | `172.66.0.162:443` | 84 ms | 984 ms | - |
| 27 | EPODONIOS | ss | `51.222.200.165:5000` | 86 ms | 1338 ms | - |
| 28 | EPODONIOS | ss | `51.222.136.236:8882` | 86 ms | 1325 ms | - |
| 29 | EPODONIOS | vless | `169.40.42.104:443` | 88 ms | 1237 ms | - |
| 30 | CA 🇨🇦 / @Raydikalx / 0940F6 | vmess | `23.162.200.198:18000` | 94 ms | 1509 ms | - |
| 31 | EPODONIOS | vless | `169.40.42.104:443` | 102 ms | 1246 ms | - |
| 32 | EPODONIOS | vless | `172.64.150.28:2082` | 102 ms | 1000 ms | - |
| 33 | EPODONIOS | vless | `172.64.150.28:2082` | 104 ms | 994 ms | - |
| 34 | EPODONIOS | vless | `45.91.248.127:8443` | 106 ms | 822 ms | - |
| 35 | EPODONIOS | vless | `172.64.150.28:2082` | 112 ms | 976 ms | - |
| 36 | EPODONIOS | ss | `37.19.198.236:443` | 112 ms | 921 ms | - |
| 37 | EPODONIOS | ss | `156.146.38.167:443` | 114 ms | 931 ms | - |
| 38 | EPODONIOS | ss | `156.146.38.170:443` | 117 ms | 931 ms | - |
| 39 | EPODONIOS | vless | `209.200.246.148:443` | 118 ms | 1289 ms | - |
| 40 | EPODONIOS | ss | `156.146.38.169:443` | 120 ms | 918 ms | - |
| 41 | EPODONIOS | vless | `169.40.42.35:443` | 126 ms | 1025 ms | - |
| 42 | EPODONIOS | vless | `169.40.42.74:443` | 129 ms | 1053 ms | - |
| 43 | CA 🇨🇦 / @Raydikalx / A1CD58 | vmess | `cf.0sm.com:80` | 129 ms | 919 ms | - |
| 44 | EPODONIOS | vless | `169.40.42.235:443` | 130 ms | 1132 ms | - |
| 45 | @VPsave | vmess | `cf.0sm.com:443` | 130 ms | 973 ms | - |
| 46 | EPODONIOS | vless | `169.40.42.235:443` | 131 ms | 1106 ms | - |
| 47 | EPODONIOS | ss | `156.146.38.168:443` | 132 ms | 929 ms | - |
| 48 | CA 🇨🇦 / @Raydikalx / A7D452 | vmess | `134.195.196.211:18000` | 132 ms | 1168 ms | - |
| 49 | EPODONIOS | vmess | `134.195.196.211:18000` | 134 ms | 1460 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / 00DD16 | vmess | `134.195.196.211:18000` | 135 ms | 1158 ms | - |

> 仅展示前 50 个，共 754 个；完整列表见 `sub/nodes.txt`。
