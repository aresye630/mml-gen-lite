"""G35：params.csv 引用完整性检查（生成 mml 之前）。

★ 2026-11-12（从 3 单重跑失败分析得出）

## 实测问题

NC20260823000103 的 params.csv：
  第 1476 行: RULEBINDING#2 (UDG) 引用 @USERPROFILE#2.USERPROFILENAME
  但 params.csv 里只有 USERPROFILE#1（UNC 侧）
  → 组不存在

现有 G21 能抓到（csv 生不出 mml），但错误信息只有：
  「csv 生成失败: ['引用了不存在的组: @USERPROFILE#2.USERPROFILENAME']」

agent 看到这个提示不知道该干什么：是删掉这条？还是补一个组？
3 轮都改不对，最后 failed。

## 本判据的价值

在生成 mml **之前**做引用完整性检查，并给出「可操作的三选一」指引：
  1. 补上缺失的组（如果确实要配这个对象）
  2. 改成引用已有的组（如 @USERPROFILE#1）
  3. 删掉这条命令（如果本不需要）

## 检查内容

  1. 引用目标组是否存在
  2. 引用目标参数是否存在
  3. 循环引用（A→B→A）
  4. 跨网元引用（UDG 组引用 UNC 组，通常不允许）
"""
import csv
import re
from collections import defaultdict
from pathlib import Path

REF_PATTERN = re.compile(r'^@([A-Za-z0-9_]+(?:#\d+)?)\.([A-Za-z0-9_]+)$')


def _read_csv(csv_path):
    """读 params.csv，返回行列表。"""
    rows = []
    with open(csv_path, encoding='utf-8-sig', newline='') as f:
        for r in csv.DictReader(f):
            rows.append(r)
    return rows


def check_ref_integrity(csv_path):
    """检查 params.csv 的引用完整性。

    返回：{
      'ok': bool,
      'n_groups': int,
      'n_refs': int,
      'missing_groups': [{'group','param','line','actual_group','suggest'}],
      'missing_params': [{'group','param','line','ref_group'}],
      'cycles': [...],
      'warnings': [...],
    }
    """
    result = {
        'ok': True,
        'n_groups': 0,
        'n_refs': 0,
        'missing_groups': [],
        'missing_params': [],
        'cycles': [],
        'warnings': [],
    }

    p = Path(csv_path)
    if not p.exists():
        return {'ok': True, 'skipped': True, 'reason': 'csv 不存在'}

    try:
        rows = _read_csv(str(p))
    except Exception as e:
        return {'ok': False, 'error': f'读 csv 失败: {e}'}

    if not rows:
        return {'ok': True, 'skipped': True, 'reason': 'csv 为空'}

    # 建索引：组名 → {参数: 值}，以及 组名 → 网元
    groups = defaultdict(dict)
    group_ne = {}
    for i, r in enumerate(rows, 2):  # 2 因为第 1 行是表头
        g = (r.get('组') or '').strip()
        prm = (r.get('参数') or '').strip().upper()
        val = (r.get('值') or '').strip()
        ne = (r.get('网元') or '').strip().upper()
        if not g:
            continue
        groups[g][prm] = val
        if ne and g not in group_ne:
            group_ne[g] = ne

    result['n_groups'] = len(groups)

    # 检查每个引用
    for i, r in enumerate(rows, 2):
        g = (r.get('组') or '').strip()
        prm = (r.get('参数') or '').strip().upper()
        val = (r.get('值') or '').strip()
        ne = (r.get('网元') or '').strip().upper()
        if not val.startswith('@'):
            continue
        m = REF_PATTERN.match(val)
        if not m:
            result['warnings'].append({
                'line': i, 'group': g, 'param': prm, 'value': val,
                'why': '引用语法不标准（应为 @组名.参数名）',
            })
            continue
        result['n_refs'] += 1
        ref_g, ref_p = m.group(1), m.group(2).upper()

        if ref_g not in groups:
            # 找同族前缀的已有组，给建议
            base = re.sub(r'#\d+$', '', ref_g)
            same_base = [x for x in groups if re.sub(r'#\d+$', '', x) == base]
            if same_base:
                suggest = f'引用已存在的组 @{same_base[0]}.{ref_p}'
                alt = f'或新建一个 {ref_g} 组（若要配另一个对象）'
            else:
                suggest = f'新建 {ref_g} 组（含参数 {ref_p}）'
                alt = '或删掉这条命令（若本不需要）'

            result['missing_groups'].append({
                'line': i,
                'group': g,
                'param': prm,
                'ref_group': ref_g,
                'ref_param': ref_p,
                'value': val,
                'actual_existing': same_base,
                'suggest': suggest + '；' + alt,
            })
            result['ok'] = False
            continue

        if ref_p not in groups[ref_g]:
            result['missing_params'].append({
                'line': i,
                'group': g,
                'param': prm,
                'ref_group': ref_g,
                'ref_param': ref_p,
                'available': sorted(groups[ref_g].keys())[:10],
            })
            result['ok'] = False
            continue

        # 跨网元引用检查
        ref_ne = group_ne.get(ref_g, '')
        if ne and ref_ne and ne != ref_ne:
            result['warnings'].append({
                'line': i, 'group': g, 'param': prm, 'value': val,
                'why': f'跨网元引用：{g}（{ne}）引用 {ref_g}（{ref_ne}），'
                       f'通常不允许',
            })

    # 循环引用检测
    def _resolve_chain(gname, seen):
        if gname in seen:
            return True
        seen = seen | {gname}
        for prm, val in (groups.get(gname) or {}).items():
            if not val.startswith('@'):
                continue
            m2 = REF_PATTERN.match(val)
            if m2 and m2.group(1) == gname:
                return True  # 自引用
            if m2 and _resolve_chain(m2.group(1), seen):
                return True
        return False

    for gname in groups:
        if _resolve_chain(gname, frozenset()):
            result['cycles'].append(gname)
            result['ok'] = False

    return result


