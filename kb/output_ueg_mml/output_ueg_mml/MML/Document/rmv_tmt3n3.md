# 删除Tm接口指定消息T3N3参数(RMV TMT3N3)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

本命令用于删除指定Tm接口消息T3N3参数。不能用于删除TM路径的T3和N3系统初始设置值，初始设置值请在**ADD TMT3N3**命令查看。

#### 注意事项

- 该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------------|:---------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TMSPECIALMSGCFG | 指定Tm接口消息 | 可选必选说明：必选参数 参数含义：指定具体的Tm接口消息设置T3N3参数。 数据来源：全网规划 取值范围：“SPECIAL_TM_MSG（指定Tm接口消息）” 默认值 ：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| TMMSG           | Tm接口消息   | 可选必选说明：条件必选参数 前提条件：该参数在“指定Tm接口消息”参数配置为“SPECIAL_TM_MSG”后生效。 参数含义：Tm接口消息列表。 数据来源：全网规划 取值范围：“ECHO（Echo Request）”“STRT_ENB_TA_INFO_UPDATE_REQ（Start eNB TA Information Update Request）”“UPDATE_ENB_TA_INFO_REQ（Update eNodeB TA Information Request）”“TRK_GP_UL_S1_DT_NTF（Trunk Group UL S1 Direct Transfer Notification）”“TRK_USR_ATT_REQ（Trunk User Attach Request）”“TRK_USR_DET_REQ（Trunk User Detach Request）”“TRK_USR_HO_REQ（Trunk User Handover Request）”“TRK_USR_HO_NTF（Trunk User Handover Notification）”“TRK_USR_TAU_REQ（Trunk User TAU Request）”“TRK_USR_SR_REQ（Trunk User Service Request）”“NODE_ST_NTF（NE Status Notification）” 默认值 ：无 |

#### 使用实例

删除Tm接口Trunk User Attach Request消息T3N3参数：

```
RMV TMT3N3: TMSPECIALMSGCFG=SPECIAL_TM_MSG, TMMSG=TRK_USR_ATT_REQ;
```