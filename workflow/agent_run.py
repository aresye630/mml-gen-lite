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


def round_hard_limit_for(sess_dir):
    """按工单复杂度返回单轮硬上限（秒）。

    ★ 2026-11-08 新增：原来固定 900s，复杂工单正常就需要 15-25 分钟，
      被误判成死循环。实测失败案例：
        NC20260806001780  单轮 912s（154 条命令）
        NC20260825001638  单轮 1245s
        NC20260828000360  单轮 1560s（1227 条命令）
      重跑时同一工单分别 702s / 1233s / 1103s 通过 —— 说明不是死循环，就是慢。

      复杂度判据：params.csv 行数（agent 生成前就能看到）
        实测相关性：params.csv 行数 vs GT 命令数 = 0.98
        （对比 EXP 大小只有 0.23，不能用）
    """
    try:
        import csv as _csv
        from pathlib import Path as _P
        csv_p = _P(sess_dir) / 'analysis_code' / 'params.csv'
        if not csv_p.exists():
            # 还没写产物 → 用上传的 params.csv
            ups = list(_P(sess_dir).glob('uploads/*params*.csv'))
            csv_p = ups[0] if ups else None
        if not csv_p or not csv_p.exists():
            return ROUND_HARD_LIMIT
        n = sum(1 for _ in open(csv_p, encoding='utf-8', errors='replace'))
        # ★ 2026-11-09 调整：新判据让配置量变大
        #   同名前缀属性族判据生效后，配 1 个 APN 要写 32 条命令
        #   （ADD APN + 31 个 SET APNxxx），params.csv 行数暴涨，
        #   原阈值（>500 → 1800s）不够用。
        #   实测第三轮全量：
        #     NC20260824002020  1512s 超 1200s 上限失败
        #     NC20260907000688  1472s 超 1200s 上限失败
        #     NC20260909000612  1422s（超了但完成了）
        #   新阈值：整体上抬一档，避免把「活干多了」误判成死循环。
        if n > 800:
            return 2400      # 很复杂：>800 行
        if n > 300:
            return 1800      # 复杂：300-800 行
        if n > 100:
            return 1500      # 中等：100-300 行
        return ROUND_HARD_LIMIT   # 简单：<100 行（900s）
    except Exception:
        return ROUND_HARD_LIMIT

# ★ 2026-11-05 死循环防护上限
#   实测校准：
#     单网元正常探索 30-60 次工具调用
#     多网元（2 个 EXP）正常探索 80-120 次
#     真死循环：Guard 27 次 / 总 149 次，且集中在 Code↔Guard 交替
#   所以不能只卡总数（会误伤多网元），主要靠 guard 次数 + 耗时判。
# ★ 2026-11-06 调整：8 → 10。实测正常修产物时 guard 会调 4-5 次，
#   留 10 次余量；真死循环靠「严格连续交替」判定更准。
# ★ 2026-11-12 调整 15 → 25
#   实测 NC20260828000409（GT 148 条命令）：
#     agent 调 guard_check 16 次被判死循环，但产物齐全（mml.txt 28KB / params.csv 58KB）
#     且第 1 轮 guard verdict=pass（n_fatal=0, n_warn=0）
#   → 16 次是「反复自检试图收敛」，不是死循环
#   大单（GT > 100 条）需要更多次自检，15 次太紧
#   真死循环还有 ROUND_HARD_LIMIT 900s 兜底
#
# ★ 2026-11-12 调整 25 → 8（与 prompt 对齐）
#   实测 NC20260828000360（v15）：agent 调 guard_check 26 次，
#     从第 22 次起间隔只有 14-17 秒（改一点→立即自检→又改 的循环）
#     最终 fatal=0（问题其实已经清零），但因为调用次数超限被判失败。
#   → 上限 25 太松，agent 觉得「还有余量」就反复自检
#   → prompt 里写的是「最多调 6 次」，代码上限应该一致
#   真死循环还有 ROUND_HARD_LIMIT 兜底
#
# ★ 2026-11-13 调整 8 → 12（8 太紧，误杀正常修复）
#   实测 8 个小单：
#     通过的单 guard_check 调用：3, 4, 3, 4, 5 次
#     失败的单：9, 9 次 ← 刚好被我设的 8 卡掉，但其实还在正常修
#   → 通过的单最多 5 次，设 12 留 7 次余量
# ★ 2026-11-13 最终定档：12 → 40（只作「防无限」极高档兜底）
#   用户裁定：死循环判据应该看「是不是重复报同一个错」，不是看调了几次。
#   真正的判据在 call_hermes 里：连续 3 次 fatal 集合完全不变才杀。
#   这里只防「agent 无限自检」这种极端情况，40 次足够宽松。
MAX_GUARD_CALLS = int(os.environ.get('AGENT_MAX_GUARD_CALLS', '40'))
# ★ 2026-11-06：无进展判定。超过这个秒数还没写出任何产物 → 判卡住。
#   实测 c4 卡住 905s 全是反复查 EXP，产物一个没写。
# ★ 2026-11-06 调整 300 → 480：大 EXP（40MB+）的正常探索就会超过 300 秒，
#   实测 NC20260819001887 在 304 秒被杀时还在正常探索（只是探索方式不对）。
#   现在配合「禁止用 execute_code 解析 EXP」的 prompt 约束，
#   给 480 秒余量让 agent 走正确路径（exp_query）。
STALL_SECONDS = int(os.environ.get('AGENT_STALL_SECONDS', '480'))
MAX_TOOL_CALLS = int(os.environ.get('AGENT_MAX_TOOL_CALLS', '300'))


# ★★ 2026-11-14 性能优化：按工单规模自适应 STALL 阈值和执行超时
#
#   问题（75 单全量实测）：
#     3 单 STALL（NC20260814000701 / NC20260804001027 / NC20260805002150）
#     都是 20-30 条命令的小单，却在 480s 时还没写出第一个产物
#     工具调用只有 24-51 次 → 平均每次 10-20s，是 LLM 响应慢，不是死循环
#
#     重验 NC20260814000701：
#       上次：480s 时 0 产物 → STALL 判死
#       这次：196s 写出第 1 个产物 → 203s 完成（verdict=pass）
#     → 同一单同一镜像，结果差 2.4 倍，纯 LLM 响应速度波动
#
#   数据支撑（75 单）：
#     按 GT 命令数分档的耗时：
#       1-30 条：中位 294s，P90 562s，最长 1802s
#       31-100：中位 572s，P90 1588s，最长 2574s
#       101-300：中位 917s，P90 2595s
#       301-800：中位 1459s
#       >800：中位 1824s，最长 2716s
#
#     规模相关性（数据清单行数预测 GT 命令数）：r = 0.950
#     → 上传清单后就能估出预期耗时，不用等 params.csv（agent 生成后才有）
#
#   新策略：
#     规模估算 perf_scale(sess_dir) → 返回 'small'|'medium'|'large'|'xlarge'
#     STALL 阈值 = 基准 480s × 规模系数（小 1.0 / 中 1.5 / 大 2.5 / 特大 3.5）
#     执行超时同理由规模决定，不再依赖 params.csv 行数

# 规模 → (STALL 秒数, 单轮执行超时秒数, 说明)
_PERF_TIERS = {
    'small':  (480, 900,  '<=30 条命令'),        # 实测 P90 562s
    'medium': (720, 1800, '31-300 条命令'),      # 实测 P90 1588s
    'large':  (1200, 2400, '301-800 条命令'),    # 实测中位 1459s
    'xlarge': (1680, 3600, '>800 条命令'),       # 实测最长 2716s
}


def perf_scale(sess_dir):
    """按上传的数据清单规模估算工单复杂度。

    优先看上传的数据清单（上传时就有），没有则看 params.csv/EXP 行数。
    返回 'small' | 'medium' | 'large' | 'xlarge'
    """
    import re as _re
    from pathlib import Path as _P
    try:
        sd = _P(sess_dir)

        # 1) 上传的数据清单（最可靠：与 GT 命令数相关性 0.950）
        n_rows = 0
        for f in list(sd.glob('uploads/*清单*.md')) + list(sd.glob('uploads_text/*清单*.md')):
            try:
                txt = f.read_text(encoding='utf-8', errors='replace')
            except Exception:
                continue
            cnt = 0
            for line in txt.split('\n'):
                s2 = line.strip()
                if s2.startswith('|') and '---' not in s2:
                    cnt += 1
            n_tables = len(_re.findall(r'^## ', txt, _re.M))
            n_rows = max(n_rows, max(0, cnt - n_tables))
            if n_rows:
                break

        # 2) 退化：params.csv 行数
        if not n_rows:
            for cand in [sd / 'analysis_code' / 'params.csv'] + list(sd.glob('uploads/*params*.csv')):
                if cand.exists():
                    try:
                        n_rows = sum(1 for _ in open(cand, encoding='utf-8', errors='replace'))
                    except Exception:
                        pass
                    break

        # 3) 全都没有 → 按小单处理
        if not n_rows:
            return 'small'

        if n_rows > 800:
            return 'xlarge'
        if n_rows > 300:
            return 'large'
        if n_rows > 30:
            return 'medium'
        return 'small'
    except Exception:
        return 'small'


def stall_seconds_for(sess_dir):
    """按规模返回 STALL 阈值（秒）。"""
    try:
        if not os.environ.get('AGENT_STALL_SECONDS'):
            return _PERF_TIERS[perf_scale(sess_dir)][0]
    except Exception:
        pass
    return STALL_SECONDS


def round_timeout_for(sess_dir):
    """按规模返回单轮执行超时（秒）。"""
    try:
        if not os.environ.get('AGENT_ROUND_TIMEOUT'):
            return _PERF_TIERS[perf_scale(sess_dir)][1]
    except Exception:
        pass
    return ROUND_TIMEOUT

# ★ 2026-11-06 新增：Code 调用单独限额
#
#   实测（86 工单批量）：
#     通过的 case 里 Code 用得最多的用了 49 次（792s 通过）
#     失败超时的 9 个里，NC20260819001887 用了 114 次、NC20260909000612 用了 100+ 次
#     Code 事件的内容都是 "import csv, collections" —— 在反复分析自己的产物
#
#   结论：Code 超过 N 次基本就是陷入「读产物→跑脚本→改→再读」循环，该杀。
#   ★ 2026-11-07 调整 60 → 100 → 200：
#     实测 NC20260819001887（1294 条 GT 命令的超大工单）：
#       单跑一次 Code 0 次通过（466s）
#       批量跑时 Code 101 次超限（1280s）
#     → 同一输入 agent 行为不可复现，Code 用量从 0 到 101 都出现过
#     200 是为了让这类超大工单能跑完（真死循环还有 ROUND_HARD_LIMIT 900s 兜底）
MAX_CODE_CALLS = int(os.environ.get('AGENT_MAX_CODE_CALLS', '200'))

