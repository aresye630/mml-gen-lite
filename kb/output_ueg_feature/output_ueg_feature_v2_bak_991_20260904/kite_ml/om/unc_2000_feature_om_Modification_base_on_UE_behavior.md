# 激活基于原因值的UE行为调整

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于原因值的UE行为调整特性的操作过程。

UEG通过向UE发送不同的原因值以调整UE的行为。

**说明** 

适用于SGSN、MME。

## 必备事项

前提条件

- HLR/HSS上已有相关用户签约信息。
- 请仔细阅读GWFD-024301 基于原因值的UE行为调整（适用于MME）特性概述。

数据

| 类别                                           | 参数名称                                          | 取值样例                  | 获取方法   | 说明       |
|:---------------------------------------------|:----------------------------------------------|:----------------------|:-------|:---------|
| ADD CAUSEGRP                                 | 原因值组标识(CAUSEGRPID)                            | 3                     | 全网规划   | 原因值映射组配置 |
| ADD CAUSEGRP                                 | 原因值组名称(CAUSEGRPNM)                            | 4G-S6a-To-NAS         | 全网规划   | 原因值映射组配置 |
| ADD CAUSEMAP                                 | 原因值组标识(CAUSEGRPID)                            | 3                     | 全网规划   | 原因值映射配置  |
| ADD CAUSEMAP                                 | 原因值范围(CAUSERANGE)                             | SPECIAL               | 全网规划   | 原因值映射配置  |
| ADD CAUSEMAP                                 | 起始原始原因值(BGCAUSE)                              | 5000                  | 全网规划   | 原因值映射配置  |
| ADD CAUSEMAP                                 | 终止原始原因值(EDCAUSE)                              | 5100                  | 全网规划   | 原因值映射配置  |
| ADD CAUSEMAP                                 | 目标原因值(TCAUSE)                                 | 12                    | 全网规划   | 原因值映射配置  |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | 流程类型(PROT)                                    | UPDATE_LOCATION       | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（IMSIGT错误）(ULRIMSIGTERR)              | 11                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（SCCPGT错误）(ULRSCCPGTERR)              | 22                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（链路异常）（ULRLINKERR）                    | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（HLR/HSS超时）(ULRHLRHSSTMOUT)           | 33                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（HLR/HSS拒绝）(ULRHLRHSSREJ)             | 0                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（IMSIGT错误）(AIRIMSIGTERR)              | 14                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（SCCPGT错误）(AIRSCCGPERR)               | 9                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（链路异常）（AIRLINKERR）                    | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（HLR/HSS超时）（AIRHLRHSSTMOUT）           | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（HLR/HSS拒绝）（AIRHLRHSSREJ）             | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Attach拒绝原因值（漫游受限）(ATTACHROAMRST)              | 13                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Intra RAU拒绝原因值（Identity超时）（INTRARAUIDTYTMOUT） | 9                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter RAU拒绝原因值（INTERRAUSGSNTMOUT）             | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter RAU拒绝原因值（漫游受限）（INTERRAUROAMRST）         | 0                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter RAU拒绝原因值（Identity超时）（INTERRAUIDTYTMOUT） | 0                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter RAU拒绝原因值（DNS解析失败） （INTERRAUDNSFAIL）     | 9                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Authentication拒绝原因值（鉴权检查失败）（AUTHRESCHKFAIL）   | 9                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Check IMEI拒绝原因值（IMEI检查失败）（CHKIMEICHKFAIL）     | 9                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（HSS超时）（ULRHSSTMOUT）                  | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（HSS拒绝）（ULRHSSREJ）                    | 3                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | ULR拒绝原因值（Diameter链路异常）（ULRDMERR）              | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（HSS超时）(AIRHSSTMOUT)                  | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（HSS拒绝）(AIRHSSREJ)                    | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | AIR拒绝原因值（Diameter链路异常）（AIRDMERR）              | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter TAU拒绝原因值（漫游受限）（INTERTAUROAMRST）         | 17                    | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | 分离请求原因值（DETACHCAUSE_CLR）                      | 7                     | 全网规划   | MM流程控制参数 |
| SET PMMPROCTRL SET GMMPROCTRL SET EMMPROCTRL | Inter TAU拒绝原因值（DNS解析失败）（INTERTAUDNSFAIL）      | 17                    | 全网规划   | MM流程控制参数 |
| SET GBSMPROCTRL SET IUSMPROCTRL              | 流程类型（PROT）                                    | ACT_PROC              | 全网规划   | SM流程控制参数 |
| SET GBSMPROCTRL SET IUSMPROCTRL              | 激活拒绝原因（ACTGGSNTMOUT）                          | 0                     | 全网规划   | SM流程控制参数 |
| SET GBSMPROCTRL SET IUSMPROCTRL              | 激活拒绝原因（ACTGGSNREJ）                            | 0                     | 全网规划   | SM流程控制参数 |
| SET GBSMPROCTRL SET IUSMPROCTRL              | 修改拒绝原因值（MODGGSNREJ）                           | 215                   | 全网规划   | SM流程控制参数 |
| SET S1SMPROCTRL                              | 流程类型（PROT）                                    | PDN_CONNECTIVITY_PROC | 全网规划   | SM流程控制参数 |
| SET S1SMPROCTRL                              | PDN连接拒绝原因值组号(SGW拒绝)(PDNCONSGWREJ)             | 1                     | 全网规划   | SM流程控制参数 |
| SET S1SMPROCTRL                              | PDN连接拒绝原因值(SGW超时)(PDNCONSGWTMOUT)             | 0                     | 全网规划   | SM流程控制参数 |

