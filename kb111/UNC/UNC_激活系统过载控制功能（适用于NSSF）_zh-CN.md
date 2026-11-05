---
id: ''
name: 激活系统过载控制功能（适用于NSSF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。  适用于NSSF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010801 系统过载控制功能","系统过载控制功能（适用于NSSF）","激活系统过载控制功能（适用于NSSF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。适用于NSSF。

## 必备事项
前提条件

请仔细阅读WSFD-010801系统过载控制功能特性概述（适用于NSSF）。
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
          description: '设置基于CPU过载的流控开关。'
          data_source: '本端规划'
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
  examples:
    set_fcswitch_list:
    - SWITCH: ENABLE
    set_httpfixedfcmsg_list:
    - MSGTYPE: NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST
      FCSWITCH: ON
      THRESHOLD: 4000
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

### 3 设置服务化接口上指定消息类型的固定速率。

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

