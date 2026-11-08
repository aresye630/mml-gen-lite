"""受限脚本执行器（安全沙箱）。

三层防护：
  1. AST 白名单 —— 过滤语法
  2. SafeStr / SafeDict 代理 —— 限制能力（关键层）
  3. 超时保护 —— 防死循环

用法：
  safe_eval("x[:8] + '_' + ctx['制式']", {'_self': 'grp-abc', '制式': '2g'})
"""
import ast
import signal
import threading

__all__ = ['safe_eval', 'SecurityError', 'DeriveError']


class SecurityError(Exception):
    """表达式包含不允许的语法或操作。"""


class DeriveError(Exception):
    """表达式执行失败（语法错、运行时错、超时）。"""


# ── 第 1 层：AST 白名单 ──

_ALLOWED_NODES = {
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Compare,
    ast.Call, ast.Attribute, ast.Name, ast.Constant, ast.Subscript,
    ast.Slice, ast.IfExp, ast.Tuple, ast.List, ast.Load,
    ast.Add, ast.Sub, ast.Mult, ast.Mod, ast.Eq, ast.NotEq,
    ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.And, ast.Or, ast.Not,
    ast.USub, ast.UAdd, ast.Index if hasattr(ast, 'Index') else ast.Expression,
}

_FORBIDDEN_NODES = {
    ast.Import, ast.ImportFrom, ast.Lambda, ast.FunctionDef,
    ast.AsyncFunctionDef, ast.ClassDef, ast.ListComp, ast.SetComp,
    ast.DictComp, ast.GeneratorExp, ast.Starred, ast.Await,
    ast.Yield, ast.YieldFrom, ast.Global, ast.Nonlocal,
    ast.NamedExpr, ast.Delete, ast.Assign, ast.AugAssign,
    ast.For, ast.While, ast.If, ast.With, ast.Try, ast.Raise,
}

# 允许的属性名（字符串方法白名单）
_ALLOWED_ATTRS = {
    'replace', 'startswith', 'endswith', 'split', 'rsplit',
    'strip', 'lstrip', 'rstrip', 'lower', 'upper',
    'join', 'format', 'zfill', 'find', 'rfind', 'count',
}


def _validate_ast(tree):
    """AST 白名单校验。"""
    for node in ast.walk(tree):
        # 黑名单优先
        if type(node) in _FORBIDDEN_NODES:
            raise SecurityError(
                f'禁止的语法: {type(node).__name__}')
        # 白名单检查
        if type(node) not in _ALLOWED_NODES:
            raise SecurityError(
                f'不支持的语法: {type(node).__name__}')
        # 属性访问只允许白名单方法
        if isinstance(node, ast.Attribute):
            if node.attr not in _ALLOWED_ATTRS:
                raise SecurityError(
                    f'禁止的属性访问: .{node.attr}')
            if node.attr.startswith('_'):
                raise SecurityError(
                    f'禁止访问下划线属性: .{node.attr}')
        # 名字只能是允许的变量
        if isinstance(node, ast.Name):
            if node.id not in ('x', 'ctx', 'len', 'str', 'int',
                               'min', 'max', 'enumerate', 'True', 'False', 'None'):
                raise SecurityError(f'未定义的变量: {node.id}')


# ── 第 2 层：代理对象 ──

class SafeStr:
    """受限字符串。只暴露白名单方法，返回值仍是 SafeStr。"""
    __slots__ = ('_v',)

    def __init__(self, v):
        object.__setattr__(self, '_v', str(v))

    def __getattr__(self, name):
        if name not in _ALLOWED_ATTRS:
            raise SecurityError(f'SafeStr 不允许 .{name}')
        real = getattr(object.__getattribute__(self, '_v'), name)

        def wrapper(*a, **kw):
            args = [_unwrap(z) for z in a]
            kwargs = {k: _unwrap(v) for k, v in kw.items()}
            r = real(*args, **kwargs)
            return _wrap(r)
        return wrapper

    def __add__(self, o):
        return SafeStr(object.__getattribute__(self, '_v') + _unwrap(o))

    def __radd__(self, o):
        return SafeStr(_unwrap(o) + object.__getattribute__(self, '_v'))

    def __mul__(self, o):
        return SafeStr(object.__getattribute__(self, '_v') * int(_unwrap(o)))

    def __getitem__(self, k):
        return SafeStr(object.__getattribute__(self, '_v')[_to_slice(k)])

    def __eq__(self, o):
        return object.__getattribute__(self, '_v') == _unwrap(o)

    def __ne__(self, o):
        return object.__getattribute__(self, '_v') != _unwrap(o)

    def __lt__(self, o):
        return object.__getattribute__(self, '_v') < _unwrap(o)

    def __gt__(self, o):
        return object.__getattribute__(self, '_v') > _unwrap(o)

    def __str__(self):
        return object.__getattribute__(self, '_v')

    def __repr__(self):
        return 'SafeStr(%r)' % object.__getattribute__(self, '_v')

    def __bool__(self):
        return bool(object.__getattribute__(self, '_v'))

    def __len__(self):
        return len(object.__getattribute__(self, '_v'))

    def __iter__(self):
        raise SecurityError('SafeStr 不可迭代')


