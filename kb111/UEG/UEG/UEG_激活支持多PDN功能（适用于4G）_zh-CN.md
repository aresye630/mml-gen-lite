---
id: GWFD-020809
name: 激活支持多PDN功能（适用于4G）
ne_type: UEG
type: feature
description: 当UE需要同时访问多个网络，可以开启本功能，并针对特定APN，配置用户可以建立的PDN连接最大数目和IP地址最大数目。  多PDN/PDU（Packet Data Network）功能是指一个UE同时创建多个PDN连接（EPC）/PDU会话（5GC）来访问外部多个PDN网络，满足用户同时访问多个网络的要求。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020800 基本业务","GWFD-020809 支持多PDN/PDU功能","激活支持多PDN功能（适用于4G）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-020800 基本业务","GWFD-020809 支持多PDN/PDU功能","激活支持多PDN功能（适用于4G）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020800 基本业务","GWFD-020809 支持多PDN/PDU功能","激活支持多PDN功能（适用于4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当UE需要同时访问多个网络，可以开启本功能，并针对特定APN，配置用户可以建立的PDN连接最大数目和IP地址最大数目。多PDN/PDU（Packet Data Network）功能是指一个UE同时创建多个PDN连接（EPC）/PDU会话（5GC）来访问外部多个PDN网络，满足用户同时访问多个网络的要求。

## 必备事项
前提条件

请仔细阅读GWFD-020809 支持多PDN/PDU功能特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apnactnum_list:
      type: items
      properties:
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNNUM:
          name: 'PDN连接数目'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
        IPV4ADDRNUM:
          name: 'IPv4地址数目'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
        IPV6ADDRNUM:
          name: 'IPv6地址数目'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
        PDNCONNREJCAUSE:
          name: 'PDN连接拒绝原因'
          type: string
          enum:
          - INSUFFICIENT_RESOURCES_26
          - MULTI_PDN_FOR_APN_NOT_ALW_55
          - NETWORK_FAILURE_38
          - OPERATOR_DETERMINED_BARRING_8
          - PROTOCOL_ERROR_UNSPECIFED_111
          - REQUEST_REJECT_BY_SGW_OR_PGW_30
          - REQUEST_SERVICE_OPT_NOT_SUB_33
          - SERVICE_OPTION_NOT_SUPPORTED_32
          - UNKNOWN_OR_MISSING_APN_27
          - USER_AUTH_FAILED_29
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MULTI_PDN_FOR_APN_NOT_ALW_55
  examples:
    add_apnactnum_list:
    - APNNI: 'Internet'
      PDNNUM: 2
      IPV4ADDRNUM: 2
      IPV6ADDRNUM: 2
      PDNCONNREJCAUSE: MULTI_PDN_FOR_APN_NOT_ALW_55
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置针对某一APN，同一个用户可以建立的PDN连接最大数目和IP地址最大数目。

### ****ADD APNACTNUM****

```jinja2
{%- for item in add_apnactnum_list -%}
    ADD APNACTNUM:
    {#- --- 必选参数 --- -#}
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNNUM is not none -%}
        PDNNUM={{item.PDNNUM}},
    {%- endif -%}
    {%- if item.IPV4ADDRNUM is not none -%}
        IPV4ADDRNUM={{item.IPV4ADDRNUM}},
    {%- endif -%}
    {%- if item.IPV6ADDRNUM is not none -%}
        IPV6ADDRNUM={{item.IPV6ADDRNUM}},
    {%- endif -%}
    {%- if item.PDNCONNREJCAUSE is not none -%}
        PDNCONNREJCAUSE={{item.PDNCONNREJCAUSE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

