# 修改Tm接口消息T3N3参数(MOD TMT3N3)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

本命令用于修改Tm接口消息T3N3参数。

#### 注意事项

- 该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称             | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------------|:-----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMMSGCFGMODE | Tm接口消息配置模式       | 可选必选说明：必选参数 参数含义：本参数用于选择Tm接口消息配置方式。 数据来源：全网规划 取值范围：“TMMSG_ALL（Tm接口消息全集）”“SPECIAL_TM_MSG（指定Tm接口消息）” 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TMMSG        | Tm接口消息           | 可选必选说明：条件必选参数 前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。 参数含义：Tm接口消息列表。 数据来源：全网规划 取值范围：“ECHO（Echo Request）”“STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”“UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”“TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”“TRK_USR_ATT_REQ（Trunk User Attach Request）”“TRK_USR_DET_REQ（Trunk User Detach Request）”“TRK_USR_HO_REQ（Trunk User Handover Request）”“TRK_USR_HO_NTF（Trunk User Handover Notification）”“TRK_USR_TAU_REQ（Trunk User TAU Request）”“TRK_USR_SR_REQ（Trunk User Service Request）”“NODE_ST_NTF（NE Status Notification）” 默认值 ：无 |
| TRSP         | T-RESPONSE(s)    | 可选必选说明：可选参数 参数含义：该参数用于指定等待一条T3请求消息的响应消息的最大时长。如果请求消息没有在“TRSP”内收到响应，并且发送次数小于“NREQ”，则重新发送该请求消息。 数据来源：全网规划 取值范围：1~20 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| NREQ         | N-REQUEST(times) | 可选必选说明：可选参数 参数含义：该参数用于指定Tm接口发送一条请求消息的最大尝试次数。 数据来源：本端规划 取值范围：1~5 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

#### 使用实例

修改Tm消息类型为用户会话类消息，在7s内，MME发送一条请求消息的最大尝试数为2次：

```
MOD TMT3N3: TMMSGCFGMODE=TMMSG_ALL, TRSP=7, NREQ=2;
```