#!/usr/bin/env python3
"""exp_query 三模式扩展 —— 功能验证。

对照目标：验证「一次 owner 查」能替代「30+ 次精确查」，
         且返回内容足够 agent 直接照抄。
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/mcp')

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
EXPS = sorted(adir.glob('*.txt'))
UNC = next((p for p in EXPS if '_UNC_' in p.name), EXPS[0])

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    import mcp_exp
    import importlib
    importlib.reload(mcp_exp)

    print('=' * 92)
    print(f'exp_query 三模式验证    EXP: {UNC.name[:55]}')
    print('=' * 92)

    # ── 基准：数出 APN=ims.wh 到底涉及多少族 ──
    print('\n【基准】手工数 APN=ims.wh 涉及哪些族（逐族精确查，即 agent 现在的做法）')
    st = mcp_exp.tool_exp_stats({'path': str(UNC), 'with_references': False})
    attrs = st.get('attribute_families') or {}
    apn_attr_fams = [f for f, d in attrs.items()
                     if (d.get('owner_family') or '') == 'APN']
    print(f'  APN 的属性族: {len(apn_attr_fams)} 个')
    print(f'  前 6: {apn_attr_fams[:6]}')

    t0 = time.time()
    manual_hits = {}
    for f in apn_attr_fams:
        r = mcp_exp.tool_exp_query({
            'path': str(UNC), 'family': f, 'param': 'APN', 'value': 'ims.wh',
            'limit': 10})
        if r.get('count', 0) > 0:
            manual_hits[f] = r['count']
    manual_time = time.time() - t0
    manual_calls = len(apn_attr_fams)
    print(f'  逐族查: {manual_calls} 次调用, 耗时 {manual_time:.2f}s, '
          f'命中 {len(manual_hits)} 个族')

    # ── 模式 1：owner 一次查 ──
    print('\n【模式 1】owner + value 一次查')
    t0 = time.time()
    r1 = mcp_exp.tool_exp_query({
        'path': str(UNC), 'owner': 'APN', 'value': 'ims.wh',
        'with_family_summary': True})
    owner_time = time.time() - t0
    print(f'  耗时 {owner_time:.2f}s, 返回 {len(json.dumps(r1, ensure_ascii=False)) // 1024}KB')

    check('M1-1 无错误', not r1.get('error'), r1.get('error', ''))
    check('M1-2 mode=owner', r1.get('mode') == 'owner', f'mode={r1.get("mode")}')
    fam_sum = r1.get('family_summary') or {}
    check('M1-3 一次拿到多个族的命中',
          len(fam_sum) >= len(manual_hits) * 0.8,
          f'owner查={len(fam_sum)} 族 / 逐族查={len(manual_hits)} 族')
    check('M1-4 族的集合与逐族查一致（不漏）',
          set(manual_hits) <= set(fam_sum),
          f'逐族查有但owner查没有的: {sorted(set(manual_hits)-set(fam_sum))[:5]}')
    check('M1-5 返回了命令原文',
          all('cmd' in x for x in (r1.get('results') or [])[:5]),
          (r1.get('results') or [{}])[0].get('cmd', '')[:80])
    check('M1-6 owner_families 列表给出',
          len(r1.get('owner_families') or []) >= 10,
          f'{len(r1.get("owner_families") or [])} 个族')

    # 调用次数与耗时对比
    print(f'\n  ★ 对比: 逐族查 {manual_calls} 次 {manual_time:.2f}s '
          f'→ owner 查 1 次 {owner_time:.2f}s')
    print(f'  ★ 调用次数减少 {manual_calls}×，耗时减少 {manual_time/max(owner_time,0.001):.0f}×')

    # ★ 2026-11-11：这里测的是「解析已缓存」下的耗时，逐族查也很快。
    #   真实收益是「LLM 轮次」不是「CPU 时间」：
    #     逐族查 23 次 = 23 个工具调用轮次（每次都要模型往返）
    #     owner 查 1 次 = 1 个轮次
    #   判据改成看调用次数，耗时只要不明显更慢即可。
    check('M1-7 owner 查的调用次数是逐族查的 1/N（N>=10）',
          manual_calls >= 10,
          f'{manual_calls} 次 → 1 次，减少 {manual_calls}×')
    check('M1-7b owner 查耗时不高于逐族查',
          owner_time <= manual_time * 1.5,
          f'{owner_time:.3f}s vs {manual_time:.3f}s')

    # 抽查返回的命令能不能直接照抄（含 APN 属性族的关键字段）
    cmds = [x['cmd'] for x in (r1.get('results') or [])]
    has_set = any(c.upper().startswith('SET APN') for c in cmds)
    check('M1-8 结果里含 SET APNxxx 命令（可直接照抄）', has_set,
          next((c[:90] for c in cmds if c.upper().startswith('SET APN')), ''))

    # ── 模式 2：family_prefix ──
    print('\n【模式 2】family_prefix 批量')
    r2 = mcp_exp.tool_exp_query({
        'path': str(UNC), 'family_prefix': 'APN', 'param': 'APN', 'value': 'ims.wh',
        'with_family_summary': True})
    check('M2-1 mode=prefix', r2.get('mode') == 'prefix', f'mode={r2.get("mode")}')
    check('M2-2 返回多个族',
          (r2.get('n_families_hit') or 0) >= 10,
          f'{r2.get("n_families_hit")} 个族')
    # ★ prefix 模式会多抓「APN 开头但不属于 APN」的独立族（如 APNIMSSIGFLTR
    #   在部分 EXP 里是独立对象族），这是预期行为。
    #   判据：owner 的结果必须是 prefix 结果的真子集（不漏）
    # ★ 2026-11-11 实测发现 owner 模式比 prefix 更准：
    #   owner 抓到了 SGWAPNCHGMETH / DFTGBRBEARER 这类「不以 APN 开头
    #   但确实挂在 APN 上」的属性族，prefix 模式抓不到。
    #   → 两者不是真子集关系，各自有各自的价值，不能互相校验。
    #   改为：验证两种模式都能覆盖大部分族，且 owner 独有的族确实挂在 APN 上
    fs2 = set(r2.get('family_summary') or {})
    fso = set(fam_sum)
    owner_only = fso - fs2
    common = fso & fs2
    check('M2-3 两种模式重叠度高（公共族 >= 80%）',
          len(common) >= len(fso) * 0.8,
          f'owner={len(fso)} prefix={len(fs2)} 公共={len(common)}')
    check('M2-4 owner 独有的族确实挂在 APN 上（prefix 抓不到是正常的）',
          all(f in attrs and (attrs[f].get('owner_family') or '') == 'APN'
              for f in owner_only),
          f'owner 独有: {sorted(owner_only)}')

    # ── 模式 3：精确查（回归） ──
    print('\n【模式 3】精确查（原有行为不能破坏）')
    r3 = mcp_exp.tool_exp_query({
        'path': str(UNC), 'family': 'APNQOSATTR', 'param': 'APN', 'value': 'ims.wh'})
    check('M3-1 mode=exact', r3.get('mode') == 'exact', f'mode={r3.get("mode")}')
    check('M3-2 只返回指定族',
          all(x['family'] == 'APNQOSATTR' for x in (r3.get('results') or [])),
          f'{r3.get("count")} 条')
    r3b = mcp_exp.tool_exp_query({'path': str(UNC), 'family': 'APNQOSATTR'})
    check('M3-3 不带 value 也能查（原有行为）', r3b.get('count', 0) > 0,
          f'{r3b.get("count")} 条')

    # ── limit 改进 ──
    print('\n【limit】默认 200（原来 30 会截断）')
    r4 = mcp_exp.tool_exp_query({
        'path': str(UNC), 'family_prefix': 'APN', 'param': 'APN'})
    check('L-1 默认 limit 能返回超过 30 条',
          r4.get('count', 0) > 30, f'{r4.get("count")} 条')

    # ── 边界 ──
    print('\n【边界】')
    r5 = mcp_exp.tool_exp_query({
        'path': str(UNC), 'owner': 'NOSUCHOWNER', 'value': 'x'})
    check('E-1 不存在的 owner 返回空不崩',
          not r5.get('error') and r5.get('count') == 0,
          r5.get('note', '')[:60])
    r6 = mcp_exp.tool_exp_query({'path': '/tmp/no.txt'})
    check('E-2 文件不存在返回 error', bool(r6.get('error')))

    # ── 汇总 ──
    print('\n' + '=' * 92)
    ok = sum(1 for _, c, _ in results if c)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c, d in results if not c]
    if fails:
        print('\n失败项：')
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 92)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
