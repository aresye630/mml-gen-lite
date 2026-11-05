---
id: ''
name: H-PCF（数据）
ne_type: UNC
type: feature
description: 当用户在拜访地接入网络时，归属地UPCF侧通过归属地SMF侧在Npcf\_SMPolicyControl\_Create/Npcf\_SMPolicyControl\_Update请求消息中携带了vplmnQos信元判断此时用户需要进行SA国际漫游策略控制，随之归属地的UPCF通过更新下发已配置的关联了CmdSessionRule动作的规则来实现SA国际漫游策略控制功能，下发更新的带宽。  本特性支持配置任意条件或不配置条件，只要购买了本特性license（即“82403309 LRM0PCFSAIR100 SA国际漫游策略控制”）且用户在拜访地接入网络时Npcf\_SMPolicyControl\_Create/Npcf\_SMPolicyControl\_Update请求消息中携带了vplmnQos信元，即可支持SA国际漫游策略控制。  以用户在拜访地上线，不配置条件，UPCF对接华为UNC为例：  * SMF发送给UPCF的Npcf\_SMPolicyControl\_Create请求消息中携带“vplmnQos”信元，最大上、下行带宽分别为1000 Kbps、1000 Kbps。 * UPCF上配置的会话级最大上、下行带宽分别为50 Mbps、20 Mbps。 * 系统比较用户请求的带宽和UPCF上配置的带宽，取带宽低的进行下发。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 国际漫游解决方案","功能部署","业务部署","运营商B（中小型运营商）配置","H-PCF（数据）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户在拜访地接入网络时，归属地UPCF侧通过归属地SMF侧在Npcf\_SMPolicyControl\_Create/Npcf\_SMPolicyControl\_Update请求消息中携带了vplmnQos信元判断此时用户需要进行SA国际漫游策略控制，随之归属地的UPCF通过更新下发已配置的关联了CmdSessionRule动作的规则来实现SA国际漫游策略控制功能，下发更新的带宽。本特性支持配置任意条件或不配置条件，只要购买了本特性license（即“82403309 LRM0PCFSAIR100 SA国际漫游策略控制”）且用户在拜访地接入网络时Npcf\_SMPolicyControl\_Create/Npcf\_SMPolicyControl\_Update请求消息中携带了vplmnQos信元，即可支持SA国际漫游策略控制。以用户在拜访地上线，不配置条件，UPCF对接华为UNC为例：* SMF发送给UPCF的Npcf\_SMPolicyControl\_Create请求消息中携带“vplmnQos”信元，最大上、下行带宽分别为1000 Kbps、1000 Kbps。* UPCF上配置的会话级最大上、下行带宽分别为50 Mbps、20 Mbps。* 系统比较用户请求的带宽和UPCF上配置的带宽，取带宽低的进行下发。

## 必备事项
前提条件

操作员已参考《UPCF 产品文档》了解**WHFD-611107 SA国际漫游策略控制特性概述**，且通过**4G/5G业务配置差异介绍**已经了解5G规则配置原理。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngaction_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulengaction_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policy_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policyrule_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policytrigger_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICETYPE:
          name: 'SERVICETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: 'SP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISMETERTOBASIC:
          name: 'ISMETERTOBASIC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: 'ACTIVATEDBY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QOSMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: 'SUBSCRIPTIONFORCED'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROBILLDATE:
          name: 'PROBILLDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: 'QUOTAALLOCATIONMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: 'ISSETSHAREDMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: 'ISGROUPSERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: 'ISTEMPLATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: 'ISRECUSRLOC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APNMATCHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: 'HASBASESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: 'CALCVALIDFORDYNSUBGROUP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_servicepolicy_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
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
    add_ngaction_list:
    - ACTIONNAME: gjmy_arp
      TYPE: Arp
    add_ngactionattr_list:
    - ACTIONNAME: gjmy_arp
      ATTRNAME: priorityLevel
      TYPE: Object Attribute
      VALUE: SmfSession.SubsDefQosPriorityLevel
    add_rule_list:
    - RULENAME: gjmy_SR
      TYPE: Smf Session Rule 5G
      RELATION: AND
    add_rulengaction_list:
    - RULENAME: gjmy_SR
      ACTIONNAME: gjmy_SessAction
    add_policy_list:
    - POLICYNAME: gjmy_5GPCC
      TYPE: N7 Policy
    add_policyrule_list:
    - POLICYNAME: gjmy_5GPCC
      RULENAME: gjmy_SR
    add_policytrigger_list:
    - POLICYNAME: gjmy_5GPCC
      TRIGGERNAME: IPCAN_EST
    add_service_list:
    - SERVICENAME: gjmy_5GPCC
      SERVICETYPE: VALUE_ADDED_SERVICE
      SP: default1
      ISMETERTOBASIC: Yes
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
    add_servicepolicy_list:
    - SERVICENAME: gjmy_5GPCC
      POLICYNAME: gjmy_5GPCC
    add_psub_list:
    - USRIDENTIFIER: 46010381012****
      USRMSISDN: '12345678901'
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 46010381012****
      SRVNAME: gjmy_5GPCC
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 确认已加载特性License。

