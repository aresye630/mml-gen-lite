# 激活系统过载控制功能（适用于SGSN、MME）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。

适用于SGSN、MME。

## 必备事项

前提条件

请仔细阅读GWFD-021401系统过载控制功能特性概述（适用于SGSN、MME）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****SET INTERMMEFC**** | InterMME接入流控功能开关（FCSWITCH） | ON | 全网规划 | 设置Inter-MME流控参数。 |
|  | 流控速率最小值（MINTHD） | 10 |  |  |
|  | 流控速率最大值（MAXTHD） | 200 |  |  |
| ****SET S1PAGINGFC**** | S1寻呼流控功能开关（FCSWITCH） | ON | 全网规划 | 设置S1寻呼流控参数。  开启PAE寻呼反压流控开关时，还需要通过SET PAECHECKPARA、SET PAECHECKTHD、SET REVERSEFCPARA设置PAE寻呼反压流控相关参数。 |
|  | SGs寻呼流控开关（SGSSWITCH） | ON |  |  |
|  | S102寻呼流控开关（S102SWITCH） | ON |  |  |
|  | 寻呼重发控制开关（PAGINGRESENDSWITCH） | ON |  |  |
|  | 寻呼突发预防功能开关（ANTIBURSTSWITCH） | ON |  |  |
|  | PAE反压流控功能开关（PAEFCSWITCH） | ON |  |  |
|  | 寻呼流控速率门限（FCTHD） | 150 |  |  |
|  | 寻呼流控速率最小值（FCTHDMIN） | 10 |  |  |
|  | 寻呼预留处理量（RSVCAP） | 15 |  |  |
|  | 语音寻呼预留处理量（RSVVOCAP） | 5 |  |  |
| **SET PAECHECKPARA** | 检测间隔(s)（CHECKINTERVAL） | 1 | 本端规划 | 通过**SET S1PAGINGFC**开启PAE寻呼反压流控开关时，需要设置PAE寻呼反压流控相关参数。 |
|  | 检测次数（CHECKTIMES） | 5 |  |  |
| **SET PAECHECKTHD** | 资源类型（RESTYPE） | PBUF |  |  |
|  | 触发过载阈值（%）（TRIGTHD） | 60 |  |  |
|  | 触发过载恢复阈值（%）（RESUMTHD） | 30 |  |  |
| **SET REVERSEFCPARA** | 控制策略 （CTRLPLCY） | PERCENT |  |  |
|  | 过载阈值（%）（PERCENTTRGTHD） | 50 |  |  |
|  | 恢复阈值（%）（PERCENTRESUMTHD） | 5 |  |  |
| ****SET FLOWCTRLPARA**** | 业务权重获取方式（WEIGHTMODE） | LEARN(统计学习) | 全网规划 | 设置流控系统参数。 |
|  | 进程类型（PROCTYPE） | GBP |  |  |
|  | 窗口最小值（MINWAL） | 30 |  |  |
|  | 窗口最大值（MAXWAL） | 2000 |  |  |
|  | 2G用户面窗口最小值（MINWAL\_GBDATA） | 2500 |  |  |
|  | 2G用户面窗口最大值（MAXWAL\_GBDATA） | 16000 |  |  |
|  | 2G寻呼窗口最大值（MAXWAL\_GBPAGING） | 900 |  |  |
|  | 丢包率告警阈值（DROPRATETHD） | 5 |  |  |
| ****SET FLOWCTRLQUE**** | 业务类型（APPTYPE） | APP\_2G | 全网规划 | 设置流控队列信息。 |
|  | 2G消息类型（MSG2GTYPE）  3G消息类型（MSG3GTYPE）  4G消息类型（MSG4GTYPE） | ATTACH |  |  |
|  | 业务权重(WEIGHT) | 9 |  |  |
|  | 队列期望长度（QUELENTH） | 400 |  |  |
| **ADD TALISTPAGINGCFG** | 跟踪区域码（TAC） | 0xBF85 | 全网规划 | 设置S1模式基于TALIST寻呼消息不重发的TAC区间，以及不重发的TAC区间对于IMS寻呼消息不生效。 |
|  | 跟踪区域码范围（TACRANGE） | 0xBFFF |  |  |
|  | 语音寻呼开关（IMSPAGINGSW） | OFF（关闭） |  |  |
| **SET SOFTPARAOFBIT** | DT（参数类型） | BYTE\_EX\_B | 本端规划 | 配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。 |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 1 |  |  |
|  | POSITION（比特位） | 1 |  |  |
|  | DT（参数类型） | BYTE\_EX\_B |  |  |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 2 |  |  |
|  | DT（参数类型） | BYTE\_EX\_B |  |  |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 1 |  |  |
|  | POSITION（比特位） | 3 |  |  |
|  | DT（参数类型） | BYTE\_EX\_B |  |  |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 4 |  |  |
|  | DT（参数类型） | BYTE\_EX\_B |  |  |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 5 |  |  |
|  | DT（参数类型） | BYTE\_EX\_B |  |  |
|  | PARANUM（参数索引） | 323 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 6 |  |  |
|  | DT（参数类型） | DWORD\_EX\_B |  |  |
|  | PARANUM（参数索引） | 85 |  |  |
|  | VALUE（参数值） | 1 |  |  |
|  | POSITION（比特位） | 3 |  |  |
|  | DT（参数类型） | DWORD\_EX\_B |  |  |
|  | PARANUM（参数索引） | 85 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 4 |  |  |
|  | DT（参数类型） | DWORD\_EX\_B |  |  |
|  | PARANUM（参数索引） | 85 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 5 |  |  |
|  | DT（参数类型） | DWORD\_EX\_B |  |  |
|  | PARANUM（参数索引） | 85 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 6 |  |  |

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET INTERMMEFIXFC** | 流控粒度（FCTYPE） | PROCESS | 全网规划 | 设置Inter-MME接入固定速率流控功能的相关参数，对Inter-MME的ServiceRequest和AttachRequest消息分别进行流控。  说明：  * 该命令与**SET INTERMMEFC**不建议同时开启。同时开启时该命令优先级高于**SET INTERMMEFC**。 * 当“FCTYPE”为“PROCESS（单进程）”时：    + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值是单SGP进程每秒钟可以通过的Attach Request消息数。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值是单SGP进程每秒钟可以通过的Service Request消息数。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值是整系统每秒钟可以通过的Service Request消息数。每个SGP进程独立进行流控，整系统的流控阈值除以SGP进程个数作为每个SGP进程的流控阈值。 * 当“FCTYPE”为“POD（POD）”时：   + “ATTACHSCOPE”值为：      - “PROCESS（单进程）”：表示“ATTACHTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Attach Request消息流控阈值。     - “SYSTEM（整系统）”：表示“ATTACHTHD”参数指定的值是整系统每秒钟可以通过的Attach Request消息数。每个LINK-POD独立进行流控，整系统的流控阈值除以LINK-POD个数作为每个LINK-POD的流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。   + “SRSCOPE”值为：     - “PROCESS（单进程）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，作为每个LINK-POD的Service Request消息流控阈值。     - “SYSTEM（整系统）”：表示“SRTHD”参数指定的值乘以LINK-POD中SGP进程个数，数作为每个LINK-POD的Service Request消息流控阈值。当部分Pod故障时，正常的Pod的流控阈值不变。 |
|  | ATTACHFCSWITCH（Attach接入流控功能开关） | ON | 全网规划 |  |
|  | ATTACHSCOPE（Attach Request流控阈值作用范围） | PROCESS | 全网规划 |  |
|  | ATTACHTHD（  Attach Request速率门限(个/秒)） | 4080 | 全网规划 |  |
|  | SRFCSWITCH（SR接入流控功能开关） | ON | 全网规划 |  |
|  | SRSCOPE（Service Request流控阈值作用范围） | PROCESS | 全网规划 |  |
|  | SRTHD（Service Request速率门限(个/秒)） | 4080 | 全网规划 |  |
| **SET SOFTPARAOFBIT** | DT（参数类型） | BYTE\_EX\_B | 本端规划 | 控制系统中S1接口Inter-MME Service Request固定速率流控失效阈值。 |
|  | PARANUM（参数索引） | 339 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 1 |  |  |
| **SET SOFTPARAOFBIT** | DT（参数类型） | BYTE\_EX\_B | 本端规划 | 控制系统在启用Inter-MME Service Request流程S1接口流控失效功能后，设定软参BYTE\_EX\_B339设置的每SGP进程每秒接入用户数阈值的倍数。 |
|  | PARANUM（参数索引） | 340 |  |  |
|  | VALUE（参数值） | 0 |  |  |
|  | POSITION（比特位） | 1 |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置Inter-MME流控参数。

   **SET INTERMMEFC**
