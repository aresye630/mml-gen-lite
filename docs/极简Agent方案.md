# expgv 极简 Agent 方案（2026-11-05）

## 0. 背景与决策

### 为什么重做

上一版是「九步硬隔离 workflow」+「agent loop」两套并存，实测数据：

| 方案 | 代码量 | 命令数 | 族数 | 问题 |
|---|---|---|---|---|
| 九步硬隔离 | 4058 行 | 8 | 7 | 步骤间 JSON 传递导致信息衰减（②a 检索 55KB 候选 → ②b 判定「采用 0」→ ③ 基于空依据出方案）|
| agent loop | 1040 行 | 29-38 | 12-16 | 计费链完整 |

**九步已删除。新方案彻底重写，只保留 agent loop 主流程。**

### 用户核心要求

1. **以模型为中心**：agent 自主决定读什么、查什么、怎么配、何时收手
2. **一切能力通过 MCP**：知识库、EXP 分析、文件解析都是 MCP 工具
3. **开放式意图**：不限网元类型、不限单网元、不限对象类型
4. **只有两个约束**：澄清方式 + 产物格式
5. **易扩展**：加知识源 / 加工具要能快速适配
6. **校验与 agent 一体化**：guard 不通过时回注同一会话，不另开会话

---

## 1. 核心架构

```
┌─────────────────────────────────────────────────────────────────┐
│  前端 app_v3.html                                                │
│  左：workspace 文件树   右：对话 + SSE 实时过程                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ POST /sessions/{sid}/chat
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│  task_runner（单 worker）                                        │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │  for round in 1..3:                                       │  │
│  │    round==1: hermes chat -q "<任务>" --pass-session-id    │  │
│  │    round>1 : hermes chat -q "<guard错误>" -r <session_id> │  │
│  │    ├─ 同步 readline 读 stdout → 解析工具行 → SSE 事件      │  │
│  │    ├─ 跑 guard（纯代码，7 道门）                            │  │
│  │    └─ 通过 → break；不过 → 错误喂回同一会话                 │  │
│  └───────────────────────────────────────────────────────────┘  │
└──────────────────────────┬──────────────────────────────────────┘
                           │ MCP 协议（stdio）
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│mcp_knowledge │   │   mcp_exp    │   │    mcp_io    │
│  3 个工具     │   │  5 个工具     │   │   6 个工具    │
└──────────────┘   └──────────────┘   └──────────────┘
  知识库检索          EXP 分析          文件/产物/校验/澄清
```

### 为什么 3 个 server

- **1 个**：启动快，但一处出错全挂，增删工具要动大文件
- **3 个**：启动多 2 次 stdio 握手（约 +0.3s），但**知识源可独立增删**（加知识库只动 mcp_knowledge）、故障隔离
- 内存增量：约 30-50MB

---

## 2. 目录结构

```
/data/sessions/{sid}/
├── uploads/             用户上传的原始文件（任意类型）
├── uploads_text/        markitdown 转换后的 markdown
├── uploads_index.json   文件索引
├── analysis_code/       产物（覆盖式，不保留历史）
│   ├── mml.txt              [必须] 可执行 MML
│   ├── params.csv           [必须] 参数表
│   ├── 配置分析.md          [必须] 分析说明
│   └── 方案澄清.json        [可选] 方案级问题
└── chat.json            对话记录
```

**没有 gen1/gen2/run1/run2** —— 每次改进直接覆盖 `analysis_code/`。

**不生成确认清单.md**。

### uploads_index.json 格式

```json
{
  "session": "20261105_UDG_xxx",
  "updated_at": "2026-11-05T08:00:00+00:00",
  "files": [
    {
      "name": "EXPMML_ME0_UDG_20.13.2.58_xxx.txt",
      "size": 2353143,
      "kind": "text",
      "parsed": "EXPMML_ME0_UDG_20.13.2.58_xxx.md",
      "is_exp": true,
      "me_type": "UDG",
      "version": "20.13.2",
      "patch_version": "20.13.2.58",
      "cmd_count": 16355,
      "error": null,
      "notes": ["识别为 MML 现网快照"]
    }
  ],
  "summary": {"total": 2, "ok": 2, "failed": 0, "exp_count": 1}
}
```

