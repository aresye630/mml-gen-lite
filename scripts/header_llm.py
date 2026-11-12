"""用 LLM 生成表头的自然语言描述（含多样性）。

★ 2026-11-12（用户要求）
  「这里很多都需要 llm 来做（描述多样性）」

## 为什么要 LLM

  语素推导能覆盖 98% 的参数，但质量不稳：
    INTELSHUNT  → 智能旁路      ❌ 实际是「智能分流关键字」
    SUBNETMASK  → 掩码长度      ⚠ 应该是「掩码」
  而且所有清单都用同一个说法，agent 容易学到「词 → 参数」的硬映射。

## LLM 做什么

  输入：参数名 + 所属命令族 + 该族的命令样例（提供上下文）
  输出：多种中文描述（3-4 个等价说法）

  例：INTELSHUNT（ADD APNINTELSHUNT，配置 APN 智能分流）
      → ["智能分流关键字", "分流关键词", "智能分流标识"]

## 缓存策略

  · 按 (参数名, 族名) 缓存，跨工单复用
  · 缓存文件 /tmp/header_llm_cache.json
  · 只在缓存未命中时调 LLM

## 成本

  实测 195 个引号参数 × 1 次调用 ≈ 195 次
  批量处理（一次问 20 个参数）→ 10 次调用
"""
import json
import re
import urllib.request
from pathlib import Path

CACHE_PATH = Path('/tmp/header_llm_cache.json')
API_KEY = 'sk-841a236695af4c6db5086dfc56d815ca'
API_URL = 'https://api.deepseek.com/v1/chat/completions'
MODEL = 'deepseek-chat'

BATCH_SIZE = 15          # 每次问多少个参数
MAX_RETRY = 3


def _load_cache():
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text(encoding='utf-8'))
        except Exception:
            return {}
    return {}


def _save_cache(cache):
    try:
        CACHE_PATH.write_text(
            json.dumps(cache, ensure_ascii=False, indent=1), encoding='utf-8')
    except Exception:
        pass


def _call_llm(prompt, max_tokens=1500):
    """调 DeepSeek API。"""
    body = json.dumps({
        'model': MODEL,
        'messages': [
            {'role': 'system',
             'content': (
                 '你是 5G 核心网（UDG/UNC/UEG）配置专家。'
                 '任务：把 MML 参数名翻译成运维人员能看懂的中文业务描述。'
                 '\n\n要求：'
                 '\n1. 每个参数给 3 个等价说法（同一个意思的不同表达，供随机选用，让界面文案有变化）'
                 '\n2. 每个说法不超过 10 个汉字'
                 '\n3. 不要出现英文参数名（APN/DNN/VRF 这类通用缩写可以保留）'
                 '\n4. 结合所属命令的业务含义来判断，不要只看字面'
                 '\n5. 只输出 JSON，不要解释'
                 '\n\n输出格式：{"参数名": ["说法1", "说法2", "说法3"], ...}'
             )},
            {'role': 'user', 'content': prompt},
        ],
        'max_tokens': max_tokens,
        'temperature': 0.3,
        'response_format': {'type': 'json_object'},
    }).encode()

    req = urllib.request.Request(
        API_URL, data=body,
        headers={'Content-Type': 'application/json',
                 'Authorization': f'Bearer {API_KEY}'})

    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
        return data['choices'][0]['message']['content']


def _parse_json_response(text):
    """解析 LLM 返回的 JSON（容错）。"""
    text = text.strip()
    # 去掉 markdown 代码块
    if text.startswith('```'):
        text = re.sub(r'^```\w*\n?', '', text)
        text = re.sub(r'\n?```$', '', text)
    try:
        return json.loads(text)
    except Exception:
        # 尝试提取第一个 {...}
        m = re.search(r'\{[\s\S]*\}', text)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                pass
    return {}


def build_prompt(params_with_context):
    """构建批量提示。

    params_with_context: [{'param': 'INTELSHUNT', 'family': 'APNINTELSHUNT',
                           'sample': 'ADD APNINTELSHUNT: APN="cmnet", INTELSHUNT="multidomain";'}]
    """
    lines = ['为下列 MML 参数生成中文业务描述（每个 3 个等价说法）：\n']
    for i, p in enumerate(params_with_context, 1):
        lines.append(f'{i}. 参数 {p["param"]}（命令族 {p["family"]}）')
        if p.get('sample'):
            lines.append(f'   命令样例：{p["sample"][:150]}')
    lines.append('\n输出 JSON，key 是参数名，value 是 3 个中文说法的数组。')
    return '\n'.join(lines)


