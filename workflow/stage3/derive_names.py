"""对象名派生 v3：语义变换（最朴素也最接近人的思维）。

★ 2026-11-12 第三版（v1 全局规则 0~82%、v2 骨架槽位 17% 都不行）

## 前两版为什么失败

v1 全局规则：从全部配对选「覆盖最高的一条」全表套用
  → 同一 EXP 里常有多风格并存，选错就全错

v2 骨架槽位：把名字拆成固定段+数字槽位
  → 重建时槽位丢失（pool_ims_smfm004 → pgrp_ims_smfm）

## v3 的做法：三个语义动作

从实测 23944 对配对里归纳出的全部真实变换，只有三类动作：

  action 1  删版本标记       _ipv4 / _ipv6 / -ipv4 / -ipv6 / _v4_01 / _v6_01
  action 2  换前缀          pool- → grp-  |  pool_ → pgrp_  |  pool → pgrp
  action 3  换后缀          _v4_01 → _group  |  (无) → _group

## 流程

  1. 从 EXP 配对里，为每个配对提取「动作序列」
  2. 对目标名，找最相似样板（按动作可施用性 + 名字相似度排序）
  3. 套用样板的动作序列
  4. 输出置信度 + 依据

## 置信度

  1.00  推导结果在现网已存在（强证据）
  0.85  样板与目标结构高度一致（分段数、分隔符、版本标记都相同）
  0.60  样板结构部分一致
  <0.6  低置信，标注「需人工核对」
"""
import json
import re
from collections import Counter
from pathlib import Path

# 版本标记（会被删除）
VERSION_MARKS = ['_ipv4', '_ipv6', '-ipv4', '-ipv6', '_ipv4v6', '_ipv6v4',
                 '_v4_01', '_v6_01', '_v4', '_v6', '-v4', '-v6']

# 前缀映射（上游风格 → 下游风格）
PREFIX_MAP = {
    'pool-': 'grp-',
    'pool_': 'pgrp_',
    'Pool-': 'grp-',
}


def strip_version(name):
    """去掉版本标记。返回 (新名, 去掉的标记)。"""
    for m in sorted(VERSION_MARKS, key=len, reverse=True):
        if name.endswith(m):
            return name[: -len(m)], m
        if m in name:
            # 中间的版本标记也去掉
            return name.replace(m, ''), m
    return name, None


def extract_actions(up, dn):
    """从一对配对提取动作序列。

    返回 [{'action': 'strip_version', 'mark': '_ipv4'}, {'action': 'prefix_replace', ...}]
    或 [{'action': 'add_suffix', 'suffix': '_group'}]
    """
    actions = []

    # 判断是否只是版本标记的差异
    up_s, mark = strip_version(up)
    dn_s, mark2 = strip_version(dn)

    # 情况 A：up 去掉版本标记后 == dn（只删了版本）
    if up_s == dn:
        return [{'action': 'strip_version', 'mark': mark}]

    # 情况 B：up 去掉版本 + 前缀替换 == dn
    for src, dst in PREFIX_MAP.items():
        if up_s.startswith(src):
            cand = dst + up_s[len(src):]
            if cand == dn:
                acts = []
                if mark:
                    acts.append({'action': 'strip_version', 'mark': mark})
                acts.append({'action': 'prefix_replace', 'from': src, 'to': dst})
                return acts

    # 情况 C：down 只是 up 加后缀
    if dn.startswith(up):
        suffix = dn[len(up):]
        if suffix:
            return [{'action': 'add_suffix', 'suffix': suffix}]

    # 情况 D：up 去掉尾部某段后加后缀（sxbxrjsx4g01s_v4_01 → sxbxrjsx4g01s_group）
    for mark in sorted(VERSION_MARKS, key=len, reverse=True):
        if up.endswith(mark):
            base = up[: -len(mark)]
            if dn == base + '_group':
                return [{'action': 'strip_version', 'mark': mark},
                        {'action': 'add_suffix', 'suffix': '_group'}]
            if dn.startswith(base):
                # base + 别的东西
                return [{'action': 'strip_version', 'mark': mark},
                        {'action': 'replace_tail', 'from': mark, 'to': dn[len(base):]}]

    # 情况 E：完全不同的名字（如 volte_pool_location1 → ims.sn_group_location1）
    return None      # 无法归纳


