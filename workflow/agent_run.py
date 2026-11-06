#!/usr/bin/env python3
"""agent_run.py — agent 生成主流程（替代旧 loop_runner + 九步）。

★ 设计（2026-11-05 用户裁定：彻底重做，以模型为中心）
  · agent 自主 loop，代码只负责：起进程、推事件、跑校验、回注错误
  · 校验与 agent 一体化：guard 不通过 → 把错误喂回**同一 agent 会话**（--resume）
  · 最多 3 轮
  · 产物覆盖式，不保留历史

★ 为什么用 hermes chat -q（不加 -Q）
  实测三个数据源只有一个可用：
    hermes -z 的 stdout          → 进程结束才返回
    ~/.hermes/logs/agent.log     → -z 模式不写工具调用
    ~/.hermes/state.db           → 会话结束才落库
    hermes chat -q（不加 -Q）    → stdout 实时打印 `┊ 💻 $ 命令 0.2s` ✅
  `-Q/--quiet` 的作用正是 "suppress tool previews"，所以必须去掉。

★ 为什么用同步 readline 循环（不用线程 / communicate / wait）
  三者任一都会和读循环抢 pipe，实测导致读到空 / 线程不启动。
"""
import json
import os
import re
import subprocess
import time
from pathlib import Path

SESSIONS_ROOT = Path(os.environ.get('EXP_SESSIONS_ROOT', '/data/sessions'))
WORKFLOW_ROOT = Path(os.environ.get('WF_ROOT', '/opt/expgv/workflow'))
GUARD_PY = WORKFLOW_ROOT / 'guard' / 'guard.py'

MAX_ROUNDS = int(os.environ.get('AGENT_MAX_ROUNDS', '3'))
ROUND_TIMEOUT = int(os.environ.get('AGENT_ROUND_TIMEOUT', '1800'))
# ★ 2026-11-05：单轮硬上限。超过就判定为 agent 死循环，强制停。
#   实测：正常单轮 100-400s；陷入「改产物↔自检」循环的单轮能跑满 1800s。
ROUND_HARD_LIMIT = int(os.environ.get('AGENT_ROUND_HARD_LIMIT', '900'))

# ★ 2026-11-05 死循环防护上限
#   实测校准：
#     单网元正常探索 30-60 次工具调用
#     多网元（2 个 EXP）正常探索 80-120 次
#     真死循环：Guard 27 次 / 总 149 次，且集中在 Code↔Guard 交替
#   所以不能只卡总数（会误伤多网元），主要靠 guard 次数 + 耗时判。
MAX_GUARD_CALLS = int(os.environ.get('AGENT_MAX_GUARD_CALLS', '8'))
# ★ 2026-11-06：无进展判定。超过这个秒数还没写出任何产物 → 判卡住。
#   实测 c4 卡住 905s 全是反复查 EXP，产物一个没写。
STALL_SECONDS = int(os.environ.get('AGENT_STALL_SECONDS', '300'))
MAX_TOOL_CALLS = int(os.environ.get('AGENT_MAX_TOOL_CALLS', '300'))

# 产物清单
REQUIRED_ARTIFACTS = ['mml.txt', 'params.csv', '配置分析.md']

# hermes 工具预览行：┊ 💻 $  <命令>  0.2s
_TOOL_LINE = re.compile(
    r'┊\s*(\S+)\s+(\S+)\s+(.*?)\s+(-?[\d.]+)s(?:\s+\[exit \d+\])?\s*$')

_ICON_ACTION = {
    '💻': 'Bash', '💰': 'Bash', '🖥': 'Bash',
    '📖': 'Read', '📄': 'Read',
    '✍': 'Write', '📝': 'Write', '💾': 'Write',
    '🔎': 'Search', '🔍': 'Search',
    '🌐': 'Web', '🔗': 'Web',
    '🧠': 'Think', '🤔': 'Think',
    '📊': 'Code', '🐍': 'Code', '⚙': 'Code',
    '🛠': 'Tool', '🔧': 'Tool',
    '⚡': 'MCP',      # MCP 工具调用
    '📚': 'Skill',    # skill 加载
}

# MCP 工具行第二列是 server 缩写（如 mcp_io_fi / mcp_exp_e / mcp_knowl），
# 用它反推具体动作，比图标精确。
_MCP_SERVER_ACTION = {
    'mcp_io': 'IO',         # file_* / artifact_write / guard_check / clarify
    'mcp_exp': 'EXP',       # exp_detect / exp_stats / exp_query / exp_refs / exp_baseline
    'mcp_knowl': 'KB',      # kb_search_feature / kb_search_command / kb_get_naming
}

# MCP 工具名 → 动作名（从 args 或 target 里的内容推断不到时用）
_MCP_TOOL_HINTS = [
    ('mcp_io_fi', 'Files'), ('mcp_io_ar', 'Write'), ('mcp_io_gu', 'Guard'),
    ('mcp_io_cl', 'Clarify'), ('mcp_io_fi', 'Files'),
    ('mcp_exp_', 'EXP'), ('mcp_knowl', 'KB'),
]

