---
id: GWFD-021401
name: 激活系统过载控制功能（适用于AMF）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。  在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021400 可靠性功能","GWFD-021401 系统过载控制功能","激活系统过载控制功能（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-021401系统过载控制功能特性概述（适用于AMF）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_amffcpara_list:
      type: items
      properties:
        FCACT:
          name: '流控措施'
          type: string
          enum:
          - DISCARD
          - REJECT
          required: false
          description: '设置自保流控的初始注册请求消息流控策略。AMF回复注册拒绝消息，并携带Backoff timer信元，用于指示请求消息重复尝试的延迟时长。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BOTSW:
          name: 'Backoff Timer信元开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINBOT:
          name: 'Backoff timer最小值(秒)'
          type: integer
          minimum: 1
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXBOT:
          name: 'Backoff timer最大值(秒)'
          type: integer
          minimum: 1
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_n2overload_list:
      type: items
      properties:
        SWITCH:
          name: 'Overload功能开关'
          type: string
          enum:
          - On
          - Off
          required: true
          description: '设置自保流控的N2接口消息流控策略。AMF过载时给gNodeB发Overload Start消息，并携带拒绝比例指示。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OVERLDACTION:
          name: '过载行为'
          type: string
          enum:
          - None
          - RejectNonEmergencyMoDt
          - RejectAllSignallingEstablishMent
          - PermitEmergencyAndMt
          - PermitHighPriorityAndMt
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REJRATEIND:
          name: '拒绝比例指示'
          type: string
          enum:
          - No
          - Yes
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_fcparam_list:
      type: items
      properties:
        SERVICETYPE:
          name: '服务类型'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICEID:
          name: '实例组ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CASEID:
          name: '流控套餐ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARAMCAT:
          name: '参数类别'
          type: string
          enum:
          - GENERAL
          - WEIGHTS
          - THRESHOLD
          - TARGETCPU
          - OVERLOADLEVEL
          - STOPALGO
          - BPBACKEND
          - BPFRONTEND
          - WALPARAMETER
          - GCCPUCONFIG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTOKEN:
          name: '最小令牌数'
          type: integer
          minimum:
          - 10
          - 4294967295
          maximum:
          - 50000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXTOKEN:
          name: '最大令牌数'
          type: integer
          minimum:
          - 10
          - 4294967295
          maximum:
          - 50000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fcswitch_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '开启整系统的流控功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_interamffc_list:
      type: items
      properties:
        FCSWITCH:
          name: 'Inter-AMF接入流控功能开关'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '开启Inter-AMF用户接入流控功能，设置流控阈值作用范围为整系统。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REGSCOPE:
          name: 'Registration Request流控阈值作用范围'
          type: string
          enum:
          - POD
          - SYSTEM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGTHD:
          name: 'Registration Request速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 640000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRSCOPE:
          name: 'Service Request流控阈值作用范围'
          type: string
          enum:
          - POD
          - SYSTEM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRTHD:
          name: 'Service Request速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 640000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTALMTIMES:
          name: '告警上报周期数'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_httpfixedfcmsg_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - NSMF_PDUSESSION_SMCONTEXTSCREATE
          - NSMF_PDUSESSION_RETRIEVESMCONTEXT
          - NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY
          - NAMF_COMMUNICATION_UECONTEXTTRANSFER
          - NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION
          - NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION
          - NNSSF_NSSELECTION_NSSELECTIONGET
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST
          - NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION
          - NSMSF_SMSERVICESERVICEAPI_SENDSMS
          - NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE
          - NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE
          - NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE
          - NUPF_EVENTEXPOSURE_NOTIFY
          - NSMF_EVENTEXPOSURE_NOTIFY
          - NAMF_EVENTEXPOSURE_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_SUBSCRIBER
          - NUDN_RAILWAYSAMPLEDATARECORDR
          required: true
          description: '设置服务化接口指定消息类型的固定速率流控功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfnasfixedfc_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - PDUSESSIONEST
          required: true
          description: '开启PDU会话建立请求消息的固定速率流控功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCOPE:
          name: '流控阈值作用范围'
          type: string
          enum:
          - SYSTEM
          - POD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_n2fixedfcbymsg_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - NGSETUP
          - PAGING
          - REGISTER
          - SERVICEREQUEST
          - PATHSWITCH
          - WPWR
          - PCR
          - PRI
          - PFI
          required: true
          description: '开启N2接口Paging消息的固定速率流控功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - On
          - Off
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpagingarppri_list:
      type: items
      properties:
        ARP:
          name: 'ARP数值'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: '配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          enum:
          - PAGING_LOW
          - PAGING_HIGH
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpagingdnnpri_list:
      type: items
      properties:
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          enum:
          - PAGING_LOW
          - PAGING_HIGH
          required: true
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
          description: '（可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。'
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
    set_amfsoftpara_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '（可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明：  此处阈值为举例值，请根据网络具体情况进行阈值设置。'
          data_source: ''
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
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_n2pagingfcplcy_list:
      type: items
      properties:
        SWITCH:
          name: 'N2模式寻呼反压流控功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: '开启N2模式寻呼反压流控功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRECISEPAGINGSW:
          name: '精准寻呼控制开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_paecheckpara_list:
      type: items
      properties:
        CHECKINTERVAL:
          name: '检测间隔(s)'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKTIMES:
          name: '检测次数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_paecheckthd_list:
      type: items
      properties:
        RESTYPE:
          name: '资源类型'
          type: string
          enum:
          - PBUF
          - SHAREQUEUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGTHD:
          name: '触发过载阈值（%）'
          type: integer
          minimum: 2
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUMTHD:
          name: '触发过载恢复阈值（%）'
          type: integer
          minimum: 2
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_reversefcpara_list:
      type: items
      properties:
        CTRLPLCY:
          name: '控制策略 '
          type: string
          enum:
          - INSTANCENUM
          - PERCENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERCENTTRGTHD:
          name: '过载阈值（%）'
          type: integer
          minimum: 1
          maximum: 99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERCENTRESUMTHD:
          name: '恢复阈值（%）'
          type: integer
          minimum: 0
          maximum: 99
          required: false
          description: ''
          data_source: ''
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
          description: '配置开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。'
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
    set_amffcpara_list:
    - FCACT: REJECT
      BOTSW: ON
      MINBOT: 900
      MAXBOT: 1800
    set_n2overload_list:
    - SWITCH: On
      OVERLDACTION: RejectAllSignallingEstablishMent
      REJRATEIND: Yes
    add_fcparam_list:
    - SERVICETYPE: 'UeamExecSvc'
      SERVICEID: 999
      CASEID: 0
      PARAMCAT: GENERAL
      MINTOKEN: 30
      MAXTOKEN: 5000
    set_fcswitch_list:
    - SWITCH: ENABLE
    set_interamffc_list:
    - FCSWITCH: ON
      REGSCOPE: SYSTEM
      REGTHD: 1000
      SRSCOPE: SYSTEM
      SRTHD: 2000
      STARTALMTIMES: 3
    set_httpfixedfcmsg_list:
    - MSGTYPE: NAMF_COMMUNICATION_UECONTEXTTRANSFER
      FCSWITCH: ON
      THRESHOLD: 4000
    set_amfnasfixedfc_list:
    - MSGTYPE: PDUSESSIONEST
      FCSWITCH: On
      THRESHOLD: 1000
      SCOPE: POD
    set_n2fixedfcbymsg_list:
    - MSGTYPE: PAGING
      FCSWITCH: On
      THRESHOLD: 2000
    add_ngpagingarppri_list:
    - ARP: 1
      PRIORITY: PAGING_HIGH
    add_ngpagingdnnpri_list:
    - DNN: 'IMS'
      PRIORITY: PAGING_HIGH
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 14
      VALUE: VALUE_0
      POSITION: 30
    set_amfsoftpara_list:
    - DT: Dw
      DWORDNUM: 28
      DWORDVALUE: 80000
    set_n2pagingfcplcy_list:
    - SWITCH: ON
      PRECISEPAGINGSW: ON
    set_paecheckpara_list:
    - CHECKINTERVAL: 1
      CHECKTIMES: 5
    set_paecheckthd_list:
    - RESTYPE: PBUF
      TRIGTHD: 60
      RESUMTHD: 30
    set_reversefcpara_list:
    - CTRLPLCY: PERCENT
      PERCENTTRGTHD: 50
      PERCENTRESUMTHD: 5
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 323
      VALUE: VALUE_1
      POSITION: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 开启自保流控功能。

