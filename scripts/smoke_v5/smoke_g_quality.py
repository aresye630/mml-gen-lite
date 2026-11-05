#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_g_quality.py — G 组冒烟：产物质量与三产品（容器内执行）

覆盖原冒烟集 D/B 组的判据升级（见 原冒烟集问题反查.md）：
  G1  mml.txt 非空（行数阈值）              ★问题#5.2
  G2  引号成对率 100%                        ★问题#6
  G3  无空值参数（=, / =;）
  G4  命令可解析率 100%
  G5  六种产物齐全且均非空（含 template/清单）
  G6  三库产品分布逐项断言                   ★原 B1 只查非空
  G7  三产品检索均可用
  G8  nav 数据量提示（UDG/UNC 源数据少）

用法:
    python3 smoke_g_quality.py --sid <session_id>
    python3 smoke_g_quality.py --sid <sid> --gen g4 --json out.json
"""
import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

RESULTS = []
SESSION_ROOT = Path('/data/sessions')
SKILLS = Path.home() / '.hermes' / 'skills'
MILVUS_DB = Path.home() / 'workspace' / 'database' / 'milvus_mml.db'

CMD_RE = re.compile(r'^([A-Z][A-Z0-9]*(?:\s+[A-Z0-9*]+)?):(.*?);?\s*$')
KV_RE = re.compile(r'([A-Z][A-Z0-9]*)=(?:"[^"]*"|[^,;]*)')
EMPTY_RE = re.compile(r'=\s*[,;]')


def case(cid, name, fn):
    import time
    t0 = time.time()
    try:
        detail = fn()
        ok, msg = (detail if isinstance(detail, tuple) else (bool(detail), ''))
    except Exception as e:
        ok, msg = False, f'{type(e).__name__}: {e}'
    dt = time.time() - t0
    RESULTS.append({'id': cid, 'name': name, 'ok': bool(ok),
                    'msg': str(msg), 'sec': round(dt, 2)})
    print(f'  [{"PASS" if ok else "FAIL"}] {cid} {name}  ({dt:.1f}s)')
    if msg:
        for ln in str(msg).splitlines()[:6]:
            print(f'         {ln}')
    return ok


def _read(gid, fname):
    p = SESSION_ROOT / SID / 'gen_v1' / gid / fname
    return p.read_text(encoding='utf-8', errors='replace') if p.is_file() else None


def _cmd_lines(txt):
    lines = [l.strip() for l in (txt or '').splitlines() if l.strip()]
    return [l for l in lines if not l.startswith('//')], \
           [l for l in lines if l.startswith('//')]


# ─────────── G1 mml.txt 非空 ───────────

def g1_mml_nonempty():
    """mml.txt 必须有真实命令（非纯注释）—— 反例：19 字节只有注释头"""
    txt = _read(GID, 'mml.txt')
    if txt is None:
        return False, f'{GID}/mml.txt 不存在'
    cmds, cmts = _cmd_lines(txt)
    if len(txt) < 60 or not cmds:
        return False, (f'{GID}/mml.txt = {len(txt)} 字符、'
                       f'命令 {len(cmds)} 条、注释 {len(cmts)} 条 —— 空产物')
    return True, f'{len(txt)} 字符 / 命令 {len(cmds)} 条 / 注释 {len(cmts)} 条'


# ─────────── G2 引号成对 ───────────

def g2_quotes():
    txt = _read(GID, 'mml.txt') or ''
    cmds, _ = _cmd_lines(txt)
    withq = [c for c in cmds if '"' in c]
    bad = [c for c in withq if c.count('"') % 2]
    if bad:
        return False, f'{len(bad)}/{len(withq)} 条引号不成对，样本: {bad[0][:80]}'
    return True, f'{len(withq)} 条含引号命令全部成对'


# ─────────── G3 空值参数 ───────────

def g3_empty_value():
    txt = _read(GID, 'mml.txt') or ''
    cmds, _ = _cmd_lines(txt)
    bad = [c for c in cmds if EMPTY_RE.search(c)]
    if bad:
        return False, f'{len(bad)} 条含空值参数(=, / =;)，样本: {bad[0][:80]}'
    return True, '无空值参数'


# ─────────── G4 可解析率 ───────────

def g4_parsable():
    txt = _read(GID, 'mml.txt') or ''
    cmds, _ = _cmd_lines(txt)
    bad = [c for c in cmds if not CMD_RE.match(c)]
    if bad:
        return False, f'{len(bad)}/{len(cmds)} 条无法解析，样本: {bad[0][:80]}'
    return True, f'{len(cmds)} 条 100% 可解析'


# ─────────── G5 六种产物齐全且非空 ───────────

PRODUCTS = [('schema.json', 500), ('params.csv', 100),
            ('确认清单.md', 200), ('template.md', 200),
            ('mml.txt', 60), ('gen.json', 100)]


def g5_all_products():
    """★ 2026-09-18 修：产物集因**生成路径**而异，不能拿一个固定 gen 判「六件套齐」。
      · agent 路径（配置分析）：md + params.csv + schema.json + 确认清单.md + mml.txt
        —— **无 template.md**（md 即方案正文）
      · 装配路径（确定性）：schema.json + params.csv + 确认清单.md + template.md + mml.txt
    旧实现固定取最新 gen（常是 agent 草案）→ 误报「缺 template.md」。
    现改为：优先挑**含 template.md 的装配节点**；若本会话确实只有 agent 草案，
    则按 agent 的产物集校验（5 件），并在消息里说明路径。
    """
    base = SESSION_ROOT / SID / 'gen_v1'
    # 探测：哪些 gen 有 template.md（装配路径）
    asm, agent_path = [], []
    for d in sorted(base.glob('g*'), key=lambda x: x.stat().st_mtime, reverse=True):
        if not d.is_dir():
            continue
        has_tpl = (d / 'template.md').is_file()
        has_mml = (d / 'mml.txt').is_file()
        has_csv = (d / 'params.csv').is_file()
        if not (has_mml or has_csv):
            continue
        (asm if has_tpl else agent_path).append(d.name)
    # ★ 取样稳健性（2026-09-18）：优先取**产物完备**的节点，而不是「最新」的 ——
    #   生成中的节点（文件未落齐）会被误判成缺产物，导致同类用例结果抖动。
    #   判据：优先装配路径（含 template.md），其中再优先 6 件齐全者。
    if asm:
        complete = [n for n in asm
                    if all((base / n / f).is_file() for f, _ in PRODUCTS)]
        gid = (complete or asm)[0]
    else:
        gid = (agent_path or [GID])[0]
    path_kind = '装配' if (asm and gid in asm) else 'agent'
    need = (PRODUCTS if path_kind == '装配'
            else [(f, m) for f, m in PRODUCTS if f != 'template.md'])
    missing, tiny = [], []
    for fname, minsize in need:
        p = base / gid / fname
        if not p.is_file():
            missing.append(fname)
        elif p.stat().st_size < minsize:
            tiny.append(f'{fname}({p.stat().st_size}B<{minsize}B)')
    if missing:
        return False, f'[{path_kind}路径 {gid}] 缺失: {missing}'
    if tiny:
        return False, f'[{path_kind}路径 {gid}] 过小: {tiny}'
    return True, f'[{path_kind}路径 {gid}] {len(need)} 种产物齐全且非空'


# ─────────── G6 三库产品分布 ───────────

EXPECT = {
    'mml_feature': {'UEG': 600, 'UDG': 357, 'UNC': 547},
    'mml_nav': {'UEG': 9578, 'UDG': 3, 'UNC': 2},
    'mml_support': {'UEG': 22238, 'UDG': 4746, 'UNC': 8771},
}


def _g6_worker():
    """子进程 worker：查产品分布，结果以 JSON 打到 stdout。

    ⚠ Milvus Lite 单进程独占，且 close() 不释放文件锁
      → 必须走子进程，用完进程退出即释放（同 G7 检索子进程可继续访问）。
    """
    sys.path.insert(0, '/opt/expgv/scripts/mml_retrieval')
    from pymilvus import MilvusClient
    c = MilvusClient(str(MILVUS_DB))
    out = {}
    for coll in EXPECT:
        c.load_collection(coll)
        cnt = Counter()
        off = 0
        while True:
            rows = c.query(coll, filter='', output_fields=['product'],
                           limit=4096, offset=off)
            if not rows:
                break
            for r in rows:
                cnt[r.get('product')] += 1
            if len(rows) < 4096:
                break
            off += 4096
        out[coll] = dict(cnt)
    print(json.dumps(out, ensure_ascii=False))


def g6_distribution():
    """逐产品条数断言（走子进程，避免占用 Milvus 文件锁）"""
    py = os.environ.get('SMOKE_PY') or (sys.executable if sys.executable else '') or 'python3'
    self_path = Path(__file__).resolve()
    if not self_path.is_file():
        return False, f'无法定位自身脚本（{self_path}）—— 需以文件方式执行'
    try:
        r = subprocess.run([py, str(self_path), '--g6-worker'],
                           capture_output=True, text=True, timeout=300)
    except Exception as e:
        return False, f'{type(e).__name__}: {e}'
    if r.returncode != 0:
        return False, f'G6 worker rc={r.returncode}: {(r.stderr or "")[-200:]}'
    # 取最后一行 JSON（前面可能有 SyntaxWarning）
    data = None
    for ln in reversed((r.stdout or '').strip().splitlines()):
        ln = ln.strip()
        if ln.startswith('{'):
            try:
                data = json.loads(ln)
                break
            except Exception:
                continue
    if data is None:
        return False, f'G6 worker 无反序列化输出: {(r.stdout or "")[-200:]}'
    bad, good = [], []
    for coll, exp in EXPECT.items():
        got_map = data.get(coll) or {}
        for prod, want in exp.items():
            got = got_map.get(prod, 0)
            if got != want:
                bad.append(f'{coll}.{prod}: {got} != {want}')
            else:
                good.append(f'{coll}.{prod}={got}')
    if bad:
        return False, '分布不符:\n' + '\n'.join(bad[:5])
    return True, f'{len(good)} 项产品分布逐项吻合'


# ─────────── G7 三产品检索 ───────────

def g7_retrieval():
    """三产品特性检索必须可用（有正确命中）"""
    outs, bad = [], []
    py = os.environ.get('SMOKE_PY') or (sys.executable if sys.executable else '') or 'python3'
    p = SKILLS / 'mml_feature' / 'scripts' / 'mml_feature_query.py'
    if not p.is_file():
        return False, f'检索脚本缺失: {p}'
    for prod in ('UEG', 'UDG', 'UNC'):
        try:
            r = subprocess.run([py, str(p), 'semantic',
                                'QoS 保障', '--product', prod],
                               capture_output=True, text=True, timeout=300,
                               cwd=str(p.parent))
            out = r.stdout or ''
            hit = 'feature_name' in out
            rc = r.returncode
        except Exception as e:
            bad.append(f'{prod}: {type(e).__name__}: {e}')
            outs.append(f'{prod}:ERR')
            continue
        outs.append(f'{prod}:{"OK" if hit else "NO_HIT"}')
        if not hit:
            bad.append(f'{prod} 无命中（rc={rc}）')
    if bad:
        return False, '; '.join(bad)
    return True, ' '.join(outs)


# ─────────── G8 nav 数据提示 ───────────

def g8_nav_notice():
    """nav 数据少的产品应被识别（不是缺陷，但须可见）"""
    notes = []
    for prod in ('UEG', 'UDG', 'UNC'):
        n = EXPECT['mml_nav'].get(prod, 0)
        notes.append(f'{prod}={n}')
    thin = [p for p in ('UDG', 'UNC') if EXPECT['mml_nav'].get(p, 0) < 10]
    return True, f'nav 分布 {" ".join(notes)}；薄弱产品: {thin or "无"}'


GID = 'g4'
SID = ''

CASES = [
    ('G1', 'mml.txt 非空（有真实命令）', g1_mml_nonempty),
    ('G2', '引号成对率 100%', g2_quotes),
    ('G3', '无空值参数', g3_empty_value),
    ('G4', '命令可解析率 100%', g4_parsable),
    ('G5', '六种产物齐全且非空', g5_all_products),
    ('G6', '三库产品分布逐项吻合', g6_distribution),
    ('G7', '三产品检索可用', g7_retrieval),
    ('G8', 'nav 数据量可见', g8_nav_notice),
]


def main():
    global SID, GID
    ap = argparse.ArgumentParser(description='G 组冒烟：产物质量与三产品')
    ap.add_argument('--sid', default='')
    ap.add_argument('--gen', default='', help='指定 gen（默认取第一个有 mml.txt 的）')
    ap.add_argument('--json', default='')
    ap.add_argument('--only', default='')
    ap.add_argument('--g6-worker', action='store_true',
                    help='内部：以子进程方式执行 G6 数据采集')
    args = ap.parse_args()

    # 子进程 worker 模式（Milvus Lite 单进程独占 → 走子进程）
    if args.g6_worker:
        _g6_worker()
        return 0

    SID = args.sid
    if not SID:
        print('!! 必须指定 --sid', file=sys.stderr)
        return 2
    if args.gen:
        GID = args.gen
    else:
        root = SESSION_ROOT / SID / 'gen_v1'
        cands = [d.name for d in sorted(root.iterdir())
                 if d.is_dir() and (d / 'mml.txt').is_file()
                 and (d / 'mml.txt').stat().st_size > 200] if root.is_dir() else []
        if cands:
            GID = cands[-1]
    only = {x.strip().upper() for x in args.only.split(',') if x.strip()}

    print('=' * 58)
    print(f' G 组冒烟（产物质量/三产品）sid={SID} gen={GID}')
    print('=' * 58)

    for cid, name, fn in CASES:
        if only and cid not in only:
            continue
        case(cid, name, fn)

    total = len(RESULTS)
    passed = sum(1 for r in RESULTS if r['ok'])
    print('\n' + '=' * 58)
    print(f' G 组汇总: {passed}/{total} 通过')
    for r in [x for x in RESULTS if not x['ok']]:
        print(f'   {r["id"]} {r["name"]}: {r["msg"][:140]}')
    print('=' * 58)

    if args.json:
        Path(args.json).write_text(json.dumps(
            {'group': 'G', 'total': total, 'passed': passed, 'results': RESULTS},
            ensure_ascii=False, indent=2))
        print(f'结果已落盘: {args.json}')
    return 0 if not [x for x in RESULTS if not x['ok']] else 1


if __name__ == '__main__':
    sys.exit(main())
