# 配置会话管理

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

本操作指导介绍在运行网络中配置会话管理特性的操作过程。

会话管理功能是MME的基本功能，是用户与外部PDN建立连接，进行数据业务的基础。MME的会话管理功能包括网络侧发起的会话管理和UE发起的会话管理。

## 必备事项

前提条件

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

- UNC软件安装已完成。

- EPS网络中各网元系统及操作维护台运行正常。
- 用户在HSS中已签约EPS业务。

数据

**说明** 

本文以IPv4组网为例说明。

- 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
- 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                | 参数名称                       | 取值样例                       | 获取方法            | 说明                                                                    |
|:------------------|:---------------------------|:---------------------------|:----------------|:----------------------------------------------------------------------|
| SET ESM           | T3485（s）（T3485）            | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | N3485（times）（N3485）        | 3                          | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | T3486（s）（T3486）            | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | N3486（times）（N3486）        | 2                          | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | T3489（s）（T3489）            | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | N3489（times）（N3489）        | 1                          | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | T3495（s）（T3495）            | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | N3495（times）（N3495）        | 3                          | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | SAE承载建立定时器（s）（TSAEBRSETUP） | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | SAE承载修改定时器（s）（TSAEBRMOD）   | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET ESM           | SAE承载释放定时器（s）（TSAEBRREL）   | 10                         | 参见“水平网设LLD文档 ”。 | 此命令中的所有参数均有系统初始值，如果用户使用初始值，就不必执行此命令 当使用NB-IoT业务时，需通过SET NBESM来配置会话管理。 |
| SET SMFUNC        | 强制启动间接转发方式 （INDFWD ）       | YES                        | 参见“水平网设LLD文档 ”。 | 设置会话管理扩展功能。                                                           |
| SET SMFUNC        | 拓扑选择开关 （TOPSELCFG ）        | YES                        | 参见“水平网设LLD文档 ”。 | 设置会话管理扩展功能。                                                           |
| SET SMFUNC        | APN限制功能开关 （APNRES ）        | NO                         | 参见“水平网设LLD文档 ”。 | 设置会话管理扩展功能。                                                           |
| SET SMFUNC        | APN限制的去激活方式 （PDPRMD ）      | MAX                        | 参见“水平网设LLD文档 ”。 | 设置会话管理扩展功能。                                                           |
| SET SMFUNC        | PDP/PDN Type策略 （PDPTYPE ）  | IPv4                       | 参见“水平网设LLD文档 ”。 | 设置会话管理扩展功能。                                                           |
| SET R8QOSMAP      | QoS级别标识（QCI）               | 1                          | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 流量等级（TC）                   | CC                         | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 最大SDU长度（MAXSDU）            | 150                        | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 发送次序（DO）                   | ORDER                      | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 保留BER（RBER）                | E_RESIDUAL_BIT_ERR_RATIO_1 | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 发送错误SDU（DESDU）             | NOT_DETECT                 | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | SDU误码率（SDUER）              | SDUER4                     | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET R8QOSMAP      | 传递时延（TD）                   | 10                         | 参见“水平网设LLD文档 ”。 | 设置EPS QoS参数到Pre-R8 QoS参数映射规则                                          |
| SET COMPATIBILITY | H值（HARP）                   | 1                          | 参见“水平网设LLD文档 ”。 | 设置QoS兼容性配置。                                                           |
| SET COMPATIBILITY | M值（MARP）                   | 14                         | 参见“水平网设LLD文档 ”。 | 设置QoS兼容性配置。                                                           |

文档

获取网设LLD文档。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. **可选：**设置S1模式SM协议参数。

   ```
   SET ESM:T3485=10,N3485=3,T3486=10,N3486=2,T3489=10,N3489=1,T3495=10,N3495=3,TSAEBRSETUP=10,TSAEBRMOD=10,TSAEBRREL=10;
   ```
3. **可选：**设置会话管理扩展功能。

   ```
   SET SMFUNC:INDFWD=YES,TOPSELCFG=YES,APNRES=NO,PDPRMD=MAX,PDPTYPE=IPv4;
   ```
4. **可选：**设置EPS QoS参数到Pre-R8 QoS参数映射规则。

   ```
   SET R8QOSMAP:QCI=1,TC=CC,MAXSDU=150,DO=ORDER,RBER=E_RESIDUAL_BIT_ERR_RATIO_1,DESDU=NOT_DETECT,SDUER=SDUER4,TD=10;
   ```
5. **可选：**设置QoS兼容性配置。

   ```
   SET COMPATIBILITY:HARP=1,MARP=14;
   ```

## 验证方法

**说明** 

以附着过程中EPS缺省承载的建立为例来说明验证方法，会话管理其他流程的验证方法类似。

在验证操作前做如下准备：

- 用户在HSS中已签约EPS业务。
- 用户处于分离状态。但在该MME上曾附着过，MME中有该用户的信息。

在相关网元均完成本特性的配置后，可以采用以下步骤检查特性工作是否正常：

1. 在MME上建立S1接口跟踪、用户跟踪、GTPC跟踪任务。
2. 用户开机发起GUTI附着。

   预期结果：UE成功附着到网络。
3. 查询用户的SM上下文。

   进入“MML命令行-UNC”窗口。

   ****DSP SMCTX****: QUERYOPT=BYIMSI, IMSI="IMSI", IDTYPE=BYBEARID/NSAPI, BEARIDORNSAPI=承载ID或网络层业务接入点标识;

   预期结果：缺省承载建立成功，有缺省承载上下文信息。
4. 查看消息跟踪。

   预期结果：消息跟踪能够跟踪到相应的消息，流程正确。