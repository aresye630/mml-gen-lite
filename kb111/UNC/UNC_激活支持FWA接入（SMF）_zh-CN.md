---
id: ''
name: 激活支持FWA接入（SMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持FWA接入特性的操作过程。  FWA（Fixed Wireless Access）是一种固定宽带的接入技术，指家庭或企业的各种终端设备通过CPE（Customer-Premises Equipment ）直接接入无线网络，提供用户宽带接入功能。根据接入方式可以将固定宽带的接入方式分为有线接入技术和无线接入技术两种，有线接入技术主要包括混合光纤同轴电缆（HFC）接入、铜线（xDSL）接入和光纤（FTTx）接入；无线接入技术主要就是固定无线接入（FWA）。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","基本接入功能","WSFD-010112 支持FWA接入","激活支持FWA接入（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持FWA接入特性的操作过程。FWA（Fixed Wireless Access）是一种固定宽带的接入技术，指家庭或企业的各种终端设备通过CPE（Customer-Premises Equipment ）直接接入无线网络，提供用户宽带接入功能。根据接入方式可以将固定宽带的接入方式分为有线接入技术和无线接入技术两种，有线接入技术主要包括混合光纤同轴电缆（HFC）接入、铜线（xDSL）接入和光纤（FTTx）接入；无线接入技术主要就是固定无线接入（FWA）。

## 必备事项
前提条件

* 请仔细阅读WSFD-010112 支持FWA接入特性概述。
* 完成加载License，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_fwamatchrule_list:
      type: items
      properties:
        MATCHTYPE:
          name: '匹配类型'
          type: string
          enum:
          - MatchTypeRule
          - MatchTypeApn
          required: true
          description: '增加FWA用户匹配规则。SMF根据匹配方式和匹配类型判断当前用户是否是FWA用户。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHFUNC:
          name: '匹配方式'
          type: string
          enum:
          - MatchFuncFull
          - MatchFuncContain
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULE:
          name: 'PCC规则'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: 'DWORD1040 BIT19 控制N11SMF是否支持FWA用户的识别。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_fwamatchrule_list:
    - MATCHTYPE: RULE
      MATCHFUNC: FULL
      RULE: 'up_87000017'
      APN: ''
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1040
      VALUE: VALUE_1
      POSITION: 19
      BYTENUM: ''
      BYTEPOSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 增加FWA用户匹配规则。SMF根据匹配方式和匹配类型判断当前用户是否是FWA用户。

#### 2.1 //增加FWA用户匹配规则。

```jinja2
{%- for item in add_fwamatchrule_list -%}
    ADD FWAMATCHRULE:
    {#- --- 必选参数 --- -#}
    MATCHTYPE={{item.MATCHTYPE}},
    MATCHFUNC={{item.MATCHFUNC}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MATCHTYPE=MatchTypeRule 时必选 --- -#}
    {%- if item.MATCHTYPE == 'MatchTypeRule' -%}
        RULE="{{item.RULE}}",
    {%- endif -%}
    {#- --- 条件必选：MATCHTYPE=MatchTypeApn 时必选 --- -#}
    {%- if item.MATCHTYPE == 'MatchTypeApn' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置N11SMF支持FWA用户的识别。

#### 3.1 //配置N11SMF支持FWA用户的识别。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

