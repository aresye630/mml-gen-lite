"""阶段3 派生补全：走链发现下游族 + 样板推导对象名。

★ 2026-11-12（用户裁定）
  「我要配地址池，给个 POOL 列表，参考 EXP 发现 POOL 有 POOLGROUP，
   那就添加族 POOLGROUP，但是没有 POOLGROUP 的规划数据，
   那就使用命名风格推导出对象名，且输出 param.csv 支持用户来调整」
  「URR 或者其他的 FILTER 都是一样的逻辑」
  「特性指纹这个功能不需要全量运行，按需即可，就找链条的功能就行」

## 完整流程

  输入：数据清单只给了上游对象名（POOL / URR / FILTER ...）
    ↓
  Step A  走链发现下游族（graph_walk 值驱动 BFS，带维度约束）
          给 pool_ims_smfm004 → 发现 POOLBINDGROUP/POOLGROUP/POOLGRPMAP/SECTION
    ↓
  Step B  判断哪些下游族缺数据（数据清单没给名字）
    ↓
  Step C  用样板推导名字（derive_names 的三类语义动作）
    ↓
  Step D  生成 param.csv 行（带 source=derived:conf=XX + 依据说明）
    ↓
  Step E  推不出的进澄清清单

## 按需触发（用户要求）

  不是每个工单都跑。触发条件：
    · 规划表里有 ADD 上游族，但没有对应下游族
    · 意图里提到下游对象（「地址池组」「URR组」），但数据清单没给名字
"""
import json
import re
import sys
from pathlib import Path

_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

import chain_finder as CF
import derive_names as DN

# ═══════════════════════════════════════════════════════════
# 链条定义（数据驱动：族 → 走链维度 + 绑定族）
# ═══════════════════════════════════════════════════════════
# 为什么需要这个表：
#   graph_walk 需要 param_scope 约束维度，否则会走飞（实测 9128 实例）
#   不同业务链的参数名不同，无法完全自动推断
# 这不是硬编码局点值，是「业务链的知识」——参数名是产品定义的
CHAIN_SPECS = {
    'POOL': {
        'entry_param': 'POOLNAME',
        'scope_hint': ['POOLNAME', 'POOLGROUPNAME', 'POOLGRPNAME',
                       'MAPPINGNAME', 'SECTIONNUM'],
        'downstream': {
            'POOLGROUP': {'param': 'POOLGRPNAME', 'bind_family': 'POOLBINDGROUP',
                          'up_param': 'POOLNAME', 'down_param': 'POOLGROUPNAME'},
            'POOLGRPMAP': {'param': 'MAPPINGNAME',
                           'up_param': 'POOLGROUPNAME', 'down_param': 'MAPPINGNAME'},
        },
    },
    'URR': {
        'entry_param': 'URRNAME',
        'scope_hint': ['URRNAME', 'URRGROUPNAME', 'UPURRNAME1', 'DOWNURRNAME1',
                       'PCCPOLICYGRPNM', 'RULENAME', 'USERPROFILENAME'],
        'downstream': {
            'URRGROUP': {'param': 'URRGROUPNAME', 'bind_family': 'URRGROUP',
                         'up_param': 'UPURRNAME1', 'down_param': 'URRGROUPNAME'},
            'PCCPOLICYGRP': {'param': 'PCCPOLICYGRPNM',
                             'bind_family': 'PCCPOLICYGRP',
                             'up_param': 'URRGROUPNAME',
                             'down_param': 'PCCPOLICYGRPNM'},
        },
    },
    'FILTER': {
        'entry_param': 'FILTERNAME',
        'scope_hint': ['FILTERNAME', 'FLOWFILTERNAME', 'FILTERINGMODE'],
        'downstream': {
            'FLOWFILTER': {'param': 'FLOWFILTERNAME',
                           'bind_family': 'FLTBINDFLOWF',
                           'up_param': 'FILTERNAME',
                           'down_param': 'FLOWFILTERNAME'},
        },
    },
}