3. 设置S1寻呼流控参数，包括寻呼流控功能开关、寻呼流控速率门限、寻呼流控速率最小值和寻呼预留处理量等。

   1. ****SET S1PAGINGFC****
   2. （可选）当开启PAE寻呼反压流控开关时，还需要设置PAE寻呼反压流控相关参数。

      **SET PAECHECKPARA**

      **SET PAECHECKTHD**

      **SET REVERSEFCPARA**
4. 配置是否开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

   **SET SOFTPARAOFBIT**
5. 设置流控系统参数。

   ****SET FLOWCTRLPARA****
6. 设置流控队列参数。

   ****SET FLOWCTRLQUE****
7. 分别控制Inter-MME ServiceRequest流程和 Attach流程S1接口流控参数。与2中命令不建议同时开启。

   **SET INTERMMEFIXFC**
8. 设置Inter-MME Service Request固定速率流控失效相关参数。

   **SET SOFTPARAOFBIT**
9. 设置S1模式基于TALIST寻呼消息不重发的TAC区间。

   **ADD TALISTPAGINGCFG**

## 任务示例

任务描述

任务一：

* 系统正常运行或轻度过载时，启动Inter-MME用户接入流控。
* 系统中度过载时，启动队列流控。
* 系统中度或者重度过载时，启动自保流控。
* 当S1接口的包转发速率拥塞时，启动S1寻呼流控。
* 开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。
* 当用户所在TALIST的TAC在配置的不重发TAC范围内时，不对寻呼范围是TALIST的寻呼消息进行重发。

