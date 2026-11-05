# 设置BSF配置(SET BSFCFG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响语音业务处理，需联系华为技术支持确认后再执行。

该命令用于设置BSF开关状态以及指定支持BSF时需要上报的属性参数。

该命令的使用场景：

PES在处理完N7会话上线流程后，系统需要根据设置的BSF开关状态判断是否要支持BSF功能。

如果BSF开关打开，根据设置的BSF属性参数从N7会话携带的消息和PCF的网元信息中获取到对应的参数，将获取到的每个参数通过HLB服务发送给BSF进行注册和查询。

## 注意事项

该命令存在系统初始记录，参数的初始设置值如下：

- “ID”为“1”
- “Switch”为“不支持”
- “Supi”为“不支持”
- “Gpsi”为“不支持”
- “Ipv4Addr”为“不支持”
- “Ipv6Prefix”为“不支持”
- “IpDomain”为“不支持”
- “MacAddr48”为“不支持”
- “Fqdn”为“不支持”
- “IpEndPoint”为“不支持”
- “PcfDiamHost”为“不支持”
- “PcfDiamRealm”为“不支持”
- “FailedRelease”为“不支持”

## 参数说明

| 参数标识          | 参数名称          | 参数说明                                                                                                                                                                                                                                  |
|:--------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID            | ID            | 可选必选说明：必选参数 参数含义：用于设置BSF配置信息的唯一标识。 取值范围：1。 默认值：无。 配置原则：无。                                                                                                                                                                             |
| SWITCH        | Switch        | 可选必选说明：必选参数 参数含义：用于指定是否支持BSF功能。 取值范围： Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                                                                        |
| SUPI          | Supi          | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持5G终端用户标识。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                      |
| GPSI          | Gpsi          | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持终端的移动台国际ISDN号码。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                |
| IPV4ADDR      | Ipv4Addr      | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持终端Ipv4地址。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                      |
| IPV6PREFIX    | Ipv6Prefix    | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持终端IPv6地址前缀。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                    |
| IPDOMAIN      | IpDomain      | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持终端IPv4地址域标识符。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                  |
| MACADDR48     | MacAddr48     | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持终端Mac地址。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。                                                                                                       |
| FQDN          | Fqdn          | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持PCF全量域名。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：UPCF支持N5接口时，参数“Fqdn”和“IpEndPoint”至少有一个需要配置为“Support(支持)”。                                                |
| IPENDPOINT    | IpEndPoint    | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持PCF的IP端口。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：UPCF支持N5接口时，参数“Fqdn”和“IpEndPoint”至少有一个需要配置为“Support(支持)”。                                               |
| PCFDIAMHOST   | PcfDiamHost   | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持由ADD PCRF命令配置的“本地主机名”。 取值范围：Support(支持) Unsupport(不支持) 默认值：无。 配置原则：UPCF支持Rx接口时，参数“PcfDiamHost”和“PcfDiamRealm”需要配置为“Support(支持)”。                             |
| PCFDIAMREALM  | PcfDiamRealm  | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示发送到BSF的属性是否支持由ADD PCRF命令配置的“本地域名”。 取值范围：Support(支持)Unsupport(不支持) 默认值：无。 配置原则：UPCF支持Rx接口时，参数“PcfDiamHost”和“PcfDiamRealm”需要配置为“Support(支持)”。                               |
| FAILEDRELEASE | FailedRelease | 可选必选说明：可选参数 参数含义：当且仅当选择参数“Switch”选择“Support(支持)”时，此参数有效。用于表示UPCF发送到BSF的会话绑定失败场景下是否支持释放N7会话能力。 取值范围： Support(支持)Unsupport(不支持) 默认值：无。 配置原则：无。  说明： 只有在“FAILEDRELEASE”取值为“Support(支持)”，且N7会话携带“VoLTE-APN”或者“Emergency-APN”的场景下才会释放N7会话。 |

## 使用实例

设置BSF配置信息。

- “ID”为“1”
- “Switch”为“支持”
- “Supi”为“支持”
- “Ipv4Addr”为“支持”
- “Fqdn”为“支持”

```
SET BSFCFG: ID=1, SWITCH=Support, SUPI=Support, IPV4ADDR=Support, FQDN=Support;
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。

命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                                             | 原因分析                                                                                                         | 处理建议                                                                                            |
|------:|:--------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
| 57889 | Ipv4Addr、Ipv6Prefix和MacAddr48至少需要选择一个。            | 配置“属性”参数时均没有选择“Ipv4Addr(Ipv4Addr)”、“Ipv6Prefix(Ipv6Prefix)”和“MacAddr48(MacAddr48)”。                          | 以下参数值至少选择一个： Ipv4Addr(Ipv4Addr)Ipv6Prefix(Ipv6Prefix)MacAddr48(MacAddr48)                       |
| 57890 | Fqdn、IpEndPoint、PcfDiamHost、PcfDiamRealm至少需要选择一个。 | 配置“属性”参数时均没有选择“Fqdn(Fqdn)”、“IpEndPoint(IpEndPoint)”、“PcfDiamHost(PcfDiamHost)”和“PcfDiamRealm(PcfDiamRealm)”。 | 以下参数值至少选择一个： Fqdn(Fqdn)IpEndPoint(IpEndPoint)PcfDiamHost(PcfDiamHost)PcfDiamRealm(PcfDiamRealm) |