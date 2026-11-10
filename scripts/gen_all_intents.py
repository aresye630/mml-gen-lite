"""批量生成 86 个工单的意图 + 数据清单。

基于 gt_to_intent.py 的结构化分析 + analyze_gt.py 的固定/规律/变化分类，
按 gt-to-intent-dataset skill 的规则生成。

输出：
  /tmp/intent_dataset/<TICKET>_意图.md
  /tmp/intent_dataset/<TICKET>_数据清单.md   （markdown 表格，可转 xlsx）
"""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/scripts')
from gt_to_intent import load, analyze, cn_name
from analyze_gt import seq_like

OUT = Path('/tmp/intent_dataset')
OUT.mkdir(exist_ok=True)

# 手工补充的中文名（KB 库里没有的 8 个族）
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


def cn(fam, idx):
    """族名 → 中文名（含手工补充）。"""
    return cn_name(fam, idx) or EXTRA_CN.get(fam)


# 表名用「业务对象」视角，不用命令名（避免泄露族）
SHEET_NAME = {
    'GRE隧道': '隧道清单',
    '接口IPv4地址': '接口地址清单',
    '接口IPv6地址': '接口地址清单',
    '地址池': '地址池清单',
    '接口绑定VPN': '接口与VPN对应关系',
    'IPv4静态路由': '路由规划',
    'IPv6静态路由': '路由规划',
    '过滤器': '过滤规则清单',
    'IPv6过滤器': '过滤规则清单',
    '流过滤器': '流分类清单',
    '流过滤器的过滤器绑定关系': '流分类与过滤规则对应关系',
    '域名对象': '域名清单',
    'URR': '计费规则清单',
    '规则': '策略规则清单',
    '用户模板': '用户模板清单',
    '用户模板和规则的绑定关系': '用户模板与规则对应关系',
    '用户模板的URR组绑定关系': '用户模板与计费组对应关系',
    'PCC策略组': '策略组清单',
    'APN的IMS分类器': 'APN信令分类清单',
    '显示地址池组映射关系': '池组映射规划',
    '基于APN去活用户面专有QoS Flow策略': 'APN去活策略',
    '地址池组': '地址池组清单',
    '地址段': '地址段规划',
}


def is_placeholder(v):
    """判断是不是占位符值（<x> / 【待填写】 / *** 等）。"""
    if not v:
        return True
    v = str(v).strip()
    if not v:
        return True
    if v.startswith('<') and v.endswith('>'):
        return True
    if '待填写' in v or '待确认' in v or '占位' in v:
        return True
    if v.strip('*') == '':
        return True
    return False


def _fallback_biz(pname):
    """参数名兜底→业务说法。

    ★ 2026-11-10：用户要求「数据清单补 IP 地址和命名，不补具体参数细节」。
    原来 biz_param() 返回 None 就整列丢掉，导致 IP/名称类的列全没了。
    这里对「标识类」参数给中性业务说法（不暴露 MML 参数名），
    对「配置类」参数仍然返回 None（不补）。
    """
    U = pname.upper()

    # IP / 地址类 → 允许
    if 'STARTIP' in U or 'BEGINIP' in U:
        return '起始地址'
    if 'ENDIP' in U:
        return '结束地址'
    if 'IPV4' in U and ('ADDR' in U or 'IP' in U):
        return 'IPv4地址'
    if 'IPV6' in U and ('ADDR' in U or 'IP' in U):
        return 'IPv6地址'
    if 'IPADDR' in U or U.endswith('IP'):
        return 'IP地址'
    if 'MASK' in U or 'PREFIXLEN' in U:
        return '掩码长度'
    if 'GATEWAY' in U or 'NEXTHOP' in U:
        return '下一跳'
    if 'VLAN' in U:
        return 'VLAN'

    # 名称 / 标识类 → 允许
    if U.endswith('NAME') or U.endswith('NAMED'):
        return '名称'
    if U in ('APN', 'POOLNAME', 'TNLNAME', 'VRFNAME', 'IFNAME',
             'SECTIONNUM', 'PRIORITY', 'ID', 'INDEX'):
        return '标识'

    # 端口 / 号段 → 允许
    if 'PORT' in U:
        return '端口'
    if 'TACSTART' in U or 'TACEND' in U or 'TAC' in U:
        return 'TAC号段'
    if 'SNSSAI' in U or 'SST' in U or 'SD' in U:
        return '切片标识'

    # 其余（枚举、开关、属性值）→ 不补，让 agent 自己判断
    return None


