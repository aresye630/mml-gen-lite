# 设置S1模式eMTC SM协议参数（SET EMTCBESM）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于设置S1模式CE Mode B（一种eMTC终端）用户的SM协议参数。

当网络中有CE Mode B终端处于无线信号覆盖较差的区域导致业务流程成功率较低时，可通过本命令调大定时器时长以改善业务成功率。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-------|:--------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T3485  | T3485 （s）     | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3485的时长。此定时器在MME发送ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST时启动。在收到UE发回的ACTIVATE DEFAULT EPS BEARER ACCEPT、ACTIVATE DEFAULT EPS BEARER REJECT、ACTIVATE DEDICATED EPS BEARER ACCEPT或ACTIVATE DEDICATED EPS BEARER REJECT时停止。如果超时会重发ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息，重启定时器，重发次数由参数“N3485”确定。如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就释放已经分配的资源，启动此定时器的流程结束。 数据来源：全网规划 取值范围：3~48 系统初始设置值：16 |
| N3485  | N3485 （times） | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3485超时后ACTIVATE DEFAULT EPS BEARER CONTEXT REQUEST或ACTIVATE DEDICATED EPS BEARER CONTEXT REQUEST消息的重发次数。 数据来源：全网规划 取值范围：0~5 系统初始设置值：4  说明： “0times”表示不进行重发。                                                                                                                                                                                                                                                                                                                              |
| T3486  | T3486 （s）     | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3486的时长。此定时器在MME发送MODIFY EPS BEARER CONTEXT REQUEST时启动。在收到UE发回的MODIFY EPS BEARER CONTEXT ACCEPT或MODIFY EPS BEARER CONTEXT REJECT时停止。如果超时会重发MODIFY EPS BEARER CONTEXT REQUEST消息用于重启定时器，重发次数由参数“N3486”确定。如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME中承载上下文保持为激活态，启动此定时器的流程结束。 数据来源：全网规划 取值范围：3~48 系统初始设置值：16                                                                                                                                                                                            |
| N3486  | N3486 （times） | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3486的超时后MODIFY EPS BEARER CONTEXT REQUEST消息的重发次数。 数据来源：全网规划 取值范围：0~5 系统初始设置值：4  说明： “0”表示不进行重发。                                                                                                                                                                                                                                                                                                                                                                                          |
| T3489  | T3489 （s）     | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3489的时长。此定时器在MME给UE发ESM INFORMATION REQUEST消息时启动。在收到UE响应消息ESM INFORMATION RESPONSE停止。如果超时会重发ESM INFORMATION REQUEST消息用于重启定时器，重发次数由参数“N3489”确定。如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就释放相应资源，启动此定时器的流程结束。 数据来源：全网规划 取值范围：3~48 系统初始设置值：12                                                                                                                                                                                                                                                          |
| N3489  | N3489 （times） | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3489的超时后ESM INFORMATION REQUEST消息的重发次数。 数据来源：全网规划 取值范围：0~5 系统初始设置值：2  说明： “0”表示不进行重发。                                                                                                                                                                                                                                                                                                                                                                                                    |
| T3495  | T3495 （s）     | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3495的时长。此定时器在MME在发送DEACTIVATE EPS BEARER CONTEXT REQUEST消息时启动。在收到UE响应DEACTIVATE EPS BEARER CONTEXT ACCEPT消息停止。如果超时会重发DEACTIVATE EPS BEARER CONTEXT REQUEST消息用于重启定时器，重发次数由参数“N3495”确定。如果重发次数达到配置的最大次数仍没有收到UE响应消息，MME就去激活EPS承载上下文，启动此定时器的流程结束。 数据来源：全网规划 取值范围：3~48。 系统初始设置值：16                                                                                                                                                                                                             |
| N3495  | N3495 （times） | 可选必选说明：可选参数 参数含义：该参数用于指定定时器T3495超时后DEACTIVATE EPS BEARER CONTEXT REQUEST消息的重发次数。 数据来源：全网规划 取值范围：0~5 系统初始设置值：4  说明： “0”表示不进行重发。                                                                                                                                                                                                                                                                                                                                                                                       |

#### 使用实例

如果终端的无线信号覆盖好，设置S1模式eMTC SM协议参数“T3485 (s)”为“3”，“N3485 (times)”为“1”，“T3486 (s)”为“3”，“N3486 (times)”为“1”，“T3489 (s)”为“3”，“N3489 (times)”为“1”，“T3495 (s)”为“3”，“N3495 (times)”为“1”：

`SET EMTCBESM: T3485=3, N3485=1, T3486=3, N3486=1, T3489=3, N3489=1, T3495=3, N3495=1;`

如果终端的无线信号覆盖差，需调大定时器时长，设置S1模式eMTC SM协议参数“T3485 (s)”为“48”，“N3485 (times)”为“5”，“T3486 (s)”为“48”，“N3486 (times)”为“5”，“T3489 (s)”为“48”，“N3489 (times)”为“5”，“T3495 (s)”为“48”，“N3495 (times)”为“5”：

`SET EMTCBESM: T3485=48, N3485=5, T3486=48, N3486=5, T3489=48, N3489=5, T3495=48, N3495=5;`