"""去重判据自证：确认 _norm_for_dedup 只抹格式、不抹内容。

正例（应判为相同 → 被去重）:
  1. 字节完全相同
  2. 仅开头多目录块（实测 case）
  3. 仅空白/换行差异

反例（应判为不同 → 保留）:
  4. 正文有一个参数值不同
  5. 正文多一条命令
  6. 只差一个标点（中文句号）—— 保守起见判「不同」
"""
import sys
sys.path.insert(0, '/opt/expgv/scripts')
import gen_feature_all as G

N = G._norm_for_dedup

BASE = """# 更新物理数据库帐户密码

#### 操作场景

* 在调测完成后，系统管理员必须及时更新物理数据库帐号的密码。

#### 操作步骤

1. 执行 ADD DBUSER: NAME="admin", PWD="xxx";
"""

WITH_TOC = """# 更新物理数据库帐户密码

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤

#### 操作场景

* 在调测完成后，系统管理员必须及时更新物理数据库帐号的密码。

#### 操作步骤

1. 执行 ADD DBUSER: NAME="admin", PWD="xxx";
"""

WHITESPACE = BASE.replace('，', '，').replace('\n\n', '\n').replace('：', '：')

DIFF_PARAM = BASE.replace('PWD="xxx"', 'PWD="yyy"')
EXTRA_CMD = BASE + '\n2. 执行 MOD DBUSER: NAME="admin", PWD="zzz";\n'
DIFF_PUNCT = BASE.replace('。', '！')

cases = [
    ('正1 字节相同',        BASE, BASE, True),
    ('正2 多目录块',        BASE, WITH_TOC, True),
    ('正3 空白差异',        BASE, WHITESPACE, True),
    ('反4 参数值不同',      BASE, DIFF_PARAM, False),
    ('反5 多一条命令',      BASE, EXTRA_CMD, False),
    ('反6 标点不同',        BASE, DIFF_PUNCT, False),
]

ok = 0
print('%-18s %-10s %-10s %s' % ('用例', '期望', '实际', '判定'))
print('-' * 52)
for name, a, b, expect_same in cases:
    same = (N(a) == N(b))
    good = (same == expect_same)
    ok += good
    print('%-18s %-10s %-10s %s' % (
        name,
        '相同' if expect_same else '不同',
        '相同' if same else '不同',
        '✓' if good else '✗ 判据失效'))
print('-' * 52)
print('结果: %d/%d 通过' % (ok, len(cases)))
sys.exit(0 if ok == len(cases) else 1)
