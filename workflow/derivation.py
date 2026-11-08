"""派生规则算子引擎。

设计原则：
  1. 算子固定 —— 只有有限的几种字符串变换，代码硬实现
  2. 规则数据化 —— agent 填 CSV 列，不发明语法
  3. 确定性 —— 同样的输入必定产生同样的输出

算子集（从 87 个真实工单归纳）：
  IDENTITY          原样取值
  PREFIX_REPLACE    前缀替换  grp-xxx -> pool-xxx
  PREPEND           前缀拼接  xxx -> f_xxx
  APPEND            后缀拼接  xxx -> xxx_l7
  CONCAT            多列/常量拼接
  MAP               值映射    2g -> LAC
  SEQ               序号递增  -> _001 / _002

用法：
  ops = parse_ops("PREFIX_REPLACE(grp,pool)|APPEND()")
  val = apply_ops("grp-cmnet-ipv6", ops, ctx={'制式': '2g', '_seq': 1})
"""
import re


class OpError(ValueError):
    """派生规则不合法（算子不认识 / 参数不对）。"""


# ── 算子实现 ──

def _op_identity(value, args, ctx):
    return value


def _op_prefix_replace(value, args, ctx):
    """PREFIX_REPLACE(old,new)：把开头的前缀 old 换成 new。

    grp-cmnet-ipv6 --PREFIX_REPLACE(grp,pool)--> pool-cmnet-ipv6
    """
    if len(args) != 2:
        raise OpError('PREFIX_REPLACE 需要 2 个参数: (old,new)')
    old, new = args
    # 只替换开头的整段前缀（后面跟 - 或 _ 或结尾）
    for sep in ('-', '_'):
        if value.startswith(old + sep):
            return new + value[len(old):]
    if value == old:
        return new
    return value


def _op_prepend(value, args, ctx):
    """PREPEND(text)：加前缀。PREPEND(f_) → f_xxx"""
    if len(args) != 1:
        raise OpError('PREPEND 需要 1 个参数: (text)')
    return args[0] + value


def _op_append(value, args, ctx):
    """APPEND(text)：加后缀。APPEND(_l7) → xxx_l7"""
    if len(args) != 1:
        raise OpError('APPEND 需要 1 个参数: (text)')
    return value + args[0]


def _op_concat(value, args, ctx):
    """CONCAT(part1,part2,...)：拼接。

    每个 part 可以是：
      · 字面量          "tj"      （用引号括起来）
      · 列引用          $CSV.区
      · 当前值          $SELF
      · 已解析占位符    {{制式}}
    拼接符由 CONCAT 后的 sep 决定，默认 '-'。
    """
    if not args:
        raise OpError('CONCAT 至少需要 1 个参数')
    parts = []
    for a in args:
        a = a.strip()
        if a == '$SELF':
            parts.append(value)
        elif a.startswith('$CSV.'):
            col = a[5:]
            parts.append(str(ctx.get(col, '')))
        elif a.startswith('{{') and a.endswith('}}'):
            var = a[2:-2].strip()
            parts.append(str(ctx.get(var, '')))
        elif a.startswith('"') and a.endswith('"'):
            parts.append(a[1:-1])
        else:
            parts.append(a)
    sep = ctx.get('_concat_sep', '-')
    return sep.join(p for p in parts if p)


def _op_map(value, args, ctx):
    """MAP(k1:v1,k2:v2,...,default:v)。

    2g --MAP(2g:LAC,4g:TAC,default:TAC)--> LAC
    """
    if not args:
        raise OpError('MAP 至少需要 1 个参数')
    default = None
    for a in args:
        if ':' not in a:
            raise OpError(f'MAP 参数格式应为 k:v，收到 {a!r}')
        k, v = a.split(':', 1)
        k, v = k.strip(), v.strip()
        if k in ('default', '默认'):
            default = v
        elif k.lower() == str(value).lower():
            return v
    if default is None:
        raise OpError(f'MAP 没有匹配 {value!r} 且未提供 default')
    return default


def _op_seq(value, args, ctx):
    """SEQ(width)：用实例序号替换该值。SEQ(3) → 001 / 002 ..."""
    width = int(args[0]) if args else 3
    n = ctx.get('_seq', 0)
    return str(n).zfill(width)


OPERATORS = {
    'IDENTITY': _op_identity,
    'PREFIX_REPLACE': _op_prefix_replace,
    'PREPEND': _op_prepend,
    'APPEND': _op_append,
    'CONCAT': _op_concat,
    'MAP': _op_map,
    'SEQ': _op_seq,
}


# ── 规则解析与执行 ──

_OP_RE = re.compile(r'([A-Z_]+)\s*\((.*)\)\s*$', re.S)


