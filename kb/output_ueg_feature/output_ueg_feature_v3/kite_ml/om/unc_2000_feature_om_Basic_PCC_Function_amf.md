# 配置AM策略和UE策略

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当需要配置AM策略和UE策略时，请参考本页面。

本版本AMF暂不支持与PCF交互。

## 必备事项

前提条件

* 请仔细阅读特性概述。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD PCFSELPLCY** | 用户范围（SUBRANGE） | HOME\_USER | 全网规划 | AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。 |
|  | 是否适用目标PLMN（TGTPLMNSW） | NO | 全网规划 |  |
|  | 是否适用SUPI（SUPISW） | YES | 全网规划 |  |
|  | 是否适用GPSI（GPSISW） | NO | 全网规划 |  |
|  | 是否适用网络切片（NSSW） | NO | 全网规划 |  |
|  | 是否重选PCF（RETRYSW） | YES | 全网规划 | AMF在收到初选PCF的5xx原因值后，是否重选PCF再次重试AM策略和UE策略偶联创建流程。 |
|  | 描述信息（DESC） | for home user |  | 自定义，便于运维即可。 |
| **ADD AMUEPLCYCTRL** | 用户范围（SUBRANGE） | HOME\_USER | 全网规划 | 在AMF上配置AM策略和UE策略控制参数的用户范围。 |
|  | 网络切片群组标识（NSGRPID） | 0 | 全网规划 | 0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。 |
|  | 是否建立AM策略偶联（ISAMASSOC） | NO | 固定取值 | AMF与PCF无交互，使用样例值。 |
|  | 是否建立UE策略偶联（ISUEASSOC） | NO | 固定取值 |  |
|  | 描述信息（DESC） | Enable UE Policy for Home Subscribers | 本端规划 | 描述配置AM策略和UE策略控制参数的用户（群），便于记忆。 |
| **ADD NGMMSUBDATA** | 用户范围（SUBRANGE） | HOME\_USER | 全网规划 | 在AMF上配置哪些用户可使用本地RFSP索引。 |
|  | RAT限制（RATRESTRICT） | NR | 全网规划 | 此处以5G终端接入5G Core为例。 |
|  | 核心网类型限制（CORERESTRICT） | FIFTHGC | 全网规划 |  |
|  | RFSP索引（RFSPINDEX） | 5 | 全网规划 | 取值非0时，此处是本地配置的RFSP索引。  取值为0时，标识未配置本地的RFSP索引。 |
|  | RFSP优先级（RFSPPRI） | CFG\_FIRST | 全网规划 | * 设置为“CFG\_FIRST”，无论用户是否签约RFSP ID，均使用本地配置的RFSP索引。该场景下本地的“RFSP索引”不能为“0”。 * 设置为“SUB\_FIRST”时，优先使用用户签约的RFSP ID，如用户未签约RFSP ID，使用本地配置的RFSP索引。   AMF根据该配置，决策携带哪个RFSP索引 给PCF。后续处理为：   * PCF返回RFSP索引时，AMF将PCF返回的RFSP索引发送给无线侧。 * PCF未返回RFSP索引时，AMF将此处决策的RFSP索引发送给无线侧。 |
| **MOD CPNFPROFILE** | NF实例名称（NFINSTANCENAME） | SMF\_Instance\_0 | - | 根据NFLOC选择PCF时需要规划。 |
|  | 位置信息（LOCALITY） | beijing | 全网规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开License配置开关。

   **SET LICENSESWITCH**
3. 配置AMF选择PCF的策略信息。

   **ADD PCFSELPLCY**
4. 配置应用网络侧规划的AM策略/UE策略的用户群。

   **ADD AMUEPLCYCTRL**

   默认情况下，未开启网络侧规划的AM策略/UE策略。
5. 配置本地的RFSP索引。用户未签约RFSP ID，或签约的RFSP ID不适用时需要配置。

   **ADD NGMMSUBDATA**
6. 配置根据位置选择PCF。

   **MOD CPNFPROFILE**

## 任务示例

任务描述

* 任务实例一：规划AMF开启本地PCC功能，使用本地配置的AM策略和UE策略。
* 任务实例二：规划AMF开启动态PCC功能，从PCF获取AM策略和UE策略。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2PCCBF01", SWITCH=ENABLE;
```

//（任务实例一）在AMF上配置应用本地配置的AM策略和UE策略的用户群。

```
ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=NO, ISUEASSOC=NO, DESC="Enable UE Policy for Home Subscribers";
```

//（任务实例二）配置AMF选择PCF的策略信息。

```
ADD PCFSELPLCY: SUBRANGE=HOME_USER, TGTPLMNSW=NO, SUPISW=YES, GPSISW=NO, NSSW=NO,  RETRYSW=YES, DESC="for home user";
```

//（任务实例二）在AMF上配置应用网络侧规划的AM策略和UE策略的用户群。

```
ADD AMUEPLCYCTRL: SUBRANGE=HOME_USER, NSGRPID=0, ISAMASSOC=YES, ISUEASSOC=YES, DESC="Enable UE Policy for Home Subscribers";
```

//在AMF上配置本地的RFSP索引，并且本地配置的RFSP索引优先级高于签约的RFSP索引。

```
ADD NGMMSUBDATA: SUBRANGE=HOME_USER, RATRESTRICT=EUTRA-0&NR-1, CORERESTRICT=FIFTHGC, RFSPPRI=CFG_FIRST, RFSPINDEX=5;
```

版权所有 © 华为技术有限公司
