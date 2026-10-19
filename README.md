# v2sub · V2RayN 订阅自动筛选

把一堆 V2RayN 订阅合并 → **真的连上去测**（不是 ping 端口）→ 只留下能用的节点 → 生成一条新的订阅地址。

筛完的结果自动推到 GitHub，得到一个固定链接，粘进 V2RayN 就是一个永远只有「活节点」的订阅。

---

## 它和 V2RayN 的测试是同一套逻辑

V2RayN 的「真连接延迟」并不是 TCP 探活，而是：**临时起一个内核 → 本地开 socks5 → 通过这个节点真的发一次 HTTP 请求 → 记录耗时**。测速同理：**通过节点真的下载一段数据 → 算 MB/s**。

本工具照搬这个流程：

| 步骤 | V2RayN | v2sub |
|---|---|---|
| 内核 | xray-core / sing-box | xray-core / sing-box（同一个） |
| 延迟测试 | 真连接，请求测试 URL 记时间 | `curl -x socks5h://127.0.0.1:<port>` 请求 `delay_test_url`，取 `time_total` |
| 测速 | 通过代理下载文件 | 通过代理下载 `speed_test_url`，取 `speed_download` |
| 判定 | HTTP 有响应即通 | HTTP 状态码非 0 即通（可配置严格模式） |

所以「本地 V2RayN 里显示 300ms 能用」的节点，这里测出来也是 300ms 左右；机场挂掉、被墙、证书错、密码错的节点会在这里直接失败。

---

## 快速开始（本地）

**依赖**：Python 3.9+、`curl`（系统自带）、`unzip`

```bash
# 1. 装 Python 依赖
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 2. 下载代理内核到 ./bin（xray + sing-box，约 50MB）
chmod +x install_core.sh
./install_core.sh              # 只要 xray 就 ./install_core.sh xray

# 3. 填订阅地址（一行一个，支持 http(s) 链接或本地文件）
cp sources.example.txt sources.txt
vim sources.txt

# 4. 跑
python3 filter.py -c config.yaml
```

或者一步到位：

```bash
./run.sh          # 自动建 venv、装依赖、装内核、跑筛选
```

跑完在 `sub/` 下：

| 文件 | 用途 |
|---|---|
| `sub/base64.txt` | **新订阅**（base64 格式，V2RayN 直接吃） |
| `sub/nodes.txt` | 明文链接，方便肉眼核对 |
| `sub/report.json` | 每个节点的延迟/速度/失败原因 |
| `sub/report.md` | 汇总表，适合贴到仓库首页 |

控制台输出长这样：

```
③ 真连接测试 + 测速（并发 8）
  [  1/214] ✓ 香港01 | 87ms | 12.4MB/s
  [  2/214] ✓ 日本02 | 132ms | 8.1MB/s
  [  3/214] ✗ 新加坡03        curl: (56) Recv failure
  ...
④ 筛选结果
  测试通过 96 / 214，最终保留 61
```

---

## 常用参数

```bash
python3 filter.py -c config.yaml --no-speed          # 只测延迟，快 3 倍
python3 filter.py -c config.yaml --limit 30         # 只留最快的 30 个
python3 filter.py -c config.yaml --proto vless      # 只测 vless
python3 filter.py -c config.yaml --max-delay 800    # 延迟超过 800ms 的不要
python3 filter.py -c config.yaml --no-upload        # 只生成文件，不推 GitHub
python3 filter.py -c config.yaml --dry-run          # 只抓取+解析，先看看有多少节点
```

主要配置项（`config.yaml` 的 `settings`）：

| 项 | 默认 | 说明 |
|---|---|---|
| `concurrency` | 8 | 同时测几个节点，太高会被机场风控 |
| `delay_test_url` | gstatic/generate_204 | 延迟测试目标，换 `https://cp.cloudflare.com/generate_204` 也行 |
| `speed_test_url` | cachefly 10mb | 测速目标，建议换成离你近的大文件 |
| `max_delay_ms` | 2500 | 延迟上限 |
| `min_speed_mbps` | 0.5 | 速度下限（0 = 不看速度） |
| `require_speed` | false | true = 必须测速成功才算可用 |
| `max_nodes` | 0 | 最多保留几个（0 = 不限） |
| `rename_template` | `{index:02d}·{delay}ms·{speed}·{name}` | 节点命名，占位符见配置文件 |

---

## 上传到 GitHub，变成固定订阅地址

### 方式 A：GitHub Actions 全自动（推荐）

1. 在 GitHub 新建一个仓库，把本目录所有文件推上去（`config.yaml` 里没有隐私信息）。
2. 仓库 **Settings → Secrets and variables → Actions → New repository secret**
   - 名称 `SUBS`，值是你的订阅地址，**一行一个**（支持多行）。
3. 打开 **Actions** 标签，启用 `update-subscription` 工作流，点一次 `Run workflow` 验证。
4. 之后每 6 小时自动跑一次，结果自动 commit 回仓库。

你的订阅地址就是：

```
https://raw.githubusercontent.com/<你的用户名>/<仓库名>/main/sub/base64.txt
```

国内直连 raw 常常不通，用 jsDelivr 镜像（脚本跑完会打印出来）：

```
https://cdn.jsdelivr.net/gh/<你的用户名>/<仓库名>@main/sub/base64.txt
```

> jsDelivr 有缓存（约 12 小时）。要立刻刷新可以加 `?t=时间戳`，或者用 `raw.githack.com`。
> 更稳的做法：把仓库 `sub/` 目录挂到自己的域名/Cloudflare Worker 上做反向代理。

### 方式 B：本地跑，用 PAT 推仓库

1. 生成 Token：GitHub → Settings → Developer settings → Personal access tokens
   - classic：勾 `repo`
   - fine-grained：目标仓库 + `Contents: Read and write`
