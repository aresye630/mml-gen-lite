#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""引号规则自证：正例（该带）/ 反例（不该带）配对，确保判据有判别力。

不变量（很重要）：
  · 字符串标识（含 . 或小写字母）→ 必须带引号
  · 纯大写枚举 / 开关 → 必须**不**带
  · 纯数字 / IP → 必须**不**带
  · 已带引号 → 幂等（不重复加）
"""
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent      # materials/
spec = importlib.util.spec_from_file_location('ga', ROOT / 'backend' / 'gen_assemble.py')
ga = importlib.util.module_from_spec(spec)
sys.modules['ga'] = ga
spec.loader.exec_module(ga)

ok = fail = 0


def chk(desc, param, val, want):
    global ok, fail
    got = ga.needs_quote(param, val)
    if got == want:
        ok += 1
        print(f'  [OK]   {desc:44s} {param}={val!r:22s} → {"带引号" if got else "不带"}')
    else:
        fail += 1
        print(f'  [FAIL] {desc:44s} {param}={val!r:22s} → 期望 want={want} 实际={got}')


def chk_q(desc, param, val, want):
    """测 quote_value 的最终形态"""
    global ok, fail
    got = ga.quote_value(param, val)
    if got == want:
        ok += 1
        print(f'  [OK]   {desc:44s} {param}={val!r:22s} → {got!r}')
    else:
        fail += 1
        print(f'  [FAIL] {desc:44s} 期望 {want!r} 实际 {got!r}')


print('─── 正例：字符串标识必须带引号 ───')
chk('APN 域名形态', 'APN', 'cbiotgzqjyjgb001.gd', True)
chk('APN 简单标识', 'APN', 'cmnet', True)
chk('VPN 实例名', 'VPNINSTANCE', 'VRF_Internet', True)
chk('对象名（推导结果）', 'BWMSERVICENAME', 'bs_wecall_2g', True)
chk('对象名（连字符）', 'BWMCNAME', 'bc-p2p-subs', True)
chk('过滤名（含数字序号）', 'FILTERNAME', '12530_01_f_f_001', True)
chk('APN 占位符（专家待替换）', 'APN', '<APN>', True)

print('─── 反例①：枚举/开关不得带引号 ───')
chk('开关', 'HASVPN', 'ENABLE', False)
chk('枚举（继承）', 'PSEUDOACTSWITCH', 'INHERIT', False)
chk('类型枚举', 'CTRLTYPE', 'CAR', False)
chk('带宽控制类型', 'BWMSERVICETYPE', 'TOS', False)
chk('用户组类型', 'USERGROUPTYPE', 'SPECIFIC_GROUP', False)
chk('刷新类型', 'REFRESHTYPE', 'ALL', False)

print('─── 反例②：数字/IP 不得带引号 ───')
chk('数值 CIR', 'CIR', '50', False)
chk('数值 CBS', 'CBS', '9600', False)
chk('优先级', 'BWMRULEPRI', '80', False)
chk('IPv4', 'IPADDR', '20.16.2.36', False)

print('─── 幂等性：已带引号不重复加 ───')
chk_q('已带引号', 'APN', '"cmnet"', '"cmnet"')
chk_q('裸值 → 加引号', 'APN', 'cmnet', '"cmnet"')
chk_q('枚举 → 不加', 'HASVPN', 'ENABLE', 'ENABLE')

print('─── 现网实证：APN 行应逐参数正确 ───')
chk_q('现网行复现', 'APN', 'cmnet', '"cmnet"')
chk_q('现网行复现', 'HASVPN', 'ENABLE', 'ENABLE')
chk_q('现网行复现', 'VPNINSTANCE', 'VRF_Internet', '"VRF_Internet"')
chk_q('现网行复现', 'PSEUDOACTSWITCH', 'INHERIT', 'INHERIT')

print(f'\n结果: {ok}/{ok + fail} 通过')
sys.exit(1 if fail else 0)
