#!/usr/bin/env python3
"""生成「意图删减版」：去掉可从上游推导出来的下游数据清单和对应描述。

★ 2026-11-12（用户要求）
  「同步考虑意图的删减版（即以现在的为基线，删减被关联的数据清单和对应描述作为新版本）」

## 什么是「删减版」

  完整版：数据清单给了所有对象名（POOL + POOLGROUP + POOLGRPMAP ...）
  删减版：只给上游对象名（POOL），下游（POOLGROUP）让 agent 自己推导

  这更接近真实运维：人手上只有核心对象清单，
  下游对象的命名由系统按现网风格推导，人再 review 调整。

## 删减规则

  1. 数据清单：删掉「可推导的下游族」对应的整张表
     可推导判据 = derive_fill.CHAIN_SPECS 里定义了 upstream → downstream，
                  且该工单的 EXP 里能找到绑定族配对（有样板可学）
  2. 意图正文：删掉对应下游族的条目
  3. 保留：上游族条目、无法推导的族条目

## 输出

  /tmp/intent_v5_slim/<TK>_意图.md
  /tmp/intent_v5_slim/<TK>_数据清单.md
  /tmp/intent_v5_slim/_slim_report.json   每单删了什么
"""
import json
import re
import sys
from pathlib import Path

PROJ = Path('/Users/alesc/workspace/mml-gen-lite')
sys.path.insert(0, str(PROJ / 'workflow/stage3'))

import derive_fill as DF

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

SRC = Path('/tmp/intent_v5')          # 完整版基线
OUT = Path('/tmp/intent_v5_slim')     # 删减版输出


