---
id: ''
name: 激活系统过载控制功能（适用于SMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010801 系统过载控制功能","系统过载控制功能（适用于SMF）","激活系统过载控制功能（适用于SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。适用于SMF。

## 必备事项
前提条件

请仔细阅读WSFD-010801系统过载控制功能特性概述（适用于SMF）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: '设置整系统的流控功能禁用/启用状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    setapnaccesswal_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALNUMBER:
          name: '用户的接入速率'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_n4fixedfc_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - ERRIND
          - DLDATA
          - UPSDR
          - MULTIDNN
          required: true
          description: '设置N4接口上指定消息类型固定速率流控信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - OFF
          - ON
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
          description: '设置服务化接口上指定消息类型固定速率流控信息。'
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
    set_overloadctrl_list:
      type: items
      properties:
        CTRLENABLE:
          name: '信令抑制功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置信令抑制功能开关以及老化定时器时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AGINGTIME:
          name: '信令抑制记录的老化定时器时长(秒)'
          type: integer
          minimum: 30
          maximum: 180
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVTRIGCCRI:
          name: 'OCS CCR-I去活是否开启信令抑制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVTRIGACCT:
          name: 'ACCT去活是否开启信令抑制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcpfixedfc_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - HEARTBEATREQ
          - HEARTBEATRSP
          - ASSOCIATIONSETUPREQ
          - ASSOCIATIONSETUPRSP
          - ASSOCIATIONUPDATEREQ
          - ASSOCIATIONUPDATERSP
          - ASSOCIATIONRELEASEREQ
          - ASSOCIATIONRELEASERSP
          - NOTSUPPORTRSP
          - NODEREPORTREQ
          - NODEREPORTRSP
          required: true
          description: '设置N4接口上指定PFCP偶联消息类型固定速率流控信息。  说明：  此处仅以心跳请求消息举例，请根据实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 100000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_fcswitch_list:
    - SWITCH: ENABLE
    setapnaccesswal_list:
    - APN: 'huawei.com'
      WALNUMBER: 300
    set_n4fixedfc_list:
    - MSGTYPE: DLDATA
      FCSWITCH: ON
      THRESHOLD: 2000
    set_httpfixedfcmsg_list:
    - MSGTYPE: NSMF_PDUSESSION_SMCONTEXTSCREATE
      FCSWITCH: ON
      THRESHOLD: 4000
    set_overloadctrl_list:
    - CTRLENABLE: ENABLE
      AGINGTIME: 34
      SRVTRIGCCRI: ENABLE
      SRVTRIGACCT: ENABLE
    set_pfcpfixedfc_list:
    - MSGTYPE: HEARTBEATREQ
      FCSWITCH: ON
      THRESHOLD: 500
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置基于CPU过载流控开关。

```jinja2
{%- for item in set_fcswitch_list -%}
    SET FCSWITCH:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 设置APN下用户接入速率。

```jinja2
{%- for item in setapnaccesswal_list -%}
    SETAPNACCESSWAL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WALNUMBER is not none -%}
        WALNUMBER={{item.WALNUMBER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置N4接口指定消息类型固定流控速率。

```jinja2
{%- for item in set_n4fixedfc_list -%}
    SET N4FIXEDFC:
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

### 5 设置服务化接口上指定消息类型的固定速率。

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

### 6 设置信令抑制功能开关以及老化定时器时长。

```jinja2
{%- for item in set_overloadctrl_list -%}
    SET OVERLOADCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLENABLE is not none -%}
        CTRLENABLE={{item.CTRLENABLE}},
    {%- endif -%}
    {%- if item.SRVTRIGCCRI is not none -%}
        SRVTRIGCCRI={{item.SRVTRIGCCRI}},
    {%- endif -%}
    {%- if item.SRVTRIGACCT is not none -%}
        SRVTRIGACCT={{item.SRVTRIGACCT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLENABLE=ENABLE 时可选 --- -#}
    {%- if item.CTRLENABLE == 'ENABLE' -%}
        {%- if item.AGINGTIME is not none -%}
            AGINGTIME={{item.AGINGTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 设置N4接口上指定PFCP偶联消息类型固定速率流控信息。

```jinja2
{%- for item in set_pfcpfixedfc_list -%}
    SET PFCPFIXEDFC:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FCSWITCH=ON 时必选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        THRESHOLD={{item.THRESHOLD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

