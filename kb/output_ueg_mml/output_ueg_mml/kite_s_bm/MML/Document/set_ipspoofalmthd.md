# 设置IP Spoofing攻击告警阈值控制（SET IPSPOOFALMTHD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来配置是否产生ip spoofing告警以及何时产生告警。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- ip spoofing事件：系统的PDP如果受到ip spoofing攻击，则认为是一个事件，以PDP作为事件单位。
- 当ALARMSWITCH从ENABLE配置为DISABLE时，INITTHRESH和ADDTHRESH将恢复为默认记录。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | ALARMSWITCH   |   INITTHRESH |   ADDTHRESH |
|:-------|:--------------|-------------:|------------:|
| 初始值    | DISABLE       |         1000 |        1000 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称              | 参数说明                                                                                                                                                                      |
|:------------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALARMSWITCH | anti spoofing告警开关 | 可选必选说明：必选参数 参数含义：该参数用于配置是否打开anti spoofing告警功能。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：设置ENABLE：使能，打开anti spoofing告警功能；设置DISABLE: 不使能，关闭anti spoofing告警功能。 |
| INITTHRESH  | 初始阈值              | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMSWITCH”配置为“ENABLE”时为可选参数。 参数含义：该参数用于在anti spoofing事件计数大于INITTHRESH值时触发事件告警。 数据来源：本端规划 取值范围：整数类型，取值范围为100～65535。 默认值：无 配置原则：无                 |
| ADDTHRESH   | 增量阈值              | 可选必选说明：条件可选参数 前提条件：该参数在“ALARMSWITCH”配置为“ENABLE”时为可选参数。 参数含义：该参数用于在anti spoofing事件计数减去INITTHRESH等于ADDTHRESH的整数倍时再次触发告警。 数据来源：本端规划 取值范围：整数类型，取值范围为100～65535。 默认值：无 配置原则：无   |

#### 使用实例

假设运营商需要感知ip spoofing是否到达所配置的INITTHRSH为1500，ADDTHRESH为1500时告警：

```
SET IPSPOOFALMTHD:ALARMSWITCH=ENABLE,INITTHRESH=1500,ADDTHRESH=1500;
```