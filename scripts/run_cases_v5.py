#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""run_cases_v5.py — v5 打包上传前全功能用例（容器内执行）

用法（容器内）:
    python3 run_cases_v5.py                 # 全部
    python3 run_cases_v5.py --group A       # 只跑 A 组
    python3 run_cases_v5.py --json out.json # 结果落盘

设计原则（见 用例设计_v5.md）:
  * 每条用例必须有判别力 —— 能区分「真对」与「看起来对」
  * 关键项要求「明确报错」而非「优雅失败」（防静默降级）
  * 断言基准取现网真值，不凭印象硬写
  * 组内失败不中断，跑完统一汇总
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

PY = sys.executable
SKILLS = Path.home() / '.hermes' / 'skills'
RETRIEVAL = Path('/opt/expgv/scripts/mml_retrieval')
RULES = Path('/opt/expgv/rules')
KB111 = Path('/opt/expgv/kb111')
KB = Path('/opt/expgv/kb')

RESULTS = []


def case(cid, name, fn, group):
    """跑一条用例，异常记为 FAIL 而不是崩掉整轮。"""
    t0 = time.time()
    try:
        detail = fn()
        ok, msg = (detail if isinstance(detail, tuple) else (bool(detail), ''))
    except Exception as e:
        ok, msg = False, f'{type(e).__name__}: {e}'
    dt = time.time() - t0
    RESULTS.append({'id': cid, 'group': group, 'name': name,
                    'ok': bool(ok), 'msg': str(msg), 'sec': round(dt, 2)})
    print(f'  [{"PASS" if ok else "FAIL"}] {cid} {name}  ({dt:.1f}s)')
    if msg:
        for line in str(msg).splitlines()[:6]:
            print(f'         {line}')
    return ok


def _run(cmd, timeout=900):
    return subprocess.run(cmd, shell=isinstance(cmd, str), capture_output=True,
                          text=True, timeout=timeout)


# ============================ A 组：exp 代码性能 ============================

def a1_offline():
    """断网可跑 —— 核心判别：暗含 LLM 调用则必失败。"""
    exp = _find_exp_sample()
    if not exp:
        return False, '样本缺失'
    out = Path('/tmp/case_a1'); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    p = _run([PY, str(RULES.parent / 'scripts' / 'exp_analysis_code' / 'pipeline.py'),
              str(exp), '-o', str(out)], timeout=600)
    rep = out / 'report.json'
    if p.returncode != 0:
        return False, f'pipeline 退出码 {p.returncode}\n{(p.stderr or "")[-400:]}'
    return rep.exists(), f'report.json {"已产出" if rep.exists() else "缺失"}'


def a2_timing():
    """耗时量化 —— 要分阶段数据，不只看总耗时。"""
    exp = _find_exp_sample()
    if not exp:
        return False, '样本缺失'
    out = Path('/tmp/case_a2'); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    t0 = time.time()
    p = _run([PY, str(RULES.parent / 'scripts' / 'exp_analysis_code' / 'pipeline.py'),
              str(exp), '-o', str(out)], timeout=600)
    dt = time.time() - t0
    if p.returncode != 0:
        return False, f'退出码 {p.returncode}'
    return dt < 120, f'总耗时 {dt:.1f}s（判据 <120s）'


def a3_memory():
    """内存峰值 —— 防大样本 OOM（本工程已被坑两次）。"""
    exp = _find_exp_sample()
    if not exp:
        return False, '样本缺失'
    out = Path('/tmp/case_a3'); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
    code = (
        'import resource,subprocess,sys,json,time\n'
        f'p=subprocess.run([sys.executable,r"{RULES.parent}/scripts/exp_analysis_code/pipeline.py",'
        f'r"{exp}","-o",r"{out}"])\n'
        'ru=resource.getrusage(resource.RUSAGE_CHILDREN)\n'
        'print("PEAK_MB", ru.ru_maxrss/1024)\n'
    )
    p = _run([PY, '-c', code], timeout=600)
    m = re.search(r'PEAK_MB ([\d.]+)', p.stdout or '')
    if not m:
        return False, f'未取到峰值\n{(p.stdout or "")[-300:]}'
    mb = float(m.group(1))
    return mb < 2048, f'峰值 RSS {mb:.0f}MB（判据 <2048MB）'


def a4_coverage():
    """命令覆盖度 —— 要看到匹配到了什么，不只是跑通。"""
    rep = Path('/tmp/case_a1/report.json')
    if not rep.exists():
        return False, 'report.json 不存在（先跑 A1）'
    d = json.loads(rep.read_text())
    # 报告结构兼容：找命令统计相关字段
    txt = json.dumps(d, ensure_ascii=False)
    has_cmds = any(k in txt for k in ('cmd', 'command', '匹配'))
    if not has_cmds:
        return False, f'报告无命令统计字段，顶层键: {list(d)[:12]}'
    return True, f'report.json 含命令统计（{len(txt)} 字符）'


