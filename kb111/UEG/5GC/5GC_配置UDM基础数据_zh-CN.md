---
id: ''
name: 配置UDM基础数据
ne_type: UEG
type: feature
description: 本场景用于在UDM上配置用户的开户数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB 业务发放概述（专网，入驻式）","参考","用户数据发放","数据配置","配置UDM基础数据"]
  - ["专线（仅连接，地市共享式）","业务发放","5GC toB 业务发放概述（专线，共享式）","参考","用户数据发放","数据配置","配置UDM基础数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 业务发放概述（云网，带计算）","参考","用户数据发放","数据配置","配置UDM基础数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在UDM上配置用户的开户数据。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '配置5G QoS模板。“HLRSN”由**ADD HLRSN**中定义，在此处引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGQI:
          name: '5QI'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '是否允许抢占低优先级业务的资源'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '是否允许资源被高优先级业务抢占'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '配置5G DNN QoS模板。   * “HLRSN”由**ADD HLRSN**定义，在此处引用。 * “NGCQOSTPLID”由**ADD NGCQOSTPL**定义，在此处引用。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDPDUTYPE:
          name: '其它允许的PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ki_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '配置加载终端鉴权秘钥。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        OPERTYPE:
          name: '操作类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        KIVALUE:
          name: 'KI值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALG:
          name: '鉴权算法类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sub_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '配置终端开户数据。'
          data_source: '已有数据中获取'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: ''
          data_source: '全局规划'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NAM:
          name: '网络接入模式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTCALL:
          name: '缺省呼叫类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TS:
          name: '电信业务'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_amdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '配置AMF签约数据。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供AM签约数据'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_snssai_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '配置切片数据。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认S-NSSAI'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '配置SMF签约数据。'
          data_source: '全局规划'
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否默认DNN'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQoS模板'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: 1
      TPLID: 13
      TPLNAME: '5QI'
      NGQI: 9
      ARPPRILEVEL: 14
      PREEMPTIONCAP: TRUE
      PREEMPTIONVUL: TRUE
      NGQIPRILEVEL: 90
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 153
      TPLNAME: '8-0480-80-5'
      PDUTYPE: IPV4V6
      ALLOWEDPDUTYPE: IPV4&IPV6
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2&SSC_MODE_3
      NGCQOSTPLID: 13
      AMBRUP: 60
      UPUNIT: Mbps
      AMBRDW: 5
      DWUNIT: Mbps
      CHARGE: '0480'
    add_ki_list:
    - HLRSN: '1'
      IMSI: '460020000000001'
      OPERTYPE: ADD
      KIVALUE: '******'
      K4SNO: '1'
      CARDTYPE: USIM
      ALG: MILENAGE
      OPSNO: '1'
      AMFSNO: '1'
    add_sub_list:
    - HLRSN: '1'
      IMSI: '460020000000001'
      ISDN: '86106000001'
      CARDTYPE: USIM
      NAM: BOTH
      DEFAULTCALL: TS11
      TS: TS11&TS21&TS22&TS61&TS62
    mod_amdata_list:
    - IMSI: '460010000000001'
      PROV: TRUE
      AUTHTYPE: 5G-AKA
    add_snssai_list:
    - IMSI: '460010000000001'
      SNSSAI: 1-131313
      DEFAULT: TRUE
    add_smdata_list:
    - IMSI: '460010000000001'
      SNSSAI: 1-131313
      DNN: net
      DEFAULT: TRUE
      DNNQOSTPLID: '153'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置5G QoS模板。

```jinja2
{%- for item in add_ngcqostpl_list -%}
    ADD NGCQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    NGQI={{item.NGQI}},
    ARPPRILEVEL={{item.ARPPRILEVEL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.PREEMPTIONCAP is not none -%}
        PREEMPTIONCAP={{item.PREEMPTIONCAP}},
    {%- endif -%}
    {%- if item.PREEMPTIONVUL is not none -%}
        PREEMPTIONVUL={{item.PREEMPTIONVUL}},
    {%- endif -%}
    {%- if item.NGQIPRILEVEL is not none -%}
        NGQIPRILEVEL={{item.NGQIPRILEVEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置5G DNN QoS模板。

```jinja2
{%- for item in add_dnnqostpl_list -%}
    ADD DNNQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    PDUTYPE={{item.PDUTYPE}},
    SSCMODE={{item.SSCMODE}},
    NGCQOSTPLID={{item.NGCQOSTPLID}},
    AMBRUP={{item.AMBRUP}},
    UPUNIT={{item.UPUNIT}},
    AMBRDW={{item.AMBRDW}},
    DWUNIT={{item.DWUNIT}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.ALLOWEDPDUTYPE is not none -%}
        ALLOWEDPDUTYPE={{item.ALLOWEDPDUTYPE}},
    {%- endif -%}
    {%- if item.ALLOWEDSCCMODE is not none -%}
        ALLOWEDSCCMODE={{item.ALLOWEDSCCMODE}},
    {%- endif -%}
    {%- if item.CHARGE is not none -%}
        CHARGE="{{item.CHARGE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置加载终端鉴权秘钥。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=3 -->
```

### 4 配置终端开户数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_sub_list的变量区（command: ADD SUB） -#}
<!-- MISSING_MACRO: command=ADD SUB list_name=add_sub_list step_id=4 -->
```

### 5 配置AMF签约数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_amdata_list的变量区（command: MOD AMDATA） -#}
<!-- MISSING_MACRO: command=MOD AMDATA list_name=mod_amdata_list step_id=5 -->
```

### 6 配置切片数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_snssai_list的变量区（command: ADD SNSSAI） -#}
<!-- MISSING_MACRO: command=ADD SNSSAI list_name=add_snssai_list step_id=6 -->
```

### 7 配置SMF签约数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=7 -->
```

