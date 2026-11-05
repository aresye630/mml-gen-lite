# 设置CCO策略（SET CCOPOLICY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

本条命令用于设置CCO拥塞控制策略开关。

#### 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | BWMCAR   | BWMSHAPING   | EFLOWTHROTTLE   | TOPLY   |
|:-------|:---------|:-------------|:----------------|:--------|
| 初始值    | ENABLE   | ENABLE       | DISABLE         | ENABLE  |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称           | 参数说明                                                                                              |
|:--------------|:---------------|:--------------------------------------------------------------------------------------------------|
| BWMCAR        | BWMCAR策略开关     | 可选必选说明：可选参数 参数含义：BWMCAR策略开关。 数据来源：本端规划 取值范围： DISABLE：不使能（关闭）。ENABLE：使能（开启）。 默认值：ENABLE 配置原则：无     |
| BWMSHAPING    | BWMSHAPING策略开关 | 可选必选说明：可选参数 参数含义：BWMSHAPING策略开关。 数据来源：本端规划 取值范围： DISABLE：不使能（关闭）。ENABLE：使能（开启）。 默认值：ENABLE 配置原则：无 |
| EFLOWTHROTTLE | 大象流抑制策略开关      | 可选必选说明：可选参数 参数含义：大象流抑制策略开关。 数据来源：本端规划 取值范围： DISABLE：不使能（关闭）。ENABLE：使能（开启）。 默认值：DISABLE 配置原则：无     |
| TOPLY         | TO分流策略开关       | 可选必选说明：可选参数 参数含义：TO分流策略开关。 数据来源：本端规划 取值范围： DISABLE：不使能（关闭）。ENABLE：使能（开启）。 默认值：ENABLE 配置原则：无       |

#### 使用实例

用户可以设置某种CCO拥塞控制策略是否生效; 例如：设置BWMCAR策略为可用，BWMSHAPING策略为可用，EFLOWTHROTTLE策略为不可用，TO策略为可用。

```
SET CCOPOLICY: BWMCAR=ENABLE, BWMSHAPING=ENABLE, EFLOWTHROTTLE=DISABLE, TOPLY=ENABLE;
```