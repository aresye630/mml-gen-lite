# 设置OSPF的平滑重启（SET OSPFGR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于配置设备平滑重启Helper模式。

#### 注意事项

- 该命令执行后立即生效。
- 只有执行MOD OSPF配置了OPAQCAPFLG才能使用此命令。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| HELPERROLEFLAG   | PLANNEDONLYFLG   | IGNEXTELSAFLG   | NEVERFLAG   | HELPERFLAG   | HELPERFILTERTYPE   |
|:-----------------|:-----------------|:----------------|:------------|:-------------|:-------------------|
| False            | False            | False           | False       | False        | none               |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称                  | 参数说明                                                                                                                                                                           |
|:-----------------|:----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROCID           | 进程号                   | 可选必选说明：必选参数 参数含义：OSPF进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295。 默认值：无 配置原则：OSPF进程必须已经存在。请使用LST OSPF命令查看可用的OSPF进程。                                                             |
| HELPERROLEFLAG   | 使能Helper模式            | 可选必选说明：必选参数 参数含义：使能Helper模式。 数据来源：本端规划 取值范围：枚举类型。 FALSE：不使能。TRUE：使能。 默认值：无 配置原则：当HELPERROLEFLAG配置为TRUE时，至少需要配置PLANNEDONLYFLG、IGNEXTELSAFLG、NEVERFLAG或HELPERFILTERTYPE四个参数其中一个。 |
| PLANNEDONLYFLG   | 只支持计划GR               | 可选必选说明：条件可选参数 前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。 参数含义：在设备上支持计划内的平滑重启。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 配置原则：缺省情况下，设备支持planned-GR和unplanned-GR。           |
| IGNEXTELSAFLG    | 不检查Type-5和Type-7类的LSA | 可选必选说明：条件可选参数 前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。 参数含义：不检查Type-5和Type-7类的LSA。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无                                            |
| NEVERFLAG        | 不支持Helper模式           | 可选必选说明：条件可选参数 前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。 参数含义：不支持Helper模式。 数据来源：本端规划 取值范围：枚举类型。 FALSE：不使能。TRUE：使能。 默认值：无                                                        |
| HELPERFLAG       | 使能GR                  | 可选必选说明：必选参数 参数含义：使能GR。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无                                                                                                         |
| HELPERFILTERTYPE | Helper过滤类型            | 可选必选说明：条件可选参数 前提条件：该参数在“HELPERROLEFLAG”配置为“TRUE”时为可选参数。 参数含义：Helper过滤类型。 数据来源：本端规划 取值范围：枚举类型。 acl_name：ACL名称。ip_prefix：IP前缀过滤策略名称。acl_num：ACL号。none：空。 默认值：无                   |
| HELPERROLEVALUE  | Helper过滤值             | 可选必选说明：条件必选参数 前提条件：该参数在“HELPERFILTERTYPE”配置为“acl_name”、“ip_prefix” 或 “acl_num”时为必选参数。 参数含义：Helper过滤值。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～169。 默认值：无                                 |

#### 使用实例

使能OSPF进程1的平滑重启Helper模式的策略特性，配置本地Helper策略为只支持Planned GR：

```
SET OSPFGR:PROCID=1,PLANNEDONLYFLG=TRUE,HELPERROLEFLAG=TRUE,NEVERFLAG=FALSE,HELPERFLAG=TRUE;
```