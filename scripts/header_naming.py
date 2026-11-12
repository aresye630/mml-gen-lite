"""表头命名：把 MML 参数名转成自然语言描述。

★ 2026-11-12（用户要求）
  「表头不能是参数名，就是通用的自然语言描述（查询参数知识获取，
    且可以做多样性描述，比如IP地址，IPADDR，v4地址等等）」
  「这里很多都需要 llm 来做（描述多样性）」

## 三档映射

  第 1 档 PARAM_BIZ_CURATED   人工精校（高频参数，准确）
  第 2 档 语素推导            按大写字母切分 + 语素词典拼接（实测 85% 有效）
  第 3 档 LLM 兜底            前两档都失败时，调 LLM 生成 + 缓存

## 多样性

  同一参数可能有多种等价说法（IP地址 / 接口IP地址 / v4地址）。
  用 hash 固定选择，保证：
    · 同一参数在同一份清单里写法一致
    · 不同参数之间写法有差异（像不同人写的）
    · 不同工单之间同一参数写法可能不同（避免 agent 学到词→参数的硬映射）

## 为什么需要多样性

  如果所有清单都用「接口IP地址」指 IFIPADDR，agent 会学到这个映射，
  换一批清单就失效。多样性让 agent 必须靠「理解业务语义 + 查 EXP 参数」
  来判断，而不是死记表头。
"""
import hashlib
import json
import re
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 第 1 档：人工精校映射（高频、易错的参数）
# ═══════════════════════════════════════════════════════════
PARAM_BIZ_CURATED = {
    # 地址类
    'IFIPADDR': '接口IP地址',
    'SUBNETMASK': '掩码',
    'IPV4ADDRESS': 'IPv4地址',
    'IPV6ADDRESS': 'IPv6地址',
    'IPV4ADDRESS1': 'IPv4地址',
    'IPV6ADDRESS1': 'IPv6地址',
    'IPV4MASK1': 'IPv4掩码',
    'IPV6PREFIXLEN1': 'IPv6前缀长度',
    'NETWORKADDRESS': '网络地址',
    'MASKLEN': '掩码长度',
    'V4STARTIP': '起始IPv4地址',
    'V4ENDIP': '结束IPv4地址',
    'V6PREFIXSTART': '起始IPv6前缀',
    'V6PREFIXEND': '结束IPv6前缀',
    'V6PREFIXLENGTH': 'IPv6前缀长度',
    'SRCIPV6ADDR': '源IPv6地址',
    'DSTIPV6ADDR': '目的IPv6地址',
    'PCSCFIPV6': 'P-CSCF的IPv6地址',
    'SERVERIPV6': '服务器IPv6地址',
    'AGGREADDRESSV6': '聚合读IPv6地址',
    'DSTIPADDR': '目的IP地址',
    'PEERADDR': '对端地址',
    'PEERADDRV6': '对端IPv6地址',

    # 名称类
    'APN': 'APN',
    'DNN': 'DNN',
    'VRFNAME': 'VRF名称',
    'USERPROFILENAME': '用户模板名称',
    'POOLNAME': '地址池名称',
    'POOLGROUPNAME': '地址池组名称',
    'POOLGRPNAME': '地址池组名称',
    'URRNAME': 'URR名称',
    'RULENAME': '规则名称',
    'PCCPOLICYGRPNM': '策略组名称',
    'URRGROUPNAME': 'URR组名称',
    'USERPROFGNAME': '用户模板组名称',
    'FLOWFILTERNAME': '流过滤器名称',
    'FILTERNAME': '过滤器名称',
    'IFNAME': '接口名称',
    'NAME': '名称',
    'MAPPINGNAME': '映射名称',
    'GROUPNAME': '组名称',
    'LICITEM': 'License项',
    'VPNINSTANCE': 'VPN实例名称',
    'POLICYNAME': '策略名称',
    'BINDNWDAFINFOID': '绑定的NWDAF信息标识',
    'BINDSMFINFOID': '绑定的SMF信息标识',
    'BSFINSTANCENAME': 'BSF实例名称',
    'BFDTEMPLATENAME': 'BFD模板名称',
    'DNNSMARTPLCY': 'DNN智能策略名称',

    # 编号/标识类
    'URRID': 'URR编号',
    'INDEX': '索引',
    'PNFNSINDEX': 'PNFNS索引',
    'NFINSTANCEID': 'NF实例标识',
    'UPFINSTANCEID': 'UPF实例标识',
    'GROUPID': '组标识',
    'AREANAME': '区域名称',
    'AREAID': '区域标识',
    'TACRANGEINDEX': 'TAC范围索引',
    'TACSECNUM': 'TAC段编号',
    'SECTIONNUM': '地址段编号',
    'PRIORITY': '优先级',
    'MCC': 'MCC',
    'MNC': 'MNC',
    'NOID': '编号',

    # 描述类
    'DESC': '描述',
    'DESCRIPTION': '描述',
    'CPDESCRIPTION': 'CP描述',
    'IFDESCR': '接口描述',
    'VRFDESCRIPTION': 'VRF描述',
    'DNAI': 'DNAI',
    'FQDN': 'FQDN',
    'DNN': 'DNN',
    'APNNI': 'APN网络标识',
    'ACCESSNAME': '接入点名称',
    'CPNAME': 'CP名称',
    'CCNAME': '计费特性名称',
    'CCTEMPLATE': '计费特性模板',
    'SEMANTICS': '语义',

    # 号码/IMSI 类
    'ENDIMSI': '结束IMSI',
    'ISPREV6PREFIX': 'IPv6前缀',
    'NVALUE': '数量',
}