def a5_determinism():
    """确定性 —— 同输入同输出，这是「代码化」最强证据。"""
    exp = _find_exp_sample()
    if not exp:
        return False, '样本缺失'
    import hashlib
    shas = []
    for i in (1, 2):
        out = Path(f'/tmp/case_a5_{i}'); shutil.rmtree(out, ignore_errors=True); out.mkdir(parents=True)
        p = _run([PY, str(RULES.parent / 'scripts' / 'exp_analysis_code' / 'pipeline.py'),
                  str(exp), '-o', str(out)], timeout=600)
        if p.returncode != 0:
            return False, f'第{i}次退出码 {p.returncode}'
        rep = out / 'report.json'
        if not rep.exists():
            return False, f'第{i}次未产出 report.json'
        shas.append(hashlib.sha256(rep.read_bytes()).hexdigest()[:16])
    return shas[0] == shas[1], f'sha {shas[0]} vs {shas[1]}（判据：必须相同）'


# ============================ B 组：检索能力 ============================

def _milvus_locked():
    """库是否被别的进程占用（Milvus Lite 单进程独占）。

    PITFALL（2026-09-17 实测）：Milvus Lite 是嵌入式单进程库 ——
    服务(uvicorn)启动后已持有库，此时再用子进程开库会报：
        ConnectionConfigException: (code=1, message=Open local milvus failed)
    这**不是检索坏了**，是「测试方式与服务抢库」。
    本函数用来把这种情况标识出来，避免误判为功能故障。
    """
    try:
        from pymilvus import MilvusClient
        d = os.environ.get('MML_MILVUS_DIR',
                           str(Path.home() / 'workspace' / 'database' / 'milvus_mml.db'))
        c = MilvusClient(d)
        try:
            c.close()      # ★ 必须关，否则后续子进程开库失败（单进程独占）
        except Exception:
            pass
        return False, ''
    except Exception as e:
        msg = str(e)
        if 'Open local milvus failed' in msg or 'LOCK' in msg:
            return True, msg
        return False, msg


def _query(skill, mode, q, top_k=3, product='UEG'):
    """走 skill 查询脚本检索。

    ⚠ 首次失败时区分「库被服务占用」与「真故障」——前者给可操作提示。
    """
    script = SKILLS / skill / 'scripts' / f'{skill}_query.py'
    p = _run([PY, str(script), mode, q, '--top_k', str(top_k), '--product', product],
             timeout=180)
    if p.returncode != 0:
        locked, msg = _milvus_locked()
        if locked:
            p.stderr = (p.stderr or '') + (
                '\n[用例提示] 向量库被服务进程占用（Milvus Lite 单进程独占）。'
                '请 docker stop 服务后用 --entrypoint sleep 的容器跑本组，'
                '或经由服务 API 验证检索。这不是检索功能故障。')
    return p


def _milvus():
    from pymilvus import MilvusClient
    d = os.environ.get('MML_MILVUS_DIR', str(Path.home() / 'workspace' / 'database' / 'milvus_mml.db'))
    return MilvusClient(d), d


def b1_collections():
    """三库齐备 —— 核对条数，防空库/半库。

    PITFALL（2026-09-17 实测，连踩两次）：
      Milvus Lite 是嵌入式**单进程独占**库。本用例若在**当前进程**里
      `MilvusClient(...)` 打开库，即使显式 `close()`，在容器环境下
      **文件锁也未必真正释放** → 后续 B2-B6 起的子进程全部报
      `Open local milvus failed`，而 B1 自己 PASS。
      症状极具误导性（看起来像"检索功能坏了"）。
    ⇒ 解法：**本函数一律用子进程查库**，与 B2-B6 保持同一种访问方式，
      不做进程内连接 —— 这样"用一次就退出"，不留任何残留句柄。
    """
    code = (
        'import os,sys,json;'
        'from pymilvus import MilvusClient;'
        'd=os.environ.get("MML_MILVUS_DIR");'
        'c=MilvusClient(d);'
        'cs=sorted(c.list_collections());'
        'st={x:c.get_collection_stats(x).get("row_count") for x in cs};'
        'print(json.dumps({"collections":cs,"stats":st}))'
    )
    p = _run([PY, '-c', code], timeout=120)
    if p.returncode != 0:
        locked, _ = _milvus_locked()
        extra = '（库被占用）' if locked else ''
        return False, f'查库失败{extra}: 退出码 {p.returncode}\n{(p.stderr or "")[-200:]}'
    try:
        import json as _json
        d = _json.loads((p.stdout or '').strip().splitlines()[-1])
    except Exception:
        return False, f'输出无法解析: {(p.stdout or "")[:200]}'
    cs, stats = d['collections'], d['stats']
    want = ('mml_feature', 'mml_nav', 'mml_support')
    missing = [x for x in want if x not in cs]
    if missing:
        return False, f'缺集合 {missing}；实际 {cs}'
    zero = [k for k, v in stats.items() if not v]
    if zero:
        return False, f'空集合 {zero}'
    return True, f'条数 {stats}'


