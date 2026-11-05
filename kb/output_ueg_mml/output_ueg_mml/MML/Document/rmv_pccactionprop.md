# 删除PCC动作属性（RMV PCCACTIONPROP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于删除PCC动作属性。支持批量删除，不输入条件，表示删除所有未被引用的PCC动作属性。

#### 注意事项

- 该命令执行后立即生效。
- 输入的PccActPropName通过LST PCCPOLICYGRP和LST SRVPBINDPCCPG查询PccPolicyGrp记录，如果引用了该PccActionProp的PccPolicyGrp的记录存在，则不允许删除PccActionProp记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称      | 参数说明                                                                                      |
|:---------------|:----------|:------------------------------------------------------------------------------------------|
| PCCACTPROPNAME | PCC动作属性名称 | 可选必选说明：可选参数 参数含义：设置PCC动作属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

删除名称为TestPccActPropName的PCC动作属性：

```
RMV PCCACTIONPROP:PCCACTPROPNAME="TestPccActPropName";
```