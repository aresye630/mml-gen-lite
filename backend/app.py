#!/usr/bin/env python3
"""app.py — 极简后端（2026-11-05 彻底重写）。

★ 设计原则
  以模型为中心：agent 自主 loop，后端只负责
    · 文件上传与解析（markitdown）
    · 起 agent 进程、把 stdout 转成 SSE
    · 跑 guard、把错误回喂同一会话
    · 提供产物读写

★ 会话状态：idle / running / done / failed

★ 接口（5 类，共 11 个）
  会话   GET  /api/v1/sessions                        列表
         POST /api/v1/sessions                        新建
         GET  /api/v1/sessions/{sid}                  详情
         DELETE /api/v1/sessions/{sid}                删除
  文件   GET  /api/v1/sessions/{sid}/files             列表（左树）
         POST /api/v1/sessions/{sid}/files             上传
         GET  /api/v1/sessions/{sid}/file?path=        读文件
         DELETE /api/v1/sessions/{sid}/files/{name}    删除
  运行   POST /api/v1/sessions/{sid}/run               触发生成
         GET  /api/v1/sessions/{sid}/events            SSE 实时事件
         GET  /api/v1/sessions/{sid}/run               查运行状态
  产物   GET  /api/v1/sessions/{sid}/artifacts         产物列表
         GET  /api/v1/sessions/{sid}/artifacts/{name} 产物内容
  对话   GET  /api/v1/sessions/{sid}/chat              对话历史
         POST /api/v1/sessions/{sid}/chat             发消息（转发给 agent）

★ 环境变量
  EXP_SESSIONS_ROOT  会话根目录（默认 /data/sessions）
  WF_ROOT            workflow 代码目录（默认 /opt/expgv/workflow）
  PORT               端口（默认 8600）
"""
import asyncio
import datetime as dt
import json
import os
import re
import shutil
import sys
import time
import uuid
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form, Body
from fastapi.responses import HTMLResponse, JSONResponse, StreamingResponse

# ═══════════════════════════════════════════════════════════
# 配置
# ═══════════════════════════════════════════════════════════
SESSIONS_ROOT = Path(os.environ.get('EXP_SESSIONS_ROOT', '/data/sessions'))
WF_ROOT = Path(os.environ.get('WF_ROOT', '/opt/expgv/workflow'))
WEB_DIR = Path(__file__).parent / 'web'
PORT = int(os.environ.get('PORT', '8600'))

sys.path.insert(0, str(WF_ROOT))

ALLOWED_ARTIFACTS = ['mml.txt', 'params.csv', '配置分析.md', '方案澄清.json']

# 运行中的任务：sid -> asyncio.Task
#   ★ 2026-11-06：提前定义，会话列表接口要用它判断 running 是否为残留状态
_RUNNING: dict = {}

app = FastAPI(title='expgv', docs_url='/docs')


# ═══════════════════════════════════════════════════════════
# 会话存储（文件系统，无数据库）
# ═══════════════════════════════════════════════════════════
def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec='seconds')


def sess_dir(sid: str) -> Path:
    """会话目录（防穿越）。"""
    safe = Path(str(sid)).name
    if not safe or safe.startswith('.'):
        raise HTTPException(400, f'非法 session_id: {sid}')
    d = (SESSIONS_ROOT / safe).resolve()
    if not d.exists():
        raise HTTPException(404, f'会话不存在: {safe}')
    return d


def load_meta(sid: str) -> dict:
    """读会话元信息。"""
    d = sess_dir(sid)
    p = d / 'session.json'
    if p.exists():
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {'session_id': sid, 'created_at': _now(), 'status': 'idle',
            'product': '', 'name': sid}


def save_meta(sid: str, meta: dict):
    d = sess_dir(sid)
    meta = dict(meta)
    meta['updated_at'] = _now()
    (d / 'session.json').write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    try:
        os.chmod(d / 'session.json', 0o644)
    except Exception:
        pass


def load_index(sid: str) -> dict:
    d = sess_dir(sid)
    p = d / 'uploads_index.json'
    if p.exists():
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {'session': sid, 'files': [],
            'summary': {'total': 0, 'ok': 0, 'failed': 0, 'exp_count': 0}}


def load_chat(sid: str) -> list:
    d = sess_dir(sid)
    p = d / 'chat.json'
    if p.exists():
        try:
            return json.loads(p.read_text(encoding='utf-8'))
        except Exception:
            pass
    return []


def append_chat(sid: str, role: str, content: str, extra: Optional[dict] = None):
    msgs = load_chat(sid)
    m = {'role': role, 'content': content, 'ts': _now()}
    if extra:
        m.update(extra)
    msgs.append(m)
    (sess_dir(sid) / 'chat.json').write_text(
        json.dumps(msgs, ensure_ascii=False, indent=1), encoding='utf-8')


