# mml-gen-lite

极简 MML 配置生成系统 —— 以模型（Agent）为中心，一切能力通过 MCP 提供。

## 这是什么

输入：任意资料（EXP 现网快照 / 数据规划表 / 需求文档）+ 一句自然语言意图
输出：可执行的 MML 配置 + 参数表 + 分析说明 + 方案澄清

**核心设计**：没有九步编排、没有固定流程、没有网元类型限制。Agent 自己决定读什么、查什么、怎么配、什么时候收手。

```
┌──────────────────────────────────────────────────────────┐
│  前端：左 workspace 文件树 / 右对话 + SSE 实时过程        │
└────────────────────┬─────────────────────────────────────┘
                     │ POST /run
                     ▼
┌──────────────────────────────────────────────────────────┐
│  app.py（581 行）：会话 / 文件 / 运行 / 产物 / 对话       │
│    └─ agent_run.py：3 轮校验闭环 + 实时事件               │
│         └─ hermes chat -q（agent 自主 loop）              │
└────────────────────┬─────────────────────────────────────┘
                     │ MCP
     ┌───────────────┼───────────────┐
     ▼               ▼               ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│mcp_      │  │ mcp_exp  │  │  mcp_io  │
│knowledge │  │          │  │          │
├──────────┤  ├──────────┤  ├──────────┤
│特性文档   │  │EXP 识别  │  │文件列表   │
│命令文档   │  │统计规律   │  │文件读取   │
│命名规律   │  │条件查询   │  │markitdown│
│          │  │引用关系   │  │产物写入   │
│          │  │典型写法   │  │守门校验   │
│          │  │          │  │方案澄清   │
└──────────┘  └──────────┘  └──────────┘
```

## 快速开始

### 用 Docker（推荐）

```bash
docker build -f dockerfiles/Dockerfile.workflow -t mml-gen-lite .

docker run -d --name mmlgen \
  -p 8600:8600 \
  -e DEEPSEEK_API_KEY=<your-key> \
  mml-gen-lite

open http://127.0.0.1:8600/
```

### 本地跑（需要 Python 3.10+）

```bash
pip install fastapi uvicorn python-multipart pyyaml pymilvus onnxruntime \
            markitdown[pdf,docx,pptx,xlsx] mcp==1.26.0

export EXP_SESSIONS_ROOT=$PWD/sessions
export WF_ROOT=$PWD/workflow
export MML_MILVUS_DIR=$PWD/milvus-seed/milvus_mml.db
export MML_EMB_MODEL=$PWD/models/bge-small-zh-v1.5-onnx
export MML_EMB_BACKEND=onnx

python backend/app.py
```

## 目录结构

```
backend/
  app.py                581 行  FastAPI 主程序（11 个接口）
  task_runner.py        320 行  任务队列
  web/app_v3.html        40KB   前端（左树 + 右对话）
  templates/                     prompt 模板

workflow/
  agent_run.py          870 行  agent 主流程（3 轮闭环 + SSE 事件）
  guard/guard.py       1090 行  七道守门判据
  mcp/mcp_knowledge.py         知识检索 MCP（3 工具）
  mcp/mcp_exp.py               EXP 分析 MCP（5 工具）
  mcp/mcp_io.py                文件/产物/校验/澄清 MCP（6 工具）
  lib/                         Milvus 批量查询、摘要
  skills/                      检索脚本（MCP 内部调用）

rules/                  46 个 YAML 规则表
kb/                     623M  原始知识库（三产品 feature/mml/nav）
kb111/                  101M  结构化知识库
models/                  91M  嵌入模型（bge-small-zh-onnx）
milvus-seed/            358M  向量索引（3 个 collection）
scripts/                1.7M  分析脚本
tools/                        自检工具
docs/                         方案文档
dockerfiles/                  Dockerfile
```

## 会话结构

```
sessions/{sid}/
├── uploads/                 原始文件（任意类型）
├── uploads_text/            解析后 markdown
├── uploads_index.json       文件索引（含 EXP 识别结果）
├── analysis_code/           产物（覆盖式）
│   ├── mml.txt                  可执行 MML
│   ├── params.csv               参数表
│   ├── 配置分析.md               分析说明
│   └── 方案澄清.json             方案级问题
├── .agent/
│   ├── events.jsonl         实时事件流
│   ├── prompt_r1.txt        首轮 prompt
│   └── round{N}_out.txt     每轮输出
├── chat.json                对话记录
└── session.json             元信息（状态机 idle/running/done/failed）
```

## API

| 方法 | 路径 | 说明 |
|---|---|---|
| GET | `/api/v1/sessions` | 会话列表 |
| POST | `/api/v1/sessions` | 新建（form: name, product）|
| GET | `/api/v1/sessions/{sid}` | 会话详情（含文件+产物）|
| DELETE | `/api/v1/sessions/{sid}` | 删除 |
| GET | `/api/v1/sessions/{sid}/files` | 文件列表（左树数据源）|
| POST | `/api/v1/sessions/{sid}/files` | 上传（自动解析）|
| GET | `/api/v1/sessions/{sid}/file?path=` | 读文件（预览）|
| DELETE | `/api/v1/sessions/{sid}/files/{name}` | 删文件 |
| POST | `/api/v1/sessions/{sid}/run` | 触发生成 `{intent, product?}` |
| GET | `/api/v1/sessions/{sid}/run` | 查运行状态 |
| GET | `/api/v1/sessions/{sid}/events` | SSE 实时事件 |
| GET | `/api/v1/sessions/{sid}/artifacts` | 产物列表 |
| GET | `/api/v1/sessions/{sid}/artifacts/{name}` | 产物内容 |
| GET | `/api/v1/sessions/{sid}/chat` | 对话历史 |
| POST | `/api/v1/sessions/{sid}/chat` | 发消息 |
| GET | `/health` | 健康检查 |