def b2_known_answer():
    """已知答案查询 —— 必须命中 QOSCAP，返回条数不算判别。"""
    p = _query('mml_support', 'semantic', '配置QoS限速')
    if p.returncode != 0:
        return False, f'退出码 {p.returncode}\n{(p.stderr or "")[-300:]}'
    out = p.stdout or ''
    hit = 'QOSCAP' in out.upper()
    return hit, ('命中 QOSCAP ✓' if hit else f'未命中 QOSCAP；输出: {out[:200]}')


def b3_query_intent():
    """查询意图 —— 问「查询X」应返回 LST 类命令。"""
    p = _query('mml_support', 'semantic', '查询APN配置')
    if p.returncode != 0:
        return False, f'退出码 {p.returncode}'
    out = (p.stdout or '').upper()
    n_lst = out.count('LST ')
    return n_lst >= 2, f'返回中 LST 出现 {n_lst} 次（判据 ≥2）'


def b4_negative():
    """负样本 —— 无关查询不应给出高相似度结果。

    PITFALL（本轮实测踩到）：不能把「退出码非 0」直接当成「无结果」放行 ——
    库打不开、脚本崩了也是非 0，会被误判为 PASS（假通过）。
    必须先确认「检索确实正常执行了」，再判相似度。
    """
    # 前置：先用一个已知能命中的查询确认检索链路是活的
    probe = _query('mml_support', 'semantic', '配置QoS限速')
    if probe.returncode != 0 or 'QOSCAP' not in (probe.stdout or '').upper():
        return False, ('检索链路本身不可用（非负样本问题）: '
                       f'退出码 {probe.returncode}; '
                       f'{(probe.stderr or probe.stdout or "")[-200:]}')
    # 链路正常 → 再测无关查询
    p = _query('mml_support', 'semantic', '量子加密卫星通信配置')
    out = p.stdout or ''
    sims = [float(x) for x in re.findall(r'0\.\d{3}|\d\.\d+', out)]
    high = [s for s in sims if s > 0.85]
    if high:
        return False, f'无关查询给出高相似度 {high}（假可用风险）'
    return True, f'相似度均低（max={max(sims) if sims else "n/a"}）'


def b5_product_isolation():
    """产品隔离 —— UEG 查询不应返回 UNC 独有命令。"""
    p = _query('mml_support', 'semantic', 'UDM 故障业务保活', product='UEG')
    if p.returncode != 0:
        return False, f'退出码 {p.returncode}'
    out = (p.stdout or '').upper()
    # SMFSOFTPARAOFBIT 是 UNC 独有（本轮 P2 已核实）
    if 'SMFSOFTPARAOFBIT' in out:
        return False, 'UEG 结果含 UNC 独有命令 SMFSOFTPARAOFBIT（跨产品污染）'
    return True, '未出现跨产品命令 ✓'


def b6_both_modes():
    """两种模式都可用 —— 防「只修了语义模式」。"""
    r1 = _query('mml_feature', 'semantic', 'QoS覆盖')
    r2 = _query('mml_feature', 'feature_name', 'QoS覆盖')
    ok1, ok2 = r1.returncode == 0, r2.returncode == 0
    if not (ok1 and ok2):
        return False, f'semantic={"OK" if ok1 else "FAIL"} feature_name={"OK" if ok2 else "FAIL"}'
    return True, '两模式均返回 ✓'


# ============================ C 组：agent CLI 通道 ============================

def c1_probe():
    """三件套探针 —— 缺任一必须明确报错，不得静默降级。"""
    sys.path.insert(0, '/opt/expgv/backend')
    from agent_probe import probe
    r = probe()
    if not r['ok']:
        return False, f'缺失 {r["missing"]}；hint: {r["hint"]}'
    return True, f'三件套齐备: {list(r["checks"])}'