def _sheet_name(cnname):
    """中文名 → 业务视角的表名（避免直接用命令名）。"""
    return SHEET_NAME.get(cnname, cnname)


# ★ 参数名 → 业务说法（意图里绝不能出现参数名）
# ★ 2026-11-10 用户裁定：数据清单补 IP 地址和命名，不补具体参数细节
#   背景：45/87 工单的 GT 里有意图和清单都没有的 IP（如 NC20260911000610 有 300 个），
#        agent 只能编造，导致对象级指标天然不可能高。
#   原则：IP、名称、地址段这类「客户能提供的规划数据」要补；
#        枚举值、开关、具体属性值不补（那是配置决策，让 agent 自己判断）。
PARAM_BIZ = {
    'IPV6ADDR': '探测地址', 'IPV4ADDR': '地址', 'IFIPADDR': '接口地址',
    'IPV6MASK': '掩码', 'SUBNETMASK': '子网掩码',
    'IPVERSION': 'IP 版本', 'TNLNAME': '隧道名称', 'GREKEY': '隧道密钥',
    'POOLNAME': '地址池名称', 'POOLTYPE': '池类型', 'REDUNDFUNC': '冗余功能',
    'IFNAME': '接口名称', 'FILTERNAME': '过滤器名称', 'HOSTNAME': '域名对象名称',
    'VRFNAME': 'VPN 名称', 'PREFIX': '路由目标网段', 'MASKLENGTH': '掩码长度',
    'AFTYPE': '地址族', 'PRIORITY': '优先级', 'POLICYTYPE': '策略类型',
    'FILTERINGMODE': '过滤模式', 'UPTYPE': '模板类型', 'PCCPOLICYGRPNM': '策略组名称',
    'REFRESHTYPE': '刷新类型', 'DOMAINVALUE': '域名', 'TACSECNUM': 'TAC 编号',
    'SECTIONNUM': '地址段编号', 'V4STARTIP': '起始地址', 'V4ENDIP': '结束地址',
    'V6PREFIXSTART': '起始前缀', 'V6PREFIXEND': '结束前缀',
    'LOCATIONGRPTYPE': '位置区类型', 'LOCATIONGRPNAME': '位置区名称',
    'MAPPINGNAME': '映射名称', 'URRNAME': 'URR 名称', 'URRID': 'URR 编号',
    'RULENAME': '规则名称', 'USERPROFILENAME': '用户模板名称',
    'APN': 'APN 名称', 'DNN': 'DNN 名称', 'SNSSAI': '切片标识',
    'SRCIFNAME': '源接口', 'DSTIPADDR': '目的地址', 'DSTVPNNAME': '目的 VPN',
    'TNLTYPE': '隧道类型', 'SRCTYPE': '源类型',
    'KEEPALVEN': '保活使能', 'GREKEYEN': '密钥使能', 'REDUNDANCYEN': '冗余使能',
    'V1DATAECHOSW': '数据面探测开关', 'LOGICINFTYPE': '逻辑接口类型',
    'HASVPN': '是否绑定 VPN', 'IPLEASE': '地址租期开关',
    'RELEASETIME': '地址释放时长', 'SINGLEIPFLAG': '单地址标志',
    'ALARMSWITCH': '告警开关', 'IMSSW': 'IMS 开关',
}

# 值 → 业务说法
VALUE_BIZ = {
    'ENABLE': '开启', 'DISABLE': '关闭', 'TRUE': '是', 'FALSE': '否',
    'EXTERNAL': '外部池', 'LOCAL': '本地池', 'IPV4': 'IPv4', 'IPV6': 'IPv6',
    'PCC': 'PCC', 'ALL': '全部',
}