# 产物清单
# ★ 2026-11-09 按「错了会怎样」分级（用户裁定）
#   REQUIRED：缺了配置不可用 → fatal
#   RECOMMENDED：只是说明性内容 → warn
REQUIRED_ARTIFACTS = ['mml.txt', 'params.csv']
RECOMMENDED_ARTIFACTS = ['配置分析.md']

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
def _build_wildcard_expansion(plan_txt, files_info, workdir):
    """扫规划表里的通配行，调 exp_attr_chain 展开成具体族名，返回提示文本。

    ★ 2026-11-12 机制保证（用户要求：不能只靠 prompt）
    问题：规划表写「SET APN*（UNC）」时，阶段2 不知道该配哪些族，
         加上「不要在规划之外增加命令族」的规则，保守只配主体族，
         25 个属性族全丢（实测 NC20260810002261）。

    做法：在拼阶段2 prompt 时就调 exp_attr_chain，把展开结果直接附上。
         agent 拿到的是「SET APNCHARGECTRL / SET APNIDLETIME / ...」的清单，
         不需要它自己理解通配符，也不需要它去调工具。

    识别通配：复用 guard/plan_wildcard.py 的 parse_plan_rows + 模式匹配。
    展开方式：exp_attr_chain(owner_family=<通配前缀>)。
    失败时静默返回空串（不阻塞流程，由 G31 判据兜 warn）。
    """
    try:
        import sys as _sys
        _gd = str(Path(__file__).parent / 'guard')
        if _gd not in _sys.path:
            _sys.path.insert(0, _gd)
        import plan_wildcard as _pw
    except Exception:
        return ''

    try:
        rows = _pw.parse_plan_rows(plan_txt)
    except Exception:
        return ''
    if not rows:
        return ''

    # 找出用了通配的行
    wild_rows = []
    for r in rows:
        if '跳过' in (r.get('status') or ''):
            continue
        cell = r.get('fam_cell') or ''
        if not cell:
            continue
        for pat, _why in _pw.WILDCARD_PATTERNS:
            if pat.search(cell):
                wild_rows.append(r)
                break
    if not wild_rows:
        return ''

    # 推断要展开的 owner family：取通配里的族名前缀
    import re as _re
    owners = []
    for r in wild_rows:
        cell = r['fam_cell']
        # ① 通配星号：SET APN*  → APN
        for m in _re.finditer(r'([A-Z][A-Z0-9_]{2,})\*', cell):
            owners.append(m.group(1))
        # ② xxx 占位：SET APNxxx → APN
        for m in _re.finditer(r'([A-Z][A-Z0-9_]{2,})xxx', cell, _re.I):
            owners.append(m.group(1).upper())
        # ③ 「等 N 个」写法：SET APNADDRESSATTR / SET APNIMSATTR 等 23 个
        #    做法：取所有具体族名的公共前缀（APNADDRESSATTR 和 APNIMSATTR → APN）
        #    但公共前缀可能是 Apn 全名，需限制长度 3-12 且是已知对象族
        if _re.search(r'等\s*\d*|\d+\s*个', cell):
            fams_in_cell = _re.findall(r'\b([A-Z][A-Z0-9_]{3,})\b', cell)
            # 过滤掉动词
            fams_in_cell = [f for f in fams_in_cell
                            if f not in ('ADD', 'MOD', 'SET', 'RMV')]
            if len(fams_in_cell) >= 2:
                # 求公共前缀
                pref = fams_in_cell[0]
                for f in fams_in_cell[1:]:
                    while pref and not f.startswith(pref):
                        pref = pref[:-1]
                # 公共前缀至少 3 字符，且不能等于某个具体族名
                if len(pref) >= 3 and pref not in fams_in_cell:
                    owners.append(pref)
    owners = list(dict.fromkeys(owners))     # 去重保序

    if not owners:
        return ''

    # 找 EXP 路径（优先 UNC，因为属性族多在 UNC 侧）
    exp_paths = []
    for f in (files_info or []):
        if f.get('is_exp'):
            pp = f.get('path') or ''
            parsed = f.get('parsed') or ''
            cand = parsed if parsed else pp
            if workdir and cand and not Path(cand).is_absolute():
                cand = str(Path(workdir) / cand)
            if cand and Path(cand).exists():
                exp_paths.append((f.get('me_type') or '', cand))
    # UNC 优先
    exp_paths.sort(key=lambda x: 0 if x[0].upper() == 'UNC' else 1)

    if not exp_paths:
        return ''

    # 调 exp_attr_chain 展开
    out_lines = []
    try:
        _mcp = str(Path(__file__).parent / 'mcp')
        if _mcp not in _sys.path:
            _sys.path.insert(0, _mcp)
        import mcp_exp
    except Exception:
        return ''

    for owner in owners:
        best = None
        for me, path in exp_paths:
            try:
                r = mcp_exp.tool_exp_attr_chain({
                    'path': path, 'owner_family': owner})
                if r.get('error'):
                    continue
                fams = [a['family'] for a in (r.get('attribute_families') or [])]
                if fams and (best is None or len(fams) > len(best[2])):
                    best = (me, path, fams)
            except Exception:
                continue
        if not best:
            continue
        _me, _path, fams = best
        out_lines.append(
            f'  · {owner} 的属性族（实测 {len(fams)} 个，来自 {_me} 侧 EXP）：')
        # 每行 4 个，便于阅读
        for k in range(0, len(fams), 4):
            out_lines.append('      ' + ', '.join(fams[k:k + 4]))

    if not out_lines:
        return ''

    head = [
        '【⚠ 程序已替你把规划表里的通配展开（不用你自己猜）】',
        '',
        '  规划表里有「SET APN*」这类通配写法。下面是从现网 EXP 实测得到的完整族清单，',
        '  这就是「*」代表的具体族 —— 这些族全部都要配，一个都不能少。',
        '  展开通配不算「增加规划外的族」，是执行规划的应有之义。',
        '',
    ]
    return '\n'.join(head + out_lines + [''])


