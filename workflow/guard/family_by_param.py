"""G34：根据参数反推正确的命令族（族名写错检测）。

★ 2026-11-12（从 15 单失败分析得出）

## 实测问题

agent 反复犯同一个错：把 APN 属性族的族名全写成 `APNAFFUNC`。

  NC20260828000360 的产物：
    L33: SET APNAFFUNC:APNNAME=sos, CFSWITCHVALUE=DISABLE;   // @src=exp:L102415
         ↑ 族名错                      ↑ CFSWITCHVALUE 属于 APNCFFUNC
    L39: SET APNAFFUNC:APN="sos", TRAFFICFDSW=DISABLE;      // @src=exp:L102367
         ↑ 族名错                 ↑ TRAFFICFDSW 属于 APNTRAFDFUNC

  而 EXP 里对应的行是：
    L102415: SET APNCFFUNC:APNNAME="...", CFSWITCHVALUE=DISABLE;
    L102367: SET APNTRAFDFUNC:APN="...", TRAFFICFDSW=DISABLE;

  → agent 参数抄对了，但族名全写成了 APNAFFUNC。

## 判据（数据驱动）

从 EXP 学「参数 → 族」映射：
  · 82/85 个参数唯一属于某个族（实测 29 个 EXP）
  · CFSWITCHVALUE → APNCFFUNC（2351 次，唯一）
  · TRAFFICFDSW → APNTRAFDFUNC（2351 次，唯一）

判定：如果命令的「专有参数」全部指向另一个族，说明族名写错了。

  例：SET APNAFFUNC:APN="x", TRAFFICFDSW=DISABLE;
      · 专有参数 = {TRAFFICFDSW}（APN 是主键，不算）
      · TRAFFICFDSW 唯一属于 APNTRAFDFUNC
      · 当前族 APNAFFUNC ≠ APNTRAFDFUNC
      → 报「族名写错，应为 APNTRAFDFUNC」

## 分级

  fatal：专有参数 100% 指向另一个族，且该族在原族里从未出现过这些参数
  warn ：部分参数指向另一个族（可能是多族共用参数）
"""
import re
from collections import defaultdict
from pathlib import Path

# 主键类参数（不算「专有参数」，它们是对象标识）
KEY_PARAMS = {
    'APN', 'APNNAME', 'DNN', 'VRFNAME', 'VPNINSTANCE', 'POLICYNAME',
    'IFNAME', 'POOLNAME', 'URRNAME', 'URRGROUPNAME', 'RULENAME',
    'USERPROFILENAME', 'FILTERNAME', 'FLOWFILTERNAME', 'HOSTNAME',
    'POOLGRPNAME', 'PCCPOLICYGRPNM', 'TNLNAME', 'MAPPINGNAME',
}

# 缓存
_PARAM_FAM_INDEX = {}


def build_param_family_index(exp_paths=None, exp_text=''):
    """从 EXP 建 {参数名: {族名: 次数}} 索引。

    只统计「属性族」（SET/MOD 类，非对象创建族）：
      因为对象族（ADD POOL/APN）的参数是各种属性大杂烩，
      对族名纠错没意义。
    """
    idx = defaultdict(lambda: defaultdict(int))

    def _feed(text):
        for line in text.split('\n'):
            s = line.split('//')[0].strip()
            m = re.match(r'^(SET|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)', s, re.I)
            if not m:
                continue
            fam = m.group(2).upper()
            for pm in re.finditer(r'([A-Z][A-Z0-9_]*)\s*=', m.group(3)):
                idx[pm.group(1).upper()][fam] += 1

    for p in (exp_paths or []):
        try:
            _feed(Path(p).read_text(encoding='utf-8', errors='replace'))
        except Exception:
            continue
    if exp_text:
        _feed(exp_text)

    return {k: dict(v) for k, v in idx.items()}


def get_param_family_index(exp_paths=None, exp_text=''):
    """带缓存的索引（EXP 只解析一次）。"""
    key = (tuple(sorted(exp_paths or [])), len(exp_text or ''))
    if key not in _PARAM_FAM_INDEX:
        _PARAM_FAM_INDEX[key] = build_param_family_index(exp_paths, exp_text)
    return _PARAM_FAM_INDEX[key]


