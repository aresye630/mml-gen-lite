---
id: GWFD-020909
name: 激活LTE UE信令控制
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活LTE UE信令控制功能的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020909 LTE UE信令控制","激活LTE UE信令控制"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST S1IMEICFG')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE UE信令控制功能的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-020909 LTE UE信令控制特性概述。
* 如果采用Parking APN激活的抑制规则，需要S-GW/P-GW对Parking APN配置不进行数据业务和不生成话单；需要MME增加Parking APN的DNS解析配置，或增加DNS服务器的配置，Parking APN的DNS解析配置请参考配置Hostfile的数据，增加DNS服务器的配置请参考配置到DNS相关数据。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1imeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imeilib_list:
      type: items
      properties:
        IMEITAC:
          name: '设备型号核准号码'
          type: string
          maxLength: 15
          required: true
          description: '配置IMEI和终端类型的对应关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1smartpara_list:
      type: items
      properties:
        ATTACHTHRESH:
          name: '附着异常识别门限'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置S1模式信令抑制参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHMEPERIOD:
          name: '附着异常测量周期'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQTHRESH:
          name: '服务请求异常识别门限'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQMEPERIOD:
          name: '服务请求异常测量周期'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPSRVREQTHRESH:
          name: '控制面服务请求异常识别门限'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPSRVREQMEPERIOD:
          name: '控制面服务请求异常测量周期'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNTHRESH:
          name: 'PDN连接异常识别门限'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNMEPERIOD:
          name: 'PDN连接异常测量周期'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1smartrule_list:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: '配置S1模式信令抑制规则。  本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHREJCAUSE:
          name: '附着拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        SRVREQCTRLRULE:
          name: '服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREJCAUSE:
          name: '服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        CPSRVREQCTRLRULE:
          name: '控制面服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPSRVREJCAUSE:
          name: '控制面服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNREJCAUSE:
          name: '连接拒绝原因'
          type: string
          enum:
          - INSUFFICIENT_RESOURCES
          - MULTI_PDN_FOR_APN_NOT_ALLOWED
          - NETWORK_FAILURE
          - ODB
          - PROTOCOL_ERROR_UNSPECIFED
          - REQUEST_REJECT_BY_SGW_OR_PGW
          - REQUEST_SERVICE_NOT_SUBCRIBED
          - SERVICE_OPTION_NOT_SUPPORTED
          - UNKNOWN_OR_MISSING_APN
          - USER_AUTH_FAILED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MULTI_PDN_FOR_APN_NOT_ALLOWED
        DETACHCAUSE:
          name: '抑制分离原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        BACKOFFSW:
          name: 'Backoff Timer分配开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置抑制唤醒参数。  “Parking APN唤醒措施”设置为“CNDETACH(网络侧分离)”时，唤醒会影响用户其他正常APN的业务，导致正在使用的业务中断。'
          data_source: '全网规划'
          pattern: ''
          default: OFF
        PARKAPNWAKEUPRULE:
          name: 'Parking APN唤醒措施'
          type: string
          enum:
          - CNDEACT
          - CNDETACH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CNDEACT
    set_s1smartpara_list_1:
      type: items
      properties:
        PARKINGAPN:
          name: 'Parking APN'
          type: string
          maxLength: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1smartrule_list_1:
      type: items
      properties:
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - UNKNOWN_TYPE
          - WINDOWS
          required: true
          description: '配置S1模式信令抑制规则。  本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTACHREJCAUSE:
          name: '附着拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        SRVREQCTRLRULE:
          name: '服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREJCAUSE:
          name: '服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        CPSRVREQCTRLRULE:
          name: '控制面服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPSRVREJCAUSE:
          name: '控制面服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNREJCAUSE:
          name: '连接拒绝原因'
          type: string
          enum:
          - INSUFFICIENT_RESOURCES
          - MULTI_PDN_FOR_APN_NOT_ALLOWED
          - NETWORK_FAILURE
          - ODB
          - PROTOCOL_ERROR_UNSPECIFED
          - REQUEST_REJECT_BY_SGW_OR_PGW
          - REQUEST_SERVICE_NOT_SUBCRIBED
          - SERVICE_OPTION_NOT_SUPPORTED
          - UNKNOWN_OR_MISSING_APN
          - USER_AUTH_FAILED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MULTI_PDN_FOR_APN_NOT_ALLOWED
        DETACHCAUSE:
          name: '抑制分离原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        BACKOFFSW:
          name: 'Backoff Timer分配开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置抑制唤醒参数。  “Parking APN唤醒措施”设置为“CNDETACH(网络侧分离)”时，唤醒会影响用户其他正常APN的业务，导致正在使用的业务中断。'
          data_source: '全网规划'
          pattern: ''
          default: OFF
        PARKAPNWAKEUPRULE:
          name: 'Parking APN唤醒措施'
          type: string
          enum:
          - CNDEACT
          - CNDETACH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CNDEACT
    set_s1smartpara_list_2:
      type: items
      properties:
        ATTACHDURATION:
          name: '附着异常抑制时长'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: '配置抑制唤醒参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVREQDURATION:
          name: '服务请求异常抑制时长'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPSRVREQDURATION:
          name: '控制面服务请求异常抑制时长'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCONNDURATION:
          name: 'PDN连接异常抑制时长'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1smartplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: '配置信令抑制的用户范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHTHRESH:
          name: '附着异常识别门限'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置对指定用户范围进行附着异常的识别门限和信令抑制策略相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: 30
        ATTACHMEPERIOD:
          name: '附着异常测量周期（秒）'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3600
        ATTACHDURATION:
          name: '附着异常抑制时长（分钟）'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
        ATTACHCTRLRULE:
          name: '附着抑制措施'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ATTACHREJCAUSE:
          name: '附着拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        SRVREQTHRESH:
          name: '服务请求异常识别门限（次）'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置对指定用户范围进行服务请求异常的识别门限和信令抑制策略相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: 100
        SRVREQMEPERIOD:
          name: '服务请求异常测量周期（秒）'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3600
        SRVREQDURATION:
          name: '服务请求异常抑制时长（分钟）'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
        SRVREQCTRLRULE:
          name: '服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVREJCAUSE:
          name: '服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        CPSRVREQTHRESH:
          name: '控制面服务请求异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置对指定用户范围进行控制面服务请求异常的识别门限和信令抑制策略相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: 100
        CPSRVREQMEPERIOD:
          name: '控制面服务请求异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3600
        CPSRVREQDURATION:
          name: '控制面服务请求异常抑制时长(分钟)'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
        CPSRVREQCTRLRULE:
          name: '控制面服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPSRVREJCAUSE:
          name: '控制面服务请求拒绝原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        PDNCONNTHRESH:
          name: 'PDN连接异常识别门限（次）'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置对指定用户范围进行PDN连接异常的识别门限和信令抑制策略相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: 30
        PDNCONNMEPERIOD:
          name: 'PDN连接异常测量周期（秒）'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3600
        PDNCONNDURATION:
          name: 'PDN连接异常抑制时长（分钟）'
          type: integer
          minimum: 10
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
        PDNCONNCTRLRULE:
          name: 'PDN连接抑制措施'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNCONNREJCAUSE:
          name: 'PDN连接拒绝原因'
          type: string
          enum:
          - INSUFFICIENT_RESOURCES
          - MULTI_PDN_FOR_APN_NOT_ALLOWED
          - NETWORK_FAILURE
          - ODB
          - PROTOCOL_ERROR_UNSPECIFED
          - REQUEST_REJECT_BY_SGW_OR_PGW
          - REQUEST_SERVICE_NOT_SUBCRIBED
          - SERVICE_OPTION_NOT_SUPPORTED
          - UNKNOWN_OR_MISSING_APN
          - USER_AUTH_FAILED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MULTI_PDN_FOR_APN_NOT_ALLOWED
        BACKOFFSW:
          name: 'Backoff Timer分配开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: OFF
        MINBOT:
          name: 'Back off timer最小值（秒）'
          type: integer
          minimum: 1
          maximum: 1116000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 660
        MAXBOT:
          name: 'Back off timer最大值（秒）'
          type: integer
          minimum: 1
          maximum: 1116000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3000
        PARKINGAPN:
          name: 'Parking APN'
          type: string
          maxLength: 62
          required: false
          description: '配置执行Parking APN激活抑制策略时使用的APN NI。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DETACHCAUSE:
          name: '抑制分离原因'
          type: string
          enum:
          - CONGESTION
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - ILLEGAL_ME
          - ILLEGAL_UE
          - IMPLICITLY_DETACHED
          - IMSI_UNKNOWN_IN_HSS
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - PROTOCOL_ERROR_UNSPEC
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: '设置网络侧发起的分离请求消息中携带的协议原因值。'
          data_source: '全网规划'
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        PARKAPNWAKEUPRULE:
          name: 'Parking APN唤醒措施'
          type: string
          enum:
          - CNDEACT
          - CNDETACH
          required: false
          description: '设置当对用户进行Parking APN激活抑制的时间超时后，系统通知用户重新接入业务的方式。'
          data_source: '全网规划'
          pattern: ''
          default: CNDEACT
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: '通过软参BYTE_EX_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2LUSC01'
      SWITCH: ENABLE
    mod_s1imeicfg_list:
    - SUBRANGE: ''
    add_imeilib_list:
    - IMEITAC: '12345678'
      UETYPE: ANDROID
    set_s1smartpara_list:
    - ATTACHTHRESH: 30
      ATTACHMEPERIOD: 3600
      SRVREQTHRESH: 100
      SRVREQMEPERIOD: 3600
      CPSRVREQTHRESH: 100
      CPSRVREQMEPERIOD: 3600
      PDNCONNTHRESH: 30
      PDNCONNMEPERIOD: 3600
    add_s1smartrule_list:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1
      ATTACHREJCAUSE: IMPLICITLY_DETACHED
      SRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      SRVREJCAUSE: PLMN_NOT_ALLOWED
      CPSRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      CPSRVREJCAUSE: PLMN_NOT_ALLOWED
      PDNCONNCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1
      PDNCONNREJCAUSE: MULTI_PDN_FOR_APN_NOT_ALLOWED
      DETACHCAUSE: NO_SUITABLE_CELLS_IN_TA
      BACKOFFSW: ON
      PARKAPNWAKEUPRULE: CNDEACT
    set_s1smartpara_list_1:
    - PARKINGAPN: 'PARKING'
    add_s1smartrule_list_1:
    - UETYPE: ANDROID
      ATTACHCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1
      ATTACHREJCAUSE: IMPLICITLY_DETACHED
      SRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      SRVREJCAUSE: PLMN_NOT_ALLOWED
      CPSRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      CPSRVREJCAUSE: PLMN_NOT_ALLOWED
      PDNCONNCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1
      PDNCONNREJCAUSE: MULTI_PDN_FOR_APN_NOT_ALLOWED
      DETACHCAUSE: NO_SUITABLE_CELLS_IN_TA
      BACKOFFSW: ON
      PARKAPNWAKEUPRULE: CNDEACT
    set_s1smartpara_list_2:
    - ATTACHDURATION: 60
      SRVREQDURATION: 60
      CPSRVREQDURATION: 60
      PDNCONNDURATION: 60
    add_s1smartplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '1230301'
      ATTACHTHRESH: 30
      ATTACHMEPERIOD: 3600
      ATTACHDURATION: 60
      ATTACHCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&DISCARD-1
      ATTACHREJCAUSE: NO_SUITABLE_CELLS_IN_TA
      SRVREQTHRESH: 100
      SRVREQMEPERIOD: 3600
      SRVREQDURATION: 60
      SRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      SRVREJCAUSE: NO_SUITABLE_CELLS_IN_TA
      CPSRVREQTHRESH: 100
      CPSRVREQMEPERIOD: 3600
      CPSRVREQDURATION: 60
      CPSRVREQCTRLRULE: SPECCAUSEREJ-1&CNDETACH-1
      CPSRVREJCAUSE: NO_SUITABLE_CELLS_IN_TA
      PDNCONNTHRESH: 30
      PDNCONNMEPERIOD: 3600
      PDNCONNDURATION: 60
      PDNCONNCTRLRULE: SPECCAUSEREJ-1&PARKAPNACT-1&CNDETACH-1
      PDNCONNREJCAUSE: MULTI_PDN_FOR_APN_NOT_ALLOWED
      BACKOFFSW: ON
      MINBOT: 660
      MAXBOT: 3000
      PARKINGAPN: 'PARKING'
      DETACHCAUSE: NO_SUITABLE_CELLS_IN_TA
      PARKAPNWAKEUPRULE: CNDEACT
      MSISDNPRE: '-'
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 141
      VALUE: VALUE_1
      POSITION: 8
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置识别终端类型的数据库。

