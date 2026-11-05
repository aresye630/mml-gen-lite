---
id: ''
name: 配置切片业务数据（SMF）
ne_type: UEG
type: feature
description: 本场景用于在SMF上配置切片相关的业务数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 网络切片发放（专网，入驻式）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（SMF）"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 网络切片发放（专线，共享式）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（SMF）"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 网络切片发放（云网，带计算）","通过CN NSSMF发放","切片发放操作","普通创建（复用NSSI）","制作切片业务脚本","配置切片业务数据（风筝S）","配置切片业务数据（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在SMF上配置切片相关的业务数据。

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
          data_source: '全网规划'
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
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
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
          description: '配置SMF支持的切片。   * 参数“NFTYPE”固定取值为“NfSMF”。 * 参数“NSIDX”在**ADD PLMNS**的参数“NSIDX”中定义，此处引用。'
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
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置SMF支持的DNN。   * 参数“NSIDX”在**ADD PLMNS**的参数“NSIDX”中定义，此处引用。 * 参数“DNN”在**ADD APN**中定义，在此处引用。 说明：  当存在DNN发放的场景时，需要以DNN发放中的**ADD APN**命令的配置为准。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
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
          description: '配置UPF支持的切片。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“SST”在**ADD PLMNS**的参数“SST”中定义，此处引用。 * 参数“SD”在**ADD PLMNS**的参数“SD”中定义，此处引用。'
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
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: 'FFFFFF'
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置UPF支持的DNN。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“PNFNSINDEX”在**ADD PNFNS**的参数“INDEX”中定义，此处引用。'
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '已有配置中获取'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
  examples:
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '131313'
      STATE: INACTIVE
    add_nfns_list:
    - NFTYPE: NfSMF
      NSIDX: 1
    add_nsdnn_list:
    - NSIDX: 1
      DNN: 'net'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: '81304a9d-0202-41db-8272-59159a70c123'
      SST: 1
      SD: '131313'
    add_pnfdnn_list:
    - INDEX: 0
      NFINSTANCEID: '81304a9d-0202-41db-8272-59159a70c123'
      DNN: 'net'
      PNFNSINDEX: 1
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
    {%- if item.STATE is not none -%}
        STATE={{item.STATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置SMF支持的切片信息。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

### 3 配置SMF切片支持的DNN。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 4 配置SMF对接的UPF支持的切片信息。

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

### 5 配置SMF对接的UPF切片支持的DNN。

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PNFNSINDEX is not none -%}
        PNFNSINDEX={{item.PNFNSINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

