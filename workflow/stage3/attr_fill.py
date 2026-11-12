"""Step 3：属性族链补齐。

★ 2026-11-12 P0-4

## 实测数据驱动的设计（有反直觉结论）

### 发现 1：属性族覆盖率无法区分「要不要配」
NC20260810002261 的 UNC EXP 里，21 个 APN 属性族的实例覆盖率都是 100%
（333 个 APN 实例全都配了），但 GT 只要其中 6 个。
→ 「现网多数都配了」这个判据完全无效。

原因：GT = 本次变更的命令，EXP = 现网完整配置。
     GT 里没出现 ≠ 不需要配，只是本次没改。

### 发现 2：三种候选策略的多配量
| 策略 | 候选族数 | 命中 GT | 多配 |
|---|---|---|---|
| A EXP 全量属性族 | 44 | 7 | 37 |
| B 参照对象（ims.wh）配过的 | 22 | 8 | 14 |
| C 参照 ∩ 数据清单提及 | 0 | 0 | 0 |

策略 C 不可行：数据清单的列名是业务说法（「优先级」「IPv6地址」「名称」），
没有任何 MML 族名或参数名线索。

### 发现 3：策略 B 的漏配
ims.wh 有 22 族，GT 要 12 族，命中 8 个。漏的 4 个：
  · APN               ← 对象本体，由 Step 2 覆盖
  · APNADDRESSATTR    ← ims.wh 恰好没配（个例）
  · APNIMSSIGFLTR     ← 意图明确提到，由 Step 2 覆盖
  · APNSGLPASS        ← ims.wh 恰好没配

## 采用的设计（按用户裁定）

用户裁定：「直接配，多配的这些标明注释让判断
          （让用户删比让用户再补意图交互要简单）」

所以：
  1. 候选来源 = 参照对象的完整属性配置（策略 B）
     + 意图明确点名的族（由 Step 2 提供）
     + 同族「业务必备」的族（覆盖率极高的，作为兜底）
  2. 全部生成，但每条命令标 @stage3=attr_chain 注释
  3. 无法确定参数值的，标【待填写】
  4. 生成结果进澄清清单，让用户 review

## 边界控制（避免补出几十个无关族）

  · 只补 owner_family 直接挂载的属性族（exp_attr_chain 返回的）
  · 不算跨族引用链（那是 Step 6 的事）
  · 每族每个实例最多补 1 条命令（属性配置通常一对一）
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

MCP_DIR = str(Path(__file__).parent.parent / 'mcp')
import sys as _sys
if MCP_DIR not in _sys.path:
    _sys.path.insert(0, MCP_DIR)

try:
    import mcp_exp as _MCP
except Exception:
    _MCP = None


# ★ 2026-11-12：owner 族的身份参数在不同属性族里写法不同
#   实测 APN 的 owner 参数名有：APN / APNNAME / APN名称
#   实测 USERPROFILE 的有：USERPROFILENAME
#   实测 POOL 的有：POOLNAME / POOLGRPNAME
OWNER_PK_CANDIDATES = {
    'APN': ('APN', 'APNNAME', 'APNNAME_'),
    'USERPROFILE': ('USERPROFILENAME', 'USERPROFILE'),
    'USRPROFGROUP': ('USERPROFGNAME', 'USRPROFGROUPNAME'),
    'POOL': ('POOLNAME', 'POOL'),
    'POOLGROUP': ('POOLGROUPNAME', 'POOLGRPNAME', 'POOLGROUP'),
    'INTERFACE': ('IFNAME', 'INTERFACE'),
    'URR': ('URRNAME', 'URR'),
    'RULE': ('RULENAME', 'RULE'),
}


def _owner_pk_names(owner_family):
    """返回该 owner 族的身份参数名候选。"""
    return OWNER_PK_CANDIDATES.get(
        owner_family, (owner_family, owner_family + 'NAME'))


# 覆盖率阈值：作为「业务必备族」的兜底判据
MUSTHAVE_COVERAGE = 0.9


def _scan_attr_usage(exp_paths, owner_family, owner_values=None):
    """扫描 EXP，统计每个属性族被多少个 owner 实例配了。

    ★ 2026-11-12 修 bug（旧实现覆盖率算成 0.3%）：
      旧实现对 owner_values 里的值统计 attr_coverage，
      导致覆盖率 = 1/333（分子只有一个 owner，分母是全部）。
      正确做法：
        attr_coverage 统计【全部】owner（用于「业务必备」判据）
        owner_attrs   只记录 owner_values 里那些（用于「参照配了哪些」）

    返回:
      {
        'n_owners': 333,
        'attr_coverage': {'APNQOSATTR': 333, ...},
        'attr_samples': {'APNQOSATTR': 'SET APNQOSATTR:...'},
        'owner_attrs': {'ims.wh': {'APNQOSATTR', ...}},
      }
    """
    if isinstance(exp_paths, (str, Path)):
        exp_paths = [exp_paths]

    owners = set()
    attr_coverage = Counter()
    attr_samples = {}
    owner_attrs = defaultdict(set)
    ov_set = set(owner_values or [])
    seen_pairs = set()      # ★ 修重复计数：(族, owner) 去重

    # 第一遍：收集全部 owner 实例
    for ep in exp_paths:
        p = Path(ep)
        if not p.exists():
            continue
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    m0 = re.match(
                        rf'^ADD\s+{re.escape(owner_family)}\s*:\s*'
                        rf'[A-Z][A-Z0-9_]*\s*=\s*"([^"]+)"', s)
                    if m0:
                        owners.add(m0.group(1))
        except Exception:
            continue

    all_owner_vals = owners
    if not all_owner_vals:
        return {'n_owners': 0, 'attr_coverage': {}, 'attr_samples': {},
                'owner_attrs': {}}

    # 第二遍：统计属性族覆盖 + 参照对象的明细
    for ep in exp_paths:
        p = Path(ep)
        if not p.exists():
            continue
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    m = re.match(
                        r'^(SET|ADD|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*'
                        r'([A-Z][A-Z0-9_]*)\s*=\s*"([^"]+)"', s)
                    if not m:
                        continue
                    verb, fam, pk, val = m.groups()
                    if fam == owner_family:
                        continue
                    # ★ 2026-11-12：必须用 owner 身份参数名判断，
                    #   不能只看「值在 owner 集合里」
                    #   实测 SET BACKOFFTIME:APNNAME="x" 的 pk 是 APNNAME 不是 APN
                    if pk not in _owner_pk_names(owner_family):
                        continue
                    if val not in all_owner_vals:
                        continue
                    # ★ 2026-11-12 去重：同一 (族, owner) 在 UDG+UNC 各出现一次，
                    #   旧实现重复计数导致覆盖率 104.5%
                    pair = (fam, val)
                    if pair not in seen_pairs:
                        seen_pairs.add(pair)
                        attr_coverage[fam] += 1
                    if val in ov_set:
                        owner_attrs[val].add(fam)
                    if fam not in attr_samples:
                        attr_samples[fam] = s
        except Exception:
            continue

    return {
        'n_owners': len(owners),
        'attr_coverage': dict(attr_coverage),
        'attr_samples': attr_samples,
        'owner_attrs': dict(owner_attrs),
    }


def collect_attr_candidates(exp_paths, owner_family, ref_owner_value,
                            intent_mentioned_fams=None):
    """收集属性族候选（策略 B + 意图点名 + 业务必备兜底）。

    参数：
      exp_paths              EXP 路径列表
      owner_family           owner 族名（如 'APN' / 'USERPROFILE'）
      ref_owner_value        参照对象的实例名（如 'ims.wh'）；None 表示自动选
      intent_mentioned_fams  意图里明确提到的族（来自 Step 2）

    返回：
      {
        'owner_family': 'APN',
        'ref_owner': 'ims.wh',
        'candidates': [
            {'family': 'APNCHARGECTRL', 'source': 'ref'|'intent'|'musthave',
             'coverage': 1.0, 'sample': 'SET ...', 'n_params_needed': None},
        ],
        'stats': {...}
      }
    """
    # ★ 2026-11-12：如果没指定参照对象的属性配置，用「覆盖最全」的自动兜底
    #   实测：意图说「按 ims.wh 配齐」时 ref_owner_value='ims.wh'（22 族）
    #        未指定时自动选 cmiotjwwst.hb（47 族，覆盖最全但可能含不相干的）
    auto_selected = False
    if not ref_owner_value:
        auto, _rank = find_ref_owner_for_attrchain(exp_paths, owner_family)
        if auto:
            ref_owner_value = auto
            auto_selected = True

    usage = _scan_attr_usage(exp_paths, owner_family,
                             [ref_owner_value] if ref_owner_value else [])

    cands = {}

    # ── 来源 1：参照对象实际配了的族（策略 B）──
    if ref_owner_value:
        for fam in usage['owner_attrs'].get(ref_owner_value, set()):
            cands[fam] = {
                'family': fam,
                'source': 'ref',
                'coverage': (usage['attr_coverage'].get(fam, 0)
                             / max(1, usage['n_owners'])),
                'sample': usage['attr_samples'].get(fam, ''),
            }

    # ── 来源 2：意图明确点名的族 ──
    #   ★ 2026-11-12：如果该族已在 ref 来源里，把来源升级为 intent
    #     （意图点名比参照推断更可信，置信度都算 high，但来源标记要准确）
    for fam in (intent_mentioned_fams or []):
        if fam in cands:
            cands[fam]['source'] = 'intent'
            cands[fam]['from_ref_too'] = True
        else:
            cands[fam] = {
                'family': fam,
                'source': 'intent',
                'coverage': (usage['attr_coverage'].get(fam, 0)
                             / max(1, usage['n_owners'])),
                'sample': usage['attr_samples'].get(fam, ''),
            }

    # ── 来源 3：业务必备族兜底（覆盖率 >= 90%）──
    #   为什么需要：参照对象可能有遗漏（实测 ims.wh 没配 APNADDRESSATTR，
    #   但 333 个 APN 里绝大多数都配了）
    n_owners = max(1, usage['n_owners'])
    for fam, cnt in usage['attr_coverage'].items():
        cov = cnt / n_owners
        if cov >= MUSTHAVE_COVERAGE and fam not in cands:
            cands[fam] = {
                'family': fam,
                'source': 'musthave',
                'coverage': cov,
                'sample': usage['attr_samples'].get(fam, ''),
            }

    return {
        'owner_family': owner_family,
        'ref_owner': ref_owner_value,
        'ref_auto_selected': auto_selected,
        'candidates': sorted(cands.values(),
                             key=lambda x: (-x['coverage'], x['family'])),
        'stats': {
            'n_owners': usage['n_owners'],
            'n_from_ref': sum(1 for c in cands.values() if c['source'] == 'ref'),
            'n_from_intent': sum(1 for c in cands.values() if c['source'] == 'intent'),
            'n_from_musthave': sum(1 for c in cands.values() if c['source'] == 'musthave'),
        },
    }


def generate_attr_commands(candidates, target_owner_value, exp_paths,
                           stage3_tag='@stage3=attr_chain'):
    """为候选属性族生成命令（换 owner 值，其余照抄）。

    参数：
      candidates          collect_attr_candidates 的返回
      target_owner_value  目标实例名（如 'sos'）
      exp_paths           EXP 路径（用于取完整命令）

    返回：
      {
        'commands': [{'family':..., 'cmd':..., 'annotated':..., 'source':...,
                      'coverage':..., 'confidence': 'high'|'medium'}],
        'skipped': [{'family':..., 'reason':...}],
      }
    """
    out_cmds = []
    skipped = []

    for c in candidates.get('candidates') or []:
        fam = c['family']
        sample = c.get('sample') or ''
        if not sample:
            skipped.append({'family': fam, 'reason': 'EXP 里没找到该族的命令样例'})
            continue

        # ★ 2026-11-12 修：样例里的 owner 值不一定等于 ref_owner
        #   实测：样例取自 cmiotjwwst.hb，但 ref_owner 可能是 ims.wh
        #   做法：从样例命令里提取「第一个参数的值」，那就是 owner 值
        m = re.match(
            r'^(SET|ADD|MOD)\s+[A-Z][A-Z0-9_]+\s*:\s*'
            r'([A-Z][A-Z0-9_]*)\s*=\s*"([^"]+)"', sample)
        owner_pk, owner_val_in_sample = (m.group(2), m.group(3)) if m else (None, None)
        # 校验这个参数名确实是 owner 身份参数
        of = candidates.get('owner_family')
        if owner_pk and of and owner_pk not in _owner_pk_names(of):
            skipped.append({'family': fam,
                            'reason': f'样例首参数 {owner_pk} 不是 {of} 的身份参数'})
            continue

        if not owner_val_in_sample:
            skipped.append({'family': fam,
                            'reason': '样例命令里没解析出 owner 参数值'})
            continue

        new_cmd = sample.replace(f'{owner_pk}="{owner_val_in_sample}"',
                                 f'{owner_pk}="{target_owner_value}"')
        if new_cmd == sample:
            skipped.append({'family': fam,
                            'reason': f'替换 {owner_pk} 未生效（样例: {sample[:60]}）'})
            continue

        # 置信度：ref 来源高，musthave 中（可能本次不需要）
        conf = 'high' if c['source'] in ('ref', 'intent') else 'medium'

        out_cmds.append({
            'family': fam,
            'cmd': new_cmd.rstrip(';').rstrip() + ';',
            'annotated': f'{new_cmd.rstrip(";").rstrip()};   // {stage3_tag} '
                         f'src={c["source"]} cov={c["coverage"]*100:.0f}%',
            'source': c['source'],
            'coverage': c['coverage'],
            'confidence': conf,
        })

    return {'commands': out_cmds, 'skipped': skipped}


def find_ref_owner_for_attrchain(exp_paths, owner_family):
    """如果没指定参照对象，自动选一个「属性配置最全」的 owner 实例。

    为什么：意图里可能只说「新增 APN sos」，没说照谁配。
    做法：统计每个 owner 实例配了多少种属性族，选最多的那个。
    """
    if isinstance(exp_paths, (str, Path)):
        exp_paths = [exp_paths]

    owner_attrs = defaultdict(set)
    for ep in exp_paths:
        p = Path(ep)
        if not p.exists():
            continue
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                # 先收集 owner 实例
                owners = set()
                lines = []
                for line in f:
                    s = line.strip()
                    lines.append(s)
                    m0 = re.match(
                        rf'^ADD\s+{re.escape(owner_family)}\s*:\s*'
                        rf'[A-Z][A-Z0-9_]*\s*=\s*"([^"]+)"', s)
                    if m0:
                        owners.add(m0.group(1))
                for s in lines:
                    m = re.match(
                        r'^(SET|ADD|MOD)\s+([A-Z][A-Z0-9_]+)\s*:\s*'
                        r'([A-Z][A-Z0-9_]*)\s*=\s*"([^"]+)"', s)
                    if not m:
                        continue
                    verb, fam, pk, val = m.groups()
                    if fam == owner_family:
                        continue
                    if val in owners:
                        owner_attrs[val].add(fam)
        except Exception:
            continue

    if not owner_attrs:
        return None, {}

    ranked = sorted(owner_attrs.items(), key=lambda x: -len(x[1]))
    return ranked[0][0], {k: len(v) for k, v in ranked[:5]}


if __name__ == '__main__':
    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    adir = Path(g['path']) / '备份附件'
    EXPS = [str(p) for p in sorted(adir.glob('*.txt'))]

    print('=' * 92)
    print('Step 3 属性族链补齐自测')
    print('=' * 92)

    # 自动选参照 owner
    ref, ranking = find_ref_owner_for_attrchain(EXPS, 'APN')
    print(f'\n自动选参照 owner: {ref}')
    print(f'属性族最全的 5 个: {ranking}')

    # 收集候选
    c = collect_attr_candidates(EXPS, 'APN', ref,
                                intent_mentioned_fams=['APNIMSSIGFLTR'])
    print(f'\n候选统计: {c["stats"]}')
    print(f'候选 {len(c["candidates"])} 个:')
    for x in c['candidates'][:12]:
        print(f'  {x["family"]:<24} src={x["source"]:<9} cov={x["coverage"]*100:>5.1f}%')

    # 生成命令
    r = generate_attr_commands(c, 'sos', EXPS)
    print(f'\n生成 {len(r["commands"])} 条命令，跳过 {len(r["skipped"])} 个')
    for cmd in r['commands'][:6]:
        print(f'  [{cmd["confidence"]}] {cmd["annotated"][:150]}')
