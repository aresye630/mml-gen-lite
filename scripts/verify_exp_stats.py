#!/usr/bin/env python3
"""exp_stats 四层模型重写 —— 功能级验证。

每个用例验证一个具体能力，全部用真实 EXP 数据，可独立判断真假。

用例：
  T1 兼容性     旧 key families / family_count 仍在，且语义不变（只含对象族）
  T2 对象族     ADD 型族全部被识别，身份参数正确
  T3 属性族     SET-only 族不再丢失，且能识别归属对象
  T4 数量守恒   对象族 + 属性族 == EXP 里的全部族（不再丢 82%）
  T5 引用关联   已知的强引用（FLTBINDFLOWF→FLOWFILTER/FILTER）被识别
  T6 行为参数   身份参数/引用参数不算行为参数，PRIORITY 给出区间
  T7 过滤       family= 参数只返回指定族，两个层都过滤
  T8 缓存       同参数二次调用命中缓存，结果一致
  T9 性能       大文件（15MB+）单次调用耗时在可接受范围
  T10 边界      不存在的文件 / 空 family 不崩
"""
import json
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/mcp')

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260806001780'      # GT 41 族，其中 13 族是 SET-only
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'


def _profile(p):
    """统计一个 EXP 的族数与各层规模。"""
    fams, add_fams, has_set = set(), set(), 0
    try:
        with open(p, encoding='utf-8', errors='replace') as f:
            for line in f:
                m = re.match(r'^(ADD|SET|MOD|RMV)\s+([A-Z][A-Z0-9_]+)', line)
                if m:
                    fams.add(m.group(2))
                    if m.group(1) == 'ADD':
                        add_fams.add(m.group(2))
                    else:
                        has_set += 1
    except Exception:
        pass
    return {'fams': fams, 'add': add_fams, 'has_set': has_set,
            'size': p.stat().st_size}


def _pick_exp(pred):
    """按条件挑 EXP（条件写在 pred 里），多个候选取族数最多的。"""
    cands = [(p, _profile(p)) for p in sorted(adir.glob('*.txt'))]
    cands = [(p, pr) for p, pr in cands if pred(pr)]
    if not cands:
        return None
    cands.sort(key=lambda x: -len(x[1]['fams']))
    return cands[0][0]


# 主验证用 UDG EXP（大文件、族最全、含 FLTBINDFLOWF/SECTION）
EXP = _pick_exp(lambda pr: {'FLTBINDFLOWF', 'SECTION', 'POOL'} <= pr['fams'])
if EXP is None:
    EXP = _pick_exp(lambda pr: len(pr['fams']) > 50)
if EXP is None:
    raise SystemExit('没有可用的 EXP')

# 顺带找一个有 SET-only 族的 EXP，单独验证属性族与归属
EXP_ATTR = _pick_exp(lambda pr: len(pr['fams'] - pr['add']) >= 5)
print(f'  主 EXP  : {EXP.name}')
if EXP_ATTR and EXP_ATTR != EXP:
    print(f'  属性族 EXP: {EXP_ATTR.name}')

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    mark = '✅' if cond else '❌'
    print(f'  {mark} {name}' + (f'  —— {detail}' if detail else ''))
    return cond