# ═══════════════════════════════════════════════════════════
# 第 2 档：语素词典（用于规则推导）
# ═══════════════════════════════════════════════════════════
MORPHEMES = {
    # 通用名词
    'NAME': '名称', 'ID': '标识', 'INDEX': '索引', 'NUM': '编号',
    'NUMBER': '数量', 'COUNT': '数量', 'SEQ': '序号', 'SIZE': '大小',
    'LEN': '长度', 'LENGTH': '长度', 'TYPE': '类型', 'MODE': '模式',
    'DESC': '描述', 'DESCRIPTION': '描述',
    # 地址
    'ADDR': '地址', 'ADDRESS': '地址', 'IP': 'IP', 'MASK': '掩码',
    'NET': '网络', 'NETWORK': '网络', 'SUBNET': '子网', 'PORT': '端口',
    'MAC': 'MAC', 'VLAN': 'VLAN', 'FQDN': 'FQDN', 'DOMAIN': '域名',
    'URI': 'URI', 'URL': 'URL', 'PATH': '路径', 'PREFIX': '前缀',
    # 网络对象
    'APN': 'APN', 'DNN': 'DNN', 'VRF': 'VRF', 'VPN': 'VPN',
    'POOL': '地址池', 'SECTION': '地址段', 'FILTER': '过滤器',
    'FLOW': '流', 'RULE': '规则', 'POLICY': '策略', 'PROFILE': '模板',
    'TEMPLATE': '模板', 'GROUP': '组', 'GRP': '组', 'FARM': 'Farm',
    'INTERFACE': '接口', 'IF': '接口', 'NODE': '节点', 'INSTANCE': '实例',
    'HOST': '主机', 'SERVER': '服务器', 'CLIENT': '客户端', 'PEER': '对端',
    'USER': '用户', 'SESSION': '会话', 'SERVICE': '服务', 'APP': '应用',
    # 无线/核心网
    'IMSI': 'IMSI', 'IMEI': 'IMEI', 'IMEISV': 'IMEISV', 'MSISDN': '号码',
    'PLMN': 'PLMN', 'MCC': 'MCC', 'MNC': 'MNC', 'TAC': 'TAC',
    'TAI': 'TAI', 'QCI': 'QCI', 'QOS': 'QoS', 'QFI': 'QFI',
    'SLICE': '切片', 'PDU': 'PDU', 'SSC': 'SSC', 'GUTI': 'GUTI',
    'AMF': 'AMF', 'SMF': 'SMF', 'UPF': 'UPF', 'PCF': 'PCF',
    'BSF': 'BSF', 'NRF': 'NRF', 'UDM': 'UDM', 'NSSF': 'NSSF',
    'NWDAF': 'NWDAF', 'AUSF': 'AUSF', 'UDR': 'UDR',
    # 属性
    'PRIORITY': '优先级', 'PRI': '优先级', 'WEIGHT': '权重',
    'RATE': '速率', 'SPEED': '速率', 'BANDWIDTH': '带宽',
    'TIMER': '定时器', 'TIME': '时间', 'DELAY': '延迟',
    'BUF': '缓冲', 'BUFFER': '缓冲', 'SWITCH': '开关', 'FLAG': '标志',
    'STATUS': '状态', 'STATE': '状态', 'VALUE': '值',
    # 方向
    'SRC': '源', 'SOURCE': '源', 'DST': '目的', 'DEST': '目的',
    'UP': '上行', 'DOWN': '下行', 'UL': '上行', 'DL': '下行',
    'IN': '入', 'OUT': '出', 'LOCAL': '本地', 'REMOTE': '远端',
    'START': '起始', 'END': '结束', 'BEGIN': '起始',
    'MIN': '最小', 'MAX': '最大', 'DEF': '默认', 'DEFAULT': '默认',
    # IP 版本
    'V4': 'IPv4', 'V6': 'IPv6', 'IPV4': 'IPv4', 'IPV6': 'IPv6',
    # ★ 2026-11-12 补充：从实测 67 种缺口里补的
    'URR': 'URR', 'GRP': '组', 'SEG': '段', 'SEGMENT': '段',
    'SRV': '服务', 'SVR': '服务器', 'NF': 'NF', 'VTEP': 'VTEP',
    'VXLAN': 'VXLAN', 'CTX': '上下文', 'INTF': '接口', 'IF': '接口',
    'PROTOCOL': '协议', 'PROP': '属性', 'PARA': '参数', 'PARAM': '参数',
    'EMG': '紧急', 'FW': '防火墙', 'RD': 'RD', 'VN': '虚拟网络',
    'LOCATION': '位置', 'LOCALITY': '位置', 'PRE': '预',
    'PWD': '密码', 'PSWD': '密码', 'PASSWORD': '密码',
    'KEY': '密钥', 'AUTH': '鉴权', 'TEXT': '文本', 'MD5': 'MD5',
    'HOST': '主机', 'NEXT': '下一跳', 'HOP': '跳',
    'HYST': ' hysteresis', 'HYSTERESIS': '迟滞',
    'SELPLY': '选择策略', 'USRPROF': '用户模板',
    'DFT': '默认', 'DFTSIG': '默认信令', 'PRT': '端口',
    'MPCSCF': 'MPCSCF', 'TELSHUNT': '话务旁路', 'INTELSHUNT': '智能旁路',

    # 杂项
    'URI': 'URI', 'RANGE': '范围', 'LIST': '列表', 'SET': '集合',
    'BIND': '绑定', 'BINDING': '绑定', 'MAP': '映射', 'MAPPING': '映射',
    'ROUTE': '路由', 'GATEWAY': '网关', 'ROUTER': '路由器',
    'CHARGE': '计费', 'CHARGING': '计费', 'RATING': '计费',
    'LIC': 'License', 'LICENSE': 'License', 'ITEM': '项',
    'TCP': 'TCP', 'UDP': 'UDP', 'MSS': 'MSS', 'MTU': 'MTU',
    'QOS': 'QoS', 'GBR': 'GBR', 'ARP': 'ARP',
}

