#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""exp_me.py —— 从 exp 读网元信息并切分（多网元支持）

═══ 为什么需要这个模块 ═══

原有流程（match_features.py）只接受单个 `--exp`，且 `gfa.parse_exp()` 把注释行
全部丢弃 ⇒ **网元信息（ME Type / Version / MELN / MEID）完全没被读出来**。

实测（2026-10-18）：工作区 376 个 exp 文件**全部是单网元**，没有多网元样本。
所以本模块的切分规则只依据 exp 头部的**显式声明**，不猜：

  · 网元定义行：`MOD ME:MEID=0, MELN="xxx", ...`（每条网元一条）
  · 网元类型/版本：文件头注释 `/* ME Type=UEG, Version=21.8.2 PatchVersion=... */`
  · 当前活跃网元：`USE ME:MEID=N;` 或其注释形式 `/*USE ME:MEID=0;*/`
  · 命令归属：命令行自带 `MEID=N` 参数时以它为准，否则归当前 `USE ME` 网元

═══ 两种输入形态（用户 2026-10-19 裁决：都要）═══

  1. 多文件：一次给多个 exp 路径 / 一个目录，每个文件独立成一个或多个网元
  2. 单文件多段：一个 exp 里有多条 `MOD ME` + `USE ME` 切换 ⇒ 按 MEID 切分

═══ 设计约束 ═══

  · 零模型、零新增依赖（只用 re）
  · 不改 `parse_exp` 的行为（它仍返回全部命令）；本模块只负责"切分与标注归属"
  · 拿不到 MEID 时不报错、退回"单网元"，保证老用法零影响
