#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""N19 主键推导验证（**走真实装配路径**，不直接调内部函数）。

用法（容器内 /opt/expgv/backend 下）：
    python3 n19_verify2.py <schema.json> <exp.txt>

为什么必须走 schema_to_mml：
  · 去重、引用链查表、预扫描都在**装配循环**里，直接调 _derive_key_value
    会绕开它们 → 验证结果与真实产物不符（上一版就漏掉了「重复名」问题）。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, '/opt/expgv/backend')
import gen_assemble as ga  # noqa: E402


def main():
    if len(sys.argv) < 3:
        print('用法: n19_verify2.py <schema.json> <exp.txt>')
        return 2
    schema = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    schema.setdefault('meta', {})['exp_path'] = sys.argv[2]

    idx = ga._load_exp_name_index(schema)
    print(f'现网 EXP 命名索引: {len(idx)} 类命令')

    mml = ga.schema_to_mml(schema)
    lines = [l for l in mml.splitlines() if l.strip() and not l.strip().startswith('//')]
    print(f'装配产出可执行命令: {len(lines)} 条')
    print('=' * 88)

    # 提取「命令 → **对象名**（规则表 key_param 指定的参数）」
    #  ⚠ 不能取"第一个参数"：实测 ADD BWMUSERGROUP 的首参是
    #    USERGROUPTYPE（类型枚举），真正的对象名是 USERGROUPNAME。
    rules = ga._load_name_rules()
    fams = rules.get('command_families') or {}
    names, ph = [], []
    for l in lines:
        m = re.match(r'^([A-Z][A-Z0-9_ ]*?)\s*:\s*(.*?);?$', l)
        if not m:
            continue
        cmd, body = m.group(1).strip(), m.group(2)
        bare = ga._cmd_bare(cmd)
        fam = fams.get(bare) or {}
        kp = (fam.get('key_param') or '').upper()
        if not kp:
            continue                     # 无对象名参数的命令（SET/DSP 等）跳过
        kv = re.search(rf'\b{kp}\s*=\s*"?([^,";]*)', body)
        if not kv:
            continue
        v = kv.group(1).strip()
        if v.startswith('<') or '【' in v:
            ph.append((cmd, kp, v))
        else:
            names.append((cmd, kp, v))

    print(f'{"命令":30s} {"主键参数":22s} 对象名')
    print('-' * 88)
    for c, p, v in names:
        print(f'  {c:28s} {p:22s} {v}')

    if ph:
        print(f'\n  —— 落占位 {len(ph)} 条 ——')
        for c, p, v in ph:
            print(f'  {c:28s} {p:22s} {v}')

    print('-' * 88)
    print(f'  真名 {len(names)} 条 / 占位 {len(ph)} 条 / 合计 {len(names) + len(ph)}')

    # ── 判据①：同族对象名不得重复（MML 唯一性）──
    from collections import Counter
    dup = [f'{c}::{v}×{n}' for (c, v), n in
           Counter((c, v) for c, p, v in names).items() if n > 1]
    if dup:
        print(f'\n  ✗ 同族对象名重复（第 2 条起会执行失败）: {dup}')
        return 1
    print('  ✓ 同族对象名无重复（唯一性满足）')

    # ── 判据②：真名须符合现网命名形态 ──
    bad = []
    for c, pk, v in names:
        bare = ga._cmd_bare(c)
        fam = (rules.get('command_families') or {}).get(bare) or {}
        pfx = fam.get('prefix') or ''
        if pfx and not v.startswith(pfx.rstrip('_')):
            bad.append(f'{bare}: {v} 缺前缀 {pfx}')
        elif not re.fullmatch(r'[A-Za-z0-9_.\-]+', v):
            bad.append(f'{bare}: {v} 形态异常')
    if bad:
        print('\n  ✗ 形态异常:')
        for b in bad:
            print(f'      {b}')
        return 1
    print('  ✓ 全部真名符合现网命名形态')
    return 0


if __name__ == '__main__':
    sys.exit(main())
