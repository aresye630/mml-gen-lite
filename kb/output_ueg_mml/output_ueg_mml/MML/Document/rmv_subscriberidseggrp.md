# 删除IMSI/MSISDN/IMEISV号段组（RMV SUBSCRIBERIDSEGGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来删除IMSI/MSISDN/IMEISV号码段组或号段组与号段的绑定关系。如果删除号段组，该号段组下所有的号段绑定关系同步删除。

#### 注意事项

- 该命令执行后立即生效。
- 如果输入IMSI/MSISDN/IMEISV号码段组与IMSI/MSISDN/IMEISV号码段，表示解除该号码段组与号码段的绑定关系。如果只输入IMSI/MSISDN/IMEISV号码段组，表示解除该号码段组下所有号码段的绑定信息并删除该号码段组。如果此IMSI/MSISDN/IMEISV号码段组被其他命令使用，则不允许删除。可以通过LST OCSBINDING/LST OCSGRPBINDING/LST CGGRPBINDING/LST SGWSEGGCHGMETH/LST UPBINDUPG分别查询不同的引用记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称                    | 参数说明                                                                                                                                    |
|:-------------|:------------------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                           |
| SEGMENTNAME  | IMSI/MSISDN/IMEISV号段名称  | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：若此参数未填充，则删除号段组下所有号段信息。       |
| SEGMENTTYPE  | 号段类型                    | 可选必选说明：可选参数 参数含义：该参数用于指定用户标识号段类型。 数据来源：本端规划 取值范围：枚举类型。 IMSIMSISDN：IMSIMSISDN类型号段。IMEISV：IMEISV类型号段。 默认值：无 配置原则：若指定了SegmentName，此参数需要指定。 |

#### 使用实例

删除IMSI/MSISDN/IMEISV号码段组，其中IMSI/MSISDN/IMEISV号段组名称为group1：

```
RMV SUBSCRIBERIDSEGGRP: SEGGROUPNAME="group1";
```