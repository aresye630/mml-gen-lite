# 修改兼容性参数（MOD COMPATSWITCH）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会导致系统异常，影响业务处理，需联系华为技术支持确认后再执行。

修改兼容性软参的值。

当产品在完成版本升级操作后，在特定场景下出现升级前版本可以正常使用的功能在升级后无法正常使用的问题时，可通过此命令进行特定场景的修改。

## 注意事项

- 该命令用于在配置软参数据时，只需要对软参作适当修改以得到所需要的配置数据，而不需要添加或删除软参的操作。
- 操作员应使用默认值。如果操作员确实需要修改软件参数，请联系华为公司技术服务工程师处理，禁止随意修改。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                           |
|:--------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| SWNAME  | 参数名    | 可选必选说明：必选参数 参数含义：标识一条软参数据记录的关键字段之一（其取值在枚举值内取得），用于指定需要对哪一类软参数据记录的参数进行修改。 取值说明：详细信息请参考产品手册的“UPCF软件参数 > PES兼容性软参”。 默认值：无。 配置原则：无。                 |
| SWVALUE | 参数值    | 可选必选说明：必选参数 参数含义：标识一条软参数据记录的关键字段之一，此处取值应在取值范围内取值。其中，类型的编号规则是从上到下，从0开始顺序编号。 取值范围：0～2147483647 详细信息请参考产品手册的“UPCF软件参数 > PES兼容性软参”。 默认值：无。 配置原则：无。 |

## 使用实例

修改兼容性软参。参数名为N7ReleaseCause，参数值为1。

```
MOD COMPATSWITCH: SWNAME=N7ReleaseCause, SWVALUE=1;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表 错误码列表所示。

|   错误码 | 错误码解释                                      | 原因分析                                   | 处理建议                                     |
|------:|:-------------------------------------------|:---------------------------------------|:-----------------------------------------|
| 56121 | 参数取值无效：参数N15PolicySW的取值范围是0或者1。            | 输入参数N15PolicySW的取值不在取值范围内。             | 重新输入N15PolicySW取值，并保证取值为0或1。             |
| 56122 | 参数取值无效：参数N15RfspSW的取值范围是0或1。               | 输入参数N15RfspSW的取值不在取值范围内。               | 重新输入N15RfspSW取值，并保证取值为0或1。               |
| 56123 | 参数取值无效：参数SessionBackupType的取值范围是0或1。       | 输入参数SessionBackupType的取值不在取值范围内。       | 重新输入SessionBackupType取值，并保证取值为0或1。       |
| 56124 | 参数取值无效：参数NFStatusNtyProcScope的取值范围是0-1。    | 输入参数NFStatusNtyProcScope的取值不在取值范围内。    | 重新输入NFStatusNtyProcScope取值，并保证取值为0或1。    |
| 56125 | 参数取值无效：参数UePTICheckSwitch的取值范围是0或1。        | 输入参数UePTICheckSwitch的取值不在取值范围内。        | 重新输入UePTICheckSwitch取值，并保证取值为0或1。        |
| 56126 | 参数取值无效：参数QuotaDefaultStatusMode的取值范围是0或1。  | 输入参数QuotaDefaultStatusMode的取值不在取值范围内。  | 重新输入QuotaDefaultStatusMode取值，并保证取值为0或1。  |
| 56127 | 参数取值无效：参数RouteBatchSwitch的取值范围是0或1。        | 输入参数RouteBatchSwitch的取值不在取值范围内。        | 重新输入RouteBatchSwitch取值，并保证取值为0或1。        |
| 56128 | 参数取值无效：参数DciThreadSeparation的取值范围是0或1。     | 输入参数DciThreadSeparation的取值不在取值范围内。     | 重新输入DciThreadSeparation取值，并保证取值为0或1。     |
| 56130 | 参数取值无效：参数STAWIFILOCSW的取值范围是0或1。            | 输入参数STAWIFILOCSW的取值不在取值范围内。            | 重新输入STAWIFILOCSW取值，并保证取值为0或1。            |
| 56131 | 参数取值无效：参数N7UserLocInfoMatchMode的取值范围是0或1。  | 输入参数N7UserLocInfoMatchMode的取值不在取值范围内。  | 重新输入N7UserLocInfoMatchMode取值，并保证取值为0或1。  |
| 56132 | 参数取值无效：参数DIAMREALMSELECT的取值范围是0或1。         | 输入参数DIAMREALMSELECT的取值不在取值范围内。         | 重新输入DIAMREALMSELECT取值，并保证取值为0或1。         |
| 56133 | 参数取值无效：参数ChfRangeMatchEnhanceSW的取值范围是0或1。  | 输入参数ChfRangeMatchEnhanceSW的取值不在取值范围内。  | 重新输入ChfRangeMatchEnhanceSW取值，并保证取值为0或1。  |
| 56134 | 参数取值无效：参数HttpProblemDetailsSW的取值范围是0或1。    | 输入参数HttpProblemDetailsSW的取值不在取值范围内。    | 重新输入HttpProblemDetailsSW取值，并保证取值为0或1。    |
| 56137 | 参数取值无效：参数ProUptActionSw的取值范围是0或1。          | 输入参数ProUptActionSw的取值不在取值范围内。          | 重新输入ProUptActionSw取值，并保证取值为0或1。          |
| 56139 | 参数取值无效：参数SySelectPeerMethod的取值范围是0或1。      | 输入参数SySelectPeerMethod的取值不在取值范围内。      | 重新输入SySelectPeerMethod取值，并保证取值为0或1。      |
| 56136 | 参数取值无效：参数RelSesByNotifyTimeout的取值范围是0或1。   | 输入参数RelSesByNotifyTimeout的取值不在取值范围内。   | 重新输入RelSesByNotifyTimeout取值，并保证取值为0或1。   |
| 56140 | 参数取值无效：参数ServiceTypeUpdateSwitch的取值范围是0或1。 | 输入参数ServiceTypeUpdateSwitch的取值不在取值范围内。 | 重新输入ServiceTypeUpdateSwitch取值，并保证取值为0或1。 |
| 56138 | 参数取值无效：参数CCRUTriggerRxUpdate的取值范围是0或1。     | 输入参数CCRUTriggerRxUpdate的取值不在取值范围内。     | 重新输入CCRUTriggerRxUpdate取值，并保证取值为0或1。     |
| 56142 | 参数取值无效：参数RACDecodeMode的取值范围是0或1。           | 输入参数RACDecodeMode的取值不在取值范围内。           | 重新输入RACDecodeMode取值，并保证取值为0或1。           |
| 56143 | 参数取值无效：参数N15CalcPLMN的取值范围是0或1。             | 输入参数N15CalcPLMN的取值不在取值范围内。             | 重新输入N15CalcPLMN取值，并保证取值为0或1。             |