---
id: ''
name: 基于业务路由的策略控制
ne_type: UEG
type: feature
description: N5接口位于AF（Application Function）与PCF（Policy Control Function）功能实体之间，用于传递用户应用会话请求，包括特定QoS请求、业务路由、Sponsored业务请求。  用户上线，SMF建立缺省QoS Flow后，若AF向UPCF发起业务路由请求消息，UPCF根据AF发送的用户IP进行N7与N5会话绑定，并根据应用标识和业务路由请求进行策略计算，向SMF下发指定的策略。如表1所示场景根据应用标识下发业务路由策略。  **表1** 根据应用标识下发策略  | 应用标识 | UPCF业务 | 策略控制 | | --- | --- | --- | | AFapp02 | AF\_RoutReq | 业务路由 |
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UPCF特性指南","基于业务路由的策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
N5接口位于AF（Application Function）与PCF（Policy Control Function）功能实体之间，用于传递用户应用会话请求，包括特定QoS请求、业务路由、Sponsored业务请求。用户上线，SMF建立缺省QoS Flow后，若AF向UPCF发起业务路由请求消息，UPCF根据AF发送的用户IP进行N7与N5会话绑定，并根据应用标识和业务路由请求进行策略计算，向SMF下发指定的策略。如表1所示场景根据应用标识下发业务路由策略。**表1** 根据应用标识下发策略| 应用标识 | UPCF业务 | 策略控制 || --- | --- | --- || AFapp02 | AF\_RoutReq | 业务路由 |

## 必备事项
前提条件

前提条件

* 操作员已了解**WHFD-611081 N5接口（使用HTTP协议）策略控制**特性概述，且通过**4G/5G业务配置差异介绍**已经了解5G规则配置原理。
* 操作已完成**配置UPCF与NRF的对接数据**。

**AF侧激活的业务配置逻辑**

AF侧激活的业务下动作“类型”需配置为“DynamicPccRuleIMS”，配置逻辑仅针对AF侧激活的业务，该业务配置场景中涉及PCEF侧激活的业务配置逻辑直接参见**WHFD-601042 N7接口（使用HTTP协议）策略控制**特性配置。

**图1** **AF侧激活的业务配置逻辑**  

图中“必须配置的动作类型”也仅是针对当前场景而言，其他不同场景须参考对应的配置逻辑。
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
      SRVNAME: Def_Service
      SRVUSAGESTATE: Normal
      SRVROAMINGTYPE: 'NULL'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录UPCF Web UI界面。

### 2 配置条件组。

### 导航入口为“策略管理 > 策略 > 条件组”。

#### 2.1 当业务的使用需要设置控制条件时，需要配置条件组。若某规则不配置条件组，表示在同一业务里其他条件都匹配不上时，才触发此规则。

#### 2.2 条件组是一个或多个条件的组合。条件组中的各条件之间可以是“与”的关系，也可以是“或”的关系。条件之间的与/或关系由参数“关系”的取值决定。

### 需要配置2个条件组，分别用于用户上线和使用应用的媒体类型。条件组的数据规划如表3所示。

### **表3** 条件组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 条件组1 | 基本信息 | 名称 | Def\_CG |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | Def\_C |

### |  |  | 对象属性 | * 对象：SmfSession * 属性：RatType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | NR  说明：  “NR”：表示用户从5G网络接入。 |

### | 条件组2 | 基本信息 | 名称 | AFApp\_CG |

### |  |  | 关系 | AND |

### |  | 条件 | 名称 | AFApp\_C |

### |  |  | 对象属性 | * 对象：AfSession * 属性：MediaType |

### |  |  | 操作符 | Equal |

### |  |  | 右值类型 | Value |

### |  |  | 右值 | Application  说明：  表示媒体类型为应用。 |

### 3 配置5G动作组。

### 导航入口为“策略管理 > 策略 > 5G动作组”。

