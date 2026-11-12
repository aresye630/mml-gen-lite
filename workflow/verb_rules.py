"""动词规则加载：从 rules/verb_rules.yaml 读「族 → 允许动词」+ 必含命令。

★ 2026-11-12
  解决两个问题：
    1. mml_gen.SET_FAMILIES 硬编码只有 5 个族，导致 60 个族的 SET 被写成 ADD
    2. REFRESHSRV 这类「配置生效必要命令」缺失或动词错误，没有任何判据拦

## 用法

  from verb_rules import VerbRules
  vr = VerbRules()
  vr.verb_for('REFRESHSRV')        # → 'SET'
  vr.verb_for('APN')               # → 'ADD'（不在 SET_ONLY 里）
  vr.is_set_only('REFRESHSRV')     # → True
  vr.check_must_have(mml_text)     # → {'ok': bool, 'missing': [...], 'wrong_verb': [...]}
"""
import re
from pathlib import Path

_RULES_PATH = Path(__file__).parent.parent / 'rules' / 'verb_rules.yaml'


def _parse_simple_yaml(text):
    """极简 YAML 解析（只支持本项目用到的结构，避免引入 pyyaml 依赖）。

    支持：
      KEY:
        - VALUE       # 列表
        KEY2:
          SUBKEY: VAL  # 一层嵌套
    """
    out = {}
    cur_key = None
    cur_list = None
    cur_sub = None

    for raw in text.split('\n'):
        line = raw.rstrip()
        if not line or line.lstrip().startswith('#'):
            continue
        # 顶层 key
        if re.match(r'^[A-Z_]+:\s*$', line):
            cur_key = line.split(':')[0].strip()
            out[cur_key] = {}
            cur_list = None
            cur_sub = None
            continue
        # 列表项
        m = re.match(r'^\s+-\s+(.+)$', line)
        if m and cur_key:
            val = m.group(1).split('#')[0].strip()
            if isinstance(out[cur_key], dict) and not out[cur_key]:
                out[cur_key] = []
            if isinstance(out[cur_key], list):
                out[cur_key].append(val)
            continue
        # 二层 key（如 MUST_HAVE 下的 REFRESHSRV:）
        m2 = re.match(r'^  ([A-Z_]+):\s*$', line)
        if m2 and cur_key:
            cur_sub = m2.group(1).strip()
            if isinstance(out[cur_key], list):
                out[cur_key] = {}
            out[cur_key][cur_sub] = {}
            continue
        # 三层 key: value
        m3 = re.match(r'^\s{4,}([A-Za-z_]+):\s*(.*)$', line)
        if m3 and cur_key and cur_sub:
            k = m3.group(1).strip()
            v = m3.group(2).split('#')[0].strip()
            out[cur_key][cur_sub][k] = v
            continue

    return out


class VerbRules:
    """动词规则。"""

    def __init__(self, path=None):
        self.path = Path(path) if path else _RULES_PATH
        self.set_only = set()
        self.must_have = {}
        self._load()

    def _load(self):
        if not self.path.exists():
            # 兜底：至少保住 REFRESHSRV
            self.set_only = {'REFRESHSRV', 'LICENSESWITCH', 'URRGRPBINDING'}
            self.must_have = {}
            return
        try:
            data = _parse_simple_yaml(self.path.read_text(encoding='utf-8'))
            self.set_only = {str(x).upper() for x in (data.get('SET_ONLY') or [])}
            self.must_have = data.get('MUST_HAVE') or {}
            # 转大写 key
            self.must_have = {k.upper(): v for k, v in self.must_have.items()}
        except Exception:
            self.set_only = {'REFRESHSRV', 'LICENSESWITCH', 'URRGRPBINDING'}
            self.must_have = {}

    def is_set_only(self, family):
        return (family or '').upper() in self.set_only

    def verb_for(self, family, default='ADD'):
        """该族应该用什么动词。"""
        return 'SET' if self.is_set_only(family) else default

    def check_must_have(self, mml_text):
        """检查「必含命令」。

        返回：{
          'ok': bool,
          'missing': [{'family','verb','reason'}],
          'wrong_verb': [{'family','expected','actual','line'}],
          'applicable': [ '触发条件说明' ]
        }
        """
        result = {'ok': True, 'missing': [], 'wrong_verb': [], 'applicable': []}
        if not mml_text:
            return result

        # 解析产物里的 (动词, 族)
        present = []      # [(verb, fam, line)]
        for line in mml_text.split('\n'):
            s = line.split('//')[0].strip()
            m = re.match(r'^(ADD|MOD|SET|RMV)\s+([A-Z][A-Z0-9_]+)\s*[:;]', s, re.I)
            if m:
                present.append((m.group(1).upper(), m.group(2).upper(), s))

        present_fams = {f for _, f, _ in present}

        for fam, spec in self.must_have.items():
            when_text = spec.get('when') or ''
            need_verbs = re.findall(r'[A-Z][A-Z0-9_]{2,}', when_text)
            triggered = any(f in present_fams for f in need_verbs)
            if not triggered:
                continue

            result['applicable'].append(
                f"{fam} 应该存在（触发族: {[f for f in need_verbs if f in present_fams]}）")

            hits = [(v, l) for v, f, l in present if f == fam]
            if not hits:
                result['missing'].append({
                    'family': fam,
                    'verb': spec.get('verb', 'SET'),
                    'reason': spec.get('reason', '配置生效的必要命令'),
                })
                result['ok'] = False
                continue

            expected = (spec.get('verb') or 'SET').upper()
            for v, l in hits:
                if v != expected:
                    result['wrong_verb'].append({
                        'family': fam, 'expected': expected,
                        'actual': v, 'line': l[:120],
                    })
                    result['ok'] = False

        return result


# 单例（避免反复读文件）
_INSTANCE = None


def get_rules():
    global _INSTANCE
    if _INSTANCE is None:
        _INSTANCE = VerbRules()
    return _INSTANCE


if __name__ == '__main__':
    vr = VerbRules()
    print(f'规则文件: {vr.path}')
    print(f'SET_ONLY: {len(vr.set_only)} 个族')
    print(f'MUST_HAVE: {list(vr.must_have.keys())}')

    print(f'\n=== 动词推导抽查 ===')
    for fam in ['REFRESHSRV', 'LICENSESWITCH', 'APNIDLETIME', 'APN',
                'IFIPV6ENABLE', 'POOL', 'URRGROUP']:
        print(f'  {fam:<20} → {vr.verb_for(fam)}'
              f'{"  (SET_ONLY)" if vr.is_set_only(fam) else ""}')

    print(f'\n=== 必含命令检查 ===')
    TESTS = [
        ('有 FILTER 但没 REFRESHSRV',
         'ADD FILTER:FILTERNAME="x";'),
        ('有 FILTER 且有 SET REFRESHSRV',
         'ADD FILTER:FILTERNAME="x";\nSET REFRESHSRV:REFRESHTYPE=ALL;'),
        ('REFRESHSRV 动词错（ADD）',
         'ADD FILTER:FILTERNAME="x";\nADD REFRESHSRV:REFRESHTYPE=ALL;'),
        ('没有 FILTER（不触发）',
         'ADD POOL:POOLNAME="x";'),
    ]
    for label, text in TESTS:
        r = vr.check_must_have(text)
        print(f'\n  {label}')
        print(f'    ok={r["ok"]}')
        for m in r['missing']:
            print(f'    缺: {m["family"]}（{m["reason"]}）')
        for w in r['wrong_verb']:
            print(f'    动词错: {w["family"]} 应为 {w["expected"]}，实际 {w["actual"]}')
