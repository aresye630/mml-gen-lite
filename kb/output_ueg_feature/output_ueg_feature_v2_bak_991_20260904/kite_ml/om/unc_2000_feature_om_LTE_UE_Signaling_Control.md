# 激活LTE UE信令控制

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活LTE UE信令控制功能的操作过程。

**说明** 

适用于MME。

## 必备事项

前提条件

- 请仔细阅读GWFD-020909 LTE UE信令控制特性概述。
- 如果采用Parking APN激活的抑制规则，需要S-GW/P-GW对Parking APN配置不进行数据业务和不生成话单；需要MME增加Parking APN的DNS解析配置，或增加DNS服务器的配置，Parking APN的DNS解析配置请参考配置Hostfile的数据，增加DNS服务器的配置请参考配置到DNS相关数据。
- 已完成加载License。

数据

| 类别                | 参数名称                                | 取值样例                                   | 获取方法   | 说明                                                                              |
|:------------------|:------------------------------------|:---------------------------------------|:-------|:--------------------------------------------------------------------------------|
| ADD IMEILIB       | 设备型号核准号码(IMEITAC)                   | 12345678                               | 全网规划   | 配置IMEI和终端类型的对应关系。                                                               |
| ADD IMEILIB       | 终端类型（UETYPE）                        | Android                                | 全网规划   | 配置IMEI和终端类型的对应关系。                                                               |
| SET S1SMARTPARA   | 附着异常识别门限（ATTACHTHRESH）              | 30                                     | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | 附着异常测量周期（ATTACHMEPERIOD）            | 3600                                   | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | 服务请求异常识别门限（SRVREQTHRESH）            | 100                                    | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | 服务请求异常测量周期（SRVREQMEPERIOD）          | 3600                                   | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | 控制面服务请求异常识别门限（CPSRVREQTHRESH）       | 100                                    | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | 控制面服务请求异常测量周期（CPSRVREQMEPERIOD）     | 3600                                   | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | PDN连接异常识别门限（PDNCONNTHRESH）          | 30                                     | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | PDN连接异常测量周期（PDNCONNMEPERIOD）        | 3600                                   | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| SET S1SMARTPARA   | Parking APN（PARKINGAPN）             | PARKING                                | 全网规划   | 配置S1模式信令抑制参数。                                                                   |
| ADD S1SMARTRULE   | 终端类型（UETYPE）                        | Android                                | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 附着抑制措施（ATTACHCTRLRULE）              | SPECCAUSEREJ                           | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 附着拒绝原因（ATTACHREJCAUSE）              | IMPLICITLY_DETACHED                    | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 服务请求抑制措施（SRVREQCTRLRULE）            | SPECCAUSEREJ                           | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 服务请求拒绝原因（SRVREJCAUSE）               | PLMN_NOT_ALLOWED                       | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 控制面服务请求抑制措施（CPSRVREQCTRLRULE）       | SPECCAUSEREJ                           | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 控制面服务请求拒绝原因（CPSRVREJCAUSE）          | PLMN_NOT_ALLOWED                       | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | PDN连接抑制措施（PDNCONNCTRLRULE）          | SPECCAUSEREJ                           | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 连接拒绝原因（PDNCONNREJCAUSEPDN）          | UNKNOWN_OR_MISSING_APN                 | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| ADD S1SMARTRULE   | 抑制分离原因（DETACHCAUSE）                 | TA_NOT_ALLOWED                         | 全网规划   | 配置S1模式信令抑制规则。 本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。                               |
| SET S1SMARTPARA   | 附着异常抑制时长（ATTACHDURATION）            | 60                                     | 全网规划   | 配置抑制唤醒参数。                                                                       |
| SET S1SMARTPARA   | 服务请求异常抑制时长（SRVREQDURATION）          | 60                                     | 全网规划   | 配置抑制唤醒参数。                                                                       |
| SET S1SMARTPARA   | 控制面服务请求异常抑制时长（CPSRVREQDURATION）     | 60                                     | 全网规划   | 配置抑制唤醒参数。                                                                       |
| SET S1SMARTPARA   | PDN连接异常抑制时长（PDNCONNDURATION）        | 60                                     | 全网规划   | 配置抑制唤醒参数。                                                                       |
| ADD S1SMARTRULE   | Backoff Timer分配开关（BACKOFFSW）        | ON                                     | 全网规划   | 配置抑制唤醒参数。 “Parking APN唤醒措施”设置为“CNDETACH(网络侧分离)”时，唤醒会影响用户其他正常APN的业务，导致正在使用的业务中断。 |
| ADD S1SMARTRULE   | Parking APN唤醒措施（PARKAPNWAKEUPRULE）  | CNDEACT                                | 全网规划   | 配置抑制唤醒参数。 “Parking APN唤醒措施”设置为“CNDETACH(网络侧分离)”时，唤醒会影响用户其他正常APN的业务，导致正在使用的业务中断。 |
| ADD S1SMARTPLCY   | 用户范围（SUBRANGE）                      | IMSI_PREFIX                            | 全网规划   | 配置信令抑制的用户范围。                                                                    |
| ADD S1SMARTPLCY   | IMSI前缀（IMSIPRE）                     | 1230301                                | 全网规划   | 配置信令抑制的用户范围。                                                                    |
| ADD S1SMARTPLCY   | MSISDN前缀（MSISDNPRE）                 | -                                      | 全网规划   | 配置信令抑制的用户范围。                                                                    |
| ADD S1SMARTPLCY   | 附着异常识别门限（ATTACHTHRESH）              | 30                                     | 全网规划   | 配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。                                                |
| ADD S1SMARTPLCY   | 附着异常测量周期（秒）（ATTACHMEPERIOD）         | 3600                                   | 本端规划   | 配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。                                                |
| ADD S1SMARTPLCY   | 附着异常抑制时长（分钟）（ATTACHDURATION）        | 60                                     | 全网规划   | 配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。                                                |
| ADD S1SMARTPLCY   | 附着抑制措施（ATTACHCTRLRULE）              | SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1  | 全网规划   | 配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。                                                |
| ADD S1SMARTPLCY   | 附着拒绝原因（ATTACHREJCAUSE）              | NO_SUITABLE_CELLS_IN_TA                | 全网规划   | 配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。                                                |
| ADD S1SMARTPLCY   | 服务请求异常识别门限（次）（SRVREQTHRESH）         | 100                                    | 全网规划   | 配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。                                              |
| ADD S1SMARTPLCY   | 服务请求异常测量周期（秒）（SRVREQMEPERIOD）       | 3600                                   | 本端规划   | 配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。                                              |
| ADD S1SMARTPLCY   | 服务请求异常抑制时长（分钟）（SRVREQDURATION）      | 60                                     | 全网规划   | 配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。                                              |
| ADD S1SMARTPLCY   | 服务请求抑制措施（SRVREQCTRLRULE）            | SPECCAUSEREJ-1&CNDETACH-1              | 全网规划   | 配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。                                              |
| ADD S1SMARTPLCY   | 服务请求拒绝原因（SRVREJCAUSE）               | NO_SUITABLE_CELLS_IN_TA                | 全网规划   | 配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。                                              |
| ADD S1SMARTPLCY   | 控制面服务请求异常识别门限(次)（CPSRVREQTHRESH）    | 100                                    | 全网规划   | 配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。                                           |
| ADD S1SMARTPLCY   | 控制面服务请求异常测量周期(秒)（CPSRVREQMEPERIOD）  | 3600                                   | 本端规划   | 配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。                                           |
| ADD S1SMARTPLCY   | 控制面服务请求异常抑制时长(分钟)（CPSRVREQDURATION） | 60                                     | 全网规划   | 配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。                                           |
| ADD S1SMARTPLCY   | 控制面服务请求抑制措施（CPSRVREQCTRLRULE）       | SPECCAUSEREJ-1&CNDETACH-1              | 全网规划   | 配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。                                           |
| ADD S1SMARTPLCY   | 控制面服务请求拒绝原因（CPSRVREJCAUSE）          | NO_SUITABLE_CELLS_IN_TA                | 全网规划   | 配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。                                           |
| ADD S1SMARTPLCY   | PDN连接异常识别门限（次）（PDNCONNTHRESH）       | 30                                     | 全网规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | PDN连接异常测量周期（秒）（PDNCONNMEPERIOD）     | 3600                                   | 本端规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | PDN连接异常抑制时长（分钟）（PDNCONNDURATION）    | 60                                     | 全网规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | PDN连接抑制措施（PDNCONNCTRLRULE）          | SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1 | 全网规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | PDN连接拒绝原因（PDNCONNREJCAUSE）          | MULTI_PDN_FOR_APN_NOT_ALLOWED          | 全网规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | Backoff Timer分配开关（BACKOFFSW）        | ON                                     | 全网规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | Back off timer最小值（秒）（MINBOT）        | 660                                    | 本端规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | Back off timer最大值（秒）（MAXBOT）        | 3000                                   | 本端规划   | 配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。                                             |
| ADD S1SMARTPLCY   | Parking APN（PARKINGAPN）             | PARKING                                | 全网规划   | 配置执行Parking APN激活抑制策略时使用的APN NI。                                                |
| ADD S1SMARTPLCY   | 抑制分离原因（DETACHCAUSE）                 | NO_SUITABLE_CELLS_IN_TA                | 全网规划   | 设置网络侧发起的分离请求消息中携带的协议原因值。                                                        |
| ADD S1SMARTPLCY   | Parking APN唤醒措施（PARKAPNWAKEUPRULE）  | CNDEACT                                | 全网规划   | 设置当对用户进行Parking APN激活抑制的时间超时后，系统通知用户重新接入业务的方式。                                  |
| SET SOFTPARAOFBIT | 参数类型（DT）                            | BYTE_EX_B                              | 本端规划   | 通过软参BYTE_EX_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。                      |
| SET SOFTPARAOFBIT | 参数索引（PARANUM）                       | 141                                    | 本端规划   | 通过软参BYTE_EX_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。                      |
| SET SOFTPARAOFBIT | 参数值（VALUE）                          | 1                                      | 本端规划   | 通过软参BYTE_EX_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。                      |
| SET SOFTPARAOFBIT | 比特位（POSITION）                       | 8                                      | 本端规划   | 通过软参BYTE_EX_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。                      |