### 此场景需配置5G动作：Ambr、Arp、DefaultQosInformation、SessionRuleAction、FlowDescription、FlowInformation、QoSData、TrafficControlData、RouteToLocation、UpPathChgEvent、RouteInformation、DynamicPccRule和DynamicPccRuleIMS。其中：

#### 3.1 PCC规则类型动作：

##### 3.1.1 DynamicPccRule：用于默认QoS Flow的建立。

##### 3.1.2 DynamicPccRuleIMS：用于AF请求场景需要配置此动作。

#### 3.2 业务路由相关动作：

##### 3.2.1 RouteInformation：业务路由的信息

##### 3.2.2 RouteToLocation：业务路由的策略方法

##### 3.2.3 UpPathChgEvent：AF订阅的用户面路径管理事件通知

#### 3.3 AF请求保障带宽相关动作：

##### 3.3.1 QoSData：当需要进行带宽控制时均需配置此动作，若不配置则表示不限制Qos。

##### 3.3.2 TrafficControlData：当需要做门限控制时，配置此动作。在下发流描述时，如果不配默认为放通该流，当需要限制流时，此动作必须配置。此场景根据AF请求的FlowStatus，下发门限策略。

### 5G动作组的数据规划如表4所示。

### **表4** 5G动作组

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 5G动作组1 | 基本信息 | 名称 | AG\_FlowDesc |

### |  |  | 类型 | FlowDescription |

### |  | 属性 | action | * 类型：Value * 值：PERMIT |

### |  |  | direction | * 类型：Value * 值：OUT |

### |  |  | protocol | * 类型：Value * 值：ANY |

### |  |  | sourceIP | * 类型：Value * 值：any |

### |  |  | destinationIP | * 类型：Value * 值：any |

### | 5G动作组2 | 基本信息 | 名称 | AG\_FlowInfo |

### |  |  | 类型 | FlowInformation |

### |  | 属性 | flowDescription | * 类型：Reference ActionGroup * 值：AG\_FlowDesc 说明：  已在5G动作组中定义。 |

### |  |  | flowDirection | * 类型：Value * 值：BIDIRECTIONAL |

### | 5G动作组3 | 基本信息 | 名称 | AG\_Arp |

### |  |  | 类型 | Arp |

### |  | 属性 | priorityLevel | * 类型：Value * 值：1 |

### |  |  | preemptCap | * 类型：Value * 值：NOT\_PREEMPT |

### |  |  | preemptVuln | * 类型：Value * 值：NOT\_PREEMPTABLE |

### | 5G动作组4 | 基本信息 | 名称 | AG\_Ambr |

### |  |  | 类型 | Ambr |

### |  | 属性 | uplink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | downlink | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组5 | 基本信息 | 名称 | AG\_DefQos |

### |  |  | 类型 | DefaultQosInformation |

### |  | 属性 | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Arp 说明：  已在5G动作组中定义。 |

### | 5G动作组6 | 基本信息 | 名称 | AG\_SessRule |

### |  |  | 类型 | SessionRuleAction |

### |  | 属性 | sessRuleId | * 类型：Value * 值：AG\_Sess |

### |  |  | authSessAmbr | * 类型：Reference ActionGroup * 值：AG\_Ambr 说明：  已在5G动作组中定义。 |

### |  |  | authDefQos | * 类型：Reference ActionGroup * 值：AG\_DefQos 说明：  已在5G动作组中定义。 |

### | 5G动作组7 | 基本信息 | 名称 | AG\_TrafficCtrl |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：AG\_TrafficCtrl |

### |  |  | flowStatus | * 类型：Value * 值：ENABLED |

### | 5G动作组8 | 基本信息 | 名称 | AG\_QosData |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：AG\_QosData |

### |  |  | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | maxbrUl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrUplink |

### |  |  | maxbrDl | * 类型：Object Attribute * 值：SmfSession.SubsSessAmbrDownlink |

### | 5G动作组9 | 基本信息 | 名称 | AG\_PccRule |

### |  |  | 类型 | DynamicPccRule |

### |  | 属性 | pccRuleId | * 类型：Value * 值：AG\_PccRule |

