# 激活Non-IP数据传输

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活Non-IP数据传输的操作过程。

本特性支持NB-IoT（Narrow Band Internet of Things）制式UE通过NB-IoT RAN接入MME后，建立Non-IP的PDN上下文，并采用Non-IP进行数据传输，从而减小传送数据包大小，提高传输效率和空口容量。

**说明** 

适用于MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-026107 Non-IP数据传输特性概述（MME）。
- 已按照配置到S-GW的数据完成S11-U接口的配置。
- 完成加载License。

数据

| 类别               | 参数名称                     | 取值样例          | 获取方法   | 说明                                                        |
|:-----------------|:-------------------------|:--------------|:-------|:----------------------------------------------------------|
| ADD M2MPLCY      | 用户范围（SUBRANGE）           | IMSI_PREFIX   | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY      | IMSI前缀（IMSIPRE）          | 12303         | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY      | APNNI（APNNI）             | huawei.com    | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD M2MPLCY      | CP优化功能（CPOPSW）           | SUPPORT       | 全网规划   | 增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。 |
| ADD NONIPSUBCTRL | 用户范围（SUBRANGE）           | IMSI_PREFIX   | 全网规划   | 配置支持激活Non-IP类型PDN的APNNI。                                  |
| ADD NONIPSUBCTRL | IMSI前缀（IMSIPRE）          | 12303         | 全网规划   | 配置支持激活Non-IP类型PDN的APNNI。                                  |
| ADD NONIPSUBCTRL | 支持Non-IP的APNNI（SUPAPNNI） | ALL_APNNI     | 全网规划   | 配置支持激活Non-IP类型PDN的APNNI。                                  |
| SET DMCMPT       | 是否支持NBIoT RAT（NBIOTRAT）  | SUPPORT       | 全网规划   | 设置Diameter兼容性。                                            |
| SET DMCMPT       | 特性列表2（SF2）               | FLSTID2_BIT21 | 全网规划   | 设置Diameter兼容性。                                            |
| ADD MMECHARACT   | 对端设备范围（RANGE）            | ALL_MME       | 全网规划   | 增加MME属性配置信息。                                              |
| ADD MMECHARACT   | CIoT优化支持指示（CIOTIND）      | SGNIPDN       | 全网规划   | 增加MME属性配置信息。                                              |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 增加M2M策略参数。

   **ADD M2MPLCY**
3. （可选）设置Diameter兼容性。

   **SET DMCMPT**
4. （可选）当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要增加Non-IP APNNI配置。

   **ADD NONIPSUBCTRL**

   **说明** 

   - 当开启WSFD-215301 HSS免升级时，**ADD NONIPSUBCTRL**生效。
   - 当“SUPAPNNI”选为“SPECIAL\_APNNI”时，需要先通过**ADD APNNIGROUP**和**ADD APNNI**来绑定APNNI组。
   - 签约数据匹配时，如果UE未携带请求的APN NI，系统将使用签约的Non-IP Default APN作为该PDN的APN NI。
5. （可选）当用户发生Inter MME移动，且目标MME支持Non-IP数据传输时，需要增加MME属性配置信息。

   **ADD MMECHARACT**
6. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

某行业用户APNNI为"huawei.com"，运营商为其分配了IMSI前缀为"12303"的号段，配置本特性时，需要进行以下操作。

脚本

//增加M2M策略参数。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", APNNI="huawei.com", CPOPSW=SUPPORT;
```

//（可选）设置Diameter兼容性。

```
SET DMCMPT: SF2=FLSTID2_BIT21-1,NBIOTRAT=SUPPORT;
```

//（可选）当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要增加Non-IP APNNI配置。

```
ADD NONIPSUBCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", SUPAPNNI=ALL_APNNI;
```

//（可选）当用户发生Inter MME移动，需要目标MME支持Non-IP数据传输时，需要增加MME属性配置信息。

```
ADD MMECHARACT: RANGE=ALL_MME, CIOTIND=SGNIPDN-1;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2NOIP01", SWITCH=ENABLE;
```