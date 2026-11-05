# 增加P-GW特性对接配置（ADD PGWCHARACT）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于增加需要匹配的对端P-GW的属性信息。MME将此配置作为与对端网元间信令交互时的参考条件。

#### 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为128。
- 该命令部分参数与相关特性License共同完成该特性的开启，请在设置参数前使用**DSP LICENSE**命令确认对应特性License是否得到授权，执行**LST LICENSESWITCH**命令确认特性开关状态为“ENABLE（打开）”，具体相关特性请参考参数的说明。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称                                | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:--------------|:------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RANGE         | 对端设备范围                              | 可选必选说明：必选参数 参数含义：该参数用于指定需要设置属性信息的对端P-GW范围。 数据来源：本端规划 取值范围：“ALL（所有P-GW）”“HOME（本网P-GW）”“FOREIGN（外网P-GW）”“SPECIFIC（指定IP的P-GW）” 默认值：无 配置原则： 系统中只能配置一条“ALL（所有P-GW）”的记录。当系统中已存在一条“ALL（所有P-GW）”的记录时，如果再增加一条“ALL（所有P-GW）”的记录，新记录会将旧记录覆盖。系统中只能配置一条“HOME（本网P-GW）”的记录。当系统中已存在一条“HOME（本网P-GW）”的记录时，如果在客户端再增加一条“HOME（本网P-GW）”的记录，新记录将添加失败。系统中只能配置一条“FOREIGN（外网P-GW）”的记录。当系统中已存在一条“FOREIGN（外网P-GW）”的记录时，如果在客户端再增加一条“FOREIGN（外网P-GW）”的记录，新记录将添加失败。系统中可以配置多条“SPECIFIC（指定IP的P-GW）”的记录，但是IP网段区间不能重叠。优先级关系：“SPECIFIC（指定IP的P-GW）” >“HOME（本网P-GW）” = “FOREIGN（外网P-GW）” >“ALL（所有P-GW）” 。                                               |
| IPT           | IP地址类型                              | 可选必选说明：条件必选参数 参数含义：该参数用于指定P-GW信令面IP地址类型。 前提条件：只有在“RANGE（对端设备范围）”配置为“SPECIFIC（指定IP的P-GW）”时，该参数有效。 数据来源：本端规划 取值范围： “IPV4（IPv4）”“IPV6（IPv6）” 默认值：“IPV4（IPv4）”                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| IPV4          | IPv4地址                              | 可选必选说明：条件必选参数 参数含义：该参数用于指定P-GW信令面IPv4地址。 前提条件：只有在“IPT（IP地址类型）”配置为“IPV4（IPv4）”时，才需要配置该类型的IP地址。 数据来源：本端规划 取值范围：0.0.0.0～255.255.255.255 默认值：无 配置原则： 有效的IPv4地址不能为0.0.0.0、255.255.255.255和环回地址（127.x.y.z）。有效的IPv4地址必须是A、B或者C类地址。                                                                                                                                                                                                                                                                                                                                                                                      |
| IPV4MASK      | IPv4地址掩码                            | 可选必选说明：条件必选参数 参数含义：该参数用于指定对端P-GW的信令面IPv4地址的掩码。 前提条件：只有在“IPT（IP地址类型）”配置为“IPV4（IPv4）”时，才需要配置该类型的IP地址。 数据来源：本端规划 取值范围：0.0.0.1～255.255.255.255 默认值：无 配置原则：输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。                                                                                                                                                                                                                                                                                                                                                       |
| IPV6          | IPv6地址                              | 可选必选说明：条件必选参数 参数含义：该参数用于指定P-GW信令面IPv6地址。 前提条件：只有在“IPT（IP地址类型）”配置为“IPV6（IPv6）”时，才需要配置该参数。 数据来源：本端规划 取值范围：:: ～ FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无 配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8）。                                                                                                                                                                                                                                                                                                                                        |
| IPV6MASK      | IPv6地址前缀长度                          | 可选必选说明：条件必选参数 参数含义：该参数用于指定子网前缀的长度。 前提条件：只有在“IPT（IP地址类型）”配置为“IPV6（IPv6）”时，才需要配置该参数。 数据来源：本端规划 取值范围：1～128 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MMEID         | P-GW支持MME ID                        | 可选必选说明：可选参数 参数含义：该参数用于设置P-GW是否支持MME ID信元。 数据来源：本端规划 取值范围： “YES（支持）”“NO（不支持）” 默认值：“NO（不支持）” 配置原则： “S-GW/P-GW故障下的业务恢复”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-201203，License部件编码：LKV2SRGF01）参数设置为“YES（支持）”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息携带“MME ID”信元。参数设置为“NO（不支持）”，发送给对应S-GW的Create Session Request/ModifyBearer Request消息不携带“MME ID”信元。                                                                                                                                                                                                                                                 |
| RATTYPELTEM   | 是否向P-GW转发LTE-M类型的RAT TYPE           | 可选必选说明：可选参数 参数含义：该参数用于设置UNC是否通知S-GW向P-GW上报LTE-M类型的RAT TYPE。 数据来源：本端规划 取值范围： “NO（不支持）” “YES（支持）” 默认值：“NO（不支持）” 配置原则： 针对LTE-M类型的用户，UNC向SGW发送Create Session Request消息或者Modify Bearer Request消息时，如果参数设置为“YES”，消息中的Indication-flag的“LTE-M RAT type reporting to PGW”会设置为1；否则消息中Indication-flag的“LTE-M RAT type reporting to PGW”会设置为0。当ADD GTPCV2CMPT命令支持LTE-M类型的RAT TYPE且SGW感知到RAT TYPE为LTE-M，该配置命令才生效。 当软参BYTE_EX_B41 BIT2设置为0时，ADD GTPCV2CMPT命令支持LTE-M类型的RAT TYPE且SGW感知到RAT TYPE为LTE-M，或当软参BYTE_EX_B41 BIT2设置为1时，该配置命令才生效。  说明： Indication-flag信元中的“LTE-M RAT type reporting to PGW”用于指示SGW向PGW传递LTE-M类型的RAT TYPE。 |
| PCSCFRESTOIND | P-GW支持P-CSCF Restoration Indication | 可选必选说明：可选参数 参数含义：该参数用于指定P-GW是否支持indication Flags信元内的“P-CSCF Restoration Indication”标志位。 数据来源：全网规划 取值范围： "NO（不支持）" "YES（支持）" 默认值："NO（不支持）" 配置原则： “ 基于HSS的P-CSCF故障恢复”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-201205，License部件编码：LKV2FRPH02） 如果P-GW支持“P-CSCF Restoration Indication”标志位，才设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。功能同时受ADD PCSCFRESTOPLCY配置的“PCO-based optional extension功能”参数、ADD SGWCHARACT的“S-GW支持P-CSCF Restoration Indication”参数控制，只有全部开启功能才生效。                                                                                                                                                         |

#### 使用实例

当“S-GW/P-GW故障下的业务恢复”特性开启时，如果UE选择的S-GW和P-GW非合一并且P-GW不支持MME ID信元，则添加一条指定IP的P-GW不支持MME ID信元的配置：

```
ADD PGWCHARACT: RANGE=SPECIFIC, IPT=IPV4, IPV4="10.141.196.197", IPV4MASK="255.255.255.0",MMEID=NO;
```