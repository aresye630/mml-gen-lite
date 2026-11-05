# 修改PCRF对端PCEF能力字典项(MOD PCEFABIITEM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响业务的正常使用，需联系华为技术支持确认后再执行。

该命令为配置类命令，用于修改或调整配置数据库中的一条对端PCEF实体能力字典项的数据记录的某些参数，执行命令后立即生效。在该命令中，系统通过“能力字典ID”和“能力字典项ID”参数来唯一标识一条PCEF能力字典记录。

在缺省的情况下，系统初始化时默认为“能力字典项ID”参数的每个字典项进行了赋值，预置的“能力字典项值”如下（以其中一个“能力字典ID”为例）：

```
 能力字典ID  能力字典项ID                   能力字典项值                 

 127         IPSessAbort                       ASR/ASA                      
 127         IPSessRevalidation                UnsupportedRevalidation      
 127         UsageMonitor                      UsageMonitorHuawei           
 127         R7ExtraEvent                      UnsupportedR7ExtraEvent      
 127         BearerControlMode                 DeriveBCMUEOnly              
 127         R8QoS                             UnsupportedR8QoS             
 127         MultipleServiceAPN                UnsupportedMultipleServiceAPN
 127         ProtoClassifierName               UnsupportedProClassifierName 
 127         PredefinedRuleName                UnsupportedPredefinedRuleName
 127         MonitorKeyCodecModeForR9          FourBytesHex                 
 127         AccessNode                        UnsupportedAccessNode        
 127         FBBAction                         UnsupportedFBBAction         
 127         GxFailover                        UnsupportedGxFailover
 127         URLFiltering                      UnsupportedURLFiltering
 127         TetheringControl                  UnsupportedTetheringControl
 127         EventTriggerVersion               R940                        
 127         InstSubID                         Msisdn                       
 127         CiscoSCE                          UnsupportedCiscoSCE          
 127         SecondaryPDP                      UnsupportedSecPDP            
 127         NoEventTriggers                   UnsupportedNoEventTriggers
 127         CarryARPInQosInfoAVPAtSession     NotCarryARPAVP
 127         RedirectionAbility                UnsupportedSFD
 127         ResultCodeSwitch                  UnsupportedRCSwitch
 127         ChangePolicyByRAR                 SupportedChangePolicyByRAR
 127         TermSessionMode                   FailedCCAAndRAR
 127         ForcedMask                        UnsupportedForcedMask
 127         SubProfile                        UnsupportedSubProfile
 127         CiscoQoSGroupRule                 UnsupportQoSGroupRule
 127         AppDetectionAbility               SupportedAppDetection
 127         FlowDirection                     UnsupportedFlowDirection
 127         CombineRule                       UnsupportedCombineRule
 127         ReInsertRule                      NotReInsertRule
 127         FlowDescriptionPosition           ControledByR8QoS
 127         SubscriptionIDInCCA               UnsupportedSubscriptionIDInCCA
 127         SGWRestoreAbility                 UnsupportedSGWRestore
 127         PRAAbility                        UnsupportedPRA
 127         RATTypeinSdSwitch                 Support3gppRatType
 127         G4QosNegotiation                  UnsupportedG4QoSNegotiation
 127         OriginRealmAndHost                FromPeerCfg
 127         MIGAction                         UnsupportMIGAction
 127         CCGroup                           SupportedCCGroup
 127         Disconnectlink                    UnsupportDisconnectlink
 127         BackfillQoS                       SupportedBackfillQoS
 127         DirectLinkFaultSwitchDRA          SupportedSwitchDRA
 127         CarryCommandQoS                   SupportedCarryCommandQoS
 127         OriginStateId                     UnsupportedOriginStateId
```

## 注意事项

需保证能力字典项配置正确，如果配置错误，可能会导致UPCF下发额外的AVP或UPCF没有给对端下发所需要的AVP，从而影响业务的正常使用。

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:--------------|:--------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABILITYDICTID | 能力字典ID  | 用于标识PCEF能力字典的编号。 取值范围：0～127 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ABILITYITEMID | 能力字典项ID | 用于标识PCEF能力字典项。 取值说明： IPSessAbort(IPSessAbort)IPSessRevalidation(IPSessRevalidation)UsageMonitor(UsageMonitor)R7ExtraEvent(R7ExtraEvent)BearerControlMode(BearerControlMode)R8QoS(R8QoS)MultipleServiceAPN(MultipleServiceAPN)ProtoClassifierName(ProtoClassifierName)PredefinedRuleName(PredefinedRuleName)MonitorKeyCodecModeForR9(MonitorKeyCodecModeForR9)AccessNode(AccessNode)FBBAction(FBBAction)GxFailover(GxFailover)URLFiltering(URLFiltering)TetheringControl(TetheringControl)EventTriggerVersion(EventTriggerVersion)InstSubID(InstSubID)CiscoSCE(CiscoSCE)SecondaryPDP(SecondaryPDP)NoEventTriggers(NoEventTriggers)CarryARPInQosInfoAVPAtSession(CarryARPInQosInfoAVPAtSession)RedirectionAbility(RedirectionAbility)ResultCodeSwitch(ResultCodeSwitch)ChangePolicyByRAR(ChangePolicyByRAR)TermSessionMode(TermSessionMode)ForcedMask(ForcedMask)SubProfile(SubProfile)CiscoQoSGroupRule(CiscoQoSGroupRule)AppDetectionAbility(AppDetectionAbility)FlowDirection（FlowDirection）CombineRule(CombineRule)ReInsertRule(ReInsertRule)FlowDescriptionPosition(FlowDescriptionPosition)SubscriptionIDInCCA(SubscriptionIDInCCA)SGWRestoreAbility(SGWRestoreAbility)PRAAbility(PRAAbility)RATTypeinSdSwitch（RATTypeinSdSwitch）G4QosNegotiation（G4QosNegotiation）OriginRealmAndHost（OriginRealmAndHost）MIGAction(MIGAction)CCGroup(CCGroup)DisconnectLink(DisconnectLink)BackfillQoS（BackfillQoS）DirectLinkFaultSwitchDRA（DirectLinkFaultSwitchDRA）CarryCommandQoS(CarryCommandQoS)OriginStateId(OriginStateId) 默认值：无 |
| ABLITYVALUE   | 能力字典项值  | 用于标识能力字典项的取值，能力字典项取值详细描述请参考能力字典项。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## 使用实例

修改PCEF能力项。“能力字典ID”为“64”，“能力字典项ID”为“IPSessAbort”，“能力项取值”为“ASR/ASA”。

```
MOD PCEFABIITEM: ABILITYDICTID=64, ABILITYITEMID=IPSessAbort, ABLITYVALUE=ASR/ASA;
```

```
%%MOD PCEFABIITEM: ABILITYDICTID=64, ABILITYITEMID=IPSessAbort, ABLITYVALUE=ASR/ASA;%%
RETCODE = 0  操作成功

---    END
```