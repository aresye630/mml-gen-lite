"""链条发现：用 graph_walk 的值驱动 BFS，从上游对象发现整条下游链。

★ 2026-11-12（用户指出已有能力）
  「之前有个功能是特性指纹，我觉得可以放到阶段3，特性指纹这个功能不需要全量运行，
    按需即可，就找链条的功能就行；URR 或者其他的 FILTER 都是一样的逻辑」

## 为什么用 graph_walk 而不是自己写配对查找

  我原来写的 derive_names 只查 POOLBINDGROUP 这一个族的配对，
  只能发现 POOL → POOLGROUP 一层。

  graph_walk 是实例级引用图走链：
    对象名值 v 是枢纽 → 连接「定义方」和「引用方」→ 值驱动 BFS 递归

  给一个 POOL 名，它能一次发现：
    POOL（定义）+ POOLBINDGROUP（引用）+ SECTION（引用）+ POOLGRPMAP（间接）
    → 整条链，而且跨参数同值也能聚合

## param_scope 的作用（关键）

  None = 全维度走链 → 从 RULE 会同时沿过滤维度和计费维度走通整个 PCC 域
  指定白名单 → 只沿指定参数走，避免维度爆炸

  例：要 POOL 链，scope = {POOLNAME, POOLGROUPNAME, MAPPINGNAME}
      要 URR 链，scope = {URRNAME, URRGROUPNAME, PCCPOLICYGRPNM, RULENAME}

## 按需运行

  不是每个工单都要走链。触发条件：
    · 意图里提到「地址池组」「URR组」等下游对象，但数据清单没给名字
    · 规划表里有 ADD 上游族，但没有下游族
  单次走链约 0.1-0.5s（1.9MB EXP），比全量解析快得多。
"""
import re
import sys
from pathlib import Path

# graph_walk 在 scripts/exp_analysis_code 下
_GW_DIR = Path(__file__).parent.parent.parent / 'scripts' / 'exp_analysis_code'
if str(_GW_DIR) not in sys.path:
    sys.path.insert(0, str(_GW_DIR))


def load_commands(exp_paths, max_cmds=None):
    """把 EXP 文件读成 {seq: line} 格式（graph_walk 的输入格式）。"""
    commands = {}
    seq = 0
    for p in exp_paths:
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    if not s or s.startswith(('#', '//', '/*')):
                        continue
                    if not re.match(r'^[A-Z]{2,}\s+[A-Z0-9]+', s):
                        continue
                    seq += 1
                    commands[seq] = s
                    if max_cmds and seq >= max_cmds:
                        return commands
        except Exception:
            continue
    return commands


def find_chain(exp_paths, entry_values, param_scope=None, cross_params=None):
    """从入口对象名值出发，走链发现所有相关实例。

    entry_values: ['pool_multidomain.fzmqly_ipv4', 'pool_xxx']
    param_scope:  参数白名单（None=全维度，容易走飞）
    cross_params: 跨参数同值映射

    返回：{
      'ok': bool,
      'chain': {命令类型: [(seq, {参数: 值})]},
      'ref_degrees': {值: 引用次数},
      'stats': {instances, cmd_types, values},
      'families': [链上出现的命令族],
      'error': str
    }
    """
    try:
        import graph_walk as GW
    except ImportError as e:
        return {'ok': False, 'error': f'graph_walk 不可用: {e}',
                'chain': {}, 'ref_degrees': {}, 'stats': {}, 'families': []}

    commands = load_commands(exp_paths)
    if not commands:
        return {'ok': False, 'error': 'EXP 为空', 'chain': {},
                'ref_degrees': {}, 'stats': {}, 'families': []}

    try:
        r = GW.run(commands, entry_values, param_scope=param_scope,
                   cross_params=cross_params)
    except Exception as e:
        return {'ok': False, 'error': f'走链失败: {e}', 'chain': {},
                'ref_degrees': {}, 'stats': {}, 'families': []}

    return {
        'ok': True,
        'chain': r.get('commands', {}),
        'ref_degrees': r.get('ref_degrees', {}),
        'stats': r.get('stats', {}),
        'families': sorted(r.get('commands', {}).keys()),
        'error': None,
    }