---

## 3. MCP 工具清单（3 server / 14 工具）

### 3.1 mcp_knowledge（知识源，可独立增删）

| 工具 | 参数 | 返回 |
|---|---|---|
| `kb_search_feature` | `query, product?, top_k?` | 特性文档列表：名称、适用网元、操作场景、关联对象 |
| `kb_search_command` | `name \| query, product?` | 命令文档：参数表（类型/枚举/必选）、使用实例 |
| `kb_get_naming` | `product, family` | 该族命名规律（从现网统计得出）|

**实现**：内部调用现有 `skills/mml_feature/scripts/mml_feature_query.py` 和 `skills/mml_support/scripts/mml_support_query.py`

### 3.2 mcp_exp（EXP 分析，纯确定性代码）

| 工具 | 参数 | 返回 |
|---|---|---|
| `exp_detect` | `path` | `{is_exp, me_type, version, patch_version, cmd_count}` |
| `exp_stats` | `path, family?` | 每族条数、命名规律、优先级区间、枚举值分布 |
| `exp_query` | `path, family?, param?, value?` | 匹配的命令列表（可限量）|
| `exp_refs` | `path, object_name` | 被谁引用 + 引用了谁 |
| `exp_baseline` | `path, families[]` | 典型写法样例（供参考）|

### 3.3 mcp_io（文件 + 产物 + 校验 + 澄清）

| 工具 | 参数 | 返回 |
|---|---|---|
| `file_list` | — | 文件清单 + 类型 + 解析状态 + 是否 EXP |
| `file_read` | `path, offset?, limit?` | 文件内容 |
| `file_parse` | `path` | markitdown 转换，自动存 `uploads_text/` |
| `artifact_write` | `filename, content` | 写入 `analysis_code/`（限 4 个固定名字）|
| `guard_check` | `exp_path?` | 七道门结果 `{fatal[], warnings[]}` |
| `clarify` | `questions[]` | 提交方案级问题（前端渲染可点选卡片）|

---

## 4. 主流程

```
1. 用户上传文件（任意类型）
   → mcp_io.file_parse 自动转 markdown 到 uploads_text/
   → 校验头部三行，判断是否 EXP，写入 uploads_index.json

2. 用户输入意图（自然语言，可跨网元、可开放式）

3. task_runner 启动 agent：
   hermes chat -q "<prompt>" --yolo \
     --skills "" \
     --pass-session-id

   prompt 包含：
   · workspace 文件清单（从 uploads_index.json）
   · 本轮意图
   · 产物要求（4 个文件、@src 标注规则）
   · 结束条件（写完产物后调 guard_check）

4. agent 自主 loop（它自己决定顺序）：
   · file_list            → 看有什么
   · exp_detect           → 判断哪个是现网快照
   · exp_stats / exp_baseline / exp_query / exp_refs
   · kb_search_feature / kb_search_command / kb_get_naming
   · 推理方案
   · artifact_write × 4
   · guard_check
   · 不过自己修
   · clarify（如果有方案问题）

5. task_runner 收尾：
   · 跑 guard（纯代码，后端兜底）
   · 通过 → done
   · 不通过 → 把 fatal 转人话，-r 同一会话续跑（最多 3 轮）
   · 3 轮仍不过 → failed，告诉用户哪几条没过
```

---

## 5. 校验闭环（3 轮，同一会话）

### 5.1 循环逻辑

