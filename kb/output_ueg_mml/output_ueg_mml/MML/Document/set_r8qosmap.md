# 设置EPS QoS参数到Pre-R8 QoS参数映射规则（SET R8QOSMAP）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

**适用网元：MME**

此命令用于设置EPS QoS参数到Pre-R8 QoS参数的映射规则。在GUL互操作中，从4G网络向2/3G网络切换的时候，MME会根据配置的映射规则，将4G中使用的EPS QoS参数映射成适用于2/3G中使用的Pre-R8 QoS参数，以保证网络切换后，不影响业务服务质量。

#### 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- 该命令仅支持范围在1～9、65～66、69～70之间的QCI到Pre-R8 QoS的映射，如果QCI不在此范围内，需要先通过**ADD QCICONV**命令将扩展QCI映射为标准QCI(1～9)。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识   | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QCI    | QoS 级别标识 | 可选必选说明：必选参数 参数含义：该参数用于指定映射规则所对应QoS的级别。 数据来源：整网规划 取值范围：1~254 系统初始设置值：请参考表1。 配置原则：1～9为标准QoS，10～254为扩展QoS。1～3表示会话类业务。4表示流类业务。5～8表示交互类业务。9表示背景类业务。65表示公共安全PTT业务的语音业务。66表示普通消费者PTT业务的语音业务。69表示公共安全PTT业务的信令保障。70表示公共安全数据业务。                                                                                                                                                                                                                                                                                                                                                                   |
| TC     | 流量等级     | 可选必选说明：可选参数 参数含义：该参数用于指定映射后的QoS流量等级。 数据来源：整网规划 取值范围：“CC(Conversational class)”“SC(Streaming class)”“IC(Interactive class)”“BC(Background class)” 默认值：无 配置原则：建议值请参考表1。                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MAXSDU | 最大SDU长度  | 可选必选说明：可选参数 参数含义：该参数用于指定映射后的最大服务数据单元的长度。 数据来源：整网规划 取值范围：1~153 默认值：无 配置原则：1~150表示10~1500 octets。151表示1502 octets。152表示1510 octets。153表示1520 octets。建议值为150。                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DO     | 发送次序     | 可选必选说明：可选参数 参数含义：该参数用于指定映射后的缺省QoS发送次序。 数据来源：整网规划 取值范围：“ORDER(With delivery order)”“NORDER(Without delivery order)” 默认值：无 配置原则：建议值为“NORDER(Without delivery order)”。                                                                                                                                                                                                                                                                                                                                                                                                                     |
| RBER   | 保留BER    | 可选必选说明：可选参数 参数含义：该参数用于指定映射后的保留错误比特率。 数据来源：整网规划 取值范围：“E_RESIDUAL_BIT_ERR_RATIO_1(保留BER1)”：代表的比特率为5*10-2。“E_RESIDUAL_BIT_ERR_RATIO_2(保留BER2)”：代表的比特率为1*10-2。“E_RESIDUAL_BIT_ERR_RATIO_3(保留BER3)”：代表的比特率为5*10-3。“E_RESIDUAL_BIT_ERR_RATIO_4(保留BER4)”：代表的比特率为4*10-3。“E_RESIDUAL_BIT_ERR_RATIO_5(保留BER5)”：代表的比特率为1*10-3。“E_RESIDUAL_BIT_ERR_RATIO_6(保留BER6)”：代表的比特率为1*10-4。“E_RESIDUAL_BIT_ERR_RATIO_7(保留BER7)”：代表的比特率为1*10-5。“E_RESIDUAL_BIT_ERR_RATIO_8(保留BER8)”：代表的比特率为1*10-6。“E_RESIDUAL_BIT_ERR_RATIO_9(保留BER9)”：代表的比特率为6*10-8。 默认值：无 配置原则：建议值为“E_RESIDUAL_BIT_ERR_RATIO_7(保留BER7 =7)”。 |
| DESDU  | 发送错误SDU  | 可选必选说明：可选参数 参数含义：该参数用于指定映射后发送错误的服务数据单元。 数据来源：整网规划 取值范围：“NOT_DETECT(不检查)”：表示不需要侦查发送的服务数据单元是否有错。“ERR_SDU_DELIVERED(发送错误SDU)”：表示检测到发送的服务数据单元如果有错则需要上报。“ERR_SDU_NOT_DELIVERED(不发送错误SDU)”：表示检测到发送的服务数据单元如果有错不需要上报。 默认值：无 配置原则：建议值为“NOT_DETECT(不检查)”。                                                                                                                                                                                                                                                                                                                                         |
| SDUER  | SDU误码率   | 可选必选说明：可选参数 参数含义：该参数用于指定映射后的缺省QoS SDU误码率。 数据来源：整网规划 取值范围：“SDUER1(1*10^-2)”“SDUER2(7*10^-3)”“SDUER3(1*10^-3)”“SDUER4(1*10^-4)”“SDUER5(1*10^-5)”“SDUER6(1*10^-6)”“SDUER7(1*10^-1)” 默认值：无 配置原则：建议值请参考表1。                                                                                                                                                                                                                                                                                                                                                                                   |
| THPRI  | 发送控制优先级  | 可选必选说明：条件可选参数 参数含义：该参数用于指定映射后的缺省QoS发送控制优先级。 前提条件：该参数在“TC(流量等级)”配置为“IC(Interactive class)”后生效。 数据来源：整网规划 取值范围：“THPRI1(Priority level 1)”“THPRI2(Priority level 2)”“THPRI3(Priority level 3)” 默认值：无 配置原则：建议值请参考表1。                                                                                                                                                                                                                                                                                                                                                                        |
| TD     | 传递时延     | 可选必选说明：条件可选参数 参数含义：该参数用于指定映射后的缺省QoS传递时延。 前提条件：该参数在“TC(流量等级)”配置为“CC(Conversational class)”或“SC(Streaming class)”后生效。 数据来源：整网规划 取值范围：1~62（数值型） 默认值：无 配置原则：1~15表示10~150ms，以10ms递增。16~31表示200~950ms，以50ms递增。32~62表示1000~4000ms，以100ms递增。只在Traffic Class为实时类（Conversational，Streaming）时有效。建议值请参考表1。                                                                                                                                                                                                                                                                                          |

