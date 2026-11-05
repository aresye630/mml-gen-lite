# 系统层支持多 exp 分析（会话 / 上传 / 分析链路）

## 背景

上一版只改了脚本层（`match_features.py` 支持多 exp / 多网元），但**系统层仍只认单 exp**：

- 上传接口 `PUT /sessions/{sid}/exp` 只接一个文件
- 会话存储 `store_exp()` 一次只写一个文件
- 分析链路 `_analysis_code_fn()` 固定对 `exp_current()`（第一个文件）跑四个脚本
- 前端文件选择框没有 `multiple`

本次（2026-10-19）按用户裁决打成三层：**会话存多个 exp / 上传支持多文件 / 分析逐网元跑并汇总**。

## 改动

### 1. 存储层 `session_store.py`

| 新增/改动 | 说明 |
|---|---|
| `exp_files(sid)` | 当前版本目录下**全部** `.txt`，按名排序 |
| `exp_is_multi(sid)` | 是否多文件 |
| `exp_current(sid)` | **保持不变**：返回 `exp_files()[0]`（11 个旧调用点零改动） |
| `store_exp_multi(sid, items)` | 一次存多文件，**同一版本**、版本号只 +1；`store_exp()` 变成它的单文件封装 |
| `exp_me_info(sid)` | 扫全部文件，返回分析单元列表（file + MEID + MELN + 命令数） |
| `analysis_out(sid, sub='')` / `match_arts(sid, sub='')` | 加可选 `sub`（网元子目录）；缺省 `''` 时路径与改造前**完全一致** |
| `sanitize_me_sub(fn, meid)` | 网元子目录名安全化（中文/空格/超长 → 下划线+限长） |

`exp_me` 模块用 `importlib` 按 `SCRIPTS` 路径动态加载 —— 不用 `sys.path.insert + import`，
因为 backend 与 scripts 是两棵目录，容器内 `SCRIPTS=/opt/expgv/scripts`、开发机是源码目录。

### 2. 校验层 `exp_upload_check.py`（新增，纯函数）

从 `app_v1` 抽出来的**不依赖 fastapi** 的校验模块：

```
check_one(filename, data, product)   → {ok, errors, warnings}
check_many(items, product)           → {ok, errors, warnings, names}
```

规则（沿用 2026-09-22 用户裁决）：

| 类型 | 情形 |
|---|---|
| 硬错误 | 空文件 / 非 .txt / 文件名含路径分隔 / **同批重名** / 一个文件都没有 |
| 软提示 | 读不到 ME Type（`requires_confirm`）/ ME Type 与会话产品不符 |

**任一份硬错误 ⇒ 整体拒绝**，避免"存了一半"的半残版本。
warnings 带 `filename`，前端能定位到具体文件。

### 3. 接口层 `app_v1.py`

| 接口 | 改动 |
|---|---|
| `POST /sessions` | 新增 `files: List[UploadFile]`，可与 `exp` 混用；响应加 `exp_files` / `exp_count` |
| `PUT /sessions/{sid}/exp` | 新增 `files`；三种字段（`file`/`exp`/`files`）合并上传；响应加 `exp_files` / `exp_count` |

### 4. 分析链路 `app_v1.py`

新增 `_analysis_multi(sid, payload, mei)`：

```
for 每个分析单元（file + MEID）:
    切出该网元的命令 → 临时 exp（**保留头部注释**）
    ① feature_relations.py   -o <会话>/<exp名>__ME<id>/特性关联与公共配置/
    ② pipeline.py             -o <会话>/<单元>/analysis_code/
    ③ feature_chain_map.py
    ④ match_features.py       -o <会话>/<单元>/ --no-split-me
       gen_feature_all.py     -o <会话>/<单元>/特性配置基线/
全跑完 → <会话>/各网元汇总.json（units + aggregate + failures）
```

`_analysis_code_fn()` 开头加分流：`exp_me_info().has_multi` 为真 → 走 `_analysis_multi`，
否则**原路径一行未改**。

### 5. 前端 `app_v2.html`

- 建会话文件框：`multiple`
- 工作区上传：`inp.multiple = true`
- 本地校验改为**逐份**检查 + **同批重名**拦截
- 单文件走 `exp`/`file` 字段（旧后端兼容），多文件走 `files` 字段

