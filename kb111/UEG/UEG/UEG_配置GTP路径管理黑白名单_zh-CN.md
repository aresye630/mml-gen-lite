---
id: GWFD-020802
name: 配置GTP路径管理黑白名单
ne_type: UEG
type: feature
description: 当运营商在部署分组交换网，新增UEG时，需要配置GTP路径管理黑白名单。UEG可以通过GTP路径管理黑白名单区分是否需要对网络中的对端网元进行探测。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-020800 基本业务","GWFD-020802 路径管理","配置GTP路径管理黑白名单"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增UEG时，需要配置GTP路径管理黑白名单。UEG可以通过GTP路径管理黑白名单区分是否需要对网络中的对端网元进行探测。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020802 路径管理。
* 完成配置GTP/PFCP路径管理参数。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
  examples:
    set_upgtppath_list:
    - ECHOLISTSWITCH: ENABLE
      ECHOLISTTYPE: WHITE
    add_echoiplist_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.1.10'
      IPV4MASK: 24
      IPV6ADDR: fc00::1
      IPV6MASK: '64'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 开启GTP路径管理的黑白名单开关，配置GTP路径管理名单属性为白名单。

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

```jinja2
{%- for item in add_echoiplist_list -%}
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
```

