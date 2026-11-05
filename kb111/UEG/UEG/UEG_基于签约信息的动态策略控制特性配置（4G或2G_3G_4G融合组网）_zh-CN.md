---
id: GWFD-025302
name: '                            基于签约信息的动态策略控制特性配置（4G或2G/3G/4G融合组网）                            '
ne_type: UEG
type: feature
description: UPCF支持根据用户签约的属性信息进行策略控制，如针对不同的用户类别提供差异化的QoS。同时，当4G或2G/3G/4G融合组网在线用户的签约数据被更改时，例如修改用户的属性、为该用户增删业务，如果签约数据的更改会使用户当前正在使用的策略发生变化，则UPCF会立刻根据修改后的属性值重新进行策略判断，并下发新生成的规则给PCEF（Policy and Charging Enforcement Function），使得用户的业务签约变化能够实时生效。  以用户类别不同，UPCF下发不同的策略控制为例：  * 金牌用户接入网络时，上下行带宽为2 Mbit/s。 * 银牌用户接入网络时，上下行带宽为1 Mbit/s。 * 配置动态规则。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF FE基本功能","GWFD-025302 基于签约的动态策略控制","                        特性配置                        ","                            基于签约信息的动态策略控制特性配置（4G或2G/3G/4G融合组网）                            "]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPCF支持根据用户签约的属性信息进行策略控制，如针对不同的用户类别提供差异化的QoS。同时，当4G或2G/3G/4G融合组网在线用户的签约数据被更改时，例如修改用户的属性、为该用户增删业务，如果签约数据的更改会使用户当前正在使用的策略发生变化，则UPCF会立刻根据修改后的属性值重新进行策略判断，并下发新生成的规则给PCEF（Policy and Charging Enforcement Function），使得用户的业务签约变化能够实时生效。以用户类别不同，UPCF下发不同的策略控制为例：* 金牌用户接入网络时，上下行带宽为2 Mbit/s。* 银牌用户接入网络时，上下行带宽为1 Mbit/s。* 配置动态规则。

## 必备事项
前提条件

