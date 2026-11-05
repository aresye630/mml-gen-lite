# 增加业务切换策略(ADD SRVHANDOVER)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN**

该命令用于增加业务切换策略信息。切换策略控制就是根据业务级别、用户级别确定用户在2G和3G网络中的切换策略，来引导2G和3G的网络业务承载和网络负荷。切换策略可以由运营商配置。

通过Iu接口消息RAB ASSIGNMENT REQUEST和RELOCATION REQUEST中信元Service Handover以及Gb接口消息Create-BSS-PFC携带的信元Service UTRAN CCO将业务切换策略结果通知RNC/BSS。

#### 注意事项

- 该命令执行后立即生效。
- 本表最大记录数为28条。
- 需要加载支持该特性的License，对应的License项为“切换策略控制”。
- 基于业务的切换策略控制只针对同时支持2G和3G的终端并且签约信息允许同时使用2G和3G网络的用户。
- RNC(Radio Network Controller)/BSS(Base Station Subsystem)需支持基于业务的切换。
- 此配置涉及切换策略控制特性（特性编号：WSFD-104507，license部件编码：LKV2SRVHD02），执行命令请使用**DSP LICENSE**命令确认对应特性license是否得到授权，执行**LST LICENSESWITCH**命令确认特性开关状态为“打开”。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:-------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRVLVL | 业务级别        | 可选必选说明：必选参数 参数含义：该参数需根据用户PDP上下文QoS中的流量等级（Traffic class）、下行保证速率（Guaranteed bit rate for downlink）和发送控制优先级（Traffic handling priority）确定。 数据来源：整网规划 取值范围：“CONVERSATION(Conversation)”：流量等级为Conversational class。“STREAMINGGBRMORE25KBPS(StreamGBRMore25kbps)”：流量等级为Streaming class，下行保证速率大于等于25kbit/s。“STREAMINGGBRLESS24KBPS(StreamGBRLess24kbps)”：流量等级为Streaming class，下行保证速率小于24kbit/s。“INTERACTIVETRAFFICPRI1(InteractiveTrafficPri1)”：流量等级为Interactive class，发送控制优先级为1。“INTERACTIVETRAFFICPRI2(InteractiveTrafficPri2)”：流量等级为Interactive class，发送控制优先级为2。“INTERACTIVETRAFFICPRI3(InteractiveTrafficPri3)”：流量等级为Interactive class，发送控制优先级为3。“BACKGROUND(Background)”：流量等级为Background class。 默认值：无                                                                                                                    |
| USRPRI | 用户级别        | 可选必选说明：必选参数 参数含义：该参数用于指定用户签约QoS属性中的分配保留优先级（Allocation/Retention Priority）。分配/保留优先级参数用于指示各UMTS承载在确定分配和保留时的相对重要性，该参数仅在Gn/Gp接口上传送，用于SGSN和GGSN之间的QoS协商，移动终端的QoS信元中不携带该参数。 数据来源：整网规划 取值范围： “HIGHLEVELUSER(高端用户)”：分配/保留优先级为1。“NORMALUSER(普通用户)”：分配/保留优先级为2。“LOWLEVELUSER(低端用户)”：分配/保留优先级为3。“NONE(None)”：通用用户级别，表示该用户没有用户级别，设置的门限就是该业务级别所有用户级别的切换策略。 默认值：无  说明： 在相同业务级别下，配置不同的用户级别，其中配置了“通用用户级别”，表示在相同的业务级别下，对已配置用户级别之外的所有用户级别都使用“通用用户级别”的策略。                                                                                                                                                                                                                                                                                                                                                                                |
| WSHS   | WCDMA业务切换策略 | 可选必选说明：必选参数 参数含义：该参数用于指定3G业务切换策略。在3G网络中，SGSN通过Iu接口消息RAB ASSIGNMENT REQUEST或者RELOCATION REQUEST中的信元Service Handover将业务切换策略结果通知RNC。 数据来源：整网规划 取值范围：“GPRS(建议切换到GPRS)”：即建议切换到2G。请求的RAB（Radio Access Bearer）需要尽快切换到GSM（Global System for Mobile Communication）网络。业务切换信元Service Hanover携带的信息是Handover to GSM should be performed（0）。“WCDMA(不建议切换到GPRS)”：不建议切换到2G。请求的RAB需要尽可能长时间地保留在UMTS网络中。业务切换信元Service Hanover携带的信息是Handover to GSM should not be performed（1）。“ONLYWCDMA(只选WCDMA)”：即保留3G业务。请求的RAB保留在WCDMA网络：这意味着UTRAN不应该为MS发起到GSM网络的切换请求，除非携带此指示的RAB已经按照正常的释放流程释放。业务切换信元Service Hanover携带的信息是Handover to GSM shall not be performed（2）。 默认值：无                                                                                                                                                                            |
| GSHS   | GPRS业务切换策略  | 可选必选说明：必选参数 参数含义：该参数用于指定2G业务切换策略。在2G网络中，SGSN通过Gb接口消息Create-BSS-PFC携带的信元Service UTRAN CCO将业务切换策略结果通知BSS。 数据来源：整网规划 取值范围：“WCDMA(建议切换到WCDMA)”：建议切换到3G。请求的RAB需要切换到UMTS网络：对于NAS(Non-Access Stratum)，尽管是否切换到UMTS网络的最终决策仍然在GERAN网络内做出，但是请求的RAB需要尽快切换到UMTS网络。业务切换信元Service UTRAN CCO携带的信息是Network initiated cell change order procedure to UTRAN should be performed（0）。“GPRS(不建议切换到WCDMA)”：不建议切换到3G。 请求的RAB不需要切换到UMTS网络：对于NAS，尽管是否切换到UMTS网络的最终决策仍然在GERAN网络内做出，但是请求的RAB需要尽可能长时间地保留在GSM网络中。业务切换信元Service UTRAN CCO携带的信息是Network initiated cell change order procedure to UTRAN should not be performed（1）。“ONLYGPRS(只选GPRS)”：即保留2G业务。请求的PFC保留在GSM网络：这意味着BSS不应该为MS发起到WCDMA网络的切换请求，除非携带此指示的PFC已经按照正常的释放流程释放。业务切换信元Service UTRAN CCO携带的信息是Network initiated cell change order procedure to UTRAN shall not be performed（2）。 默认值：无 |

#### 使用实例

增加业务级别为“BACKGROUND(Background)”，用户级别为“HIGHLEVELUSER(高端用户)”，WCDMA业务切换策略为“GPRS(建议切换到GPRS)”，GPRS业务切换策略为“WCDMA(建议切换到WCDMA)”：

ADD SRVHANDOVER:SRVLVL=BACKGROUND, USRPRI=HIGHLEVELUSER, WSHS=GPRS, GSHS=WCDMA;