## 核心机制

### 1. Agent 自主 loop

Agent 拿到意图和文件清单后自己决定调用顺序：

```
file_list          → 看有什么资料
exp_detect         → 判断哪个是现网快照
exp_stats          → 摸命名规律、优先级区间、枚举分布
kb_search_feature  → 查特性文档
kb_search_command  → 查命令参数和实例
artifact_write     → 写产物
guard_check        → 自检
```

### 2. 3 轮校验闭环（同一会话）

```
第 1 轮  hermes chat -q "<任务>" --pass-session-id
          ↓ 跑 guard
    不过 ↓ 把 fatal 转人话
第 2 轮  hermes chat -q "<guard 错误>" --resume <session_id>
          ↓ 再跑 guard
第 3 轮  同上
          ↓ 还不过 → failed，告诉用户哪几条没过
```

**关键**：错误回注同一会话，agent 保留完整上下文直接修，不需要重新探索。

### 3. SSE 实时推送（tool call 级）

数据源实测唯一可行路径：`hermes chat -q`（**不加 `-Q`**）的 stdout 实时打印工具预览行。

```
┊ 💻 $         cd /home/expgv && ls  0.1s          → Bash
┊ 📖 read      /opt/expgv/kb/add_urr.md  0.1s      → Read
┊ ⚡ mcp_io_fi uploads_text/域名规划.md  0.0s      → Files
┊ ⚡ mcp_exp_e uploads_text/EXP.md  0.1s           → EXP
┊ ⚡ mcp_knowl 内容计费 七层识别  1.3s             → KB
```

不用线程 / `communicate()` / `wait()` —— 三者任一都会和读循环抢 pipe。

### 4. 七道守门

| 判据 | 检查什么 |
|---|---|
| C2 | 引用闭合（引用的对象必须有定义，或在 EXP 里存在）|
| G11 | 主键唯一（含复合主键：`FLTBINDFLOWF=(FLOWFILTERNAME,FILTERNAME)`）|
| G12 | 参数格式 |
| G17 | 数量级（防把整个现网都复制进来）|
| G18 | 意图点名的族覆盖 |
| G19 | 来源标注核验（`@src=exp:L1101` 的值必须真的在那一行）|
| clarify | 方案问题边界检查 |

### 5. EXP 识别（221/221 实证）

```python
# 三行头全匹配 → 判定为 EXP
/* TIME = 2026-08-10 15:20:24.522 */
/* ME Type=UDG, Version=20.13.2  PatchVersion=20.13.2.58 */
/*USE ME:MEID=0;*/
```

提取 `ME Type`（UDG/UEG/UNC/UDC）、`Version`、`PatchVersion`。

### 6. @src 来源标注

```mml
ADD HOST:HOSTNAME="hncatv_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=10600;   // @src=plan:域名规划#1
```

**必须用 `//`**。写成 `;  @src=...`（缺双斜杠）会被当成命令内容，参数值被污染，来源标注失效。

可用类型：

```
@src=exp:L1101                  取自 EXP 第 N 行（会被核验）
@src=exp:derive L1101-L1107     派生自现网统计（区间会被核验）
@src=doc:F352:表2               取自特性文档
@src=intent:TCP80,443           意图明确给出
@src=plan:域名规划#1            用户数据规划表
@src=infer 离线URRID=在线+10000 业务逻辑推导
```

## 加新知识源

**只加文档**（零代码改动）：

```bash
# 1. 把文档放进 kb111/
cp -r your_docs kb111/output_xxx_feature/

# 2. 重建索引
python workflow/skills/mml_feature/scripts/import_feature_v3.py \
  --product XXX --data_dir kb111 --rebuild
```

**加一类新知识**（新建 collection + MCP 工具）：

1. 写导入脚本 → 建 Milvus collection
2. 在 `mcp_knowledge.py` 加一个 `kb_xxx` 工具
3. 重启容器

**加非向量知识**（规则表 / 模板）：

放进 `rules/`，prompt 里告诉 agent 去读。

## 环境变量

| 变量 | 默认 | 说明 |
|---|---|---|
| `EXP_SESSIONS_ROOT` | `/data/sessions` | 会话根目录 |
| `WF_ROOT` | `/opt/expgv/workflow` | workflow 代码目录 |
| `MML_MILVUS_DIR` | `/opt/expgv/milvus-seed/milvus_mml.db` | 向量库 |
| `MML_EMB_MODEL` | `/opt/expgv/models/bge-small-zh-v1.5-onnx` | 嵌入模型 |
| `MML_EMB_BACKEND` | `onnx` | onnx / torch |
| `MML_DEFAULT_PRODUCT` | `UDG` | 默认产品 |
| `AGENT_MAX_ROUNDS` | `3` | 校验闭环轮次 |
| `AGENT_ROUND_TIMEOUT` | `1800` | 单轮超时（秒）|
| `PORT` | `8600` | 端口 |

## 从旧版本迁移

旧的多步引擎（九步硬隔离）代码已移除。设计原因见 `docs/极简Agent方案.md`：

| 方案 | 代码量 | 命令数 | 族数 |
|---|---|---|---|
| 九步硬隔离 | 4058 行 | 8 | 7 |
| agent loop | 1040 行 | 29-38 | 12-16 |

九步方案漏掉 `FLOWFILTER / USERPROFILE / RULEBINDING / SET REFRESHSRV` 等计费链必经环节，根因是步骤间 JSON 传递导致信息衰减（②a 检索 55KB 候选 → ②b 判定「采用 0」→ ③④ 基于空依据出方案）。

## 许可

内部使用。
