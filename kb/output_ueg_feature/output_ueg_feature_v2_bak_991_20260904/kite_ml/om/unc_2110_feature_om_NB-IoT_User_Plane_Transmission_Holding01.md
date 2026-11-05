# 激活NB-IoT用户面传输通道保活

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活NB-IoT用户面传输通道保活的操作过程。

NB-IoT终端数据收发频率低、数据包较小且多数情况为单向发送（例如智能抄表），建立、释放S1–U连接和数据无线承载信令开销大，需要一种高效的小数据传输解决方案。3GPP协议针对此类业务定义了用户面优化功能UP-CIoT（User Plane CIoT EPS Optimization）。UP-CIoT的方式是当终端进入ECM-IDLE态时，UE、eNodeB和MME保存用于恢复连接的S1-AP关联、UE上下文和承载上下文数据。当需要恢复数传时，无需进行频繁的E-RAB重建，提升数传效率，节省信令开销。

**说明** 

适用于MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-026106 NB-IoT用户面传输通道保活特性概述。
- 完成加载License。

数据

| 类别          | 参数名称                           | 取值样例                       | 获取方法   | 说明                                                        |
|:------------|:-------------------------------|:---------------------------|:-------|:----------------------------------------------------------|
| ADD M2MPLCY | 用户范围（SUBRANGE）                 | IMSI_PREFIX                | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | IMSI前缀（IMSIPRE）                | 123037301                  | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | APNNI（APNNI）                   | HUAWEI1.com                | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY | S1-U能力（S1UCAPA）                | SUPPORT_S1UDATA_AND_UP     | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD TAICIOT | 起始TAI（BEGINTAI）                | 123037301                  | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |
| ADD TAICIOT | 终止TAI（ENDTAI）                  | 123037302                  | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |
| ADD TAICIOT | 窄带数据传输能力指示（NBDATATRANSSUPPORT） | SUPPORT_UP-1&SUPPORT_S1U-1 | 全网规划   | 增加指定TAI下eNodeB支持的CIoT能力。                                  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置UP-CIoT功能。
   1. 查询某指定用户范围的相关配置。

      **LST M2MPLCY**
   2. **可选：**如果2.a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围配置UP-CIoT功能。

      **ADD M2MPLCY**
   3. **可选：**如果2.a查询到系统已存在该指定用户范围的相关配置，且未配置UP-CIoT功能，则执行此步骤，为该用户范围添加UP-CIoT功能。

      **MOD M2MPLCY**
3. **可选：**配置某指定TAI下eNodeB的UP-CIoT能力。
   1. 查询某指定TAI下相关配置。

      **LST TAICIOT**
   2. **可选：**如果3.a未查询到该指定TAI下的相关配置，则执行此步骤，为该TAI下的eNodeB配置UP-CIoT能力。

      **ADD TAICIOT**
   3. **可选：**如果3.a查询到系统已存在该指定TAI下的相关配置，且不支持UP-CIoT能力，则执行此步骤，为该TAI下的eNodeB添加UP-CIoT能力。

      **MOD TAICIOT**
4. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

假设某行业用户APNNI为"HUAWEI1.com"，运营商为其分配了IMSI前缀为"123037301"的号段，配置本特性。

脚本

//配置该用户的UP-CIoT能力。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123037301", APNNI="HUAWEI1.com", S1UCAPA=SUPPORT_S1UDATA_AND_UP;
```

//配置eNodeB的UP-CIoT能力。

```
ADD TAICIOT: BEGINTAI="123037301", ENDTAI="123037301", NBDATATRANSSUPPORT=SUPPORT_UP-1&SUPPORT_S1U-1;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2UPTH01", SWITCH=ENABLE;
```