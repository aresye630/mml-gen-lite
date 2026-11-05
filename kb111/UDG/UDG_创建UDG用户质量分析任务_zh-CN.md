---
id: ''
name: 创建UDG用户质量分析任务
ne_type: UDG
type: feature
description: '设备跟踪中能够显示消息，不代表跟踪到的消息一定从本设备向外发送成功，请关注系统其他异常告警和性能统计。  * 提供针对大带宽用户的TCP、QUIC业务流量分析手段，用来定位TCP、QUIC业务数传问题。 * 维护人员调试设备运行情况。  * 适用于SGW-U、PGW-U、UPF。 * 质量分析功能主要用于保障网络运营和服务、检测通信传输中的故障和错误，该功能涉及使用或存储个人用户标识和用户通信内容。建议您只有在所适用法律法规允许的目的和范围内方可启用相应的功能。在使用、存储用户通信内容的过程中，您应采取足够的措施以确保用户的通信内容受到严格保护。 * 操作员在现场使用跟踪功能时，消息跟踪中的IMSI、MSISDN、IMEI、IP地址信息仍然是用户的真实信息，是未被加密的。跟踪信息将自动保存到“跟踪管理文件”中。保存到“跟踪管理文件”中的用户IMSI、MSISDN、IMEI、IP地址将被OM Portal做匿名化处理（即被加密）。IMSI字段标准定义由0-9的数字组成，匿名化后可能出现A-F字母。 * 业务POD复位可能造成跟踪任务丢失，请在复位后检查跟踪任务是否存在，如果不存在，请重新创建。 * 业务POD复位可能造成OM Portal断连，请在复位后检查OM Portal是否断连。如果是，请重新登录OM Portal，并重新创建跟踪任务。 * 当DPE线程CPU占用率超过80%时，会停止EMS-TCPSTATIC/EMS-QUICSTATIC/EMS-GTPUSTATIC跟踪处理。 * 当软参BIT2548设置为0，并且平台启用了跟踪流控功能（可通过命令LST MTSCFG: TYPE=FLOW\_CONTROL\_SWITCH, MEID=0查询是否开启），同时CPU使用率超过80%，系统将暂停上报跟踪信息。一旦CPU使用率降至70%以下，或者跟踪流控开关被关闭，跟踪信息将恢复常态上报。'
risk_level: ''
doc_source: ["网络运维","日常维护","UDG基础运维操作","创建消息跟踪","创建用户跟踪","创建UDG用户质量分析任务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
设备跟踪中能够显示消息，不代表跟踪到的消息一定从本设备向外发送成功，请关注系统其他异常告警和性能统计。* 提供针对大带宽用户的TCP、QUIC业务流量分析手段，用来定位TCP、QUIC业务数传问题。* 维护人员调试设备运行情况。* 适用于SGW-U、PGW-U、UPF。* 质量分析功能主要用于保障网络运营和服务、检测通信传输中的故障和错误，该功能涉及使用或存储个人用户标识和用户通信内容。建议您只有在所适用法律法规允许的目的和范围内方可启用相应的功能。在使用、存储用户通信内容的过程中，您应采取足够的措施以确保用户的通信内容受到严格保护。* 操作员在现场使用跟踪功能时，消息跟踪中的IMSI、MSISDN、IMEI、IP地址信息仍然是用户的真实信息，是未被加密的。跟踪信息将自动保存到“跟踪管理文件”中。保存到“跟踪管理文件”中的用户IMSI、MSISDN、IMEI、IP地址将被OM Portal做匿名化处理（即被加密）。IMSI字段标准定义由0-9的数字组成，匿名化后可能出现A-F字母。* 业务POD复位可能造成跟踪任务丢失，请在复位后检查跟踪任务是否存在，如果不存在，请重新创建。* 业务POD复位可能造成OM Portal断连，请在复位后检查OM Portal是否断连。如果是，请重新登录OM Portal，并重新创建跟踪任务。* 当DPE线程CPU占用率超过80%时，会停止EMS-TCPSTATIC/EMS-QUICSTATIC/EMS-GTPUSTATIC跟踪处理。* 当软参BIT2548设置为0，并且平台启用了跟踪流控功能（可通过命令LST MTSCFG: TYPE=FLOW\_CONTROL\_SWITCH, MEID=0查询是否开启），同时CPU使用率超过80%，系统将暂停上报跟踪信息。一旦CPU使用率降至70%以下，或者跟踪流控开关被关闭，跟踪信息将恢复常态上报。

## 必备事项
前提条件

* 具备管理员权限的操作员已经登录OM Portal。
* 维护人员具有用户消息跟踪权限。
* 有用户业务激活。
* 在U2020/MAE上配置了匿名化开关和密钥。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在OM Portal界面的“监控分析”页签中，单击“消息跟踪”按钮，单击“UDG”>“用户跟踪”>“用户质量分析”，单击“创建跟踪任务”。弹出“用户质量分析”对话框，如图1所示。

### **图1** “用户质量分析”参数配置对话框

### 2 在对话框中进行参数配置，参数说明如表1所示。

### 用户质量分析跟踪与用户跟踪任务中的**EMS TCPSTATIC**/**EMS QUICSTATIC/EMS GTPUSTATIC****/EMS ICMPSTATIC**质量分析上报功能，同一用户数据可同时上报，不同用户数据只能上报到对应用户的第一个跟踪任务窗口。

### **EMS TCPSTATIC**/**EMS QUICSTATIC/EMS GTPUSTATIC****/EMS ICMPSTATIC**业务质量同时分析时需在第一个任务中同时使能**。**

### 下发质量分析跟踪任务时，如果使能GTPU序列号分析消息（**EMS GTPUSTATIC**），最多可以下发8个跟踪任务；如果使能ICMP分析消息（**EMS ICMPSTATIC**），最多可以下发16个跟踪任务；如果使能业务质量分析消息（**EMS TCPSTATIC**），最多可下发4个跟踪任务，如果使能业务质量分析消息（**EMS QUICSTATIC**），最多可下发1个跟踪任务。

### **表1** 用户质量分析参数配置说明

### | 字段名 | 说明 |

### | --- | --- |

### | 选择参数 | 取值为IMSI、MSISDN、IMEI。  * IMSI：表示按照IMSI号段跟踪消息，1～15位字符。 * MSISDN：表示按照MSISDN号段跟踪消息，1～15位字符。 说明：  MSISDN号段跟踪需要输入不含编码指示的字符。 * IMEI：表示按照IMEI号段跟踪消息，1～16位字符。 说明：  终端的IMEI和IMEISV中前14位是固定的，第15位和16位在不同的使用方法下有不同的取值，所以系统内部只使用前14位标识用户。 |

### | IMSI | 当“用户标识选项”值为“IMSI”时，该参数会显示，表示需跟踪的IMSI号段。 |

### | MSISDN | 当“用户标识选项”值为“MSISDN”时，该参数会显示，表示需跟踪的MSISDN号段。 |

### | IMEI | 当“用户标识选项”值为“IMEI”时，该参数会显示，表示需跟踪的IMEI号段。 |

### | EMS统计上报周期(秒) | 当“用户标识选项”值为“IMSI”/“MSISDN”/“IMEI”时，该参数会显示，表示"EMS TCPSTATIC"、"EMS QUICSTATIC"、"EMS GTPUSTATIC"的上报周期。取值范围：1～60秒，默认值为20秒。 |

### | 消息类型 | * **EMS** **TCPSTATIC**：TCP业务质量分析消息。 * **EMS QUICSTATIC**：QUIC业务质量分析消息。 * **EMS GTPUSTATIC**：用于N3/S1-U/SA链路丢包和乱序情况分析。前提条件：需要先使能RAN侧的Sequence染色功能。 * **EMS ICMPSTATIC**：ping报文质量分析消息。 说明：  当同一用户开启多个包含EMS TCPSTATIC的质量分析跟踪任务时，仅支持上报到该用户第一个建立的跟踪任务窗口。当需要对多种业务进行分析时，请在第一个跟踪任务中勾选该业务对应的全部消息类型。例如：如果需要对单用户的TCP和GTPU业务同时进行分析，请在该用户的第一个跟踪任务中同时勾选EMS TCPSTATIC和EMS GTPUSTATIC消息。  使能EMS GTPUSTATIC功能后，会修改外发N3/S1-U/SA链路的GTP报文，增加SN字段。  **EMS QUICSTATIC**仅支持分析GQUIC协议Q27版本及后续版本。 |

### | 任务名称 | 该参数表示任务名称的自定义部分，用于用户区分和查找不同的跟踪任务。 说明：  * 任务名命名方式：“自定义任务名\_年月日\_时分秒毫秒\_任务序列号”，如“test2\_20170116\_154201632\_0”。自定义任务名仅支持数字，字母和下划线。 * 默认情况下，依据跟踪类型、跟踪开始日期及时间（含夏令时标志）和当前跟踪任务的序列号作为跟踪任务的名称。 |

### 3 单击“确认”，启动跟踪任务。

### 跟踪任务启动后，双击跟踪到的数据会显示用户质量分析的内容，各字段解释如下。

### **表2** 用户TCP业务质量分析内容解释

### | 字段名 | 说明 |

### | --- | --- |

### | msip | 用户的IP地址。 |

### | serverip | 服务器的IP地址。 |

### | msPort | 用户端口。 |

### | serverPort | 服务器端口。 |

### | teidc | 用户teidc。 |

### | creatDirFlag | 流表触发创建标记，0：上行触发；1：下行触发。 |

### | useState | 流表老化标记，0：未使用态；1：已经老化回收； 2：使用态。 |

### | tcpConnectionStatus | TCP建链状态 0： 无效状态 ；1：收到SYN； 2： 已收到SYN ACK报文； 3：已收到ACK报文，完成三次握手。 |

### | startTime | 流表创建时间。 |

### | lastTime | 最后一次收到报文的时间。 |

### | onlineTime | 流的在线时长。 |

### | ueToCNRTT | RAN侧建链时延，无效值：65535。 |

### | cnToServerRTT | SP侧建链时延，无效值：65535。 |

### | msMss | RAN侧MSS。 |

### | serverMss | SP侧MSS。 |

### | msSackFlag | RAN侧接收方是否会通知发送方哪些数据块丢失的标记位，1：是，0：否。 |

### | serverSackFlag | SP侧接收方是否会通知发送方哪些数据块丢失的标记位，1：是，0：否。 |

### | msWinScale | RAN侧窗口扩大因子选项。 |

### | serverWinScale | SP侧窗口扩大因子选项。 |

### | msWinSize | RAN侧窗口大小。 |

### | serverWinSize | 服务侧窗口大小。 |

### | upRanDiscardPktNum | 上行RAN侧丢包数。 |

### | ranDiscardseqInfo | 上行RAN侧丢包报文的seq。 |

### | upSPDiscardPktNum | 上行SP侧丢包数。 |

### | upSPDiscardseqInfo | 上行SP侧丢包报文的seq。 |

### | upRanSlowDisorderPktNum | 上行RAN侧比正常报文晚到导致乱序的报文数。 |

### | upRanFastDisorderPktNum | 上行RAN侧比正常报文早到导致乱序的报文数。 |

### | dnRanDiscardPktNum | 下行RAN侧丢包数。 |

### | ranDiscardseqInfo | 下行RAN侧丢包报文的seq。 |

### | dnSPDiscardPktNum | 下行SP侧丢包数。 |

### | spDiscardseqInfo | 下行SP侧丢包报文的seq。 |

### | dnSPSlowDisorderPktNum | 下行SP侧比正常报文晚到导致乱序的报文数。 |

### | dnSPFastDisorderPktNum | 下行SP侧比正常报文早到导致乱序的报文数。 |

### | ranAverageRtt | RAN侧的平均RTT时延(ms)。 |

### | spAverageRtt | SP侧的平均RTT时延(ms)。 |

### | ranMoreThan5sNoAckPktNum | RAN侧超过5秒没有收到ack的报文数 |

### | spMoreThan5sNoAckPktNum | SP侧超过5秒没有收到ack的报文数 |

### | upInPktNum | 上行入口包数。 |

### | upOutPktNum | 上行出口包数。 |

### | dnInPktNum | 下行入口包数。 |

### | dnOutPktNum | 下行出口包数。 |

### | upInFlowByte | 上行入口流量字节数。 |

### | dnInFlowByte | 下行入口流量字节数。 |

### | upOutFlowByte | 上行出口流量字节数。 |

### | dnOutFlowByte | 下行出口流量字节数。 |

### | upAvgPktLength | 上行入口数据报文流量平均包长。 |

### | dnAvgPktLength | 下行入口数据报文流量平均包长。 |

### | upInIpFragPktNum | 上行IP分片入口包数。 |

### | upOutIpFragPktNum | 上行IP分片出口包数。 |

### | dnInIpFragPktNum | 下行IP分片入口包数。 |

### | dnOutIpFragPktNum | 下行IP分片出口包数。 |

### | upFirstIpFragNum | 上行入口IP分片首包数。 |

### | dnFirstIpFragNum | 下行入口IP分片首包数。 |

### | upInDisorderPkt | 报文上行入口乱序统计。 |

### | upInDisorderPktSeq | 上行乱序报文的seq。 |

### | upOutDisorderPkt | 报文上行出口乱序统计。 |

### | DnInDisorderPkt | 报文下行入口乱序统计。 |

### | dnInDisorderPktSeq | 下行乱序报文的seq。 |

### | dnOutDisorderPkt | 报文下行出口乱序统计。 |

### | maxUpPktDelay | 上行报文处理最大时延(ms)。 |

### | maxDnPktDelay | 下行报文处理最大时延(ms)。 |

### | upPktAvgDelay | 上行报文处理平均时延(ms)。 |

### | dnPktAvgDelay | 下行报文处理平均时延(ms)。 |

### | teidu | 用户teidu。 |

### | dpeRateMax | 线程负载率统计。 |

### | msRecvWnScale | MS侧是否支持窗口扩大选项，默认值为1。 |

### | msRecvWnZeroNum | 数据业务报文在MS侧的接受窗口大小为零的次数。 |

### | msRecvWnZeroPktSeq | 数据业务报文在MS侧的接受窗口大小为零的seq。 |

### | msRecvWnMax | 数据业务报文在MS侧的接受窗口的最大值。 |

### | msSendNum | 数据业务报文在MS侧的接受窗口的统计个数。 |

### | msRecvWnTotal | 数据业务报文在MS侧的接受窗口大小的累加值。 |

### | msRecvWnAvg | 数据业务报文在MS侧的接受窗口大小的平均值。 |

### | spRecvWnScale | SP侧是否支持窗口扩大选项，默认值为1。 |

### | spRecvWnZeroNum | 数据业务报文在SP侧的接受窗口大小为零的次数。 |

### | spRecvWnZeroPktSeq | 数据业务报文在SP侧的接受窗口大小为零的seq。 |

### | spRecvWnMax | 数据业务报文在SP侧的接受窗口的最大值。 |

### | spSendNum | 数据业务报文在SP侧的接受窗口的统计个数。 |

### | spRecvWnTotal | 数据业务报文在SP侧的接受窗口大小的累加值。 |

### | spRecvWnAvg | 数据业务报文在SP侧的接受窗口大小的平均值。 |

### | upLastAckNumber | 上行方向时间上最新的Ack序号。 |

### | dnLastAckNumber | 下行方向时间上最新的Ack序号。 |

### | upByteInFlightMax | 上行已发送但未被确认的字节数的最大值。 |

### | dnByteInFlightMax | 下行已发送但未被确认的字节数的最大值。 |

### | upDupAckOne | 上行至少被重复发送一次的报文数目。 |

### | upDupAckMax | 上行被重复发送的最大值。 |

### | upDupAckAll | 上行累计被重复发送的报文数目。 |

### | dnDupAckOne | 下行至少被重复发送一次的报文数目。 |

### | dnDupAckMax | 下行被重复发送的最大值。 |

### | dnDupAckAll | 下行累计被重复发送的报文数目。 |

### | upInNotAckAveragePktByte | 非纯ack上行入口平均包长。 |

### | dnInNotAckAveragePktByte | 非纯ack下行入口平均包长。 |

### | upOutNotAckAveragePktByte | 非纯ack上行出口平均包长。 |

### | dnOutNotAckAveragePktByte | 非纯ack下行出口平均包长。 |

### | upBurstPktNum | 上行最大突发包数。 |

### | dnBurstPktNum | 下行最大突发包数。 |

### | upBurstPktByte | 上行最大突发包字节数。 |

### | dnBurstPktByte | 下行最大突发包字节数。 |

### | ranMaxJitter | 上行最大抖动。 |

### | spMaxJitter | 下行最大抖动。 |

### | ranSumJitter | 上行抖动和。 |

### | spSumJitter | 下行抖动和。 |

### | ranAvgJitter | 上行平均抖动。 |

### | spAvgJitter | 下行平均抖动。 |

### | upRetranPktNum | 上行重传包数。 |

### | upRetranseqInfo | 上行重传报文的seq。 |

### | dnRetranPktNum | 下行重传包数。 |

### | dnRetranseqInfo | 下行重传报文的seq。 |

### | upRetranAverageDelay | 上行平均重传时延(ns)。 |

### | upRetranMaxDelay | 上行最大重传时延(ns)。 |

### | dnRetranAverageDelay | 下行平均重传时延(ns)。 |

### | dnRetranMaxDelay | 下行最大重传时延(ns)。 |

### | relayServiceFlag | 媒体业务流标识。1：是，0：否。 |

### | upPktAvgKbps | 上行报文出口平均速率(kbps)。 |

### | dnPktAvgKbps | 下行报文出口平均速率(kbps)。 |

### **表3** 用户QUIC业务质量分析内容解释

### | 字段名 | 说明 |

### | --- | --- |

### | msip | 用户的IP地址。 |

### | serverip | 服务器的IP地址。 |

### | msPort | 用户端口。 |

### | serverPort | 服务器端口。 |

### | imsi | 用户imsi。 |

### | imei | 用户imei。 |

### | msisdn | 用户msisdn。 |

### | creatDirFlag | 流表触发创建标记，0：上行触发；1：下行触发。 |

### | useState | 流表老化标记，0：未使用态；1：已经老化回收； 2：使用态。 |

### | teidu | 用户teidu。 |

### | ulConnectionID | 用户上行流ConnectionID |

### | dlConnectionID | 用户下行流ConnectionID |

### | startTime | 流表创建时间。 |

### | lastTime | 最后一次收到报文的时间。 |

### | onlineTime | 流的在线时长。 |

### | ulInPkt | 上行入口包数。 |

### | ulOutPkt | 上行出口包数。 |

### | dlInPkt | 下行入口包数。 |

### | dlOutPkt | 下行出口包数。 |

### | ulInBytes | 上行入口流量字节数。 |

### | ulOutBytes | 上行出口流量字节数。 |

### | dlInBytes | 下行入口流量字节数。 |

### | dlOutBytes | 下行出口流量字节数。 |

### | upAvgPktLength | 上行入口流量平均包长。 |

### | dnAvgPktLength | 下行入口流量平均包长。 |

### | ulInIpFragPkt | 上行IP分片入口包数。 |

### | ulOutIpFragPkt | 上行IP分片出口包数。 |

### | dlInIpFragPkt | 下行IP分片入口包数。 |

### | dlOutIpFragPkt | 下行IP分片出口包数。 |

### | ulInIpFragFirstPkt | 上行入口IP分片首包数。 |

### | dlInIpFragFirstPkt | 下行入口IP分片首包数。 |

### | ulAvgInnerDelay | 上行报文处理平均时延。 |

### | dlAvgInnerDelay | 下行报文处理平均时延。 |

### | ulMaxInnerDelay | 上行报文处理最大时延。 |

### | dlMaxInnerDelay | 下行报文处理最大时延。 |

### | ulRanDiscardPkt | 报文上行无线侧丢包统计。 |

### | dlSPDiscardPkt | 报文下行网络侧丢包统计。 |

### | ulRanDisorderPkt | 报文上行无线侧乱序统计。 |

### | dlSPDisorderPkt | 报文下行网络侧乱序统计。 |

### **表4** GTPU业务质量分析内容解释

### | 字段名 | 说明 |

### | --- | --- |

### | ipVer | ip版本类型 |

### | localip | 本端IP地址。 |

### | peerip | 对端IP地址。 |

### | teidu | 隧道的teid号。 |

### | totalPktNum | 上行N3/S1-U/SA链路入口包数。 |

### | discardPktNum | 报文上行N3/S1-U/SA链路丢包统计。 |

### | disorderPktNum | 报文上行N3/S1-U/SA链路乱序报文统计。 |

### | abnormalPktNum | 报文上行N3/S1-U/SA链路异常报文统计。 |

### **表5** ICMP业务质量分析内容解释

### | 字段名 | 说明 |

### | --- | --- |

### | direct | ping报文发起的方向 |

### | ipVer | ip的版本 |

### | msip | 用户的IP地址。 |

### | serverip | 服务器的IP地址。 |

### | fragment | 报文分片的标记，0不分片，1表示分片且为首片。 |

### | icmpID | ping报文的Identifier字段。 |

### | icmpSN | ping报文的Sequence number字段。 |

### | inRequestTickNs | ping请求报文的入口时间(ns)。 |

### | outRequestTickNs | ping请求报文的出口时间(ns)。 |

### | inReplytimeTickNs | ping响应报文的入口时间(ns)。 |

### | outReplytimeTickNs | ping响应报文的出口时间(ns)。 |

### | innerRequestLatencyNs | ping请求报文的内部时延(ns)。 |

### | innerReplyLatencyNs | ping响应报文的内部时延(ns)。 |

### | outLatencyNs | ping请求报文的出口时间与ping响应报文入口时间的差值(ns) |