## 操作流程

激活LTE UE信令控制操作流程如图1所示。

**图1** 激活LTE UE信令控制操作流程

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 配置识别终端类型的数据库。
   1. 查询S1模式IMEI配置。

      **LST S1IMEICFG**

      - “IMEI获取策略”等于“获取IMEI”或“获取IMEISV”，操作结束。
      - “IMEI获取策略”等于“不获取”，执行3.b。
   2. 修改S1模式IMEI配置。

      **MOD S1IMEICFG**

      **说明** 

      将“IMEI获取策略”设置为“获取IMEI”或“获取IMEISV”。
   3. 增加IMEI库记录。

      **ADD IMEILIB**
4. **可选：**配置异常信令识别门限。

   **说明** 

   - 如果不配置如下参数，系统会根据默认值对Smartphone用户异常行为进行识别。
     - “ATTACHTHRESH（附着异常识别门限）”和“ATTACHMEPERIOD（附着异常测量周期）”
     - “PDNCONNTHRESH（PDN连接异常识别门限）”和“PDNCONNMEPERIOD（PDN连接异常测量周期）”
     - “SRVREQTHRESH（服务请求异常识别门限）”和“SRVREQMEPERIOD（服务请求异常测量周期）”
     - “CPSRVREQTHRESH（控制面服务请求异常识别门限）”和“CPSRVREQMEPERIOD（控制面服务请求异常测量周期）”
   - 特性部署时“附着异常识别门限(次)”设置须大于10次，为了测试方便，当此参数设置小于或等于10时，需要将软参ByteEx21Bit7设置为1。

   **SET S1SMARTPARA**
