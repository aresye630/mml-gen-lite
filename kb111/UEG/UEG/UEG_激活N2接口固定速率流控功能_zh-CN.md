---
id: GWFD-021404
name: 激活N2接口固定速率流控功能
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活N2接口固定速率流控功能的操作过程。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021400 可靠性功能","GWFD-021404 周边网元过载保护","N2接口固定速率流控功能","激活N2接口固定速率流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活N2接口固定速率流控功能的操作过程。适用于AMF。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_n2fixedfcbymsg_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - NGSETUP
          - PAGING
          - REGISTER
          - SERVICEREQUEST
          - PATHSWITCH
          - WPWR
          - PCR
          - PRI
          - PFI
          required: true
          description: '设置N2接口上指定消息类型固定速率流控信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - On
          - Off
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '（可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftpara_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '（可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明：  此处阈值为举例值，请根据网络具体情况进行阈值设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_n2fixedfcbymsg_list:
    - MSGTYPE: PAGING
      FCSWITCH: On
      THRESHOLD: 4000
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 14
      VALUE: VALUE_0
      POSITION: 30
    set_amfsoftpara_list:
    - DT: Dw
      DWORDNUM: 28
      DWORDVALUE: 80000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置N2接口指定消息类型固定流控速率。

```jinja2
{%- for item in set_n2fixedfcbymsg_list -%}
    SET N2FIXEDFCBYMSG:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=On 时可选 --- -#}
    {%- if item.FCSWITCH == 'On' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

```jinja2
{%- if is_optional_enable_paging_fc -%}
    {%- for item in set_amfsoftparaofbit_list -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

```jinja2
{%- if is_optional_set_paging_fc_threshold -%}
    {%- for item in set_amfsoftpara_list -%}
        SET AMFSOFTPARA:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

