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

from fastapi import FastAPI, HTTPException, Request, UploadFile, File, Form
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
def api_list_sessions():
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
            items.append(meta)
    return {'items': items, 'total': len(items)}


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
# 运行中的任务：sid -> asyncio.Task
_RUNNING: dict = {}


def _append_event(sid: str, ev: dict):
    d = sess_dir(sid)
    wf = d / '.agent'
    wf.mkdir(exist_ok=True)
    with (wf / 'events.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(ev, ensure_ascii=False) + '\n')


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

    # 清空上一轮产物与事件
    adir = d / 'analysis_code'
    adir.mkdir(exist_ok=True)
    for n in ALLOWED_ARTIFACTS:
        f = adir / n
        if f.exists():
            f.unlink()
    wf = d / '.agent'
    wf.mkdir(exist_ok=True)
    (wf / 'events.jsonl').write_text('', encoding='utf-8')

    append_chat(sid, 'user', intent)

    meta['status'] = 'running'
    meta['intent'] = intent
    save_meta(sid, meta)

    import agent_run

    def _worker():
        try:
            return agent_run.run_agent(sid, intent, product_hint=product)
        except Exception as e:
            return {'status': 'failed', 'error': f'{type(e).__name__}: {e}',
                    'rounds': [], 'produced': [],
                    'guard': {'verdict': None, 'fatal': [], 'warnings': []}}

    task = asyncio.create_task(asyncio.to_thread(_worker))
    _RUNNING[sid] = task

    def _done(t: asyncio.Task):
        try:
            res = t.result()
        except Exception as e:
            res = {'status': 'failed', 'error': str(e)}
        m = load_meta(sid)
        m['status'] = res.get('status') or 'failed'
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


@app.get('/api/v1/sessions/{sid}/events')
async def api_events(sid: str, follow: int = 1):
    """SSE 实时事件流。"""
    d = sess_dir(sid)
    evfile = d / '.agent' / 'events.jsonl'

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


# ═══════════════════════════════════════════════════════════
# 产物接口
# ═══════════════════════════════════════════════════════════
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
    return {'session_id': sid, 'artifacts': items}


@app.get('/api/v1/sessions/{sid}/artifacts/{name}')
def api_get_artifact(sid: str, name: str):
    if name not in ALLOWED_ARTIFACTS:
        raise HTTPException(400, f'不允许的产物名: {name}')
    d = sess_dir(sid)
    p = d / 'analysis_code' / name
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
    """发消息。有生成意图就走 run，否则只记对话。"""
    body = await request.json()
    text = (body.get('text') or body.get('question') or '').strip()
    if not text:
        raise HTTPException(400, 'text 必填')

    meta = load_meta(sid)
    if meta.get('status') == 'running':
        raise HTTPException(409, '正在生成中，请等这一轮结束')

    append_chat(sid, 'user', text)

    # 判定是否生成意图（复用 agent_run 的关键词逻辑）
    _GEN_WORDS = ('生成', '配置', '新增', '添加', '创建', '修改', '调整',
                  '删除', '去掉', '补充', '再配', '改成')
    is_gen = any(w in text for w in _GEN_WORDS)

    if is_gen:
        return {'action': 'run', 'session_id': sid,
                'hint': '已识别为生成任务，请调用 POST /run'}

    # 只记对话，返回历史
    return {'action': 'chat', 'session_id': sid,
            'messages': load_chat(sid)}


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
    return HTMLResponse(p.read_text(encoding='utf-8'))


# ═══════════════════════════════════════════════════════════
# 启动
# ═══════════════════════════════════════════════════════════
if __name__ == '__main__':
    import uvicorn
    SESSIONS_ROOT.mkdir(parents=True, exist_ok=True)
    uvicorn.run(app, host='0.0.0.0', port=PORT, log_level='info')
