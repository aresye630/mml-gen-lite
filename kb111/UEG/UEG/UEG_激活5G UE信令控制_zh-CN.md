---
id: GWFD-020908
name: 激活5G UE信令控制
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活5G UE信令控制功能的操作过程。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-020900 接入管理","GWFD-020908 5G UE信令控制","激活5G UE信令控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活5G UE信令控制功能的操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020908 5G UE信令控制特性概述。
* 如果采用Parking DNN激活的抑制规则，需要SMF对Parking DNN配置不进行数据业务和不生成话单，并增加Parking切片为支持的切片；需要AMF增加Parking DNN的DNS解析配置，或增加DNS服务器的配置。
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
    set_ngsmartpara_list:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGSW:
          name: '初始注册信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQSW:
          name: '服务请求信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUREQSW:
          name: 'PDU会话建立信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngsmartpara_list_1:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGTHRESH:
          name: '初始注册异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: '配置异常识别参数，包括异常识别门限、异常测量周期。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGMEPERIOD:
          name: '初始注册异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQTHRESH:
          name: '服务请求异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQPERIOD:
          name: '服务请求异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUREQTHRESH:
          name: 'PDU会话建立异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUREQPERIOD:
          name: 'PDU会话建立异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngsmartpara_list_2:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGDURATION:
          name: '初始注册异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: '配置抑制时长。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGCTRLRULE:
          name: '注册抑制措施'
          type: string
          required: false
          description: '配置信令抑制措施“特殊原因值拒绝 ”。  本命令中各种场景的拒绝原因值如果设置不当，可能会导致终端后续不再接入。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGREJCAUSE:
          name: '注册拒绝原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQCTRLRULE:
          name: '服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREJCAUSE:
          name: '服务请求拒绝原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUREQCTRLRULE:
          name: 'PDU会话建立抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUREQREJCAUSE:
          name: 'PDU会话建立原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEREGISTCAUSE:
          name: '去注册原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVREQDURATION:
          name: '服务请求异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDUREQDURATION:
          name: 'PDU会话建立异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngsmartpara_list_4:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PARKINGDNN:
          name: 'Parking DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARKDNNWAKEUP:
          name: 'Parking DNN唤醒措施'
          type: string
          enum:
          - CNDEACT
          - CNDEREG
          required: false
          description: '配置信令抑制措施“Parking DNN激活”的唤醒措施。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PARKINGSST:
          name: 'Parking切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PARKINGSD:
          name: 'Parking切片细分标识'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngsmartpara_list_5:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PARKINGDNN:
          name: 'Parking DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARKDNNWAKEUP:
          name: 'Parking DNN唤醒措施'
          type: string
          enum:
          - CNDEACT
          - CNDEREG
          required: false
          description: '配置信令抑制措施“Parking DNN激活”的唤醒措施。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngsmartpara_list_6:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LTETONRINITREGSW:
          name: '4G到5G初始注册信令抑制开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置4G到5G初始注册以及无N26接口场景的4G到5G的重选和初始注册流程信令抑制开关。  说明：  4G到5G初始注册以及无N26接口场景的4G到5G的重选和初始注册流程信令抑制功能的异常识别门限、异常测量周期、抑制时长以及抑制措施使用始注册流程配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngsmartpara_list_7:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LTETONRRSLSW:
          name: '4G到5G重选信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '配置4G到5G重选流程的异常信令抑制功能相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LTETONRRSLTHRESH:
          name: '4G到5G重选异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRRSLMEPERIOD:
          name: '4G到5G重选异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRRSLDURATION:
          name: '4G到5G重选异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRREGCTRLRULE:
          name: '4G到5G重选抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRRSLREJCAUSE:
          name: '4G到5G重选拒绝原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngsmartpara_list_8:
      type: items
      properties:
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启用户异常信令抑制功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LTETONRHOSW:
          name: '4G到5G切换信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '配置4G到5G切换流程的异常信令抑制功能相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LTETONRHOTHRESH:
          name: '4G到5G切换异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRHOMEPERIOD:
          name: '4G到5G切换异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRHODURATION:
          name: '4G到5G切换异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRHOCTRLRULE:
          name: '4G到5G切换抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTETONRHOREJCAUSE:
          name: '4G到5G切换拒绝原因值'
          type: integer
          minimum: 64
          maximum: 239
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngsmartpara_list_9:
      type: items
      properties:
        SESSIONSRSW:
          name: '基于会话粒度的服务请求信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '配置基于会话粒度的服务请求异常信令抑制功能相关参数。  说明：  “基于会话粒度的服务请求异常测量周期(秒)”与“服务请求异常测量周期(秒)”相同时，“基于会话粒度的服务请求异常识别门限(次)”值应小于“服务请求异常识别门限(次)”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SESSIONSRTHR:
          name: '基于会话粒度的服务请求异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONSRPERIOD:
          name: '基于会话粒度的服务请求异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONSRDURAT:
          name: '基于会话粒度的服务请求异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONSRCTRRUL:
          name: '基于会话粒度的服务请求抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONSRREJCS:
          name: '基于会话粒度的服务请求拒绝原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngsmartpara_list_10:
      type: items
      properties:
        SESSIONPDUSW:
          name: '基于会话粒度的PDU会话建立信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '配置基于会话粒度的PDU会话建立请求异常信令抑制功能相关参数。  说明：  “基于会话粒度的PDU会话建立异常测量周期(秒)”与“PDU会话建立异常测量周期(秒)”相同时，“基于会话粒度的PDU会话建立异常识别门限(次)”值应小于“PDU会话建立异常识别门限(次)”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SESSIONPDUTHR:
          name: '基于会话粒度的PDU会话建立异常识别门限(次)'
          type: integer
          minimum: 2
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONPDUPER:
          name: '基于会话粒度的PDU会话建立异常测量周期(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONPDUDUR:
          name: '基于会话粒度的PDU会话建立异常抑制时长(分钟)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONPDUCTRUL:
          name: '基于会话粒度的PDU会话建立抑制措施'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONPDUREJCA:
          name: '基于会话粒度的PDU会话建立原因值'
          type: integer
          minimum: 1
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSDNNWAKEUP:
          name: '基于会话粒度的Parking DNN唤醒措施'
          type: string
          enum:
          - CNDEACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLSW:
          name: '信令抑制开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '（可选）配置AMF对于Paging触发的Service Request流程是否进行信令抑制判断。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
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
    set_amfsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '（可选）配置PDU会话建立流程信令抑制功能去使能后是否执行 Parking DNN 唤醒措施。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
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
    - LICITEM: 'LKV2SAUSC01'
      SWITCH: ENABLE
    set_ngsmartpara_list:
    - CTRLSW: ON
      REGSW: ON
      SRVREQSW: ON
      PDUREQSW: ON
    set_ngsmartpara_list_1:
    - CTRLSW: ON
      REGTHRESH: 30
      REGMEPERIOD: 3600
      SRVREQTHRESH: 30
      SRVREQPERIOD: 3600
      PDUREQTHRESH: 30
      PDUREQPERIOD: 3600
    set_ngsmartpara_list_2:
    - CTRLSW: ON
      REGDURATION: 60
      REGCTRLRULE: SPECCAUSEREJ&CNDEREG-1&DISCARD-1
      REGREJCAUSE: 15
      SRVREQCTRLRULE: SPECCAUSEREJ-1&CNDEREG-1&DISCARD-1
      SRVREJCAUSE: 15
      PDUREQCTRLRULE: SPECCAUSEREJ-1&PARKDNNACT-1&CNDEREG-1&DISCARD-1
      PDUREQREJCAUSE: 65
      DEREGISTCAUSE: 15
      SRVREQDURATION: 60
      PDUREQDURATION: 60
    set_ngsmartpara_list_4:
    - CTRLSW: ON
      PARKINGDNN: 'PARKING'
      PARKDNNWAKEUP: CNDEACT
      PARKINGSST: 1
      PARKINGSD: “000001”
    set_ngsmartpara_list_5:
    - CTRLSW: ON
      PARKINGDNN: 'PARKING'
      PARKDNNWAKEUP: CNDEACT
    set_ngsmartpara_list_6:
    - CTRLSW: ON
      LTETONRINITREGSW: ON
    set_ngsmartpara_list_7:
    - CTRLSW: ON
      LTETONRRSLSW: ON
      LTETONRRSLTHRESH: 50
      LTETONRRSLMEPERIOD: 3600
      LTETONRRSLDURATION: 60
      LTETONRREGCTRLRULE: SPECCAUSEREJ-1
      LTETONRRSLREJCAUSE: 15
    set_ngsmartpara_list_8:
    - CTRLSW: ON
      LTETONRHOSW: ON
      LTETONRHOTHRESH: 50
      LTETONRHOMEPERIOD: 3600
      LTETONRHODURATION: 60
      LTETONRHOCTRLRULE: SPECCAUSEREJ-1
      LTETONRHOREJCAUSE: 81
    set_ngsmartpara_list_9:
    - SESSIONSRSW: ON
      SESSIONSRTHR: 80
      SESSIONSRPERIOD: 3600
      SESSIONSRDURAT: 60
      SESSIONSRCTRRUL: SPECCAUSEREJ-1&DISCARD-1
      SESSIONSRREJCS: 15
      CTRLSW: ''
    set_ngsmartpara_list_10:
    - SESSIONPDUSW: ON
      SESSIONPDUTHR: 30
      SESSIONPDUPER: 3600
      SESSIONPDUDUR: 60
      SESSIONPDUCTRUL: SPECCAUSEREJ-1&PARKDNNACT-1&DISCARD-1
      SESSIONPDUREJCA: 65
      SESSDNNWAKEUP: CNDEACT
      CTRLSW: ''
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 72
      VALUE: VALUE_0
      POSITION: 3
    set_amfsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: 80
      VALUE: VALUE_1
      POSITION: 21
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

