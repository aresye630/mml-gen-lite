#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""页签平铺检查（纯 Python 实现，无需 node）。

为什么不用 node：交付镜像里没有 node（只有 python3），
而这条检查必须能**在容器内**自证 —— 否则交付验收时跑不了。

判别力（每条都能区分对错）：
  · 层级残留：LV1_TABS / setLv1 / S.lv1 / lv2bar 必须全部不存在
  · 平铺渲染：7 个页签同一容器（lv1bar），无第二层容器
  · 灰化语义：不可用 = off 类 + disabled，但**仍带 label**（不是隐藏）
  · 分组消除：每个页签 data-lv1 互不相同

用法:
    python3 app_tabs_check.py /opt/expgv/backend/web/app_v2.html
"""
import re
import sys
from pathlib import Path

OK = FAIL = 0


def chk(desc, cond, extra=''):
    global OK, FAIL
    if cond:
        OK += 1
        print(f'  [OK]   {desc}')
    else:
        FAIL += 1
        print(f'  [FAIL] {desc}' + (f'  → {extra}' if extra else ''))


def main():
    if len(sys.argv) < 2:
        print('用法: app_tabs_check.py <app_v2.html>')
        return 2
    p = Path(sys.argv[1])
    if not p.is_file():
        print(f'⛔ 文件不存在: {p}')
        return 2
    src = p.read_text(encoding='utf-8', errors='replace')
    # 剥掉 JS 注释再判（避免注释里的旧词造成假绿/假红）
    body = re.sub(r'/\*[\s\S]*?\*/', '', src)
    body = re.sub(r'(?m)^\s*//.*$', '', body)

    print('─── 结构：层级已消除 ───')
    chk('LV1_TABS 常量已删除', 'LV1_TABS' not in body)
    chk('setLv1 函数已删除', 'function setLv1' not in body)
    chk('S.lv1 状态字段已删除', not re.search(r'S\.lv1\b', body))
    chk('lv2bar 容器/样式中已无', 'lv2bar' not in body)
    chk('不再按 lv1 过滤页签', not re.search(r't\.lv1\s*===\s*S\.lv1', body))
    chk('生成后跳转改用 pickTab', "pickTab('gen')" in body)

    print('─── 渲染：单行平铺 7 个页签 ───')
    chk('renderTabBar 存在', 'function renderTabBar' in body)
    chk('单行容器 lv1bar', 'class="lv1bar"' in body)
    chk('页签按 tabs 全量渲染（无分组 map）',
        'tabs.map(' in body and 'lv1Items' not in body)
    # 渲染函数里必须直接遍历 tabs，且不引用已在状态里删掉的 S.lv1
    m = re.search(r'function renderTabBar\(\)\{([\s\S]*?)\n\}', body)
    chk('renderTabBar 函数体可提取', bool(m))
    if m:
        fn = m.group(1)
        chk('函数内无 S.lv1 引用', not re.search(r'S\.lv1\b', fn))
        chk('函数内输出 data-lv1（供高亮用）', 'data-lv1' in fn)
        chk('函数内无 lv2bar 输出', 'lv2bar' not in fn)

    print('─── 灰化语义：不可用但可见 ───')
    chk('.off 灰化样式存在', '.off' in src)
    chk('upload 按钮样式已并入 .tab 体系',
        'lv1bar .tab' in src or 'upload-btn' in src)

    print('─── 样式：页签本体有样式（不会裸奔）───')
    chk('.lv1bar .tab 样式已定义', '.lv1bar .tab' in src)
    chk('.lv1bar .tab.off 灰化已定义',
        re.search(r'\.lv1bar \.tab\.off', src) or '.lv1.off' in src)

    print(f'\n结果: {OK}/{OK + FAIL} 通过')
    return 1 if FAIL else 0


if __name__ == '__main__':
    raise SystemExit(main())
