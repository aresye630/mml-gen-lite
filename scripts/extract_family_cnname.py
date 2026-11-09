#!/usr/bin/env python3
"""从本地 MML 命令库提取「族名 → 中文名」，跨 UDG/UEG/UNC 三个产品。

关键：GT 里的族名可能属于不同网元，必须三个产品都查。
实测：ADD EMGCFG / ADD USRPROFGROUP / SET SOFTPARA 都在 UNC 库里，
     只查 UDG 会全部漏掉。

用法（在容器内执行）：
  python3 extract_family_cnname.py [族名...]
  python3 extract_family_cnname.py --all          # 输出全部映射 JSON
  python3 extract_family_cnname.py --by-product   # 按产品分组输出
"""
import json
import re
import sys
from pathlib import Path

KB_ROOT = Path('/opt/expgv/kb')
PRODUCTS = ['udg', 'ueg', 'unc']

# 标题格式：`# 设置HTR流控全局配置（SET HTTPHTRCFG）`
TITLE_RE = re.compile(
    r'^#\s*(.+?)[（(]\s*(ADD|SET|MOD|RMV|LST|DSP|ACT|DEA|CLR)\s+([A-Z0-9_]+)\s*[)）]')


def build_index():
    """扫三个产品的文档，建 {族名: {产品: 中文名}}。"""
    out = {}
    stats = {}
    for prod in PRODUCTS:
        doc_root = KB_ROOT / f'output_{prod}_mml' / 'mml' / 'MML' / 'Document'
        if not doc_root.exists():
            stats[prod] = 0
            continue
        n = 0
        for p in doc_root.glob('*.md'):
            try:
                with open(p, encoding='utf-8', errors='replace') as f:
                    for _ in range(8):
                        line = f.readline()
                        if not line:
                            break
                        m = TITLE_RE.match(line.strip().lstrip('\ufeff'))
                        if m:
                            cn = m.group(1).strip()
                            fam = m.group(3).upper()
                            out.setdefault(fam, {})[prod] = cn
                            n += 1
                            break
            except Exception:
                continue
        stats[prod] = n
    return out, stats


def main():
    idx, stats = build_index()
    print(f'索引 {len(idx)} 个族（{" ".join(f"{k}:{v}" for k, v in stats.items())}）',
          file=sys.stderr)

    if len(sys.argv) > 1 and sys.argv[1] == '--all':
        print(json.dumps(idx, ensure_ascii=False, indent=1, sort_keys=True))
        return

    if len(sys.argv) > 1 and sys.argv[1] == '--by-product':
        for prod in PRODUCTS:
            fams = sorted(k for k, v in idx.items() if prod in v)
            print(f'=== {prod.upper()}（{len(fams)} 族）===')
            for fam in fams[:20]:
                print(f'  {fam:<28} {idx[fam][prod]}')
            print()
        return

    if len(sys.argv) > 1:
        for fam in sys.argv[1:]:
            hit = idx.get(fam.upper())
            if hit:
                parts = ' | '.join(f'{p}: {c}' for p, c in hit.items())
                print(f'  {fam:<26} → {parts}')
            else:
                print(f'  {fam:<26} → (未找到)')
        return

    print(__doc__)


if __name__ == '__main__':
    main()
