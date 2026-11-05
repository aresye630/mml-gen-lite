---
id: GWFD-026201
name: 激活RedCap接入（AMF和SMF，周边网元全升级场景）
ne_type: UEG
type: feature
description: 本操作指导用于核心网所有网元及gNodeB都支持RedCap功能的场景下，激活RedCap用户接入。  适用于AMF和SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","RedCap基本功能","GWFD-026201 RedCap终端标准接入","激活RedCap接入","激活RedCap接入（AMF和SMF，周边网元全升级场景）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导用于核心网所有网元及gNodeB都支持RedCap功能的场景下，激活RedCap用户接入。适用于AMF和SMF。

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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATCMPTSW:
          name: 'RatType兼容性开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NTYSMFPLCY:
          name: '空闲态会话通知SMF策略'
          type: string
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PCF:
          name: 'PCF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        UPF:
          name: 'UPF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AAAACCT:
          name: 'AAAACCT'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AAAAUTH:
          name: 'AAAAUTH'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        N16SMF:
          name: 'N16SMF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        N16ASMF:
          name: 'N16ASMF'
          type: string
          enum:
          - NR
          - NR_REDCAP
          required: false
          description: '保持系统初始值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_qosctrl_list:
      type: items
      properties:
        USERTYPE:
          name: 'USERTYPE'
          type: string
          enum:
          - ROAMING
          - VISITING
          - HOME
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RATTYPE'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_amfredcapfunc_list:
    - REDCAPSW: YES
      RATCMPTSW: UDM-1&PCF-1&SMSF-1&SMF-1
      NTYSMFPLCY: IMMEDIATELY_NOTIFY_ON_CHANGE-1&CHANNEL_ASSOCIATED_NOTIFY-0
    set_smffunc_list:
    - REDCAPSW: Support
    set_redcapratvalue_list:
    - CHF: NR_REDCAP
      PCF: NR_REDCAP
      UPF: NR_REDCAP
      AAAACCT: NR_REDCAP
      AAAAUTH: NR_REDCAP
      N16SMF: NR_REDCAP
      N16ASMF: NR_REDCAP
    set_qosctrl_list:
    - USERTYPE: HOME
      RATTYPE: REDCAP-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加AMF兼容性策略：

#### 2.1 //打开AMF上的RedCap功能开关，RatType所有周边网元兼容性开关，配置AMF向空闲态PDU会话关联的SMF通知RatType的策略。

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

#### 3.1 //打开SMF上的RedCap功能开关。

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

#### 4.1 //配置SMF向所有周边网元传递RatType的值为NR\_REDCAP。

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

### 5 设置RedCap终端接入Qos控制：

#### 5.1 //配置SMF上的RedCap制式的Qos控制功能开关。

```jinja2
{%- for item in set_qosctrl_list -%}
    SET QOSCTRL:
    {#- --- 必选参数 --- -#}
    USERTYPE={{item.USERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.RATTYPE is not none -%}
        RATTYPE={{item.RATTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

