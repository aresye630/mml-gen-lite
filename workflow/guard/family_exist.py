"""G32：命令族名在 EXP 里不存在（agent 编造/拼错）。

★ 2026-11-12（从 14 单删减版测试发现）

实测问题（NC20260814000701）：
  产物: ADD REFREFSHSRV:REFRESHTYPE=ALL;
  EXP:  SET REFRESHSRV:REFRESHTYPE=ALL;      ← 真实族名

  两个错误：
    1. 族名拼错 REFREFSHSRV 多了 "REF"
    2. 动词用错（该命令是 SET 类操作命令，不能用 ADD）

  而 guard 全部判 pass，没抓住。

## 判据

  扫描产物（mml.txt 或 params.csv）里每个「动词 + 族名」：
    · 族名在 EXP 里完全没出现过 → warn（可能是编造/拼错）
    · 族名存在但动词不对 → warn（如 REFRESHSRV 只有 SET，产物用 ADD）

  分级：
    fatal  族名完全不存在且相似度高的族存在（明显是拼错）
    warn   族名完全不存在（可能是新产品特性，EXP 里没有）
    降级   动词不匹配（可能是 EXP 里恰好没这种动词，不算错）

## 为什么不是 fatal 一律

  有些新特性能在文档里有但现网 EXP 还没有，一律 fatal 会误杀。
  这里用「相似度」分级：
    · 若 EXP 里存在 DICE 相似度 > 0.85 的族 → 明显拼错 → fatal
    · 否则 → warn
"""
import difflib
import re
from collections import defaultdict


def _norm_cmd(line):
    """从命令行提取 (动词, 族名, 参数集)。"""
    s = line.split('//')[0].strip()
    m = re.match(r'^(ADD|MOD|SET|RMV)\s+([A-Z][A-Z0-9_]+)\s*[:;]?\s*(.*)', s, re.I)
    if not m:
        return None
    params = set(re.findall(r'([A-Z][A-Z0-9_]*)\s*=', m.group(3)))
    return m.group(1).upper(), m.group(2).upper(), params


def build_exp_family_index(exp_paths=None, exp_text=''):
    """从 EXP 建 {族名: {动词集合}} 索引。

    支持两种输入：exp_paths（文件列表）或 exp_text（已读入的文本）。
    """
    idx = defaultdict(set)

    def _feed(text):
        for line in text.split('\n'):
            r = _norm_cmd(line)
            if r:
                idx[r[1]].add(r[0])

    for p in (exp_paths or []):
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                _feed(f.read())
        except Exception:
            continue
    if exp_text:
        _feed(exp_text)

    return dict(idx)


def check_family_exists(artifact_text, exp_paths=None, mode='mml',
                        csv_rows=None, exp_text=''):
    """检查产物里的命令族是否都在 EXP 里存在。

    artifact_text: mml.txt 内容（mode='mml'）
    csv_rows:      params.csv 行（mode='csv'）

    返回：{
      'ok': bool,
      'n_checked': int,
      'unknown_families': [{'family','verb','line','similar','suggest'}],
      'verb_mismatch': [{'family','verb','allowed'}],
      'fatal': [...], 'warn': [...]
    }
    """
    exp_idx = build_exp_family_index(exp_paths, exp_text)
    exp_fams = set(exp_idx.keys())

    # 收集产物里的 (族, 动词, 位置)
    items = []
    if mode == 'mml':
        for i, line in enumerate((artifact_text or '').split('\n'), 1):
            r = _norm_cmd(line)
            if r:
                items.append({'family': r[1], 'verb': r[0],
                              'line': line.strip()[:120], 'loc': f'行{i}'})
    else:
        seen = set()
        for row in (csv_rows or []):
            fam = (row.get('family') or row.get('命令族') or '').strip().upper()
            if not fam or fam in seen:
                continue
            seen.add(fam)
            verb = (row.get('verb') or 'ADD').upper()
            items.append({'family': fam, 'verb': verb,
                          'line': '', 'loc': f'族 {fam}'})

    unknown, mismatch, fatal, warn = [], [], [], []

    for it in items:
        fam = it['family']
        if fam not in exp_fams:
            # 找相似的族名
            similar = difflib.get_close_matches(fam, sorted(exp_fams), n=1, cutoff=0.85)
            entry = {
                'family': fam, 'verb': it['verb'], 'loc': it['loc'],
                'line': it['line'],
                'similar': similar[0] if similar else None,
            }
            if similar:
                entry['suggest'] = f'疑似拼错，EXP 里有 {similar[0]}'
                fatal.append(entry)
            else:
                entry['suggest'] = 'EXP 里没有该族（可能是新特性或编造）'
                warn.append(entry)
            unknown.append(entry)
            continue

        # 族存在，检查动词
        allowed = exp_idx.get(fam, set())
        if allowed and it['verb'] not in allowed:
            # 只报 ADD vs SET/MOD 这种明显冲突
            if it['verb'] == 'ADD' and allowed and 'ADD' not in allowed:
                mismatch.append({
                    'family': fam, 'verb': it['verb'],
                    'allowed': sorted(allowed),
                    'loc': it['loc'],
                })

    return {
        'ok': not fatal and not warn and not mismatch,
        'n_checked': len(items),
        'n_exp_families': len(exp_fams),
        'unknown_families': unknown,
        'verb_mismatch': mismatch,
        'fatal': fatal,
        'warn': warn,
    }


if __name__ == '__main__':
    import json
    from pathlib import Path

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    GT_MAP = {g['ticket']: g for g in GT}

    print('=' * 100)
    print('G32 命令族存在性校验')
    print('=' * 100)

    # 用之前发现的 REFREFSHSRT 案例
    tk = 'NC20260814000701'
    g = GT_MAP[tk]
    exps = [str(p) for p in sorted((Path(g['path']) / '备份附件').glob('*.txt'))]

    TEST_CASES = [
        ('正常（SET REFRESHSRV）', 'SET REFRESHSRV:REFRESHTYPE=ALL;'),
        ('拼错（ADD REFREFSHSRV）', 'ADD REFREFSHSRV:REFRESHTYPE=ALL;'),
        ('动词错（ADD REFRESHSRV）', 'ADD REFRESHSRV:REFRESHTYPE=ALL;'),
        ('完全编造（ADD FOOBARXYZ）', 'ADD FOOBARXYZ:NAME="x";'),
    ]

    for label, text in TEST_CASES:
        r = check_family_exists(text, exps)
        status = '✅ pass' if r['ok'] else (
            f"❌ fatal={len(r['fatal'])} warn={len(r['warn'])} "
            f"verb_mismatch={len(r['verb_mismatch'])}")
        print(f'\n{label}')
        print(f'  {status}')
        for f in r['fatal']:
            print(f'    [fatal] {f["family"]} → {f["suggest"]}')
        for w in r['warn']:
            print(f'    [warn]  {w["family"]} → {w["suggest"]}')
        for m in r['verb_mismatch']:
            print(f'    [verb]  {m["family"]} 用了 {m["verb"]}，EXP 里只有 {m["allowed"]}')