# ═══════════════════════════════════════════════════════════
# 会话接口
# ═══════════════════════════════════════════════════════════
@app.get('/api/v1/sessions')
def api_list_sessions(limit: int = 0):
    """会话列表，按创建时间倒序。

    ★ 2026-11-06：补 limit 参数（前端 boot() 会传 limit=1 取最近会话，
      原来被忽略导致返回全部）。
    """
    items = []
    if SESSIONS_ROOT.exists():
        for d in sorted(SESSIONS_ROOT.iterdir(), reverse=True):
            if not d.is_dir() or d.name.startswith(('_', '.')):
                continue
            meta: dict = {'session_id': d.name}
            sp = d / 'session.json'
            if sp.exists():
                try:
                    meta = json.loads(sp.read_text(encoding='utf-8'))
                except Exception:
                    pass
            # 补充文件数和产物数
            idx = d / 'uploads_index.json'
            if idx.exists():
                try:
                    meta['file_count'] = len(
                        json.loads(idx.read_text(encoding='utf-8')).get('files') or [])
                except Exception:
                    pass
            adir = d / 'analysis_code'
            if adir.is_dir():
                meta['artifact_count'] = sum(
                    1 for n in ALLOWED_ARTIFACTS if (adir / n).exists())
            # ★ 容器重启后残留的 running 状态要纠正（没有活进程就是 stale）
            if meta.get('status') == 'running' and d.name not in _RUNNING:
                meta['status'] = 'idle'
                meta['stale_running'] = True
            items.append(meta)
    total = len(items)
    if limit and limit > 0:
        items = items[:limit]
    return {'items': items, 'total': total}


@app.post('/api/v1/sessions')
async def api_create_session(name: str = Form(''), product: str = Form('')):
    sid = dt.datetime.now().strftime('%Y%m%d_%H%M%S_') + uuid.uuid4().hex[:4]
    d = SESSIONS_ROOT / sid
    for sub in ('uploads', 'uploads_text', 'analysis_code'):
        (d / sub).mkdir(parents=True, exist_ok=True)
    meta = {'session_id': sid, 'name': name or sid, 'product': (product or '').upper(),
            'status': 'idle', 'created_at': _now()}
    (d / 'session.json').write_text(
        json.dumps(meta, ensure_ascii=False, indent=1), encoding='utf-8')
    try:
        for p in [d, *d.rglob('*')]:
            os.chmod(p, 0o755 if p.is_dir() else 0o644)
    except Exception:
        pass
    return JSONResponse(meta, status_code=201)


@app.get('/api/v1/sessions/{sid}')
def api_get_session(sid: str):
    meta = load_meta(sid)
    idx = load_index(sid)
    meta['files'] = idx.get('files') or []
    meta['summary'] = idx.get('summary') or {}
    d = sess_dir(sid)
    adir = d / 'analysis_code'
    meta['artifacts'] = [
        {'name': n, 'size': (adir / n).stat().st_size}
        for n in ALLOWED_ARTIFACTS if (adir / n).exists()]
    return meta


@app.delete('/api/v1/sessions/{sid}')
def api_delete_session(sid: str):
    d = sess_dir(sid)
    shutil.rmtree(d, ignore_errors=True)
    return {'deleted': sid}


# ═══════════════════════════════════════════════════════════
# 文件接口
# ═══════════════════════════════════════════════════════════
@app.get('/api/v1/sessions/{sid}/files')
def api_list_files(sid: str):
    idx = load_index(sid)
    return {'session_id': sid,
            'files': idx.get('files') or [],
            'summary': idx.get('summary') or {}}


@app.post('/api/v1/sessions/{sid}/files')
async def api_upload_files(sid: str, files: list[UploadFile] = File(...)):
    """上传任意文件，自动解析（markitdown）。"""
    d = sess_dir(sid)
    updir = d / 'uploads'
    updir.mkdir(exist_ok=True)

    saved = []
    for f in files:
        if not f.filename:
            continue
        safe_name = Path(f.filename).name
        if not safe_name or safe_name.startswith('.'):
            continue
        target = updir / safe_name
        content = await f.read()
        target.write_bytes(content)
        try:
            os.chmod(target, 0o644)
        except Exception:
            pass
        saved.append(safe_name)

    # 解析（同步调 mcp_io 的实现，避免起 MCP 进程）
    results = []
    try:
        sys.path.insert(0, str(WF_ROOT / 'mcp'))
        import importlib
        import mcp_io as _io
        importlib.reload(_io)
        _io.SESSIONS_ROOT = SESSIONS_ROOT
        for name in saved:
            r = _io.tool_file_parse({'session_id': sid, 'path': f'uploads/{name}'})
            results.append(r)
    except Exception as e:
        return {'saved': saved, 'error': f'解析失败: {type(e).__name__}: {e}'}

    idx = load_index(sid)
    return {'saved': saved,
            'files': results,
            'summary': idx.get('summary')}


