#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""确定性自证：同一份 EXP 跑两遍，产物是否字节一致？

用途：M3 性能优化的**验收地基**。
  · 两遍一致 → 「结果不变」可严格验收（优化前后比 md5 即可）
  · 不一致   → 链路本身含非确定性（set 迭代序/时间戳/浮点），
               优化前必须先定位并消除，否则无法区分「优化改了结果」
               与「本来就不稳定」

⚠ 命令行**照抄 app_v1._analysis_code_fn**（不要自己猜参数名）：
   ① feature_relations.py --feat-dir <dir> --exp <f> -o <out> --anchors <a> --rel-rules <r>
   ② exp_analysis_code/pipeline.py <exp> -o <acd>              (cwd=exp_analysis_code)
   ③ exp_analysis_code/feature_chain_map.py --chains .. --features .. --product .. -o ..
   ④ match_features.py --product <p> --exp <f> --fingerprint <fp> -o <sd> --anchors <a>
      gen_feature_all.py --feat-dir <dir> --exp <f> -o <gt> --anchors <a>

⚠ 相对路径（rules/features_udg.yaml、chain_schemas.yaml）要求**在对应 cwd 下运行**，
   否则 FileNotFoundError → 全段失败 → 产物为空。
   **产物为空时绝不能报「一致」**（空==空 的假绿）。

用法（容器内，以 expgv 身份）：
    python3 det_check.py --sid <sid> [--runs 2]
    python3 det_check.py --exp <path> --product UDG [--runs 2]
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

SCRIPTS = Path('/opt/expgv/scripts')
PIPE = SCRIPTS / 'exp_analysis_code'


def _cfg(product):
    """产品配置（feat_dir / fingerprint / anchors / rel_rules）"""
    import yaml
    base = SCRIPTS.parent                      # /opt/expgv
    pc = yaml.safe_load((base / 'rules' / 'products.yaml').read_text(encoding='utf-8'))
    pr = (pc.get('products') or {}).get(product) or {}
    feat_dir = str(pr.get('feat_dir') or '').replace('~', str(Path.home()))
    fp = str(pr.get('fingerprint') or '')
    fp = fp if fp.startswith('/') else str(base / fp)
    # ★ 真值来源：session_store.ANCHORS / REL_RULES（别硬编码文件名）
    anchors = rel_rules = ''
    try:
        import sys as _s
        _s.path.insert(0, '/opt/expgv/backend')
        from session_store import ANCHORS as _A, REL_RULES as _R
        anchors, rel_rules = str(_A), str(_R)
    except Exception:
        anchors = str(base / 'rules' / 'param_anchor.yaml')
        rel_rules = str(base / 'rules' / 'feature_rel.yaml')
    return {'feat_dir': feat_dir, 'fingerprint': fp,
            'anchors': anchors, 'rel_rules': rel_rules, 'product': product}


def run_chain(exp, product, outdir, verbose=True):
    """跑完整 4 段链；返回 (耗时, 失败段列表)"""
    c = _cfg(product)
    env = dict(os.environ)
    env['PYTHONHASHSEED'] = '0'      # 固定哈希种子，排除 set 序带来的伪非确定性
    outdir = Path(outdir)
    acd = outdir / 'analysis_code'
    gt = outdir / '特性配置基线'
    acd.mkdir(parents=True, exist_ok=True)
    gt.mkdir(parents=True, exist_ok=True)
    fails = []

    def step(name, cmd, cwd=None):
        r = subprocess.run([str(x) for x in cmd], capture_output=True,
                           text=True, env=env, cwd=str(cwd) if cwd else None)
        if r.returncode != 0:
            fails.append(name)
            if verbose:
                print(f'    ⚠ {name} rc={r.returncode}')
                tail = (r.stderr or r.stdout or '')[-260:]
                for ln in tail.strip().splitlines()[-3:]:
                    print(f'       {ln}')
        return r.returncode

    t0 = time.time()
    step('① feature_relations',
         [sys.executable, SCRIPTS / 'feature_relations.py',
          '--feat-dir', c['feat_dir'], '--exp', exp, '-o', outdir,
          '--anchors', c['anchors'], '--rel-rules', c['rel_rules']])
    step('② pipeline',
         [sys.executable, PIPE / 'pipeline.py', exp, '-o', acd], cwd=PIPE)
    step('③ feature_chain_map',
         [sys.executable, PIPE / 'feature_chain_map.py',
          '--chains', PIPE / 'rules' / 'chain_schemas.yaml',
          '--features', c['fingerprint'], '--product', product,
          '-o', acd / 'feature_chains.json'], cwd=PIPE)
    step('④a match_features',
         [sys.executable, SCRIPTS / 'match_features.py',
          '--product', product, '--exp', exp, '--fingerprint', c['fingerprint'],
          '-o', outdir, '--anchors', c['anchors']])
    step('④b gen_feature_all',
         [sys.executable, SCRIPTS / 'gen_feature_all.py',
          '--feat-dir', c['feat_dir'], '--exp', exp, '-o', gt,
          '--anchors', c['anchors']])
    return time.time() - t0, fails


