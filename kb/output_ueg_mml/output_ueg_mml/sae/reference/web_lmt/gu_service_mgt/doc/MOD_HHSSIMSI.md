# 一键式改卡(MOD HHSSIMSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HSS的业务数据库中修改已存在用户的“IMPI”、“IMPI2”、“IMPU”以及“IMPI”和“IMPI2”关联的鉴权信息和IMSI信息。

## 注意事项

- 参数“IMPI”、“IMPU”、“IMPI2”、“IMPU2”中包含的信息必须属于同一个用户。
- “IMPU”和“NEWIMPU”必须同时输入或同时不输入，“IMPU2”和“NEWIMPU2”必须同时输入或同时不输入。
- 下面的每组参数取值不能相同:
  - “IMPI”和“IMPI2”
  - “IMPU”和“IMPU2”
  - “NEWIMPI”和“NEWIMPI2”
  - “NEWIMPU”和“NEWIMPU2”
- 对于VoLTE Multi-SIM用户，执行**MOD HHSSIMSI**命令对用户主卡进行补卡时，修改主卡的IMPI后需要重新执行**MOD HMSIM**命令设置主卡标记。
- 对于2G/3G/4G和IMS融合用户，改卡时必须在2G/3G/4G（执行**MOD IMSI**命令改卡）和IMS域（执行本命令改卡）同时修改。
- 在混合组网下，如存在异常场景下进行跨SP数据迁移时，需要通过设置“USERDATAMIGEXCEPENHANCESW（用户数据迁移容错能力增强开关）”软参支持数据的兼容处理，避免因为UDB和PaasDB数据模型不一致而处理失败。
  - 插件包schemamap.xml文件中配置RDN冲突节点（rdnconflictexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点存在冲突记录时，若该软参为“1”，根据timestampfield配置字段取最新的一条数据，无timestampfield配置，随机取一条数据；若软参为“0”，则从5G接入查询4G用户和迁移失败。
  - 插件包schemamap.xml文件中配置无父节点的节点（noparentnodeexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点无父节点记录时，若软参为“1”，忽略该节点数据不处理；若软参为“0”，则从5G接入查询4G用户和迁移失败。

## 参数说明

