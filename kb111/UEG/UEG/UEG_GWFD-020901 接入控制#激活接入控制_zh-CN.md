---
id: GWFD-020901
name: 激活接入控制
ne_type: UEG
type: feature
description: 当在线用户已用带宽过大，超出协商的最大带宽时，设置带宽接入的控制方式。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","基本接入功能","GWFD-020901 接入控制","激活接入控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当在线用户已用带宽过大，超出协商的最大带宽时，设置带宽接入的控制方式。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-020901 接入控制。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEUL:
          name: '上行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEDL:
          name: '下行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPESWUL:
          name: '上行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CARSHAPESWDL:
          name: '下行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'apn'
    set_apnqosattr_list:
    - APN: 'apn'
      CARSHAPEUL: CAR
      CARSHAPEDL: CAR
      CARSHAPESWUL: ENABLE
      CARSHAPESWDL: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 增加APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 2 将带宽控制方式绑定到APN用例下。

```jinja2
{%- for item in set_apnqosattr_list -%}
    SET APNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CARSHAPESWUL is not none -%}
        CARSHAPESWUL={{item.CARSHAPESWUL}},
    {%- endif -%}
    {%- if item.CARSHAPESWDL is not none -%}
        CARSHAPESWDL={{item.CARSHAPESWDL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CARSHAPESWUL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWUL == 'ENABLE' -%}
        CARSHAPEUL={{item.CARSHAPEUL}},
    {%- endif -%}
    {#- --- 条件必选：CARSHAPESWDL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWDL == 'ENABLE' -%}
        CARSHAPEDL={{item.CARSHAPEDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