def biz_param(k):
    """参数名 → 业务说法。查不到返回 None（不输出）。"""
    return PARAM_BIZ.get(k)


def biz_value(v):
    """参数值 → 业务说法。"""
    return VALUE_BIZ.get(str(v).upper(), v)


def classify_params(items):
    """把一个族的参数分成：固定值 / 有规律 / 变化。"""
    fixed, regular, varied = {}, {}, {}
    if not items:
        return fixed, regular, varied

    all_keys = set()
    for it in items:
        all_keys |= set(it['params'].keys())

    for k in all_keys:
        vals = [it['params'].get(k) for it in items if k in it['params']]
        uniq = {v for v in vals if v is not None}
        if not uniq:
            continue
        if len(uniq) == 1:
            fixed[k] = next(iter(uniq))
        else:
            seq = seq_like(sorted(uniq))
            if seq:
                regular[k] = seq
            else:
                varied[k] = sorted(uniq)
    return fixed, regular, varied


def gen_dataset(tk, gt, idx):
    """生成一个工单的意图 + 数据清单。"""
    g = next((x for x in gt if x['ticket'] == tk), None)
    if not g:
        return None

    a = analyze(g, idx)
    n_cmds = a['n_cmds']
    level = 'simple' if n_cmds < 50 else ('medium' if n_cmds <= 200 else 'complex')

    # 按族聚合
    by_fam = defaultdict(list)
    for ln, verb, fam, params, raw in g['kept']:
        by_fam[fam].append({'verb': verb, 'params': params, 'raw': raw})

    # ── 意图正文 ──
    intent_lines = []
    sheets = []          # [(sheet_name, headers, rows)]

    for gname in sorted(a['groups'].keys()):
        items = a['groups'][gname]
        intent_lines.append(f'【{gname}】')
        for it in sorted(items, key=lambda x: -x['n_cmds']):
            fam = it['family']
            cnname = it['biz_name']
            verb = it['verb']
            n_obj = it['n_objs']
            n_cmd = it['n_cmds']

            # 参数分类
            fixed, regular, varied = classify_params(by_fam[fam])

            # 动作词
            act = {'ADD': '新增', 'MOD': '调整', 'RMV': '删除', 'SET': '设置'}.get(verb, verb)

            # 量级描述
            if n_obj == 1:
                qty = ''
            elif n_obj <= 5:
                qty = f'{n_obj} 个'
            else:
                qty = f'约 {n_obj} 个'

            line = f'- {act} {cnname}{("，" + qty) if qty else ""}'
            intent_lines.append(line)

            # ★ 固定值 → 用业务说法描述
            biz_fixed = []
            for k, v in fixed.items():
                bk = biz_param(k)
                if not bk:
                    continue          # 未映射的参数名，跳过（绝不泄露）
                biz_fixed.append(f'{bk}为{biz_value(v)}')
            if 1 <= len(biz_fixed) <= 4:
                intent_lines.append(f'    （{"，".join(biz_fixed)}）')

            # ★ 规律值 → 用业务说法说明规律
            for k, sq in regular.items():
                bk = biz_param(k)
                if not bk:
                    continue
                intent_lines.append(
                    f'    （{bk}按 {sq["prefix"]}<序号> 递增，从 {sq["prefix"]}{sq["start"]} 起）')

            # ★ 变化值 / 对象清单 → 数据清单（列名也用业务说法）
            # 2026-11-10 改：原来只有 varied 且非 simple 才生成，
            #   导致简单工单和「对象名是固定某个值但多对象」的工单没有清单。
            #   现在：只要对象数 > 1 且有可用主键，就生成对象清单。
            _cnt = {}
            for it2 in by_fam[fam]:
                for _k, _v in it2['params'].items():
                    if _v and not is_placeholder(_v):
                        _cnt.setdefault(_k, set()).add(_v)
            _has_multi_obj = any(len(v) > 1 for v in _cnt.values())

            if (varied or _has_multi_obj) and _cnt:
                # ★ 主键选择：不能盲取第一个参数（ADD SRROUTE 的第一个是 AFTYPE，
                #   184 行全一样）。应该选「取值种类最多」的那个参数。
                main_key = max(_cnt.items(), key=lambda kv: len(kv[1]))[0]
                vary_keys = [k for k in varied if k != main_key]
                # 列名映射；未映射的列名跳过
                hdr_main = biz_param(main_key) or _fallback_biz(main_key)
                if not hdr_main:
                    continue
                hdr_vary = [(k, biz_param(k) or _fallback_biz(k))
                            for k in vary_keys
                            if (biz_param(k) or _fallback_biz(k))]
                if hdr_vary:
                    headers = [hdr_main] + [h[1] for h in hdr_vary]
                    rows = []
                    for it2 in by_fam[fam]:
                        row = [it2['params'].get(main_key, '')]
                        row += [it2['params'].get(k, '') for k, _ in hdr_vary]
                        rows.append(row)
                    # 去重（同值多行合并）
                    uniq_rows = []
                    seen_rows = set()
                    for r_ in rows:
                        key_ = tuple(r_)
                        if key_ not in seen_rows:
                            seen_rows.add(key_)
                            uniq_rows.append(r_)
                    sheets.append((cnname, headers, uniq_rows))
                else:
                    # 只有对象标识变化
                    rows = []
                    seen_v = set()
                    for it2 in by_fam[fam]:
                        v_ = it2['params'].get(main_key, '')
                        if v_ and v_ not in seen_v:
                            seen_v.add(v_)
                            rows.append([v_])
                    if rows:
                        sheets.append((_sheet_name(cnname), [hdr_main], rows))
        intent_lines.append('')

    return {
        'ticket': tk,
        'level': level,
        'n_cmds': n_cmds,
        'n_fams': a['n_fams'],
        'intent_body': '\n'.join(intent_lines).rstrip(),
        'sheets': sheets,
        'unmapped': a['unmapped'],
    }


