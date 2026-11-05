---
id: ''
name: 激活5G QoS到4G QoS灵活映射
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活5G QoS到4G QoS灵活映射特性的操作过程。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-105007 5G QoS到4G QoS灵活映射","激活5G QoS到4G QoS灵活映射"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活5G QoS到4G QoS灵活映射特性的操作过程。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读WSFD-105007 5G QoS到4G QoS灵活映射。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_qos5qi2qcimap_list:
      type: items
      properties:
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - APN_LEVEL
          - GLOBAL_LEVEL
          required: true
          description: '用于增加5QI到标准QCI的映射。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QISTART:
          name: '5QI范围起始值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QIEND:
          name: '5QI范围结束值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCI:
          name: 'QCI'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnambrctrl_list:
      type: items
      properties:
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - APN_LEVEL
          - GLOBAL_LEVEL
          required: true
          description: '配置APN-AMBR带宽速率控制参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行APN-AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行APN-AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbrbwctrl_list:
      type: items
      properties:
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - APN_LEVEL
          - GLOBAL_LEVEL
          required: true
          description: '配置GBR承载带宽速率控制参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUL:
          name: '上行保证速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行保证速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_qos5qi2qcimap_list:
    - CTRLTYPE: APN_LEVEL
      APN: 'huawei.com'
      QOS5QISTART: 1
      QOS5QIEND: 2
      QCI: 1
    add_apnambrctrl_list:
    - CTRLTYPE: APN_LEVEL
      APN: 'huawei.com'
      AMBRUL: 1000
      AMBRDL: 1000
    add_gbrbwctrl_list:
    - CTRLTYPE: APN_LEVEL
      APN: 'huawei.com'
      MBRUL: 1000
      MBRDL: 1000
      GBRUL: 1000
      GBRDL: 1000
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置5QI到标准QCI的映射。

```jinja2
{%- for item in add_qos5qi2qcimap_list -%}
    ADD QOS5QI2QCIMAP:
    {#- --- 必选参数 --- -#}
    CTRLTYPE={{item.CTRLTYPE}},
    QOS5QISTART={{item.QOS5QISTART}},
    QOS5QIEND={{item.QOS5QIEND}},
    QCI={{item.QCI}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CTRLTYPE=APN_LEVEL 时必选 --- -#}
    {%- if item.CTRLTYPE == 'APN_LEVEL' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置APN-AMBR带宽速率控制。

```jinja2
{%- for item in add_apnambrctrl_list -%}
    ADD APNAMBRCTRL:
    {#- --- 必选参数 --- -#}
    CTRLTYPE={{item.CTRLTYPE}},
    AMBRUL={{item.AMBRUL}},
    AMBRDL={{item.AMBRDL}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CTRLTYPE=APN_LEVEL 时必选 --- -#}
    {%- if item.CTRLTYPE == 'APN_LEVEL' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置GBR承载带宽速率控制。

```jinja2
{%- for item in add_gbrbwctrl_list -%}
    ADD GBRBWCTRL:
    {#- --- 必选参数 --- -#}
    CTRLTYPE={{item.CTRLTYPE}},
    MBRUL={{item.MBRUL}},
    MBRDL={{item.MBRDL}},
    GBRUL={{item.GBRUL}},
    GBRDL={{item.GBRDL}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CTRLTYPE=APN_LEVEL 时必选 --- -#}
    {%- if item.CTRLTYPE == 'APN_LEVEL' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

