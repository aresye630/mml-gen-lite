---
id: ''
name: 激活RedCap接入（周边部分网元未升级场景）
ne_type: UEG
type: feature
description: 本操作指导用于gNodeB和部分网元（AMF和SMF）支持RedCap功能的场景下，激活RedCap用户接入。RedCap功能支持周边网元免升级的情况，当部分网元不支持RedCap功能时，会将其当作普通NR用户处理。  适用于AMF和SMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置基础业务","5G Redcap功能配置","激活RedCap接入（周边部分网元未升级场景）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导用于gNodeB和部分网元（AMF和SMF）支持RedCap功能的场景下，激活RedCap用户接入。RedCap功能支持周边网元免升级的情况，当部分网元不支持RedCap功能时，会将其当作普通NR用户处理。适用于AMF和SMF。

## 必备事项
前提条件

请仔细阅读WSFD-010110 支持RedCap接入特性概述及实现原理。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_amfredcapfunc_list:
      type: items
      properties:
        REDCAPSW:
          name: 'RedCap功能开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATCMPTSW:
          name: 'RatType兼容性开关'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NTYSMFPLCY:
          name: '空闲态会话通知SMF策略'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        REDCAPSW:
          name: 'RedCap特性开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
    set_redcapratvalue_list:
      type: items
      properties:
        CHF:
          name: 'CHF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        PCF:
          name: 'PCF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        UPF:
          name: 'UPF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        AAAACCT:
          name: 'AAAACCT'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        AAAAUTH:
          name: 'AAAAUTH'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        N16SMF:
          name: 'N16SMF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        N16ASMF:
          name: 'N16ASMF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
  examples:
    set_amfredcapfunc_list:
    - REDCAPSW: YES
      RATCMPTSW: UDM-0&PCF-0&SMSF-0&SMF-1
      NTYSMFPLCY: IMMEDIATELY_NOTIFY_ON_CHANGE-1&CHANNEL_ASSOCIATED_NOTIFY-0
    set_smffunc_list:
    - REDCAPSW: Support
    set_redcapratvalue_list:
    - CHF: NR
      PCF: NR
      UPF: NR
      AAAACCT: NR
      AAAAUTH: NR
      N16SMF: NR
      N16ASMF: NR
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加AMF兼容性策略：

```jinja2
{%- for item in set_amfredcapfunc_list -%}
    SET AMFREDCAPFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.REDCAPSW is not none -%}
        REDCAPSW={{item.REDCAPSW}},
    {%- endif -%}
    {%- if item.NTYSMFPLCY is not none -%}
        NTYSMFPLCY={{item.NTYSMFPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：REDCAPSW=YES 时可选 --- -#}
    {%- if item.REDCAPSW == 'YES' -%}
        {%- if item.RATCMPTSW is not none -%}
            RATCMPTSW={{item.RATCMPTSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置SMF扩展功能：

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.REDCAPSW is not none -%}
        REDCAPSW={{item.REDCAPSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置RedCap终端接入RAT填写值：

```jinja2
{%- for item in set_redcapratvalue_list -%}
    SET REDCAPRATVALUE:
    {#- --- 可选参数 --- -#}
    {%- if item.CHF is not none -%}
        CHF={{item.CHF}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.AAAACCT is not none -%}
        AAAACCT={{item.AAAACCT}},
    {%- endif -%}
    {%- if item.AAAAUTH is not none -%}
        AAAAUTH={{item.AAAAUTH}},
    {%- endif -%}
    {%- if item.N16SMF is not none -%}
        N16SMF={{item.N16SMF}},
    {%- endif -%}
    {%- if item.N16ASMF is not none -%}
        N16ASMF={{item.N16ASMF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

