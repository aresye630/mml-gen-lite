# 修改Home Zone业务(MOD HZ)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HLR中给用户签约或去签约Home Zone业务（Home Zone业务是指一个IMSI签约多个MSISDN的业务，多个MSISDN包括一个主MSISDN号码，多个辅MSISDN号码）。

## 注意事项

- “IMSI”和“MSISDN”两个参数是可选参数，必须有且只能有一个参数出现。
- 当“是否提供Home Zone业务”为“TRUE”时，“是否提供辅MSISDN号码转移业务”为可选参数；当“是否提供Home Zone业务”为“FALSE”时，“是否提供辅MSISDN号码转移业务”不必出现。
- 当“是否提供辅MSISDN号码转移业务”为“TRUE”时，参数“辅MSISDN号码的转移状态”和“辅MSISDN号码的转移号码”至少提供一个；当“是否提供辅MSISDN号码转移业务”为“FALSE”时，参数“辅MSISDN号码的转移状态”和“辅MSISDN号码的转移号码”不必出现。
- 当“是否提供Home Zone业务”为“TRUE”且携带“辅MSISDN号码”时，才能为“IMSI”或“MSISDN”添加一个辅MSISDN号码。一个MSISDN号码最多可以增加8个辅MSISDN号码。
- 当“是否提供Home Zone业务”为“FALSE”且不携带“辅MSISDN号码”参数时，将删除“IMSI”或“MSISDN”对应的所有辅MSISDN号码；如果“是否提供Home Zone业务”为“FALSE”，且携带“辅MSISDN号码”参数时，将删除“IMSI”或“MSISDN号码”对应的辅MSISDN号码；所有的辅MSISDN号码被删除后，主用户的Home Zone业务将被删除。
- Home Zone业务还与其他许多业务存在冲突，不能同时签约。这些业务包括：COMISDN、MIMSI、多SIM、多SIM增强、一卡多号多Profile、FM、ALS、M2M COMISDN和M2M ISDN-Less。
- 在Global-Local组网场景下，不支持使用本命令为用户签约或去签约Home Zone业务，否则系统会返回错误。
- 在混合组网下，如存在异常场景下进行跨SP数据迁移时，需要通过设置“USERDATAMIGEXCEPENHANCESW（用户数据迁移容错能力增强开关）”软参支持数据的兼容处理，避免因为UDB和PaasDB数据模型不一致而处理失败。
  - 插件包schemamap.xml文件中配置RDN冲突节点（rdnconflictexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点存在冲突记录时，若该软参为“1”，根据timestampfield配置字段取最新的一条数据，无timestampfield配置，随机取一条数据；若软参为“0”，则从5G接入查询4G用户和迁移失败。
  - 插件包schemamap.xml文件中配置无父节点的节点（noparentnodeexcepproc），即从5G接入查询4G用户和用户数据迁移过程中该节点无父节点记录时，若软参为“1”，忽略该节点数据不处理；若软参为“0”，则从5G接入查询4G用户和迁移失败。

## 参数说明

| 参数标识        | 参数名称              | 参数说明                                                                                                                                  |
|:------------|:------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI              | 用于标识待签约或去签约Home Zone业务用户的IMSI号码。 取值范围：6～15位的十进制数字组成的字符串。 默认值：无。                                                                       |
| ISDN        | MSISDN            | 用于标识待签约或去签约Home Zone业务用户的MSISDN号码。 取值范围：1～15位的十进制数字组成的字符串。 默认值：无。                                                                     |
| PROV        | 是否提供Home Zone业务   | 用于标识是否给用户提供Home Zone业务。 取值范围： TRUE：提供Home Zone业务。FALSE：不提供Home Zone业务。 默认值：FALSE。                                                     |
| AMSISDN     | 辅MSISDN号码         | 用于标识待签约或去签约用户的辅MSISDN号码。 取值范围：1～15位的十进制数字组成的字符串。 默认值：无。                                                                               |
| PROVFWD     | 是否提供辅MSISDN号码转移业务 | 仅当“是否提供Home Zone业务”取值为“TRUE”时该参数有效。用于标识是否给Home Zone业务用户提供辅MSISDN号码转移业务。 取值范围： TRUE：提供辅MSISDN号码转移业务。FALSE：不提供辅MSISDN号码转移业务。 默认值：FALSE。 |
| FWDNOSTATUS | 辅MSISDN号码的转移状态    | 仅当“辅MSISDN号码的转移状态”取值为“TRUE”时该参数有效。用于标识辅MSISDN号码的转移状态。 取值范围： ACTIVE：激活辅MSISDN号码转移业务。DEACTIVE：去激活辅MSISDN号码转移业务。 默认值：DEACTIVE。           |
| FWDNO       | 辅MSISDN号码的转移号码    | 仅当“辅MSISDN号码的转移状态”取值为“TRUE”时该参数有效。用于标识辅MSISDN号码的转移号码。 取值范围：1～15位的十进制数字组成的字符串。 默认值：无。                                                  |

## 使用实例

1. 在HLR上修改“IMSI”为“460000009123456”的用户的Home Zone信息：

   ```
   MOD HZ: IMSI="460000009123456", PROV=TRUE, AMSISDN="86131075003001", PROVFWD=TRUE, FWDNOSTATUS=ACTIVE, FWDNO="86131075003011";
   ```
2. 在HLR上为“IMSI”为“460000009123456”的用户去签约Home Zone业务：

   ```
   MOD HZ: IMSI="460000009123456",PROV=FALSE;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释    | 原因分析                                   | 处理建议                                                                         |
|:--------|:---------|:---------------------------------------|:-----------------------------------------------------------------------------|
| ERR1010 | 参数冲突     | “IMSI”、“MSISDN”两个参数同时被输入。              | “IMSI”、“MSISDN”两个参数是可选参数，必须有且只能有一个参数出现。                                      |
| ERR1009 | 参数缺失     | “辅MSISDN号码”或“是否提供辅MSISDN号码转移业务”参数没有输入。 | 重新输入参数，当“是否提供Home Zone业务”为“TRUE”时，保证“辅MSISDN号码”或“是否提供辅MSISDN号码转移业务”参数至少存在一个。 |
| ERR3111 | 系统不支持该特性 | 在Global-Local组网场景下，不支持该特性。             | 在Global-Local组网场景下，请勿使用该命令。                                                  |