def _build_plan_prompt(lines, session_id, intent_text, files_info,
                       product_hint, workdir):
    """阶段1（只做命令族规划）的专属 prompt。

    ★ 2026-11-11 整体重构
    旧版问题：阶段1 专属规则只有 46 行，却和 200 行阶段2 规则
      （params.csv / mml.txt / @src 标注 / 落盘 / 交付自检）混在同一个 prompt 里，
      agent 要在干扰信息中找重点，导致：
        · 同一单三次运行规划覆盖率 11 / 33 / 13 族（波动 3 倍）
        · EXP 工具用法分散在 4 个位置，中间夹着无关内容
        · 序号断裂（2 → ★★ → ★★ → ★ → 3），读起来迷路
     新结构（按重要性 + 首尾效应排列）：
        ① 本轮 4 步硬清单（开头，首因效应）
        ② 规划表格式（照抄模板）
        ③ EXP 分析怎么做（工具用法集中一节）
        ④ 三条处理原则（已存在 / 找不到 / 属性族）
        ⑤ 禁止事项
        ⑥ 交付前自检（结尾，近因效应）
    """
    # ★ 2026-11-11 版式 A/B 开关（环境变量 PROMPT_STYLE）
    #   box  = ════ 分节 ════   （默认）
    #   brk  = 【分节】
    #   纯文本里两种都能定位，靠实验数据决定，不靠主观判断。
    import os as _os
    _style = (_os.environ.get('PROMPT_STYLE') or 'box').lower()

    def _sec(title):
        if _style == 'brk':
            return f'【{title}】'
        return f'════ {title} ════'

    lines.append(_sec('★ 本轮任务：只做命令族规划，不写任何配置'))
    lines.append('')
    lines.append('  你的唯一产物是 analysis_code/命令族规划.md')
    lines.append('  禁止写 mml.txt / params.csv / 配置分析.md（写了会被拒绝，浪费轮次）')
    lines.append('  如果发现自己在写 MML 命令，立刻停手 —— 那是阶段2 的事')
    lines.append('')
    lines.append(_sec('本轮只做这 4 步'))
    lines.append('')
    lines.append('  第1步 摸清现网有什么')
    lines.append('    调一次 exp_stats（不带 family）→ 拿到全部族（对象族 + 属性族）')
    lines.append('    有多个 EXP（UDG + UNC）时，每个都调一次，或直接调 exp_cross_stats')
    lines.append('')
    lines.append('  第2步 意图里的每个业务对象，对应到族')
    lines.append('    对每个对象（APN / 用户模板 / 地址池 / 接口 ...）：')
    lines.append('      · 对象本身在哪个族？现网有没有？')
    lines.append('      · 它挂了哪些属性族？→ 调 exp_attr_chain(owner_family=该族)')
    lines.append('        这些属性族 全部 都要进规划表，除非写出明确的不配理由')
    lines.append('      · 该在哪个网元配？→ 调 exp_cross_stats 看分布')
    lines.append('')
    lines.append('  第3步 逐个族判断动作')
    lines.append('    调 exp_query 查现网实例：')
    lines.append('      · 现网无 → 新增（ADD）')
    lines.append('      · 现网有且参数一致 → 不配，写明「已存在且一致」')
    lines.append('      · 现网有但参数有差异 → 修改（MOD），列出差在哪')
    lines.append('      · 意图要求删除 → 删除（RMV）')
    lines.append('')
    lines.append('  第4步 逐对象核对 + 写规划表')
    lines.append('')
    lines.append('    ⚠⚠ 写规划表之前，必须先把意图里的业务对象列成清单，')
    lines.append('       然后对【每一个对象】回答下面三问。漏掉任何一个，规划表就不合格。')
    lines.append('')
    lines.append('    ┌─ 逐对象核对表（心里过一遍，也可以写进规划表的「对象清单」节）──')
    lines.append('    │ 对象：APN「sos」')
    lines.append('    │   ① 在哪个网元？ → 调 exp_cross_stats 看 APN 各侧条数')
    lines.append('    │      （实测反例：NC20260810002261 那次没查，')
    lines.append('    │        误判「APN 只在 UDG」→ 但 UNC 有 333 条、')
    lines.append('    │        APNCHARGECTRL/APNIDLETIME 也只在 UNC → 整链漏配 9 族）')
    lines.append('    │   ② 挂了哪些属性族？ → 调 exp_attr_chain(owner_family="APN")')
    lines.append('    │      （实测：APN 挂 23 个属性族）')
    lines.append('    │   ③ 这些属性族都进表了吗？ → 每个都要有一行，')
    lines.append('    │      现网没有实例的写「新增」，有的写「跳过 + 理由」')
    lines.append('    │')
    lines.append('    │ 对象：用户模板「up_sos」')
    lines.append('    │   ①②③ 同上（owner_family="USERPROFILE"）')
    lines.append('    │')
    lines.append('    │ 对象：地址池 / 池组 / 接口 / 过滤器 ... 逐个过')
    lines.append('    └────────────────────────────────────────────────────')
    lines.append('')
    lines.append('    ★ 判断某个族该在哪个网元配，必须用 exp_cross_stats 的数字说话，')
    lines.append('      不能凭「这个族名看起来像 UPF 的」推断。')
    lines.append('')
    lines.append('    然后 artifact_write 写 analysis_code/命令族规划.md（格式见下）')
    lines.append('')
    lines.append(_sec('规划表格式（必须完全照这个结构）'))
    lines.append('')
    lines.append('  # 命令族规划')
    lines.append('')
    lines.append('  ## 总览')
    lines.append('  | # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |')
    lines.append('  |---|---|---|---|---|---|---|---|---|')
    lines.append('  | 1 | 地址池清单 | 地址池 | 190 | 190 | MOD POOL | 修改 | 现网同池名190条 | 确认 |')
    lines.append('')
    lines.append('  ## 配套关系')
    lines.append('  | 主族 | 配套族 | 置信度 | 是否需要 | 说明 |')
    lines.append('  |---|---|---|---|---|')
    lines.append('')
    lines.append('  ## 不确定项')
    lines.append('  ## 待人工确认')
    lines.append('')
    lines.append('  ★ 状态列只能填：确认 / 待定 / 跳过')
    lines.append('')
    lines.append('  ⚠⚠ 「命令族」列必须是【具体的族名】，不许用通配或概括：')
    lines.append('     ✗ SET APN*（UNC）              ← 一行概括 25 个族')
    lines.append('     ✗ SET APNxxx 属性族 25 个       ← 数量概括')
    lines.append('     ✓ SET APNCHARGECTRL（UNC）      ← 一行一个具体族')
    lines.append('     ✓ SET APNIDLETIME（UNC）')
    lines.append('')
    lines.append('     为什么：阶段2 拿到的就是这个表。写通配它就要自己猜有哪些族，')
    lines.append('     猜错就漏配。实测 NC20260810002261 用「SET APN*」概括后，')
    lines.append('     阶段2 只配了 APN 本体，25 个属性族全部丢失。')
    lines.append('')
    lines.append('     展开方法：调 exp_attr_chain(owner_family="APN") 拿到族清单，')
    lines.append('     每个族写一行。20-40 行不嫌多 —— 这正是这张表的价值。')
    lines.append('  ★ 判断依据必须能回溯（写现网第几行、多少条、参数值是什么）')
    lines.append('')
    lines.append('  ⚠⚠ 无论有没有把握，都要写成规划表的【行】。')
    lines.append('     实测反例（NC20260810002261 的一次运行）：')
    lines.append('      agent 把 23 个族写成了「不确定项」的散文段落，')
    lines.append('      规划表只填了 36 行 → 阶段2 读不到那 23 个族 → 真的漏配。')
    lines.append('      正确做法：拿不准就把该行状态写「待定」，但【行必须在表里】。')
    lines.append('')
    lines.append(_sec('EXP 分析怎么做'))
    lines.append('')
    lines.append('  ★★★ 用 MCP 工具，不要自己写代码扫 EXP')
    lines.append('    实测反例（NC20260810002261）：agent 用 21 次 execute_code')
    lines.append('    自己写 Python 解析 EXP，每次 3.2s = 67s，且三次运行结果不一致')
    lines.append('    （规划覆盖 11 / 33 / 13 族）。工具已经把解析和缓存做好了。')
    lines.append('')
    lines.append('  ┌─ 四个工具，各管一件事 ─────────────────────────────')
    lines.append('  │')
    lines.append('  │ ① exp_stats(path)                    摸全景')
    lines.append('  │    一次拿全量族，返回两组：')
    lines.append('  │      object_families    有 ADD 的族（能独立创建）')
    lines.append('  │      attribute_families 只有 SET/MOD 的族（挂在 owner_family 上）')
    lines.append('  │    ⚠ 两组都要看。属性族同样是必须配的，')
    lines.append('  │      GT 里 32% 的族属于这一类，漏掉就是漏配。')
    lines.append('  │')
    lines.append('  │ ② exp_attr_chain(path, owner_family, owner_value?)  查属性族链')
    lines.append('  │    配某个对象时，它身上挂了哪些属性族？→ 一次回答')
    lines.append('  │    实测：APN 挂 23 个属性族（APNCHARGECTRL/APNIDLETIME/...）')
    lines.append('  │    给 owner_value 时还会标出哪些族现网已有该实例、给出样例命令')
    lines.append('  │    ⚠ 冷调 14s，热调 0ms；千万别自己写代码扫')
    lines.append('  │')
    lines.append('  │ ③ exp_cross_stats(paths=[udg, unc])  跨网元分布')
    lines.append('  │    这个族该在哪个网元配？→ 一次回答')
    lines.append('  │    实测：POOLGROUP     UDG 659 / UNC 0   → 只在 UDG')
    lines.append('  │          PCSCFGROUP    UDG 0   / UNC 5   → 只在 UNC')
    lines.append('  │          USERPROFILE   UDG 19  / UNC 82  → 两侧都要判断')
    lines.append('  │    ⚠ 冷调 1s，热调 0ms')
    lines.append('  │')
    lines.append('  │ ④ exp_query(path, ...)               查具体命令')
    lines.append('  │    三种模式，按需选：')
    lines.append('  │      owner 模式（最省事）：')
    lines.append('  │        exp_query(owner="APN", value="ims.wh")')
    lines.append('  │        → 一次返回该对象在【所有属性族】里的命令（实测 23 条）')
    lines.append('  │          代替原来逐族查 23 次')
    lines.append('  │      prefix 模式：exp_query(family_prefix="APN", param="APN", ...)')
    lines.append('  │      exact 模式： exp_query(family="URR", param="URRID", value="1040")')
    lines.append('  │    ⚠ limit 默认 200；结果多时加 family 过滤，别靠反复翻页')
    lines.append('  │')
    lines.append('  └────────────────────────────────────────────────────')
    lines.append('')
    lines.append('  ★ exp_siblings 也要用：查某族的配套族（会漏配 30-50%）')
    lines.append('     两种判据都要看：')
    lines.append('      ① 参数名指向：B 族有指向 A 族的参数名（POOLBINDGROUP 的 POOLNAME）')
    lines.append('      ② 同名前缀属性族：SET <A>xxx 与 ADD <A> 前缀相同且数量 1:1')
    lines.append('         例：配 APN 时除 ADD APN 外，还有 20-40 个 SET APNxxx')
    lines.append('')
    lines.append(_sec('三条处理原则（实测踩过的坑）'))
    lines.append('')
    lines.append('  ★★ 原则1：对象已存在，不等于不用配')
    lines.append('     必须逐参数比对现网值和意图要求的值：')
    lines.append('       · 完全一致 → 真不用配，在判断依据里写明')
    lines.append('       · 参数有差异 → 必须用 MOD，不能跳过')
    lines.append('     实测反例（NC20260803001614）：意图「新增 Host 约 14 个」，')
    lines.append('      agent 发现 14 个都已存在就全跳过，但其中 3 个域名要从')
    lines.append('      「*.edge.agora.io.*」改成三层「*.edge.agora.io」—— 这才是本次核心。')
    lines.append('')
    lines.append('  ★★ 原则2：找不到对应族，不许用名字相近的顶替')
    lines.append('     1) 先按业务对象的【特征值】搜（exp_query 不指定 family，只给 value）')
    lines.append('     2) 还找不到 → 规划表该行状态=「待定」，族名写「未找到（意图要的是 XXX）」')
    lines.append('     3) 同时写进「本网元无法配置的项」，说明可能要从其它网元配')
    lines.append('     ⚠ 绝对不要用名字相近的族替代 —— 会生成错误的配置')
    lines.append('')
    lines.append('  ★★ 原则3：大工单必须分片写，但每片都要进表')
    lines.append('     实测：GT 族数 >20 时一次性写覆盖率断崖下降（80% → 44%）')
    lines.append('     做法：按业务链路分片，每片 8-12 个族')
    lines.append('           第1片 artifact_write(mode="overwrite")')
    lines.append('           第2片起 artifact_write(mode="append")')
    lines.append('     每片写之前自问：这一片业务链里，意图提到的每个对象都对应到族了吗？')
    lines.append('')
    lines.append(_sec('禁止事项'))
    lines.append('')
    lines.append('  ✗ 不要写 mml.txt / params.csv / 配置分析.md')
    lines.append('  ✗ 不要用 execute_code / terminal 的 open() 写文件到 analysis_code/')
    lines.append('  ✗ 不要自己写代码扫 EXP（Python 解析、grep 统计都算）')
    lines.append('  ✗ 不要把族写成散文段落 —— 必须是规划表的行')
    lines.append('')
    lines.append(_sec('交付前自检（写完规划表后逐条核对）'))
    lines.append('')
    lines.append('  □ 意图里每个【】分组，规划表里都有对应行吗？')
    lines.append('  □ 意图里每个业务对象，都调过 exp_cross_stats 确认网元归属了吗？')
    lines.append('  □ 意图点名的每个对象，都调过 exp_attr_chain 看它的属性族了吗？')
    lines.append('  □ 属性族（exp_attr_chain 返回的）都进表了吗？没进的写了理由吗？')
    lines.append('  □ 每个族的「判断依据」都能回溯到现网（行号 / 条数 / 参数值）吗？')
    lines.append('  □ 多网元场景，每个族都确认过该在哪侧配吗？')
    lines.append('  □ 拿不准的族是写在【表的行里】且状态=待定，还是写成了散文？')
    lines.append('     → 必须是前者')
    lines.append('')
    return lines


