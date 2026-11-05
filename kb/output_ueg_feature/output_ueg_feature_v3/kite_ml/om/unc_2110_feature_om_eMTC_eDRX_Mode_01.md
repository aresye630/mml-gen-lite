# 激活eMTC eDRX模式（适用于MME）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活eMTC eDRX模式的操作过程。

本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的eMTC终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-026302 eMTC eDRX模式特性概述（适用于MME）。
* 已完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET HSFNTIME** | 时间类型（TIMETYPE） | GPS | 全网规划  说明：  如下参数值都需要与eNodeB侧协商一致：  * “时间类型” * “使用GPS起始时间” * 以及当不使用GPS起始时间时，“H-SFN参考日期”和“H-SFN参考时间（TIME）” | 设置H-SFN参考时间 |
|  | 使用GPS起始时间（GPSBEGIN） | YES |  |  |
|  | H-SFN参考日期（DATE） | 2010/01/01 |  |  |
|  | H-SFN参考时间（TIME） | 00：00：00 |  |  |
|  | 当前时间与参考时间闰秒差（GPSLEAPSEC） | 18 |  |  |
| **SET M2MCTRL** | WB-S1模式寻呼窗口差值（WBEDRXPAGDIFF） | SAME | 全网规划  说明：  “WB-S1模式寻呼窗口差值”的取值依据eNodeB提供寻呼窗口起始时间的最大时间差值进行配置，MME配置值为大于等于该差值的可配置的最小值。 | 设置eMTC控制参数 |
|  | 用户面建立优化（USERPLANOPT） | YES |  |  |
| **ADD M2MPLCY** | 用户范围（SUBRANGE） | ALL\_USER | 全网规划 | 增加eMTC终端省电策略 |
|  | APNNI（APNNI） | huawei.com |  |  |
|  | eDRX开关（EDRXSW） | ON |  |  |
|  | 宽带S1模式寻呼周期（WBECL） | USE\_UE\_REQUEST |  |  |
|  | 宽带S1模式寻呼时间窗口时长（WBPTW） | USE\_UE\_REQUEST |  |  |
|  | 窄带寻呼时间窗口时长签约优先（NBPTWSUBPRI） | NO |  |  |
|  | 宽带寻呼时间窗口时长签约优先（WBPTWSUBPRI） | NO |  |  |
| **ADD GTPCV2CMPT** | 索引（IDX） | 0/1/2/3 | 本端规划 | 协议兼容性相关参数 |
|  | 消息分类（MSGCLS） | TM(隧道管理)  MM(移动管理) | 本端规划 |  |
|  | 是否支持LTE-M类型的RAT TYPE（RATTYPELTEM） | YES | 本端规划 |  |
| **ADD PGWCHARACT** | 对端设备范围（RANGE） | ALL | 本端规划 | PGW-C对接相关参数 |
|  | 是否向P-GW转发LTE-M类型的RAT TYPE（RATTYPELTEM） | YES | 本端规划 |  |
| **SET DMCMPT** | 是否支持LTE-M类型的RAT TYPE（RATTYPELTEM） | ULR-1&NOR-0 | 本端规划 | 设置Diameter兼容性 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置H-SFN参考时间。

   eDRX周期的取值以H-SFN（超帧）为单位。为了计算UE的寻呼时间，MME需要使用和eNodeB相同的H-SFN号。MME通过如下配置，能够配置H-SFN=0对应的参考时间，使MME和eNodeB设置为同一个时间，对齐H-SFN。

   **SET HSFNTIME**

   计算寻呼时间的算法请参见协议3GPP TS 36.304。
3. 设置eMTC控制参数。

   如果确认eNodeB对H-SFN进行了偏移处理，即eNodeB计算的寻呼时间窗口起始时间与MME计算的寻呼窗口起始时间存在偏差值时，可通过执行如下命令的“WB-S1模式寻呼窗口差值”参数进行配置。

   **SET M2MCTRL**

   由于eNodeB和MME上的时间可能存在时间差，或eNodeB为了减少SFN的跳变，在计算H-SFN时以SFN为准对H-SFN进行偏移，导致eNodeB与MME计算得到的寻呼窗口起始时间有差值，如果MME严格按照计算得出的寻呼窗口进行寻呼，可能错过部分eNodeB计算的寻呼窗口而导致寻呼成功率较低。
4. 增加eMTC终端省电策略。

   **ADD M2MPLCY**

   “宽带S1模式寻呼时间窗口时长”设置时，建议WBPTW的值至少为DefaultPagingDRX值的2倍，这样eNodeB在WBPTW窗口内可以有多次机会寻呼用户。Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。
5. 打开本功能的License配置开关。

   **SET LICENSESWITCH**
6. **可选：**如果eMTC终端需要添加RAT Type为LTE-M类型时，需要执行此步骤。
   1. 将RAT Type为LTE-M的消息传递给SGW-C。

      **ADD GTPCV2CMPT**
   2. 指示SGW-C向PGW-C传递RAT Type为LTE-M类型。

      **ADD PGWCHARACT**
   3. UEG向HSS发送Update Location Request消息或者Notify Request消息时，消息中的RAT TYPE信元设置为LTE-M。

      **SET DMCMPT**

## 任务示例

任务描述

任务一：某APNNI为“huawei.com”物联网行业用户需要开启eMTC制式下的eDRX模式，需要进行以下操作。

任务二：eMTC终端添加RAT Type为LTE-M类型。

脚本

* 任务一：

//设置H-SFN参考时间。假设当前时间为2017年01月01日，则当前时间与参考时间闰秒差为18s。

```
SET HSFNTIME: TIMETYPE=GPS, GPSBEGIN=YES, GPSLEAPSEC=18;
```

//设置eMTC控制参数。

```
SET M2MCTRL: WBEDRXPAGDIFF=SAME, USERPLANOPT=YES;
```

//配置eMTC终端省电策略。

```
ADD M2MPLCY: SUBRANGE=ALL_USER, APNNI="huawei.com", EDRXSW=ON, WBECL=USE_UE_REQUEST, WBPTW=USE_UE_REQUEST, WBPTWSUBPRI=NO, NBPTWSUBPRI=NO;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2EDRX02", SWITCH=ENABLE;
```

* 任务二：

//eMTC终端添加RAT Type为LTE-M类型

```
ADD GTPCV2CMPT: IDX=0, MSGCLS=TM, TMMSGTYPE=CRT_SES_REQ, CRTSESREQ=INDICATION, CRTSESREQIND=CPOPCI-0, RATTYPELTEM=YES; 
ADD GTPCV2CMPT: IDX=1, MSGCLS=TM, TMMSGTYPE=MOD_BR_REQ, MODBRREQ=BCMOD, FTEIDVALUE=VALID, RATTYPELTEM=YES; 
ADD GTPCV2CMPT: IDX=2, MSGCLS=MM, MMMSGTYPE=FWD_RLC_REQ, FWDRLCREQ=INDICATION, FWDRLCREQIND=SQCI-0, RATTYPELTEM=YES; 
ADD GTPCV2CMPT: IDX=3, MSGCLS=MM, MMMSGTYPE=CTX_RSP, CTXRSP=INDICATION, CTXRSPIND=SQCI-0&SRNI-0&CPOPCI-0&BDWI-0, RATTYPELTEM=YES; 
ADD PGWCHARACT: RANGE=ALL, RATTYPELTEM=YES; 
SET DMCMPT: RATTYPELTEM=ULR-1&NOR-0;
```

版权所有 © 华为技术有限公司
