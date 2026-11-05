---
id: ''
name: PCF侧业务配置
ne_type: UNC
type: feature
description: 该场景根据整体方案设计需配置1个业务，该业务挂载3个策略：  * 策略1（Policy\_ADC\_Normal），规划两个规则，详细如下：   + 规则1（Rule\_ADC\_Normal\_PCC）：关键参数规划为maxbrUL=1 Mbit/s，maxbrDL=1 Mbit/s。   + 规则2（Rule\_ADC\_AppId\_PCC）：关键参数规划为maxbrUL=1 Mbit/s，maxbrDL=1 Mbit/s，AppId=flow\_ADC。 * 策略2（Policy\_ADC\_Start），规划1个规则，详细如下：    规则3（Rule\_ADC\_Start\_PCC）：关键参数规划为5qi=4，arp=1，maxbrUL=100 Mbit/s，maxbrDL=100 Mbit/s，gbrUI=100 Mbit/s，gbrDI=100 Mbit/s，AppId=flow\_ADC。 * 策略3（Policy\_ADC\_Stop），规划1个规则，详细如下：    规则4（Rule\_ADC\_Stop\_PCC）：选择Non-PCC类型规则。
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于业务类别的带宽差异化控制方案设计（ADC）","E2E业务配置","PCF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该场景根据整体方案设计需配置1个业务，该业务挂载3个策略：* 策略1（Policy\_ADC\_Normal），规划两个规则，详细如下：  + 规则1（Rule\_ADC\_Normal\_PCC）：关键参数规划为maxbrUL=1 Mbit/s，maxbrDL=1 Mbit/s。  + 规则2（Rule\_ADC\_AppId\_PCC）：关键参数规划为maxbrUL=1 Mbit/s，maxbrDL=1 Mbit/s，AppId=flow\_ADC。* 策略2（Policy\_ADC\_Start），规划1个规则，详细如下：  规则3（Rule\_ADC\_Start\_PCC）：关键参数规划为5qi=4，arp=1，maxbrUL=100 Mbit/s，maxbrDL=100 Mbit/s，gbrUI=100 Mbit/s，gbrDI=100 Mbit/s，AppId=flow\_ADC。* 策略3（Policy\_ADC\_Stop），规划1个规则，详细如下：  规则4（Rule\_ADC\_Stop\_PCC）：选择Non-PCC类型规则。

## 必备事项
前提条件

已通过学习SM策略E2E实现原理、业务配置方法及业务调测方法了解了SM策略的配置原理及方法。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    - USRIDENTIFIER: 46000120010****
      USRMSISDN: 861390010****
      USRSTATE: Normal
      USRPAIDTYPE: 'NULL'
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
    add_psrv_list:
    - USRIDENTIFIER: 46000120010****
      SRVNAME: ADC_Service
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录**“UPCF Web UI”**界面

### 2 配置策略“Policy\_ADC\_Normal”。

#### 2.1 配置“动作组”。

#### 导航入口为“策略管理 > 5G动作组”

#### 此场景配置5G动作组需要考虑流信息、业务流开关和带宽调整，则需配置动作：FlowInformation、TrafficControlData和QoSData。相关应用场景如下：

#### FlowInformation：当需要下发流信息时需配置此动作。

#### TrafficControlData：当需要做门限控制时，配置此动作。在下发流描述时，如果不配默认为放通该流，当需要限制流时，此动作必须配置。

#### QoSData：当需要进行带宽控制时，配置此动作。

#### 根据业务配置逻辑章节介绍的5G场景中QoS Flow的建立方法，此处示例采用“仅使用DynamicPccRule类型动作建立缺省QoS Flow”的方法进行配置。根据整体方案设计步骤可知，该业务场景须建立两条规则，对应需要配置2个“DynamicPccRule”类型的5G动作组，其中Rule\_ADC\_Normal\_PCC保障用户使用其他应用时的带宽，Rule\_ADC\_AppId\_PCC用于下发appId，通知UPF检测用户是否在使用特定视频应用。详细动作组参数可参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>5G动作组”。

#### **表1** 5G动作组之流描述配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组1 | 基本信息 | 名称 | AG\_FlowDesc |

#### |  |  | 类型 | FlowDescription |

#### |  | 属性 | action | * 类型：Value * 值：PERMIT |

#### |  |  | direction | * 类型：Value * 值：OUT |

#### |  |  | protocol | * 类型：Value * 值：ANY |

#### |  |  | sourceIP | * 类型：Value * 值：any |

#### |  |  | destinationIP | * 类型：Value * 值：any |

#### **表2** 5G动作组之流信息配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组2 | 基本信息 | 名称 | AG\_FlowInfo |