def _load_chain_pairs(exp_paths, dspec):
    """从 EXP 提取「上游名 → 下游名」配对，用于归纳推导规律。

    ★ 用绑定族（POOLBINDGROUP / URRGROUP / FLTBINDFLOWF）里的配对，
      这是最可靠的「同一命令里同时出现上下游」的证据。

    dspec = {'param', 'bind_family', 'up_param', 'down_param'}
    """
    pairs = []
    bind_family = dspec.get('bind_family')
    up_p = dspec.get('up_param')
    dn_p = dspec.get('down_param')
    if not (bind_family and up_p and dn_p):
        return pairs     # 该下游族没定义绑定关系，无法从 EXP 归纳
    for p in exp_paths:
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    if not re.match(rf'^ADD\s+{bind_family}\b', s):
                        continue
                    m_up = re.search(rf'{up_p}\s*=\s*"([^"]*)"', s)
                    m_dn = re.search(rf'{dn_p}\s*=\s*"([^"]*)"', s)
                    if m_up and m_dn:
                        pairs.append((m_up.group(1), m_dn.group(1)))
        except Exception:
            continue
    return pairs


def _chain_params_for_scope(spec):
    """从一个下游族规格生成 param_scope。"""
    s = set(spec.get('scope_hint') or [])
    s.add(spec['up_param'])
    s.add(spec['down_param'])
    return s or None


def discover_downstream_families(exp_paths, entry_family, entry_values,
                                 max_instances=200):
    """Step A：走链发现上游对象涉及的下游族。

    返回：{
      'ok', 'families': {族: 实例数}, 'ref_degrees': {...}, 'param_hint': {...}
    }
    """
    spec = CHAIN_SPECS.get(entry_family)
    if not spec:
        return {'ok': False, 'error': f'{entry_family} 不在 CHAIN_SPECS 里',
                'families': {}, 'ref_degrees': {}}

    scope = _chain_params_for_scope({
        'scope_hint': spec.get('scope_hint'),
        'up_param': spec['entry_param'],
        'down_param': spec['entry_param'],
    })

    r = CF.find_chain(exp_paths, entry_values, param_scope=scope)
    if not r.get('ok'):
        return {'ok': False, 'error': r.get('error'), 'families': {},
                'ref_degrees': {}}

    # 统计每个族的实例数，并提取「该族的身份参数」
    fam_count = {}
    fam_pk = {}
    for cmd_with_verb, insts in r['chain'].items():
        fam = cmd_with_verb.replace('ADD ', '').replace('MOD ', '').replace('SET ', '')
        fam_count[fam] = fam_count.get(fam, 0) + len(insts)
        for seq, params in insts:
            if params and fam not in fam_pk:
                fam_pk[fam] = list(params.keys())[0]

    return {
        'ok': True,
        'families': fam_count,
        'fam_pk': fam_pk,
        'ref_degrees': r.get('ref_degrees', {}),
        'stats': r.get('stats', {}),
    }


def derive_for_entry(exp_paths, entry_family, entry_values,
                     already_have=None):
    """主入口：给上游对象列表，推导所有下游族的对象名。

    already_have: 已有数据的族（数据清单给了名字的），不重复推导

    返回：[{
      'downstream_family', 'param', 'rows': [csv rows],
      'clarifications': [...], 'stats': {...}
    }]
    """
    spec = CHAIN_SPECS.get(entry_family)
    if not spec:
        return []

    already_have = already_have or set()
    out = []

    for down_fam, dspec in spec['downstream'].items():
        if down_fam in already_have:
            continue

        if not dspec.get('bind_family'):
            # 该下游族没有绑定族可参考，直接跳过（不产生澄清，避免噪音）
            continue
        pairs = _load_chain_pairs(exp_paths, dspec)
        if not pairs:
            out.append({
                'downstream_family': down_fam,
                'param': dspec['param'],
                'rows': [],
                'clarifications': [{
                    'type': '无法发现下游关系',
                    'item': f'{entry_family} → {down_fam}',
                    'reason': f'EXP 里找不到 {dspec["bind_family"]} 的配对',
                    'suggestion': '请在数据清单里直接提供下游对象名称',
                }],
                'stats': {'n_pairs': 0, 'n_derived': 0},
            })
            continue

        results = DN.derive_by_analogy(entry_values, pairs)
        rows = DN.to_csv_rows(results, family=down_fam,
                              down_param=dspec['param'])
        clars = DN.build_clarifications(results, up_family=entry_family,
                                        down_family=down_fam)
        out.append({
            'downstream_family': down_fam,
            'param': dspec['param'],
            'rows': rows,
            'clarifications': clars,
            'stats': {
                'n_pairs': len(pairs),
                'n_derived': sum(1 for r in results if r.get('derived')),
                'n_total': len(results),
            },
            'detail': results,
        })

    return out


