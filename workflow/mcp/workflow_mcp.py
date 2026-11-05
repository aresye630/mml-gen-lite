#!/usr/bin/env python3
"""workflow_mcp.py — 把 workflow 封装成 MCP server。

★ 设计（用户裁决 2026-11-04）：
  agent 通过 MCP 工具调 workflow，中间过程通过对话交互。

★ 三个工具：
  workflow_generate(intent, action, parent_gen_id)  提交生成任务
  workflow_status(task_id)                           查进度（九步）
  workflow_result(gen_id)                            取产物

★ 传输：stdio（hermes 以子进程方式启动）

★ 关键：不阻塞。generate 立即返回 task_id，agent 可以继续对话；
  用户问进度时 agent 调 status。
"""
import json
import os
import sys
import time
import traceback
from pathlib import Path

# ═══ MCP 协议最小实现（stdio）═══
# 协议：JSON-RPC 2.0，每行一个 JSON 消息

SERVER_INFO = {'name': 'workflow', 'version': '1.0.0'}
PROTOCOL_VERSION = '2024-11-05'

TOOLS = [
    {
        'name': 'workflow_generate',
        'description': (
            '提交配置生成任务到九步 workflow 引擎。'
            '当用户要求生成/修改网络配置时调用。'
            '立即返回 task_id，任务在后台执行（约 5~15 分钟）。'
            '执行期间可以用 workflow_status 查进度。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'intent': {
                    'type': 'string',
                    'description': '本次要配置什么，用自然语言完整描述（含用户的所有要求）',
                },
                'action': {
                    'type': 'string',
                    'enum': ['fresh', 'revise', 'append'],
                    'description': 'fresh=首次生成；revise=基于前代改版；append=前代保留只追加',
                    'default': 'fresh',
                },
                'parent_gen_id': {
                    'type': 'string',
                    'description': '改版时的前代 gen_id（如 g1）；首次生成留空',
                },
                'session_id': {
                    'type': 'string',
                    'description': '当前会话 id（agent 从上下文取）',
                },
            },
            'required': ['intent', 'session_id'],
        },
    },
    {
        'name': 'workflow_status',
        'description': '查询生成任务的九步进度。用户问「进度如何」「到哪一步了」时调用。',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'task_id': {'type': 'string', 'description': 'workflow_generate 返回的 task_id'},
                'session_id': {'type': 'string'},
            },
            'required': ['task_id', 'session_id'],
        },
    },
    {
        'name': 'workflow_result',
        'description': '取生成结果的产物清单与摘要。任务完成后调用，向用户汇报。',
        'inputSchema': {
            'type': 'object',
            'properties': {
                'gen_id': {'type': 'string', 'description': '如 g1'},
                'session_id': {'type': 'string'},
            },
            'required': ['gen_id', 'session_id'],
        },
    },
]


def _sessions_root():
    return Path(os.environ.get('SESSIONS_DIR', '/data/sessions'))


def _call_api(method, path, body=None, timeout=60):
    """调后端 API（在容器内直接 HTTP）。"""
    import urllib.request
    base = os.environ.get('API_BASE', 'http://127.0.0.1:8600/api/v1')
    url = base + path
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        url, data=data, method=method,
        headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode() or '{}')


# ═══ 工具实现 ═══
def tool_generate(args):
    sid = args.get('session_id', '')
    intent = (args.get('intent') or '').strip()
    action = args.get('action') or 'fresh'
    parent = args.get('parent_gen_id') or None

    if not sid:
        return {'error': 'session_id 必填'}
    if not intent:
        return {'error': 'intent 必填'}
    if action in ('revise', 'append') and not parent:
        return {'error': '%s 模式需要 parent_gen_id' % action}

    try:
        body = {'action': action, 'intent_text': intent}
        if parent:
            body['parent_gen_id'] = parent
        resp = _call_api('POST', '/sessions/%s/generations' % sid, body, timeout=120)
        return {
            'ok': True,
            'task_id': resp.get('task_id'),
            'gen_id': resp.get('gen_id'),
            'action': action,
            'parent_gen_id': parent,
            'message': '任务已提交，九步流程在后台执行（约 5~15 分钟）。'
                       '用户可以继续对话，问「进度」时我会查。',
        }
    except Exception as e:
        return {'error': '%s: %s' % (type(e).__name__, str(e)[:200])}