### |  |  | flowInfos | * 类型：Reference ActionGroup * 值：AG\_FlowInfo 说明：  已在5G动作组中定义。 |

### |  |  | precedence | * 类型：Value * 值：1 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：AG\_QosData 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：AG\_TrafficCtrl 说明：  已在5G动作组中定义。 |

### | 5G动作组10 | 基本信息 | 名称 | N5\_QosData2 |

### |  |  | 类型 | QoSData |

### |  | 属性 | qosId | * 类型：Value * 值：N5\_Qos2 |

### |  |  | 5qi | * 类型：Value * 值：9 |

### |  |  | arp | * 类型：Reference ActionGroup * 值：AG\_Arp 说明：  已在5G动作组中定义。 |

### |  |  | defQosFlowIndication | * 类型：Value * 值：True 说明：  用于将AF请求的媒体流直接绑定到默认QoS Flow上。 |

### | 5G动作组11 | 基本信息 | 名称 | N5\_UpPath |

### |  |  | 类型 | UpPathChgEvent |

### |  | 属性 | dnaiChgType | * 类型：Object Attribute * 值：AfSession.PathChangeDnaiType |

### |  |  | notificationUri | * 类型：Object Attribute * 值：AfSession.PathChangeNotificationUri |

### |  |  | notifCorreId | * 类型：Object Attribute * 值：AfSession.PathChangeNotificationCorreId |

### | 5G动作组12 | 基本信息 | 名称 | N5\_RouteInfo |

### |  |  | 类型 | RouteInformation |

### |  | 属性 | portNumber | * 类型：Object Attribute * 值：AfSession.RoutePort |

### |  |  | ipv4Addr | * 类型：Object Attribute * 值：AfSession.RouteIpv4Address |

### |  |  | ipv6Addr | * 类型：Object Attribute * 值：AfSession.RouteIpv4Address |

### | 5G动作组13 | 基本信息 | 名称 | N5\_RouteLoc |

### |  |  | 类型 | RouteToLocation |

### |  | 属性 | dnai | * 类型：Object Attribute * 值：AfSession.RouteDnai |

### |  |  | routeInfo | * 类型：Reference ActionGroup * 值：N5\_RouteInfo 说明：  已在5G动作组中定义。 |

### |  |  | routeProfId | * 类型：Object Attribute * 值：AfSession.RouteProfId |

### | 5G动作组14 | 基本信息 | 名称 | N5\_TrafficCtrl2 |

### |  |  | 类型 | TrafficControlData |

### |  | 属性 | tcId | * 类型：Value * 值：N5\_tcId2 |

### |  |  | flowStatus | * 类型：Object Attribute * 值：AfSession.FlowStatus |

### |  |  | routeToLocs | * 类型：Reference ActionGroup * 值：N5\_RouteLoc 说明：  已在5G动作组中定义。 |

### |  |  | upPathChgEvent | * 类型：Reference ActionGroup * 值：N5\_UpPath 说明：  已在5G动作组中定义。 |

### | 5G动作组15 | 基本信息 | 名称 | N5\_PccRule2 |

### |  |  | 类型 | DynamicPccRuleIMS |

### |  | 属性 | pccRuleId | * 类型：Value * 值：N5\_Pcc2 |

### |  |  | refQosData | * 类型：Reference ActionGroup * 值：N5\_QosData2 说明：  已在5G动作组中定义。 |

### |  |  | refTcData | * 类型：Reference ActionGroup * 值：N5\_TrafficCtrl2 说明：  已在5G动作组中定义。 |

### 4 配置规则

### 导航入口为“策略管理 > 策略 > 规则”。

### AF触发规则激活场景，规则的“类型”需要配置为“5G Smf Pcc Rule for IMS”。

### 规则的数据规划如表5所示。

### **表5** 规则

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 规则1 | 基本信息 | 名称 | R\_SessNorm |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Session Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Def\_CG  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_SessRule  说明：  已在5G动作组中定义。 |

