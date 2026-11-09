"""命令族 → 业务说法映射（用于生成意图，不泄露命令名）。

这是给「意图生成」用的字典：把 GT 的 MML 族名翻译成业务描述。
生成意图时只用业务说法，绝不出现族名本身。

数据来源：86 个工单的 GT 族 + 命令族中文名映射表。
"""
import json
import re
from pathlib import Path

# 族名 → 业务说法
# 规则：用运维人员日常说法的名词短语，能让人理解「要配什么」
FAMILY_BIZ_NAME = {
    # ── 计费 / 策略链 ──
    'URR': '用量上报规则',
    'URRGROUP': '用量上报组',
    'URRGRPBINDING': '用量上报组绑定',
    'RULE': '计费规则',
    'RULEBINDING': '规则与用户模板的绑定',
    'USERPROFILE': '用户模板',
    'PCCPOLICYGRP': 'PCC 策略组',
    'SPECURRGRPLIST': '专用用量上报组列表',
    'CHARGECHAR': '计费属性',
    'CHARGECHARCHK': '计费属性校验开关',
    'GLBCHARGECHAR': '全局计费属性',
    'CHGMODE': '计费接口模式',
    'ROAMCHGMODE': '漫游计费接口模式',
    'APNCHGMODE': 'APN 计费接口模式',
    'PCCCHGMODEBYPCFID': '按 PCF ID 的计费接口模式',
    'SELCHFGBYIMSI': 'CHF 选择方式',
    'APPPOLICYCTRL': '应用策略控制',
    'POLICYCONDITION': '策略条件',
    'RDSSTATICIPPARA': 'RADIUS 静态 IP 参数',

    # ── 内容识别 / 过滤链 ──
    'FILTER': '四层过滤器',
    'FILTERIPV6': 'IPv6 四层过滤器',
    'FILTERGROUP': '过滤器组',
    'FLTBINDFLOWF': '过滤器与流过滤器的绑定',
    'FLOWFILTER': '流过滤器',
    'PROTBINDFLOWF': '流过滤器协议绑定',
    'L7FILTER': '七层过滤器',
    'HOST': '域名对象',
    'FWPOLICY': '防火墙策略',
    'CFPROTOCOLLST': '内容过滤协议列表',
    'GLBCFFUNC': '全局内容过滤开关',

    # ── 地址池 / 接口 / 路由 ──
    'POOL': '地址池',
    'POOLGROUP': '地址池组',
    'POOLBINDGROUP': '地址池与池组的绑定',
    'POOLGRPMAP': '池组映射',
    'SECTION': '地址段',
    'INTERFACE': '接口',
    'LOGICINF': '逻辑接口',
    'IFIPV4ADDRESS': '接口 IPv4 地址',
    'IFIPV6ADDRESS': '接口 IPv6 地址',
    'IFIPV6ENABLE': '接口 IPv6 使能',
    'IPBINDVPN': '接口与 VPN 的绑定',
    'SRROUTE': '静态路由',
    'SRROUTE6': 'IPv6 静态路由',
    'NETWORKROUTE': '网络路由',
    'GRETUNNEL': 'GRE 隧道',
    'VPNINST': 'VPN 实例',
    'L3VPNINST': 'L3VPN 实例',
    'VPNINSTAF': 'VPN 地址族',

    # ── APN / 移动性 ──
    'APN': 'APN',
    'CPAPN': 'APN',
    'APNIMSSIGFLTR': 'APN IMS 信令过滤器',
    'APNUSRPROFG': 'APN 用户模板组',
    'APNIPALLOCRULE': 'APN IP 分配规则',
    'APNQOSATTR': 'APN QoS 属性',
    'APNSOFTPARA': 'APN 软件参数',
    'APNPCCFUNC': 'APN PCC 功能',
    'APNIDLETIME': 'APN 空闲时长',
    'APNCHARGECTRL': 'APN 计费控制',
    'APNIMSATTR': 'APN IMS 属性',
    'APNADDRESSATTR': 'APN 地址属性',
    'CONNECTPLMN': '接入 PLMN',
    'HPLMN': '归属 PLMN',
    'PNFDNN': '对端 NF 的 DNN 信息',
    'NSDNN': '网络切片的 DNN',
    'PNFSMFSERAREA': '对端 NF 的 SMF 服务区域',
    'PNFNS': '对端 NF 实例',
    'PNFPROFILE': '对端 NF 概述信息',
    'PNFTAIRANGE': '对端 NF 的 TAI 范围',
    'TAIRANGELIST': 'TAI 范围列表',
    'TACRANGE': 'TAC 区域',
    'UPAREA': 'UPF 服务区',
    'UPAREABINDN2TAI': 'UPF 服务区与 5G TAI 的绑定',
    'UPNODE': 'UPF 节点',
    'UPBINDS11': 'UPF 与 S11 接口的绑定',
    'UPIPDOMAIN': 'UPF 绑定的 IP 域',
    'LOCBINDAREA': '位置区绑定',
    'BSFIPRANGEBIND': 'BSF 实例与 IP 范围的绑定',
    'PEERNFIPLIST': '对端局向 IP 列表',
    'SUPI': '对端 NF 的 SUPI 信息',

    # ── P-CSCF / IMS ──
    'PCSCFIP': 'P-CSCF 地址',
    'PCSCFGROUP': 'P-CSCF 组',
    'PCSCFGRPBNDAPN': 'P-CSCF 组与 APN 的绑定',
    'PCSCFIMSISDNSEG': 'IMSI 与 MSISDN 号段',
    'IMSIBINDUP': 'IMS 与 UPF 的绑定',

    # ── 切片 ──
    'SNSSAI': '网络切片标识',
    'NSDNN': '切片的 DNN',

    # ── 通用 / 开关 ──
    'LICENSESWITCH': 'License 开关',
    'REFRESHSRV': '业务刷新',
    'DEACTIVERATE': '去活用户会话速率',
    'UPGTPPATH': 'GTP 路径属性',
    'ECHOIPLIST': '探测地址列表',
    'IPFARM': 'IP 地址池农场',
    'IPFARMSERVER': 'IP 农场服务器',
    'IPFARMGLOBAL': 'IP 农场全局配置',
    'TCPMSS': 'TCP MSS 配置',
    'ACLBINDAPN': 'APN 的 ACL 绑定',
    'UNCIPRESOUCE': 'UNC 接口 IP 资源',
    'TAIGROUP': 'TAI 组',
    'N2TACID': 'N2 TAC 标识',
    'S1TACID': 'S1 TAC 标识',
    'ALMINFO': '告警配置信息',
    'SFEPASSGREFRAG': 'SFE 透传 GRE 分片报文使能',
    'APPTRAFFICPARA': '应用流量参数',
    'BGPPEER': 'BGP 对等体',
    'BGPVRF': 'BGP VPN 实例',
    'BGPPEERAF': 'BGP 对等体地址族',
    'BGPVRFAF': 'BGP VPN 地址族',
    'BFDSESSION': 'BFD 会话',
    'IMPORTROUTE': '引入路由',
    'PREFIXLIMIT': '前缀数量限制',
    'IPFRR': 'IP FRR',
    'SRROUTEFRR': '静态路由 FRR',
    'CPNODEID': 'CP 节点标识',
    'AUTOSCALINGSERVICE': '自动化服务',
    'AUTOSCALINGSRROUTE': '自动化静态路由',
    'AUTOSCALINGETHTRUNK': '自动化以太网隧道',
    'SSUPROTCOLGROUP': 'S1-U 协议组',
    'EPRPDYN': '动态对端',
    'EPRPDYNIP': '动态对端 IP',
    'CPASSOCIATION': 'CP 关联',
    'MMEIPTOMMEPOOL': 'MME IP 与 MME 池的绑定',
    'VIRTUALAPNRULE': '虚拟 APN 规则',
    'QOSPROP': 'QoS 属性',
    'IPALLOCBYSMFSW': '基于 SMF 分配地址的开关',
    'DNAI': 'DNAI',
    'UPF': 'UPF',
}


