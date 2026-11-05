---
id: GWFD-021102
name: 激活漫游控制特性(适用于SGSN/MME)
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活漫游控制特性的操作过程。  漫游控制，是指UEG提供互联PLMN表的配置，只有用户的归属PLMN属于互联PLMN表才能够接入本UEG。漫游控制特性使网络具有限制用户移动范围和业务访问的能力。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021100 移动性管理","GWFD-021102 漫游控制","激活漫游控制特性(适用于SGSN/MME)"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021100 移动性管理","GWFD-021102 漫游控制","激活漫游控制特性(适用于SGSN/MME)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活漫游控制特性的操作过程。漫游控制，是指UEG提供互联PLMN表的配置，只有用户的归属PLMN属于互联PLMN表才能够接入本UEG。漫游控制特性使网络具有限制用户移动范围和业务访问的能力。适用于SGSN、MME。

## 必备事项
前提条件

请仔细阅读GWFD-021102 漫游控制特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '互联的PLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMS:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMSCT:
          name: '纠正后的短消息中心'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MATCHIMSI:
          name: '匹配IMSI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        LCS:
          name: '是否允许LCS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        COUNTRYORAREANAME:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        EXCLUSIVEPLMN:
          name: '专属互连PLMN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
    set_chgplmnchar_list:
      type: items
      properties:
        PLMN:
          name: 'PLMN类型'
          type: string
          enum:
          - HPLMN
          - VPLMN
          required: true
          description: '漫游PLMN用户的计费属性参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LCSNIP:
          name: '生成LCS-NI-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MP:
          name: '生成M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: '生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMOP:
          name: '生成S-SMO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMTP:
          name: '生成S-SMT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMOP:
          name: '生成LCS-MO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMTP:
          name: '生成LCS-MT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_connectplmn_list:
    - MCC: '460'
      MNC: '00'
      CC: '86'
      SMS: YES
      SMSCR: YES
      SMSCT: '861395678956778'
      MATCHIMSI: '1234'
      NOID: 3
      MAXSMNUM: 2
      LCS: YES
      S5S8TYPE: GTP
      COUNTRYORAREANAME: 'noname'
      EXCLUSIVEPLMN: NO
      SM: YES
    set_chgplmnchar_list:
    - PLMN: VPLMN
      LCSNIP: NO
      MP: YES
      SP: YES
      SMOP: YES
      SMTP: YES
      LCSMOP: YES
      LCSMTP: YES
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加互联的PLMN，并配置允许的业务。

```jinja2
{%- for item in add_connectplmn_list -%}
    ADD CONNECTPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.MATCHIMSI is not none -%}
        MATCHIMSI="{{item.MATCHIMSI}}",
    {%- endif -%}
    {%- if item.COUNTRYORAREANAME is not none -%}
        COUNTRYORAREANAME="{{item.COUNTRYORAREANAME}}",
    {%- endif -%}
    {%- if item.EXCLUSIVEPLMN is not none -%}
        EXCLUSIVEPLMN={{item.EXCLUSIVEPLMN}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.LCS is not none -%}
        LCS={{item.LCS}},
    {%- endif -%}
    {%- if item.NOID is not none -%}
        NOID={{item.NOID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SMSCR=YES 时必选 --- -#}
    {%- if item.SMSCR == 'YES' -%}
        SMSCT="{{item.SMSCT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置漫游PLMN用户的计费属性参数。

```jinja2
{%- for item in set_chgplmnchar_list -%}
    SET CHGPLMNCHAR:
    {#- --- 必选参数 --- -#}
    PLMN={{item.PLMN}},
    {#- --- 可选参数 --- -#}
    {%- if item.LCSNIP is not none -%}
        LCSNIP={{item.LCSNIP}},
    {%- endif -%}
    {%- if item.SP is not none -%}
        SP={{item.SP}},
    {%- endif -%}
    {%- if item.SMOP is not none -%}
        SMOP={{item.SMOP}},
    {%- endif -%}
    {%- if item.SMTP is not none -%}
        SMTP={{item.SMTP}},
    {%- endif -%}
    {%- if item.LCSMOP is not none -%}
        LCSMOP={{item.LCSMOP}},
    {%- endif -%}
    {%- if item.MP is not none -%}
        MP={{item.MP}},
    {%- endif -%}
    {%- if item.LCSMTP is not none -%}
        LCSMTP={{item.LCSMTP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“PLMN”（PLMN类型）选择“VPLMN”（拜访PLMN）。