# ═══════════════════════════════════════════════════════════
# 按需触发判据
# ═══════════════════════════════════════════════════════════
def should_run(plan_text, intent_text, dataset_sheets):
    """判断是否需要跑派生补全（按需，不是每次跑）。

    ★ 2026-11-12 弱化（用户裁定「可以弱化」）

    实测发现：agent 自己就会派生。
      NC20260803002122 的规划表写：
        「ADD POOL → POOLGROUP | high（ratio 0.859）」
        「地址池组（POOLGROUP） | sxbxrjsx4g02s_group」← 与 GT 一致
    说明 agent 能查 EXP 发现下游族，并按命名规律推出对象名。

    原 T2 判据「意图提到但清单没给」误触发率高：
      NC20260818000342 触发了，但 agent 已把 FLOWFILTER/URRGROUP 全配出来。

    新判据：只保留 T1（规划表真的缺下游族）
      即：规划表有 ADD/SET/MOD <上游族>，但完全没有 <下游族> 的任何字面出现

    返回：(bool, [触发原因])
    """
    reasons = []

    for up_fam, spec in CHAIN_SPECS.items():
        has_up = re.search(rf'(?:ADD|SET|MOD)\s+{re.escape(up_fam)}\b',
                           plan_text or '', re.I)
        if not has_up:
            continue
        for down_fam in spec['downstream']:
            if not re.search(rf'\b{re.escape(down_fam)}\b', plan_text or '', re.I):
                reasons.append(
                    f'规划表有 {up_fam} 但完全没有 {down_fam}（agent 可能漏了）')

    return bool(reasons), reasons


if __name__ == '__main__':
    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 100)
    print('派生补全验证：走链发现 + 样板推导')
    print('=' * 100)

    for tk in ['NC20260824002020', 'NC20260820001773', 'NC20260805000498']:
        g = next((x for x in GT if x['ticket'] == tk), None)
        if not g:
            continue

        pools = []
        real_map = {}
        for _, v, fam, params, raw in g['kept']:
            if fam == 'POOL' and params.get('POOLNAME'):
                pools.append(params['POOLNAME'])
            elif fam == 'POOLBINDGROUP':
                pn, gn = params.get('POOLNAME'), params.get('POOLGROUPNAME')
                if pn and gn:
                    real_map[pn] = gn

        adir = Path(g['path']) / '备份附件'
        exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []

        print(f'\n{tk}  (POOL {len(pools)} 个)')

        # Step A：走链发现
        disc = discover_downstream_families(exps, 'POOL', pools[:3])
        if disc.get('ok'):
            print(f'  [A] 走链发现: {disc["families"]}')
        else:
            print(f'  [A] 走链失败: {disc.get("error")}')

        # Step B/C/D：派生
        res = derive_for_entry(exps, 'POOL', pools)
        for item in res:
            if item['stats'].get('n_derived'):
                print(f'  [{item["downstream_family"]}] '
                      f'推导 {item["stats"]["n_derived"]}/{item["stats"]["n_total"]}'
                      f'，生成 {len(item["rows"])} 行')
            if item['clarifications']:
                print(f'  [{item["downstream_family"]}] '
                      f'{len(item["clarifications"])} 条澄清')

        # 校验
        if res and real_map:
            detail = res[0].get('detail') or []
            n_ok = n_test = 0
            for r in detail:
                if not r.get('derived'):
                    continue
                exp = real_map.get(r['upstream'])
                if not exp:
                    continue
                n_test += 1
                if r['derived'] == exp:
                    n_ok += 1
            if n_test:
                print(f'  [校验] 推导 vs GT: {n_ok}/{n_test} = {n_ok/n_test*100:.0f}%')
