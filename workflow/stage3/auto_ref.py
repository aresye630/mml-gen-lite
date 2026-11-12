"""自动选参照对象：不需要用户指定，系统自己挑最合适的。

★ 2026-11-12 重构（用户质疑："不能自己找么？"）

原设计缺陷：
  假设用户会指定参照对象（「按现网 ims.wh 配齐」）。
  但实测 86 单里：
    · 只有 17% 意图里明确提了参照对象
    · 20% 只给了业务名字
    · 58% 什么都没给（新建对象，不需要参照）

  即使是 17% 提了参照的，用户提的也可能不是最优参照：
    意图说「按 ims.wh 配齐」→ ims.wh 是 APN 层面的参照，
    但配「规则」时该参照的是别的 RULE，不是 APN 的属性。
    实测 UNC 的 r_ims_sig 缺 FLOWFILTERNAME，而 UDG 的 r_ims_sig 有。

新设计：自动选参照（评分制，不依赖 GT）
  输入（运行时可得的全部信息）：
    · 意图条目：「新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）」
    · 数据清单的列名和值
    · EXP 里同族的全部实例

  评分维度：
    D1 参数形态匹配  意图约束里提到的参数，参照对象有吗？（权重 0.4）
       例：意图说「过滤模式为FLOWFILTER」→ 参照必须有 FILTERINGMODE
    D2 约束值匹配    意图给的约束值，参照对象是否同值？（权重 0.3）
       例：意图说「策略类型为PCC」→ 参照的 POLICYTYPE 也是 PCC
    D3 形态代表性    参照所在参数形态在同族的占比（权重 0.2）
       避免选到 0.4% 的特例配置
    D4 业务相似度    参照对象名字与目标业务名字的相似度（权重 0.1）
       例：目标 sos_sig，参照 ims_sig → 都含 "_sig"

  输出：排序后的候选列表 + 每个候选的得分明细
"""
import re
from collections import Counter
from pathlib import Path

# 参数名 → 中文说法的映射（用于从意图约束里提取参数需求）
# ★ 注意：这是「业务术语 → MML 参数」的映射，不是硬编码命令模板。
#   它服务于「意图理解」，属于必要的领域词表，已在此集中维护。
PARAM_BIZ_TERMS = {
    'FILTERINGMODE': [r'过滤模式'],
    'FLOWFILTERNAME': [r'流过滤器', r'过滤器名称', r'过滤器名'],
    'POLICYTYPE': [r'策略类型'],
    'PRIORITY': [r'优先级'],
    'POLICYNAME': [r'策略组', r'策略名称'],
    'RULERANGE': [r'规则范围'],
    'APN': [r'APN\s*名称', r'APN\s*名'],
    'USERPROFILENAME': [r'用户模板名称', r'用户模板名'],
    'IFNAME': [r'接口名称', r'接口名'],
    'POOLNAME': [r'地址池名称', r'池名称', r'池名'],
    'URRNAME': [r'URR\s*名称', r'计费规则名称'],
    'VPNINSTANCE': [r'VPN\s*名称', r'VPN\s*实例'],
    'TEMPLATETYPE': [r'模板类型'],
    'UPTYPE': [r'模板类型'],
    'IPVERSION': [r'IP\s*版本'],
}

# 名字类参数（不同对象的这个参数值必然不同，不能用于值匹配评分）
NAME_LIKE_PARAMS = {
    'RULENAME', 'POLICYNAME', 'FLOWFILTERNAME', 'APN', 'USERPROFILENAME',
    'POOLNAME', 'URRNAME', 'IFNAME', 'VPNINSTANCE', 'URRPOLICYNAME',
    'PCCPOLICYGRPNM', 'URRGROUPNAME', 'USERPROFGNAME', 'NAME',
}


def extract_constraints(intent_line):
    """从意图条目里提取约束：{参数名: 值} 或 {参数名: None（只提到没给值）}。

    输入样例：
      '新增 规则（见数据清单）\\n    （策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）'

    输出：
      {'POLICYTYPE': 'PCC', 'PRIORITY': '1000', 'FILTERINGMODE': 'FLOWFILTER'}
    """
    if not intent_line:
        return {}

    out = {}
    for param, patterns in PARAM_BIZ_TERMS.items():
        for pat in patterns:
            # 匹配「XX为YYY」或「XX 为 YYY」
            m = re.search(rf'{pat}\s*为\s*([A-Za-z0-9_\-\.]+)', intent_line)
            if m:
                out[param] = m.group(1)
                break
            # 只提到没给值
            if re.search(pat, intent_line, re.I):
                if param not in out:
                    out[param] = None
                break
    return out


