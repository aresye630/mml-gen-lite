# 查询业务统计信息（DSP FLOWSTATISTICS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查看指定用户的TCP/QUIC业务质量监控信息。

#### 注意事项

- 单用户TCP/QUIC业务质量监控最多支持统计100条流。
- 当用户上下文在线时，通过该命令显示指定用户的TCP/QUIC业务质量监控信息（必须先启动此用户的TCP/QUIC业务质量监控）。开启指定用户的TCP/QUIC业务质量监控功能需要在CSP的用户跟踪界面上选择FLOW\_STATISTICS消息类型。勾选FLOW\_STATISTICS后，用户激活后，进行TCP/QUIC业务后每隔20秒会上报一个FLOW-STATISTICS消息，其中包含了该用户所需要上报的流信息。业务质量监控启动和停止（包括去激活）时分别上报一条EMS消息，表明此用户是否被选定进行业务质量监控，因此用户跟踪建议同时开启EMS。
- 系统设备割接、升级、扩容、参数调整、新业务部署（SA、TCP/QUIC/网页/视频优化等业务），以及单用户业务质量问题定位（速率慢、时延大等）等场景下，通过单用户TCP/QUIC业务质量监控的手段，能够方便的获取用户TCP/QUIC业务质量信息，用于评估业务质量，提升维护和定位效率。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                 |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------|
| USERID | 用户标识   | 可选必选说明：必选参数 参数含义：用户标识类型。 数据来源：本端规划 取值范围：枚举类型。 IMSI：用户的IMSI号。MSISDN：用户的MSISDN号。IMEI：用户的IMEI号。 默认值：无 配置原则：无                            |
| IMSI   | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“USERID”配置为“IMSI”时为必选参数。 参数含义：指定待查询用户的IMSI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0～9的数字。 默认值：无 配置原则：无     |
| MSISDN | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“USERID”配置为“MSISDN”时为必选参数。 参数含义：指定待查询用户的MSISDN号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0～9的数字。 默认值：无 配置原则：无 |
| IMEI   | IMEI   | 可选必选说明：条件必选参数 前提条件：该参数在“USERID”配置为“IMEI”时为必选参数。 参数含义：指定待查询用户的IMEI号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0～9的数字。 默认值：无 配置原则：无     |

#### 使用实例

查询单用户的业务质量监控信息：

```
DSP FLOWSTATISTICS: USERID=IMSI,IMSI="2456789012342";
```