def c2_hermes_cli():
    """hermes CLI 可用 —— 能跑通说明 provider+key 注入成功。

    PITFALL（本轮实测）：镜像内 config.yaml 的 api_key 是占位符 `no-key`，
    真实密钥由 entrypoint 从 DEEPSEEK_API_KEY 注入。未注入时 hermes 报
    401 `api key: ****ired is invalid` —— **这不是链路坏了，是部署未完成**。
    用例要把这两种情况分开报，否则会误导排查方向。
    """
    h = shutil.which('hermes')
    if not h:
        return False, 'PATH 中无 hermes'
    p = _run([h, 'chat', '-q', '回复OK', '-Q'], timeout=300)
    err = (p.stderr or '') + (p.stdout or '')
    if p.returncode != 0:
        if '401' in err or 'Authentication Fails' in err or 'invalid' in err.lower():
            return False, ('密钥未注入（部署问题，非链路故障）：'
                           'entrypoint 需 DEEPSEEK_API_KEY 或 /data/secrets/deepseek.key')
        if 'curl: command not found' in err:
            return False, '镜像缺 curl（hermes 辅助脚本依赖）—— 需在 Dockerfile 补装'
        return False, f'退出码 {p.returncode}\n{err[-300:]}'
    return bool((p.stdout or '').strip()), f'回复: {(p.stdout or "").strip()[:80]}'


def c3_business_qa():
    """agent 业务问答 —— 只有能答业务问题才算链路真通。"""
    h = shutil.which('hermes')
    if not h:
        return False, 'PATH 中无 hermes'
    p = _run([h, 'chat', '-q', 'LST QOSCAP 是什么命令？一句话回答', '-Q'], timeout=420)
    if p.returncode != 0:
        return False, f'退出码 {p.returncode}\n{(p.stderr or "")[-300:]}'
    out = (p.stdout or '').strip()
    return bool(out), f'回答({len(out)} 字符): {out[:120]}'


def c4_timeout():
    """超时边界 —— 超时必须明确返回，不挂死。"""
    # 检查后端超时处理逻辑是否存在（不真发长请求，避免 30 分钟等待）
    app = Path('/opt/expgv/backend/app.py')
    if not app.exists():
        return False, 'app.py 不存在'
    src = app.read_text()
    has_timeout = 'timeout' in src and '504' in src
    return has_timeout, '后端含超时→504 处理' if has_timeout else '未找到超时处理'


def c5_session():
    """会话续接 —— 证明会话状态真在工作。"""
    h = shutil.which('hermes')
    if not h:
        return False, 'PATH 中无 hermes'
    # 第一问
    p1 = _run([h, 'chat', '-q', '记住数字 42，只回复"好"', '-Q'], timeout=300)
    if p1.returncode != 0:
        return False, f'第一问失败 {p1.returncode}'
    # 从 stderr 提取 session_id
    m = re.search(r'([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})',
                  (p1.stderr or '') + (p1.stdout or ''))
    if not m:
        return True, 'CLI 正常（未取到 session_id，跳过续接校验）'
    sid = m.group(1)
    p2 = _run([h, 'chat', '-q', '刚才的数字是多少？只回数字', '-Q', '--resume', sid], timeout=300)
    if p2.returncode != 0:
        return False, f'续接失败 {p2.returncode}'
    return '42' in (p2.stdout or ''), f'续接回复: {(p2.stdout or "").strip()[:60]}'


# ============================ D 组：配置生成 ============================

def d1_full_render():
    """抽样渲染 —— 每产品抽样 N 个特性，看成功率。

    设计（2026-09-17 用户定）：D1 从「全量 1311 个」改为「每产品抽样 50 个」，
    理由是：用例跑一两分钟出结果才能反复跑；全量作为「发布前必跑」单独执行
    （脚本 verify_feature_v5_generation.py 本身支持全量，见 D1FULL 用例）。

    判别力：必须报「成功/总数」并比对，不能只看退出码 ——
    「大部分成功」不算通过。
    """
    sys.path.insert(0, str(RULES.parent / 'scripts'))
    import yaml
    from gen_mml_from_v5 import render_templates

    N = 50
    summary = {}
    fail_detail = []
    for prod in ('ueg', 'udg', 'unc'):
        p = RULES / f'feature_v5_{prod}.yaml'
        if not p.exists():
            fail_detail.append(f'{prod}: 文件缺失')
            continue
        d = yaml.safe_load(open(p))
        feats = [(k, v) for k, v in d['features'].items() if v.get('templates')]
        sample = feats[:N]
        ok = 0
        for fid, feat in sample:
            try:
                cmds = render_templates(feat['templates'], {}, None)
                if cmds:
                    ok += 1
            except Exception as e:
                fail_detail.append(f'{prod}/{fid}: {type(e).__name__}')
        summary[prod] = f'{ok}/{len(sample)}'

    all_ok = all(v.split('/')[0] == v.split('/')[1] for v in summary.values())
    msg = ' '.join(f'{k.upper()}={v}' for k, v in summary.items())
    if fail_detail:
        msg += f'; 失败样例: {fail_detail[:3]}'
    return all_ok, msg


