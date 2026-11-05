---
id: ''
name: 激活基于IMSI号段的QoS控制（适用于SMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于IMSI号段的QoS控制特性的操作过程。  SMF能够按IMSI号段对特定用户群的QoS进行单独配置，从而实现灵活的QoS控制策略。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-105104 基于IMSI号段的QoS控制","WSFD-105104 基于IMSI号段的QoS控制（适用于SMF）","激活基于IMSI号段的QoS控制（适用于SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于IMSI号段的QoS控制特性的操作过程。SMF能够按IMSI号段对特定用户群的QoS进行单独配置，从而实现灵活的QoS控制策略。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-105104 基于IMSI号段的QoS控制（适用于SMF）。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    add_qoscapwhiteapns_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加不受SMFQOSCAP配置控制的APN白名单列表。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - VISITING
          - ROAMING
          - HOME_USER
          - ALL_USER
          - HOME_NOLOCAL_USER
          required: true
          description: ''
          data_source: ''
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
    add_smfqoscap_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - VISITING
          - ROAMING
          - HOME_USER
          - ALL_USER
          - HOME_NOLOCAL_USER
          required: true
          description: '添加QosFlow QoS限制的配置。'
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
        QOSIDTYPE:
          name: 'QoS资源类型'
          type: string
          enum:
          - NONGBR
          - GBR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行APN AMBR(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行APN AMBR(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QI:
          name: '标准5QI'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI的优先级别'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPRL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPCI:
          name: 'ARP的抢占能力'
          type: string
          enum:
          - MAY_PREEMPT
          - NOT_PREEMPT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPVI:
          name: 'ARP的被抢占能力'
          type: string
          enum:
          - PREEMPTABLE
          - NOT_PREEMPTABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSACTION:
          name: 'QoS协商动作'
          type: string
          enum:
          - ACCEPT
          - RESTRICT
          - REPLACE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ACCEPT
        GFBRDL:
          name: '下行保证速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRUL:
          name: '上行保证速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRDL:
          name: '下行最大速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRUL:
          name: '上行最大速率(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 65000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qoscapby5qi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - IMSI_PREFIX
          - VISITING
          - ROAMING
          - HOME_USER
          - ALL_USER
          - HOME_NOLOCAL_USER
          required: true
          description: '当需要基于5QI粒度进一步限制QoS时，添加基于5QI的QosFlow QoS限制配置。'
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
        QOS5QI:
          name: '标准5QI'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI的优先级别'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPRL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPCI:
          name: 'ARP的抢占能力'
          type: string
          enum:
          - MAY_PREEMPT
          - NOT_PREEMPT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPVI:
          name: 'ARP的被抢占能力'
          type: string
          enum:
          - PREEMPTABLE
          - NOT_PREEMPTABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2QCBISM01'
      SWITCH: ENABLE
    add_qoscapwhiteapns_list:
    - APN: 'ims'
      SUBRANGE: ALL_USER
      IMSIPRE: ''
    add_smfqoscap_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '3080107000'
      QOSIDTYPE: NONGBR
      AMBRUL: 20000000
      AMBRDL: 16600000
      QOS5QI: 9
      QOS5QIPL: 10
      ARPPRL: 5
      ARPPCI: MAY_PREEMPT
      ARPPVI: NOT_PREEMPTABLE
      QOSACTION: RESTRICT
      GFBRDL: ''
      GFBRUL: ''
      MFBRDL: ''
      MFBRUL: ''
    add_qoscapby5qi_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '3080107000'
      QOS5QI: 9
      QOS5QIPL: 10
      ARPPRL: 5
      ARPPCI: MAY_PREEMPT
      ARPPVI: NOT_PREEMPTABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 （可选）针对使用语音业务的用户，如果这些用户不受基于IMSI号段的QoS控制，可将其加入白名单。

```jinja2
{%- if is_optional_user_whitelist -%}
    {%- for item in add_qoscapwhiteapns_list -%}
        ADD QOSCAPWHITEAPNS:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 添加QosFlow QoS限制的配置。

```jinja2
{%- for item in add_smfqoscap_list -%}
    ADD SMFQOSCAP:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    QOSIDTYPE={{item.QOSIDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.QOS5QI is not none -%}
        QOS5QI={{item.QOS5QI}},
    {%- endif -%}
    {%- if item.QOS5QIPL is not none -%}
        QOS5QIPL={{item.QOS5QIPL}},
    {%- endif -%}
    {%- if item.ARPPRL is not none -%}
        ARPPRL={{item.ARPPRL}},
    {%- endif -%}
    {%- if item.ARPPCI is not none -%}
        ARPPCI={{item.ARPPCI}},
    {%- endif -%}
    {%- if item.ARPPVI is not none -%}
        ARPPVI={{item.ARPPVI}},
    {%- endif -%}
    {%- if item.QOSACTION is not none -%}
        QOSACTION={{item.QOSACTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOSIDTYPE=NONGBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'NONGBR' -%}
        {%- if item.AMBRUL is not none -%}
            AMBRUL={{item.AMBRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSIDTYPE=NONGBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'NONGBR' -%}
        {%- if item.AMBRDL is not none -%}
            AMBRDL={{item.AMBRDL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSIDTYPE=GBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'GBR' -%}
        {%- if item.GFBRDL is not none -%}
            GFBRDL={{item.GFBRDL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSIDTYPE=GBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'GBR' -%}
        {%- if item.GFBRUL is not none -%}
            GFBRUL={{item.GFBRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSIDTYPE=GBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'GBR' -%}
        {%- if item.MFBRDL is not none -%}
            MFBRDL={{item.MFBRDL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOSIDTYPE=GBR 时可选 --- -#}
    {%- if item.QOSIDTYPE == 'GBR' -%}
        {%- if item.MFBRUL is not none -%}
            MFBRUL={{item.MFBRUL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**（可选）当需要基于5QI粒度进一步限制QoS时，添加基于5QI的QosFlow QoS限制配置。

```jinja2
{%- if is_optional_qos_5qi_limit -%}
    {%- for item in add_qoscapby5qi_list -%}
        ADD QOSCAPBY5QI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        QOS5QI={{item.QOS5QI}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS5QIPL is not none -%}
            QOS5QIPL={{item.QOS5QIPL}},
        {%- endif -%}
        {%- if item.ARPPRL is not none -%}
            ARPPRL={{item.ARPPRL}},
        {%- endif -%}
        {%- if item.ARPPCI is not none -%}
            ARPPCI={{item.ARPPCI}},
        {%- endif -%}
        {%- if item.ARPPVI is not none -%}
            ARPPVI={{item.ARPPVI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

