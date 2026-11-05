# 增加OCS Counter映射(ADD OCSCOUNTERMAP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响UPCF与OCS相关的业务的正常使用，需联系华为技术支持确认后再执行。

该命令用于在UPCF配置数据库中增加一条配额名称与配额状态的映射记录。

OCS通过Sy接口向UPCF发送的SNR/SLA消息中，当使用两个Policy-Counter-Status-Report AVP分别携带一个配额的配额名称和配额状态时，可通过执行本命令降低UPCF上策略配置的复杂度及规则匹配时系统的开销。

配置了OCS Counter映射关系后，UPCF收到OCS通过Sy接口发送的SNR/SLA消息中，如果通过两个Policy-Counter-Status-Report AVP分别携带一个配额的配额名称和配额状态，则会将携带配额名称的Policy-Counter-Status-Report AVP中Policy-Counter-Identifier AVP的值映射为配额名称，将携带配额状态的Policy-Counter-Status-Report AVP中Policy-Counter-Status AVP的值映射为配额状态。

**说明** 

该命令暂不支持N7和N28接口业务。

## 注意事项

- 在“VRM\_SYSWITCH”软参为“2”或“3”或“4”且“VRM\_SAVESYORGSTATUS”软参为“1”时，本命令配置的映射关系才会生效。
- 系统最多配置32个“QUOTANAME”与“QUOTASTATUS”的映射关系。
- 对于同一用户的Sy接口会话，SNR和SLA消息总共携带的Policy-Counter-Status-Report AVP数量不能超过26对，否则，超过此数量的Policy-Counter-Status-Report AVP将会被丢弃。

  **说明** 

  当SNR消息携带的成对的Policy-Counter-Status-Report AVP缺失了一个时，UPCF会根据OCS Counter映射关系，补齐缺失的Policy-Counter-Status-Report AVP，SNR和SLA消息携带的Policy-Counter-Status-Report AVP总数不能超过26对。

## 参数说明

| 参数标识        | 参数名称   | 参数描述                                                                                                                                                                                |
|:------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUOTANAME   | 配额名称   | 可选必选说明：必选参数 参数含义：用于标识配额名称。配置为携带配额名称的Policy-Counter-Status-Report AVP中Policy-Counter-Identifier AVP的值。 取值范围：长度不超过32的字符串。 默认值：无。 配置原则：不能与已有的QUOTANAME或QUOTASTATUS或本次输入的QUOTASTATUS重复。 |
| QUOTASTATUS | 配额状态   | 可选必选说明：必选参数 参数含义：用于标识配额状态。配置为携带配额状态的Policy-Counter-Status-Report AVP中Policy-Counter-Status AVP的值。 取值范围：长度不超过32的字符串。 默认值：无。 配置原则：不能与已有的QUOTANAME或QUOTASTATUS或本次输入的QUOTANAME重复。       |

## 使用实例

新增一条OCS Counter映射关系：“QUOTANAME”为“PackName”，“QUOTASTATUS”为“PackUsage”。

```
ADD OCSCOUNTERMAP: QUOTANAME="PackName", QUOTASTATUS="PackUsage";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                          | 原因分析                                                                                                                        | 处理建议                                                                                                                                                 |
|------:|:-------------------------------|:----------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| 53199 | 表记录已经达到最大数限制。                  | 映射记录数已达到最大数32。                                                                                                              | 执行LST OCSCOUNTERMAP查询所有已存在映射记录，执行RMV OCSCOUNTERMAP删除不需要的映射记录，再执行本命令添加映射记录。                                                                           |
| 58125 | QUOTANAME或者QUOTASTATUS与已有记录重复。 | “QUOTANAME”与已有的“QUOTANAME”或者“QUOTASTATUS”重复。“QUOTASTATUS”与已有的“QUOTANAME”或者“QUOTASTATUS”重复。本次输入的“QUOTANAME”与“QUOTASTATUS”重复。 | 执行LST OCSCOUNTERMAP查询已经存在的映射记录，再执行本命令重新输入“QUOTANAME”和“QUOTASTATUS”，确保输入的“QUOTANAME”和“QUOTASTATUS”与系统中已存在的记录不重复。确保本次输入的“QUOTANAME”与“QUOTASTATUS”没有重复。 |