## 操作流程

激活基于原因值的UE行为调整操作流程如图1所示。

**图1** 激活基于原因值的UE行为调整操作流程

## 操作步骤

- 处理一：UEG直接向UE下发用户事先配置的原因值。

  **说明** 

  以下三种情况适用：

  - 由于UEG系统内部异常（配置/链路）导致的流程失败。
  - 由于周边网元响应消息超时。
  - 周边网元返回响应消息，但响应消息错误。

  - 设置Gb模式移动性管理流程中指定原因值的下发。

    进入“MML命令行-UEG”窗口。

    **SET GMMPROCTRL**

    **说明** 

    此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。
  - 设置Iu模式移动性管理流程中指定原因值的下发。

    **SET PMMPROCTRL**

    **说明** 

    此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。
  - 设置S1模式移动性管理流程中指定原因值的下发。

    **SET EMMPROCTRL**

    **ADD EMMPROCTRLIMSI**：基于指定用户范围的原因值映射控制，与**SET EMMPROCTRL**命令配合使用，系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配**SET EMMPROCTRL**命令的配置记录。

    **说明** 

    此命令这里列出了所有参数，但是这些参数不会同时显示，具体“流程类型”选择不同，对应的参数也不同。
  - 设置Gb模式会话管理流程中指定原因值的下发。

    **SET GBSMPROCTRL**

    **说明** 

    具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。
  - 设置Iu模式会话管理流程中指定原因值的下发。

    **SET IUSMPROCTRL**

    **说明** 

    具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。
  - 设置S1模式会话管理流程中指定原因值的下发。

    **SET S1SMPROCTRL**

    **说明** 

    具体“流程类型”选择不同，对应的参数也不同。此处以PDN连接建立流程为例。
- 处理二：UEG首先根据用户事先配置的规则完成原始原因值到目标原因值的映射后，将映射后的目标原因值下发给UE。

  **说明** 

  当周边网元返回拒绝消息时，采用此操作。

  1. 增加原因值映射组配置记录。

     **ADD CAUSEGRP**
  2. 增加原因值映射配置。

     **ADD CAUSEMAP**
  3. 配置用户指定原因值。

     - 设置Gb模式移动性管理流程中指定原因值的下发。

       **SET GMMPROCTRL**
     - 设置Iu模式移动性管理流程中指定原因值的下发。

       **SET PMMPROCTRL**
     - 设置S1模式移动性管理流程中指定原因值的下发。

       **SET EMMPROCTRL**

       **ADD EMMPROCTRLIMSI**：基于指定用户范围的原因值映射控制，与**SET EMMPROCTRL**命令配合使用，系统会首先匹配本命令的配置记录，若发现系统中不存在或不匹配本命令的配置记录才会匹配**SET EMMPROCTRL**命令的配置记录。
     - 设置Gb模式会话管理流程中指定原因值的下发。

       **SET GBSMPROCTRL**

       **说明** 

       具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。
     - 设置Iu模式会话管理流程中指定原因值的下发。

       **SET IUSMPROCTRL**

       **说明** 

       具体“流程类型”选择不同，对应的参数也不同。此处以激活流程为例。
     - 设置S1模式会话管理流程中指定原因值的下发。

       **SET S1SMPROCTRL**

       **说明** 

       具体“流程类型”选择不同，对应的参数也不同。此处以PDN连接建立流程为例。

## 任务示例

任务描述

- 场景一：GERAN ULR流程中，由于UEG系统内部异常导致的流程失败，即IMSIGT配置错误，UEG下发的原因值导致UE无法接入。
- 场景二：当UE进行附着时，HLR/HSS响应超时导致流程失败，因为UEG下发原因值与UE处理不一致，导致UE不再尝试接入。
- 场景三：当UE未在PS签约，UE进行PS附着，由于UEG下发原因值导致UE无法重新附着到CS网络。

脚本

- 脚本一

  //GERAN ULR流程中，配置用户特殊指定原因值。

  ```
  SET GMMPROCTRL: PROT=UPDATE_LOCATION, ULRIMSIGTERR=11, ULRSCCPGTERR=22;
  ```
- 脚本二

  //UTRAN流程中，配置用户特殊指定原因值。

  ```
  SET PMMPROCTRL: PROT=UPDATE_LOCATION, ULRHLRHSSTMOUT=33;
  ```
- 脚本三

  //在E-UTRAN ULR流程中，配置用户特殊指定原因值。

  ```
  ADD CAUSEGRP: CAUSEGRPID=3, CAUSEGRPNM="4G-S6a-To-NAS";
  ADD CAUSEMAP: CAUSEGRPID=3, CAUSERANGE=SPECIAL, BGCAUSE=5000, EDCAUSE=5100, TCAUSE=12;
  SET EMMPROCTRL: PROT=UPDATE_LOCATION, ULRHSSREJ=3;
  ADD EMMPROCTRLIMSI:SUBRANGE=IMSI_PREFIX, IMSIPRE="12307", ULRHSSREJ=3;
  ```