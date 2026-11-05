---
id: GWFD-025305
name: N7接口策略请求/更新/下线流程特性配置
ne_type: UEG
type: feature
description: 以一个典型的N7接口PDU上线、SMF发起的会话更新及会话删除为例，详细介绍PCF侧的业务配置。操作场景为，当5G网络中用户配额状态正常时，可享受正常高速带宽，当配额耗尽时，运营商可调整用户的访问带宽。  以典型的上网流量包月业务为例：  * 配额为1000MB。 * 每月1号01:00:00进行配额复位，剩余配额采用清零方式。 * 带宽控制：   + 当配额消耗小于100%时，上行带宽为10 Mbit/s，下行带宽为10 Mbit/s。   + 当配额消耗大于等于100%时，上行带宽降为1 Mbit/s，下行带宽降为1 Mbit/s。 * UPCF进行配额累积。 * 不配置消息通知。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF FE基本功能","GWFD-025305 N7接口(使用HTTP协议)策略控制","GWFD-025305 N7接口(使用HTTP协议)策略控制特性配置","N7接口策略请求/更新/下线流程特性配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
以一个典型的N7接口PDU上线、SMF发起的会话更新及会话删除为例，详细介绍PCF侧的业务配置。操作场景为，当5G网络中用户配额状态正常时，可享受正常高速带宽，当配额耗尽时，运营商可调整用户的访问带宽。以典型的上网流量包月业务为例：* 配额为1000MB。* 每月1号01:00:00进行配额复位，剩余配额采用清零方式。* 带宽控制：  + 当配额消耗小于100%时，上行带宽为10 Mbit/s，下行带宽为10 Mbit/s。  + 当配额消耗大于等于100%时，上行带宽降为1 Mbit/s，下行带宽降为1 Mbit/s。* UPCF进行配额累积。* 不配置消息通知。

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
  examples:
    add_psub_list:
    - USRIDENTIFIER: 46010381012****
      USRMSISDN: 1234567****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB
    add_psrv_list:
    - USRIDENTIFIER: 46010381012****
      SRVNAME: Service_FUP_N7
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UPCF Web UI界面。

### 2 配置配额。

### 导航入口为“业务管理 > 业务 > 配额”。

### 配额（Quota）是指一个指定周期内供用户使用的流量或时长额度，也可指单个会话内供用户使用的时长额度。当业务的使用与流量、时长相关时，需要配置配额。

### 配额的数据规划如表2所示，详细参数说明请参见参数说明。

### **表2** 配额

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 配额 | 基本信息 | 名称 | 20GB\_DailyQuota |

### |  |  | 配额管理归属 | UPCC |

### |  |  | 配额类型 | 流量 |

### |  |  | 类型 | 会话级 |

### |  |  | 监控键值 | 1001 |

### |  |  | 值(KB) | 102400 |

### |  |  | 分片类型 | 百分比 |

### |  |  | 分片(%) | 100 |

### |  | 复位设置 | 结帐模式 | 自然日历 |

### |  |  | 复位周期类型 | 月 |

### |  |  | 复位日 | 1 |

### |  |  | 复位时间 | 01:00:00 |

### |  |  | 剩余额处理方式 | 清零 |

### 3 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

### **表3** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_QuotaNormal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_QuotaNormal |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | 20GB\_DailyQuota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal  说明：  “Normal”：表示配额消耗小于Level1。 |

### | 条件组2 | 基本信息 | 名称 | CG\_QuotaExhaust |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | CG\_QuotaExhaust |

### |  |  | 对象属性 | * 对象：Quota * 属性：QuotaStatus |

### |  |  | 对象实例 | 20GB\_DailyQuota  说明：  已在配额中定义。 |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Exhaust  说明：  “Exhaust”：表示配额阈值大于等于100%。 |

### 4 配置5G动作组。导航入口为“策略管理 > 策略 > 5G动作组”。5G动作组的数据规划如表4所示，详细参数说明请参见参数说明。

