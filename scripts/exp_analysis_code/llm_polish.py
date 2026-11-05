#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""llm_polish.py — T8 P2 LLM 润色器（可选增强，不阻塞主路径）。

输入 report.json（P1 确定性管线产物），调用 LLM 生成三段语义增强：
  1. conclusion        关键结论叙述化（一段话业务定性，替代模板摘要）
  2. diff_review       差异语义判断（等价 / 缺口 / 需审视，补 license_off/structure 空列）
  3. watchlist_meaning 待审视业务含义 + 建议动作（尤其跨层推理项①④）
独立 120s 超时、失败/无 key 静默返回 None（任务仍成功、报告缺段可读）。

红线：代码只含 prompt 模板与协议字段；所有现网实例值均由 report 运行时注入。
"""

import json
import os
import re
import time
from pathlib import Path

try:
    import requests
except ImportError:  # 精简环境无 requests（如容器 python3.14）→ 静默降级，不阻塞主路径
    requests = None

BASE_URL = os.environ.get('DEEPSEEK_BASE_URL', 'https://api.deepseek.com/v1')
# ★ 默认模型名必须是**确定存在**的（此前 'deepseek-v4-pro' 存疑，
#   若环境变量未设 → 每次都静默失败）。可用 DEEPSEEK_MODEL 覆盖。
MODEL = os.environ.get('DEEPSEEK_MODEL', 'deepseek-chat')
TIMEOUT = 120


def _load_key():
    for p in (Path.home() / '.hermes/.env', Path.home() / '.env'):
        if p.exists():
            for line in p.read_text(encoding='utf-8').splitlines():
                if line.startswith('DEEPSEEK_API_KEY='):
                    return line.split('=', 1)[1].strip().strip('"').strip("'")
    return os.environ.get('DEEPSEEK_API_KEY')


def _build_prompt(report):
    """把 P1 结构化事实压成摘要，注入 prompt（实例值运行时传入，非硬编码）。"""
    cv = report.get('chain_verdicts', [])
    chains = [f"链{c['chain']} {c['name']}={c['status']}"
              + (f"（锚点 {c.get('anchor_value')}）" if c.get('anchor_value') else '')
              for c in cv]
    diffs = [f"[{d.get('chain')}|{d.get('category')}] 文档:{d.get('doc_side') or '—'} "
             f"现网:{d.get('exp_side') or '—'} 说明:{d.get('note') or ''}"
             for d in report.get('diffs', [])]
    wl = [f"[{w.get('heuristic')}] {w.get('cmd')} {w.get('param','')}={w.get('value','')} "
          f"（L{w.get('seq','?')}）"
          for w in report.get('watchlist', [])]
    top = '；'.join(f"{x['type']}({x['n']})"
                    for x in report.get('stats', {}).get('top_cmd_types', [])[:5])
    # ★ 局点信息一律从 report 取（此前硬编码「102275 条命令」，
    #   换局点后数字失真且会被模型当事实）；缺字段则中性表述。
    #   实测字段位置：meta.ne_name / stats.cmd_count
    meta = report.get('meta') or {}
    stats = report.get('stats') or {}
    ne = meta.get('ne_name') or '未知网元'
    n_cmd = stats.get('cmd_count') or ''
    scope = f'{ne}（{n_cmd} 条命令）' if n_cmd else str(ne)
    return f"""你是核心网 UDG/UPF 领域的配置分析专家。以下是局点 {scope} 的 EXP 经确定性代码管线（P1）提取的结构化事实，请做三段语义润色。

【功能链判定】
{chr(10).join('  ' + s for s in chains)}

【现网 vs 标准差异】
{chr(10).join('  ' + s for s in diffs) or '  （无）'}

【待审视候选】
{chr(10).join('  ' + s for s in wl) or '  （无）'}

【命令族 Top】{top}

要求输出严格 JSON（不要 markdown 代码块、不要多余文字），结构：
{{
  "conclusion": "一段话业务定性（<200字）：本局点是什么定位、核心能力在哪、有无明显缺口",
  "diff_review": ["逐条差异给语义判断，格式「链X｜类别｜等价/缺口/需审视｜一句话理由」"],
  "watchlist_meaning": ["逐条待审视给业务含义与建议动作，格式「heuristic｜含义｜建议」"]
}}
只输出 JSON 本体。"""


def _extract_json(text):
    """从模型输出里取 JSON。

    ★ 健壮化（2026-09-18）：旧实现用贪婪 `re.search(r'{.*}')` 抓第一个 { 到
      最后一个 }，遇 markdown 代码块或多段 JSON 会把内容连起来 → loads 失败。
      现在先剥 ```json 围栏，再按大括号配平扫描取第一个完整对象。
    """
    t = text.strip()
    # 剥 markdown 代码围栏
    m = re.search(r'```(?:json)?\s*(.*?)```', t, re.S)
    if m:
        t = m.group(1).strip()
    # 按大括号配平找第一个完整 JSON 对象（跳过字符串内的括号）
    start = t.find('{')
    if start < 0:
        raise ValueError('no json in llm output')
    depth, in_str, esc = 0, False, False
    for i in range(start, len(t)):
        ch = t[i]
        if in_str:
            if esc:
                esc = False
            elif ch == '\\':
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return json.loads(t[start:i + 1])
    raise ValueError('unbalanced json in llm output')


def polish(report, timeout=TIMEOUT):
    """润色入口。返回 {'status','reason','model',...}；成功时含三段内容。

    ★ 显式成败（2026-09-18 改）：此前失败静默返回 None，报告里只有 'llm': None，
      跑一万次没人知道它一直在失败。现固定返回带 status 的结构，
      由调用方决定如何呈现 —— 与「UI 只呈现明确成败」的口径一致。

    status ∈ {'ok','no_requests','no_key','error'}
    """
    if requests is None:
        return {'status': 'no_requests',
                'reason': '环境无 requests 模块（精简容器）'}
    key = _load_key()
    if not key:
        return {'status': 'no_key', 'reason': '未找到 DEEPSEEK_API_KEY'}
    try:
        r = requests.post(
            f'{BASE_URL}/chat/completions',
            headers={'Authorization': f'Bearer {key}',
                     'Content-Type': 'application/json'},
            json={'model': MODEL,
                  'messages': [{'role': 'user', 'content': _build_prompt(report)}],
                  'temperature': 0.2, 'max_tokens': 8000},
            timeout=timeout)
        r.raise_for_status()
        content = r.json()['choices'][0]['message']['content']
        out = _extract_json(content)
        out['status'] = 'ok'
        out['model'] = MODEL
        return out
    except Exception as e:
        print(f'[llm_polish] 失败（{type(e).__name__}: {e}）')
        return {'status': 'error', 'model': MODEL,
                'reason': f'{type(e).__name__}: {e}'}


if __name__ == '__main__':
    import sys
    rp = sys.argv[1] if len(sys.argv) > 1 else '/tmp/ac_t7final/report.json'
    report = json.load(open(rp, encoding='utf-8'))
    t0 = time.time()
    out = polish(report)
    if out.get('status') != 'ok':
        print(f"FAIL [{out.get('status')}] {out.get('reason')}")
        raise SystemExit(1)
    print(f"OK {time.time() - t0:.1f}s  model={out.get('model')}")
    print(json.dumps({k: v for k, v in out.items() if k != 'status'},
                     ensure_ascii=False, indent=1))