def format_for_agent(r):
    """把检查结果格式化成给 agent 看的可操作提示。"""
    lines = []
    for m in r.get('missing_groups') or []:
        lines.append(
            f"第 {m['line']} 行（组 {m['group']}，网元见行内）："
            f"引用了不存在的组 {m['ref_group']}\n"
            f"    修复三选一：\n"
            f"      a) {m['suggest'].split('；')[0]}\n"
            f"      b) {m['suggest'].split('；')[-1]}\n"
            f"      c) 把该值从 @{m['ref_group']}.{m['ref_param']} 改成具体值"
        )
    for m in r.get('missing_params') or []:
        lines.append(
            f"第 {m['line']} 行（组 {m['group']}）：引用了 {m['ref_group']} "
            f"里不存在的参数 {m['ref_param']}\n"
            f"    该组现有参数: {m['available']}"
        )
    for c in r.get('cycles') or []:
        lines.append(f'组 {c} 存在循环引用')
    return '\n'.join(lines)


if __name__ == '__main__':
    import json
    import subprocess
    import sys

    print('=' * 100)
    print('G35：params.csv 引用完整性检查')
    print('=' * 100)

    # 从容器拷一个真实失败案例
    CONT = {'8620': 'mmlgen-clean', '8621': 'mmlgen-b1',
            '8622': 'mmlgen-b2', '8623': 'mmlgen-b3'}
    res = json.loads(Path('/tmp/eval_retry3/result.json').read_text(encoding='utf-8'))
    tk = 'NC20260823000103'
    r = next((x for x in res if x['ticket'] == tk), None)
    if r:
        sid = r['sid']
        for port, c in CONT.items():
            t = subprocess.run(
                ['docker', 'exec', '-u', 'expgv', c, 'test', '-f',
                 f'/data/sessions/{sid}/analysis_code/params.csv'],
                capture_output=True, timeout=30)
            if t.returncode == 0:
                subprocess.run(
                    ['docker', 'cp',
                     f'{c}:/data/sessions/{sid}/analysis_code/params.csv',
                     f'/tmp/{tk}_params.csv'],
                    capture_output=True, timeout=120)
                break

        csv_p = Path(f'/tmp/{tk}_params.csv')
        if csv_p.exists():
            chk = check_ref_integrity(str(csv_p))
            print(f'\n{tk}')
            print(f'  组数: {chk["n_groups"]}, 引用数: {chk["n_refs"]}')
            print(f'  ok: {chk["ok"]}')
            print(f'  缺失组: {len(chk["missing_groups"])}')
            for m in chk['missing_groups'][:5]:
                print(f'    L{m["line"]}: @{m["ref_group"]}.{m["ref_param"]}')
                print(f'      现有同族组: {m["actual_existing"]}')
                print(f'      建议: {m["suggest"]}')

    # 构造用例
    print(f'\n{"=" * 100}')
    print('构造用例')
    print(f'{"=" * 100}')

    TEST_CSV = '''序号,组,网元,命令族,参数,值,占位符,来源,说明
1,USERPROFILE#1,UNC,USERPROFILE,USERPROFILENAME,up_ims,,plan:test,
2,RULEBINDING#1,UNC,RULEBINDING,USERPROFILENAME,@USERPROFILE#1.USERPROFILENAME,,plan:test,
3,RULEBINDING#2,UDG,RULEBINDING,USERPROFILENAME,@USERPROFILE#2.USERPROFILENAME,,plan:test,
4,POOL#1,UDG,POOL,POOLNAME,pool_x,,plan:test,
5,SECTION#1,UDG,SECTION,POOLNAME,@POOL#2.POOLNAME,,plan:test,
6,AAAA#1,UDG,AAAA,X,@BBBB#1.X,,plan:test,
7,BBBB#1,UDG,BBBB,X,@AAAA#1.X,,plan:test,
'''
    Path('/tmp/test_ref.csv').write_text(TEST_CSV, encoding='utf-8')
    chk = check_ref_integrity('/tmp/test_ref.csv')
    print(f'\nok: {chk["ok"]}')
    print(f'组数: {chk["n_groups"]}, 引用: {chk["n_refs"]}')
    print(f'缺失组: {len(chk["missing_groups"])}')
    for m in chk['missing_groups']:
        print(f'  L{m["line"]}: @{m["ref_group"]}.{m["ref_param"]} '
              f'（现有同族: {m["actual_existing"]}）')
    print(f'循环引用: {chk["cycles"]}')
    print(f'\n给 agent 的提示:\n{format_for_agent(chk)}')