#### 3.1 查询S1模式IMEI配置。

#### “IMEI获取策略”等于“获取IMEI”或“获取IMEISV”，操作结束。

#### “IMEI获取策略”等于“不获取”，执行3.b。

#### 3.2 修改S1模式IMEI配置。

```jinja2
{%- set LST_S1IMEICFG=getParameterValue('LST S1IMEICFG') -%}
{%- if LST_S1IMEICFG=='不获取' -%}
    {%- for item in mod_s1imeicfg_list -%}
        MOD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 将“IMEI获取策略”设置为“获取IMEI”或“获取IMEISV”。

#### 3.3 增加IMEI库记录。

```jinja2
{%- for item in add_imeilib_list -%}
    ADD IMEILIB:
    {#- --- 必选参数 --- -#}
    IMEITAC="{{item.IMEITAC}}",
    UETYPE={{item.UETYPE}},
    ;
{%- endfor -%}
```

### 4 **可选：**配置异常信令识别门限。

#### 4.1 如果不配置如下参数，系统会根据默认值对Smartphone用户异常行为进行识别。

##### 4.1.1 “ATTACHTHRESH（附着异常识别门限）”和“ATTACHMEPERIOD（附着异常测量周期）”

##### 4.1.2 “PDNCONNTHRESH（PDN连接异常识别门限）”和“PDNCONNMEPERIOD（PDN连接异常测量周期）”

##### 4.1.3 “SRVREQTHRESH（服务请求异常识别门限）”和“SRVREQMEPERIOD（服务请求异常测量周期）”

##### 4.1.4 “CPSRVREQTHRESH（控制面服务请求异常识别门限）”和“CPSRVREQMEPERIOD（控制面服务请求异常测量周期）”

#### 4.2 特性部署时“附着异常识别门限(次)”设置须大于10次，为了测试方便，当此参数设置小于或等于10时，需要将软参ByteEx21Bit7设置为1。

```jinja2
{%- if is_optional_abnormal_signaling_threshold -%}
    {%- for item in set_s1smartpara_list -%}
        SET S1SMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHTHRESH is not none -%}
            ATTACHTHRESH={{item.ATTACHTHRESH}},
        {%- endif -%}
        {%- if item.ATTACHMEPERIOD is not none -%}
            ATTACHMEPERIOD={{item.ATTACHMEPERIOD}},
        {%- endif -%}
        {%- if item.SRVREQTHRESH is not none -%}
            SRVREQTHRESH={{item.SRVREQTHRESH}},
        {%- endif -%}
        {%- if item.SRVREQMEPERIOD is not none -%}
            SRVREQMEPERIOD={{item.SRVREQMEPERIOD}},
        {%- endif -%}
        {%- if item.CPSRVREQTHRESH is not none -%}
            CPSRVREQTHRESH={{item.CPSRVREQTHRESH}},
        {%- endif -%}
        {%- if item.CPSRVREQMEPERIOD is not none -%}
            CPSRVREQMEPERIOD={{item.CPSRVREQMEPERIOD}},
        {%- endif -%}
        {%- if item.PDNCONNTHRESH is not none -%}
            PDNCONNTHRESH={{item.PDNCONNTHRESH}},
        {%- endif -%}
        {%- if item.PDNCONNMEPERIOD is not none -%}
            PDNCONNMEPERIOD={{item.PDNCONNMEPERIOD}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加异常信令抑制规则。

```jinja2
{%- for item in add_s1smartrule_list -%}
    ADD S1SMARTRULE:
    {#- --- 必选参数 --- -#}
    UETYPE={{item.UETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ATTACHCTRLRULE is not none -%}
        ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
    {%- endif -%}
    {%- if item.ATTACHREJCAUSE is not none -%}
        ATTACHREJCAUSE={{item.ATTACHREJCAUSE}},
    {%- endif -%}
    {%- if item.SRVREQCTRLRULE is not none -%}
        SRVREQCTRLRULE={{item.SRVREQCTRLRULE}},
    {%- endif -%}
    {%- if item.SRVREJCAUSE is not none -%}
        SRVREJCAUSE={{item.SRVREJCAUSE}},
    {%- endif -%}
    {%- if item.CPSRVREQCTRLRULE is not none -%}
        CPSRVREQCTRLRULE={{item.CPSRVREQCTRLRULE}},
    {%- endif -%}
    {%- if item.CPSRVREJCAUSE is not none -%}
        CPSRVREJCAUSE={{item.CPSRVREJCAUSE}},
    {%- endif -%}
    {%- if item.PDNCONNCTRLRULE is not none -%}
        PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
    {%- endif -%}
    {%- if item.PDNCONNREJCAUSE is not none -%}
        PDNCONNREJCAUSE={{item.PDNCONNREJCAUSE}},
    {%- endif -%}
    {%- if item.DETACHCAUSE is not none -%}
        DETACHCAUSE={{item.DETACHCAUSE}},
    {%- endif -%}
    {%- if item.BACKOFFSW is not none -%}
        BACKOFFSW={{item.BACKOFFSW}},
    {%- endif -%}
    {%- if item.PARKAPNWAKEUPRULE is not none -%}
        PARKAPNWAKEUPRULE={{item.PARKAPNWAKEUPRULE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.1 针对每一种终端类型，系统可以配置0～3个具体规则项，并会自动按照特定原因值拒绝激活、Parking APN激活、丢弃、网络侧分离的顺序依次执行，直到用户停止异常激活行为。

#### 5.2 网络侧主动分离用户是抑制用户激活最有效的规则，一般最后采用此规则。

### 6 **可选：**配置Parking APN参数。

```jinja2
{%- if is_optional_parking_apn_params -%}
    {%- for item in set_s1smartpara_list_1 -%}
        SET S1SMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.PARKINGAPN is not none -%}
            PARKINGAPN="{{item.PARKINGAPN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.1 4G用户Service Request、Control Plane Service Request异常的抑制规则组不包含“Parking APN激活”，因此对Service Request、Control Plane Service Request异常信令的抑制不需要配置Parking APN。