#### 使用实例

设置QCI为1的EPS QoS参数到Pre-R8 QoS参数映射规则：

SET R8QoSMAP: QCI=1, TC=CC, MAXSDU=1, DO=ORDER, RBER=E\_RESIDUAL\_BIT\_ERR\_RATIO\_2, DESDU=ERR\_SDU\_DELIVERED, SDUER=SDUER1, TD=2;

#### 参考信息

|   QoS 级别标识 | 流量等级                 |   最大SDU长度 | 发送次序   | 保留BER                      | 发送错误SDU    | SDU误码率   | 发送控制优先级          |   传递时延 |
|-----------:|:---------------------|----------:|:-------|:---------------------------|:-----------|:---------|:-----------------|-------:|
|          1 | Conversational class |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-2   | Priority level 3 |     10 |
|          2 | Conversational class |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-3   | Priority level 3 |     15 |
|          3 | Conversational class |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-3   | Priority level 3 |     10 |
|          4 | Streaming class      |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 3 |     18 |
|          5 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 1 |     10 |
|          6 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 1 |     18 |
|          7 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-3   | Priority level 2 |     10 |
|          8 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 3 |     18 |
|          9 | Background class     |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 3 |     18 |
|         65 | Conversational class |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-2   | Priority level 3 |     10 |
|         66 | Conversational class |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-2   | Priority level 3 |     10 |
|         69 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 1 |     18 |
|         70 | Interactive class    |       150 | NORDER | E_RESIDUAL_BIT_ERR_RATIO_7 | NOT_DETECT | 1*10-4   | Priority level 1 |     18 |