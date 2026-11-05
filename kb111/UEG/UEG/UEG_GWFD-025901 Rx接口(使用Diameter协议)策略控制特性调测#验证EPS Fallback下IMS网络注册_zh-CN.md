---
id: GWFD-025901
name: 验证EPS Fallback下IMS网络注册
ne_type: UEG
type: feature
description: 用于验证EPS Fallback下IMS网络注册业务，IMS网络注册是NR用户使用IMS网络提供业务的前提，UPCF支持用户在IMS网络注册过程中发起Rx注册会话。Rx注册会话主要应用于IMS Restoration，AF（P-CSCF）单点故障场景。 若AF侧（通过ADD RXPLC命令将“使能信令承载功能”参数设置为“是”）开启用户注册建立Rx会话的开关，则用户在IMS初始注册时AF会向UPCF发送AAR消息并携带P-CSCF地址，UPCF会将AF发送的P-CSCF地址透传给SMF。SMF支持检测P-CSCF故障状态，并在P-CSCF故障时选择正常的P-CSCF完成IMS Restoration。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","PCRF&PCF特性指南","PCF语音基本功能","GWFD-025901 Rx接口(使用Diameter协议)策略控制","GWFD-025901 Rx接口(使用Diameter协议)策略控制特性调测","验证EPS Fallback下IMS网络注册"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用于验证EPS Fallback下IMS网络注册业务，IMS网络注册是NR用户使用IMS网络提供业务的前提，UPCF支持用户在IMS网络注册过程中发起Rx注册会话。Rx注册会话主要应用于IMS Restoration，AF（P-CSCF）单点故障场景。若AF侧（通过ADD RXPLC命令将“使能信令承载功能”参数设置为“是”）开启用户注册建立Rx会话的开关，则用户在IMS初始注册时AF会向UPCF发送AAR消息并携带P-CSCF地址，UPCF会将AF发送的P-CSCF地址透传给SMF。SMF支持检测P-CSCF故障状态，并在P-CSCF故障时选择正常的P-CSCF完成IMS Restoration。

## 必备事项
前提条件

* 已完成EPS FB IMS网络注册的业务配置，业务名称为“ EPS\_Signalling\_Service”。具体的配置方法参见配置EPS Fallback下IMS网络注册。
* 已为业务“ EPS\_Signalling\_Service”配置应用业务映射，应用标识为“IMS\_Signalling”。
* 用户A未在UPCF中开户。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在OM Portal界面上创建“用户消息跟踪”任务。

#### 1.1 选择“监控分析 > 消息跟踪 > 用户跟踪 > PCF用户跟踪”。

#### 1.2 单击“用户消息跟踪”，在“用户消息跟踪”任务对话框点击“创建跟踪任务”。

#### 1.3 填写“任务名称”、“跟踪时长”和用户的“用户标识”，并选中“N7”和“Rx”接口。

#### 1.4 单击“确认”。

### 2 用户成功附着5GC网络后通过UE向AF发送REGISTER消息，请求IMS网络注册，通过OM Portal消息跟踪结果查看AF向UPCF请求携带的媒体流信息。如表1所示。

### **表1** 注册Rx请求消息验证结果

### | 消息名称 | 验证信息 | 预期结果 |

### | --- | --- | --- |

### | AAR | 媒体部件编码 | Media-Component-Number AVP取值为“0”。 |

### |  | 媒体流的使用方式 | * Flow-Usage AVP取值为“AF\_SIGNALLING(2)”。 * Flow-Description AVP携带流信息（包含AF地址）。 |

### |  | 应用标识 | AF-Application-Identifier AVP取值为“IMS\_Signalling”。 |

### 3 UPCF收到AF发起的Rx注册请求后，进行策略计算，向SMF发起Npcf\_SMPolicyControl\_UpdateNotify请求消息。

### **表2** 注册Rx消息触发的N7会话更新验证结果

### | 消息名称 | 验证信息 | 预期结果 |

### | --- | --- | --- |

### | Npcf\_SMPolicyControl\_UpdateNotify请求 | 5qi和arp | qosDecs下的“5qi”取值为“5”，“arp”取值为“2”。 |

### |  | 流信息 | flowInfos下的flowDescription中携带取值与AAR消息中取值相同。 |

### 4 UPCF处理注册Rx会话成功后，会向AF返回AAA响应消息携带用户接入网络类型。如表3所示。

### **表3** 注册Rx响应消息验证结果

### | 消息名称 | 验证信息 | 预期结果 |

### | --- | --- | --- |

### | AAA | 用户接入网络类型 | * IP-CAN-Type AVP携带取值为“3GPP-5GS”。 * RAT-Type AVP携带取值为“NR”。 |

