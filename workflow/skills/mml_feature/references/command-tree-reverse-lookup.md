# 命令树反查：把命令映射到官方功能分类

## 用途

分析"某 exp 涉及多少特性"时，把 exp 的命令类型批量反查到 UEG 官方功能分类
（如 DN管理/业务匹配策略/业务控制策略/VNRS功能管理），验证手工特性聚类、
发现遗漏特性域（如路径管理/会话管理/质量监控）。

## 数据源

`~/workspace/zhijian/ueg_command_tree.json`（10,587 条命令，由
exp-config-analyzer 的 build_command_tree.py 生成）

## 结构（⚠️ children 是 dict 不是 list）

```json
{
  "name": "UEG MML命令",
  "children": {
    "平台服务管理": {
      "name": "平台服务管理",
      "children": { "单体服务公共功能管理": { "children": {...}, "commands": [...] } },
      "commands": [ {"cmd": "LST MSISDNSUBGPMEMALL", "nfs": []} ]
    }
  },
  "commands": [...]
}
```

## 反查方法

```python
import json
t = json.load(open('ueg_command_tree.json'))
cmd_index = {}   # cmd -> [分类路径列表]
def walk(node, path):
    for c in node.get('commands', []):
        cmd_index.setdefault(c['cmd'], []).append(path)
    for name, child in node.get('children', {}).items():
        walk(child, path + [name])
walk(t, [t['name']])
# 对 exp 中每个命令类型 cmd 查 cmd_index[cmd]，取三级分类路径聚合统计
```

命中率通常 95%+；未收录命令多为运维类（LCK / SET NTPCFG / SET ALMINFO 等）
或命令树版本（v21.12.2）之后的较新特性命令——标记"未收录，需人工确认"。

## 与其他检索方式的配合（特性覆盖分析三层法）

1. 命令树反查：批量、精确、分类权威 → 官方功能分类
2. Milvus 语义检索（本 skill hybrid_search.py）：模糊定位特性名
   （"EPRP 双机热备"→"使能热备容灾功能"）
3. 特性文档 JSON 关键词 grep：精确确认（语义检索命中不准时兜底）
   - 数据源：`~/workspace/zhijian/output_ueg_feature/output_ueg_feature_v2/`
     （991 个 JSON，字段 feature_name / feature_description / full_nav）

产出：特性域三分类（规则已覆盖 / 候选扩展补 chains.yaml / 系统级降噪白名单）。