def build_prompt(session_id, intent_text, files_info, product_hint='', workdir=None,
                 stage='fill'):
    """构造首轮 prompt。

    stage='plan'  只做命令族规划（产物只有 命令族规划.md + 方案澄清.json）
    stage='fill'  按已有规划填充配置
    """
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

    # ★ 2026-11-09 移除操作清单
    #   原因：意图已改为「按业务链路分组 + 明确动词」的写法（如【计费链】- 新增 URR，2 个），
    #        再套一层 verb 解析会重复且可能冲突（意图写「调整」被解析成 ADD_OR_MOD）。
    #        旧机制是为「意图只有业务名词」的场景设计的（如【新增/修改】- 地址池），
    #        新意图不再有这个问题。

    # ★ 2026-11-11 两阶段分离重构：
    #   阶段1 走专属 prompt（_build_plan_prompt），不再和阶段2 规则混在一起。
    #   旧版问题：阶段1 专属只有 46 行，共用段却包含 200 行阶段2 规则，
    #   agent 在干扰里找重点 → 同一单三次运行覆盖 11/33/13 族。
    if stage == 'plan':
        return '\n'.join(_build_plan_prompt(
            lines, session_id, intent_text, files_info, product_hint, workdir))

    elif stage == 'fill':
        # 阶段2：把规划表全文注入（从文件读，不截断）
        _plan_txt = ''
        if workdir:
            _pf = Path(workdir) / 'analysis_code' / '命令族规划.md'
            if _pf.exists():
                _plan_txt = _pf.read_text(encoding='utf-8', errors='replace')
        if _plan_txt:
            lines.append('【★ 已确认的命令族规划（必须严格按此执行）】')
            lines.append(_plan_txt[:12000])
            lines.append('')
            # ★ 2026-11-12 机制保证：程序替 agent 展开通配，不靠它自己理解
            #   实测：规划表写「SET APN*」时，阶段2 只配 APN 本体，
            #        25 个属性族全丢（NC20260810002261）。
            #   prompt 里写了「必须自己展开」但 agent 不一定执行，
            #   所以在这里直接把展开结果附上。
            _exp_hint = _build_wildcard_expansion(_plan_txt, files_info, workdir)
            if _exp_hint:
                lines.append(_exp_hint)
                lines.append('')
            lines.append('  ★ 执行规则：')
            lines.append('    · 状态=确认 或 ★人工调整 的，必须配')
            lines.append('    · 状态=跳过的，不配')
            lines.append('    · 状态=待定的，写进方案澄清，不要擅自决定')
            lines.append('    · 对象数量严格按规划表，不要多配也不要少配')
            lines.append('    · 不要在规划之外增加命令族；认为规划有问题就写澄清，不要自己改')
            lines.append('')
            lines.append('  ★★ 规划表里出现通配或数量概括时，必须自己展开（2026-11-11）')
            lines.append('     例：规划表写「SET APN*（UNC）」或「SET APNxxx 属性族 25 个」')
            lines.append('     → 这不是让你只配 APN 本体！')
            lines.append('     → 调 exp_attr_chain(owner_family="APN", owner_value="sos")')
            lines.append('       拿到全部属性族（实测 20-40 个），逐个配')
            lines.append('     → 展开通配【不算】「增加规划外的族」，这是执行规划的应有之义')
            lines.append('')
            lines.append('     判据：如果规划表某行的命令族列含 * 或「N 个」字样，')
            lines.append('           该行必须展开成对应的具体族才允许进入下一步。')
            lines.append('')
        else:
            lines.append('⚠ 警告：找不到 命令族规划.md，请按意图自行判断（不推荐）')
            lines.append('')

    # ★ 2026-11-09 新增：数据清单用法说明
    #   客户上传的业务数据表（IP 列表 / 名称清单 / 规划表），
    #   列名是业务说法（如「隧道名称」「目的地址」），不是 MML 参数名。
    _has_dataset = any(
        f.get('is_dataset') or
        (f.get('name') or '').endswith(('数据清单.md', '数据清单.xlsx', '数据清单.csv', '数据清单.csv'))
        for f in (files_info or []))
    if _has_dataset:
        lines.append('【数据清单】')
        lines.append('  客户提供的业务数据表（IP 列表、名称清单、规划表等）。')
        lines.append('  ★ 列名是业务说法（如「隧道名称」「目的地址」「池类型」），')
        lines.append('    不是 MML 参数名，需要你自己判断对应哪个命令族的哪个参数。')
        lines.append('  ★ 用法：')
        lines.append('    1. 先识别每一列对应哪类业务对象、哪个参数')
        lines.append('    2. 逐行填充到 params.csv（一行数据 = 一个对象实例）')
        lines.append('    3. 数据清单没给、但配置必需的值：按现网规律或文档补，')
        lines.append('       补不了的填【待填写】，不要编造')
        lines.append('  ★ 数据清单里有多少行，产物就要有多少个对应对象——不要只配样本。')
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
    lines.append('  exp_detect / exp_stats / exp_query / exp_refs / exp_baseline / exp_siblings   EXP 分析')
    lines.append('  kb_search_feature / kb_search_command / kb_get_naming         知识检索')
    lines.append('  file_list / file_read / file_parse                            文件读写')
    lines.append('  artifact_write / guard_check / clarify                        产物与校验')
    lines.append('')

    lines.append('【建议流程】（你自己判断是否需要，不必机械执行）')
    lines.append('  1. file_list 看有什么资料；有 EXP 就 exp_detect 确认')
    lines.append('  2. ⚠ 摸现网规律：调【一次】exp_stats 不带 family 参数，一次拿全量')
    lines.append('     然后对【每个要新建的族】调 exp_siblings 查配套族，一起配。')
    lines.append('     exp_siblings 的判据有两种，都要看：')
    lines.append('     ① 参数名指向：B 族有指向 A 族的参数名（如 POOLBINDGROUP 的 POOLNAME）')
    lines.append('     ② 同名前缀属性族：SET <A>xxx 与 ADD <A> 前缀相同且数量 1:1，')
    lines.append('        这是同一对象的属性命令，必须一起配。')
    lines.append('        例：配 APN 时除 ADD APN 外，还有 31 个 SET APNxxx 属性命令。')
    lines.append('     只配配套链里的一个会被判漏配（G25 会报出来）。')
    lines.append('')
    lines.append('  ★★ 对象已存在时的处理原则（重要）')
    lines.append('     现象：意图要求配置某个对象，但 exp_query 查到它已经存在。')
    lines.append('     错误做法：直接跳过，认为「已存在就不用配」。')
    lines.append('     正确做法：必须逐参数比对现网值和意图要求的值：')
    lines.append('       · 完全一致 → 确实不用配，在配置分析里写明「已存在且一致，跳过」')
    lines.append('       · 参数有差异 → 必须用 MOD 改成意图要求的值，不能跳过')
    lines.append('     实测反例（NC20260803001614）：')
    lines.append('       意图「新增 Host 约 14 个」，agent 发现 14 个都已存在就全部跳过，')
    lines.append('       但其中 3 个的域名要从「*.edge.agora.io.*」改成三层「*.edge.agora.io」')
    lines.append('       —— 这才是本次变更的核心，跳过等于没做。')
    lines.append('')
    lines.append('  ★★ 找不到对应命令族时的处理原则（重要）')
    lines.append('     现象：意图点名的业务对象，在本网元 EXP 的族清单里查不到。')
    lines.append('     错误做法：挑一个名字相近的族顶替（例：要「TAI 区域」却选了「TAI 组」）。')
    lines.append('     正确做法：')
    lines.append('       1) 先用 exp_query 按业务对象的**特征值**搜（不只是族名），')
    lines.append('          看现网有没有承载这类对象的族（按参数名、按取值形态搜）；')
    lines.append('       2) 仍然找不到，就在规划表该行标状态=「待确认」，')
    lines.append('          命令族列写「未找到（意图要的是 XXX 业务对象）」，')
    lines.append('          判断依据写清楚：查了哪些族、按什么搜的、为什么判断本网元没有；')
    lines.append('       3) 同时在「本网元无法配置的项」小节列出来，')
    lines.append('          说明「该对象可能需要从其它网元配置，需确认目标网元」。')
    lines.append('     ⚠ 绝对不要用名字相近的族替代 —— 那会生成一条错误的配置。')
    lines.append('')
    lines.append('  ★ 强制要求（不查会被 G25 判 warn）：')
    lines.append('    产物里出现的每个 ADD 族，都要先调 exp_siblings 查一次。')
    lines.append('    配套族（confidence=high）如果确实不需要配，')
    lines.append('    必须写进 clarify，说明「XXX 族的配套族 YYY 不配的理由」。')
    lines.append('    实测：不查会导致漏配 30-50% 的族')
    lines.append('     实测对比（86 工单）：逐个族调 exp_query 查明细，')
    lines.append('     平均要 15-38 次 EXP 调用、每次 6.5 秒 = 100-250 秒；')
    lines.append('     一次不带参 exp_stats 返回全部 101 个族的规律，只需 1 次调用。')
    lines.append('     只有确实需要看某族全部实例明细时，才用 exp_query 定向查。')
    lines.append('')
    lines.append('  ★★★ exp_stats 返回两类族，两类都要看（2026-11-11 新增）')
    lines.append('     object_families    有 ADD 的族（能独立创建，identity_param 是主键）')
    lines.append('     attribute_families 只有 SET/MOD/RMV 的族（不能独立创建，')
    lines.append('                        挂在 owner_family 上）')
    lines.append('')
    lines.append('     ⚠ attribute_families 最容易被忽略，但它同样是「必须配的」：')
    lines.append('       GT 里大量 SET 只落在属性族上，漏掉它们就是漏配。')
    lines.append('       典型：APNCHARGECTRL(owner=APN) / APNIDLETIME(owner=APN) /')
    lines.append('             IFIPV6ENABLE(owner=INTERFACE) / URRGRPBINDING(owner=USERPROFILE)')
    lines.append('')
    lines.append('     规划时的强制做法：')
    lines.append('       1) 对意图里出现的每个对象（APN / 接口 / 用户模板 ...），')
    lines.append('          在 attribute_families 里筛 owner_family == 该族，')
    lines.append('          这些属性族都要进规划表，除非明确写出不配的理由。')
    lines.append('       2) 对每个族看 references（引用关联），确认上级对象先创建。')
    lines.append('          例 FLTBINDFLOWF 的 FLOWFILTERNAME/FILTERNAME 指向')
    lines.append('          FLOWFILTER/FILTER → 必须先有这两个对象。')
    lines.append('')
    lines.append('  ★★ 两个专用工具，替代「自己写代码扫 EXP」（2026-11-11 新增）')
    lines.append('     exp_attr_chain(path, owner_family, owner_value?)')
    lines.append('       → 查「配某个对象时还要配哪些属性族」。')
    lines.append('         意图说「APN sos 按现网 ims.wh 存量配齐」时，')
    lines.append('         调它一次就能拿到 APN 的完整属性族链（实测 23-44 个族），')
    lines.append('         并标出哪些族现网已有 ims.wh 实例、给出可直接照抄的样例命令。')
    lines.append('         ⚠ 不要自己写代码扫 EXP 找属性族 —— 冷调 14s，热调 0ms')
    lines.append('')
    lines.append('     exp_cross_stats(paths=[...])')
    lines.append('       → 对比同一个族在多个网元 EXP 里的分布，判断「该在哪配」。')
    lines.append('         实测：POOLGROUP 在 UDG 659 条、UNC 0 条 → 只在 UDG 配；')
    lines.append('               PCSCFGROUP 在 UDG 0 条、UNC 5 条 → 只在 UNC 配；')
    lines.append('               USERPROFILE 双侧都有（UDG 19 / UNC 82）→ 需分别判断')
    lines.append('         ⚠ 不要自己写代码统计跨网元分布 —— 冷调 1s，热调 0ms')
    lines.append('')
    lines.append('  ★ 查什么用哪个工具')
    lines.append('  3. kb_search_feature 查特性文档；kb_search_command 查命令参数')
    lines.append('  4. 推理出配置方案')
    lines.append('  5. artifact_write 写产物')
    lines.append('  6. guard_check 自检；有 fatal 自己修完再检')
    lines.append('')

    if stage == 'plan':
        lines.append('  ★★★ 大工单必须分片规划（实测：GT 族数 > 20 时覆盖率断崖下降）')
        lines.append('     数据：')
        lines.append('       GT 0-9 族    → 规划覆盖率 80.0%')
        lines.append('       GT 10-19 族  → 规划覆盖率 74.6%')
        lines.append('       GT 20-29 族  → 规划覆盖率 51.5%   ← 断崖')
        lines.append('       GT 40-59 族  → 规划覆盖率 44.3%')
        lines.append('     说明：一次要列几十个族，模型会漏。必须分片。')
        lines.append('    ')
        lines.append('     分片做法：')
        lines.append('       1) 先按业务链路把意图里的条目分成几片，每片不超过 8-12 个族：')
        lines.append('          典型分片：APN与移动性 / 流量识别 / 计费链 / 地址池与承载 /')
        lines.append('                    紧急呼叫 / 刷新与开关 / 许可与告警')
        lines.append('       2) 每次只处理一片，写完 append 到规划表：')
        lines.append('          第1片 → artifact_write(..., mode="overwrite")')
        lines.append('          第2片起 → artifact_write(..., mode="append")')
        lines.append('       3) 每片写之前，先自问：')
        lines.append('          「这一片业务链里，意图提到的每个对象都对应到族了吗？」')
        lines.append('       4) 全部写完后，检查意图里的每个【】分组都有对应行；')
        lines.append('          没有的，说明漏了，回去补。')
        lines.append('    ')
        lines.append('     ⚠ 不要先想好全部再一次性写 —— 那正是覆盖率掉到 44% 的原因。')
        lines.append('')
        lines.append('【产物要求】阶段1（规划）只写这一个文件：')
        lines.append('  1. 命令族规划.md  按上面的格式写命令族规划表')
        lines.append('  2. 方案澄清.json  （可选）规划阶段拿不准的写这里')
        lines.append('')
        lines.append('  ★ 不要写 mml.txt / params.csv / 配置分析.md')
        lines.append('')
        return '\n'.join(lines)

    lines.append('【产物要求】写到 analysis_code/，一共这几个文件：')
    lines.append('  1. params.csv     参数表（★ 这是你的核心产物，写全）')
    lines.append('       列：序号,组,网元,动词,命令族,参数,值,来源,说明')
    lines.append('  2. 配置分析.md    用了哪些依据、为什么选这些族、命名来源、注意事项')
    lines.append('  3. 方案澄清.json  （可选）只放方案级问题，没有就给 []')
    lines.append('')
    lines.append('  ★★★ 不要写 mml.txt —— 它由代码从 params.csv 自动生成')
    lines.append('    实测反例（NC20260811002706，GT 1164 条）：')
    lines.append('      agent 手写 mml.txt 只写出 21 条就停了（被输出长度截断），')
    lines.append('      而它写的 params.csv 有 826 组（数据是齐全的）。')
    lines.append('      现在改成：你只负责 params.csv，代码会把它 1:1 转成 MML 命令，')
    lines.append('      有多少组就生成多少条，不会被截断。')
    lines.append('    ⚠ 写 mml.txt 是浪费轮次，而且会和 params.csv 不一致。')
    lines.append('    ⚠ 唯一例外：如果你需要特殊的 Phase 分组注释，写在 params.csv 的')
    lines.append('      「说明」列里，代码会带出来。')
    lines.append('')
    lines.append('  【params.csv 写法（重要）】')
    lines.append('    一行一个参数。同一个「组」的多行 = 一条 MML 命令。')
    lines.append('    组名格式：<命令族>#<序号>，如 HOST#1 / FILTER#1 / URR#2')
    lines.append('')
    lines.append('    ★★ 动词列必须与规划表的「动作」列一致')
    lines.append('      MML 动词不止 ADD/MOD/SET/RMV，会改数据/状态的都要支持：')
    lines.append('        配置类：ADD 新增 / MOD 修改现网已有对象 / RMV 删除 / SET 设置')
    lines.append('        操作类：ACT 激活 / DEA 去激活 / RTR 复位 / RST 重置')
    lines.append('                STR 启动 / STP 停止 / CLR 清除 / OPR 操作')
    lines.append('                SYN 同步 / LOD 加载 / RBL 重载 / UPD 更新')
    lines.append('                LCK 锁定 / ULK 解锁')
    lines.append('        （查询类 LST/DSP/TST/EXP 是只读命令，不要写进配置产物）')
    lines.append('      判断依据：规划表的「动作」列写了什么，动词就填什么。')
    lines.append('      实测反例 NC20260819001887：规划表写「MOD POOL 修改」')
    lines.append('        （190 个现网池要改 REDUNDFUNC 开关），但 params.csv 没记动词，')
    lines.append('        代码按「POOL 现网只有 ADD」推断成 ADD POOL ×190')
    lines.append('        → 会尝试新建已存在的 190 个池，全部失败。')
    lines.append('      留空则按现网规则推断（不推荐，容易和规划矛盾）。')
    lines.append('')
    lines.append('    例：')
    lines.append('      序号,组,网元,动词,命令族,参数,值,来源,说明')
    lines.append('      1,HOST#1,UDG,ADD,HOST,HOSTNAME,hncatv_00_h_001,plan:域名规划#1,')
    lines.append('      2,HOST#1,UDG,ADD,HOST,DOMAINVALUE,video.hncatv.com,plan:域名规划#1,')
    lines.append('      3,HOST#1,UDG,ADD,HOST,PRIORITY,10600,exp:derive L1103,')
    lines.append('      4,FILTER#1,UDG,ADD,FILTER,FILTERNAME,hncatv_00_f_h_001,exp:derive,')
    lines.append('      5,FILTER#1,UDG,ADD,FILTER,SVRIPMODE,HOSTNAME,doc:F352,')
    lines.append('      6,FILTER#1,UDG,ADD,FILTER,HOSTNAME,@HOST#1.HOSTNAME,infer 引用HOST#1,')
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
    lines.append('    序号,组,网元,动词,命令族,参数,值,来源,说明')
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
    lines.append('')
    lines.append('  ★★ 必须主动提示「意图里的族在本网元配不了」的情况（2026-11-10 用户要求）')
    lines.append('     实测背景：87 个工单里 26 个跨 UDG+UNC 两个网元，')
    lines.append('              但工单材料只提供了 UDG 侧的 EXP 快照。')
    lines.append('              UNC 侧的族（EMGCFG / USRPROFGROUP / DBPARAS / PNFDNN 等）')
    lines.append('              在本网元 EXP 里查不到，agent 配不出来；')
    lines.append('              用户不知道为什么少了这些族。')
    lines.append('     做法：如果意图里点名要做某项，但你判断「对应的命令族在本网元 EXP 里不存在」')
    lines.append('           （exp_query 查 0 条、族清单里没有），')
    lines.append('           必须在 配置分析.md 里单开一节说明：')
    lines.append('             ## 本网元无法配置的项')
    lines.append('             | 意图项 | 对应命令族 | 判断依据 | 建议 |')
    lines.append('             | 删除BSF实例绑定 | BSFIPRANGEBIND | exp_query 查 0 条，81 族清单无此族 | 需在 BSF 网元操作 |')
    lines.append('           同时在 方案澄清.json 里提一条（如果影响方案完整性）：')
    lines.append('             {"id":"cross_ne","question":"XX 项属于按个网元，本网元配不了，是否已另行处理？"')
    lines.append('              ,"why":"...","default_choice":"已跳过","options":[...]}')
    lines.append('     ⚠ 不要因为配不了就默默跳过，也不要在 mml 里硬凑一个不存在的族。')
    lines.append('  格式：[{"id":"q1","question":"...","why":"...","default_choice":"当前采用的默认",')
    lines.append('         "options":[{"label":"...","reply":"...","is_default":true}]}]')
    lines.append('  options 每个 2-3 个，必须有一个 is_default=true 对应你已采用的做法。')
    lines.append('  reply 写成用户点了之后会发的原话（第一人称，不依赖上下文）。')
    lines.append('  why 里写清楚：为什么这么选、另一个选项的代价是什么。')
    lines.append('')

    lines.append('【hard 要求】')
    lines.append('  · 命名：有 EXP 沿用现网统计规律（不要照抄文档示例）；无 EXP 按文档示例或用户规划')
    lines.append('  · 不要编造没有依据的数值')
    lines.append('  · ★ EXP 里的 *** 是脱敏值，绝对不要照抄到产物里！')
    lines.append('    正确做法：用 exp_stats / exp_query 统计同族其他实例的取值，')
    lines.append('    取多数值；或查文档取默认值。例：TOKENFUNCFLAG 现网 101 条全是 DISABLE，')
    lines.append('    如果看到某行是 ***，说明那行被脱敏了，要按 DISABLE 写。')
    lines.append('  · 区分「现网已有」和「本次新增」：现网已有的对象不要重复创建')
    lines.append('  · ★ 按意图给的对象数量配全：意图说「约 190 个地址池」就配 190 个，')
    lines.append('    说「约 184 个 GRE 隧道」就配 184 个，不要只配几个样本。')
    lines.append('    数量多时用 params.csv 分块写（150-200 行/块），不要因为量大就省略。')
    lines.append('  · 写完产物后调一次 guard_check；有 fatal 自己修完再调，直到通过')
    lines.append('  · 完成后简述：做了什么、哪些需要人工确认')
    lines.append('')
    lines.append('【⚠ 效率硬要求（违反会导致任务失败）】')
    # ★ 2026-11-12 修：原规则「3 次后一律收尾」导致 agent 遇到真错也放弃
    #   实测 NC20260828000360：agent 第 3 次 guard_check 后说
    #     「剩余告警都来自校验规则本身，不是配置错误...按规则收尾」
    #   但那些 fatal 是真错（族名写错、动词错误），本该能改对。
    #   新规则：区分「机械错误」和「规则争议」
    lines.append('  · guard_check 调多少次都可以，只要每轮报的错在变/在减少。')
    lines.append('    但【机械错误必须在收尾前改完】：')
    lines.append('    - G32 族名不存在/动词错误：把族名或动词改成 guard 提示的那个，数值不动')
    lines.append('    - G34 族名写错：把族名改成 guard 提示的 should_be，参数和值都不动')
    lines.append('    - G35 引用不存在的组：按提示三选一（改引用/补组/删命令）')
    lines.append('    - G19 虚假依据：改行号，或把 @src=exp:Lxxx 改成 @src=infer 说明规则')
    lines.append('    这几类都是「照提示直接改」就能过的，不要以「规则有争议」为由跳过。')
    lines.append('  · 只有【方案选择类】的问题（跨网元配置、意图歧义、配套族要不要配）')
    lines.append('    才写进 方案澄清.json 交人判断，不要硬改。')
    lines.append('  · 不要用 execute_code / terminal 写脚本去批量修改 mml.txt。')
    lines.append('    改产物只用 artifact_write（整文件覆盖）。')
    lines.append('  · ⚠⚠ 禁止用 execute_code 分析自己的产物！')
    lines.append('    实测反例（NC20260819001887）：agent 反复跑')
    lines.append('      import csv, collections / 读 params.csv 统计 / 读 mml.txt 比对')
    lines.append('    共调用 114 次，耗时 22 分钟被强杀，产物质量没有提升。')
    lines.append('    正确做法：')
    lines.append('      - 要改产物 → 直接 artifact_write 重写整份')
    lines.append('      - 要核对 → 用 guard_check（它会给结构化的检查结果）')
    lines.append('      - 要统计 → 不需要，guard_check 已经报了命令数和族数')
    lines.append('  · ⚠ 禁止往会话目录写临时文件（c_*.txt / final.csv / FINAL.txt 等）')
    lines.append('    这些文件不会被收集，只会浪费轮次。')
    lines.append('')
    lines.append('  · ⚠⚠⚠ 查 EXP 只能用 exp_* 工具，禁止用 execute_code 解析 EXP 文件！')
    lines.append('    实测反例（NC20260819001887，42MB EXP）：')
    lines.append('      agent 反复 execute_code: "import json" / "import csv, collections"')
    lines.append('      去自己解析 45MB 的 EXP 文本 → 55 次 Code 调用、304 秒、一个产物没写出')
    lines.append('    正确工具：')
    lines.append('      - 找某族有哪些实例     → exp_query(family="FILTER")')
    lines.append('      - 统计命名规律/取值    → exp_stats(family="HOST")')
    lines.append('      - 查引用关系           → exp_refs(...)')
    lines.append('      - 摸现网基线           → exp_baseline(...)')
    lines.append('      - 查配套族/业务链      → exp_siblings(...)  ★ 建新对象前必查')
    lines.append('    这些工具已内置索引，比你自己 read+parse 快 100 倍。')
    lines.append('    想清楚要改成什么，一次改完。')
    lines.append('  · 单轮总耗时控制在 10 分钟内。超过说明陷入循环了，立刻收尾。')
    lines.append('')
    lines.append('【⚠⚠ 产物落盘硬要求（最容易出错的地方）】')
    lines.append('  · 4 个产物必须用 artifact_write 写到 analysis_code/，')
    lines.append('    名字严格是：mml.txt / params.csv / 配置分析.md / 方案澄清.json')
    lines.append('  · 禁止往 /tmp/ 写 mml2.txt、params2.csv 这种临时文件当"草稿"再指望转换。')
    lines.append('    实测过这样做的结果：任务结束只写出 mml.txt，params.csv 全丢。')
    lines.append('')
    lines.append('  ★★★ 大文件必须分块写（params.csv 和 mml.txt 都一样，最容易出错）')
    lines.append('    实测：本模型单次可输出约 5900 token / 200 行 CSV / 12000 字符，')
    lines.append('    所以每块写 150-200 行最合适 —— 写太少会浪费轮次。')
    lines.append('')
    lines.append('    【params.csv 分块】')
    lines.append('      1) artifact_write(filename="params.csv", content="表头+前150行", mode="overwrite")')
    lines.append('      2) artifact_write(filename="params.csv", content="第151-300行", mode="append")')
    lines.append('      3) 重复 append 直到写完（每块 150-200 行，不要更小）')
    lines.append('      4) artifact_write(filename="params.csv", content="", mode="finalize")')
    lines.append('')
    lines.append('    （mml.txt 不需要你写 —— 代码会从 params.csv 生成）')
    lines.append('')
    lines.append('    ⚠ 不要一次写超过 200 行（会超模型输出上限被截断）')
    lines.append('    ⚠ 也不要一次只写 30 行（浪费轮次，实测一份 600 行 CSV 会被拆成 20 次）')
    lines.append('')
    lines.append('  ★★ 交付前自检（必做，不做会漏配）')
    lines.append('    1. params.csv 里有多少个不同的「组」，等于会生成多少条 MML 命令')
    lines.append('       对照意图里说的对象数量：意图说「约 190 个地址池」，')
    lines.append('       就应该有 190 个 POOL#N 组。数量差太多说明漏配了。')
    lines.append('    2. 每个「组」的参数是否齐全（主键 + 必要属性）')
    lines.append('    3. 3 个产物文件名必须齐全：')
    lines.append('       params.csv / 配置分析.md / 方案澄清.json')
    lines.append('       ★ 配置分析.md 经常被忘，写完 csv 后立刻补上（哪怕很简短）')
    lines.append('')
    lines.append('  · 需要迭代修改时：重新 overwrite 同名文件，不要另起文件名。')
    return '\n'.join(lines)


