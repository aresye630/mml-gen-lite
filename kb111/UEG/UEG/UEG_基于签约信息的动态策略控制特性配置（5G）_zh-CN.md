---
id: GWFD-025302
name: 基于签约信息的动态策略控制特性配置（5G）
ne_type: UEG
type: feature
description: UPCF支持根据用户签约的属性信息进行策略控制，如针对不同的用户类别提供差异化的QoS。同时，当5G组网在线用户的签约数据被更改时，例如修改用户的属性、为该用户增删业务，如果签约数据的更改会使用户当前正在使用的策略发生变化，则UPCF会立刻根据修改后的属性值重新进行策略判断，并下发新生成的规则给SMF，使得用户的业务签约变化能够实时生效。  以用户类别不同，UPCF下发不同的策略控制为例：  * 金牌用户接入网络时，上下行带宽为100 Mbit/s。 * 银牌用户接入网络时，上下行带宽为50 Mbit/s。 * 配置动态规则。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF FE基本功能","GWFD-025302 基于签约的动态策略控制","                        特性配置                        ","基于签约信息的动态策略控制特性配置（5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPCF支持根据用户签约的属性信息进行策略控制，如针对不同的用户类别提供差异化的QoS。同时，当5G组网在线用户的签约数据被更改时，例如修改用户的属性、为该用户增删业务，如果签约数据的更改会使用户当前正在使用的策略发生变化，则UPCF会立刻根据修改后的属性值重新进行策略判断，并下发新生成的规则给SMF，使得用户的业务签约变化能够实时生效。以用户类别不同，UPCF下发不同的策略控制为例：* 金牌用户接入网络时，上下行带宽为100 Mbit/s。* 银牌用户接入网络时，上下行带宽为50 Mbit/s。* 配置动态规则。

## 必备事项
前提条件

操作员已了解GWFD-025302 基于签约的动态策略控制特性概述，且通过4G/5G业务配置差异介绍已经了解5G规则配置原理。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
      SRVNAME: 5GService_Category
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UPCF Web UI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 根据用户签约信息的用户类别做策略控制：条件选择对象Subscriber下的属性Category。

### 配置条件组1和条件组2用于判断用户类别为银牌用户或金牌用户。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

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

### 3 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 若配置的规则为动态规则，则必须配置动作组。

### 此场景配置动态规则且需要考虑缺省QoS Flow和调整带宽，则需配置动作：Arp、Ambr、DefaultQosInformation、SessionRuleAction、FlowDescription、FlowInformation、QoSData、DynamicPccRule。相关应用场景如下：

### SessionRuleAction：当需要建立缺省QoS Flow时可配置此动作。

### QoSData：当需要进行带宽控制时均需配置此动作，若不配置则表示不限制QoS。

### 请增加如下动作组和动作：

### 动作组AG\_Category\_Session\_01：动作Arp、Ambr、DefaultQosInformation、SessionRuleAction

### 动作组AG\_Category\_Session\_02：动作Arp、Ambr、DefaultQosInformation、SessionRuleAction

### 动作组AG\_Category\_Dynamic\_01：动作Arp、FlowDescription、FlowInformation、QoSData、DynamicPccRule

### 动作组AG\_Category\_Dynamic\_02：动作Arp、FlowDescription、FlowInformation、QoSData、DynamicPccRule

### 配置动作组用于终端类型为UE1或UE2动作的下发。动作组的数据规划如表3所示，详细参数说明请参见5G动作参数表。

### **表3** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_Category\_Arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组2 | 基本信息 | 名称 | AG\_Category\_Ambr\_01 |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Value * 值：50 Mbps |

### |  |  | downlink | * 类型：Value * 值：50 Mbps |

### | 5G动作组3 | 基本信息 | 名称 | AG\_Category\_Ambr\_02 |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Value * 值：100 Mbps |

### |  |  | downlink | * 类型：Value * 值：100 Mbps |

### | 5G动作组4 | 基本信息 | 名称 | AG\_Category\_DefQoSInfo |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Category\_Arp  说明：  已在5G动作组中定义。 |

### | 5G动作组5 | 基本信息 | 名称 | AG\_Category\_Session\_01 |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG\_Category\_Session\_01 |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：AG\_Category\_Ambr\_01 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：AG\_Category\_DefQoSInfo 说明：  已在5G动作组中定义。 |

### | 5G动作组6 | 基本信息 | 名称 | AG\_Category\_Session\_02 |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG\_Category\_Session\_02 |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：AG\_Category\_Ambr\_02 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：AG\_Category\_DefQoSInfo 说明：  已在5G动作组中定义。 |

### | 5G动作组7 | 基本信息 | 名称 | AG\_Category\_FloDes |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组8 | 基本信息 | 名称 | AG\_Category\_FloInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### |  |  | flowDescription | * 类型：Reference ActionGroup * 值：AG\_Category\_FloDes 说明：  已在5G动作组中定义。 |

### | 5G动作组9 | 基本信息 | 名称 | AG\_Category\_TraCon |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG\_Category\_TraCon |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组10 | 基本信息 | 名称 | AG\_Category\_QoSData\_01 |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_Category\_Default\_01 |

### |  |  | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Category\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：50 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：50 Mbps |

### | 5G动作组11 | 基本信息 | 名称 | AG\_Category\_QoSData\_02 |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_Category\_Default\_02 |

### |  |  | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Category\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：100 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：100 Mbps |

### | 5G动作组12 | 基本信息 | 名称 | AG\_Category\_Dynamic\_01 |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_Category\_Dynamic\_01 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_Category\_TraCon 说明：  已在5G动作组中定义。 |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_Category\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Category\_QoSData\_01 说明：  已在5G动作组中定义。 |

### | 5G动作组13 | 基本信息 | 名称 | AG\_Category\_Dynamic\_02 |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_Category\_Dynamic\_02 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_Category\_TraCon 说明：  已在5G动作组中定义。 |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_Category\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Category\_QoSData\_02 说明：  已在5G动作组中定义。 |

### 4 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表4所示，详细参数说明请参见规则参数表。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Rule1\_silver |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_silver  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Category\_Session\_01  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Rule1\_gold |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND |

### |  |  | 条件组 | CG\_gold  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Category\_Session\_02  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Rule2\_silver |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND |

### |  |  | 条件组 | CG\_silver  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Category\_Dynamic\_01  说明：  已在5G动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | Rule2\_gold |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND |

### |  |  | 条件组 | CG\_gold  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Category\_Dynamic\_02  说明：  已在5G动作组中定义。 |

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表5所示，详细参数说明请参见策略参数表。

### **表5** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | 5GPolicy\_Category |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * Rule1\_silver * Rule1\_gold * Rule2\_silver * Rule2\_gold 说明：  已在规则中定义。 |

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见套餐。

### 业务的数据规划如表6所示，详细参数说明请参见业务参数表。

### **表6** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | 5GService\_Category |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | 5GPolicy\_Category  说明：  已在策略中定义。 |

### 7 登录“UPCF 业务管理”窗口。

### 8 发放业务。

#### 8.1 执行**ADD PSUB**增加一个银牌用户和一个金牌用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=8.1 -->
```

#### 8.2 执行**ADD PSRV**给银牌用户和金牌用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=8.2 -->
```

