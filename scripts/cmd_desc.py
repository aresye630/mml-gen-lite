#!/usr/bin/env python3
"""命令/参数说明解析（按需）：从 MML 指令文档提取命令功能 + 参数说明

索引：rules/cmd_doc_index_<产品>.yaml（build_cmd_doc_index.py 生成）
参数表：按索引 path 读取指令文档「参数说明」表格（参数标识|参数名称|参数说明）
说明精简：取「参数含义：…」段（至 数据来源/取值范围 前），缺省截 120 字。

用法（backend/CLI）：
  from cmd_desc import CmdDesc
  cd = CmdDesc('UEG')
  cd.cmd_meta('ADD RULE')            # {'name','func','path'} 或 None
  cd.param_desc('ADD RULE', ['POLICYTYPE','RULENAME'])
      # -> {'POLICYTYPE': {'name': '策略类型', 'desc': '…'}}
"""
import os
import re
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
RULES = Path(__file__).resolve().parent.parent / 'rules'

TABLE_ROW_RE = re.compile(r'^\|\s*([A-Z][A-Z0-9_]*)\s*\|\s*([^|]+?)\s*\|\s*(.*?)\s*\|\s*$')
MEAN_RE = re.compile(r'参数含义[:：]\s*(.*?)(?:数据来源|取值范围|默认值|配置原则|前提条件|可选必选|\Z)', re.S)


class CmdDesc:
    def __init__(self, product: str):
        self.product = product
        self._index = self._load_index(product)

    @staticmethod
    @lru_cache(maxsize=8)
    def _load_index(product: str):
        import yaml
        p = RULES / f'cmd_doc_index_{product.lower()}.yaml'
        if not p.exists():
            return {}
        return yaml.safe_load(p.read_text(encoding='utf-8')).get('cmds', {})

    def cmd_meta(self, cmd: str):
        """命令级说明：{name, func, path} 或 None"""
        m = self._index.get(cmd)
        if not m:
            return None
        return m

    @lru_cache(maxsize=512)
    def _table(self, cmd: str):
        """参数说明表：{PARAM: {name, desc}}（整表解析，缓存）"""
        m = self._index.get(cmd)
        if not m:
            return {}
        path = Path(os.path.expanduser('~')) / m['path']
        try:
            text = path.read_text(encoding='utf-8-sig', errors='replace')
        except Exception:
            return {}
        table = {}
        for ln in text.split('\n'):
            tm = TABLE_ROW_RE.match(ln.strip())
            if not tm:
                continue
            pid, pname, pdesc = tm.group(1), tm.group(2).strip(), tm.group(3).strip()
            if not pdesc or '参数含义' not in pdesc:
                continue
            mm = MEAN_RE.search(pdesc)
            desc = (mm.group(1).strip() if mm else pdesc[:120]).strip()
            desc = re.sub(r'\s+', ' ', desc)[:140]
            table[pid] = {'name': pname, 'desc': desc}
        return table

    def param_desc(self, cmd: str, params):
        """参数级说明：{PARAM: {name, desc}}（仅返回能解析到的）"""
        t = self._table(cmd)
        return {p: t[p] for p in params if p in t}


if __name__ == '__main__':
    cd = CmdDesc(sys.argv[1] if len(sys.argv) > 1 else 'UEG')
    for cmd, ps in [('ADD RULE', ['POLICYTYPE', 'RULENAME']),
                    ('ADD FILTER', ['L34PROTOCOL', 'FILTERNAME'])]:
        m = cd.cmd_meta(cmd)
        print(f'== {cmd}：{m["name"] if m else "?"} | {m["func"][:50] if m and m["func"] else ""}')
        for p, d in cd.param_desc(cmd, ps).items():
            print(f'   {p} {d["name"]}: {d["desc"][:70]}')
