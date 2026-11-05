# 多 exp 分析与网元信息解析

## 问题

1. **只支持单个 exp**：`--exp` 只能给一个文件，多个局点要手动跑多次、结果互不相通。
2. **网元信息完全没被读取**：`gfa.parse_exp()` 把所有 `/* ... */` 注释行直接丢弃，
   所以 exp 头部声明的 `ME Type` / `Version` / `PatchVersion`，以及文档里最重要的
   `MOD ME:MEID=..., MELN="..."` 定义行，**一条都没进结果**。

实测（2026-10-19）：工作区 **376 个 exp 文件全部是单网元**，没有多网元样本。
所以切分规则只依据 exp 里的**显式声明**，不猜。

## exp 里的网元信息长什么样

```text
/* TIME = 2026-04-20 16:14:24.438 */
/* ME Type=UEG, Version=21.8.2  PatchVersion=21.8.2.20 */   ← 类型/版本
/*USE ME:MEID=0;*/                                          ← 当前活跃网元
MOD ME:MEID=0, MEIID="21.8.2.20", MELN="FSUPFm102BHW", MENAME="FSUPFm102BHW";  ← 网元定义
SET ALMINFO:ALARMID=221257870, MASKED=NO, MEID=0;           ← 命令自带的 MEID
```

| 字段 | 含义 | 实测坑 |
|---|---|---|
| `ME Type` | 产品类型（UEG/UDG/UNC） | 无 |
| `Version` | 主版本（`21.8.2`） | **已含 patch 前缀**，再拼 `PatchVersion` 会得到 `21.8.2.21.8.2.20` |
| `PatchVersion` | 完整版本（`21.8.2.20`） | 与 `MEIID` 同义 |
| `MELN` | 网元名 | **可能是字面量 `"null"`**（实测 UNC），要回退到 `MENAME` |
| `MEIID` | 网元软件版本 | 曾被误当成"网元 ID" |
| `MEID` | 网元编号，命令用它关联所属网元 | 命令行自带时以它为准 |

## 改动

### 新增 `scripts/exp_me.py`

| 函数 | 作用 |
|---|---|
| `read_exp_text()` | 读 exp（utf-8 → gbk → 替换，与 `parse_exp` 同口径） |
| `scan_me()` | 扫出 `elements`（MEID → MELN/MENAME/MEIID/命令数）、`line_meid`（逐行归属）、`has_multi` |
| `split_by_me()` | 把 `parse_exp` 的结果按 MEID 切开；`has_multi` 为假时返回单组，**与改造前等价** |
| `describe()` | 一句话描述网元（日志/报告用） |
| `expand_inputs()` | 展开输入：文件原样、目录递归取 `*.txt`、去重、不存在则报错 |

归属规则（三层，逐层精确）：

```
1. 命令行自带 MEID=N          ⇒ 归 N（最高优先，能跨回别的段）
2. 否则 = 当前 USE ME 的 MEID
3. MOD ME 行本身              ⇒ 归它**自己声明的** MEID（不是当前活跃网元）
   没有任何声明                ⇒ 退化单网元 0（老 exp 零影响）
```

### `match_features.py`

- 原 `main()` 主体改名为 `_run_single(args)`，**逻辑一行未改**，只多读
  `args._cmds`（已解析好的命令，避免 10 万行 exp 重复读）、`args._me_info` 等，
  并**返回本次统计**供汇总
- 新 `main()` 负责：展开输入 → 逐文件 `scan_me` → 按 MEID 切分 → 逐个 `_run_single` → 写汇总
- `--exp` 改为 `nargs='+'`（可给多个文件/目录），新增 `--no-split-me`（整文件当一个网元）
- `match_result.json` 的 `meta` 新增 `me` 块
- 判定逻辑**零改动**（`judge_*` / 收窄 / 公共判据全未触碰）

## 输出布局

单 exp 且未给 `-o`（旧用法，**完全不变**）：

```
match_<产品>_<exp名>/匹配报告.md
match_<产品>_<exp名>/match_result.json
```

多 exp / 多网元 / 显式给了 `-o`：

