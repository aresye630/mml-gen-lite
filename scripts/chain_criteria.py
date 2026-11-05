#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""链装配产物形态判据（2026-09-19 改版：认「链装配 + 开关判定」新形态）。

## 为什么改版

旧版判据为**旧产物**（大区间平铺）设计，核心是数「EXP 行区间标题」。
链路改造后产物已无区间标题，旧判据因此永远报「平铺/混合」——
**不是产物有问题，是判据的眼睛盯着一个已不存在的东西**（用户裁决方案甲：换眼睛）。

## 新形态特征（两段式产物：文档原文 + 现网实例）

产物结构（`gen_feature_all --fingerprint` 输出）：
    # <特性标题>
    ## 1. 特性完整内容（官方文档原文）      ← 人学习入口
    ## 2. 官方示例命令（特性文档原始示例）    ← 对照基线
    ## 3. 现网实例（链装配）                 ← ★ 本文判据主战场
       ### 一、<命令> …                     （链装配类：分组装配）
          #### 组 N: ADD A + ADD B  [共享参数: X]
             实例 K: 值
                L<seq> ADD A:...
                //通过 X 关联到 Y
                ⛔ 缺 …
       ### 二、<开关类特性>                  （开关判定类：命令存在性）
       ### 三、结论

## 判据（N1~N5）

| 判据 | 含义 | 正例形态 |
|---|---|---|
| N1 组结构   | 按 link_groups 分组装配 | `#### 组 N: A + B  [共享参数: X]` |
| N2 实例聚合 | 组内按共享值聚合出实例 | `实例 N: <值>（完整 X / 枚举不符 Y / 缺命令 Z）` |
| N3 逐跳说明 | 引用关系可追溯 | `//通过 X 关联到 Y` |
| N4 三态结论 | 命中/枚举不符/未配置分列 | `### 三、结论` + `未配置·严重(L1` |
| N5 原文对照 | 文档原文 + 示例块 | `## 1. 特性完整内容（官方文档原文）` |

**两类产物判据不同**（不可一刀切）：
  · 链装配类（有 link_groups）：N1/N2/N3 必须有；N5 必须有
  · 开关判定类（无 link_groups）：无 N1/N2（结构使然，不是缺陷）；N4 必须有

⇒ 判定按**产物自身类型**分流，用产物内的「### 二、」段标记识别开关判定类。

用法：
    python3 chain_criteria.py <产物目录>          # 统计 + 判定
    python3 chain_criteria.py --selftest          # 判据自证（正/反/边界成对）
