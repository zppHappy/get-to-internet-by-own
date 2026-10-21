# 可用节点（自动生成）

> 每次筛选后自动重写，最后更新：`2026-10-21 17:24:56+0800`

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
| 抓取链接 | 19783 |
| 去重后节点 | 7966 |
| TCP 预筛剔除 | 3854 |
| 真连接测试 | 7966 |
| 测试通过 | 733 |
| **最终保留** | **733** |
| 耗时 | 305.9 秒 |

> 解析阶段跳过：重复 11789、协议未启用 0、无法解析 28

## 协议分布

vless 406 · ss 142 · vmess 102 · trojan 78 · hysteria2 5

## 国内方向探测（节点 → 中国，非中国 → 节点）

保留的 733 个节点中，有 **619** 个能经代理访问到国内目标站，**114** 个访问不到。

> 两个必须说清楚的点：
> 1. 这是「节点 → 中国」方向，**不能证明「中国能连到这个节点」**——后者才是你实际使用的方向，必须在国内机器上测才算数。
> 2. 这个延迟值被「测试机 → 节点」那段主导，**不反映节点离中国有多近**（实测香港节点比美国节点还高），所以不参与排序。只能当「能不能到」的参考。

## 节点明细（按延迟升序）

| # | 名称 | 协议 | 服务器 | 延迟 | 到国内目标 | 速度 |
|---|------|------|--------|------|------------|------|
| 1 | EPODONIOS | ss | `156.146.38.167:443` | 61 ms | 855 ms | - |
| 2 | EPODONIOS | ss | `156.146.38.169:443` | 63 ms | 832 ms | - |
| 3 | EPODONIOS | ss | `156.146.38.168:443` | 67 ms | 859 ms | - |
| 4 | EPODONIOS | ss | `156.146.38.170:443` | 75 ms | 993 ms | - |
| 5 | EPODONIOS | vless | `104.18.0.181:2082` | 117 ms | 1155 ms | - |
| 6 | ⚡ b2n.ir/v2ray-configs / 747 | vless | `104.18.0.181:2082` | 120 ms | 934 ms | - |
| 7 | EPODONIOS | vless | `104.18.35.86:8080` | 122 ms | 960 ms | - |
| 8 | EPODONIOS | vless | `104.18.0.181:2082` | 127 ms | 1109 ms | - |
| 9 | EPODONIOS | vless | `172.64.150.28:2082` | 131 ms | 946 ms | - |
| 10 | EPODONIOS | vless | `172.64.150.28:2082` | 133 ms | 969 ms | - |
| 11 | ⚡ b2n.ir/v2ray-configs / 782 | vless | `172.64.150.43:8080` | 133 ms | 940 ms | - |
| 12 | EPODONIOS | ss | `95.215.201.18:19999` | 136 ms | 1185 ms | - |
| 13 | EPODONIOS | vless | `172.64.150.43:443` | 137 ms | 957 ms | - |
| 14 | EPODONIOS | vless | `188.114.98.0:443` | 139 ms | 1002 ms | - |
| 15 | EPODONIOS | vless | `188.114.98.0:443` | 139 ms | 934 ms | - |
| 16 | EPODONIOS | vless | `188.114.97.6:443` | 141 ms | 1132 ms | - |
| 17 | EPODONIOS | trojan | `172.67.131.217:443` | 142 ms | 946 ms | - |
| 18 | EPODONIOS | vless | `188.114.98.0:443` | 142 ms | 947 ms | - |
| 19 | EPODONIOS | vless | `188.114.97.6:443` | 143 ms | 1154 ms | - |
| 20 | EPODONIOS | vless | `188.114.98.0:443` | 143 ms | 950 ms | - |
| 21 | EPODONIOS | vless | `188.114.98.0:443` | 144 ms | 933 ms | - |
| 22 | EPODONIOS | vless | `188.114.97.6:443` | 145 ms | 1025 ms | - |
| 23 | EPODONIOS | ss | `173.244.56.6:443` | 146 ms | 873 ms | - |
| 24 | EPODONIOS | ss | `37.19.198.160:443` | 146 ms | 1207 ms | - |
| 25 | ⚡ b2n.ir/v2ray-configs / 411 | vless | `b2n.ir:443` | 146 ms | 1216 ms | - |
| 26 | EPODONIOS | vless | `15.204.97.219:23576` | 147 ms | 不可达 | - |
| 27 | EPODONIOS | vless | `162.159.135.234:443` | 148 ms | 981 ms | - |
| 28 | EPODONIOS | vless | `188.114.98.0:443` | 148 ms | 935 ms | - |
| 29 | EPODONIOS | vless | `cf-socks.caoyuwu.eu.org:443` | 149 ms | 1157 ms | - |
| 30 | EPODONIOS | vless | `cf.877774.xyz:443` | 149 ms | 963 ms | - |
| 31 | EPODONIOS | vless | `188.114.98.0:443` | 151 ms | 945 ms | - |
| 32 | EPODONIOS | vless | `104.18.43.174:443` | 153 ms | 976 ms | - |
| 33 | EPODONIOS | vless | `104.18.43.174:443` | 153 ms | 963 ms | - |
| 34 | ⚡ b2n.ir/v2ray-configs / 62 | vless | `104.21.91.244:443` | 153 ms | 970 ms | - |
| 35 | EPODONIOS | vless | `188.114.98.0:443` | 154 ms | 989 ms | - |
| 36 | EPODONIOS | vless | `104.21.91.244:443` | 154 ms | 991 ms | - |
| 37 | ⚡ b2n.ir/v2ray-configs / 60 | vless | `188.114.97.6:443` | 154 ms | 1033 ms | - |
| 38 | EPODONIOS | ss | `37.19.198.236:443` | 156 ms | 1866 ms | - |
| 39 | EPODONIOS | vless | `188.114.97.6:443` | 156 ms | 981 ms | - |
| 40 | EPODONIOS | vless | `188.114.97.6:443` | 156 ms | 943 ms | - |
| 41 | EPODONIOS | ss | `37.19.198.244:443` | 157 ms | 1179 ms | - |
| 42 | EPODONIOS | vless | `188.114.97.6:443` | 157 ms | 956 ms | - |
| 43 | EPODONIOS | vless | `15.204.97.219:23576` | 157 ms | 不可达 | - |
| 44 | ⚡ b2n.ir/v2ray-configs / 316 | vless | `172.67.155.65:8443` | 157 ms | 999 ms | - |
| 45 | EPODONIOS | vless | `188.114.97.6:443` | 158 ms | 956 ms | - |
| 46 | EPODONIOS | vless | `188.114.97.6:443` | 159 ms | 1165 ms | - |
| 47 | EPODONIOS | vless | `188.114.98.0:443` | 159 ms | 960 ms | - |
| 48 | EPODONIOS | vless | `15.204.97.206:23576` | 160 ms | 不可达 | - |
| 49 | EPODONIOS | vless | `172.66.0.162:443` | 161 ms | 1119 ms | - |
| 50 | EPODONIOS | vless | `172.67.155.65:8443` | 161 ms | 961 ms | - |

> 仅展示前 50 个，共 733 个；完整列表见 `sub/nodes.txt`。
