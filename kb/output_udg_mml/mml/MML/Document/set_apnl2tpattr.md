# 设置APN L2TP配置（SET APNL2TPATTR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于设置APN的L2TP相关信息，当用户需要修改APN下配置的L2TP信息时，可以使用该命令。

#### 注意事项

- 该命令执行后立即生效。
- 系统最多支持配置10000条ApnL2tpAttr。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | L2TPSWITCH   |   L2TPGROUPID | RDSLNSMODE   | ICRQ_CALLINGNO   | ICCN_AUTH   | IPCP_NEGO   | ICCN_PGROUPID   | ICCN_TXSPEED   | ICRQ_BEARER   | ICCN_LCPNEGO   | DOMAINNAMEACT             |   DOMAINNAMEPOS | SUPPORTIPV6   |
|:-------|:-------------|--------------:|:-------------|:-----------------|:------------|:------------|:----------------|:---------------|:--------------|:---------------|:--------------------------|----------------:|:--------------|
| 初始值    | DISABLE      |           nan | REDUNDANCY   | MSISDN           | DISABLE     | DISABLE     | ENABLE          | DISABLE        | ENABLE        | ENABLE         | ADD_DISABLE_STRIP_DISABLE |             nan | DISABLE       |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                       | 参数说明                                                                                                                                                                                                                                                                       |
|:---------------|:---------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称                      | 可选必选说明：必选参数 参数含义：指定APN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格以及特殊字符：“_”、“#”、“$”、“&”等，不区分大小写。 默认值：无 配置原则：执行该命令前，必须先使用ADD APN命令配置APN。                                                                                                                                   |
| L2TPSWITCH     | APN支持L2TP功能                | 可选必选说明：必选参数 参数含义：配置指定APN是否支持L2TP功能。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                               |
| L2TPGROUPID    | L2TP组号                     | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：指定该APN下用户使用的L2TP组。APN下的用户根据此配置使用对应的L2TP组信息建立L2TP隧道。 数据来源：本端规划 取值范围：整数类型，取值范围为1～1500。 默认值：无 配置原则：该参数必须是通过ADD L2TPGROUP命令添加的有效的L2TP组ID。                                                                           |
| RDSLNSMODE     | RADIUS服务器返回多LNS的工作模式       | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：指定RADIUS鉴权服务器返回多LNS时LNS的工作模式。 数据来源：本端规划 取值范围：枚举类型。 REDUNDANCY：表示采用主备工作模式。TUNNEL_PREFER：表示根据配置的LNS优先级决定是主备工作模式还是负荷分担工作模式，如果有多个优先级相同的LNS服务器，则多个LNS服务器之间是负荷分担模式；如果有两个优先级不同的LNS服务器，则认为两个LNS服务器之间是主备模式。 默认值：无 配置原则：无 |
| ICRQ_CALLINGNO | ICRQ携带Calling-number AVP值  | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制系统发往LNS服务器的ICRQ消息属性。 数据来源：本端规划 取值范围：枚举类型。 MSISDN：指定系统发送的ICRQ消息中Calling-number AVP中携带的是MSISDN。IMSI：指定系统发送的ICRQ消息中Calling-number AVP中携带的是IMSI。IMEI：指定系统发送的ICRQ消息中Calling-number AVP中携带的是IMEI。 默认值：无 配置原则：无      |
| ICCN_AUTH      | ICCN携带鉴权信元开关               | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制ICCN消息中是否携带鉴权相关信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：ICCN消息中是否携带鉴权相关信元，根据用户是否需要鉴权而定。ENABLE：当PPP鉴权开关为不鉴权时，ICCN消息中不携带鉴权相关信元。当PPP鉴权开关为鉴权时，且用户需要进行鉴权的情况下，ICCN消息中携带鉴权相关信元。 默认值：无 配置原则：无                                 |
| IPCP_NEGO      | 发起IPCP协商开关                 | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制系统是否主动发起IPCP协商。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：该参数只对非PAP/CHAP鉴权用户生效。                                                                                                                  |
| ICCN_PGROUPID  | ICCN携带PrivateGroupId AVP开关 | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制系统发出的ICCN报文中是否携带PrivateGroupId AVP。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                  |
| ICCN_TXSPEED   | ICCN携带TxConnectSpeed值      | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制ICCN报文中的TxConnectSpeed AVP信元的值。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：表示ICCN报文中的TxConnectSpeed AVP信元的值为0。ENABLE：表示ICCN报文中的TxConnectSpeed AVP信元的值为8640000。 默认值：无 配置原则：无                                                 |
| ICRQ_BEARER    | ICRQ携带Bearer Type AVP开关    | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制ICRQ报文中是否携带Bearer Type AVP信元。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                        |
| ICCN_LCPNEGO   | ICCN携带LCP CONFREQ信元开关      | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：控制系统在进行L2TP协商时，系统发送的ICCN报文中是否携带Initial Received LCP CONFREQ、Last Sent LCP CONFREQ和Last Received LCP CONFREQ三个可选信元，用于系统和不同的LNS对接。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                       |
| DOMAINNAMEACT  | 增加或剥离域名                    | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定APN下入网的L2TP用户去LNS鉴权时，ICCN\CHAP\PAP消息中的用户名是否支持增加或剥离域名功能。 数据来源：本端规划 取值范围：枚举类型。 ADD_DISABLE_STRIP_DISABLE：不支持增加和剥离域名功能。ADD_ENABLE_STRIP_DISABLE：仅支持增加域名功能。ADD_DISABLE_STRIP_ENABLE：仅支持剥离域名功能。 默认值：无 配置原则：无  |
| DOMAINNAMEPOS  | 域名位置                       | 可选必选说明：条件必选参数 前提条件：该参数在“DOMAINNAMEACT”配置为“ADD_ENABLE_STRIP_DISABLE”时为必选参数。 参数含义：该参数用于指定APN下入网的用户增加的域名为前缀域名还是后缀域名。 数据来源：本端规划 取值范围：枚举类型。 PREFIX：前缀域名。SUFFIX：后缀域名。 默认值：无 配置原则：无                                                                                               |
| SUPPORTIPV6    | l2tp支持ipv6功能开关             | 可选必选说明：条件可选参数 前提条件：该参数在“L2TPSWITCH”配置为“ENABLE”时为可选参数。 参数含义：配置指定APN是否支持L2TP激活IPV6用户功能。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                             |

#### 使用实例

假设用户需要APN “huawei.com”支持L2TP用户接入功能时，使用该命令配置：

```
SET APNL2TPATTR:APN="huawei.com",L2TPSWITCH=ENABLE;
```