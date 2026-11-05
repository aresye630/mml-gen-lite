# 激活精准寻呼（LTE）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活LTE精准寻呼的操作过程。

UEG基于用户类型、业务类型选择相应的寻呼策略，综合用户的移动性进行寻呼规则过滤，选择合适的范围对用户进行寻呼，从而有效地减少整个网络中eNodeB的寻呼负荷，节省网络资源。

**说明** 

- 适用于MME。
- 本特性与**GWFD-025402 基于VoLTE的优先语音服务**特性中的**MPS优先级**业务存在冲突，启用前请先检查是否已配置MPS业务（**SET MPSARP**），如果已配置，建议先关闭MPS业务，再开启本特性，否则精准寻呼业务会失效。

## 必备事项

前提条件

- 请仔细阅读GWFD-021411 精准寻呼（4G）。
- 部署基于APN，QCI或ARP的精准寻呼策略时，S-GW需要支持在发送给MME的Downlink Data Notification消息中携带EPS Bearer ID信元。
- 建议由华为专业服务对本网进行评估后选定最优的精准寻呼参数。
- 已完成加载License。

数据

| 类别                  | 参数                            | 取值样例                          | 获取方法   | 说明               |
|:--------------------|:------------------------------|:------------------------------|:-------|:-----------------|
| ADD S1PAGINGRULE    | 用户群类型（GRPTYPE）                | ALL_USER                      | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | IMSI前缀（IMSIPRE）               | 460002                        | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | MSISDN前缀（MSISDNPRE）           | 861392                        | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | IMEI TAC（IMEITAC）             | 12345678                      | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 业务类型（SVRTYPE）                 | S11_DOWNLINK                  | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | APN指示（APNIND）                 | SPEC_APN                      | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 移动国家码（MCC）                    | 460                           | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 移动网号（MNC）                     | 03                            | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | APN NI（APN）                   | huawei.com                    | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | QCI值（QCI）                     | 123                           | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | ARP优先级（ARPPL）                 | 3                             | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | SGs接口业务指示（SGSSI）              | CS_CALL                       | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 消息类型(MSGTYPE)                 | “DDN(DDN)”+“CBR/UBR(CBR/UBR)” | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 匹配优先级（PRIORITY）               | 23                            | 全网规划   | 配置S1寻呼规则。        |
| ADD S1PAGINGRULE    | 寻呼动作组合（ACTGRP）                | LAST_ENODEB                   | 全网规划   | 配置S1寻呼规则。        |
| SET S1PAGINGCTRL    | 最近eNodeB开关（LASTENBSW）         | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | 邻接eNodeB开关（NEIB_ENBSW）        | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | 最近TA开关（LASTTA）                | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | SUB_T3413（SUBT3413）           | 3                             | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | 低移动性检查开关（LOWMOBICHKSW）        | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | eNodeB粘性时长（ENB_STICK_TIME）    | 2                             | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | TA粘性时长（TA_STICK_TIME）         | 60                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | ECT学习开关（ECT_LRN_SW）           | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | X2HO学习开关（X2HO_LRN_SW）         | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | S1HO学习开关（S1HO_LRN_SW）         | ON                            | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | 邻接eNodeB老化时间（NEB_EXPIRE_TIME） | 360                           | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | 全网寻呼开关（ALLNET）                | OFF                           | 全网规划   | 设置S1寻呼策略。        |
| SET S1PAGINGCTRL    | SGs寻呼重发上限（SGS_REPAG_THRE）     | 15                            | 全网规划   | 设置S1寻呼策略。        |
| ADD TALSTPAGINGPLCY | TA List标号（TALISTID）           | 5                             | 本端规划   | 配置指定TA List寻呼规则。 |
| ADD TALSTPAGINGPLCY | 是否关闭精准寻呼（CLSPRECISEPAG）       | YES                           | 全网规划   | 配置指定TA List寻呼规则。 |
| ADD TALSTPAGINGPLCY | 是否配置定时器（CONFIGTIMER）          | YES                           | 全网规划   | 配置指定TA List寻呼规则。 |
| ADD TALSTPAGINGPLCY | T3413(s)（T3413）               | 3                             | 全网规划   | 配置指定TA List寻呼规则。 |
| ADD TALSTPAGINGPLCY | N3413(times)（N3413）           | 2                             | 全网规划   | 配置指定TA List寻呼规则。 |
| ADD TALSTPAGINGPLCY | 重寻呼间隔递增值(s)（PAGINGDELTA）      | 2                             | 全网规划   | 配置指定TA List寻呼规则。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 打开eNodeB学习邻接关系和寻呼范围开关。

   **SET S1PAGINGCTRL**
