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

# ★ 2026-11-12：表头自然语言化（三档映射 + 多样性）
try:
    from header_naming import header_for as _header_for_static
except ImportError:
    def _header_for_static(pname, use_variant=True):
        return None

try:
    import header_llm as _HL
except ImportError:
    _HL = None


def header_for(pname, seed=None):
    """参数名 → 自然语言表头（带多样性）。

    ★ 2026-11-12 优先级：
      1. LLM 缓存（多种变体，按 seed 稳定选择）
      2. 静态映射（精校 + 语素推导）
    理由：LLM 生成的描述更准确（INTELSHUNT → 智能分流模式，
         语素推导给的是「智能旁路」，不准），且有多样性。
    """
    if _HL:
        h = _HL.get_header(pname, seed=seed)
        if h:
            return h
    return _header_for_static(pname)

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


def family_cn(fam, seed=None):
    """命令族 → 中文业务名（表名用）。

    ★ 2026-11-12
      原实现只用 SHEET_NAME（23 条）+ EXTRA_CN（8 条），
      导致 201 个族里大部分表名是英文（URRGROUP / RULE / USERPROFILE），
      删减脚本按中文表名匹配时匹配不上。

      现在优先用 LLM 缓存（201 个族全有，每族 2 个说法），
      退回到 SHEET_NAME / EXTRA_CN 静态映射。
    """
    key = f'FAMILY::{fam.upper()}'
    if _HL is not None:
        try:
            cache = _HL._load_cache()
            names = cache.get(key)
            if names:
                if isinstance(names, str):
                    return names
                if isinstance(names, list) and names:
                    import hashlib as _hs
                    h = int(_hs.md5(str(seed or fam).encode()).hexdigest()[:8], 16)
                    return names[h % len(names)]
        except Exception:
            pass
    # 静态兜底
    return EXTRA_CN.get(fam) or SHEET_NAME.get(fam) or fam


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


# ═══════════════════════════════════════════════════════════
# ★ 2026-11-12 数据清单只还原「引号值」
# ═══════════════════════════════════════════════════════════
# 用户要求：「把引号还原出来就行了」
#   非引号值（ENABLE/DISABLE/数字）是枚举或常量，不进数据清单
#   实测 86 单 790 个参数：引号 195 个 / 非引号 596 个 / 交叉 1 个

def is_quoted_value(raw, pname):
    """判断某个参数在原始命令里是否用引号包起来。

    为什么不能靠 params 字典：解析时引号已被剥掉。
    必须回 raw 命令里看。
    """
    if not raw or not pname:
        return False
    m = re.search(rf'\b{re.escape(pname)}\s*=\s*("[^"]*"|[^,\s;]+)', raw, re.I)
    if not m:
        return False
    return m.group(1).startswith('"')


def filter_quoted_params(items):
    """过滤掉非引号参数，只留引号值参数。

    items 结构：[{'params': {...}, 'raw': '...'}]
    返回：新的 items（params 已过滤）
    """
    out = []
    for it in items:
        raw = it.get('raw') or ''
        kept = {k: v for k, v in (it.get('params') or {}).items()
                if is_quoted_value(raw, k)}
        if kept:
            ni = dict(it)
            ni['params'] = kept
            out.append(ni)
    return out