# 从 hermes 输出里抽 session id
_SID_PATTERNS = [
    re.compile(r'Session(?:\s*ID)?[:\s]+([0-9a-zA-Z_\-]{8,})', re.I),
    re.compile(r'session[:\s]+([0-9a-zA-Z_\-]{8,})', re.I),
]


# ═══════════════════════════════════════════════════════════
# prompt 构造
# ═══════════════════════════════════════════════════════════
def build_prompt(session_id, intent_text, files_info, product_hint='', workdir=None):
    """构造首轮 prompt。"""
    lines = []
    lines.append('你是 5G 核心网 MML 配置专家。')
    lines.append('')
    lines.append(f'【会话】session_id = {session_id}')
    if product_hint:
        lines.append(f'【产品提示】{product_hint}（仅供参考，以实际文件为准）')
    lines.append('')
    lines.append('【本次任务】')
    lines.append(intent_text.strip())
    lines.append('')

    # workspace 文件清单
    lines.append('【workspace 文件】')
    if files_info:
        for f in files_info:
            tag = []
            if f.get('is_exp'):
                tag.append(f"EXP快照 {f.get('me_type') or ''} {f.get('version') or ''}".strip())
            if f.get('kind'):
                tag.append(f"类型{f['kind']}")
            if f.get('cmd_count'):
                tag.append(f"{f['cmd_count']}条命令")
            suffix = f"  [{', '.join(tag)}]" if tag else ''
            lines.append(f"  · {f.get('name')} → {f.get('parsed') or '(未解析)'}{suffix}")
    else:
        lines.append('  （没有上传文件）')
    lines.append('')

    # 二次意图：上一版产物摘要
    prev_summary = Path(workdir) / '.agent' / 'prev_summary.md' if workdir else None
    if prev_summary and prev_summary.exists():
        lines.append('【上一版产物（本轮是二次意图，基于此修改）】')
        lines.append(prev_summary.read_text(encoding='utf-8', errors='replace')[:4000])
        lines.append('')
        lines.append('⚠ 修改规则：')
        lines.append('  · 上一版已有的正确命令全部保留，只改需要改的部分')
        lines.append('  · 不要整体重写，除非用户明确要求重做')
        lines.append('  · 改完后 artifact_write 覆盖对应文件')
        lines.append('')

    lines.append('【可用工具】')
    lines.append('  exp_detect / exp_stats / exp_query / exp_refs / exp_baseline   EXP 分析')
    lines.append('  kb_search_feature / kb_search_command / kb_get_naming         知识检索')
    lines.append('  file_list / file_read / file_parse                            文件读写')
    lines.append('  artifact_write / guard_check / clarify                        产物与校验')
    lines.append('')

    lines.append('【建议流程】（你自己判断是否需要，不必机械执行）')
    lines.append('  1. file_list 看有什么资料；有 EXP 就 exp_detect 确认')
    lines.append('  2. exp_stats / kb_get_naming 摸现网命名规律和取值')
    lines.append('  3. kb_search_feature 查特性文档；kb_search_command 查命令参数')
    lines.append('  4. 推理出配置方案')
    lines.append('  5. artifact_write 写产物')
    lines.append('  6. guard_check 自检；有 fatal 自己修完再检')
    lines.append('')

    lines.append('【产物要求】写到 analysis_code/，一共这几个文件：')
    lines.append('  1. mml.txt        可执行 MML。按 Phase 分注释；引用必须闭合（后引用的对象必须先定义）')
    lines.append('  2. params.csv     参数表。列：序号,组,网元,命令族,参数,值,来源,说明')
    lines.append('       ★ params.csv 是 MML 的**唯一数据源** —— mml.txt 要能由它机械生成')
    lines.append('       ★ 需人工确认的值填【待填写】，不要编造')
    lines.append('')
    lines.append('  【params.csv 写法（重要）】')
    lines.append('    一行一个参数。同一个「组」的多行 = 一条 MML 命令。')
    lines.append('    组名格式：<命令族>#<序号>，如 HOST#1 / FILTER#1 / URR#2')
    lines.append('')
    lines.append('    例：')
    lines.append('      序号,组,网元,命令族,参数,值,来源,说明')
    lines.append('      1,HOST#1,UDG,HOST,HOSTNAME,hncatv_00_h_001,plan:域名规划#1,')
    lines.append('      2,HOST#1,UDG,HOST,DOMAINVALUE,video.hncatv.com,plan:域名规划#1,')
    lines.append('      3,HOST#1,UDG,HOST,PRIORITY,10600,exp:derive L1103,')
    lines.append('      4,FILTER#1,UDG,FILTER,FILTERNAME,hncatv_00_f_h_001,exp:derive,')
    lines.append('      5,FILTER#1,UDG,FILTER,SVRIPMODE,HOSTNAME,doc:F352,')
    lines.append('      6,FILTER#1,UDG,FILTER,HOSTNAME,@HOST#1.HOSTNAME,infer 引用HOST#1,')
    lines.append('')
    lines.append('    ⇒ 生成结果：')
    lines.append('      ADD HOST:HOSTNAME="hncatv_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=10600;')
    lines.append('      ADD FILTER:FILTERNAME="hncatv_00_f_h_001", SVRIPMODE=HOSTNAME, HOSTNAME="hncatv_00_h_001";')
    lines.append('')
    lines.append('    ★ 关联参数用引用语法 @<组名>.<参数名>，不要重复写值')
    lines.append('      这样用户改 HOST#1 的 HOSTNAME，FILTER 会自动跟着变')
    lines.append('    ★ 来源列格式：')
    lines.append('      plan:<规划文件名>#<行号>   取自数据规划表第 N 行（G20 靠这个校验覆盖率）')
    lines.append('      exp:L1101 / exp:derive L1101-L1107   取自现网')
    lines.append('      doc:<文档>:<章节>          取自特性文档')
    lines.append('      intent:<要素>              意图明确给出的')
    lines.append('      infer <规则说明>           业务推导')
    lines.append('')
    lines.append('  3. 配置分析.md    用了哪些依据、为什么选这些族、命名来源、注意事项')
    lines.append('  4. 方案澄清.json  （可选）只放方案级问题，没有就给 []')
    lines.append('')
    lines.append('【多网元场景的产物格式（重要）】')
    lines.append('  如果这次要配多个网元（如 UDG + UNC），仍然只写上面这几个文件，但要按网元分段：')
    lines.append('')
    lines.append('  mml.txt 用注释分段，每段一个网元（**分段标记必须带 ===== **）：')
    lines.append('    /* ===== 网元: UDG  UPF-HN-01  10.20.1.10 ===== */')
    lines.append('    ADD HOST:...')
    lines.append('    /* ===== 网元: UNC  SMF-HN-01  10.20.2.10 ===== */')
    lines.append('    ADD RULE:...')
    lines.append('')
    lines.append('  ★ 文件头的说明文字里不要用「网元: XXX」这种写法，')
    lines.append('    否则会被当成分段标记（后端按 /* ===== 网元: 来切分）。')
    lines.append('    想描述网元清单就写在 配置分析.md 里。')
    lines.append('')
    lines.append('  params.csv 的「网元」列（第 3 列）按网元填：')
    lines.append('    序号,组,网元,命令族,参数,值,来源,说明')
    lines.append('    1,HOST#1,UDG,HOST,HOSTNAME,xxx,plan:域名规划#1,')
    lines.append('    2,RULE#1,UNC,RULE,RULENAME,xxx,exp:derive L12902,')
    lines.append('')
    lines.append('  ★ 同一对象在不同网元下可以同名（各自网元独立），')
    lines.append('    但同一网元内不得重复定义。')
    lines.append('  ★ 单网元时网元列填该网元类型即可（如全部填 UDG）。')
    lines.append('')

    lines.append('【@src 来源标注（mml.txt 里每条命令都要标）】')
    lines.append('')
    lines.append('  ⚠ 格式硬要求：必须用双斜杠注释符')
    lines.append('')
    lines.append('    正确：  ADD HOST:HOSTNAME="x_00_h_001", DOMAINVALUE="a.com";   // @src=plan:域名规划#1')
    lines.append('    错误：  ADD HOST:HOSTNAME="x_00_h_001", DOMAINVALUE="a.com";  @src=plan:域名规划#1')
    lines.append('            ↑ 缺 // 会被当成命令内容，参数值被污染（PRIORITY 变成 "10600;  @src=..."），')
    lines.append('              来源标注全部失效，产物直接判不合格')
    lines.append('')
    lines.append('  可用类型：')
    lines.append('    // @src=exp:L1101                  取自 EXP 第 N 行（会被核验，必须真的在那一行）')
    lines.append('    // @src=exp:derive L1101-L1107 说明  派生自现网统计（区间会被核验）')
    lines.append('    // @src=doc:F352:表2               取自特性文档')
    lines.append('    // @src=intent:TCP80,443           意图明确给出的')
    lines.append('    // @src=plan:域名规划#1            用户提供的数据规划表')
    lines.append('    // @src=infer 离线URRID=在线+10000  业务逻辑推导（必须写规则）')
    lines.append('')
    lines.append('  多个标注可以并列，中间用空格分隔：')
    lines.append('    ADD HOST:...;   // @src=plan:域名规划#1 @src=exp:derive L1103-L1109 命名规律')
    lines.append('')
    lines.append('  规则：')
    lines.append('    · 有注释 = 有依据；无注释 = 无依据（占位符【待填写】天然算无依据，不用标）')
    lines.append('    · 主键参数（HOSTNAME/FILTERNAME/URRNAME/RULENAME 等）有值就必须标 @src')
    lines.append('    · 整族超过 5 条且全部无 @src → 判为空壳族')
    lines.append('    · 只要某条命令有值但没标注，就会被判为编造值')
    lines.append('')

    lines.append('【方案澄清.json 的边界（重要）】')
    lines.append('  ★★ 核心原则：先按默认方案把配置生成完，再把选择权交给用户。')
    lines.append('     不要因为某个方案点不确定就停下来问，也不要只生成一半。')
    lines.append('     遇到方案分歧时：')
    lines.append('       1) 自己选一个最合理的默认（依据 EXP 现网规律 / 意图 / 文档）')
    lines.append('       2) 按这个默认把完整配置生成出来')
    lines.append('       3) 把「我选了什么 + 为什么 + 另一个选择会怎样」写进方案澄清.json')
    lines.append('       4) 用户看完后可以选另一条，再触发一次生成')
    lines.append('')
    lines.append('  只提「影响配置方案走向」的选择题，最多 5 条，宁缺勿滥。')
    lines.append('  该问：场景选择 / 可选能力要不要 / 意图歧义 / 两条路代价不同')
    lines.append('  不该问：具体域名 IP URRID 端口值 / 某参数填什么 / 「请提供清单」/ 格式问题')
    lines.append('  格式：[{"id":"q1","question":"...","why":"...","default_choice":"当前采用的默认",')
    lines.append('         "options":[{"label":"...","reply":"...","is_default":true}]}]')
    lines.append('  options 每个 2-3 个，必须有一个 is_default=true 对应你已采用的做法。')
    lines.append('  reply 写成用户点了之后会发的原话（第一人称，不依赖上下文）。')
    lines.append('  why 里写清楚：为什么这么选、另一个选项的代价是什么。')
    lines.append('')

    lines.append('【硬要求】')
    lines.append('  · 命名：有 EXP 沿用现网统计规律（不要照抄文档示例）；无 EXP 按文档示例或用户规划')
    lines.append('  · 不要编造没有依据的数值')
    lines.append('  · 区分「现网已有」和「本次新增」：现网已有的对象不要重复创建')
    lines.append('  · 单工单规模合理：同一个族一般不超过 20-30 条（除非意图明确要求批量）')
    lines.append('  · 写完产物后调一次 guard_check；有 fatal 自己修完再调，直到通过')
    lines.append('  · 完成后简述：做了什么、哪些需要人工确认')
    lines.append('')
    lines.append('【⚠ 效率硬要求（违反会导致任务失败）】')
    lines.append('  · guard_check 最多调 3 次。第 3 次还有 fatal，就把当前状态写进产物然后收尾，')
    lines.append('    不要继续改。剩下的问题在 配置分析.md 里列出来，交给人判断。')
    lines.append('  · 不要用 execute_code / terminal 写脚本去批量修改 mml.txt。')
    lines.append('    改产物只用 artifact_write（整文件覆盖）。')
    lines.append('  · 不要反复「读自己的产物 → 跑脚本分析 → 再改」的循环。')
    lines.append('    想清楚要改成什么，一次改完。')
    lines.append('  · 单轮总耗时控制在 10 分钟内。超过说明陷入循环了，立刻收尾。')
    lines.append('')
    lines.append('【⚠⚠ 产物落盘硬要求（最容易出错的地方）】')
    lines.append('  · 4 个产物必须用 artifact_write 写到 analysis_code/，')
    lines.append('    名字严格是：mml.txt / params.csv / 配置分析.md / 方案澄清.json')
    lines.append('  · 禁止往 /tmp/ 写 mml2.txt、params2.csv 这种临时文件当"草稿"再指望转换。')
    lines.append('    实测过这样做的结果：任务结束只写出 mml.txt，params.csv 全丢。')
    lines.append('')
    lines.append('  ★★ 大文件必须分块写（否则会被模型的输出长度上限截断，产物直接丢失）')
    lines.append('    params.csv 动辄几百行、十几 KB。一次性写完必然触发')
    lines.append('    「Response truncated (finish_reason=length)」，工具调用被截断，写不出来。')
    lines.append('    正确做法：')
    lines.append('      1) artifact_write(filename="params.csv", content="表头+前30行", mode="overwrite")')
    lines.append('      2) artifact_write(filename="params.csv", content="第31-60行", mode="append")')
    lines.append('      3) 重复 append 直到写完')
    lines.append('      4) artifact_write(filename="params.csv", content="", mode="finalize")')
    lines.append('    每次 append 控制在 30-50 行以内。mml.txt 超过 100 行时同理。')
    lines.append('')
    lines.append('  · 需要迭代修改时：重新 overwrite 同名文件，不要另起文件名。')
    lines.append('  · 交付前必须自己确认这 4 个文件都写过了（缺一个任务就算失败）。')
    return '\n'.join(lines)