@app.get('/api/v1/sessions/{sid}/file')
def api_read_file(sid: str, path: str, offset: int = 0, limit: int = 500):
    """读会话目录内的文件（用于预览）。"""
    d = sess_dir(sid)
    rel = path.replace('\\', '/').lstrip('/')
    if '..' in rel.split('/'):
        raise HTTPException(400, '非法路径')
    p = (d / rel).resolve()
    try:
        p.relative_to(d)
    except ValueError:
        raise HTTPException(400, '路径越界')
    if not p.exists() or not p.is_file():
        raise HTTPException(404, f'文件不存在: {rel}')

    raw = p.read_bytes()
    text = None
    for enc in ('utf-8', 'gbk', 'gb18030'):
        try:
            text = raw.decode(enc)
            break
        except UnicodeDecodeError:
            continue
    if text is None:
        text = raw.decode('utf-8', errors='replace')

    lines = text.split('\n')
    total = len(lines)
    chunk = lines[offset:offset + limit]
    return {'path': rel, 'size': len(raw), 'total_lines': total,
            'offset': offset, 'returned': len(chunk),
            'content': '\n'.join(chunk),
            'truncated': offset + limit < total}


@app.delete('/api/v1/sessions/{sid}/files/{name}')
def api_delete_file(sid: str, name: str):
    d = sess_dir(sid)
    safe = Path(name).name
    removed = []
    for sub in ('uploads', 'uploads_text'):
        p = d / sub / safe
        if p.exists():
            p.unlink()
            removed.append(f'{sub}/{safe}')
    # 从索引删
    idx = load_index(sid)
    files = [f for f in (idx.get('files') or []) if f.get('name') != safe]
    idx['files'] = files
    idx['summary'] = {
        'total': len(files),
        'ok': sum(1 for f in files if not f.get('error')),
        'failed': sum(1 for f in files if f.get('error')),
        'exp_count': sum(1 for f in files if f.get('is_exp')),
    }
    (d / 'uploads_index.json').write_text(
        json.dumps(idx, ensure_ascii=False, indent=1), encoding='utf-8')
    return {'deleted': removed}


# ═══════════════════════════════════════════════════════════
# 运行接口（核心）
# ═══════════════════════════════════════════════════════════

def _append_event(sid: str, ev: dict):
    d = sess_dir(sid)
    wf = d / '.agent'
    wf.mkdir(exist_ok=True)
    # ★ 写到最新 run 目录（与 agent_run 一致）
    evf = _latest_events_file(d)
    evf.parent.mkdir(parents=True, exist_ok=True)
    with evf.open('a', encoding='utf-8') as f:
        f.write(json.dumps(ev, ensure_ascii=False) + '\n')


def _split_and_export_parts(adir: Path):
    """多网元产物自动拆分成 parts/（方案 C）。

    ★ 2026-11-05 用户裁定：
      agent 只写 mml.txt（带网元分段注释）+ params.csv（带网元列），
      后端机械拆分出 parts/{mml,params}_<网元>.{txt,csv}，给导入脚本直接用。
      这样产物约束不放松（仍只有 4 个固定名字），但导入侧零解析成本。
    """
    parts_dir = adir / 'parts'
    mml = adir / 'mml.txt'
    if not mml.exists():
        return []

    # 每次重新拆分前清空，避免残留旧文件（如网元名变了的旧 parts）
    if parts_dir.exists():
        shutil.rmtree(parts_dir, ignore_errors=True)

    txt = mml.read_text(encoding='utf-8', errors='replace')
    marks = list(re.finditer(
        r'/\*\s*={3,}\s*网元[:：]\s*([A-Za-z0-9_\-\u4e00-\u9fa5]+)', txt))

    # 没有网元分段 → 单网元，不拆
    if not marks:
        if parts_dir.exists():
            shutil.rmtree(parts_dir, ignore_errors=True)
        return []

    parts_dir.mkdir(exist_ok=True)
    units = []
    for i, m in enumerate(marks):
        start = m.start()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(txt)
        unit = m.group(1).strip()
        if unit in units:
            continue          # 同名网元只取第一段
        units.append(unit)
        seg = txt[start:end]
        safe = re.sub(r'[^A-Za-z0-9_\-]', '_', unit)
        (parts_dir / f'mml_{safe}.txt').write_text(seg, encoding='utf-8')

    # params.csv 按网元列拆
    csv = adir / 'params.csv'
    if csv.exists():
        import csv as _csv
        rows = []
        fieldnames = []
        try:
            with csv.open(encoding='utf-8-sig', newline='') as f:
                rd = _csv.DictReader(f)
                fieldnames = list(rd.fieldnames or [])
                rows = list(rd)
        except Exception:
            rows = []

        if '网元' in (fieldnames or []):
            by_unit = {}
            for r in rows:
                u = (r.get('网元') or '').strip().upper()
                # 跳过重复表头行、空行
                if not u or u == '网元':
                    continue
                # 「UDG/UNC」这种跨网元行 → 归到 ALL（两边都用）
                if '/' in u or '\\' in u or '、' in u:
                    u = 'ALL'
                by_unit.setdefault(u, []).append(r)
            for u, rs in by_unit.items():
                safe = re.sub(r'[^A-Za-z0-9_\-]', '_', u)
                with (parts_dir / f'params_{safe}.csv').open(
                        'w', encoding='utf-8', newline='') as f:
                    wr = _csv.DictWriter(f, fieldnames=fieldnames)
                    wr.writeheader()
                    wr.writerows(rs)
        else:
            # 没网元列：整体复制一份
            shutil.copy2(csv, parts_dir / 'params_ALL.csv')

    for p in parts_dir.iterdir():
        try:
            os.chmod(p, 0o644)
        except Exception:
            pass
    return units