def _explain_guard(guard_result, has_artifacts=True):
    """把 guard 结果翻成人话（失败时降级为原始结构）。"""
    try:
        import importlib
        import sys as _sys
        _here = str(Path(__file__).resolve().parent / 'guard')
        if _here not in _sys.path:
            _sys.path.insert(0, _here)
        _ex = importlib.import_module('explain')
        gr = dict(guard_result or {})
        gr['has_artifacts'] = has_artifacts
        return _ex.explain_guard(gr)
    except Exception as e:
        return {
            'verdict': (guard_result or {}).get('verdict'),
            'summary': f'{len((guard_result or {}).get("fatal") or [])} 个问题（解释生成失败: {e}）',
            'items': [],
            'n_fatal': len((guard_result or {}).get('fatal') or []),
            'n_warn': len((guard_result or {}).get('warnings') or []),
            'has_artifacts': has_artifacts,
        }


def build_feedback(guard_result):
    """把 guard 的 fatal 转成给 agent 的修正指令。

    ★ 2026-11-06：改用 explain.py 生成结构化说明，
      每条问题都带「现象 / 为什么不对 / 怎么改」，
      避免 agent 只看到「G21 主键重复」这种代码看不懂在改什么。
    """
    try:
        import importlib
        import sys as _sys
        _here = str(Path(__file__).resolve().parent / 'guard')
        if _here not in _sys.path:
            _sys.path.insert(0, _here)
        _ex = importlib.import_module('explain')
        return _ex.to_agent_instruction(guard_result)
    except Exception:
        # 兜底：用旧格式
        fatal = guard_result.get('fatal') or []
        warnings = guard_result.get('warnings') or []
        lines = ['【上一轮产物未通过代码校验，请修正】', '']
        if fatal:
            lines.append('发现以下必须修正的问题：')
            for f in fatal[:10]:
                if isinstance(f, dict):
                    lines.append(f"  · [{f.get('code','')}] {f.get('message') or f.get('msg') or ''}")
                else:
                    lines.append(f'  · {f}')
            lines.append('')
        if warnings:
            lines.append('另有以下告警（建议一并处理）：')
            for w in warnings[:5]:
                lines.append(f'  · {w}')
            lines.append('')
        lines.append('【修正要求】')
        lines.append('  1. 上一轮已有的正确命令全部保留，只在需要的地方增/改')
        lines.append('  2. 不能为了消除某个告警就删掉整族命令')
        lines.append('  3. 修完后用 artifact_write 重新写对应的产物文件')
        lines.append('  4. 再调一次 guard_check 确认')
        return '\n'.join(lines)


