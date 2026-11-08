"""G24：省略说明检测。

用户裁定（2026-11-08）：
  配置分析.md 里出现「不做」「跳过」「用 XXX 代替」这类措辞时，
  必须在 方案澄清.json 里有对应条目，让用户能补充要求。

背景：
  实测 NC20260812000714，agent 在配置分析里写
  「PNFNSINDEX 在本 UPF 现网基线中均不存在，故本产物只做 UPF 侧可落地部分」
  「本次不新增接口、不删除接口」
  然后就不配了。用户完全不知道 agent 做了这个决定。
"""
import json
import re
from pathlib import Path

# 省略措辞
OMIT_PATTERNS = [
    r'不做', r'不配', r'不新增', r'不删除', r'不修改',
    r'跳过', r'省略', r'忽略', r'暂不', r'无需配置',
    r'用[^，。\n]{0,20}代替', r'以[^，。\n]{0,20}替代',
    r'只做[^，。\n]{0,20}部分', r'仅配置', r'无法配置',
    r'该[^，。\n]{0,10}不存在', r'现网[^，。\n]{0,10}不存在',
]

_OMIT_RE = re.compile('|'.join(OMIT_PATTERNS))


def _split_sentences(text):
    """按句号/换行切句，保留较长的句子。"""
    parts = re.split(r'[。\n]+', text)
    return [p.strip() for p in parts if len(p.strip()) >= 8]


def _get_clarify_text(session_dir):
    """读方案澄清.json 的全文（用于匹配）。"""
    p = Path(session_dir) / 'analysis_code' / '方案澄清.json'
    if not p.exists():
        # 兜底：也看根目录
        p = Path(session_dir) / '方案澄清.json'
    if not p.exists():
        return '', False
    try:
        txt = p.read_text(encoding='utf-8')
        # 尝试解析成 list/dict，把 question/why 全拼起来
        try:
            d = json.loads(txt)
            parts = []
            def walk(x):
                if isinstance(x, dict):
                    for v in x.values():
                        walk(v)
                elif isinstance(x, list):
                    for v in x:
                        walk(v)
                elif isinstance(x, str):
                    parts.append(x)
            walk(d)
            return ' '.join(parts), True
        except Exception:
            return txt, True
    except Exception:
        return '', False


def _similar(a, b, min_len=4):
    """粗略判断两个句子是否讲同一件事：共享足够长的子串。"""
    if not a or not b:
        return False
    shorter = a if len(a) < len(b) else b
    longer = b if len(a) < len(b) else a
    # 取 shorter 里所有长度 >= min_len 的片段，看有没有出现在 longer 里
    for i in range(0, max(1, len(shorter) - min_len + 1)):
        seg = shorter[i:i + min_len]
        if seg in longer:
            return True
    return False


def check_omission_explained(session_dir, max_report=8):
    """G24：检测「省略了但没说明」。

    Returns {
      ok, skipped, n_omissions, unexplained: [{sentence, hint}], has_clarify
    }
    """
    d = Path(session_dir)
    ana = d / 'analysis_code' / '配置分析.md'
    if not ana.exists():
        ana = d / '配置分析.md'
    if not ana.exists():
        return {'ok': True, 'skipped': True, 'reason': '无配置分析.md'}

    try:
        text = ana.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        return {'ok': True, 'skipped': True, 'reason': f'读不了配置分析: {e}'}

    clarify_text, has_clarify = _get_clarify_text(session_dir)

    omissions = []
    for sent in _split_sentences(text):
        if not _OMIT_RE.search(sent):
            continue
        # 排除「不存在的对象已确认」这类中性描述？先不排除，宁可多报
        omissions.append(sent)

    if not omissions:
        return {'ok': True, 'n_omissions': 0, 'unexplained': [],
                'has_clarify': has_clarify}

    unexplained = []
    for sent in omissions:
        if has_clarify and _similar(sent, clarify_text):
            continue
        unexplained.append({'sentence': sent[:160],
                            'hint': '在配置分析里说了不做/跳过，但方案澄清里没对应条目'})
        if len(unexplained) >= max_report * 2:
            break

    return {
        'ok': not unexplained,
        'n_omissions': len(omissions),
        'n_unexplained': len(unexplained),
        'unexplained': unexplained[:max_report],
        'has_clarify': has_clarify,
        'note': ('配置分析里提到「不做/跳过/用...代替」等，'
                 '如果是有意省略，请在方案澄清.json 里加一条说明，'
                 '让用户知道并可以补充要求。'),
    }