### **表4** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | DynNormal\_FlowDes |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组2 | 基本信息 | 名称 | DynNormal\_FlowInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：DynNormal\_FlowDes 说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组3 | 基本信息 | 名称 | 20GB\_FlowStatus |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：33 |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组4 | 基本信息 | 名称 | 20GB\_Arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组5 | 基本信息 | 名称 | 20GB\_1001 |

### |  |  | 类型 | UsageMonitoringData |

### |  | 属性 | umId | * 类型：Value * 值：1001 说明：  已在配额中定义。 |

### | 5G动作组6 | 基本信息 | 名称 | 20GB\_QosData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：20GB\_QosData |

### |  |  | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：20GB\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：1000 Kbps |

### |  |  | maxbrDl | * 类型：Value * 值：1000 Kbps |

### | 5G动作组7 | 基本信息 | 名称 | 20GB\_QosData\_speedLimt |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：20GB\_QosData\_speedLimt |

### |  |  | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：20GB\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：1000 Kbps |

### |  |  | maxbrDl | * 类型：Value * 值：1000 Kbps |

### | 5G动作组8 | 基本信息 | 名称 | DynPcc\_Normal |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：DynPcc\_Normal |

### |  |  | appId | 8 |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：DynNormal\_FlowInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：20GB\_QosData 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：20GB\_FlowStatus 说明：  已在5G动作组中定义。 |

### |  |  | refUmData | * 类型：Reference ActionGroup * 值：20GB\_1001 说明：  已在5G动作组中定义。 |

### | 5G动作组9 | 基本信息 | 名称 | DynPcc\_Exhaust |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：DynPcc\_Exhaust |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：DynNormal\_FlowInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：20GB\_QosData\_speedLimt 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：20GB\_FlowStatus 说明：  已在5G动作组中定义。 |

### |  |  | refUmData | * 类型：Reference ActionGroup * 值：20GB\_1001 说明：  已在5G动作组中定义。 |

### | 5G动作组10 | 基本信息 | 名称 | 20GB\_Ambr |

### |  |  | 类型 | Ambr |

### |  | 基本信息 | uplink | * 类型：Value * 值：10 Mbit/s |

### |  |  | downlink | * 类型：Value * 值：10 Mbit/s |

### | 5G动作组11 | 基本信息 | 名称 | 20GB\_DefQos |

### |  |  | 类型 | DefaultQosInformation |

### |  | 基本信息 | 5qi | * 类型：Value * 值：8 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：20GB\_Arp 说明：  已在5G动作组中定义。 |

### | 5G动作组12 | 基本信息 | 名称 | Default\_Normal |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：Default\_Normal |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：20GB\_Ambr 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：20GB\_DefQos 说明：  已在5G动作组中定义。 |

### 5 配置规则。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表5所示，详细参数说明请参见参数说明。

### **表5** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Default\_Normal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_QuotaNormal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Default\_Normal  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | Default\_Exhaust |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_QuotaExhaust  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Default\_Normal  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | Dynamic\_Normal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf PccRule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_QuotaNormal  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Dynamic\_Normal  说明：  已在5G动作组中定义。 |

### | 规则4 | 基本信息 | 名称 | Dynamic\_Exhaust |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_QuotaExhaust  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | Dynamic\_Exhaust  说明：  已在5G动作组中定义。 |

### 6 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表6所示，详细参数说明请参见参数说明。

### **表6** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Policy\_usage |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | * IPCAN\_EST * US\_RE |

### |  | 规则 | 名称 | * Default\_Normal * Dynamic\_Normal * Dynamic\_Exhaust * Default\_Exhaust 说明：  已在规则中定义。 |

### 7 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见套餐。

### 业务的数据规划如表7所示，详细参数说明请参见参数说明。

### **表7** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Service\_FUP\_N7 |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_usage  说明：  已在策略中定义。 |

### |  | 配额 | 名称 | 20GB\_DailyQuota  说明：  已在配额中定义。 |

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

