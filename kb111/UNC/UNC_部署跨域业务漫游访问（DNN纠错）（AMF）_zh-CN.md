---
id: ''
name: 部署跨域业务漫游访问（DNN纠错）（AMF）
ne_type: UNC
type: feature
description: 在行业用户签约专用DNN场景下，需要将用户请求的DNN纠正为专用DNN再进行后续流程。  可按此指导配置AMF上的DNN纠错功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-228001 跨域业务访问","部署跨域业务漫游访问（DNN纠错）（AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在行业用户签约专用DNN场景下，需要将用户请求的DNN纠正为专用DNN再进行后续流程。可按此指导配置AMF上的DNN纠错功能。

## 必备事项
前提条件

* 请仔细阅读WSFD-228001 跨域业务访问特性概述。
* 已完成特性License（82209921 LKV2DNNC01 DNN纠正）加载并打开license配置开关，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
        DISFAILPLCY:
          name: 'SMF发现失败处理策略'
          type: string
          enum:
          - STANDARD_MODEL
          - RETRY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD_MODEL
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
  examples:
    add_localnsdnn_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      CORRECTTYPE: DNN_CORRECTION
      DNN: 'Huawei.com'
      DNNPLCY: Default_DNN_preferred
      DISFAILPLCY: STANDARD_MODEL
      SD: 'FFFFFF'
      SST: ''
      IMSI: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置DNN纠正信息及DNN纠正策略。

#### 2.1 //为全网IMSI前缀为12303的用户配置DNN纠正信息，AMF本地配置的DNN是Huawei.com，DNN纠正策略为签约default DNN优先。

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
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNNPLCY={{item.DNNPLCY}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CORRECTTYPE=DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        {%- if item.DISFAILPLCY is not none -%}
            DISFAILPLCY={{item.DISFAILPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