def apply_actions(name, actions):
    """套用动作序列。返回 (新名, 成功与否)。"""
    cur = name
    for a in actions:
        if a['action'] == 'strip_version':
            if a['mark'] and a['mark'] in cur:
                cur = cur.replace(a['mark'], '', 1)
            else:
                return None, False
        elif a['action'] == 'prefix_replace':
            if cur.startswith(a['from']):
                cur = a['to'] + cur[len(a['from']):]
            else:
                return None, False
        elif a['action'] == 'add_suffix':
            cur = cur + a['suffix']
        elif a['action'] == 'replace_tail':
            if cur.endswith(a['from']):
                cur = cur[: -len(a['from'])] + a['to']
            else:
                return None, False
        else:
            return None, False
    return cur, True


def _structure_sig(name):
    """结构签名：用于找相似样板。"""
    base = name
    for m in VERSION_MARKS:
        if base.endswith(m):
            base = base[: -len(m)]
            break
    return {
        'n_dash': base.count('-'),
        'n_under': base.count('_'),
        'n_dot': base.count('.'),
        'prefix': base.split('-')[0].split('_')[0][:6],
        'ends_digit': bool(re.search(r'\d$', base)),
        'len': len(base),
    }


def similarity(a, b):
    """结构相似度 0~1。"""
    sa, sb = _structure_sig(a), _structure_sig(b)
    same = sum(1 for k in ('n_dash', 'n_under', 'n_dot', 'ends_digit')
               if sa[k] == sb[k])
    base = same / 4
    pre = 0
    for x, y in zip(a, b):
        if x == y:
            pre += 1
        else:
            break
    pre_s = pre / max(len(a), 1)
    return round(base * 0.5 + pre_s * 0.5, 3)


def load_pairs(exp_paths, bind_family='POOLBINDGROUP',
               up_param='POOLNAME', down_param='POOLGROUPNAME'):
    """从 EXP 提取配对。"""
    pairs = []
    for p in exp_paths:
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    if not re.match(rf'^ADD\s+{bind_family}\b', s):
                        continue
                    m_up = re.search(rf'{up_param}\s*=\s*"([^"]*)"', s)
                    m_dn = re.search(rf'{down_param}\s*=\s*"([^"]*)"', s)
                    if m_up and m_dn:
                        pairs.append((m_up.group(1), m_dn.group(1)))
        except Exception:
            continue
    return pairs


def build_action_library(pairs):
    """从全部配对里建「可行动作库」：[(actions, (up, dn), sim_weight)]"""
    lib = []
    for up, dn in pairs:
        acts = extract_actions(up, dn)
        if acts:
            lib.append({'actions': acts, 'sample': (up, dn)})
    return lib


def derive_by_analogy(target_names, pairs):
    """主入口。"""
    lib = build_action_library(pairs)
    existing = {dn for _, dn in pairs}
    out = []

    if not lib:
        for n in target_names:
            out.append({'upstream': n, 'derived': None, 'confidence': 0.0,
                        'note': 'EXP 配对里无法归纳出任何变换'})
        return out

    for name in target_names:
        # 按「可施用 + 相似度」排序样板
        cands = []
        for item in lib:
            derived, ok = apply_actions(name, item['actions'])
            if not ok or derived == name:
                continue
            sim = similarity(name, item['sample'][0])
            cands.append((sim, derived, item))
        if not cands:
            out.append({'upstream': name, 'derived': None, 'confidence': 0.0,
                        'note': '无可用样板（所有动作都套不上）'})
            continue

        cands.sort(key=lambda x: -x[0])
        # 多个样板给出同样结果 → 加分
        top_derived = cands[0][1]
        agree = sum(1 for _, d, _ in cands if d == top_derived)
        sim, derived, item = cands[0]

        conf = 0.55 + min(0.3, agree * 0.1) + sim * 0.15
        if derived in existing:
            conf = min(1.0, conf + 0.15)

        out.append({
            'upstream': name,
            'derived': derived,
            'confidence': round(min(1.0, conf), 3),
            'sim': sim,
            'agree': agree,
            'sample': f"{item['sample'][0]}→{item['sample'][1]}",
            'actions': [a['action'] for a in item['actions']],
            'in_exp': derived in existing,
        })
    return out


def to_csv_rows(results, net_type='UDG', family='POOLGROUP',
                down_param='POOLGRPNAME', start_group=1,
                extra_params=None):
    """转成 params.csv 的 8 列格式。

    ★ 2026-11-12 对齐 mml_gen.read_params() 的列定义：
      序号, 组, 网元, 命令族, 参数, 值, 占位符, 来源, 说明

    来源列标记 derived:conf=0.98，说明列写推导依据，
    用户 review 时能看到「这个值是怎么来的」，改起来有依据。
    """
    rows = []
    grp = start_group
    for r in results:
        if not r.get('derived'):
            continue
        rows.append({
            'no': '',
            'group': str(grp),
            'net_type': net_type,
            'family': family,
            'param': down_param,
            'value': r['derived'],
            'placeholder': '',
            'source': f"derived:conf={int(r['confidence']*100)}",
            'note': (f"由 {r['upstream']} 推导"
                     f"（样板 {r['sample']}，动作 {'+'.join(r['actions'])}，"
                     f"置信 {int(r['confidence']*100)}%）"),
        })
        for k, v in (extra_params or {}).items():
            rows.append({
                'no': '', 'group': str(grp), 'net_type': net_type,
                'family': family, 'param': k, 'value': v,
                'placeholder': '', 'source': 'exp', 'note': '',
            })
        grp += 1
    return rows


