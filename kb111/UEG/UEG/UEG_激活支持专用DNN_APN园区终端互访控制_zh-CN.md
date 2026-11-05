---
id: ''
name: 激活支持专用DNN/APN园区终端互访控制
ne_type: UEG
type: feature
description: 对于UPF下沉到园区的场景，仅在不出园区的情况下允许终端互访，出园区后禁止终端互访时，需要激活本功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","支持专用DNN/APN园区终端互访控制","激活支持专用DNN/APN园区终端互访控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
对于UPF下沉到园区的场景，仅在不出园区的情况下允许终端互访，出园区后禁止终端互访时，需要激活本功能。

## 必备事项
前提条件

请仔细阅读支持专用DNN/APN园区终端互访控制功能概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apnuemutacc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '可以使用**LST UPAPN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INNERAPNS:
          name: '同APN内的控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: 'DISABLE表示允许终端互访。  ENABLE表示禁止终端互访。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERAPNS:
          name: '不同APN间的控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INNERAPNS_S5S8P:
          name: '同APN内S5S8口互访控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'ENABLE表示禁止未命中SGW白名单的终端互访流量。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INNERAPNS_N9A:
          name: '同APN内N9A口互访控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'ENABLE表示禁止未命中I-UPF白名单的终端互访流量。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_uemutaccwlist_list:
      type: items
      properties:
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '当前也支持IPV6的地址类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4START:
          name: 'IPV4起始地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4END:
          name: 'IPV4截止地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uemutwlistbind_list:
      type: items
      properties:
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '可以使用**LST UPAPN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WLISTTYPE:
          name: '白名单类型'
          type: string
          enum:
          - SGWU
          - UPF
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '可以使用**LST UEMUTACCWLIST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_apnuemutacc_list:
    - APN: 'apn-test'
      INNERAPNS: DISABLE
      INTERAPNS: ENABLE
      INNERAPNS_S5S8P: ENABLE
      INNERAPNS_N9A: ENABLE
    add_uemutaccwlist_list:
    - WLISTNAME: 'pawlist'
      IPVERSION: IPV4
      IPV4START: '192.168.1.1'
      IPV4END: '192.168.1.100'
    add_uemutwlistbind_list:
    - APNNAME: 'apn-test'
      WLISTTYPE: SGWU
      WLISTNAME: 'pawlist'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 APN下配置终端互访控制。

```jinja2
{%- for item in set_apnuemutacc_list -%}
    SET APNUEMUTACC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    INNERAPNS={{item.INNERAPNS}},
    INTERAPNS={{item.INTERAPNS}},
    {#- --- 可选参数 --- -#}
    {%- if item.INNERAPNS_S5S8P is not none -%}
        INNERAPNS_S5S8P={{item.INNERAPNS_S5S8P}},
    {%- endif -%}
    {%- if item.INNERAPNS_N9A is not none -%}
        INNERAPNS_N9A={{item.INNERAPNS_N9A}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 （可选）配置终端互访白名单。

```jinja2
{%- if is_optional_terminal_interaccess_whitelist -%}
    {%- for item in add_uemutaccwlist_list -%}
        ADD UEMUTACCWLIST:
        {#- --- 必选参数 --- -#}
        WLISTNAME="{{item.WLISTNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4START="{{item.IPV4START}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4END="{{item.IPV4END}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_terminal_interaccess_whitelist -%}
    {%- for item in add_uemutwlistbind_list -%}
        ADD UEMUTWLISTBIND:
        {#- --- 必选参数 --- -#}
        APNNAME="{{item.APNNAME}}",
        WLISTTYPE={{item.WLISTTYPE}},
        WLISTNAME="{{item.WLISTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