任务二：

配置Inter-MME固定速率流控，流控粒度为按进程进行流控。

脚本

任务一脚本：

//设置Inter-MME接入流控参数。

```
SET INTERMMEFC: FCSWITCH=ON, MINTHD=10, MAXTHD=200;
```

//设置流控队列参数。

```
SET FLOWCTRLQUE: APPTYPE=APP_2G, MSG2GTYPE=ATTACH, WEIGHT=9, QUELENTH=400;
```

//设置流控系统参数（GBP）。

```
SET FLOWCTRLPARA: WEIGHTMODE=LEARN, PROCTYPE=GBP, MINWAL=30, MAXWAL=2000, MINWAL_GBDATA=2500, MAXWAL_GBDATA=16000, MAXWAL_GBPAGING=900, DROPRATETHD=5;
```

//设置S1寻呼流控参数。

```
SET S1PAGINGFC: FCSWITCH=ON, SGSSWITCH=ON, S102SWITCH=ON, PAGINGRESENDSWITCH=ON, ANTIBURSTSWITCH=ON, PAEFCSWITCH=ON, FCTHD=150, FCTHDMIN=10, RSVCAP=15, RSVVOCAP=5;
```

//开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

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

//设置PAE寻呼反压流控相关参数。

```
SET PAECHECKPARA: CHECKINTERVAL=1, CHECKTIMES=5;
SET PAECHECKTHD: RESTYPE=PBUF, TRIGTHD=60, RESUMTHD=30;
SET REVERSEFCPARA: CTRLPLCY=PERCENT, PERCENTTRGTHD=50, PERCENTRESUMTHD=5;
```

//设置S1模式基于TALIST寻呼消息不重发的TAC区间。

```
ADD TALISTPAGINGCFG: TAC="0xBF85", TACRANGE="0xBFFF", IMSPAGINGSW=OFF;
```

//分别控制Inter-MME ServiceRequest流程和 Attach流程S1接口流控参数。

```
SET INTERMMEFIXFC: ATTACHFCSWITCH=OFF, SRFCSWITCH=OFF;
```

//设置Inter-MME Service Request固定速率流控失效相关参数。

```
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=1;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=2;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=3;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=4;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=5;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=6;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=7;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=339, VALUE=VALUE_0, POSITION=8;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=340, VALUE=VALUE_0, POSITION=1;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=340, VALUE=VALUE_0, POSITION=2;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=340, VALUE=VALUE_0, POSITION=3;
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=340, VALUE=VALUE_0, POSITION=4;
```

任务二脚本：

//关闭Inter-MME接入流控。

```
SET INTERMMEFC:FCSWITCH=OFF;
```

//配置Inter-MME固定速率流控。

```
SET INTERMMEFIXFC:FCTYPE=PROCESS, ATTACHFCSWITCH=ON, ATTACHSCOPE=PROCESS, ATTACHTHD=4080, SRFCSWITCH=ON, SRSCOPE=PROCESS, SRTHD=4080;
```

版权所有 © 华为技术有限公司