def main():
    import mcp_exp
    import importlib
    importlib.reload(mcp_exp)

    print('=' * 90)
    print(f'exp_stats 四层模型验证   EXP: {EXP.name} ({EXP.stat().st_size // 1024}KB)')
    print('=' * 90)

    # ── 基准：用独立实现算出真值 ──
    print('\n【基准】独立解析 EXP 得真值')
    all_fams, add_fams, nonadd_fams = set(), set(), set()
    fam_verbs = {}
    t0 = time.time()
    with open(EXP, encoding='utf-8', errors='replace') as f:
        for line in f:
            m = re.match(r'^(ADD|SET|MOD|RMV)\s+([A-Z][A-Z0-9_]+)', line)
            if not m:
                continue
            v, fam = m.group(1), m.group(2)
            all_fams.add(fam)
            fam_verbs.setdefault(fam, set()).add(v)
    add_fams = {f for f, vs in fam_verbs.items() if 'ADD' in vs}
    nonadd_fams = all_fams - add_fams
    print(f'  全族 {len(all_fams)}  对象族(ADD) {len(add_fams)}  '
          f'属性族(SET/MOD/RMV only) {len(nonadd_fams)}   '
          f'(独立解析 {time.time()-t0:.1f}s)')

    # ── 调用新版 ──
    print('\n【调用】exp_stats(path=EXP)')
    t0 = time.time()
    r = mcp_exp.tool_exp_stats({'path': str(EXP)})
    el = time.time() - t0
    if r.get('error'):
        print(f'  ❌ 报错: {r["error"]}')
        return
    print(f'  返回 {len(json.dumps(r, ensure_ascii=False)) // 1024}KB，耗时 {el:.2f}s')

    L = r.get('layers') or {}
    print(f'  layers: {json.dumps(L, ensure_ascii=False)}')

    # ── T1 兼容性 ──
    print('\n【T1】兼容性（旧调用方 mcp_knowledge 依赖 families / family_count）')
    fams_old = r.get('families') or {}
    check('families key 存在', bool(fams_old))
    check('family_count 存在', 'family_count' in r)
    check('families 只含对象族（与 object_families 一致）',
          set(fams_old) == set(r.get('object_families') or {}),
          f'families={len(fams_old)} object_families={len(r.get("object_families") or {})}')
    check('family_count == len(families)',
          r.get('family_count') == len(fams_old),
          f'{r.get("family_count")} vs {len(fams_old)}')
    # 旧字段仍在
    some = next(iter(fams_old.values()))
    check('旧字段 count / sample_names / name_patterns 仍在',
          all(k in some for k in ('count', 'sample_names')),
          f'keys={sorted(some)}')

    # ── T2 对象族 ──
    print('\n【T2】对象族识别')
    obj = r.get('object_families') or {}
    check('对象族数量 == 独立解析的 ADD 族数',
          len(obj) == len(add_fams),
          f'{len(obj)} vs {len(add_fams)}')
    check('对象族集合完全一致',
          set(obj) == add_fams,
          f'差集: 多={sorted(set(obj)-add_fams)[:5]} 少={sorted(add_fams-set(obj))[:5]}')
    # 身份参数抽查
    id_ok = 0
    id_samples = [('RULE', 'RULENAME'), ('FLOWFILTER', 'FLOWFILTERNAME'),
                  ('POOL', 'POOLNAME'), ('USERPROFILE', 'USERPROFILENAME')]
    for fam, expect_ip in id_samples:
        if fam in obj:
            got = obj[fam].get('identity_param')
            if got == expect_ip:
                id_ok += 1
            else:
                print(f'      {fam}: 期望 {expect_ip} 实际 {got}')
    check('身份参数正确（4 个抽样族）', id_ok == len(id_samples),
          f'{id_ok}/{len(id_samples)}')

    # ── T3 属性族 ──
    print('\n【T3】属性族识别（旧版全丢的部分）')
    attr = r.get('attribute_families') or {}
    check('属性族数量 == 独立解析的 SET-only 族数',
          len(attr) == len(nonadd_fams),
          f'{len(attr)} vs {len(nonadd_fams)}')
    # GT 里"看不见"的 13 族现在应该都在
    gt_fams = {f for _, _, f, _, _ in g['kept']}
    gt_invisible = ['APNADDRESSATTR', 'APNCHARGECTRL', 'APNIDLETIME', 'APNIMSATTR',
                    'APNIPALLOCRULE', 'APNPCCFUNC', 'APNQOSATTR', 'APNSGLPASS',
                    'APNSOFTPARA', 'DBPARAS', 'LICENSESWITCH', 'REFRESHSRV',
                    'URRGRPBINDING']
    # 只检查「这个 EXP 里确实存在」的族（其他网元的族不在本文件里，属正常）
    present = [f for f in gt_invisible if f in all_fams]
    now_visible = [f for f in present if f in attr or f in obj]
    check('GT 里原本不可见、且本 EXP 含有的族现在全部可见',
          len(now_visible) == len(present),
          f'{len(now_visible)}/{len(present)}（EXP 含 {len(present)}/13），缺: '
          f'{[f for f in present if f not in now_visible]}')
    # 归属对象识别
    # 已知归属的属性族（挑本 EXP 里存在的）
    #   IFIPV6ENABLE / NDIFCONFIG 挂在 INTERFACE 上（参数 IFNAME）
    #   APNCHARGECTRL / APNIDLETIME 挂在 APN 上（参数 APN）
    # 已知归属的属性族分两类：
    #   A 类：参数名有语义（APN / IFNAME / USERPROFILENAME）→ 必须判对
    #   B 类：参数名是通用名（NAME / ID / INDEX）→ 允许返回 None（判不准就不猜），
    #         但候选列表里必须包含真值，让 agent 自己决定
    KNOWN_A = [('APNCHARGECTRL', 'APN'), ('APNIDLETIME', 'APN'),
               ('APNQOSATTR', 'APN'), ('IFIPV6ENABLE', 'INTERFACE'),
               ('NDIFCONFIG', 'INTERFACE'), ('URRGRPBINDING', 'USERPROFILE')]
    KNOWN_B = [('UPGPATTIMER', 'LOGICINF')]     # 参数名是通用 NAME

    a_cases = [(f, o) for f, o in KNOWN_A if f in all_fams]
    a_ok = 0
    for fam, expect_owner in a_cases:
        got = (attr.get(fam) or {}).get('owner_family')
        if got == expect_owner:
            a_ok += 1
        else:
            print(f'      {fam}: 期望 owner={expect_owner} 实际 {got}')
    if a_cases:
        check(f'A 类属性族归属正确（参数名有语义，{len(a_cases)} 个）',
              a_ok == len(a_cases), f'{a_ok}/{len(a_cases)}')

    b_cases = [(f, o) for f, o in KNOWN_B if f in all_fams]
    b_ok = 0
    for fam, expect_owner in b_cases:
        d = attr.get(fam) or {}
        got = d.get('owner_family')
        cands = d.get('owner_candidates') or []
        if got == expect_owner or (got is None and expect_owner in cands):
            b_ok += 1
        else:
            print(f'      {fam}: 期望 owner={expect_owner} 或 None+候选含它，'
                  f'实际 owner={got} 候选={cands}')
    if b_cases:
        check(f'B 类属性族（通用参数名）判对或安全降级（{len(b_cases)} 个）',
              b_ok == len(b_cases), f'{b_ok}/{len(b_cases)}')

    # ── T4 数量守恒 ──
    print('\n【T4】数量守恒（旧版丢 82%，新版必须 0 丢失）')
    total_new = len(obj) + len(attr)
    check('对象族 + 属性族 == EXP 全部族',
          total_new == len(all_fams),
          f'{total_new} vs {len(all_fams)}')
    check('family_count_all 正确',
          r.get('family_count_all') == len(all_fams),
          f'{r.get("family_count_all")} vs {len(all_fams)}')
    lost = all_fams - set(obj) - set(attr)
    check('无族丢失', not lost, f'丢失: {sorted(lost)[:8]}')

    # ── T5 引用关联 ──
    print('\n【T5】引用关联（第三层）')
    refs = r.get('references') or {}
    check('references 非空', bool(refs), f'{len(refs)} 个族有引用')
    # 已知强引用
    def has_ref(fam, param, target):
        for it in (refs.get(fam) or []):
            if it['param'] == param and it['target_family'] == target:
                return it['n']
        return 0
    n1 = has_ref('FLTBINDFLOWF', 'FLOWFILTERNAME', 'FLOWFILTER')
    n2 = has_ref('FLTBINDFLOWF', 'FILTERNAME', 'FILTER')
    n3 = has_ref('RULEBINDING', 'RULENAME', 'RULE')
    n4 = has_ref('SECTION', 'POOLNAME', 'POOL')
    check('FLTBINDFLOWF.FLOWFILTERNAME → FLOWFILTER', n1 > 0, f'{n1} 次')
    check('FLTBINDFLOWF.FILTERNAME → FILTER', n2 > 0, f'{n2} 次')
    check('RULEBINDING.RULENAME → RULE', n3 > 0, f'{n3} 次')
    check('SECTION.POOLNAME → POOL', n4 > 0, f'{n4} 次')
    check('layers.L3 有统计',
          (L.get('L3_references') or {}).get('n_ref_edges', 0) > 0,
          json.dumps(L.get('L3_references') or {}, ensure_ascii=False))

    # ── T6 行为参数 ──
    print('\n【T6】行为参数（第四层）')
    # RULE 有 PRIORITY / FLOWFILTERNAME / POLICYNAME
    rule = obj.get('RULE') or {}
    rule_refs = rule.get('references') or []
    # ★ 2026-11-11：FLOWFILTERNAME 可能指向 FLOWFILTER / FILTERIPV6 等多个族
    #   （它们的身份参数都叫 FLOWFILTERNAME），所以要看「参数 + 目标族」
    has_ff = any(x['param'] == 'FLOWFILTERNAME' and x['target_family'] == 'FLOWFILTER'
                 for x in rule_refs)
    has_pol = any(x['param'] == 'POLICYNAME' for x in rule_refs)
    check('RULE.FLOWFILTERNAME → FLOWFILTER（PPT 里的例子）', has_ff,
          f'refs={[(x["param"], x["target_family"]) for x in rule_refs]}')
    check('RULE.POLICYNAME → 策略族', has_pol,
          f'refs={[(x["param"], x["target_family"]) for x in rule_refs]}')
    check('RULE 的 priority_range 正确',
          bool(rule.get('priority_range')),
          f'{rule.get("priority_range")}')
    # 引用参数不能出现在行为参数 enums 里
    rule_enums = set((rule.get('enums') or {}))
    check('行为参数不含引用参数（FLOWFILTERNAME/POLICYNAME）',
          not (rule_enums & {'FLOWFILTERNAME', 'POLICYNAME'}),
          f'enums={sorted(rule_enums)}')
    check('layers.L4 有统计',
          (L.get('L4_behavior') or {}).get('families_with_behavior_params', 0) > 0,
          json.dumps(L.get('L4_behavior') or {}, ensure_ascii=False))

    # ── T7 过滤 ──
    print('\n【T7】family 过滤')
    # 挑本 EXP 里真实存在的一个属性族来测
    some_attr = next(iter(attr), None)
    if some_attr:
        r2 = mcp_exp.tool_exp_stats({'path': str(EXP), 'family': some_attr})
        check(f'属性族可单独过滤出来（{some_attr}）',
              some_attr in (r2.get('attribute_families') or {}),
              f'attr={list((r2.get("attribute_families") or {}).keys())}')
    else:
        print('      （本 EXP 无属性族，跳过）')
    r3 = mcp_exp.tool_exp_stats({'path': str(EXP), 'family': 'RULE'})
    check('对象族可单独过滤出来',
          'RULE' in (r3.get('object_families') or {}))
    check('过滤后另一层为空',
          not (r3.get('attribute_families') or {}),
          f'{list((r3.get("attribute_families") or {}).keys())}')

    # ── T8 缓存 ──
    print('\n【T8】缓存')
    t0 = time.time()
    r4 = mcp_exp.tool_exp_stats({'path': str(EXP)})
    el2 = time.time() - t0
    check('二次调用走缓存（<0.1s）', el2 < 0.1, f'{el2*1000:.0f}ms')
    check('缓存结果一致',
          r4.get('family_count_all') == r.get('family_count_all'),
          f'{r4.get("family_count_all")} vs {r.get("family_count_all")}')

    # ── T9 性能 ──
    print('\n【T9】性能')
    mcp_exp._RESULT_CACHE.clear()
    t0 = time.time()
    mcp_exp.tool_exp_stats({'path': str(EXP)})
    cold = time.time() - t0
    check('冷启动 < 60s', cold < 60, f'{cold:.1f}s')
    t0 = time.time()
    mcp_exp.tool_exp_stats({'path': str(EXP), 'with_references': False})
    no_ref = time.time() - t0
    check('with_references=False 更快或相当', no_ref <= cold * 1.2,
          f'{no_ref:.1f}s vs {cold:.1f}s')

    # ── T10 边界 ──
    print('\n【T10】边界')
    r5 = mcp_exp.tool_exp_stats({'path': '/tmp/not_exist.txt'})
    check('不存在文件返回 error 不崩', bool(r5.get('error')))
    r6 = mcp_exp.tool_exp_stats({'path': str(EXP), 'family': 'NOSUCHFAMILY'})
    check('不存在的族返回空而非崩',
          not (r6.get('object_families') or {})
          and not (r6.get('attribute_families') or {})
          and not r6.get('error'))
    r7 = mcp_exp.tool_exp_stats({'path': str(EXP), 'family': ''})
    check('family 空字符串 == 不过滤',
          r7.get('family_count_all') == r.get('family_count_all'))

    # ── 汇总 ──
    print('\n' + '=' * 90)
    ok = sum(1 for _, c, _ in results if c)
    total = len(results)
    print(f'结果: {ok}/{total} 通过')
    fails = [(n, d) for n, c, d in results if not c]
    if fails:
        print('\n失败项：')
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 90)
    return 0 if ok == total else 1


if __name__ == '__main__':
    sys.exit(main())