def parse_ops(expr):
    """解析算子表达式。

    "PREFIX_REPLACE(grp,pool)|APPEND(_l7)"
      → [('PREFIX_REPLACE', ['grp','pool']), ('APPEND', ['_l7'])]
    """
    if not expr or not expr.strip():
        return []
    ops = []
    for seg in expr.split('|'):
        seg = seg.strip()
        if not seg:
            continue
        m = _OP_RE.match(seg)
        if not m:
            raise OpError(f'算子语法错误: {seg!r}（应为 NAME(arg1,arg2)）')
        name, raw_args = m.group(1), m.group(2)
        if name not in OPERATORS:
            raise OpError(
                f'未知算子 {name}。可用: {", ".join(sorted(OPERATORS))}')
        # 切参数（保留引号内容里的逗号）
        args, cur, inq = [], '', False
        for ch in raw_args:
            if ch == '"':
                inq = not inq
                cur += ch
            elif ch == ',' and not inq:
                args.append(cur.strip())
                cur = ''
            else:
                cur += ch
        if cur.strip():
            args.append(cur.strip())
        ops.append((name, args))
    return ops


def apply_ops(value, ops, ctx=None):
    """按顺序应用算子。"""
    ctx = ctx or {}
    v = str(value)
    for name, args in ops:
        v = OPERATORS[name](v, args, ctx)
    return v


_INLINE_RE = re.compile(r'\$\{CSV\.([^}]+)\}')
# 受限脚本：${SCRIPT.列名} <python expr>
#   显式指定 x 绑定哪个 CSV 列（不猜，避免歧义）
_SCRIPT_RE = re.compile(r'^\$\{SCRIPT\.([^}]+)\}\s*(.+)$', re.S)
# 兼容不带列名的旧写法：${SCRIPT} <expr>，此时 x 为空
_SCRIPT_BARE_RE = re.compile(r'^\$\{SCRIPT\}\s*(.+)$', re.S)
_SELF_INLINE_RE = re.compile(r'\$\{SELF\}')
# 值表达式开头的算子链：${CSV.x}|OPS(...)
_LEADING_REF_RE = re.compile(r'^\$\{CSV\.([^}]+)\}(?:\|(.*))?$', re.S)


def interpolate(template, ctx, self_value=''):
    """内嵌替换：把 ${CSV.列名} 和 ${SELF} 替换掉。

    'f_${CSV.DNN}_l7'  →  'f_zjltcs03s_l7'
    '${SELF}_001'      →  'xxx_001'
    """
    out = _INLINE_RE.sub(lambda m: str(ctx.get(m.group(1).strip(), '')), template)
    out = _SELF_INLINE_RE.sub(lambda m: str(self_value), out)
    return out


def resolve(expr, ctx):
    """解析一个「值表达式」。

    统一语法（2026-11-08）：
      ${CSV.列名}                         → 取该列原值
      ${CSV.列名}|PREFIX_REPLACE(grp,pool) → 取列值后应用算子链
      f_${CSV.DNN}_l7                     → 内嵌替换
      ${SELF}_001                         → 基于当前值加后缀
      纯字面量                             → 原样返回

    ctx 里需含：各 CSV 列（键为列名）、以及 _seq / _concat_sep 等内部键。
    """
    expr = (expr or '').strip()
    if not expr:
        return ''

    # 0) 受限脚本：${SCRIPT.列名} <expr>
    #    ★ 2026-11-08 新增：固定算子写不出来时用
    #    安全由 safe_expr.safe_eval 保证（AST 白名单 + SafeStr 代理 + 超时）
    #    x 绑定到 ${SCRIPT.列名} 指定的 CSV 列
    ms = _SCRIPT_RE.match(expr)
    if ms:
        from safe_expr import safe_eval, SecurityError, DeriveError
        col = ms.group(1).strip()
        code = ms.group(2).strip()
        if col not in ctx:
            raise OpError(f'CSV 里没有列 {col!r}')
        c2 = dict(ctx)
        c2['_self'] = ctx[col]
        try:
            return safe_eval(code, c2)
        except SecurityError as e:
            raise OpError(f'受限脚本不安全: {e}')
        except DeriveError as e:
            raise OpError(f'受限脚本执行失败: {e}')
    # 兼容裸 ${SCRIPT}（x 为空）
    mb = _SCRIPT_BARE_RE.match(expr)
    if mb:
        from safe_expr import safe_eval, SecurityError, DeriveError
        try:
            return safe_eval(mb.group(1).strip(), ctx)
        except SecurityError as e:
            raise OpError(f'受限脚本不安全: {e}')
        except DeriveError as e:
            raise OpError(f'受限脚本执行失败: {e}')

    # 1) 整体表达式：${CSV.x}|OPS
    m = _LEADING_REF_RE.match(expr)
    if m:
        col = m.group(1).strip()
        op_expr = (m.group(2) or '').strip()
        if col not in ctx:
            raise OpError(f'CSV 里没有列 {col!r}（现有列: {", ".join(ctx.keys())}）')
        base = str(ctx[col])
        if not op_expr:
            return base
        # ★ 2026-11-08：算子参数里可能含内嵌变量（如 APPEND(-${CSV.制式})）
        #   先内嵌替换，再解析算子
        op_expr = interpolate(op_expr, ctx)
        return apply_ops(base, parse_ops(op_expr), ctx)

    # 2) 内嵌替换（f_${CSV.x}_l7 / ${SELF}_001）
    return interpolate(expr, ctx)