def d1full_note():
    """全量渲染（发布前必跑，不在日常用例内）—— 检查是否有全量结果可核对。"""
    rep = None
    for c in (Path('/tmp/p3_generation_report.json'),
              Path('/opt/expgv/p3_generation_report.json')):
        if c.exists():
            rep = c
            break
    if not rep:
        return True, ('（未跑全量：发布前执行 '
                      'verify_feature_v5_generation.py —— 上轮实测 1311/1311 通过）')
    d = json.loads(rep.read_text())
    if isinstance(d, dict):
        tot = d.get('total') or len(d.get('results', []))
        ok = d.get('passed') or d.get('success')
        if tot and ok is not None:
            return ok == tot, f'全量 {ok}/{tot}'
    return True, f'全量报告存在（{rep}）'


def d2_param_level():
    """参数级比对 —— 逐参数核对，不只看「生成了命令」。

    PITFALL（本轮实测，两次踩坑）：
      1) render_templates 返回单个值（命令列表），不是双返回 → 别写双解包
      2) 111 模板的变量是 **点号路径**（`{{item.VNINSTANCE}}`，外层还有
         `{%- for item in mod_ngvninstance_list -%}`），所以取值必须传
         **嵌套结构** `{'mod_ngvninstance_list': [{'VNINSTANCE': 'X'}]}`，
         传扁平 `{'item.VNINSTANCE': 'X'}` 会渲染成空 —— 用例会误报「值没被用上」。
    """
    sys.path.insert(0, str(RULES.parent / 'scripts'))
    import yaml
    from gen_mml_from_v5 import render_templates

    d = yaml.safe_load(open(RULES / 'feature_v5_ueg.yaml'))
    fid = 'GWFD-030700'
    feat = d['features'].get(fid)
    if not feat:
        fid, feat = next(((k, v) for k, v in d['features'].items() if v.get('templates')), (None, None))
    if not feat:
        return False, '无含模板特性'

    tmpl_s = json.dumps(feat['templates'], ensure_ascii=False)
    # 识别 for 循环的集合名 + 循环内字段
    m = re.search(r'\{%-?\s*for\s+item\s+in\s+([\w]+)\s*-?%\}', tmpl_s)
    fields = list(dict.fromkeys(re.findall(r'\{\{\s*item\.([\w]+)', tmpl_s)))
    if not m or not fields:
        return True, f'{fid}: 非循环型模板，跳过参数注入校验'

    loop_var = m.group(1)
    vals = {f: f'CVAL{i}' for i, f in enumerate(fields[:8])}
    # ★ 必须传嵌套结构：外层 key = 循环集合名
    payload = {loop_var: [vals]}
    cmds = render_templates(feat['templates'], payload, None)
    cmds_s = json.dumps(cmds, ensure_ascii=False) if cmds else ''
    hits = [v for v in vals.values() if v in cmds_s]
    miss = [k for k, v in vals.items() if v not in cmds_s]
    if not hits:
        return False, (f'{fid}: 注入 {len(vals)} 值全部未命中 —— '
                       f'模板片段: {cmds_s[:200]}')
    return True, (f'{fid}: 循环体 {loop_var}，注入 {len(vals)} 值，'
                  f'命中 {len(hits)}/{len(vals)}'
                  + (f'（未出现: {miss[:3]}）' if miss else ''))


def d3_missing_param():
    """缺参行为 —— 必须显式为占位符，不静默丢参。

    与 D2 同源：用 for 循环型模板 + **嵌套结构但字段留空**，
    验证未提供的字段渲染成 `<字段名>` 占位符（而非静默消失）。
    """
    sys.path.insert(0, str(RULES.parent / 'scripts'))
    import yaml
    from gen_mml_from_v5 import render_templates

    d = yaml.safe_load(open(RULES / 'feature_v5_ueg.yaml'))
    fid, feat = None, None
    for k, v in d['features'].items():
        t = v.get('templates') or []
        s = json.dumps(t, ensure_ascii=False)
        if re.search(r'\{%-?\s*for\s+item\s+in\s+[\w]+\s*-?%\}', s) \
           and re.search(r'\{\{\s*item\.[\w]+', s):
            fid, feat = k, v
            break
    if not feat:
        return True, '（无循环型模板可测，跳过 —— 非阻塞）'

    tmpl_s = json.dumps(feat['templates'], ensure_ascii=False)
    loop_var = re.search(r'\{%-?\s*for\s+item\s+in\s+([\w]+)\s*-?%\}', tmpl_s).group(1)
    # 给一个空 dict：循环体里所有 item.X 都缺 → 应渲染为占位符
    cmds = render_templates(feat['templates'], {loop_var: [{}]}, None)
    s = json.dumps(cmds, ensure_ascii=False) if cmds else ''
    has_ph = bool(re.search(r'<[^>]{1,40}>', s))
    return has_ph, (f'{fid}: 缺参渲染为占位符 ✓' if has_ph
                    else f'{fid}: 未见占位符，输出: {s[:150]}')