def generate_headers_batch(params_with_context):
    """批量生成表头，返回 {参数名: [说法1, 说法2, 说法3]}。"""
    prompt = build_prompt(params_with_context)
    for attempt in range(MAX_RETRY):
        try:
            resp = _call_llm(prompt)
            data = _parse_json_response(resp)
            if data:
                return data
        except Exception as e:
            if attempt == MAX_RETRY - 1:
                print(f'  ⚠ LLM 调用失败: {e}')
    return {}


def generate_missing_headers(all_params, verbose=True):
    """为所有缺表头的参数生成描述（批量 + 缓存）。

    all_params: [{'param': ..., 'family': ..., 'sample': ...}]
    返回：更新后的缓存
    """
    cache = _load_cache()
    # 找出缓存里没有的
    missing = [p for p in all_params if p['param'].upper() not in cache]
    if not missing:
        return cache

    # 去重（同参数只问一次）
    seen = set()
    uniq = []
    for p in missing:
        k = p['param'].upper()
        if k in seen:
            continue
        seen.add(k)
        uniq.append(p)

    if verbose:
        print(f'  需 LLM 生成的参数: {len(uniq)} 个')

    n_ok = 0
    for i in range(0, len(uniq), BATCH_SIZE):
        batch = uniq[i:i + BATCH_SIZE]
        if verbose:
            print(f'    批次 {i//BATCH_SIZE + 1}: {len(batch)} 个')
        result = generate_headers_batch(batch)
        for pname, variants in result.items():
            if isinstance(variants, list) and variants:
                cache[pname.upper()] = [str(v) for v in variants if v][:5]
                n_ok += 1
            elif isinstance(variants, str) and variants:
                cache[pname.upper()] = [variants]
                n_ok += 1
        _save_cache(cache)

    if verbose:
        print(f'  ✅ 生成成功 {n_ok}/{len(uniq)}')
    return cache


def get_header(pname, seed=None):
    """从缓存里取表头，用 seed（如对象名）稳定选择变体。"""
    cache = _load_cache()
    variants = cache.get(pname.upper())
    if not variants:
        return None
    if isinstance(variants, str):
        return variants
    if not variants:
        return None
    if seed is None:
        return variants[0]
    import hashlib
    h = int(hashlib.md5(str(seed).encode()).hexdigest()[:8], 16)
    return variants[h % len(variants)]


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    import header_naming as HN

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    # 收集所有引号值参数 + 上下文
    need = {}
    for g in GT:
        if not g['kept']:
            continue
        for _, v, fam, params, raw in g['kept']:
            for pname in params:
                m = re.search(rf'\b{re.escape(pname)}\s*=\s*("?[^",;]+"?)', raw)
                if not (m and m.group(1).startswith('"')):
                    continue
                k = pname.upper()
                if k in need:
                    continue
                need[k] = {'param': k, 'family': fam, 'sample': raw}

    print('=' * 90)
    print(f'LLM 表头生成（引号值参数 {len(need)} 个）')
    print('=' * 90)

    # 只处理前三档失败的，加上质量可疑的
    SUSPECT = ['INTELSHUNT', 'SUBNETMASK', 'AGGREADDRESSV6', 'SQN',
               'AUTHTEXTMD5', 'KI', 'SD', 'GREKEY', 'PARAVALUE', 'PASSWORD']
    todo = [v for k, v in need.items()
            if k in SUSPECT or not HN.header_for(k)]

    print(f'\n需要 LLM 的参数: {len(todo)} 个')
    for p in todo[:15]:
        print(f'  {p["param"]:<24} ({p["family"]})')

    cache = generate_missing_headers(todo)

    print(f'\n{"=" * 90}')
    print('生成结果')
    print(f'{"=" * 90}')
    for p in todo[:20]:
        k = p['param']
        v = cache.get(k)
        if v:
            print(f'  {k:<24} → {v}')
        else:
            print(f'  {k:<24} → ❌ 未生成')
