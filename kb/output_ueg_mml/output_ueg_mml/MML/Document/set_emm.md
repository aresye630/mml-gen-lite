# 设置S1模式MM协议参数(SET EMM)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于设置4G移动性管理参数。

#### 注意事项

- 该命令执行后立即生效。
- 针对特定TA List配置定时器（**ADD TALSTPAGINGPLCY** 命令中“是否配置定时器”值为“YES(是)”）后，该TA List范围内的寻呼**SET EMM**中配置的“T3413” “N3413” “PAGINGDELTA”参数失效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| T3422           | T3422（s）            | 可选必选说明：可选参数 参数含义：此定时器用于控制MME发起分离请求消息与UE响应的时间间隔。此定时器在MME发送Detach request消息时启动，在收到Detach Accept消息时停止，超时后MME会重发Detach request消息。 数据来源：整网规划 取值范围：3s~12s 系统初始设置值：6s。                                                                                                                                                                                            |
| N3422           | N3422（times）        | 可选必选说明：可选参数 参数含义：该参数用于指定MME发送Detach request消息时没有收到UE的响应消息，MME重发Detach request消息的次数。 数据来源：整网规划 取值范围：0times~5times 系统初始设置值：4times。                                                                                                                                                                                                                           |
| T3450           | T3450（s）            | 可选必选说明：可选参数 参数含义：此定时器用于控制MME发起接受附着、跟踪区更新流程与UE响应流程成功的时间间隔。此定时器在MME发送Attach accept、TAU accept、GUTI rellocation command启动，在收到Attach complete、TAU complete、GUTI rellocation complete停止，超时后，MME将重发Attach accept、TAU accept、GUTI rellocation command消息。 数据来源：整网规划 取值范围：3s~12s 系统初始设置值：6s。                                                                        |
| N3450           | N3450（times）        | 可选必选说明：可选参数 参数含义：该参数用于指定在用户附着、跟踪区更新流程中没有收到UE的响应消息，MME重复发送Attach accept、TAU accept、GUTI rellocation command消息的次数。 数据来源：整网规划 取值范围：0times~5times 系统初始设置值：4times。                                                                                                                                                                                              |
| T3460           | T3460（s）            | 可选必选说明：可选参数 参数含义：此定时器用于控制网络侧发起鉴权加密流程与手机侧响应的时间间隔。在网络侧发送Authentication Request或Security Mode Command消息启动，在收到Autentication Response或Security Mode Complete消息停止，超时后，MME将重发Authentication Request或Security Mode Command消息。 数据来源：整网规划 取值范围：3s~12s 系统初始设置值：6s。                                                                                                    |
| N3460           | N3460（times）        | 可选必选说明：可选参数 参数含义：该参数用于指定在鉴权或安全流程中，没有收到UE的响应消息，MME重复发送Authentication Request、Security Mode Command消息的次数。 数据来源：整网规划 取值范围：0times~5times 系统初始设置值：4times。                                                                                                                                                                                                       |
| T3470           | T3470（s）            | 可选必选说明：可选参数 参数含义：此定时器用于控制MME发起身份识别与UE响应的时间间隔。在MME发送Identity request消息时启动，在收到Identity Response消息时停止，超时后，MME将重发Identity request消息。 数据来源：整网规划 取值范围：3s~12s 系统初始设置值：6s。                                                                                                                                                                                         |
| N3470           | N3470（times）        | 可选必选说明：可选参数 参数含义：该参数用于指定身份识别请求消息重发次数。 数据来源：整网规划 取值范围：0times~5times 系统初始设置值：4times。                                                                                                                                                                                                                                                                         |
| T3412           | T3412（min）          | 可选必选说明：可选参数 参数含义：此定时器用于控制UE自动发起周期性跟踪区更新流程的时间间隔。在UE从ECM-CONNECTED变为ECM-IDLE时启动，超时后，UE发起跟踪区更新流程。 数据来源：整网规划 取值范围：1min~186min 系统初始设置值：54min。 配置原则：此定时器时长应小于“移动可达定时器(min)”时长。  说明： 该定时器的取值范围为离散值，根据3gpp规范24.008的10.5.7.3章节中定义的取值规则如下：当范围为1min~31min，间隔为1min；当范围为36min-186min，间隔为6min。增加T3412(min)的值会减少ECM-CONNECTED附着用户数、增加ECM-IDLE附着用户数、减少周期TAU请求次数、增加寻呼次数。    |
| T3402           | T3402（min）          | 可选必选说明：可选参数 参数含义：该定时器用于控制UE Attach/TAU重试的时长。 数据来源：整网规划 取值范围：1min~186min 系统初始设置值：12min。 说明：该定时器的取值范围为离散值，根据3gpp规范24.008的10.5.7.3章节中定义的取值规则如下：当范围为1min~31min，间隔为1min；当范围为36min-186min，间隔为6min。  说明： 增加T3402(min)的值会减少附着请求次数、减少附着失败次数、提高附着成功率、减少TAU请求次数、减少TAU失败次数、提高TAU成功率。                                                                                   |
| T3413           | T3413（s）            | 可选必选说明：可选参数 参数含义：此定时器用于控制MME发起寻呼与UE响应的时间间隔。在MME发送Paging Request消息后启动，在收到Service Request消息后停止，超时后，MME重发Paging Request消息。 数据来源：整网规划 取值范围：3s~12s 系统初始设置值：6s。  说明： 增加T3413(s)的值可能会提高寻呼成功率。                                                                                                                                                                     |
| N3413           | N3413（times）        | 可选必选说明：可选参数 参数含义：该参数用于指定在寻呼流程中，没有收到UE的响应消息，MME重复发送Paging Request消息的最大次数。 数据来源：整网规划 取值范围：0times~5times 系统初始设置值：2times。  说明： 增加N3413(times)的值可能会提高寻呼成功率。本参数不包含在一次寻呼流程中对UE的第一次寻呼。                                                                                                                                                                             |
| PAGINGDELTA     | 重寻呼间隔递增值（s）         | 可选必选说明：可选参数 参数含义：该参数用于指定在寻呼流程中，没有收到Service Request消息，MME重复发送Paging Request消息的间隔递增时间值。 数据来源：整网规划 取值范围：0s~20s 系统初始设置值：0s。  说明： 增加重寻呼间隔递增值(s)可能会提高寻呼成功率。                                                                                                                                                                                                      |
| HPT3413         | 高优先级业务的T3413（s）     | 可选必选说明：可选参数 参数含义：此定时器用于控制高优先级业务的MME发起寻呼与UE响应的时间间隔。在MME发送Paging Request消息后启动，在收到Service Request消息后停止，超时后，MME重发Paging Request消息。 数据来源：整网规划 取值范围：1s~12s 系统初始设置值：2s。 配置原则：如下几个业务流程将使用本参数的配置，其他业务的被叫寻呼仍使用“T3413(s)”、“N3413(times)”、“重寻呼间隔递增值(s)”的参数。VoLTE紧急呼叫VoLTE普通语音业务  说明： 增加“高优先级业务的T3413(s)”的值可能会提高寻呼成功率。                                                  |
| HPN3413         | 高优先级业务的N3413（times） | 可选必选说明：可选参数 参数含义：该参数用于指定在高优先级业务的寻呼流程中，没有收到UE的响应消息，MME重复发送Paging Request消息的最大次数。 数据来源：整网规划 取值范围：0times~10times 系统初始设置值：4times。 配置原则：如下几个业务流程将使用本参数的配置，其他业务的被叫寻呼仍使用“T3413(s)”、“N3413(times)”、“重寻呼间隔递增值(s)”的参数。VoLTE紧急呼叫VoLTE普通语音业务  说明： 增加“高优先级业务的N3413(times)”的值可能会提高寻呼成功率。                                                                                 |
| HPPAGINGDELTA   | 高优先级业务的重寻呼间隔递增值（s）  | 可选必选说明：可选参数 参数含义：该参数用于指定在高优先级业务的寻呼流程中，没有收到Service Request消息，MME重复发送Paging Request消息的间隔递增时间值。 数据来源：整网规划 取值范围：0s~20s 系统初始设置值：0s。 配置原则：如下几个业务流程将使用本参数的配置，其他业务的被叫寻呼仍使用“T3413(s)”、“N3413(times)”、“重寻呼间隔递增值(s)”的参数。VoLTE紧急呼叫VoLTE普通语音业务  说明： 增加“高优先级业务的重寻呼间隔递增值(s)”的值可能会提高寻呼成功率。                                                                                 |
| RCHTMR          | 移动可达定时器（min）        | 可选必选说明：可选参数 参数含义：此定时器用于监测UE发起周期性TAU，在用户的NAS信令连接释放时启动，在NAS信令连接建立时停止，超时后，如果UE还没有发起周期性TAU，则启动不可达用户隐式分离定时器。 数据来源：整网规划 取值范围：2min~198min 系统初始设置值：58min。 配置原则：此定时器时长应大于“T3412(min)”时长。  说明： 增加移动可达定时器(min)的值会增加ECM-IDLE附着用户数、减少DEREGISTERED态用户数、增加寻呼次数。当启用M2M长周期性定时器功能后，如果UE支持长周期RAU/TAU定时器，则本参数的值将自动调整为DSP MMCTX命令的参数“使用的周期RAU-TAU定时器（分钟）”的值加上4分钟                |
| IMDTCHTMR       | 不可达用户隐式分离定时器（min）   | 可选必选说明：可选参数 参数含义：此定时器用于移动可达定时器超时后保持一段时间用户信息。移动可达定时器超时时，MME认为用户脱离了网络覆盖范围，但无法明确脱离时间，所以MME不能立即隐式分离用户，启动不可达用户隐式分离定时器。该定时器启动期间，MME拒绝网络侧对UE的寻呼。如果用户在不可达用户隐式分离定时器超时时仍未连上网络，则MME认为用户已经离开网络覆盖范围很长一段时间了并隐式分离用户。 数据来源：整网规划 取值范围：0min~198min 系统初始设置值：0min。 配置原则：当参数设置为0min，表示移动可达定时器超时时立即隐式分离用户。  说明： 增加不可达用户隐式分离定时器(min)的值会增加ECM-IDLE附着用户数、减少DEREGISTERED态用户数、增加寻呼次数。 |
| GUTITMR         | GUTI重分配定时器（h）       | 可选必选说明：可选参数 参数含义：此定时器用于控制GUTI重分配时长。在UE进入CONNECT态时启动定时器，如果用户一直处于在CONNECT态并且持续时间超过本定时器，则进行GUTI重分配；如果UE切换到IDLE态，则关闭定时器，等用户下次进入CONNECT态则会重新启动定时器。 数据来源：整网规划 取值范围：0h~24h 系统初始设置值：0h。 配置原则：当参数设置为0h，表示不会启动GUTI重分配定时器。                                                                                                                                            |
| GUTIREALLOC     | Attach或TAU中重分配GUTI  | 可选必选说明：可选参数 参数含义：该参数用来指定在Attach和TAU时，是否重分配GUTI。 数据来源：整网规划 取值范围：“NO(不重分配GUTI)”“YES(重分配GUTI)” 系统初始设置值：“YES(重分配GUTI)”。                                                                                                                                                                                                                                        |
| HOPRETMR        | Handover准备定时器（s）    | 可选必选说明：可选参数 参数含义：此定时器用于控制MME等待HANDOVER REQUEST ACK消息的时间间隔。此定时器在向目标eNodeB发送HANDOVER REQUEST消息以后启动，在收到目标eNodeB的HANDOVER REQUEST ACK消息后停止，超时后，向源eNodeB发送HANDOVER准备失败消息。 数据来源：整网规划 取值范围：5s~15s 系统初始设置值：10s。                                                                                                                                                    |
| HOCMPSRCTMR     | 源侧Handover完成定时器（s）  | 可选必选说明：可选参数 参数含义：此定时器用于控制源侧MME切换完成的时间。此定时器在向源eNodeB发送Handover Command以后启动，在收到目标MME的Forward Relocation Complete消息后停止，超时后，将释放用户信息。 数据来源：整网规划 取值范围：5s~15s 系统初始设置值：10s。                                                                                                                                                                                        |
| HOCMPTGTTMR     | 目标侧Handover完成定时器（s） | 可选必选说明：可选参数 参数含义：此定时器用于控制目标侧MME切换完成的时间。此定时器在向源MME发送Forward Relocation Response后启动，在收到目标eNodeB的Handover Notify消息后停止，超时后，将释放用户信息。 数据来源：整网规划 取值范围：5s~15s 系统初始设置值：10s。                                                                                                                                                                                         |
| T3              | T3定时器（s）            | 可选必选说明：可选参数 参数含义：此参数用于指定T3定时器时长。在以下场景中会触发T3定时器： Inter TAU中老侧MME向新侧MME发送上下文响应(Context Response)消息时； 当T3定时器超时时，MME将删除相应的老侧数据及承载资源。 数据来源：整网规划 取值范围：3s~60s 系统初始设置值：10s。                                                                                                                                                                                        |
| GUTITMRFORDEBUG | 测试用GUTI重分配定时器（min）  | 可选必选说明：可选参数 参数含义：该参数描述的是内部测试用的GUTI重新分配的定时器参数对应值。 数据来源：整网规划 取值范围：0min~254min 系统初始设置值：0min。                                                                                                                                                                                                                                                                  |
| HOT3            | 切换流程资源释放定时器（s）      | 可选必选说明：可选参数 参数含义：此参数用于指定HOT3定时器时长。在以下场景中会触发HOT3定时器： Inter HO中老侧MME收到Forward Relocation Complete消息时；Inter HO中新侧MME收到老侧MME的Forward Relocaton Complete Ack消息并且之前已在新侧SGW创建间接承载时；Intra HO中MME收到Handover Notify消息时；X2-Based HO中若SGW改变，在MME收到新侧SGW的Create Session Response消息时。 当HOT3定时器超时时，MME将删除相应的老侧数据及承载资源。 数据来源：整网规划 取值范围：1s~60s 系统初始设置值：2s。                  |
| GUTIREALLOCTMR  | GUTI重分配最大间隔（h）      | 可选必选说明：可选参数 参数含义：该参数用于指定GUTI重分配最大间隔。 数据来源：整网规划 取值范围：0~24 系统初始设置值：0 配置原则：当参数设置为0时，GUTI重分配最大间隔功能不启用。  说明： 在Attach/TAU/GUTI Reallocation流程中，当MME为用户分配GUTI后，启动一个随机定时器，在随机定时器超时且用户处于连接态时，则MME为用户重新分配一个新的GUTI。当参数不为0时，系统默认随机定时器的下限值为0.5小时，上限为本参数“GUTI重分配最大间隔”设定值；随机定时器定时时长为下限值和上限值中间的随机值；下限值为0.5h是为了防止GUTI频繁更新，影响系统性能。                                           |

#### 使用实例

设置EMM参数，T3422为6s，N3422为4次，T3450为6s，N3450为4times，T3460为6s，N3460为4times，T3470为6s，N3470为4times，T3412为54min，T3402为12min，T3413为6s，N3413为2times，PAGINGDELTA为0，HPT3413为2s，HPN3413为4times，HPPAGINGDELTA为1s，RCHTMR为58min，IMDTCHTMR为0min，GUTITMR为0h，GUTIREALLOC为“YES”，HOPRETMR为10s，HOCMPSRCTMR为10s，HOCMPTGTTMR为10s，T3为10s：

SET EMM: T3422=6, N3422=4, T3450=6, N3450=4, T3460=6, N3460=4, T3470=6, N3470=4, T3412=54, T3402=12, T3413=6, N3413=2, PAGINGDELTA=0, HPT3413=2, HPN3413=4, HPPAGINGDELTA=1, RCHTMR=58, IMDTCHTMR=0, GUTITMR=0, GUTIREALLOC=YES, HOPRETMR=10, HOCMPSRCTMR=10, HOCMPTGTTMR=10, T3=10;