def score_candidate(target_family, target_constraints, target_biz,
                    candidate_params, candidate_name, family_shape_share):
    """给一个候选参照打分。

    参数：
      target_family         目标族名
      target_constraints    意图约束 {参数: 值}
      target_biz            目标业务段（如 'sos' / 'sos_sig'），可为 None
      candidate_params      候选的参数集 {参数: 值}
      candidate_name        候选对象名
      family_shape_share    候选所在形态在同族的占比

    返回：
      {'score': 0-1, 'd1': ..., 'd2': ..., 'd3': ..., 'd4': ..., 'reasons': [...]}
    """
    reasons = []

    # ── D1 参数形态匹配（0.4）──
    want_params = set(target_constraints.keys())
    if want_params:
        have = want_params & set(candidate_params.keys())
        d1 = len(have) / len(want_params)
        if d1 < 1.0:
            missing = sorted(want_params - set(candidate_params.keys()))
            reasons.append(f'缺意图要求的参数: {", ".join(missing)}')
    else:
        d1 = 1.0   # 没有约束要求，默认满分

    # ── D2 约束值匹配（0.3）──
    #   只比较「非名字类」且有明确值的约束
    cmp_params = [p for p, v in target_constraints.items()
                  if v is not None and p not in NAME_LIKE_PARAMS
                  and p in candidate_params]
    if cmp_params:
        matched = sum(1 for p in cmp_params
                      if str(candidate_params[p]).upper() == str(target_constraints[p]).upper())
        d2 = matched / len(cmp_params)
        if d2 < 1.0:
            diff = [p for p in cmp_params
                    if str(candidate_params[p]).upper() != str(target_constraints[p]).upper()]
            reasons.append(f'约束值不符: {", ".join(diff)}')
    else:
        d2 = 1.0

    # ── D3 形态代表性（0.2）──
    d3 = min(1.0, family_shape_share / 0.5)   # 占比 >= 50% 满分
    if family_shape_share < 0.02:
        reasons.append(f'该形态仅占 {family_shape_share*100:.1f}%，可能是特例')

    # ── D4 业务相似度（0.1）──
    d4 = 0.5    # 中性默认
    if target_biz and candidate_name:
        tb = target_biz.lower().replace('_', '')
        cn = candidate_name.lower().replace('_', '')
        # 长公共子串 > 3 视为相似
        common = 0
        for ln in range(min(len(tb), len(cn)), 2, -1):
            found = False
            for i in range(len(tb) - ln + 1):
                if tb[i:i+ln] in cn:
                    common = ln
                    found = True
                    break
            if found:
                break
        if common >= 4:
            d4 = 1.0
            reasons.append(f'名字与目标业务有 {common} 字符公共段')
        elif common >= 3:
            d4 = 0.7

    score = d1 * 0.4 + d2 * 0.3 + d3 * 0.2 + d4 * 0.1
    return {'score': round(score, 3), 'd1': round(d1, 2), 'd2': round(d2, 2),
            'd3': round(d3, 2), 'd4': round(d4, 2), 'reasons': reasons}


