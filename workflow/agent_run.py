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
def build_prompt(session_id, intent_text, files_info, product_hint=''):
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
    lines.append('  2. params.csv     参数表。列：序号,命令族,参数,值,来源,说明；需人工确认的填【待填写】')
    lines.append('  3. 配置分析.md    用了哪些依据、为什么选这些族、命名来源、注意事项')
    lines.append('  4. 方案澄清.json  （可选）只放方案级问题，没有就给 []')
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
    lines.append('  只提「影响配置方案走向」的选择题，最多 5 条，宁缺勿滥。')
    lines.append('  该问：场景选择 / 要不要某个可选能力 / 意图歧义 / 两个方案代价不同')
    lines.append('  不该问：具体域名 IP URRID 端口值 / 某参数填什么 / 「请提供清单」/ 格式问题')
    lines.append('  格式：[{"id":"q1","question":"...","why":"...",')
    lines.append('         "options":[{"label":"...","reply":"..."}]}]')
    lines.append('  options 每个 2-3 个，reply 写成用户点了之后会发的原话（第一人称，不依赖上下文）。')
    lines.append('')

    lines.append('【硬要求】')
    lines.append('  · 命名：有 EXP 沿用现网统计规律（不要照抄文档示例）；无 EXP 按文档示例或用户规划')
    lines.append('  · 不要编造没有依据的数值')
    lines.append('  · 区分「现网已有」和「本次新增」：现网已有的对象不要重复创建')
    lines.append('  · 单工单规模合理：同一个族一般不超过 20-30 条（除非意图明确要求批量）')
    lines.append('  · 写完产物后调一次 guard_check；有 fatal 自己修完再调，直到通过')
    lines.append('  · 完成后简述：做了什么、哪些需要人工确认')
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
    if exp_path and Path(exp_path).exists():
        cmd += ['--exp', str(exp_path)]
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


def check_artifacts(sess_dir):
    """检查必需产物是否齐全。"""
    adir = Path(sess_dir) / 'analysis_code'
    missing = [n for n in REQUIRED_ARTIFACTS if not (adir / n).exists()]
    return missing


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def run_agent(session_id, intent_text, product_hint='', on_event=None):
    """跑 agent 主流程（含 3 轮校验闭环）。

    Returns dict: {status, rounds, elapsed, produced, guard, error, session_id}
    """
    sess_dir = SESSIONS_ROOT / session_id
    adir = sess_dir / 'analysis_code'
    adir.mkdir(parents=True, exist_ok=True)
    wfdir = sess_dir / '.agent'
    wfdir.mkdir(exist_ok=True)
    events_path = wfdir / 'events.jsonl'
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

    # 找 EXP
    exp_path = ''
    for f in files_info:
        if f.get('is_exp') and f.get('parsed'):
            rel = f['parsed']
            cand = sess_dir / rel if '/' in rel else sess_dir / 'uploads_text' / rel
            if cand.exists():
                exp_path = str(cand)
                break

    prompt = build_prompt(session_id, intent_text, files_info, product_hint)
    (wfdir / 'prompt_r1.txt').write_text(prompt, encoding='utf-8')

    events_fp = open(events_path, 'a', encoding='utf-8')
    t_start = time.time()
    agent_sid = None
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

            (wfdir / f'round{rnd}_out.txt').write_text(out or '', encoding='utf-8')

            if err:
                error = f'第{rnd}轮: {err}'
                rounds.append({'round': rnd, 'ok': False, 'elapsed': elapsed,
                               'error': err})
                break

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
