#!/usr/bin/env python3
"""expgv 集成测试 —— 端到端冒烟用例集（真实 UNC/UEG/UDG exp）。

设计（用户口径 2026-09-19）：
  · 集成测试 = 端到端冒烟：把产品当黑盒，验证各模块串起来能跑通
  · 用真实三产品 exp（不是造的小样本）
  · 覆盖四条路：分析路 / 生成路 / agent路 / 检索路

与单元自证的区别：
  smoke_v5/test_*_selftest.py   单模块判据自证（判据本身对不对）
  本套件                          跨模块端到端（拼起来能不能跑）

用法（日常回归跑全量）:
    python3 test_integration.py                # 全量（三产品真实 exp，约 31 秒）★回归基线
    python3 test_integration.py --product ueg  # 只跑某产品（调试用）
    python3 test_integration.py --quick        # 跳过 UDG 大 exp（仅开发中频繁试跑用）

退出码 0 = 全通过；1 = 有失败。
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = Path('/opt/expgv/scripts')
RULES = Path('/opt/expgv/rules')
TESTDATA = Path('/opt/expgv/testdata/real_exp')
KB111 = Path('/opt/expgv/kb111')

# ── 三产品配置（路径按存在性探测，不写死 —— UEG 的 NAV 多一层）──
PRODUCTS = {
    'udg': {
        'feat_dir': Path('/home/expgv/workspace/zhijian/output_udg_feature/feature_v3'),
        'nav_root': Path('/home/expgv/workspace/zhijian/output_udg_nav'),
        'fp': RULES / 'features_udg.yaml',
        'exp': TESTDATA / 'udg.exp.txt',
        'kb': KB111 / 'UDG',
    },
    'ueg': {
        'feat_dir': Path('/home/expgv/workspace/zhijian/output_ueg_feature/output_ueg_feature_v3'),
        'nav_root': Path('/home/expgv/workspace/zhijian/output_ueg_nav/output_ueg_nav_v2'),
        'fp': RULES / 'features_ueg.yaml',
        'exp': TESTDATA / 'ueg.exp.txt',
        'kb': KB111 / 'UEG',
    },
    'unc': {
        'feat_dir': Path('/home/expgv/workspace/zhijian/output_unc_feature/feature_v3'),
        'nav_root': Path('/home/expgv/workspace/zhijian/output_unc_nav'),
        'fp': RULES / 'features_unc.yaml',
        'exp': TESTDATA / 'unc.exp.txt',
        'kb': KB111 / 'UNC',
    },
}

# ── 结果收集 ──
RESULTS = []


SKIPS = []


def case(name, ok, detail=''):
    """ok=True 通过 / False 失败 / None 跳过（输入类客户数据缺失时用）。

    跳过与"失败"必须分开：real_exp 是客户数据（不入版本库），别处 clone 后天然没有，
    若记成失败会让 release.sh 在干净环境下永远红。
    """
    if ok is None:
        SKIPS.append((name, detail))
        print('  %s %-52s %s' % ('-', name, detail))
        return
    RESULTS.append((name, bool(ok), detail))
    print('  %s %-52s %s' % ('✓' if ok else '✗', name, detail))


def run(cmd, timeout=600, cwd=None):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd)
    return r.returncode, r.stdout + r.stderr


# ══════════════════════════════════════════════════════════
# 用例 1: 生成路 —— 特性文档 + 指纹 + NAV + 真实 exp → 产物
# ══════════════════════════════════════════════════════════
def t_generate(prod, cfg, outdir):
    print('\n【生成路】%s' % prod.upper())
    t0 = time.time()
    rc, out = run(['python3', 'gen_feature_all.py',
                   '--feat-dir', str(cfg['feat_dir']),
                   '--nav-dir', str(cfg['nav_root']),
                   '--fingerprint', str(cfg['fp']),
                   '--exp', str(cfg['exp']),
                   '-o', str(outdir)], cwd=SCRIPTS, timeout=900)
    el = time.time() - t0
    case('%s-1 生成完成（退出码 0）' % prod, rc == 0, '%.1fs' % el)
    if rc != 0:
        print(out[-800:])
        return None

    mds = list(Path(outdir).glob('*.md'))
    mds = [m for m in mds if m.name != 'README.md']
    case('%s-2 产物非空' % prod, len(mds) > 0, '%d 篇' % len(mds))

    # 无重名（命名降级链的验收）
    names = [m.name for m in mds]
    case('%s-3 产物无重名' % prod, len(names) == len(set(names)),
         '%d/%d 唯一' % (len(set(names)), len(names)))

    # 序号兜底归零
    seq = [n for n in names if '同名文档' in n]
    case('%s-4 无序号兜底' % prod, not seq, '%d 个带序号' % len(seq))

    # 三段结构齐全
    body = (Path(outdir) / mds[0].name).read_text(encoding='utf-8')
    case('%s-5 §1 文档原文' % prod, '## 1.' in body or '特性完整内容' in body)
    case('%s-6 §2 官方示例' % prod, '## 2.' in body or '官方示例命令' in body)
    case('%s-7 §3 现网实例' % prod, '## 3.' in body or '现网实例' in body)
    return mds


# ══════════════════════════════════════════════════════════
# 用例 1b: 指纹匹配段（match_features）—— 覆盖「文档缺失分支」
#   背景：UEG 有 249 条指纹无 doc_path → match_features 走「文档缺失」分支
#   → 该分支曾漏写 domain 键 → 统计段 dom_stat[r['domain']] KeyError
#   → 整个分析 stage=failed（UDG/UNC 文档齐全，不触发 ⇒ 曾漏网）
#   判据：退出码 0 + match_result.json 产出 + 状态分布齐备
# ══════════════════════════════════════════════════════════
def t_match(prod, cfg, outdir):
    print('\n【指纹匹配段】%s' % prod.upper())
    t0 = time.time()
    rc, out = run(['python3', 'match_features.py',
                   '--product', prod.upper(),
                   '--exp', str(cfg['exp']),
                   '--fingerprint', str(cfg['fp']),
                   '-o', str(outdir)], cwd=SCRIPTS, timeout=900)
    el = time.time() - t0
    case('%s-8 匹配段完成（退出码 0）' % prod, rc == 0, '%.1fs' % el)
    if rc != 0:
        print(out[-800:])
        return
    # KeyError('domain') 的直接症状：Traceback 出现在输出里
    case('%s-9 无 KeyError/domain 崩溃' % prod,
         'KeyError' not in out and 'Traceback' not in out)
    mj = Path(outdir) / 'match_result.json'
    # ⚠ 2026-10-23：match_features 用**多网元布局**输出（outdir/<exp名>/ME<id>/match_result.json）。
    #   旧判据找 outdir/match_result.json（顶层）⇒ 永远 False，且连带跳过 -11/-12/-13
    #   三条守卫（domain 键守卫、状态分布守卫都被静默跳过）。改为递归查找。
    mj = next(iter(sorted(Path(outdir).rglob('match_result.json'))), None) \
        if Path(outdir).is_dir() else None
    case('%s-10 match_result.json 产出' % prod, bool(mj and mj.is_file()),
         str(mj.relative_to(outdir)) if mj else '未找到（含子目录）')
    if mj and mj.is_file():
        import json as _j
        d = _j.loads(mj.read_text(encoding='utf-8'))
        res = d.get('results', {})
        case('%s-11 结果非空' % prod, len(res) > 0, '%d 条' % len(res))
        # 每条结果必须有 domain 键（本次 bug 的守卫）
        bad = [k for k, v in list(res.items())[:2000] if 'domain' not in v]
        case('%s-12 每条结果含 domain 键' % prod, not bad,
             '%d 条缺 domain' % len(bad))
        # 状态分布齐备（绿/黄/红/人工四态，且统计段能跑通）
        st = {}
        for v in res.values():
            st[v.get('status', '?')] = st.get(v.get('status', '?'), 0) + 1
        case('%s-13 状态分布可统计' % prod, len(st) >= 2,
             ' '.join('%s=%d' % (k, v) for k, v in sorted(st.items())))


# ══════════════════════════════════════════════════════════
# 用例 2: 确定性 —— 同输入两遍字节一致（铁律）
# ══════════════════════════════════════════════════════════
def t_determinism(prod, cfg, out1, out2):
    print('\n【确定性】%s 两遍字节一致' % prod.upper())
    rc, out = run(['python3', 'gen_feature_all.py',
                   '--feat-dir', str(cfg['feat_dir']),
                   '--nav-dir', str(cfg['nav_root']),
                   '--fingerprint', str(cfg['fp']),
                   '--exp', str(cfg['exp']),
                   '-o', str(out2)], cwd=SCRIPTS, timeout=900)
    if rc != 0:
        case('%s 确定性' % prod, False, '第二遍失败')
        return
    rc2, out2s = run(['diff', '-rq', str(out1), str(out2)], timeout=120)
    n_diff = len([x for x in out2s.split('\n') if x.strip()])
    case('%s 两遍字节一致' % prod, rc2 == 0 and n_diff == 0, '%d 处差异' % n_diff)


# ══════════════════════════════════════════════════════════
# 用例 3: 判据合格率
# ══════════════════════════════════════════════════════════
def t_criteria(prod, outdir):
    print('\n【判据】%s' % prod.upper())
    rc, out = run(['python3', 'chain_criteria.py', str(outdir)], cwd=SCRIPTS, timeout=300)
    rate_ok = '100.0%' in out
    m = [l for l in out.split('\n') if '判定:' in l]
    case('%s 判据合格率 100%%' % prod, rate_ok, m[-1].strip() if m else out[-120:])
    old = [l for l in out.split('\n') if '旧区间标题残留' in l]
    if old:
        case('%s 无旧形态残留' % prod, '0 篇' in old[0], old[0].strip())


# ══════════════════════════════════════════════════════════
# 用例 4: 检索路 —— kb111 知识库
# ══════════════════════════════════════════════════════════
def t_retrieval(prod, cfg):
    print('\n【检索路】%s' % prod.upper())
    kb = cfg['kb']
    # ⚠ 不能写死 kb.glob('*.md')：三产品目录层级不统一 ——
    #   UDG/UNC 是扁平（kb111/UDG/*.md），UEG 多一层（kb111/UEG/5GC/*.md）。
    #   写死会静默返回 0 条（实测踩过）。按存在性 + 递归探测。
    if not kb.exists():
        case('%s kb111 目录存在' % prod, False, str(kb))
        return
    n = len(list(kb.rglob('*.md')))
    case('%s kb111 可用' % prod, n > 0, '%d 篇（递归）' % n)
    # 目录层级也要报出来，便于发现层级变化
    depth = 1 if list(kb.glob('*.md')) else 2
    case('%s kb111 层级探测' % prod, True, '%d 层' % depth)


# ══════════════════════════════════════════════════════════
# 用例 4b: exp 吞吐指标（归一化 ms/万行 + 线性度）
# ══════════════════════════════════════════════════════════
THROUGHPUT = []   # (产品, 行数, 解exp秒)


def t_throughput(prod, cfg, repeat=1):
    """exp 解析吞吐 —— 归一化到 ms/万行，并检查线性度。

    为什么单列（用户口径 2026-09-19）：
      "求平均或者以 s/100000loc 为单位衡量" —— 总时长没有可比性
      （文档库大小不同），exp 处理必须归一化才看得出真实吞吐。
      实测基线 ≈ 44 ms/万行（UEG/UNC/UDG 三点 41/46/44，波动 ±5%）。
      若哪天冒出 O(n^2) 逻辑，线性度会被破坏，这里就能立刻看出来。
    """
    import time as _t
    sys.path.insert(0, str(SCRIPTS))
    try:
        import gen_feature_all as G
    except Exception as e:
        case('%s exp 吞吐' % prod, False, 'import 失败: %s' % e)
        return
    lines = sum(1 for _ in open(cfg['exp'], encoding='utf-8', errors='ignore'))
    el = 0.0
    for _ in range(max(1, repeat)):       # --bench N：多次采样取均值
        t0 = _t.time()
        G.parse_exp(cfg['exp'])
        el += _t.time() - t0
    el /= max(1, repeat)
    per = el / (lines / 10000) * 1000 if lines else 0
    THROUGHPUT.append((prod, lines, el))
    tag = '' if repeat <= 1 else '（%d 次均值）' % repeat
    case('%s exp 吞吐' % prod, per < 200,
         '%d 行 → %.3f s = %.1f ms/万行%s' % (lines, el, per, tag))


def t_throughput_summary():
    """汇总吞吐 + 线性度检查。"""
    print('\n【吞吐汇总】exp 解析归一化')
    if not THROUGHPUT:
        # 无真实 exp ⇒ 无从测吞吐（客户数据缺失，非缺陷）
        case('吞吐汇总', None, '跳过：无真实 exp（客户数据），无从测吞吐')
        return
    for prod, lines, el in THROUGHPUT:
        per = el / (lines / 10000) * 1000 if lines else 0
        print('    %-4s %8d 行  %7.3f s  %7.1f ms/万行' % (prod.upper(), lines, el, per))
    pers = [el / (l / 10000) * 1000 for _, l, el in THROUGHPUT if l]
    if len(pers) >= 2:
        avg = sum(pers) / len(pers)
        spread = (max(pers) - min(pers)) / avg * 100
        # 线性度：最快/最慢差 ≤3 倍（跨 45 倍数据量）
        case('线性度（归一化后波动 ≤3x）', spread < 200,
             '均值 %.1f ms/万行，极差 %.0f%%' % (avg, spread))
        print('    → 即 %.2f 秒 / 10 万行（容量估算用）' % (avg / 1000 * 10))


# ══════════════════════════════════════════════════════════
# 用例 5: 冒烟 —— 单元自证套件全绿（作为集成的一部分）
# ══════════════════════════════════════════════════════════
def t_version_alignment():
    """判据实现 vs 自证套件：版本一致性（防「僵尸套件」）。

    为什么单列这一项（2026-09-19 实测教训）：
      chain_criteria.py 从 F1~F5 改版为 N1~N5，但自证套件没跟着改，
      套件引用 C.RE_F1 直接 AttributeError —— 长期没人发现，
      因为「没人跑它」。这类缺陷的特征是「文件在、看着绿、实际失效」。

    检查法：套件里引用的每个 C.RE_xxx 必须在实现里存在。
    """
    print('\n【版本一致性】实现 vs 套件')
    import re as _re
    impl = (SCRIPTS / 'chain_criteria.py').read_text(encoding='utf-8')
    impl_names = set(_re.findall(r'^(RE_[A-Z0-9_]+)\s*=', impl, _re.M))

    pairs = [
        ('test_chain_criteria_selftest.py', 'chain_criteria'),
        ('test_linkgroups_selftest.py', 'chain_by_linkgroups'),
        ('test_dedup_selftest.py', 'gen_feature_all'),
        ('test_quote_guard.py', 'gen_assemble'),
    ]
    for fname, modname in pairs:
        p = SCRIPTS / 'smoke_v5' / fname
        if not p.exists():
            case('%s 存在' % fname, False)
            continue
        src = p.read_text(encoding='utf-8')
        # 套件引用的 C.RE_xxx / G.xxx
        refs = set(_re.findall(r'\bC\.(RE_[A-Z0-9_]+)', src))
        if not refs:
            case('%s 版本一致' % fname, True, '未直接引用 RE_*')
            continue
        missing = refs - impl_names
        case('%s 版本一致' % fname, not missing,
             ('引用不存在的: %s' % ', '.join(sorted(missing))) if missing else
             '引用 %d 个判据全部存在' % len(refs))


def t_selftests():
    print('\n【自证套件】全绿')
    for t in ('test_linkgroups_selftest.py', 'test_linkgroups_edge.py',
              'test_dedup_selftest.py', 'test_path_suffix_selftest.py',
              'test_chain_criteria_selftest.py'):
        p = SCRIPTS / 'smoke_v5' / t
        if not p.exists():
            case(t, False, '不存在')
            continue
        rc, out = run(['python3', t], cwd=SCRIPTS / 'smoke_v5', timeout=300)
        case(t, rc == 0, '通过' if rc == 0 else out[-100:])


# ══════════════════════════════════════════════════════════
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--quick', action='store_true',
                    help='跳过 UDG 大 exp（仅开发中试跑；回归基线用全量）')
    ap.add_argument('--product', choices=['udg', 'ueg', 'unc'], help='只跑某产品')
    ap.add_argument('--keep', action='store_true', help='保留产物目录')
    ap.add_argument('--bench', type=int, default=1, metavar='N',
                    help='吞吐采样次数（默认 1；求稳定均值可设 5）')
    args = ap.parse_args()

    prods = [args.product] if args.product else ['ueg', 'unc', 'udg']
    if args.quick:
        prods = [p for p in prods if p != 'udg']

    print('=' * 66)
    print('expgv 集成测试（端到端冒烟）')
    print('  产品: %s' % ', '.join(p.upper() for p in prods))
    print('  大 exp: %s' % ('跳过' if args.quick else '包含'))
    print('=' * 66)

    t0 = time.time()
    outroot = Path('/tmp/integ_smoke')

    # 前置：路径存在性
    print('\n【前置】输入路径')
    for p in prods:
        cfg = PRODUCTS[p]
        case('%s 文档库' % p, cfg['feat_dir'].exists(), str(cfg['feat_dir']))
        case('%s NAV' % p, cfg['nav_root'].exists(), str(cfg['nav_root']))
        case('%s 指纹' % p, cfg['fp'].exists())
        case('%s 真实 exp' % p,
             True if cfg['exp'].exists() else None,
             ('%.1f MB' % (cfg['exp'].stat().st_size / 1e6)) if cfg['exp'].exists()
             else '客户数据缺失（不入版本库）→ 本产品用例跳过')

    for p in prods:
        cfg = PRODUCTS[p]
        if not all([cfg['feat_dir'].exists(), cfg['fp'].exists(), cfg['exp'].exists()]):
            _why = []
            if not cfg['feat_dir'].exists():
                _why.append('文档库缺失')
            if not cfg['fp'].exists():
                _why.append('指纹缺失')
            if not cfg['exp'].exists():
                _why.append('真实 exp 缺失（客户数据）')
            case('%s 全部用例' % p, None, '跳过：' + '、'.join(_why))
            continue
        o1 = outroot / ('%s_a' % p)
        o2 = outroot / ('%s_b' % p)
        om = outroot / ('%s_match' % p)
        for d in (o1, o2, om):
            if d.exists():
                shutil.rmtree(d)
        om.mkdir(parents=True, exist_ok=True)
        t_generate(p, cfg, o1)
        t_match(p, cfg, om)          # 指纹匹配段（覆盖「文档缺失」分支的 domain KeyError）
        t_determinism(p, cfg, o1, o2)
        t_criteria(p, o1)
        t_retrieval(p, cfg)
        t_throughput(p, cfg, args.bench)
        if not args.keep:
            for d in (o1, o2):
                if d.exists():
                    shutil.rmtree(d)

    t_throughput_summary()
    t_selftests()
    t_version_alignment()

    # ── 汇总 ──
    print('\n' + '=' * 66)
    n_pass = sum(1 for _, ok, _ in RESULTS if ok)
    n_fail = len(RESULTS) - n_pass
    print('总计: %d/%d 通过，失败 %d，跳过 %d，耗时 %.1f 秒' %
          (n_pass, len(RESULTS), n_fail, len(SKIPS), time.time() - t0))
    if SKIPS:
        print('\n跳过用例（输入缺失，非缺陷）:')
        for name, detail in SKIPS:
            print('  - %s  %s' % (name, detail))
    if n_fail:
        print('\n失败用例:')
        for name, ok, detail in RESULTS:
            if not ok:
                print('  ✗ %s  %s' % (name, detail))
    print('=' * 66)
    return 0 if n_fail == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
