# 设置Sdup消息重传参数(SET SDAPRETRSMT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

本命令用于控制Sdup接口的消息传输可靠性管理的参数。

#### 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为4。
- 恢复管理类消息的T-Response和N-Request数值配置，需要结合对应的端到端业务流程的时间决定。
- 链路管理类消息的T-Response和N-Request数值配置，（T-Response\*N-Request）的结果应小于“Sdup接口探测间隔时长”，此参数见**SET SDAPINTF**。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SMSGCLS | Sdup接口消息分类 | 可选必选说明：必选参数 参数含义：本参数用于选择Sdup接口消息分类。 数据来源：本端规划 取值范围：“LNKM(链路管理类消息)”，包括“SDAP Echo Request”。“DUPM(备份管理类消息)”，包括“Create User Information Request”、“Update User Information Request”、“Delete User Information Request”、“Create Subscription Information Request”、“Update Subscription Information Request”、“Delete Subscription Information Request”。“RESM(恢复管理类消息)”，包括“Restore User Information Request”、“IDR Information Inquiry Request”、“Paging Information Inquiry Request”、“Subscription Data Inquiry Request”。“OTHERS(其他消息)”，包括“Restart Notification”。 系统初始设置值：无 |
| TRSP    | T-RESPONSE | 可选必选说明：可选参数 参数含义：该参数用于指定等待消息响应的时长。如果发送的请求消息在“T-RESPONSE”的时间内未收到响应，并且发送次数小于“N-REQUEST”，则重新发送该请求消息。 数据来源：本端规划 取值范围：1s~10s 系统初始设置值：见“说明”  说明： T-RESPONSE的初始值： 链路管理类消息：5备份管理类消息：5恢复管理类消息：1其他消息：5                                                                                                                                                                                                                                                                                                                                                                      |
| NREQ    | N-REQUEST  | 可选必选说明：可选参数 参数含义：该参数用于指定请求消息的最大发送次数。 数据来源：本端规划 取值范围：1~5 系统初始设置值：见“说明”  说明： T-RESPONSE的初始值： 链路管理类消息：4备份管理类消息：4恢复管理类消息：1其他消息：4                                                                                                                                                                                                                                                                                                                                                                                                                                      |

#### 使用实例

当TRSP=1, NREQ=1，设置Sdup接口的消息传输可靠性管理的参数：

SET SDAPRETRSMT: SMSGCLS=RESM, TRSP=1, NREQ=1;