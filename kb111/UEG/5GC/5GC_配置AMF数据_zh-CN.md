---
id: ''
name: 配置AMF数据
ne_type: UEG
type: feature
description: 本场景用于在AMF上配置切片相关的业务数据。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","运营商","配置5GC网元","配置AMF数据"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST LOCALNSDNN')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在AMF上配置切片相关的业务数据。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置切片的基本信息。其中，“NSIDX”不能重复且“PLMNIDX”由命令**LST NGSRVPLMN**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nfns_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: '配置AMF支持的切片。   * 参数“NFTYPE”固定取值为“NfAMF”。 * 参数“NSIDX”在**ADD PLMNNS**的参数“NSIDX”中定义，此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '已有配置中获取'
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
          description: '5G LAN用户均为HOME_USER，需要使用样例值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CORRECTTYPE:
          name: '纠正类型'
          type: string
          enum:
          - NS_CORRECTION
          - DNN_CORRECTION
          required: true
          description: '此处配置的是DNN纠正，需要使用样例值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '与**ADD PLMNNS**命令配置的SST保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: '与**ADD PLMNNS**命令配置的SD保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '与5G LAN业务的DNN一致。'
          data_source: '全网规划'
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
          description: '用户请求APN与签约APN不匹配时，优先纠正为签约数据中的Default DNN。如果未签约Default DNN，则纠正为本命令中配置的DNN。'
          data_source: '固定取值'
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
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: '该参数为可选参数，在运维中起助记作用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端SMF实例支持的DNN，可以基于DNN选择SMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端SMF实例支持的服务切片信息，可以基于切片选择SMF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'FFFFFF'
  examples:
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 1
    add_localnsdnn_list:
    - SUBRANGE: HOME_USER
      CORRECTTYPE: DNN_CORRECTION
      SST: 1
      SD: '010101'
      DNN: 'dnn5glan01'
      DNNPLCY: Default_DNN_preferred
      DISFAILPLCY: STANDARD_MODEL
      DESC: '5GLAN_DNN_Correction'
    add_pnfdnn_list:
    - INDEX: 5
      NFINSTANCEID: 'SMF_Instance_1'
      DNN: 'dnn5glan01'
    add_pnfns_list:
    - INDEX: 5
      NFINSTANCEID: 'SMF_Instance_1'
      SST: 1
      SD: '010101'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置PLMN支持的切片。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_plmnns_list -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置AMF切片信息。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

### 3 配置AMF对5G LAN切片下的DNN纠正。如现网已涉及DNN纠正功能（可通过**LST LOCALNSDNN**查询），则需要执行如下配置；否则，请跳过如下配置。

#### 3.1 //用户请求APN与签约APN不匹配时，优先纠正为签约数据中的Default DNN，如果未签约Default DNN，则纠正为dnn5glan01。

```jinja2
{%- set LST_LOCALNSDNN=getParameterValue('LST LOCALNSDNN') -%}
{%- if LST_LOCALNSDNN -%}
    {%- for item in add_localnsdnn_list -%}
        ADD LOCALNSDNN:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        CORRECTTYPE={{item.CORRECTTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
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
        {#- --- 条件可选：CORRECTTYPE=DNN_CORRECTION 时可选 --- -#}
        {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
            {%- if item.DISFAILPLCY is not none -%}
                DISFAILPLCY={{item.DISFAILPLCY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置对端SMF实例支持的DNN。可以基于DNN选择SMF。

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 5 配置对端SMF实例支持的切片。可以基于切片选择SMF。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

