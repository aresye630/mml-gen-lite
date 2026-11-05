---
id: ''
name: 激活SGSN的黑白名单
ne_type: UNC
type: feature
description: 当需要对SGSN/MME/SGW-C进行接入控制时，激活SGSN的黑白名单。  适用于GGSN、SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-104509 SGSN的黑白名单","激活SGSN的黑白名单"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要对SGSN/MME/SGW-C进行接入控制时，激活SGSN的黑白名单。适用于GGSN、SGW-C、PGW-C。

## 必备事项
前提条件

请仔细阅读WSFD-104509 SGSN的黑白名单特性概述。
完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    set_accesslistfunc_list:
      type: items
      properties:
        LISTSWITCH:
          name: '设置系统是否支持接入控制名单的功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'GGSN/PGW-C支持两种SGSN/MME/SGW-C接入的控制名单类型：  * BLACK：黑名单使能。 * WHITE：白名单使能。  配置时只能根据需要选择一种名单。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LISTTYPE:
          name: '黑白名单类型'
          type: string
          enum:
          - WHITE
          - BLACK
          required: false
          description: '接入控制名单类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_accesslistip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '接入控制的SGSN/MME/SGW-C IP地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVNODEIPV4:
          name: 'IPv4地址段的地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVNODEIPV4MASK:
          name: '掩码长度'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVNODEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEIPV6MASK:
          name: '掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9SBWL11'
      SWITCH: ENABLE
    set_accesslistfunc_list:
    - LISTSWITCH: ENABLE
      LISTTYPE: BLACK
    add_accesslistip_list:
    - IPVERSION: IPV4
      SRVNODEIPV4: '10.20.0.2'
      SRVNODEIPV4MASK: 27
      SRVNODEIPV6: ''
      SRVNODEIPV6MASK: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 使能黑白名单控制开关并配置SGSN/MME/SGW-C接入控制名单类型。

```jinja2
{%- for item in set_accesslistfunc_list -%}
    SET ACCESSLISTFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.LISTSWITCH is not none -%}
        LISTSWITCH={{item.LISTSWITCH}},
    {%- endif -%}
    {%- if item.LISTTYPE is not none -%}
        LISTTYPE={{item.LISTTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置接入控制名单的SGSN/MME/SGW-C的IP地址段。

```jinja2
{%- for item in add_accesslistip_list -%}
    ADD ACCESSLISTIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SRVNODEIPV4="{{item.SRVNODEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SRVNODEIPV4MASK={{item.SRVNODEIPV4MASK}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SRVNODEIPV6="{{item.SRVNODEIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SRVNODEIPV6MASK={{item.SRVNODEIPV6MASK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

