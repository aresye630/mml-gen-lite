# 增加IMSI/MSISDN/IMEISV号段组（ADD SUBSCRIBERIDSEGGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来配置IMSI/MSISDN/IMEISV号码段组，用于根据号段组选择USERPROFILE作为本地策略、根据号段选择OCS、用户根据号段选择OCS组以及在线计费模板、根据号段选择CG组、根据号段选择SGW离线计费方式等。

#### 注意事项

- 该命令执行后立即生效。
- 如果绑定多个IMSI/MSISDN/IMEISV号码段，需多次执行此命令。
- 系统最大支持配置128条IMSI/MSISDN/IMEISV号码段组。每条IMSI/MSISDN/IMEISV号码段组最大绑定12000条IMSI/MSISDN/IMEISV号码段，号段组单个UNC绑定规格为25000个。
- 配置SUBSCRIBERIDSEGGRP前，需要首先通过ADD IMSIMSISDNSEG命令或ADD IMEISVSEG命令配置号段。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称                    | 参数说明                                                                                                                                     |
|:-------------|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| SEGGROUPNAME | IMSI/MSISDN/IMEISV号段组名称 | 可选必选说明：必选参数 参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                            |
| SEGMENTNAME  | IMSI/MSISDN/IMEISV号段名称  | 可选必选说明：必选参数 参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD IMSIMSISDNSEG命令配置生成。 |
| SEGMENTTYPE  | 号段类型                    | 可选必选说明：必选参数 参数含义：该参数用于指定用户标识号段类型。 数据来源：本端规划 取值范围：枚举类型。 IMSIMSISDN：IMSIMSISDN类型号段。IMEISV：IMEISV类型号段。 默认值：无 配置原则：无                         |

#### 使用实例

配置IMSI/MSISDN/IMEISV号码段组内添加一个号段，其中IMSI/MSISDN/IMEISV号段组名称为group1，IMSI/MSISDN号段名称为huawei：

```
ADD SUBSCRIBERIDSEGGRP: SEGGROUPNAME="group1", SEGMENTNAME="huawei", SEGMENTTYPE=IMEISV;
```