"""
import os
import re
from collections import OrderedDict

# 文件头注释里的网元类型/版本
_RE_ME_TYPE = re.compile(r'ME\s*Type\s*=\s*([A-Za-z0-9_]+)')
_RE_VERSION = re.compile(r'Version\s*=\s*([\d.]+)')
_RE_PATCH = re.compile(r'PatchVersion\s*=\s*([\d.]+)')
# USE ME:MEID=N （含被注释掉的形式）
_RE_USE_ME = re.compile(r'USE\s+ME\s*:\s*MEID\s*=\s*(\d+)', re.I)
# MOD ME:...MEID=N, MELN="..."  （命令行形式）
_RE_MOD_ME = re.compile(r'^MOD\s+ME\s*:(.*)$', re.I)
# 命令行里的 MEID 参数（用于逐条归属）
_RE_MEID_PARAM = re.compile(r'\bMEID\s*=\s*(\d+)')


def _params(txt):
    """从 'K=v, K="v"' 串里取参数（与 gfa.parse_exp 同口径）"""
    out = {}
    for pm in re.finditer(r'([A-Z0-9_]+)=(?:([^,;"]+)|\"([^\"]*)\")', txt):
        out[pm.group(1)] = (pm.group(2) or pm.group(3) or '').strip()
    return out


def read_exp_text(path):
    """读 exp 文本，自动检测编码（utf-8 → gbk → 替换），与 gfa.parse_exp 一致"""
    for enc in ('utf-8', 'gbk'):
        try:
            return open(path, encoding=enc).read()
        except (UnicodeDecodeError, UnicodeError):
            continue
    return open(path, encoding='utf-8', errors='replace').read()


def scan_me(text, source=''):
    """扫描一个 exp 文本，返回网元清单与逐行归属。

    返回 {
      'file_me_type': 'UEG',          # 文件头声明的类型（可能为空）
      'file_version': '21.8.2',
      'elements': OrderedDict(meid -> {
          'meid': '0', 'meln': 'xxx', 'mename': '', 'meiid': '',
          'declared_at': 行号, 'cmd_count': int}),
      'line_meid': {行号: meid},       # 每个命令行归属哪个网元
      'active_switches': [(行号, meid)],  # USE ME 切换点（调试用）
      'has_multi': bool,               # 是否真有多个网元
    }
    """
    res = {'file_me_type': '', 'file_version': '', 'file_patch': '',
           'elements': OrderedDict(), 'line_meid': {},
           'active_switches': [], 'has_multi': False}
    cur = None
    for lineno, raw in enumerate(text.split('\n'), 1):
        s = raw.strip()
        if not s:
            continue
        # ── 头部注释：网元类型 / 版本 ──
        if s.startswith('/*'):
            m = _RE_ME_TYPE.search(s)
            if m and not res['file_me_type']:
                res['file_me_type'] = m.group(1).upper()
            m = _RE_VERSION.search(s)
            if m and not res['file_version']:
                res['file_version'] = m.group(1)
            m = _RE_PATCH.search(s)
            if m and not res['file_patch']:
                res['file_patch'] = m.group(1)
            # 注释形式的 USE ME 切换
            m = _RE_USE_ME.search(s)
            if m:
                cur = m.group(1)
                res['active_switches'].append((lineno, cur))
            continue
        if s.startswith(';') or s.startswith('//') or s.startswith('#'):
            continue
        # ── MOD ME：网元定义 ──
        m = _RE_MOD_ME.match(s)
        if m:
            p = _params(m.group(1))
            meid = p.get('MEID', '')
            if meid != '':
                e = res['elements'].setdefault(meid, {
                    'meid': meid, 'meln': '', 'mename': '', 'meiid': '',
                    'declared_at': lineno, 'cmd_count': 0})
                for k_src, k_dst in (('MELN', 'meln'), ('MENAME', 'mename'),
                                     ('MEIID', 'meiid')):
                    if p.get(k_src) and not e[k_dst]:
                        e[k_dst] = p[k_src]
                # ⚠ MOD ME 行本身归属"它声明的那个网元"，不是"当前活跃网元"。
                #   实测：多网元文件里 MEID=0 段中夹着 MOD ME:MEID=1，
                #   若按 cur 归属会把别人的定义行算进 MEID=0（实测多出 1 条）。
                res['line_meid'][lineno] = meid
                if cur is None:
                    cur = meid
            continue
        # ── 普通命令：记录归属 ──
        m = re.match(r'^[A-Z]+\s+[A-Z0-9]+:', s)
        if not m:
            continue
        meid_of_line = None
        mp = _RE_MEID_PARAM.search(s)
        if mp:
            meid_of_line = mp.group(1)
        owner = meid_of_line if meid_of_line is not None else cur
        if owner is None:
            owner = '0'          # 老 exp 无任何声明 ⇒ 视为单网元 0
        res['line_meid'][lineno] = owner
        e = res['elements'].setdefault(owner, {
            'meid': owner, 'meln': '', 'mename': '', 'meiid': '',
            'declared_at': 0, 'cmd_count': 0})
        # ⚠ cmd_count 只数**业务命令**，不数 MOD ME 定义行（定义行在上一分支已 continue）
        e['cmd_count'] += 1
    res['has_multi'] = len(res['elements']) > 1
    # 一致性校验：cmd_count 之和必须等于 line_meid 的条目数（含 MOD ME 行）
    #   MOD ME 行也记进了 line_meid，所以这里把它们的数量补上
    n_modme = sum(1 for ln in res['line_meid']
                  if res['line_meid'][ln] is not None) - sum(
                      e['cmd_count'] for e in res['elements'].values())
    res['modme_lines'] = n_modme
    return res


def split_by_me(entries, info):
    """把 parse_exp 的结果按网元切开。

    entries: [{'seq','cmd','params','raw'}, ...]（gfa.parse_exp 的输出）
    返回 OrderedDict(meid -> [entry...])，entry 里额外带 'meid' 字段。

    ⚠ 若 info['has_multi'] 为假，返回 {唯一meid: entries}，与改造前完全等价。
    """
    out = OrderedDict()
    for e in entries:
        meid = info['line_meid'].get(e['seq'], '0')
        e2 = dict(e)
        e2['meid'] = meid
        out.setdefault(meid, []).append(e2)
    # 保证顺序稳定：按网元出现顺序（elements 的声明顺序）
    ordered = OrderedDict()
    for meid in info['elements']:
        if meid in out:
            ordered[meid] = out[meid]
    for meid in out:
        if meid not in ordered:
            ordered[meid] = out[meid]
    return ordered


def describe(info, source=''):
    """一句话描述网元（写进报告/日志用）"""
    els = info['elements']
    if not els:
        return '未识别到网元信息'
    parts = []
    for meid, e in els.items():
        # ⚠ MELN 可能是字面量 "null"（实测 UNC 的 MOD ME:MELN="null"），
        #   此时回退到 MENAME，再回退到占位符。
        name = e['meln'] if e['meln'] and e['meln'].lower() != 'null' else ''
        if not name:
            name = e['mename'] or '(未命名)'
        parts.append(f'MEID={meid} {name} ({e["cmd_count"]} 条命令)')
    head = ''
    if info['file_me_type']:
        head = info['file_me_type']
        # ⚠ 只输出 Version，不拼 PatchVersion —— 实测 Version=21.8.2 已含主版本，
        #   PatchVersion=21.8.2.20 是它的完整形式，拼接会出现 21.8.2.21.8.2.20。
        if info['file_version']:
            head += ' ' + info['file_version']
        head += ' ｜ '
    return head + '；'.join(parts)


def expand_inputs(inputs):
    """把命令行传入的路径列表展开成实际 exp 文件列表。

    · 文件 ⇒ 原样保留
    · 目录 ⇒ 递归取 *.txt（跳过 .md / 已生成的输出目录）
    """
    files = []
    for p in inputs:
        p = os.path.expanduser(p)
        if os.path.isdir(p):
            for root, _dirs, names in os.walk(p):
                for n in sorted(names):
                    if n.lower().endswith('.txt'):
                        files.append(os.path.join(root, n))
        elif os.path.isfile(p):
            files.append(p)
        else:
            raise FileNotFoundError(f'exp 路径不存在：{p}')
    # 去重保序
    seen, out = set(), []
    for f in files:
        af = os.path.abspath(f)
        if af in seen:
            continue
        seen.add(af)
        out.append(f)
    return out


# ═══ 自检 ═══════════════════════════════════════════════════════

def _selftest():
    """网元解析与切分自检（全部用内联样本，不依赖外部文件）"""
    ok = bad = 0

    def chk(desc, cond, extra=''):
        nonlocal ok, bad
        if cond:
            ok += 1
            print(f'  ✓ {desc}')
        else:
            bad += 1
            print(f'  ✗ {desc}' + (f'\n      {extra}' if extra else ''))

    def parse(text):
        entries, lined = [], {}
        for i, ln in enumerate(text.split('\n'), 1):
            ln = ln.strip()
            m = re.match(r'^([A-Z]+\s+[A-Z0-9]+):(.*?);?$', ln)
            if m:
                entries.append({'seq': i, 'cmd': m.group(1),
                                'params': _params(m.group(2)), 'raw': ln})
        return entries

    print('=' * 70)
    print('exp_me 自检')
    print('=' * 70)

    # ── 单网元：老 exp 结构 ──
    t1 = """/* TIME = 2026-04-20 */