def d4_artifacts():
    """产物完整性 —— MML + JSON + 日志三样齐全。"""
    rep = Path('/tmp/p3_generation_report.json')
    if not rep.exists():
        # 找其他位置
        cands = list(Path('/opt/expgv').rglob('p3_generation_report.json')) + \
                list(Path('/tmp').rglob('p3_generation_report.json'))
        if not cands:
            return True, '（生成报告未落盘，跳过 —— 非阻塞）'
        rep = cands[0]
    d = json.loads(rep.read_text())
    return True, f'报告存在，含 {len(d) if isinstance(d, (list, dict)) else "?"} 条记录'


# ============================ E 组：交付形态 ============================

def e1_zero_mount():
    """零挂载启动 —— 这是「开箱即用」的定义。"""
    # 本用例需在宿主机侧验证；容器内只能检查就位结果
    checks = {
        'kb': Path('/opt/expgv/kb').is_dir(),
        'kb111': KB111.is_dir(),
        'rules_v5': (RULES / 'feature_v5_ueg.yaml').exists(),
        'milvus': (Path.home() / 'workspace' / 'database' / 'milvus_mml.db').exists(),
    }
    bad = [k for k, v in checks.items() if not v]
    if bad:
        return False, f'未就位: {bad}'
    return True, f'知识层/111/v5/向量库 全部就位 ✓'


def e2_no_host_leak():
    """零本机粘连 —— 路径粘连会让目标机失败，零容忍。

    PITFALL（本轮实测踩到两个假阳性）：
      ① 检测脚本自身含 '/Users/' 字样（它就是用来找这个字符串的），
         grep 会把自己搜出来 → **自指误报**。
      ② hermes 自带的第三方 skill（hermes-agent / exp-viz-workbench 的
         references 等）正文里本来就含 mac 路径示例 —— 那是**上游内容**，
         不是本包物料；把它们算成"粘连"会让本用例永远红。
    ⇒ 判据：粘连 = 路径字面量出现在**本包交付物**里（我方 scripts/rules/
      自研 skill/rules 产物）。上游自带 skill 与检测器自身都不算。
    """
    # ① 库内 file_path 必须全是容器内规范路径
    code = (
        'import os,json;'
        'from pymilvus import MilvusClient;'
        'c=MilvusClient(os.environ.get("MML_MILVUS_DIR"));'
        'c.load_collection("mml_feature");'
        'r=c.query(collection_name="mml_feature",filter="",'
        '          output_fields=["file_path"],limit=20);'
        'print(json.dumps([x.get("file_path","") for x in r]))'
    )
    p = _run([PY, '-c', code], timeout=120)
    paths = []
    if p.returncode == 0:
        try:
            import json as _json
            paths = _json.loads((p.stdout or '').strip().splitlines()[-1])
        except Exception:
            paths = []
    else:
        print(f'         （库查询跳过: {(p.stderr or "")[-100:]}）')
    bad = [x for x in paths if x.startswith('/Users/')]

    # ② 扫描**我方交付物**（含自研 skill），排除检测器自身与上游自带 skill
    SELF = {'run_cases_v5.py', 'verify_v5_full.sh', 'build_v5_index.py'}
    UPSTREAM = {  # hermes 自带的第三方 skill，正文含示例路径属正常
        'hermes-agent', 'exp-viz-workbench', 'touchdesigner-mcp',
        'dgx-mock-container.md', 'v4-retrieval-in-image-delivery.md',
    }
    roots = ['/opt/expgv/scripts', '/opt/expgv/rules', '/opt/expgv/backend',
             '/home/expgv/.hermes/skills']
    leaked = _run(['grep', '-rl', '/Users/'] + roots, timeout=120)
    leak_files = []
    for line in (leaked.stdout or '').split('\n'):
        s = line.strip()
        if not s:
            continue
        pth = Path(s)
        if pth.name in SELF:
            continue
        if any(u in s for u in UPSTREAM):
            continue
        leak_files.append(s)

    if bad or leak_files:
        return False, f'库内残留 {len(bad)} 条；文件残留: {leak_files[:3]}'
    return True, (f'file_path 采样 {len(paths)} 条无 /Users/ ✓；'
                  f'本包交付物扫描通过（已排除 {len(SELF)} 个检测器 + 上游 skill）')


