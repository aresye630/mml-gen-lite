---
id: GWFD-021102
name: 激活漫游控制特性(适用于AMF)
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活漫游控制特性的操作过程。  漫游控制，是指UEG提供互连PLMN表的配置，只有配置允许互连的PLMN用户才能够接入本UEG。漫游控制特性使网络具有限制用户移动范围和业务访问的能力。对于非本网的且不在互联PLMN表中的用户，将拒绝其接入，拒绝的原因值可灵活配置。  适用于AMF。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021100 移动性管理","GWFD-021102 漫游控制","激活漫游控制特性(适用于AMF)"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021100 移动性管理","GWFD-021102 漫游控制","激活漫游控制特性(适用于AMF)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活漫游控制特性的操作过程。漫游控制，是指UEG提供互连PLMN表的配置，只有配置允许互连的PLMN用户才能够接入本UEG。漫游控制特性使网络具有限制用户移动范围和业务访问的能力。对于非本网的且不在互联PLMN表中的用户，将拒绝其接入，拒绝的原因值可灵活配置。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-021102 漫游控制特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngconnectplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '5G互联的PLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AUSF_DISCOVERY
          - AIR
          - AUTHENTICATION
          - SMC
          - CHECK_IMEI
          - UDM_DISCOVERY
          - UDM_REGISTRATION
          - UDM_GET_SUBSCRIBER_DATA
          - UDM_SUBSCIBE
          - PCF_DISCOVERY
          - PCF_POLICY
          - OTHER_PROC
          - CAG
          required: true
          description: '设置漫游受限拒绝原因值'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMRST:
          name: '漫游受限拒绝原因值'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngconnectplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '45'
      DESC: 'for MNO A'
    set_ngmmproctrl_list:
    - PROT: OTHER_PROC
      ROAMRST: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加互联的PLMN，并配置允许的业务。

```jinja2
{%- for item in add_ngconnectplmn_list -%}
    ADD NGCONNECTPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置漫游受限拒绝原因值。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=OTHER_PROC 时可选 --- -#}
    {%- if item.PROT == 'OTHER_PROC' -%}
        {%- if item.ROAMRST is not none -%}
            ROAMRST={{item.ROAMRST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