"""
import re
import sys
from collections import Counter
from pathlib import Path

# ── N1 组结构：`#### 组 N: 命令A + 命令B    [共享参数: X]` ──
#    ⚠ 必须有「组 N:」+ 至少两个命令（`+` 连接），否则会误吞标题里的「+」
RE_N1 = re.compile(r'^#{3,5}\s*组\s*\d+\s*[:：].+\+.+?(?:\[共享参数|$)', re.M)
# ── N2 实例聚合 ──
#    实测产物形态（两个都要认，它们是同一件事的两半）：
#      a) 组头下的汇总行：`现网实例: 6 条（完整 1 / 缺命令 5）`
#      b) 逐条实例行：    `**实例 1. VRF_INTERNET** — ✅ 完整`
#                          `**实例 2. CHINAMOBILE_ACCESS** — 缺: ADD APN`
#                          `**实例 5. xxx** — 枚举不符: ADD SECTION`
#    ⚠ 两种写法（`实例 N.` 点号 / `实例 N:` 冒号）都要认 ——
#      第一版只认冒号，实测 N2 命中 0（产物明明有实例），是判据错不是产物错。
RE_N2_SUM = re.compile(r'现网实例\s*[:：]?\s*\d+\s*条'
                       r'\s*[（(].{0,60}?(完整|枚举不符|缺命令|未配置)')
RE_N2_ITEM = re.compile(r'实例\s*\d+\s*[.．:：]\s*\S+'
                        r'\s*\*{0,2}\s*(?:—|–|-|·)\s*'
                        r'(✅\s*完整|缺\s*[:：]|枚举不符\s*[:：])')
RE_N2 = re.compile(r'(?:%s|%s)' % (RE_N2_SUM.pattern, RE_N2_ITEM.pattern))
# ── N3 逐跳说明（沿用旧 F1 的正确形态，⚠ 不含流程箭头 →）──
RE_N3 = re.compile(r'(//\s*通过\s*\S+\s*(?:关联到|找到|反查到)\s*\S+'
                   r'|//\s*(?:汇聚|不再展开|不再找))')
# ── N4 三态结论 ──
RE_N4 = re.compile(r'^###\s*三、结论|^\s*结论[:：]', re.M)
RE_N4_STATE = re.compile(r'(未配置·(严重|重要|提示)|枚举不符·|未装配|命中\s*\d+)')
# ── N5 原文对照 ──
RE_N5 = re.compile(r'^##\s*1\.\s*特性完整内容|^##\s*2\.\s*官方示例命令', re.M)
# ── 组级「现网无实例」明示（特性未配置时的正确形态，不是缺陷）──
RE_NOINST = re.compile(r'⛔\s*现网无实例|该组未配置')
# ── 旧形态标记（用于识别「还是旧产物」）──
RE_OLD_SPAN = re.compile(r'^#{2,4}\s*\d+\.\d+\s*EXP\s*行\s*[\d,]+', re.M)
# ── 开关判定类标记 ──
RE_SWITCH_SEC = re.compile(r'^###\s*二、', re.M)


def scan(text):
    """单产物扫描 → 判据命中字典"""
    return {
        'N1': len(RE_N1.findall(text)),
        'N2': len(RE_N2.findall(text)),
        'N3': len(RE_N3.findall(text)),
        'N4': len(RE_N4.findall(text)),
        'N4S': len(RE_N4_STATE.findall(text)),
        'N5': len(RE_N5.findall(text)),
        'NI': len(RE_NOINST.findall(text)),
        'OLD': len(RE_OLD_SPAN.findall(text)),
        'SW': len(RE_SWITCH_SEC.findall(text)),
    }


NAMES = {'N1': '组结构（link_groups 装配）', 'N2': '实例聚合（组内按共享值）',
         'N3': '逐跳说明（//通过X关联到Y）', 'N4': '结论段存在',
         'N4S': '三态结论（命中/枚举不符/未配置）', 'N5': '文档原文+示例块',
         'OLD': '旧区间标题（应为 0）', 'SW': '开关判定段（### 二、）',
         'NI': '组级无实例明示（未配置）'}


def verdict(h, is_switch):
    """按产物类型给判定（链装配类 / 开关判定类 判据不同）"""
    if h['OLD']:
        return '旧形态（区间平铺，未走链装配）', False
    if is_switch:
        # 开关判定类：无组/实例是结构使然；必须有结论三态
        ok = h['N4S'] > 0
        return ('开关判定类·合格' if ok else '开关判定类·缺三态结论'), ok
    if h['N1'] == 0:
        return '链装配类但无组结构（可疑）', False
    # 链装配类：组结构 + 结论三态，且「实例」或「无实例明示」至少有一个。
    #   ⚠ N2 不能作为硬条件 —— 特性未配置时产物是「有组 + ⛔现网无实例」，
    #     这是正确形态（实测 F270 等 23 篇），把 N2 当硬条件会误判成缺陷。
    #   N3 逐跳同理可缺（组内可能全是汇聚/未配）。
    ok = h['N4S'] > 0 and (h['N2'] > 0 or h['NI'] > 0)
    return ('链装配类·合格' if ok else '链装配类·要素不全'), ok


def main():
    if '--selftest' in sys.argv:
        return selftest()

    root = Path(sys.argv[1])
    gt = root / '特性配置基线'
    if not gt.is_dir():
        gt = root
    # README 是目录说明，不是特性产物（实测唯一「不合格」就是它）
    mds = [p for p in sorted(gt.glob('*.md')) if p.name != 'README.md']
    if not mds:
        print('✗ 无产物: %s' % gt)
        return 1

    print('产物目录: %s' % gt)
    print('产物 %d 篇' % len(mds))
    print()

    tot = Counter()
    rows = []
    kinds = Counter()
    for md in mds:
        t = md.read_text(encoding='utf-8', errors='replace')
        h = scan(t)
        for k in ('N1', 'N2', 'N3', 'N4', 'N4S', 'N5', 'OLD', 'SW'):
            tot[k] += (h[k] > 0)
        is_switch = h['SW'] > 0 and h['N1'] == 0
        v, ok = verdict(h, is_switch)
        kinds[v.split('·')[0]] += 1
        rows.append((md.name, h, v, ok, is_switch))

    print('═' * 74)
    print('判据覆盖（多少篇产物里出现过）')
    print('═' * 74)
    for k in ('N1', 'N2', 'N3', 'N4', 'N4S', 'N5'):
        n = tot[k]
        pct = 100.0 * n / len(mds)
        print('  %-4s %-28s %5d/%d (%5.1f%%) %s' % (
            k, NAMES[k], n, len(mds), pct, '█' * int(pct / 4)))
    print()
    print('  旧区间标题残留: %d 篇  %s' % (
        tot['OLD'], '✓ 全无（已是新形态）' if not tot['OLD'] else '⚠ 仍有旧产物'))
    print()

    print('═' * 74)
    print('产物类型分布')
    print('═' * 74)
    for k, v in kinds.most_common():
        print('  %-40s %5d 篇' % (k, v))
    print()

    n_ok = sum(1 for r in rows if r[3])
    print('═' * 74)
    print('判定: %d / %d 篇合格 (%.1f%%)' % (
        n_ok, len(rows), 100.0 * n_ok / len(rows)))
    bad = [r for r in rows if not r[3]]
    if bad:
        print('  不合格 %d 篇，示例:' % len(bad))
        for name, h, v, ok, sw in bad[:6]:
            print('     %-46s %s' % (name[:44], v))
    print('═' * 74)
    return 0 if n_ok == len(rows) else 2


# ═══ 自证：正/反/边界成对（改判据必跑）═══
POS_CHAIN = """# 基于位置分配地址

