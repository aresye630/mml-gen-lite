---
id: GWFD-020905
name: 激活请求信息纠正功能
ne_type: UEG
type: feature
description: 如果某地区因手机DNN参数设置错误，导致用户携带DNN的不被选择的切片支持，并且所选切片中不包含默认DNN，从而造成的PDU会话激活成功率低，建议开启本特性。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-020900 接入管理","GWFD-020905 请求信息纠正功能（适用于AMF、SMF）","激活请求信息纠正功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
如果某地区因手机DNN参数设置错误，导致用户携带DNN的不被选择的切片支持，并且所选切片中不包含默认DNN，从而造成的PDU会话激活成功率低，建议开启本特性。

## 必备事项
前提条件

* 请仔细阅读GWFD-020905 请求信息纠正功能特性概述（适用于AMF、SMF）。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnsdnn_list:
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
          description: '增加DNN纠正和DNN纠正策略配置。'
          data_source: '全网规划'
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
        CORRECTTYPE:
          name: '纠正类型'
          type: string
          enum:
          - NS_CORRECTION
          - DNN_CORRECTION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'AMF本地配置的DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNPLCY:
          name: 'DNN纠正策略'
          type: string
          enum:
          - Default_DNN_preferred
          - Only_The_Configured_DNN
          - Configured_DNN_Preferred
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pduactctrl_list:
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
          - SPECIFIC_IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNTYPE:
          name: 'DNN类型'
          type: string
          enum:
          - ALL_DNN
          - NOT_NULL_DNN
          - NULL_DNN
          - SPECIAL_DNN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnsdnn_list_1:
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
          description: '增加DNN纠正和DNN纠正策略配置。'
          data_source: '全网规划'
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
        CORRECTTYPE:
          name: '纠正类型'
          type: string
          enum:
          - NS_CORRECTION
          - DNN_CORRECTION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'AMF本地配置的DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNPLCY:
          name: 'DNN纠正策略'
          type: string
          enum:
          - Default_DNN_preferred
          - Only_The_Configured_DNN
          - Configured_DNN_Preferred
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
          description: ''
          data_source: ''
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2DNNC01'
      SWITCH: ENABLE
    add_localnsdnn_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      CORRECTTYPE: NS_CORRECTION
      SST: 1
      SD: '010101'
      DNN: 'Huawei'
      DNNPLCY: Configured_DNN_Preferred
    add_pduactctrl_list:
    - SUBRANGE: ''
      DNNTYPE: ''
    add_localnsdnn_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      CORRECTTYPE: DNN_CORRECTION
      SST: 1
      SD: '010101'
      DNN: 'Huawei'
      DNNPLCY: Configured_DNN_Preferred
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1039
      VALUE: VALUE_1
      POSITION: 21
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **以下步骤在AMF上执行**

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 打开license配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.3 配置切片纠正信息。

```jinja2
{%- for item in add_localnsdnn_list -%}
    ADD LOCALNSDNN:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    CORRECTTYPE={{item.CORRECTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNNPLCY={{item.DNNPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 **可选：**配置基于DNN配置PDU会话激活处理策略。当运营商需要限制某些特定DNN的用户接入网络，或者PDU会话激活流程中，若签约数据DNN匹配失败，需要AMF拒绝UE的PDU激活请求，可以通过配置本步骤实现。

```jinja2
{%- if is_optional_pdu_session_activation_policy -%}
    {%- for item in add_pduactctrl_list -%}
        ADD PDUACTCTRL:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        DNNTYPE={{item.DNNTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置DNN纠正信息及DNN纠正策略。

```jinja2
{%- for item in add_localnsdnn_list_1 -%}
    ADD LOCALNSDNN:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    CORRECTTYPE={{item.CORRECTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNNPLCY={{item.DNNPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **以下步骤在SMF上执行**

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 5G用户接入时将AMF携带的SelectedDNN作为用户请求DNN使用。

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
    ;
{%- endfor -%}
```

