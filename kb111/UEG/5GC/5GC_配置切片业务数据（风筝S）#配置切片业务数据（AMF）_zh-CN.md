---
id: ''
name: 配置切片业务数据（AMF）
ne_type: UEG
type: feature
description: 本场景用于在AMF上配置切片相关的业务数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 网络切片发放（专网，入驻式）","通过OMC发放","切片发放操作","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（AMF）"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 网络切片发放（专线，共享式）","通过OMC发放","切片发放操作","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（AMF）"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 网络切片发放（云网，带计算）","通过OMC发放","切片发放操作","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
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
          description: '配置AMF支持的切片。   * 参数“NFTYPE”固定取值为“NfAMF”。 * 参数“NSIDX”在**ADD PLMNS**的参数“NSIDX”中定义，此处引用。'
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
  examples:
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '131313'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置PLMN支持的切片。

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

### 2 配置AMF切片信息。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

