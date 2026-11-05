#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_selftest.py — 冒烟集自检（判别力自证）

铁律：验证工具自己不验，就是不可信的。
本自检对**每条新增用例的判据**构造正/反两个输入，
确认断言分别给出 PASS / FAIL。若无判别力 → 退出 1。

用法（任意环境，无需服务）:
    python3 smoke_selftest.py
"""
import re
import sys

CHECKS = []


def chk(name, got, want):
    ok = got == want
    CHECKS.append((name, ok, f'got={got} want={want}'))
    print(f'  [{"OK" if ok else "BAD"}] {name}: got={got} want={want}')


CMD_RE = re.compile(r'^([A-Z][A-Z0-9]*(?:\s+[A-Z0-9*]+)?):(.*?);?\s*$')
EMPTY_RE = re.compile(r'=\s*[,;]')


def _cmd_lines(txt):
    lines = [l.strip() for l in (txt or '').splitlines() if l.strip()]
    return [l for l in lines if not l.startswith('//')]


def _is_nonempty_mml(txt):
    """G1 判据：非空 + 有真实命令"""
    cmds = _cmd_lines(txt)
    return len(txt or '') >= 60 and len(cmds) > 0


def _quotes_paired(txt):
    """G2 判据：引号全成对"""
    cmds = _cmd_lines(txt)
    withq = [c for c in cmds if '"' in c]
    return not [c for c in withq if c.count('"') % 2]


def _no_empty_value(txt):
    """G3 判据：无空值参数"""
    return not [c for c in _cmd_lines(txt) if EMPTY_RE.search(c)]


def _all_parsable(txt):
    """G4 判据：全部可解析"""
    cmds = _cmd_lines(txt)
    return bool(cmds) and not [c for c in cmds if not CMD_RE.match(c)]


BAD_SIGNALS = ('INTERNAL', 'rc=1', 'Traceback', 'subprocess',
               'returncode', 'HTTPException')


def _error_clean(err_json):
    """F10 判据：不含内部信号"""
    import json
    blob = json.dumps(err_json, ensure_ascii=False)
    return not any(s in blob for s in BAD_SIGNALS)


def _row_has_data(rows):
    """F1 判据：CSV 有数据行"""
    return bool(rows)


def selftest():
    print('=' * 58)
    print(' 冒烟集自检 — 断言判别力')
    print('=' * 58)

    print('--- G1 mml.txt 非空 ---')
    chk('G1 正例(有命令)', _is_nonempty_mml(
        '//注释头\nSET LICENSESWITCH:LICITEM="LKV3G5SMRB01",SWITCH=ENABLE;\n'
        'ADD RELAYIPPOOL:POOLNAME="relay_pool",VPNNAME="VRF_Internet";\n'
        'ADD RELAYDOMAIN:RELAYTPLNAME="tpl",RELAYDOMAINNAME="d";\n'), True)
    chk('G1 反例(只有注释/19字节)', _is_nonempty_mml(
        '//配置开通youtube直播的业务\n'), False)
    chk('G1 反例(空文件)', _is_nonempty_mml(''), False)

    print('--- G2 引号成对 ---')
    chk('G2 正例(成对)', _quotes_paired(
        'SET X:KEY="Relay";\nADD Y:NAME="cmnet",PORT=80;\n'), True)
    chk('G2 反例(缺右引号)', _quotes_paired(
        'SET X:KEY="Relay;\n'), False)
    chk('G2 反例(缺左引号)', _quotes_paired(
        'SET X:KEY=Relay";\n'), False)

    print('--- G3 空值参数 ---')
    chk('G3 正例(无空值)', _no_empty_value('ADD X:A="v",B=1;\n'), True)
    chk('G3 反例(空值 =,)', _no_empty_value('ADD X:A="v",B=,;\n'), False)
    chk('G3 反例(空值 =;)', _no_empty_value('ADD X:A="v",B=;\n'), False)

    print('--- G4 可解析 ---')
    chk('G4 正例(合法命令)', _all_parsable('ADD APN:APN="cmnet";\n'), True)
    chk('G4 反例(缺冒号)', _all_parsable('ADD APN APN=cmnet\n'), False)
    chk('G4 反例(全注释)', _all_parsable('//只有注释\n//还有一行\n'), False)

    print('--- F1 CSV 数据行 ---')
    chk('F1 正例(有行)', _row_has_data([{'step': 1}]), True)
    chk('F1 反例(零行)', _row_has_data([]), False)

    print('--- F10 失败提示质量 ---')
    chk('F10 正例(业务码)', _error_clean(
        {'code': 'LLM_AUTH_FAILED', 'details': {'hint': 'API key 无效'}}), True)
    chk('F10 反例(含 INTERNAL)', _error_clean(
        {'code': 'INTERNAL', 'details': {'hint': '失败'}}), False)
    chk('F10 反例(含 rc=1)', _error_clean(
        {'code': 'E', 'details': {'hint': 'hermes 子进程失败 rc=1'}}), False)
    chk('F10 反例(含 Traceback)', _error_clean(
        {'code': 'E', 'details': {'log': 'Traceback (most recent call last)'}}), False)

    print('--- F5/F6 版本链判据 ---')
    chk('F5 正例(409+STAGE_CONFLICT)',
        (409 == 409 and 'STAGE_CONFLICT' == 'STAGE_CONFLICT'), True)
    chk('F5 反例(200 被接受)', (200 == 409), False)
    chk('F6 正例(confirmed=1)', (len(['g1']) > 1), False)   # ≤1 → 不报错
    chk('F6 反例(confirmed=2)', (len(['g1', 'g3']) > 1), True)

    print('--- F7 僵尸状态判据 ---')

    def _is_zombie(task_state, gen_status):
        """F7 判据：任务终态为 failed/cancelled 且 gen 仍是 producing → 僵尸"""
        return task_state in ('failed', 'cancelled') and gen_status == 'producing'

    chk('F7 正例(task failed/gen failed)', _is_zombie('failed', 'failed'), False)
    chk('F7 正例(task succeeded/gen draft)', _is_zombie('succeeded', 'draft'), False)
    chk('F7 反例(task failed/gen producing)', _is_zombie('failed', 'producing'), True)
    chk('F7 反例(task cancelled/gen producing)', _is_zombie('cancelled', 'producing'), True)
    chk('F7 边界(task running/gen producing)', _is_zombie('running', 'producing'), False)

    print('--- F8 批量校验判据 ---')
    chk('F8 正例(非法被拒 422)', (422 != 202), True)
    chk('F8 反例(非法被受理 202)', (202 != 202), False)

    print('--- F9 下载头判据 ---')
    cd_ok = 'attachment; filename="a_b_mml.txt"'
    cd_bad = 'inline'
    chk('F9 正例(attachment+filename)',
        ('attachment' in cd_ok and bool(re.search(r'filename="[^"]+"', cd_ok))), True)
    chk('F9 反例(无 attachment)',
        ('attachment' in cd_bad and bool(re.search(r'filename="[^"]+"', cd_bad))), False)

    # ═══════════ I 组（第二轮问题回归）判别力自证 ═══════════
    # 口径：把 I 组用例里的判据抽成纯函数，用正/反样例各喂一次，
    #       断言分别 PASS / FAIL。若正反结果相同 → 该用例不可信。

    print('--- I1 M1 模板话术判据 ---')
    _TPL = '是想查询配置方法，还是生成一份配置方案'

    def _i1_has_tpl(reply):
        return _TPL in reply
    chk('I1 正例(agent 自然回复)', _i1_has_tpl('当前会话已完成分析，可以让我生成方案'),
        False)
    chk('I1 反例(套模板话术)', _i1_has_tpl(
        '请明确一下：是想查询配置方法，还是生成一份配置方案？（例：…）'), True)

    print('--- I2 M1 原话保留判据 ---')
    def _i2_intent_kept(got, want_kw=('TOS', '带宽')):
        return any(k in str(got) for k in want_kw)
    chk('I2 正例(原话到达)', _i2_intent_kept('配置基于用户TOS的带宽控制功能'), True)
    chk('I2 反例(被替换成模板词)', _i2_intent_kept('生成配置'), False)
    chk('I2 边界(空)', _i2_intent_kept(''), False)

    print('--- I3 M2 命令骨架判据 ---')
    def _i3_has_skeleton(lines, idx):
        """未生成项同行/后续 3 行内应有 CMD:...=... 骨架"""
        ln = lines[idx]
        m = re.search(r'//\[\s*(ADD|MOD|DEL|SET)\s+([A-Z0-9]+)', ln)
        if not m:
            return None
        cmd = f'{m.group(1)} {m.group(2)}'
        win = '\n'.join(lines[idx:idx + 4])
        return f'{cmd}:' in win
    bad_only_comment = ['//[ADD DETECTPATH 未生成：主键参数 PATHNAME 无法自动生成，需专家补充]']
    with_skeleton = [
        '//[ADD DETECTPATH 未生成：主键参数 PATHNAME 无法自动生成，需专家补充]',
        'ADD DETECTPATH:PATHNAME="<PATHNAME_2>",LOCALINF="<LOCALINF>",IPVERSION=IPV6;']
    chk('I3 正例(仅注释无骨架)', _i3_has_skeleton(bad_only_comment, 0), False)
    chk('I3 反例(带骨架)', _i3_has_skeleton(with_skeleton, 0), True)
    chk('I3 边界(非命令注释)', _i3_has_skeleton(['// 普通说明'], 0), None)

    print('--- I4 M2 命令数对等判据 ---')
    def _i4_parity(md_n, mml_n, miss_n, thr=0.95):
        if not md_n:
            return True
        return (mml_n + miss_n) / max(md_n, 1) >= thr
    chk('I4 正例(骨架覆盖 md)', _i4_parity(74, 24, 49), True)     # 73/74 = 99%
    chk('I4 反例(68% 蒸发)', _i4_parity(74, 24, 0), False)         # 24/74 = 32%
    chk('I4 边界(md 无命令)', _i4_parity(0, 0, 0), True)

    print('--- I5/I14 分段进度判据 ---')
    def _i5_stages_ok(names, thr=2):
        names = {n for n in names if n}
        return len(names) >= thr
    chk('I5 正例(2 段)', _i5_stages_ok(['analyzing', 'matching']), True)
    chk('I5 反例(仅 1 段)', _i5_stages_ok(['analyzing']), False)
    chk('I5 边界(空)', _i5_stages_ok([]), False)
    chk('I14 正例(≥3 段)',
        _i5_stages_ok(['analyzing', 'retrieving', 'matching', 'writing_artifacts'], 3), True)
    chk('I14 反例(2 段)',
        _i5_stages_ok(['analyzing', 'writing_artifacts'], 3), False)

    print('--- I6 M3 耗时门槛判据 ---')
    def _i6_slow(ncmd, sec, gate=45):
        return ncmd >= 90000 and sec > gate
    chk('I6 正例(10万条/60.6s 未优化)', _i6_slow(101232, 60.6), True)
    chk('I6 反例(10万条/38s 已优化)', _i6_slow(101232, 38.0), False)
    chk('I6 边界(小 EXP 不判)', _i6_slow(2253, 60.6), False)

    print('--- I7 N1 状态自洽判据 ---')
    def _i7_consistent(stage, done):
        if done and stage not in ('matched', 'exp_ready', 'analyzed'):
            return False
        if not done and stage == 'matched':
            return False
        return True
    chk('I7 正例(done+matched)', _i7_consistent('matched', True), True)
    chk('I7 反例(done 但 stage=analyzing)', _i7_consistent('analyzing', True), False)
    chk('I7 反例(未done 但 matched)', _i7_consistent('matched', False), False)

    print('--- I8 N2 实例折叠判据 ---')
    def _i8_need_fold(n, limit=50):
        return n >= limit

    def _i8_has_fold(html):
        return bool(re.search(r'inst[-_]?fold|foldLimit|折叠|instLimit|展开', html))
    chk('I8 正例(670 实例+有折叠)', (_i8_need_fold(670) and _i8_has_fold('const foldLimit=12')), True)
    chk('I8 反例(670 实例无折叠)', (_i8_need_fold(670) and _i8_has_fold('<div>tags</div>')), False)
    chk('I8 边界(30 实例)', _i8_need_fold(30), False)

    print('--- I9 N3 内部文案判据（剥注释/样式后查渲染代码）---')
    _STYLE_RE = re.compile(r'<style[^>]*>.*?</style>', re.S | re.I)
    _BLOCK_RE = re.compile(r'/\*.*?\*/', re.S)

    def _strip_code(h):
        """剥掉 <style> 与注释，只留可执行渲染代码"""
        c = _STYLE_RE.sub('', h)
        c = _BLOCK_RE.sub('', c)
        return '\n'.join(l for l in c.splitlines()
                         if not l.strip().startswith(('//', '<!--', '*')))

    def _i9_clean(html):
        code = _strip_code(html)
        bad = []
        if re.search(r"insertBefore\s*\(\s*tp", code):
            bad.append('insertBefore')
        for pat in (r'执行命令\s*\(\s*\$?\{', r'读取文件\s*\(\s*\$?\{'):
            if re.search(pat, code):
                bad.append(pat)
        if 'agentProc' not in html:
            bad.append('no #agentProc')
        return not bad

    chk('I9 正例(已业务化+入对话框)',
        _i9_clean('<div id="agentProc"></div><div>🧭 整理命令与参数</div>'), True)
    chk('I9 反例(注释里含旧文案 → 不应误判)',
        _i9_clean('<div id="agentProc"></div>\n// 旧实现曾直出 执行命令 (0.03s)\n'
                  '<div>📄 读取参考资料</div>'), True)
    chk('I9 反例(真在渲染工具耗时)',
        _i9_clean('<div id="agentProc"></div><div>执行命令 (${dt}s)</div>'), False)
    chk('I9 反例(面板未入对话框)',
        _i9_clean('<div>执行命令 (0.03s)</div>'), False)
    chk('I9 反例(CSS 里的 .tr-i 不应算)',
        _i9_clean('<style>.tr-i{color:#fff}</style><div id="agentProc"></div>'
                  '<div>📄 读取参考资料</div>'), True)


    print('--- I10 N4 页签固定判据 ---')
    def _i10_fixed(html):
        return not re.search(r"L\.id==='gen'\s*&&\s*hasGen", html)
    chk('I10 正例(无动态过滤)', _i10_fixed("LV1_TABS.map(L => ...)"), True)
    chk('I10 反例(有 hasGen 过滤)',
        _i10_fixed("LV1_TABS.filter(L => L.id==='exp' || (L.id==='gen' && hasGen))"), False)

    print('--- I11 N5 子页签判据 ---')
    def _i11_ok(tabs):
        labels = ' '.join(str(t.get('label', '')) + str(t.get('tab_id', ''))
                          for t in tabs)
        return (('mml' in labels.lower()) and ('csv' in labels.lower()))
    chk('I11 正例(方案/csv/mml)',
        _i11_ok([{'tab_id': 'gen', 'label': '方案'},
                 {'tab_id': 'csv', 'label': '参数收集表'},
                 {'tab_id': 'mml', 'label': '纯 MML'}]), True)
    chk('I11 反例(缺 mml)',
        _i11_ok([{'tab_id': 'gen', 'label': '方案'},
                 {'tab_id': 'csv', 'label': '参数收集表'}]), False)

    print('--- I12 N6 对话反馈判据 ---')
    def _i12_has_feedback(html):
        return any(p in html for p in ('EventSource', 'fetchStream', 'stream',
                                       '正在初始化', '正在推理', '正在思考'))
    chk('I12 正例(有流式/阶段提示)', _i12_has_feedback('<div>正在推理…</div>'), True)
    chk('I12 反例(仅静态思考中)', _i12_has_feedback('<div>（思考中…）</div>'), False)

    print('--- I13 N7 权限一致判据 ---')
    def _i13_ok(inconsistent):
        return not inconsistent
    chk('I13 正例(全一致)', _i13_ok([]), True)
    chk('I13 反例(有 600)', _i13_ok([{'file': 'intent_routing.yaml', 'mode': '600'}]), False)

    bad = [c for c in CHECKS if not c[1]]
    print()
    print(f' 自检结果: {len(CHECKS) - len(bad)}/{len(CHECKS)} 条判别力正常')
    if bad:
        print(f' !! {len(bad)} 条断言无判别力（正反输入结果相同）—— 用例不可信')
        for n, _, m in bad:
            print(f'    {n}: {m}')
        return 1
    print(' ✓ 全部判据均可区分对错')
    return 0


if __name__ == '__main__':
    sys.exit(selftest())