def biz_name(fam):
    """族名 → 业务说法。查不到时返回族名的可读化形式（不直接暴露）。"""
    if fam in FAMILY_BIZ_NAME:
        return FAMILY_BIZ_NAME[fam]
    # 兜底：把驼峰拆成词，但这样仍会露出族名，标记出来供人工补充
    return None


def group_families(fams):
    """把族集合按业务链路分组。

    fams: ['URR', 'FILTER', ...]  纯族名集合
    返回: {业务组名: [业务说法, ...]}
    """
    GROUPS = {
        '计费链': ['URR', 'URRGROUP', 'URRGRPBINDING', 'RULE', 'RULEBINDING',
                  'USERPROFILE', 'PCCPOLICYGRP', 'SPECURRGRPLIST', 'CHARGECHAR',
                  'CHARGECHARCHK', 'GLBCHARGECHAR', 'CHGMODE', 'ROAMCHGMODE',
                  'APNCHGMODE', 'PCCCHGMODEBYPCFID', 'SELCHFGBYIMSI',
                  'APPPOLICYCTRL', 'POLICYCONDITION', 'RDSSTATICIPPARA'],
        '流量识别': ['FILTER', 'FILTERIPV6', 'FILTERGROUP', 'FLTBINDFLOWF',
                    'FLOWFILTER', 'PROTBINDFLOWF', 'L7FILTER', 'HOST',
                    'FWPOLICY', 'CFPROTOCOLLST', 'GLBCFFUNC'],
        '地址池与承载': ['POOL', 'POOLGROUP', 'POOLBINDGROUP', 'POOLGRPMAP',
                       'SECTION', 'INTERFACE', 'LOGICINF', 'IFIPV4ADDRESS',
                       'IFIPV6ADDRESS', 'IFIPV6ENABLE', 'IPBINDVPN', 'SRROUTE',
                       'SRROUTE6', 'NETWORKROUTE', 'GRETUNNEL', 'VPNINST',
                       'L3VPNINST', 'VPNINSTAF'],
        'APN 与移动性': ['APN', 'CPAPN', 'APNIMSSIGFLTR', 'APNUSRPROFG',
                        'APNIPALLOCRULE', 'APNQOSATTR', 'APNSOFTPARA', 'APNPCCFUNC',
                        'APNIDLETIME', 'APNCHARGECTRL', 'APNIMSATTR', 'APNADDRESSATTR',
                        'CONNECTPLMN', 'HPLMN', 'PNFDNN', 'NSDNN', 'PNFSMFSERAREA',
                        'PNFNS', 'PNFPROFILE', 'PNFTAIRANGE', 'TAIRANGELIST',
                        'TACRANGE', 'UPAREA', 'UPAREABINDN2TAI', 'UPNODE',
                        'UPBINDS11', 'UPIPDOMAIN', 'LOCBINDAREA', 'BSFIPRANGEBIND',
                        'PEERNFIPLIST', 'SUPI', 'TAIGROUP', 'N2TACID', 'S1TACID'],
        'IMS / P-CSCF': ['PCSCFIP', 'PCSCFGROUP', 'PCSCFGRPBNDAPN',
                        'PCSCFIMSISDNSEG', 'IMSIBINDUP'],
        '网络切片': ['SNSSAI'],
        '刷新与开关': ['REFRESHSRV', 'LICENSESWITCH', 'DEACTIVERATE'],
    }

    out = {}
    used = set()
    for gname, kws in GROUPS.items():
        items = []
        for f in fams:
            if f in kws and f not in used:
                bn = biz_name(f)
                if bn:
                    items.append(bn)
                    used.add(f)
        if items:
            # 去重保序
            seen = set()
            uniq = []
            for x in items:
                if x not in seen:
                    seen.add(x)
                    uniq.append(x)
            out[gname] = uniq

    # 未分组的
    rest = [f for f in fams if f not in used]
    if rest:
        out['其他'] = rest
    return out


if __name__ == '__main__':
    import sys
    gt = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    tk = sys.argv[1] if len(sys.argv) > 1 else 'NC20260831000131'
    g = next((x for x in gt if x['ticket'] == tk), None)
    if not g:
        print('找不到工单')
        sys.exit(1)

    fams = sorted({f for _, v, f, p, _ in g['kept']})
    groups = group_families(fams)
    print(f'{tk}  GT {len(g["kept"])} 条 / {len(fams)} 族\n')
    for gname, items in groups.items():
        print(f'【{gname}】')
        for x in items:
            print(f'  · {x}')
        print()