def build_feedback(guard_result):
    """把 guard 的 fatal 转成给 agent 的修正指令。"""
    fatal = guard_result.get('fatal') or []
    warnings = guard_result.get('warnings') or []

    lines = ['【上一轮产物未通过代码校验，请修正】', '']

    if fatal:
        lines.append('发现以下必须修正的问题：')
        for f in fatal[:10]:
            if isinstance(f, dict):
                code = f.get('code') or ''
                msg = f.get('message') or f.get('msg') or ''
                lines.append(f'  · [{code}] {msg}')
            else:
                lines.append(f'  · {f}')
        lines.append('')

    if warnings:
        lines.append('另有以下告警（建议一并处理）：')
        for w in warnings[:5]:
            if isinstance(w, dict):
                lines.append(f"  · [{w.get('code','')}] {w.get('message') or w.get('msg') or ''}")
            else:
                lines.append(f'  · {w}')
        lines.append('')

    lines.append('【修正要求】')
    lines.append('  1. 上一轮已有的正确命令全部保留，只在需要的地方增/改')
    lines.append('  2. 不能为了消除某个告警就删掉整族命令')
    lines.append('  3. 缺的对象要补上（先用 exp_query 确认现网有没有，有就复用）')
    lines.append('  4. 修完后用 artifact_write 重新写对应的产物文件')
    lines.append('  5. 再调一次 guard_check 确认')
    return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════