# ═══════════════════════════════════════════════════════════
# 调 hermes（同步 readline + 实时事件）
# ═══════════════════════════════════════════════════════════
def call_hermes(prompt, workdir, resume_sid=None, events_fp=None,
                timeout=ROUND_TIMEOUT, stage='fill'):
    """调 hermes 跑一轮。

    Returns (ok, out_text, elapsed, session_id, error)
    """
    env = dict(os.environ)
    env['HERMES_SKIP_NODE_BOOTSTRAP'] = '1'
    # ★ 2026-11-09 两阶段：把 stage 传给 MCP 工具
    #   env 方式不可靠：MCP server 由 hermes 按 config.yaml 启动，
    #   不继承这里的环境变量（config 里 mcp_servers.io 无 env 字段）。
    #   → 真正生效的是 <session>/.agent/stage 文件（在 run_agent 开头写）。
    try:
        env['AGENT_STAGE'] = str(stage or 'fill')
    except Exception:
        pass
    # ★ 2026-11-14 按规模自适应 STALL 阈值和执行超时
    _stall_sec = stall_seconds_for(workdir)
    # 调用方没显式给 timeout（仍是默认 ROUND_TIMEOUT）时，按规模覆盖
    if timeout == ROUND_TIMEOUT:
        timeout = round_timeout_for(workdir)
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
    # ★ 2026-11-14 STALL 判定状态（Popen 不能挂自定义属性，用局部变量）
    _stall_base = None          # STALL 计时基准（有进展就前移）
    _last_ev_size = -1          # 上次看到的 events 字节数
    _tool_cnt = {'total': 0, 'guard': 0, 'code': 0, 'seq': [],
                 'guard_fatals': [],       # 旧：正则抓的文本（保留兼容）
                 'guard_fatal_sets': []}   # 新：每次 guard 的 fatal 内容集合
    _same_count = 0        # 连续「fatal 集合完全不变」的次数

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
            # ★★ 2026-11-08 修复：STALL 检测提到工具行判断之前
            #   原 bug：检测代码放在 `if not _is_tool_line: continue` 之后，
            #   agent 如果长时间只「思考」不产生工具行（例如反复纠结
            #   「业务名词对应哪个命令族」），STALL 永远不触发。
            #   实测 NC20260820000552 跑了 34 分钟、产物 0 个仍未被杀。
            #   现在每读到一行就检查一次时间，不依赖工具行。
            _sb = _stall_base or t0
            if time.time() - _sb > _stall_sec:
                # ★★ 2026-11-14 重写 STALL 判据（原版只看「无产物」，漏了「有产物但不动」）
                #
                #   实测 NC20260819001887（v22 重跑）：
                #     run2 第 2 轮修 G34 报的族名错，agent 收到修正指令后 9 分钟无动作
                #     events 停在 198 行（10:54），但 analysis_code 已有 5 个文件
                #     → 原判据 `if _n_art == 0` 不成立 → 完全跳过 STALL 检查 → 卡死没人管
                #
                #   新判据：不管有没有产物，只要 events 不增长就算卡住
                #     · events 在增长 → agent 在工作 → 前移 STALL 基准
                #     · events 不增长 → 真卡住 → 杀
                #
                #   为什么用 events 而不是产物文件：
                #     产物可能最后一次性写（agent 先探索后落盘），
                #     events 是每个工具调用都追加，更能反映「有没有在动」
                _adir = Path(workdir) / 'analysis_code'
                _n_art = 0
                if _adir.is_dir():
                    _n_art = len([p for p in _adir.iterdir()
                                  if p.is_file() and not p.name.startswith('.')])
                _ev_p = Path(workdir).parent / '.agent' / 'events.jsonl'
                _ev_now = 0
                try:
                    if _ev_p.exists():
                        _ev_now = _ev_p.stat().st_size
                except Exception:
                    pass
                _progressing = (_ev_now > _last_ev_size)
                _last_ev_size = _ev_now
                if _progressing:
                    # 有进展：把 STALL 基准往后推（不动 t0，它用于算总耗时）
                    _stall_base = time.time()
                else:
                    _el = int(time.time() - t0)
                    loop_killed = (
                        f'agent 运行 {_el}s events 无增长'
                        f'（产物 {_n_art} 个，已调用工具 {_tool_cnt["total"]} 次），判为卡住')
                    try:
                        proc.kill()
                    except Exception:
                        pass
                    break

            _is_tool_line = '┊' in line
            if not _is_tool_line:
                continue
            _tool_cnt['total'] += 1

            # 识别动作类型（用于判断 Code↔Guard 交替）
            _act = ''
            if 'mcp_io_gu' in line:
                _act = 'guard'
            elif '🐍 exec' in line or 'mcp_io_ar' in line:
                _act = 'code' if '🐍 exec' in line else 'write'

            if _act:
                _tool_cnt['seq'].append(_act)
                if len(_tool_cnt['seq']) > 20:
                    _tool_cnt['seq'] = _tool_cnt['seq'][-20:]

                # ★ 2026-11-06 第3项：Code 调用单独限额
                #   实测 Code 事件全是 "import csv, collections"（分析自己的产物），
                #   通过的 case 最多 49 次，失败的用了 114 次。
                #   超 60 次直接杀，不等 900s 超时（省 10 分钟/单）。
                if _act == 'code':
                    _tool_cnt['code'] += 1
                    if _tool_cnt['code'] > MAX_CODE_CALLS:
                        loop_killed = (f'Code 调用 {_tool_cnt["code"]} 次超过上限 '
                                       f'{MAX_CODE_CALLS}（在反复分析产物而非直接修改），已终止')
                        try:
                            proc.kill()
                        except Exception:
                            pass
                        break

                # ★★ 2026-11-06 修正：原判定过激，误杀正常调试
                #   原逻辑：最近 10 个动作里 {code,guard} 相邻出现 ≥4 次
                #   实测误杀：末尾是 Code,Tool,Tool,Code,Guard,Tool,Code,Code,Guard
                #            —— 中间隔着 Tool，根本不算「反复交替」，却因计数方式被判死循环。
                #
                #   新逻辑：要求 **严格连续** 交替，即 C,G,C,G,C 或 G,C,G,C,G
                #   （中间不能有 Tool/Write 打断），才判为死循环。
                #   同时 guard 总次数上限仍然保留（>8 次）作为兜底。
                _s = _tool_cnt['seq']
                _strict = 0
                for i in range(len(_s) - 1, 0, -1):
                    prev, cur = _s[i - 1], _s[i]
                    if {prev, cur} == {'code', 'guard'}:
                        _strict += 1
                    else:
                        break          # 一旦被打断就停，只数尾部连续交替
                # ★ 2026-11-08 改进：不只看交替次数，还要看错误是否相同
                #   原逻辑：Code↔Guard 交替 4 次就杀
                #   实测误杀：agent 在逐步收敛（每次 Guard 报不同的错，
                #           说明每次都在修不同的问题），却被判死循环
                #   新逻辑：交替 ≥4 次 且 最近 3 次 Guard 的 fatal 内容完全相同
                #           → 才是真死循环（改不动同一个错）
                if _strict >= 4:
                    _gf = _tool_cnt.get('guard_fatals') or []
                    _same_err = (len(_gf) >= 3 and _gf[-1] and
                                 len(set(_gf[-3:])) == 1)
                    if _same_err:
                        loop_killed = (
                            f'检测到 Code↔Guard 连续交替 {_strict} 次，'
                            f'且最近 3 次 Guard 报同一个错「{_gf[-1][:60]}」，'
                            f'判定为死循环，已终止')
                        try:
                            proc.kill()
                        except Exception:
                            pass
                        break
                    # 错误不同 → 在逐步收敛，放行（但仍在 seq 里记录）

            if _act == 'guard':
                _tool_cnt['guard'] += 1
                # ★★ 2026-11-13：改为读 guard_check 落盘的 guard_history.jsonl
                #   原来靠正则从终端抓 fatal 文本，MCP 返回值不一定完整出现在终端，
                #   格式一变就抓空 → 3 次空值被判「相同」→ 误杀。
                _cur_set = None
                try:
                    _hist_p = sess_dir / '.agent' / 'guard_history.jsonl'
                    if _hist_p.exists():
                        _lines = _hist_p.read_text(encoding='utf-8').strip().split('\n')
                        if _lines and _lines[-1]:
                            _last = json.loads(_lines[-1])
                            _cur_set = frozenset(_last.get('fatal') or [])
                except Exception:
                    _cur_set = None

                # 退化：读不到文件时用正则（兼容老行为）
                if _cur_set is None:
                    _fatal_sig = ''
                    _m_fatal = re.search(r'(?:fatal|致命)[:：]\s*([^\n]{0,120})',
                                         line, re.I)
                    if _m_fatal:
                        _fatal_sig = _m_fatal.group(1).strip()
                    _cur_set = frozenset([_fatal_sig] if _fatal_sig else [])

                _tool_cnt['guard_fatal_sets'].append(_cur_set)
                if len(_tool_cnt['guard_fatal_sets']) > 10:
                    _tool_cnt['guard_fatal_sets'] = _tool_cnt['guard_fatal_sets'][-10:]

                emit({'type': 'meta', 'event': 'guard_call',
                      'n': _tool_cnt['guard'], 't': round(time.time() - t0, 1)})
                # ★★ 2026-11-13 重写死循环判据（用户裁定）
                #
                #   用户原话：
                #     「如果是重复报错就说明修不了还报啥错呢，
                #       然后即使没有修正错误就没修正呗，提示有这个问题就行了」
                #     「fatal 一直是一个数值，如果都是不一样的错误不是误杀么」
                #
                #   旧逻辑的两个毛病：
                #     1. 只看 guard 累计次数 > 12 就杀 —— 不管错误有没有在收敛
                #        实测 NC20260913000295：guard 9 次被杀，但其实在正常修
                #        （重跑后 210s done，100% 族覆盖）
                #     2. 判据靠正则从终端输出抓 fatal 文本，格式一变就抓不到
                #        → 3 次都抓空 → 误判「相同错误」
                #
                #   新逻辑：比对「fatal 内容集合」是否真的没变
                #     · 集合完全相同 → 改了也不变 → 真死循环，杀
                #     · 集合在变小 / 内容在换 → 在收敛，放行
                #   累计次数只作极高档兜底（30 次），防止无限自检
                _gs = _tool_cnt['guard_fatal_sets']
                if len(_gs) >= 2:
                    _prev = _gs[-2]
                    _cur = _gs[-1]
                    if _cur and _prev == _cur:
                        # 集合一字不差 → 上一轮改了个寂寞
                        _same_count += 1
                    else:
                        _same_count = 0
                    if _same_count >= 2:
                        loop_killed = (
                            f'连续 {_same_count + 1} 次 guard_check 报'
                            f'完全相同的 {len(_cur)} 个问题'
                            f'（首个: {sorted(_cur)[0][:60]}），'
                            f'改不动了，判定为死循环，已终止')
                        try:
                            proc.kill()
                        except Exception:
                            pass
                        break

                if _tool_cnt['guard'] > MAX_GUARD_CALLS:
                    loop_killed = (f'guard_check 被调用 {_tool_cnt["guard"]} 次'
                                   f'（极高档兜底 {MAX_GUARD_CALLS}），已终止')
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

        # ★★ 2026-11-12 关键修复：resume 失效检测
        #
        #   bug：第 1 轮跑完后 agent_sid 拿到，第 2 轮用 --resume <sid> 续跑。
        #   但 hermes 的 session 在上下文压缩后会失效：
        #     "Session not found: compressed"
        #   → 进程直接 Goodbye 退出，什么也没做。
        #   → 3 轮循环里第 2、3 轮全是空转，fatal 数一模一样不变。
        #
        #   实测 NC20260828000360 / NC20260823000103：
        #     3 轮 fatal = 8/8/8 和 7/7/7，完全没有变化，
        #     原因就是第 2、3 轮 agent 根本没启动。
        #
        #   修复：检测到 resume 失效 → 不带 resume 重跑（降级为全新会话）
        if resume_sid and ('Session not found' in out
                           or 'session ID from a previous CLI run' in out):
            emit({'type': 'meta', 'event': 'resume_failed',
                  'resume_sid': resume_sid,
                  'action': 'retry_without_resume'})
            # 降级：不带 --resume 重跑
            return call_hermes(prompt, workdir, resume_sid=None,
                               events_fp=events_fp, timeout=timeout,
                               stage=stage)

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
def run_guard(sess_dir, exp_path='', intent_path='', stage='fill'):
    """
    ★ exp_path 支持多个：用 ; 分隔，内部转成 --exp-multi
    """
    """跑 guard，返回结构化结果。

    ★ 2026-11-09 两阶段：stage='plan' 时不跑 guard
      （阶段1 没有 mml.txt，跑 guard 只会报 NO_MML，导致 agent 死循环改产物）
    """
    if stage == 'plan':
        return {'verdict': 'pass', 'fatal': [], 'warnings': [],
                'skipped': True, 'reason': '阶段1（命令族规划）不跑配置校验'}

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
    # ★ 2026-11-10：必须传 --session-dir 和 --params，否则 G20/G21/G26 全部 skipped
    #   （历史坑：2026-11-08 也踩过一次，G20/G21 因为没传 session_dir 而全 skipped）
    if sess_dir and Path(sess_dir).exists():
        cmd += ['--session-dir', str(sess_dir)]
        _pcsv = Path(sess_dir) / 'analysis_code' / 'params.csv'
        if _pcsv.exists():
            cmd += ['--params', str(_pcsv)]

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


