---
id: GWFD-021201
name: 激活QoS与流量管理（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中控制EPS QoS各项功能的启动和调整的操作过程。  在E-UTRAN网络和GERAN/UTRAN网络互操作过程中，UEG支持EPS（Evolved Packet System） QoS参数和Pre-Rel-8 QoS参数之间的映射，实现网络间的切换和重选。UEG支持承载级别、APN级别、终端级别的EPS QoS控制。  QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021200 QoS与流量管理","GWFD-021201 QoS与流量管理","激活QoS与流量管理（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中控制EPS QoS各项功能的启动和调整的操作过程。在E-UTRAN网络和GERAN/UTRAN网络互操作过程中，UEG支持EPS（Evolved Packet System） QoS参数和Pre-Rel-8 QoS参数之间的映射，实现网络间的切换和重选。UEG支持承载级别、APN级别、终端级别的EPS QoS控制。QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_r8qosmap_list:
      type: items
      properties:
        QCI:
          name: 'QoS级别标识'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: '配置EPS QoS参数到Pre-Rel-8 QoS参数映射。'
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
    set_compatibility_list:
      type: items
      properties:
        HARP:
          name: 'H值'
          type: integer
          minimum: 1
          maximum: 13
          required: false
          description: '配置QoS兼容性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MARP:
          name: 'M值'
          type: integer
          minimum: 2
          maximum: 14
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSQOSEXT2:
          name: '发送EPS QoS Extended-2'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_r8qosmap_list:
    - QCI: 1
      TC: CC
      MAXSDU: 150
      DO: ORDER
      DESDU: NOT_DETECT
      RBER: E_RESIDUAL_BIT_ERR_RATIO_1
      SDUER: SDUER4
      TD: 10
      THPRI: THPRI1
    set_compatibility_list:
    - HARP: 5
      MARP: 10
      EPSQOSEXT2: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加EPS QoS参数到Pre-Rel-8 QoS参数映射规则。

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
    {%- if item.DESDU is not none -%}
        DESDU={{item.DESDU}},
    {%- endif -%}
    {%- if item.RBER is not none -%}
        RBER={{item.RBER}},
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

### 3 设置QoS兼容性（EPS ARP、Pre-Rel-8 ARP转换参数和EPS QoS Extended-2信元控制参数等）。

```jinja2
{%- for item in set_compatibility_list -%}
    SET COMPATIBILITY:
    {#- --- 可选参数 --- -#}
    {%- if item.HARP is not none -%}
        HARP={{item.HARP}},
    {%- endif -%}
    {%- if item.MARP is not none -%}
        MARP={{item.MARP}},
    {%- endif -%}
    {%- if item.EPSQOSEXT2 is not none -%}
        EPSQOSEXT2={{item.EPSQOSEXT2}},
    {%- endif -%}
    ;
{%- endfor -%}
```

