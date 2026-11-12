"""默认值过滤：识别并剔除 EXP 导出里的系统默认值配置。

★ 2026-11-12（用户洞察）
  「冗余族的参数有没有是默认值（exp 会存在导出默认值的情况）
   如果是默认值的设置其实可以直接删减掉」

## 问题的本质

  EXP 导出会把「系统默认值」也带出来：
    SET APNAFFUNC: APN="xxx", ISENABLE=DISABLE;        ← 默认关闭
    SET APNCHARGECTRL: APN="xxx", ONLINESW=INHERIT;    ← 默认继承
    SET DFTGBRBEARER: APN="xxx", DFTGBRBEARERSW=DISABLE;

  这些命令「配了等于没配」，但会让产物膨胀 2-3 倍。

## 判据（数据驱动，不猜）

  方法 1：单值占比法（最可靠）
    某个参数在所有 EXP 里 95%+ 都是同一个值 → 该值是默认值
    实测：4517 个参数里 674 个符合（TCPCHGPROFLAG=NOTCONFIG 占 100%，14 万条）

  方法 2：整条命令法
    某个族的所有实例，参数集和值都完全一致 → 整族是默认配置
    实测：47 个冗余族里 37 个是这种

  方法 3：族属性法（辅助）
    如果某族在 GT 里没出现过（= 本次变更不涉及），且参数全是默认值 → 可以整族删

## 输出

  filter 之后，params.csv 里只剩「非默认值」的行。
  默认值行要么删掉，要么标注 default:true / default:inherited，让用户决定。
"""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

# ═══════════════════════════════════════════════════════════
# 默认值识别阈值
# ═══════════════════════════════════════════════════════════
DEFAULT_RATIO_TH = 0.95      # 单值占比 >= 95% → 认定为默认值
DEFAULT_MIN_SAMPLES = 100    # 样本数 < 100 不判定（数据太少不可靠）

# 明确表示「继承/未配置」的值（即使占比不高也是默认语义）
INHERIT_VALUES = {'INHERIT', 'NOTCONFIG', 'NOTCONFIGURED', 'DEFAULT'}


def build_default_value_index(exp_paths, include_cache=True):
    """从 EXP 建立「参数 → 默认值」索引。

    返回：{参数名: {'value': 默认值, 'ratio': 占比, 'n': 样本数}}

    为什么用 EXP 而不是写死默认值表：
      · 不同版本默认值可能不同
      · 无法预先知道全部参数
      · 数据说了算，不靠人工维护
    """
    cache_p = Path('/tmp/default_value_index.json')
    if include_cache and cache_p.exists():
        try:
            return json.loads(cache_p.read_text(encoding='utf-8'))
        except Exception:
            pass

    param_vals = defaultdict(Counter)
    for p in exp_paths:
        try:
            with open(p, encoding='utf-8', errors='replace') as f:
                for line in f:
                    s = line.strip()
                    m = re.match(r'^(SET|MOD|ADD)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)', s)
                    if not m:
                        continue
                    # ★ 2026-11-12 修：同上，用 3 元组
                    for pm in re.finditer(
                            r'([A-Z][A-Z0-9_]*)\s*=\s*(?:"([^"]*)"|([^,\s;]+))',
                            m.group(3)):
                        pname = pm.group(1)
                        val = pm.group(2) if pm.group(2) else pm.group(3)
                        param_vals[pname][val] += 1
        except Exception:
            continue

    index = {}
    for pname, cnt in param_vals.items():
        total = sum(cnt.values())
        if total < DEFAULT_MIN_SAMPLES:
            continue
        top_val, top_n = cnt.most_common(1)[0]
        ratio = top_n / total
        n_kinds = len(cnt)

        # ★ 2026-11-12 第四版判据：区分「真默认值」和「业务普遍值」
        #
        #   只有 1 种取值（n_kinds == 1）→ 现网所有实例都这样，是系统默认值
        #     例：DFTGBRBEARERSW 512 条全是 DISABLE
        #         IFDF 330 条全是 FALSE
        #         → 用户改不了/没人改过 → 默认值
        #
        #   有 2+ 种取值 → 是业务选择，即使某种占 99%
        #     例：ISENABLE 有 ENABLE/DISABLE → 默认值可能是 DISABLE，但也可能是业务选择
        #         POLICYTYPE 有 PCC/SPR → 97.9% 是 PCC 但它是业务枚举
        #         → 不能判成默认值（误删会有业务影响）
        #
        #   例外：值本身是 INHERIT/NOTCONFIG 这类继承语义 → 无论几种取值都算默认值
        if n_kinds == 1:
            index[pname] = {
                'value': top_val,
                'ratio': 1.0,
                'n': total,
                'reason': 'single_value',
            }
        elif str(top_val).upper() in INHERIT_VALUES:
            index[pname] = {
                'value': top_val,
                'ratio': round(ratio, 4),
                'n': total,
                'reason': 'inherit_semantic',
            }
    return index


