# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-25 18:55:19+0800`

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
| 抓取链接 | 19713 |
| 去重后节点 | 8051 |
| TCP 预筛剔除 | 3967 |
| 真连接测试 | 8051 |
| 测试通过 | 558 |
| **最终保留** | **558** |
| 耗时 | 296.6 秒 |

> 解析阶段跳过：重复 11635、协议未启用 0、无法解析 27

## 协议分布

vless 268 · ss 133 · vmess 119 · trojan 34 · hysteria2 4

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 558 个节点中，有 **454** 个能经代理访问到国内目标站，**104** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | vmess | `129.146.77.248:39495` | 28 ms | 842 ms | - |
| 2 | US 🇺🇸 / @Raydikalx / 452ED5 | vmess | `129.146.77.248:39495` | 28 ms | 1097 ms | - |
| 3 | EPODONIOS | ss | `95.215.201.18:19999` | 34 ms | 1012 ms | - |
| 4 | EPODONIOS | vless | `172.64.150.28:2082` | 65 ms | 774 ms | - |
| 5 | CA 🇨🇦 / @Raydikalx / 8BB1EE | vmess | `us16-4.998998.best:443` | 76 ms | 741 ms | - |
| 6 | EPODONIOS | vless | `172.64.152.241:443` | 77 ms | 771 ms | - |
| 7 | ⚡ b2n.ir/v2ray-configs / 388 | vless | `104.18.45.38:443` | 77 ms | 782 ms | - |
| 8 | EPODONIOS | vless | `172.64.158.170:443` | 79 ms | 734 ms | - |
| 9 | US 🇺🇸 / @Raydikalx / 8D9E8F | vmess | `169.197.142.22:18000` | 79 ms | 1177 ms | - |
| 10 | EPODONIOS | vless | `104.26.4.2:443` | 82 ms | 758 ms | - |
| 11 | EPODONIOS | vless | `104.21.221.158:443` | 83 ms | 764 ms | - |
| 12 | EPODONIOS | vless | `172.64.150.28:2082` | 83 ms | 750 ms | - |
| 13 | ⚡ b2n.ir/v2ray-configs / 97 | vless | `104.21.221.158:443` | 83 ms | 735 ms | - |
| 14 | EPODONIOS | ss | `173.244.56.6:443` | 84 ms | 824 ms | - |
| 15 | ⚡ b2n.ir/v2ray-configs / 450 | vless | `188.164.248.216:443` | 85 ms | 838 ms | - |
| 16 | US 🇺🇸 / @Raydikalx / E38DDB | vmess | `169.197.142.22:18000` | 85 ms | 1044 ms | - |
| 17 | EPODONIOS | vless | `cf.877774.xyz:443` | 86 ms | 748 ms | - |
| 18 | EPODONIOS | ss | `156.146.38.169:443` | 87 ms | 854 ms | - |
| 19 | EPODONIOS | ss | `156.146.38.167:443` | 87 ms | 889 ms | - |
| 20 | EPODONIOS | vless | `cf.877774.xyz:443` | 87 ms | 911 ms | - |
| 21 | EPODONIOS | vless | `104.18.0.181:2082` | 89 ms | 806 ms | - |
| 22 | ⚡ b2n.ir/v2ray-configs / 287 | vless | `88.216.69.253:443` | 90 ms | 746 ms | - |
| 23 | ⚡ b2n.ir/v2ray-configs / 200 | vless | `8.47.69.60:443` | 91 ms | 767 ms | - |
| 24 | EPODONIOS | ss | `156.146.38.168:443` | 99 ms | 889 ms | - |
| 25 | EPODONIOS | ss | `156.146.38.170:443` | 107 ms | 866 ms | - |
| 26 | EPODONIOS | vless | `172.66.0.162:443` | 110 ms | 750 ms | - |
| 27 | EPODONIOS | vless | `104.18.35.86:8080` | 111 ms | 740 ms | - |
| 28 | EPODONIOS | vless | `3h-unitedstates1.09vpn.com:80` | 119 ms | 819 ms | - |
| 29 | EPODONIOS | vmess | `84.17.41.2:18000` | 128 ms | 不可达 | - |
| 30 | EPODONIOS | ss | `173.244.56.9:443` | 131 ms | 741 ms | - |
| 31 | EPODONIOS | vmess | `guanwang.awsno.com:443` | 135 ms | 不可达 | - |
| 32 | US 🇺🇸 / @Raydikalx / 94BA12 | vmess | `84.17.41.2:18000` | 137 ms | 4671 ms | - |
| 33 | EPODONIOS | vless | `38.107.232.36:80` | 139 ms | 不可达 | - |
| 34 | EPODONIOS | vless | `15.204.97.197:23576` | 145 ms | 不可达 | - |
| 35 | EPODONIOS | vless | `15.204.97.214:23576` | 146 ms | 不可达 | - |
| 36 | EPODONIOS | vless | `15.204.97.219:23576` | 147 ms | 不可达 | - |
| 37 | EPODONIOS | vless | `15.204.97.216:23576` | 148 ms | 不可达 | - |
| 38 | US 🇺🇸 / @Raydikalx / FC15CE | vmess | `84.17.41.2:18000` | 148 ms | 927 ms | - |
| 39 | EPODONIOS | vless | `15.204.97.197:23576` | 149 ms | 不可达 | - |
| 40 | EPODONIOS | vless | `15.204.97.206:23576` | 150 ms | 不可达 | - |
| 41 | CA 🇨🇦 / @Raydikalx / 0AD519 | vmess | `172.67.187.145:80` | 153 ms | 989 ms | - |
| 42 | EPODONIOS | vless | `15.204.97.206:23576` | 154 ms | 不可达 | - |
| 43 | EPODONIOS | vless | `15.204.97.219:23576` | 158 ms | 不可达 | - |
| 44 | EPODONIOS | ss | `149.22.95.183:443` | 162 ms | 900 ms | - |
| 45 | US 🇺🇸 / @Raydikalx / 25DD23 | vmess | `us-23.hihu.net:80` | 162 ms | 941 ms | - |
| 46 | EPODONIOS | vmess | `38.91.107.49:18000` | 166 ms | 1426 ms | - |
| 47 | US 🇺🇸 / @Raydikalx / B7DF3B | vmess | `38.91.107.49:18000` | 167 ms | 1707 ms | - |
| 48 | US 🇺🇸 / @Raydikalx / C10152 | vmess | `23.158.72.131:80` | 174 ms | 923 ms | - |
| 49 | EPODONIOS | trojan | `blog.findlocaljobnetworkandbuildcommunityconnections.com:443` | 182 ms | 883 ms | - |
| 50 | EPODONIOS | vmess | `38.110.1.246:18000` | 184 ms | 1956 ms | - |

> 仅展示前 50 个，共 558 个；完整列表见 `sub/nodes.txt`。