def _gen_mml_from_params(adir):
    """从 params.csv 机械生成 mml.txt（纯代码，不调 LLM）。

    ★ 2026-11-09 方案B（用户裁定）：
      agent 只负责 params.csv（理解意图、选族、填参数是它的强项），
      mml.txt 由代码生成 —— 确定性、不会因输出长度上限被截断。

    实测对比（NC20260811002706）：
      params.csv 1102 行 / 826 组 → 代码生成 826 条 / 132KB / 0 错误
      agent 手写 mml.txt → 21 条 / 3.7KB（只完成 2 个 Phase）
    """
    csv_path = Path(adir) / 'params.csv'
    if not csv_path.exists() or csv_path.stat().st_size == 0:
        return None
    try:
        import sys as _s
        _wf = str(Path(__file__).resolve().parent)
        if _wf not in _s.path:
            _s.path.insert(0, _wf)
        import importlib
        import mml_gen as _mg
        importlib.reload(_mg)
        r = _mg.gen_mml(str(csv_path))
    except Exception as e:
        return {'ok': False, 'error': f'{type(e).__name__}: {e}'}

    text = (r or {}).get('text') or ''
    n_cmd = (r or {}).get('n_commands') or 0
    if not text.strip() or n_cmd == 0:
        return {'ok': False, 'error': '生成结果为空',
                'errors': (r or {}).get('errors') or []}

    # 写 mml.txt（保留 agent 写过的头部注释，如果有）
    target = Path(adir) / 'mml.txt'
    header = ''
    if target.exists():
        try:
            old = target.read_text(encoding='utf-8', errors='replace')
            # 取开头连续的 /* */ 注释块作为头部
            lines = old.split('\n')
            hl = []
            for ln in lines[:20]:
                if ln.strip().startswith('/*') or ln.strip().startswith('*') \
                        or ln.strip().startswith('*/') or ln.strip().startswith('   '):
                    hl.append(ln)
                elif ln.strip() == '' and hl:
                    hl.append(ln)
                else:
                    break
            header = '\n'.join(hl).rstrip() + '\n\n' if hl else ''
        except Exception:
            header = ''

    body = (r or {}).get('text') or ''
    note = ('/* ===== 本文件由 params.csv 自动生成（代码，非 agent 手写）===== */\n'
            f'/* 数据源：params.csv（{{n_groups}} 组）→ 生成 {{n_commands}} 条命令 */\n\n')
    note = note.replace('{n_groups}', str((r or {}).get('n_groups') or 0))
    note = note.replace('{n_commands}', str(n_cmd))
    target.write_text(header + note + body, encoding='utf-8')

    return {'ok': True, 'n_commands': n_cmd,
            'n_groups': (r or {}).get('n_groups') or 0,
            'errors': (r or {}).get('errors') or []}


