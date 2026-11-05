---
id: ''
name: 激活RedCap eDRX功能（DDN寻呼流程）
ne_type: UNC
type: feature
description: 本操作指导介绍在5G eDRX模式时，UE不在寻呼窗口时的DDN寻呼流程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-990005 支持RedCap eDRX功能","激活RedCap eDRX功能（DDN寻呼流程）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在5G eDRX模式时，UE不在寻呼窗口时的DDN寻呼流程。适用于SMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-990005 支持5G eDRX功能特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_glbedrxattr_list:
      type: items
      properties:
        EDRXSW:
          name: '支持eDRX模式开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PKTCNTPRIORITY:
          name: '下行包缓存数获取优先级'
          type: string
          enum:
          - DLBUFFPKTCNT
          - UDM
          required: false
          description: '无特殊情况，保持初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DLBUFFPKTCNT:
          name: '下行包缓存数'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '无特殊情况，保持初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EXTDLBUFFTIME:
          name: '下行包缓存额外时长'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: '无特殊情况，保持初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_apnedrxattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EDRXSW:
          name: '支持eDRX模式开关'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: '* 当eDRX模式开关关闭时，请确保AMF上已经没有eDRX用户，否则存量eDRX用户的下行数据包，可能会被丢弃。 * 此参数优先级大于**SET GLBEDRXATTR**。根据不同APN的主要业务模型，可以针对性地配置下行包缓存缓存数获取优先级和下行包缓存数。例如，物流监控类业务，建议优先使用本地签约数据，配置本地缓存最大包数为10。 * 若有此类APN定制的业务需求，**EDRXSW**需配置为“ENABLE“。若无针对性的业务需求，此参数也可配置为“INHERIT“，继承全局下行包缓存参数。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        PKTCNTPRIORITY:
          name: '下行包缓存数获取优先级'
          type: string
          enum:
          - DLBUFFPKTCNT
          - UDM
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DLBUFFPKTCNT:
          name: '下行包缓存数'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        EXTDLBUFFTIME:
          name: '下行包缓存额外时长'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_pfcpcmpt_list:
      type: items
      properties:
        BAR:
          name: '是否支持BAR信元'
          type: string
          enum:
          - SUPPORT
          - NOT_SUPPORT
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
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
  examples:
    set_glbedrxattr_list:
    - EDRXSW: ENABLE
      PKTCNTPRIORITY: DLBUFFPKTCNT
      DLBUFFPKTCNT: 10
      EXTDLBUFFTIME: 20
    add_apnedrxattr_list:
    - APN: 'test'
      EDRXSW: ENABLE
      PKTCNTPRIORITY: DLBUFFPKTCNT
      DLBUFFPKTCNT: 10
      EXTDLBUFFTIME: 20
    set_pfcpcmpt_list:
    - BAR: SUPPORT
    set_licenseswitch_list:
    - LICITEM: 'LKV2RCEDRXSM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 （可选）以全局粒度配置下行包缓存参数：

```jinja2
{%- if is_optional_global_downlink_packet_cache -%}
    {%- for item in set_glbedrxattr_list -%}
        SET GLBEDRXATTR:
        {#- --- 可选参数 --- -#}
        {%- if item.EDRXSW is not none -%}
            EDRXSW={{item.EDRXSW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：EDRXSW=ENABLE 时必选 --- -#}
        {%- if item.EDRXSW == 'ENABLE' -%}
            PKTCNTPRIORITY={{item.PKTCNTPRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：EDRXSW=ENABLE 时必选 --- -#}
        {%- if item.EDRXSW == 'ENABLE' -%}
            EXTDLBUFFTIME={{item.EXTDLBUFFTIME}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 下行包缓存数: 条件必选(下行包缓存数获取优先级=DLBUFFPKTCNT) / 条件可选(下行包缓存数获取优先级=UDM) --- -#}
        {%- if (item.PKTCNTPRIORITY == 'DLBUFFPKTCNT') -%}
            DLBUFFPKTCNT={{item.DLBUFFPKTCNT}},
        {%- elif (item.PKTCNTPRIORITY == 'UDM') -%}
            {%- if item.DLBUFFPKTCNT is not none -%}
                DLBUFFPKTCNT={{item.DLBUFFPKTCNT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 以APN为粒度配置下行包缓存参数：

```jinja2
{%- for item in add_apnedrxattr_list -%}
    ADD APNEDRXATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EDRXSW is not none -%}
        EDRXSW={{item.EDRXSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：EDRXSW=ENABLE 时必选 --- -#}
    {%- if item.EDRXSW == 'ENABLE' -%}
        PKTCNTPRIORITY={{item.PKTCNTPRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：EDRXSW=ENABLE 时必选 --- -#}
    {%- if item.EDRXSW == 'ENABLE' -%}
        EXTDLBUFFTIME={{item.EXTDLBUFFTIME}},
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 下行包缓存数: 条件必选(下行包缓存数获取优先级=DLBUFFPKTCNT) / 条件可选(下行包缓存数获取优先级=UDM) --- -#}
    {%- if (item.PKTCNTPRIORITY == 'DLBUFFPKTCNT') -%}
        DLBUFFPKTCNT={{item.DLBUFFPKTCNT}},
    {%- elif (item.PKTCNTPRIORITY == 'UDM') -%}
        {%- if item.DLBUFFPKTCNT is not none -%}
            DLBUFFPKTCNT={{item.DLBUFFPKTCNT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置PFCP接口兼容性：

```jinja2
{%- for item in set_pfcpcmpt_list -%}
    SET PFCPCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.BAR is not none -%}
        BAR={{item.BAR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 打开本功能的License配置开关：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

