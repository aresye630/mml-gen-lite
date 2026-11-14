"""G37：检测 agent 越界访问/修改程序源码。

★★ 2026-11-14（用户裁定 C 方案后新增）

## 背景（75 单全量实测发现）

agent 有 Bash / Read / Code 工具，且 expgv 用户对 /opt/expgv 可写，
导致它在生成过程中直接改生产代码：

  · 205 次 Bash/Read 访问 /opt/expgv/workflow/*
  · 实际改写了 plan_expander.py

实测 4 个容器内容不一致（同一镜像）：
  镜像原始      b4a12a3f1e31dc95  （31875 字节）
  mmlgen-b1     b4a12a3f1e31dc95  （未改）
  mmlgen-b2     b4a12a3f1e31dc95  （未改）
  mmlgen-clean  e088f6d7638b1d8e  （38988 字节，被改）
  mmlgen-b3     6781c5230761234b  （39754 字节，被改）
→ 同一镜像的 4 个容器不再一致，评测结果不可信。

## 本次防护三层

  1. 镜像层（Dockerfile.incr）：/opt/expgv 代码目录 chmod 555/444，物理只读
  2. prompt 层：明令禁止 Read/Bash/import/subprocess 访问 /opt/expgv
  3. guard 层（本模块）：扫 events.jsonl，发现越界就报 fatal

## 判据

fatal：
  · Bash / Code 里出现 /opt/expgv/**/*.py 且含写操作（open(...,'w') / write_text / sed -i / tee / cp ... /）
  · Bash 里出现 subprocess / os.system / chmod / chown 作用于 /opt/expgv

warn：
  · Read / Bash cat/grep/head/tail 读 /opt/expgv/**/*.py（只读，但仍属越界）

## 为什么不把「读」也算 fatal

agent 读规则源码有时是为了理解判据（如 guard 逻辑），
物理上已禁止写，读不改变行为。所以读=warn（留痕），写=fatal。
"""
import glob
import json
import re

# 源码根目录
CODE_ROOTS = ('/opt/expgv/',)

# 代码文件特征
CODE_FILE_RE = re.compile(r'/opt/expgv/[\w./-]+\.(py|yaml|yml|json|js|ts|sh)\b')

# 写操作特征
WRITE_PAT = re.compile(
    r"open\s*\([^)]*['\"][wa]['\"]"          # open(..., 'w' / 'a')
    r"|write_text|write_bytes|\.write\("      # Path.write_text / f.write(
    r"|sed\s+-i|perl\s+-[pi]"                 # 就地编辑
    r"|\bcp\b[^|]*/opt/expgv"                 # cp 到/从源码
    r"|\bmv\b[^|]*/opt/expgv"
    r"|\btee\b"
    r"|>\s*/opt/expgv"                        # 重定向写
    r"|chmod\s+-?R?\s*[0-7]+\s+/opt/expgv"
    r"|chown\s+-?R?\s+\S+\s+/opt/expgv",
    re.I)

# 执行外部命令（绕过 MCP）
EXEC_PAT = re.compile(r'\bsubprocess\b|\bos\.system\b|\bos\.popen\b|\bos\.exec', re.I)

# ★ 2026-11-14 补：agent 用 Hermes 内部 API 绕过 MCP
#   实测 mmlgen-b3 的会话里：
#     Code: from hermes_tools import read_file, patch
#     Code: from hermes_tools import read_file, write_file
#   这两个 API 能直接读写任意文件（包括 /opt/expgv 源码），
#   比 Bash 更隐蔽（events 里 action=Code，target 只有 import 语句）。
HERMES_TOOLS_WRITE_PAT = re.compile(
    r'from\s+hermes_tools\s+import[^\n]*\b(write_file|patch|terminal)\b', re.I)

# 动态加载内部模块
IMPORT_PAT = re.compile(
    r'importlib\.import_module\s*\(\s*[\'"]'
    r'|sys\.path\.insert\s*\(\s*0\s*,\s*[\'"]/opt/expgv',
    re.I)