def save_default_index(index):
    try:
        Path('/tmp/default_value_index.json').write_text(
            json.dumps(index, ensure_ascii=False, indent=1), encoding='utf-8')
    except Exception:
        pass


def is_default(param, value, index):
    """判断某个参数值是否是默认值。

    ★ 2026-11-12 第三版（前两版都误删）

    第一版：qv if qv is not None else uv → 解包错，命中 0 条
    第二版：只看「单值占比 >= 95%」→ 误删业务配置
        实测误删：ADD RULEBINDING: ... POLICYTYPE=PCC;
                  POLICYTYPE 现网 97.9% 都是 PCC，但它是业务枚举（还有 SPR 等值）
                  → 判成默认值 → 整条命令被删 → 少了规则绑定

    第三版：只用「语义明确的默认/继承值」白名单
        认定：INHERIT / NOTCONFIG / DEFAULT / NONE / NOTCONFIGURED
        不认定：PCC / ALL / ANY / STRING 这类业务取值（即使占比 100%）

        理由：这些词本身就表示「沿用上级配置」或「未配置」，
             配了等于没配。而 PCC/ALL 是真实业务选择，改了会有行为变化。
    """
    v = str(value).strip().strip('"')
    if v.upper() in INHERIT_VALUES:
        return True, 'inherit'
    info = index.get(param.upper())
    if info and info.get('reason') == 'single_value' and v == str(info['value']):
        return True, f"default(single,n={info['n']})"
    return False, ''


