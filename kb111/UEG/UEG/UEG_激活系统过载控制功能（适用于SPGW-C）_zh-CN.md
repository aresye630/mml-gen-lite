---
id: GWFD-021401
name: 激活系统过载控制功能（适用于SPGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。  在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。  适用于SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021400 可靠性功能","GWFD-021401 系统过载控制功能","系统过载控制功能（适用于SPGW-C）","激活系统过载控制功能（适用于SPGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。在系统过载时，UEG通过控制接入系统的业务量来防止拥塞进一步恶化而造成整系统的瘫痪，从而保证了自身处理业务的稳定性和高优先级业务（如语音业务）的成功率。适用于SGW-C、PGW-C。

## 必备事项
前提条件

请仔细阅读GWFD-021401系统过载控制功能特性概述（适用于SPGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_cpapnaccesswal_list:
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
    set_gtpcfixedfc_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - CREATESESSIONREQUEST
          - MODIFYBEARERREQUEST
          - ALLMSGTYPE
          required: true
          description: '设置GTPC接口上指定消息类型固定速率流控信息。'
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
  examples:
    set_fcswitch_list:
    - SWITCH: ENABLE
    set_cpapnaccesswal_list:
    - APN: 'huawei.com'
      WALNUMBER: 300
    set_gtpcfixedfc_list:
    - MSGTYPE: CREATESESSIONREQUEST
      FCSWITCH: ON
      THRESHOLD: 4000
    set_overloadctrl_list:
    - CTRLENABLE: ENABLE
      AGINGTIME: 34
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

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
{%- for item in set_cpapnaccesswal_list -%}
    SET CPAPNACCESSWAL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WALNUMBER is not none -%}
        WALNUMBER={{item.WALNUMBER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置GTPC接口指定消息类型固定流控速率。

```jinja2
{%- for item in set_gtpcfixedfc_list -%}
    SET GTPCFIXEDFC:
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

### 5 设置信令抑制功能开关以及老化定时器时长。

```jinja2
{%- for item in set_overloadctrl_list -%}
    SET OVERLOADCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLENABLE is not none -%}
        CTRLENABLE={{item.CTRLENABLE}},
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

