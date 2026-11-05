---
id: ''
name: 激活Nnrf接口流控功能
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活Nnrf接口流控功能的操作过程。  适用于NRF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010802 周边网元过载保护","Nnrf接口流控功能","激活Nnrf接口流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Nnrf接口流控功能的操作过程。适用于NRF。

## 必备事项
前提条件

请仔细阅读WSFD-010802 周边网元过载保护特性概述（Nnrf接口流控功能特性概述）。
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrfnotifyfcpara_list:
      type: items
      properties:
        FCSWITCH:
          name: 'NFPROFILE变更事件流控开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '设置NRF每秒处理NFPROFILE变更事件的流控功能信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FCTHD:
          name: '每秒处理NFPROFILE变更事件的数量'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RSDFCSWITCH:
          name: '失败通知重传流控开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_notifyrsdpara_list:
      type: items
      properties:
        NOTIFYRSDSW:
          name: '失败通知重传开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '配置NRF不重新发送那些发送失败的通知消息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfnotifyfcpara_list_1:
      type: items
      properties:
        NFCHGCACHETHD:
          name: 'NF更新事件缓冲最长时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: '设置NRF针对同一频繁变更的NF的多长时间内的变更事件合并。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFCHGCACHETIME:
          name: 'NF更新事件最短缓冲时长(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: '设置多长时间内同一个NF超过1次变更就识别此NF为频繁变更，需要对其变更通知做抑制合并。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_fcswitch_list:
    - SWITCH: ENABLE
    set_nrfnotifyfcpara_list:
    - FCSWITCH: FUNC_ON
      FCTHD: 200
      RSDFCSWITCH: FUNC_OFF
    set_notifyrsdpara_list:
    - NOTIFYRSDSW: FUNC_OFF
    set_nrfnotifyfcpara_list_1:
    - NFCHGCACHETHD: 900
      NFCHGCACHETIME: 50
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置NRF每秒处理NFPROFILE变更事件的流控功能。

```jinja2
{%- for item in set_fcswitch_list -%}
    SET FCSWITCH:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nrfnotifyfcpara_list -%}
    SET NRFNOTIFYFCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {%- if item.FCTHD is not none -%}
        FCTHD={{item.FCTHD}},
    {%- endif -%}
    {%- if item.RSDFCSWITCH is not none -%}
        RSDFCSWITCH={{item.RSDFCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置NRF状态通知失败时重传的参数。

```jinja2
{%- for item in set_notifyrsdpara_list -%}
    SET NOTIFYRSDPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.NOTIFYRSDSW is not none -%}
        NOTIFYRSDSW={{item.NOTIFYRSDSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置NRF平滑通知参数，合并变更通知。

```jinja2
{%- for item in set_nrfnotifyfcpara_list_1 -%}
    SET NRFNOTIFYFCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.NFCHGCACHETHD is not none -%}
        NFCHGCACHETHD={{item.NFCHGCACHETHD}},
    {%- endif -%}
    {%- if item.NFCHGCACHETIME is not none -%}
        NFCHGCACHETIME={{item.NFCHGCACHETIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