| 参数标识             | 参数名称         | 参数说明                                                                                                                                                                                                                                                         |
|:-----------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMPI             | IMPI         | 用于标识需要修改的旧的IMPI。该参数的配置原则是：输入的IMPI值符合NAI格式，字母区分大小写。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                                                    |
| IMPU             | IMPU         | 用于标识需要修改的旧的IMPU。该参数的配置原则是：输入的IMPU值符合SIP URI或TEL URI格式，字母区分大小写。IMPU类型必须是非通配的。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。 说明：一个通配IMPU可以代表一组IMPU，一个非通配IMPU只能代表一个IMPU。如果“IMPU”没有关联“IMPI”，“IMPU”的共享属性必须为“TRUE”时才能被修改。可以通过SET HIMPUSHARE设置“IMPU”的共享属性。 |
| NEWIMPI          | 新的IMPI       | 用于标识一个新的IMPI。该参数的配置原则是：输入的IMPI值符合NAI格式，字母区分大小写。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                                                       |
| NEWIMPIAUTHTYPE  | 新的IMPI的鉴权类型  | 用于标识一个新的IMPI的鉴权类型。 取值范围：EAA(Early AKA)：表示鉴权类型为Early AKA鉴权。TAA(Trusted Access)：表示鉴权类型为Trusted Access鉴权。 默认值：无。                                                                                                                                                |
| IMSI             | IMSI         | 仅当本命令中的“新的IMPI的鉴权类型”参数为“EAA”时该参数有效。用于标识NEWIMPI签约EAA鉴权时关联的IMSI。采用E.212格式。例如：460001234567890。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                    |
| ISDN             | MSISDN       | 仅当本命令中的“新的IMPI的鉴权类型”参数为“EAA”时该参数有效。用于标识NEWIMPI签约EAA鉴权时关联的MSISDN。采用E.164格式。例如：861381234567890。 取值范围：长度不超过15位的十进制数字。 默认值：无。                                                                                                                                    |
| NEWIMPU          | 新的IMPU       | 用于标识一个新的IMPU。该参数的配置原则是：输入的新的IMPU值符合SIP URI或TEL URI格式，字母区分大小写。新的IMPU类型必须是非通配的。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                         |
| IMPI2            | IMPI2        | 用于标识需要修改的旧的IMPI2。该参数的配制原则是：输入的IMPI2值符合NAI格式，字母区分大小写。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                                                  |
| IMPU2            | IMPU2        | 用于标识需要修改的旧的IMPU2。该参数的配置原则是：输入的IMPU2值符合SIP URI或TEL URI格式，字母区分大小写。IMPU2类型必须是非通配的。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。 说明：如果“IMPU2”没有关联“IMPI2”，“IMPU2”的共享属性必须为“TRUE”时才能被修改。可以通过SET HIMPUSHARE设置“IMPU2”的共享属性。                                 |
| NEWIMPI2         | 新的IMPI2      | 用于标识一个新的IMPI2。该参数的配制原则是：输入的IMPI2值符合NAI格式，字母区分大小写。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                                                     |
| NEWIMPI2AUTHTYPE | 新的IMPI2的鉴权类型 | 用于标识新的IMPI2的鉴权类型。 取值范围：EAA(Early AKA)：表示鉴权类型为Early AKA鉴权。TAA(Trusted Access)：表示鉴权类型为Trusted Access鉴权。 默认值：无。                                                                                                                                                 |
| IMSI2            | IMSI2        | 仅当本命令中的“新的IMPI2的鉴权类型”参数为“EAA”时该参数有效。用于标识NEWIMPI2签约EAA鉴权时关联的IMSI2。采用E.212格式。例如：460001234567890。 取值范围：6～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                 |
| ISDN2            | MSISDN2      | 仅当本命令中的“新的IMPI2的鉴权类型”参数为“EAA”时该参数有效。用于标识NEWIMPI2签约EAA鉴权时关联的MSISDN2。采用E.164格式。例如：861381234567890。 取值范围：长度不超过15位的十进制数字。 默认值：无。                                                                                                                                 |
| NEWIMPU2         | 新的IMPU2      | 用于标识一个新的IMPU2。该参数的配置原则是：输入的新的IMPU2值符合SIP URI或TEL URI格式，字母区分大小写。新的IMPU2类型必须是非通配的。 取值范围：长度不超过127的由字母、数字或“.”、“_”、“—”、空格等特殊字符组成的字符串。 默认值：无。                                                                                                                      |

## 使用实例

操作人员进行一键式改卡，参数取值如下：

- IMPI：impiinfo
- IMPU：sip:impuinfo@huawei.com
- EWIMPI：new\_impiinfo
- NNEWIMPIAUTHTYPE：EAA
- IMSI：460001234567890
- ISDN：8613977777777
- NEWIMPU：sip:new\_impuinfo@huawei.com
- IMPI2：impi2info
- IMPU2：sip:impu2info@huawei.com
- NEWIMPI2：new\_impi2info
- NEWIMPI2AUTHTYPE：TAA
- NEWIMPU2：sip:new\_impu2info@huawei.com

执行如下命令：

