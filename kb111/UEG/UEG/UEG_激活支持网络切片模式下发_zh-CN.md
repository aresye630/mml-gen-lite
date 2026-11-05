---
id: GWFD-026001
name: 激活支持网络切片模式下发
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持网络切片模式下发的操作过程。  AMF支持基于PLMN（Public Land Mobile Network）配置NSSAI Inclusion Mode信元，来决定AMF控制UE在创建RRC（Radio Resource Connection）连接时是否携带网络切片信息及携带此信息的方式。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-026001 支持网络切片模式下发","激活支持网络切片模式下发"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持网络切片模式下发的操作过程。AMF支持基于PLMN（Public Land Mobile Network）配置NSSAI Inclusion Mode信元，来决定AMF控制UE在创建RRC（Radio Resource Connection）连接时是否携带网络切片信息及携带此信息的方式。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-026001 支持网络切片模式下发特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngmmsubdata_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NIM:
          name: '3GPP接入方式下的网络切片包含模式'
          type: string
          enum:
          - MODE_A
          - MODE_B
          - MODE_C
          - MODE_D
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: MODE_C
    set_ngmmfunc_list:
      type: items
      properties:
        NIMPLCY:
          name: '网络切片包含模式策略'
          type: string
          enum:
          - STANDARD_MODE
          - CUSTOMIZED_MODE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NIM:
          name: '3GPP接入方式下的网络切片包含模式'
          type: string
          enum:
          - NOT_INCLUDE_NIM
          - MODE_A
          - MODE_B
          - MODE_C
          - MODE_D
          required: false
          description: 'AMF配置网络切片包含模式及下发NIM给UE的判断策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_ngmmsubdata_list:
    - SUBRANGE: HOME_USER
      NIM: MODE_A
    set_ngmmfunc_list:
    - NIMPLCY: STANDARD_MODE
      NIM: MODE_A
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置网络切片包含模式。

```jinja2
{%- for item in add_ngmmsubdata_list -%}
    ADD NGMMSUBDATA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NIM is not none -%}
        NIM={{item.NIM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置下发NIM给UE的判断策略。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NIMPLCY is not none -%}
        NIMPLCY={{item.NIMPLCY}},
    {%- endif -%}
    {%- if item.NIM is not none -%}
        NIM={{item.NIM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