def check_artifacts(sess_dir, stage='fill', with_recommended=False):
    """检查必需产物是否齐全。

    ★ 2026-11-09 两阶段：
      stage='plan'  只要求 命令族规划.md（配置类产物本来就不该有）
      stage='fill'  要求 mml.txt + params.csv（配置本体）

    ★ 2026-11-09 分级（用户裁定「按错了会怎样分级」）：
      · mml.txt / params.csv 缺失 → 配置不可用 → fatal
      · 配置分析.md 缺失        → 只是缺说明 → warn（不判失败）
      实测：87 工单里 6 个因为忘写 配置分析.md 被整单判失败，
           但它们的 mml.txt 和 params.csv 都是完整的。
    """
    adir = Path(sess_dir) / 'analysis_code'
    if stage == 'plan':
        required, recommended = ['命令族规划.md'], []
    else:
        required = REQUIRED_ARTIFACTS
        recommended = RECOMMENDED_ARTIFACTS

    missing = [n for n in required
               if not (adir / n).exists() or (adir / n).stat().st_size == 0]
    if with_recommended:
        miss_rec = [n for n in recommended
                    if not (adir / n).exists() or (adir / n).stat().st_size == 0]
        return missing, miss_rec
    return missing


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def run_agent(session_id, intent_text, product_hint='', on_event=None,
              resume_agent_session=None, stage='fill'):
    """跑 agent 主流程（含 3 轮校验闭环）。

    Returns dict: {status, rounds, elapsed, produced, guard, error, session_id}
    """
    sess_dir = SESSIONS_ROOT / session_id
    adir = sess_dir / 'analysis_code'
    adir.mkdir(parents=True, exist_ok=True)
    wfdir = sess_dir / '.agent'
    wfdir.mkdir(exist_ok=True)
    # ★ 两阶段：写 stage 标记文件，供 MCP 工具（artifact_write）读取判白名单
    try:
        (wfdir / 'stage').write_text(str(stage or 'fill'), encoding='utf-8')
    except Exception:
        pass
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
                          workdir=sess_dir, stage=stage)
    (rundir / 'prompt_r1.txt').write_text(prompt, encoding='utf-8')

    events_fp = open(events_path, 'a', encoding='utf-8')
    t_start = time.time()
    # ★ 二次意图：接着上一轮的 agent 会话跑（保留完整上下文，不用重新探索）
    agent_sid = resume_agent_session or None
    rounds = []
    final_guard = None
    error = None
    remaining_fatal = []      # 产物完整但仍有 fatal 的项（待人工确认）

    try:
        for rnd in range(1, MAX_ROUNDS + 1):
            # ★ 2026-11-06 修 bug：这里原来写成 `emit = {...}`，
            #   把函数 emit 覆盖成了 dict，后面 rescue 分支调 emit(...) 就炸
            #   TypeError: 'dict' object is not callable（偶发，只在有 /tmp 草稿时触发）
            _ev_round_start = {'type': 'meta', 'event': 'round_start', 'round': rnd}
            events_fp.write(json.dumps(_ev_round_start, ensure_ascii=False) + '\n')
            events_fp.flush()

            cur_prompt = prompt if rnd == 1 else build_feedback(final_guard or {})
            ok, out, elapsed, got_sid, err = call_hermes(
                cur_prompt, sess_dir, resume_sid=agent_sid,
                events_fp=events_fp, timeout=ROUND_TIMEOUT, stage=stage)

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
            _rh = round_hard_limit_for(sess_dir)
            if elapsed > _rh:
                error = (f'第{rnd}轮耗时 {elapsed}s 超过 {_rh}s 上限，'
                         f'判定为 agent 陷入循环（反复改产物+自检）')
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'error': 'round_slow_loop', 'fatal_limit': True})
                break

            # ★ 2026-11-06：先尝试从 /tmp 捞回 agent 遗留的草稿
            #
            # ⚠ 这里原来调 emit(...)，但 emit 是 call_hermes 内部的闭包，
            #   run_agent 里访问不到 → NameError: name 'emit' is not defined
            #   （只有在真捞到草稿时才触发，所以之前一直是偶发）
            #   直接写 events_fp 即可，run_agent 有这个文件句柄
            _rescued = rescue_tmp_artifacts(sess_dir)
            if _rescued:
                try:
                    events_fp.write(json.dumps(
                        {'type': 'meta', 'event': 'rescue',
                         'round': rnd, 'files': _rescued},
                        ensure_ascii=False) + '\n')
                    events_fp.flush()
                except Exception:
                    pass

            # ★ 两阶段：阶段1 结束后清理越界产物
            #   agent 可能用 execute_code + open() 绕过 artifact_write 白名单
            #   直接写文件，这里事后清理，保证阶段1 产物干净
            if stage == 'plan':
                for _n in ('mml.txt', 'params.csv', '配置分析.md'):
                    _f = adir / _n
                    if _f.exists():
                        try:
                            _f.unlink()
                            events_fp.write(json.dumps(
                                {'type': 'meta', 'event': 'stage_cleanup',
                                 'removed': _n, 'round': rnd},
                                ensure_ascii=False) + '\n')
                            events_fp.flush()
                        except Exception:
                            pass

            # ★★ 2026-11-09 方案B：mml.txt 由代码从 params.csv 生成
            #   实测 NC20260811002706：params.csv 826 组（数据齐全），
            #   但 agent 手写 mml.txt 只写了 21 条（被输出长度截断）。
            #   改为 agent 只负责 params.csv，代码机械生成 mml.txt。
            if stage == 'fill':
                _gen = _gen_mml_from_params(adir)
                if _gen and _gen.get('ok'):
                    try:
                        events_fp.write(json.dumps(
                            {'type': 'meta', 'event': 'mml_generated',
                             'round': rnd, 'n_commands': _gen.get('n_commands'),
                             'n_groups': _gen.get('n_groups'),
                             'errors': len(_gen.get('errors') or [])},
                            ensure_ascii=False) + '\n')
                        events_fp.flush()
                    except Exception:
                        pass

            # 检查产物（★ 两阶段：阶段1 只要求 命令族规划.md）
            # ★ 分级：mml.txt/params.csv 缺 → fatal；配置分析.md 缺 → warn
            missing, missing_rec = check_artifacts(sess_dir, stage=stage,
                                                   with_recommended=True)
            _rec_warn = []
            if missing_rec:
                _rec_warn = [f'缺少 {", ".join(missing_rec)}'
                             f'（不影响配置可用性，只是缺依据说明）']
            if missing:
                final_guard = {'fatal': [{'code': 'MISSING_ARTIFACT',
                                          'message': f'缺少产物: {", ".join(missing)}'}],
                               'warnings': _rec_warn}
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'missing': missing})
                if rnd == MAX_ROUNDS:
                    error = f'3 轮后仍缺产物: {", ".join(missing)}'
                continue

            # 跑 guard
            final_guard = run_guard(sess_dir, exp_path, str(intent_file), stage=stage)
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

            # ★★ 2026-11-13 用户裁定：fatal 不再作为失败标志
            #   「即使没有修正错误就没修正呗，提示有这个问题就行了」
            #
            #   原逻辑：3 轮后仍有 fatal → error = '...致命问题' → 整单判 failed
            #   问题：fatal 里有相当一部分是「agent 判断 vs 判据口径」的分歧
            #        （如跨网元族在本网元配不了、方案选择类），
            #        产物其实完整可交付，只因 fatal 未清零就判失败太严。
            #
            #   新逻辑：
            #     · 产物完整 → done（fatal 作为「待人工确认项」附在报告里）
            #     · 产物缺失 / STALL / 崩溃 / 超时 → failed
            #   留在 fatal 里但不阻断的，写进 remaining_fatal 供报告展示。
            if rnd == MAX_ROUNDS:
                _nf = len(final_guard.get('fatal') or [])
                if _nf:
                    remaining_fatal = final_guard.get('fatal') or []
                    events_fp.write(json.dumps({
                        'type': 'meta', 'event': 'fatal_not_blocking',
                        'n': _nf,
                        'note': '产物完整，fatal 作为待确认项交付，不判失败',
                    }, ensure_ascii=False) + '\n')
                    events_fp.flush()

    finally:
        try:
            # ★ 2026-11-13 改：done 只取决于「有没有产出」
            _has_artifacts = not error
            events_fp.write(json.dumps({
                'type': 'done',
                'status': 'done' if _has_artifacts else 'failed',
                'remaining_fatal': len(remaining_fatal),
            }, ensure_ascii=False) + '\n')
            events_fp.flush()
            events_fp.close()
        except Exception:
            pass

    # 产物清单
    produced = []
    # ★ 2026-11-13 修：阶段1 只产出「命令族规划.md」，原来没列入 produced
    #   → 阶段1 判 status 时 produced=[] → 判 failed（即使 verdict=pass）
    #   实测：5 单阶段1 全部 verdict=pass、规划表已写出，却被判 failed
    _ARTIFACT_NAMES = ['命令族规划.md',          # 阶段1 必需
                       'mml.txt', 'params.csv',   # 阶段2 必需
                       '配置分析.md', '方案澄清.json',  # 阶段2 建议
                       '阶段3修复清单.md']          # 阶段3 产出
    for name in _ARTIFACT_NAMES:
        f = adir / name
        if f.exists():
            produced.append({'name': name, 'size': f.stat().st_size})

    verdict = (final_guard or {}).get('verdict')
    # ★★ 2026-11-13 用户裁定：fatal 不作为失败标志
    #   「即使没有修正错误就没修正呗，提示有这个问题就行了」
    #
    #   旧：verdict in ('pass','warn') 才算 done → 有 fatal 一律 failed
    #   新：产物齐全就算 done（fatal 作为待人工确认项随报告交付）
    #       failed 只保留三种真失败：
    #         · error 非空（STALL / 崩溃 / 超时 / 缺产物）
    #         · 没有任何产物
    # ★ 2026-11-13 修：按阶段判断「产物齐全」，不能用统一列表
    #   阶段1 只看 命令族规划.md
    #   阶段2 看 params.csv + mml.txt
    def _stage_ok(st):
        names = {x['name'] for x in produced}
        if st == 'plan':
            return '命令族规划.md' in names
        # fill / repair：params.csv 和 mml.txt 是核心产物
        return 'params.csv' in names and 'mml.txt' in names

    _has_produced = _stage_ok(stage)
    status = 'done' if (not error and _has_produced) else 'failed'

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
            # ★ 2026-11-06：附上人话解释，前端直接展示
            'explain': _explain_guard(final_guard or {},
                                      has_artifacts=bool(produced)),
        },
        'error': error,
    }