def _summarize_artifacts(adir: Path) -> str:
    """给上一版产物做个摘要，让 agent 快速理解现状。"""
    lines = ['# 上一版产物摘要（本轮是二次意图，基于此修改）', '']
    mml = adir / 'mml.txt'
    if mml.exists():
        txt = mml.read_text(encoding='utf-8', errors='replace')
        cmds = [l for l in txt.split('\n') if l.strip().startswith(('ADD ', 'SET ', 'MOD ', 'RMV '))]
        fams = {}
        for c in cmds:
            m = re.match(r'^(\w+)\s+([A-Za-z0-9_]+)', c.strip())
            if m:
                k = f'{m.group(1)} {m.group(2)}'
                fams[k] = fams.get(k, 0) + 1
        lines.append(f'## mml.txt（{len(cmds)} 条命令，{len(fams)} 个族）')
        for k, v in sorted(fams.items(), key=lambda x: -x[1]):
            lines.append(f'  - {k}: {v} 条')
        lines.append('')
        lines.append('前 30 行：')
        lines.append('```')
        lines.extend(txt.split('\n')[:30])
        lines.append('```')
    for name in ('params.csv', '配置分析.md', '方案澄清.json'):
        f = adir / name
        if f.exists():
            lines.append('')
            lines.append(f'## {name}（{f.stat().st_size} 字节）')
            if name == '方案澄清.json':
                lines.append(f.read_text(encoding='utf-8', errors='replace')[:500])
    return '\n'.join(lines)