#### |  |  | 类型 | FlowInformation |

#### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：AG\_FlowDesc  说明：  已在表1中定义。 |

#### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

#### |  |  | packetFilterUsage | * 类型：Value * 值：True |

#### **表3** 5G动作组之流控制信息配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组3 | 基本信息 | 名称 | AG\_TraCtrl |

#### |  |  | 类型 | TrafficControlData |

#### |  | 属性 | tcId | * 类型：Value * 值：AG\_TraCtrl |

#### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

#### **表4** 5G动作组之“用户使用其他应用”的ARP配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组4 | 基本信息 | 名称 | AG\_Arp\_Normal |

#### |  |  | 类型 | Arp |

#### |  | 属性 | priorityLevel | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPriorityLevel  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

#### |  |  | preemptCap | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionCap  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

#### |  |  | preemptVuln | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionVuln  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

#### **表5** 5G动作组之“用户使用其他应用”的QoSData配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组5 | 基本信息 | 名称 | AG\_Qos\_Normal |

#### |  |  | 类型 | QoSData |

#### |  | 属性 | qosId | * 类型：Value * 值：AG\_Qos\_Normal |

#### |  |  | 5qi | * 类型：Object Attribute * 值：SmfSession.SubsDefQos5qi 说明：  该种配置表明PCF直接取的用户上线请求的5qi进行配置下发。 |

#### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Arp\_Normal 说明：  已在中表4定义。 |

#### |  |  | maxbrUl | * 类型：Value * 值：1 Mbps |

#### |  |  | maxbrDl | * 类型：Value * 值：1 Mbps |

#### **表6** 5G动作组之“用户使用其他应用”的DynamicPccRule配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组6 | 基本信息 | 名称 | AG\_ADC\_Normal |

#### |  |  | 类型 | DynamicPccRule |

#### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_ADC\_Normal |

#### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_FlowInfo 说明：  已在表2中定义。 |

#### |  |  | precedence | * 类型：Value * 值：30 说明：  规则或业务流的优先级。Precedence值越小优先级越高。 |

#### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Normal 说明：  已在表5中定义。 |

#### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表3中定义。 |

#### **表7** 5G动作组之“下发appId”的DynamicPccRule配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组7 | 基本信息 | 名称 | AG\_ADC\_AppId |

#### |  |  | 类型 | DynamicPccRule |

#### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_ADC\_AppId |

#### |  |  | appId | * 类型：Value * 值：flow\_ADC 说明：  该appId的取值需与UPF上配置的取值保持一致。 |

#### |  |  | precedence | * 类型：Value * 值：2 说明：  规则或业务流的优先级。Precedence值越小优先级越高。 |

#### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Normal 说明：  已在表5中定义。 |

#### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表3中定义。 |

#### 2.2 配置“规则”。

#### 导航入口为“策略管理 > 策略 > 规则”。

#### 规则的数据规划如表8和表9所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>规则”。

#### **表8** 规则(“用户使用其他应用”)

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 规则1 | 基本信息 | 名称 | Rule\_ADC\_Normal\_PCC |

#### |  |  | 操作类型 | Change Rule |

#### |  |  | 类型 | 5G Smf Pcc Rule |

#### |  | 5G动作组 | 5G动作组 | AG\_ADC\_Normal  说明：  已在表6中定义。 |

#### **表9** 规则(“下发appId”)

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 规则2 | 基本信息 | 名称 | Rule\_ADC\_AppId\_PCC |

#### |  |  | 操作类型 | Change Rule |

#### |  |  | 类型 | 5G Smf Pcc Rule |

#### |  | 5G动作组 | 5G动作组 | AG\_ADC\_AppId  说明：  已在表7中定义。 |

#### 2.3 配置“策略”。

#### 导航入口为“策略管理 > 策略 > 策略”。

#### 策略的数据规划如表10所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>策略”。

#### **表10** 策略（Policy\_ADC\_Normal）

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 策略1 | 基本信息 | 名称 | Policy\_ADC\_Normal |

#### |  |  | 策略类型 | N7 Policy |

#### |  | 触发器 | 名称 | IPCAN\_EST |

#### |  | 规则 | 名称 | * Rule\_ADC\_Normal\_PCC * Rule\_ADC\_AppId\_PCC 说明：  已在表8和表9中定义。 |

### 3 配置策略“Policy\_ADC\_Start”。

#### 3.1 配置“动作组”。

#### 导航入口为“策略管理 > 5G动作组”

#### 5G动作组的数据规划如表11，表12和表13所示，详细动作组参数可参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>5G动作组”。

#### **表11** 5G动作组之“特定视频应用”的ARP配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组8 | 基本信息 | 名称 | AG\_Arp\_Special |

