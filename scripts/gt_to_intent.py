#!/usr/bin/env python3
"""从 GT 生成「意图 + 数据清单」的分析器。

核心：把 GT 的命令族翻译成业务说法，再按业务链路分组，
      最终产出「完备但不细节」的意图。

依赖 /tmp/family_cnname.json（由 extract_family_cnname.py --all 生成）。

用法：
  python3 gt_to_intent.py <ticket>          # 单个工单分析
  python3 gt_to_intent.py --all             # 全部工单概览
  python3 gt_to_intent.py <ticket> --json   # JSON 输出（供 LLM 生成意图用）
"""
import argparse
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

GT_PATH = Path('/tmp/gt_cleaned.json')
IDX_PATH = Path('/tmp/family_cnname.json')

# 业务链路分组（按族名前缀关键词）
GROUP_RULES = [
    ('计费链', ['URR', 'RULE', 'USERPROFILE', 'USRPROF', 'PCCPOLICY', 'CHARGECHAR',
               'CHGMODE', 'SELCHF', 'APPPOLICY', 'POLICYCOND', 'RDSSTATIC', 'CTXSTART']),
    ('流量识别', ['FILTER', 'FLTBIND', 'FLOWFILTER', 'PROTBIND', 'L7FILTER', 'HOST',
                'FWPOLICY', 'CFPROTOCOL', 'GLBCFFUNC', 'APNDEACTQFPLCY']),
    ('地址池与承载', ['POOL', 'SECTION', 'INTERFACE', 'LOGICINF', 'IFIPV4', 'IFIPV6',
                   'IPBINDVPN', 'SRROUTE', 'NETWORKROUTE', 'GRETUNNEL', 'VPNINST',
                   'L3VPN', 'VPNINSTAF', 'IPFARM', 'CONFLICTIPV6']),
    ('APN 与移动性', ['APN', 'CPAPN', 'CONNECTPLMN', 'HPLMN', 'PNFDNN', 'NSDNN', 'PNFSMF',
                    'PNFNS', 'PNFPROFILE', 'PNFTAIRANGE', 'PNFSUPI', 'TAIRANGELIST',
                    'TACRANGE', 'TAIGROUP', 'UPAREA', 'UPAREABIND', 'UPNODE', 'UPBIND',
                    'UPIPDOMAIN', 'LOCBIND', 'BSFIPRANGE', 'PEERNF', 'N2TACID',
                    'S1TACID', 'MMEIPTOMMEPOOL', 'VIRTUALAPN', 'QOSPROP',
                    'IPALLOCBYSMF', 'DNAI', 'SUPI']),
    ('IMS / P-CSCF', ['PCSCF', 'IMSIBINDUP']),
    ('网络切片', ['SNSSAI']),
    ('紧急呼叫', ['EMGCFG', 'EMGAPN', 'NGEMG']),
    ('网络自愈/软参', ['SOFTPARA', 'SOFTPARAOFBIT', 'AMFSOFTPARA', 'DBPARAS',
                     'NODEHEAL', 'PODHEAL', 'MMFUNC', 'NGMMFUNC', 'NODEREP']),
    ('刷新与开关', ['REFRESHSRV', 'LICENSESWITCH', 'LICX', 'DEACTIVERATE', 'UPGTPPATH',
                 'ECHOIPLIST', 'TCPMSS', 'ACLBINDAPN', 'SFEPASS', 'APPTRAFFIC', 'ALMINFO']),
    ('License', ['LICENSESWITCH', 'LICX']),
]


def load():
    gt = json.loads(GT_PATH.read_text(encoding='utf-8'))
    idx = json.loads(IDX_PATH.read_text(encoding='utf-8'))
    return gt, idx


def cn_name(fam, idx):
    """族名 → 中文业务说法。去掉「增加/设置/查询/删除」等动作前缀。"""
    hit = idx.get(fam)
    if not hit:
        return None
    cn = next(iter(hit.values()))
    # 去掉动作前缀
    cn = re.sub(r'^(增加|添加|设置|修改|删除|查询|激活|去激活|清除|锁定)+', '', cn)
    return cn.strip() or None


def group_of_family(fam):
    """族名 → 业务组名。"""
    up = fam.upper()
    for gname, kws in GROUP_RULES:
        for kw in kws:
            if up.startswith(kw) or kw in up:
                return gname
    return '其他'