# ★ 已知的**合法非确定字段**——比对时归一化掉，否则每轮都"不一致"，
#   噪声淹没真实差异。
#
#   实测（2026-09-18，15MB EXP / 529 产物，两轮）：
#     · match_result.json → 唯一差异 = meta.updated_at
#     · 匹配报告.md       → 唯一差异 = 「耗时：10.8s」vs「11.0s」
#     · 其余 527 个文件    → 字节完全一致（results 的 435 特性判定全等）
#   ⇒ 链路确定性成立，「结果不变」可机器验收。
#
#   ⚠ 踩坑：键名必须写**完整路径**（`meta.updated_at`），
#     而 scrub 是递归的、每层只拿到**本级 key 名** —— 首版写成
#     `'meta.updated_at' in keys` 与顶层 `'meta'` 比对，永不命中，
#     归一化形同虚设（表现为「修了还在报不一致」）。
NONDET_PATHS = {
    # 文件名 → 该文件内**需置为占位**的字段 key（按递归层级匹配 key 名）
    'match_result.json': {'updated_at', 'created_at', 'elapsed', 'elapsed_sec'},
    'gen.json': {'created_at', 'updated_at', 'finished_at', 'started_at',
                 'elapsed', 'elapsed_sec'},
}
# 文本类产物：按正则抹掉时长/时间戳数字（如「- 耗时：10.8s」）
NONDET_TEXT_RE = [
    # ⚠ 本文件曾被「转义拷贝」坑过：r'\s*' 落盘成 '\\s*' ⇒ 正则匹配字面
    #   反斜杠、永不命中且不报错。这里改用**不含反斜杠**的等价写法：
    #   空白用字面空格/制表（真实产物是空格分隔），数字用 [0-9]。
    #   形态覆盖：'耗时：10.8s' / '耗时:10.8s' / '耗时 10.8s' / '- 耗时 10.8 s'
    re.compile('耗时[：: ][ ]*[0-9.]+[ ]*s'),
    re.compile('elapsed[_a-z]*[ =:][ ]*[0-9.]+'),
    # 时间戳：用 [0-9] 代替 \d，用 [ T] 字面字符类
    re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}[ T][0-9]{2}:[0-9]{2}:[0-9]{2}'),
]


def _normalize(name: str, raw: bytes) -> bytes:
    """把已知的合法非确定值（时间戳/耗时）替换为占位，再算摘要。"""
    base = Path(name).name
    keys = NONDET_PATHS.get(base)
    if keys:
        try:
            d = json.loads(raw)
        except Exception:
            return raw

        def scrub(o):
            if isinstance(o, dict):
                # ★ 只看**本级 key 名**（递归天然覆盖 meta.updated_at）
                return {k: ('<TS>' if k in keys else scrub(v))
                        for k, v in o.items()}
            if isinstance(o, list):
                return [scrub(x) for x in o]
            return o

        return json.dumps(scrub(d), sort_keys=True,
                          ensure_ascii=False).encode()

    # 文本类：时间戳/耗时归一化（仅对 .md/.txt/.csv，避免动二进制）
    if base.endswith(('.md', '.txt', '.csv')):
        try:
            t = raw.decode('utf-8')
        except UnicodeDecodeError:
            return raw
        for rx in NONDET_TEXT_RE:
            t = rx.sub('<T>', t)
        return t.encode()
    return raw


