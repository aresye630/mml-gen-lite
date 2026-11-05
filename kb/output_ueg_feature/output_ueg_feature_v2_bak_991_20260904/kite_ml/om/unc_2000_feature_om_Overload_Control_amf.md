# 激活系统过载控制功能（适用于AMF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。

在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。

**说明** 

适用于AMF。

## 必备事项

前提条件

请仔细阅读GWFD-021401系统过载控制功能特性概述（适用于AMF）。

数据

| 类别                   | 参数名称                                   | 取值样例                                 | 获取方法   | 说明                                                                    |
|:---------------------|:---------------------------------------|:-------------------------------------|:-------|:----------------------------------------------------------------------|
| SET AMFFCPARA        | 流控措施（FCACT）                            | REJECT                               | 全网规划   | 设置自保流控的初始注册请求消息流控策略。AMF回复注册拒绝消息，并携带Backoff timer信元，用于指示请求消息重复尝试的延迟时长。 |
| SET AMFFCPARA        | Backoff Timer信元开关（BOTSW）               | ON                                   | 全网规划   | 设置自保流控的初始注册请求消息流控策略。AMF回复注册拒绝消息，并携带Backoff timer信元，用于指示请求消息重复尝试的延迟时长。 |
| SET AMFFCPARA        | Backoff timer最小值(秒)（MINBOT）            | 900                                  | 全网规划   | 设置自保流控的初始注册请求消息流控策略。AMF回复注册拒绝消息，并携带Backoff timer信元，用于指示请求消息重复尝试的延迟时长。 |
| SET AMFFCPARA        | Backoff timer最大值(秒)（MAXBOT）            | 1800                                 | 全网规划   | 设置自保流控的初始注册请求消息流控策略。AMF回复注册拒绝消息，并携带Backoff timer信元，用于指示请求消息重复尝试的延迟时长。 |
| SET N2OVERLOAD       | Overload功能开关（SWITCH）                   | On                                   | 本端规划   | 设置自保流控的N2接口消息流控策略。AMF过载时给gNodeB发Overload Start消息，并携带拒绝比例指示。           |
| SET N2OVERLOAD       | 过载行为（OVERLDACTION）                     | RejectAllSignallingEstablishMent     | 本端规划   | 设置自保流控的N2接口消息流控策略。AMF过载时给gNodeB发Overload Start消息，并携带拒绝比例指示。           |
| SET N2OVERLOAD       | 拒绝比例指示（REJRATEIND）                     | Yes                                  | 本端规划   | 设置自保流控的N2接口消息流控策略。AMF过载时给gNodeB发Overload Start消息，并携带拒绝比例指示。           |
| SET FCSWITCH         | 开关（SWITCH）                             | ENABLE                               | 本端规划   | 开启整系统的流控功能。                                                           |
| SET INTERAMFFC       | Inter-AMF接入流控功能开关（FCSWITCH）            | ON                                   | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET INTERAMFFC       | Registration Request流控阈值作用范围（REGSCOPE） | SYSTEM                               | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET INTERAMFFC       | Registration Request速率门限(个/秒)（REGTHD）  | 1000                                 | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET INTERAMFFC       | Service Request流控阈值作用范围（SRSCOPE）       | SYSTEM                               | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET INTERAMFFC       | Service Request速率门限(个/秒)（SRTHD）        | 2000                                 | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET INTERAMFFC       | 告警上报周期数（STARTALMTIMES）                 | 3                                    | 全网规划   | 开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。                                   |
| SET HTTPFIXEDFCMSG   | 流控消息类型（MSGTYPE）                        | NAMF_COMMUNICATION_UECONTEXTTRANSFER | 全网规划   | 设置服务化接口指定消息类型的固定速率流控功能。                                               |
| SET HTTPFIXEDFCMSG   | 固定速率流控开关（FCSWITCH）                     | ON                                   | 全网规划   | 设置服务化接口指定消息类型的固定速率流控功能。                                               |
| SET HTTPFIXEDFCMSG   | 流控速率门限(个/秒)（THRESHOLD）                 | 4000                                 | 全网规划   | 设置服务化接口指定消息类型的固定速率流控功能。                                               |
| SET AMFNASFIXEDFC    | 流控消息类型（MSGTYPE）                        | PDUSESSIONEST                        | 全网规划   | 开启PDU会话建立请求消息的固定速率流控功能。                                               |
| SET AMFNASFIXEDFC    | 固定速率流控开关（FCSWITCH）                     | On                                   | 全网规划   | 开启PDU会话建立请求消息的固定速率流控功能。                                               |
| SET AMFNASFIXEDFC    | 流控速率门限(个/秒)（THRESHOLD）                 | 1000                                 | 全网规划   | 开启PDU会话建立请求消息的固定速率流控功能。                                               |
| SET AMFNASFIXEDFC    | 流控阈值作用范围（SCOPE）                        | POD                                  | 全网规划   | 开启PDU会话建立请求消息的固定速率流控功能。                                               |
| SET N2FIXEDFCBYMSG   | 流控消息类型（MSGTYPE）                        | PAGING                               | 全网规划   | 开启N2接口Paging消息的固定速率流控功能。                                              |
| SET N2FIXEDFCBYMSG   | 固定速率流控开关（FCSWITCH）                     | On                                   | 全网规划   | 开启N2接口Paging消息的固定速率流控功能。                                              |
| SET N2FIXEDFCBYMSG   | 流控速率门限(个/秒)                            | 2000                                 | 全网规划   | 开启N2接口Paging消息的固定速率流控功能。                                              |
| ADD NGPAGINGARPPRI   | ARP数值（ARP）                             | 1                                    | 本端规划   | 配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。                                  |
| ADD NGPAGINGARPPRI   | 优先级（PRIORITY）                          | PAGING_HIGH                          | 本端规划   | 配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。                                  |
| ADD NGPAGINGDNNPRI   | DNN（DNN）                               | "IMS"                                | 本端规划   | 配置基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。                                  |
| ADD NGPAGINGDNNPRI   | 优先级（PRIORITY）                          | PAGING_HIGH                          | 本端规划   | 配置基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。                                  |
| SET N2PAGINGFCPLCY   | N2模式寻呼反压流控功能开关（FCSW）                   | ON                                   | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET N2PAGINGFCPLCY   | 精准寻呼控制开关（PRECISEPAGINGSW）              | ON                                   | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET PAECHECKPARA     | 检测间隔(s)（CHECKINTERVAL）                 | 1                                    | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET PAECHECKPARA     | 检测次数（CHECKTIMES）                       | 5                                    | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET PAECHECKTHD      | 资源类型（RESTYPE）                          | PBUF                                 | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET PAECHECKTHD      | 触发过载阈值（%）（TRIGTHD）                     | 60                                   | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET PAECHECKTHD      | 触发过载恢复阈值（%）（RESUMTHD）                  | 30                                   | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET REVERSEFCPARA    | 控制策略 （CTRLPLCY）                        | PERCENT                              | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET REVERSEFCPARA    | 过载阈值（%）（PERCENTTRGTHD）                 | 50                                   | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET REVERSEFCPARA    | 恢复阈值（%）（PERCENTRESUMTHD）               | 5                                    | 本端规划   | 开启N2模式寻呼反压流控功能。                                                       |
| SET AMFSOFTPARAOFBIT | 数据类型（DT）                               | Dw                                   | 本端规划   | （可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。                                         |
| SET AMFSOFTPARAOFBIT | Dword索引（DWORDNUM）                      | 14                                   | 本端规划   | （可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。                                         |
| SET AMFSOFTPARAOFBIT | 软参记录值（VALUE）                           | VALUE_0                              | 本端规划   | （可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。                                         |
| SET AMFSOFTPARAOFBIT | 比特位（POSITION）                          | 30                                   | 本端规划   | （可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。                                         |
| SET AMFSOFTPARA      | 数据类型（DT）                               | dw                                   | 本端规划   | （可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明： 此处阈值为举例值，请根据网络具体情况进行阈值设置。          |
| SET AMFSOFTPARA      | Dword索引（DWORDNUM）                      | 28                                   | 本端规划   | （可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明： 此处阈值为举例值，请根据网络具体情况进行阈值设置。          |
| SET AMFSOFTPARA      | Dword值（DWORDVALUE）                     | 80000                                | 本端规划   | （可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明： 此处阈值为举例值，请根据网络具体情况进行阈值设置。          |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 1                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 1                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 2                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 1                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 3                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 4                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 5                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | BYTE_EX_B                            | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 323                                  | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 6                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | DWORD_EX_B                           | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 85                                   | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 1                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 3                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | DWORD_EX_B                           | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 85                                   | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 4                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | DWORD_EX_B                           | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 85                                   | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 5                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | DT（参数类型）                               | DWORD_EX_B                           | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | PARANUM（参数索引）                          | 85                                   | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | VALUE（参数值）                             | 0                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |
| SET SOFTPARAOFBIT    | POSITION（比特位）                          | 6                                    | 本端规划   | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。                                        |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 开启自保流控功能。

   - 设置初始注册请求消息流控策略。

     **SET AMFFCPARA**

   - 设置N2接口消息流控策略。

     **SET N2OVERLOAD**
   - 增加具体微服务实例的流控参数。

     **ADD FCPARAM**
   - 开启整系统流控功能开关。

     **SET FCSWITCH**