5. 增加异常信令抑制规则。

   **ADD S1SMARTRULE**

   **说明** 

   - 针对每一种终端类型，系统可以配置0～3个具体规则项，并会自动按照特定原因值拒绝激活、Parking APN激活、丢弃、网络侧分离的顺序依次执行，直到用户停止异常激活行为。
   - 网络侧主动分离用户是抑制用户激活最有效的规则，一般最后采用此规则。
6. **可选：**配置Parking APN参数。

   **SET S1SMARTPARA**

   **说明** 

   - 4G用户Service Request、Control Plane Service Request异常的抑制规则组不包含“Parking APN激活”，因此对Service Request、Control Plane Service Request异常信令的抑制不需要配置Parking APN。
   - Parking APNNI参数的其他应用场景，请参考Parking APNNI相关操作。
7. **可选：**配置抑制唤醒参数。

   **说明** 

   - 如果不配置“附着异常抑制时长”、“服务请求异常抑制时长”、“控制面服务请求异常抑制时长”、“PDN连接异常抑制时长”，系统会根据参数系统初始设置值执行相应唤醒流程。
   - “Backoff Timer分配开关”开启时，当系统发现终端PDN连接建立异常后，给终端回复PDN连接拒绝消息，在消息中携带Backoff Timer。Backoff Timer为UE和网络启动的定时器，在该定时器时间内，UE不允许发起PDN连接流程。如果UE在定时器时间内仍然发起了PDN连接流程，系统会拒绝该流程。

   **SET S1SMARTPARA**

   **ADD S1SMARTRULE**
8. 配置基于指定用户范围进行异常信令抑制。

   **ADD S1SMARTPLCY**
