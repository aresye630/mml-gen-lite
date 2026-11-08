# exp_pairs 工具设计

## 为什么需要

agent 写模板时，最难的是推断「A 族的对象名 → B 族的对象名」的命名规律。
现在只能靠 agent 自己对比 exp_baseline 返回的样本，容易漏或猜错。

实测：NC20260824002208 的 97 对配对全是 `grp-* → pool-*` 前缀替换，
但 agent 需要看多个样本才能确认这个规律。

## 工具设计

```
exp_pairs(path, family_a, family_b, limit=20)
```

**原理**：
1. 用 exp_siblings 的方法找出 A 和 B 的引用关系
2. 找出现网里实际配对的实例（B 的参数引用了 A 的主键值）
3. 提取 A 主键 → B 主键的命名对
4. 自动归纳命名规律（用 derivation.py 的算子试探）

**返回**：
```json
{
  "family_a": "POOLGROUP",
  "family_b": "POOL",
  "pairs": [
    {"a": "grp-cmnet-ipv6-lfsmf01-tj-bcq", "b": "pool-cmnet-ipv6-lfsmf01-tj-bcq"},
    ...
  ],
  "inferred_rules": [
    {"op": "PREFIX_REPLACE", "args": ["grp", "pool"], "coverage": "97/97"}
  ],
  "samples": 20
}
```

**关键**：`inferred_rules` 用真实的 derivation 算子试探，返回 agent 可以直接用的写法。

## 后续流程

```
1. agent: exp_siblings(ADD POOL)        → 知道配套族
2. agent: exp_pairs(POOLGROUP, POOL)    → 知道 grp→pool 规律
3. agent: exp_pairs(POOLGROUP, POOLGRPMAP) → 知道 grp→map + 加制式后缀
4. agent: 写模板，值列直接抄 inferred_rules 的写法
```

## 覆盖度保证

- 每个 rule 带 coverage（例 `97/97`），agent 能判断是否可靠
- 无法归纳的配对会列在 `unmatched` 里，agent 能看到残留风险