# 调 hermes（同步 readline + 实时事件）
# ═══════════════════════════════════════════════════════════
def call_hermes(prompt, workdir, resume_sid=None, events_fp=None,
                timeout=ROUND_TIMEOUT):
    """调 hermes 跑一轮。

    Returns (ok, out_text, elapsed, session_id, error)
    """
    env = dict(os.environ)
    env['HERMES_SKIP_NODE_BOOTSTRAP'] = '1'
    t0 = time.time()

    cmd = ['hermes', 'chat', '-q', prompt, '--yolo', '--pass-session-id']
    if resume_sid:
        cmd += ['--resume', resume_sid]

    def emit(ev):
        if not events_fp:
            return
        try:
            events_fp.write(json.dumps(ev, ensure_ascii=False) + '\n')
            events_fp.flush()
        except Exception:
            pass

    out_lines = []
    proc = None
    timed_out = False
    loop_killed = None
    _tool_cnt = {'total': 0, 'guard': 0, 'seq': []}

    try:
        proc = subprocess.Popen(
            cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1, cwd=str(workdir), env=env)

        emit({'type': 'meta', 'event': 'spawn', 'pid': proc.pid,
              'resume': bool(resume_sid)})

        assert proc.stdout is not None
        for raw in iter(proc.stdout.readline, ''):
            if time.time() - t0 > timeout:
                timed_out = True
                try:
                    proc.kill()
                except Exception:
                    pass
                break
            out_lines.append(raw)
            line = raw.rstrip('\r\n')
            if not line.strip():
                continue

            # ★ 2026-11-05 死循环防护（代码层，不依赖 prompt 自觉）
            #   统计 MCP guard 调用次数 + 总工具调用数 + Code↔Guard 交替，
            #   超限直接杀进程。
            # ★★ 2026-11-06 修正：原来每行非空输出都 +1，把 agent 的
            #   **思考文字**也当成了工具调用。实测 c1 只有 16 个真实工具行，
            #   却因为 356 行输出被判「301 次调用」误杀。
            #   现在只对「真正的工具行」（含 ┊ 前缀）计数。
            _is_tool_line = '┊' in line
            if not _is_tool_line:
                continue
            _tool_cnt['total'] += 1

            # ★★ 2026-11-06 无进展检测
            #   实测：c4 用例 agent 反复查 EXP 35 次、一个产物都没写，
            #   工具只花 8.5s 却耗满 905s，只能等时间上限。
            #   判据：超过 STALL_SECONDS 且产物一个都没写出 → 判卡住。
            if time.time() - t0 > STALL_SECONDS:
                _adir = Path(workdir) / 'analysis_code'
                _n_art = 0
                if _adir.is_dir():
                    _n_art = len([p for p in _adir.iterdir()
                                  if p.is_file() and not p.name.startswith('.')])
                if _n_art == 0:
                    loop_killed = (
                        f'agent 运行 {int(time.time() - t0)}s 仍无任何产物写出'
                        f'（已调用工具 {_tool_cnt["total"]} 次），判为卡住')
                    try:
                        proc.kill()
                    except Exception:
                        pass
                    break

            # 识别动作类型（用于判断 Code↔Guard 交替）
            _act = ''
            if 'mcp_io_gu' in line:
                _act = 'guard'
            elif '🐍 exec' in line or 'mcp_io_ar' in line:
                _act = 'code' if '🐍 exec' in line else 'write'

            if _act:
                _tool_cnt['seq'].append(_act)
                if len(_tool_cnt['seq']) > 12:
                    _tool_cnt['seq'] = _tool_cnt['seq'][-12:]
                # 最近 10 个动作里，code/guard 交替出现 ≥4 次 → 死循环
                _s = _tool_cnt['seq'][-10:]
                _alt = sum(1 for i in range(len(_s) - 1)
                           if {_s[i], _s[i+1]} == {'code', 'guard'})
                if _alt >= 4:
                    loop_killed = (f'检测到 Code↔Guard 反复交替（最近 10 次动作中 '
                                   f'{_alt} 次），判定为死循环，已终止')
                    try:
                        proc.kill()
                    except Exception:
                        pass
                    break

            if _act == 'guard':
                _tool_cnt['guard'] += 1
                emit({'type': 'meta', 'event': 'guard_call',
                      'n': _tool_cnt['guard'], 't': round(time.time() - t0, 1)})
                if _tool_cnt['guard'] > MAX_GUARD_CALLS:
                    loop_killed = (f'guard_check 被调用 {_tool_cnt["guard"]} 次'
                                   f'（上限 {MAX_GUARD_CALLS}），判定为死循环')
                    try:
                        proc.kill()
                    except Exception:
                        pass
                    break
            if _tool_cnt['total'] > MAX_TOOL_CALLS:
                loop_killed = (f'工具调用 {_tool_cnt["total"]} 次'
                               f'（上限 {MAX_TOOL_CALLS}），判定为死循环')
                try:
                    proc.kill()
                except Exception:
                    pass
                break

            m = _TOOL_LINE.search(line)
            if m:
                icon, kind, content, dur = m.groups()
                action = _ICON_ACTION.get(icon, 'Tool')
                tgt = content.strip()
                detail = content

                # ★ MCP 工具行格式：`┊ ⚡ mcp_io_fi <参数摘要> 0.0s`
                #   第二列（kind）是 server 缩写，不是 `$`。用它反推动作。
                if action == 'MCP' or kind.startswith('mcp_'):
                    srv = kind.replace('-', '_').lower()
                    hint = 'MCP'
                    for pre, name in _MCP_TOOL_HINTS:
                        if srv.startswith(pre) or srv.startswith('mcp_' + pre):
                            hint = name
                            break
                    else:
                        for pre, name in _MCP_SERVER_ACTION.items():
                            if srv.startswith(pre):
                                hint = name
                                break
                    action = hint
                    # target 已经是第一手参数（如文件路径 / 查询词）
                    tgt = tgt[:70]
                elif action == 'Skill':
                    tgt = tgt[:40]
                elif action in ('Bash', 'Code'):
                    _py = re.search(r'python3?\s+(\S+)', tgt)
                    tgt = os.path.basename(_py.group(1)) if _py else tgt[:60]
                else:
                    tgt = tgt[:70]

                emit({'type': 'step', 'kind': 'tool', 'action': action,
                      'target': tgt, 'dur': abs(float(dur)),
                      'detail': detail[:150], 'server': kind})
                continue

            # 模型回复段落（非工具行）
            s = line.strip()
            if (len(s) > 8 and not s.startswith(('Query:', '⚠', '✓', '✗', '—', '─',
                                                 '┊', '└', 'Initializing', '→'))
                    and '┊' not in s):
                pass  # 暂不推，避免噪音

        try:
            proc.wait(timeout=15)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass

        out = ''.join(out_lines)

        if timed_out:
            return False, out, round(time.time() - t0, 1), None, f'超时 {timeout}s'

        # 死循环被主动终止：out 仍然返回（产物可能已写出，交给 guard 判）
        if loop_killed:
            return False, out, round(time.time() - t0, 1), None, loop_killed

        # 抽 session id
        sid = None
        for pat in _SID_PATTERNS:
            found = pat.findall(out)
            if found:
                sid = found[-1]
                break

        return True, out, round(time.time() - t0, 1), sid, None

    except Exception as e:
        return False, ''.join(out_lines), round(time.time() - t0, 1), None, \
               f'{type(e).__name__}: {e}'
    finally:
        if proc and proc.poll() is None:
            try:
                proc.kill()
            except Exception:
                pass


