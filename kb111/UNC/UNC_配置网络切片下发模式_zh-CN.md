---
id: ''
name: 配置网络切片下发模式
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置支持网络切片模式下发的操作过程。  AMF支持基于PLMN配置NSSAI Inclusion Mode，来决定UNC控制UE在创建RRC连接时是否携带网络切片信息及携带此信息的方式。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF非容灾组网","AMF配置","可选功能配置","配置网络切片下发模式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置支持网络切片模式下发的操作过程。AMF支持基于PLMN配置NSSAI Inclusion Mode，来决定UNC控制UE在创建RRC连接时是否携带网络切片信息及携带此信息的方式。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读网络切片模式下发原理。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCS:
          name: 'MCS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPS:
          name: 'MPS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPSMCSPRI:
          name: 'MPSMCS优先级'
          type: string
          enum:
          - CFG_FIRST
          - SUB_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CFG_FIRST
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
      IMSI: ''
      IMSIPRE: ''
      MCS: 'NULL'
      MPS: 'NULL'
      MPSMCSPRI: CFG_FIRST
    set_ngmmfunc_list:
    - NIMPLCY: STANDARD_MODE
      NIM: MODE_A
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置网络切片包含模式。

#### 2.1 //配置网络切片包含模式。

```jinja2
{%- for item in add_ngmmsubdata_list -%}
    ADD NGMMSUBDATA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NIM is not none -%}
        NIM={{item.NIM}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MCS is not none -%}
            MCS={{item.MCS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MPS is not none -%}
            MPS={{item.MPS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MPSMCSPRI is not none -%}
            MPSMCSPRI={{item.MPSMCSPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置下发NIM给UE的判断策略。

#### 3.1 //配置下发NIM给UE的判断策略。

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