```
User Info
---------
Flow Statistics Info  =  
-----------------
User Info: IMSI = 2456789012342 MSISDN = 12341234 IMEI = 123456789012371
-----------------
TCP Flow Info:
---------

No.                           0
ipVer                         :4
msip[0]                       :0xd6025f01
msip[1]                       :0x00000000
msip[2]                       :0x00000000
msip[3]                       :0x00000000
serverip[0]                   :0x131e02b4
serverip[1]                   :0x00000000
serverip[2]                   :0x00000000
serverip[3]                   :0x00000000
msPort                        :554
serverPort                    :1079
teidc                         :2
creatDirFlag                  :1
useState                      :2
tcpConnectionStatus           :0
startTime                     :553746997
lastTime                      :553746997
onlineTime                    :<2
ueToCNRTT                     :65535
cnToServerRTT                 :65535
msMss                         :0
serverMss                     :0
msSackFlag                    :0
serverSackFlag                :0
msWinScale                    :0
serverWinScale                :0
msWinSize                     :0
serverWinSize                 :0
upRanDiscardPktNum            :0
upSPDiscardPktNum             :0
upRanSlowDisorderPktNum       :0
upRanFastDisorderPktNum       :0
dnRanDiscardPktNum            :0
dnSPDiscardPktNum             :0
dnSPSlowDisorderPktNum        :0
dnSPFastDisorderPktNum        :0
ranAverageRtt                 :<2
spAverageRtt                  :<2
upInPktNum                    :0
upOutPktNum                   :0
dnInPktNum                    :1
dnOutPktNum                   :1
upInFlowByte                  :0
dnInFlowByte                  :265
upOutFlowByte                 :0
dnOutFlowByte                 :265
upAvgPktLength                :0
dnAvgPktLength                :265
upInIpFragPktNum              :0
upOutIpFragPktNum             :0
dnInIpFragPktNum              :0
dnOutIpFragPktNum             :0
upFirstIpFragNum              :0
dnFirstIpFragNum              :0
upInDisorderPkt               :0
upOutDisorderPkt              :0
dnInDisorderPkt               :0
dnOutDisorderPkt              :0
maxUpPktDelay                 :<2
maxDnPktDelay                 :<2
upPktAvgDelay                 :<2
dnPktAvgDelay                 :<2
teidu                         :9502722
dpeRateMax                    :4
msRecvWnScale                 :0
msRecvWnZeroNum               :0
msRecvWnMax                   :0
msSendNum                     :0
msRecvWnTotal                 :0
msRecvWnAvg                   :0
spRecvWnScale                 :0
spRecvWnZeroNum               :0
spRecvWnMax                   :29920
spSendNum                     :1
spRecvWnTotal                 :29920
spRecvWnAvg                   :29920
upLastAckNumber               :0
dnLastAckNumber               :639411594
upByteInFlightMax             :0
dnByteInFlightMax             :0
upDupAckOne                   :0
upDupAckMax                   :0
upDupAckAll                   :0
dnDupAckOne                   :0
dnDupAckMax                   :0
dnDupAckAll                   :0
upInNotAckAveragePktByte      :0
dnInNotAckAveragePktByte      :265
upOutNotAckAveragePktByte     :0
dnOutNotAckAveragePktByte     :265
upBurstPktNum                 :0
dnBurstPktNum                 :1
upBurstPktByte                :0
dnBurstPktByte                :265
ranMaxJitter                  :0
spMaxJitter                   :0
ranSumJitter                  :0
spSumJitter                   :0
ranAvgJitter                  :0
spAvgJitter                   :0
upRetranPktNum                :0
dnRetranPktNum                :0
upRetranAverageDelay          :0
upRetranMaxDelay              :0
dnRetranAverageDelay          :0
dnRetranMaxDelay              :0
RelayServiceFlag              :0
upPktAvgKbps                  :0
dnPktAvgKbps                  :0

(Number of results = 1)

-----------------
User Info: IMSI = 2456789012342 MSISDN = 12341234 IMEI = 123456789012371
-----------------
QUIC Flow Info:
---------

No.                           0
ipVer                         :4
teidu                         :1
ulConnectionID                :6786571632704945195
dlConnectionID                :6786571632704945195
msip[0]                       :0xd6025f01
msip[1]                       :0x00000000
msip[2]                       :0x00000000
msip[3]                       :0x00000000
serverip[0]                   :0x131e02b4
serverip[1]                   :0x00000000
serverip[2]                   :0x00000000
serverip[3]                   :0x00000000
msPort                        :7716
serverPort                    :443
creatDirFlag                  :0
useState                      :2
startTime                     :185627871
lastTime                      :185629739
onlineTime                    :1868
ulInPkt                       :4
ulOutPkt                      :4
dlInPkt                       :4
dlOutPkt                      :4
ulInBytes                     :2284
ulOutBytes                    :4197
dlInBytes                     :2284
dlOutBytes                    :4197
upAvgPktLength                :571
dnAvgPktLength                :1049
ulInIpFragPkt                 :0
ulOutIpFragPkt                :0
dlInIpFragPkt                 :0
dlOutIpFragPkt                :0
ulInIpFragFirstPkt            :0
dlInIpFragFirstPkt            :0
ulAvgInnerDelay               :<2
dlAvgInnerDelay               :<2
ulMaxInnerDelay               :<2
dlMaxInnerDelay               :<2
ulRanDiscardPkt               :0
dlSPDiscardPkt                :0
ulRanDisorderPkt              :2
dlSPDisorderPkt               :2

(Number of results = 2)

---    END
```

#### 输出结果说明