操作员已了解GWFD-025302 基于签约的动态策略控制特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_pcefabiitem_list:
      type: items
      properties:
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ABILITYITEMID:
          name: '能力字典项ID'
          type: string
          enum:
          - IPSessAbort
          - IPSessRevalidation
          - UsageMonitor
          - R7ExtraEvent
          - BearerControlMode
          - R8QoS
          - MultipleServiceAPN
          - ProtoClassifierName
          - PredefinedRuleName
          - MonitorKeyCodecModeForR9
          - AccessNode
          - FBBAction
          - GxFailover
          - URLFiltering
          - TetheringControl
          - EventTriggerVersion
          - InstSubID
          - CiscoSCE
          - SecondaryPDP
          - NoEventTriggers
          - CarryARPInQosInfoAVPAtSession
          - RedirectionAbility
          - ResultCodeSwitch
          - ChangePolicyByRAR
          - TermSessionMode
          - ForcedMask
          - SubProfile
          - CiscoQoSGroupRule
          - AppDetectionAbility
          - FlowDirection
          - CombineRule
          - ReInsertRule
          - FlowDescriptionPosition
          - SubscriptionIDInCCA
          - SGWRestoreAbility
          - PRAAbility
          - RATTypeinSdSwitch
          - G4QosNegotiation
          - OriginRealmAndHost
          - MIGAction
          - CCGroup
          - DisconnectLink
          - BackfillQoS
          - DirectLinkFaultSwitchDRA
          - CarryCommandQoS
          - OriginStateId
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ABLITYVALUE:
          name: '能力字典项值'
          type: string
          enum:
          - ASR/ASA
          - RARWithRelCause
          - UnsupportedRevalidation
          - SupportedRevalidation
          - UsageMonitorHuawei
          - UsageMonitorPreR9
          - UsageMonitor3GPPR9
          - UsageMonitorHuaweiExQtaInst
          - UsageMonitor3GPPR9Enhanced
          - UnsupportedR7ExtraEvent
          - SupportedR7ExtraEvent
          - DeriveBCMUEOnly
          - UnsupportedBCM
          - UnsupportedR8QoS
          - SupportedR8QoS
          - SupportedR7ToR8QoS
          - UnsupportedMultipleServiceAPN
          - SupportedMultipleServiceAPN
          - UnsupportedProClassifierName
          - SupportedProClassifierName
          - UnsupportedPredefinedRuleName
          - SupportedPredefinedRuleName
          - FourBytesHex
          - MaxFourBytesHex
          - ASCIIMode
          - UnsupportedAccessNode
          - SupportedAccessNode
          - UnsupportedFBBAction
          - SupportedFBBAction
          - UnsupportedGxFailover
          - SupportedGxFailover
          - UnsupportedURLFiltering
          - SupportedURLFiltering
          - UnsupportedTetheringControl
          - SupportedTetheringControl
          - R940
          - R970
          - Msisdn
          - Imsi
          - Nai
          - All
          - UnsupportedCiscoSCE
          - SupportedCiscoSCE
          - UnsupportedSecPDP
          - AppendPostfixToRule
          - CreateDynamicRule
          - UnsupportedNoEventTriggers
          - SupportedNoEventTriggers
          - NotCarryARPAVP
          - CarryARPAVP
          - UnsupportedRCSwitch
          - SupportedRCSwitch
          - UnsupportedSFD
          - SupportedSFD
          - SupportedSFDOnly
          - SupportedRedirectOnly
          - SupportNULL
          - FailedCCAAndRAR
          - SuccessedCCAAndRAR
          - CCA
          - FailedCCA
          - UnsupportedChangePolicyByRAR
          - SupportedChangePolicyByRAR
          - UnsupportedForcedMask
          - SupportedForcedMask
          - UnsupportedSubProfile
          - SupportedSubProfile
          - SupportedHWSubProfile
          - UnsupportQoSGroupRule
          - SupportQoSGroupRule
          - UnsupportedAppDetection
          - SupportedAppDetection
          - UnsupportedFlowDirection
          - SupportedFlowDirection
          - UnsupportedCombineRule
          - SupportedCombineRule
          - NotReInsertRule
          - ReInsertRule
          - ControledByR8QoS
          - WithinFlowInformation
          - WithinRuleDefinition
          - UnsupportedSubscriptionIDInCCA
          - SupportedSubscriptionIDInCCA
          - UnsupportedSGWRestore
          - SupportedSGWRestore
          - UnsupportedPRA
          - SupportedPRA
          - SupportRatType
          - Support3gppRatType
          - UnsupportedG4QoSNegotiation
          - NotMoreThanFirstMessage
          - NotMoreThanPreMessage
          - NotMoreThanReqQoSfor4G
          - FillLastMessageQoS
          - LastMsgQoSNegWithPolicyQoS
          - NotMoreThanCCRIUQoS
          - FromPeerCfg
          - FromMessage
          - UnsupportMIGAction
          - SupportMIGAction
          - UnsupportedCCGroup
          - SupportedCCGroup
          - UnsupportDisconnectLink
          - SupportDisconnectLink
          - UnsupportedBackfillQoS
          - SupportedBackfillQoS
          - UnsupportedSwitchDRA
          - SupportedSwitchDRA
          - UnsupportedCarryCommandQoS
          - SupportedCarryCommandQoS
          - UnsupportedOriginStateId
          - SupportedOriginStateId
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_pcefabiitem_list_1:
      type: items
      properties:
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ABILITYITEMID:
          name: '能力字典项ID'
          type: string
          enum:
          - IPSessAbort
          - IPSessRevalidation
          - UsageMonitor
          - R7ExtraEvent
          - BearerControlMode
          - R8QoS
          - MultipleServiceAPN
          - ProtoClassifierName
          - PredefinedRuleName
          - MonitorKeyCodecModeForR9
          - AccessNode
          - FBBAction
          - GxFailover
          - URLFiltering
          - TetheringControl
          - EventTriggerVersion
          - InstSubID
          - CiscoSCE
          - SecondaryPDP
          - NoEventTriggers
          - CarryARPInQosInfoAVPAtSession
          - RedirectionAbility
          - ResultCodeSwitch
          - ChangePolicyByRAR
          - TermSessionMode
          - ForcedMask
          - SubProfile
          - CiscoQoSGroupRule
          - AppDetectionAbility
          - FlowDirection
          - CombineRule
          - ReInsertRule
          - FlowDescriptionPosition
          - SubscriptionIDInCCA
          - SGWRestoreAbility
          - PRAAbility
          - RATTypeinSdSwitch
          - G4QosNegotiation
          - OriginRealmAndHost
          - MIGAction
          - CCGroup
          - DisconnectLink
          - BackfillQoS
          - DirectLinkFaultSwitchDRA
          - CarryCommandQoS
          - OriginStateId
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ABLITYVALUE:
          name: '能力字典项值'
          type: string
          enum:
          - ASR/ASA
          - RARWithRelCause
          - UnsupportedRevalidation
          - SupportedRevalidation
          - UsageMonitorHuawei
          - UsageMonitorPreR9
          - UsageMonitor3GPPR9
          - UsageMonitorHuaweiExQtaInst
          - UsageMonitor3GPPR9Enhanced
          - UnsupportedR7ExtraEvent
          - SupportedR7ExtraEvent
          - DeriveBCMUEOnly
          - UnsupportedBCM
          - UnsupportedR8QoS
          - SupportedR8QoS
          - SupportedR7ToR8QoS
          - UnsupportedMultipleServiceAPN
          - SupportedMultipleServiceAPN
          - UnsupportedProClassifierName
          - SupportedProClassifierName
          - UnsupportedPredefinedRuleName
          - SupportedPredefinedRuleName
          - FourBytesHex
          - MaxFourBytesHex
          - ASCIIMode
          - UnsupportedAccessNode
          - SupportedAccessNode
          - UnsupportedFBBAction
          - SupportedFBBAction
          - UnsupportedGxFailover
          - SupportedGxFailover
          - UnsupportedURLFiltering
          - SupportedURLFiltering
          - UnsupportedTetheringControl
          - SupportedTetheringControl
          - R940
          - R970
          - Msisdn
          - Imsi
          - Nai
          - All
          - UnsupportedCiscoSCE
          - SupportedCiscoSCE
          - UnsupportedSecPDP
          - AppendPostfixToRule
          - CreateDynamicRule
          - UnsupportedNoEventTriggers
          - SupportedNoEventTriggers
          - NotCarryARPAVP
          - CarryARPAVP
          - UnsupportedRCSwitch
          - SupportedRCSwitch
          - UnsupportedSFD
          - SupportedSFD
          - SupportedSFDOnly
          - SupportedRedirectOnly
          - SupportNULL
          - FailedCCAAndRAR
          - SuccessedCCAAndRAR
          - CCA
          - FailedCCA
          - UnsupportedChangePolicyByRAR
          - SupportedChangePolicyByRAR
          - UnsupportedForcedMask
          - SupportedForcedMask
          - UnsupportedSubProfile
          - SupportedSubProfile
          - SupportedHWSubProfile
          - UnsupportQoSGroupRule
          - SupportQoSGroupRule
          - UnsupportedAppDetection
          - SupportedAppDetection
          - UnsupportedFlowDirection
          - SupportedFlowDirection
          - UnsupportedCombineRule
          - SupportedCombineRule
          - NotReInsertRule
          - ReInsertRule
          - ControledByR8QoS
          - WithinFlowInformation
          - WithinRuleDefinition
          - UnsupportedSubscriptionIDInCCA
          - SupportedSubscriptionIDInCCA
          - UnsupportedSGWRestore
          - SupportedSGWRestore
          - UnsupportedPRA
          - SupportedPRA
          - SupportRatType
          - Support3gppRatType
          - UnsupportedG4QoSNegotiation
          - NotMoreThanFirstMessage
          - NotMoreThanPreMessage
          - NotMoreThanReqQoSfor4G
          - FillLastMessageQoS
          - LastMsgQoSNegWithPolicyQoS
          - NotMoreThanCCRIUQoS
          - FromPeerCfg
          - FromMessage
          - UnsupportMIGAction
          - SupportMIGAction
          - UnsupportedCCGroup
          - SupportedCCGroup
          - UnsupportDisconnectLink
          - SupportDisconnectLink
          - UnsupportedBackfillQoS
          - SupportedBackfillQoS
          - UnsupportedSwitchDRA
          - SupportedSwitchDRA
          - UnsupportedCarryCommandQoS
          - SupportedCarryCommandQoS
          - UnsupportedOriginStateId
          - SupportedOriginStateId
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_psub_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRMSISDN:
          name: 'USRMSISDN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATE:
          name: 'USRSTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRPAIDTYPE:
          name: 'USRPAIDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRCATEGORY:
          name: 'USRCATEGORY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSTATION:
          name: 'USRSTATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRCONTACTMETHOD:
          name: 'USRCONTACTMETHOD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRBILLCYCLEDATE:
          name: 'USRBILLCYCLEDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSUBNETTYPE:
          name: 'USRSUBNETTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_psrv_list:
      type: items
      properties:
        USRIDENTIFIER:
          name: 'USRIDENTIFIER'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNAME:
          name: 'SRVNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVUSAGESTATE:
          name: 'SRVUSAGESTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVROAMINGTYPE:
          name: 'SRVROAMINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_pcefabiitem_list:
    - ABILITYDICTID: 68
      ABILITYITEMID: R8QoS
      ABLITYVALUE: SupportedR8QoS
    mod_pcefabiitem_list_1:
    - ABILITYDICTID: 68
      ABILITYITEMID: ChangePolicyByRAR
      ABLITYVALUE: SupportedChangePolicyByRAR
    add_psub_list:
    - USRIDENTIFIER: 460103810123***
      USRMSISDN: 123456788***
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRCATEGORY: silver
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: MBB
    add_psrv_list:
    - USRIDENTIFIER: 460103810123***
      SRVNAME: Service_Category
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 修改对端PCEF能力字典项。

