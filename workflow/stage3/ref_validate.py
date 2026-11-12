"""参照对象结构校验：判断选的参照对象能否满足目标需求。

★ 2026-11-12 P0-2（用户要求新增）

问题（实测 NC20260810002261）：
  意图说「新增规则」，sos 要配的 RULE 带 FLOWFILTERNAME + FILTERINGMODE。
  如果随便拿一个现网 RULE 当参照（如 r_ims_sig，7 个参数无 FLOWFILTERNAME），
  平移后会漏掉 FLOWFILTERNAME / FILTERINGMODE 两个关键参数。

  实测现网 RULE 有 3 种参数集形态：
    687 个（93%）：RULENAME/POLICYTYPE/PRIORITY/POLICYNAME/RULERANGE/RULESPECTYPE/NWDAFEVENTS
     51 个（ 7%）：缺 RULERANGE
      3 个（0.4%）：多 FLOWFILTERNAME（ULCL 类型）
  而 UDG 侧还有第 4 种：PCC + FLOWFILTERNAME + FILTERINGMODE（sos 要的正是这种）

  选错参照 → 参数不全 → 配置不生效。

判据设计（三层）：
  L1 参数覆盖：参照对象的参数集，必须覆盖目标需要的参数集
  L2 形态匹配：参照对象的参数集，应该在同族的主流形态里（避免选到极端个例）
  L3 族内代表性：参照对象所在形态的实例数不能太少（否则可能是个例/例外配置）

用法：
  validate_reference_structure(
      exp_path=UNC,
      family='RULE',
      ref_name='r_ims_sig',
      target_params={'RULENAME', 'POLICYTYPE', 'PRIORITY', 'POLICYNAME',
                     'FLOWFILTERNAME', 'FILTERINGMODE', 'RULESPECTYPE'},
  )
  → {'ok': False, 'missing': ['FLOWFILTERNAME', 'FILTERINGMODE'],
     'suggestion': '换参照：...', 'better_candidates': [...]}
"""
import re
from collections import Counter, defaultdict
from pathlib import Path


def collect_family_param_sets(exp_path, family, limit=5000):
    """收集某族所有实例的 (对象名, 参数集)。

    返回：{'names': {对象名: 参数集}, 'combos': Counter, 'total': n}
    """
    p = Path(exp_path)
    if not p.exists():
        return {'names': {}, 'combos': Counter(), 'total': 0}

    names = {}
    combos = Counter()
    pk = None

    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            for line in f:
                s = line.strip()
                m = re.match(rf'^ADD\s+{re.escape(family)}\s*:\s*(.*)', s)
                if not m:
                    continue
                rest = m.group(1)
                ps = set(re.findall(r'([A-Z][A-Z0-9_]*)\s*=', rest))
                if not ps:
                    continue
                # 身份参数 = 第一个
                first = re.match(r'([A-Z][A-Z0-9_]*)\s*=\s*"?([^",;]+)"?', rest)
                if not first:
                    continue
                if pk is None:
                    pk = first.group(1)
                name = first.group(2).strip()
                if len(names) >= limit:
                    break
                names[name] = ps
                combos[frozenset(ps)] += 1
    except Exception:
        return {'names': {}, 'combos': Counter(), 'total': 0}

    return {'names': names, 'combos': combos, 'total': len(names),
            'pk': pk}