def check_family_by_params(mml_text, exp_paths=None, exp_text='', strict=True):
    """G34：根据参数反推命令族，检测族名写错。

    返回：{
      'ok': bool,
      'n_checked': int,
      'suspects': [{'line_no','family','should_be','params','why'}],
      'fatal': [...], 'warn': [...]
    }
    """
    if not mml_text:
        return {'ok': True, 'skipped': True, 'reason': 'no mml'}

    idx = get_param_family_index(exp_paths, exp_text)
    if not idx:
        return {'ok': True, 'skipped': True, 'reason': 'no exp index'}

    suspects = []
    n_checked = 0

    for line_no, raw in enumerate(mml_text.split('\n'), 1):
        s = raw.split('//')[0].strip()
        m = re.match(r'^(SET|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)', s, re.I)
        if not m:
            continue
        verb, fam, body = m.group(1).upper(), m.group(2).upper(), m.group(3)
        n_checked += 1

        # 提取参数（排除主键）
        params = [pm.group(1).upper() for pm in
                  re.finditer(r'([A-Z][A-Z0-9_]*)\s*=', body)]
        attr_params = [p for p in params if p not in KEY_PARAMS]
        if not attr_params:
            continue

        # 每个参数的归属族
        votes = defaultdict(int)
        detail = {}
        for p in attr_params:
            fams = idx.get(p, {})
            if not fams:
                continue
            # 取该参数最主要的族
            best_fam = max(fams.items(), key=lambda x: x[1])[0]
            votes[best_fam] += 1
            detail[p] = best_fam

        if not votes:
            continue

        # 如果所有专有参数都指向另一个族（且不是当前族）
        top_fam, top_n = max(votes.items(), key=lambda x: x[1])
        if top_fam == fam:
            continue
        if top_n < len(attr_params) * (1.0 if strict else 0.6):
            continue

        # 检查参数是否真的在原族里从没出现过
        orig_fams_for_params = set()
        for p in attr_params:
            orig_fams_for_params |= set(idx.get(p, {}).keys())
        if fam in orig_fams_for_params:
            # 该族确实用过这些参数 → 不是写错
            continue

        suspects.append({
            'line_no': line_no,
            'family': fam,
            'should_be': top_fam,
            'params': attr_params,
            'why': f'参数 {attr_params} 在 EXP 里只属于 {top_fam}，不属于 {fam}',
            'line': raw.strip()[:150],
        })

    fatal = suspects if strict else []
    warn = [] if strict else suspects

    return {
        'ok': not suspects,
        'n_checked': n_checked,
        'suspects': suspects,
        'fatal': fatal,
        'warn': warn,
    }


if __name__ == '__main__':
    import json

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 100)
    print('G34：根据参数反推命令族')
    print('=' * 100)

    # 建索引
    all_exps = []
    for g in GT[:30]:
        if not g['kept']:
            continue
        adir = Path(g['path']) / '备份附件'
        if adir.exists():
            all_exps.extend(str(p) for p in sorted(adir.glob('*.txt'))[:1])

    idx = build_param_family_index(all_exps)
    print(f'\n索引: {len(idx)} 个参数, 扫 {len(all_exps)} 个 EXP')
    uniq = sum(1 for v in idx.values() if len(v) == 1)
    print(f'唯一归属: {uniq}/{len(idx)} = {uniq/len(idx)*100:.0f}%')

    # 测试用例
    TESTS = [
        ('族名写错（APNAFFUNC + CFSWITCHVALUE）',
         'SET APNAFFUNC:APNNAME="sos", CFSWITCHVALUE=DISABLE;'),
        ('族名写错（APNAFFUNC + TRAFFICFDSW）',
         'SET APNAFFUNC:APN="sos", TRAFFICFDSW=DISABLE;'),
        ('族名正确（APNCFFUNC + CFSWITCHVALUE）',
         'SET APNCFFUNC:APNNAME="sos", CFSWITCHVALUE=DISABLE;'),
        ('族名正确（APNAFFUNC + ISENABLE）',
         'SET APNAFFUNC:APN="sos", ISENABLE=ENABLE;'),
        ('正常命令（非属性族）',
         'ADD POOL:POOLNAME="p1", POOLTYPE=EXTERNAL;'),
    ]

    for label, mml in TESTS:
        r = check_family_by_params(mml, all_exps)
        print(f'\n{label}')
        print(f'  结果: {"✅ pass" if r["ok"] else "❌ 检出"}')
        for s in r['suspects']:
            print(f'    L{s["line_no"]}: {s["family"]} → 应为 {s["should_be"]}')
            print(f'      {s["why"]}')
