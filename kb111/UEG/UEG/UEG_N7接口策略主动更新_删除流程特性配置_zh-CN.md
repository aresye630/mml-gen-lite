---
id: GWFD-025305
name: N7接口策略主动更新/删除流程特性配置
ne_type: UEG
type: feature
description: 以一个典型的N7接口PDU上线、PCF发起的会话更新及会话删除为例，详细介绍PCF侧的业务配置。操作场景为，当5G网络中用户上线状态正常时，可享受正常高速带宽，当状态不正常时，运营商可调整用户的访问带宽。  场景具体描述如下：  * PDU会话上线阶段：用户上线，根据上线状态做带宽控制，   + 当上线状态正常时，上行带宽为10 Mbit/s，下行带宽为10 Mbit/s。   + 当上线状态不正常时，上行带宽降为1 Mbit/s，下行带宽降为1 Mbit/s。 * PDU会话更新：PCF侧修改用户状态不为“Normal”。 * 不配置消息通知。 * PDU会话删除：用户主动下线。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF FE基本功能","GWFD-025305 N7接口(使用HTTP协议)策略控制","GWFD-025305 N7接口(使用HTTP协议)策略控制特性配置","N7接口策略主动更新/删除流程特性配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
以一个典型的N7接口PDU上线、PCF发起的会话更新及会话删除为例，详细介绍PCF侧的业务配置。操作场景为，当5G网络中用户上线状态正常时，可享受正常高速带宽，当状态不正常时，运营商可调整用户的访问带宽。场景具体描述如下：* PDU会话上线阶段：用户上线，根据上线状态做带宽控制，  + 当上线状态正常时，上行带宽为10 Mbit/s，下行带宽为10 Mbit/s。  + 当上线状态不正常时，上行带宽降为1 Mbit/s，下行带宽降为1 Mbit/s。* PDU会话更新：PCF侧修改用户状态不为“Normal”。* 不配置消息通知。* PDU会话删除：用户主动下线。

## 必备事项
前提条件

操作员已了解GWFD-025305 N7接口（使用HTTP协议）策略控制特性概述，且通过4G/5G业务配置差异介绍已经了解5G规则配置原理。
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
    mod_psub_list:
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
        USRSTATE:
          name: 'USRSTATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRRSTCATEGORY:
          name: 'USRRSTCATEGORY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRCLRHOMESRVZONE:
          name: 'USRCLRHOMESRVZONE'
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
      SRVNAME: Service_N7
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
    mod_psub_list:
    - USRIDENTIFIER: 46010381012****
      USRSTATE: SubStatusA
      USRRSTCATEGORY: No
      USRCLRHOMESRVZONE: No
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UPCF Web UI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### **表2** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Normal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_Normal |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Status |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal  说明：  “Normal”：源自PGW Web LMT上的开户命令**ADD PSUB**中的参数“USRSTATE”。 |

### | 条件组2 | 基本信息 | 名称 | CG\_NotNormal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_NotNormal |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Status |

### |  |  | 操作符 | Not Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal  说明：  “Normal”：源自PGW Web LMT上的开户命令**ADD PSUB**中的参数“USRSTATE”。 |

### 3 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 5G动作组的数据规划如表4所示，详细参数说明请参见参数说明。

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

### | 5G动作组2 | 基本信息 | 名称 | Default\_FloInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：Default\_FloDes 说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组3 | 基本信息 | 名称 | TcData |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：TcData |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组4 | 基本信息 | 名称 | Arp01 |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组5 | 基本信息 | 名称 | DefQoSData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：DefQoSData |

### |  |  | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：10000 Kbps |

### |  |  | maxbrDl | * 类型：Value * 值：10000 Kbps |

### | 5G动作组6 | 基本信息 | 名称 | NotNormalDynQoSData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：NotNormalDynQoSData |

### |  |  | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：1000 Kbps |

### |  |  | maxbrDl | * 类型：Value * 值：1000 Kbps |

### | 5G动作组7 | 基本信息 | 名称 | AG3\_Dynamic\_NotNor |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG3\_Dynamic\_NotNor |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：Default\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：NotNormalDynQoSData 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：TcData 说明：  已在5G动作组中定义。 |

### | 5G动作组8 | 基本信息 | 名称 | AG2\_Default\_Dynamic |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG2\_Default\_Dynamic |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：Default\_FloInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：DefQoSData 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：TcData 说明：  已在5G动作组中定义。 |

### | 5G动作组9 | 基本信息 | 名称 | DefSessionAmbr |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Value * 值：10000 Kbps |

### |  |  | downlink | * 类型：Value * 值：10000 Kbps |

### | 5G动作组10 | 基本信息 | 名称 | DefQoSInfo |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：Arp01 说明：  已在5G动作组中定义。 |

### | 5G动作组11 | 基本信息 | 名称 | AG1\_Default\_Session |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG1\_Default\_Session |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：DefSessionAmbr 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：DefQoSInfo 说明：  已在5G动作组中定义。 |

### 4 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表4所示，详细参数说明请参见参数说明。

### **表4** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Default\_Normal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Normal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG1\_Default\_Session  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Dynamic\_Normal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Normal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG2\_Default\_Dynamic  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Default\_NotNormal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_NotNormal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG1\_Default\_Session  说明：  已在5G动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | Dynamic\_NotNormal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_NotNormal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG3\_Dynamic\_NotNor  说明：  已在5G动作组中定义。 |

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表5所示，详细参数说明请参见参数说明。

### **表5** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Policy\_N7 |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * Default\_Normal * Default\_NotNormal * Dynamic\_Norma * Dynamic\_NotNormal 说明：  已在规则中定义。 |

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见套餐。

### 业务的数据规划如表6所示，详细参数说明请参见参数说明。

### **表6** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Service\_N7 |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_N7  说明：  已在策略中定义。 |

### 7 登录“UPCF 业务管理”窗口。

### 8 发放业务。

#### 8.1 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=8.1 -->
```

#### 8.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=8.2 -->
```

#### 8.3 PDU会话更新时，执行**MOD PSUB**修改用户状态。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_psub_list的变量区（command: MOD PSUB） -#}
<!-- MISSING_MACRO: command=MOD PSUB list_name=mod_psub_list step_id=8.3 -->
```