def group_by_shape(items):
    """同族内按「引号参数集合」分组，集合不同的对象分到不同组。

    ★ 2026-11-12：解决空单元格问题
      NC20260820001773 的 RULE 族有两种形态：
        有 FLOWFILTERNAME 的（4 个对象）
        没有的（另一批）
      原来混在一张表里，导致空单元格。

    返回：[{'shape': frozenset, 'items': [...]}, ...]
    """
    groups = {}
    for it in items:
        shape = frozenset((it.get('params') or {}).keys())
        groups.setdefault(shape, []).append(it)
    # 按对象数降序，保证输出稳定
    return [{'shape': s, 'items': v}
            for s, v in sorted(groups.items(), key=lambda kv: -len(kv[1]))]


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
            cnname = family_cn(fam, seed=tk) or it['biz_name']
            verb = it['verb']
            n_obj = it['n_objs']
            n_cmd = it['n_cmds']

            # 参数分类
            fixed, regular, varied = classify_params(by_fam[fam])

            # 动作词
            act = {'ADD': '新增', 'MOD': '调整', 'RMV': '删除', 'SET': '设置'}.get(verb, verb)

            # ★ 2026-11-11 用户裁定：不再写个数
            #   「不需要再描写个数了，如果有数据表就说见数据表，
            #     如果是简单工单就列举出来」
            #
            #   有数据表   → 「【】新增 地址池（见数据清单）」
            #   简单工单   → 「【】新增 地址池：pool_a、pool_b」
            #   其他       → 「【】新增 地址池」
            #
            #   个数本来也容易被误读：ADD+RMV 混在一个族里时，
            #   按命令条数算是 9，按对象算是 14，都不是「变更量」。
            _cnt_pre = {}
            for it2 in by_fam[fam]:
                for _k, _v in it2['params'].items():
                    if _v and not is_placeholder(_v):
                        _cnt_pre.setdefault(_k, set()).add(_v)
            _will_have_sheet = bool(varied or any(len(v) > 1 for v in _cnt_pre.values()))

            detail = ''
            if _will_have_sheet:
                detail = '（见数据清单）'
            elif level == 'simple' and _cnt_pre:
                # 简单工单：直接列举对象名（最多 8 个，超出加省略）
                _mk = max(_cnt_pre.items(), key=lambda kv: len(kv[1]))[0]
                _vals = sorted(v for v in _cnt_pre[_mk] if v)
                if 1 <= len(_vals) <= 8:
                    detail = '：' + '、'.join(str(v) for v in _vals)

            line = f'- {act} {cnname}{detail}'
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
            # ★ 2026-11-11 改：按 (族, 动词) 分组生成，
            #   否则 ADD 的对象和 RMV 的对象会混在同一张表里，
            #   agent 分不清哪些要新建、哪些要删除。
            _fams_items_all = [it2 for it2 in by_fam[fam] if it2['verb'] == verb]
            if not _fams_items_all:
                continue

            # ★ 2026-11-12 改动 1：只保留「引号值」参数
            #   用户要求：「把引号还原出来就行了」
            #   非引号（ENABLE/DISABLE/数字）是枚举或常量，不进清单
            _fams_items_q = filter_quoted_params(_fams_items_all)
            if not _fams_items_q:
                continue    # 该族没有任何引号值 → 不生成清单

            # ★ 2026-11-12 改动 2：同族按「引号参数集合」分表
            #   解决 NC20260820001773 的 RULE 族空单元格问题
            _shape_groups = group_by_shape(_fams_items_q)

            for _gi, _grp in enumerate(_shape_groups):
                _fams_items = _grp['items']
                _shape = _grp['shape']

                _cnt = {}
                for it2 in _fams_items:
                    for _k, _v in it2['params'].items():
                        if _v and not is_placeholder(_v):
                            _cnt.setdefault(_k, set()).add(_v)
                if not _cnt:
                    continue

                # 主键选择：取「取值种类最多」的参数
                main_key = max(_cnt.items(), key=lambda kv: len(kv[1]))[0]
                # 其余引号参数都作为变列（不再用 varied，因为 varied 混了非引号）
                vary_keys = [k for k in _shape if k != main_key]

                hdr_main = header_for(main_key, seed=tk) or biz_param(main_key) or _fallback_biz(main_key)
                if not hdr_main:
                    continue

                hdr_vary = []
                for k in vary_keys:
                    h = header_for(k, seed=tk) or biz_param(k) or _fallback_biz(k)
                    if h:
                        hdr_vary.append((k, h))

                # 表名：多形态时加区分后缀
                _sheet_base = cnname
                if len(_shape_groups) > 1:
                    # 用「变列的中文名组合」区分，或者用序号
                    if hdr_vary:
                        _sheet_base = f'{cnname}（含{"/".join(h[1] for h in hdr_vary[:2])}）'
                    else:
                        _sheet_base = f'{cnname}（仅{header_for(main_key, seed=tk) or main_key}）'

                headers = [hdr_main] + [h[1] for h in hdr_vary]
                rows = []
                for it2 in _fams_items:
                    row = [it2['params'].get(main_key, '')]
                    row += [it2['params'].get(k, '') for k, _ in hdr_vary]
                    rows.append(row)

                # 去重
                uniq_rows = []
                seen_rows = set()
                for r_ in rows:
                    key_ = tuple(r_)
                    if key_ not in seen_rows:
                        seen_rows.add(key_)
                        uniq_rows.append(r_)

                if uniq_rows:
                    # ★ 2026-11-12：第 5 个元素是命令族（供下游精确匹配）
                    sheets.append((_sheet_base, headers, uniq_rows, act, fam))
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
        for item in r['sheets']:
            name, headers, rows, act = item[0], item[1], item[2], item[3]
            # 表名带动作，避免「新增对象」和「删除对象」混在一张表
            parts.append(f'\n## {name}（{act}，{len(rows)} 行）\n')
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
