# 激活NB-IoT eDRX模式（MME）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活NB-IoT eDRX模式的操作过程。

本特性通过在网元间传递eDRX（Extended Discontinuous Reception）信元并计算出合理的寻呼时机来缩短对移动性、实时性较低的M2M终端的监控寻呼信道时长，从而减少网络信令负荷，节省终端耗电量，延长电池使用寿命。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-026104 NB-IoT eDRX模式特性概述（MME）。
* 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| **SET HSFNTIME** | 时间类型（TIMETYPE） | GPS | 全网规划  说明：  如下参数值都需要与eNodeB侧协商一致：  * “时间类型” * “使用GPS起始时间” * 以及当不使用GPS起始时间时，“H-SFN参考日期”和“H-SFN参考时间（TIME）” | 设置H-SFN参考时间 |
|  | 使用GPS起始时间（GPSBEGIN） | YES |  |  |
|  | H-SFN参考日期（DATE） | 2010/01/01 |  |  |
|  | H-SFN参考时间（TIME） | 00：00：00 |  |  |
|  | 当前时间与参考时间闰秒差（GPSLEAPSEC） | 18 |  |  |
| **SET M2MCTRL** | NB-S1模式寻呼窗口差值（NBEDRXPAGDIFF） | SAME | 全网规划  说明：  “NB-S1模式寻呼窗口差值”的取值依据eNodeB提供寻呼窗口起始时间的最大时间差值进行配置，MME配置值为大于等于该差值的可配置的最小值。 | 设置Diameter兼容性参数，保证网元间支持信元的兼容性。 |
|  | 用户面建立优化（USERPLANOPT） | YES |  |  |
| **ADD M2MPLCY** | 用户范围（SUBRANGE） | ALL\_USER | 全网规划 | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
|  | APNNI（APNNI） | huawei.com |  |  |
|  | eDRX开关（EDRXSW） | ON |  |  |
|  | 窄带S1模式寻呼周期（NBECL） | USE\_UE\_REQUEST |  |  |
|  | 窄带S1模式寻呼时间窗口时长（NBPTW） | USE\_UE\_REQUEST |  |  |
|  | 窄带EDRX寻呼周期签约优先（NBEDRXSUBPRI） | NO |  |  |
|  | 窄带寻呼时间窗口时长签约优先（NBPTWSUBPRI） | NO |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置H-SFN参考时间。

   eDRX周期的取值以H-SFN（超帧）为单位。为了计算UE的寻呼时间，MME需要使用和eNodeB相同的H-SFN号。MME通过如下配置，能够配置H-SFN=0对应的参考时间，使MME和eNodeB设置为同一个时间，对齐H-SFN。

   **SET HSFNTIME**

   计算寻呼时间的算法请参见协议3GPP TS 36.304。
3. **可选：**设置M2M控制参数。

   如果确认eNodeB对H-SFN进行了偏移处理，即eNodeB计算的寻呼时间窗口起始时间与MME计算的寻呼窗口起始时间存在偏差值时，可通过执行如下命令的“NB-S1模式寻呼窗口差值”参数进行配置。

   **SET M2MCTRL**

   由于eNodeB和MME上的时间可能存在时间差，或eNodeB为了减少SFN的跳变，在计算H-SFN时以SFN为准对H-SFN进行偏移，导致eNodeB与MME计算得到的寻呼窗口起始时间有差值，如果MME严格按照计算得出的寻呼窗口进行寻呼，可能错过部分eNodeB计算的寻呼窗口而导致寻呼成功率较低。
4. 增加M2M终端省电策略。

   **ADD M2MPLCY**

   “窄带S1模式寻呼时间窗口时长”设置时，建议NBPTW的值至少为NB-IoT Default Paging DRX值的2倍，这样eNodeB在NBPTW窗口内可以有多次机会寻呼用户。NB-IoT Default Paging DRX值是eNodeB在S1 Setup Request消息中携带给MME的。
5. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

某APNNI为"huawei.com"物联网行业用户需要开启NB-IoT（窄带）制式下的eDRX模式。部署前需与eNodeB侧协商对其H-SFN=0的参考时间类型和具体的参考时间点。例如协商后确定以GPS的起始时间（1980年1月6日00:00:00）作为与eNodeB对齐H-SFN=0的参考时间。执行如下操作进行完成任务部署。

脚本

//设置H-SFN参考时间。假设当前时间为2017年01月01日，则当前时间与参考时间闰秒差为18s。

```
SET HSFNTIME: TIMETYPE=GPS, GPSBEGIN=YES, GPSLEAPSEC=18;
```

//设置M2M控制参数。

```
SET M2MCTRL: NBEDRXPAGDIFF=SAME, USERPLANOPT=YES;
```

//配置M2M终端省电策略。

```
ADD M2MPLCY: SUBRANGE=ALL_USER, APNNI="huawei.com", EDRXSW=ON, NBECL=USE_UE_REQUEST, NBPTW=USE_UE_REQUEST, NBPTWSUBPRI=NO;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2EDRX01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
