#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""意图定位预检查 —— 生成前跑一次，把「该走哪条检索路线」变成确定性结论。

为什么需要它（实测驱动）：
  现状：agent 任务书里写「业务口语/组合需求在特性标题语义检索可能系统性低分
        —— 不要只依赖语义检索，按盲点兜底路线 grep 命令名定位源文档」
        ⇒ 这是**保险起见都走兜底**的指导
  实测后果：直播业务那次语义检索 top1 = 1.0000（逐字命中），
           agent 却判定"语义检索低分"直接跳过 → 白走一趟兜底。
  ⇒ 改成**分档指导**：判据说清晰就直达，说不清晰才走兜底。

判据来源：intent_judge.py（★ 唯一真相源，本文件只做渲染）
  · 判据实现（LCS 双门限）抽到 materials/scripts/intent_judge.py
  · 构建期验证在 tools/intent_locate.py（import 同一份）
  → 消除双实现：判据只有一份，渲染/验证各自消费

用法（运行期，容器内）:
  python3 intent_precheck.py --intent "配置ULCL分流的双域专网" --product UEG
  python3 intent_precheck.py --intent "..." --product UEG --json
"""
import argparse
import argparse as _ap
import json
import re
import sys
from pathlib import Path

# ── 判据唯一真相源（同目录的 intent_judge.py）──
sys.path.insert(0, str(Path(__file__).resolve().parent))
from intent_judge import (          # noqa: E402
    MILVUS_URI, locate, load_titles, norm,
)

def feature_path(match, product, uri=MILVUS_URI):
    """定位特性的文档路径（供 agent 直达）"""
    try:
        import pymilvus
        c = pymilvus.MilvusClient(uri=uri)
        c.load_collection('mml_feature')
        r = c.query('mml_feature',
                    filter=f'feature_name == "{match}"',
                    output_fields=['file_path', 'full_nav'], limit=1)
        if r:
            return r[0].get('file_path', ''), r[0].get('full_nav', '')
    except Exception:
        pass
    return '', ''


def render_block(res, product):
    """判据结果 → 任务书段落（人话，分档指导）"""
    v = res['verdict']
    if v == 'strong':
        path, nav = feature_path(res['match'], product)
        L, R = res['L'], res['R']
        return (
            '\n【意图定位（代码已完成，确定性判据）】\n'
            f'- 判据档位：strong（最长连续公共子串 L={L}，稀有度 R={R} → 定位明确）\n'
            f'- 目标特性：{res["match"]}\n'
            + (f'- 文档路径：{path}\n' if path else '')
            + (f'- 导航位置：{nav}\n' if nav else '')
            + '- ★ 直接按此特性生成，**无需**再做语义检索探索。\n'
              '  但若你读取该文档后发现与用户意图不符，可自行另选，并在'
              '「检索与选型」中说明推翻理由。\n'
        )
    if v == 'weak':
        return (
            '\n【意图定位（代码已完成，确定性判据）】\n'
            f'- 判据档位：weak（L={res["L"]}，R={res["R"]} → 有弱信号，不足以定位）\n'
            f'- 参考候选：{res["match"]}（**仅供参照，不保证是目标**）\n'
            '- ★ 请自行检索判断：优先语义检索，再由你从候选中做语义选择。\n'
        )
    if v == 'none':
        return (
            '\n【意图定位（代码已完成，确定性判据）】\n'
            '- 判据档位：none（无明确命中）\n'
            '- ★ 请自行检索判断：先试语义检索，若候选不贴切，'
            '按盲点兜底路线（grep 命令名/配置实例关键词）定位源文档。\n'
        )
    if v == 'out_of_scope':
        return (
            '\n【意图定位（代码已完成，确定性判据）】\n'
            '- 判据档位：out_of_scope（意图与特性名无 ≥2 字连续重叠）\n'
            '- ★ 可能超出知识库范围，或用户用了业务口语。请先尝试：\n'
            '  1. 把口语意图转成配置域术语（如"开通微信直播" → 相关业务/APN 配置）\n'
            '  2. 语义检索获取最接近的候选\n'
            '  3. 仍无对应特性 → 写入「待澄清点」，不要硬编。\n'
        )
    return '\n【意图定位】代码判据不可用，请按常规流程自行检索。\n'


def _selftest():
    """自证：用合成特性名证明判据分档正确（不依赖容器/Milvus）"""
    ok, fails = 0, []

    def chk(c, n):
        nonlocal ok
        if c:
            ok += 1
        else:
            fails.append(n)

    T = ['配置直播业务的安全认证策略',
         '配置“ULCL UPF+辅锚点UPF双主负荷分担模式”',
         '激活支持网络切片模式下发',
         '配置VoLTE用户修改为2/3/4G用户']

    chk(locate('配置ULCL分流的双域专网', T)['verdict'] == 'strong', '1: ULCL→strong')
    chk(locate('配置直播业务的安全认证策略', T)['verdict'] == 'strong', '2: 直播→strong')
    chk(locate('开通微信直播', T)['verdict'] != 'strong', '3: 口语→非strong')
    chk(locate('今天天气不错', T)['verdict'] == 'out_of_scope', '4: 无关→out_of_scope')
    chk(locate('配置手机上网', T)['verdict'] != 'strong', '5: 停用词不误判')
    chk(locate('x', [])['verdict'] == 'no_titles', '6: 空库不崩')

    # 渲染分档：strong 含"无需探索"，none 含"自行检索"
    b1 = render_block(locate('配置ULCL分流的双域专网', T), 'UEG')
    chk('无需' in b1 and 'ULCL' in b1, '7: strong 渲染含直达指引')
    b2 = render_block({'verdict': 'none', 'L': 3, 'R': 5, 'match': '', 'sub': ''}, 'UEG')
    chk('自行检索' in b2, '8: none 渲染含自行检索指引')
    b3 = render_block({'verdict': 'out_of_scope', 'L': 0, 'R': -1, 'match': '', 'sub': ''}, 'UEG')
    chk('待澄清' in b3, '9: out_of_scope 渲染含待澄清指引')
    b4 = render_block({'verdict': 'no_titles', 'L': 0, 'R': -1, 'match': '', 'sub': ''}, 'UEG')
    chk('常规流程' in b4, '10: no_titles 降级不阻塞')

    print(f'intent_precheck --selftest: {ok}/{ok+len(fails)} 通过')
    for f in fails:
        print(f'  ✗ {f}')
    return 0 if not fails else 1


def main():
    if '--selftest' in sys.argv:
        sys.exit(_selftest())
    ap = _ap.ArgumentParser()
    ap.add_argument('--intent', required=True)
    ap.add_argument('--product', default='UEG')
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--block', action='store_true', help='输出任务书段落')
    a = ap.parse_args()
    try:
        titles = load_titles(a.product)
        res = locate(a.intent, titles)
    except Exception as e:
        # ★ 任何异常都降级，不阻塞生成
        res = {'verdict': 'no_titles', 'L': 0, 'sub': '', 'R': -1, 'match': '',
               'error': f'{type(e).__name__}: {e}'}
    res['product'] = a.product
    res['n_titles'] = len(locals().get('titles', []) or [])
    if a.block:
        print(render_block(res, a.product))
    elif a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"档位: {res['verdict']}  L={res['L']} R={res['R']}  定位: {res['match']}")


if __name__ == '__main__':
    main()