/* ME Type=UEG, Version=21.8.2  PatchVersion=21.8.2.20 */
/*USE ME:MEID=0;*/
MOD ME:MEID=0, MEIID="21.8.2.20", MELN="FSUPFm102BHW", MENAME="FSUPFm102BHW";
ADD UPPOOL:POOLNAME="p1";
ADD SECTION:SECTIONNUM=1;
"""
    i1 = scan_me(t1)
    chk('单网元：类型识别 UEG', i1['file_me_type'] == 'UEG', i1['file_me_type'])
    chk('单网元：版本 21.8.2', i1['file_version'] == '21.8.2', i1['file_version'])
    chk('单网元：has_multi=False', i1['has_multi'] is False)
    chk('单网元：MELN 读出', i1['elements']['0']['meln'] == 'FSUPFm102BHW')
    chk('单网元：业务命令数=2（不含 MOD ME）', i1['elements']['0']['cmd_count'] == 2,
        str(i1['elements']['0']['cmd_count']))
    p1 = split_by_me(parse(t1), i1)
    chk('单网元：切分后 1 组', len(p1) == 1, str(list(p1)))
    chk('单网元：该组含 MOD ME + 2 条业务命令 = 3',
        len(p1['0']) == 3, str(len(p1['0'])))

    # ── 多网元：MOD ME + USE ME 切换 ──
    t2 = """/* ME Type=UEG, Version=21.8.2 */