2. 改 `config.yaml`：

```yaml
github:
  enabled: true
  mode: repo
  owner: 你的用户名
  repo: 仓库名
  path: sub/base64.txt
  branch: main
```

3. 跑：

```bash
export GITHUB_TOKEN=ghp_xxxxxxxx
python3 filter.py -c config.yaml
```

### 方式 C：Gist 模式（更私密）

公开仓库里的 `sub/base64.txt` 谁都能看到你的节点。不想公开就用 secret gist：

```yaml
github:
  enabled: true
  mode: gist
  gist_id: ""          # 第一次留空，脚本会新建并把 id 打印出来，填回来即可
  gist_filename: sub.txt
  gist_public: false
```

Token 需要 `gist` 权限。secret gist 的 raw 地址不需要登录就能拉，V2RayN 能直接用。

> ⚠️ 注意：`GITHUB_TOKEN`（Actions 内置的那个）**不能**创建 Gist，方式 C 必须用你自己的 PAT，并把它存成仓库 Secret（例如 `GH_PAT`），然后把工作流里的 `GITHUB_TOKEN` 换成 `${{ secrets.GH_PAT }}`。

---

## 在 V2RayN 里用

1. **订阅分组 → 订阅设置 → 添加**
2. 地址填上面的订阅链接，备注随便写
3. 保存 → **更新订阅（不走代理）**
4. 每次想刷新，右键「更新订阅」即可

因为输出是标准 base64 订阅，节点名里已经带了延迟和速度，一眼就能挑：

```
01·87ms·12.4MB/s·香港01
02·132ms·8.1MB/s·日本02
```

---

## 支持的协议

| 协议 | 内核 | 传输层 |
|---|---|---|
| vmess | xray | tcp / raw / ws / grpc / xhttp / httpupgrade / kcp / quic |
| vless | xray | 同上 + reality + vision(flow) |
| trojan | xray | tcp / ws / grpc |
| shadowsocks（AEAD / 2022） | xray | tcp（**不支持 ss 插件**：obfs、v2ray-plugin 会被跳过） |
| shadowsocks（aes-*-cfb、rc4-md5 等旧加密） | sing-box | tcp |
| vmess / vless / trojan（`net=http` 即 h2 传输） | sing-box | h2 |
| hysteria2 / hy2 | sing-box | 含 salamander obfs |
| tuic | sing-box | v5 |

**内核自动路由**：xray v25+ 移除了非 AEAD 的 shadowsocks 加密和 h2 传输，这类节点会被自动交给
sing-box 跑；反过来如果 sing-box 不支持（例如 xhttp、kcp），会回退到 xray。所以同一份订阅里
新旧写法都能测，不会因为内核不支持而被误判成「节点挂了」。

暂不支持：`ssr://`、`hysteria://`(v1)、`juicity://`、Clash YAML 订阅（请在机场后台找 base64/通用订阅链接）。

---

## 目录结构

```
.
├── filter.py              # 主程序
├── v2sub/
│   ├── fetch.py           # 抓订阅、解 base64
│   ├── parse.py           # 链接 → 内核 outbound
│   ├── core.py            # 拉起/回收 xray、sing-box
│   ├── tester.py          # 真连接延迟 + 测速
│   ├── emit.py            # 筛选、改名、生成订阅/报告
│   ├── upload.py          # GitHub 仓库 / Gist 上传
│   └── config.py          # 配置默认值与合并
├── install_core.sh        # 下载内核
├── run.sh                 # 一键本地运行
├── config.yaml            # 运行配置（可提交）
├── sources.txt            # 订阅地址（已 gitignore）
└── .github/workflows/filter.yml
```

---

## 常见问题

**Q：全部节点都被筛掉了？**
先用 `--dry-run` 确认订阅抓到了节点，再 `--no-speed --max-delay 5000` 放宽条件跑一遍，看 `sub/report.json` 里每个节点的 `error`。如果是 `内核未能监听`，多半是内核没装好；如果是 `curl: (97)` 之类，是本机网络本身出不去（测试机自己得能直连外网）。

**Q：测出来的延迟比 V2RayN 高一点？**
V2RayN 会复用已启动的内核，本工具每个节点都要冷启动一次内核，第一次 TLS 握手也更冷。差值一般在 10~50ms，不影响排序和筛选。想更接近就把 `delay_retries` 调大（取最快的一次）。

**Q：跑得很慢？**
214 个节点、开测速、并发 8，大约 5~8 分钟。关掉测速能快 2/3；把 `concurrency` 提到 16 还能再快，但机场可能限速导致误判。

**Q：测速数字很离谱（几百 MB/s）？**
说明测速 URL 被 CDN 就近命中或者文件太小提前下完了。换个大文件（比如 100MB 的测试文件）并设 `speed_timeout: 10`。

**Q：Actions 里报 `没有配置订阅源`？**
Secret `SUBS` 没配，或者名字拼错了。多行 Secret 直接粘贴多行地址即可。

**Q：仓库是私有的，V2RayN 拉不到？**
私有仓库的 raw 地址需要 Token，客户端不支持。要么仓库公开，要么用 Gist 模式，要么自建反代。

---

## 安全提醒

- **订阅链接 = 账号密码**。`sources.txt` 和 `sub/` 里的内容都等同于凭据，别提交到公开仓库、别发群里。
- 用仓库模式时，`sub/base64.txt` 会被公开，且每次 Actions 提交都会留在 git 历史里 —— 换节点记得清历史或换仓库。
- 只想自己用：优先 Gist（secret）+ 本地跑，或私有仓库 + 自建反代。
- 请仅用于个人合法的网络访问需求，遵守你所在地区的法律法规与服务商条款。