#### 6.2 Parking APNNI参数的其他应用场景，请参考Parking APNNI相关操作。

### 7 **可选：**配置抑制唤醒参数。

#### 7.1 如果不配置“附着异常抑制时长”、“服务请求异常抑制时长”、“控制面服务请求异常抑制时长”、“PDN连接异常抑制时长”，系统会根据参数系统初始设置值执行相应唤醒流程。

#### 7.2 “Backoff Timer分配开关”开启时，当系统发现终端PDN连接建立异常后，给终端回复PDN连接拒绝消息，在消息中携带Backoff Timer。Backoff Timer为UE和网络启动的定时器，在该定时器时间内，UE不允许发起PDN连接流程。如果UE在定时器时间内仍然发起了PDN连接流程，系统会拒绝该流程。

```jinja2
{%- if is_optional_suppression_wakeup_params -%}
    {%- for item in add_s1smartrule_list_1 -%}
        ADD S1SMARTRULE:
        {#- --- 必选参数 --- -#}
        UETYPE={{item.UETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHCTRLRULE is not none -%}
            ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
        {%- endif -%}
        {%- if item.ATTACHREJCAUSE is not none -%}
            ATTACHREJCAUSE={{item.ATTACHREJCAUSE}},
        {%- endif -%}
        {%- if item.SRVREQCTRLRULE is not none -%}
            SRVREQCTRLRULE={{item.SRVREQCTRLRULE}},
        {%- endif -%}
        {%- if item.SRVREJCAUSE is not none -%}
            SRVREJCAUSE={{item.SRVREJCAUSE}},
        {%- endif -%}
        {%- if item.CPSRVREQCTRLRULE is not none -%}
            CPSRVREQCTRLRULE={{item.CPSRVREQCTRLRULE}},
        {%- endif -%}
        {%- if item.CPSRVREJCAUSE is not none -%}
            CPSRVREJCAUSE={{item.CPSRVREJCAUSE}},
        {%- endif -%}
        {%- if item.PDNCONNCTRLRULE is not none -%}
            PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
        {%- endif -%}
        {%- if item.PDNCONNREJCAUSE is not none -%}
            PDNCONNREJCAUSE={{item.PDNCONNREJCAUSE}},
        {%- endif -%}
        {%- if item.DETACHCAUSE is not none -%}
            DETACHCAUSE={{item.DETACHCAUSE}},
        {%- endif -%}
        {%- if item.BACKOFFSW is not none -%}
            BACKOFFSW={{item.BACKOFFSW}},
        {%- endif -%}
        {%- if item.PARKAPNWAKEUPRULE is not none -%}
            PARKAPNWAKEUPRULE={{item.PARKAPNWAKEUPRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_suppression_wakeup_params -%}
    {%- for item in set_s1smartpara_list_2 -%}
        SET S1SMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.ATTACHDURATION is not none -%}
            ATTACHDURATION={{item.ATTACHDURATION}},
        {%- endif -%}
        {%- if item.SRVREQDURATION is not none -%}
            SRVREQDURATION={{item.SRVREQDURATION}},
        {%- endif -%}
        {%- if item.CPSRVREQDURATION is not none -%}
            CPSRVREQDURATION={{item.CPSRVREQDURATION}},
        {%- endif -%}
        {%- if item.PDNCONNDURATION is not none -%}
            PDNCONNDURATION={{item.PDNCONNDURATION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置基于指定用户范围进行异常信令抑制。

```jinja2
{%- for item in add_s1smartplcy_list -%}
    ADD S1SMARTPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ATTACHTHRESH is not none -%}
        ATTACHTHRESH={{item.ATTACHTHRESH}},
    {%- endif -%}
    {%- if item.ATTACHMEPERIOD is not none -%}
        ATTACHMEPERIOD={{item.ATTACHMEPERIOD}},
    {%- endif -%}
    {%- if item.ATTACHDURATION is not none -%}
        ATTACHDURATION={{item.ATTACHDURATION}},
    {%- endif -%}
    {%- if item.ATTACHCTRLRULE is not none -%}
        ATTACHCTRLRULE={{item.ATTACHCTRLRULE}},
    {%- endif -%}
    {%- if item.ATTACHREJCAUSE is not none -%}
        ATTACHREJCAUSE={{item.ATTACHREJCAUSE}},
    {%- endif -%}
    {%- if item.SRVREQTHRESH is not none -%}
        SRVREQTHRESH={{item.SRVREQTHRESH}},
    {%- endif -%}
    {%- if item.SRVREQMEPERIOD is not none -%}
        SRVREQMEPERIOD={{item.SRVREQMEPERIOD}},
    {%- endif -%}
    {%- if item.SRVREQDURATION is not none -%}
        SRVREQDURATION={{item.SRVREQDURATION}},
    {%- endif -%}
    {%- if item.SRVREQCTRLRULE is not none -%}
        SRVREQCTRLRULE={{item.SRVREQCTRLRULE}},
    {%- endif -%}
    {%- if item.SRVREJCAUSE is not none -%}
        SRVREJCAUSE={{item.SRVREJCAUSE}},
    {%- endif -%}
    {%- if item.CPSRVREQTHRESH is not none -%}
        CPSRVREQTHRESH={{item.CPSRVREQTHRESH}},
    {%- endif -%}
    {%- if item.CPSRVREQMEPERIOD is not none -%}
        CPSRVREQMEPERIOD={{item.CPSRVREQMEPERIOD}},
    {%- endif -%}
    {%- if item.CPSRVREQDURATION is not none -%}
        CPSRVREQDURATION={{item.CPSRVREQDURATION}},
    {%- endif -%}
    {%- if item.CPSRVREQCTRLRULE is not none -%}
        CPSRVREQCTRLRULE={{item.CPSRVREQCTRLRULE}},
    {%- endif -%}
    {%- if item.CPSRVREJCAUSE is not none -%}
        CPSRVREJCAUSE={{item.CPSRVREJCAUSE}},
    {%- endif -%}
    {%- if item.PDNCONNTHRESH is not none -%}
        PDNCONNTHRESH={{item.PDNCONNTHRESH}},
    {%- endif -%}
    {%- if item.PDNCONNMEPERIOD is not none -%}
        PDNCONNMEPERIOD={{item.PDNCONNMEPERIOD}},
    {%- endif -%}
    {%- if item.PDNCONNDURATION is not none -%}
        PDNCONNDURATION={{item.PDNCONNDURATION}},
    {%- endif -%}
    {%- if item.PDNCONNCTRLRULE is not none -%}
        PDNCONNCTRLRULE={{item.PDNCONNCTRLRULE}},
    {%- endif -%}
    {%- if item.PDNCONNREJCAUSE is not none -%}
        PDNCONNREJCAUSE={{item.PDNCONNREJCAUSE}},
    {%- endif -%}
    {%- if item.BACKOFFSW is not none -%}
        BACKOFFSW={{item.BACKOFFSW}},
    {%- endif -%}
    {%- if item.PARKINGAPN is not none -%}
        PARKINGAPN="{{item.PARKINGAPN}}",
    {%- endif -%}
    {%- if item.DETACHCAUSE is not none -%}
        DETACHCAUSE={{item.DETACHCAUSE}},
    {%- endif -%}
    {%- if item.PARKAPNWAKEUPRULE is not none -%}
        PARKAPNWAKEUPRULE={{item.PARKAPNWAKEUPRULE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BACKOFFSW=ON 时可选 --- -#}
    {%- if item.BACKOFFSW == 'ON' -%}
        {%- if item.MINBOT is not none -%}
            MINBOT={{item.MINBOT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BACKOFFSW=ON 时可选 --- -#}
    {%- if item.BACKOFFSW == 'ON' -%}
        {%- if item.MAXBOT is not none -%}
            MAXBOT={{item.MAXBOT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 **可选：**通过软参BYTE\_EX\_B141 BIT8控制在移除信令抑制规则后，是否立即清除受对应规则抑制的用户的信令抑制状态。

```jinja2
{%- if is_optional_clear_suppression_state -%}
    {%- for item in set_softparaofbit_list -%}
        SET SOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

