# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-22 19:20:00+0800`

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
| 抓取链接 | 19477 |
| 去重后节点 | 8024 |
| TCP 预筛剔除 | 3909 |
| 真连接测试 | 8024 |
| 测试通过 | 735 |
| **最终保留** | **735** |
| 耗时 | 293.8 秒 |

> 解析阶段跳过：重复 11428、协议未启用 0、无法解析 25

## 协议分布

vless 406 · ss 147 · vmess 99 · trojan 77 · hysteria2 6

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 735 个节点中，有 **633** 个能经代理访问到国内目标站，**102** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `15.204.233.41:8882` | 34 ms | 1193 ms | - |
| 2 | EPODONIOS | ss | `37.19.198.160:443` | 37 ms | 1012 ms | - |
| 3 | EPODONIOS | vless | `172.64.150.28:2082` | 38 ms | 952 ms | - |
| 4 | EPODONIOS | vless | `104.18.0.181:2082` | 39 ms | 1008 ms | - |
| 5 | EPODONIOS | vmess | `67.220.85.46:18000` | 46 ms | 897 ms | - |
| 6 | US 🇺🇸 / @Raydikalx / F2583B | vmess | `67.220.85.46:18000` | 47 ms | 1385 ms | - |
| 7 | EPODONIOS | vless | `104.18.35.86:8080` | 50 ms | 939 ms | - |
| 8 | EPODONIOS | ss | `37.19.198.243:443` | 55 ms | 920 ms | - |
| 9 | EPODONIOS | vless | `188.114.98.0:443` | 60 ms | 1325 ms | - |
| 10 | EPODONIOS | vless | `195.123.235.177:443` | 60 ms | 846 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 391 | vless | `188.114.97.6:443` | 61 ms | 945 ms | - |
| 12 | EPODONIOS | vless | `188.114.98.0:443` | 64 ms | 1071 ms | - |
| 13 | EPODONIOS | vless | `104.21.91.244:443` | 64 ms | 1010 ms | - |
| 14 | EPODONIOS | vless | `172.64.154.211:443` | 65 ms | 1007 ms | - |
| 15 | EPODONIOS | vless | `45.138.100.248:10443` | 65 ms | 1288 ms | - |
| 16 | EPODONIOS | vless | `104.18.43.174:443` | 68 ms | 956 ms | - |
| 17 | ⚡ b2n.ir/v2ray-configs / 435 | vless | `188.114.97.6:443` | 68 ms | 1011 ms | - |
| 18 | EPODONIOS | vless | `cf.130519.xyz:443` | 69 ms | 964 ms | - |
| 19 | EPODONIOS | vless | `104.21.91.244:443` | 69 ms | 1007 ms | - |
| 20 | EPODONIOS | vless | `104.21.91.244:443` | 69 ms | 990 ms | - |
| 21 | EPODONIOS | vless | `188.114.97.6:443` | 72 ms | 1153 ms | - |
| 22 | EPODONIOS | vless | `188.114.98.0:443` | 72 ms | 1054 ms | - |
| 23 | EPODONIOS | vless | `104.21.91.244:443` | 72 ms | 996 ms | - |
| 24 | EPODONIOS | vless | `162.159.135.234:443` | 73 ms | 1023 ms | - |
| 25 | EPODONIOS | vless | `169.40.42.231:443` | 73 ms | 1238 ms | - |
| 26 | EPODONIOS | vless | `104.18.41.190:443` | 73 ms | 1021 ms | - |
| 27 | EPODONIOS | vless | `169.40.42.74:443` | 74 ms | 1206 ms | - |
| 28 | EPODONIOS | vless | `169.40.42.235:443` | 75 ms | 1185 ms | - |
| 29 | EPODONIOS | vless | `188.114.97.6:443` | 76 ms | 1012 ms | - |
| 30 | EPODONIOS | vless | `188.114.98.0:443` | 76 ms | 1279 ms | - |
| 31 | EPODONIOS | vless | `cf.877774.xyz:443` | 77 ms | 980 ms | - |
| 32 | EPODONIOS | vless | `188.114.98.0:443` | 78 ms | 991 ms | - |
| 33 | EPODONIOS | vless | `188.114.98.0:443` | 78 ms | 1698 ms | - |
| 34 | EPODONIOS | vless | `169.40.42.104:443` | 79 ms | 1176 ms | - |
| 35 | EPODONIOS | vless | `104.21.91.244:443` | 79 ms | 941 ms | - |
| 36 | EPODONIOS | vless | `188.114.98.0:443` | 80 ms | 982 ms | - |
| 37 | EPODONIOS | vless | `188.114.98.0:443` | 81 ms | 984 ms | - |
| 38 | EPODONIOS | vless | `188.164.248.216:443` | 81 ms | 1007 ms | - |
| 39 | EPODONIOS | vless | `cf.090227.xyz:443` | 81 ms | 965 ms | - |
| 40 | Telegram---@MTMVPN---@MTMVPN---@MTMVPN-- | vless | `104.21.91.244:443` | 81 ms | 965 ms | - |
| 41 | ⚡ b2n.ir/v2ray-configs / 360 | vless | `104.21.91.244:443` | 81 ms | 993 ms | - |
| 42 | EPODONIOS | vless | `172.64.150.43:443` | 82 ms | 962 ms | - |
| 43 | ⚡ b2n.ir/v2ray-configs / 695 | vless | `188.114.97.6:443` | 82 ms | 1001 ms | - |
| 44 | EPODONIOS | vless | `104.18.43.174:443` | 85 ms | 1311 ms | - |
| 45 | EPODONIOS | vless | `162.159.135.234:443` | 86 ms | 967 ms | - |
| 46 | EPODONIOS | vless | `188.114.97.6:443` | 86 ms | 995 ms | - |
| 47 | EPODONIOS | vless | `169.40.42.104:443` | 86 ms | 1181 ms | - |
| 48 | EPODONIOS | vless | `169.40.42.168:443` | 86 ms | 1134 ms | - |
| 49 | EPODONIOS | vless | `104.21.91.244:443` | 86 ms | 988 ms | - |
| 50 | EPODONIOS | vless | `188.114.98.0:443` | 87 ms | 987 ms | - |

> 仅展示前 50 个，共 735 个；完整列表见 `sub/nodes.txt`。
