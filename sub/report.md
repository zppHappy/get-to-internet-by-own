# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-25 04:24:32+0800`

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
| 抓取链接 | 19993 |
| 去重后节点 | 8042 |
| TCP 预筛剔除 | 3923 |
| 真连接测试 | 8042 |
| 测试通过 | 581 |
| **最终保留** | **581** |
| 耗时 | 318.5 秒 |

> 解析阶段跳过：重复 11928、协议未启用 0、无法解析 23

## 协议分布

vless 278 · ss 136 · vmess 127 · trojan 36 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 581 个节点中，有 **464** 个能经代理访问到国内目标站，**117** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.167:443` | 70 ms | 813 ms | - |
| 2 | EPODONIOS | ss | `156.146.38.169:443` | 70 ms | 849 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.170:443` | 79 ms | 844 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.168:443` | 94 ms | 847 ms | - |
| 5 | EPODONIOS | vless | `172.64.150.28:2082` | 113 ms | 933 ms | - |
| 6 | EPODONIOS | vless | `172.64.150.28:2082` | 118 ms | 1138 ms | - |
| 7 | EPODONIOS | vless | `172.64.150.28:2082` | 121 ms | 966 ms | - |
| 8 | ⚡ b2n.ir/v2ray-configs / 821 | vless | `88.216.69.253:443` | 126 ms | 950 ms | - |
| 9 | EPODONIOS | ss | `95.215.201.18:19999` | 135 ms | 1579 ms | - |
| 10 | EPODONIOS | vless | `cf.877774.xyz:443` | 136 ms | 969 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 34 | vless | `104.18.45.38:443` | 138 ms | 1039 ms | - |
| 12 | EPODONIOS | vless | `172.64.158.170:443` | 142 ms | 1043 ms | - |
| 13 | EPODONIOS | vless | `8.47.69.60:443` | 142 ms | 989 ms | - |
| 14 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 144 ms | 不可达 | - |
| 15 | EPODONIOS | vless | `15.204.97.197:23576` | 145 ms | 不可达 | - |
| 16 | EPODONIOS | vless | `15.204.97.219:23576` | 145 ms | 不可达 | - |
| 17 | EPODONIOS | vless | `172.66.0.162:443` | 145 ms | 1035 ms | - |
| 18 | EPODONIOS | vless | `15.204.97.197:23576` | 146 ms | 不可达 | - |
| 19 | EPODONIOS | vless | `15.204.97.214:23576` | 146 ms | 不可达 | - |
| 20 | EPODONIOS | ss | `37.19.198.160:443` | 147 ms | 1054 ms | - |
| 21 | ⚡ b2n.ir/v2ray-configs / 350 | vless | `104.21.221.158:443` | 147 ms | 979 ms | - |
| 22 | EPODONIOS | vless | `15.204.97.206:23576` | 149 ms | 不可达 | - |
| 23 | EPODONIOS | vless | `15.204.97.216:23576` | 149 ms | 不可达 | - |
| 24 | EPODONIOS | vless | `172.64.152.241:443` | 150 ms | 1019 ms | - |
| 25 | EPODONIOS | ss | `37.19.198.236:443` | 151 ms | 1270 ms | - |
| 26 | EPODONIOS | ss | `37.19.198.244:443` | 153 ms | 1090 ms | - |
| 27 | CA 🇨🇦 / @Raydikalx / 0940F6 | vmess | `23.162.200.198:18000` | 153 ms | 1535 ms | - |
| 28 | CA 🇨🇦 / @Raydikalx / 391CAA | vmess | `23.162.200.198:18000` | 156 ms | 1268 ms | - |
| 29 | EPODONIOS | vmess | `67.220.85.46:18000` | 157 ms | 1671 ms | - |
| 30 | EPODONIOS | vless | `104.18.45.38:443` | 158 ms | 983 ms | - |
| 31 | EPODONIOS | vless | `104.18.0.181:2082` | 158 ms | 1549 ms | - |
| 32 | EPODONIOS | ss | `37.19.198.243:443` | 158 ms | 1524 ms | - |
| 33 | EPODONIOS | vless | `15.204.97.206:23576` | 159 ms | 不可达 | - |
| 34 | US 🇺🇸 / @Raydikalx / FC15CE | vmess | `84.17.41.2:18000` | 159 ms | 4263 ms | - |
| 35 | EPODONIOS | vless | `15.204.97.219:23576` | 160 ms | 不可达 | - |
| 36 | ⚡ b2n.ir/v2ray-configs / 118 | vless | `88.216.69.253:443` | 160 ms | 1009 ms | - |
| 37 | CA 🇨🇦 / @Raydikalx / 4BA3A6 | vmess | `23.162.200.198:18000` | 162 ms | 1537 ms | - |
| 38 | EPODONIOS | ss | `138.199.42.68:8080` | 163 ms | 940 ms | - |
| 39 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 165 ms | 不可达 | - |
| 40 | EPODONIOS | vmess | `23.254.194.215:8080` | 168 ms | 850 ms | - |
| 41 | EPODONIOS | vless | `cf.877774.xyz:443` | 175 ms | 978 ms | - |
| 42 | EPODONIOS | vless | `cf.090227.xyz:443` | 178 ms | 959 ms | - |
| 43 | EPODONIOS | vmess | `67.220.95.3:18000` | 179 ms | 1488 ms | - |
| 44 | EPODONIOS | ss | `173.244.56.9:443` | 180 ms | 891 ms | - |
| 45 | EPODONIOS | vless | `ww13.levikogjgfdd.ir:23576` | 182 ms | 不可达 | - |
| 46 | US 🇺🇸 / @Raydikalx / 101269 | vmess | `84.17.41.2:18000` | 183 ms | 4501 ms | - |
| 47 | EPODONIOS | vmess | `67.220.95.3:18000` | 187 ms | 1521 ms | - |
| 48 | EPODONIOS | ss | `173.244.56.6:443` | 192 ms | 881 ms | - |
| 49 | EPODONIOS | vmess | `134.195.196.211:18000` | 193 ms | 1561 ms | - |
| 50 | CA 🇨🇦 / @Raydikalx / 874860 | vmess | `134.195.196.211:18000` | 193 ms | 1528 ms | - |

> 仅展示前 50 个，共 581 个；完整列表见 `sub/nodes.txt`。
