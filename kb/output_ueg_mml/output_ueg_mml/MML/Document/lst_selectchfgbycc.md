# 查询基于CC选择CHF处理（LST SELECTCHFGBYCC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于查询基于CC选择CHF处理。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

无

## 使用实例

查询基于CC选择CHF处理：

```
%%LST SELECTCHFGBYCC:;%%
RETCODE = 0  操作成功

结果如下
--------
      Charge Characteristic类型  =  未指定Charge Characteristic的值
        Charge Characteristic值  =  0x0000
Charge Characteristic特定值掩码  =  0xFFFF
    Charge Characteristic优先级  =  0
                        主CHF组  =  chf-grp01
                        备CHF组  =  NULL
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称                      | 输出项解释                                  |
|:---------------------------|:---------------------------------------|
| Charge Characteristic类型    | 该参数用于指定计费属性。                           |
| Charge Characteristic值     | 该参数用于指定特殊的Charge Characteristic值。      |
| Charge Characteristic特定值掩码 | 该参数用于指定计费属性的掩码。                        |
| Charge Characteristic优先级   | 该参数用于设置优先级；不允许指定相同的优先级；配置mask时必须指定优先级。 |
| 主CHF组                      | 该参数用于设置主CHF组。                          |
| 备CHF组                      | 该参数用于设置备CHF组。                          |