#!/usr/bin/env python3
"""loop_runner.py — Agent 自主 loop + 代码守门（替代九步硬隔离）。

★ 设计（2026-11-04 用户裁决：A+C）
  A = agent loop + 代码守门
  C = 意图澄清（治理解漂移）

★ 与九步的区别
  九步：代码编排，每步独立 LLM 调用，JSON 传递（信息衰减）
  loop：一个 agent 会话跑完，上下文连续（信息不丢）+ 守门兜底

★ 流程
  ┌─ 1. 预检：EXP 存在、意图可用
  ├─ 2. 意图澄清：产出问题清单（写入确认清单，不阻断）
  ├─ 3. agent loop（hermes -z，带工具和时间盒）
  │     · 每 3 分钟检查中间产物（节拍控制）
  │     · 总时限 15 分钟
  ├─ 4. 守门（guard.py）：C2/G11/G12/G16/G17
  │     · pass  → 收编产物
  │     · warn  → 收编 + 记录告警
  │     · fail  → 回炉重试（最多 2 轮，把 fatal 原因喂回去）
  └─ 5. 产物收编 + 确认清单生成

★ 用法
  python3 loop_runner.py --sid <会话> --gid g1 --intent <文件> --exp <文件>
                         [--action fresh|revise] [--parent-dir <前代目录>]
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

WF_ROOT = Path('/opt/expgv/workflow')
GUARD = WF_ROOT / 'guard' / 'guard.py'
sys.path.insert(0, str(WF_ROOT))

# ── 时间盒 ──
TICK_SEC = 180          # 每 3 分钟检查一次中间产物
MAX_TOTAL_SEC = 900     # 总时限 15 分钟
MAX_RETRY = 2           # 守门失败最多回炉 2 次
HERMES_TIMEOUT = 1500   # 单次 hermes 调用上限（留余量给守门）

CANON_MML = 'mml.txt'
CANON_CSV = 'params.csv'
CANON_MD = '配置分析.md'


def log(msg):
    print(msg, flush=True)


# ═══════════════════════════════════════════════════════════
# 产物收集（容忍各种命名）
# ═══════════════════════════════════════════════════════════
def find_products(adir):
    """在 agent 工作目录里找 mml/csv/md（容忍命名差异）。"""
    adir = Path(adir)
    if not adir.exists():
        return {}

    def pick(patterns, exclude_v=False):
        out = []
        for p in adir.rglob('*'):
            if not p.is_file():
                continue
            n = p.name.lower()
            if exclude_v and re.search(r'_v\d+|第.*版', n):
                continue
            for pat in patterns:
                if re.search(pat, n):
                    out.append(p)
                    break
        # 优先选 mml.txt / params.csv / 配置分析.md
        out.sort(key=lambda p: (len(p.name), p.stat().st_mtime))
        return out

    mml = pick([r'^mml\.txt$', r'\.mml\.txt$', r'\.mml$', r'mml.*\.txt$'])
    csv = pick([r'^params\.csv$', r'params.*\.csv$', r'.*参数.*\.csv$'])
    md = pick([r'^配置分析\.md$', r'配置分析.*\.md$', r'.*分析.*\.md$'])
    clarify = pick([r'^方案澄清\.json$', r'方案澄清.*\.json$', r'clarify.*\.json$'])

    return {
        'mml': mml[0] if mml else None,
        'csv': csv[0] if csv else None,
        'md': md[0] if md else None,
        'clarify': clarify[0] if clarify else None,
    }


def check_tick(adir, start_ts, tick_no):
    """节拍检查：有没有中间产物。"""
    prods = find_products(adir)
    n = sum(1 for v in prods.values() if v)
    elapsed = time.time() - start_ts
    log(f'  ⏱ 节拍 #{tick_no}（{int(elapsed)}s）：中间产物 {n}/3')
    return n


# ═══════════════════════════════════════════════════════════
# agent loop
# ═══════════════════════════════════════════════════════════
def build_prompt(sid, sdir, intent_text, action, prior_dir, guard_feedback=None):
    """构造 agent 任务 prompt。"""
    # ★ 2026-11-05：资料清单改为读 uploads_index.json
    #   用户可上传任意文件（不限 EXP、不限数量、不限网元）
    #   有 EXP 就用（走统计规律），没有就用其他文件（按文档/意图生成）
    files_block = ''
    has_exp = False
    data_root = Path(sdir)
    idx_path = data_root / 'uploads_index.json'
    if idx_path.exists():
        try:
            import json as _json
            idx = _json.loads(idx_path.read_text(encoding='utf-8'))
            lines = []
            for f in idx.get('files') or []:
                if f.get('error'):
                    lines.append(f"- {f['name']}（解析失败：{f['error']}，跳过）")
                    continue
                role = f.get('role') or 'data'
                parsed = f.get('parsed')
                size_kb = max(1, (f.get('size') or 0) // 1024)
                note = '；'.join(f.get('notes') or [])
                tag = {'exp': '【现网快照】', 'data': '【数据文件】'}.get(role, '')
                path_hint = f' → 已解析为 uploads_text/{parsed}' if parsed else ''
                lines.append(f"- {tag}{f['name']}（{size_kb}KB）{path_hint}"
                             + (f'  [{note}]' if note else ''))
                if role == 'exp':
                    has_exp = True
            if lines:
                files_block = '\n'.join(lines)
        except Exception:
            pass

    # 兜底：老会话没有 uploads_index，看 exp_v1
    if not files_block:
        exp_files = list((data_root / 'exp_v1').glob('*.txt')) if (data_root / 'exp_v1').exists() else []
        if exp_files:
            has_exp = True
            files_block = '\n'.join(
                f'- 【现网快照】{f}（{f.stat().st_size // 1024}KB）' for f in exp_files)
        else:
            files_block = '（无上传文件）'

    # 无 EXP 时的额外提示
    no_exp_hint = '' if has_exp else (
        '\n⚠ 本次**没有现网 EXP 快照**：\n'
        '  · 命名不要编造现网规律，按特性文档示例或用户给出的规划\n'
        '  · 所有业务值（域名/IP/URRNAME 等）如用户未提供，一律标【待填写】\n'
        '  · @src 依据只能用 doc（文档）/ plan（规划表）/ intent（意图），'
        '不能用 exp（没有快照）\n')

    prior_hint = ''
    if prior_dir and Path(prior_dir).exists():
        prior_hint = (f'\n【前代产物】{prior_dir} 下已有上一版配置。'
                      f'本次是改版：**必须保留前代的全部命令**，只做增/删/改。')

    fb = ''
    if guard_feedback:
        # 附加现有产物摘要（让 agent 知道「已有的是什么，只补缺的」）
        existing = ''
        try:
            ap = Path(sdir) / 'analysis_code'
            mml_p = ap / 'mml.txt'
            if mml_p.exists():
                txt = mml_p.read_text(encoding='utf-8', errors='replace')
                n = len([l for l in txt.split('\n')
                         if l.strip() and not l.strip().startswith(('/*','*','//','#'))])
                fams = sorted(set(re.findall(r'^(?:ADD|SET)\s+([A-Z0-9_]+)', txt, re.M)))
                existing = (f'\n\n【上一轮已有产物（不要重写，只做补丁）】'
                            f'\n  analysis_code/mml.txt：{n} 条命令，'
                            f'{len(fams)} 个族（{", ".join(fams[:15])}）')
        except Exception:
            pass

        fb = ('\n\n【⚠ 上一轮产物未通过代码校验】\n'
              + '\n'.join('  · ' + x for x in guard_feedback)
              + existing
              + '\n\n【⚠ 修正方式：增量补丁，不要重写】'
              + '\n  1. 上一轮已有的命令**全部保留**，只在需要的地方增/改'
              + '\n  2. 不能为了消除某个告警就删掉整族命令'
              + '\n  3. 缺的族要补上，多的族不要删（除意图明确要求）'
              + '\n  4. 修完自己核一遍：意图要求的所有对象是否都在产物里')

    return f'''你是 5G 核心网 UDG/UPF 配置专家。工作目录 {sdir}。

【任务】{intent_text}

【工作目录里的文件】
{files_block}

【其他资料】
- 特性配置基线/ ：特性文档（含官方示例）
- 匹配报告.md ：特性匹配结果（若存在；注意分类标题可能错位，可疑处自己核对文档）
{no_exp_hint}{prior_hint}
【产出要求】写到 analysis_code/ 下，四个文件：
1. mml.txt —— 可执行 MML，按依赖顺序分 Phase 注释，**引用必须闭合**（后用的对象必须先定义）
2. params.csv —— 参数表，列：序号,命令族,参数,值,来源,说明；需人工确认的用【待填写】
3. 配置分析.md —— 用了哪些文档、为什么选这些族、命名依据、注意事项
4. 方案澄清.json —— **只放方案层面的问题**（见下），没有就给空数组 []

【方案澄清.json 的边界（重要）】
只提「影响配置方案走向」的选择题，最多 5 条，宁缺勿滥。

✅ 该问的（方案类）：
  · 场景选择（如 F352 的场景一缺省费率 / 场景二单独费率）
  · 要不要某个可选能力（如是否需要七层 L7FILTER 识别）
  · 意图歧义（如"调整刷新服务器"是新建绑定还是改存量）
  · 两个方案都能做但代价不同（如复用现网对象 vs 全新建）

❌ 不该问的（一律进 params.csv，不要在 json 里问）：
  · 具体域名 / IP / URRID / 端口 / 优先级 的值   ← 这些是【待填写】，用户统一在参数表填
  · 某个参数该填什么
  · 「请提供完整清单」这类要数据的要求
  · 格式问题、语法问题（你自己定）

格式：
[
  {{
    "id": "q1",
    "question": "本次计费走哪个场景？",
    "why": "F352 场景一用缺省费率 RG=2000000002 只建 URRGROUP；场景二要单独 ADD URR 并指定 URRID",
    "options": [
      {{"label": "场景一：缺省费率", "reply": "按场景一配，用缺省费率 RG=2000000002，只建 URRGROUP"}},
      {{"label": "场景二：单独费率", "reply": "按场景二配，需要单独 ADD URR，URRID 我后续在参数表填"}}
    ]
  }}
]

options 每个 2-3 个，reply 写成用户点了之后会发给你的原话（第一人称需求）。
用户还可以自己编辑回复，所以 reply 要能独立成立、不依赖上下文代词。

【硬要求】
- 命名：有 EXP 时沿用现网统计规律（不要照抄文档示例）；无 EXP 时按文档示例或用户规划
- 不要编造没有依据的数值（有 EXP 就以 EXP 为准）
- **区分「现网已有」和「本次新增」**：现网已有的对象不要重复创建，本工单只配新增的部分
- 单工单规模合理：同一个族一般不超过 20-30 条（除非意图明确要求批量）
{fb}

【⚠ 来源标注：mml.txt 里每条命令都要标依据】
在命令行尾用注释标来源，格式 `@src=<类型>:<定位>`：

  @src=exp:L<行号>          取自 EXP 第 N 行（守门会去核验）
  @src=exp:derive <规律说明>  命名/格式派生自现网统计，值本身是新造的
  @src=doc:<文档>:<章节>     取自特性文档（如 doc:F352:表2）
  @src=intent:<要素>         意图明确给出的（如 intent:TCP80,443）
  @src=plan:<来源>           用户提供的数据规划表
  @src=infer <推导规则>      从业务逻辑推出（必须写规则，如 infer 离线URRID=在线+10000）

规则：
1. **有注释 = 有依据；无注释 = 无依据**（占位符【待填写】天然算无依据，不用标）
2. 主键参数（HOSTNAME/FILTERNAME/URRNAME/RULENAME/USERPROFILENAME 等）**有值就必须标 @src**，
   否则判为编造值
3. 整族超过 5 条且全部无 @src → 判为空壳族（必须标依据或减少条数）
4. @src=exp:L### 会被自动核验——值必须真的在那一行里，标错会判为虚假依据

示例：
  ADD HOST:HOSTNAME="hngd_00_h_001", DOMAINVALUE="video.hncatv.com", PRIORITY=30000;   // @src=plan:域名规划#1
  ADD HOST:HOSTNAME="hngd_00_h_002", DOMAINVALUE="【待填写】", PRIORITY=30001;          // @src=exp:derive naming=hngd_00_h_NNN
  ADD FILTER:FILTERNAME="hngd_00_f_h_001", SVRIPMODE=HOSTNAME;                          // @src=exp:L1230
  ADD URR:URRNAME="hngd_00_cbb_online", URRNAME2="【待填写】";                            // @src=doc:F352:表2

完成后简述：做了什么、遇到什么问题、哪些需要人工确认。'''


# 工具名 → 动作类型（仿 DeepSeek harness 的 Think/Bash/Write/Read 标签）
_TOOL_ACTION = {
    'read_file': 'Read', 'search_files': 'Search', 'glob': 'Search',
    'list_dir': 'List', 'skill_view': 'Skill',
    'write_file': 'Write', 'patch': 'Edit', 'apply_patch': 'Edit',
    'terminal': 'Bash', 'execute_code': 'Code', 'bash': 'Bash',
    'process': 'Proc', 'web_search': 'Web', 'web_extract': 'Web',
    'delegate_task': 'Agent', 'todo': 'Todo', 'clarify': 'Ask',
}


# hermes chat 的工具预览行：``┊ 💻 $  <命令>  0.2s``
# 图标 → 动作类型
_ICON_ACTION = {
    '💻': 'Bash', '💰': 'Bash', '🖥': 'Bash',
    '📖': 'Read', '📄': 'Read',
    '✍': 'Write', '📝': 'Write', '💾': 'Write',
    '🔎': 'Search', '🔍': 'Search',
    '🌐': 'Web', '🔗': 'Web',
    '🧠': 'Think', '🤔': 'Think',
    '📊': 'Code', '🐍': 'Code', '⚙': 'Code',
    '🛠': 'Tool', '🔧': 'Tool',
}
_TOOL_LINE = re.compile(r'┊\s*(\S+)\s+(\S+)\s+(.*?)\s+(-?[\d.]+)s(?:\s+\[exit \d+\])?\s*$')


def _drain_stdout(proc, collected, stop_flag):
    """无事件推送时，只把 stdout 收集起来。"""
    try:
        for raw in iter(proc.stdout.readline, ''):
            collected.append(raw)
    except Exception:
        pass


def _stream_stdout(proc, events_fp, stop_flag, collected=None):
    """逐行读 hermes chat 的 stdout，解析工具调用行写事件。

    ★ 唯一可靠的实时源（2026-11-05 实测）：
      - hermes -z：工具调用不写日志、不实时落库 ⇒ 无法实时
      - agent.log：-z 模式下工具行根本不写
      - state.db ：会话结束才落库
      - hermes chat -q（不加 -Q）：**stdout 实时打印工具预览行** ✅
    """
    import json as _json
    # 标记：确认线程真的启动了（排查用）
    try:
        with open(str(events_fp.name).replace('events.jsonl', 'thread_mark.txt'), 'w') as _mf:
            _mf.write('started\n')
    except Exception:
        pass

    def emit(ev):
        try:
            events_fp.write(_json.dumps(ev, ensure_ascii=False) + '\n')
            events_fp.flush()
        except Exception:
            pass

    _dbg = None
    try:
        _dbg = open(str(events_fp.name).replace('events.jsonl', 'stdout_raw.log'), 'a',
                    encoding='utf-8')
    except Exception:
        _dbg = None

    for raw in iter(proc.stdout.readline, ''):
        if stop_flag['stop']:
            break
        if collected is not None:
            collected.append(raw)
        if _dbg:
            try:
                _dbg.write(raw); _dbg.flush()
            except Exception:
                pass
        line = raw.rstrip('\r\n')
        if not line.strip():
            continue
        # 工具预览行
        m = _TOOL_LINE.search(line)
        if m:
            icon, kind, content, dur = m.groups()
            action = _ICON_ACTION.get(icon, 'Tool')
            # content 可能含前缀符号，取有用的部分
            tgt = content.strip()
            # 命令类：提取文件名或前 60 字符
            if action in ('Bash', 'Code'):
                _py = re.search(r'python3?\s+(\S+)', tgt)
                if _py:
                    tgt = os.path.basename(_py.group(1))
                else:
                    tgt = tgt[:60]
            else:
                tgt = tgt[:70]
            emit({'type': 'step', 'kind': 'tool', 'action': action,
                  'target': tgt, 'dur': abs(float(dur)), 'detail': content[:150]})
            continue
        # 模型转发/思考（非工具行，且有内容）
        if line.startswith('  ┊') or line.startswith(' └'):
            continue
        # 其它输出暂不推（避免噪音）

    if _dbg:
        try: _dbg.close()
        except Exception: pass


def call_hermes(prompt, workdir, timeout=HERMES_TIMEOUT, events_path=None):
    """调 hermes 单次执行，实时解析工具调用写入事件文件。

    ★ 实现要点（2026-11-05 多次踩坑后的最终版）：
      1. 用 `hermes chat -q`（不加 -Q）——它的 stdout 实时打印工具预览行
             `┊ 💻 $ <命令>  0.2s`
         `hermes -z` 不行：工具调用既不写 agent.log，也不实时落 state.db
      2. **不用线程、不用 communicate()、不用 wait()** —— 直接 for line in stdout
         三者任一都会和本循环争抢 pipe，实测导致读到空、线程不启动等问题
      3. 超时用外部计时器检查（读循环里判 time.time() - t0）
    """
    import json as _json

    env = dict(os.environ)
    env['HERMES_SKIP_NODE_BOOTSTRAP'] = '1'
    t0 = time.time()

    events_fp = None
    if events_path:
        try:
            events_fp = open(events_path, 'a', encoding='utf-8')
        except Exception:
            events_fp = None

    def emit(ev):
        if not events_fp:
            return
        try:
            events_fp.write(_json.dumps(ev, ensure_ascii=False) + '\n')
            events_fp.flush()
        except Exception:
            pass

    out_lines = []
    proc = None
    try:
        proc = subprocess.Popen(
            ['hermes', 'chat', '-q', prompt, '--yolo',
             '--skills', 'mml_feature,mml_support'],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, bufsize=1, cwd=str(workdir), env=env)

        emit({'type': 'meta', 'event': 'spawn', 'pid': proc.pid})

        timed_out = False
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

            # ── 工具预览行：`┊ 💻 $  <命令>  0.2s` ──
            m = _TOOL_LINE.search(line)
            if m:
                icon, kind, content, dur = m.groups()
                action = _ICON_ACTION.get(icon, 'Tool')
                tgt = content.strip()
                if action in ('Bash', 'Code'):
                    _py = re.search(r'python3?\s+(\S+)', tgt)
                    tgt = os.path.basename(_py.group(1)) if _py else tgt[:60]
                else:
                    tgt = tgt[:70]
                emit({'type': 'step', 'kind': 'tool', 'action': action,
                      'target': tgt, 'dur': abs(float(dur)),
                      'detail': content[:150]})
                continue

        try:
            proc.wait(timeout=15)
        except Exception:
            try:
                proc.kill()
            except Exception:
                pass

        if timed_out:
            return '', round(time.time() - t0, 1), f'超时 {timeout}s'
        return ''.join(out_lines), round(time.time() - t0, 1), None

    except Exception as e:
        return '', round(time.time() - t0, 1), f'{type(e).__name__}: {e}'
    finally:
        if events_fp:
            try:
                events_fp.close()
            except Exception:
                pass
        if proc and proc.poll() is None:
            try:
                proc.kill()
            except Exception:
                pass


# ═══════════════════════════════════════════════════════════
# 守门
# ═══════════════════════════════════════════════════════════
def run_guard(mml_path, exp_path, intent_path, prior_mml_path=None,
              action='fresh'):
    cmd = [sys.executable, str(GUARD), '--mml', str(mml_path), '--json',
           '--action', action]
    if exp_path and Path(exp_path).exists():
        cmd += ['--exp', str(exp_path)]
    if intent_path and Path(intent_path).exists():
        cmd += ['--intent', str(intent_path)]
    if prior_mml_path and Path(prior_mml_path).exists():
        cmd += ['--prior-mml', str(prior_mml_path)]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        return json.loads(r.stdout)
    except Exception as e:
        return {'verdict': 'error', 'fatal': [f'守门执行失败: {e}'],
                'warnings': [], 'questions': [], 'checks': {}}


# ═══════════════════════════════════════════════════════════
# 主流程
# ═══════════════════════════════════════════════════════════
def run(sid, gid, intent_path, exp_path, action='fresh', parent_dir=None):
    sdir = Path('/data/sessions') / sid
    gdir = sdir / 'gen_v1' / gid
    adir = sdir / 'analysis_code'
    wfdir = gdir / 'wf'
    wfdir.mkdir(parents=True, exist_ok=True)
    adir.mkdir(parents=True, exist_ok=True)

    intent_text = Path(intent_path).read_text(encoding='utf-8', errors='replace')

    # ★ 2026-11-05：exp_path 为空时，自动从 uploads_index 里找 EXP
    #   （用户上传了 EXP 但没显式传 --exp 的场景）
    if not exp_path:
        _idx = sdir / 'uploads_index.json'
        if _idx.exists():
            try:
                import json as _json
                _d = _json.loads(_idx.read_text(encoding='utf-8'))
                for _f in _d.get('files') or []:
                    if _f.get('role') == 'exp' and _f.get('parsed'):
                        _cand = sdir / 'uploads_text' / _f['parsed']
                        if _cand.exists():
                            exp_path = str(_cand)
                            log(f'  自动探测到 EXP: {_f["name"]} → {_f["parsed"]}')
                            break
            except Exception:
                pass

    # 前代 mml（revise 用）
    prior_mml_path = None
    if action in ('revise', 'append') and parent_dir:
        cand = Path(parent_dir) / 'wf' / 'steps' / '07_render' / 'mml.txt'
        if not cand.exists():
            cand = Path(parent_dir) / 'analysis_code' / 'mml.txt'
        if not cand.exists():
            cand = Path(parent_dir) / 'mml.txt'
        if cand.exists():
            prior_mml_path = str(cand)

    # ★ 2026-11-04：revise 时先跑一遍前代的守门，把前代的缺陷一起告诉 agent
    #   实测：run2 漏了 SET REFRESHSRV，revise 直接继承了这个缺陷。
    prior_defects = []
    if prior_mml_path:
        try:
            pg = run_guard(prior_mml_path, exp_path, intent_path, None, action='fresh')
            prior_defects = (pg.get('fatal') or []) + (pg.get('warnings') or [])[:3]
            if prior_defects:
                log(f'  前代已知缺陷 {len(prior_defects)} 条（会要求本轮一并修）:')
                for d0 in prior_defects[:3]:
                    log(f'    · {d0}')
        except Exception:
            pass

    log(f'=== loop 开始：{sid} / {gid} / action={action} ===')
    log(f'  意图: {len(intent_text)} 字符')
    log(f'  EXP:  {exp_path or "（无，基于其他上传文件生成）"}')
    if prior_mml_path:
        log(f'  前代: {prior_mml_path}')

    # ── 意图澄清（预检，不阻断）──
    from guard.guard import clarify_intent  # type: ignore
    exp_text = ''
    if exp_path and Path(exp_path).exists():
        exp_text = Path(exp_path).read_text(encoding='utf-8', errors='replace')
    pre_clarify = clarify_intent(intent_text, exp_text)

    t_start = time.time()
    # 首轮就把前代缺陷带上（revise 场景）
    guard_feedback = (['前代遗留（本轮要一并修复）: ' + x for x in prior_defects]
                      if prior_defects else None)
    final = None
    attempts = []

    for attempt in range(1, MAX_RETRY + 2):
        log(f'\n── 第 {attempt} 轮 agent loop ──')
        prompt = build_prompt(sid, sdir, intent_text, action, parent_dir, guard_feedback)

        # ★ 2026-11-04：回炉时**不删产物**，改为增量修复
        #   实测教训：删了让 agent 从头写，它每轮写的范围越来越小
        #   （轮1缺2族 → 轮2缺6族 → 轮3缺1族），越改越乱。
        #   正确做法：保留上一轮产物，让 agent 只补缺失的部分。

        # 防御：目录可能被外部清理（实测：手工 rm 或容器重启后丢失）
        wfdir.mkdir(parents=True, exist_ok=True)
        adir.mkdir(parents=True, exist_ok=True)
        _evpath = str(wfdir / 'events.jsonl')
        out, elapsed, err = call_hermes(prompt, sdir, events_path=_evpath)
        try:
            (wfdir / f'llm_round{attempt}.txt').write_text(out, encoding='utf-8')
        except Exception:
            pass
        log(f'  agent 完成，耗时 {elapsed}s' + (f'（错误: {err}）' if err else ''))

        prods = find_products(adir)
        n = sum(1 for v in prods.values() if v)
        log(f'  产物: {n}/3 { {k: (v.name if v else None) for k,v in prods.items()} }')

        # ★ 2026-11-04：三件产物缺一不可（实测有一次只写了 mml.txt，守门 PASS 就收编了）
        missing_files = []
        if not prods.get('mml'):
            missing_files.append('mml.txt（可执行 MML）')
        if not prods.get('csv'):
            missing_files.append('params.csv（参数收集表）')
        if not prods.get('md'):
            missing_files.append('配置分析.md（用了哪些文档、为什么选这些族）')

        if missing_files:
            guard_feedback = [
                '上一轮缺少以下产物，必须补齐（都在 analysis_code/ 下）：',
            ] + ['  · ' + m for m in missing_files]
            if prods.get('mml'):
                guard_feedback.append(
                    '（mml.txt 已存在，**不要重写**，只补上缺的那几个文件）')
            log(f'  ⚠ 产物不全: {missing_files}')
            attempts.append({'round': attempt, 'elapsed': elapsed,
                             'verdict': 'incomplete',
                             'missing_files': missing_files})
            continue

        # ── 守门 ──
        g = run_guard(prods['mml'], exp_path, intent_path, prior_mml_path,
                      action=action)
        log(f'  守门: {g["verdict"].upper()}')
        for f in g['fatal']:
            log(f'    ❌ {f}')
        for w in g['warnings'][:3]:
            log(f'    ⚠️  {w}')
        attempts.append({'round': attempt, 'elapsed': elapsed,
                         'verdict': g['verdict'], 'fatal': g['fatal'],
                         'warnings': g['warnings'][:5]})

        if g['verdict'] in ('pass', 'warn'):
            final = (prods, g, attempt)
            break

        # fail → 回炉
        guard_feedback = g['fatal'] + [w for w in g['warnings'][:2]]
        if attempt <= MAX_RETRY:
            log(f'  → 回炉重试（第 {attempt+1} 轮）')

        # 超时保护
        if time.time() - t_start > MAX_TOTAL_SEC:
            log(f'  ⚠ 超过总时限 {MAX_TOTAL_SEC}s，用当前产物收尾')
            final = (prods, g, attempt)
            break

    if not final:
        log('  ❌ 所有轮次都失败')
        return {'ok': False, 'error': 'agent loop 未能产出合格配置',
                'attempts': attempts, 'elapsed': round(time.time()-t_start, 1)}

    prods, g, n_round = final

    # ── 收编到 gen 目录（固定名）──
    produced = []
    if prods['mml']:
        shutil.copy2(prods['mml'], gdir / CANON_MML); produced.append(CANON_MML)
    if prods['csv']:
        shutil.copy2(prods['csv'], gdir / CANON_CSV); produced.append(CANON_CSV)
    if prods['md']:
        shutil.copy2(prods['md'], gdir / '配置分析_workflow.md'); produced.append('配置分析_workflow.md')

    # 方案澄清（可选，agent 自己决定有没有）
    clarify_items = []
    if prods.get('clarify'):
        try:
            import json as _json
            _raw = prods['clarify'].read_text(encoding='utf-8', errors='replace')
            clarify_items = _json.loads(_raw)
            if not isinstance(clarify_items, list):
                clarify_items = []
            # 规范化：确保每条有 id / question / options
            norm = []
            for i, q in enumerate(clarify_items[:5], 1):   # 最多 5 条
                if not isinstance(q, dict) or not q.get('question'):
                    continue
                opts = []
                for o in (q.get('options') or [])[:4]:
                    if isinstance(o, dict) and o.get('label'):
                        opts.append({'label': str(o['label'])[:60],
                                     'reply': str(o.get('reply') or o['label'])[:500]})
                norm.append({
                    'id': q.get('id') or f'q{i}',
                    'question': str(q['question'])[:300],
                    'why': str(q.get('why') or '')[:500],
                    'options': opts,
                })
            clarify_items = norm
            # 原样收编
            shutil.copy2(prods['clarify'], gdir / '方案澄清.json')
            produced.append('方案澄清.json')
        except Exception as _e:
            log(f'  ⚠ 方案澄清.json 解析失败（忽略）: {_e}')
            clarify_items = []

    # ── 生成确认清单 ──
    checklist = build_checklist(intent_text, g, pre_clarify, produced,
                                Path(gdir / CANON_MML), attempts,
                                clarify_items=clarify_items,
                                csv_path=gdir / CANON_CSV)
    (gdir / '确认清单.md').write_text(checklist, encoding='utf-8')
    produced.append('确认清单.md')

    elapsed_total = round(time.time() - t_start, 1)
    log(f'\n=== 完成：{len(produced)} 个产物，总耗时 {elapsed_total}s，{n_round} 轮 ===')

    return {
        'ok': True, 'produced': produced, 'engine': 'loop',
        'elapsed': elapsed_total, 'rounds': n_round,
        'guard': {'verdict': g['verdict'], 'fatal': g['fatal'],
                  'warnings': g['warnings']},
        'clarify': clarify_items,          # 方案级问题（前端可点选）
        'attempts': attempts,
    }


def build_checklist(intent_text, guard_result, pre_clarify, produced, mml_path, attempts,
                    clarify_items=None, csv_path=None):
    """生成确认清单（含待确认问题）。"""
    L = ['# 配置确认清单（agent loop 引擎）', '']

    # 概况
    mml = mml_path.read_text(encoding='utf-8', errors='replace') if mml_path.exists() else ''
    sys.path.insert(0, str(WF_ROOT))
    from guard.guard import parse_mml, split_cmd  # type: ignore
    cmds = parse_mml(mml)
    from collections import Counter
    fams = Counter()
    for c in cmds:
        v, f, _ = split_cmd(c)
        if v and f:
            fams[f'{v} {f}'] += 1
    n_ph = len(re.findall(r'【待填写】|TBD_|TBD:|\{TODO', mml))

    L.append('## 一、概况')
    L.append('')
    L.append('| 项 | 值 |')
    L.append('|---|---|')
    L.append(f'| 引擎 | agent loop + 代码守门 |')
    L.append(f'| 命令数 | {len(cmds)} |')
    L.append(f'| 命令族数 | {len(fams)} |')
    L.append(f'| 待填参数 | {n_ph} |')
    L.append(f'| 守门判定 | {guard_result["verdict"].upper()} |')
    L.append(f'| agent 轮次 | {len(attempts)} |')
    L.append('')

    # 命令族
    L.append('## 二、命令族')
    L.append('')
    L.append('| 命令族 | 条数 |')
    L.append('|---|---|')
    for f, n in fams.most_common():
        L.append(f'| {f} | {n} |')
    L.append('')

    # 守门告警
    if guard_result['warnings'] or guard_result['fatal']:
        L.append('## 三、守门告警')
        L.append('')
        for f in guard_result['fatal']:
            L.append(f'- ❌ {f}')
        for w in guard_result['warnings']:
            L.append(f'- ⚠️  {w}')
        L.append('')

    # ── 四、方案待确认（只放方案级问题）──
    #   ★ 2026-11-05 用户裁定：澄清只管方案层面，参数一律走 params.csv
    #     不做"挨个问 IP/域名"这种无边界的澄清
    if clarify_items:
        L.append('## 四、方案待确认')
        L.append('')
        L.append('> 以下问题会影响配置方案的走向，请在对话里点选确认。')
        L.append('> 参数值（域名/IP/URRID 等）不在此处问，统一在 params.csv 里填。')
        L.append('')
        for i, q in enumerate(clarify_items, 1):
            L.append(f'### {i}. {q["question"]}')
            if q.get('why'):
                L.append(f'')
                L.append(f'{q["why"]}')
            L.append('')
            for o in (q.get('options') or []):
                L.append(f'- [ ] {o["label"]}')
            L.append('')

    # ── 五、参数待填（统一走表格）──
    n_ph_csv = 0
    ph_sample = []
    if csv_path and Path(csv_path).exists():
        try:
            _c = Path(csv_path).read_text(encoding='utf-8', errors='replace')
            _lines = [l for l in _c.split('\n') if '【待填写】' in l or 'TBD' in l]
            n_ph_csv = len(_lines)
            ph_sample = _lines[:8]
        except Exception:
            pass
    if n_ph_csv or n_ph:
        L.append('## 五、参数待填')
        L.append('')
        L.append(f'共 **{n_ph_csv or n_ph}** 处需要在 `params.csv` 里填。')
        L.append('')
        L.append('> 请打开 `params.csv` 统一填写，不要在这里逐个问 agent。')
        L.append('> 填完重新上传或直接说明"已填好"，agent 会重新生成。')
        L.append('')
        if ph_sample:
            L.append('样例（前 8 行）：')
            L.append('')
            L.append('```csv')
            for l in ph_sample:
                L.append(l[:160])
            L.append('```')
            L.append('')

    # 回炉记录
    if len(attempts) > 1:
        L.append('## 六、回炉记录')
        L.append('')
        for a in attempts:
            L.append(f"- 第 {a['round']} 轮：{a.get('verdict', '?')} "
                     f"{'; '.join((a.get('fatal') or [])[:2])}")
        L.append('')

    # MML
    L.append('## 七、MML 命令')
    L.append('')
    L.append('```mml')
    L.append(mml.rstrip())
    L.append('```')

    return '\n'.join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sid', required=True)
    ap.add_argument('--gid', required=True)
    ap.add_argument('--intent', required=True)
    ap.add_argument('--exp', default='',
                    help='EXP 路径；可空（无 EXP 时基于其他上传文件生成）')
    ap.add_argument('--action', default='fresh')
    ap.add_argument('--parent-dir', default=None)
    a = ap.parse_args()

    r = run(a.sid, a.gid, a.intent, a.exp, a.action, a.parent_dir)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    sys.exit(0 if r.get('ok') else 1)


if __name__ == '__main__':
    main()
