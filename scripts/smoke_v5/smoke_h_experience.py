#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_h_experience.py — H 组冒烟：体验与入口（容器内执行）

覆盖原冒烟集完全缺失的"体验"维度（见 原冒烟集问题反查.md 第四节）：
  H1  对话通道可达且回复合理（问题#5/#7 的基础）
  H2  对话回复无安装噪音（问题#10）
  H3  失败提示不含内部信号（问题#4/#9，UI 侧同源）
  H4  无冗余不可用入口（问题#1）
  H5  生成过程记录不含内部计数外露（问题#2）
  H6  任务终态 UI 语义（问题#3：不得停留"生成中"）
  H7  上下文拼装与实际会话一致（T1 附带发现）

说明：本组为**接口/静态**判据（无需浏览器）。
浏览器端交互见 ui_click_smoke.js（另有配套增强）。

用法:
    python3 smoke_h_experience.py --sid <session_id>
"""
import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

RESULTS = []
BASE = 'http://localhost:8600'
SID = ''
BACKEND = Path('/opt/expgv/backend')
WEB = BACKEND / 'web' / 'app_v2.html'

# 本进程启动时刻（H3/F10 分界：只审这之后产生的失败）
_PROC_START_ISO = __import__("datetime").datetime.utcnow()\
    .strftime("%Y-%m-%dT%H:%M:%SZ")

BAD_SIGNALS = ('INTERNAL', 'rc=1', 'Traceback', 'subprocess',
               'returncode', 'HTTPException')
INSTALL_NOISE = ('Detected: linux', 'Checking Node.js', 'Downloading node-',
                 'Extracting to ~/.hermes/node', 'installing Node.js',
                 'Ignoring inherited PYTHONPATH')


def api(path, method='GET', body=None, timeout=300, use_v1=True):
    """use_v1=False 时直连 /api/<path>（对话接口在 /api/chat，非 /api/v1）"""
    url = f'{BASE}/api/v1{path}' if use_v1 else f'{BASE}/api{path}'
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.loads(r.read() or b'{}')
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b'{}')
        except Exception:
            return e.code, {}
    except Exception as e:
        return -1, {'exception': f'{type(e).__name__}: {e}'}


def chat(question, timeout=660):
    """★ 超时必须 > 后端 hermes 子进程超时（app.py 里 subprocess timeout=600）。

    ⚠ 实测（2026-09-18）：H1 报 FAIL「420s 超时」，真因不是对话坏了 ——
    冷启动对话（首跑依赖就位 + 真 LLM）实测 400~600s，用例侧 420s 先到 ⇒ 假红。
    ⇒ 用例超时要留出后端超时 + 余量，否则测的是「用例耐心」不是「产品能力」。
    """
    """对话通道（/api/chat，非 v1 前缀）"""
    return api('/chat', 'POST', {'case': SID, 'question': question},
               timeout=timeout, use_v1=False)


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


# ─────────── H1 对话通道 ───────────

def h1_chat():
    """对话通道必须可达且回复合理"""
    st, r = chat('你好')
    if st == 404:
        return False, '对话接口不存在（/api/chat）—— 前端无法支持基础对话'
    if st != 200:
        return False, f'HTTP {st}: {json.dumps(r, ensure_ascii=False)[:200]}'
    reply = (r.get('reply') or '')
    if len(reply.strip()) < 2:
        return False, f'回复过短/为空: {reply[:80]!r}'
    return True, f'{len(reply)} 字符，样例: {reply[:70]}'


# ─────────── H2 无安装噪音 ───────────

def h2_no_install_noise():
    st, r = chat('你好')
    reply = (r.get('reply') or '')
    hits = [s for s in INSTALL_NOISE if s in reply]
    if hits:
        return False, ('回复混入首跑安装日志（内部噪音外露）: '
                       + '; '.join(hits[:3]))
    if '\x1b[' in reply:
        return False, '回复含 ANSI 转义码（未剥离终端控制字符）'
    return True, '无安装噪音、无 ANSI 残留'


# ─────────── H3 失败提示不含内部信号 ───────────

def h3_error_ui_signal():
    """失败提示不得含内部信号（UI 会直显）。

    ★ 2026-09-18 修（与 F10 同源口径）：必须限定「**本次运行期**产生的失败」。
      历史失败记录（修复前旧代码跑出的）会永久留在 tasks 里，
      拿它判当前实现 = 永远 FAIL 且掩盖真实回归。
      分界时刻：env SMOKE_SINCE 优先，否则取本进程启动时刻。
    """
    import os as _os
    st, r = api('/tasks?limit=50')
    tasks = r.get('items') or []
    since = _os.environ.get('SMOKE_SINCE') or _PROC_START_ISO

    all_failed = [t for t in tasks if t.get('state') in ('failed', 'cancelled')]
    recent = [t for t in all_failed if (t.get('created_at') or '') >= since]
    stale = len(all_failed) - len(recent)

    bad = []
    for t in recent:
        blob = json.dumps(t.get('error') or {}, ensure_ascii=False)
        hits = [s for s in BAD_SIGNALS if s in blob]
        if hits:
            bad.append(f"{t.get('id')}: {hits}")
    note = f'（另有 {stale} 条历史失败已忽略）' if stale else ''
    if bad:
        return False, ('失败提示含内部信号（UI 会直显）:\n'
                       + '\n'.join(bad[:3]) + '\n' + note)
    return True, f'本次运行期 {len(recent)} 个失败任务，提示均无内部信号{note}'


# ─────────── H4 无冗余不可用入口 ───────────

def h4_no_dead_entry():
    """「生成结果验证(groundtruth对照)」入口 —— 来源在 rules/session_stages.yaml（非前端）"""
    # 入口定义在规则文件里（guide 渲染），前端不含该字样（实测确认）
    cands = [Path('/opt/expgv/rules/session_stages.yaml'),
             Path('/opt/expgv/rules') / 'session_stages.yaml']
    rule = next((p for p in cands if p.is_file()), None)
    if rule is None:
        rule = next(Path('/opt/expgv/rules').rglob('session_stages.yaml'), None)
    if rule is None:
        return False, '未找到 rules/session_stages.yaml（无法判定）'
    txt = rule.read_text(encoding='utf-8', errors='replace')
    # ⚠ 判据必须排除**注释行**：入口修掉后原位会留「已移除」说明注释，
    #   注释里含同样字样 ⇒ 不排除会误报 FAIL（实测踩到）。
    live_txt = '\n'.join(ln for ln in txt.splitlines()
                         if not ln.lstrip().startswith('#'))
    if 'run_verification' in live_txt or '生成结果验证' in live_txt:
        return False, (f'{rule.name} 仍登记「生成结果验证（groundtruth 对照）」入口 —— '
                       '与判定卡「官方基线」概念重复（问题#1，待修）')
    return True, '规则文件中无冗余验证入口（注释中的历史说明已排除）'


# ─────────── H5 无内部计数外露 ───────────

def h5_no_internal_counter():
    """生成过程记录不得直接展示 LLM 调用计数（来源在后端 generations_v1.py）"""
    cands = [Path('/opt/expgv/backend/generations_v1.py'),
             Path('/opt/expgv/backend') / 'generations_v1.py']
    src = next((p for p in cands if p.is_file()), None)
    if src is None:
        src = next(Path('/opt/expgv/backend').rglob('generations_v1.py'), None)
    if src is None:
        return False, '未找到 generations_v1.py（无法判定）'
    txt = src.read_text(encoding='utf-8', errors='replace')
    # 判据：是否把 API call #N 渲染成用户可见文案
    if re.search(r'API call\s*#', txt) and '正在分析与生成（第' in txt:
        return False, ('后端把 LLM 调用计数渲染为「正在分析与生成（第 N 步）」'
                       ' —— 内部计数外露（问题#2，待修）')
    return True, '未见 LLM 调用计数外露'


# ─────────── H6 任务终态 UI 语义 ───────────

def h6_terminal_ui():
    """完成后不得停留'生成中'（检查前端是否用统一判定）"""
    if not WEB.is_file():
        return False, f'前端文件缺失 {WEB}'
    txt = WEB.read_text(encoding='utf-8', errors='replace')
    # 完成通知与自动切页签的判据
    # ★ 2026-09-18 更新：页签组织重构后 `setLv1` 已删除（层级取消，7 页签平铺），
    #   切页签改走 `pickTab`。旧判据查 setLv1 属**判据过期**，不是功能回归。
    has_done_notice = ('方案已生成' in txt) or ('生成完成' in txt)
    has_switch = ('pickTab(' in txt) or ('setLv1(' in txt)
    if not has_done_notice:
        return False, '前端无「完成通知」文案（done 分支未设置完成消息）—— 问题#3'
    if not has_switch:
        return False, '前端无页签切换调用（pickTab / setLv1）'
    # 反向断言：层级已被取消，旧的三级切换函数不应再存在（防退回旧结构）
    if 'function setLv1' in txt:
        return False, '仍存在 setLv1（页签层级应已取消，7 页签平铺）'
    return True, '存在完成通知 + 页签切换（pickTab，已平铺）'


# ─────────── H7 上下文一致 ───────────

def h7_context():
    """对话上下文应认识当前会话（不得称'数据集为空'而实际有 exp）"""
    st, r = chat('这个会话有哪些文件？')
    reply = (r.get('reply') or '')
    # 会话实际有 exp → 断言回复不应声称"无 exp/数据集为空"
    sess_root = Path('/data/sessions') / SID
    has_exp = any((sess_root / d).is_dir() and any((sess_root / d).iterdir())
                  for d in ('exp_v1', 'exp') if (sess_root / d).is_dir())
    if has_exp and re.search(r'数据集.{0,4}为空|无 exp|没有 exp', reply):
        return False, f'上下文与实际不符（会话有 exp 但回复称无）: {reply[:120]}'
    return True, f'上下文一致（has_exp={has_exp}）'


SID = ''

def h8_intent_routing():
    """M1（2026-09-18 用户裁决）：对话全开放给 agent，**不再有规则分类**。

    ★ 判据已按新设计重写。旧判据查的是一套**已被裁决删除**的实现
      （classify_intent / INTENT_CHAT_REQUIRED / intent_routing.yaml /
       前端 classifyIntent），拿它判新设计必然 FAIL —— 属判据过期，
      不是产品回归。

    新设计的正确判据（反向断言：旧机制必须**不在**；新机制必须**在**）：
      ① 后端：不得再有入口意图守卫（classify_intent 若保留须标记废弃）
      ② 前端：不得再有 classifyIntent（关键词规则分类）
      ③ 前端：不得再有二次确认（doAgentConfirm / pendingGen）
      ④ 原话必须**直传** agent（intent_text 不再被替换）
      ⑤ 对话通道 /api/chat 仍在（聊天能力不丢）
    """
    # ── ① 后端：旧守卫必须移除 ──
    gen_src = BACKEND / 'generations_v1.py'
    if not gen_src.is_file():
        return False, f'缺文件 {gen_src}'
    t = gen_src.read_text(encoding='utf-8', errors='replace')
    if 'raise_biz(\'INTENT_CHAT_REQUIRED\'' in t:
        return False, '后端仍抛 INTENT_CHAT_REQUIRED（旧入口守卫未删）'
    # classify_intent 允许作为废弃函数保留，但不得被生产路径调用
    for i, l in enumerate(t.splitlines()):
        if 'classify_intent(' in l and not l.strip().startswith(('#', '"')):
            if '_cls = classify_intent' in l or '= classify_intent' in l:
                return False, f'后端生产路径仍调用 classify_intent（line {i+1}）'

    # ── ② 前端：关键词规则分类必须移除 ──
    if not WEB.is_file():
        return False, f'缺文件 {WEB}'
    wt = WEB.read_text(encoding='utf-8', errors='replace')
    wcode = '\n'.join(l for l in wt.splitlines()
                      if not l.strip().startswith(('//', '*')))
    if 'function classifyIntent' in wcode:
        return False, '前端仍有 classifyIntent（关键词规则分类未删）'
    # ── ③ 前端：二次确认必须移除 ──
    if 'function doAgentConfirm' in wcode:
        return False, '前端仍有 doAgentConfirm（二次确认未删）'
    if 'a.pendingGen' in wcode or 'S.agent.pendingGen' in wcode:
        return False, '前端仍用 pendingGen（原话被中转，有丢失风险）'
    # ── ④ 对话通道仍在 ──
    if '/chat' not in wcode:
        return False, '前端未接对话通道 /api/chat'
    # ── ⑤ 原话直传：send 处 intent_text 来自输入框原文 ──
    if 'intent_text: intent' not in wcode and 'intent_text:intent' not in wcode:
        return False, '未发现 intent_text 直传（原话可能仍被替换）'
    return True, '意图直通就位（去规则分类 + 去二次确认 + 对话通道在）'



def h9_agent_contract():
    """P1-5：agent 契约化与减负（skills 列全 + md 契约 + 不再逼双文件）"""
    gen_src = (BACKEND / 'generations_v1.py')
    if not gen_src.is_file():
        return False, f'缺文件 {gen_src}'
    t = gen_src.read_text(encoding='utf-8', errors='replace')
    # ① skills 显式列全（问题#7：子 skill 加载 0 次）
    need = ['mml_assistant', 'mml_feature', 'mml_support',
            'mml_nav', 'mml-config-guide', 'command-context-resolver']
    # ⚠ --skills 的值在源码里是**跨行 Python 字符串拼接**：
    #     '--skills', 'mml_assistant,mml_feature,...'
    #                 'mml-config-guide,...',
    #   旧正则 [^\]]+?\] 匹配不到 ⇒ 假 FAIL。改为按 '--toolsets' 边界取，
    #   再把其中所有单引号字面量拼起来（等价于 Python 的隐式拼接）。
    _m = re.search(r"'--skills',(.*?)'--toolsets'", t, re.S)
    _raw = _m.group(1) if _m else ''
    skills_arg = ''.join(re.findall(r"'([^']*)'", _raw))
    miss = [s for s in need if s not in skills_arg]
    if miss:
        return False, f'--skills 未列全，缺 {miss}（问题#7 未修）'
    # ② 任务书契约化（md 为必须、mml 块要求、csv 降为可选）
    tpl = BACKEND / 'templates' / 'agent_task_prompt.md'
    if not tpl.is_file():
        return False, f'缺任务书模板 {tpl}'
    tt = tpl.read_text(encoding='utf-8', errors='replace')
    if '```mml' not in tt:
        return False, '任务书未要求 mml 代码块（md 直提无法生效）'
    if '【可选】' not in tt:
        return False, '任务书未把 csv 降为可选（仍在逼双文件）'
    return True, 'agent 契约就位（6 skill 列全 + md/mml 块契约 + csv 可选）'


CASES = [
    ('H1', '对话通道可达且回复合理', h1_chat),
    ('H2', '对话回复无安装噪音/ANSI', h2_no_install_noise),
    ('H3', '失败提示不含内部信号', h3_error_ui_signal),
    ('H4', '无冗余不可用入口', h4_no_dead_entry),
    ('H5', '生成过程无内部计数外露', h5_no_internal_counter),
    ('H6', '任务终态 UI 语义', h6_terminal_ui),
    ('H7', '上下文拼装与会话一致', h7_context),
    ('H8', '意图分流（寒暄不建任务）', h8_intent_routing),
    ('H9', 'agent 契约与减负', h9_agent_contract),
]


def main():
    global BASE, SID
    ap = argparse.ArgumentParser(description='H 组冒烟：体验与入口')
    ap.add_argument('--base', default='http://localhost:8600')
    ap.add_argument('--sid', required=True)
    ap.add_argument('--json', default='')
    ap.add_argument('--only', default='')
    args = ap.parse_args()

    BASE = args.base.rstrip('/')
    SID = args.sid
    only = {x.strip().upper() for x in args.only.split(',') if x.strip()}

    print('=' * 58)
    print(f' H 组冒烟（体验与入口）sid={SID}')
    print('=' * 58)

    for cid, name, fn in CASES:
        if only and cid not in only:
            continue
        case(cid, name, fn)

    total = len(RESULTS)
    passed = sum(1 for r in RESULTS if r['ok'])
    print('\n' + '=' * 58)
    print(f' H 组汇总: {passed}/{total} 通过')
    for r in [x for x in RESULTS if not x['ok']]:
        print(f'   {r["id"]} {r["name"]}: {r["msg"][:140]}')
    print('=' * 58)

    if args.json:
        Path(args.json).write_text(json.dumps(
            {'group': 'H', 'total': total, 'passed': passed, 'results': RESULTS},
            ensure_ascii=False, indent=2))
        print(f'结果已落盘: {args.json}')
    return 0 if not [x for x in RESULTS if not x['ok']] else 1


if __name__ == '__main__':
    sys.exit(main())
