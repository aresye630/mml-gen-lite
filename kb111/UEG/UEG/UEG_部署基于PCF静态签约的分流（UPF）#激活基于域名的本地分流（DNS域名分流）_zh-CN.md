---
id: ''
name: 激活基于域名的本地分流（DNS域名分流）
ne_type: UEG
type: feature
description: 部署基于域名的本地分流功能，需要配置七层分流规则。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC ULCL专题（公共）","分流业务部署","基于PCF静态签约的分流","功能部署","部署基于PCF静态签约的分流（UPF）","激活基于域名的本地分流（DNS域名分流）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
部署基于域名的本地分流功能，需要配置七层分流规则。

## 必备事项
前提条件

* 请仔细阅读分流原理。
* 已完成与周边网元的对接。
* 完成协议识别库和解析库的加载。
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
          description: '配置UL CL与PSA1共部署的本地分流功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_host_list:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置触发分流的Host信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
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
          description: '流过滤器。  说明：  flowfilter_ulcl01用于DNS报文的匹配，flowfilter_ulcl02用于TCP报文的匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。  说明：  匹配DNS报文的过滤条件，三四层协议只能配置为UDP。'
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
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 65535
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
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: 'Host配置名称已通过**ADD HOST**命令配置。'
          data_source: '已配置数据中获取'
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
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '匹配DNS报文的过滤条件需要配置七层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URL类型'
          type: string
          enum:
          - HOST
          - URL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: URL
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '该参数取值要和**ADD HOST**命令配置的域名保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_protbindflowf_list:
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
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '匹配DNS报文的过滤条件需要绑定七层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '七层过滤器名字已通过**ADD L7FILTER**命令配置。'
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
    add_host_list:
    - HOSTNAME: 'host1'
      DOMAINVALUE: 'www.huawei.com'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl01'
      TETHERDETFLAG: NONE
    add_filter_list:
    - FILTERNAME: 'filter_test01'
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: 53
      SVRENDPORT: 53
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'host1'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl01'
      FILTERNAME: 'filter_test01'
    add_l7filter_list:
    - L7FILTERNAME: 'l7filter-test'
      SUBL7FLTNAME: 'sl7filter-test'
      URLTYPE: URL
      URL: 'www.huawei.com'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl01'
      PROTOCOLNAME: 'dns'
      L7FILTERNAME: 'l7filter-test'
    add_flowfiltergrp_list:
    - FLWFLTRGRPNAME: 'flowfiltergrp_ulcl01'
      FLOWFILTERNAME: 'flowfilter_ulcl01'
      FLWFLTRLOGICGRP: OR
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置UL CL与PSA1共部署的本地分流功能开关。

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

### 2 配置Host信息。

```jinja2
{%- for item in add_host_list -%}
    ADD HOST:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    DOMAINVALUE="{{item.DOMAINVALUE}}",
    ;
{%- endfor -%}
```

### 3 配置基于域名的本地分流过滤条件。

#### 3.1 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置三四层过滤条件。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {%- if item.SVRIPMODE is not none -%}
        SVRIPMODE={{item.SVRIPMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 绑定三四层过滤条件。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.4 配置七层过滤条件。

```jinja2
{%- for item in add_l7filter_list -%}
    ADD L7FILTER:
    {#- --- 必选参数 --- -#}
    L7FILTERNAME="{{item.L7FILTERNAME}}",
    SUBL7FLTNAME="{{item.SUBL7FLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URLTYPE is not none -%}
        URLTYPE={{item.URLTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLTYPE=URL 时可选 --- -#}
    {%- if item.URLTYPE == 'URL' -%}
        {%- if item.URL is not none -%}
            URL="{{item.URL}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 绑定七层过滤条件。

```jinja2
{%- for item in add_protbindflowf_list -%}
    ADD PROTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.L7FILTERNAME is not none -%}
        L7FILTERNAME="{{item.L7FILTERNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置本地分流流过滤器组。

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

### 流过滤器组对应SMF下发的AppID。一个流过滤器组中需要绑定基于域名的本地分流过滤条件，才能实现针对一个AppID的分流功能。

### 匹配中流过滤器组后，根据ApplD检索到分流PDR，然后按照PDR中的转发规则FAR、QoS规则QER执行策略动作。