@app.post('/api/v1/sessions/{sid}/run')
async def api_run(sid: str, request: Request):
    """触发生成。body: {intent, product?}"""
    d = sess_dir(sid)
    meta = load_meta(sid)
    if meta.get('status') == 'running':
        raise HTTPException(409, '上一轮还在跑')

    body = await request.json()
    intent = (body.get('intent') or '').strip()
    if not intent:
        raise HTTPException(400, 'intent 必填')

    product = body.get('product') or meta.get('product') or ''

    # ★ 2026-11-05：区分首次生成 vs 二次意图
    #   fresh  = 全新生成，清空产物
    #   revise = 基于上一版改，**保留产物**（agent 要看到上一版才知道怎么改）
    #   append = 保留上一版，只追加新内容
    action = (body.get('action') or 'auto').lower()
    adir = d / 'analysis_code'
    adir.mkdir(exist_ok=True)

    has_prev = bool(list(adir.glob('mml.txt')))
    if action == 'auto':
        action = 'revise' if has_prev else 'fresh'

    if action == 'fresh':
        for n in ALLOWED_ARTIFACTS:
            f = adir / n
            if f.exists():
                f.unlink()
    # revise / append：产物原样保留，agent 读得到

    # 事件流每轮重置（这是本轮的过程记录，不是产物）
    wf = d / '.agent'
    wf.mkdir(exist_ok=True)
    # 清空最新 run 的 events（agent_run 会新建 runN 目录，这里清的是上一个）
    _prev = _latest_events_file(d)
    _prev.parent.mkdir(parents=True, exist_ok=True)
    _prev.write_text('', encoding='utf-8')

    # 二次意图：把上一版产物摘要写进 .agent/prev_summary.md，供 agent 参考
    if action in ('revise', 'append') and has_prev:
        try:
            _prev = _summarize_artifacts(adir)
            (wf / 'prev_summary.md').write_text(_prev, encoding='utf-8')
        except Exception:
            pass

    append_chat(sid, 'user', intent)

    meta['status'] = 'running'
    meta['intent'] = intent
    meta['action'] = action
    save_meta(sid, meta)

    import agent_run

    # 二次意图：接着上一轮的 agent 会话（meta 里存着）
    _prev_agent = meta.get('agent_session') if action in ('revise', 'append') else None

    def _worker():
        try:
            return agent_run.run_agent(sid, intent, product_hint=product,
                                       resume_agent_session=_prev_agent)
        except Exception as e:
            # ★ 2026-11-06：把完整 traceback 写进日志，只报 'dict' not callable 查不出位置
            import traceback
            tb = traceback.format_exc()
            try:
                (d / '.agent').mkdir(parents=True, exist_ok=True)
                (d / '.agent' / 'worker_error.log').write_text(tb, encoding='utf-8')
            except Exception:
                pass
            print(f'[worker_error] {tb}', flush=True)
            return {'status': 'failed', 'error': f'{type(e).__name__}: {e}',
                    'rounds': [], 'produced': [],
                    'guard': {'verdict': None, 'fatal': [], 'warnings': []}}

    task = asyncio.create_task(asyncio.to_thread(_worker))
    _RUNNING[sid] = task

    def _done(t: asyncio.Task):
        try:
            res = t.result()
        except Exception as e:
            # ★ 2026-11-06：带上完整 traceback，否则只能看到一句
            #   "TypeError: 'dict' object is not callable" 不知道在哪
            import traceback
            tb = traceback.format_exc()
            print(f'[agent_run failed] {tb}', flush=True)
            try:
                (d / '.agent' / 'error.log').write_text(tb, encoding='utf-8')
            except Exception:
                pass
            res = {'status': 'failed',
                   'error': f'{type(e).__name__}: {e}',
                   'traceback': tb[-3000:]}
        m = load_meta(sid)
        m['status'] = res.get('status') or 'failed'
        if res.get('agent_session'):
            m['agent_session'] = res.get('agent_session')

        # ★ 多网元：自动拆出 parts/（导入侧零解析）
        try:
            units = _split_and_export_parts(d / 'analysis_code')
            if units:
                m['units'] = units
        except Exception as e:
            m['parts_error'] = f'{type(e).__name__}: {e}'

        m['last_run'] = {
            'elapsed': res.get('elapsed'),
            'rounds': res.get('rounds'),
            'guard': res.get('guard'),
            'error': res.get('error'),
            'agent_session': res.get('agent_session'),
            'finished_at': _now(),
        }
        save_meta(sid, m)
        # 对话里补一条 agent 回复
        if res.get('status') == 'done':
            produced = [p.get('name', '') for p in (res.get('produced') or [])]
            append_chat(sid, 'assistant',
                        f"已完成。产物：{', '.join(produced) or '（无）'}")
        else:
            append_chat(sid, 'assistant',
                        f"失败：{res.get('error') or '未知原因'}",
                        {'failed': True})
        _RUNNING.pop(sid, None)

    task.add_done_callback(_done)

    return {'session_id': sid, 'status': 'running', 'started_at': _now()}


@app.get('/api/v1/sessions/{sid}/run')
def api_run_status(sid: str):
    meta = load_meta(sid)
    return {'session_id': sid,
            'status': meta.get('status'),
            'intent': meta.get('intent'),
            'last_run': meta.get('last_run')}


def _latest_events_file(d: Path) -> Path:
    """定位最新一次 run 的 events.jsonl。

    ★ 2026-11-06：每次 run 写 .agent/runN/events.jsonl（避免多轮对话覆盖）。
      兼容旧布局 .agent/events.jsonl。
    """
    wf = d / '.agent'
    runs = sorted([p for p in wf.iterdir()
                   if p.is_dir() and p.name.startswith('run')],
                  key=lambda p: int(re.sub(r'\D', '', p.name) or 0))
    if runs:
        return runs[-1] / 'events.jsonl'
    return wf / 'events.jsonl'


@app.get('/api/v1/sessions/{sid}/events')
async def api_events(sid: str, follow: int = 1):
    """SSE 实时事件流。"""
    d = sess_dir(sid)
    evfile = _latest_events_file(d)

    async def gen():
        yield 'event: open\ndata: {"sid":"%s"}\n\n' % sid
        pos = 0
        idle = 0.0
        closed = False

        while True:
            try:
                if evfile.exists():
                    with evfile.open('r', encoding='utf-8', errors='replace') as f:
                        f.seek(pos)
                        chunk = f.read()
                        pos = f.tell()
                    for ln in chunk.splitlines():
                        ln = ln.strip()
                        if ln:
                            yield 'data: ' + ln + '\n\n'
            except Exception:
                pass

            if not closed:
                meta = load_meta(sid)
                if meta.get('status') in ('done', 'failed', 'idle'):
                    # 发完剩余事件再关
                    await asyncio.sleep(0.3)
                    try:
                        if evfile.exists():
                            with evfile.open('r', encoding='utf-8', errors='replace') as f:
                                f.seek(pos)
                                rest = f.read()
                            for ln in rest.splitlines():
                                if ln.strip():
                                    yield 'data: ' + ln.strip() + '\n\n'
                    except Exception:
                        pass
                    yield ('event: done\ndata: ' +
                           json.dumps({'status': meta.get('status'),
                                       'last_run': meta.get('last_run')},
                                      ensure_ascii=False) + '\n\n')
                    closed = True
                    break

            if not follow and pos > 0:
                break

            await asyncio.sleep(0.4)
            idle += 0.4
            if idle > 3600:      # 1 小时硬上限
                yield 'event: timeout\ndata: {}\n\n'
                break

    return StreamingResponse(gen(), media_type='text/event-stream', headers={
        'Cache-Control': 'no-cache',
        'X-Accel-Buffering': 'no',
        'Connection': 'keep-alive',
    })