class _SafeSlice:
    """受限切片。"""
    def __init__(self, s):
        self._s = s

    def __index__(self):
        return self._s if isinstance(self._s, int) else 0


def _to_slice(k):
    """把 SafeStr 或 tuple 转成切片。"""
    if isinstance(k, slice):
        return slice(_unwrap(k.start), _unwrap(k.stop), _unwrap(k.step))
    if isinstance(k, tuple):
        return tuple(_unwrap(x) for x in k)
    return _unwrap(k)


class SafeDict:
    """只读 dict 代理，禁止访问下划线键。"""
    __slots__ = ('_d',)

    def __init__(self, d):
        object.__setattr__(self, '_d', dict(d))

    def __getitem__(self, k):
        k = _unwrap(k)
        if isinstance(k, str) and k.startswith('_'):
            raise SecurityError(f'ctx 不允许访问 {k}')
        d = object.__getattribute__(self, '_d')
        if k not in d:
            raise DeriveError(f'ctx 里没有 {k!r}')
        return _wrap(d[k])

    def get(self, k, default=None):
        try:
            return self[k]
        except (SecurityError, DeriveError):
            return _wrap(default)

    def __contains__(self, k):
        try:
            self[k]
            return True
        except (SecurityError, DeriveError):
            return False

    def keys(self):
        return list(object.__getattribute__(self, '_d').keys())

    def __setitem__(self, k, v):
        raise SecurityError('ctx 只读')


def _wrap(v):
    if isinstance(v, (SafeStr, SafeDict)):
        return v
    if isinstance(v, str):
        return SafeStr(v)
    if isinstance(v, dict):
        return SafeDict(v)
    if isinstance(v, (list, tuple)):
        return [_wrap(x) for x in v]
    return v


def _unwrap(v):
    if isinstance(v, SafeStr):
        return object.__getattribute__(v, '_v')
    if isinstance(v, SafeDict):
        return dict(object.__getattribute__(v, '_d'))
    if isinstance(v, list):
        return [_unwrap(x) for x in v]
    return v


# ── 第 3 层：超时保护 ──

def _run_with_timeout(fn, timeout_sec):
    """在独立线程里跑，超时抛错（线程无法强杀，但能返回）。"""
    result = {}

    def target():
        try:
            result['v'] = fn()
        except BaseException as e:
            result['e'] = e

    t = threading.Thread(target=target, daemon=True)
    t.start()
    t.join(timeout_sec)
    if t.is_alive():
        raise DeriveError(f'表达式执行超过 {timeout_sec}s，已中断')
    if 'e' in result:
        raise result['e']
    return result.get('v')


# ── 对外接口 ──

def safe_eval(expr, ctx, timeout=1.0):
    """安全求值。

    expr: Python 表达式，可用 x（当前值）、ctx（CSV 列）、
          len/str/int/min/max
    ctx:  dict（键为列名）
    """
    expr = (expr or '').strip()
    if not expr:
        return ''

    try:
        tree = ast.parse(expr, mode='eval')
    except SyntaxError as e:
        raise DeriveError(f'表达式语法错误: {e}')

    _validate_ast(tree)

    env = {
        '__builtins__': {},
        'x': SafeStr(ctx.get('_self', '')),
        'ctx': SafeDict({k: v for k, v in ctx.items() if not k.startswith('_')}),
        'len': len,
        'str': lambda v: _unwrap(v),
        'int': int,
        'min': min,
        'max': max,
    }

    code = compile(tree, '<derive>', 'eval')

    def _do():
        return eval(code, env)

    r = _run_with_timeout(_do, timeout)
    return str(_unwrap(r))