9. **可选：**通过软参BYTE\_EX\_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。

   **SET SOFTPARAOFBIT**

## 任务示例

任务描述

为了减轻由于UE的异常行为对网络侧的影响，有效地减少网络中的异常信令，提升网络可用性和可靠性，对4G用户异常反复发送Attach Request、PDN Connectivity Request、Service Request、Control Plane Service Request消息进行抑制，需要对用户手机采用抑制唤醒规则最终使其恢复正常业务。

针对Android手机的终端类型，配置执行三种抑制激活规则（特定原因值拒绝、Parking APN激活、丢弃请求）来消除用户异常行为。

对于IMSI前缀为“1230301”的用户异常反复发送Attach Request、PDN Connectivity Request、Service Request、Control Plane Service Request消息的场景进行信令抑制，并执行三种抑制激活规则（特定原因值拒绝、Parking APN激活、丢弃请求）来消除用户异常行为。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2LUSC01", SWITCH=ENABLE;
```

//配置IMEI库。

```
ADD IMEILIB: IMEITAC="12345678", UETYPE=ANDROID;
```

//设置Smartphone用户Attach Request、PDN Connectivity Request、Service Request、Control Plane Service Request消息异常行为识别门限。

```
SET S1SMARTPARA: ATTACHTHRESH=30, ATTACHMEPERIOD=3600, SRVREQTHRESH=100, SRVREQMEPERIOD=3600, CPSRVREQTHRESH=100, CPSRVREQMEPERIOD=3600, PDNCONNTHRESH=30, PDNCONNMEPERIOD=3600;
```

//增加异常信令抑制规则、抑制唤醒参数。

```
ADD S1SMARTRULE: UETYPE=ANDROID, ATTACHCTRLRULE=SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1, ATTACHREJCAUSE=IMPLICITLY_DETACHED, SRVREQCTRLRULE=SPECCAUSEREJ-1&CNDETACH-1, SRVREJCAUSE=PLMN_NOT_ALLOWED, CPSRVREQCTRLRULE=SPECCAUSEREJ-1&CNDETACH-1, CPSRVREJCAUSE=PLMN_NOT_ALLOWED, PDNCONNCTRLRULE=SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1, PDNCONNREJCAUSE=MULTI_PDN_FOR_APN_NOT_ALLOWED, DETACHCAUSE=NO_SUITABLE_CELLS_IN_TA, BACKOFFSW=ON, PARKAPNWAKEUPRULE=CNDEACT;
```

//配置Parking APN参数。

```
SET S1SMARTPARA: PARKINGAPN="PARKING";
```

//配置抑制唤醒参数。

```
SET S1SMARTPARA: ATTACHDURATION=60, SRVREQDURATION=60, CPSRVREQDURATION=60, PDNCONNDURATION=60;
```

//配置基于指定用户范围进行异常信令抑制。

```
ADD S1SMARTPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="1230301", ATTACHTHRESH=30, ATTACHMEPERIOD=3600, ATTACHDURATION=60, ATTACHCTRLRULE=SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1, ATTACHREJCAUSE=NO_SUITABLE_CELLS_IN_TA, SRVREQTHRESH=100, SRVREQMEPERIOD=3600, SRVREQDURATION=60, SRVREQCTRLRULE=SPECCAUSEREJ-1&CNDETACH-1, SRVREJCAUSE=NO_SUITABLE_CELLS_IN_TA, CPSRVREQTHRESH=100, CPSRVREQMEPERIOD=3600, CPSRVREQDURATION=60, CPSRVREQCTRLRULE=SPECCAUSEREJ-1&CNDETACH-1, CPSRVREJCAUSE=NO_SUITABLE_CELLS_IN_TA, PDNCONNTHRESH=30, PDNCONNMEPERIOD=3600, PDNCONNDURATION=60, PDNCONNCTRLRULE=SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1, PDNCONNREJCAUSE=MULTI_PDN_FOR_APN_NOT_ALLOWED, BACKOFFSW=ON, MINBOT=660, MAXBOT=3000, PARKINGAPN="PARKING", DETACHCAUSE=NO_SUITABLE_CELLS_IN_TA, PARKAPNWAKEUPRULE=CNDEACT;
```

//可选：通过软参BYTE\_EX\_B141 BIT8配置制在移除信令抑制规则后，立即清除受对应规则抑制的用户的信令抑制状态。

```
SET SOFTPARAOFBIT: DT=BYTE_EX_B, PARANUM=141, VALUE=VALUE_1, POSITION=8;
```