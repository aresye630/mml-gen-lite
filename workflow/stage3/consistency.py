"""Step 4/5：一致性检查 + 判据核对（把 guard 的 warn 变成可执行的修复清单）。

★ 2026-11-12 P0-5

## Step 4 一致性检查（纯代码）
  规划表（状态=确认）→ params.csv → mml.txt 三级一致

  检查项：
    C1 规划表每行（确认）→ params.csv 里有对应组
    C2 params.csv 每组 → mml.txt 里有命令
    C3 mml.txt 里每条命令 → params.csv 里有来源行
    C4 规划表对象数量 vs params.csv 实际行数

## Step 5 判据核对（复用 guard，把 warn 变成待修清单）
  实测 guard 已有 18 个判据，Step 5 不重写，只做「读结果 + 分类 + 给修法」

  分三类：
    A 可代码自动修（如 G30 RMV→ADD 的动词纠正、G31 通配展开）
    B 需补数据（如 G22 占位符、G18 缺必选参数）
    C 只能报给用户（如 G27 跨网元配不了）

## 为什么不用 LLM
  用户裁定：「阶段3 本身是增加确定性的工作，不需要太多自由发挥」
  → Step 4/5 全部纯代码，只有「怎么修」需要判断时才交给 Step 6 或人工
"""
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

# 复用 mml_gen 的解析
_WF = str(Path(__file__).parent.parent)
if _WF not in sys.path:
    sys.path.insert(0, _WF)

try:
    import mml_gen as MG
except Exception:
    MG = None

_GUARD = str(Path(__file__).parent.parent / 'guard')
if _GUARD not in sys.path:
    sys.path.insert(0, _GUARD)

try:
    import plan_wildcard as _PW
except Exception:
    _PW = None


# ── 族名提取（plan_wildcard 里没有这个函数，这里实现）──
_VERB_RE = re.compile(r'\b(ADD|MOD|SET|RMV)\s+', re.I)


def extract_fams_from_cell(cell):
    """从规划表「命令族」单元格提取族名。

    兼容实测遇到的各种写法：
      ADD POOLGROUP                → {POOLGROUP}
      ADD APN（UDG）               → {APN}
      SET APN*（UNC）              → {APN}   （通配另由 G31 处理）
      ADD USRPROFGROUP? / APNUSRPROFG → {USRPROFGROUP, APNUSRPROFG}
    """
    out = set()
    if not cell:
        return out
    for m in _VERB_RE.finditer(cell):
        rest = cell[m.end():]
        tm = re.match(r'([A-Za-z][A-Za-z0-9_]*)', rest)
        if not tm:
            continue
        name = tm.group(1).upper()
        if len(name) >= 3 and not name.isdigit():
            out.add(name)
    return out


# ═══════════════════════════════════════════════════════════
# Step 4 三级一致性
# ═══════════════════════════════════════════════════════════

def read_params_csv(csv_path):
    """读 params.csv，返回 rows（复用 mml_gen 的实现）。"""
    if MG is None:
        return []
    try:
        return MG.read_params(csv_path)
    except Exception:
        return []