def validate_reference_structure(exp_paths, family, ref_name,
                                  target_params=None, min_share=0.02):
    """校验参照对象能否满足目标需求。

    参数：
      exp_paths       EXP 路径（字符串或列表，多网元时传全部）
      family          族名
      ref_name        参照对象名
      target_params   目标需要的参数集（None 时退化为 L2/L3 校验）
      min_share       参照形态在族内的最低占比（默认 2%，低于此视为个例）

    返回：
      {'ok': bool,
       'issues': [...],
       'missing': [...],          # 参照缺的参数
       'ref_shape_share': 0.93,   # 参照所在形态的占比
       'better_candidates': [...] # 建议换用的参照
      }
    """
    # ★ 2026-11-12 修：支持多个 EXP
    #   实测问题：r_ims_sig 在 UNC 缺 FLOWFILTERNAME，
    #   正确参照 1001271_pptv_r 在 UDG 侧。只扫单个 EXP 找不到更好的参照。
    if isinstance(exp_paths, (str, Path)):
        exp_paths = [exp_paths]

    # ★ 2026-11-12 修 bug：同名对象在不同网元参数集可能不同，不能按名字合并
    #   实测：1001271_pptv_r 在 UDG 带 FILTERINGMODE+FLOWFILTERNAME，
    #        在 UNC 带 NWDAFEVENTS+RULERANGE
    #   旧写法 if nm not in names: names[nm]=ps → UNC 先占位，
    #   UDG 的版本被丢弃 → 参照校验结论完全反了
    #
    #   改为：names_by_exp = {exp: {name: params}}
    #        校验时按「参照所在 EXP」取参数集
    names_by_exp = {}
    combos = Counter()
    per_exp = {}
    ref_found_in = []

    for ep in exp_paths:
        info = collect_family_param_sets(ep, family)
        if info['total'] == 0:
            per_exp[str(ep)] = 0
            continue
        per_exp[str(ep)] = info['total']
        names_by_exp[str(ep)] = info['names']
        for c, n in info['combos'].items():
            combos[c] += n
        if ref_name in info['names']:
            ref_found_in.append(str(ep))

    total = sum(per_exp.values())
    if total == 0:
        return {'ok': True, 'skipped': True,
                'reason': f'所有 EXP 里都没有 {family} 的 ADD 命令',
                'per_exp': per_exp}

    # 合并所有名字（用于统计形态），但校验参照时用它在的那个 EXP
    all_names = {}
    for exp, nm_map in names_by_exp.items():
        for nm, ps in nm_map.items():
            all_names.setdefault(nm, []).append((exp, ps))

    entries = all_names.get(ref_name)
    if not entries:
        return {'ok': False, 'skipped': False,
                'issues': [f'参照对象 {ref_name} 不在任何 EXP 的 {family} 里'],
                'missing': [], 'ref_shape_share': 0,
                'better_candidates': [], 'per_exp': per_exp}

    # ★ 2026-11-12 修：同名对象在不同网元的参数集可能完全不同
    #   实测 r_ims_sig：
    #     UNC 7 参数（NWDAFEVENTS+RULERANGE，无 FLOWFILTERNAME）
    #     UDG 7 参数（FILTERINGMODE+FLOWFILTERNAME，无 RULERANGE）
    #   旧做法取「参数最全的版本」→ 掩盖了单侧缺参数的事实
    #
    #   正确做法：逐个 EXP 校验，任一版本满足即通过（说明该参照在某网元可用）
    ref_versions = [{'exp': Path(ep).name, 'params': sorted(ps),
                     'n_params': len(ps)}
                    for ep, ps in entries]

    # 选「最能满足 target_params 的版本」做代表
    if target_params:
        want0 = set(target_params)
        best = max(entries, key=lambda x: len(want0 & x[1]))
        ref_params = best[1]
        ref_exp_of_version = Path(best[0]).name
    else:
        best = max(entries, key=lambda x: len(x[1]))
        ref_params = best[1]
        ref_exp_of_version = Path(best[0]).name

    issues = []
    missing = []

    # ── L1 参数覆盖 ──
    if target_params:
        missing = sorted(set(target_params) - ref_params)
        if missing:
            issues.append(f'参照缺参数: {", ".join(missing)}')

    # ── L2/L3 形态代表性 ──
    shape = frozenset(ref_params)
    shape_count = combos.get(shape, 0)
    share = shape_count / total if total else 0

    if share < min_share:
        issues.append(
            f'参照所在形态只有 {shape_count}/{total} 个实例（{share*100:.1f}%），'
            f'可能是特例配置')

    # ── 找更好的参照（★ 必须跨所有 EXP 找）──
    #   实测问题：只给 UNC 校验时，UNC 里没有覆盖全参数的 RULE 形态，
    #   但 UDG 侧有 667 个实例满足 → 换参照建议必须跨 EXP 搜
    better = []
    # ★ 2026-11-12 修：候选始终搜索（不只在缺参数时）
    #   旧条件 "if target_params and missing" → 参照已通过时 missing 为空，
    #   候选列表为空。但用户仍需要知道「还有哪些可参照的对象」。
    if target_params:
        want = set(target_params)
        seen_names = set()
        for exp, nm_map in names_by_exp.items():
            for nm, ps in nm_map.items():
                if want <= ps and nm not in seen_names and nm != ref_name:
                    # 这个候选在它所在 EXP 里的形态占比
                    ei = collect_family_param_sets(exp, family)
                    combo = frozenset(ps)
                    shape_cnt = ei['combos'].get(combo, 0)
                    better.append({
                        'name': nm,
                        'count': shape_cnt,
                        'share': shape_cnt / max(1, ei['total']),
                        'params': sorted(ps),
                        'in_exp': Path(exp).name,
                    })
                    seen_names.add(nm)
                    break   # 每个 EXP 只取一个代表
        better.sort(key=lambda x: (-x['share'], -x['count']))

    return {
        'ok': not issues,
        'issues': issues,
        'missing': missing,
        'ref_versions': ref_versions,
        'ref_used_exp': ref_exp_of_version,
        'ref_shape_share': share,
        'ref_shape_count': shape_count,
        'family_total': total,
        'better_candidates': better[:5],
        'all_shapes': [
            {'params': sorted(c), 'count': n, 'share': n / total}
            for c, n in combos.most_common(8)
        ],
    }