## 1. 特性完整内容（官方文档原文）

### 操作场景

运营商规划UDG基于位置区为UE分配IP地址时，可激活本特性。

## 2. 官方示例命令（特性文档原始配置示例，完整）

```text
ADD POOL: POOLNAME="testpool1";
```

## 3. 现网实例（链装配）

### 一、基于位置分配地址

#### 组 1: ADD POOL + ADD SECTION    [共享参数: POOLNAME]

  现网实例: 600 条（完整 24 / 枚举不符 576 / 缺命令 0）

  **实例 1. pool_cmnet_ipv4** — ✅ 完整

  ```text
  L1  ADD POOL: POOLNAME="pool_cmnet_ipv4";
  //通过 POOLNAME 关联到 ADD SECTION
  L2  ADD SECTION: POOLNAME="pool_cmnet_ipv4", IPVERSION=IPV4;
  ```

  **实例 2. pool_cmnet_ipv6** — 枚举不符: ADD SECTION

> 枚举不符明细（期望=文档示例值）: ADD SECTION: IPVERSION=IPV6≠IPV4

### 三、结论

- ✅ 命中: ADD POOL（符合 24/600 条）
- ⛔ 未配置·严重(L1,1): ADD XXX
"""

# 开关判定类：无组无实例（结构使然），但有结论三态
POS_SWITCH = """# 配置系统过载特性

## 1. 特性完整内容（官方文档原文）