### 3 **可选：**开启用户异常信令抑制功能。

```jinja2
{%- if is_optional_user_abnormal_signaling_suppression -%}
    {%- for item in set_ngsmartpara_list -%}
        SET NGSMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CTRLSW is not none -%}
            CTRLSW={{item.CTRLSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGSW is not none -%}
                REGSW={{item.REGSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREQSW is not none -%}
                SRVREQSW={{item.SRVREQSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQSW is not none -%}
                PDUREQSW={{item.PDUREQSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置异常信令识别门限和测量周期。

```jinja2
{%- if is_optional_abnormal_signaling_threshold_period -%}
    {%- for item in set_ngsmartpara_list_1 -%}
        SET NGSMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CTRLSW is not none -%}
            CTRLSW={{item.CTRLSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGTHRESH is not none -%}
                REGTHRESH={{item.REGTHRESH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGMEPERIOD is not none -%}
                REGMEPERIOD={{item.REGMEPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREQTHRESH is not none -%}
                SRVREQTHRESH={{item.SRVREQTHRESH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREQPERIOD is not none -%}
                SRVREQPERIOD={{item.SRVREQPERIOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQTHRESH is not none -%}
                PDUREQTHRESH={{item.PDUREQTHRESH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQPERIOD is not none -%}
                PDUREQPERIOD={{item.PDUREQPERIOD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**设置异常信令抑制规则和抑制时长。

```jinja2
{%- if is_optional_abnormal_signaling_suppression_rule -%}
    {%- for item in set_ngsmartpara_list_2 -%}
        SET NGSMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CTRLSW is not none -%}
            CTRLSW={{item.CTRLSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGDURATION is not none -%}
                REGDURATION={{item.REGDURATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGCTRLRULE is not none -%}
                REGCTRLRULE={{item.REGCTRLRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.REGREJCAUSE is not none -%}
                REGREJCAUSE={{item.REGREJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREQCTRLRULE is not none -%}
                SRVREQCTRLRULE={{item.SRVREQCTRLRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREJCAUSE is not none -%}
                SRVREJCAUSE={{item.SRVREJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQCTRLRULE is not none -%}
                PDUREQCTRLRULE={{item.PDUREQCTRLRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQREJCAUSE is not none -%}
                PDUREQREJCAUSE={{item.PDUREQREJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.DEREGISTCAUSE is not none -%}
                DEREGISTCAUSE={{item.DEREGISTCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PDUREQDURATION is not none -%}
                PDUREQDURATION={{item.PDUREQDURATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.SRVREQDURATION is not none -%}
                SRVREQDURATION={{item.SRVREQDURATION}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 设置Parking DNN、Parking SST、Parking SD值。

```jinja2
{%- for item in set_ngsmartpara_list_4 -%}
    SET NGSMARTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLSW is not none -%}
        CTRLSW={{item.CTRLSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.PARKINGDNN is not none -%}
            PARKINGDNN="{{item.PARKINGDNN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.PARKDNNWAKEUP is not none -%}
            PARKDNNWAKEUP={{item.PARKDNNWAKEUP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.PARKINGSST is not none -%}
            PARKINGSST={{item.PARKINGSST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.PARKINGSD is not none -%}
            PARKINGSD="{{item.PARKINGSD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **可选：**配置抑制唤醒参数。

```jinja2
{%- if is_optional_suppression_wakeup_parameter -%}
    {%- for item in set_ngsmartpara_list_5 -%}
        SET NGSMARTPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.CTRLSW is not none -%}
            CTRLSW={{item.CTRLSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PARKINGDNN is not none -%}
                PARKINGDNN="{{item.PARKINGDNN}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
        {%- if item.CTRLSW == 'ON' -%}
            {%- if item.PARKDNNWAKEUP is not none -%}
                PARKDNNWAKEUP={{item.PARKDNNWAKEUP}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置4G到5G初始注册流程异常信令抑制开关。

```jinja2
{%- for item in set_ngsmartpara_list_6 -%}
    SET NGSMARTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLSW is not none -%}
        CTRLSW={{item.CTRLSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.LTETONRINITREGSW is not none -%}
            LTETONRINITREGSW={{item.LTETONRINITREGSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置4G到5G重选流程的异常信令抑制功能相关参数。

```jinja2
{%- for item in set_ngsmartpara_list_7 -%}
    SET NGSMARTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLSW is not none -%}
        CTRLSW={{item.CTRLSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.LTETONRRSLSW is not none -%}
            LTETONRRSLSW={{item.LTETONRRSLSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRRSLSW=ON 时可选 --- -#}
    {%- if item.LTETONRRSLSW == 'ON' -%}
        {%- if item.LTETONRRSLTHRESH is not none -%}
            LTETONRRSLTHRESH={{item.LTETONRRSLTHRESH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRRSLSW=ON 时可选 --- -#}
    {%- if item.LTETONRRSLSW == 'ON' -%}
        {%- if item.LTETONRRSLMEPERIOD is not none -%}
            LTETONRRSLMEPERIOD={{item.LTETONRRSLMEPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRRSLSW=ON 时可选 --- -#}
    {%- if item.LTETONRRSLSW == 'ON' -%}
        {%- if item.LTETONRRSLDURATION is not none -%}
            LTETONRRSLDURATION={{item.LTETONRRSLDURATION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRRSLSW=ON 时可选 --- -#}
    {%- if item.LTETONRRSLSW == 'ON' -%}
        {%- if item.LTETONRREGCTRLRULE is not none -%}
            LTETONRREGCTRLRULE={{item.LTETONRREGCTRLRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRRSLSW=ON 时可选 --- -#}
    {%- if item.LTETONRRSLSW == 'ON' -%}
        {%- if item.LTETONRRSLREJCAUSE is not none -%}
            LTETONRRSLREJCAUSE={{item.LTETONRRSLREJCAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 配置4G到5G切换流程的异常信令抑制功能相关参数。

```jinja2
{%- for item in set_ngsmartpara_list_8 -%}
    SET NGSMARTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLSW is not none -%}
        CTRLSW={{item.CTRLSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.LTETONRHOSW is not none -%}
            LTETONRHOSW={{item.LTETONRHOSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRHOSW=ON 时可选 --- -#}
    {%- if item.LTETONRHOSW == 'ON' -%}
        {%- if item.LTETONRHOTHRESH is not none -%}
            LTETONRHOTHRESH={{item.LTETONRHOTHRESH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRHOSW=ON 时可选 --- -#}
    {%- if item.LTETONRHOSW == 'ON' -%}
        {%- if item.LTETONRHOMEPERIOD is not none -%}
            LTETONRHOMEPERIOD={{item.LTETONRHOMEPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRHOSW=ON 时可选 --- -#}
    {%- if item.LTETONRHOSW == 'ON' -%}
        {%- if item.LTETONRHODURATION is not none -%}
            LTETONRHODURATION={{item.LTETONRHODURATION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRHOSW=ON 时可选 --- -#}
    {%- if item.LTETONRHOSW == 'ON' -%}
        {%- if item.LTETONRHOCTRLRULE is not none -%}
            LTETONRHOCTRLRULE={{item.LTETONRHOCTRLRULE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LTETONRHOSW=ON 时可选 --- -#}
    {%- if item.LTETONRHOSW == 'ON' -%}
        {%- if item.LTETONRHOREJCAUSE is not none -%}
            LTETONRHOREJCAUSE={{item.LTETONRHOREJCAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 配置基于会话粒度的服务请求异常信令抑制功能相关参数。

```jinja2
{%- for item in set_ngsmartpara_list_9 -%}
    SET NGSMARTPARA:
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.SESSIONSRSW is not none -%}
            SESSIONSRSW={{item.SESSIONSRSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONSRSW=ON 时可选 --- -#}
    {%- if item.SESSIONSRSW == 'ON' -%}
        {%- if item.SESSIONSRTHR is not none -%}
            SESSIONSRTHR={{item.SESSIONSRTHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONSRSW=ON 时可选 --- -#}
    {%- if item.SESSIONSRSW == 'ON' -%}
        {%- if item.SESSIONSRPERIOD is not none -%}
            SESSIONSRPERIOD={{item.SESSIONSRPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONSRSW=ON 时可选 --- -#}
    {%- if item.SESSIONSRSW == 'ON' -%}
        {%- if item.SESSIONSRDURAT is not none -%}
            SESSIONSRDURAT={{item.SESSIONSRDURAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONSRSW=ON 时可选 --- -#}
    {%- if item.SESSIONSRSW == 'ON' -%}
        {%- if item.SESSIONSRCTRRUL is not none -%}
            SESSIONSRCTRRUL={{item.SESSIONSRCTRRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONSRSW=ON 时可选 --- -#}
    {%- if item.SESSIONSRSW == 'ON' -%}
        {%- if item.SESSIONSRREJCS is not none -%}
            SESSIONSRREJCS={{item.SESSIONSRREJCS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 配置基于会话粒度的PDU会话建立请求异常信令抑制功能相关参数。

```jinja2
{%- for item in set_ngsmartpara_list_10 -%}
    SET NGSMARTPARA:
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLSW=ON 时可选 --- -#}
    {%- if item.CTRLSW == 'ON' -%}
        {%- if item.SESSIONPDUSW is not none -%}
            SESSIONPDUSW={{item.SESSIONPDUSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSIONPDUTHR is not none -%}
            SESSIONPDUTHR={{item.SESSIONPDUTHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSIONPDUPER is not none -%}
            SESSIONPDUPER={{item.SESSIONPDUPER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSIONPDUDUR is not none -%}
            SESSIONPDUDUR={{item.SESSIONPDUDUR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSIONPDUCTRUL is not none -%}
            SESSIONPDUCTRUL={{item.SESSIONPDUCTRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSIONPDUREJCA is not none -%}
            SESSIONPDUREJCA={{item.SESSIONPDUREJCA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SESSIONPDUSW=ON 时可选 --- -#}
    {%- if item.SESSIONPDUSW == 'ON' -%}
        {%- if item.SESSDNNWAKEUP is not none -%}
            SESSDNNWAKEUP={{item.SESSDNNWAKEUP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 **可选：**配置AMF对于Paging触发的Service Request流程是否进行信令抑制判断。

```jinja2
{%- if is_optional_amf_paging_service_request_suppression -%}
    {%- for item in set_amfsoftparaofbit_list -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 14 配置PDU会话建立流程信令抑制功能去使能后是否执行 Parking DNN 唤醒措施。

```jinja2
{%- for item in set_amfsoftparaofbit_list_1 -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