def classify_commands(mml_or_rows, index, mode='mll'):
    """把命令/行分成「非默认」「默认」两组。

    mml_or_rows: mml.txt 文本（mode='mll'）或 params.csv 行（mode='rows'）
    返回：{'kept': [...], 'dropped': [...], 'stats': {...}}
    """
    kept, dropped = [], []
    stats = {'total': 0, 'n_default': 0, 'n_inherit': 0}

    if mode == 'rows':
        for row in mml_or_rows:
            stats['total'] += 1
            pname = (row.get('param') or '').upper()
            val = row.get('value') or ''
            d, why = is_default(pname, val, index)
            if d:
                dropped.append({**row, '_why': why})
                if why.startswith('inherit'):
                    stats['n_inherit'] += 1
                else:
                    stats['n_default'] += 1
            else:
                kept.append(row)
        return {'kept': kept, 'dropped': dropped, 'stats': stats}

    # mml 文本模式：逐条解析
    for line in (mml_or_rows or '').split('\n'):
        s = line.split('//')[0].strip()
        if not re.match(r'^(ADD|MOD|SET|RMV)\s+', s, re.I):
            kept.append(line)
            continue
        stats['total'] += 1
        # 解析参数
        m = re.match(r'^(ADD|MOD|SET)\s+([A-Z][A-Z0-9_]+)\s*:\s*(.*)', s, re.I)
        if not m:
            kept.append(line)
            continue
        # ★ 2026-11-12 修：用 3 元组正则，避免 4 元组解包取错位置
        #   旧写法的坑：('ONLINESW', 'INHERIT', '', 'INHERIT')
        #               pname      raw         qv   uv
        #   qv 是空字符串而不是 None → `qv if qv is not None else uv` 取到 '' → 判定全错
        params = re.findall(r'([A-Z][A-Z0-9_]*)\s*=\s*(?:"([^"]*)"|([^,\s;]+))',
                            m.group(3))
        if not params:
            kept.append(line)
            continue

        # ★ 2026-11-12 修（首版过滤 0 条）
        #   原逻辑：所有参数都是默认值才删整条
        #   问题：主键参数（APN/VRFNAME/POLICYNAME）的值是对象名，永远不是「默认值」
        #         → all_default 永远是 False → 一条都删不掉
        #
        #   新逻辑：先排除「主键/引用参数」，只看剩下的「属性参数」是否全默认
        #     主键判据：参数名以 NAME/NM/INSTANCE/ID 结尾，或是 APN/DNN 这类标识
        #     实测：SET APNAFFUNC: APN="xxx", ISENABLE=DISABLE;
        #           APN 是主键（排除），ISENABLE 是属性（默认值）→ 整条可删

        def _is_key_param(pname):
            """判断参数是否是「主键/引用」参数（值指向某个对象，不是配置值）。

            ★ 2026-11-12 补充（实测漏判）
              原规则漏掉了中间位置的引用参数：
                DFTURRGRPNAME / DFTSIGURRGNAME  ← 引用 URRGROUP 对象
                SRVPOLICYNAME / FLOWFILTERNAME
              这些参数的值是对象名，被误判成「默认值参数」，
              但因为查不到索引而判非默认，导致：
                SET URRGRPBINDING: ... TCPCHGPROFLAG=NOTCONFIG(默认), DFTURRGRPNAME="xxx"(漏判)
                → attr_params 只有 TCPCHGPROFLAG → 全默认 → 整条被删（丢了业务配置）
            """
            u = pname.upper()
            if u in ('APN', 'DNN', 'VRFNAME', 'VPNINSTANCE', 'POLICYNAME'):
                return True
            # 名字/标识类
            if re.search(r'(NAME|NM|INSTANCE|INSTNAME|ID|INDEX)$', u):
                return True
            # ★ 引用类：参数名里含 NAME 但不在结尾（如 DFTURRGRPNAME 已在上面覆盖）
            #   补充：含 GRPNAME / URRGNAME / PROFNAME 等复合引用
            if re.search(r'(GRPNAME|URRGNAME|PROFNAME|FILTERNAME|VRFNAME|'
                         r'TNLNAME|POOLNAME|GROUPNAME)', u):
                return True
            return False

        attr_params = [(pn, qv if qv else uv)
                       for pn, qv, uv in params
                       if not _is_key_param(pn)]

        if not attr_params:
            # 只有主键参数（如 ADD VPNINST:VPNINSTANCE="x"）→ 不是默认值命令，保留
            kept.append(line)
            continue

        # ★ 2026-11-12 关键补充：绑定/关系类命令不能按属性判默认
        #   实测误删：SET URRGRPBINDING: USERPROFILENAME="x", DFTURRGRPNAME="y",
        #                            TCPCHGPROFLAG=NOTCONFIG, DFTSIGURRGNAME="z";
        #     · 3 个参数是引用（被排除）
        #     · 只剩 TCPCHGPROFLAG=NOTCONFIG（默认值）
        #     → 判成「整条可删」，但这条命令的业务价值在「建立绑定关系」，
        #       属性只是附加，删了绑定就没了
        #
        #   判据：如果「非主键参数」里只有默认值，但命令本身含 2+ 个引用参数，
        #        说明这是绑定关系命令，应保留
        n_ref_params = sum(1 for pn, _q, _u in params if _is_key_param(pn))
        if n_ref_params >= 2 and verb in ('ADD', 'SET', 'MOD'):
            # 多引用 = 关系/绑定命令，属性全默认也保留
            kept.append(line)
            continue

        # ★ 2026-11-12 关键修正（两轮迭代）
        #   第一轮：所有 ADD 都不删 → 结果一条都删不掉（产物全是 ADD）
        #   第二轮：ADD 也判属性默认 → 误删 ADD INTERFACE:IFNAME=Tunnel2603
        #
        #   正确判据：区分「对象族 ADD」和「属性族 ADD」
        #     对象族 ADD：命令创建的是一个独立对象（INTERFACE / POOL / APN / VPNINST）
        #                → 即使属性全默认，对象本身是新的，不能删
        #     属性族 ADD：命令创建的是「某个对象上的属性配置」（APNAFFUNC / APNCHARGECTRL）
        #                → 一条独立命令，属性全默认 = 配了等于没配，可以删
        #
        #   区分方法（数据驱动）：
        #     看该族的参数是否「全是引用/主键 + 默认属性」
        #     若该族的主键参数本身指向另一个族（如 APNAFFUNC.APN 指向 APN），
        #     说明它是属性族
        verb = m.group(1).upper()

        def _looks_like_attr_family(fam, params):
            """判断该族是「属性族」（依附于其它对象）还是「对象族」（独立对象）。"""
            # 属性族特征：主键参数名 == 另一个已知对象族的身份参数
            #   例：APNAFFUNC 的主键 APN → 指向 APN 族
            #   例：APNCHARGECTRL 的 APN → 指向 APN 族
            key_names = [pn for pn, _q, _u in params if _is_key_param(pn)]
            if not key_names:
                return False
            first_key = key_names[0].upper()
            # 该参数名（去掉 NAME 后缀）是否构成另一个族名
            stem = re.sub(r'(NAME|NM)$', '', first_key)
            if stem and stem != fam and len(stem) >= 2:
                # 例：APN → 族 APN；USERPROFILENAME → USERPROFILE
                return True
            return False

        if verb == 'ADD' and not _looks_like_attr_family(m.group(2), params):
            # 对象族 ADD，永不删
            kept.append(line)
            continue

        all_default = True
        whys = []
        for pname, val in attr_params:
            d, why = is_default(pname, val, index)
            if not d:
                all_default = False
                break
            whys.append(why)

        if all_default:
            dropped.append({'line': line, '_why': whys[0] if whys else ''})
            if whys and whys[0].startswith('inherit'):
                stats['n_inherit'] += 1
            else:
                stats['n_default'] += 1
        else:
            kept.append(line)

    return {'kept': kept, 'dropped': dropped, 'stats': stats}