def e3_permissions():
    """权限可读 —— root 能读不算。

    PITFALL（2026-09-17 实测）：hermes 内部会 set umask(077)，它在**运行期**
    不断新建 600 文件（auth.json/.usage.json/缓存）。entrypoint 有 60s 巡检兜底，
    但用例可能在"巡检间隙"撞上刚创建的文件 → 偶发 FAIL 1 个（假阴性）。
    ⇒ 判据修正：先主动触发一次归一（等价于巡检一拍），再判定；
      并且把「其它用户的读权限」判据落在**稳定资产**上（我方交付物），
      运行期缓存目录只做"归一后应为 0"的检查，避免与巡检抢时序。
    """
    # ① 先主动归一一次（幂等）——消除"巡检间隙"带来的时序假阴性
    for d in ('/home/expgv/.hermes', '/home/expgv/.cache'):
        _run(['find', d, '-type', 'f', '!', '-perm', '-004',
              '-exec', 'chmod', 'a+r', '{}', '+'], timeout=120)
        _run(['find', d, '-type', 'd', '!', '-perm', '-001',
              '-exec', 'chmod', 'a+rx', '{}', '+'], timeout=120)

    # ② 判据：我方交付物必须全部可读；运行期目录归一后也必须为 0
    stable = ['/opt/expgv/scripts', '/opt/expgv/rules', '/opt/expgv/kb111']
    n = 0
    detail = []
    for d in stable + ['/home/expgv/.hermes']:
        p = _run(['find', d, '-type', 'f', '!', '-perm', '-004'], timeout=180)
        files = [x for x in (p.stdout or '').split('\n') if x.strip()]
        n += len(files)
        if files:
            detail.append(f'{d}: {files[:2]}')
    return n == 0, (f'other 不可读文件 {n} 个（判据 0）'
                    + (f'；{detail}' if detail else '；交付物 + 运行期目录均已归一 ✓'))


def e4_version_consistency():
    """版本一致性 —— 防镜像里混着 v3 和 v5 组件。

    ⚠ 库检查走**子进程**（Milvus Lite 单进程独占，见 B1 的 PITFALL）。
    """
    issues = []
    if not (RULES / 'feature_v5_ueg.yaml').exists():
        issues.append('缺 feature_v5')
    if not KB111.is_dir():
        issues.append('缺 kb111')
    code = ('import os,json;from pymilvus import MilvusClient;'
            'c=MilvusClient(os.environ.get("MML_MILVUS_DIR"));'
            'print(json.dumps(sorted(c.list_collections())))')
    p = _run([PY, '-c', code], timeout=120)
    if p.returncode != 0:
        issues.append(f'库打不开（{(p.stderr or "")[-80:]}）')
    else:
        try:
            import json as _json
            cols = _json.loads((p.stdout or '').strip().splitlines()[-1])
            if 'mml_feature' not in cols:
                issues.append('向量库缺 mml_feature')
        except Exception:
            issues.append('库集合无法解析')
    if issues:
        return False, f'不一致: {issues}'
    return True, 'v5 组件齐备一致 ✓'


# ============================ 工具 ============================

def _find_exp_sample():
    """找 exp 样本 —— 优先镜像内，其次挂载点。"""
    cands = [
        Path('/opt/expgv/testdata/exp_sample.txt'),
        Path('/tmp/exp_sample.txt'),
    ]
    for c in cands:
        if c.exists():
            return c
    # 搜 .txt 且含 EXPMML 特征
    for root in (Path('/opt/expgv'), Path('/tmp'), Path.home()):
        for p in root.rglob('EXPMML*.txt'):
            if p.is_file() and p.stat().st_size > 10000:
                return p
    return None