def _latest_session_id():
    """从 hermes sessions list 取最新会话 id。

    ★ 为什么不用 stdout 匹配：实测 `hermes chat -q` 在 pipe 环境下
      **不打印** "Session: xxx" 那几行（只在 TTY 下打印），
      所以只能从 sessions list 拿。
    """
    try:
        r = subprocess.run(['hermes', 'sessions', 'list'],
                           capture_output=True, text=True, timeout=30)
        if r.returncode != 0:
            return None
        lines = [l for l in (r.stdout or '').split('\n') if l.strip()]
        # 跳过表头两行，第一条数据是最新的
        for ln in lines:
            m = re.search(r'(\d{8}_\d{6}_[0-9a-f]{6})\s*$', ln.strip())
            if m:
                return m.group(1)
    except Exception:
        pass
    return None


# ═══════════════════════════════════════════════════════════
# guard
# ═══════════════════════════════════════════════════════════
def run_guard(sess_dir, exp_path='', intent_path=''):
    """
    ★ exp_path 支持多个：用 ; 分隔，内部转成 --exp-multi
    """
    """跑 guard，返回结构化结果。"""
    mml = Path(sess_dir) / 'analysis_code' / 'mml.txt'
    if not mml.exists():
        return {'verdict': 'fail',
                'fatal': [{'code': 'NO_MML', 'message': 'analysis_code/mml.txt 不存在'}],
                'warnings': []}

    if not GUARD_PY.exists():
        return {'verdict': 'fail',
                'fatal': [{'code': 'NO_GUARD', 'message': f'guard 脚本不存在: {GUARD_PY}'}],
                'warnings': []}

    cmd = ['python3', str(GUARD_PY), '--mml', str(mml), '--json']
    if exp_path:
        _paths = [x for x in str(exp_path).split(';') if x.strip()]
        _paths = [x for x in _paths if Path(x).exists()]
        if len(_paths) > 1:
            cmd += ['--exp-multi', ';'.join(_paths)]
        elif _paths:
            cmd += ['--exp', _paths[0]]
    if intent_path and Path(intent_path).exists():
        cmd += ['--intent', str(intent_path)]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if not r.stdout.strip():
            return {'verdict': 'fail',
                    'fatal': [{'code': 'GUARD_CRASH',
                               'message': f'guard 无输出: {(r.stderr or "")[-200:]}'}],
                    'warnings': []}
        return json.loads(r.stdout)
    except subprocess.TimeoutExpired:
        return {'verdict': 'fail',
                'fatal': [{'code': 'GUARD_TIMEOUT', 'message': 'guard 超时 >300s'}],
                'warnings': []}
    except Exception as e:
        return {'verdict': 'fail',
                'fatal': [{'code': 'GUARD_ERROR', 'message': f'{type(e).__name__}: {e}'}],
                'warnings': []}


