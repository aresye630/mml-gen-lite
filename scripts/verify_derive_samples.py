#!/usr/bin/env python3
"""样例验证：两个版本意图各跑一遍完整链路（含阶段3 Step3.5 派生）。

★ 2026-11-12（用户要求）
  「派生补全接入，记得所有容器都改；同步考虑意图的删减版...
    然后再跑样例验证链路，两个版本的意图都要跑」

## 验证内容

  版本 A：完整版意图（/tmp/intent_v5）
  版本 B：删减版意图（/tmp/intent_v5_slim）

  每个版本跑：
    · 上传 EXP + 意图 + 数据清单
    · 阶段1（规划）
    · 阶段2（params.csv + mml.txt）
    · 阶段3（含新增的 Step 3.5 派生补全）

## 判据

  1. 阶段1/2 是否跑通（产物存在）
  2. Step 3.5 是否触发（删减版应该更常触发，因为数据少）
  3. 派生补全是否生成了 POOLGROUP 等下游族
  4. 两个版本对比：族覆盖、派生行数
"""
import json
import subprocess
import sys
import time
from pathlib import Path

PROJ = Path('/Users/alesc/workspace/mml-gen-lite')
GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

VERSIONS = {
    'full': Path('/tmp/intent_v5'),
    'slim': Path('/tmp/intent_v5_slim'),
}

BASES = ['http://127.0.0.1:8620', 'http://127.0.0.1:8621',
         'http://127.0.0.1:8622', 'http://127.0.0.1:8623']
CONT = {'8620': 'mmlgen-clean', '8621': 'mmlgen-b1',
        '8622': 'mmlgen-b2', '8623': 'mmlgen-b3'}

OUT = Path('/tmp/eval_full_v16')


def api_get(base, path, timeout=120):
    """GET 请求（带 1 次重试）。"""
    import urllib.request
    last = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(base + path, timeout=timeout) as r:
                return json.loads(r.read())
        except Exception as e:
            last = e
            if attempt == 0:
                import time as _t
                _t.sleep(2)
    raise last


def api_post(base, path, payload, timeout=120):
    import urllib.request
    req = urllib.request.Request(
        base + path, data=json.dumps(payload).encode(),
        headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read())


