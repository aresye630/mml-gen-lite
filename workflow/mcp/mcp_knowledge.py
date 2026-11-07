#!/usr/bin/env python3
"""mcp_knowledge.py — 知识库检索 MCP server。

★ 3 个工具
  kb_search_feature  查特性文档（语义 / 精确名）
  kb_search_command  查 MML 命令（参数表 / 使用实例）
  kb_get_naming      查某族的命名规律（从 EXP 统计，需传 exp_path）

★ 设计原则
  · 内部复用现有 skills/*/scripts/*_query.py 的检索能力（不重写向量检索）
  · 对外返回结构化 JSON（不是人类可读文本），方便 agent 直接消费
  · 知识源独立：加新 collection 只改这个 server

★ 环境变量
  MML_MILVUS_DIR   向量库路径（容器内 /opt/expgv/milvus-seed/milvus_mml.db）
  MML_FEATURE_SCRIPT / MML_SUPPORT_SCRIPT   检索脚本路径（可覆盖）
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

WORKFLOW_ROOT = Path(os.environ.get('WF_ROOT', '/opt/expgv/workflow'))
SKILLS_ROOT = WORKFLOW_ROOT / 'skills'

FEATURE_SCRIPT = os.environ.get(
    'MML_FEATURE_SCRIPT',
    str(SKILLS_ROOT / 'mml_feature' / 'scripts' / 'mml_feature_query.py'))
SUPPORT_SCRIPT = os.environ.get(
    'MML_SUPPORT_SCRIPT',
    str(SKILLS_ROOT / 'mml_support' / 'scripts' / 'mml_support_query.py'))

DEFAULT_PRODUCT = os.environ.get('MML_DEFAULT_PRODUCT', 'UDG')


# ═══════════════════════════════════════════════════════════
# 调用检索脚本
# ═══════════════════════════════════════════════════════════
def _run_script(script, mode, query, product, top_k=5, timeout=120):
    """调检索脚本，返回 stdout 文本。

    ★ 必须显式传 --product：两个脚本的 argparse 默认值是 UEG，
      不传会拿到别的产品的文档（实测：查 UDG 内容计费，前 3 条全是 UEG/UNC 的）。
    """
    if not Path(script).exists():
        return None, f'检索脚本不存在: {script}'

    cmd = [sys.executable, script, mode, query,
           '--product', product or DEFAULT_PRODUCT]
    if mode == 'semantic':
        cmd += ['--top_k', str(top_k)]

    env = dict(os.environ)
    env.setdefault('TQDM_DISABLE', '1')
    env.setdefault('TOKENIZERS_PARALLELISM', 'false')
    env.setdefault('OMP_NUM_THREADS', '1')

    try:
        r = subprocess.run(cmd, capture_output=True, text=True,
                           timeout=timeout, env=env, cwd=str(Path(script).parent))
        if r.returncode != 0:
            return None, f'脚本退出码 {r.returncode}: {(r.stderr or "")[-300:]}'
        return r.stdout, None
    except subprocess.TimeoutExpired:
        return None, f'检索超时（>{timeout}s）'
    except Exception as e:
        return None, f'{type(e).__name__}: {e}'


# ═══════════════════════════════════════════════════════════
# 工具 1：kb_search_feature
# ═══════════════════════════════════════════════════════════
# ★ 2026-11-06 性能优化：知识库检索结果缓存
#
#   实测：单次 kb_search_command 1.4s（向量检索 + 文档读取）
#        agent 一单会调 14 次 KB，同样的问题反复查
#        同一查询重复 3 次都是 1.4s —— 没有任何缓存
#   加缓存后重复查询 0.00s
_KB_CACHE = {}
_KB_CACHE_MAX = 200


def _kb_cached(fn):
    """给 kb 工具加结果缓存（按函数名 + 参数指纹）。"""
    import functools
    import hashlib

    @functools.wraps(fn)
    def wrapper(args):
        try:
            key = (fn.__name__,
                   hashlib.md5(json.dumps(args, sort_keys=True,
                                          ensure_ascii=False).encode()).hexdigest())
        except Exception:
            return fn(args)
        if key in _KB_CACHE:
            return _KB_CACHE[key]
        val = fn(args)
        if len(_KB_CACHE) >= _KB_CACHE_MAX:
            _KB_CACHE.pop(next(iter(_KB_CACHE)))
        _KB_CACHE[key] = val
        return val
    return wrapper


@_kb_cached
def tool_kb_search_feature(args):
    """查特性文档。"""
    query = (args.get('query') or '').strip()
    product = (args.get('product') or DEFAULT_PRODUCT).upper()
    top_k = int(args.get('top_k') or 5)
    mode = args.get('mode') or 'semantic'

    if not query:
        return {'error': 'query 必填'}

    if mode not in ('semantic', 'feature_name'):
        mode = 'semantic'

    out, err = _run_script(FEATURE_SCRIPT, mode, query, product, top_k)
    if err:
        return {'error': err}
    out = out or ''

    items = []
    if mode == 'semantic':
        # 解析：第N个结果：\nfeature_name: xxx\nfeature_description: xxx\n----
        blocks = re.split(r'第\d+个结果[：:]\s*\n', out)
        for b in blocks:
            b = b.strip()
            if not b or b.startswith('未检索到'):
                continue
            name_m = re.search(r'feature_name:\s*(.+)', b)
            desc_m = re.search(r'feature_description:\s*([\s\S]+?)(?:\n-{5,}|$)',
                               b)
            if name_m:
                items.append({
                    'feature_name': name_m.group(1).strip(),
                    'description': (desc_m.group(1).strip() if desc_m else ''),
                })
    else:
        # feature_name 模式：全文 + 导航目录
        blocks = re.split(r'第\d+个结果[：:]\s*\n', out)
        for b in blocks:
            b = b.strip()
            if not b or b.startswith('未检索到'):
                continue
            full_m = re.search(r'全文内容：\s*\n([\s\S]*?)(?:\n完整导航目录|$)', b)
            nav_m = re.search(r'完整导航目录：\s*\n([\s\S]*)', b)
            items.append({
                'content': (full_m.group(1).strip() if full_m else '')[:8000],
                'nav': [x.strip() for x in ((nav_m.group(1) or '').split('\n')
                                            if nav_m else []) if x.strip()][:50],
            })

    return {
        'product': product,
        'mode': mode,
        'query': query,
        'count': len(items),
        'items': items[:top_k if mode == 'semantic' else 3],
        'note': ('特性文档不含 MML 命令示例。要命令写法请用 kb_search_command。'
                 if mode == 'semantic' else None),
    }


# ═══════════════════════════════════════════════════════════
# 工具 2：kb_search_command
# ═══════════════════════════════════════════════════════════
@_kb_cached
def tool_kb_search_command(args):
    """查 MML 命令文档（参数表 + 使用实例）。"""
    # 支持两种调用：name（精确命令名）或 query（语义）
    name = (args.get('name') or '').strip()
    query = (args.get('query') or '').strip()
    product = (args.get('product') or DEFAULT_PRODUCT).upper()
    top_k = int(args.get('top_k') or 5)

    if name:
        mode, q = 'command_name', name
    elif query:
        mode, q = 'semantic', query
    else:
        return {'error': 'name 或 query 至少给一个'}

    out, err = _run_script(SUPPORT_SCRIPT, mode, q, product, top_k)
    if err:
        return {'error': err}
    out = out or ''

    items = []
    if mode == 'semantic':
        blocks = re.split(r'第\d+个结果[：:]\s*\n', out)
        for b in blocks:
            b = b.strip()
            if not b or b.startswith('未检索到'):
                continue
            nm = re.search(r'(?:command_name|命令名|name):\s*(.+)', b)
            desc = re.search(r'(?:description|功能描述|描述):\s*([\s\S]+?)(?:\n-{5,}|$)', b)
            items.append({
                'command': (nm.group(1).strip() if nm else ''),
                'description': (desc.group(1).strip()[:1500] if desc else b[:1500]),
            })
    else:
        # command_name 模式：返回完整文档（参数表 + 实例）
        items.append({
            'command': q,
            'doc': out.strip()[:12000],
        })

    return {
        'product': product,
        'mode': mode,
        'query': q,
        'count': len(items),
        'items': items,
    }


# ═══════════════════════════════════════════════════════════
# 工具 3：kb_get_naming
# ═══════════════════════════════════════════════════════════
@_kb_cached
def tool_kb_get_naming(args):
    """查某族的命名规律（从 EXP 统计）。"""
    exp_path = (args.get('exp_path') or '').strip()
    family = (args.get('family') or '').strip().upper()

    if not exp_path:
        return {'error': 'exp_path 必填（命名规律必须基于现网统计）'}
    if not Path(exp_path).exists():
        return {'error': f'EXP 文件不存在: {exp_path}'}

    try:
        sys.path.insert(0, str(Path(__file__).parent))
        import mcp_exp
    except Exception as e:
        return {'error': f'无法导入 mcp_exp: {e}'}

    # 复用 mcp_exp 的统计能力
    stats = mcp_exp.tool_exp_stats({'path': exp_path, 'family': family})
    if stats.get('error'):
        return stats

    fams = stats.get('families') or {}
    if not fams:
        return {'error': f'EXP 里没找到 {family} 族的 ADD 命令', 'family': family}

    return {
        'family': family,
        'exp_path': exp_path,
        'naming': fams,
        'note': '命名骨架里 N 代表数字段；照此结构命名，不要照抄具体值。',
    }


# ═══════════════════════════════════════════════════════════
# MCP 协议
# ═══════════════════════════════════════════════════════════
TOOLS = [
    {
        'name': 'kb_search_feature',
        'description': (
            '查特性文档库（UEG/UDG/UNC）。想知道「某个业务功能怎么配、依赖哪些对象、'
            '适用哪些网元」时用这个。返回特性名称 + 描述。\n'
            '★ 特性文档不含 MML 命令示例，要命令写法请用 kb_search_command。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'query': {'type': 'string', 'description': '语义描述或特性名'},
                'product': {'type': 'string', 'enum': ['UDG', 'UEG', 'UNC'],
                            'description': '产品，默认 UDG（必须显式指定，否则会拿到别的产品）'},
                'top_k': {'type': 'integer', 'description': '返回条数，默认 5'},
                'mode': {'type': 'string', 'enum': ['semantic', 'feature_name'],
                         'description': 'semantic=语义检索（默认）；feature_name=按特性名精确查全文'},
            },
            'required': ['query'],
        },
    },
    {
        'name': 'kb_search_command',
        'description': (
            '查 MML 命令文档库。返回参数表（类型/枚举/必选性）和使用实例。\n'
            '已知命令名用 name（如 "ADD URR"），只知道功能用 query（如 "配置计费费率"）。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'name': {'type': 'string', 'description': '精确命令名，如 ADD URR'},
                'query': {'type': 'string', 'description': '语义描述（name 为空时用）'},
                'product': {'type': 'string', 'enum': ['UDG', 'UEG', 'UNC'],
                            'description': '产品，默认 UDG'},
                'top_k': {'type': 'integer', 'description': '语义检索返回条数，默认 5'},
            },
        },
    },
    {
        'name': 'kb_get_naming',
        'description': (
            '查某个命令族在现网的命名规律（骨架 + 序号范围 + 优先级区间）。'
            '命名前先查这个，照结构取名，不要凭空编造。'
        ),
        'inputSchema': {
            'type': 'object',
            'properties': {
                'exp_path': {'type': 'string', 'description': 'EXP 文件路径'},
                'family': {'type': 'string', 'description': '命令族，如 HOST / FILTER / URR'},
            },
            'required': ['exp_path', 'family'],
        },
    },
]

HANDLERS = {
    'kb_search_feature': tool_kb_search_feature,
    'kb_search_command': tool_kb_search_command,
    'kb_get_naming': tool_kb_get_naming,
}


def handle(msg):
    method = msg.get('method')
    mid = msg.get('id')

    if method == 'initialize':
        return {'jsonrpc': '2.0', 'id': mid, 'result': {
            'protocolVersion': '2024-11-05',
            'capabilities': {'tools': {}},
            'serverInfo': {'name': 'mcp_knowledge', 'version': '1.0.0'},
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