#### 1.1 登录“UEG MML命令”界面。

#### 1.2 执行**MOD PCEFABIITEM**，调整对端PCEF能力字典，使其支持R8标准的QoS。

#### 命令举例：

```jinja2
{%- for item in mod_pcefabiitem_list -%}
    MOD PCEFABIITEM:
    {#- --- 必选参数 --- -#}
    ABILITYDICTID={{item.ABILITYDICTID}},
    ABILITYITEMID={{item.ABILITYITEMID}},
    {#- --- 可选参数 --- -#}
    {%- if item.ABLITYVALUE is not none -%}
        ABLITYVALUE={{item.ABLITYVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 在4G或2G/3G/4G融合组网中，UPCF与华为UEG对接时，“ABILITYDICTID”需设置为“68”。实际的值可以通过如下方式查询：

#### 当UPCF与PCEF直连时，“能力字典ID”可以通过**LST PPCEF**命令查询。

#### 当UPCF与PCEF通过DRA准直连时，“能力字典ID”可以通过**LST PDHOSTCFG**查询。

#### 1.3 执行**MOD PCEFABIITEM**，调整对端PCEF能力字典，使其支持RAR变更策略。

#### 命令举例：

```jinja2
{%- for item in mod_pcefabiitem_list_1 -%}
    MOD PCEFABIITEM:
    {#- --- 必选参数 --- -#}
    ABILITYDICTID={{item.ABILITYDICTID}},
    ABILITYITEMID={{item.ABILITYITEMID}},
    {#- --- 可选参数 --- -#}
    {%- if item.ABLITYVALUE is not none -%}
        ABLITYVALUE={{item.ABLITYVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 登录UPCF Web UI界面。

### 3 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与或关系由参数“关系”决定。

### 需要配置两个条件组，用于判断用户为银牌用户或金牌用户。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_silver |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Condition\_silver |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Category |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | silver  说明：  “silver”：表示用户类别为银牌用户。 |

### | 条件组2 | 基本信息 | 名称 | CG\_gold |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Condition\_gold |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Category |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | gold  说明：  “gold”：表示用户类别为金牌用户。 |

### 4 配置动作组。

### 导航入口为“策略管理 > 策略 > 动作组”。

### 若配置的规则为动态规则，则必须配置动作组。

### 此场景配置动态规则且需要考虑默认承载的QoS、调整带宽和计费动作，则每个动作组需配置动作：DefaultBearerQoS、QoSAction和ChargingAction。相关应用场景如下：

#### 4.1 DefaultBearerQoS：当需要建立默认承载时必须配置此动作。

#### 4.2 QoSAction：当需要进行带宽控制时均需配置此动作，若不配置则表示不限制QoS。

#### 4.3 ChargingAction：当需要做计费策略控制时，配置此动作（若对端为华为UEG，此动作必须配置）。

### 需要配置三个动作组，用于在金牌用户或银牌用户接入网络时动作的下发。动作组的数据规划如表3所示，详细参数说明请参见动作组参数表。

### **表3** 动作组

### | 类别 | 参数 |  |  | 取值样例 |

### | --- | --- | --- | --- | --- |

### | 动作组1 | 基本信息 | 名称 |  | AG1\_silver |

### |  | 动作 | 动作 |  | DefaultBearerQoS |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  |  |  | AMBRDL | * 值类型：Value * 值(Kbit/s)：1000 |

### |  |  |  | AMBRUL | * 值类型：Value * 值(Kbit/s)：1000 |

### | 动作组2 | 基本信息 | 名称 |  | AG1\_gold |

### |  | 动作 | 动作 |  | DefaultBearerQoS |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  |  |  | PreemptionCapability | * 值类型：Value * 值：Disabled |

### |  |  |  | PreemptionVulnerability | * 值类型：Value * 值：Enabled |

### |  |  |  | AMBRDL | * 值类型：Value * 值(Kbit/s)：2000 |

### |  |  |  | AMBRUL | * 值类型：Value * 值(Kbit/s)：2000 |

### | 动作组3 | 基本信息 | 名称 |  | AG2\_silver |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 |

### |  |  |  | MBRUL | * 值类型：Value * 值(Kbit/s)：1000 |

### |  |  |  | MBRDL | * 值类型：Value * 值(Kbit/s)：1000 |

### |  |  |  | GBRUL | * 值类型：Value * 值(Kbit/s)：1000 |

### |  |  |  | GBRDL | * 值类型：Value * 值(Kbit/s)：1000 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  | 动作2 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：1 说明：  与计费系统协商一致。RatingGroup为1，表示不计费。 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### | 动作组4 | 基本信息 | 名称 |  | AG2\_gold |

### |  | 动作1 | 动作 |  | QoSAction |

### |  |  | 动作元素 | QCI | * 值类型：Value * 值：8 |

### |  |  |  | MBRUL | * 值类型：Value * 值(Kbit/s)：2000 |

### |  |  |  | MBRDL | * 值类型：Value * 值(Kbit/s)：2000 |

### |  |  |  | GBRUL | * 值类型：Value * 值(Kbit/s)：2000 |

### |  |  |  | GBRDL | * 值类型：Value * 值(Kbit/s)：2000 |

### |  |  |  | ARPLevel | * 值类型：Value * 值：1 |

### |  | 动作2 | 动作 |  | ChargingAction |

### |  |  | 动作元素 | MeteringMethod | * 值类型：Value * 值：Volume |

### |  |  |  | RatingGroup | * 值类型：Value * 值：1 说明：  与计费系统协商一致。RatingGroup为1，表示不计费。 |

### |  |  |  | ReportingLevel | * 值类型：Value * 值：Rating Group Level |

### 5 配置业务流。

### 导航入口为“策略管理 > 策略 > 业务流”。

### 当对端为华为UEG时，所有的动态规则都必须配置业务流。

### 业务流的数据规划如表4所示，详细参数说明请参见业务流参数表。

### **表4** 业务流

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务流 | 基本信息 | 名称 | Flow\_Filter |

### |  | 流过滤器1 | 名称 | up\_pass |

### |  |  | 流方向 | Up |

### |  |  | 协议 | Any IP Protocol |

### |  | 流过滤器2 | 名称 | down\_pass |

### |  |  | 流方向 | Down |

### |  |  | 协议 | Any IP Protocol |

### 6 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表5所示，详细参数说明请参见规则参数表。

### **表5** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Rule1\_silver |

### |  |  | 类型 | Default Bearer QoS  说明：  默认承载QoS场景，规则类型必须为“Default Bearer QoS”。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_silver  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG1\_silver  说明：  已在动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Rule1\_gold |

### |  |  | 类型 | Default Bearer QoS  说明：  默认承载QoS场景，规则类型必须为“Default Bearer QoS”。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_gold  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG1\_gold  说明：  已在动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Rule2\_silver |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_silver  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG2\_silver  说明：  已在动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | Rule2\_gold |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | Dynamic |

### |  |  | 业务流 | Flow\_Filter  说明：  已在业务流中定义。 |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_gold  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG2\_gold  说明：  已在动作组中定义。 |

### 7 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表6所示，详细参数说明请参见策略参数表。

### **表6** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Policy\_usage |

### |  |  | 策略类型 | Gx Policy |

### |  | 触发器 | 名称 | IPCANSessionEstablish |

### |  | 规则 | 名称 | * Rule1\_silver * Rule1\_gold * Rule2\_silver * Rule2\_gold 说明：  已在规则中定义。 |

### 8 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见套餐。

### 业务的数据规划如表7所示，详细参数说明请参见业务参数表。

### **表7** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Service\_Category |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_usage  说明：  已在策略中定义。 |

### 9 登录“UPCF 业务管理”窗口。

### 10 发放业务。

#### 10.1 执行**ADD PSUB**增加一个银牌用户和一个金牌用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=10.1 -->
```

#### 10.2 执行**ADD PSRV**给银牌用户和金牌用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=10.2 -->
```

### 11 **脚本**

### CLI脚本