def upload_via_api(base, sid, file_path):
    """用 /api/v1/sessions/{sid}/files 上传（POST multipart 或原始）。"""
    import urllib.request
    import uuid
    fp = Path(file_path)
    data = fp.read_bytes()
    boundary = uuid.uuid4().hex
    body = (
        f'--{boundary}\r\n'
        f'Content-Disposition: form-data; name="files"; filename="{fp.name}"\r\n'
        f'Content-Type: application/octet-stream\r\n\r\n'
    ).encode() + data + f'\r\n--{boundary}--\r\n'.encode()
    req = urllib.request.Request(
        base + f'/api/v1/sessions/{sid}/files', data=body,
        headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
    with urllib.request.urlopen(req, timeout=300) as r:
        return json.loads(r.read())


def run_once(base, cont, tk, version):
    """跑一个工单的一个版本：上传 → plan → fill（阶段3 自动跟在 fill 后）。"""
    g = GT_MAP.get(tk)
    if not g:
        return {'ticket': tk, 'version': version, 'error': 'not in GT'}

    adir = Path(g['path']) / '备份附件'
    exps = sorted(adir.glob('*.txt')) if adir.exists() else []
    src = VERSIONS[version]
    intent_p = src / f'{tk}_意图.md'
    ds_p = src / f'{tk}_数据清单.md'

    t0 = time.time()
    try:
        # 建会话
        r = api_post(base, '/api/v1/sessions',
                     {'name': f'{tk}_{version}', 'product': 'UDG'})
        sid = r.get('session_id') or r.get('sid')

        # 上传 EXP + 意图 + 清单
        files = list(exps)
        if intent_p.exists():
            files.append(intent_p)
        if ds_p.exists():
            files.append(ds_p)
        n_up = 0
        for f in files:
            try:
                upload_via_api(base, sid, f)
                n_up += 1
            except Exception as e:
                return {'ticket': tk, 'version': version,
                        'error': f'上传失败 {Path(f).name}: {e}',
                        'elapsed': round(time.time()-t0, 1)}

        # 校验上传
        fl = api_get(base, f'/api/v1/sessions/{sid}/files')
        n_files = len(fl.get('files') or [])
        if n_files < len(files):
            return {'ticket': tk, 'version': version,
                    'error': f'上传不完整 {n_files}/{len(files)}',
                    'elapsed': round(time.time()-t0, 1)}

        intent_text = intent_p.read_text(encoding='utf-8') if intent_p.exists() else ''

        # 阶段1
        api_post(base, f'/api/v1/sessions/{sid}/run',
                 {'intent': intent_text, 'stage': 'plan', 'product': 'UDG'})
        s1 = wait_done(base, sid, timeout=1800)
        if s1.get('status') != 'done':
            return {'ticket': tk, 'version': version, 'sid': sid,
                    's1_status': s1.get('status'),
                    'error': f'阶段1 {s1.get("status")}: {(s1.get("last_run") or {}).get("error")}',
                    'elapsed': round(time.time()-t0, 1)}

        # 阶段2（阶段3 自动跟跑）
        api_post(base, f'/api/v1/sessions/{sid}/run',
                 {'intent': intent_text, 'stage': 'fill', 'product': 'UDG'})
        s2 = wait_done(base, sid, timeout=2400)
        lr = s2.get('last_run') or {}

        return {
            'ticket': tk, 'version': version, 'sid': sid,
            'elapsed': round(time.time()-t0, 1),
            's1_status': s1.get('status'),
            's2_status': s2.get('status'),
            's3': lr.get('stage3'),
        }
    except Exception as e:
        return {'ticket': tk, 'version': version,
                'error': str(e)[:300], 'elapsed': round(time.time()-t0, 1)}


def wait_done(base, sid, timeout=1800, poll=10):
    """等 run 结束（status != running）。

    ★ 2026-11-12 修：原来单次 api_get 失败就抛异常，
      实测第 10 单跑了 1082s 后连接被拒 → 整个用例失败 →
      后续 4 单连锁失败（0.0s）。

      现在：连接失败时重试 3 次（各等 5s），仍失败才算错。
    """
    t0 = time.time()
    consecutive_err = 0
    while time.time() - t0 < timeout:
        time.sleep(poll)
        try:
            st = api_get(base, f'/api/v1/sessions/{sid}/run', timeout=30)
            consecutive_err = 0
            if st.get('status') != 'running':
                return st
        except Exception as e:
            consecutive_err += 1
            if consecutive_err >= 3:
                return {'status': 'conn_error', 'error': str(e)[:200]}
            time.sleep(5)
    return {'status': 'timeout'}


def load_eval_tickets(all_tickets=None, include_excluded=False):
    """加载测试集工单，按 rules/eval_ticket_tags.json 的标签过滤。

    ★ 2026-11-13（用户裁定）
      「这些概率失败的大单暂时不跑，从测试集剔除（打上标签即可，不用删除）」

      剔除规则：n_exp >= 2 且 n_cmd >= 200（多网元大单）
      实测依据：多网元大单失败率 64%，单网元大单 17%

    标签文件：rules/eval_ticket_tags.json
      excluded[]  —— 剔除的单（含 baseline_status / n_exp / n_cmd / tags）
      kept[]      —— 保留的单

    返回：(tickets, meta)
    """
    import json as _json
    tag_file = Path(__file__).resolve().parent.parent / 'rules' / 'eval_ticket_tags.json'
    meta = {'excluded': [], 'source': 'all'}
    if not tag_file.exists():
        return (all_tickets or []), meta

    tags = _json.loads(tag_file.read_text(encoding='utf-8'))
    excluded = {x['ticket'] for x in tags.get('excluded', [])}
    meta['excluded'] = sorted(excluded)

    pool = all_tickets or [x['ticket'] for x in tags.get('kept', [])]
    if include_excluded:
        return pool, meta

    kept = [t for t in pool if t not in excluded]
    meta['source'] = 'tags'
    return kept, meta


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    import json as _json
    import os as _os

    # ★ 2026-11-13：默认跑全量（按标签过滤掉多网元大单）
    #   TICKETS_JSON=<path>  指定工单清单
    #   INCLUDE_EXCLUDED=1   包含被剔除的单（调试用）
    _tk_file = _os.environ.get('TICKETS_JSON', '/tmp/full_v5_tickets.json')
    _all = _json.loads(Path(_tk_file).read_text(encoding='utf-8'))
    TICKETS, _meta = load_eval_tickets(
        _all, include_excluded=bool(_os.environ.get('INCLUDE_EXCLUDED')))

    print('=' * 100)
    print(f'评测：{len(TICKETS)} 单（已剔除 {len(_meta["excluded"])} 个多网元大单）')
    if _meta['excluded']:
        print(f'  剔除: {", ".join(_meta["excluded"][:5])}'
              f'{" ..." if len(_meta["excluded"]) > 5 else ""}')
    print('=' * 100)

    # ★ 2026-11-12 修：原来串行（i % len(BASES) 但仍是 for 循环顺序执行）
    #   实测 14 单串行 95 分钟，期间 3 个容器闲置
    #   改为 ThreadPoolExecutor 4 并发，每个容器一个槽位
    from concurrent.futures import ThreadPoolExecutor, as_completed
    import threading

    jobs = [('full', tk) for tk in TICKETS]
    results = []
    lock = threading.Lock()
    slot_free = {b: threading.Semaphore(1) for b in BASES}

    def _run_one(job):
        ver, tk = job
        # 抢占一个空闲容器
        import time as _t
        while True:
            for b in BASES:
                if slot_free[b].acquire(blocking=False):
                    try:
                        base = b
                        cont = CONT[base.rsplit(':', 1)[-1]]
                        with lock:
                            print(f'  ▶ {tk} @ {ver}  ({cont})', flush=True)
                        r = run_once(base, cont, tk, ver)
                        with lock:
                            if r.get('error'):
                                print(f'  ❌ {tk}: {r["error"]}  ({r.get("elapsed")}s)',
                                      flush=True)
                            else:
                                s3v = r.get('s3') or {}
                                s3_desc = ('跑了' if s3v.get('ran') else
                                           ('错误' if s3v.get('error') else '跳过'))
                                print(f'  ✅ {tk}: S1={r["s1_status"]} S2={r["s2_status"]} '
                                      f'S3={s3_desc} ({r["elapsed"]}s)', flush=True)
                                if s3v.get('ran'):
                                    steps = s3v.get('steps') or []
                                    print(f'      步骤: {steps}', flush=True)
                        return r
                    finally:
                        slot_free[b].release()
            _t.sleep(2)

    t0 = __import__('time').time()
    with ThreadPoolExecutor(max_workers=4) as ex:
        futs = [ex.submit(_run_one, job) for job in jobs]
        for f in as_completed(futs):
            try:
                results.append(f.result())
            except Exception as e:
                results.append({'error': str(e)[:200]})

    (OUT / 'result.json').write_text(
        json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')

    el = __import__('time').time() - t0
    print(f'\n{"=" * 100}')
    print(f'总计 {len(results)} 单，耗时 {el/60:.0f} 分钟')
    ok = sum(1 for r in results if r.get('s2_status') == 'done')
    print(f'完成 {ok}/{len(results)}')
    print(f'结果: {OUT}/result.json')


if __name__ == '__main__':
    main()