### 操作场景

略。

## 2. 官方示例命令（特性文档原始配置示例，完整）

```text
SET APNACCESSWAL: SWITCH=ENABLE;
```

## 3. 现网实例（链装配）

### 二、开关类特性

✅ SET DEACTIVERATE
   L96386 SET DEACTIVERATE:RATE=50;

### 三、结论

- ⛔ 未配置·严重(L1,1): SET APNACCESSWAL —— 特性很可能未生效
- 枚举不符·提示(L3,1): SET XXX
"""

# 反例 1：旧区间平铺产物
NEG_OLD = """# 配置系统过载特性

## 3.8 EXP 行 45671–94602（48489 条：ADD FLTBINDFLOWF×43630 ...）

12530_01_l7_f
139yxlj_00_l7_f_001
"""

# 反例 2：流程图箭头（假阳性陷阱）—— md 列表缩进也不算层深
NEG_ARROW = """# 某特性

## 配置步骤

      **SET A** → **SET B** → **SET C**
"""

# 边界：链装配段有组但无实例、无结论（要素不全）
EDGE_INCOMPLETE = """# 某特性

## 1. 特性完整内容（官方文档原文）

略

## 3. 现网实例（链装配）

#### 组 1: ADD A + ADD B    [共享参数: X]
"""

# 边界 2：有组但现网未配置（正确形态，不是缺陷）—— 实测 F270 等 23 篇
EDGE_UNCONFIGURED = """# 某特性

## 1. 特性完整内容（官方文档原文）

略

## 2. 官方示例命令（特性文档原始配置示例，完整）

```text
ADD CCT: ...;
```

## 3. 现网实例（链装配）

#### 组 1: ADD CCT + ADD SELECTCCTBYCC    [共享参数: CCTMPLTNAME]

  ⛔ 现网无实例 —— 该组未配置

### 三、结论

- ⛔ 未配置·严重(L1,1): ADD CCT
"""


def selftest():
    cases = [
        ('正例·链装配类', POS_CHAIN, False, True),
        ('正例·开关判定类', POS_SWITCH, True, True),
        ('反例·旧区间平铺', NEG_OLD, False, False),
        ('反例·流程箭头假阳性', NEG_ARROW, False, False),
        ('边界·要素不全', EDGE_INCOMPLETE, False, False),
        ('边界·有组但未配置', EDGE_UNCONFIGURED, False, True),
    ]
    print('=' * 74)
    print('判据自证（正例 / 反例 / 边界 成对）')
    print('=' * 74)
    n_pass = 0
    for label, text, is_sw, want_ok in cases:
        h = scan(text)
        # 类型判定用文本自身特征（模拟真实调用）
        real_sw = h['SW'] > 0 and h['N1'] == 0
        v, ok = verdict(h, real_sw)
        good = (ok == want_ok)
        n_pass += good
        print('  %-20s N1=%d N2=%d N3=%d N4S=%d OLD=%d → %-28s %s' % (
            label, h['N1'], h['N2'], h['N3'], h['N4S'], h['OLD'],
            v, '✓' if good else '✗ 期望 ok=%s' % want_ok))
    print()
    # 假阳性专项：反例必须被判为不合格
    h = scan(NEG_ARROW)
    fp_ok = h['N1'] == 0 and h['N3'] == 0 and h['N2'] == 0
    print('  假阳性守卫（流程箭头/列表缩进不得计入）: %s' %
          ('✓' if fp_ok else '✗ N1=%d N2=%d N3=%d' % (h['N1'], h['N2'], h['N3'])))
    n_pass += fp_ok
    print()
    total = len(cases) + 1
    print('=' * 74)
    print('%s  %d/%d' % ('✓ 全部通过' if n_pass == total else '✗ 有失败',
                         n_pass, total))
    print('=' * 74)
    return 0 if n_pass == total else 1


if __name__ == '__main__':
    sys.exit(main())