def infer_target_params_from_intent(intent_text, dataset_text=''):
    """从意图/数据清单推断目标需要哪些参数。

    这是 P0-2 的难点：目标参数集无法直接知道。
    只能从意图的措辞 + 数据清单的列名推断。

    规则（实测有效）：
      意图/清单提到「过滤器」「流过滤器」 → 需要 FLOWFILTERNAME
      意图/清单提到「过滤模式」           → 需要 FILTERINGMODE
      意图/清单提到「策略组」             → 需要 POLICYNAME
      意图/清单提到「优先级」             → 需要 PRIORITY
      意图/清单提到「VPN」                → 需要 VPNINSTANCE
    """
    txt = (intent_text or '') + '\n' + (dataset_text or '')
    mapping = {
        r'流过滤器|过滤器名称|FLOWFILTER': {'FLOWFILTERNAME'},
        r'过滤模式|FILTERINGMODE': {'FILTERINGMODE'},
        r'策略组|PCC策略': {'POLICYNAME'},
        r'优先级': {'PRIORITY'},
        r'VPN实例|VPN 名称': {'VPNINSTANCE'},
        r'地址池名称|池名': {'POOLNAME'},
        r'APN名称|APN 名称': {'APN'},
        r'用户模板名称': {'USERPROFILENAME'},
        r'接口名称|接口名': {'IFNAME'},
        r'URR名称|计费规则': {'URRNAME'},
    }
    hint = set()
    for pat, params in mapping.items():
        if re.search(pat, txt, re.I):
            hint |= params
    return hint


if __name__ == '__main__':
    import json
    import sys

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    adir = Path(g['path']) / '备份附件'
    UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)
    UDG = next((p for p in adir.glob('*.txt') if '_UDG_' in p.name), None)

    print('=' * 88)
    print('参照对象结构校验自测')
    print('=' * 88)

    # 目标需要的参数（sos 的 RULE 实际参数集）
    TARGET = {'RULENAME', 'POLICYTYPE', 'PRIORITY', 'POLICYNAME',
              'FLOWFILTERNAME', 'FILTERINGMODE', 'RULESPECTYPE'}

    for label, exp, ref in [
        ('UNC 的 r_ims_sig（缺 FLOWFILTERNAME）', UNC, 'r_ims_sig'),
        ('UDG 的 1001271_pptv_r（参数齐全）', UDG, '1001271_pptv_r'),
    ]:
        print(f'\n【{label}】')
        r = validate_reference_structure(
            [str(UNC), str(UDG)], 'RULE', ref, target_params=TARGET)
        if r.get('skipped'):
            print(f'  跳过: {r["reason"]}')
            continue
        print(f'  ok={r["ok"]}  形态占比={r["ref_shape_share"]*100:.1f}%'
              f'（{r["ref_shape_count"]}/{r["family_total"]}）')
        for iss in r['issues']:
            print(f'  ⚠ {iss}')
        if r['better_candidates']:
            print(f'  建议换参照：')
            for c in r['better_candidates'][:2]:
                print(f'    {c["name"]}  ({c["count"]} 个实例, '
                      f'{c["share"]*100:.0f}%)')

    # 测意图参数推断
    print('\n【意图参数推断】')
    text = '新增 规则（规则名称为r_sos_sig，策略类型为PCC，过滤模式为FLOWFILTER）；新增 流过滤器'
    hint = infer_target_params_from_intent(text)
    print(f'  推断出: {sorted(hint)}')