def collect_family_instances(exp_paths, family):
    """收集某族在所有 EXP 里的实例，含形态统计。

    返回：
      {
        'instances': [{'name', 'params', 'exp', 'shape_share'}],
        'shape_stats': {frozenset(params): count},
        'exp_total': {exp: n},
      }
    """
    if isinstance(exp_paths, (str, Path)):
        exp_paths = [exp_paths]

    instances = []
    shape_stats = Counter()
    exp_total = {}

    for ep in exp_paths:
        p = Path(ep)
        if not p.exists():
            continue
        n_this = 0
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    m = re.match(rf'^ADD\s+{re.escape(family)}\s*:\s*(.*)', s)
                    if not m:
                        continue
                    rest = m.group(1)
                    ps = {}
                    for pm in re.finditer(
                            r'([A-Z][A-Z0-9_]*)\s*=\s*(?:"([^"]*)"|([^,\s;]+))', rest):
                        ps[pm.group(1)] = (pm.group(2) if pm.group(2) is not None
                                           else pm.group(3))
                    if not ps:
                        continue
                    name = next(iter(ps.values()))
                    shape = frozenset(ps.keys())
                    instances.append({'name': name, 'params': ps,
                                      'exp': str(p), 'shape': shape})
                    shape_stats[shape] += 1
                    n_this += 1
        except Exception:
            continue
        exp_total[str(p)] = n_this

    total = len(instances)
    for inst in instances:
        inst['shape_share'] = (shape_stats[inst['shape']] / total
                               if total else 0)

    return {'instances': instances, 'shape_stats': shape_stats,
            'exp_total': exp_total, 'total': total}


def auto_select_reference(exp_paths, family, intent_line, target_biz=None,
                          top_k=5, min_score=0.5):
    """自动选参照对象（不依赖 GT，只用意图约束 + EXP）。

    返回：
      {
        'family': 'RULE',
        'constraints': {...},        # 从意图提取的约束
        'candidates': [...],          # 按得分排序
        'best': {...} 或 None,
        'reason': '...'               # 选择理由
      }
    """
    constraints = extract_constraints(intent_line)
    info = collect_family_instances(exp_paths, family)

    if info['total'] == 0:
        return {'family': family, 'constraints': constraints,
                'candidates': [], 'best': None,
                'reason': f'所有 EXP 里都没有 {family} 的实例'}

    scored = []
    for inst in info['instances']:
        sc = score_candidate(family, constraints, target_biz,
                             inst['params'], inst['name'],
                             inst['shape_share'])
        if sc['score'] < min_score:
            continue
        scored.append({
            'name': inst['name'],
            'exp': Path(inst['exp']).name,
            'score': sc['score'],
            'detail': sc,
            'n_params': len(inst['params']),
            'shape_share': round(inst['shape_share'], 3),
        })

    # 去重：同名对象在多个 EXP 里，保留得分最高的
    best_by_name = {}
    for c in scored:
        key = c['name']
        if key not in best_by_name or c['score'] > best_by_name[key]['score']:
            best_by_name[key] = c

    ranked = sorted(best_by_name.values(),
                    key=lambda x: (-x['score'], -x['shape_share']))
    ranked = ranked[:top_k]

    best = ranked[0] if ranked else None
    if best:
        reason = (f'自动选中 {best["name"]}（{best["exp"][:40]}），'
                  f'得分 {best["score"]}')
        if best['detail']['reasons']:
            reason += '；' + '；'.join(best['detail']['reasons'][:2])
    else:
        reason = '没有候选达到最低分，建议人工指定参照或按标准写法生成'

    return {'family': family, 'constraints': constraints,
            'candidates': ranked, 'best': best, 'reason': reason,
            'family_total': info['total']}


if __name__ == '__main__':
    import json
    import sys

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    adir = Path(g['path']) / '备份附件'
    UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)
    UDG = next((p for p in adir.glob('*.txt') if '_UDG_' in p.name), None)

    print('=' * 92)
    print('自动选参照自测')
    print('=' * 92)

    # 意图里「规则」那一条
    LINE = '新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）'
    print(f'\n意图行: {LINE}')
    c = extract_constraints(LINE)
    print(f'提取约束: {c}')

    r = auto_select_reference([str(UNC), str(UDG)], 'RULE', LINE,
                              target_biz='sos_sig')
    print(f'\n{r["reason"]}')
    print(f'\n候选 TOP 5（共 {r["family_total"]} 个实例）:')
    print(f'{"得分":>5} {"D1":>4} {"D2":>4} {"D3":>4} {"D4":>4} {"对象名":<26} {"网元"}')
    print('-' * 80)
    for c0 in r['candidates']:
        d = c0['detail']
        print(f'{c0["score"]:>5.2f} {d["d1"]:>4.1f} {d["d2"]:>4.1f} '
              f'{d["d3"]:>4.1f} {d["d4"]:>4.1f} {c0["name"]:<26} {c0["exp"][:18]}')