def digest_tree(d):
    """目录内所有文件 → {相对路径: sha256}（逐文件比对）

    时间戳类字段先归一化（见 NONDET_NORMALIZE），其余字节级比对。
    """
    out = {}
    for p in sorted(Path(d).rglob('*')):
        if p.is_file():
            rel = str(p.relative_to(d))
            out[rel] = hashlib.sha256(_normalize(rel, p.read_bytes())).hexdigest()
    return out


def _selftest() -> int:
    """自证判别力：用**构造目录**验证 digest 比较真的能分辨「同/异/空」。

    判别力要求（每条都必须能让错误实现失败）：
      ① 逐字节相同 → 判「一致」
      ② 只差 1 字节（非归一化字段）→ 判「不一致」并指出该文件
      ③ 只在归一化字段（时间戳/耗时）上不同 → 判「一致」（归一化有效）
      ④ 产物为 0（空目录互比）→ 判「判据无效」，**不得**报一致
      ⑤ 文件数不同 → 判「不一致」
    """
    import json as _json
    ok = bad = 0

    def _mk(root, files):
        r = Path(root)
        r.mkdir(parents=True, exist_ok=True)
        for name, content in files.items():
            fp = r / name
            fp.parent.mkdir(parents=True, exist_ok=True)
            fp.write_text(content, encoding='utf-8')
        return r

    def _report(label, cond, extra=''):
        nonlocal ok, bad
        if cond:
            ok += 1
            print(f'  [OK]   {label}')
        else:
            bad += 1
            print(f'  [FAIL] {label}' + (f'  → {extra}' if extra else ''))

    with tempfile.TemporaryDirectory(prefix='detself_') as td:
        td = Path(td)

        # ① 完全相同
        a = _mk(td / 'a', {'x.txt': 'hello\nworld\n', 'sub/y.json': '{"k":1}'})
        b = _mk(td / 'b', {'x.txt': 'hello\nworld\n', 'sub/y.json': '{"k":1}'})
        da, db = digest_tree(a), digest_tree(b)
        _report('相同产物 → 判一致', da == db and len(da) == 2, f'{da} vs {db}')

        # ② 差 1 字节
        c = _mk(td / 'c', {'x.txt': 'hello\nWorld\n', 'sub/y.json': '{"k":1}'})
        dc = digest_tree(c)
        diff = [k for k in da if dc.get(k) != da[k]]
        _report('差 1 字节 → 判不一致且定位到文件',
                dc != da and diff == ['x.txt'], f'diff={diff}')

        # ③ 仅归一化字段不同 → 应判一致（证明 _normalize 真的在起作用）
        #    ⚠ 归一化是**白名单驱动**（NONDET_PATHS / NONDET_TEXT_RE）——
        #      必须用名单里的真实文件名与字段，否则用例测的是「没归一化」这个事实。
        e = _mk(td / 'e', {'match_result.json':
                           '{"updated_at": "2026-01-01T00:00:00Z", "total": 435}',
                           'r.md': '耗时 10.8s\n'})
        f = _mk(td / 'f', {'match_result.json':
                           '{"updated_at": "2026-09-18T12:00:00Z", "total": 435}',
                           'r.md': '耗时 11.0s\n'})
        _report('仅归一化字段（白名单文件名+字段）不同 → 判一致',
                digest_tree(e) == digest_tree(f))

        # ③b 反向验证：真实差异不得被归一化吃掉（防归一化过宽）
        e2 = _mk(td / 'e2', {'match_result.json': '{"total": 435}'})
        f2 = _mk(td / 'f2', {'match_result.json': '{"total": 999}'})
        _report('归一化不得吃掉真实差异（435 vs 999 仍判不同）',
                digest_tree(e2) != digest_tree(f2))

        # ④ 空目录
        g = _mk(td / 'g', {})
        h = _mk(td / 'h', {})
        dg, dh = digest_tree(g), digest_tree(h)
        _report('空目录 → digest 为空（调用方据此判「判据无效」）',
                len(dg) == 0 and len(dh) == 0, f'{len(dg)},{len(dh)}')

        # ⑤ 文件数不同
        i = _mk(td / 'i', {'x.txt': 'a'})
        j = _mk(td / 'j', {'x.txt': 'a', 'extra.txt': 'b'})
        _report('文件数不同 → 判不一致',
                digest_tree(i) != digest_tree(j))

    print(f'\n结果: {ok}/{ok + bad} 通过')
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--exp', default='')
    ap.add_argument('--product', default='UDG')
    ap.add_argument('--sid', default='')
    ap.add_argument('--sid-root', default='/data/sessions')
    ap.add_argument('--runs', type=int, default=2)
    ap.add_argument('--selftest', action='store_true',
                    help='自证判别力（构造用例验证能分辨同/异/空）')
    a = ap.parse_args()

    if a.selftest:
        return _selftest()

    exp = a.exp
    if a.sid and not exp:
        root = Path(a.sid_root) / a.sid / 'exp_v1'
        cands = sorted(root.glob('*.txt'))
        if not cands:
            print(f'⛔ {root} 下无 EXP 文件')
            return 2
        exp = str(cands[0])
    if not exp or not Path(exp).is_file():
        print('用法: det_check.py --sid <sid> | --exp <path> [--product UDG] [--runs 2]')
        return 2

    p = Path(exp)
    nlines = sum(1 for _ in open(exp, encoding='utf-8', errors='replace'))
    print(f'EXP: {exp}')
    print(f'  大小 {p.stat().st_size/1024/1024:.2f} MB / {nlines} 行')
    print(f'  产品 {a.product}   轮次 {a.runs}')
    print()

    digests, times, allfails = [], [], []
    for i in range(a.runs):
        with tempfile.TemporaryDirectory(prefix=f'det{i}_') as td:
            out = Path(td) / 'out'
            out.mkdir(parents=True)
            sec, fails = run_chain(exp, a.product, out)
            d = digest_tree(out)
            digests.append(d)
            times.append(sec)
            allfails.append(fails)
            print(f'  第 {i+1} 轮: {sec:7.2f}s   产物 {len(d)} 个   失败段 {fails or "无"}')

    print()
    print('═══ 判定 ═══')
    # ★ 关键守卫：产物为空/太少 → 不得报「一致」（空==空 的假绿）
    if min(len(d) for d in digests) == 0:
        print('  ⛔ 产物为 0 → **判据无效**（空目录互比必然"一致"）')
        print(f'     失败段: {allfails}')
        print('     先修命令行/路径，再谈确定性。')
        return 3
    if allfails and any(allfails):
        print(f'  ⚠ 存在失败段 {allfails} → 结果可信度受损，建议先修')

    base = digests[0]
    identical = True
    for i in range(1, a.runs):
        cur = digests[i]
        only_a, only_b = set(base) - set(cur), set(cur) - set(base)
        diff = [k for k in (set(base) & set(cur)) if base[k] != cur[k]]
        if only_a or only_b or diff:
            identical = False
        print(f'  轮1 vs 轮{i+1}: 仅轮1有={sorted(only_a) or "无"}  '
              f'仅轮{i+1}有={sorted(only_b) or "无"}  内容不同={sorted(diff) or "无"}')
        for k in sorted(diff)[:5]:
            print(f'      {k}: 轮1={base[k][:16]}  轮{i+1}={cur[k][:16]}')
    print()
    if identical:
        print(f'  ✅ {len(base)} 个产物**字节完全一致** → 「结果不变」可机器验收')
        print(f'     耗时 {["%.2fs" % t for t in times]}')
    else:
        print('  ⛔ 存在非确定性 → 优化前须先消除，否则无法区分'
              '「优化改了结果」与「本来就不稳定」')
    print(json.dumps({'identical': identical, 'files': len(base),
                      'times': [round(t, 2) for t in times],
                      'fails': allfails, 'names': sorted(base)},
                     ensure_ascii=False, indent=2))
    return 0 if identical else 1


if __name__ == '__main__':
    sys.exit(main())
