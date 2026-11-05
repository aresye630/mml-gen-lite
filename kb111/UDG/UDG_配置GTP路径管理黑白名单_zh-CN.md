---
id: GWFD-010102
name: 配置GTP路径管理黑白名单
ne_type: UDG
type: feature
description: 当运营商在部署分组交换网，新增UDG时，需要配置GTP路径管理黑白名单。UDG可以通过GTP路径管理黑白名单区分是否需要对网络中的对端网元进行探测。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010102 路径管理","配置GTP路径管理黑白名单"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增UDG时，需要配置GTP路径管理黑白名单。UDG可以通过GTP路径管理黑白名单区分是否需要对网络中的对端网元进行探测。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-010102 路径管理。
* 完成配置GTP/PFCP路径管理参数。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_upgtppath_list:
      type: items
      properties:
        ECHOLISTSWITCH:
          name: 'EchoList 开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ECHOLISTTYPE:
          name: 'EchoList 类型'
          type: string
          enum:
          - BLACK
          - WHITE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_echoiplist_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IP掩码'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MASK:
          name: 'IP掩码'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_echoiplist_list_3:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MASK:
          name: 'IP掩码'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IP掩码'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_upgtppath_list:
    - ECHOLISTSWITCH: ENABLE
      ECHOLISTTYPE: WHITE
    add_echoiplist_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.1.10'
      IPV4MASK: 24
      IPV6ADDR: ''
      IPV6MASK: ''
    add_echoiplist_list_3:
    - IPVERSION: IPV6
      IPV6ADDR: fc00::1
      IPV6MASK: '64'
      IPV4ADDR: ''
      IPV4MASK: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 开启GTP路径管理的黑白名单开关，配置GTP路径管理名单属性为白名单。

#### 1.1 //开启GTP路径管理的黑白名单开关，配置GTP路径管理名单属性为白名单。

```jinja2
{%- for item in set_upgtppath_list -%}
    SET UPGTPPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.ECHOLISTSWITCH is not none -%}
        ECHOLISTSWITCH={{item.ECHOLISTSWITCH}},
    {%- endif -%}
    {%- if item.ECHOLISTTYPE is not none -%}
        ECHOLISTTYPE={{item.ECHOLISTTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置需要探测的对端网元的GTP信令面或者数据面IP地址段。

#### 2.1 //配置需要探测IPv4地址段。

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_echoiplist_list -%}
        ADD ECHOIPLIST:
        {#- --- 必选参数 --- -#}
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4MASK={{item.IPV4MASK}},
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6ADDR="{{item.IPV6ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6MASK={{item.IPV6MASK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 //配置需要探测IPv6地址段。

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_echoiplist_list_3 -%}
        ADD ECHOIPLIST:
        {#- --- 必选参数 --- -#}
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV6ADDR is not none -%}
            IPV6ADDR="{{item.IPV6ADDR}}",
        {%- endif -%}
        {%- if item.IPV6MASK is not none -%}
            IPV6MASK="{{item.IPV6MASK}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4MASK={{item.IPV4MASK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

