# 设置RADIUS计费服务器可选消息属性（SET RDSACCTREQATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来新增指定RADIUS服务器组的RADIUS计费私有扩展属性的配置，用来控制RADIUS计费消息中携带哪些私有扩展属性的字段。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 软参APN\_BIT1和SET RDSACCTREQATTR命令的RULEBASENAME参数控制的功能存在冲突，不允许同时开启。
- 当前版本不支持此命令的HWRAI参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | CALLSTAID   | CONTENT   | IMSI    | MULTISESSIONID   | CHARGINGID   | PREPAIDID   | GGSNIP   | SGSNIP   | NASIDSW   | REQUESTAPN   | ACCTEXTSW   | ACCTLINKCNT   | EVENTTIME   | INPUTOUTPUTOCT   | INPUTOUTPUTPKT   | ACCTDELAYTIME   | SESSIONID   | RULEBASENAME   | GGSNVENDOR   | GGSNVERION   | TRIGGERTYPE   | SERVEDMDN   | HWRAI   | NASPORTIDSW   | NASPORTID   | WLANADDR   | NASIPADDR   |
|:-------|:------------|:----------|:--------|:-----------------|:-------------|:------------|:---------|:---------|:----------|:-------------|:------------|:--------------|:------------|:-----------------|:-----------------|:----------------|:------------|:---------------|:-------------|:-------------|:--------------|:------------|:--------|:--------------|:------------|:-----------|:------------|
| 初始值    | ENABLE      | MSISDN    | DISABLE | ENABLE           | DISABLE      | DISABLE     | DISABLE  | DISABLE  | DISABLE   | DISABLE      | ENABLE      | ENABLE        | ENABLE      | ENABLE           | ENABLE           | ENABLE          | ENABLE      | DISABLE        | DISABLE      | DISABLE      | DISABLE       | DISABLE     | DISABLE | DISABLE       | UNC         | DISABLE    | LOCALCONFIG |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                                         | 参数说明                                                                                                                                                                                                                                                                                                                                 |
|:---------------|:---------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME  | RADIUS Server Group名称                        | 可选必选说明：必选参数 参数含义：RADIUS服务器组名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：该参数使用ADD RDSSVRGRP命令配置生成。                                                                                                                                                                                                                                 |
| CALLSTAID      | 支持Calling-Station-Id                         | 可选必选说明：可选参数 参数含义：指定是否支持携带Calling-Station-Id信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                    |
| CONTENT        | 指定Calling-Station-Id的内容                      | 可选必选说明：条件可选参数 前提条件：该参数在“CALLSTAID”配置为“ENABLE”时为可选参数。 参数含义：指定Calling-Station-Id的内容。 数据来源：本端规划 取值范围：枚举类型。 MSISDN：填充内容是MSISDN。IMSI：填充内容是IMSI。 默认值：无 配置原则：无                                                                                                                                                                              |
| IMSI           | 支持携带IMSI属性                                   | 可选必选说明：可选参数 参数含义：指定是否支持携带IMSI信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                                  |
| MULTISESSIONID | 支持携带acct-multi-session-id属性                  | 可选必选说明：可选参数 参数含义：指定是否支持携带acct-multi-session-id信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                 |
| CHARGINGID     | 支持携带Charging ID属性                            | 可选必选说明：可选参数 参数含义：指定是否支持携带Charging ID信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                           |
| PREPAIDID      | 支持携带Prepaid-ind属性                            | 可选必选说明：可选参数 参数含义：指定是否支持携带Prepaid-ind信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                           |
| GGSNIP         | 支持携带GGSN-IP-address属性                        | 可选必选说明：可选参数 参数含义：指定是否支持携带GGSN-IP-address信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                       |
| SGSNIP         | 支持携带SGSN（S-GW）-IP-address属性                  | 可选必选说明：可选参数 参数含义：指定是否支持携带SGSN(SGW)-IP-address信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                  |
| NASIDSW        | 支持携带Nas-Identifier属性                         | 可选必选说明：可选参数 参数含义：指定是否支持携带nas-id-value信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不携带nas-id-value信元。APN：携带的nas-id-value信元为用户所在的APN名。SPECIFIC_VALUE：携带的nas-id-value信元为用户自定义的字符串。 默认值：无 配置原则：无                                                                                                                                                     |
| NASID          | Nas-Identifier属性值                            | 可选必选说明：条件必选参数 前提条件：该参数在“NASIDSW”配置为“SPECIFIC_VALUE”时为必选参数。 参数含义：当NASIDSW配置为SPECIFIC_VALUE时，指定nas-id-value信元携带的用户自定义的字符串。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，区分大小写。 默认值：无 配置原则：无                                                                                                                                                  |
| REQUESTAPN     | Requested-apn                                | 可选必选说明：可选参数 参数含义：指定是否支持计费请求消息中携带HW-Requested-APN属性。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                               |
| ACCTEXTSW      | 计费扩展属性开关                                     | 可选必选说明：可选参数 参数含义：指定是否支持携带计费扩展属性。即是否携带Acct-Delay-Time（41）、Acct-Input-Octets（42）、Acct-Output-Octets（43）、Acct-Authentic（45）、Acct-Session-Time（46）、Acct-Input-Packets（47）、Acct-Output-Packets（48）、Acct-Terminate-Cause（49）、Acct-Link-Count（51）、Event-Timestamp（55）属性。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无 |
| ACCTLINKCNT    | 支持携带属性Acct-Link-Count                        | 可选必选说明：条件可选参数 前提条件：该参数在“ACCTEXTSW”配置为“ENABLE”时为可选参数。 参数含义：指定是否支持携带信元Acct-Link-Count。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                              |
| EVENTTIME      | 支持携带属性Event-Time                             | 可选必选说明：条件可选参数 前提条件：该参数在“ACCTEXTSW”配置为“ENABLE”时为可选参数。 参数含义：指定是否支持携带信元event-time。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                   |
| INPUTOUTPUTOCT | 支持携带属性Acct-Input-Octets和Acct-Output-Octets   | 可选必选说明：条件可选参数 前提条件：该参数在“ACCTEXTSW”配置为“ENABLE”时为可选参数。 参数含义：指定是否支持携带信元Acct-Input-Octets和Acct-Output-Octets。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                         |
| INPUTOUTPUTPKT | 支持携带属性Acct-Input-Packets和Acct-Output-Packets | 可选必选说明：条件可选参数 前提条件：该参数在“ACCTEXTSW”配置为“ENABLE”时为可选参数。 参数含义：指定是否支持携带信元Acct-Input-Packets和Acct-Output-Packets。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                       |
| ACCTDELAYTIME  | 支持携带属性acct-delay-time                        | 可选必选说明：条件可选参数 前提条件：该参数在“ACCTEXTSW”配置为“ENABLE”时为可选参数。 参数含义：指定是否支持携带信元acct-delay-time。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                              |
| SESSIONID      | 支持携带属性Acct-Session-ID                        | 可选必选说明：可选参数 参数含义：指定是否支持携带信元Acct-Session-ID。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                       |
| RULEBASENAME   | 支持携带属性Charge-Rule-Base-Name                  | 可选必选说明：可选参数 参数含义：指定是否支持携带信元Charge-Rule-Base-Name。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                 |
| GGSNVENDOR     | 支持携带属性GGSN-Vendor                            | 可选必选说明：可选参数 参数含义：指定是否支持携带信元GGSN-Vendor。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                           |
| GGSNVERION     | 支持携带属性GGSN-Version                           | 可选必选说明：可选参数 参数含义：指定是否支持携带信元GGSN-Version。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                          |
| TRIGGERTYPE    | 支持携带属性trigger-type                           | 可选必选说明：可选参数 参数含义：指定是否支持携带信元trigger-type 。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                         |
| SERVEDMDN      | 支持携带属性Served-MDN                             | 可选必选说明：可选参数 参数含义：指定是否支持携带Served-MDN信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                            |
| HWRAI          | HW-RAI属性开关                                   | 可选必选说明：可选参数 参数含义：指定是否支持携带HW-RAI属性。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                                |
| NASPORTIDSW    | NAS-Port-Id属性开关                              | 可选必选说明：可选参数 参数含义：指定是否支持携带NAS-Port-Id属性。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                                           |
| NASPORTID      | NAS-Port-Id属性值                               | 可选必选说明：条件可选参数 前提条件：该参数在“NASPORTIDSW”配置为“ENABLE”时为可选参数。 参数含义：指定当NASPortIdSw字段设置为ENABLE时，NAS-Port-Id信元携带的填充值。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～16。 默认值：无 配置原则：输入单空格将删除该参数已有配置项。                                                                                                                                                           |
| WLANADDR       | UE-Local-IP-Address和UE-UDP-Port              | 可选必选说明：可选参数 参数含义：指定是否支持携带UE-Local-IP-Address和UE-UDP-Port属性。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不支持携带该信元。ENABLE：支持携带该信元。 默认值：无 配置原则：无                                                                                                                                                                                                       |
| NASIPADDR      | NAS IP Address                               | 可选必选说明：可选参数 参数含义：指定主/备计费服务器的NAS-IP-Address或NAS-IPv6-Address取值的获取方式。 抄送服务器的NAS-IP-Address或NAS-IPv6-Address取值由BIT304控制。 数据来源：全网规划 取值范围：枚举类型。 LOCALCONFIG：使用命令ADD RADIUSNASIP本地控制配置的NAS-IP-Address或NAS-IPv6-Address。当ADD RADIUSNASIP未配置时，使用GI本端接口IP。UPADDR：填写UPF设备的N4接口IPv4、IPv6地址。 默认值：无 配置原则：无                                        |

#### 使用实例

新增名为“radiusgroup”的RADIUS服务器组的RADIUS计费私有扩展属性，支持携带GGSN-IP-address和Prepaid-ind信元，根据RADIUS计费消息中携带的这些私有扩展属性字段进行相关的业务控制：

```
SET RDSACCTREQATTR:RDSSVRGRPNAME="radiusgroup",PREPAIDID=ENABLE,GGSNIP=ENABLE;
```