## 输出结构

```
<会话>/
├── exp_v1/                      ← 一个版本，多个 txt
│   ├── ne_a.txt
│   └── ne_b.txt
├── ne_a__ME0/                   ← 每个网元一个子目录
│   ├── match_result.json
│   ├── 匹配报告.md
│   ├── 特性关联与公共配置/
│   ├── analysis_code/
│   └── 特性配置基线/
├── ne_b__ME0/
└── 各网元汇总.json              ← units + aggregate + failures
```

**单 exp 单网元时结构完全不变**（产物直接在会话根目录，无子目录、无汇总文件）。

## 实测

### 真实局点（两个 UEG 网元）

```
A: FSUPFm102BHW  2253 条命令 → 绿66 黄339 红541 人工348
B: GZUPFm101BHW  2247 条命令 → 绿66 黄339 红541 人工348
合计: 绿132 黄678 红1082 人工696
耗时: 38.0s（2 网元 × 4 脚本）
```

每个单元的判定分布与**单独跑该 exp 完全一致**（66/339/541/348），证明按网元隔离没有串味。

### 验证套件（共 116 项，全绿）

| 文件 | 项数 | 覆盖 |
|---|---|---|
| `selfcheck_multi_exp.py` | 41 | 逻辑层：存储/校验/命名（脱 fastapi） |
| `e2e_multi_exp.py` | 21 | HTTP 层：多文件上传 / 建会话同传 / 非法拒绝不留残 |
| `e2e_multi_analysis.py` | 27 | 分析流程（构造样本）：子目录产物 / 汇总一致性 / me 块 |
| `e2e_single_regress.py` | 16 | **旧行为回归**：单 exp 判定 66/339/541/348 与改造前逐项一致 |
| `e2e_real_exp.py` | 11 | 真实 exp：两局点 38s / 判定分布正确 |
| `scripts/exp_me.py` | 23 | 网元解析与切分（脚本层，上一轮已交付） |

负例注入（确认断言真会红）：
- `exp_current` 返回最后一个 → 「多文件时返回第一个」变红
- `exp_files` 不排序 → 「按名排序」变红
- 不查重名 → 两条重名断言变红
- 任一文件不合格也放行 → 两条「整体拒绝」变红

## 开发中修掉的 bug（全部靠实测发现）

| # | bug | 现象 | 后果 |
|---|---|---|---|
| 1 | 切出的临时 exp **丢了头部注释** | 下游脚本读不到 `ME Type` | 所有单元失败，且汇总 `failures=[]` 看不出原因 |
| 2 | 逐单元调 `match_features` 未带 `--no-split-me` | 产物多套一层 `<exp>/ME0/` | 后端判"没产出 match_result.json" |
| 3 | `--no-split-me` 时 `sub.out = ''` | 把用户显式给的 `-o` 清掉 | 产物跑到当前目录，`-o` 目录空 |
| 4 | `old_layout` 只判"单文件+单网元+无 -o" | 后端传了 `-o` 就走新布局 | **回归**：单 exp 产物进子目录，旧链路判失败 |
| 5 | 异常只取 `str(e)` | `BizFail` 的描述在 `details['log']` | 汇总里全是 `BizFail: INTERNAL`，无法定位 |

第 4 条是**本次改动引入的回归**，由 `e2e_single_regress.py` 拦住后修复；
`app.py` 的老通道（`/api/upload`，已失效但仍保留）也同步加了 `--no-split-me`。

## 界面显示（2026-10-19 补充）

按用户口径「界面能显示」，补齐三处：

| 位置 | 显示内容 |
|---|---|
| 会话列表 | 多文件时显示「N 个文件」，单文件/旧会话不显示（与改造前一致） |
| 会话头部 | `UEG · exp v1 · 2 个文件（ui_a.txt、ui_b.txt）· <sid>` |
| 判定卡页顶部 | `多网元（2 个 exp）FSUPFm102BHW → GZUPFm101BHW`<br>`下方判定卡展示的是 FSUPFm102BHW 这一个网元的结果`<br>`全部 2 个网元合计（不含下方筛选）：已配置 0 · 弱匹配 26 · 人工 696 · 未配置 1866` |

配套接口改动：

