---
id: ''
name: 部署基于位置信息的分流策略控制（AMF）
ne_type: UNC
type: feature
description: 本操作用于指导基于位置信息的分流策略控制特性关于AMF上PRA配置以及UE Location Report功能配置的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223001 基于位置信息的分流策略控制","部署基于位置信息的分流策略控制（AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导基于位置信息的分流策略控制特性关于AMF上PRA配置以及UE Location Report功能配置的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-223001 基于位置信息的分流策略控制和WSFD-106010 基于指定区域的策略控制。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngpra_list:
      type: items
      properties:
        PRAID:
          name: 'PRA标识'
          type: integer
          minimum: 8388608
          maximum: 16777215
          required: true
          description: 'AMF增加PRA标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpramem_list:
      type: items
      properties:
        PRAID:
          name: 'PRA标识'
          type: integer
          minimum: 8388608
          maximum: 16777215
          required: true
          description: 'AMF增加PRA区域列表成员。在为PRA增加区域成员前首先需要通过**ADD NGPRA**配置PRA基本信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCTYPE:
          name: '位置区标识类型'
          type: string
          enum:
          - TAI
          - GNBID
          - NRCELLID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCIDBEGIN:
          name: '小区起始标识'
          type: string
          minLength: 9
          maxLength: 9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCIDEND:
          name: '小区结束标识'
          type: string
          minLength: 9
          maxLength: 9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GNBIDBEGIN:
          name: 'gNodeB起始标识'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GNBIDEND:
          name: 'gNodeB结束标识'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GNBIDLEN:
          name: 'gNodeB标识长度'
          type: integer
          minimum: 22
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACBEGIN:
          name: '跟踪区起始编码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACEND:
          name: '跟踪区结束编码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmfunc_list:
      type: items
      properties:
        SUBLOCRPTSW:
          name: '是否订阅位置上报'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置感兴趣区域订阅失败后的处理策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBLOCRPTPLCY:
          name: '订阅位置上报策略'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBLOCRPTSRC:
          name: '订阅位置上报来源'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngapcmpt_list:
      type: items
      properties:
        AOILIST:
          name: '是否携带感兴趣区域列表'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '设置NGAP兼容性参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ngpra_list:
    - PRAID: 8388616
      DESC: 'for EastLake Campus'
    add_ngpramem_list:
    - PRAID: 8388616
      LOCTYPE: NRCELLID
      MCC: '123'
      MNC: '45'
      NGCIDBEGIN: '000900001'
      NGCIDEND: '000900003'
      GNBIDBEGIN: ''
      GNBIDEND: ''
      GNBIDLEN: ''
      TACBEGIN: ''
      TACEND: ''
    set_ngmmfunc_list:
    - SUBLOCRPTSW: YES
      SUBLOCRPTPLCY: ''
      SUBLOCRPTSRC: ''
    set_ngapcmpt_list:
    - AOILIST: NO
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //AMF配置PRA区域（校园）基本信息。

```jinja2
{%- for item in add_ngpra_list -%}
    ADD NGPRA:
    {#- --- 必选参数 --- -#}
    PRAID={{item.PRAID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 //AMF在指定的PRA区域配置位置信息。

```jinja2
{%- for item in add_ngpramem_list -%}
    ADD NGPRAMEM:
    {#- --- 必选参数 --- -#}
    PRAID={{item.PRAID}},
    LOCTYPE={{item.LOCTYPE}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOCTYPE=NRCELLID 时必选 --- -#}
    {%- if item.LOCTYPE == 'NRCELLID' -%}
        NGCIDBEGIN="{{item.NGCIDBEGIN}}",
    {%- endif -%}
    {#- --- 条件必选：LOCTYPE=GNBID 时必选 --- -#}
    {%- if item.LOCTYPE == 'GNBID' -%}
        GNBIDBEGIN={{item.GNBIDBEGIN}},
    {%- endif -%}
    {#- --- 条件必选：LOCTYPE=GNBID 时必选 --- -#}
    {%- if item.LOCTYPE == 'GNBID' -%}
        GNBIDLEN={{item.GNBIDLEN}},
    {%- endif -%}
    {#- --- 条件必选：LOCTYPE=TAI 时必选 --- -#}
    {%- if item.LOCTYPE == 'TAI' -%}
        TACBEGIN="{{item.TACBEGIN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=NRCELLID 时可选 --- -#}
    {%- if item.LOCTYPE == 'NRCELLID' -%}
        {%- if item.NGCIDEND is not none -%}
            NGCIDEND="{{item.NGCIDEND}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOCTYPE=GNBID 时可选 --- -#}
    {%- if item.LOCTYPE == 'GNBID' -%}
        {%- if item.GNBIDEND is not none -%}
            GNBIDEND={{item.GNBIDEND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOCTYPE=TAI 时可选 --- -#}
    {%- if item.LOCTYPE == 'TAI' -%}
        {%- if item.TACEND is not none -%}
            TACEND="{{item.TACEND}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //配置感兴趣区域订阅失败后的处理策略。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.SUBLOCRPTSW is not none -%}
        SUBLOCRPTSW={{item.SUBLOCRPTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBLOCRPTSW=YES 时可选 --- -#}
    {%- if item.SUBLOCRPTSW == 'YES' -%}
        {%- if item.SUBLOCRPTPLCY is not none -%}
            SUBLOCRPTPLCY={{item.SUBLOCRPTPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBLOCRPTSW=YES 时可选 --- -#}
    {%- if item.SUBLOCRPTSW == 'YES' -%}
        {%- if item.SUBLOCRPTSRC is not none -%}
            SUBLOCRPTSRC={{item.SUBLOCRPTSRC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //设置NGAP兼容性参数。

```jinja2
{%- for item in set_ngapcmpt_list -%}
    SET NGAPCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.AOILIST is not none -%}
        AOILIST={{item.AOILIST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

