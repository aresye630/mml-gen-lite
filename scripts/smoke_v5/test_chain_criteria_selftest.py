#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chain_criteria 判据自证：每个特征都必须「正例命中、反例不命中」。

⚠ 本文件 2026-09-19 重写：原版用的是旧判据（F1~F5 + RE_SPAN），
   而 chain_criteria.py 已改版为认新产物形态（N1~N5）。
   旧套件早已失效（AttributeError: RE_F1）却没人发现 ——
   说明「套件全绿」不能光看有没有跑，还要看它跟实现是否同版本。
   本次由集成测试抓出（test_integration.py 会跑本套件）。

正例 = 新形态产物片段（组结构 + 实例聚合 + 逐跳说明 + 三态结论）
反例 = 旧平铺样式（区间标题 + 裸命令列表，无跳转说明、无结论三态）
边界 = 会误导判据的两种文本（流程箭头 / md 列表缩进）
"""
import sys

sys.path.insert(0, '/opt/expgv/scripts')
import chain_criteria as C   # noqa: E402

PASS, FAIL = [], []


def chk(name, cond, detail=''):
    (PASS if cond else FAIL).append(name)
    print(f'  {"✓" if cond else "✗"} {name}' + (f'  — {detail}' if detail else ''))


# ── 正例：新形态（自包含内嵌，不依赖任何外部文件）──
GOOD = """# 基于位置分配地址

## 3. 现网实例（链装配）

### 二、现网实例（EXP 中的实际配置）

#### 组 1: ADD VPNINST + ADD APN    [共享参数: VPNINSTANCE]

  现网实例: 2 条（完整 2 / 缺命令 0）

  **实例 1. VPN.A.GD** — ✅ 完整

  ```text
  L1553 ADD VPNINST:VPNINSTANCE="vpn.a.gd";
  //通过 VPN.A.GD 关联到 ADD APN
  L1588 ADD APN:APN="a.gd", HASVPN=ENABLE, VPNINSTANCE="vpn.a.gd";
  ```

### 三、结论

- 现网状态: 命中 2 / 枚举不符 0 / 未配置 1（共 3 条指纹命令）
- 未配置·严重（L1，1）: SET APNACCESSWAL  —— 特性专有命令

## 1. 特性完整内容（官方文档原文）

### 操作场景

在系统负荷较重的情况下，建议开启流控策略。

## 2. 官方示例命令（特性文档原始配置示例，完整）

```mml
ADD APN:APN="apn1";
```
"""

# ── 反例：旧平铺样式（区间 + 裸命令，无组/无跳转/无三态）──
FLAT = """# 某特性
## 3. exp 对应实例
### 3.2 EXP 行 3060–30332（27273 条：ADD FILTER×27273）
```text
 3060  ADD FILTER:FILTERNAME="a", L34PROTTYPE=STRING;
 3061  ADD FILTER:FILTERNAME="b", L34PROTTYPE=STRING;
```
"""

# ── 边界文本（易误导）──
ARROW = "**配置步骤命令链**：SET LICENSESWITCH → SET FPIFUNC → ADD FILTER\n"
BOLD_LIST = "1. 步骤：\n      **ADD FILTER**\n      **ADD FLOWFILTER**\n"


def L(name):
    """判据是否命中（返回命中数）。"""
    rx = getattr(C, name, None)
    if rx is None:
        return None
    return len(rx.findall(GOOD))


print('═══ N1 组结构（link_groups 装配）═══')
n = L('RE_N1')
chk('判据存在', n is not None, '缺 RE_N1' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % n)
    chk('反例不命中', len(C.RE_N1.findall(FLAT)) == 0)

print('═══ N2 实例聚合（组内按共享值）═══')
n = L('RE_N2')
chk('判据存在', n is not None, '缺 RE_N2' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % len(C.RE_N2.findall(GOOD)))
    chk('反例不命中', len(C.RE_N2.findall(FLAT)) == 0)

print('═══ N3 逐跳说明（//通过X关联到Y）═══')
n = L('RE_N3')
chk('判据存在', n is not None, '缺 RE_N3' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % len(C.RE_N3.findall(GOOD)))
    chk('反例不命中', len(C.RE_N3.findall(FLAT)) == 0)
    chk('边界·流程箭头不命中', len(C.RE_N3.findall(ARROW)) == 0)

print('═══ N4 结论段 ═══')
n = L('RE_N4')
chk('判据存在', n is not None, '缺 RE_N4' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % len(C.RE_N4.findall(GOOD)))
    chk('反例不命中', len(C.RE_N4.findall(FLAT)) == 0)

print('═══ N4S 三态结论 ═══')
n = L('RE_N4_STATE')          # 实现里的名字是 RE_N4_STATE（N4S 是展示名）
chk('判据存在', n is not None, '缺 RE_N4_STATE' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % len(C.RE_N4_STATE.findall(GOOD)))
    chk('反例不命中（平铺无三态）', len(C.RE_N4_STATE.findall(FLAT)) == 0)

print('═══ N5 文档原文 + 示例块 ═══')
n = L('RE_N5')
chk('判据存在', n is not None, '缺 RE_N5' if n is None else '')
if n is not None:
    chk('正例命中', n > 0, '%d 处' % len(C.RE_N5.findall(GOOD)))
    chk('反例不命中', len(C.RE_N5.findall(FLAT)) == 0)

print('═══ 旧形态标志（区间标题）═══')
n = L('RE_OLD_SPAN')          # 实现里的名字是 RE_OLD_SPAN
chk('判据存在', n is not None, '缺 RE_OLD_SPAN' if n is None else '')
if n is not None:
    chk('反例命中区间（平铺标志）', len(C.RE_OLD_SPAN.findall(FLAT)) > 0)
    chk('正例不含区间', len(C.RE_OLD_SPAN.findall(GOOD)) == 0)

print()
print('═' * 56)
print(f'  通过 {len(PASS)} / {len(PASS) + len(FAIL)}')
for f in FAIL:
    print(f'    ✗ {f}')
raise SystemExit(1 if FAIL else 0)
