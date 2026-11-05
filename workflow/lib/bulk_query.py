"""bulk_query.py — 容器内批量查询（一次进程，供 ②a 调用）。

★ 为什么需要它：
  Milvus Lite 是嵌入式单文件库，多进程并发打开会锁冲突
  （实测 8 路并发 0/8 成功）。
  但串行 docker exec 每次都要重新 import（1.7s）+ 实例化，
  20 次 = 34 秒纯开销。

  解法：一个进程内完成所有查询，结果一次返回。

★ 用法（stdin 传 JSON，stdout 返回 JSON）：
  输入：{"cmd_descs": ["ADD FILTER", ...], "semantic": [{"key":"...", "query":"..."}]}
  输出：{"cmd_descs": {"ADD FILTER": "描述"}, "semantic": {"key": [{feature_name, description}]}, "elapsed": {...}}
"""
import json
import sys
import time

# ★ 2026-11-04：路径动态解析 —— workflow 用自己的 skill 副本，
#   不写死 /home/expgv（legacy 的 skill 空间）
def _skill_scripts(skill):
    import os
    cands = [
        os.path.join(os.environ.get('WF_HOME', ''), '.hermes/skills', skill, 'scripts'),
        '/opt/expgv/workflow/home/.hermes/skills/%s/scripts' % skill,
        '/home/expgv/.hermes/skills/%s/scripts' % skill,
    ]
    for c in cands:
        if c and os.path.isdir(c):
            return c
    return ''


for _sk in ('mml_support', 'mml_feature'):
    _p = _skill_scripts(_sk)
    if _p:
        sys.path.insert(0, _p)


def main():
    t0 = time.time()
    req = json.load(sys.stdin)

    product = req.get('product', 'UDG')
    want_descs = req.get('cmd_descs') or []
    want_semantic = req.get('semantic') or []
    top_k = req.get('top_k', 5)

    out = {'cmd_descs': {}, 'semantic': {}, 'errors': {}}

    # ── 命令描述（mml_support）──
    if want_descs:
        try:
            import mml_support_query as ms
            db = ms.MMLSupportDB(product=product) if _accepts_product(
                ms.MMLSupportDB) else ms.MMLSupportDB()
            t1 = time.time()
            for fam in want_descs:
                try:
                    # ★ search_by_command_name(self, command_name: str) 无 top_k
                    res = db.search_by_command_name(fam)
                    txt = _flatten(res)
                    out['cmd_descs'][fam] = _extract_func(txt)
                except Exception as e:
                    out['errors']['cmd:' + fam] = str(e)[:120]
            out['elapsed_support'] = round(time.time() - t1, 1)
        except Exception as e:
            out['errors']['support_init'] = str(e)[:200]

    # ── 语义检索（mml_feature）──
    if want_semantic:
        try:
            import mml_feature_query as mf
            fdb = mf.MMLFeatureDB(product=product) if _accepts_product(
                mf.MMLFeatureDB) else mf.MMLFeatureDB()
            t2 = time.time()
            for item in want_semantic:
                key = item.get('key') or item.get('query')
                q = item.get('query') or ''
                try:
                    res = fdb.search_by_semantic(q, top_k=top_k)
                    out['semantic'][key] = _extract_features(res)
                except Exception as e:
                    out['errors']['sem:' + str(key)[:30]] = str(e)[:120]
            out['elapsed_feature'] = round(time.time() - t2, 1)
        except Exception as e:
            out['errors']['feature_init'] = str(e)[:200]

    out['elapsed_total'] = round(time.time() - t0, 1)
    json.dump(out, sys.stdout, ensure_ascii=False)


def _accepts_product(cls):
    import inspect
    try:
        sig = inspect.signature(cls.__init__)
        return 'product' in sig.parameters
    except Exception:
        return False


def _flatten(res):
    """把命令检索结果拍平成文本。

    ★ _struct_fixed：真实结构是 list[tuple(2)]
      tuple[0] = 分类路径 list，tuple[1] = 命令帮助 Markdown
      取 tuple[1] 即可（Markdown 全文含「命令功能」段）。
    """
    if isinstance(res, str):
        return res
    if isinstance(res, list):
        parts = []
        for r in res:
            if isinstance(r, (tuple, list)) and len(r) >= 2:
                parts.append(str(r[1]))
            elif isinstance(r, dict):
                parts.append(' '.join(str(v) for v in r.values()))
            else:
                parts.append(str(r))
        return '\n'.join(parts)
    if isinstance(res, (tuple, list)) and len(res) >= 2:
        return str(res[1])
    if isinstance(res, dict):
        return ' '.join(str(v) for v in res.values())
    return str(res)


def _extract_func(txt):
    """从命令帮助里抽「命令功能」段的第一段。"""
    import re
    m = re.search(r'#{2,4}\s*命令功能\s*\n+(.*?)(?=\n#{2,4}\s|\Z)', txt or '', re.S)
    if not m:
        return ''
    body = m.group(1)
    lines = []
    for l in body.split('\n'):
        s = l.strip()
        if not s:
            continue
        if s.startswith(('**适用', '适用NF', '- ', '|')):
            continue
        if re.fullmatch(r'\*\*[^*]{0,10}\*\*', s):
            continue
        lines.append(s)
    if not lines:
        return ''
    first = lines[0]
    for l in lines[:5]:
        if not any(w in l for w in ('高危', '可能会影响', '注意', '警告', '须知')):
            first = l
            break
    s2 = re.match(r'^([^。\n]{6,200})', first)
    desc = (s2.group(1) if s2 else first[:200]).strip()
    desc = re.sub(r'^(该|本|此)?命令(主要)?(用于|用来|属于|可以)?', '', desc).strip()
    return desc[:200]


def _extract_features(res):
    """从特性检索结果抽 [{feature_name, description, path}]。

    ★ _struct_fixed：真实结构是 list[tuple(4)]
      [0] 分类路径 list
      [1] 元信息文本
      [2] 特性名
      [3] 完整描述
    """
    out = []
    for r in (res or []):
        if isinstance(r, (tuple, list)) and len(r) >= 4:
            path = r[0]
            if isinstance(path, (list, tuple)):
                path = ' > '.join(str(x) for x in path)[:120]
            out.append({
                'feature_name': str(r[2])[:120],
                'description': str(r[3])[:400],
                'meta': str(r[1])[:200],
                'path': str(path),
            })
        elif isinstance(r, dict):
            out.append({
                'feature_name': r.get('feature_name') or r.get('name') or '?',
                'description': (r.get('feature_description') or r.get('description') or '')[:400],
                'path': '',
            })
        else:
            out.append({'feature_name': str(r)[:80], 'description': '', 'path': ''})
    return out


if __name__ == '__main__':
    main()
