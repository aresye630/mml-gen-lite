# 查询IPDOMAIN组（LST BSFIPDOMAINGRP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询IPDOMAIN组。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                    |
|:--------|:-----------|:----------------------------------------------------------------------------------------|
| GRPNAME | IPDOMAIN组名 | 可选必选说明：可选参数  参数含义：该参数用于指定IPDOMAIN组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：无 |

## 使用实例

查询IPDOMAIN组"ipdomaingroup1"中的IPDOMAIN信息：

```
%%LST BSFIPDOMAINGRP: GRPNAME="ipdomaingroup1";%%
RETCODE = 0  操作成功

结果如下
--------
IPDOMAIN组名  =  ipdomaingroup1
IPDOMAIN名称  =  Domain_0
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称      | 输出项解释              |
|:-----------|:-------------------|
| IPDOMAIN组名 | 该参数用于指定IPDOMAIN组名。 |
| IPDOMAIN名称 | 该参数用于指定IPDOMAIN名称。 |