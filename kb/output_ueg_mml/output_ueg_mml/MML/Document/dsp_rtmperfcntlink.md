# 显示LINK性能统计实时结果(DSP RTMPERFCNTLINK)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

该命令用于实时查看LINK\_VNFC当前性能统计的情况，即查询某一对象实例的某一单元下所有指标的当前性能统计值。

#### 注意事项

- 系统最多支持5个用户并发执行该命令。
- 由于各进程、各类型指标的采样点不能完全统一，因此指标结果存在一定的误差，统计误差最大不超过该指标在10s内的统计变化值。
- 测量周期前10s执行该命令查看性能统计，“查询结果”会返回“Result is UnReliable”，如果出现了此现象，可等待10s再查询。
- 使用该命令查询之前需要先在U2020/MAE上创建基于该测量对象实例的话统统计任务，等待5min后再执行相应查询命令。基于SGSN对象的话统指标不需要创建统计任务，该对象的测量单元可直接查询。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MOC    | 测量对象   | 可选必选说明：必选参数。 参数含义：测量对象类ID。 数据来源：本端规划。 取值范围：“GNGPIP(GnGp IP)”“SGSN(USN function)”“M3UA_LNK(M3UA链路)”“M3UA_LNKSET(M3UA链路集)”“M3UA_DE(M3UA目的实体)”“VLR(VLR)”“DNS_INQUIRY(DNS查询)”“DIAMETER_LINK(Diameter链路)”“DIAMETER_LINKSET(Diameter链路集)”“SCTP_LINK(SCTP链路)”“VM_USN(虚拟机)”“M3UA_RT(M3UA信令路由)”“RU(资源单元)”“ScalGroup(ScalGroup)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| MOI    | 实例名称   | 可选必选说明：必选参数。 参数含义：测量对象实例。 数据来源：本端规划。 前提条件：该测量实例已经在U2020/MAE上话统测量管理（通过“性能->测量管理”菜单打开）中下发，SGSN对象类实例除外。 取值范围：1~63位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| MUID   | 测量单元   | 可选必选说明：必选参数。 参数含义：测量对象对应的测量单元。 数据来源：本端规划。 取值范围： 该参数在“MOC”参数设置为“GNGPIP(GnGp IP)”时：“PERF_TYPE_GTPU_IP(指定Gn IP流量)”“PERF_TYPE_GTP_MESSAGE_WITH_IP(指定IP地址的GTP报文)” 该参数在“MOC”参数设置为“SGSN(USN function)”时：“PERF_TYPE_GTP(GTP承载)”“PERF_TYPE_GTP_CP(GTP消息处理)”“PERF_TYPE_GTP_DNS(SGSN的DNS请求)”“PERF_TYPE_RANAP(RANAP)”“PERF_TYPE_SS7_SCCP_PERFORM(SCCP性能)”“PERF_TYPE_SS7_SCCP_AVAILABILITY(SCCP可用性)”“PERF_TYPE_SS7_SCCP_ULTILIZATION(SCCP利用率)”“PERF_TYPE_SS7_TCAP_ULTILIZATION(TCAP组元利用率)”“PERF_TYPE_SS7_TCAP_MSG_NUM(TCAP消息)”“PERF_TYPE_SS7_TCAP_TSL(TCAP TSL)”“PERF_TYPE_SS7_TCAP_CSL(TCAP CSL)”“PERF_TYPE_SPECIFIC_ABNORMAL_GTP(GTP异常报文)”“PERF_TYPE_S1AP(S1接口统计)”“PERF_TYPE_S6A(S6a接口统计)”“PERF_TYPE_S1_PAGING(S1模式寻呼)”“PERF_TYPE_SGS(SGs接口统计)”“PERF_TYPE_CBS(小区广播业务)”“PERF_TYPE_SYS_OVERLOAD_CTRL_WHOLE_SYSTEM(整系统因流控而丢弃的消息统计)”“PERF_TYPE_NBS1_PAGING(NB-S1模式寻呼)”“PERF_TYPE_IP_PACKETS(转发面报文统计)”“PERF_TYPE_S13(S13接口统计)”“PERF_TYPE_IP_PACKETS(转发面报文统计)” 该参数在“MOC”参数设置为“M3UA_LNK(M3UA链路)”时：“PERF_TYPE_SS7_M3UA_LINK(M3UA信令链路)” 该参数在“MOC”参数设置为“M3UA_LNKSET(M3UA链路集)”时：“PERF_TYPE_SS7_M3UA_LINKSET(M3UA信令链路集)” 该参数在“MOC”参数设置为“M3UA_DE(M3UA目的实体)”时：“PERF_TYPE_SS7_M3UA_DE(M3UA目的信令点)” 该参数在“MOC”参数设置为“VLR(VLR)”时：“PERF_TYPE_SGS_WITH_SPECIFIC_VLR(指定VLR的SGs基本业务)” 该参数在“MOC”参数设置为“DNS_INQUIRY(DNS查询)”时：“PERF_TYPE_DNS_INQUIRY(DNS服务器查询)” 该参数在“MOC”参数设置为“DIAMETER_LINK(Diameter链路)”时：“PERF_TYPE_DIAMETER_LINK(Diameter链路)”“PERF_TYPE_DIAMETER_LINKSET_S1_MODE_LOCATION_UPDATE(指定Diameter链路S1模式位置更新)”“PERF_TYPE_DIAMETER_LINKSET_S1_MODE_AUTHENTICATION(指定Diameter链路S1模式信息鉴权)” 该参数在“MOC”参数设置为“DIAMETER_LINKSET(Diameter链路集)”时：“PERF_TYPE_DIAMETER_LINKSET(Diameter链路集)” 该参数在“MOC”参数设置为“SCTP_LNK(SCTP链路)”时：“PERF_TYPE_SCTP_LINK_S1_MODE_SCTP_LINK_TRANSFER(指定SCTP链路S1模式SCTP链路转发)” 该参数在“MOC”参数设置为“VM_USN(虚拟机)”时：“PERF_TYPE_VM_LINK(虚拟机资源_LINK)”“PERF_TYPE_GTPC_VM_MSG_SPECS(虚拟机级信令面消息处理统计)” 该参数在“MOC”参数设置为“RU(资源单元)”时：“PERF_TYPE_RU_CPU_RESOURCE(资源单元CPU资源_LINK)” 该参数在“MOC”参数设置为“ScalGroup(ScalGroup)”时:“PERF_TYPE_SCALEGROUP_WORKLOAD(ScalGroup负载_LINK)” 默认值：无 |