```python
session_id = None
for round in range(1, 4):          # 3 轮
    if session_id is None:
        out = call_hermes(prompt, workdir, pass_session_id=True)
        session_id = extract_session_id(out)
    else:
        out = call_hermes(feedback, workdir, resume=session_id)

    g = run_guard(mml_path, exp_path, intent_path)
    if g['verdict'] in ('pass', 'warn'):
        break

    feedback = format_guard_feedback(g)   # fatal 转成人话
else:
    status = 'failed'                      # 3 轮都没过
```

### 5.2 feedback 格式（喂回 agent 的原话）

```
【上一轮产物未通过代码校验，请修正】

发现以下问题：
  · C2 引用悬空 2 处：URRGRPBINDING.DFTURRGRPNAME=xxx 被 4 条引用但无定义
  · G18 意图要求的族缺失：ADD URR、ADD URRGROUP

【修正要求】
  1. 上一轮已有的命令全部保留，只在需要的地方增/改
  2. 不能为了消除某个告警就删掉整族命令
  3. 缺的族要补上
  4. 修完自己再调一次 guard_check 确认
```

### 5.3 为什么用同一会话（`-r`）

- agent 保留完整上下文（读过哪些文件、推导过程）
- 不需要重新探索，直接修
- 这是「校验与 agent 一体化」的关键

### 5.4 hermes 续跑机制

```bash
# 首轮：输出 session id
hermes chat -q "<任务>" --pass-session-id

# 续跑：同一会话
hermes chat -q "<反馈>" -r <session_id>
```

---

## 6. EXP 识别规则（实证 221/221 = 100%）

### 6.1 头部格式

```
第 1 行：/* TIME = 2026-08-28 09:00:16.278 */
第 2 行：/* ME Type=UDG, Version=20.13.2  PatchVersion=20.13.2.58 */
第 3 行：/*USE ME:MEID=0;*/
第 4 行起：SET LICENSESWITCH:LICITEM="...", SWITCH=ENABLE;
```

### 6.2 校验正则

```python
EXP_HEADER_PATTERNS = [
    (1, r'^/\* TIME = \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+(\+8:00)? \*/$'),
    (2, r'^/\* ME Type=(\w+), Version=([\d.]+)\s+PatchVersion=([\d.]+) \*/$'),
    (3, r'^/\*USE ME:MEID=(\d+);\*/$'),
]
```

**三条全匹配 → 判定为 EXP**，同时从第 2 行提取 ME Type / Version / PatchVersion。

### 6.3 实证结果

```
样本：221 个真实 EXP 文件（>100KB，覆盖 UDG/UEG/UNC/UDC）
结果：221/221 匹配（100%）
ME Type 分布：UDG 120 / UEG 79 / UNC 20 / UDC 2
```

失败的样本全是测试假文件（3-4 字节的 `EXPMML_ME0_UEG_mx.txt` 之类）。

---

## 7. 产物要求（唯一硬约束之一）

### 7.1 四个文件

| 文件 | 必须 | 说明 |
|---|---|---|
| `mml.txt` | ✅ | 可执行 MML，按 Phase 分注释，引用必须闭合 |
| `params.csv` | ✅ | 参数表（序号/命令族/参数/值/来源/说明），缺值标【待填写】 |
| `配置分析.md` | ✅ | 用了哪些依据、为什么选这些族、命名来源、注意事项 |
| `方案澄清.json` | ❌ | 只放方案级问题，没有给 `[]` |

### 7.2 写入约束

`artifact_write(filename, content)` **只接受这 4 个名字**，其他一律拒绝。

### 7.3 @src 来源标注规则

每条命令的行尾用注释标依据：

```
@src=exp:L1101                    取自 EXP 第 N 行（守门会去核验）
@src=exp:derive L1101-L1107 说明   派生自现网统计（区间可核验）
@src=doc:F352:表2                 取自特性文档
@src=intent:TCP80,443             意图明确给出的
@src=plan:域名规划#1              用户提供的数据规划表
@src=infer 离线URRID=在线+10000    业务逻辑推导（必须写规则）
```

