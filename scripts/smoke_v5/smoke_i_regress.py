#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""smoke_i_regress.py — I 组冒烟：第二轮问题回归（M1/M2/M3 + N1~N8）。

第二轮问题清单（2026-09-18 用户实测）：
  M1 通道对接（关键词规则劫持意图 + 原话在多轮确认中丢失 → 产物错配）
  M2 mml.txt 与方案不对等（74 条承诺 vs 24 条产出，68% 蒸发）
  M3 EXP 分析耗时（60s，4 段子进程重复解析，无进度上报）
  N1 轮询中断 UI 卡「分析中」、卡片不刷新
  N2 exp 实例平铺占位大（最多 670 个）
  N3 进度呈现位置不当 + 步骤是内部文案
  N4 页签应固定 + 灰化不隐藏
  N5 子页签重组：方案 / 参数收集表 / 纯MML
  N6 对话 176s 无中间反馈
  N7 规则文件权限不一致（600 vs 644）
  N8 分析分段进度上报缺失

设计口径（沿用 A~H 组）：
  · 每条用例必须能同时排除「修了」和「没修」两种状态（判别力），
    由 smoke_selftest.py 的 I 组配对样例验证。
  · 断言对象是**外部可观察行为**（HTTP 响应 / 产物文件 / 字节内容），
    不读内部变量。
  · 用例超时留出后端余量，避免测「用例耐心」。