3. 设置Inter-AMF用户接入流控功能的相关参数。

   **SET INTERAMFFC**
4. 开启服务化接口指定消息类型的固定速率流控功能。

   **SET HTTPFIXEDFCMSG**
5. 开启PDU会话建立请求消息的固定速率流控功能。

   **SET AMFNASFIXEDFC**
6. 开启N2接口Paging消息固定速率流控功能。

   - 设置流控消息类型和门限，开启流控功能开关。

     **SET N2FIXEDFCBYMSG**
   - 配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。

     **ADD NGPAGINGARPPRI**
   - 配置基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。

     **ADD NGPAGINGDNNPRI**
   - **可选：**设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

     **SET AMFSOFTPARAOFBIT**
   - **可选：**通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

     **SET AMFSOFTPARA**
7. 开启N2模式寻呼反压流控功能。

   - 开启流控功能开关。

     **SET N2PAGINGFCPLCY**
   - 设置流控相关参数

     **SET PAECHECKPARA**

     **SET PAECHECKTHD**

     **SET REVERSEFCPARA**
8. 配置是否开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

   **SET SOFTPARAOFBIT**

## 任务示例

任务描述

系统中度或者重度过载时，启动各项流控功能。

脚本

- 开启自保流控功能

  //设置初始注册请求消息流控策略为拒绝，并向终端下发Backoff timer时长。

  ```
  SET AMFFCPARA: FCACT=REJECT, MINBOT=900, MAXBOT=1800;
  ```

  //设置N2接口过载控制策略，开启Overload Start功能。

  ```
  SET N2OVERLOAD:SWITCH=On, OVERLDACTION=RejectAllSignallingEstablishMent, REJRATEIND=Yes;
  ```

  //添加具体实例的流控参数，增加微服务类型为UesmCtrlSvc、微服务实例ID为999、流控套餐ID为0的流控参数，最小令牌数为30，最大令牌数为5000。

  ```
  ADD FCPARAM: SERVICETYPE="UeamExecSvc", SERVICEID=999, CASEID=0, PARAMCAT=GENERAL, MINTOKEN=30, MAXTOKEN=5000;
  ```

  //开启整系统流控开关。

  ```
  SET FCSWITCH: SWITCH=ENABLE;
  ```