**规则**：
1. 有注释 = 有依据；无注释 = 无依据（占位符【待填写】天然算无依据）
2. 主键参数（HOSTNAME/FILTERNAME/URRNAME/RULENAME/USERPROFILENAME 等）有值就必须标 @src
3. 整族超过 5 条且全部无 @src → 判为空壳族
4. `@src=exp:L###` 会被自动核验——值必须真的在那一行里

---

## 8. 方案澄清（唯一硬约束之二）

### 8.1 边界（用户裁定）

**只问影响配置方案走向的选择题，最多 5 条，宁缺勿滥。**

✅ 该问的：
- 场景选择（如 F352 场景一缺省费率 / 场景二单独费率）
- 要不要某个可选能力（如是否需要七层 L7FILTER 识别）
- 意图歧义（如"调整刷新服务器"是新建绑定还是改存量）
- 两个方案都能做但代价不同（如复用现网对象 vs 全新建）

❌ 不该问的（一律进 params.csv）：
- 具体域名 / IP / URRID / 端口 / 优先级的值
- 某个参数该填什么
- 「请提供完整清单」这类要数据的要求
- 格式问题、语法问题（agent 自己定）

### 8.2 格式

```json
[
  {
    "id": "q1",
    "question": "本次计费走哪个场景？",
    "why": "F352 场景一用缺省费率 RG=2000000002 只建 URRGROUP；场景二要单独 ADD URR 并指定 URRID",
    "options": [
      {"label": "场景一：缺省费率", "reply": "按场景一配，用缺省费率 RG=2000000002，只建 URRGROUP"},
      {"label": "场景二：单独费率", "reply": "按场景二配，需要单独 ADD URR，URRID 我后续在参数表填"}
    ]
  }
]
```

### 8.3 前端渲染

```
❓ 方案待确认（2 项）
┌────────────────────────────────────────┐
│ 1. 本次计费走哪个场景？                 │
│    场景一用缺省费率；场景二需单独 ADD URR│
│    [场景一：缺省费率] [场景二：单独费率] │
│    [✎ 自己写]                          │
└────────────────────────────────────────┘
```

点选项 → 文字自动填进输入框 → 用户可编辑 → 发送
点「自己写」→ 展开文本框 → 输入后发送

---

## 9. 状态机

```
idle → running → done | failed
```

| 状态 | 含义 | 触发 |
|---|---|---|
| `idle` | 空闲 | 建会话 / 上一轮完成 |
| `running` | agent 跑着 | 用户发消息 |
| `done` | 完成 | guard 通过 |
| `failed` | 失败 | 3 轮仍不过 / agent 报错 |

**删除**：`exp_ready` / `analyzing` / `matched`

---

## 10. 实时过程推送（SSE）

### 10.1 数据源（实测唯一可行）

| 数据源 | 实时性 |
|---|---|
| `hermes -z` 的 stdout | ❌ 进程结束才返回 |
| `~/.hermes/logs/agent.log` | ❌ `-z` 模式不写工具调用 |
| `~/.hermes/state.db` | ❌ 会话结束才落库 |
| **`hermes chat -q`（不加 `-Q`）的 stdout** | ✅ **实时打印工具预览行** |

### 10.2 实现要点

```python
# 必须用同步 readline 循环
# 不能用 communicate() / wait() / threading —— 都会和读循环抢 pipe

proc = subprocess.Popen(
    ['hermes', 'chat', '-q', prompt, '--yolo', '--pass-session-id'],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    text=True, bufsize=1, cwd=workdir, env=env)

for raw in iter(proc.stdout.readline, ''):
    line = raw.rstrip('\r\n')
    m = _TOOL_LINE.search(line)   # ┊ 💻 $ <命令>  0.2s
    if m:
        emit({'type': 'step', 'kind': 'tool', 'action': ..., 'target': ...})
```

