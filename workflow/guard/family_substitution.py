"""G28：族名「张冠李戴」检测（prompt 的兜底）。

用户要求（2026-11-10）：
  「所有的 prompt 增强，不一定能稳定的解决问题，
    后续这种方案都要有对应的兜底策略。」

背景实测（NC20260803000197）：
  意图要「NF TAI 区域信息」「UPF服务区名称绑定的5G TAI范围」
  GT 用的是 TAIRANGELIST / UPAREABINDN2TAI（UNC 网元）
  agent 在 UDG 找不到，就选了 TAIGROUP / TAIGROUPBINDING 顶替
  → 生成了一条错误的配置，而且是「确认」状态，看起来很有把握

判据设计（不硬编码任何产品名 / 网元名）：
  读规划表，找出「命令族」列的族名与「业务对象」列的业务描述
  词根不匹配的行 → warn。

  匹配判断：把业务对象描述拆成中文词块，
  和族的英文名做模糊比对（族名拆词后是否出现在业务描述里）。

  这是启发式，只做 warn，不判 fatal。
"""
import re
from pathlib import Path

# 业务对象描述里的中文 → 族名可能的英文片段
# 只做通用的语义映射，不绑定任何具体产品
ZH_EN = {
    '区域': ['AREA', 'RANGE', 'REGION'],
    '范围': ['RANGE', 'AREA'],
    '列表': ['LIST'],
    '绑定': ['BIND'],
    '服务区': ['AREA', 'AREAINFO'],
    '跟踪区': ['TAI', 'TAC', 'TRACKING'],
    '过滤器': ['FILTER'],
    '规则': ['RULE'],
    '策略': ['POLICY'],
    '地址池': ['POOL'],
    '隧道': ['TUNNEL', 'TNL'],
    '路由': ['ROUTE'],
    '接口': ['INTERFACE', 'IF'],
    '用户模板': ['USERPROFILE', 'PROFILE'],
    '计费': ['CHARG', 'URR'],
    '切片': ['SNSSAI', 'SLICE'],
    '域名': ['HOST', 'DOMAIN'],
    '服务器': ['SERVER', 'SVR'],
    '定时器': ['TIMER'],
    '参数': ['PARA'],
    '开关': ['SWITCH'],
}


# 常见族名缩写 → 完整词（帮助拆词和匹配）
ABBR = {
    'SVR': 'SERVER', 'FLT': 'FILTER', 'TNL': 'TUNNEL',
    'IF': 'INTERFACE', 'PROF': 'PROFILE', 'CHARG': 'CHARGING',
    'PARA': 'PARAMETER', 'CFG': 'CONFIG', 'BIND': 'BIND',
}


def _words(text):
    """把族名拆成词块。

    ★ 2026-11-10：原实现只按「连续大写」拆，NTPSVR 会得到一个整词，
      无法匹配 SERVER/SVR → 造成误报。
      现在再加一层：在已知缩写处切分。
    """
    u = text.upper()

    # 第一层：已知缩写前后切分（长缩写优先）
    for abbr in sorted(ABBR, key=len, reverse=True):
        u = u.replace(abbr, f'|{abbr}|')

    parts = re.findall(r'[A-Z]+[0-9]*', u)
    out = set()
    for p in parts:
        if len(p) < 2:
            continue
        out.add(p)
        # 缩写同时贡献全称
        if p in ABBR:
            out.add(ABBR[p])
    # 短缩写也保留（TAI/AREA 等）
    return sorted(out)


def _biz_tokens(desc):
    """业务描述 → 可能对应的英文片段集合。"""
    out = set()
    for zh, ens in ZH_EN.items():
        if zh in desc:
            out.update(ens)
    return out


def parse_plan_rows(plan_text):
    """解析规划表，返回 [{biz, family, status}]。"""
    rows = []
    if not plan_text:
        return rows

    lines = plan_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue
        header = [c.strip() for c in line.strip().strip('|').split('|')]
        if '命令族' not in header or '业务对象' not in header:
            i += 1
            continue

        fam_idx = header.index('命令族')
        biz_idx = header.index('业务对象')
        st_idx = header.index('状态') if '状态' in header else None
        ncol = len(header)

        i += 1
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1

        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) >= ncol:
                rows.append({
                    'biz': cells[biz_idx],
                    'family': cells[fam_idx],
                    'status': cells[st_idx] if (st_idx is not None and st_idx < len(cells)) else '',
                })
            i += 1
        continue
    return rows


def check_family_substitution(sess_dir):
    """检查规划表里「族名和业务对象对不上」的行。

    Returns:
      {
        'ok': bool,
        'skipped': bool,
        'suspicious': [{biz, family, why}],
      }
    """
    adir = Path(sess_dir) / 'analysis_code'
    plan_p = adir / '命令族规划.md'
    if not plan_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无规划表', 'suspicious': []}

    plan_text = plan_p.read_text(encoding='utf-8', errors='replace')
    rows = parse_plan_rows(plan_text)
    if not rows:
        return {'ok': True, 'skipped': True, 'reason': '规划表解析为空', 'suspicious': []}

    suspicious = []
    for r in rows:
        fam = (r['family'] or '').strip().upper()
        biz = r['biz'] or ''
        status = r['status'] or ''

        # 跳过：没有族名 / 标了未找到 / 跳过
        if not fam or '无' in fam or '未找到' in fam or '跳过' in status:
            continue

        # 提取族名（可能带 ADD/MOD 前缀）
        m = re.match(r'^(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]+)$', fam)
        bare = m.group(1) if m else fam
        if not re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', bare):
            continue

        fam_words = _words(bare)
        biz_tok = _biz_tokens(biz)

        # 业务描述里没有可识别的词 → 无法判断，跳过
        if not biz_tok:
            continue

        # 族名拆出的词，有没有落在业务描述的可能词里
        # 双向匹配：族名词 in 业务词，或 业务词 in 族名词
        hit = any(
            w in biz_tok or any(b in w or w in b for b in biz_tok)
            for w in fam_words
        )
        if not hit:
            suspicious.append({
                'biz': biz[:60],
                'family': bare,
                'why': f'族名拆词 {fam_words} 与业务描述的可能词 {sorted(biz_tok)} 无交集',
            })

    return {
        'ok': not suspicious,
        'skipped': False,
        'n_rows': len(rows),
        'suspicious': suspicious[:8],
    }


if __name__ == '__main__':
    import json
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(check_family_substitution(sd), ensure_ascii=False, indent=1))