| 输出项名称                     | 输出项解释                                                                       |
|:--------------------------|:----------------------------------------------------------------------------|
| IMSI                      | 国际移动用户标识，当用户接入不携带IMSI时，显示为"NULL"。                                           |
| IMEI                      | 国际移动设备标识，当用户接入不携带IMEI时，显示为"NULL"。                                           |
| MSISDN                    | 用户的MSISDN号，当用户接入不携带MSISDN时，显示为"NULL"。                                       |
| msip                      | 终端的IP。                                                                      |
| serverip                  | 服务器的IP。                                                                     |
| msPort                    | 终端的端口号。                                                                     |
| serverPort                | 服务器的端口号。                                                                    |
| teidc                     | 流对应的本端控制面隧道ID。                                                              |
| creatDirFlag              | 触发创建当前流统计的报文方向。0表示上行包触发，1表示下行包触发。                                           |
| useState                  | 流使用标记。0表示未使用，1表示已老化，2表示在使用。                                                 |
| tcpConnectionStatus       | TCP建链状态。                                                                    |
| startTime                 | 流被创建的时间戳。单位ms。                                                              |
| lastTime                  | 流最后一个报文的时间戳。单位ms。                                                           |
| onlineTime                | 流业务持续时间。单位是ms。持续时间在2ms以下显示为“<2”，其余按实际值显示。                                   |
| ueToCNRTT                 | TCP流RAN侧的平均RTT时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                            |
| cnToServerRTT             | TCP流SP侧的平均RTT时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| msMss                     | TCP流终端的最大分片值。单位是字节。如果没有监控到TCP建链三次握手的报文，则统计信息显示为NA。如果报文中不携带MSS字段，则统计信息显示为0。  |
| serverMss                 | TCP流服务器的最大分片值。单位是字节。如果没有监控到TCP建链三次握手的报文，则统计信息显示为NA。如果报文中不携带MSS字段，则统计信息显示为0。 |
| msSackFlag                | TCP流MS侧报文是否携带Sackflag;。                                                     |
| serverSackFlag            | TCP流Server侧报文是否携带Sackflag;。                                                 |
| msWinScale                | TCP流MS接收窗口扩大因子。TCP报文头中携带了这个字段的值。                                            |
| serverWinScale            | TCP流Server接收窗口扩大因子。TCP报文头中携带了这个字段的值。                                        |
| msWinSize                 | TCP流MS接收窗口值。                                                                |
| serverWinSize             | TCP流Server接收窗口值。                                                            |
| upRanDiscardPktNum        | TCP流上行RAN侧丢包数。单位是报文个数。                                                      |
| upSPDiscardPktNum         | TCP流上行SP侧丢包数。单位是报文个数。                                                       |
| upRanSlowDisorderPktNum   | TCP流上行RAN侧跑的慢的乱序包数。单位是报文个数。                                                 |
| upRanFastDisorderPktNum   | TCP流上行RAN侧跑的快的乱序包数。单位是报文个数。                                                 |
| dnRanDiscardPktNum        | TCP流下行RAN侧丢包数。单位是报文个数。                                                      |
| dnSPDiscardPktNum         | TCP流下行SP侧丢包数。单位是报文个数。                                                       |
| dnSPSlowDisorderPktNum    | TCP流下行SP侧跑的慢的乱序包数。单位是报文个数。                                                  |
| dnSPFastDisorderPktNum    | TCP流下行SP侧跑的快的乱序包数。单位是报文个数。                                                  |
| ranAverageRtt             | TCP流RAN侧的平均RTT时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                            |
| spAverageRtt              | TCP流SP侧的平均RTT时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| upInPktNum                | TCP流上行入口包数。单位是报文个数。                                                         |
| upOutPktNum               | TCP流上行出口包数。单位是报文个数。                                                         |
| dnInPktNum                | TCP流下行入口包数。单位是报文个数。                                                         |
| dnOutPktNum               | TCP流下行出口包数。单位是报文个数。                                                         |
| upInFlowByte              | TCP流上行入口流量字节数。单位是字节。                                                        |
| dnInFlowByte              | TCP流下行入口流量字节数。单位是字节。                                                        |
| upOutFlowByte             | TCP流上行出口流量字节数。单位是字节。                                                        |
| dnOutFlowByte             | TCP流上行出口流量字节数。单位是字节。                                                        |
| upAvgPktLength            | TCP流上行流量平均包长。单位是字节。                                                         |
| dnAvgPktLength            | TCP流下行流量平均包长。单位是字节。                                                         |
| upInIpFragPktNum          | TCP流上行入口IP分片包数。单位是报文个数。                                                     |
| upOutIpFragPktNum         | TCP流上行出口IP分片包数。单位是报文个数。                                                     |
| dnInIpFragPktNum          | TCP流下行入口IP分片包数。单位是报文个数。                                                     |
| dnOutIpFragPktNum         | TCP流下行出口IP分片包数。单位是报文个数。                                                     |
| upFirstIpFragNum          | TCP流上行入口IP分片首包数 。单位是报文个数。                                                   |
| dnFirstIpFragNum          | TCP流下行入口IP分片首包数。单位是报文个数。                                                    |
| upInDisorderPkt           | TCP流上行入口乱序包数。单位是报文个数。                                                       |
| upOutDisorderPkt          | TCP流上行出口乱序包数。单位是报文个数。                                                       |
| dnInDisorderPkt           | TCP流下行入口乱序包数。单位是报文个数。                                                       |
| dnOutDisorderPkt          | TCP流下行出口乱序包数。单位是报文个数。                                                       |
| maxUpPktDelay             | TCP流上行报文处理最大时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                              |
| maxDnPktDelay             | TCP流下行报文处理最大时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                              |
| upPktAvgDelay             | TCP流上行报文处理平均时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                              |
| dnPktAvgDelay             | TCP流下行报文处理平均时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                              |
| teidu                     | 流对应的本端用户面隧道ID。                                                              |
| dpeRateMax                | 业务处理对应DPE调度域CPU最大使用率。                                                       |
| msRecvWnScale             | TCP流MS接收窗口扩大因子。TCP报文头中携带了这个字段的值。                                            |
| msRecvWnZeroNum           | TCP流MS的接收窗口值为0的报文个数。单位是报文个数。                                                |
| msRecvWnMax               | TCP流MS的接收窗口最大值。单位是字节。                                                       |
| msSendNum                 | TCP流MS的接收窗口个数。                                                              |
| msRecvWnTotal             | TCP流MS的接收窗口总和。单位是字节。                                                        |
| msRecvWnAvg               | TCP流MS的接收窗口平均值。单位是字节。                                                       |
| spRecvWnScale             | TCP流SP接收窗口扩大因子。TCP报文头中携带了这个字段的值。                                            |
| spRecvWnZeroNum           | TCP流SP的接收窗口值为0的报文个数。单位是报文个数。                                                |
| spRecvWnMax               | TCP流SP侧的接收窗口最大值。单位是字节。                                                      |
| spSendNum                 | TCP流SP侧的接收窗口个数。                                                             |
| spRecvWnTotal             | TCP流SP侧的接收窗口总和。单位是字节。                                                       |
| spRecvWnAvg               | TCP流SP侧的接收窗口平均值。单位是字节。                                                      |
| upLastAckNumber           | TCP流上行方向收到的最后一个ACK Number；。                                                 |
| dnLastAckNumber           | TCP流下行方向收到的最后一个ACK Number；。                                                 |
| upByteInFlightMax         | TCP流上行在传输路径中字节流的最大值。单位是字节。                                                  |
| dnByteInFlightMax         | TCP流下行在传输路径中字节流的最大值。单位是字节。                                                  |
| upDupAckOne               | TCP流上行至少重复1次的Ack统计，对于相同TCP SN下行数据报文对应的Ack多次重复时，不做重复统计。单位是报文个数。              |
| upDupAckMax               | TCP流上行重复次数最多的Ack统计，对于相同TCP SN下行数据报文对应的Ack多次重发最多统计。单位是报文个数。                  |
| upDupAckAll               | TCP流上行重复Ack总数统计，对于相同TCP SN下行数据报文对应的Ack多次重发累计。单位是报文个数。                       |
| dnDupAckOne               | TCP流下行至少重复1次的Ack统计，对于相同TCP SN上行数据报文对应的Ack多次重复时，不做重复统计。单位是报文个数。              |
| dnDupAckMax               | TCP流下行重复次数最多的Ack统计，对于相同TCP SN上行数据报文对应的Ack多次重发最多统计。单位是报文个数。                  |
| dnDupAckAll               | TCP流下行重复Ack总数统计，对于相同TCP SN上行数据报文对应的Ack多次重发累计。单位是报文个数。                       |
| upInNotAckAveragePktByte  | TCP流上行入口非纯ack报文平均包长。单位是字节。                                                  |
| dnInNotAckAveragePktByte  | TCP流下行入口非纯ack报文平均包长。单位是字节。                                                  |
| upOutNotAckAveragePktByte | TCP流上行出口非纯ack报文平均包长。单位是字节。                                                  |
| dnOutNotAckAveragePktByte | TCP流下行出口非纯ack报文平均包长。单位是字节。                                                  |
| upBurstPktNum             | TCP流上行最大突发报文数。单位是报文个数。                                                      |
| dnBurstPktNum             | TCP流下行最大突发报文数。单位是报文个数。                                                      |
| upBurstPktByte            | TCP流上行最大突发报文字节数。单位是字节。                                                      |
| dnBurstPktByte            | TCP流下行最大突发报文字节数。单位是字节。                                                      |
| ranMaxJitter              | TCP流RAN侧最大抖动。单位ms。                                                          |
| spMaxJitter               | TCP流SP侧最大抖动。单位ms。                                                           |
| ranSumJitter              | TCP流RAN侧抖动总和。单位ms。                                                          |
| spSumJitter               | TCP流SP侧抖动总和。单位ms。                                                           |
| ranAvgJitter              | TCP流RAN侧平均抖动。单位ms。                                                          |
| spAvgJitter               | TCP流SP侧平均抖动。单位ms。                                                           |
| upRetranPktNum            | TCP流上行重传包数。单位是报文个数。                                                         |
| dnRetranPktNum            | TCP流下行重传包数。单位是报文个数。                                                         |
| upRetranAverageDelay      | TCP流上行重传报文平均时延。单位ms。                                                        |
| upRetranMaxDelay          | TCP流上行重传报文最大时延。单位ms。                                                        |
| dnRetranAverageDelay      | TCP流下行重传报文平均时延。单位ms。                                                        |
| dnRetranMaxDelay          | TCP流下行重传报文最大时延。单位ms。                                                        |
| RelayServiceFlag          | 媒体业务流标识。                                                                    |
| upPktAvgKbps              | TCP流上行报文出口平均速率。单位kbps。                                                      |
| dnPktAvgKbps              | TCP流下行报文出口平均速率。单位kbps。                                                      |
| ulConnectionID            | QUIC流上行标识。                                                                  |
| dlConnectionID            | QUIC流下行标识。                                                                  |
| ulInPkt                   | QUIC流上行入口包数。单位是报文个数。                                                        |
| ulOutPkt                  | QUIC流上行出口包数。单位是报文个数。                                                        |
| dlInPkt                   | QUIC流下行入口包数。单位是报文个数。                                                        |
| dlOutPkt                  | QUIC流下行出口包数。单位是报文个数。                                                        |
| ulInBytes                 | QUIC流上行入口流量字节数。单位是字节。                                                       |
| ulOutBytes                | QUIC流上行出口流量字节数。单位是字节。                                                       |
| dlInBytes                 | QUIC流下行入口流量字节数。单位是字节。                                                       |
| dlOutBytes                | QUIC流下行出口流量字节数。单位是字节。                                                       |
| upAvgPktLength            | QUIC流上行流量平均包长度。单位是字节。                                                       |
| dnAvgPktLength            | QUIC流下行流量平均包长度。单位是字节。                                                       |
| ulInIpFragPkt             | QUIC流上行入口IP分片包数。单位是报文个数。                                                    |
| ulOutIpFragPkt            | QUIC流上行出口IP分片包数。单位是报文个数。                                                    |
| dlInIpFragPkt             | QUIC流下行入口IP分片包数。单位是报文个数。                                                    |
| dlOutIpFragPkt            | QUIC流下行出口IP分片包数。单位是报文个数。                                                    |
| ulInIpFragFirstPkt        | QUIC流上行入口IP分片首包数 。单位是报文个数。                                                  |
| dlInIpFragFirstPkt        | QUIC流下行入口IP分片首包数。单位是报文个数。                                                   |
| ulAvgInnerDelay           | QUIC流上行报文处理平均时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| dlAvgInnerDelay           | QUIC流下行报文处理平均时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| ulMaxInnerDelay           | QUIC流上行报文处理最大时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| dlMaxInnerDelay           | QUIC流下行报文处理最大时延。单位是ms。时延在2ms以下显示为“<2”，其余按实际值显示。                             |
| ulRanDiscardPkt           | QUIC流上行RAN侧丢包数。单位是报文个数。                                                     |
| dlSPDiscardPkt            | QUIC流下行SP侧丢包数。单位是报文个数。                                                      |
| ulRanDisorderPkt          | QUIC流上行RAN侧乱序包数。单位是报文个数。                                                    |
| dlSPDisorderPkt           | QUIC流下行SP侧乱序包数。单位是报文个数。                                                     |