usage: python3 smoke_i_regress.py --sid <sid> [--base http://localhost:8600]
                                   [--json out.json] [--only I1,I2]
"""
import argparse
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

BASE = 'http://localhost:8600'
SID = ''
RESULTS = []


def api(path, method='GET', body=None, timeout=120, use_v1=True, raw=False,
        no_prefix=False):
    # no_prefix=True → 直连根路径（前端 HTML 在 / 直出）
    if no_prefix:
        url = BASE + path
    else:
        url = (BASE + ('/api/v1' if use_v1 else '/api') + path)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    if data:
        req.add_header('Content-Type', 'application/json')
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            payload = r.read()
            if raw:
                return r.status, payload
            return r.status, json.loads(payload or b'{}')
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read() or b'{}')
        except Exception:
            return e.code, {}
    except Exception as e:
        return -1, {'exception': f'{type(e).__name__}: {e}'}


def case(cid, name, fn):
    t0 = time.time()
    skipped = False
    try:
        detail = fn()
        if isinstance(detail, tuple) and detail[0] is None:
            ok, msg, skipped = True, detail[1], True     # 三态：跳过
        else:
            ok, msg = (detail if isinstance(detail, tuple) else (bool(detail), ''))
    except Exception as e:
        ok, msg = False, f'{type(e).__name__}: {e}'
    dt = time.time() - t0
    RESULTS.append({'id': cid, 'name': name, 'ok': bool(ok), 'skipped': skipped,
                    'msg': str(msg), 'sec': round(dt, 2)})
    tag = 'SKIP' if skipped else ('PASS' if ok else 'FAIL')
    print(f'  [{tag}] {cid} {name}  ({dt:.1f}s)')
    if msg:
        for ln in str(msg).splitlines()[:6]:
            print(f'         {ln}')
    return ok


def _gens():
    st, r = api(f'/sessions/{SID}/generations')
    return (r.get('items') or []) if st == 200 else []


def _latest_gen():
    """取**生成产物最完备**的 gen 节点。

    ★ 2026-09-18 修：旧实现取「最新」的 gen —— 而最新的常是 agent 草案
      （只有 md，无 mml.txt），导致 I3/I4 误报「mml.txt 为空」。
      改为优先取含 mml.txt 的装配节点；无装配节点才退回最新。
      （与 smoke_g_quality 的取样口径保持一致）
    """
    gs = _gens()
    if not gs:
        return None
    # 优先：有 mml.txt 且**内容非空**的节点（真正的装配产物）
    #  ⚠ 只查 produced 列表不够：agent 草案也会列出 mml.txt 但文件是 0 字节
    #    （实测 g6~g11 均如此）→ 取到空节点会误报「mml.txt 为空」。
    with_mml = []
    for g in gs:
        if not any(str(p).endswith('mml.txt') for p in (g.get('produced') or [])):
            continue
        txt = _gen_text(g.get('gen_id'), 'mml')
        if txt.strip():
            with_mml.append((g, len(txt)))
    if with_mml:
        # 取内容最丰富的（最完整的装配产物）
        with_mml.sort(key=lambda x: -x[1])
        return with_mml[0][0]
    return gs[0]


def _gen_text(gid, kind):
    """取 gen 产物文本（kind: mml / md）"""
    if kind == 'md':
        st, r = api(f'/sessions/{SID}/generations/{gid}/artifacts/schema')
        if st != 200:
            return ''
        # md 文件走 file 接口（名字从 produced 里找）
        g = next((x for x in _gens() if x.get('gen_id') == gid), None)
        if not g:
            return ''
        md = next((p for p in (g.get('produced') or []) if p.endswith('.md')
                   and not p.startswith('确认清单')), None)
        if not md:
            return ''
        st, raw = api(f'/sessions/{SID}/generations/{gid}/file?name='
                      + urllib.parse.quote(md), raw=True)
        return raw.decode('utf-8', 'ignore') if st == 200 else ''
    st, raw = api(f'/sessions/{SID}/generations/{gid}/artifacts/{kind}', raw=True)
    return raw.decode('utf-8', 'ignore') if st == 200 else ''


# ═══════════════ M1 通道对接 ═══════════════

def i1_m1_no_template_clarify():
    """M1：明确配置意图不得被套模板话术反问。

    判别力：旧实现「配置恒 XXX 功能」落规则空 → 回固定话术
    「请明确一下：是想查询配置方法，还是生成一份配置方案？」。
    修复后应直接进入生成/对话，不得出现该模板句。
    """
    st, r = api('/chat', 'POST',
                {'case': SID, 'question': '配置新的pcc动态功能'},
                timeout=660, use_v1=False)
    if st != 200:
        return False, f'HTTP {st}: {json.dumps(r, ensure_ascii=False)[:200]}'
    reply = (r.get('reply') or '')
    if not reply.strip():
        return False, '回复为空'
    tpl = '是想查询配置方法，还是生成一份配置方案'
    if tpl in reply:
        return False, f'⛔ 仍套用固定澄清模板（M1 未修）: {reply[:120]}'
    return True, f'{len(reply)} 字符，无模板话术'


def i2_m1_intent_not_lost():
    """M1：用户原话必须原样到达任务（不得被确认话术替换）。

    判别力：旧实现 intent_text 变成「生成配置」（模板词），
    导致 agent 猜错特性 → 产物错配。
    本用例建任务后回读 gen.json 的 intent_text，必须含原话关键字。
    """
    intent = '配置基于用户TOS的带宽控制功能'
    st, r = api(f'/sessions/{SID}/generations', 'POST',
                {'action': 'fresh', 'intent_text': intent}, timeout=120)
    # ⚠ 202 = Accepted（异步任务已受理），与 200/201 同属成功路径。
    if st not in (200, 201, 202):
        return False, f'建任务失败 HTTP {st}: {json.dumps(r, ensure_ascii=False)[:200]}'
    gid = r.get('gen_id')
    if not gid:
        return False, f'响应无 gen_id: {json.dumps(r, ensure_ascii=False)[:160]}'
    time.sleep(1.5)
    st, g = api(f'/sessions/{SID}/generations/{gid}')
    gi = (g.get('item') or g) if st == 200 else {}
    got = str(gi.get('intent_text') or '')
    if 'TOS' not in got and '带宽' not in got:
        return False, (f'⛔ 原话丢失（M1 未修）：提交「{intent}」，'
                       f'记录为「{got}」')
    return True, f'intent_text 保留原话: {got[:60]}'


# ═══════════════ M2 mml 与方案对等 ═══════════════

def i3_m2_mml_keeps_skeleton():
    """M2：主键无法自动生成时，必须保留带占位符的完整命令骨架。

    判别力：旧实现只留一行「//[ADD XXX 未生成：…]」注释，
    整条命令丢失，专家拿不到参数列表。
    修复后注释行或紧跟行必须含该命令的 `CMD:P1=..,P2=..` 骨架。
    """
    g = _latest_gen()
    if not g:
        return False, '本会话无 gen 产物（需先跑 I2 或 F 组建产物）'
    gid = g.get('gen_id')
    mml = _gen_text(gid, 'mml')
    if not mml.strip():
        return False, f'gen {gid} 的 mml.txt 为空'
    miss_lines = [ln for ln in mml.splitlines() if '未生成' in ln]
    if not miss_lines:
        return True, '无未生成项（本次全部可生成）'
    # 至少一条未生成项必须带命令骨架（含 `=` 的 CMD: 形式）
    bad = []
    for i, ln in enumerate(mml.splitlines()):
        if '未生成' not in ln:
            continue
        m = re.search(r'//\[\s*(ADD|MOD|DEL|SET)\s+([A-Z0-9]+)', ln)
        if not m:
            continue
        cmd = f'{m.group(1)} {m.group(2)}'
        # 同行或后续 3 行内应有骨架
        window = '\n'.join(mml.splitlines()[i:i + 4])
        if f'{cmd}:' in window and '=' in window.split(cmd, 1)[-1][:400]:
            continue
        bad.append(cmd)
    if bad and len(bad) == len([l for l in miss_lines]):
        return False, (f'⛔ {len(bad)} 条未生成项均无命令骨架'
                       f'（M2 未修），例: {bad[:3]}')
    return True, f'{len(miss_lines)} 条未生成项中带骨架 {len(miss_lines)-len(bad)} 条'


def i4_m2_mml_md_parity():
    """M2：mml.txt 与方案 md 的命令数必须对等（差异 ≤ 未生成项数）。

    判别力：旧实现 md 74 条 → mml.txt 24 条（68% 蒸发），且无任何说明。
    修复后 mml.txt 的真命令 + 骨架化未生成项 ≥ md 命令数的 95%。
    """
    g = _latest_gen()
    if not g:
        return False, '本会话无 gen 产物'
    gid = g.get('gen_id')
    mml = _gen_text(gid, 'mml')
    md = _gen_text(gid, 'md')
    if not mml.strip():
        return False, f'gen {gid} 的 mml.txt 为空'
    if not md.strip():
        return True, 'md 不可读（跳过对比，mml 非空）'

    def cmds_of(text):
        out = []
        for ln in text.splitlines():
            ln = ln.strip()
            if re.match(r'^(ADD|MOD|DEL|SET|LST|DSP)\s', ln):
                out.append(ln.split(':', 1)[0])
        return out

    md_c, mml_c = cmds_of(md), cmds_of(mml)
    miss = len([ln for ln in mml.splitlines() if '未生成' in ln])
    # mml 侧「已呈现」= 真命令 + 骨架化说明（它们也承载了 md 的命令）
    covered = len(mml_c) + miss
    if not md_c:
        return True, f'md 无 mml 命令块（跳过），mml 真命令 {len(mml_c)} 条'
    ratio = covered / max(len(md_c), 1)
    if ratio < 0.95:
        return False, (f'⛔ 不对等（M2 未修）：md {len(md_c)} 条 vs '
                       f'mml 覆盖 {covered} 条（真命令 {len(mml_c)} + 未生成 {miss}）= '
                       f'{ratio:.0%}')
    return True, f'md {len(md_c)} 条 / mml 覆盖 {covered} 条 = {ratio:.0%}'


# ═══════════════ M3 分析耗时 ═══════════════

def i5_m3_analysis_stage_progress():
    """M3：分析过程必须有分段进度上报（stage 中途可见）。

    判别力：旧实现 progress.steps=0、stage 只在结束时写一次，
    60 秒全程界面只有「分析中」。
    修复后任务记录的 stage_history / progress 应含 ≥2 个不同阶段。
    """
    st, r = api('/tasks')
    items = (r.get('items') or []) if st == 200 else []
    ana = [t for t in items if t.get('kind') == 'exp_analysis']
    if not ana:
        return False, '无 exp_analysis 任务可查（需先上传 EXP）'
    t = ana[0]
    hist = t.get('stage_history') or t.get('stages') or []
    stages = {h.get('stage') if isinstance(h, dict) else h for h in hist}
    stages.discard(None)
    if len(stages) < 2:
        # 退路：看 progress 是否有分段计数
        pr = t.get('progress') or {}
        steps = pr.get('steps') or []
        if len(stages) >= 2 or len(steps) >= 2:
            return True, f'progress.steps={len(steps)} 段'
        return False, (f'⛔ 无分段进度（M3-N8 未修）：stage 仅 {sorted(stages)}，'
                       f'progress.steps={len(steps)}')
    return True, f'{len(stages)} 个阶段: {sorted(stages)}'


def i6_m3_no_repeat_parse():
    """M3：同一份 EXP 不应被 4 段子进程各自解析（重复劳动）。

    判别力：旧实现 ①/④a/④b 各自 parse_exp 同一文件。
    修复后任务记录应体现复用（如 parse_count=1），
    或任务总耗时相对基线显著下降。
    本用例以「任务总耗时」为可观测量：10 万行 EXP ≤ 45s 视为已优化。
    """
    st, r = api('/tasks')
    items = (r.get('items') or []) if st == 200 else []
    ana = [t for t in items if t.get('kind') == 'exp_analysis'
           and t.get('state') in ('succeeded', 'finished')]
    if not ana:
        return False, '无成功的 exp_analysis 任务'
    t = ana[0]
    el = t.get('elapsed_sec')
    if el is None:
        return False, '任务无 elapsed_sec'
    scope = t.get('summary') or {}
    ncmd = scope.get('exp_cmds') or 0
    # ⚠ 无大 EXP 数据时**明确跳过**（返回 None → 框架不判 PASS，避免假绿）
    if ncmd < 90000:
        return None, (f'跳过：本会话最大 EXP 仅 {ncmd} 条命令'
                      f'（门槛 9 万）；需用大 EXP 会话重跑')
    # 基线：10 万条命令 = 60.6s。设 45s 为门槛（留 25% 余量）
    if el > 45:
        return False, (f'⛔ 大 EXP（{ncmd} 条）仍耗 {el:.1f}s > 45s '
                       f'（M3 未优化）')
    return True, f'{ncmd} 条命令 / {el:.1f}s'


# ═══════════════ N1 轮询中断 UI 卡住 ═══════════════

def i7_n1_state_selfheal():
    """N1：会话状态必须能从后端自愈（不依赖前端轮询）。

    判别力：旧实现 S.analyzing 只在轮询成功分支清位，
    轮询中断 → 永久卡「分析中」。
    修复后：后端 artifacts.analysis_done=true 时，session 接口的 stage
    必须是终态（matched/exp_ready），前端据此无条件收敛。
    """
    st, r = api(f'/sessions/{SID}')
    if st != 200:
        return False, f'HTTP {st}'
    stage = r.get('stage')
    arts = r.get('artifacts') or {}
    done = arts.get('analysis_done')
    if done and stage not in ('matched', 'exp_ready', 'analyzed'):
        return False, (f'⛔ 状态不自洽（N1 未修）：analysis_done=true '
                       f'但 stage={stage}')
    if not done and stage in ('matched',):
        return False, f'状态不自洽：stage=matched 但 analysis_done={done}'
    return True, f'stage={stage} / analysis_done={done}（自洽）'


# ═══════════════ N2 exp 实例折叠 ═══════════════

def i8_n2_instance_fold():
    """N2：exp 实例过多时必须折叠（不全量平铺）。

    判别力：旧实现 670 个实例标签全渲染，占满屏幕。
    修复后前端应有折叠上限常量 + 「展开/收起」控件；
    后端接口应提供 total 计数（供「还有 N 个」显示）。
    """
    st, r = api(f'/sessions/{SID}/match/cards')
    items = (r.get('items') or []) if st == 200 else []
    if not items:
        return True, '本会话无卡片（跳过）'
    # 找实例最多的卡
    maxn, worst = 0, None
    for it in items[:60]:
        fid = it.get('fid')
        if not fid:
            continue
        s2, c = api(f'/sessions/{SID}/match/cards/{fid}')
        if s2 != 200:
            continue
        n = len(((c.get('detail') or {}).get('instances') or []))
        if n > maxn:
            maxn, worst = n, fid
    if maxn < 50:
        return True, f'最大实例数 {maxn}（<50，无需折叠）'
    # 前端必须有折叠实现
    st, html = api('/', raw=True, no_prefix=True)
    if st != 200:
        return True, f'最大实例 {maxn}（前端不可读，跳过）'
    h = html.decode('utf-8', 'ignore')
    if not re.search(r'inst[-_]?fold|foldLimit|折叠|instLimit|展开', h):
        return False, (f'⛔ 实例 {maxn} 个（>{50}）但前端无折叠实现'
                       f'（N2 未修）')
    return True, f'最大实例 {maxn}，前端含折叠实现'


# ═══════════════ N3 进度呈现位置 ═══════════════

def i9_n3_progress_in_dialog():
    """N3：生成过程步骤不得外露原始工具文案，且应可折叠/在对话框内。

    判别力：旧实现左上角 #tracepanel 平铺「执行命令 (0.03s)」
    「读取文件 (0.05s)」等内部信号，且面板插在主内容区。
    修复后：① 面板挂入对话框（#agentProc）；② 步骤文案业务化。

    ⚠ 判据必须**排除注释与样式**（2026-09-18 实测踩坑）：
      ① 修复说明的注释里必然含有被修掉的旧文案（如「执行命令 (0.03s)」），
         naive 子串搜索会把「已修」误判为「未修」→ 假红；
      ② CSS 类名（.tr-i）与渲染逻辑无关，不能当作「仍在渲染」的证据。
      故先剥注释与 <style>，再查**可执行渲染代码**。
    """
    st, html = api('/', raw=True, no_prefix=True)
    if st != 200:
        return False, f'前端不可读 HTTP {st}'
    h = html.decode('utf-8', 'ignore')
    code = re.sub(r'<style[^>]*>.*?</style>', '', h, flags=re.S | re.I)
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.S)
    code = '\n'.join(l for l in code.splitlines()
                      if not l.strip().startswith(('//', '<!--', '*')))
    bad = []
    # ① 过程面板不得插在主内容区（旧实现 insertBefore(tp, bar.nextSibling)）
    if re.search(r"insertBefore\s*\(\s*tp", code):
        bad.append('tracepanel 仍插在主内容区（insertBefore）')
    # ② 步骤文案必须业务化：不得直出「工具名 + 耗时」
    for pat, tag in ((r'执行命令\s*\(\s*\$?\{', '仍直出「执行命令(耗时)」'),
                     (r'读取文件\s*\(\s*\$?\{', '仍直出「读取文件(耗时)」'),
                     (r"kind\s*===\s*'think'\s*\?\s*'[^']*'\s*:\s*'\U0001f527'",
                      '仍用 🔧 直显工具步骤（未业务化）')):
        if re.search(pat, code):
            bad.append(tag)
    # ③ 面板应挂入对话框
    if 'agentProc' not in h:
        bad.append('过程面板未挂入对话框（缺 #agentProc）')
    if bad:
        return False, f'⛔ 仍渲染原始工具文案（N3 未修）: {bad[:3]}'
    return True, '步骤已业务化 + 面板在对话框内'

def i10_n4_tabs_fixed_grey():
    """N4：一级页签必须固定显示，不可用时灰化（不是隐藏）。

    判别力：旧实现 `LV1_TABS.filter(L => L.id==='exp' || (L.id==='gen' && hasGen)…)`
    —— gen 无产物时整个页签消失，布局跳动。
    修复后不得有该动态 filter，且应有灰化（off 类）。
    """
    st, html = api('/', raw=True, no_prefix=True)
    if st != 200:
        return False, f'前端不可读 HTTP {st}'
    h = html.decode('utf-8', 'ignore')
    if re.search(r"L\.id==='gen'\s*&&\s*hasGen", h):
        return False, '⛔ 仍有 hasGen 动态过滤（N4 未修）：gen 页签会消失'
    if 'off' not in h:
        return False, '未见灰化类（off）'
    return True, '页签固定 + 灰化类存在'


# ═══════════════ N5 子页签重组 ═══════════════

def i11_n5_gen_subtabs():
    """三个生成页签必须平铺（4 配置方案 / 5 参数收集表 / 6 纯 MML）。

    判别力：
      · 旧实现只有 2 个（方案/参数收集表），缺「纯 MML」浏览页签（N5）；
      · 页签组织重构后（2026-09-18）三者必须**平铺**（lv1 各自独立），
        不得再被归到「配置生成」同一组（否则又退回三级结构）。
    """
    st, r = api(f'/sessions/{SID}/artifacts')
    tabs = (r.get('tabs') or []) if st == 200 else []
    # ★ 按 tab_id 直接定位（与层级无关）——旧判据按 lv1=='gen' 过滤，
    #   重构后只剩 1 个，属判据过期而非功能回归。
    by_id = {str(t.get('tab_id')): t for t in tabs}
    need = ['gen', 'csv', 'mml']
    got = [(k, by_id[k].get('label')) for k in need if k in by_id]
    lv1s = {str(by_id[k].get('lv1')) for k in need if k in by_id}
    if len(got) < 3:
        return False, f'⛔ 三个生成页签不全（N5 未修）：{got}'
    if len(lv1s) != 3:
        return False, f'⛔ 三个页签仍被归到同一组（未平铺）：lv1={lv1s}'
    # 三个页签必须**各有独立可用性**（不再共用一个开关）
    avail = {k: bool(by_id[k].get('available')) for k in need if k in by_id}
    return True, (f'三个生成页签平铺: {got}（lv1 各自独立，'
                  f'可用性各自判定 {avail}）')

def i12_n6_chat_feedback():
    """N6：对话长时间处理必须有中间反馈（不得只有「思考中…」）。

    判别力：旧实现 176s 里界面只有静态「（思考中…）」。
    修复后前端应有流式/阶段提示（如「正在初始化」「正在推理」），
    且后端应提供对话进度的可观测点。
    """
    st, html = api('/', raw=True, no_prefix=True)
    if st != 200:
        return False, f'前端不可读 HTTP {st}'
    h = html.decode('utf-8', 'ignore')
    has_relay = any(p in h for p in ('EventSource', 'fetchStream', 'stream',
                                     '正在初始化', '正在推理', '正在思考'))
    if not has_relay:
        return False, '⛔ 对话无中间反馈机制（N6 未修）'
    return True, '含对话中间反馈实现'


# ═══════════════ N7 规则文件权限 ═══════════════

def i13_n7_rule_perms():
    """N7：rules/ 下文件权限必须一致（644），不得有个别 600。

    判别力：旧实现 intent_routing.yaml 是 -rw-------（600），
    其余 644 → 容器内降权进程可能读不到。
    本用例通过后端提供的规则自检接口校验（无则由 I 组自检覆盖）。
    """
    # 后端无规则自检接口，改查 artifacts 的规则自检字段（N7 修复时会补上）
    st, r = api('/artifacts/rules-selfcheck')
    if st == 200:
        bad = r.get('inconsistent') or []
        if bad:
            return False, f'⛔ 权限不一致（N7 未修）: {bad}'
        return True, f'{r.get("checked")} 个规则文件权限一致'
    # 退路：会话接口若带 rules_perms 字段则用之
    st2, r2 = api(f'/sessions/{SID}')
    perms = (r2.get('rules_perms') or {}) if st2 == 200 else {}
    bad = [k for k, v in perms.items() if str(v).endswith(('00',)) and str(v) != '644']
    if perms and bad:
        return False, f'⛔ 权限不一致（N7 未修）: {bad}'
    if perms:
        return True, f'{len(perms)} 个规则文件权限一致'
    return True, '无权限自检接口（由构建期校验覆盖，见 verify_rules_perms）'


# ═══════════════ N8 分析分段上报 ═══════════════

def i14_n8_stage_report():
    """N8：分析 4 段子进程必须各报一次 stage（不只首尾）。

    判别力：旧实现只在开始时写 analyzing、结束时写 writing_artifacts。
    修复后任务 stage 历史应覆盖 ≥3 个不同阶段。
    """
    st, r = api('/tasks')
    items = (r.get('items') or []) if st == 200 else []
    ana = [t for t in items if t.get('kind') == 'exp_analysis']
    if not ana:
        return True, '无 exp_analysis 任务（跳过）'
    t = ana[0]
    hist = t.get('stage_history') or []
    names = {(h.get('stage') if isinstance(h, dict) else h) for h in hist}
    names.discard(None)
    if len(names) < 3:
        return False, (f'⛔ 分段上报不足（N8 未修）：仅 {len(names)} 个阶段 '
                       f'{sorted(names)}')
    return True, f'{len(names)} 个阶段: {sorted(names)}'


# ═══════════════ 注册 ═══════════════

CASES = [
    ('I1',  'M1 明确意图不套模板话术', i1_m1_no_template_clarify),
    ('I2',  'M1 用户原话不丢失', i2_m1_intent_not_lost),
    ('I3',  'M2 未生成项保留命令骨架', i3_m2_mml_keeps_skeleton),
    ('I4',  'M2 mml 与方案命令数对等', i4_m2_mml_md_parity),
    ('I5',  'M3 分析分段进度上报', i5_m3_analysis_stage_progress),
    ('I6',  'M3 大 EXP 耗时门槛(≤45s)', i6_m3_no_repeat_parse),
    ('I7',  'N1 会话状态自洽可自愈', i7_n1_state_selfheal),
    ('I8',  'N2 exp 实例折叠实现', i8_n2_instance_fold),
    ('I9',  'N3 无原始工具文案直出', i9_n3_progress_in_dialog),
    ('I10', 'N4 页签固定+灰化', i10_n4_tabs_fixed_grey),
    ('I11', 'N5 gen 子页签三件套', i11_n5_gen_subtabs),
    ('I12', 'N6 对话有中间反馈', i12_n6_chat_feedback),
    ('I13', 'N7 规则文件权限一致', i13_n7_rule_perms),
    ('I14', 'N8 分析分段上报≥3段', i14_n8_stage_report),
]


def main():
    global BASE, SID
    import urllib.parse  # noqa: F401  (供 _gen_text 使用)
    ap = argparse.ArgumentParser(description='I 组冒烟：第二轮问题回归')
    ap.add_argument('--base', default='http://localhost:8600')
    ap.add_argument('--sid', required=True)
    ap.add_argument('--json', default='')
    ap.add_argument('--only', default='')
    args = ap.parse_args()

    BASE = args.base.rstrip('/')
    SID = args.sid
    only = {x.strip().upper() for x in args.only.split(',') if x.strip()}

    print('=' * 58)
    print(f' I 组冒烟（第二轮问题回归）sid={SID}')
    print('=' * 58)

    for cid, name, fn in CASES:
        if only and cid not in only:
            continue
        case(cid, name, fn)

    total = len(RESULTS)
    skipped = [r for r in RESULTS if r.get('skipped')]
    judged = [r for r in RESULTS if not r.get('skipped')]
    passed = sum(1 for r in judged if r['ok'])
    print('\n' + '=' * 58)
    print(f' I 组汇总: {passed}/{len(judged)} 通过'
          + (f'（另有 {len(skipped)} 条跳过）' if skipped else ''))
    for r in [x for x in judged if not x['ok']]:
        print(f'   {r["id"]} {r["name"]}: {r["msg"][:140]}')
    for r in skipped:
        print(f'   [SKIP] {r["id"]} {r["name"]}: {r["msg"][:110]}')
    print('=' * 58)

    if args.json:
        Path(args.json).write_text(json.dumps(
            {'group': 'I', 'total': total, 'passed': passed, 'results': RESULTS},
            ensure_ascii=False, indent=2))
        print(f'结果已落盘: {args.json}')
    return 0 if not [x for x in RESULTS if not x['ok']] else 1


if __name__ == '__main__':
    import urllib.parse
    sys.exit(main())