```
MOD HHSSIMSI: IMPI="impiinfo", IMPU="sip:impuinfo@huawei.com", NEWIMPI="new_impiinfo", NEWIMPIAUTHTYPE=EAA, IMSI="460001234567890", ISDN="8613977777777", NEWIMPU="sip:new_impuinfo@huawei.com", IMPI2="impi2info", IMPU2="sip:impu2info@huawei.com", NEWIMPI2="new_impi2info", NEWIMPI2AUTHTYPE=TAA, NEWIMPU2="sip:new_impu2info@huawei.com";
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码       | 错误码解释                    | 原因分析                                                                                                                                                                                                                                  | 处理建议                                                                                                                                                                                  |
|:----------|:-------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004   | 无效的参数值                   | 原因为下列情况中的一种：参数“IMSI”或“IMSI2”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”或“MSISDN2”的取值不是1～15位十进制数字组成的字符串。                                                                                                                                          | 根据实际情况，重新输入“IMSI”、“IMSI2”、“MSISDN”或“MSISDN2”的取值，确保其取值符合要求。                                                                                                                            |
| ERR1009   | 参数丢失                     | 原因为下列情况中的一种：“IMPU”和“NEWIMPU”只输入了其中一个参数。“IMPU2”和“NEWIMPU2”只输入了其中一个参数。                                                                                                                                                                  | 根据实际情况，重新输入参数，确保满足以下两点：“IMPU”和“NEWIMPU”必须同时输入或同时不输入。“IMPU2”和“NEWIMPU2”必须同时输入或同时不输入。                                                                                                   |
| ERR1010   | 参数冲突                     | 原因为下列情况中的一种：“IMPI”和“IMPI2”取值相同。“IMPU”和“IMPU2”取值相同。“NEWIMPI”和“NEWIMPI2”取值相同。“NEWIMPU”和“NEWIMPU2”取值相同。                                                                                                                                  | 根据实际情况，重新输入参数，确保满足以下四点：“IMPI”和“IMPI2”取值不能相同。“IMPU”和“IMPU2”取值不能相同。“NEWIMPI”和“NEWIMPI2”取值不能相同。“NEWIMPU”和“NEWIMPU2”取值不能相同。                                                               |
| ERR3001   | 用户未定义                    | 用户的“MSISDN”输入错误，实际输入的参数“MSISDN”对应的用户未开户。                                                                                                                                                                                              | 核实用户的“MSISDN”，如果确定输入无误，证明实际输入的参数“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                                                                                                  |
| 900003509 | SUB没有绑定IMSI              | SET HSYSTEMPARA命令中的软参“EAA_IMPI_SHARE_IMSI_SUPPORT”取值为“TRUE”的场景下，本命令输入的“新的IMPI的鉴权类型”或“新的IMPI2的鉴权类型”为“EAA”时，同一“SUBID”下的IMPI都没有关联IMSI。                                                                                                   | 重新执行命令，通过“IMSI”或“IMSI2”参数为IMPI关联IMSI。                                                                                                                                                 |
| 900003510 | SUB绑定了多个IMSI             | SET HSYSTEMPARA命令中的软参“EAA_IMPI_SHARE_IMSI_SUPPORT”取值为“TRUE”的场景下，本命令输入的“IMPI的鉴权类型”或“新的IMPI2的鉴权类型”为“EAA”时，同一“SUBID”下存在多个关联了IMSI的IMPI。                                                                                                   | 先通过RMV HASSOC命令删除SUBID下部分IMSI，保证SUBID下只有一个IMPI关联了IMSI。                                                                                                                                |
| 900003511 | SUB已经绑定IMSI              | SET HSYSTEMPARA命令中的软参“EAA_IMPI_SHARE_IMSI_SUPPORT”取值为“TRUE”的场景下，本命令输入的“IMPI的鉴权类型”为“EAA”且输入了“IMSI”或“新的IMPI2的鉴权类型”为“EAA”且输入了“IMSI2”时，同一“SUBID”下存在关联了IMSI的IMPI。                                                                          | 重新执行命令，“IMSI”或“IMSI2”参数不用输入。                                                                                                                                                          |
| 900003512 | IMPI绑定的IMSI被共用，IMPI不能被删除 | 可能原因为当SET HSYSTEMPARA命令中的软参“EAA_IMPI_SHARE_IMSI_SUPPORT”取值为“TRUE”且出现如下场景之一：当“IMPI”是EAA鉴权时，“新的IMPI的鉴权类型”选择了“TAA”。当“IMPI”不是EAA鉴权时，“新的IMPI的鉴权类型”选择了“EAA”。当“IMPI2”是EAA鉴权时，“新的IMPI2的鉴权类型”选择了“TAA”。当“IMPI2”不是EAA鉴权时，“新的IMPI2的鉴权类型”选择了“EAA”。 | 根据实际情况，重新输入参数，确保满足以下四点：当“IMPI”是EAA鉴权时，“新的IMPI的鉴权类型”参数取值“EAA”。当“IMPI”不是EAA鉴权时，“新的IMPI的鉴权类型”参数取值“TAA”。当“IMPI2”是EAA鉴权时，“新的IMPI2的鉴权类型”参数取值“EAA”。当“IMPI2”不是EAA鉴权时，“新的IMPI2的鉴权类型”参数取值“TAA”。 |