```
<out>/<exp名>/网元信息.md          ← 该 exp 的网元清单（MEID/MELN/MENAME/版本/命令数）
<out>/<exp名>/ME<MEID>/匹配报告.md
<out>/<exp名>/ME<MEID>/match_result.json
<out>/汇总.md                      ← 跨 exp/网元汇总表
<out>/summary.json                 ← 同上，机读
```

## 用法

```bash
# 1. 单个 exp（旧用法，输出布局不变）
python3 scripts/match_features.py --product UEG --exp a.txt

# 2. 多文件
python3 scripts/match_features.py --exp a.txt b.txt c.txt -o match_multi

# 3. 整个目录（递归取 *.txt）
python3 scripts/match_features.py --exp /path/to/cases -o match_multi

# 4. 单文件多网元：自动识别，不用额外参数
python3 scripts/match_features.py --exp multi_me.txt -o out

# 5. 不切分（整文件当一个网元）
python3 scripts/match_features.py --exp multi_me.txt --no-split-me
```

不指定 `--product` 时按文件名自动探测（`products.yaml` 的 `detect` 列表）。

## 实测

### 三产品单网元（旧用法回归）

| 产品 | 网元识别 | 命令数 | 绿 | 黄 | 红 | 人工 | 与改造前 |
|---|---|---|---|---|---|---|---|
| UEG | `MEID=0 FSUPFm102BHW` UEG 21.8.2 | 2,253 | 66 | 339 | 541 | 348 | **完全一致** |
| UDG | `MEID=0 YULUPF006BHW` UDG 20.16.2 | 101,231 | 48 | 188 | 145 | 54 | **完全一致** |
| UNC | `MEID=0 APP-XBXAsnSMF001BHW-04AHW011` UNC 20.16.2 | 11,136 | 49 | 338 | 160 | 62 | **完全一致** |

UNC 的 `MELN="null"` 正确回退到 `MENAME`。

### 多网元（构造样本，手头无真实样本）

```text
UEG 21.8.2 ｜ MEID=0 NE_A_UPF (5 条命令)；MEID=1 NE_B_UPF (4 条命令)
  ── MEID=0 NE_A_UPF：6 条命令 → out/xxx/ME0/
  ── MEID=1 NE_B_UPF：5 条命令 → out/xxx/ME1/
合计 2 个网元：绿 0 / 黄 130 / 红 1762 / 人工 696
```

### 多文件（两个真实 UEG 局点）

```text
[1/2] FSUPFm102BHW：MEID=0 FSUPFm102BHW → 绿 66 / 黄 339 / 红 541 / 人工 348
[2/2] GZUPFm101BHW：MEID=0 GZUPFm101BHW → 绿 66 / 黄 339 / 红 541 / 人工 348
合计 2 个网元：绿 132 / 黄 678 / 红 1082 / 人工 696
```

## 验证

```
exp_me.py 自检:  23 PASS / 0 FAIL

覆盖：单网元识别 / 多网元切分 / MOD ME 归属 / 显式 MEID 覆盖活跃网元 /
      无声明退化 / MELN=null 回退 / 版本不重复拼接 / 目录递归 / 去重 / 路径不存在

负例注入（确认断言真会红）：
  · MOD ME 行不记归属     → 「第二个 MOD ME 行归 MEID=1」变红
  · MELN 不过滤 null      → 两条 MELN=null 断言变红
```

## 已知限制

1. **多网元只用构造样本验证过**：手头 376 个 exp 全是单网元，真实多网元文件未见过。
   切分规则依据 `MOD ME` + `USE ME` 的显式声明，若真实文件用别的方式分段（如
   分隔注释块），需要再适配。
2. **`MEIID` 当版本用**：实测它是 `21.8.2.20` / `20.16.2.56` 这种软件版本号，
   与 `PatchVersion` 同义。若某些产品的 `MEIID` 另有含义，`网元信息.md` 里会显示成版本。
3. **目录递归不筛内容**：`expand_inputs` 取所有 `*.txt`，若目录里混有非 exp 的 txt
   会被当成 exp 解析（命令数为 0，不报错但会占用汇总一行）。
4. **`--no-split-me` 与真实多网元混用**：会把多个网元的命令当成一个网元，判定结果无意义。
