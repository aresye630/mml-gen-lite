# 删除IMSI和MSISDN号段（RMV IMSIMSISDNSEG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于删除IMSI/MSISDN号码段。

#### 注意事项

- 该命令执行后立即生效。
- 如果输入的字段SEGMENTNAME被引用，则不能删除该记录。可以通过LST PCRFGRPBNDAPN/LST GLBPCRFGROUP/LST UPBINDUPG/LST SUBSCRIBERIDSEGGRP/LST GLBDIAMREALM/LST L2RULEGRPBIND分别查询不同的引用记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                |
|:------------|:----------------|:--------------------------------------------------------------------------------------------------------------------|
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：可选参数 参数含义：该参数用于指定IMSI/MSISDN号段名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：若此参数未填充，则删除所有号段。 |

#### 使用实例

删除IMSI和MSISDN号段，SEGMENTNAME为huawei，命令为：

```
RMV IMSIMSISDNSEG:SEGMENTNAME="huawei";
```