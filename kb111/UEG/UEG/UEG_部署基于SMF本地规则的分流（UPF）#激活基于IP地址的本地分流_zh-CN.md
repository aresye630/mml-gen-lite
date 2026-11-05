---
id: ''
name: 激活基于IP地址的本地分流
ne_type: UEG
type: feature
description: 部署基于IP地址的本地分流功能，需要配置三四层分流规则。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC ULCL专题（公共）","分流业务部署","基于SMF本地规则的分流","功能部署","部署基于SMF本地规则的分流（UPF）","激活基于IP地址的本地分流"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
部署基于IP地址的本地分流功能，需要配置三四层分流规则。

## 必备事项
前提条件

* 请仔细阅读分流原理。
* 已完成与周边网元的对接。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_colocatedlbo_list:
      type: items
      properties:
        ULCLSWITCH:
          name: 'ULCL功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置UL CL与PSA1共部署功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ANY
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - DOMAIN
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMASKLEN:
          name: '服务器IP地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfiltergrp_list:
      type: items
      properties:
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '对应SMF下发的Application ID。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLWFLTRLOGICGRP:
          name: '流过滤器逻辑分组'
          type: string
          enum:
          - AND
          - NOT
          - OR
          required: false
          description: '或组内的任何一个流过滤器命中，则执行分流流程。'
          data_source: '本端规划'
          pattern: ''
          default: OR
  examples:
    set_colocatedlbo_list:
    - ULCLSWITCH: ENABLE
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl03'
    add_filter_list:
    - FILTERNAME: 'filter_test03'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '192.168.1.1'
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: 32
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl03'
      FILTERNAME: 'filter_test03'
    add_flowfiltergrp_list:
    - FLWFLTRGRPNAME: 'flowfiltergrp_ulcl01'
      FLOWFILTERNAME: 'flowfilter_ulcl03'
      FLWFLTRLOGICGRP: OR
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置UL CL与PSA1共部署功能开关。

```jinja2
{%- for item in set_colocatedlbo_list -%}
    SET COLOCATEDLBO:
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLSWITCH is not none -%}
        ULCLSWITCH={{item.ULCLSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置基于IP地址的本地分流过滤条件。

#### 2.1 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 2.2 配置三四层过滤条件。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRIPMODE is not none -%}
        SVRIPMODE={{item.SVRIPMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIP="{{item.SVRIP}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMASKTYPE=LENGTHTYPE 时必选 --- -#}
    {%- if item.SVRIPMASKTYPE == 'LENGTHTYPE' -%}
        SVRIPMASKLEN={{item.SVRIPMASKLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 绑定三四层过滤条件。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

### 3 配置本地分流流过滤器组。

```jinja2
{%- for item in add_flowfiltergrp_list -%}
    ADD FLOWFILTERGRP:
    {#- --- 必选参数 --- -#}
    FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWFILTERNAME is not none -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {%- if item.FLWFLTRLOGICGRP is not none -%}
        FLWFLTRLOGICGRP={{item.FLWFLTRLOGICGRP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 流过滤器组对应SMF下发的AppID。一个流过滤器组中需要绑定基于IP地址的本地分流过滤条件，才能实现针对一个AppID的分流功能。

### 匹配中流过滤器组后，根据ApplD检索到分流PDR，然后按照PDR中的转发规则FAR、QoS规则QER执行策略动作。

