"""评估口径：幂等命令豁免。

★ 2026-11-13（用户裁定：「这种判决不能适配么」）

## 背景

GT 是「变更工单的完整脚本」，包含两类命令：
  A. 真实变更：改了现网没有的东西（新增对象 / 改参数值）
  B. 幂等重放：现网已经有完全一样的命令，重放一遍（结果不变）

agent 按意图配置时，会正确判断「现网已有且一致 → 不重复创建」，
于是 B 类不会出现在产物里。但按「族覆盖」统计时，这些族被算成漏配。

实测（86 单）：
  · GT 共 12765 条命令，187 条（1%）是幂等重放
  · 但 49/86 单含幂等命令，小单里占比高达 25%-100%
    例：NC20260803000378  1/1 条 = 100%（整单都是幂等重放）
        NC20260907000688  67/209 条 = 32%
        NC20260828001504   4/12 条 = 33%

## 判据

一条 GT 命令属于「幂等」当且仅当：
  归一化后与某个 EXP 里的某条命令**字符串完全一致**

归一化规则：
  · 去首尾空白、去尾部分号
  · 多个空格压成一个
  · : = , 前后不留空格
  · 全大写

不考虑的情况（保守）：
  · 参数顺序不同 → 不算幂等（宁可误判为「真实变更」，不放过真漏配）
  · 参数子集 → 不算幂等（GT 可能只写部分参数，但现网全量一致不代表意图一致）

## 用法

  from idempotent_check import build_exp_cmd_index, is_idempotent, \
      evaluate_coverage

  idx = build_exp_cmd_index(exp_paths)
  # 逐条判断
  is_idem = is_idempotent(gt_raw, idx)
  # 评估
  result = evaluate_coverage(gt_kept, mml_text, exp_paths)
"""
import re
from pathlib import Path


def norm_cmd(raw):
    """归一化命令字符串，用于幂等比对。"""
    s = (raw or '').strip()
    if not s:
        return ''
    s = s.rstrip(';').strip()
    s = re.sub(r'\s+', ' ', s)
    s = re.sub(r'\s*([:=,])\s*', r'\1', s)
    return s.upper()


def build_exp_cmd_index(exp_paths):
    """从 EXP 建立「归一化命令 → (文件名, 行号)」索引。"""
    idx = {}
    for p in (exp_paths or []):
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for i, line in enumerate(f, 1):
                    s = line.strip()
                    if not re.match(r'^(ADD|MOD|SET|RMV)\s', s, re.I):
                        continue
                    n = norm_cmd(s)
                    if n and n not in idx:
                        idx[n] = (Path(p).name, i)
        except Exception:
            continue
    return idx


def is_idempotent(gt_raw, exp_index):
    """判断一条 GT 命令是否是幂等重放。"""
    n = norm_cmd(gt_raw)
    if not n:
        return False, None
    hit = exp_index.get(n)
    if hit:
        return True, {'exp_file': hit[0], 'exp_line': hit[1]}
    return False, None


