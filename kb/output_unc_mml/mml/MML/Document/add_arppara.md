# 增加ARP策略参数配置(ADD ARPPARA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：SGSN**

此命令用于设置核心网侧PDP上下文中的ARP参数到无线侧ARP参数的映射规则。SGSN会根据配置的规则，将核心网侧PDP上下文中的ARP以及业务级别参数映射成无线侧的ARP参数，2G网络中SGSN向BSC发送的Create BSS Packet Flow Context Request消息（Priority信元中的Priority Level，Pre-emption Capability ，Pre-emption Vulnerability，Queuing Allowed），或SGSN向BSC发送的数传DL-UNITDATA消息（Priority信元中的Priority Level），3G网络中SGSN向RNC发送的RAB Assign消息和Relocation Request消息（包含4个信元：Priority Level，Pre-emption Capability，Pre-emption Vulnerability，Queuing Allowed）。

#### 注意事项

- 此命令的最大记录数为210条。
- “ARP策略组”为“G0(系统缺省组)”的记录是系统默认配置，只能修改其对应的ARP属性值，不能被删除，用于系统缺省场景下对全网用户的ARP策略；“G0(系统缺省组)”的记录可以使用**ADD ARPPARA**或者**MOD ARPPARA**命令进行修改，“自定义组”的记录不可用使用**ADD ARPPARA**命令进行修改。
- 本命令配置的“G1(自定义组1)”-“G9(自定义组9)”APR策略信息可以被**ADD ARPRANGE**命令引用；自定义组的ARP策略优先级高于系统缺省组。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GROUPID     | ARP策略组 | 可选必选说明：必选参数 参数含义：用于指定“用户级别”和“业务级别”共同确定的记录归属的ARP策略组。 数据来源：整网规划 取值范围：“G0(系统缺省组)”“G1(自定义组1)”“G2(自定义组2)”“G3(自定义组3)”“G4(自定义组4)”“G5(自定义组5)”“G6(自定义组6)”“G7(自定义组7)”“G8(自定义组8)”“G9(自定义组9)” 默认值：无  说明： “用户级别”和“业务级别”参数在同一个ARP策略组下最多只能配置21条记录，“ARP策略组”、“用户级别”和“业务级别”三者唯一确定一条记录。“ARP策略组”为“G0(系统缺省组)”的记录是系统默认配置，只能修改其对应的ARP属性值，不能被删除，用于系统缺省场景下对全网用户的取值。最多只能配置10组记录。                                                                                                                                                                                                                                                                                                                                                           |
| USRPRI      | 用户级别   | 可选必选说明：必选参数 参数含义：该参数用于指定用户级别，根据用户协商QoS属性中的分配保留优先级（Allocation/Retention Priority）确定。 数据来源：整网规划 取值范围：“HIGHLEVELUSER(高端用户)”：核心网侧协商的ARP为1。“NORMALUSER(普通用户)”：核心网侧协商的ARP为2。“LOWLEVELUSER(低端用户)”：核心网侧协商的ARP为3。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SRVLVL      | 业务级别   | 可选必选说明：必选参数 参数含义：该参数用于指定业务级别。根据用户PDP上下文QoS中的流量等级（Traffic class），下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。 数据来源：整网规划 取值范围：“CONVERSATION(Conversation)”：流量等级为Conversational class。“STREAMINGGBRMORE25KBPS(StreamingGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。“STREAMINGGBRLESS24KBPS(StreamingGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于25kbit/s。“INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。“INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。“INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。“BACKGROUND(Background)”：流量等级为Background class。 默认值：无 |
| PRTLVL      | 承载优先级  | 可选必选说明：条件必选参数，当ARP策略组为“G0(系统缺省组)”时为可选，其余为必选。 参数含义：该参数对应于承载中分配保留优先级（Allocation/Retention Priority）属性中的Priority Level信元，该信元表示请求建立和修改的承载优先级，RNC/BSC在决定资源分配时使用。 数据来源：整网规划 取值范围：1~15 默认值：无 配置原则：取值1~14按照优先级的降序排列，1表示最高优先级，14表示最低优先级。取值15表示无优先级，即“不触发抢占”并且“不允许抢占”。  说明： 优先级和抢占性标识一起决定无线承载是否无条件立即执行。如果资源不足需要进行抢占，并且请求的无线承载被标识为“可能触发抢占”，RNC/BSC可以触发抢占过程，强制释放一个优先级更低并且被标识为“允许抢占”的无线承载（参见3GPP TS 25.413、48.008）。                                                                                                                                                                                                                                                                                                           |
| PRELVL      | 抢占性    | 可选必选说明：条件必选参数，当ARP策略组为“G0(系统缺省组)”时为可选，否则为必选。 参数含义：该参数对应于无线承载中分配保留优先级（Allocation/Retention Priority）属性中的Pre-emption Capability信元，该信元表示无线承载建立请求对于其它无线承载的抢占能力（参见3GPP TS 25.413，48.008）。 数据来源：整网规划 取值范围：“NOTPRE-EMPTION(不触发抢占)”“MAYPRE-EMPTION(可能触发抢占)” 默认值：无  说明： “NOTPRE-EMPTION(不触发抢占)”：请求建立的无线承载不触发抢占过程。“MAYPRE-EMPTION(可能触发抢占)”：请求建立的无线承载可能触发抢占过程。                                                                                                                                                                                                                                                                                                                                                              |
| PREVUL      | 被抢占性   | 可选必选说明：条件必选参数，当ARP策略组为“G0(系统缺省组)”时为可选，否则为必选。 参数含义：该参数用于指定对应于无线承载中分配保留优先级（Allocation/Retention Priority）属性中的Pre-emption Vulnerability信元，该信元表示请求建立的承载是否可被其它承载抢占（参见3GPP TS 25.413， 48.008）。 数据来源：整网规划 取值范围：“NOTPRE-EMPTABLE(不允许抢占)”“PRE-EMPTABLE(允许抢占)” 默认值：无  说明： “NOTPRE-EMPTABLE(不允许抢占)”：请求建立的无线承载不允许被抢占。“PRE-EMPTABLE(允许抢占)”：请求建立的无线承载允许被抢占。                                                                                                                                                                                                                                                                                                                                                                    |
| QUEUE       | 排队属性   | 可选必选说明：条件必选参数，当ARP策略组为“G0(系统缺省组)”时为可选，否则为必选。 参数含义：该参数用于指定对应于无线承载中分配保留优先级（Allocation/Retention Priority）属性中的Queuing Allowed信元，该信元表示无线承载建立请求是否可以放入资源分配队列（参见3GPP TS 25.413, 48.008）。 数据来源：整网规划 取值范围：“NOTQUEUING(不允许排队)”“QUEUING(允许排队)” 默认值：无  说明： “ NOTQUEUING(不允许排队)”：不允许排队，无线侧不应该将该承载建立请求放入资源分配队列。 “QUEUING(允许排队)”：允许排队，无线侧可以将该承载建立请求放入资源分配队列。                                                                                                                                                                                                                                                                                                                                                                    |
| DESCRIPTION | 描述     | 可选必选说明：可选参数 参数含义：用于设置本条记录的配置描述信息。 数据来源：整网规划 取值范围：0~32位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

#### 使用实例

1. 修改系统缺省场景下对全网用户的取值记录，系统缺省值参考表1。

   ADD ARPPARA: GROUPID=G0, USRPRI=HIGHLEVELUSER, SRVLVL=CONVERSATION, PRTLVL=3, PRELVL=NOTPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
2. 配置完整的自定义ARP策略组G1，以便后续特定用户使用该策略组，配置如下：

   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=CONVERSATION, PRTLVL=4, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=STREAMINGGBRMORE25KBPS, PRTLVL=5, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=STREAMINGGBRLESS24KBPS, PRTLVL=5, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI1, PRTLVL=5, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI2, PRTLVL=6, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI3, PRTLVL=7, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=HIGHLEVELUSER, SRVLVL=BACKGROUND, PRTLVL=7, PRELVL=MAYPRE-EMPTION, PREVUL=NOTPRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=CONVERSATION, PRTLVL=7, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=STREAMINGGBRMORE25KBPS, PRTLVL=8, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=STREAMINGGBRLESS24KBPS, PRTLVL=8, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=INTERACTIVETRAFFICPRI1, PRTLVL=9, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=INTERACTIVETRAFFICPRI2, PRTLVL=9, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=INTERACTIVETRAFFICPRI3, PRTLVL=10, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=NORMALUSER, SRVLVL=BACKGROUND, PRTLVL=10, PRELVL=MAYPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=QUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=CONVERSATION, PRTLVL=10, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=STREAMINGGBRMORE25KBPS, PRTLVL=11, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=STREAMINGGBRLESS24KBPS, PRTLVL=11, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI1, PRTLVL=12, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI2, PRTLVL=12, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=INTERACTIVETRAFFICPRI3, PRTLVL=12, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;
   - ADD ARPPARA: GROUPID=G1, USRPRI=LOWLEVELUSER, SRVLVL=BACKGROUND, PRTLVL=14, PRELVL=NOTPRE-EMPTION, PREVUL=PRE-EMPTABLE, QUEUE=NOTQUEUING;

   使用上述命令配置完整的ARP策略组（由用户级别和业务级别确定，总共有21条记录），参考表2。

#### 参考信息

| ARP策略组    | 用户级别   | 业务级别                   |   承载优先级 | 抢占性    | 被抢占性   | 排队属性   |
|:----------|:-------|:-----------------------|--------:|:-------|:-------|:-------|
| 系统缺省组（G0） | 高端用户   | Conversation           |       4 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | StreamingGBRMore25Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | StreamingGBRLess24Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | InteractiveTrafficPri1 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | InteractiveTrafficPri2 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | InteractiveTrafficPri3 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 高端用户   | Background             |       7 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| 系统缺省组(G0) | 普通用户   | Conversation           |       7 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | StreamingGBRMore25Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | StreamingGBRLess24Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | InteractiveTrafficPri1 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | InteractiveTrafficPri2 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | InteractiveTrafficPri3 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 普通用户   | Background             |      10 | 可能触发抢占 | 允许抢占   | 允许排队   |
| 系统缺省组(G0) | 低端用户   | Conversation           |      10 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | StreamingGBRMore25Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | StreamingGBRLess24Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | InteractiveTrafficPri1 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | InteractiveTrafficPri2 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | InteractiveTrafficPri3 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| 系统缺省组(G0) | 低端用户   | Background             |      13 | 不触发抢占  | 允许抢占   | 不允许排队  |

| ARP策略组    | 用户级别   | 业务级别                   |   承载优先级 | 抢占性    | 被抢占性   | 排队属性   |
|:----------|:-------|:-----------------------|--------:|:-------|:-------|:-------|
| G1(自定义组1) | 高端用户   | Conversation           |       4 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | StreamingGBRMore25Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | StreamingGBRLess24Kbps |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | InteractiveTrafficPri1 |       5 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | InteractiveTrafficPri2 |       6 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | InteractiveTrafficPri3 |       7 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 高端用户   | Background             |       7 | 可能触发抢占 | 不允许抢占  | 允许排队   |
| G1(自定义组1) | 普通用户   | Conversation           |       7 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | StreamingGBRMore25Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | StreamingGBRLess24Kbps |       8 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | InteractiveTrafficPri1 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | InteractiveTrafficPri2 |       9 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | InteractiveTrafficPri3 |      10 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 普通用户   | Background             |      10 | 可能触发抢占 | 允许抢占   | 允许排队   |
| G1(自定义组1) | 低端用户   | Conversation           |      10 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | StreamingGBRMore25Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | StreamingGBRLess24Kbps |      11 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | InteractiveTrafficPri1 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | InteractiveTrafficPri2 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | InteractiveTrafficPri3 |      12 | 不触发抢占  | 允许抢占   | 不允许排队  |
| G1(自定义组1) | 低端用户   | Background             |      14 | 不触发抢占  | 允许抢占   | 不允许排队  |