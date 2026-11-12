#!/usr/bin/env python3
"""生成「参照存量」版的意图（第三版），供与原始意图、当前版对比。

用户裁定（2026-11-11）：
  「能否对照 exp，比如对 sos 按照存量的 xx 完成全量设置？」
  「尽可能像人能写出来的东西」
  「保留现在的写法，让我对比初始意图，现在的版本以及修改后的版本」

规则（数据驱动，不硬编码）：
  1. 找 GT 里重复出现 >=3 次的锚点（如 APN="sos" / USERPROFILENAME="up_sos"）
  2. 在 EXP 里找同类对象的族覆盖（同类 = 同族的其他实例值）
  3. 覆盖 >= 90%  → 「配置参照现网 <对象> 的存量做法配齐」
     覆盖 70-90%  → 「参照 <对象> 配齐，另外单独配：xxx、yyy」
     覆盖 < 70%   → 退回逐条列（不提参照，避免误导）
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}
CUR = Path('/tmp/intent_dataset')          # 当前版本（逐条列）
OUT = Path('/tmp/intent_v3')               # 参照存量版

# 锚点参数 → 中文说法
ANCHOR_CN = {
    'APN': 'APN',
    'USERPROFILENAME': '用户模板',
    'VPNINSTANCE': 'VPN 实例',
    'POOLNAME': '地址池',
    'POOLGROUPNAME': '地址池组',
    'VRFNAME': 'VPN 名称',
}

# 参照阈值
TH_FULL = 0.90     # >= 90% 认为是"配齐"
TH_PART = 0.70     # 70-90% 需要补列差额

# ★ 2026-11-12：参数级覆盖阈值（低于此值不建参照）
TH_PARAM = 0.7


def exp_fam_anchor_params(exp_text, param):
    """EXP 里 {(族, 锚点值): 参数集}。用于参数级覆盖校验。

    ★ 2026-11-12 新增（用户质疑："GT 和 EXP 不一样还写着照着 EXP 配置么？"）

    原判据只看「参照对象覆盖了几个族」，不看「覆盖了 GT 需要的哪些参数」。
    实测 NC20260806001438：
      GT 要配 USERPROFILE 的 FREESERONLCHG/FREESEROFFCHG/UPTYPE/PROFILERANGE/QOSANASW...
      EXP 的 up_ims 只有 ALIASMARKFLAG/DDOSCHECK/CAPMODETHRES/LOCRPTSWITCH/...
      交集只有 UPSPECTYPE → 参数覆盖 36%
      但族覆盖率是 100%（USERPROFILE 族存在）
      于是意图写「按 up_ims 配齐」→ 事实上 up_ims 里没那些参数
    """
    out = {}
    pat = re.compile(rf'{param}\s*=\s*"?([^",;]+)"?', re.I)
    for line in exp_text.split('\n'):
        s = line.strip()
        m = re.match(r'^(ADD|SET|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)$', s)
        if not m:
            continue
        fam, body = m.group(2), m.group(3).rstrip(';')
        pm = pat.search(body)
        if not pm:
            continue
        key = (fam, pm.group(1).strip())
        ps = set(re.findall(r'([A-Z][A-Z0-9_]*)\s*=', body))
        # 同一 (族,锚点值) 多条时取并集
        out[key] = out.get(key, set()) | ps
    return out


def calc_param_coverage(g, ref_val, anchor_param, exp_params):
    """算参照对象的【参数级】覆盖率。

    对比对象：
      GT 侧：本工单该锚点涉及的族，每个族要配的参数集
      参照侧：参照对象在同族里的参数集

    返回 (coverage_ratio, detail)
    """
    gt_map = parse_gt_anchor(g, anchor_param)     # {值: 族集合}
    my_fams = gt_map.get(None, set())             # 占位，下面重算
    # 重新算：本工单所有族 + 每族的参数集
    gt_by_fam = defaultdict(set)
    for _, v, fam, params, _ in g['kept']:
        gt_by_fam[fam] |= set(params.keys())

    # 只算「参照对象覆盖到的族」（族级覆盖已经是前提）
    ref_fams = {f for (f, _i) in exp_params if _i == ref_val}
    if not ref_fams:
        return 0.0, {'reason': '参照对象不在任何族里'}

    total_params, covered_params = 0, 0
    per_fam = {}
    for fam in ref_fams:
        need = gt_by_fam.get(fam, set())
        if not need:
            continue
        have = exp_params.get((fam, ref_val), set())
        total_params += len(need)
        covered_params += len(need & have)
        per_fam[fam] = {
            'need': sorted(need),
            'have': sorted(have),
            'missing': sorted(need - have),
        }

    ratio = covered_params / total_params if total_params else 1.0
    return ratio, {'total': total_params, 'covered': covered_params,
                   'per_fam': per_fam}


def load_exp(tk):
    g = GT_MAP.get(tk)
    if not g:
        return ''
    adir = Path(g['path']) / '备份附件'
    if not adir.exists():
        return ''
    parts = []
    for p in sorted(adir.glob('*.txt')):
        try:
            parts.append(p.read_text(encoding='utf-8', errors='replace'))
        except Exception:
            continue
    return '\n'.join(parts)


def exp_fam_anchor_values(exp_text, param):
    """EXP 里 {族: {锚点值: 条数}}。"""
    out = defaultdict(lambda: defaultdict(int))
    pat = re.compile(rf'{param}\s*=\s*"?([^",;]+)"?', re.I)
    for line in exp_text.split('\n'):
        s = line.strip()
        m = re.match(r'^(ADD|SET|MOD|RMV)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)$', s)
        if not m:
            continue
        fam, body = m.group(2), m.group(3).rstrip(';')
        pm = pat.search(body)
        if pm:
            out[fam][pm.group(1).strip()] += 1
    return out


def parse_gt_anchor(g, param):
    """GT 里 {锚点值: set(族)}。"""
    out = defaultdict(set)
    for _, v, fam, params, _ in g['kept']:
        val = params.get(param)
        if val:
            out[str(val).strip()].add(fam)
    return out


def analyze(tk):
    """对一个工单算参照方案。返回 {anchor_param, anchor_val, ref_val, fams_full, fams_extra}"""
    g = GT_MAP.get(tk)
    if not g or not g['kept']:
        return None

    exp = load_exp(tk)
    if not exp:
        return None

    # 找重复出现 >= 3 次的锚点
    anchor_cnt = Counter()
    for _, v, fam, params, _ in g['kept']:
        for k in ANCHOR_CN:
            if params.get(k):
                anchor_cnt[(k, str(params[k]).strip())] += 1

    candidates = [(k, v, n) for (k, v), n in anchor_cnt.items() if n >= 3]
    if not candidates:
        return None

    results = []
    for param, val, cnt in candidates:
        gt_map = parse_gt_anchor(g, param)          # {值: 族集合}
        my_fams = gt_map.get(val, set())             # 本工单该锚点涉及的族
        if not my_fams:
            continue

        exp_map = exp_fam_anchor_values(exp, param)  # {族: {值: 条数}}
        # 候选参照对象：EXP 里该锚点有其他值，且覆盖本族集合最多
        other_vals = set()
        for fam, vals in exp_map.items():
            for v in vals:
                if v != val:
                    other_vals.add(v)

        # ★ 2026-11-11：参照对象选择的稳定性
        #   同分时原来取"最后遍历到的"，结果不稳定（up_sos 有时参照 up_ims、
        #   有时参照 u_p_tj）。改为：
        #     第一优先：覆盖族数多
        #     第二优先：名字前缀与本对象最接近（up_sos vs up_ims 同前缀 up_）
        #     第三优先：字典序（保证可复现）
        def _prefix_score(ov):
            # 共同前缀长度
            n = 0
            for a, b in zip(val, ov):
                if a == b:
                    n += 1
                else:
                    break
            return n

        best_val, best_cov = None, set()
        best_key = None
        for ov in sorted(other_vals):
            cov = {f for f in my_fams if ov in exp_map.get(f, {})}
            key = (len(cov), _prefix_score(ov), ov)
            if best_key is None or key > best_key:
                best_val, best_cov, best_key = ov, cov, key

        if not best_val or not best_cov:
            continue

        ratio = len(best_cov) / len(my_fams)
        if ratio < TH_PART:
            continue   # 覆盖太低，不建参照

        # ★ 2026-11-12 参数级覆盖校验（用户质疑："GT 和 EXP 不一样还写着照着 EXP 配置么？"）
        #   族级覆盖通过不代表参数级覆盖：实测 NC20260806001438 族覆盖 100%
        #   但参数覆盖只有 36%（up_ims 里没 FREESERONLCHG 等 GT 要配的参数）
        exp_params = exp_fam_anchor_params(exp, param)
        p_cov, p_detail = calc_param_coverage(g, best_val, param, exp_params)
        if p_cov < TH_PARAM:
            # 参数覆盖不足 → 不建参照（退回逐条列）
            continue
        if p_cov < 1.0:
            # 部分覆盖 → 记录缺的参数，意图里要补说明
            pass
        # ★ 2026-11-11：只涉及 1 个族的，不需要「参照 XX 配齐」
        #   （实测 NC20260805000498 出现「APN「cmdtj」→ 参照「cmnet」覆盖 1/1」，
        #     一个族的配置直接说就行，参照反而啰嗦）
        if len(my_fams) < 2:
            continue

        results.append({
            'param': param, 'anchor': val, 'n_anchor': cnt,
            'ref': best_val, 'ratio': ratio,
            'param_cov': round(p_cov, 3),
            'param_missing': p_detail.get('per_fam', {}),
            'fams': sorted(my_fams),
            'covered': sorted(best_cov),
            'extra': sorted(my_fams - best_cov),
        })

    # ★ 2026-11-11：过滤互相参照（A→B 且 B→A）
    #   实测 NC20260805000498：
    #     VPN 名称「VRF_Internet」→ 参照「ChinaMobile_SGi」
    #     VPN 名称「ChinaMobile_SGi」→ 参照「VRF_Internet」
    #   两个同类对象互为参照没有意义，保留覆盖更全的那个方向。
    if results:
        pairs = {}
        for r in results:
            pairs[(r['param'], r['anchor'])] = r
        keep = []
        for r in results:
            back = pairs.get((r['param'], r['ref']))
            if back and back['ref'] == r['anchor']:
                # 互为参照：只保留覆盖族数更多的那个
                if len(r['fams']) < len(back['fams']):
                    continue
                if len(r['fams']) == len(back['fams']) and r['anchor'] > r['ref']:
                    continue
            keep.append(r)
        results = keep

    return results or None


def merge_plans(plans):
    """把「同 param、同 ref、同覆盖模式」的方案合并成一条总述。

    ★ 2026-11-11 修（实测 NC20260805000498）：
      30+ 个地址池各写一条「地址池「X」的配置：按现网「Y」配齐」，
      比原来逐条列更啰嗦。人会说「新建的 N 个地址池，都按现网 XXX 配齐」。

    合并条件：param 相同 + ref 相同 + extra 相同（即同一种配置模式）
    """
    from collections import OrderedDict
    groups = OrderedDict()
    for pl in plans:
        key = (pl['param'], pl['ref'], tuple(pl['extra']))
        if key not in groups:
            groups[key] = {
                'param': pl['param'], 'ref': pl['ref'],
                'anchors': [], 'ratio': pl['ratio'],
                'fams': pl['fams'], 'covered': pl['covered'],
                'extra': pl['extra'],
            }
        groups[key]['anchors'].append(pl['anchor'])
    return list(groups.values())


def build_v3(tk):
    """生成参照存量版意图。"""
    g = GT_MAP.get(tk)
    if not g:
        return None
    cur_p = CUR / f'{tk}_意图.md'
    if not cur_p.exists():
        return None
    cur = cur_p.read_text(encoding='utf-8')

    plans = analyze(tk)
    if plans:
        plans = merge_plans(plans)     # 同类合并（避免每个对象写一条）

    # 用参照改写：把该锚点的所有条目替换成「参照 XXX」写法
    if not plans:
        return {'tk': tk, 'text': cur, 'plans': [], 'changed': False}

    # ── 整段重建：把该锚点相关的条目抽出来，统一改写 ──
    from collections import OrderedDict
    lines = cur.split('\n')
    # 解析：分组 + 条目 + 约束
    groups = OrderedDict()
    cur_group = None
    items = []
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('【') and s.endswith('】'):
            cur_group = s
            groups.setdefault(cur_group, [])
            i += 1
            continue
        if s.startswith('- '):
            body = s[2:].strip()
            cons = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('（'):
                cons.append(lines[j].strip())
                j += 1
            groups.setdefault(cur_group or '【其他】', []).append({
                'body': body, 'cons': cons,
            })
            i = j
            continue
        i += 1

    # 每个族的动词类型（决定能否并入参照）
    #   SET  = 属性配置，同类对象之间结构相同 → 可以「照 XX 配齐」
    #   ADD/RMV = 结构性变更（新建/删除对象），必须单独说清
    fam_verbs = defaultdict(set)
    for _, v, fam, params, _ in g['kept']:
        fam_verbs[fam].add(v)

    # 对每个参照方案，把仅由 SET 组成的条目收缩
    for pl in plans:
        cn = ANCHOR_CN.get(pl['param'], pl['param'])
        ref_line_full = f'按现网同类{cn}「{pl["ref"]}」的存量做法配齐'

        # 找哪些条目属于这个锚点、且只涉及 SET 类族
        # ★ 2026-11-11：不能只看「名称为 X」的约束行。
        #   实测 NC20260805000498：POOLNAME 是主键，被选作数据清单主键列后
        #   就不再作为约束行输出，意图里只有「- 新增 地址池（见数据清单）」。
        #   改为三条判据任一命中即算：
        #     a) 约束行里有「名称为 <锚点>」
        #     b) 条目 body 直接提到锚点值（如「接口名称为 LoopBack900」）
        #     c) 条目 body 的 biz 名与锚点涉及的族同名（如「地址池」↔ POOL）
        _anchor_fams = set(pl['fams'])
        moved = []
        for gname, its in groups.items():
            keep = []
            for it in its:
                joined = ' '.join(it['cons']) + ' ' + it['body']
                # 边界保护：ims 不能命中 ims.zhs、pool-a 不能命中 pool-ab
                def _hit(a):
                    return bool(re.search(
                        rf'(?<![A-Za-z0-9_.\-]){re.escape(a)}(?![A-Za-z0-9_.\-])',
                        joined))
                hit = any(_hit(_a) for _a in pl['anchors'])
                if not hit:
                    keep.append(it)
                    continue
                # 判断这条目对应的族是不是纯 SET
                # 从 body 里反推族：用 biz 名匹配（近似）
                body = it['body']
                is_structural = any(
                    kw in body for kw in
                    ('新增', '删除')   # ADD/RMV 类动作
                )
                # 「设置」是 SET 类
                if body.startswith('设置') and not is_structural:
                    moved.append(it)
                else:
                    keep.append(it)
            groups[gname] = keep

        if not moved:
            continue
        pl['_applied'] = True

        # 该锚点写一条总述 + 差额
        target_group = None
        for gname in groups:
            if groups[gname]:
                target_group = gname
                break
        if target_group is None:
            target_group = list(groups)[0]

        _as = pl['anchors']
        if len(_as) == 1:
            _head = f'{cn}「{_as[0]}」的配置：'
        else:
            _head = f'本次涉及的 {len(_as)} 个{cn}（{_as[0]}、{_as[1]} 等）的属性配置：'
        summary = {
            'body': f'{_head}{ref_line_full}',
            'cons': [],
            'is_summary': True,
        }
        groups[target_group].insert(0, summary)

        # 差额（EXP 存量没有的族）
        if pl['extra']:
            extra_txt = '、'.join(pl['extra'])
            groups[target_group].insert(1, {
                'body': f'存量「{pl["ref"]}」没有、需单独配置的：{extra_txt}',
                'cons': [], 'is_extra': True,
            })

    # 重建文本
    new_lines = ['# ' + tk + ' — 意图', '', '需要做的变更：', '']
    for gname, its in groups.items():
        if not its:
            continue
        new_lines.append(gname)
        for it in its:
            new_lines.append('- ' + it['body'])
            for c in it['cons']:
                new_lines.append('    ' + c)
        new_lines.append('')

    # 只返回「实际并进意图」的方案（有些锚点全被 is_structural 拦下，没生效）
    applied = [pl for pl in plans if pl.get('_applied')]
    return {
        'tk': tk, 'text': '\n'.join(new_lines).rstrip() + '\n',
        'plans': applied,
        'changed': len(applied) > 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ticket', default='')
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    n_changed = 0
    n_total = 0
    detail = []

    for g in GT:
        tk = g['ticket']
        if args.ticket and tk != args.ticket:
            continue
        if not (CUR / f'{tk}_意图.md').exists():
            continue
        r = build_v3(tk)
        if not r:
            continue
        (OUT / f'{tk}_意图.md').write_text(r['text'], encoding='utf-8')
        # 数据清单照抄当前版
        src_ds = CUR / f'{tk}_数据清单.md'
        if src_ds.exists():
            (OUT / f'{tk}_数据清单.md').write_text(
                src_ds.read_text(encoding='utf-8'), encoding='utf-8')
        n_total += 1
        if r['plans']:
            n_changed += 1
            detail.append((tk, r['plans']))

    print(f'✅ 生成 {n_total} 个工单 → {OUT}')
    print(f'   应用了「参照存量」写法的: {n_changed} 个\n')
    for tk, plans in sorted(detail, key=lambda x: -len(x[1])):
        print(f'{tk}')
        for pl in plans:
            cn = ANCHOR_CN.get(pl['param'], pl['param'])
            _as = pl.get('anchors') or [pl.get('anchor', '')]
            _desc = _as[0] if len(_as) == 1 else f'{_as[0]} 等 {len(_as)} 个'
            print(f'  {cn}「{_desc}」→ 参照「{pl["ref"]}」'
                  f'  覆盖 {len(pl["covered"])}/{len(pl["fams"])} '
                  f'({pl["ratio"]*100:.0f}%)')
            if pl['extra']:
                print(f'      需单独配: {pl["extra"]}')


if __name__ == '__main__':
    main()
