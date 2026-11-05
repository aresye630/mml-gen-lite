---
id: ''
name: 配置短消息业务功能
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活SMSF短消息业务的操作过程。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core SMSF解决方案","SMSF功能部署","部署业务特性数据","配置UNC业务特性数据","配置短消息业务功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活SMSF短消息业务的操作过程。

## 必备事项
前提条件

已完成SMSF初始配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ngmmfunc_list:
      type: items
      properties:
        SMSOVERNAS:
          name: '支持通过NAS传短消息'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: '开启AMF支持通过NAS传短消息功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
        GETPEIPLCY:
          name: 'PEI获取策略'
          type: string
          enum:
          - NOGET
          - GETIMEI
          - GETIMEISV
          required: false
          description: ''
          data_source: ''
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
        BALLOW:
          name: '是否允许黑名单用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKFAIL:
          name: '是否允许EIR返回失败时接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKPEITHRESHOLD:
          name: 'PEI检查上限'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CTFLAG:
          name: 'PEI检查超时是否允许接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DISCFAIL:
          name: '是否允许EIR发现失败时接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        EMERGENCYSW:
          name: '是否允许紧急注册用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        GRALLOW:
          name: '是否允许灰名单用户接入'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        PROTTYPE:
          name: '流程类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'INIT_REG-1&MOBL_INTER_REG-1&REG_AFT_INTERHO-1&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-1'
        REDIRECTSW:
          name: '是否支持EIR重定向'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        RETRYSW:
          name: '是否重选EIR'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
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
  examples:
    set_ngmmfunc_list:
    - SMSOVERNAS: SUPPORT
    add_ngpeiplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '123456'
      GETPEIPLCY: GETIMEI
      CHKPEIPLCY: NOCHK
      BALLOW: YES
      CHKFAIL: YES
      CHKPEITHRESHOLD: ''
      CTFLAG: YES
      DISCFAIL: YES
      EMERGENCYSW: YES
      GRALLOW: YES
      PROTTYPE: INIT_REG-1&MOBL_INTER_REG-1&REG_AFT_INTERHO-1&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-1
      REDIRECTSW: YES
      RETRYSW: YES
      PEIACCESS: YES
      IMSI: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置AMF数据

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置AMF支持短消息功能。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.SMSOVERNAS is not none -%}
        SMSOVERNAS={{item.SMSOVERNAS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 （可选）打开获取IMEISV开关。如果需要获取用户设备标识，建议配置为GETIMEISV(获取IMEISV)，这样AMF可直接向UE获取IMEISV，减少信令消耗。

```jinja2
{%- if is_optional_get_imeisv_switch -%}
    {%- for item in add_ngpeiplcy_list -%}
        ADD NGPEIPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETPEIPLCY is not none -%}
            GETPEIPLCY={{item.GETPEIPLCY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
        {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
            {%- if item.CHKPEIPLCY is not none -%}
                CHKPEIPLCY={{item.CHKPEIPLCY}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.BALLOW is not none -%}
                BALLOW={{item.BALLOW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.CHKFAIL is not none -%}
                CHKFAIL={{item.CHKFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.CHKPEITHRESHOLD is not none -%}
                CHKPEITHRESHOLD={{item.CHKPEITHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.CTFLAG is not none -%}
                CTFLAG={{item.CTFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.DISCFAIL is not none -%}
                DISCFAIL={{item.DISCFAIL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.EMERGENCYSW is not none -%}
                EMERGENCYSW={{item.EMERGENCYSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.GRALLOW is not none -%}
                GRALLOW={{item.GRALLOW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：GETPEIPLCY=GETIMEISV/GETIMEI 时可选 --- -#}
        {%- if item.GETPEIPLCY in ['GETIMEISV', 'GETIMEI'] -%}
            {%- if item.PEIACCESS is not none -%}
                PEIACCESS={{item.PEIACCESS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.PROTTYPE is not none -%}
                PROTTYPE={{item.PROTTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.REDIRECTSW is not none -%}
                REDIRECTSW={{item.REDIRECTSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHKPEIPLCY=CHKIMEISV/CHKIMEI 时可选 --- -#}
        {%- if item.CHKPEIPLCY in ['CHKIMEISV', 'CHKIMEI'] -%}
            {%- if item.RETRYSW is not none -%}
                RETRYSW={{item.RETRYSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