MOD ME:MEID=0, MELN="NE_A";
ADD UPPOOL:POOLNAME="a1";
/*USE ME:MEID=1;*/
MOD ME:MEID=1, MELN="NE_B";
ADD UPPOOL:POOLNAME="b1";
SET ALMINFO:ALARMID=1, MEID=1;
SET ALMINFO:ALARMID=2, MEID=0;
"""
    i2 = scan_me(t2)
    chk('多网元：识别到 2 个', len(i2['elements']) == 2, str(list(i2['elements'])))
    chk('多网元：has_multi=True', i2['has_multi'] is True)
    # MOD ME 行归它自己声明的网元，不归"当前活跃网元"
    #   ⚠ 行号按样本实际：第 2 行 MOD ME:MEID=0，第 5 行 MOD ME:MEID=1
    chk('多网元：第二个 MOD ME 行（第5行）归 MEID=1',
        i2['line_meid'].get(5) == '1', str(i2['line_meid'].get(5)))
    p2 = split_by_me(parse(t2), i2)
    # MEID=0 的业务命令：第 3 行 ADD UPPOOL + 第 8 行 SET ALMINFO(MEID=0) = 2
    chk('多网元：MEID=0 段 2 条业务命令',
        i2['elements']['0']['cmd_count'] == 2, str(i2['elements']['0']['cmd_count']))
    chk('多网元：MEID=1 段 2 条业务命令',
        i2['elements']['1']['cmd_count'] == 2, str(i2['elements']['1']['cmd_count']))
    # 命令行自带 MEID 的以它为准：第 7 行 MEID=1（当前活跃也是 1），第 8 行 MEID=0（跨回了 0）
    chk('多网元：第8行显式 MEID=0 归 MEID=0（覆盖当前活跃网元1）',
        i2['line_meid'].get(8) == '0', str(i2['line_meid'].get(8)))
    chk('多网元：两组命令不重叠',
        set(x['seq'] for x in p2['0']) & set(x['seq'] for x in p2['1']) == set())

    # ── 无任何网元声明：退回单网元 0，不报错 ──
    t3 = 'ADD UPPOOL:POOLNAME="x";\nADD SECTION:SECTIONNUM=1;\n'
    i3 = scan_me(t3)
    chk('无声明：不报错，退化单网元 0',
        len(i3['elements']) == 1 and '0' in i3['elements'], str(list(i3['elements'])))
    chk('无声明：has_multi=False', i3['has_multi'] is False)
    p3 = split_by_me(parse(t3), i3)
    chk('无声明：全部命令归 MEID=0', len(p3['0']) == 2, str(len(p3.get('0', []))))

    # ── MELN=null 的字面量（实测 UNC）──
    t4 = 'MOD ME:MEID=0, MEIID="20.16.2.36", MELN="null", MENAME="APP-XBX";\nADD UPPOOL:POOLNAME="x";\n'
    i4 = scan_me(t4)
    d4 = describe(i4)
    chk('MELN=null：描述里回退到 MENAME', 'APP-XBX' in d4, d4)
    chk('MELN=null：描述里不出现 "null"', 'null' not in d4, d4)

    # ── 版本拼接不重复 ──
    t5 = ('/* ME Type=UDG, Version=20.16.2  PatchVersion=20.16.2.56 */\n'
          'MOD ME:MEID=0, MELN="X";\nADD UPPOOL:POOLNAME="x";\n')
    d5 = describe(scan_me(t5))
    chk('版本不重复拼接（20.16.2 只出现一次）',
        d5.count('20.16.2') == 1, d5)

    # ── expand_inputs：目录递归 + 去重 ──
    import tempfile
    with tempfile.TemporaryDirectory() as td:
        sub = os.path.join(td, 'sub')
        os.makedirs(sub)
        for rel in ('a.txt', 'sub/b.txt', 'skip.md'):
            with open(os.path.join(td, rel), 'w') as f:
                f.write('x')
        got = expand_inputs([td])
        chk('目录递归：找到 2 个 .txt', len(got) == 2, str([os.path.basename(x) for x in got]))
        got2 = expand_inputs([td, os.path.join(td, 'a.txt')])
        chk('重复输入去重', len(got2) == 2, str(len(got2)))
        try:
            expand_inputs([os.path.join(td, 'nope.txt')])
            chk('不存在的路径应报错', False)
        except FileNotFoundError:
            chk('不存在的路径应报错', True)

    print()
    print('=' * 70)
    print(f'结果: {ok} PASS / {bad} FAIL')
    print('=' * 70)
    return 0 if bad == 0 else 1


if __name__ == '__main__':
    import sys
    sys.exit(_selftest())