def write_output(r):
    """写意图.md 和 数据清单.md。"""
    tk = r['ticket']
    # 意图文件
    ip = OUT / f'{tk}_意图.md'
    txt = f"""# {tk} — 意图

需要做的变更：

{r['intent_body']}
"""
    ip.write_text(txt, encoding='utf-8')

    # 数据清单文件
    dp = OUT / f'{tk}_数据清单.md'
    if r['sheets']:
        parts = [f'# {tk} 数据清单\n']
        for name, headers, rows in r['sheets']:
            parts.append(f'\n## {name}（{len(rows)} 行）\n')
            parts.append('| ' + ' | '.join(headers) + ' |')
            parts.append('|' + '|'.join(['---'] * len(headers)) + '|')
            for row in rows[:200]:      # 最多 200 行，避免文件过大
                parts.append('| ' + ' | '.join(str(x) for x in row) + ' |')
            if len(rows) > 200:
                parts.append(f'\n（共 {len(rows)} 行，此处只列前 200 行）')
        dp.write_text('\n'.join(parts), encoding='utf-8')
        return ip, dp
    return ip, None


def main():
    gt, idx = load()
    results = []
    for r in sorted(gt, key=lambda x: -len(x['kept'])):
        res = gen_dataset(r['ticket'], gt, idx)
        if res:
            write_output(res)
            results.append(res)

    print(f'生成 {len(results)} 个工单')
    from collections import Counter
    print(f'  分档: {dict(Counter(r["level"] for r in results))}')
    print(f'  有数据清单: {sum(1 for r in results if r["sheets"])} 个')
    print(f'  有未映射族: {sum(1 for r in results if r["unmapped"])} 个')
    print(f'\n输出目录: {OUT}')

    # 保存汇总
    summary = [{k: v for k, v in r.items() if k != 'sheets'} | {'n_sheets': len(r['sheets'])}
               for r in results]
    (OUT / '_summary.json').write_text(
        json.dumps(summary, ensure_ascii=False, indent=1), encoding='utf-8')


if __name__ == '__main__':
    main()