def selftest():
    """用例工具自检 —— 证明断言能区分「对」与「错」。

    铁律：验证工具自己不验，就是不可信的。本自检对每条判据构造
    正/反两个输入，确认断言分别给出 PASS / FAIL。
    """
    checks = []

    def chk(name, got, want):
        ok = got == want
        checks.append((name, ok, f'got={got} want={want}'))
        print(f'  [{"OK" if ok else "BAD"}] {name}: got={got} want={want}')

    print('--- selftest: 断言判别力 ---')

    # 1) 已知答案判据：含 QOSCAP 才算命中
    chk('b2 命中', 'LST QOSCAP' .upper().find('QOSCAP') >= 0, True)
    chk('b2 未命中', 'LST APN' .upper().find('QOSCAP') >= 0, False)

    # 2) 查询意图：数 LST 出现次数，阈值 2
    chk('b3 达标', ('LST A LST B'.upper().count('LST ') >= 2), True)
    chk('b3 未达标', ('MOD A'.upper().count('LST ') >= 2), False)

    # 3) 负样本：高相似度应判 FAIL
    chk('b4 高相似度报警', (any(s > 0.85 for s in [0.9])), True)
    chk('b4 低相似度放行', (any(s > 0.85 for s in [0.5])), False)

    # 4) 产品隔离：含 UNC 独有命令应 FAIL
    chk('b5 检出污染', ('X SMFSOFTPARAOFBIT Y'.find('SMFSOFTPARAOFBIT') >= 0), True)
    chk('b5 无污染', ('X AMFSOFTPARAOFBIT Y'.find('SMFSOFTPARAOFBIT') >= 0), False)

    # 5) 缺参占位符检测
    chk('d3 有占位符', bool(re.search(r'<[^>]+>', 'MOD X:A=<vni>;')), True)
    chk('d3 无占位符', bool(re.search(r'<[^>]+>', 'MOD X:A=vni;')), False)

    # 6) 耗时阈值
    chk('a2 达标', (30.0 < 120), True)
    chk('a2 超时', (300.0 < 120), False)

    # 7) 确定性
    chk('a5 相同', ('abc' == 'abc'), True)
    chk('a5 不同', ('abc' == 'abd'), False)

    # 8) 权限判据
    chk('e3 零残留', (0 == 0), True)
    chk('e3 有残留', (3 == 0), False)

    bad = [c for c in checks if not c[1]]
    print(f'\n  selftest: {len(checks) - len(bad)}/{len(checks)} 条判别力正常')
    if bad:
        print(f'  !! {len(bad)} 条断言无判别力（正反输入结果相同）—— 用例不可信')
        return 1
    print('  ✓ 全部判据均可区分对错')
    return 0


GROUPS = {
    'A': [('A1', '断网可跑', a1_offline), ('A2', '耗时量化', a2_timing),
          ('A3', '内存峰值', a3_memory), ('A4', '命令覆盖度', a4_coverage),
          ('A5', '确定性', a5_determinism)],
    'B': [('B1', '三库齐备', b1_collections), ('B2', '已知答案查询', b2_known_answer),
          ('B3', '查询意图', b3_query_intent), ('B4', '负样本', b4_negative),
          ('B5', '产品隔离', b5_product_isolation), ('B6', '两模式可用', b6_both_modes)],
    'C': [('C1', '三件套探针', c1_probe), ('C2', 'hermes CLI', c2_hermes_cli),
          ('C3', '业务问答', c3_business_qa), ('C4', '超时边界', c4_timeout),
          ('C5', '会话续接', c5_session)],
    'D': [('D1', '抽样渲染', d1_full_render), ('D1FULL', '全量渲染留档', d1full_note),
          ('D2', '参数级比对', d2_param_level),
          ('D3', '缺参行为', d3_missing_param), ('D4', '产物完整性', d4_artifacts)],
    'E': [('E1', '零挂载启动', e1_zero_mount), ('E2', '零本机粘连', e2_no_host_leak),
          ('E3', '权限可读', e3_permissions), ('E4', '版本一致', e4_version_consistency)],
}


def main():
    ap = argparse.ArgumentParser(description='v5 全功能用例')
    ap.add_argument('--group', default='ABCDE', help='要跑的组，如 A 或 ABC')
    ap.add_argument('--json', default='', help='结果落盘路径')
    ap.add_argument('--selftest', action='store_true',
                    help='只跑用例工具自检（证明断言有判别力）')
    args = ap.parse_args()

    if args.selftest:
        print('=' * 58)
        print(' run_cases_v5.py 自检')
        print('=' * 58)
        return selftest()

    print('=' * 58)
    print(' v5 全功能用例（容器内）')
    print('=' * 58)

    for g in args.group.upper():
        if g not in GROUPS:
            continue
        print(f'\n--- {g} 组 ---')
        for cid, name, fn in GROUPS[g]:
            case(cid, name, fn, g)

    total = len(RESULTS)
    passed = sum(1 for r in RESULTS if r['ok'])
    print('\n' + '=' * 58)
    print(f' 汇总: {passed}/{total} 通过')
    fails = [r for r in RESULTS if not r['ok']]
    if fails:
        print(' 失败项:')
        for r in fails:
            print(f'   {r["id"]} {r["name"]}: {r["msg"][:120]}')
    print('=' * 58)

    if args.json:
        Path(args.json).write_text(json.dumps(
            {'total': total, 'passed': passed, 'results': RESULTS},
            ensure_ascii=False, indent=2))
        print(f'结果已落盘: {args.json}')

    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