def analyze(g, idx):
    """分析一个工单，返回结构化结果。"""
    by_fam = defaultdict(list)
    for ln, verb, fam, params, raw in g['kept']:
        by_fam[fam].append({'verb': verb, 'params': params, 'raw': raw, 'line': ln})

    fam_groups = defaultdict(list)      # {业务组: [(族名, 中文名, 命令数, 对象数)]}
    unmapped = []

    # 手工补充的中文名（KB 库里查不到的少数族）
    EXTRA_CN = {
        'CPAPN': 'CP侧APN',
        'CPAPNADDRESSATTR': 'CP侧APN地址属性',
        'EDGESMCOMMFUNC': '边缘会话管理通用功能',
        'LICX1INFO': 'License扩展信息1',
        'LICX2INFO': 'License扩展信息2',
        'LICX3CFG': 'License扩展配置',
        'LICX3INTFCFG': 'License扩展接口配置',
        'RDSSTATICIPPARA': 'RADIUS静态IP参数',
    }

    for fam, items in by_fam.items():
        cn = cn_name(fam, idx) or EXTRA_CN.get(fam)
        if cn is None:
            # ★ 2026-11-10 修复：查不到中文名时不能整族跳过
            #   实测 NC20260907002110：4 个 LICX* 族都没中文名 → 整段意图变空
            #   现在用族名原文代替（这仍是业务标识，不是 MML 参数名）
            unmapped.append(fam)
            cn = fam

        gname = group_of_family(fam)

        # ★ 2026-11-11 修复致命 bug（用户以 NC20260828000409 为锚点）：
        #   原来取 items[0]['verb']，同一个族既有 ADD 又有 RMV 时只保留第一个动词。
        #   实测该工单 POOL 族 ADD 4 + RMV 5，意图只写「新增 地址池」，
        #   「删除」完全丢失 → agent 按错误意图执行，规划表也就只有 ADD。
        #   全量影响：12 个工单 / 90 条 RMV 命令在意图里消失。
        #   修法：按 (族, 动词) 拆成多条记录。
        by_verb = defaultdict(list)
        for it in items:
            by_verb[it['verb']].append(it)

        for verb, vitems in by_verb.items():
            # 对象数：优先用主键参数（取唯一值的第一个参数），
            # 同族多动词时各自单独算，避免 ADD+RMV 混算成一个数。
            n_objs = len({next(iter(it['params'].values()))
                          for it in vitems if it['params']})
            fam_groups[gname].append({
                'family': fam,
                'biz_name': cn,
                'n_cmds': len(vitems),
                'n_objs': n_objs,
                'verb': verb,
            })

    return {
        'ticket': g['ticket'],
        'n_cmds': len(g['kept']),
        'n_fams': len(by_fam),
        'groups': {k: v for k, v in fam_groups.items()},
        'unmapped': unmapped,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ticket', nargs='?')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--json', action='store_true')
    args = ap.parse_args()

    gt, idx = load()

    if args.all:
        print(f'{"工单":<22} {"GT条":>5} {"族":>3} {"业组":>3} {"未映射":>4}')
        print('=' * 46)
        for r in sorted(gt, key=lambda x: -len(x['kept'])):
            a = analyze(r, idx)
            print(f"{a['ticket']:<22} {a['n_cmds']:>5} {a['n_fams']:>3} "
                  f"{len(a['groups']):>3} {len(a['unmapped']):>4}")
        return

    if not args.ticket:
        print(__doc__)
        return

    g = next((x for x in gt if x['ticket'] == args.ticket), None)
    if not g:
        print(f'找不到 {args.ticket}')
        return

    a = analyze(g, idx)
    if args.json:
        print(json.dumps(a, ensure_ascii=False, indent=1))
        return

    print(f"\n{a['ticket']}   GT {a['n_cmds']} 条 / {a['n_fams']} 族\n")
    for gname, items in sorted(a['groups'].items()):
        total_cmds = sum(i['n_cmds'] for i in items)
        total_objs = sum(i['n_objs'] for i in items)
        print(f'【{gname}】{len(items)} 类对象，共 {total_cmds} 条命令 / {total_objs} 个对象')
        for it in sorted(items, key=lambda x: -x['n_cmds']):
            print(f"   {it['verb']:<3} {it['biz_name']:<28} {it['n_cmds']:>4} 条 "
                  f"{it['n_objs']:>4} 个对象   [{it['family']}]")
        print()
    if a['unmapped']:
        print(f"⚠ 未映射 {len(a['unmapped'])} 个族: {', '.join(a['unmapped'])}")


if __name__ == '__main__':
    main()