#### |  |  | 类型 | Arp |

#### |  | 属性 | priorityLevel | * 类型：Value * 值：2 |

#### |  |  | preemptCap | * 类型：Value * 值：MAY\_PREEMPT |

#### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

#### **表12** 5G动作组之“特定视频应用”的QoSData配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组9 | 基本信息 | 名称 | AG\_Qos\_Special |

#### |  |  | 类型 | QoSData |

#### |  | 属性 | qosId | * 类型：Value * 值：AG\_Qos\_Special |

#### |  |  | 5qi | * 类型：Value * 值：4 说明：  此处“5qi”取值为“4”，表示建立专有QoS FLow。 |

#### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Arp\_Special 说明：  已在中表11定义。 |

#### |  |  | maxbrUl | * 类型：Value * 值：100 Mbps |

#### |  |  | maxbrDl | * 类型：Value * 值：100 Mbps |

#### |  |  | gbrUl | * 类型：Value * 值：100 Mbps |

#### |  |  | gbrDl | * 类型：Value * 值：100 Mbps |

#### **表13** 5G动作组之“特定视频应用”的DynamicPccRule配置

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 5G动作组10 | 基本信息 | 名称 | AG\_ADC\_Special |

#### |  |  | 类型 | DynamicPccRule |

#### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_ADC\_Special |

#### |  |  | appId | * 类型：Value * 值：flow\_ADC 说明：  该appId的取值需与UPF上配置的取值保持一致。 |

#### |  |  | precedence | * 类型：Value * 值：1 说明：  规则或业务流的优先级。Precedence值越小优先级越高。 |

#### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Special 说明：  已在表12中定义。 |

#### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表3中定义。 |

#### 3.2 配置“规则”。

#### 导航入口为“策略管理 > 策略 > 规则”。

#### 规则的数据规划如表14所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>规则”。

#### **表14** 规则（“特定视频应用”）

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 规则3 | 基本信息 | 名称 | Rule\_ADC\_Start\_PCC |

#### |  |  | 操作类型 | Change Rule |

#### |  |  | 类型 | 5G Smf Pcc Rule |

#### |  | 5G动作组 | 5G动作组 | AG\_ADC\_Special  说明：  已在表13中定义。 |

#### 3.3 配置“策略”。

#### 导航入口为“策略管理 > 策略 > 策略”。

#### 策略的数据规划如表15所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>策略”。

#### **表15** 策略（Policy\_ADC\_Start）

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 策略2 | 基本信息 | 名称 | Policy\_ADC\_Start |

#### |  |  | 策略类型 | N7 Policy |

#### |  | 触发器 | 名称 | APP\_STA |

#### |  | 规则 | 名称 | Rule\_ADC\_Start\_PCC  说明：  已在表14中定义。 |

### 4 配置策略“Policy\_ADC\_Stop”。

#### 4.1 配置“规则”。

#### 导航入口为“策略管理 > 策略 > 规则”。

#### 规则的数据规划如表16所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>规则”。

#### **表16** 规则（“用户停止视频应用”）

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 规则4 | 基本信息 | 名称 | Rule\_ADC\_Stop\_PCC |

#### |  |  | 类型 | Non-PCC |

#### |  |  | EDR | OFF |

#### 4.2 配置“策略”。

#### 导航入口为“策略管理 > 策略 > 策略”。

#### 策略的数据规划如表17所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>策略”。

#### **表17** 策略（Policy\_ADC\_Stop）

#### | 类别 | 参数 |  | 取值样例 |

#### | --- | --- | --- | --- |

#### | 策略3 | 基本信息 | 名称 | Policy\_ADC\_Stop |

#### |  |  | 策略类型 | N7 Policy |

#### |  | 触发器 | 名称 | APP\_STO |

#### |  | 规则 | 名称 | Rule\_ADC\_Stop\_PCC  说明：  已在表16中定义。 |

### 5 配置“业务”。

### 导航入口为“业务管理 > 业务 > 业务”。

### 业务的数据规划如表18所示。

### **表18** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | ADC\_Service |

### |  |  | 类型 | BASIC\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | * Policy\_ADC\_Normal * Policy\_ADC\_Start * Policy\_ADC\_Stop 说明：  已在表10，表15和表17中定义。 |

### 6 “开户”。

### 登录**“UPCF PGW Web LMT>UPCF 业务管理”**窗口，将配置完成的业务通过UPCF开户签约系统进行下发。

### 执行**ADD PSUB**增加一个用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=6 -->
```

### 7 “业务发放”。

### 在“UPCF PGW Web LMT>UPCF 业务管理”窗口继续执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=7 -->
```