### 确认已经在NF上申请并加载对应的License项。国际漫游解决方案涉及的License控制项详细请参考特性映射与交互。

### 2 登录UPCF Web UI界面。

### 3 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 此场景需配置动作：Arp、Ambr、DefaultQosInformation、SessionRuleAction、CmdSessionRuleAction，相关应用场景如下：

### Ambr：用于设置会话类型的上下行带宽。

### Arp：当需要配置“类型”为“DefaultQosInformation”的动作组时必须配置此动作。

### DefaultQosInformation：用于设置会话类型的QoS信息。

### SessionRuleAction：当需要配置会话类型规则，配置此动作。

### CmdSessionRuleAction：当需要配置会话类型规则，配置此动作。

### 动作组的数据规划如表2所示，详细参数说明请参见动作组参数表。

### 动作组gjmy\_SessAction：动作Arp、Ambr、DefaultQosInformation、SessionRuleAction

### 动作组gjmy\_CmdSessAction：动作Arp、Ambr、DefaultQosInformation、CmdSessionRuleAction

### **表2** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | gjmy\_arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPriorityLevel |

### |  |  | preemptCap | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionCap |

### |  |  | preemptVuln | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionVuln |

### | 5G动作组2 | 基本信息 | 名称 | gjmy\_cmdarp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Object Attribute * 值：SmfSession.VPlmnQosArpPriorityLevel |

### |  |  | preemptCap | * 类型：Object Attribute * 值：SmfSession.VPlmnQosArpPreemptionCap |

### |  |  | preemptVuln | * 类型：Object Attribute * 值：SmfSession.VPlmnQosArpPreemptionVuln |

### | 5G动作组3 | 基本信息 | 名称 | gjmy\_AMBR |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | 1000 Kbps |

### |  |  | downlink | 1000 Kbps |

### | 5G动作组4 | 基本信息 | 名称 | gjmy\_CmdAMBR |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | SmfSession.VPlmnQosAmbrUplink |

### |  |  | downlink | SmfSession.VPlmnQosAmbrDownlink |

### | 5G动作组5 | 基本信息 | 名称 | gjmy\_defQos |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Object Attribute * 值：SmfSession.SubsDefQos5qi |

### |  |  | arp | * 类型：Reference ActionGroup * 值：gjmy\_arp  说明：  已在5G动作组中定义。 |

### | 5G动作组6 | 基本信息 | 名称 | gjmy\_CmddefQos |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Object Attribute * 值：SmfSession.VPlmnQos5qi |

### |  |  | arp | * 类型：Reference ActionGroup * 值：gjmy\_cmdarp  说明：  已在5G动作组中定义。 |

### | 5G动作组7 | 基本信息 | 名称 | gjmy\_SessAction |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：gjmy\_SessAction\_1 |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：gjmy\_AMBR  说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：gjmy\_defQos  说明：  已在5G动作组中定义。 |

### | 5G动作组8 | 基本信息 | 名称 | gjmy\_CmdSessAction |

### |  |  | 类型 | CmdSessionRuleAction |

### |  | 属性 | authSessAmbr | * 类型：Reference ActionGroup * 值：gjmy\_CmdAMBR  说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：gjmy\_CmddefQos  说明：  已在5G动作组中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=3 -->
```

### 4 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表3所示，详细参数说明请参见规则参数表。

### **表3** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | gjmy\_SR |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 5G动作组 | 5G动作组 | gjmy\_SessAction  说明：  已在动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | gjmy\_CmdSR |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 5G动作组 | 5G动作组 | gjmy\_CmdSessAction  说明：  已在动作组中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=4 -->
```

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表4所示，详细参数说明请参见策略参数表。

### **表4** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | gjmy\_5GPCC |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * gjmy\_SR * gjmy\_CmdSR 说明：  已在规则中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=5 -->
```

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见**套餐**。

### 业务的数据规划如表5所示，详细参数说明请参见业务参数表。

### **表5** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | gjmy\_5GPCC |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | APN匹配类型 | 全匹配 |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | gjmy\_5GPCC  说明：  已在策略中定义。 |

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=6 -->
```

### 7 登录“UPCF 业务管理”窗口。

### 8 发放业务。

#### 8.1 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参**VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）**控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=8.1 -->
```

#### 8.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=8.2 -->
```