def filter_mml_text(mml_text, index, drop_default=True):
    """过滤 mml.txt：删掉全默认值的命令，保留其它。

    返回：(新文本, 统计)
    """
    r = classify_commands(mml_text, index, mode='mll')
    if not drop_default:
        return mml_text, r['stats']
    new = '\n'.join(r['kept'])
    return new, r['stats']


def explain_dropped(dropped, limit=20):
    """生成「删掉了什么」的说明（给用户看）。"""
    lines = []
    for d in dropped[:limit]:
        if 'line' in d:
            lines.append(f"  {d['line'].strip()[:120]}")
            lines.append(f"    → {d['_why']}")
        else:
            lines.append(f"  {d.get('family','')}.{d.get('param','')}="
                         f"{d.get('value','')}  → {d['_why']}")
    return '\n'.join(lines)


if __name__ == '__main__':
    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))

    print('=' * 100)
    print('默认值识别与过滤验证')
    print('=' * 100)

    # 建索引
    all_exps = []
    for g in GT:
        if not g['kept']:
            continue
        adir = Path(g['path']) / '备份附件'
        if adir.exists():
            all_exps.extend(str(p) for p in sorted(adir.glob('*.txt'))[:2])

    print(f'\n扫描 {len(all_exps)} 个 EXP...')
    index = build_default_value_index(all_exps, include_cache=False)
    save_default_index(index)

    print(f'识别出 {len(index)} 个默认值参数')
    print(f'\n=== 高频默认值（样本数 > 10000）===')
    hot = [(k, v) for k, v in index.items() if v['n'] > 10000]
    hot.sort(key=lambda x: -x[1]['n'])
    for k, v in hot[:15]:
        print(f"  {k:<26} {str(v['value'])[:14]:<16} "
              f"占比 {v['ratio']*100:.1f}%  样本 {v['n']}")

    # 验证：NC20260803002122 的冗余族
    tk = 'NC20260803002122'
    print(f'\n{"=" * 100}')
    print(f'{tk} 的冗余族过滤效果')
    print(f'{"=" * 100}')

    prod = Path(f'/tmp/eval_derive_samples/products/full/{tk}/mml.txt')
    if prod.exists():
        txt = prod.read_text(encoding='utf-8')
        new_txt, stats = filter_mml_text(txt, index)
        print(f'\n过滤前: {len(txt.split(chr(10)))} 行')
        print(f'过滤后: {len(new_txt.split(chr(10)))} 行')
        print(f'统计: 总 {stats["total"]} 条命令，'
              f'删默认 {stats["n_default"]}，删继承 {stats["n_inherit"]}')