# ═══════════════════════════════════════════════════════════
# 第 3 档：表头多样性变体
# ═══════════════════════════════════════════════════════════
HEADER_VARIANTS = {
    'IFIPADDR': ['接口IP地址', 'IP地址', '接口地址', 'IPv4地址'],
    'SUBNETMASK': ['掩码', '子网掩码', '掩码长度'],
    'IPV4ADDRESS': ['IPv4地址', 'IP地址', 'v4地址'],
    'IPV6ADDRESS': ['IPv6地址', 'IP地址', 'v6地址'],
    'USERPROFILENAME': ['用户模板名称', '模板名', '用户模板'],
    'POOLNAME': ['地址池名称', '池名', '地址池'],
    'POOLGROUPNAME': ['地址池组名称', '池组名', '地址池组'],
    'URRNAME': ['URR名称', '计费规则名称', 'URR'],
    'RULENAME': ['规则名称', '策略规则名称', '规则'],
    'VRFNAME': ['VRF名称', 'VRF', 'VPN实例名称'],
    'FLOWFILTERNAME': ['流过滤器名称', '流过滤器', '五元组名称'],
    'FILTERNAME': ['过滤器名称', '过滤器'],
    'PRIORITY': ['优先级', '权重', '优先顺序'],
    'MCC': ['MCC', '移动国家码'],
    'MNC': ['MNC', '移动网络码'],
    'DNN': ['DNN', '数据网络名称'],
    'APN': ['APN', '接入点名'],
    'IFNAME': ['接口名称', '接口名', '端口'],
    'SECTIONNUM': ['地址段编号', '段编号', '地址段序号'],
    'URRID': ['URR编号', '计费标识', 'URR ID'],
}


def _hash_pick(pname, options):
    """用参数名哈希稳定选择变体（同参数同工单保持一致）。"""
    if not options:
        return None
    h = int(hashlib.md5(pname.encode()).hexdigest()[:8], 16)
    return options[h % len(options)]


