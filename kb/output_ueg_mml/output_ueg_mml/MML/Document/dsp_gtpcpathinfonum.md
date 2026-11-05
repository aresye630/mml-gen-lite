# 显示GTPC路径数目（DSP GTPCPATHINFONUM）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、PGW-C、SGW-C、GGSN**

该命令用于查询GTP-C路径数目。

## 注意事项

当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令DSP GTPCPATHNUM查询。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询GTP-C路径数目：DSP GTPCPATHINFONUM:;

```
%%DSP GTPCPATHINFONUM:;%%
RETCODE = 0  操作成功

结果如下
--------
路径数目  =  0
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释             |
|:--------|:------------------|
| 路径数目    | 该参数用于指示GTP-C路径数目。 |