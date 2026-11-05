# 激活基于HSS的P-CSCF故障恢复

## 操作场景

本操作指导介绍在运行网络中激活基于HSS的P-CSCF故障恢复的操作过程。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-025807 基于HSS的P-CSCF故障恢复特性概述。
* 已完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD DMCMPTBYIMSI** | SUBRANGE | IMSI\_PREFIX | 全网规划 | 基于HSS的P-CSCF故障恢复特性 |
|  | IMSIPRE | 123123 |  |  |
|  | SF2 | FLSTID2\_BIT16-1 |  |  |
| **SET DMCMPT** | SF2 | FLSTID2\_BIT16-1 | 全网规划 |  |
| **SET CPGLOBALIMS** | UDMPCSCF | ENABLE | 本端规划 | 基于UDM的P-CSCF故障恢复模式为释放PDU时，使用样例值。 |
|  | UDMPCSCFMODE | PDUREACTIVATE | 本端规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置支持基于HSS的P-CSCF故障恢复特性。

   **SET DMCMPT**

   **SET CPGLOBALIMS**

   **ADD DMCMPTBYIMSI**

   **LST DMCMPT**

   命令**SET DMCMPT**和**ADD DMCMPTBYIMSI**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。
3. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
4. **可选：**清除HSS信息。

   **CLR HSSINFO**

   根据3GPP 23.380定义，只要有一个用户通过Update Location Request消息通知HSS MME支持P-CSCF Restoration特性，HSS即认为整个MME支持此特性。如果HSS实现符合协议定义，则无需执行本步骤。

## 任务示例

任务描述

激活基于HSS的P-CSCF故障恢复特性，假设仅本网HSS支持本特性，其他用户的归属HSS都不支持本特性。

脚本

//进入“MML命令行-UEG”窗口。

//配置支持基于HSS的P-CSCF故障恢复特性。（实际部署时，需要根据HSS是否支持本特性，组合如下命令进行配置）

* 所有HSS都支持此特性：

  ```
  SET DMCMPT: SF2=FLSTID2_BIT16-1;
  ```
* 设置基于UDM的P-CSCF故障恢复模式为释放PDU。

  ```
  SET CPGLOBALIMS: UDMPCSCF=ENABLE, UDMPCSCFMODE=PDUREACTIVATE;
  ```
* 本网所有的HSS支持此特性，外网所有HSS不支持此特性：

  ```
  ADD DMCMPTBYIMSI: SUBRANGE=HOME_USER, NOID=0, SF2=FLSTID2_BIT16-1;
  ```
* 仅46123和46321为IMSI前缀的用户注册的HSS支持此特性：

  ```
  ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46123", SF2=FLSTID2_BIT16-1;
  ADD DMCMPTBYIMSI: SUBRANGE=IMSI_PREFIX, IMSIPRE="46321", SF2=FLSTID2_BIT16-1;
  ```

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2FRPH02", SWITCH=ENABLE;
```

//清除HSS信息。

```
CLR HSSINFO: HSSHTNAME="hss.epc.mnc456.mcc123.3gppnetwork.org";
```

版权所有 © 华为技术有限公司