def evaluate_coverage(gt_kept, mml_text, exp_paths=None, exp_index=None):
    """评估族覆盖，区分「真实漏配」和「幂等豁免」。

    gt_kept: GT 的 (verb, family, params, raw) 列表
             或 [(seq, verb, family, params, raw), ...]（带 sort key）
    mml_text: 产物 mml.txt 内容

    返回：{
      'gt_fams': {...},                  GT 全部族
      'gt_fams_effective': {...},        GT 去掉「幂等族」后的族
      'prod_fams': {...},                产物族
      'hit': {...},                      命中的族
      'missing_effective': [...],        真实漏配（幂等豁免后的差集）
      'missing_raw': [...],              原始差集
      'idempotent_families': [...],      因幂等而豁免的族
      'n_gt_cmds', 'n_idem_cmds', 'n_prod_cmds',
      'coverage_pct', 'coverage_raw_pct',
      'pass',
    }
    """
    if exp_index is None:
        exp_index = build_exp_cmd_index(exp_paths or [])

    # 归一化 gt_kept 结构
    rows = []
    for item in (gt_kept or []):
        if len(item) == 5:
            _, verb, fam, params, raw = item
        elif len(item) == 4:
            verb, fam, params, raw = item
        else:
            continue
        rows.append((verb, fam, params, raw))

    # 产物族
    prod_fams = set()
    n_prod = 0
    for line in (mml_text or '').split('\n'):
        s = line.split('//')[0].strip()
        m = re.match(r'^(ADD|MOD|SET|RMV)\s+([A-Z][A-Z0-9_]+)', s, re.I)
        if m:
            prod_fams.add(m.group(2).upper())
            n_prod += 1

    gt_fams = {f for _, f, _, _ in rows}
    idem_rows = []
    real_rows = []
    for verb, fam, params, raw in rows:
        ok, info = is_idempotent(raw, exp_index)
        if ok:
            idem_rows.append((verb, fam, raw, info))
        else:
            real_rows.append((verb, fam, raw))

    # 幂等豁免的族：该族的所有 GT 命令都是幂等 → 整族可豁免
    # 若该族既有幂等命令又有真实变更 → 不能豁免
    fam_real = {f for _, f, _ in real_rows}
    idem_fams = {f for _, f, _, _ in idem_rows}
    exempt_fams = idem_fams - fam_real

    gt_fams_effective = gt_fams - exempt_fams
    hit = gt_fams_effective & prod_fams
    missing_effective = gt_fams_effective - prod_fams
    missing_raw = gt_fams - prod_fams

    cov = len(hit) / len(gt_fams_effective) * 100 if gt_fams_effective else 100.0
    cov_raw = len(gt_fams & prod_fams) / len(gt_fams) * 100 if gt_fams else 100.0

    return {
        'gt_fams': sorted(gt_fams),
        'gt_fams_effective': sorted(gt_fams_effective),
        'prod_fams': sorted(prod_fams),
        'hit': sorted(hit),
        'missing_effective': sorted(missing_effective),
        'missing_raw': sorted(missing_raw),
        'idempotent_families': sorted(exempt_fams),
        'idempotent_cmds': [(v, f, r[:100]) for v, f, r, _ in idem_rows],
        'n_gt_cmds': len(rows),
        'n_idem_cmds': len(idem_rows),
        'n_prod_cmds': n_prod,
        'coverage_pct': round(cov, 1),
        'coverage_raw_pct': round(cov_raw, 1),
        'pass': len(missing_effective) == 0,
    }


if __name__ == '__main__':
    import json

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 100)
    print('幂等豁免评估（86 单）')
    print('=' * 100)

    n_has_idem = 0
    n_changed = 0
    for g in GT:
        tk = g['ticket']
        if not g['kept']:
            continue
        adir = Path(g['path']) / '备份附件'
        exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []
        if not exps:
            continue
        idx = build_exp_cmd_index(exps)
        r = evaluate_coverage(g['kept'], '', exp_index=idx)
        if r['n_idem_cmds']:
            n_has_idem += 1
            has_exempt = bool(r['idempotent_families'])
            if has_exempt:
                n_changed += 1
            if has_exempt or r['n_idem_cmds'] / max(r['n_gt_cmds'], 1) > 0.25:
                print(f"\n{tk}  GT {r['n_gt_cmds']} 条，幂等 {r['n_idem_cmds']} 条")
                if r['idempotent_families']:
                    print(f"  豁免族: {r['idempotent_families']}")
                    print(f"  GT 族 {len(r['gt_fams'])} → 有效 {len(r['gt_fams_effective'])}")

    print(f"\n{'=' * 100}")
    print(f"含幂等命令的单: {n_has_idem}/86")
    print(f"其中整族可豁免的: {n_changed} 单")
