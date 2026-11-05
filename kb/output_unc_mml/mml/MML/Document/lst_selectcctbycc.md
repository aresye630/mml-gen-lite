# 查询基于CC配置融合计费模板处理（LST SELECTCCTBYCC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF、SGW-C**

该命令用于查询基于CC配置融合计费模板处理。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询基于CC配置的融合计费模板：

```
%%LST SELECTCCTBYCC:;%%
RETCODE = 0  操作成功

结果如下
--------
                         CC类型  =  未指定Charge Characteristic的值
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0xFFFF
    Charge Characteristic优先级  =  0
               融合计费模板名称  =  global
I-SMF/SGW使用的融合计费模板名称  =  servingcct
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                                     |
|:---------------------------|:----------------------------------------------------------|
| CC类型                       | 该参数用于指定计费属性。                                              |
| Charge Characteristic值     | 该参数用于指定特殊的CC值。                                            |
| Charge Characteristic特定值掩码 | 该参数用于指定CC的掩码，通过配置掩码可以实现全匹配CC值，还是只匹配部分bit位。                |
| Charge Characteristic优先级   | 该参数用于设置优先级，配置mask时必须指定优先级，不允许指定相同的优先级。                    |
| 融合计费模板名称                   | 该命令用于指定融合计费模板（Converged Charging Template）名称。             |
| I-SMF/SGW使用的融合计费模板名称       | 该命令用于指定I-SMF/SGW使用的融合计费模板（Converged Charging Template）名称。 |