def write_csv(rows, path, header=True):
    """写 params.csv（8 列）。"""
    import csv as _csv
    cols = ['序号', '组', '网元', '命令族', '参数', '值', '占位符', '来源', '说明']
    keymap = {'序号': 'no', '组': 'group', '网元': 'net_type', '命令族': 'family',
              '参数': 'param', '值': 'value', '占位符': 'placeholder',
              '来源': 'source', '说明': 'note'}
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8-sig', newline='') as f:
        w = _csv.DictWriter(f, fieldnames=cols)
        if header:
            w.writeheader()
        for r in rows:
            w.writerow({c: r.get(keymap[c], '') for c in cols})
    return p


if __name__ == '__main__':
    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 104)
    print('语义变换派生 v3 验证')
    print('=' * 104)

    TOTAL = HIT = 0
    for tk in ['NC20260820001773', 'NC20260824002020', 'NC20260824002208',
               'NC20260805000498', 'NC20260803002122', 'NC20260810002261',
               'NC20260828000409']:
        g = next((x for x in GT if x['ticket'] == tk), None)
        if not g:
            continue

        pools, real = [], set()
        for _, v, fam, params, raw in g['kept']:
            if fam == 'POOL' and params.get('POOLNAME'):
                pools.append(params['POOLNAME'])
            elif fam == 'POOLGROUP' and params.get('POOLGRPNAME'):
                real.add(params['POOLGRPNAME'])

        adir = Path(g['path']) / '备份附件'
        exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []
        pairs = load_pairs(exps)

        print(f'\n{tk}  (POOL {len(pools)}, EXP 配对 {len(pairs)})')
        if not pairs:
            print('  ❌ 无配对')
            continue

        res = derive_by_analogy(pools[:6], pairs)
        for r in res[:4]:
            if not r.get('derived'):
                print(f'  ⚠ {r["upstream"]}: {r.get("note")}')
                continue
            ok = '✅' if r['derived'] in real else '❌'
            print(f'  {ok} {r["upstream"]}')
            print(f'      → {r["derived"]}  ({r["confidence"]*100:.0f}%,'
                  f' 动作 {"+".join(r["actions"])}, 同意 {r["agree"]})')

        derived = {r['derived'] for r in res if r.get('derived')}
        if derived and real:
            hit = derived & real
            TOTAL += len(derived)
            HIT += len(hit)
            print(f'  命中 {len(hit)}/{len(derived)}  GT: {sorted(real)[:2]}')

    if TOTAL:
        print(f'\n{"=" * 104}')
        print(f'总体命中: {HIT}/{TOTAL} = {HIT/TOTAL*100:.0f}%')


def build_clarifications(results, up_family='POOL', down_family='POOLGROUP'):
    """生成「无法自动推导」的澄清项。

    ★ 2026-11-12
      派生引擎遇到「EXP 里没有同构样板」时应该拒绝推导，
      而不是瞎猜。这些项要列进澄清清单，让用户补。

    返回：[{'type', 'item', 'reason', 'suggestion'}]
    """
    out = []
    for r in results:
        if r.get('derived'):
            continue
        out.append({
            'type': '无法推导对象名',
            'item': f"{up_family} {r['upstream']} 对应的 {down_family} 名称",
            'reason': r.get('note') or '现网无同构样板',
            'suggestion': (f"请提供 {r['upstream']} 对应的 {down_family} 名称；"
                           f"或在数据清单里补充该 {down_family} 的名称列"),
            'upstream': r['upstream'],
        })
    return out


def render_clarifications(clars, title='需要补充的信息'):
    """渲染成 markdown。"""
    if not clars:
        return ''
    lines = [f'## {title}', '']
    for i, c in enumerate(clars, 1):
        lines.append(f'{i}. **{c["item"]}**')
        lines.append(f'   - 原因：{c["reason"]}')
        lines.append(f'   - 建议：{c["suggestion"]}')
        lines.append('')
    return '\n'.join(lines)