@app.get('/api/v1/sessions/{sid}/placeholders')
def api_list_placeholders(sid: str):
    """列 params.csv 里还没填的占位符（值仍是【XXX】的）。

    ★ 2026-11-05 用户裁定：
      用户下载 csv → 填 → 上传 → 系统按占位符统一替换 → 重新生成 mml。
      这个接口告诉前端「还有几项没填」，没填完的 mml 不能直接下发。
    """
    d = sess_dir(sid)
    csv_path = d / 'analysis_code' / 'params.csv'
    if not csv_path.exists():
        raise HTTPException(404, 'params.csv 不存在')

    try:
        sys.path.insert(0, str(WF_ROOT))
        import importlib
        import mml_gen as _mg
        importlib.reload(_mg)
        unfilled = _mg.list_unfilled(str(csv_path))
        rows = _mg.read_params(str(csv_path))
        g22 = _mg.check_placeholders(rows)
    except Exception as e:
        raise HTTPException(500, f'{type(e).__name__}: {e}')

    # 组装「待填项」列表（按占位符聚合）
    items = []
    for name, occ in unfilled.items():
        items.append({
            'placeholder': f'【{name}】',
            'name': name,
            'count': len(occ),
            'groups': sorted({o['group'] for o in occ}),
            'params': [f"{o['group']}.{o['param']}" for o in occ],
            'note': next((o.get('note') for o in occ if o.get('note')), ''),
        })

    return {
        'session_id': sid,
        'n_unfilled': len(items),
        'all_filled': len(items) == 0,
        'items': items,
        'n_placeholders_total': g22.get('n_placeholders', 0),
        'consistency_errors': g22.get('errors') or [],
        'message': ('全部已填，mml 可执行' if not items
                    else f'还有 {len(items)} 项占位符未填，mml 暂不可执行'),
    }


@app.post('/api/v1/sessions/{sid}/regenerate')
async def api_regenerate(sid: str):
    """从 params.csv 重新生成 mml.txt（纯代码，秒级，不调 agent）。

    ★ 2026-11-05 用户裁定：
      params.csv 是单一数据源。用户改完 csv 后调这个接口，
      直接把 mml.txt 重写出来，不用重跑 agent（省时间也保证一致）。
    """
    d = sess_dir(sid)
    adir = d / 'analysis_code'
    csv_path = adir / 'params.csv'
    if not csv_path.exists():
        raise HTTPException(400, 'params.csv 不存在')

    try:
        sys.path.insert(0, str(WF_ROOT))
        import importlib
        import mml_gen as _mg
        importlib.reload(_mg)
        r = _mg.gen_mml(str(csv_path))
    except Exception as e:
        raise HTTPException(500, f'生成失败: {type(e).__name__}: {e}')

    if r.get('errors'):
        raise HTTPException(422, f"csv 有问题: {r['errors'][:3]}")

    # 备份旧 mml（用户可能要回退）
    mml_path = adir / 'mml.txt'
    if mml_path.exists():
        try:
            (adir / 'mml.txt.prev').write_text(
                mml_path.read_text(encoding='utf-8', errors='replace'),
                encoding='utf-8')
        except Exception:
            pass

    mml_path.write_text(r['text'], encoding='utf-8')
    try:
        os.chmod(mml_path, 0o644)
    except Exception:
        pass

    # 重新拆 parts/
    units = []
    try:
        units = _split_and_export_parts(adir)
    except Exception:
        pass

    # 跑一次 guard 看结果
    guard_result = None
    try:
        import agent_run as _ar
        importlib.reload(_ar)
        _exp_paths = []
        idx = d / 'uploads_index.json'
        if idx.exists():
            data = json.loads(idx.read_text(encoding='utf-8'))
            for f in data.get('files') or []:
                if not f.get('is_exp'):
                    continue
                # ★ 必须用原始 txt（md 行号会偏移，G19 会全部误报）
                _raw = d / (f.get('path') or '')
                if _raw.exists():
                    _exp_paths.append(str(_raw))
                    continue
                _rel = f.get('parsed') or ''
                if _rel:
                    _c = d / _rel if '/' in _rel else d / 'uploads_text' / _rel
                    if _c.exists():
                        _exp_paths.append(str(_c))
        _exp = ';'.join(_exp_paths)
        intent_file = adir / '.intent.md'
        g = _ar.run_guard(d, _exp,
                          str(intent_file) if intent_file.exists() else '')
        guard_result = {'verdict': g.get('verdict'),
                        'fatal': g.get('fatal') or [],
                        'warnings': (g.get('warnings') or [])[:5]}
    except Exception as e:
        guard_result = {'error': f'{type(e).__name__}: {e}'}

    # 检查还有没有未填占位符
    unfilled_count = 0
    try:
        importlib.reload(_mg)
        unfilled_count = len(_mg.list_unfilled(str(csv_path)))
    except Exception:
        pass

    return {
        'session_id': sid,
        'regenerated': True,
        'n_commands': r['n_commands'],
        'n_groups': r['n_groups'],
        'units': units,
        'size': mml_path.stat().st_size,
        'n_unfilled_placeholders': unfilled_count,
        'executable': unfilled_count == 0,
        'message': ('mml 可直接下发' if unfilled_count == 0
                    else f'还有 {unfilled_count} 项占位符未填，mml 暂不可下发'),
        'guard': guard_result,
    }


