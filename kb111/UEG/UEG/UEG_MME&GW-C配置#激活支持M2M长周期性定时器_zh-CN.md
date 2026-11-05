---
id: ''
name: 激活支持M2M长周期性定时器
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持M2M长周期性定时器的操作过程。  本特性针对长期处于静止或不经常移动状态的M2M类终端分配一个长周期定时器（extended periodic timer），用于延长终端位置更新（TAU/RAU）的周期，降低TAU/RAU频度，从而降低此类终端的功耗以及网络的信令负荷。  适用于MME。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","NB-IoT功能配置","MME&GW-C配置","激活支持M2M长周期性定时器"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持M2M长周期性定时器的操作过程。本特性针对长期处于静止或不经常移动状态的M2M类终端分配一个长周期定时器（extended periodic timer），用于延长终端位置更新（TAU/RAU）的周期，降低TAU/RAU频度，从而降低此类终端的功耗以及网络的信令负荷。适用于MME。

## 必备事项
前提条件

请仔细阅读GWFD-026102 支持M2M长周期性定时器特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          description: ''
          data_source: ''
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
    add_m2mplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '增加M2M的策略参数，即为不同范围的用户、不同的APN业务配置M2M业务相关参数，以满足运营商灵活部署网络的需求。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
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
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAUTAUTMRSRC:
          name: '长周期RAU或TAU定时器来源'
          type: string
          enum:
          - UE_REQUEST_PREFER
          - USE_CONFIG
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: USE_CONFIG
        LONGRAUTAUTMR:
          name: '长周期RAU或TAU定时器时长（小时）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
  examples:
    set_softparaofbit_list:
    - DT: DWORD_EX
      PARANUM: 31
      VALUE: VALUE_1
      POSITION: 26
    add_m2mplcy_list:
    - SUBRANGE: IMSI_PREFIX
      NOID: 0
      IMSIPRE: '12303'
      APNNI: 'M2M'
      RAUTAUTMRSRC: USE_CONFIG
      LONGRAUTAUTMR: 12
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开M2M长周期性定时器功能开关。

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

### 该软参控制是否下发M2M长周期定时器。

### 3 配置长周期定时器控制参数。

### 若系统同时配置了基于所有用户、本网用户或外网用户以及指定IMSI前缀的长周期定时器下发策略，当系统识别到终端支持长周期定时器时，将首先匹配基于“指定IMSI前缀”的记录，其次匹配基于“外网用户”或“本网用户”的记录，最后匹配基于“所有用户”的记录。

```jinja2
{%- for item in add_m2mplcy_list -%}
    ADD M2MPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RAUTAUTMRSRC is not none -%}
        RAUTAUTMRSRC={{item.RAUTAUTMRSRC}},
    {%- endif -%}
    {%- if item.LONGRAUTAUTMR is not none -%}
        LONGRAUTAUTMR={{item.LONGRAUTAUTMR}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
    {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
        NOID={{item.NOID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

