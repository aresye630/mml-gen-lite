---
id: GWFD-026002
name: 激活支持4G到5G多切片时的重选
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持4G到5G多切片时的重选的操作过程。  空闲态UE移动出4G基站覆盖区域进入5G基站的覆盖区域，执行小区重选，发起移动注册更新流程，进行4G到5G的重选。  UE在4G网络时，不需要切片信息，4G网络一张网络满足所有应用；UE从4G移动到5G之后，在5G组网场景下，则需要通过对切片信息的判断，将UE接入不同的切片网络，分别为不同业务场景提供服务。比如当存在2B、2C两个切片网络，需要区分处理，让2B的用户接入到2B的切片网络，2C的用户接入到2C的切片网络。  本特性通过互操作过程中的切片信息，判断用户从4G网络重选到5G网络后，AMF是否需要重分配，让支持对应切片的网元为UE提供服务，最大化的保证用户在4G到5G多切片重选时的业务连续性。  适用于AMF、SMF、NSSF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026002 支持4G到5G多切片时的重选","激活支持4G到5G多切片时的重选"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持4G到5G多切片时的重选的操作过程。空闲态UE移动出4G基站覆盖区域进入5G基站的覆盖区域，执行小区重选，发起移动注册更新流程，进行4G到5G的重选。UE在4G网络时，不需要切片信息，4G网络一张网络满足所有应用；UE从4G移动到5G之后，在5G组网场景下，则需要通过对切片信息的判断，将UE接入不同的切片网络，分别为不同业务场景提供服务。比如当存在2B、2C两个切片网络，需要区分处理，让2B的用户接入到2B的切片网络，2C的用户接入到2C的切片网络。本特性通过互操作过程中的切片信息，判断用户从4G网络重选到5G网络后，AMF是否需要重分配，让支持对应切片的网元为UE提供服务，最大化的保证用户在4G到5G多切片重选时的业务连续性。适用于AMF、SMF、NSSF

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-026002 支持4G到5G多切片时的重选特性概述。
* 已经打开GWFD-020910 LTE与5G SA网络间重选特性的license。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        REPSNSSAI:
          name: '是否在EPS获取签约的NSSAI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '5G用户在4G网络建立PDN连接时，控制SMF是否向UDM获取签约的切片和DNN。'
          data_source: '本端规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFIWKIND:
          name: 'EPS互操作默认切片指示'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '指定PDN连接建立流程中根据DNN为用户分配的互操作默认切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smfselplcy_list:
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
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISMFSW:
          name: '是否支持I-SMF选择'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        TAISW:
          name: '是否使用TAI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSISW:
          name: '是否使用用户IMSI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        MSISDNSW:
          name: '是否使用MSISDN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        RETRYSW:
          name: '是否重选SMF'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        PREFERSMFSW:
          name: '优选同一SMF开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        DNNFMT:
          name: 'DNN格式'
          type: string
          enum:
          - DEFAULT
          - NI
          - NIANDOI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        SMFLIST:
          name: '签约信息中的SMF选择策略'
          type: string
          enum:
          - DEFAULT
          - INSTANCEID_ONLY
          - INSTANCEID_PREF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        IWKNSSW:
          name: 'EPS与5GS互操作专用切片选择策略'
          type: string
          enum:
          - SUB
          - CFG
          required: false
          description: '控制AMF发现I-SMF时使用的切片来源。'
          data_source: '全网规划'
          pattern: ''
          default: SUB
        IWKSST:
          name: 'EPS与5GS互操作专用切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '指定切片类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKSD:
          name: 'EPS与5GS互操作专用切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: '设置专用切片细分标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISMFRESEL:
          name: 'I-SMF重选'
          type: string
          enum:
          - DEFAULT
          - PROTOCOL
          required: false
          description: '控制当互操作专用切片和会话切片不一致时，是否重选I-SMF。'
          data_source: '全网规划'
          pattern: ''
          default: DEFAULT
  examples:
    set_smffunc_list:
    - REPSNSSAI: NO
    add_nsdnn_list:
    - NSIDX: 0
      DNN: '123.com'
      DEFIWKIND: YES
    add_smfselplcy_list:
    - SUBRANGE: ALL_USER
      ISMFSW: NO
      TAISW: NO
      IMSISW: NO
      MSISDNSW: NO
      RETRYSW: NO
      PREFERSMFSW: NO
      DNNFMT: DEFAULT
      SMFLIST: DEFAULT
      IWKNSSW: CFG
      IWKSST: 1
      IWKSD: 'FFFFFF'
      ISMFRESEL: PROTOCOL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。-SMF

### 2 5G用户在EPS网络建立PDN连接时，控制SMF是否向UDM获取签约的切片和DNN。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.REPSNSSAI is not none -%}
        REPSNSSAI={{item.REPSNSSAI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 指定PDN连接建立流程中根据DNN为用户分配的互操作默认切片。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFIWKIND is not none -%}
        DEFIWKIND={{item.DEFIWKIND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 进入“MML命令行-UEG”窗口。-AMF

### 5 AMF支持配置互操作专用切片发现I-SMF。

```jinja2
{%- for item in add_smfselplcy_list -%}
    ADD SMFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISMFSW is not none -%}
        ISMFSW={{item.ISMFSW}},
    {%- endif -%}
    {%- if item.IMSISW is not none -%}
        IMSISW={{item.IMSISW}},
    {%- endif -%}
    {%- if item.MSISDNSW is not none -%}
        MSISDNSW={{item.MSISDNSW}},
    {%- endif -%}
    {%- if item.RETRYSW is not none -%}
        RETRYSW={{item.RETRYSW}},
    {%- endif -%}
    {%- if item.PREFERSMFSW is not none -%}
        PREFERSMFSW={{item.PREFERSMFSW}},
    {%- endif -%}
    {%- if item.DNNFMT is not none -%}
        DNNFMT={{item.DNNFMT}},
    {%- endif -%}
    {%- if item.SMFLIST is not none -%}
        SMFLIST={{item.SMFLIST}},
    {%- endif -%}
    {%- if item.IWKNSSW is not none -%}
        IWKNSSW={{item.IWKNSSW}},
    {%- endif -%}
    {%- if item.ISMFRESEL is not none -%}
        ISMFRESEL={{item.ISMFRESEL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IWKNSSW=CFG 时必选 --- -#}
    {%- if item.IWKNSSW == 'CFG' -%}
        IWKSST={{item.IWKSST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ISMFSW=NO 时可选 --- -#}
    {%- if item.ISMFSW == 'NO' -%}
        {%- if item.TAISW is not none -%}
            TAISW={{item.TAISW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IWKNSSW=CFG 时可选 --- -#}
    {%- if item.IWKNSSW == 'CFG' -%}
        {%- if item.IWKSD is not none -%}
            IWKSD="{{item.IWKSD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

