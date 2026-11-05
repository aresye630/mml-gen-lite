---
id: GWFD-026107
name: 激活Non-IP数据传输（S/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活Non-IP数据传输特性的操作过程。当Non-IP用户接入网络时，需要在UEG上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。  SGW-C、PGW-C
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026107 Non-IP数据传输（S/PGW-C）","激活Non-IP数据传输（S/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Non-IP数据传输特性的操作过程。当Non-IP用户接入网络时，需要在UEG上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。SGW-C、PGW-C

## 必备事项
前提条件

* 请仔细阅读GWFD-026107 Non-IP数据传输特性概述（S/PGW-C）。
* 完成激活基于信令面的数据传输（SGW-C）。
* 完成加载License。
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
    set_nonipfunc_list:
      type: items
      properties:
        NONIPSWITCH:
          name: 'Non-IP功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '全局Non-IP功能开关'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnnonipfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '指定APN下的Non-IP功能开关'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NONIPSWITCH:
          name: 'APN Non-IP功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpm2mservergrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'M2M服务器组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'M2M服务器组'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPTYPE:
          name: 'M2M服务器IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_cpm2mserver_list:
      type: items
      properties:
        GROUPNAME:
          name: 'M2M服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: 'M2M服务器'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERVERINDEX:
          name: 'M2M服务器索引'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPTYPE:
          name: 'M2M服务器IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SERVERIPV4ADDR:
          name: 'M2M服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVERPORT:
          name: '服务器端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 5683
    add_m2msvrgrpbind_list:
      type: items
      properties:
        GROUPNAME:
          name: 'M2M服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '指定M2M服务器组的名称'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '指定APN实例名称'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '话单字段模板名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPEEXT:
          name: 'pdp-type-extention'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SGIPTPTUNMETH:
          name: 'sgi-ptp-tunnelling-method'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WNBNIP11'
      SWITCH: ENABLE
    set_nonipfunc_list:
    - NONIPSWITCH: ENABLE
    set_apnnonipfunc_list:
    - APN: 'test'
      NONIPSWITCH: ENABLE
    add_cpm2mservergrp_list:
    - GROUPNAME: 'm2msrvgroup01'
      SERVERIPTYPE: IPV4
    add_cpm2mserver_list:
    - GROUPNAME: 'm2msrvgroup01'
      SERVERINDEX: 1
      SERVERIPTYPE: IPV4
      SERVERIPV4ADDR: '10.107.242.16'
      SERVERPORT: 2020
    add_m2msvrgrpbind_list:
    - GROUPNAME: 'm2msrvgroup01'
      APN: 'test'
    add_cdrfieldtemp_list:
    - TEMPLATENAME: 'cdrfieldtemp'
      PDPTYPEEXT: ENABLE
      SGIPTPTUNMETH: ENABLE
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

### 3 使能全局的Non-IP功能开关。

```jinja2
{%- for item in set_nonipfunc_list -%}
    SET NONIPFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NONIPSWITCH is not none -%}
        NONIPSWITCH={{item.NONIPSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 使能指定APN下的Non-IP功能开关。

```jinja2
{%- for item in set_apnnonipfunc_list -%}
    SET APNNONIPFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NONIPSWITCH is not none -%}
        NONIPSWITCH={{item.NONIPSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 业务处理过程中优先应用APN下的设置，只有当APN下配置为Inherit时才应用全局下的设置。

### 5 配置M2M服务器组。

```jinja2
{%- for item in add_cpm2mservergrp_list -%}
    ADD CPM2MSERVERGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    SERVERIPTYPE={{item.SERVERIPTYPE}},
    ;
{%- endfor -%}
```

### 6 配置M2M服务器组下的M2M服务器。

```jinja2
{%- for item in add_cpm2mserver_list -%}
    ADD CPM2MSERVER:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    SERVERINDEX={{item.SERVERINDEX}},
    SERVERIPTYPE={{item.SERVERIPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SERVERPORT is not none -%}
        SERVERPORT={{item.SERVERPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SERVERIPTYPE=IPV4 时必选 --- -#}
    {%- if item.SERVERIPTYPE == 'IPV4' -%}
        SERVERIPV4ADDR="{{item.SERVERIPV4ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **可选：**配置指定APN下的M2M服务器组。

```jinja2
{%- if is_optional_m2m_server_group -%}
    {%- for item in add_m2msvrgrpbind_list -%}
        ADD M2MSVRGRPBIND:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 **可选：**配置话单中是否携带pdp-type-extension、sgi-ptp-tunnelling-method字段。

```jinja2
{%- if is_optional_cdr_field -%}
    {%- for item in add_cdrfieldtemp_list -%}
        ADD CDRFIELDTEMP:
        {#- --- 必选参数 --- -#}
        TEMPLATENAME="{{item.TEMPLATENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PDPTYPEEXT is not none -%}
            PDPTYPEEXT={{item.PDPTYPEEXT}},
        {%- endif -%}
        {%- if item.SGIPTPTUNMETH is not none -%}
            SGIPTPTUNMETH={{item.SGIPTPTUNMETH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