def tool_status(args):
    sid = args.get('session_id', '')
    tid = args.get('task_id', '')
    if not sid or not tid:
        return {'error': 'session_id 和 task_id 必填'}

    try:
        t = _call_api('GET', '/tasks/%s' % tid)
        state = t.get('state')
        out = {'state': state}

        # 找 gen_id
        gid = (t.get('input') or {}).get('gen_id')
        if gid:
            out['gen_id'] = gid
            try:
                st = _call_api('GET', '/sessions/%s/generations/%s/steps' % (sid, gid))
                out['steps'] = [
                    {'title': s.get('title'), 'status': s.get('status'),
                     'summary': s.get('summary'), 'elapsed_s': s.get('elapsed_s')}
                    for s in (st.get('steps') or [])
                ]
                out['current'] = st.get('current')
                out['total_elapsed_s'] = st.get('total_elapsed_s')
            except Exception:
                pass

        if state == 'failed':
            out['error'] = str(t.get('error'))[:400]
        return out
    except Exception as e:
        return {'error': '%s: %s' % (type(e).__name__, str(e)[:200])}


def tool_result(args):
    sid = args.get('session_id', '')
    gid = args.get('gen_id', '')
    if not sid or not gid:
        return {'error': 'session_id 和 gen_id 必填'}

    try:
        d = _call_api('GET', '/sessions/%s/generations/%s' % (sid, gid))
        gdir = _sessions_root() / sid / 'gen_v1' / gid

        out = {
            'gen_id': gid,
            'status': d.get('status'),
            'engine': d.get('engine'),
            'produced': d.get('produced') or [],
        }

        # mml 摘要
        mml = gdir / 'mml.txt'
        if mml.exists():
            txt = mml.read_text(encoding='utf-8', errors='replace')
            n_cmd = len([l for l in txt.split('\n')
                         if l.strip() and not l.strip().startswith('//')])
            out['mml_summary'] = {'n_commands': n_cmd,
                                  'preview': txt[:600]}
        # 确认清单摘要
        ck = gdir / '确认清单.md'
        if ck.exists():
            out['checklist_preview'] = ck.read_text(
                encoding='utf-8', errors='replace')[:800]
        return out
    except Exception as e:
        return {'error': '%s: %s' % (type(e).__name__, str(e)[:200])}


HANDLERS = {
    'workflow_generate': tool_generate,
    'workflow_status': tool_status,
    'workflow_result': tool_result,
}


# ═══ JSON-RPC 处理 ═══
def handle(msg):
    method = msg.get('method')
    mid = msg.get('id')
    params = msg.get('params') or {}

    def ok(result):
        return {'jsonrpc': '2.0', 'id': mid, 'result': result}

    def err(code, message):
        return {'jsonrpc': '2.0', 'id': mid,
                'error': {'code': code, 'message': message}}

    if method == 'initialize':
        return ok({
            'protocolVersion': PROTOCOL_VERSION,
            'capabilities': {'tools': {}},
            'serverInfo': SERVER_INFO,
        })
    if method == 'notifications/initialized':
        return None
    if method == 'tools/list':
        return ok({'tools': TOOLS})
    if method == 'tools/call':
        name = params.get('name')
        args = params.get('arguments') or {}
        fn = HANDLERS.get(name)
        if not fn:
            return err(-32601, 'unknown tool: %s' % name)
        try:
            res = fn(args)
        except Exception as e:
            res = {'error': '%s: %s' % (type(e).__name__, str(e)[:200]),
                   'trace': traceback.format_exc()[-500:]}
        return ok({'content': [{'type': 'text',
                                'text': json.dumps(res, ensure_ascii=False)}],
                   'isError': bool(res.get('error'))})
    if method == 'ping':
        return ok({})

    return err(-32601, 'unknown method: %s' % method)


def main():
    """stdio 主循环。"""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception:
            continue
        try:
            resp = handle(msg)
        except Exception as e:
            resp = {'jsonrpc': '2.0', 'id': msg.get('id'),
                    'error': {'code': -32603, 'message': str(e)[:200]}}
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + '\n')
            sys.stdout.flush()


if __name__ == '__main__':
    main()