### 10.3 事件格式

```json
{"type":"meta","event":"spawn","pid":70}
{"type":"step","kind":"tool","action":"Read","target":"uploads_text/域名规划.md","dur":0.1}
{"type":"step","kind":"tool","action":"Bash","target":"gen_mml.py","dur":2.3}
{"type":"step","kind":"tool","action":"Write","target":"analysis_code/mml.txt","dur":0.02}
{"type":"done","status":"done","produced":["mml.txt","params.csv"]}
```

### 10.4 图标 → 动作映射

```
💻 → Bash    📖 → Read    ✍ → Write    🔎 → Search
🐍 → Code    🌐 → Web     🧠 → Think    🛠 → Tool
```

### 10.5 前端渲染（仿 DeepSeek harness）

```
执行过程  12 个动作 · 1m20s

Think
Read      uploads_text/域名规划.md
Search    ADD HOST:
Bash      gen_mml.py
Write     analysis_code/mml.txt
...
```

---

## 11. 文件解析（markitdown）

### 11.1 依赖

```dockerfile
RUN pip install 'markitdown[pdf,docx,pptx,xlsx]'
```

预计镜像增量 100-150MB。

### 11.2 支持的格式

| 类型 | markitdown 支持 |
|---|---|
| docx / doc | ✅ |
| xlsx / xls | ✅ |
| pptx | ✅（之前不支持，新增）|
| pdf | ✅ |
| csv / json / xml / txt / md | ✅ |
| html | ✅ |

### 11.3 实现（约 50 行）

```python
from markitdown import MarkItDown

def parse(path, out_dir):
    md = MarkItDown()
    result = md.convert(str(path))
    out = out_dir / (path.stem + '.md')
    out.write_text(result.text_content, encoding='utf-8')
    return out
```

### 11.4 不保留自建解析

**删除** `workflow/file_parser.py`（369 行）。
markitdown 解析失败 → 直接报错给 agent，不静默兜底。

---

## 12. 代码变化

### 12.1 删除（约 3900 行）

| 内容 | 位置 | 行数 |
|---|---|---|
| `_analysis_multi` / `_analysis_code_fn` | app_v1.py | 329 |
| `/analysis` / `/fingerprint-match` | app_v1.py | 20 |
| `/match` / `/match/cards` 系列 | artifacts_v1.py | 254 |
| `/exp` / `/exp/impact` / `/exp/apply` | app_v1.py | ~300 |
| `loop_runner.py`（编排逻辑，保留 readline 解析）| workflow/ | 852 |
| `file_parser.py`（换 markitdown）| workflow/ | 369 |
| 状态机 exp_ready/analyzing/matched | app_v1.py | ~200 |
| 旧测试（e2e_* / selfcheck_* / cdp_click / run_dev_server）| backend/ | ~2300 |
| 匹配卡 UI + 旧前端 | web/ | 已删 app_v2.html |

### 12.2 新建（约 1600 行）

| 模块 | 内容 | 行数 |
|---|---|---|
| `mcp/mcp_knowledge.py` | 3 个知识检索工具 | ~250 |
| `mcp/mcp_exp.py` | 5 个 EXP 分析工具 | ~350 |
| `mcp/mcp_io.py` | 6 个文件/产物/校验/澄清工具（含 markitdown 封装）| ~350 |
| `task_runner.py` | 重写：同步 readline + 3 轮校验闭环 + `--resume` | ~300 |
| `session_mgmt.py` | 简化状态机（idle/running/done/failed）| ~300 |
| 前端适配 | 去匹配卡、加澄清交互 | 改 ~300 |

### 12.3 保留

| 模块 | 行数 | 说明 |
|---|---|---|
| `guard/guard.py` | 1006 | 七道门（C2/G11/G12/G16/G17/G18/G19）|
| `lib/bulk_query.py` | 191 | Milvus 批量查询（MCP 内部复用）|
| `lib/summary.py` | 208 | 摘要 |
| `skills/`（mml_feature / mml_support 的 scripts）| — | MCP 内部调用 |
| 知识库 + 模型 + Milvus 索引 | — | 不变 |

