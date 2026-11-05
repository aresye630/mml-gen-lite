# 激活基于信令面的数据传输（MME）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于信令面的数据传输的操作过程。

IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表）。本特性是3GPP协议针对此类业务定义的控制面优化功能CP-CIoT（Control Plane Cellular Internet of Thing），实现了数据包在终端和MME之间通过NAS消息传递，在MME和SGW-U间通过S11-U口传递，上、下行数传过程中无需频繁建立E-RAB，从而提升数传效率，节省不必要的信令开销。

**说明** 

适用于MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-026105 基于信令面的数据传输特性概述（MME）。
- 已按照配置到S-GW的数据完成S11-U接口的配置。
- 完成加载License。

数据

| 类别          | 参数名称                               | 取值样例                                    | 获取方法   | 相关命令                                                      |
|:------------|:-----------------------------------|:----------------------------------------|:-------|:----------------------------------------------------------|
| ADD M2MPLCY | 用户范围（SUBRANGE）                     | IMSI_PREFIX                             | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | IMSI前缀（IMSIPRE）                    | 123038101                               | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | APNNI（APNNI）                       | HUAWEI1.com                             | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | 长周期RAU或TAU定时器时长（小时）（LONGRAUTAUTMR） | 0                                       | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | CP优化功能（CPOPSW）                     | SUPPORT                                 | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD TAICIOT | 起始TAI（BEGINTAI）                    | 123037301                               | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |
| ADD TAICIOT | 终止TAI（ENDTAI）                      | 123037302                               | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |
| ADD TAICIOT | 窄带数据传输能力指示（NBDATATRANSSUPPORT）     | SUPPORT_CP-1&SUPPORT_UP-1&SUPPORT_S1U-0 | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置CP-CIoT功能。
   1. 查询某指定用户范围是否配置了CP-CIoT功能。

      **LST M2MPLCY**
   2. **可选：**如果步骤a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围配置CP-CIoT功能。

      **ADD M2MPLCY**
   3. **可选：**如果步骤a查询到系统已存在该指定用户范围的相关配置，则执行此步骤，为该用户范围添加CP-CIoT功能。

      **MOD M2MPLCY**
3. **可选：**配置某指定TAI下eNodeB的CP-CIoT能力。
   1. 查询某指定TAI下相关配置。

      **LST TAICIOT**
   2. **可选：**如果3.a未查询到该指定TAI下的相关配置，则执行此步骤，为该TAI下的eNodeB配置CP-CIoT能力。

      **ADD TAICIOT**
   3. **可选：**如果3.a查询到系统已存在该指定TAI下的相关配置，且不支持CP-CIoT能力，则执行此步骤，为该TAI下的eNodeB添加CP-CIoT能力。

      **MOD TAICIOT**
4. **可选：**配置Control Plane Service Request流程CHR单据的上报。

   系统支持通过命令**SET CHRCFG**和**SET CHRLOWPERFSVRSUB**配置在Control Plane Service Request流程成功或失败时是否上报CHR单据，配置过程参见激活CHR功能。
5. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

假设某行业用户APNNI为"HUAWEI1.com"，运营商为其分配了IMSI前缀为"123038101"的号段，配置本特性。

脚本

//配置CP-CIoT功能。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123038101", APNNI="HUAWEI1.com", LONGRAUTAUTMR=0,  CPOPSW=SUPPORT;
```

//配置eNodeB的CP-CIoT能力。

```
ADD TAICIOT: BEGINTAI="123037301", ENDTAI="123037302", NBDATATRANSSUPPORT=SUPPORT_CP-1;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2DNAS01", SWITCH=ENABLE;
```