4. 配置寻呼策略及寻呼规则。

   **说明** 

   - 部署了WSFD-102301 基于CSFB的语音业务、GWFD-025401 VoLTE基础语音业务或GWFD-025601 LTE一键通基础功能特性概述（适用于MME）的情况下，启用LTE精准寻呼特性会增加被叫寻呼时延，在部署本特性时，建议针对CSFB、VoLTE语音或PTT业务使用TA List的寻呼范围，从而在不影响语音被叫时延的情况下节省网络资源。
   - 针对数据业务和其他非语音类业务，“寻呼动作组合”推荐采用“最近访问eNodeB -> TA List”组合，即“ACTGRP（寻呼动作组合）”取值设置为“LAST\_ENODEB-1”。这样能够有效减少寻呼范围的同时，明显减少对eNodeB侧的CPU消耗。

   **ADD S1PAGINGRULE**
5. 检查用户移动性，进行寻呼规则过滤。

   **SET S1PAGINGCTRL**

   **说明** 

   “ENB\_STICK\_TIME（eNodeB粘性时长）”推荐设置为2min。
6. 配置指定TA List寻呼规则。

   **ADD TALSTPAGINGPLCY**

   **说明** 

   - 若针对指定的TA List关闭精准寻呼功能，设置**ADD TALSTPAGINGPLCY**命令中“CLSPRECISEPAG”参数为“YES”，4设置的精准寻呼规则不生效。
   - 若需要关闭特定TA List的精准寻呼功能，且针对TA List范围的寻呼配置差异化的寻呼定时器时长，配置**ADD TALSTPAGINGPLCY**命令中“CLSPRECISEPAG”参数为“YES”，“T3413”、“N3413”和“PAGINGDELTA”为需要的值。
   - “TALISTID”需要在**ADD TALST**中已经配置。

## 任务示例

任务描述

任务1：启用LTE精准寻呼。针对CSFB和VoLTE语音业务，采用TA List寻呼范围组合，针对数据业务和其他非语音类业务，使用“最近eNodeB -> TA List”寻呼范围组合。

任务2：在任务1的基础上，对指定的TA list关闭精准寻呼，直接对指定TA List下的所有eNodeB发起寻呼。

脚本

任务1：

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;
```

//打开学习最近eNodeB开关。

```
SET S1PAGINGCTRL: LASTENBSW=ON, NEIB_ENBSW=OFF, LASTTA=OFF, SUBT3413=3;
```

//配置寻呼策略及寻呼规则。

//配置CSFB语音业务不启用LTE精准寻呼。

```
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=SGS_PAGING, SGSSI=CS_CALL, PRIORITY=100, ACTGRP=LAST_ENODEB-0&NEIGH_ENODEB-0&LAST_TAI-0, DESC="Voice of CSFB";
```

//配置VoLTE语音业务不启用LTE精准寻呼。

```
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=S11_DOWNLINK, APNIND=ALL_APN, QCI=1, PRIORITY=100, ACTGRP=LAST_ENODEB-0&NEIGH_ENODEB-0&LAST_TAI-0;
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=S11_DOWNLINK, APNIND=ALL_APN, QCI=5, PRIORITY=100, ACTGRP=LAST_ENODEB-0&NEIGH_ENODEB-0&LAST_TAI-0;
```

//配置数据业务和其他非语音业务启用LTE精准寻呼。

```
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=S11_DOWNLINK, APNIND=ALL_APN, ACTGRP=LAST_ENODEB-1, DESC="data";
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=OTHER, ACTGRP=LAST_ENODEB-1;
```

//检查用户移动性，进行寻呼规则过滤。

```
SET S1PAGINGCTRL: LOWMOBICHKSW=ON, ENB_STICK_TIME=2;
```

任务2：

//配置指定TA List寻呼规则。

```
ADD TALSTPAGINGPLCY: TALISTID=1, CLSPRECISEPAG=YES, CONFIGTIMER=NO;
```