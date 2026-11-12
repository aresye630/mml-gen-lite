#!/usr/bin/env python3
"""用 LLM 生成「命令族 → 中文业务名」映射（数据清单的表名）。

★ 2026-11-12
  问题：SHEET_NAME 只有 23 条、EXTRA_CN 只有 8 条，
        导致 201 个族里大部分表名是英文（URRGROUP / RULE / USERPROFILE）
  后果：删减脚本按中文表名匹配时匹配不到，删表失效

  解决：用 LLM 批量生成，缓存到 header_llm_cache.json（key = FAMILY::<族名>）

  与参数表头类似：每个族给 2-3 个中文叫法，表名随机选一个。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import header_llm as HL

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

BATCH = 12


def collect_families():
    """收集所有族名 + 最好的样例命令。"""
    fams = {}
    for g in GT:
        if not g['kept']:
            continue
        for _, v, fam, params, raw in g['kept']:
            if fam not in fams:
                fams[fam] = raw[:220]
            elif len(raw) > len(fams[fam]) and len(raw) < 250:
                fams[fam] = raw[:220]
    return fams


def build_prompt(batch_items):
    lines = ['为下列 MML 命令族生成中文业务名（每个族给 2 个说法，用作表名）：\n']
    for i, (fam, sample) in enumerate(batch_items, 1):
        lines.append(f'{i}. 命令族 {fam}')
        lines.append(f'   样例：{sample}')
    lines.append('\n输出 JSON，key 是族名，value 是 2 个中文名称的数组。')
    lines.append('要求：')
    lines.append('  · 每个名称 2-10 个汉字')
    lines.append('  · 不要带「配置」「信息」这类空泛后缀（除非确实是）')
    lines.append('  · 结合样例命令的业务含义，不要只看族名字面')
    return '\n'.join(lines)


def main():
    fams = collect_families()
    print('=' * 96)
    print(f'LLM 生成族名中文名（{len(fams)} 个族）')
    print('=' * 96)

    cache = HL._load_cache()
    todo = [(f, s) for f, s in fams.items() if f'FAMILY::{f}' not in cache]
    print(f'\n已有缓存: {len(fams) - len(todo)}')
    print(f'待生成: {len(todo)}')

    if not todo:
        print('\n✅ 全部已缓存')
    else:
        n_ok = 0
        for i in range(0, len(todo), BATCH):
            batch = todo[i:i + BATCH]
            print(f'  批次 {i//BATCH + 1}: {len(batch)} 个族')
            prompt = build_prompt(batch)
            try:
                resp = HL._call_llm(prompt, max_tokens=1200)
                data = HL._parse_json_response(resp)
                for fam, names in data.items():
                    key = f'FAMILY::{fam.upper()}'
                    if isinstance(names, list) and names:
                        cache[key] = [str(n) for n in names if n][:4]
                        n_ok += 1
                    elif isinstance(names, str) and names:
                        cache[key] = [names]
                        n_ok += 1
                HL._save_cache(cache)
            except Exception as e:
                print(f'    ⚠ 失败: {e}')
        print(f'  ✅ 生成 {n_ok}/{len(todo)}')

    # 验收
    print(f'\n{"=" * 96}')
    print('验收')
    print(f'{"=" * 96}')
    have = sum(1 for f in fams if f'FAMILY::{f}' in cache)
    print(f'  覆盖: {have}/{len(fams)} ({have/len(fams)*100:.0f}%)')

    print(f'\n=== 抽样（重点看之前表名是英文的族）===')
    SAMPLES = ['URRGROUP', 'RULE', 'USERPROFILE', 'FLOWFILTER', 'PCCPOLICYGRP',
               'RULEBINDING', 'URRGRPBINDING', 'UPBINDUPG', 'USRPROFGROUP',
               'POOLGROUP', 'POOLGRPMAP', 'APNCHARGECTRL', 'IPFARM',
               'HPLMN', 'CONNECTPLMN', 'LICENSESWITCH', 'DBPARAS']
    for f in SAMPLES:
        v = cache.get(f'FAMILY::{f}')
        print(f'  {f:<20} → {v}')

    missing = [f for f in fams if f'FAMILY::{f}' not in cache]
    if missing:
        print(f'\n仍未生成（{len(missing)} 个）: {missing[:10]}')


if __name__ == '__main__':
    main()