---

## 13. 实施顺序

```
第 1 步  mcp_exp + mcp_io（含 markitdown）+ 单测
第 2 步  mcp_knowledge + 单测
第 3 步  task_runner 重写（同步 readline + 3 轮闭环 + --resume）
第 4 步  会话管理简化 + 状态机
第 5 步  前端适配
第 6 步  删旧代码
第 7 步  端到端验证
```

---

## 14. 验证标准

### 14.1 单测（每个 MCP 工具）

```
· 正常输入 → 正确输出
· 边界输入 → 合理报错
· 错误输入 → 不崩溃
```

### 14.2 EXP 识别（已验证）

```
221/221 真实 EXP 文件匹配（100%）
```

### 14.3 端到端

```
· 上传 EXP + 数据规划 → 意图 → 生成
· 无 EXP 只上传规划 → 生成
· 首次校验失败 → agent 自动修 → 通过
· 3 轮仍失败 → 标 failed 并说明原因
· SSE 实时推送（tool call 级）
· 二次意图（同一会话增量改）
```

### 14.4 Guard 判别力（历史验证保持）

```
7 个历史产物，逐条核对预期：
  run1(373条)   FAIL   G17 数量级 4 条超限
  run2(50条)    FAIL   真漏 SET REFRESHSRV
  run3(38条)    PASS
  二次A/B/C     PASS
  loop第3轮(旧)  FAIL   G18 抓到删族
```

---

## 15. 风险与对策

| 风险 | 影响 | 对策 |
|---|---|---|
| agent 过度自由 | 可能不写产物 | `artifact_write` 限名 + 结束前 `guard_check` |
| agent 不停手 | 无限循环 | 3 轮上限 + prompt 说明结束条件 |
| markitdown 解析失败 | agent 读不到文件 | 明确报错，不静默兜底 |
| 历史数据不兼容 | 老会话读不了 | 保留读取兼容，不做迁移 |
| 前端改动大 | 要重测 | 逐步替换，保留回滚能力 |

---

## 16. 备份

移除的代码已备份到：

```
~/workspace/expgv-buildkit-legacy-20261105/
├── backend/     （35 项，含 e2e/selfcheck/app_v2.html）
├── workflow/    （38 项，含九步残留）
└── BACKUP_INFO.json  （git head: 9fc5761f7）
```

---

## 附录 A：hermes 关键命令

```bash
# 首轮（输出 session id，用于续跑）
hermes chat -q "<任务>" --yolo --pass-session-id

# 续跑同一会话
hermes chat -q "<反馈>" -r <session_id> --yolo

# 不带 -Q（重要！-Q 会隐藏工具预览，无法解析实时过程）
# 带 --skills 但新方案不需要（能力都走 MCP）
```

## 附录 B：MCP 注册

`/home/expgv/.hermes/config.yaml`：

```yaml
mcp_servers:
  knowledge:
    command: python3
    args: [/opt/expgv/workflow/mcp/mcp_knowledge.py]
  exp:
    command: python3
    args: [/opt/expgv/workflow/mcp/mcp_exp.py]
  io:
    command: python3
    args: [/opt/expgv/workflow/mcp/mcp_io.py]
```

## 附录 C：关键实测数据

| 项 | 数据 |
|---|---|
| EXP 识别准确率 | 221/221 (100%) |
| 九步 vs loop 命令覆盖 | 8 条/7 族 vs 29-38 条/12-16 族 |
| SSE 事件粒度 | tool call 级（Read/Write/Bash/Search/Code）|
| guard 判别力 | 7/7 正确（历史产物验证）|
| 二次意图保留率 | 98%（追加）、精确删除、最小改动 |
