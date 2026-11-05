---
id: GWFD-021404
name: 激活S6a/S6d接口固定速率流控功能
ne_type: UEG
type: feature
description: S6a/S6d/DRA存在过载风险时，微服务USN基于配置的流控速率阈值，控制Attach、Inter TAU/RAU、Intra TAU(GERAN/UTRAN->LTE)、Intra RAU(LTE->GERAN/UTRAN)流程首次到HSS/DRA的取鉴权集请求或位置更新请求的速率，对于超过阈值的请求，给UE返回Attach Reject或TAU/RAU Reject消息，并携带相应失败原因值。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","S6a/S6d接口固定速率流控功能","激活S6a/S6d接口固定速率流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
S6a/S6d/DRA存在过载风险时，微服务USN基于配置的流控速率阈值，控制Attach、Inter TAU/RAU、Intra TAU(GERAN/UTRAN->LTE)、Intra RAU(LTE->GERAN/UTRAN)流程首次到HSS/DRA的取鉴权集请求或位置更新请求的速率，对于超过阈值的请求，给UE返回Attach Reject或TAU/RAU Reject消息，并携带相应失败原因值。适用于SGSN、MME。

## 必备事项
前提条件

请仔细阅读S6a/S6d接口固定速率流控功能特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_emmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AIR
          - ATTACH
          - AUTHENTICATION
          - CHECK_IMEI
          - CONTEXT_RESPONSE
          - INTER_TAU
          - LOCATION_UPDATE
          - PAGING
          - UPDATE_LOCATION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRS6AFLOWCTRL:
          name: 'ULR拒绝原因值（S6a接口流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: '设置S1模式移动性管理流程控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AIRS6AFLOWCTRL:
          name: 'AIR拒绝原因值（S6a接口流控）'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fixedfc_list:
      type: items
      properties:
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置固定速率流控信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCTHD:
          name: '固定流控速率'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_emmproctrl_list:
    - PROT: UPDATE_LOCATION
      ULRS6AFLOWCTRL: 10
      AIRS6AFLOWCTRL: 10
    set_fixedfc_list:
    - FCSWITCH: ON
      FCTHD: 400
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置因S6a接口流控而导致ULR/AIR流程失败时，下发给UE的原因值。

### ****SET EMMPROCTRL****

```jinja2
{%- for item in set_emmproctrl_list -%}
    SET EMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=UPDATE_LOCATION 时可选 --- -#}
    {%- if item.PROT == 'UPDATE_LOCATION' -%}
        {%- if item.ULRS6AFLOWCTRL is not none -%}
            ULRS6AFLOWCTRL={{item.ULRS6AFLOWCTRL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=AIR 时可选 --- -#}
    {%- if item.PROT == 'AIR' -%}
        {%- if item.AIRS6AFLOWCTRL is not none -%}
            AIRS6AFLOWCTRL={{item.AIRS6AFLOWCTRL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开固定速率流控开关，计算并设置固定流控速率。

### ****SET FIXEDFC****

```jinja2
{%- for item in set_fixedfc_list -%}
    SET FIXEDFC:
    {#- --- 可选参数 --- -#}
    {%- if item.FCSWITCH is not none -%}
        FCSWITCH={{item.FCSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.FCTHD is not none -%}
            FCTHD={{item.FCTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 固定流控速率的取值参照S6a/S6d接口固定速率流控功能实现原理页面。