#### 使用实例

查询“虚拟机”对象的“虚拟机资源\_LINK”单元下的所有指标的当前实时统计值：

DSP RTMPERFCNTLINK: MOC=VM\_USN, MOI="SPU\_B\_0066", MUID=PERF\_TYPE\_VM\_LINK;

```
%%DSP RTMPERFCNTLINK: MOC=VM_USN, MOI="SPU_B_0066", MUID=PERF_TYPE_VM_LINK;%%
RETCODE = 0  操作成功。

操作结果如下
----------
                                             测量对象 = 虚拟机
                                     测量对象实例名称 = SPU_B_0066
                                             测量单元 = 虚拟机资源_LINK
                                             测量结果 = Result is Reliable!
       基于虚拟机的SGsAP Location Update请求次数(次) = 0
       基于虚拟机的SGsAP Location Update成功次数(次) = 0
                    
(结果个数 = 2)
---    END
```

#### 参考信息

| 测量对象类                                          | 对象实例数据获取参考             | 对象实例输入格式                  | 输入格式示例                                     |
|:-----------------------------------------------|:-----------------------|:--------------------------|:-------------------------------------------|
| GNGPIP：GnGp IP                                 | 对端GGSN/S-GW GTPC地址     | GnGp接口IP地址                | "192.168.41.11"                            |
| SGSN：USN function                              | 0                      | "0"                       | "0"                                        |
| M3UA_LNK：M3UA链路                                | LST CPM3LNK            | 链路号                       | "1"                                        |
| M3UA_LNKSET：M3UA链路集                            | LST CPM3LKS            | 链路集索引                     | "1"                                        |
| M3UA_DE：M3UA目的实体                               | LST CPM3DE             | 目的实体索引                    | "1"                                        |
| VLR：VLR                                        | LST VLR                | VLR号                      | "86139019201"                              |
| DNS_INQUIRY：DNS查询                              | LST DNSS               | IPV4地址                    | "192.168.41.11"                            |
| DIAMETER_LINK：Diameter链路                       | LST CPDMLNK            | 链路号                       | "1"                                        |
| DIAMETER_LINKSET：Diameter链路集                   | LST CPDMLKS            | 链路集索引                     | "1"                                        |
| SCTP_LNK：SCTP链路                                | LST S1APLE和DSP S1APLNK | 本端IP地址：本端端口号：对端IP地址：对端端口号 | "192.168.152.1:31201:192.168.152.20:31201" |
| VM_USN：虚拟机  说明： 此对象在Full-Stack裸机及三方CaaS场景下不生效。 | DSP NODE               | 虚拟机名称                     | "SPU_B_0066"                               |
| RU: 资源单元                                       | DSP RU                 | 资源单元名称                    | "LINK_SP_RU_0064"                          |
| ScalGroup:ScalGroup 名字                         | DSP WORKLOAD           | ScaleGroup的名字             | "SG1_LINK"                                 |