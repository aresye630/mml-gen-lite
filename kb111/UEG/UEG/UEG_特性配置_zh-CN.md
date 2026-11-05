---
id: GWFD-025909
name: 特性配置
ne_type: UEG
type: feature
description: 专有QoS Flow用于为特定业务提供特定的QoS（Quality of Service）。当5G网络中需要为特定业务提供端到端的可靠的质量保证时，部署此特性可以为用户的特定业务提供QoS保证。例如：当用户访问某个特性IP时，比如第三方视频网站，能优先保障访问该网站的服务质量，当访问其他网站仅做网页浏览时不需要提供高服务质量保证也能顺利浏览，此场景设置如下：  * 带宽控制：   + 访问第三方视频网站（假设IP地址为：172.28.82.102）时，建立专有QoS Flow，高带宽保障服务质量，上行10 Mbit/s，下行10 Mbit/s；   + 访问非第三方视频网站时，使用默认QoS Flow，普通带宽，上行1 Mbit/s，下行1 Mbit/s； * 配置动态规则
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF语音基本功能","GWFD-025909 专有QoS流","特性配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
专有QoS Flow用于为特定业务提供特定的QoS（Quality of Service）。当5G网络中需要为特定业务提供端到端的可靠的质量保证时，部署此特性可以为用户的特定业务提供QoS保证。例如：当用户访问某个特性IP时，比如第三方视频网站，能优先保障访问该网站的服务质量，当访问其他网站仅做网页浏览时不需要提供高服务质量保证也能顺利浏览，此场景设置如下：* 带宽控制：  + 访问第三方视频网站（假设IP地址为：172.28.82.102）时，建立专有QoS Flow，高带宽保障服务质量，上行10 Mbit/s，下行10 Mbit/s；  + 访问非第三方视频网站时，使用默认QoS Flow，普通带宽，上行1 Mbit/s，下行1 Mbit/s；* 配置动态规则

## 必备事项
前提条件

操作员已了解GWFD-025909 专有QoS流特性概述，且通过4G/5G业务配置差异介绍已经了解5G规则配置原理。
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
    - USRIDENTIFIER: 46010381012****
      USRMSISDN: 1234567****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 46010381012****
      SRVNAME: S_DedicatedQoS
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UPCF Web UI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

### 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 此场景仅配置1个条件组。条件组的数据规划如表2所示，详细参数说明请参见条件组参数表。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_DedicatedQoS |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_DedicatedQoS |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Status |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal |

### 3 配置动作组。

### 导航入口为“策略管理 > 策略 > 动作组”。

### 此场景需配置动作：Arp、Ambr、DefaultQosInformation、SessionRuleAction、FlowDescription、FlowInformation、QoSData、DynamicPccRule，相关应用场景如下：

### FlowInformation：当需要下发流信息时需配置此动作。

### QoSData：需要进行带宽控制时，配置此动作。

### 请增加如下动作组和动作：

### 动作组AG1\_Default\_Session：动作Arp、Ambr、DefaultQosInformation、SessionRuleAction

### 动作组AG2\_Default\_Dynamic：动作Arp、FlowDescription、FlowInformation、QoSData、DynamicPccRule

### 动作组AG3\_Dedi\_Dynamic：动作Arp、FlowDescription、FlowInformation、QoSData、DynamicPccRule

### 动作组的数据规划如表3所示，详细参数说明请参见动作组参数表。

### **表3** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | Default\_FloDes |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组2 | 基本信息 | 名称 | DediDyn\_FloDes |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：172.28.82.102 |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组3 | 基本信息 | 名称 | Default\_FloInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：Default\_FloDes  说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组4 | 基本信息 | 名称 | DediDyn\_FloInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：DediDyn\_FloDes  说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组5 | 基本信息 | 名称 | TcData |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：TcData |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组6 | 基本信息 | 名称 | Arp01 |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组7 | 基本信息 | 名称 | DefQoSData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG2\_Default |

### |  |  | 5qi | * 类型：Value * 值：8 |

### |  |  | priorityLevel | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：1 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：1 Mbps |

### | 5G动作组8 | 基本信息 | 名称 | DediDynQoSData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值： |

### |  |  | 5qi | * 类型：Value * 值：5 |

### |  |  | priorityLevel | * 类型：Value * 值：1 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：10 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：10 Mbps |

### |  |  | gbrUL | * 类型：Value * 值：10 Mbps |

### |  |  | gbrDL | * 类型：Value * 值：10 Mbps |

### | 5G动作组9 | 基本信息 | 名称 | DefQoSInfo |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### |  |  | priorityLevel | 1 |

### | 5G动作组10 | 基本信息 | 名称 | DefSessionAmbr |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Value * 值：10000 Kbps |

### |  |  | downlink | * 类型：Value * 值：10000 Kbps |

### | 5G动作组11 | 基本信息 | 名称 | AG1\_Default\_Session |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG1\_Default\_Session |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：DefSessionAmbr 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：DefQoSInfo 说明：  已在5G动作组中定义。 |

### | 5G动作组12 | 基本信息 | 名称 | AG2\_Default\_Dynamic |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG2\_Default\_Dynamic |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：Default\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：TcData 说明：  已在5G动作组中定义。 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：DefaultQoSData 说明：  已在5G动作组中定义。 |

### | 5G动作组13 | 基本信息 | 名称 | AG3\_Dedi\_Dynamic |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG3\_Dedi\_Dynamic |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：DediDyn\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：TcData 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：DediDyn\_QoSData 说明：  已在5G动作组中定义。 |

### 4 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表4所示，详细参数说明请参见规则参数表。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Default\_SessionRule1 |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_DedicatedQoS  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG1\_Default\_Session  说明：  已在动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Default\_DynamicRule2 |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_DedicatedQoS  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG2\_Default\_Dynamic  说明：  已在动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Dedicated\_DynamicRule3 |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_DedicatedQoS  说明：  已在条件组中定义。 |

### |  | 动作组 | 动作组 | AG3\_Dedi\_Dynamic  说明：  已在动作组中定义。 |

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表5所示，详细参数说明请参见策略参数表。

### **表5** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略1 | 基本信息 | 名称 | P\_DedicatedQoS |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * Default\_SessionRule1 * Default\_DynamicRule2 * Dedicated\_DynamicRule3 说明：  已在规则中定义。 |

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 业务的数据规划如表6所示，详细参数说明请参见业务参数表。

### **表6** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务1 | 基本信息 | 名称 | S\_DedicatedQoS |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### 7 发放套餐。

#### 7.1 登录“UPCF 业务管理”窗口。

#### 7.2 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=7.2 -->
```

#### 7.3 执行**ADD PSRV**给用户签约套餐。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=7.3 -->
```

