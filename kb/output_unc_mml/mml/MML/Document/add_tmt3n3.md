# 增加Tm接口指定消息T3N3参数(ADD TMT3N3)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：MME**

本命令用于增加Tm接口消息T3N3参数。

#### 注意事项

- 该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称             | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------------|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMSPECIALMSGCFG | 指定Tm接口消息         | 可选必选说明：必选参数 参数含义：指定具体的Tm接口消息设置T3N3参数。 数据来源：全网规划 取值范围：“SPECIAL_TM_MSG（指定Tm接口消息）” 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TMMSG           | Tm接口消息           | 可选必选说明：条件必选参数 前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。 参数含义：Tm接口消息列表。 数据来源：全网规划 取值范围：“ECHO（Echo Request）”“STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”“UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”“TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”“TRK_USR_ATT_REQ（Trunk User Attach Request）”“TRK_USR_DET_REQ（Trunk User Detach Request）”“TRK_USR_HO_REQ（Trunk User Handover Request）”“TRK_USR_HO_NTF（Trunk User Handover Notification）”“TRK_USR_TAU_REQ（Trunk User TAU Request）”“TRK_USR_SR_REQ（Trunk User Service Request）”“NODE_ST_NTF（NE Status Notification）” 默认值 ：无 |
| TRSP            | T-RESPONSE(s)    | 可选必选说明：必选参数 参数含义：该参数用于指定等待一条T3请求消息的响应消息的最大时长。如果请求消息没有在“TRSP”内收到响应，并且发送次数小于“NREQ”，则重新发送该请求消息。 数据来源：全网规划 取值范围：1~20 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| NREQ            | N-REQUEST(times) | 可选必选说明：必选参数 参数含义：该参数用于指定Tm接口发送一条请求消息的最大尝试次数。 数据来源：本端规划 取值范围：1~5 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### 使用实例

该命令用于增加Tm接口指定消息T3N3参数，执行如下命令：

```
ADD TMT3N3:TMSPECIALMSGCFG=SPECIAL_TM_MSG,TMMSG=ECHO,TRSP=3,NREQ=2;
```

#### 参考信息

| Tm接口消息配置模式   | Tm接口消息                      |   T-RESPONSE(s) |   N-REQUEST(times) |
|:-------------|:----------------------------|----------------:|-------------------:|
| 指定Tm接口消息     | Echo Request                |               5 |                  3 |
| Tm接口消息全集     | nan                         |               2 |                  2 |
| 指定Tm接口消息     | Trunk User Handover Request |               8 |                  2 |
| 指定Tm接口消息     | NE Status Notification      |               5 |                  1 |

**注：Tm接口消息全集指TMMSG参数中除去****Echo Request、Trunk User Handover Request、NE Status Notification消息外****的所有消息。当配置中没有Tm接口消息全集中某个消息配置时，将会使用本条配置的数值。**