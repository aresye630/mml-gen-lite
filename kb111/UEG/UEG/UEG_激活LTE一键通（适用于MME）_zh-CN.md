---
id: GWFD-025602
name: 激活LTE一键通（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活LTE一键通特性的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-025600 Push to Talk","GWFD-025602 LTE一键通（适用于MME）","激活LTE一键通（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活LTE一键通特性的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025602 LTE一键通特性概述（适用于MME）。
* 已完成加载License。
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
    add_apnpagingplcy_list:
      type: items
      properties:
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: 'PTT业务APN及优先级'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PAGINGPRIORITY:
          name: '寻呼优先级'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 7
    set_r8qosmap_list:
      type: items
      properties:
        QCI:
          name: 'QoS级别标识'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: 'PTT业务QoS参数到Pre-R8 QoS参数映射'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TC:
          name: '流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU:
          name: '最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO:
          name: '发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER:
          name: '保留BER'
          type: string
          enum:
          - E_RESIDUAL_BIT_ERR_RATIO_1
          - E_RESIDUAL_BIT_ERR_RATIO_2
          - E_RESIDUAL_BIT_ERR_RATIO_3
          - E_RESIDUAL_BIT_ERR_RATIO_4
          - E_RESIDUAL_BIT_ERR_RATIO_5
          - E_RESIDUAL_BIT_ERR_RATIO_6
          - E_RESIDUAL_BIT_ERR_RATIO_7
          - E_RESIDUAL_BIT_ERR_RATIO_8
          - E_RESIDUAL_BIT_ERR_RATIO_9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU:
          name: '发送错误SDU'
          type: string
          enum:
          - ERR_SDU_DELIVERED
          - ERR_SDU_NOT_DELIVERED
          - NOT_DETECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER:
          name: 'SDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD:
          name: '传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI:
          name: '发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qciconv_list:
      type: items
      properties:
        QCIEXT:
          name: '扩展QCI基准值'
          type: integer
          minimum: 10
          maximum: 254
          required: true
          description: 'PTT业务QCI转换为标准QCI'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCISTEP:
          name: '扩展QCI范围'
          type: integer
          minimum: 0
          maximum: 244
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCISTD:
          name: '标准QCI值'
          type: integer
          minimum: 1
          maximum: 9
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_compatibility_list:
      type: items
      properties:
        GTPV2EXTQCI:
          name: 'GTPV2通道发送扩展QCI'
          type: string
          enum:
          - NOT_SUPPORT
          - SAMEPLMN_SUPPORT
          - SUPPORT
          required: false
          description: 'MME间移动时用户的QCI传递策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2QPPT01'
      SWITCH: ENABLE
    add_apnpagingplcy_list:
    - APNNI: 'huawei.com'
      PAGINGPRIORITY: 7
    set_r8qosmap_list:
    - QCI: 65
      TC: CC
      MAXSDU: 150
      DO: NORDER
      RBER: E_RESIDUAL_BIT_ERR_RATIO_7
      DESDU: NOT_DETECT
      SDUER: SDUER1
      TD: 10
      THPRI: THPRI1
    add_qciconv_list:
    - QCIEXT: 65
      QCISTEP: 1
      QCISTD: 1
    set_compatibility_list:
    - GTPV2EXTQCI: SUPPORT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开LTE一键通功能特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置PTT APN以及PTT业务寻呼优先级。

```jinja2
{%- for item in add_apnpagingplcy_list -%}
    ADD APNPAGINGPLCY:
    {#- --- 必选参数 --- -#}
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PAGINGPRIORITY is not none -%}
        PAGINGPRIORITY={{item.PAGINGPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加PTT业务QoS参数到Pre-R8 QoS参数映射规则。

```jinja2
{%- for item in set_r8qosmap_list -%}
    SET R8QOSMAP:
    {#- --- 必选参数 --- -#}
    QCI={{item.QCI}},
    {#- --- 可选参数 --- -#}
    {%- if item.TC is not none -%}
        TC={{item.TC}},
    {%- endif -%}
    {%- if item.MAXSDU is not none -%}
        MAXSDU={{item.MAXSDU}},
    {%- endif -%}
    {%- if item.DO is not none -%}
        DO={{item.DO}},
    {%- endif -%}
    {%- if item.RBER is not none -%}
        RBER={{item.RBER}},
    {%- endif -%}
    {%- if item.DESDU is not none -%}
        DESDU={{item.DESDU}},
    {%- endif -%}
    {%- if item.SDUER is not none -%}
        SDUER={{item.SDUER}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TC=CC/SC 时可选 --- -#}
    {%- if item.TC in ['CC', 'SC'] -%}
        {%- if item.TD is not none -%}
            TD={{item.TD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TC=IC 时可选 --- -#}
    {%- if item.TC == 'IC' -%}
        {%- if item.THPRI is not none -%}
            THPRI={{item.THPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置PTT业务QCI和标准QCI的映射规则。

```jinja2
{%- for item in add_qciconv_list -%}
    ADD QCICONV:
    {#- --- 必选参数 --- -#}
    QCIEXT={{item.QCIEXT}},
    QCISTD={{item.QCISTD}},
    {#- --- 可选参数 --- -#}
    {%- if item.QCISTEP is not none -%}
        QCISTEP={{item.QCISTEP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置MME间移动时用户的QCI传递策略。

```jinja2
{%- for item in set_compatibility_list -%}
    SET COMPATIBILITY:
    {#- --- 可选参数 --- -#}
    {%- if item.GTPV2EXTQCI is not none -%}
        GTPV2EXTQCI={{item.GTPV2EXTQCI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

