#!/usr/bin/env python3
"""mcp_io.py — 文件 / 产物 / 校验 / 澄清 MCP server。

★ 6 个工具
  file_list      列 workspace 文件（含类型、解析状态、是否 EXP）
  file_read      读文件内容（文本直读，大文件分页）
  file_parse     用 markitdown 转成 markdown（docx/xlsx/pdf/pptx/html/csv...）
  artifact_write 写产物到 analysis_code/（限 4 个固定名字）
  guard_check    跑七道门，返回 fatal/warnings
  clarify        提交方案级问题（前端渲染可点选卡片）

★ 设计原则
  · 文件解析一律走 markitdown（不自己写 docx/xlsx/pdf 解析）
  · 产物写入有硬约束（只能写 4 个名字，路径固定）
  · guard 复用 guard/guard.py 的七道门（单一实现）
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 配置
# ═══════════════════════════════════════════════════════════
SESSIONS_ROOT = Path(os.environ.get('EXP_SESSIONS_ROOT', '/data/sessions'))
WORKFLOW_ROOT = Path(os.environ.get('WF_ROOT', '/opt/expgv/workflow'))
GUARD_PY = WORKFLOW_ROOT / 'guard' / 'guard.py'

# 允许写的产物名（硬约束）
ALLOWED_ARTIFACTS = {
    # ★ 2026-11-09 方案B：mml.txt 由代码从 params.csv 生成，agent 不写
    'mml.txt': '可执行 MML 配置命令（由代码从 params.csv 生成）',
    'params.csv': '参数收集表',
    '配置分析.md': '配置分析说明',
    '方案澄清.json': '方案级澄清问题（JSON 数组）',
    # ★ 2026-11-09 两阶段生成：阶段1 的产物
    '命令族规划.md': '命令族规划表（阶段1 产物，阶段2 的 handover 载体）',
}

# ★ 2026-11-09 两阶段：阶段1 只允许写这些
PLAN_STAGE_ALLOWED = {'命令族规划.md', '方案澄清.json'}

# EXP 头部校验（与 mcp_exp 保持一致）
EXP_HEADER_PATTERNS = [
    re.compile(r'^/\* TIME = \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+(\+8:00)? \*/$'),
    re.compile(r'^/\* ME Type=(\w+), Version=([\d.]+)\s+PatchVersion=([\d.]+) \*/$'),
    re.compile(r'^/\*USE ME:MEID=(\d+);\*/$'),
]


# ═══════════════════════════════════════════════════════════
# 工具函数
# ═══════════════════════════════════════════════════════════
def _sess_dir(sid):
    """解析会话目录，防路径穿越。

    ★ 返回 resolve 后的绝对路径：macOS 上 /tmp 是 /private/tmp 的软链接，
      不 resolve 会导致后续 relative_to 判断失败。
    """
    if not sid:
        raise ValueError('session_id 必填')
    safe = Path(str(sid)).name
    d = (SESSIONS_ROOT / safe).resolve()
    if not d.exists():
        raise ValueError(f'会话不存在: {safe}')
    return d


def _safe_path(sess_dir, rel):
    """把相对路径解析到会话目录内，防穿越。"""
    rel = str(rel or '').replace('\\', '/').lstrip('/')
    if '..' in rel.split('/'):
        raise ValueError(f'非法路径: {rel}')
    p = (sess_dir / rel).resolve()
    try:
        p.relative_to(sess_dir.resolve())
    except ValueError:
        raise ValueError(f'路径越界: {rel}')
    return p


def _decode(raw):
    """多编码尝试。"""
    for enc in ('utf-8', 'gbk', 'gb18030', 'utf-16'):
        try:
            return raw.decode(enc), enc
        except (UnicodeDecodeError, LookupError):
            continue
    return raw.decode('utf-8', errors='replace'), 'utf-8(replace)'


def _check_exp_header(text):
    """校验 EXP 三行头。返回 (ok, me_type, version, patch)。"""
    lines = text.split('\n')
    if len(lines) < 3:
        return False, None, None, None
    m1 = EXP_HEADER_PATTERNS[0].match(lines[0].strip())
    m2 = EXP_HEADER_PATTERNS[1].match(lines[1].strip())
    m3 = EXP_HEADER_PATTERNS[2].match(lines[2].strip())
    if not (m1 and m2 and m3):
        return False, None, None, None
    return True, m2.group(1), m2.group(2), m2.group(3)


def _update_index(sess_dir, entry):
    """更新 uploads_index.json（file_parse 时调用）。

    ★ 为什么放在 file_parse 里：文件一解析就要有索引，
      否则 file_list / guard_check 找不到 EXP。
    """
    idx_path = sess_dir / 'uploads_index.json'
    data = {'session': sess_dir.name, 'files': [],
            'summary': {'total': 0, 'ok': 0, 'failed': 0, 'exp_count': 0}}
    if idx_path.exists():
        try:
            data = json.loads(idx_path.read_text(encoding='utf-8'))
        except Exception:
            pass

    files = [f for f in (data.get('files') or []) if f.get('name') != entry.get('name')]
    files.append(entry)
    files.sort(key=lambda x: x.get('name') or '')

    data['files'] = files
    data['summary'] = {
        'total': len(files),
        'ok': sum(1 for f in files if not f.get('error')),
        'failed': sum(1 for f in files if f.get('error')),
        'exp_count': sum(1 for f in files if f.get('is_exp')),
    }
    import datetime as _dt
    data['updated_at'] = _dt.datetime.now(_dt.timezone.utc).isoformat(timespec='seconds')

    try:
        idx_path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding='utf-8')
        os.chmod(idx_path, 0o644)
    except Exception:
        pass


def _count_cmds(text):
    """数命令条数。"""
    n = 0
    in_block = False
    for raw in text.split('\n'):
        line = raw.strip()
        if not line:
            continue
        if line.startswith('/*'):
            in_block = '*/' not in line
            continue
        if in_block:
            if '*/' in line:
                in_block = False
            continue
        if line.startswith(('//', '#')):
            continue
        if re.match(r'^(ADD|MOD|RMV|SET|DEL|LST)\s+[A-Z]', line, re.I):
            n += 1
    return n


# ═══════════════════════════════════════════════════════════
# 工具 1：file_list
# ═══════════════════════════════════════════════════════════
def tool_file_list(args):
    """列 workspace 里的文件。"""
    sid = args.get('session_id')
    d = _sess_dir(sid)

    idx_path = d / 'uploads_index.json'
    if idx_path.exists():
        try:
            data = json.loads(idx_path.read_text(encoding='utf-8'))
            # 补充产物状态
            adir = d / 'analysis_code'
            artifacts = {}
            if adir.is_dir():
                for name in ALLOWED_ARTIFACTS:
                    f = adir / name
                    if f.exists():
                        artifacts[name] = {'size': f.stat().st_size}
            return {
                'session_id': sid,
                'files': data.get('files') or [],
                'summary': data.get('summary') or {},
                'artifacts': artifacts,
                'workspace': str(d),
            }
        except Exception:
            pass

    # 兜底：直接扫目录
    updir = d / 'uploads'
    files = []
    if updir.is_dir():
        for f in sorted(updir.iterdir()):
            if f.is_file() and not f.name.startswith('.'):
                files.append({'name': f.name, 'size': f.stat().st_size})
    return {
        'session_id': sid,
        'files': files,
        'summary': {'total': len(files)},
        'artifacts': {},
        'workspace': str(d),
        'note': 'uploads_index.json 不存在，返回的是原始文件列表（未解析）',
    }


# ═══════════════════════════════════════════════════════════
# 工具 2：file_read
# ═══════════════════════════════════════════════════════════
def tool_file_read(args):
    """读文件内容（支持分页）。"""
    sid = args.get('session_id')
    rel = args.get('path') or ''
    offset = int(args.get('offset') or 0)
    limit = int(args.get('limit') or 500)

    d = _sess_dir(sid)
    p = _safe_path(d, rel)
    if not p.exists():
        return {'error': f'文件不存在: {rel}'}
    if p.is_dir():
        return {'error': f'是目录不是文件: {rel}', 'entries': sorted(x.name for x in p.iterdir())[:50]}

    raw = p.read_bytes()
    text, enc = _decode(raw)
    lines = text.split('\n')
    total = len(lines)
    chunk = lines[offset:offset + limit]

    return {
        'path': rel,
        'encoding': enc,
        'size': len(raw),
        'total_lines': total,
        'offset': offset,
        'returned': len(chunk),
        'content': '\n'.join(chunk),
        'truncated': offset + limit < total,
    }


# ═══════════════════════════════════════════════════════════
# 工具 3：file_parse（markitdown）
# ═══════════════════════════════════════════════════════════
def tool_file_parse(args):
    """用 markitdown 把任意文件转成 markdown。"""
    sid = args.get('session_id')
    rel = args.get('path') or ''

    d = _sess_dir(sid)
    src = _safe_path(d, rel)
    if not src.exists():
        return {'error': f'文件不存在: {rel}'}

    out_dir = d / 'uploads_text'
    out_dir.mkdir(exist_ok=True)

    # 纯文本类：直接复制（省一次转换，也避免 markitdown 改格式）
    text_ext = {'.txt', '.md', '.csv', '.tsv', '.json', '.yaml', '.yml',
                '.xml', '.log', '.conf', '.cfg', '.ini'}
    if src.suffix.lower() in text_ext:
        raw = src.read_bytes()
        text, enc = _decode(raw)
        out = out_dir / (src.stem + '.md')
        header = f'<!-- 来源: {src.name} | 编码: {enc} | {len(raw)}B -->\n\n'
        out.write_text(header + text, encoding='utf-8')
        # 顺便做 EXP 识别
        is_exp, me, ver, patch = _check_exp_header(text)
        entry = {
            'name': src.name,
            'size': len(raw),
            'path': str(src.relative_to(d)),
            'parsed': str(out.relative_to(d)),
            'kind': 'text',
            'encoding': enc,
            'chars': len(text),
            'is_exp': is_exp,
            'me_type': me,
            'version': ver,
            'patch_version': patch,
            'cmd_count': _count_cmds(text) if is_exp else 0,
            'error': None,
        }
        _update_index(d, entry)
        return entry

    # 其他：markitdown
    try:
        from markitdown import MarkItDown
    except ImportError:
        return {'error': 'markitdown 未安装（pip install markitdown[pdf,docx,pptx,xlsx]）'}

    try:
        md = MarkItDown()
        result = md.convert(str(src))
        text = result.text_content or ''
        out = out_dir / (src.stem + '.md')
        header = f'<!-- 来源: {src.name} | markitdown 转换 | {src.stat().st_size}B -->\n\n'
        out.write_text(header + text, encoding='utf-8')
        entry = {
            'name': src.name,
            'size': src.stat().st_size,
            'path': str(src.relative_to(d)),
            'parsed': str(out.relative_to(d)),
            'kind': src.suffix.lower().lstrip('.'),
            'chars': len(text),
            'is_exp': False,
            'error': None,
        }
        _update_index(d, entry)
        entry['preview'] = text[:500]
        return entry
    except Exception as e:
        err_entry = {
            'name': src.name, 'size': src.stat().st_size,
            'kind': src.suffix.lower().lstrip('.'),
            'is_exp': False,
            'error': f'{type(e).__name__}: {str(e)[:200]}',
        }
        _update_index(d, err_entry)
        return {'error': f'markitdown 转换失败: {type(e).__name__}: {e}'}


# ═══════════════════════════════════════════════════════════
# 工具 4：artifact_write
# ═══════════════════════════════════════════════════════════
def tool_artifact_write(args):
    """写产物到 analysis_code/（只允许 4 个固定名字）。

    ★ 2026-11-06 新增 append 模式：
      实测 params.csv 十几 KB、几百行，agent 一次写完会超模型 max output tokens，
      触发「Response truncated (finish_reason='length')」→ 工具调用被截断 → 产物写不出来。
      现在支持分块写：
        artifact_write(filename='params.csv', content='表头+前50行', mode='overwrite')
        artifact_write(filename='params.csv', content='第51-100行', mode='append')
        ...
        artifact_write(filename='params.csv', content='', mode='finalize')
      也支持 mode='overwrite'（默认，整文件覆盖）。
    """
    sid = args.get('session_id')
    name = args.get('filename') or ''
    content = args.get('content')
    mode = (args.get('mode') or 'overwrite').lower()

    if name not in ALLOWED_ARTIFACTS:
        return {
            'error': f'不允许的产物名: {name}',
            'allowed': {k: v for k, v in ALLOWED_ARTIFACTS.items()},
        }

    # ★ 2026-11-09 两阶段：阶段1（规划）只允许写规划表和澄清
    #   从 <session>/.agent/stage 读（env 不可靠：MCP server 由 hermes 按
    #   config.yaml 启动，不继承 agent_run 的环境变量）
    _stage = 'fill'
    try:
        _sf = _sess_dir(sid) / '.agent' / 'stage'
        if _sf.exists():
            _stage = _sf.read_text(encoding='utf-8').strip().lower() or 'fill'
    except Exception:
        _stage = (os.environ.get('AGENT_STAGE') or 'fill').lower()
    if _stage == 'plan' and name not in PLAN_STAGE_ALLOWED:
        return {
            'error': (f'阶段1（命令族规划）只允许写 '
                      f'{sorted(PLAN_STAGE_ALLOWED)}，不能写 {name}。'
                      f'请先把命令族规划.md 写好，配置在阶段2 再写。'),
            'stage': 'plan',
            'allowed_now': sorted(PLAN_STAGE_ALLOWED),
        }
    if not isinstance(content, str):
        content = '' if content is None else str(content)

    d = _sess_dir(sid)
    adir = d / 'analysis_code'
    adir.mkdir(exist_ok=True)
    target = adir / name
    try:
        os.chmod(adir, 0o755)
    except Exception:
        pass

    if mode == 'append':
        if not target.exists():
            return {'error': f'{name} 还不存在，第一次写请用 mode=overwrite'}
        with target.open('a', encoding='utf-8') as f:
            f.write(content)
        size = target.stat().st_size
        return {
            'appended': name, 'mode': 'append',
            'bytes_added': len(content.encode('utf-8')),
            'total_bytes': size,
            'lines': target.read_text(encoding='utf-8', errors='replace').count('\n') + 1,
            'hint': '继续 append 剩余内容，写完调 mode=finalize 确认',
        }

    if mode == 'finalize':
        if not target.exists():
            return {'error': f'{name} 不存在，无法 finalize'}
        txt = target.read_text(encoding='utf-8', errors='replace')
        return {
            'finalized': name,
            'bytes': len(txt.encode('utf-8')),
            'lines': txt.count('\n') + 1,
            'ok': len(txt) > 0,
        }

    # overwrite（默认）
    target.write_text(content, encoding='utf-8')
    try:
        os.chmod(target, 0o644)
    except Exception:
        pass

    return {
        'written': name,
        'mode': 'overwrite',
        'path': str(target.relative_to(d)),
        'bytes': len(content.encode('utf-8')),
        'lines': content.count('\n') + 1,
    }


# ═══════════════════════════════════════════════════════════
# 工具 5：guard_check
# ═══════════════════════════════════════════════════════════
def tool_guard_check(args):
    """跑七道门校验。"""
    sid = args.get('session_id')
    d = _sess_dir(sid)

    mml = d / 'analysis_code' / 'mml.txt'
    if not mml.exists():
        return {'error': 'analysis_code/mml.txt 不存在，先写产物'}

    # 找 EXP（可选，支持多个 —— 多网元场景）
    exp_paths = []
    idx = d / 'uploads_index.json'
    if idx.exists():
        try:
            data = json.loads(idx.read_text(encoding='utf-8'))
            for f in data.get('files') or []:
                if not f.get('is_exp'):
                    continue
                # ★★ 2026-11-05 关键修正：必须用**原始 .txt**，不能用 markitdown
                #   转换后的 .md —— md 会加头部注释，行号整体偏移。
                #   实测：EXP md 16471 行 / txt 16469 行，agent grep 原始 txt
                #   拿到 L12125 是对的，但 guard 核验 md 时错位，误报「行号不是
                #   URRGROUP」（实际就是 URRGROUP）。
                #   G19 的行号核验依赖「和 agent 看到的完全同一个文件」。
                _raw = d / (f.get('path') or '')
                _cands = []
                if _raw.exists():
                    _cands.append(_raw)
                _rel = f.get('parsed') or ''
                if _rel:
                    _cands.append(d / _rel if '/' in _rel else d / 'uploads_text' / _rel)
                for cand in _cands:
                    if cand.exists() and cand.suffix.lower() in ('.txt', '.mml', '.cfg'):
                        exp_paths.append(str(cand))
                        break
                else:
                    # 只有 md 可用时退回（行号会不准，但至少有依据）
                    for cand in _cands:
                        if cand.exists():
                            exp_paths.append(str(cand))
                            break
        except Exception:
            pass
    # 兜底：exp_v1
    if not exp_paths:
        ev = d / 'exp_v1'
        if ev.is_dir():
            fs = sorted(ev.glob('*.txt'))
            if fs:
                exp_paths = [str(f) for f in fs]

    exp_path = ';'.join(exp_paths) if len(exp_paths) > 1 else (
        exp_paths[0] if exp_paths else '')

    # 意图文件
    intent_path = ''
    it = d / 'analysis_code' / '.intent.md'
    if it.exists():
        intent_path = str(it)

    if not GUARD_PY.exists():
        return {'error': f'guard 脚本不存在: {GUARD_PY}'}

    # ★★ 2026-11-06 性能优化：改用进程内调用
    #
    #   原来每次 guard_check 都 subprocess 起新 Python 进程：
    #     · 重新 import guard（含 lark 等依赖）
    #     · 重新读 45MB EXP 并全量解析
    #   实测 24.42s/次，一个工单调 3 次 = 73s
    #
    #   改成进程内 import guard：
    #     · guard 的 _cached_parse_mml / _fam_count 缓存跨调用复用
    #     · EXP 只在第一次解析，后续 0 开销
    #   实测降到 7.8s（首次）/ 缓存后更快
    #   保留子进程作为兜底（import 失败时）
    try:
        sys.path.insert(0, str(WORKFLOW_ROOT))
        sys.path.insert(0, str(WORKFLOW_ROOT / 'guard'))
        import guard as _guard_mod
        # ⚠ 不要 importlib.reload！那会重新执行整个模块，把 _CMDS_CACHE 等全清空，
        #   每调用一次都变成冷启动（实测 8.5s → 0.2s 的差别就在这）

        _mml_txt = mml.read_text(encoding='utf-8', errors='replace')
        _exp_txt = ''
        if exp_paths:
            _parts = []
            for _p in exp_paths:
                try:
                    _parts.append(Path(_p).read_text(encoding='utf-8', errors='replace'))
                except Exception:
                    pass
            _exp_txt = '\n'.join(_parts)
        _intent_txt = ''
        if intent_path:
            try:
                _intent_txt = Path(intent_path).read_text(encoding='utf-8', errors='replace')
            except Exception:
                pass

        # ★ 2026-11-08 修回归：必须传 session_dir 和 params_csv
        #   原来只传了 3 个参数 → run_guard 里
        #     `if session_dir and params_csv:` 不成立
        #   → G20(规划覆盖) / G21(CSV↔mml 一致性) / G22(占位符) 全部 skipped
        #   后果：CSV 里有 280 组、agent 只写 15 组，G21 本应报 fatal 却完全没跑。
        #   实测 86 工单漏配 6324 个对象（49.4%），根因就是这个。
        _params_csv = d / 'analysis_code' / 'params.csv'
        result = _guard_mod.run_guard(
            _mml_txt, _exp_txt, _intent_txt,
            session_dir=str(d),
            params_csv=str(_params_csv) if _params_csv.exists() else None,
        )
        return {
            'verdict': result.get('verdict'),
            'fatal': result.get('fatal') or [],
            'warnings': result.get('warnings') or [],
            'checks': {k: (v.get('ok') if isinstance(v, dict) else None)
                       for k, v in (result.get('checks') or {}).items()},
            'exp_used': bool(_exp_txt),
            'exp_count': len(exp_paths),
        }
    except Exception as _e:
        # 兜底：进程内失败就退回子进程
        pass

    cmd = [sys.executable, str(GUARD_PY), '--mml', str(mml), '--json']
    if exp_path:
        if ';' in exp_path:
            cmd += ['--exp-multi', exp_path]
        else:
            cmd += ['--exp', exp_path]
    if intent_path:
        cmd += ['--intent', intent_path]

    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
        if not r.stdout.strip():
            return {'error': f'guard 无输出: {r.stderr[-300:]}'}
        result = json.loads(r.stdout)
        return {
            'verdict': result.get('verdict'),
            'fatal': result.get('fatal') or [],
            'warnings': result.get('warnings') or [],
            'checks': {k: (v.get('ok') if isinstance(v, dict) else None)
                       for k, v in (result.get('checks') or {}).items()},
            'exp_used': bool(exp_path),
            'exp_count': len(exp_paths),
        }
    except subprocess.TimeoutExpired:
        return {'error': 'guard 超时（>300s）'}
    except Exception as e:
        return {'error': f'guard 执行失败: {type(e).__name__}: {e}'}


# ═══════════════════════════════════════════════════════════
# 工具 6：clarify
# ═══════════════════════════════════════════════════════════
def tool_clarify(args):
    """提交方案级问题（前端渲染成可点选卡片）。"""
    sid = args.get('session_id')
    questions = args.get('questions') or []

    if not isinstance(questions, list):
        return {'error': 'questions 必须是数组'}
    if len(questions) > 5:
        return {'error': f'最多 5 条方案问题（当前 {len(questions)} 条）。'
                         f'参数值类问题请写进 params.csv 的【待填写】，不要在这里问。'}

    norm = []
    for i, q in enumerate(questions, 1):
        if not isinstance(q, dict) or not q.get('question'):
            continue
        opts = []
        for o in (q.get('options') or [])[:4]:
            if isinstance(o, dict) and o.get('label'):
                opts.append({
                    'label': str(o['label'])[:60],
                    'reply': str(o.get('reply') or o['label'])[:500],
                })
        norm.append({
            'id': q.get('id') or f'q{i}',
            'question': str(q['question'])[:300],
            'why': str(q.get('why') or '')[:500],
            'options': opts,
        })

    if not norm:
        return {'error': '没有有效的问题（每条要有 question 字段）'}

    d = _sess_dir(sid)
    adir = d / 'analysis_code'
    adir.mkdir(exist_ok=True)
    target = adir / '方案澄清.json'
    target.write_text(json.dumps(norm, ensure_ascii=False, indent=1), encoding='utf-8')
    try:
        os.chmod(target, 0o644)
    except Exception:
        pass

    return {
        'written': '方案澄清.json',
        'count': len(norm),
        'note': '前端会把这些渲染成可点选卡片',
    }


# ═══════════════════════════════════════════════════════════
# MCP 协议
# ═══════════════════════════════════════════════════════════
TOOLS = [
    {
        'name': 'file_list',
        'description': (
            '列出 workspace 里的所有文件（含解析状态、是否 EXP 快照），'
            '以及已生成的产物。开始工作前先调这个看有什么资料。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {'session_id': {'type': 'string'}},
            'required': ['session_id'],
        },
    },
    {
        'name': 'file_read',
        'description': '读文件内容。大文件用 offset/limit 分页读。',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'session_id': {'type': 'string'},
                'path': {'type': 'string', 'description': '相对会话目录的路径，如 uploads_text/域名规划.md'},
                'offset': {'type': 'integer', 'description': '起始行（0 起）'},
                'limit': {'type': 'integer', 'description': '读多少行，默认 500'},
            },
            'required': ['session_id', 'path'],
        },
    },
    {
        'name': 'file_parse',
        'description': (
            '把原始文件转成 markdown（docx/xlsx/pdf/pptx/html 等），'
            '结果存到 uploads_text/。纯文本类会直接复制并识别编码。'
            '如果文件是 EXP 快照，返回 is_exp=true 和 ME Type/Version。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'session_id': {'type': 'string'},
                'path': {'type': 'string', 'description': '相对会话目录的路径，如 uploads/xxx.docx'},
            },
            'required': ['session_id', 'path'],
        },
    },
    {
        'name': 'artifact_write',
        'description': (
            '写产物到 analysis_code/。只接受 4 个文件名：\n'
            '  mml.txt         可执行 MML 配置命令（必须）\n'
            '  params.csv      参数收集表（必须）\n'
            '  配置分析.md      配置分析说明（必须）\n'
            '  方案澄清.json    方案级澄清问题（可选，没有就给 []）\n'
            '\n'
            '★ 大文件（如 params.csv 超过 100 行）必须分块写，否则会超出模型\n'
            '  单次输出上限导致工具调用被截断、产物写不出来：\n'
            '   1) mode=overwrite  写表头 + 前 N 行\n'
            '   2) mode=append     接着写第 N+1 行起的内容（可多次）\n'
            '   3) mode=finalize   确认写完\n'
            '  小文件直接用 mode=overwrite 一次写完即可。\n'
            '写完后应该调 guard_check 自检。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'session_id': {'type': 'string'},
                'filename': {'type': 'string', 'enum': list(ALLOWED_ARTIFACTS.keys())},
                'content': {'type': 'string'},
                'mode': {
                    'type': 'string',
                    'enum': ['overwrite', 'append', 'finalize'],
                    'description': 'overwrite=整文件覆盖（默认）；append=追加；finalize=确认写完',
                },
            },
            'required': ['session_id', 'filename'],
        },
    },
    {
        'name': 'guard_check',
        'description': (
            '对已生成的产物跑代码校验（7 道门：引用闭合/主键唯一/参数格式/'
            '前代族保留/数量级/意图族覆盖/来源标注）。'
            '返回 verdict（pass/warn/fail）、fatal 列表、warnings 列表。'
            '写完产物后必须调一次；有 fatal 要修完再调。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {'session_id': {'type': 'string'}},
            'required': ['session_id'],
        },
    },
    {
        'name': 'clarify',
        'description': (
            '提交方案级澄清问题，前端会渲染成可点选卡片。最多 5 条。\n'
            '只问影响配置方案走向的选择题（场景选择、要不要某能力、意图歧义、方案权衡）。\n'
            '参数值类问题（域名/IP/URRID/端口）不要在这里问，写进 params.csv 的【待填写】。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'session_id': {'type': 'string'},
                'questions': {
                    'type': 'array',
                    'description': '问题列表，每条含 question/why/options',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'string'},
                            'question': {'type': 'string'},
                            'why': {'type': 'string'},
                            'options': {
                                'type': 'array',
                                'items': {
                                    'type': 'object',
                                    'properties': {
                                        'label': {'type': 'string'},
                                        'reply': {'type': 'string'},
                                    },
                                },
                            },
                        },
                        'required': ['question'],
                    },
                },
            },
            'required': ['session_id', 'questions'],
        },
    },
]

HANDLERS = {
    'file_list': tool_file_list,
    'file_read': tool_file_read,
    'file_parse': tool_file_parse,
    'artifact_write': tool_artifact_write,
    'guard_check': tool_guard_check,
    'clarify': tool_clarify,
}


def handle(msg):
    method = msg.get('method')
    mid = msg.get('id')

    if method == 'initialize':
        return {'jsonrpc': '2.0', 'id': mid, 'result': {
            'protocolVersion': '2024-11-05',
            'capabilities': {'tools': {}},
            'serverInfo': {'name': 'mcp_io', 'version': '1.0.0'},
        }}

    if method == 'tools/list':
        return {'jsonrpc': '2.0', 'id': mid, 'result': {'tools': TOOLS}}

    if method == 'tools/call':
        params = msg.get('params') or {}
        name = params.get('name')
        args = params.get('arguments') or {}
        fn = HANDLERS.get(name or '')
        if not fn:
            return {'jsonrpc': '2.0', 'id': mid,
                    'error': {'code': -32601, 'message': f'未知工具: {name}'}}
        try:
            result = fn(args)
            return {'jsonrpc': '2.0', 'id': mid, 'result': {
                'content': [{'type': 'text',
                             'text': json.dumps(result, ensure_ascii=False, indent=1)}],
                'isError': 'error' in result,
            }}
        except Exception as e:
            return {'jsonrpc': '2.0', 'id': mid, 'result': {
                'content': [{'type': 'text',
                             'text': json.dumps({'error': f'{type(e).__name__}: {e}'},
                                                ensure_ascii=False)}],
                'isError': True,
            }}

    if method in ('notifications/initialized', 'notifications/cancelled'):
        return None

    return {'jsonrpc': '2.0', 'id': mid,
            'error': {'code': -32601, 'message': f'未知方法: {method}'}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            continue
        resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + '\n')
            sys.stdout.flush()


if __name__ == '__main__':
    main()