# ═══════════════════════════════════════════════════════════
# 维度白名单（数据驱动：从 EXP 自己推断，不写死）
# ═══════════════════════════════════════════════════════════
def infer_param_scope(exp_paths, entry_family, max_depth=2):
    """从 EXP 推断「从某个族出发，应该沿哪些参数走链」。

    ★ 这比手工写白名单好，因为不同网元的参数名可能不同。

    做法：
      1. 找 entry_family 的身份参数（如 POOL 的 POOLNAME）
      2. 找所有「值引用 entry_family 身份值」的参数（如 POOLBINDGROUP.POOLNAME）
      3. 从这些族的身份参数继续往外找一层（如 POOLGROUPNAME）
      4. 收集所有经过的参数名作为 scope

    返回：set of param names
    """
    commands = load_commands(exp_paths)
    if not commands:
        return None

    try:
        from p1_parse import parse_params
    except ImportError:
        return None

    # 建值 → 参数 索引
    val_to_params = {}
    fam_identity = {}      # {族: 身份参数名}

    for seq, line in commands.items():
        m = re.match(r'^([A-Z]+)\s+([A-Z0-9]+)\s*:\s*(.*)', line)
        if not m:
            continue
        fam = m.group(2)
        params = parse_params(line)
        if not params:
            continue
        # 第一个引号参数视为身份
        first = re.search(r'^([A-Z][A-Z0-9_]*)\s*=\s*"', m.group(3))
        if first and fam not in fam_identity:
            fam_identity[fam] = first.group(1)
        for p, v in params.items():
            if v:
                val_to_params.setdefault(v, set()).add((fam, p))

    if entry_family not in fam_identity:
        return None

    scope = {fam_identity[entry_family]}
    frontier_fams = {entry_family}

    for _ in range(max_depth):
        next_fams = set()
        for fam, pname in fam_identity.items():
            if fam in frontier_fams:
                continue
            # 该族的身份值是否被 frontier 族的对象引用
            # 简化：如果该族的身份参数名出现在 frontier 族的参数里，就算相连
            for ff in frontier_fams:
                if ff in fam_identity and fam_identity[ff] in pname:
                    next_fams.add(fam)
                    scope.add(pname)
        if not next_fams:
            break
        frontier_fams = next_fams

    # 补：所有「参数名含 scope 里某个参数名的主干」的参数
    stems = {p.replace('NAME', '').replace('GRP', 'GROUP') for p in scope}
    for fam, pname in fam_identity.items():
        for st in stems:
            if st and st in pname:
                scope.add(pname)
                break

    return scope or None


if __name__ == '__main__':
    import json

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 100)
    print('链条发现验证（graph_walk 接入）')
    print('=' * 100)

    for tk in ['NC20260820001773', 'NC20260824002020']:
        g = next((x for x in GT if x['ticket'] == tk), None)
        if not g:
            continue
        adir = Path(g['path']) / '备份附件'
        exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []

        # 取一个 POOL 名做入口
        pool = None
        for _, v, fam, params, raw in g['kept']:
            if fam == 'POOL' and params.get('POOLNAME'):
                pool = params['POOLNAME']
                break
        if not pool:
            continue

        print(f'\n{tk}')
        print(f'  入口: {pool}')

        # 先不约束维度（看会走多远）
        r1 = find_chain(exps, [pool], param_scope=None)
        print(f'  [无约束] 实例 {r1["stats"].get("instances")} 个, '
              f'族 {r1["stats"].get("cmd_types")} 种, 值 {r1["stats"].get("values")} 个')
        print(f'         链上族: {r1["families"][:10]}')

        # 推断 scope
        scope = infer_param_scope(exps, 'POOL')
        print(f'  [推断 scope] {sorted(scope) if scope else "无"}')

        if scope:
            r2 = find_chain(exps, [pool], param_scope=scope)
            print(f'  [有约束] 实例 {r2["stats"].get("instances")} 个, '
                  f'族 {r2["stats"].get("cmd_types")} 种')
            print(f'         链上族: {r2["families"][:10]}')