- `GET /sessions/{sid}` 与 `GET /sessions` 都返回 `exp_files` / `exp_count`（现算，不依赖 session.json 旧字段）
- `GET /sessions/{sid}/match` 多网元时不再 404：新增 `_primary_match_json()` 找主单元，
  并返回 `multi: true` / `units[]` / `aggregate` / `primary_unit`
- `artifacts_v1.py` 里 4 处 `match_arts(sid)['match_json']` 改走 `_primary_match_json()`，
  判定列表 / 单卡 / 报告 在多网元下都能正常打开

**判定卡展示的是"主网元"（第一个成功单元）的判定**，跨网元汇总看顶部提示条的合计行。

实测截图确认（Chrome headless）：
```
会话头：UEG · exp v1 · 2 个文件 (ui_a.txt、ui_b.txt) · 20261019_UEG_sess_a34e
提示条：多网元（2 个 exp）FSUPFm102BHW → GZUPFm101BHW
        下方判定卡展示的是 FSUPFm102BHW 这一个网元的结果
        全部 2 个网元合计（不含下方筛选）：已配置 0 · 弱匹配 26 · 人工 696 · 未配置 1866
筛选栏：全部 1294 / 已配置 0 / 弱匹配 13 / 人工确认 348 / 未配置 933（当前网元）
```

## 已知限制

1. **多网元仍只有一个构造样本验证**（手头 376 个 exp 全是单网元；真实多网元文件未见过）。
   多文件路径已用两个真实局点验证。
2. **逐单元串行执行**：N 个网元 = N × 4 个脚本，实测约 19s/网元。10 个网元约 3 分钟。
   没做并发（并发会抢 CPU 且日志交错，先保证正确性）。
3. **`各网元汇总.json` 只在多单元时生成**；单 exp 会话的产物结构与改造前完全一致。
4. ~~判定卡页没有"切换网元"的交互~~ —— **已实现**（2026-10-19），见下节。

## 切换网元（2026-10-19）

判定卡页顶部提示条里的网元名可点击，点击即切到该网元（列表、单卡、exp 原文行一起切）。

### 接口

| 接口 | 新增参数 | 说明 |
|---|---|---|
| `GET /match/cards` | `unit` | 取指定网元的判定列表；缺省 = 主网元 |
| `GET /match/cards/{fid}` | `unit` | 取指定网元的单卡详情 |
| `GET /match` | — | 返回 `multi` / `units[]` / `aggregate` / `primary_unit` |

### 实现要点

- `_resolve_unit_json(sid, unit)`：按网元名取 `<会话>/<unit>/match_result.json`
- `_unit_exp_file(sid, unit)`：按网元取**源 exp 文件**（从 `me_units[].file` 映射到 `exp_v<n>/<file>`）
  —— 不加这个，切了网元但单卡里的 exp 原文行还是第一个文件的（串数据）
- `_match_data` / `_exp_by_cmd` / `api_match_cards` / `api_match_card` 全部透传 `unit`

### 安全

`unit` 只接受会话内**已知单元名**（来自 `me_units` / `_match_units`），
不接受任意路径：`unit=../../etc`、`unit=../session.json` 都会退回主网元，
不会读到会话外文件（有专项用例 U5.1/U5.2）。

### 前端

- 网元 chip 可点击（鼠标 + 键盘 Enter/Space），当前网元高亮
- `S.cards.unit` 保存当前网元，列表与单卡请求都带上 `unit`
- 切网元回第一页、退出单卡视图
- 单 exp 会话不显示网元条，行为与改造前完全一致

### 实测（CDP 真点击）

```
点击前：FSUPFm102BHW* | GZUPFm101BHW
点击后：FSUPFm102BHW  | GZUPFm101BHW*
提示条：下方判定卡展示的是 GZUPFm101BHW 这一个网元的结果（点上方网元名可切换）
```

底层数据核对（证明真的换了数据源，不是只换高亮）：

```
FSUPFm102BHW   exp_cmds=2253  源文件=...FSUPFm102BHW_202604201614
GZUPFm101BHW   exp_cmds=2247  源文件=...GZUPFm101BHW_202604201614
```

验证套件 `e2e_unit_switch.py` 22 项全绿，负例注入：
- `_resolve_unit_json` 忽略 unit → U3.3/U3.5/U3.6 变红
- `_unit_exp_file` 忽略 unit → U4.3/U4.4 变红