def _iter_tool_events(session_dir):
    """遍历所有轮的 events.jsonl，产出 tool 事件。"""
    for f in sorted(glob.glob(f'{session_dir}/.agent/run*/events.jsonl')):
        rnd = 'run1'
        m = re.search(r'/\.agent/(run\d+)/', f)
        if m:
            rnd = m.group(1)
        try:
            with open(f, encoding='utf-8', errors='replace') as fh:
                for line in fh:
                    try:
                        d = json.loads(line)
                    except Exception:
                        continue
                    if d.get('kind') != 'tool':
                        continue
                    yield rnd, d
        except Exception:
            continue


def check_source_access(session_dir):
    """扫 events.jsonl，检查是否越界访问/修改源码。

    返回 {
      'ok': bool,
      'skipped': bool,
      'fatal': [str, ...],
      'warn': [...],
      'stats': {'n_tool': int, 'n_touch': int, 'n_write': int},
    }
    """
    if not session_dir:
        return {'ok': True, 'skipped': True, 'reason': 'no session_dir',
                'fatal': [], 'warn': [], 'stats': {}}

    fatal, warn = [], []
    n_tool = n_touch = n_write = 0
    seen = set()      # 去重（同一动作重复出现只报一次）

    for rnd, d in _iter_tool_events(session_dir):
        n_tool += 1
        act = str(d.get('action') or '')
        tgt = str(d.get('target') or '')
        det = str(d.get('detail') or '')
        blob = f'{tgt}\n{det}'

        # 只关心可能碰源码 / 绕过 MCP 的工具
        if act not in ('Bash', 'Read', 'Code', 'Write', 'Tool', 'Files', 'Search', 'Edit'):
            continue

        # ★ 2026-11-14 修：hermes_tools 的写 API 句子本身不含路径
        #   （from hermes_tools import write_file, patch），
        #   所以要在这道「必须含 /opt/expgv」的闸门之前判定。
        if HERMES_TOOLS_WRITE_PAT.search(blob):
            key = ('ht', act)
            if key not in seen:
                seen.add(key)
                snippet = (tgt or det).replace('\n', ' ')[:140]
                fatal.append(
                    f'{rnd} {act} 用 hermes_tools 内部 API 读写文件'
                    f'（{snippet}）—— 绕过 MCP 限制，禁止使用')
            n_touch += 1
            continue

        if '/opt/expgv' not in blob:
            continue

        n_touch += 1
        m = CODE_FILE_RE.search(blob)
        fpath = m.group(0) if m else '/opt/expgv/...'

        # 写操作
        if WRITE_PAT.search(blob):
            key = ('w', fpath)
            if key not in seen:
                seen.add(key)
                n_write += 1
                snippet = (tgt or det).replace('\n', ' ')[:140]
                fatal.append(
                    f'{rnd} {act} 试图写源码 {fpath}（{snippet}）'
                    f' —— 源码是评测对象，禁止修改')

        # subprocess / os.system（绕过 MCP 执行命令）
        elif EXEC_PAT.search(blob) and act in ('Bash', 'Code'):
            key = ('x', act)
            if key not in seen:
                seen.add(key)
                snippet = (tgt or det).replace('\n', ' ')[:140]
                warn.append(
                    f'{rnd} {act} 用了 subprocess/os.system（{snippet}）'
                    f' —— 应只用 MCP 工具')

        # 动态 import 内部模块
        elif IMPORT_PAT.search(blob):
            key = ('i', act)
            if key not in seen:
                seen.add(key)
                warn.append(
                    f'{rnd} {act} 动态加载 /opt/expgv 内部模块'
                    f' —— 应只用 MCP 工具')

        # 纯读
        else:
            key = ('r', fpath)
            if key not in seen and act in ('Read', 'Bash'):
                seen.add(key)
                warn.append(
                    f'{rnd} {act} 读了源码 {fpath}（只读，不改变行为，但属越界）')

    stats = {'n_tool': n_tool, 'n_touch': n_touch, 'n_write': n_write}
    return {
        'ok': not fatal,
        'skipped': False,
        'fatal': fatal,
        'warn': warn[:6],
        'stats': stats,
    }


if __name__ == '__main__':
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    r = check_source_access(sd)
    print(json.dumps(r, ensure_ascii=False, indent=1))