def infer_cn_name(pname):
    """第 2 档：语素规则推导。

    按「贪心最长匹配」把参数名切成语素，逐个查表拼接。
    实测：IFIPADDR → 接口IP地址、FLOWFILTERNAME → 流过滤器名称
    """
    if not pname:
        return None

    parts = []
    s = pname.upper()
    i = 0
    while i < len(s):
        matched = False
        for ln in range(min(12, len(s) - i), 0, -1):
            sub = s[i:i + ln]
            if sub in MORPHEMES:
                parts.append(MORPHEMES[sub])
                i += ln
                matched = True
                break
        if not matched:
            if s[i].isdigit():
                parts.append(s[i])
            i += 1

    if not parts:
        return None

    out = ''.join(parts)
    # ★ 2026-11-12 修：尾部数字 6 通常是 IPv6 后缀（BEGINADDR6 → 起始IPv6地址）
    #   实测 BEGINADDR6 → 「起始地址6」，AGGRESSV6 → 「地址6」
    #   规则：结尾的 6 且在 ADDR/ADDRESS 之后 → 转成 IPv6 前缀
    if out.endswith('6') and ('地址6' in out or '前缀6' in out):
        out = out.replace('地址6', 'IPv6地址').replace('前缀6', 'IPv6前缀')
    # 过滤掉明显不对的结果（单字符、纯数字）
    if len(out) < 2 or out.isdigit():
        return None
    return out


def header_for(pname, use_variant=True):
    """主入口：参数名 → 自然语言表头。

    优先级：精校映射（含变体） > 语素推导 > None（调用方走 LLM 或兜底）
    """
    if not pname:
        return None
    p = pname.upper()

    # 第 1 档：精校 + 变体
    base = PARAM_BIZ_CURATED.get(p)
    if base:
        if use_variant and p in HEADER_VARIANTS:
            return _hash_pick(p, HEADER_VARIANTS[p])
        return base

    # 第 2 档：语素推导
    inferred = infer_cn_name(p)
    if inferred:
        if use_variant and p in HEADER_VARIANTS:
            return _hash_pick(p, HEADER_VARIANTS[p])
        return inferred

    return None


# ═══════════════════════════════════════════════════════════
# LLM 兜底（带缓存）
# ═══════════════════════════════════════════════════════════
LLM_CACHE_PATH = Path('/tmp/header_llm_cache.json')


def _load_llm_cache():
    if LLM_CACHE_PATH.exists():
        try:
            return json.loads(LLM_CACHE_PATH.read_text(encoding='utf-8'))
        except Exception:
            return {}
    return {}


def _save_llm_cache(cache):
    try:
        LLM_CACHE_PATH.write_text(
            json.dumps(cache, ensure_ascii=False, indent=1), encoding='utf-8')
    except Exception:
        pass


def collect_unmapped(param_names):
    """找出前三档都失败、需要 LLM 兜底的参数。"""
    cache = _load_llm_cache()
    need = []
    for p in param_names:
        if header_for(p) or p.upper() in cache:
            continue
        need.append(p.upper())
    return sorted(set(need))


def apply_llm_results(mapping):
    """把 LLM 生成的表头写入缓存。"""
    cache = _load_llm_cache()
    cache.update({k.upper(): v for k, v in mapping.items()})
    _save_llm_cache(cache)


def header_for_with_cache(pname):
    """带 LLM 缓存的表头查询（推荐用这个）。"""
    h = header_for(pname)
    if h:
        return h
    cache = _load_llm_cache()
    return cache.get(pname.upper())


if __name__ == '__main__':
    import json as _json

    GT = _json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    # 收集全部引号值参数
    quoted = set()
    for g in GT:
        if not g['kept']:
            continue
        for _, v, fam, params, raw in g['kept']:
            for pname in params:
                m = re.search(rf'\b{re.escape(pname)}\s*=\s*("?[^",;]+"?)', raw)
                if m and m.group(1).startswith('"'):
                    quoted.add(pname.upper())

    print('=' * 90)
    print(f'表头命名覆盖率检查（引号值参数 {len(quoted)} 个）')
    print('=' * 90)

    ok_curated, ok_infer, fail = [], [], []
    for p in sorted(quoted):
        if p in PARAM_BIZ_CURATED:
            ok_curated.append(p)
        elif infer_cn_name(p):
            ok_infer.append(p)
        else:
            fail.append(p)

    print(f'\n第1档 精校映射: {len(ok_curated)} ({len(ok_curated)/len(quoted)*100:.0f}%)')
    print(f'第2档 语素推导: {len(ok_infer)} ({len(ok_infer)/len(quoted)*100:.0f}%)')
    print(f'需 LLM 兜底:   {len(fail)} ({len(fail)/len(quoted)*100:.0f}%)')

    print(f'\n=== 需 LLM 兜底的参数 ===')
    for p in fail:
        print(f'  {p}')

    print(f'\n=== 抽样：表头多样性效果（同一参数不同工单可能不同写法）===')
    SAMPLES = ['IFIPADDR', 'SUBNETMASK', 'APN', 'USERPROFILENAME',
               'POOLNAME', 'PRIORITY', 'PCCPOLICYGRPNM', 'FLOWFILTERNAME']
    for p in SAMPLES:
        h = header_for(p)
        variants = HEADER_VARIANTS.get(p, [])
        print(f'  {p:<22} → {h or "❌"}')
        if variants:
            print(f'     可选变体: {variants}')