def rescue_tmp_artifacts(sess_dir):
    """兜底：把 agent 遗留在 /tmp 里的草稿捞回 analysis_code/。

    ★ 2026-11-06 实测：agent 有时把 params2.csv / mml2.txt 写在 /tmp/，
      最后只 artifact_write 了 mml.txt，params.csv 全丢，3 轮后任务失败。
      这里按文件名相似度捞回（params*.csv → params.csv），
      只在目标产物缺失时才捞，不覆盖 agent 正常写的。
    """
    adir = Path(sess_dir) / 'analysis_code'
    adir.mkdir(parents=True, exist_ok=True)
    recovered = []
    tmp = Path('/tmp')
    if not tmp.is_dir():
        return recovered

    patterns = {
        'params.csv': ['params*.csv', '*params*.csv'],
        'mml.txt': ['mml*.txt', '*mml*.txt'],
        '配置分析.md': ['*分析*.md', '*analysis*.md'],
        '方案澄清.json': ['*澄清*.json', '*clarify*.json'],
    }
    for target, pats in patterns.items():
        dst = adir / target
        if dst.exists() and dst.stat().st_size > 0:
            continue
        cands = []
        for pat in pats:
            for f in tmp.glob(pat):
                if f.is_file() and f.stat().st_size > 100:
                    cands.append(f)
        if not cands:
            continue
        # 取最新、最大的
        cands.sort(key=lambda f: (f.stat().st_mtime, f.stat().st_size), reverse=True)
        try:
            dst.write_text(cands[0].read_text(encoding='utf-8', errors='replace'),
                           encoding='utf-8')
            recovered.append(f'{target} ← /tmp/{cands[0].name} '
                             f'({cands[0].stat().st_size}B)')
        except Exception:
            continue
    return recovered