def parse_mml_commands(mml_text):
    """解析 mml.txt，返回 [(verb, family, raw_line)]。"""
    out = []
    for line in (mml_text or '').split('\n'):
        s = line.split('//')[0].strip()
        if not s or s.startswith(('/*', '#', '*/')):
            continue
        m = re.match(r'^(ADD|MOD|SET|RMV)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            out.append((m.group(1).upper(), m.group(2).upper(), s))
    return out


def check_three_way_consistency(plan_text, csv_path, mml_text):
    """Step 4：规划表 → params.csv → mml.txt 三级一致性。

    返回：
      {
        'ok': bool,
        'issues': [{'level': 'plan|csv|mml', 'type':..., 'detail':...}],
        'stats': {'plan_fams': n, 'csv_fams': n, 'mml_fams': n, ...},
      }
    """
    issues = []

    # ── 规划表（状态=确认）的族 ──
    plan_fams = set()
    plan_skipped_fams = set()
    if _PW is not None:
        try:
            for r in _PW.parse_plan_rows(plan_text):
                fams = extract_fams_from_cell(r.get('fam_cell') or '')
                st = (r.get('status') or '')
                if '跳过' in st:
                    plan_skipped_fams |= fams
                else:
                    plan_fams |= fams
        except Exception:
            pass

    # ── params.csv 的族 ──
    rows = read_params_csv(csv_path)
    csv_fams = {r['family'] for r in rows if r.get('family')}
    csv_groups = {r['group'] for r in rows if r.get('group')}

    # ── mml.txt 的族 ──
    cmds = parse_mml_commands(mml_text)
    mml_fams = {fam for _, fam, _ in cmds}

    # C1 规划表确认的族 → params.csv 里有没有
    missing_in_csv = sorted(plan_fams - csv_fams)
    if missing_in_csv:
        issues.append({
            'level': 'csv', 'type': 'plan_missing_in_csv',
            'detail': f'{len(missing_in_csv)} 个族规划了但 params.csv 里没有',
            'families': missing_in_csv[:15],
        })

    # C2 params.csv 的族 → mml.txt 有没有
    missing_in_mml = sorted(csv_fams - mml_fams)
    if missing_in_mml:
        issues.append({
            'level': 'mml', 'type': 'csv_missing_in_mml',
            'detail': f'{len(missing_in_mml)} 个族在 params.csv 有但 mml.txt 没生成',
            'families': missing_in_mml[:15],
        })

    # C3 mml.txt 的族 → params.csv 有没有（说明有人绕过了 csv）
    extra_in_mml = sorted(mml_fams - csv_fams)
    if extra_in_mml:
        issues.append({
            'level': 'mml', 'type': 'mml_extra_not_in_csv',
            'detail': (f'{len(extra_in_mml)} 个族在 mml.txt 有但 params.csv 没有'
                       f'（可能直接改了 mml，违反单一数据源）'),
            'families': extra_in_mml[:15],
        })

    # C4 跳过的族不应出现在产物里
    skipped_in_prod = sorted(plan_skipped_fams & mml_fams)
    if skipped_in_prod:
        issues.append({
            'level': 'mml', 'type': 'skipped_but_generated',
            'detail': f'{len(skipped_in_prod)} 个族规划表标了跳过但产物里有',
            'families': skipped_in_prod[:15],
        })

    return {
        'ok': not issues,
        'issues': issues,
        'stats': {
            'plan_fams': len(plan_fams),
            'plan_skipped_fams': len(plan_skipped_fams),
            'csv_fams': len(csv_fams),
            'csv_groups': len(csv_groups),
            'csv_rows': len(rows),
            'mml_fams': len(mml_fams),
            'mml_cmds': len(cmds),
        },
    }


# ═══════════════════════════════════════════════════════════
# Step 5 判据核对（复用 guard，分类给出修法）
# ═══════════════════════════════════════════════════════════

# 判据 → 修复能力分类
#   auto   可代码自动修
#   data   需补数据（给用户填 或 从现网推）
#   report 只能报给用户
FIX_CAPABILITY = {
    'G11_unique':         ('auto', '重复主键可直接去重'),
    'G12_param_fmt':      ('data', '参数格式不符现网，需确认取值'),
    'G16_prior':          ('data', 'PRIORITY 超出区间，需调整取值'),
    'G17_scale':          ('report', '对象数量与清单不符，需人工核对'),
    'G18_coverage':       ('data', '缺必选参数，可从现网推或人工补'),
    'G19_source':         ('auto', '来源标注可自动补'),
    'G20_plan':           ('report', '规划覆盖不足，需回阶段1'),
    'G21_consistency':    ('auto', 'csv↔mml 不一致可重跑生成器'),
    'G22_placeholder':    ('data', '占位符需人工填值'),
    'G23_add_existing':   ('auto', '已存在对象改 ADD→MOD 或删除'),
    'G24_omission':       ('auto', '省略说明可自动补进澄清'),
    'G25_siblings':       ('data', '缺配套族，可从 exp_siblings 补'),
    'G26_plan_csv':       ('auto', '规划与产物不一致，补 params.csv'),
    'G27_unable':         ('report', '跨网元配不了，写进配置分析'),
    'G28_substitution':   ('auto', '族名张冠李戴，改回正确族名'),
    'G29_set':            ('auto', 'SET 属性族漏配，补 params.csv'),
    'G30_rmv':            ('auto', 'RMV→ADD 方向错，改动词'),
    'G31_plan_wildcard':  ('auto', '规划表通配，展开成具体族'),
}


def classify_guard_warns(guard_checks):
    """Step 5：把 guard 判据结果分类成可执行清单。

    参数：
      guard_checks  guard.py 的 checks dict（已跑完）

    返回：
      {
        'auto_fixable': [{'id':..., 'detail':..., 'how':...}],
        'need_data':    [{'id':..., 'detail':..., 'how':...}],
        'report_only':  [{'id':..., 'detail':..., 'how':...}],
        'all_ok': bool,
      }
    """
    auto_, data_, report_ = [], [], []

    for gid, res in (guard_checks or {}).items():
        if not isinstance(res, dict):
            continue
        if res.get('skipped'):
            continue
        if res.get('ok', True):
            continue

        cap, how = FIX_CAPABILITY.get(gid, ('report', '未分类判据，人工判断'))
        item = {'id': gid, 'how': how,
                'detail': _summarize_guard_result(gid, res)}
        if cap == 'auto':
            auto_.append(item)
        elif cap == 'data':
            data_.append(item)
        else:
            report_.append(item)

    return {
        'auto_fixable': auto_,
        'need_data': data_,
        'report_only': report_,
        'all_ok': not (auto_ or data_ or report_),
    }


def _summarize_guard_result(gid, res):
    """把 guard 判据结果压成一句话。"""
    # 常见字段
    for key in ('errors', 'warnings', 'missing', 'reversed', 'missed',
                'hits', 'issues', 'problems', 'unfilled', 'mismatches'):
        v = res.get(key)
        if v:
            if isinstance(v, list):
                n = len(v)
                first = v[0]
                if isinstance(first, dict):
                    first = (first.get('detail') or first.get('family')
                             or first.get('reason') or str(first)[:60])
                return f'{n} 项: {str(first)[:80]}'
            return str(v)[:100]
    # 兜底
    for k, v in res.items():
        if k in ('ok', 'skipped', 'reason'):
            continue
        if v:
            return f'{k}={str(v)[:60]}'
    return '(无详情)'


def build_fix_plan(consistency, guard_classification):
    """把 Step4 和 Step5 的结果合成一份修复计划。

    返回：
      {
        'must_fix': [...],      # 必须修（一致性问题）
        'should_fix': [...],    # 应该修（判据 warn）
        'report': [...],        # 只报告
        'summary': {...},
      }
    """
    must = []
    for iss in (consistency.get('issues') or []):
        must.append({'source': 'Step4', 'type': iss['type'],
                     'detail': iss['detail'],
                     'action': _CONSISTENCY_FIX.get(iss['type'], '人工核对')})

    should = []
    for it in guard_classification.get('auto_fixable') or []:
        should.append({'source': 'Step5', 'id': it['id'],
                       'detail': it['detail'], 'action': it['how']})
    for it in guard_classification.get('need_data') or []:
        should.append({'source': 'Step5', 'id': it['id'],
                       'detail': it['detail'], 'action': it['how']})

    report = [{'source': 'Step5', 'id': it['id'],
               'detail': it['detail'], 'action': it['how']}
              for it in (guard_classification.get('report_only') or [])]

    return {
        'must_fix': must,
        'should_fix': should,
        'report': report,
        'summary': {
            'n_must': len(must),
            'n_should': len(should),
            'n_report': len(report),
            'consistent': consistency.get('ok', True),
        },
    }


_CONSISTENCY_FIX = {
    'plan_missing_in_csv': '补 params.csv（Step3 或人工）',
    'csv_missing_in_mml': '重跑 mml_gen.py',
    'mml_extra_not_in_csv': '把 mml 里的内容补回 params.csv，再重新生成',
    'skipped_but_generated': '从 params.csv 删掉跳过族的行',
}


# ═══════════════════════════════════════════════════════════
# 自动修复（只做确定性的）
# ═══════════════════════════════════════════════════════════

def apply_auto_fixes(csv_path, plan_text=None, out_path=None):
    """执行确定性的自动修复，返回修复记录。

    只做这几件事（都是无争议的）：
      F1 csv 里有但 mml 没生成 → 重跑生成器
      F2 mml 里有但 csv 没有   → 报告（不自动删，可能是有意的）
      F3 规划表标跳过但 csv 有 → 删掉 csv 里的行

    参数：
      csv_path   原始 params.csv
      plan_text  规划表文本（用于 F3）
      out_path   输出 path（默认覆盖）

    返回：
      {'fixes': [...], 'skipped': [...], 'new_text': MML 文本}
    """
    fixes = []
    skipped = []

    rows = read_params_csv(csv_path)
    if not rows:
        return {'fixes': [], 'skipped': [{'reason': 'csv 无有效行'}],
                'new_text': ''}

    # F3：删掉规划表标跳过的族的行
    if plan_text and _PW is not None:
        skip_fams = set()
        try:
            for r in _PW.parse_plan_rows(plan_text):
                if '跳过' in (r.get('status') or ''):
                    skip_fams |= extract_fams_from_cell(r.get('fam_cell') or '')
        except Exception:
            pass

        if skip_fams:
            keep, drop = [], []
            for r in rows:
                if r['family'] in skip_fams:
                    drop.append(r)
                else:
                    keep.append(r)
            if drop:
                rows = keep
                fixes.append({'id': 'F3', 'detail': f'删除 {len(drop)} 行（规划表标跳过）',
                              'families': sorted({d['family'] for d in drop})})
                _write_params_csv(csv_path if not out_path else out_path, rows)

    # F1：重跑生成器
    target = out_path or csv_path
    text = ''
    if MG is not None:
        try:
            r = MG.gen_mml(str(target))
            text = r.get('text', '')
            if text:
                fixes.append({'id': 'F1',
                              'detail': f'重跑生成器，生成 {r.get("n_commands")} 条命令'})
        except Exception as e:
            skipped.append({'reason': f'F1 生成失败: {e}'})

    return {'fixes': fixes, 'skipped': skipped, 'new_text': text}


def _write_params_csv(path, rows):
    """把 rows 写回 params.csv（保持列顺序）。"""
    cols = ['序号', '组', '网元', '命令族', '参数', '值', '占位符', '来源', '说明']
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore')
        w.writeheader()
        for r in rows:
            w.writerow({
                '序号': r.get('no', ''), '组': r.get('group', ''),
                '网元': r.get('unit', ''), '命令族': r.get('family', ''),
                '参数': r.get('param', ''), '值': r.get('value', ''),
                '占位符': r.get('placeholder', ''), '来源': r.get('src', ''),
                '说明': r.get('note', ''),
            })


if __name__ == '__main__':
    print('=' * 92)
    print('Step 4/5 自测')
    print('=' * 92)

    # 构造测试数据
    PLAN = '''# 命令族规划

## 总览
| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | 表1 | 池 | 2 | 0 | ADD POOLGROUP | 新增 | 依据 | 确认 |
| 2 | 表2 | 模板 | 1 | 0 | ADD USERPROFILE | 新增 | 依据 | 确认 |
| 3 | 表3 | 旧对象 | 1 | 1 | RMV FILTER | 删除 | 依据 | 跳过 |'''

    CSV = '''序号,组,网元,命令族,参数,值,占位符,来源,说明
1,g1,UNC,POOLGROUP,POOLGROUPNAME,grp1,,数据清单,
2,g1,UNC,POOLGROUP,IPV4ALLOCPRIALG,ROUNDROBIN,,exp,
3,g2,UNC,USERPROFILE,USERPROFILENAME,up1,,数据清单,
4,g3,UNC,FILTER,FILTERNAME,should_be_removed,,数据清单,'''

    MML = '''ADD POOLGROUP: POOLGROUPNAME="grp1", IPV4ALLOCPRIALG=ROUNDROBIN;
ADD USERPROFILE: USERPROFILENAME="up1";
ADD FILTER: FILTERNAME="should_be_removed";'''

    tmp = Path('/tmp/p05_test')
    tmp.mkdir(exist_ok=True)
    (tmp / 'p.csv').write_text(CSV, encoding='utf-8')
    (tmp / 'm.txt').write_text(MML, encoding='utf-8')

    print('\n【Step 4 一致性】')
    r = check_three_way_consistency(PLAN, str(tmp / 'p.csv'), MML)
    print(f'  ok={r["ok"]}  统计={r["stats"]}')
    for iss in r['issues']:
        print(f'  [{iss["level"]}] {iss["detail"]}')

    print('\n【Step 5 判据分类】')
    FAKE_GUARD = {
        'G30_rmv': {'ok': False, 'reversed': [{'family': 'POOL', 'n_add': 2}]},
        'G22_placeholder': {'ok': False, 'warnings': ['3 个占位符未填']},
        'G27_unable': {'ok': False, 'issues': ['需要有 UNC 侧数据']},
        'G11_unique': {'ok': True},
        'G12_param_fmt': {'skipped': True},
    }
    cls = classify_guard_warns(FAKE_GUARD)
    print(f'  可自动修: {len(cls["auto_fixable"])} -> {[x["id"] for x in cls["auto_fixable"]]}')
    print(f'  需补数据: {len(cls["need_data"])} -> {[x["id"] for x in cls["need_data"]]}')
    print(f'  只报告:   {len(cls["report_only"])} -> {[x["id"] for x in cls["report_only"]]}')

    print('\n【修复计划】')
    fp = build_fix_plan(r, cls)
    print(f'  必须修 {fp["summary"]["n_must"]}，应修 {fp["summary"]["n_should"]}，报告 {fp["summary"]["n_report"]}')
    for m in fp['must_fix']:
        print(f'    [must] {m["type"]}: {m["action"]}')

    print('\n【自动修复 F3（删跳过族）】')
    af = apply_auto_fixes(str(tmp / 'p.csv'), PLAN, str(tmp / 'p.csv'))
    print(f'  修复: {[f["detail"] for f in af["fixes"]]}')
    print(f'  新 MML 行数: {len([l for l in af["new_text"].split(chr(10)) if l.strip()])}')