def exp_paths_of(tk):
    g = GT_MAP.get(tk)
    if not g:
        return []
    adir = Path(g['path']) / '备份附件'
    return [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []


def derivable_families(tk):
    """判断该工单有哪些下游族「可从上游推导」。

    判据：
      1. 上游族在这个工单的 GT 里
      2. 下游族也在 GT 里
      3. EXP 里有绑定族配对（有样板可学），且配对 >= 3 条（太少不靠谱）
    """
    g = GT_MAP.get(tk)
    if not g:
        return {}
    fams = {f for _, _, f, _, _ in g['kept']}
    exps = exp_paths_of(tk)
    if not exps:
        return {}

    out = {}
    for up_fam, spec in DF.CHAIN_SPECS.items():
        if up_fam not in fams:
            continue
        for down_fam, dspec in spec['downstream'].items():
            if down_fam not in fams:
                continue
            if not dspec.get('bind_family'):
                continue
            pairs = DF._load_chain_pairs(exps, dspec)
            if len(pairs) >= 3:
                out[down_fam] = {
                    'upstream': up_fam,
                    'n_pairs': len(pairs),
                    'bind_family': dspec['bind_family'],
                }
    return out


def family_cn_names(tk, fams):
    """从 gen_dataset 的 sheets 里直接拿「族 → 表名」映射。

    ★ 2026-11-12 第三版（前两版都失败）
      v1 按「主键值出现在表里」判断 → RULE 表含 PCCPOLICYGRPNM 的值，误判成 PCCPOLICYGRP
      v2 按「表头反查参数名」判断   → FLOWFILTERNAME 在 FLOWFILTER 和 FLTBINDFLOWF 都有，误判
      v3 让 gen_dataset 直接返回族名（sheets 第 5 个元素）→ 无歧义
    """
    import sys as _sys
    _sys.path.insert(0, str(PROJ / 'scripts'))
    import gen_all_intents as GAI

    g = GT_MAP.get(tk)
    if not g:
        return {}

    try:
        r = GAI.gen_dataset(tk, GT, GT_MAP)
    except Exception:
        return {}

    out = {}
    for item in r['sheets']:
        sname = item[0]
        fam = item[4] if len(item) >= 5 else None
        if fam and fam in fams and fam not in out:
            out[fam] = sname
    return out


def slim_dataset(tk, drop_fams):
    """删掉数据清单里属于 drop_fams 的整张表。"""
    p = SRC / f'{tk}_数据清单.md'
    if not p.exists():
        return None, []
    txt = p.read_text(encoding='utf-8', errors='replace')
    cn_map = family_cn_names(tk, set(drop_fams))
    drop_names = {cn_map[f] for f in drop_fams if f in cn_map}

    lines = txt.split('\n')
    out = []
    dropped = []
    i = 0
    while i < len(lines):
        line = lines[i]
        m = re.match(r'^##\s+(.+?)（[^）]*）\s*$', line.strip())
        if m and m.group(1).strip() in drop_names:
            # 跳过这张表（到下一个 ## 或文末）
            dropped.append(m.group(1).strip())
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('##'):
                i += 1
            continue
        out.append(line)
        i += 1

    new_txt = '\n'.join(out)
    # 去掉多余空行
    new_txt = re.sub(r'\n{3,}', '\n\n', new_txt)
    return new_txt, dropped


def slim_intent(tk, drop_fams):
    """删掉意图正文里对应下游族的描述。

    ★ 2026-11-12 重写（V5 是流水句，不是分行条目）
      V5 格式：「新增 网络切片DNN绑定、会话释放原因配置、PCC策略组、用量上报规则组、用户配置组；」
      下游族名混在逗号分隔的名字列表里。

      做法：
        1. 拿到 drop_fams 的中文名（可能有多个变体，都要试）
        2. 在意图里找「、名字、」「、名字；」「名字、」这类位置，删掉名字和相邻分隔符
        3. 清理多余的分隔符（、、 / 、； / ；、）
    """
    p = SRC / f'{tk}_意图.md'
    if not p.exists():
        return None, []
    txt = p.read_text(encoding='utf-8', errors='replace')

    cn_map = family_cn_names(tk, set(drop_fams))
    drop_names = set()
    for f in drop_fams:
        if f in cn_map:
            drop_names.add(cn_map[f])

    # 还要拿该族的所有 LLM 变体名（同一族可能有多个叫法）
    import sys as _sys
    _sys.path.insert(0, str(PROJ / 'scripts'))
    try:
        import header_llm as HL
        cache = HL._load_cache()
        for f in drop_fams:
            variants = cache.get(f'FAMILY::{f.upper()}')
            if isinstance(variants, list):
                drop_names.update(variants)
    except Exception:
        pass

    if not drop_names:
        return txt, []

    dropped = []
    new = txt
    for name in sorted(drop_names, key=len, reverse=True):
        # 记录命中
        before = new
        # 模式1：、名字、  → 、
        new = re.sub(rf'、\s*{re.escape(name)}\s*、', '、', new)
        # 模式2：、名字；  → ；
        new = re.sub(rf'、\s*{re.escape(name)}\s*；', '；', new)
        # 模式3：；名字、  → ；
        new = re.sub(rf'；\s*{re.escape(name)}\s*、', '；', new)
        # 模式4：、名字（约束）  → 删掉（含约束）
        new = re.sub(rf'、\s*{re.escape(name)}（[^）]*）', '', new)
        # 模式5：、名字 紧跟标点
        new = re.sub(rf'、\s*{re.escape(name)}(?=[，。；、])', '', new)
        # 模式6：名字、 （开头位置）
        new = re.sub(rf'(?<=[；。])\s*{re.escape(name)}\s*、', '', new)
        # ★ 模式7：；名字。  /  ；名字，  /  ；名字；  结尾位置
        new = re.sub(rf'；\s*{re.escape(name)}(?=[。，；])', '；', new)
        # ★ 模式8：动作词 + 名字（如「删除 PCC策略组。」）
        new = re.sub(rf'(?<=删除)\s*{re.escape(name)}(?=[。，；])', '', new)
        # 模式7：兜底，直接删名字
        if name in new and new != before:
            pass
        elif name in new:
            new = new.replace(name, '')
        if new != before:
            dropped.append(name)

    # 清理：连续分隔符
    new = re.sub(r'、\s*、', '、', new)
    new = re.sub(r'；\s*；', '；', new)
    new = re.sub(r'、\s*；', '；', new)
    new = re.sub(r'；\s*、', '；', new)
    new = re.sub(r'\n{3,}', '\n\n', new)

    return new, dropped


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    report = {}

    n_total = n_slimmed = 0
    for p in sorted(SRC.glob('*_意图.md')):
        tk = p.name.replace('_意图.md', '')
        if tk.startswith('_'):
            continue
        n_total += 1

        drop = derivable_families(tk)
        if not drop:
            # 无可推导，直接复制
            (OUT / p.name).write_text(p.read_text(encoding='utf-8'), encoding='utf-8')
            ds = SRC / f'{tk}_数据清单.md'
            if ds.exists():
                (OUT / ds.name).write_text(ds.read_text(encoding='utf-8'), encoding='utf-8')
            continue

        n_slimmed += 1

        # 删数据清单
        ds_new, ds_dropped = slim_dataset(tk, list(drop.keys()))
        if ds_new is not None:
            (OUT / f'{tk}_数据清单.md').write_text(ds_new, encoding='utf-8')

        # 删意图条目
        in_new, in_dropped = slim_intent(tk, list(drop.keys()))
        if in_new is not None:
            (OUT / f'{tk}_意图.md').write_text(in_new, encoding='utf-8')

        report[tk] = {
            'drop_families': drop,
            'dropped_sheets': ds_dropped,
            'dropped_intent_items': in_dropped,
        }

    (OUT / '_slim_report.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')

    print('=' * 96)
    print('意图删减版生成完成')
    print('=' * 96)
    print(f'  总工单: {n_total}')
    print(f'  发生删减: {n_slimmed}')
    print(f'  输出: {OUT}')

    print(f'\n=== 删减明细（前 12 单）===')
    for tk, r in list(report.items())[:12]:
        fams = ', '.join(r['drop_families'].keys())
        print(f'\n{tk}')
        print(f'  删族: {fams}')
        print(f'  删表: {r["dropped_sheets"]}')
        print(f'  删条目: {len(r["dropped_intent_items"])} 条')


if __name__ == '__main__':
    main()