- 设置Inter-AMF用户接入流控功能的相关参数。

  ```
  SET INTERAMFFC: FCSWITCH=ON, REGSCOPE=SYSTEM, REGTHD=1000, SRSCOPE=SYSTEM, SRTHD=2000, STARTALMTIMES=3;
  ```
- 开启服务化接口指定消息类型的固定速率流控功能

  //设置服务化接口上指定消息类型的固定速率流控参数。

  ```
  SET HTTPFIXEDFCMSG:MSGTYPE=NAMF_COMMUNICATION_UECONTEXTTRANSFER,FCSWITCH=ON,THRESHOLD=4000;
  ```
- 开启PDU会话建立请求消息的固定速率流控功能

  ```
  SET AMFNASFIXEDFC:MSGTYPE=PDUSESSIONEST,FCSWITCH=On,THRESHOLD=1000,SCOPE=POD;
  ```
- 设置N2接口Paging消息固定速率流控功能

  //设置流控消息类型和门限，开启流控功能开关

  ```
  SET N2FIXEDFCBYMSG:MSGTYPE=PAGING,FCSWITCH=On,THRESHOLD=2000;
  ```

  //设置ARP为1的Paging消息在流控期间放通的优先级为高。

  ```
  ADD NGPAGINGARPPRI: ARP=1, PRIORITY=PAGING_HIGH;
  ```

  //设置DNN为"IMS"的Paging消息在流控期间放通的优先级为高，执行如下命令。

  ```
  ADD NGPAGINGDNNPRI: DNN="IMS", PRIORITY=PAGING_HIGH;
  ```

  //（可选）设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

  ```
  SET AMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=14, VALUE=VALUE_0, POSITION=30;
  ```

  //（可选）通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

  ```
  SET AMFSOFTPARA: DT=Dw, DWORDNUM=28, DWORDVALUE=80000;
  ```
- 设置N2模式寻呼反压流控功能。

  ```
  SET N2PAGINGFCPLCY: SWITCH=ON, PRECISEPAGINGSW=ON;
  SET PAECHECKPARA: CHECKINTERVAL=1, CHECKTIMES=5;
  SET PAECHECKTHD: RESTYPE=PBUF, TRIGTHD=60, RESUMTHD=30;
  SET REVERSEFCPARA: CTRLPLCY=PERCENT, PERCENTTRGTHD=50, PERCENTRESUMTHD=5;
  ```
- 开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

  ```
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_1, POSITION=1;
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_0, POSITION=2;
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_1, POSITION=3;
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_0, POSITION=4;
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_0, POSITION=5;
  SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=323, VALUE=VALUE_0, POSITION=6;
  SET SOFTPARAOFBIT: DT=DWORD_EX_B, PARANUM=85, VALUE=VALUE_1, POSITION=3;
  SET SOFTPARAOFBIT: DT=DWORD_EX_B, PARANUM=85, VALUE=VALUE_0, POSITION=4;
  SET SOFTPARAOFBIT: DT=DWORD_EX_B, PARANUM=85, VALUE=VALUE_0, POSITION=5;
  SET SOFTPARAOFBIT: DT=DWORD_EX_B, PARANUM=85, VALUE=VALUE_0, POSITION=6;
  ```