# ═══════════════════════════════════════════════════════════
# 产物接口
# ═══════════════════════════════════════════════════════════
@app.post('/api/v1/sessions/{sid}/expand')
async def api_expand(sid: str, payload: dict = Body(...)):
    """模板批量展开：产物 params.csv（模板）+ 用户 CSV（实例清单） → 完整 params.csv。

    ★ 2026-11-08 新增
    背景：大工单本质是「一套模板 × N 个业务对象」。
         agent 只写模板，代码按用户 CSV 展开实例。

    payload:
      user_csv:      用户 CSV 文本（业务清单，不含命令族）
      write:         是否写回 analysis_code/params.csv（默认 false，只预演）
      regenerate:    展开后是否自动重新生成 mml（默认 false）

    产物 params.csv 的约定：
      · 组名带 #T 后缀 → 模板组
      · 值列写 ${CSV.列名} 或 ${CSV.列名}|算子链 或 ${SCRIPT.列名} 表达式
      · 「实例化」列指定粒度：object / item / dedup:列名
    """
    d = sess_dir(sid)
    adir = d / 'analysis_code'
    prod_csv = adir / 'params.csv'
    if not prod_csv.exists():
        raise HTTPException(400, '产物 params.csv 不存在，先生成方案')

    user_csv = payload.get('user_csv') or ''
    if not user_csv.strip():
        raise HTTPException(400, '缺少 user_csv')

    do_write = bool(payload.get('write'))
    do_regen = bool(payload.get('regenerate'))

    try:
        sys.path.insert(0, str(WF_ROOT))
        import importlib
        import expander as _ex
        import derivation as _dv
        import safe_expr as _se
        # 热重载：开发期改代码后不用重启服务
        for _m in (_se, _dv, _ex):
            importlib.reload(_m)
        r = _ex.expand(prod_csv.read_text(encoding='utf-8'), user_csv)
    except Exception as e:
        raise HTTPException(500, f'展开失败: {type(e).__name__}: {e}')

    resp = {
        'session_id': sid,
        'stats': r.get('stats') or {},
        'errors': r.get('errors') or [],
        'failed_rows': r.get('failed_rows') or [],
        'n_failed_rows': r.get('n_failed_rows', 0),
        'preview': (r.get('csv_text') or '')[:4000],
        'written': False,
        'regenerated': False,
    }

    if do_write:
        # 备份原模板
        bak = adir / 'params.template.csv'
        try:
            bak.write_text(prod_csv.read_text(encoding='utf-8'), encoding='utf-8')
            resp['template_backup'] = bak.name
        except Exception:
            pass
        prod_csv.write_text(r.get('csv_text') or '', encoding='utf-8')
        resp['written'] = True

        if do_regen:
            try:
                import mml_gen as _mg
                importlib.reload(_mg)
                g = _mg.gen_mml(str(prod_csv))
                if g.get('errors'):
                    resp['regen_errors'] = g['errors'][:5]
                else:
                    (adir / 'mml.txt').write_text(g['text'], encoding='utf-8')
                    resp['regenerated'] = True
                    resp['n_commands'] = g.get('n_commands')
            except Exception as e:
                resp['regen_errors'] = [f'{type(e).__name__}: {e}']

    return resp


@app.post('/api/v1/sessions/{sid}/expand/rollback')
async def api_expand_rollback(sid: str):
    """回滚展开：把 params.template.csv 还原成 params.csv。"""
    d = sess_dir(sid)
    adir = d / 'analysis_code'
    bak = adir / 'params.template.csv'
    if not bak.exists():
        raise HTTPException(400, '没有可回滚的模板备份')
    (adir / 'params.csv').write_text(bak.read_text(encoding='utf-8'), encoding='utf-8')
    return {'session_id': sid, 'rolled_back': True}


