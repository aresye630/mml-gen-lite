"""path_suffixes 判据自证 —— 方案2（路径段作后缀）。

正例（应给出后缀）:
  1. 同目录不同文件名（语义名）→ 各自文件名
  2. 差异在首段（BM/VM/kite）→ 取首段
  3. 公共尾段应被剥掉

反例守卫（必须给不出后缀）:
  4. 路径完全相同 → 空
  5. 只有一篇 → 空
"""
import sys
sys.path.insert(0, '/opt/expgv/scripts')
import gen_feature_all as G

P = G.path_suffixes
ok = 0


def check(name, paths, expect_ok, expect_vals=None):
    global ok
    r = P(paths)
    got = bool(all(r)) and len(set(r)) == len(r)
    good = (got == expect_ok)
    if good and expect_vals is not None:
        good = (r == expect_vals)
    ok += good
    print('%-34s → %-34r %s' % (name, r, '✓' if good else '✗'))


print('═══ 反例守卫（不得给出后缀）═══')
check('路径完全相同',
      ['x/y/z.md', 'x/y/z.md'], False, ['', ''])
check('只有一篇', ['x/y/z.md'], False, [''])
check('路径深度不同但同段',
      ['a/b/c.md', 'a/b/c.md'], False, ['', ''])

print()
print('═══ 正例（应给出后缀）═══')
check('差异在首段 BM/VM/kite',
      ['BM/csp/gui/mgr/f.md', 'VM/csp/gui/mgr/f.md', 'kite/csp/gui/mgr/f.md'],
      True, ['BM', 'VM', 'kite'])
check('差异在首段（两篇）',
      ['bas_oper_l_bm/toctopics/a.md', 'bas_oper_l_vm/toctopics/a.md'],
      True, ['bas_oper_l_bm', 'bas_oper_l_vm'])
check('同名文件在不同目录',
      ['x/pkgA/f.md', 'x/pkgB/f.md'],
      True, ['pkgA', 'pkgB'])
check('公共尾段被剥掉',
      ['a/common/deep/x/f.md', 'b/common/deep/x/f.md'],
      True, ['a', 'b'])

print()
print('-' * 58)
print('结果: %d/7 通过' % ok)
sys.exit(0 if ok == 7 else 1)
