# 查询PCRF对端PCEF能力字典项的配置信息(LST PCEFABIITEM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置数据库中查询对端PCEF实体能力字典项的配置信息。

- 如果需要查询全部PCEF能力项的配置信息，请不要输入任何参数。
- 如果需要查询某个PCEF能力项的配置信息，请依据参数说明输入查询条件。

## 注意事项

无。

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABILITYDICTID | 能力字典ID  | 用于标识PCEF能力字典的编号。 取值范围： 0～127 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ABILITYITEMID | 能力字典项ID | 用于标识PCEF能力字典项。 取值说明： IPSessAbort(IPSessAbort)IPSessRevalidation(IPSessRevalidation)UsageMonitor(UsageMonitor)R7ExtraEvent(R7ExtraEvent)BearerControlMode(BearerControlMode)R8QoS(R8QoS)MultipleServiceAPN(MultipleServiceAPN)ProtoClassifierName(ProtoClassifierName)PredefinedRuleName(PredefinedRuleName)MonitorKeyCodecModeForR9(MonitorKeyCodecModeForR9)AccessNode(AccessNode)FBBAction(FBBAction)GxFailover(GxFailover)URLFiltering(URLFiltering)TetheringControl(TetheringControl)EventTriggerVersion(EventTriggerVersion)InstSubID(InstSubID)CiscoSCE(CiscoSCE)SecondaryPDP(SecondaryPDP)NoEventTriggers(NoEventTriggers)CarryARPInQosInfoAVPAtSession(CarryARPInQosInfoAVPAtSession)RedirectionAbility(RedirectionAbility)ResultCodeSwitch(ResultCodeSwitch)ChangePolicyByRAR(ChangePolicyByRAR)TermSessionMode(TermSessionMode)ForcedMask(ForcedMask)SubProfile(SubProfile)CiscoQoSGroupRule(CiscoQoSGroupRule)AppDetectionAbility(AppDetectionAbility)FlowDirection(FlowDirection)CombineRule(CombineRule)ReInsertRule(ReInsertRule)FlowDescriptionPosition(FlowDescriptionPosition)SubscriptionIDInCCA(SubscriptionIDInCCA)SGWRestoreAbility(SGWRestoreAbility)PRAAbility(PRAAbility)RATTypeinSdSwitch（RATTypeinSdSwitch）G4QosNegotiation（G4QosNegotiation）OriginRealmAndHost（OriginRealmAndHost）MIGAction(MIGAction)CCGroup(CCGroup)DisconnectLink(DisconnectLink)BackfillQoS（BackfillQoS）DirectLinkFaultSwitchDRA(DirectLinkFaultSwitchDRA)CarryCommandQoS(CarryCommandQoS)OriginStateId(OriginStateId) 默认值：无 |
| ABLITYVALUE   | 能力字典项值  | 用于标识能力字典项的取值，能力字典项取值详细描述请参考能力字典项。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## 使用实例

查询一条PCEF能力项的配置信息。“能力字典ID”为“64”，“能力项ID”为“IPSessAbort”。

```
LST PCEFABIITEM: ABILITYDICTID=64, ABILITYITEMID=IPSessAbort;
```

```
%%LST PCEFABIITEM: ABILITYDICTID=64, ABILITYITEMID=IPSessAbort;%%
RETCODE = 0  操作成功

操作结果如下:
-------------
  能力字典ID  =  64
能力字典项ID  =  IPSessAbort
能力字典项值  =  ASR/ASA
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数说明。