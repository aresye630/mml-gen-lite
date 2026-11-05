# 添加FQDN信息(ADD FQDNINFO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于增加本地静态配置域名和IP的对应关系。

使用场景：

- UPCF收到AMF/SMF/NEF网元发送的Create请求消息时，支持将该消息中notificationUri中的host格式由FQDN转换成IP，使得UPCF可以获取AMF/SMF/NEF网元的IP地址。
- UPCF收到NRF网元发送的Nnrf\_NFManagement\_NFRegister、Nnrf\_NFManagement\_NFUpdate、Nnrf\_NFManagement\_NFStatusSubscribe、Nnrf\_NFManagement\_Get响应消息时，支持将消息中location头域URI中的host格式由FQDN转换成IP。
- UPCF主动向NRF网元发送的Nnrf\_NFManagement\_NFStatusSubscribe请求消息时，支持根据**SET SBIURICFG**配置，将消息中携带的nfStatusNotificationUri信元格式由IP转换成FQDN。
- UPCF主动向AMF/SMF网元发送Npcf\_SMPolicyControl\_UpdateNotify、Npcf\_AMPolicyControl\_UpdateNotify的请求消息时，支持根据**SET SBIURICFG**配置，将消息中携带的resourceUri信元格式由IP转换成FQDN。
- UPCF向AMF网元发送Npcf\_AMPolicyControl\_Update的响应消息时，支持根据**SET SBIURICFG**配置，将消息中携带的resourceUri信元格式由IP转换成FQDN。
- UPCF向AMF/SMF网元发送Npcf\_AMPolicyControl\_Create、Npcf\_SMPolicyControl\_Create的Create类型响应消息时，支持根据**SET SBIURICFG**配置，将消息中携带的location头域URI中的host格式由IP转换成FQDN。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                              |
|:------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INDEX       | 索引     | 可选必选说明：必选参数 参数含义：用于指定的本地静态配置域名和IP对应关系的唯一标识。 取值范围：1～1024 默认值：无。 配置原则：无。                                                                                                                            |
| FQDN        | FQDN   | 可选必选说明：必选参数 参数含义：用于标识本地静态配置的域名。 取值范围：长度不超过128位的字符串 默认值：无。 配置原则：无。  说明： 该参数的配置和应用大小写敏感。同1个FQDN仅支持配置1个IP地址。FQDN对应的IP地址被删除后，业务侧可能后续不会再向此IP对应的客户端链路发送消息，HLB已经建立的链路通过老化机制自动释放。即链路超过某段时间连续没有消息时，链路自动关闭。 |
| IPVER       | IP版本   | 可选必选说明：必选参数 参数含义：用于指定IP类型是IPV4还是IPV6。 取值范围： IPV4(IPV4)IPV6(IPV6) 默认值：无。 配置原则：无。                                                                                                                   |
| IP          | IPV4地址 | 可选必选说明：可选参数 参数含义：当“IP版本”参数选定为“IPV4”时，该参数为必选参数。 用于表述本地静态配置域名对应的IPV4内容。 取值范围：除“255.255.255.255”、“0.0.0.0”及“127.0.0.1”以外的IPV4地址。 默认值：无。 配置原则：无。                                                      |
| IPV6        | IPV6地址 | 可选必选说明：可选参数 参数含义：当“IP版本”参数选定为“IPV6”时，该参数为必选参数。 用于表述本地静态配置域名对应的IPV6内容。 取值范围：除“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、“0:0:0:0:0:0:0:0”及“0:0:0:0:0:0:0:1”以外的IPV6地址。 默认值：无。 配置原则：无。                |
| DESCRIPTION | 描述     | 可选必选说明：可选参数 参数含义：对本命令中的全部“FQDN”参数有效，用于域名对象的描述。 取值范围：长度不超过32位的字符串。 默认值：无。 配置原则：无。                                                                                                                  |

## 使用实例

增加本地静态配置域名和IP对应关系，“索引”为“1”，“FQDN”为“huawei.com”，“IP版本”为“IPV4”，“IPV4”为“192.168.0.3”，“DESCRIPTION”为“xxx”。

```
ADD FQDNINFO: INDEX=1, FQDN="huawei.com", IPVER=IPV4, IP="192.168.0.3", DESCRIPTION="xxx";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释       | 原因分析                            | 处理建议                                                                       |
|------:|:------------|:--------------------------------|:---------------------------------------------------------------------------|
|   503 | 配置数据已存在     | 当前配置的“索引”参数值与已经存在相同“索引”值重复。     | 先执行LST FQDNINFO查询已有的配置，获取已有配置的“索引”信息；重新执行ADD FQDNINFO添加与查询结果不一致的“索引”值。     |
| 58003 | 相同的FQDN已经存在 | 当前配置的“FQDN”参数值与已经存在相同“FQDN”值重复。 | 先执行LST FQDNINFO查询已有的配置，获取已有配置的“FQDN”信息；重新执行ADD FQDNINFO添加与查询结果不一致的“FQDN”值。 |