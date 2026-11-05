#!/usr/bin/env python3
"""构建命令说明索引：扫描各产品 MML 指令文档 → rules/cmd_doc_index_<产品>.yaml

索引内容（轻量，按需再解析参数表）：
  cmds:
    ADD RULE:
      path: output_ueg_mml/output_ueg_mml/MML/Document/add_rule.md
      name: 增加规则          # 标题中文名
      func: 该命令用于…      # #### 命令功能 段落（精简 120 字）

用法:
  python3 build_cmd_doc_index.py [--products UEG,UDG,UNC]
"""
import argparse
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = Path(__file__).resolve().parent.parent
RULES = ROOT / 'rules'

PRODUCT_MML = {
    'UEG': Path.home() / 'workspace/zhijian/output_ueg_mml',
    'UDG': Path.home() / 'workspace/zhijian/output_udg_mml',
    'UNC': Path.home() / 'workspace/zhijian/output_unc_mml',
}

TITLE_RE = re.compile(r'#\s+(.+?)[（(]([A-Z]+ [A-Z0-9_]+)[)）]')
FUNC_RE = re.compile(r'####\s*命令功能\s*\n(.*?)(?:\n####|\Z)', re.S)


def parse_head(md_text: str):
    """从文档头部提取 命令名（标题括号内英文）、中文名、功能句"""
    title_m = TITLE_RE.search(md_text[:600])
    if title_m:
        name_cn, cmd = title_m.group(1).strip(), title_m.group(2).strip()
    else:
        cmd, name_cn = '', ''
    func = ''
    fm = FUNC_RE.search(md_text)
    if fm:
        seg = fm.group(1).strip()
        # 去掉"适用NF"行，取第一段
        lines = [l for l in seg.split('\n') if l.strip() and not l.strip().startswith('**适用')]
        if lines:
            func = lines[0].strip()
    return cmd, name_cn, func[:120]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--products', default='UEG,UDG,UNC')
    args = ap.parse_args()

    import yaml
    for prod in args.products.split(','):
        mml_root = PRODUCT_MML.get(prod)
        if not mml_root or not mml_root.exists():
            print(f'✗ {prod}: 目录不存在 {mml_root}')
            continue
        t0 = time.time()
        docs = sorted(mml_root.rglob('*.md'))
        cmds = {}
        dup = 0
        for p in docs:
            try:
                head = p.read_text(encoding='utf-8-sig', errors='replace')[:2000]
            except Exception:
                continue
            cmd, name_cn, func = parse_head(head)
            if not cmd:
                continue
            if cmd in cmds:   # 多版本目录重复 → 保留第一条
                dup += 1
                continue
            rel = str(p.relative_to(Path.home())) if str(p).startswith(str(Path.home())) else str(p)
            cmds[cmd] = {'path': rel, 'name': name_cn, 'func': func}
        out = RULES / f'cmd_doc_index_{prod.lower()}.yaml'
        out.write_text(yaml.safe_dump({'cmds': cmds}, allow_unicode=True,
                                      sort_keys=True), encoding='utf-8')
        print(f'✅ {prod}: {len(cmds)} 条命令（重复 {dup}）→ {out}  [{time.time()-t0:.0f}s]')


if __name__ == '__main__':
    main()