def check_artifacts(sess_dir):
    """检查必需产物是否齐全。"""
    adir = Path(sess_dir) / 'analysis_code'
    missing = [n for n in REQUIRED_ARTIFACTS
               if not (adir / n).exists() or (adir / n).stat().st_size == 0]
    return missing


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def run_agent(session_id, intent_text, product_hint='', on_event=None,
              resume_agent_session=None):
    """跑 agent 主流程（含 3 轮校验闭环）。

    Returns dict: {status, rounds, elapsed, produced, guard, error, session_id}
    """
    sess_dir = SESSIONS_ROOT / session_id
    adir = sess_dir / 'analysis_code'
    adir.mkdir(parents=True, exist_ok=True)
    wfdir = sess_dir / '.agent'
    wfdir.mkdir(exist_ok=True)
    # ★ 2026-11-06：每次 run 用独立子目录，避免多轮对话时互相覆盖。
    #   实测：二次意图场景连跑 3 次 run，都写 round1_out.txt，前两次被覆盖，
    #   事后无法统计每轮的真实工具调用。
    _runs = [d for d in wfdir.iterdir() if d.is_dir() and d.name.startswith('run')]
    _run_no = len(_runs) + 1
    rundir = wfdir / f'run{_run_no}'
    rundir.mkdir(exist_ok=True)
    events_path = rundir / 'events.jsonl'
    events_path.touch()

    # 落意图（guard 的 G18 需要）
    intent_file = adir / '.intent.md'
    intent_file.write_text(intent_text, encoding='utf-8')

    # 读文件清单
    files_info = []
    idx = sess_dir / 'uploads_index.json'
    if idx.exists():
        try:
            files_info = json.loads(idx.read_text(encoding='utf-8')).get('files') or []
        except Exception:
            pass

    # 找 EXP（支持多个 —— 多网元场景）
    # ★★ 2026-11-05：必须用原始 .txt，不能用 markitdown 转换后的 .md
    #   md 会加头部，行号整体偏移，G19 行号核验会全部误报
    exp_paths = []
    for f in files_info:
        if not f.get('is_exp'):
            continue
        _raw = sess_dir / (f.get('path') or '')
        if _raw.exists() and _raw.suffix.lower() in ('.txt', '.mml', '.cfg'):
            exp_paths.append(str(_raw))
            continue
        _rel = f.get('parsed') or ''
        if _rel:
            _parsed = sess_dir / _rel if '/' in _rel else sess_dir / 'uploads_text' / _rel
            if _parsed.exists():
                exp_paths.append(str(_parsed))
    exp_path = ';'.join(exp_paths) if len(exp_paths) > 1 else (
        exp_paths[0] if exp_paths else '')

    prompt = build_prompt(session_id, intent_text, files_info, product_hint,
                          workdir=sess_dir)
    (rundir / 'prompt_r1.txt').write_text(prompt, encoding='utf-8')

    events_fp = open(events_path, 'a', encoding='utf-8')
    t_start = time.time()
    # ★ 二次意图：接着上一轮的 agent 会话跑（保留完整上下文，不用重新探索）
    agent_sid = resume_agent_session or None
    rounds = []
    final_guard = None
    error = None

    try:
        for rnd in range(1, MAX_ROUNDS + 1):
            emit = {'type': 'meta', 'event': 'round_start', 'round': rnd}
            events_fp.write(json.dumps(emit, ensure_ascii=False) + '\n')
            events_fp.flush()

            cur_prompt = prompt if rnd == 1 else build_feedback(final_guard or {})
            ok, out, elapsed, got_sid, err = call_hermes(
                cur_prompt, sess_dir, resume_sid=agent_sid,
                events_fp=events_fp, timeout=ROUND_TIMEOUT)

            if got_sid and not agent_sid:
                agent_sid = got_sid
            if not agent_sid:
                # pipe 环境下 hermes 不打印 Session 行，从 sessions list 取最新
                agent_sid = _latest_session_id()

            (rundir / f'round{rnd}_out.txt').write_text(out or '', encoding='utf-8')

            if err:
                error = f'第{rnd}轮: {err}'
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'error': err})
                break

            # ★ 2026-11-05 死循环防护
            #   实测：多网元 case agent 陷入「execute_code 改产物 → guard_check
            #   → 又改 → 又 check」，149 条事件里 Code 91 次 Guard 27 次，
            #   最后 execute_code 跑满 300s 被杀，整轮 1814s 超时。
            #   这里检测「本轮耗时」和「fatal 是否在减少」，异常就强制停。
            if elapsed > ROUND_HARD_LIMIT:
                error = (f'第{rnd}轮耗时 {elapsed}s 超过 {ROUND_HARD_LIMIT}s 上限，'
                         f'判定为 agent 陷入循环（反复改产物+自检）')
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'error': 'round_slow_loop', 'fatal_limit': True})
                break

            # ★ 2026-11-06：先尝试从 /tmp 捞回 agent 遗留的草稿
            _rescued = rescue_tmp_artifacts(sess_dir)
            if _rescued:
                emit({'type': 'meta', 'event': 'rescue',
                      'round': rnd, 'files': _rescued})

            # 检查产物
            missing = check_artifacts(sess_dir)
            if missing:
                final_guard = {'fatal': [{'code': 'MISSING_ARTIFACT',
                                          'message': f'缺少产物: {", ".join(missing)}'}],
                               'warnings': []}
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'missing': missing})
                if rnd == MAX_ROUNDS:
                    error = f'3 轮后仍缺产物: {", ".join(missing)}'
                continue

            # 跑 guard
            final_guard = run_guard(sess_dir, exp_path, str(intent_file))
            verdict = final_guard.get('verdict')
            rounds.append({'round': rnd, 'elapsed': elapsed,
                           'verdict': verdict,
                           'n_fatal': len(final_guard.get('fatal') or []),
                           'n_warn': len(final_guard.get('warnings') or [])})

            events_fp.write(json.dumps({
                'type': 'meta', 'event': 'guard',
                'round': rnd, 'verdict': verdict,
                'fatal': final_guard.get('fatal') or [],
                'warnings': (final_guard.get('warnings') or [])[:5],
            }, ensure_ascii=False) + '\n')
            events_fp.flush()

            if verdict in ('pass', 'warn'):
                break
            if rnd == MAX_ROUNDS:
                error = f'3 轮后仍有 {len(final_guard.get("fatal") or [])} 个致命问题'

    finally:
        try:
            events_fp.write(json.dumps({
                'type': 'done',
                'status': 'done' if (final_guard or {}).get('verdict') in ('pass', 'warn')
                          else 'failed',
            }, ensure_ascii=False) + '\n')
            events_fp.flush()
            events_fp.close()
        except Exception:
            pass

    # 产物清单
    produced = []
    for name in ['mml.txt', 'params.csv', '配置分析.md', '方案澄清.json']:
        f = adir / name
        if f.exists():
            produced.append({'name': name, 'size': f.stat().st_size})

    verdict = (final_guard or {}).get('verdict')
    status = 'done' if verdict in ('pass', 'warn') and not error else 'failed'

    return {
        'status': status,
        'session_id': session_id,
        'agent_session': agent_sid,
        'rounds': rounds,
        'elapsed': round(time.time() - t_start, 1),
        'produced': produced,
        'guard': {
            'verdict': verdict,
            'fatal': (final_guard or {}).get('fatal') or [],
            'warnings': ((final_guard or {}).get('warnings') or [])[:10],
        },
        'error': error,
    }
