# 修改PES静态流控配置(MOD PESSTCFLOWCTRL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会导致业务异常，需联系华为技术支持确认后再执行。

该命令用于修改PES静态流控开关、启控条件等。系统根据当前配置的流控参数信息和PES服务接收Initial、Update、Delete、AAR消息的负荷状态，判断是否启动静态流控。

该命令的使用场景：当系统处于话务高峰期或流量异常时，操作员可以使用本命令修改PES静态流控参数以达到限流目的。

**说明** 

- Initial消息数为Gx接口CCR-I、N7接口Npcf\_SMPolicyControl\_Create、N15接口Npcf\_AMPolicyControl\_Create与Npcf\_UEPolicyControl\_Create、N24接口Npcf\_AMPolicyControl\_Create消息数之和。
- Update消息数为Gx接口CCR-U、N7接口Npcf\_SMPolicyControl\_Update、N15接口Npcf\_AMPolicyControl\_Update与Npcf\_UEPolicyControl\_Update、N24接口Npcf\_AMPolicyControl\_Update与Npcf\_AMPolicyControl\_UpdateNotify Update与Npcf\_AMPolicyControl\_UpdateNotify Terminate消息数之和。
- Delete消息数为Gx接口CCR-T、N7接口Npcf\_SMPolicyControl\_Delete Request、Rx接口STR、N15接口Npcf\_AMPolicyControl\_Delete与Npcf\_UEPolicyControl\_Delete、N24接口Npcf\_AMPolicyControl\_Delete消息数之和。
- AAR消息数为Rx接口AAR-I与AAR-U消息数之和。

## 注意事项

- 当开启静态流控后，系统将自动丢弃超过系统设置阈值的消息，导致与这些消息相关的业务处理失败。
- 该命令不允许进行批操作。

## 参数说明

| 参数标识            | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                     |
|:----------------|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ID              | ID                  | 可选必选说明：必选参数 参数含义：该参数用于标识一条PES静态流控数据记录。 取值范围：1 默认值：无。 系统初始设置值：1 配置原则：无。                                                                                                                                                                                                                   |
| PESSTCFLWCTRFLG | PES静态流控开关           | 可选必选说明：必选参数 参数含义：该参数用于设置是否启动PES静态流量控制。 取值范围：ON(打开PES静态流控) OFF(关闭PES静态流控) 默认值：无。 系统初始设置值：ON(打开PES静态流控) 配置原则：无。                                                                                                                                                                            |
| TOTALMSGNUM     | 单个PES总消息数流控阈值       | 可选必选说明：可选参数 参数含义：该参数用于设置启动静态流控后，单个PES上消息总数静态流控起控阈值，仅当本命令中的“PES静态流控开关”参数为“ON(打开PES静态流控)”时该参数有效。 取值范围：0-65535，并且能被10整除。 单位：TPS 默认值：无。 系统初始设置值：1800 配置原则：该参数设置时不允许高于系统初始设置值。  说明： 裸机场景下，PES服务处理能力为虚机的1.25倍。                                                                                 |
| INITIALMSGNUM   | 单个PES Initial消息流控阈值 | 可选必选说明：可选参数 参数含义：该参数用于设置启动静态流控后，单个PES上Initial消息数静态流控起控阈值，仅当本命令中的“PES静态流控开关”参数为“ON(打开PES静态流控)”时该参数有效。 取值范围：0-65535，并且能被10整除。 单位：TPS 默认值：无。 系统初始设置值：360 配置原则：该参数设置时不允许高于系统初始设置值。  说明： 裸机场景下，PES服务处理能力为虚机的1.25倍。                                                                            |
| UPDATEMSGNUM    | 单个PES Update消息流控阈值  | 可选必选说明：可选参数 参数含义：该参数用于设置启动静态流控后，单个PES上Update消息数静态流控起控阈值，仅当本命令中的“PES静态流控开关”参数为“ON(打开PES静态流控)”时该参数有效。 取值范围：0-65535，并且能被10整除。 单位：TPS 默认值：无。 系统初始设置值：720 配置原则：该参数设置时不允许高于系统初始设置值。  说明： 裸机场景下，PES服务处理能力为虚机的1.25倍。此处的Update消息，包括N7/N15/N24/Gx的Update消息以及N24的UpdateNotify Update（/Terminate)消息。 |
| DELETEMSGNUM    | 单个PES Delete消息流控阈值  | 可选必选说明：可选参数 参数含义：该参数用于设置启动静态流控后，单个PES上Delete消息数静态流控起控阈值，仅当本命令中的“PES静态流控开关”参数为“ON(打开PES静态流控)”时该参数有效。 取值范围：0-65535，并且能被10整除。 单位：TPS 默认值：无。 系统初始设置值：360 配置原则：该参数设置时不允许高于系统初始设置值。  说明： 裸机场景下，PES服务处理能力为虚机的1.25倍。                                                                             |
| AARMSGNUM       | 单个PES AAR消息流控阈值     | 可选必选说明：可选参数 参数含义：该参数用于设置启动静态流控后，单个PES上AAR消息数静态流控起控阈值，仅当本命令中的“PES静态流控开关”参数为“ON(打开PES静态流控)”时该参数有效。 取值范围：0-65535，并且能被10整除。 单位：TPS 默认值：无。 系统初始设置值：240 配置原则：该参数设置时不允许高于系统初始设置值。  说明： 裸机场景下，PES服务处理能力为虚机的1.25倍。                                                                                |

## 使用实例

修改PES静态流控配置。“PES静态流控开关”为“ON”，“单个PES总消息数流控阈值”为“1500”，“单个PES Initial消息流控阈值”为“300”，“单个PES Update消息流控阈值”为“600”，“单个PES Delete消息流控阈值”为“300”，“单个PES AAR消息流控阈值”为“300”。

```
MOD PESSTCFLOWCTRL: ID=1, PESSTCFLWCTRFLG=ON, TOTALMSGNUM=1500, INITIALMSGNUM=300, UPDATEMSGNUM=600, DELETEMSGNUM=300, AARMSGNUM=300;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释                  | 原因分析                                  | 处理建议                               |
|------:|:-----------------------|:--------------------------------------|:-----------------------------------|
| 58252 | TOTALMSGNUM参数取值超出范围。   | “TOTALMSGNUM”参数的取值不能超过系统初始设置值“1800”。  | 请将“TOTALMSGNUM”参数设置为不超过“1800”。     |
| 58253 | INITIALMSGNUM参数取值超出范围。 | “INITIALMSGNUM”参数的取值不能超过系统初始设置值“360”。 | 请将“INITIALMSGNUM”参数的取值设置为不超过“360”。 |
| 58254 | UPDATEMSGNUM参数取值超出范围。  | “UPDATEMSGNUM”参数的取值不能超过系统初始设置值“720”。  | 请将“UPDATEMSGNUM”参数设置为不超过“720”。     |
| 58255 | DELETEMSGNUM参数取值超出范围。  | “DELETEMSGNUM”参数的取值不能超过系统初始设置值“360”。  | 请将“DELETEMSGNUM”参数设置为不超过“360”。     |
| 58256 | AARMSGNUM参数取值超出范围。     | “AARMSGNUM”参数的取值不能超过系统初始设置值“240”。     | 请将“AARMSGNUM”参数设置为不超过“240”。        |