### | 规则2 | 基本信息 | 名称 | R\_PccNorm |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | Def\_CG  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | AG\_PccRule  说明：  已在5G动作组中定义。 |

### | 规则3 | 基本信息 | 名称 | R\_N5Pcc2 |

### |  |  | 操作类型 | Change Rule |

### |  |  | 类型 | 5G Smf Pcc Rule for IMS |

### |  | 条件组 | 关系 | AND  说明：  当规则中只有一个条件组时，“关系”可设置为任意值。 |

### |  |  | 条件组 | AFApp\_CG  说明：  已在条件组中定义。 |

### |  | 5G动作组 | 5G动作组 | N5\_PccRule2  说明：  已在5G动作组中定义。 |

### 5 配置策略。

### 导航入口为“策略管理 > 策略 > 策略”。

### 策略的数据规划如表6所示。

### **表6** 策略

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 策略1 | 基本信息 | 名称 | Def\_Policy |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | IPCAN\_EST |

### |  | 规则 | 名称 | * R\_SessNorm * R\_PccNorm 说明：  已在规则中定义。 |

### | 策略2 | 基本信息 | 名称 | N5\_Policy2 |

### |  |  | 策略类型 | N7 Policy |

### |  | 触发器 | 名称 | AFSessionAuthorization |

### |  | 规则 | 名称 | R\_N5Pcc2  说明：  已在规则中定义。 |

### 6 配置业务。

### 导航入口为“业务管理 > 业务 > 业务”。

### 业务的数据规划如表7所示。

### **表7** 业务

### | 类别 | 参数 |  | 取值样例 |

### | --- | --- | --- | --- |

### | 业务1 | 基本信息 | 名称 | Def\_Service |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | PCEF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 是 |

### |  | 策略 | 名称 | Def\_Policy  说明：  已在策略中定义。 |

### | 业务2 | 基本信息 | 名称 | AF\_RoutReq |

### |  |  | 类型 | VALUE\_ADDED\_SERVICE |

### |  |  | 是否记入基本配额 | 是 |

### |  |  | 激活方式 | AF |

### |  |  | 优先级 | 0  说明：  运营商统一规划，用于设置该业务在互斥组中的优先级。当此业务不需配置相关互斥组时，此值可任意取值。 |

### |  |  | QoS模式 | 替换 |

### |  |  | 签约后才能使用 | 否  说明：  若业务“激活方式”为“AF”，但用户没有订购该业务，则需要将业务的参数“签约后才能使用”设置为“否”。 |

### |  | 策略 | 名称 | N5\_Policy2  说明：  已在策略中定义。 |

### 7 配置应用业务映射。

### 导航入口为“业务管理 > 业务 > 应用业务映射”。

### 配置AF激活的业务时，必须配置应用业务映射。其中，“应用标识”必须和AF侧协商一致；“业务”为6中已定义的业务。

### 应用业务映射的数据规划如表8所示。

### **表8** 应用业务映射

### | 类别 | 参数 | 取值样例 |

### | --- | --- | --- |

### | 应用业务映射 | 应用标识 | AFapp02  说明：  和AF中定义的应用标识协商一致。 |

### |  | 业务 | AF\_RoutReq  说明：  已在业务中定义的由AF激活的业务。 |

### 8 登录“UPCF 业务管理”窗口。

### 9 发放业务。

#### 9.1 执行**ADD PSUB**增加一个用户。

#### “USRIDENTIFIER”的参数类型受软参VRM\_SUBSRCIPTIONIDTYPE（系统支持的用户类型）控制，默认为“IMSI”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psub_list的变量区（command: ADD PSUB） -#}
<!-- MISSING_MACRO: command=ADD PSUB list_name=add_psub_list step_id=9.1 -->
```

#### 9.2 执行**ADD PSRV**给用户签约业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_psrv_list的变量区（command: ADD PSRV） -#}
<!-- MISSING_MACRO: command=ADD PSRV list_name=add_psrv_list step_id=9.2 -->
```

