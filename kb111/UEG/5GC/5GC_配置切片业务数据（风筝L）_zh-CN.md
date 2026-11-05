---
id: ''
name: 配置切片业务数据（风筝L）
ne_type: UEG
type: feature
description: 本场景用于配置风筝L场景切片相关的业务数据。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","业务发放","5GC toB 网络切片发放（专网，入驻式）","通过CN NSSMF发放","切片发放操作","普通创建（新建NSSI）","制作切片业务脚本","配置切片业务数据（风筝L）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于配置风筝L场景切片相关的业务数据。

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
          description: '配置AMF/SMF支持的切片。   * 参数“NFTYPE”固定取值为“NfAMF/NfSMF”。 * 参数“NSIDX”在**ADD PLMNS**的参数“NSIDX”中定义，此处引用。'
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
    add_nfns_list_1:
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
          description: '配置AMF/SMF支持的切片。   * 参数“NFTYPE”固定取值为“NfAMF/NfSMF”。 * 参数“NSIDX”在**ADD PLMNS**的参数“NSIDX”中定义，此处引用。'
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
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置SMF/UPF支持的切片。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“SST”在**ADD PLMNS**的参数“SST”中定义，此处引用。 * 参数“SD”在**ADD PLMNS**的参数“SD”中定义，此处引用。'
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
          description: '配置SMF/UPF支持的DNN。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“PNFNSINDEX”在**ADD PNFNS**的参数“INDEX”中定义，此处引用。'
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
    add_pnfns_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置SMF/UPF支持的切片。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“SST”在**ADD PLMNS**的参数“SST”中定义，此处引用。 * 参数“SD”在**ADD PLMNS**的参数“SD”中定义，此处引用。'
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
    add_pnfdnn_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置SMF/UPF支持的DNN。   * “NFINSTANCEID”通过**ADD PNFPROFILE**命令的参数“NFINSTANCEID”定义，此处引用。 * 参数“PNFNSINDEX”在**ADD PNFNS**的参数“INDEX”中定义，此处引用。'
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
    add_snssai_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置UPF支持的切片。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_snssaiupintf_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置切片和逻辑接口的绑定关系。   * 仅当需要支持N3接口隔离时需要配置。 * 参数“N3LOGICINF”不能为缺省N3口：n3if1/1/0。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N3LOGICINF:
          name: 'N3逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
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
    add_nfns_list_1:
    - NFTYPE: NfSMF
      NSIDX: 1
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'upf_instance_0'
      SST: 1
      SD: '131313'
    add_pnfdnn_list:
    - INDEX: 0
      NFINSTANCEID: 'upf_instance_0'
      DNN: 'kite2ul'
      PNFNSINDEX: 10
    add_pnfns_list_1:
    - INDEX: 11
      NFINSTANCEID: 'smf_instance_0'
      SST: 1
      SD: '131313'
    add_pnfdnn_list_1:
    - INDEX: 11
      NFINSTANCEID: 'smf_instance_0'
      DNN: 'kite2ul'
      PNFNSINDEX: 1
    add_snssai_list:
    - SST: 1
      SD: '131313'
    add_snssaiupintf_list:
    - SST: 1
      SD: '131313'
      N3LOGICINF: 'N3IF1/1/1'
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

### 3 配置SMF支持的切片信息。

```jinja2
{%- for item in add_nfns_list_1 -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
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

### 6 配置AMF对接的SMF支持的切片信息。

```jinja2
{%- for item in add_pnfns_list_1 -%}
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

### 7 配置AMF对接的SMF切片支持的DNN。

```jinja2
{%- for item in add_pnfdnn_list_1 -%}
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

### 8 配置UPF切片信息。

```jinja2
{%- for item in add_snssai_list -%}
    ADD SNSSAI:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置切片和N3接口绑定。

```jinja2
{%- for item in add_snssaiupintf_list -%}
    ADD SNSSAIUPINTF:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    N3LOGICINF="{{item.N3LOGICINF}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

