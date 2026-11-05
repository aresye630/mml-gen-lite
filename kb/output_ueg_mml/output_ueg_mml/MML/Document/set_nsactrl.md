# 设置NSA控制参数(SET NSACTRL)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于设置NSA组网场景下的整系统控制参数。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug。

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组。

#### 参数说明

| 参数标识        | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NRUSERPT    | NR流量上报               | 可选必选说明：可选参数 参数含义：该参数用于控制MME是否启用NR（New Radio）流量上报功能。NSA组网场景下，MME支持将来自eNodeB的NR流量统计报告发送给S-GW/P-GW。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 系统初始设置值：“NO（否）”。 默认值：无 配置原则：如果需要针对NR（5G）流量单独计费，可以将该参数置为“YES（是）”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| NCNRFORPEER | DNS查询对等网元时是否携带NCNR标志 | 可选必选说明：可选参数 参数含义：本参数用以控制NSA用户跨Pool切换，且目标侧是MME和5G MME混合Pool场景下，源侧MME通过DNS查询对等网元（即目标侧MME）时是否使用NCNR作为查询条件。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 系统初始设置值：“NO（否）”。 默认值：无 配置原则：本开关需要跟DNS服务器上配置的MME DNS记录相匹配。只有DNS服务器按照TAI+NCNR配置了MME DNS记录，才能打开本开关。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TRAFFICDIFF | 流量区分                 | 可选必选说明：可选参数 参数含义：该参数用于控制是否开启无线地址类型区分功能。功能开启后，MME会根据用户承载使用的无线侧地址类型（gNodeB地址或者eNodeB地址）识别NSA用户。 数据来源：全网规划 取值范围：枚举类型。 “NO(否)”“YES(是)” 系统初始设置值：“NO(否)” 默认值：无 配置原则： 如果需要MME根据用户承载使用的无线侧地址类型（gNodeB地址或者eNodeB地址）识别NSA用户，可以将该参数置为“YES(是)”。 说明： 该功能为局点定制功能。该功能开启后，需要将软参BYTE_EX_B41 BIT7设置为“1”来适配NSA相关性能指标统计。                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NRTYPE      | MME通知HSS是否为NSA用户的方式  | 可选必选说明：可选参数 参数含义：该参数用于控制MME通知HSS是否为NSA用户的应用场景。 数据来源：本端规划 取值范围：枚举类型。 OFF(功能关闭)：不支持通过Notify request消息携带RAT TYPE通知HSS用户类型。 TRAFFIC(流量分区)：当MME根据上报NR流量报告识别NSA用户后，通过在Notify request消息中携带RAT TYPE向HSS通知用户类型。 IPTYPE(无线地址类型区分)：当MME根据用户承载使用的无线侧地址类型（gNodeB地址或者eNodeB地址）识别NSA用户后，通过在Notify request消息中携带RAT TYPE向HSS通知用户类型。 配置原则：只有当ADD DMCMPTBYIMSI和SET DMCMPT中“是否支持NOR消息上报RAT TYPE”设置为"支持"的场景下，该参数功能才生效。 系统初始设置值：OFF(功能关闭) 默认值：无  说明： 开启该功能后，可以使用软参BYTE_EX_B35对用于通知HSS是否NSA用户的Notify Request消息进行流控。该参数设置为“TRAFFIC(流量分区)”时，如果软参BYTE_EX_B34 BIT5设置为“1”，该参数功能不生效。软参BYTE_EX_B34 BIT5用于控制MME针对本网用户是否通知HSS当前用户为NSA用户，该软参优先级高于“TRAFFIC(流量分区)”。该参数设置为“IPTYPE(无线地址类型区分)”时，需要先将“TRAFFICDIFF（流量区分）”参数设置为“YES(是)”，否则该参数功能不生效。                                                                     |
| PSCELLIDCLR | PSCell ID消息清除选项      | 可选必选说明：可选参数 参数含义：该参数用于控制在对应消息流程中不携带PSCell Information信元时，MME是否清除本地存储的PSCell信息。 数据来源：全网规划 取值范围： UE CONTEXT RELEASE COMPLETE（UE CONTEXT RELEASE COMPLETE）UE CONTEXT SUSPEND REQUEST（UE CONTEXT SUSPEND REQUEST）HANDOVER NOTIFY（HANDOVER NOTIFY）PATH SWITCH REQUEST（PATH SWITCH REQUEST）UPLINK NAS TRANSPORT（UPLINK NAS TRANSPORT）LOCATION REPORT（LOCATION REPORT）SECONDARY RAT DATA USAGE REPORT（SECONDARY RAT DATA USAGE REPORT）E-RAB MODIFICATION INDICATION（E-RAB MODIFICATION INDICATION）E-RAB SETUP RESPONSE（E-RAB SETUP RESPONSE）E-RAB MODIFY RESPONSE（E-RAB MODIFY RESPONSE）E-RAB RELEASE RESPONSE（E-RAB RELEASE RESPONSE）E-RAB RELEASE INDICATION（E-RAB RELEASE INDICATION） 系统初始设置值：“NULL”，即所有消息均不勾选。 默认值：无 配置原则：勾选消息后，对应消息中不携带PSCell Information信元时，MME清除本地存储的PSCell信息。 |

#### 使用实例

设置“NR流量上报”和“DNS查询对等网元时是否携带NCNR标志”为“NO（否）”：

```
SET NSACTRL: NRUSERPT = NO,NCNRFORPEER = NO;
```