@app.get('/api/v1/sessions/{sid}/artifacts')
def api_list_artifacts(sid: str):
    d = sess_dir(sid)
    adir = d / 'analysis_code'
    items = []
    for n in ALLOWED_ARTIFACTS:
        p = adir / n
        if p.exists():
            items.append({'name': n, 'size': p.stat().st_size,
                          'mtime': dt.datetime.fromtimestamp(
                              p.stat().st_mtime).isoformat(timespec='seconds')})

    # 多网元拆分产物（parts/）
    parts_dir = adir / 'parts'
    if parts_dir.is_dir():
        for p in sorted(parts_dir.iterdir()):
            if p.is_file():
                items.append({'name': f'parts/{p.name}',
                              'size': p.stat().st_size,
                              'mtime': dt.datetime.fromtimestamp(
                                  p.stat().st_mtime).isoformat(timespec='seconds'),
                              'parts': True})

    return {'session_id': sid, 'artifacts': items}


@app.get('/api/v1/sessions/{sid}/artifacts/{name:path}')
def api_get_artifact(sid: str, name: str):
    d = sess_dir(sid)
    adir = d / 'analysis_code'

    # parts/ 下的拆分产物
    if name.startswith('parts/'):
        p = (adir / name).resolve()
        try:
            p.relative_to(adir.resolve())
        except ValueError:
            raise HTTPException(400, '非法路径')
        if not p.exists() or not p.is_file():
            raise HTTPException(404, f'产物不存在: {name}')
        text = p.read_text(encoding='utf-8', errors='replace')
        return {'name': name, 'size': p.stat().st_size, 'content': text}

    if name not in ALLOWED_ARTIFACTS:
        raise HTTPException(400, f'不允许的产物名: {name}')
    p = adir / name
    if not p.exists():
        raise HTTPException(404, f'产物不存在: {name}')
    text = p.read_text(encoding='utf-8', errors='replace')
    return {'name': name, 'size': p.stat().st_size, 'content': text}


# ═══════════════════════════════════════════════════════════
# 对话接口
# ═══════════════════════════════════════════════════════════
@app.get('/api/v1/sessions/{sid}/chat')
def api_chat_history(sid: str):
    return {'session_id': sid, 'messages': load_chat(sid)}


@app.post('/api/v1/sessions/{sid}/chat')
async def api_chat(sid: str, request: Request):
    """发消息。

    ★ 2026-11-05 设计纠正（用户裁定：分流交 agent，禁前端/后端分类层）：
      这里**不做意图判断**。原先用关键词（"配置"/"新增"…）猜是不是生成请求，
      实测「这个配置有多少条命令？」被误判成生成任务。

      正确做法：前端对话统一走这里 → 后端原样记下来 → **由 agent 自己决定**
      是回答问题还是写产物。agent 拿到 MCP 工具，它自己知道该调什么。
    """
    body = await request.json()
    text = (body.get('text') or body.get('question') or '').strip()
    if not text:
        raise HTTPException(400, 'text 必填')

    meta = load_meta(sid)
    if meta.get('status') == 'running':
        raise HTTPException(409, '正在生成中，请等这一轮结束')

    append_chat(sid, 'user', text)
    return {'session_id': sid, 'accepted': True,
            'messages': load_chat(sid),
            'hint': '已记录。要触发 agent 处理请调 POST /run（把 text 作为 intent）'}


# ═══════════════════════════════════════════════════════════
# 健康检查 + 前端
# ═══════════════════════════════════════════════════════════
@app.get('/health')
def health():
    return {'ok': True, 'sessions_root': str(SESSIONS_ROOT),
            'wf_root': str(WF_ROOT), 'running': list(_RUNNING.keys())}


@app.get('/', response_class=HTMLResponse)
def index():
    p = WEB_DIR / 'app_v3.html'
    if not p.exists():
        return HTMLResponse('<h1>前端未部署</h1>', status_code=404)
    html = p.read_text(encoding='utf-8')
    # ★ 2026-11-06：加 no-cache 头。实测用户浏览器缓存了旧版页面，
    #   看到的是「输入框看不见 / 产物大小 NaN」等已修好的老问题。
    return HTMLResponse(html, headers={
        'Cache-Control': 'no-cache, no-store, must-revalidate',
        'Pragma': 'no-cache',
        'Expires': '0',
    })


# ═══════════════════════════════════════════════════════════
# 启动
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    import uvicorn
    SESSIONS_ROOT.mkdir(parents=True, exist_ok=True)
    uvicorn.run(app, host='0.0.0.0', port=PORT, log_level='info')
