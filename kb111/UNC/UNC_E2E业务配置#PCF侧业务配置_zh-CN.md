---
id: ''
name: PCF侧业务配置
ne_type: UNC
type: feature
description: 该场景根据整体方案设计需配置1个业务，该业务挂载1个策略，该策略包含3个规则：  * 规则1（Rule\\_Gold），详细内容规划如下：   + 条件：Subscriber.Category=Gold   + 动作：ratingGroup=11，maxbrUL=100 Mbps，maxbrDL=100 Mbps * 规则2（Rule\\_Silver），详细内容规划如下：   + 条件：Subscriber.Category=Silver   + 动作：ratingGroup=22，maxbrUL=50 Mbps，maxbrDL=50 Mbps * 规则3（Rule\\_Normal），详细内容规划如下：   + 条件：Subscriber.Category=Normal   + 动作：ratingGroup=33，maxbrUL=10 Mbps，maxbrDL=10 Mbps
risk_level: ''
doc_source: ["网络部署","业务专题","5G PCC之SM策略解决方案","典型业务场景E2E方案设计","基于用户等级的资费差异化控制方案（动态）","E2E业务配置","PCF侧业务配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该场景根据整体方案设计需配置1个业务，该业务挂载1个策略，该策略包含3个规则：* 规则1（Rule\\_Gold），详细内容规划如下：  + 条件：Subscriber.Category=Gold  + 动作：ratingGroup=11，maxbrUL=100 Mbps，maxbrDL=100 Mbps* 规则2（Rule\\_Silver），详细内容规划如下：  + 条件：Subscriber.Category=Silver  + 动作：ratingGroup=22，maxbrUL=50 Mbps，maxbrDL=50 Mbps* 规则3（Rule\\_Normal），详细内容规划如下：  + 条件：Subscriber.Category=Normal  + 动作：ratingGroup=33，maxbrUL=10 Mbps，maxbrDL=10 Mbps

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
        USRLANGUAGE:
          name: 'USRLANGUAGE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRSMSRECEIVEFLAG:
          name: 'USRSMSRECEIVEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRVERSTATUS:
          name: 'USRVERSTATUS'
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
      USRCATEGORY: Gold
      USRSTATION: Master
      USRCONTACTMETHOD: SMS
      USRBILLCYCLEDATE: 'NULL'
      USRSUBNETTYPE: eMBB-SA
      USRLANGUAGE: 'NULL'
      USRSMSRECEIVEFLAG: All
      USRVERSTATUS: Normal
    add_psrv_list:
    - USRIDENTIFIER: 46000120010****
      SRVNAME: Usr_Category_Service
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录**“UPCF Web UI”**界面。

### 2 配置“条件组”。

### 导航入口为“策略管理 > 策略 > 条件组”。

#### 2.1 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

#### 2.2 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 此业务场景下需要配置三个条件组，用于判断用户的等级为金牌用户，银牌用户还是普通用户。条件组的数据规划如表1，表2和表3所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>条件组”帮助页面。

### **表1** 条件组1（“用户等级”为“金牌”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | CG\_Gold |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Condition\_Gold |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Category |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Gold  说明：  “Gold”：表示用户等级为金牌用户。该取值须与用户在UPCF PGW Web LMT上通过**ADD PSUB**命令开户的“用户类别”相同。 |

### **表2** 条件组2（“用户等级”为“银牌”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组2 | 基本信息 | 名称 | CG\_Silver |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Condition\_Silver |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Category |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Silver  说明：  “Silver”：表示用户等级为银牌用户。该取值须与用户在UPCF PGW Web LMT上通过**ADD PSUB**命令开户的“用户类别”相同。 |

### **表3** 条件组3（“用户等级”为“普通”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组3 | 基本信息 | 名称 | CG\_Normal |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Condition\_Normal |

### |  |  | 对象属性 | * 对象：Subscriber * 属性：Category |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Normal  说明：  “Normal”：表示用户等级为普通用户。该取值须与用户在UPCF PGW Web LMT上通过**ADD PSUB**命令开户的“用户类别”相同。 |

### 3 配置“5G动作组”。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 此场景配置5G动作组需要考虑流信息、业务流开关、计费控制和带宽调整，则需配置动作：FlowInformation、TrafficControlData、ChargingData和QoSData。相关应用场景如下：

#### 3.1 FlowInformation：当需要下发流信息时需配置此动作。

#### 3.2 TrafficControlData：当需要做门限控制时，配置此动作。在下发流描述时，如果不配默认为放通该流，当需要限制流时，此动作必须配置。

#### 3.3 ChargingData：当需要做计费策略控制时，配置此动作。

#### 3.4 QoSData：当需要进行带宽控制时，配置此动作。

### 根据业务配置逻辑章节介绍的5G场景中QoS Flow的建立方法，此处示例采用“仅使用DynamicPccRule类型动作建立缺省QoS Flow”的方法进行配置。根据整体方案设计步骤可知，该业务场景须建立三条规则，对应了需要配置3个“DynamicPccRule”类型的5G动作组，分别用于在用户等级为金牌用户，用户等级为银牌用户和用户等级为普通用户时动作的下发。详细动作组参数可参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>5G动作组”。

### **表4** 5G动作组之流描述配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_FlowDesc |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### **表5** 5G动作组之流信息配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组2 | 基本信息 | 名称 | AG\_FlowInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：AG\_FlowDesc  说明：  已在表4中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### **表6** 5G动作组之流控制信息配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组3 | 基本信息 | 名称 | AG\_TraCtrl |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG\_TraCtrl |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### **表7** 5G动作组之ARP配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组4 | 基本信息 | 名称 | AG\_arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPriorityLevel  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

### |  |  | preemptCap | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionCap  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

### |  |  | preemptVuln | * 类型：Object Attribute * 值：SmfSession.SubsDefQosPreemptionVuln  说明：  该种配置表明PCF直接取的用户上线请求的ARP进行配置下发。 |

### **表8** 5G动作组之“用户等级”为“金牌”的QoSData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组5 | 基本信息 | 名称 | AG\_Qos\_Gold |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_Qos\_Gold |

### |  |  | 5qi | * 类型：Object Attribute * 值：SmfSession.SubsDefQos5qi 说明：  该种配置表明PCF直接取的用户上线请求的5qi进行配置下发。 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_arp 说明：  已在表7中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：100 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：100 Mbps |

### **表9** 5G动作组之“用户等级”为“银牌”的QoSData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组6 | 基本信息 | 名称 | AG\_Qos\_Silver |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_Qos\_Silver |

### |  |  | 5qi | * 类型：Object Attribute * 值：SmfSession.SubsDefQos5qi 说明：  该种配置表明PCF直接取的用户上线请求的5qi进行配置下发。 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_arp 说明：  已在表7中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：50 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：50 Mbps |

### **表10** 5G动作组之“用户等级”为“普通”的QoSData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组7 | 基本信息 | 名称 | AG\_Qos\_Normal |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_Qos\_Normal |

### |  |  | 5qi | * 类型：Object Attribute * 值：SmfSession.SubsDefQos5qi 说明：  该种配置表明PCF直接取的用户上线请求的5qi进行配置下发。 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_arp 说明：  已在表7中定义。 |

### |  |  | maxbrUl | * 类型：Value * 值：10 Mbps |

### |  |  | maxbrDl | * 类型：Value * 值：10 Mbps |

### **表11** 5G动作组之“用户等级”为“金牌”的ChargingData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组8 | 基本信息 | 名称 | AG\_ChargingData\_Gold |

### |  |  | 类型 | ChargingData |

### |  | 属性 | chgId | * 类型：Value * 值：AG\_ChargingData\_Gold |

### |  |  | meteringMethod | * 类型：Value * 值：VOLUME |

### |  |  | ratingGroup | * 类型：Value * 值：11 |

### |  |  | serviceId | * 类型：Value * 值：11 |

### |  |  | online | * 类型：Value * 值：False |

### |  |  | offline | * 类型：Value * 值：True |

### **表12** 5G动作组之“用户等级”为“银牌”的ChargingData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组9 | 基本信息 | 名称 | AG\_ChargingData\_Silver |

### |  |  | 类型 | ChargingData |

### |  | 属性 | chgId | * 类型：Value * 值：AG\_ChargingData\_Silver |

### |  |  | meteringMethod | * 类型：Value * 值：VOLUME |

### |  |  | ratingGroup | * 类型：Value * 值：22 |

### |  |  | serviceId | * 类型：Value * 值：22 |

### |  |  | online | * 类型：Value * 值：False |

### |  |  | offline | * 类型：Value * 值：True |

### **表13** 5G动作组之“用户等级”为“普通”的ChargingData配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组10 | 基本信息 | 名称 | AG\_ChargingData\_Normal |

### |  |  | 类型 | ChargingData |

### |  | 属性 | chgId | * 类型：Value * 值：AG\_ChargingData\_Normal |

### |  |  | meteringMethod | * 类型：Value * 值：VOLUME |

### |  |  | ratingGroup | * 类型：Value * 值：33 |

### |  |  | serviceId | * 类型：Value * 值：33 |

### |  |  | online | * 类型：Value * 值：False |

### |  |  | offline | * 类型：Value * 值：True |

### **表14** 5G动作组之“用户等级”为“金牌”的DynamicPccRule配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组11 | 基本信息 | 名称 | AG\_Gold |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_Gold |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_FlowInfo 说明：  已在表5中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Gold 说明：  已在表8中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表6中定义。 |

### |  |  | refChgData | * 类型：Reference ActionGroup * 值：AG\_ChargingData\_Gold 说明：  已在表12中定义。 |

### **表15** 5G动作组之“用户等级”为“银牌”的DynamicPccRule配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组12 | 基本信息 | 名称 | AG\_Silver |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_Silver |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_FlowInfo 说明：  已在表5中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Silver 说明：  已在表9中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表6中定义。 |

### |  |  | refChgData | * 类型：Reference ActionGroup * 值：AG\_ChargingData\_Gold 说明：  已在表12中定义。 |

### **表16** 5G动作组之“用户等级”为“普通”的DynamicPccRule配置

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组13 | 基本信息 | 名称 | AG\_Normal |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_Normal |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_FlowInfo 说明：  已在表5中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_Qos\_Normal 说明：  已在表10中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TraCtrl 说明：  已在表6中定义。 |

### |  |  | refChgData | * 类型：Reference ActionGroup * 值：AG\_ChargingData\_Gold 说明：  已在表13中定义。 |

### 4 配置**“规则”**。

### 导航入口为“策略管理 > 策略 > 规则”。

### 规则的数据规划如表17，表18和表19所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>规则”。

### 此场景下规则的配置仅用于关联5G动作和条件组，共配置三个规则，分别对应用户等级为金牌，银牌和普通。

### **表17** 规则（“用户等级”为“金牌”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Rule\_Gold |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Gold  说明：  已在表1中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Gold  说明：  已在表14中定义。 |

### **表18** 规则（“用户等级”为“银牌”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则2 | 基本信息 | 名称 | Rule\_Silver |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Silver  说明：  已在表2中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Silver  说明：  已在表15中定义。 |

### **表19** 规则（“用户等级”为“普通”）

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | Rule\_Normal |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | CG\_Normal  说明：  已在表3中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_Normal  说明：  已在表16中定义。 |

### 5 配置“策略”。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表20所示，详细参数说明请参见“UPCF产品文档>UPCF WebUI GUI参考>策略管理>策略”。

### **表20** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略 | 基本信息 | 名称 | Policy\_Category |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * Rule\_Gold * Rule\_Silver * Rule\_Normal 说明：  已在表17，表18和表19中定义。 |

### 6 配置“业务”。

### 导航入口为“业务管理 > 业务 > 业务”。

### 完成业务配置后，可以配置套餐，即对一组业务进行逻辑组合，统一包装。用户可以订购套餐，订购了套餐即把该套餐下的所有业务都订购，套餐的配置步骤请参见“UPCF产品文档>UPCF WebUI GUI参考>业务管理>套餐”。

### 业务的数据规划如表21所示。

### **表21** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务 | 基本信息 | 名称 | Usr\_Category\_Service |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Policy\_Category  说明：  已在表20中定义。 |

### 7 **开户。**

### **登录“UPCF PGW Web LMT>UPCF 业务管理”窗口**，将配置完成的业务通过UPCF开户签约系统进行下发。

### 执行**ADD PSUB**增加一个金牌用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=7 -->
```

### “USRIDENTIFIER”的参数类型受UPCF软参“VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）”控制，默认为“IMSI”。

### “USRCATEGORY”字段定义了用户类别/等级属性，通过执行**MOD PSUB**修改用户等级为Silver（银牌用户）、Normal（其他用户等级）。

### 8 **业务发放。**

### 在“UPCF PGW Web LMT>UPCF 业务管理”窗口继续执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=8 -->
```

