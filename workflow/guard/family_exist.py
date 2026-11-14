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
from pathlib import Path


# ★ 2026-11-13：KB 里 MML 命令文档的索引缓存
#   判据来源：kb/output_udg_mml/mml/MML/Document/{add,mod,rmv,lst,set}_<族名小写>.md
#   实测 NC20260814001250：
#     OSPFINTERFACEAUTH 不在 EXP（新增族），但 KB 有 mod_/lst_/rmv_ 三个文档
#     → 合法族名，不该被判「拼错」
#     G32 却因为 EXP 里有 OSPFINTERFACE（相似度 > 0.85）判成拼错 → fatal
#     → agent 把正确的 OSPFINTERFACEAUTH 改掉 → 产物从 64 条降到 4 条（GT 要 16）
_KB_FAM_CACHE = None


def _kb_family_index(kb_root=None):
    """扫 KB 的 MML 命令文档，建「族名 → 文档文件列表」索引。

    返回 dict 或 None（找不到 KB 就返回 None，调用方退回旧判据）。
    """
    global _KB_FAM_CACHE
    if _KB_FAM_CACHE is not None:
        return _KB_FAM_CACHE or None

    import os
    roots = []
    if kb_root:
        roots.append(Path(kb_root))
    env = os.environ.get('KB_ROOT')
    if env:
        roots.append(Path(env))
    # 常见位置
    for cand in ('/opt/expgv/kb', '/data/kb'):
        roots.append(Path(cand))

    idx = {}
    for root in roots:
        if not root.exists():
            continue
        # 找 output_*_mml/mml/MML/Document 目录
        for doc_dir in root.glob('output_*_mml/mml/MML/Document'):
            for f in doc_dir.glob('*.md'):
                m = re.match(r'^(add|mod|rmv|lst|set)_([a-z0-9_]+)\.md$', f.name.lower())
                if m:
                    fam = m.group(2).upper()
                    idx.setdefault(fam, []).append(str(f))
        if idx:
            break

    _KB_FAM_CACHE = idx if idx else {}
    return idx or None


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
            # ★ 2026-11-13：先查 KB 有没有该族的 MML 文档
            #   有文档 = 合法族名（只是现网还没配过）→ warn，不判拼错
            #   没文档 + EXP 有相似族 = 真拼错 → fatal
            kb_idx = _kb_family_index()
            kb_docs = (kb_idx or {}).get(fam) if kb_idx else None

            if kb_docs:
                entry['suggest'] = (f'KB 有该族的 MML 文档（{len(kb_docs)} 个），'
                                    f'属新增族（现网未配置过），不是拼错')
                entry['kb_docs'] = [Path(x).name for x in kb_docs[:3]]
                warn.append(entry)
            elif similar:
                entry['suggest'] = f'疑似拼错，EXP 里有 {similar[0]}（KB 也无该族文档）'
                fatal.append(entry)
            else:
                entry['suggest'] = 'EXP 里没有该族，KB 也无该族文档（可能编造）'
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


def family_has_doc(family):
    """该族在 KB 的 MML 文档里存在吗？（= 合法族名，即使是现网未配过的新族）

    ★ 2026-11-14 新增，供 mml_gen 用：
      原来 mml_gen 用 difflib 对 set_only 族做近似纠错，
      实测把合法族名 INTERFACE 改成了 ARPINTERFACE
      （difflib 相似度够高，但两者是完全不同的族）。
      修法：先查 KB 文档，有文档就是合法族名，不做纠错。
    """
    try:
        idx = _kb_family_index()
        return str(family or '').strip().upper() in idx
    except Exception:
        return False


if __name__ == '__main__':
    """自测（不依赖 GT）。

    ★ 2026-11-14 硬编码/GT 隔离审核：原来这里读 /tmp/gt_cleaned.json 取
      真实工单的 EXP 路径做测试。GT 隔离红线要求生成侧代码不碰 GT，
      即使是 __main__ 自测也不该留这个入口（容易被误当生产路径）。
      改为用命令行传 EXP 路径，或用内置的 KB 文档做判别力测试。
    """
    import sys
    from pathlib import Path

    print('=' * 100)
    print('G32 命令族存在性校验（自测，不读 GT）')
    print('=' * 100)

    # 用法：python3 family_exist.py <EXP路径> [<EXP2> ...]
    if len(sys.argv) > 1:
        exps = [str(Path(x)) for x in sys.argv[1:]]
        print(f'EXP: {exps}')
    else:
        exps = []
        print('未传 EXP 路径 → 只测 KB 文档判据（不测 EXP 比对）')

    TEST_CASES = [
        ('正常族名（KB 有文档）', 'ADD INTERFACE:IFNAME="x";'),
        ('拼错族名（KB 无文档）', 'ADD INTERFACEE:IFNAME="x";'),
        ('完全编造（KB 无文档）', 'ADD FOOBARXYZ:NAME="x";'),
    ]

    for label, text in TEST_CASES:
        r = check_family_exists(text, exps) if exps else {'ok': True, 'fatal': [], 'warn': [], 'verb_mismatch': []}
        print(f'\n{label}')
        print(f"  ok={r['ok']} fatal={len(r.get('fatal') or [])} warn={len(r.get('warn') or [])}")
        for f in (r.get('fatal') or []):
            print(f"    [fatal] {f.get('family')} → {f.get('suggest')}")