#### 2.1 设置初始注册请求消息流控策略。

```jinja2
{%- for item in set_amffcpara_list -%}
    SET AMFFCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FCACT is not none -%}
        FCACT={{item.FCACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BOTSW=ON 时可选 --- -#}
    {%- if item.BOTSW == 'ON' -%}
        {%- if item.MINBOT is not none -%}
            MINBOT={{item.MINBOT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BOTSW=ON 时可选 --- -#}
    {%- if item.BOTSW == 'ON' -%}
        {%- if item.MAXBOT is not none -%}
            MAXBOT={{item.MAXBOT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCACT=REJECT 时可选 --- -#}
    {%- if item.FCACT == 'REJECT' -%}
        {%- if item.BOTSW is not none -%}
            BOTSW={{item.BOTSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 设置N2接口消息流控策略。

```jinja2
{%- for item in set_n2overload_list -%}
    SET N2OVERLOAD:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=On 时可选 --- -#}
    {%- if item.SWITCH == 'On' -%}
        {%- if item.OVERLDACTION is not none -%}
            OVERLDACTION={{item.OVERLDACTION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=On 时可选 --- -#}
    {%- if item.SWITCH == 'On' -%}
        {%- if item.REJRATEIND is not none -%}
            REJRATEIND={{item.REJRATEIND}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 增加具体微服务实例的流控参数。

```jinja2
{%- for item in add_fcparam_list -%}
    ADD FCPARAM:
    {#- --- 必选参数 --- -#}
    SERVICETYPE="{{item.SERVICETYPE}}",
    SERVICEID={{item.SERVICEID}},
    CASEID={{item.CASEID}},
    PARAMCAT={{item.PARAMCAT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PARAMCAT=GENERAL 时可选 --- -#}
    {%- if item.PARAMCAT == 'GENERAL' -%}
        {%- if item.MINTOKEN is not none -%}
            MINTOKEN={{item.MINTOKEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GENERAL 时可选 --- -#}
    {%- if item.PARAMCAT == 'GENERAL' -%}
        {%- if item.MAXTOKEN is not none -%}
            MAXTOKEN={{item.MAXTOKEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 开启整系统流控功能开关。

```jinja2
{%- for item in set_fcswitch_list -%}
    SET FCSWITCH:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置Inter-AMF用户接入流控功能的相关参数。

```jinja2
{%- for item in set_interamffc_list -%}
    SET INTERAMFFC:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {%- if item.REGSCOPE is not none -%}
        REGSCOPE={{item.REGSCOPE}},
    {%- endif -%}
    {%- if item.REGTHD is not none -%}
        REGTHD={{item.REGTHD}},
    {%- endif -%}
    {%- if item.SRSCOPE is not none -%}
        SRSCOPE={{item.SRSCOPE}},
    {%- endif -%}
    {%- if item.SRTHD is not none -%}
        SRTHD={{item.SRTHD}},
    {%- endif -%}
    {%- if item.STARTALMTIMES is not none -%}
        STARTALMTIMES={{item.STARTALMTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 开启服务化接口指定消息类型的固定速率流控功能。

```jinja2
{%- for item in set_httpfixedfcmsg_list -%}
    SET HTTPFIXEDFCMSG:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 开启PDU会话建立请求消息的固定速率流控功能。

```jinja2
{%- for item in set_amfnasfixedfc_list -%}
    SET AMFNASFIXEDFC:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.SCOPE is not none -%}
            SCOPE={{item.SCOPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 开启N2接口Paging消息固定速率流控功能。

#### 6.1 设置流控消息类型和门限，开启流控功能开关。

```jinja2
{%- for item in set_n2fixedfcbymsg_list -%}
    SET N2FIXEDFCBYMSG:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=On 时可选 --- -#}
    {%- if item.FCSWITCH == 'On' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置基于ARP识别Paging消息在N2口固定速率流控期间放通的优先级。

```jinja2
{%- for item in add_ngpagingarppri_list -%}
    ADD NGPAGINGARPPRI:
    {#- --- 必选参数 --- -#}
    ARP={{item.ARP}},
    PRIORITY={{item.PRIORITY}},
    ;
{%- endfor -%}
```

#### 6.3 配置基于DNN识别Paging消息在N2口固定速率流控期间放通的优先级。

```jinja2
{%- for item in add_ngpagingdnnpri_list -%}
    ADD NGPAGINGDNNPRI:
    {#- --- 必选参数 --- -#}
    DNN="{{item.DNN}}",
    PRIORITY={{item.PRIORITY}},
    ;
{%- endfor -%}
```

#### 6.4 * **可选：**设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

```jinja2
{%- if is_optional_enable_ta_paging_flow_control -%}
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

#### 6.5 * **可选：**通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

```jinja2
{%- if is_optional_set_ta_paging_flow_control_threshold -%}
    {%- for item in set_amfsoftpara_list -%}
        SET AMFSOFTPARA:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 开启N2模式寻呼反压流控功能。

#### 7.1 开启流控功能开关。

```jinja2
{%- for item in set_n2pagingfcplcy_list -%}
    SET N2PAGINGFCPLCY:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PRECISEPAGINGSW is not none -%}
            PRECISEPAGINGSW={{item.PRECISEPAGINGSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 设置流控相关参数

```jinja2
{%- for item in set_paecheckpara_list -%}
    SET PAECHECKPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CHECKINTERVAL is not none -%}
        CHECKINTERVAL={{item.CHECKINTERVAL}},
    {%- endif -%}
    {%- if item.CHECKTIMES is not none -%}
        CHECKTIMES={{item.CHECKTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_paecheckthd_list -%}
    SET PAECHECKTHD:
    {#- --- 必选参数 --- -#}
    RESTYPE={{item.RESTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TRIGTHD is not none -%}
        TRIGTHD={{item.TRIGTHD}},
    {%- endif -%}
    {%- if item.RESUMTHD is not none -%}
        RESUMTHD={{item.RESUMTHD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_reversefcpara_list -%}
    SET REVERSEFCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLPLCY is not none -%}
        CTRLPLCY={{item.CTRLPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLPLCY=PERCENT 时可选 --- -#}
    {%- if item.CTRLPLCY == 'PERCENT' -%}
        {%- if item.PERCENTTRGTHD is not none -%}
            PERCENTTRGTHD={{item.PERCENTTRGTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLPLCY=PERCENT 时可选 --- -#}
    {%- if item.CTRLPLCY == 'PERCENT' -%}
        {%- if item.PERCENTRESUMTHD is not none -%}
            PERCENTRESUMTHD={{item.PERCENTRESUMTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置是否开启下行寻呼固定速率流控，并设置流控阈值和告警上报条件。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

