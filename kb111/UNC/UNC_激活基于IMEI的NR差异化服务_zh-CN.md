---
id: ''
name: 激活基于IMEI的NR差异化服务
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于IMEI的NR差异化服务特性的操作过程。  本特性是指AMF在获取终端IMEISV后通过N2接口将IMEISV以“Masked IMEISV”信元形式发送给gNodeB，便于gNodeB基于终端的类型、软件版本进行无线侧网络质量分析，从而实现对不同终端的差异化控制。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","差异化服务管理","WSFD-011311 基于IMEI的NR差异化服务","激活基于IMEI的NR差异化服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于IMEI的NR差异化服务特性的操作过程。本特性是指AMF在获取终端IMEISV后通过N2接口将IMEISV以“Masked IMEISV”信元形式发送给gNodeB，便于gNodeB基于终端的类型、软件版本进行无线侧网络质量分析，从而实现对不同终端的差异化控制。适用于AMF。

## 必备事项
前提条件

请仔细阅读WSFD-011311 基于IMEI的NR差异化服务特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngpeiplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: 'AMF获取终端IMEISV。  说明：  推荐选用获取所有用户的IMEISV，即“用户范围”设置为“ALL\_USER”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPEIPLCY:
          name: 'PEI获取策略'
          type: string
          enum:
          - NOGET
          - GETIMEI
          - GETIMEISV
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NOGET
        CHKPEIPLCY:
          name: 'PEI检查策略'
          type: string
          enum:
          - NOCHK
          - CHKIMEI
          - CHKIMEISV
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOCHK
        PEIACCESS:
          name: 'PEI获取失败是否允许接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
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
    set_ngapcmpt_list:
      type: items
      properties:
        MSKIMEISV:
          name: '是否携带Masked IMEISV信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: 'AMF给gNodeB下发的Initial Context Setup Request和Handover Request消息中携带Masked IMEISV信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMEISVCODING:
          name: 'IMEISV信元编码方式'
          type: string
          enum:
          - REVERSE_ORDER
          - FORWARD_ORDER
          required: false
          description: '当AMF对接异厂商gNodeB时，可通过该参数设置“Masked IMEISV”信元的编码方式，使AMF与gNodeB的该信元编码方式一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ngpeiplcy_list:
    - SUBRANGE: ALL_USER
      GETPEIPLCY: GETIMEISV
      CHKPEIPLCY: NOCHK
      PEIACCESS: YES
      IMSI: ''
      IMSIPRE: ''
    set_ngapcmpt_list:
    - MSKIMEISV: YES
      IMEISVCODING: FORWARD_ORDER
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 针对一定范围的用户，开启AMF获取终端IMEISV功能。

```jinja2
{%- for item in add_ngpeiplcy_list -%}
    ADD NGPEIPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GETPEIPLCY is not none -%}
        GETPEIPLCY={{item.GETPEIPLCY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
    {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
        {%- if item.CHKPEIPLCY is not none -%}
            CHKPEIPLCY={{item.CHKPEIPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
    {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
        {%- if item.PEIACCESS is not none -%}
            PEIACCESS={{item.PEIACCESS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置AMF在Initial Context Setup Request和Handover Request消息中携带Masked IMEISV。

```jinja2
{%- for item in set_ngapcmpt_list -%}
    SET NGAPCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.MSKIMEISV is not none -%}
        MSKIMEISV={{item.MSKIMEISV}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MSKIMEISV=YES 时可选 --- -#}
    {%- if item.MSKIMEISV == 'YES' -%}
        {%- if item.IMEISVCODING is not none -%}
            IMEISVCODING={{item.IMEISVCODING}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

