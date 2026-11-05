---
id: GWFD-022903
name: 激活IPv4v6双栈接入特性（适用于SGSN/MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。  UEG支持创建IPv4v6双栈，通过IPv4v6地址为UE提供业务，使UE可以用IPv4v6地址进行数据传输。  适用于SGSN/MME。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-022900 IPV6基本功能","GWFD-022903 IPv4v6双栈接入","激活IPv4v6双栈接入特性（适用于SGSN/MME）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022903 IPv4v6双栈接入","IPv4v6双栈接入（2G/3G/4G）","激活IPv4v6双栈接入特性（适用于SGSN/MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活IPv4v6双栈接入特性的操作过程。UEG支持创建IPv4v6双栈，通过IPv4v6地址为UE提供业务，使UE可以用IPv4v6地址进行数据传输。适用于SGSN/MME。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-022903 IPv4v6双栈接入特性概述（适用于2G/3G/4G）。
* 完成加载License。
* 支持IPv4v6的用户已经接入到网络。
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
    set_smfunc_list:
      type: items
      properties:
        DUALFLAG:
          name: 'IPv4v6双栈'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '会话管理扩展功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_smsubdata_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_USER
          required: true
          description: '签约数据纠正参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TYPE:
          name: '匹配条件'
          type: string
          enum:
          - Context_ID
          - SUBSCRIBED_PARAMETER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNIRANGE:
          name: '签约APNNI范围'
          type: string
          enum:
          - APNNI_ALL
          - APNNI_SPECIAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: '签约PDP/PDN类型'
          type: string
          enum:
          - ALL_PDP_TYPE
          - IPV4
          - IPV4/IPV6
          - IPV4V6
          - IPV6
          - PPP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4PDPADDRTYPE:
          name: '签约IPv4 PDP/PDN地址分配类型'
          type: string
          enum:
          - ALLOCATION_IPV4PDP_DYNAMIC
          - ALL_STATIC_IPV4PDP_ADDR
          - SPECIAL_STATIC_IPV4PDP_ADDR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CORRECTAPNNI:
          name: '修改签约APNNI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        NEWPDPTYPE:
          name: '新的签约PDP类型'
          type: string
          enum:
          - IPV4
          - IPV4/IPV6
          - IPV4V6
          - IPV6
          - NOT_MODIFY
          - PPP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEWIPV4PDPADDRTYPE:
          name: '新的签约IPv4 PDP/PDN地址分配类型'
          type: string
          enum:
          - DYNAMIC
          - STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEWIPV6PDPADDRTYPE:
          name: '新的签约IPv6 PDP/PDN地址分配类型'
          type: string
          enum:
          - DYNAMIC
          - STATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gtpccmpt_list:
      type: items
      properties:
        MSGCLS:
          name: '消息分类'
          type: string
          enum:
          - MM
          - PM
          - TM
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CREATE_PDP_CONTEXT_REQUEST
          - DELETE_PDP_CONTEXT_REQUEST
          - DELETE_PDP_CONTEXT_RESPONSE
          - UPDATE_PDP_CONTEXT_REQUEST
          - UPDATE_PDP_CONTEXT_RESPONSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRTPDPREQ:
          name: 'Create PDP Context Request信元类型'
          type: string
          enum:
          - COMMON_FLAGS
          - UPSELIND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPDPDPREQ:
          name: 'Update PDP Context Request信元类型'
          type: string
          enum:
          - COMMON_FLAGS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMFLG:
          name: '是否支持Common Flags信元'
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
    set_licenseswitch_list:
    - LICITEM: 'LKV2DUSA02'
      SWITCH: ENABLE
    set_smfunc_list:
    - DUALFLAG: YES
    add_smsubdata_list:
    - SUBRANGE: ALL_USER
      TYPE: SUBSCRIBED_PARAMETER
      APNNIRANGE: APNNI_ALL
      PDPTYPE: IPV4
      IPV4PDPADDRTYPE: ALLOCATION_IPV4PDP_DYNAMIC
      CORRECTAPNNI: NO
      NEWPDPTYPE: IPV4V6
      NEWIPV4PDPADDRTYPE: DYNAMIC
      NEWIPV6PDPADDRTYPE: DYNAMIC
    mod_gtpccmpt_list:
    - MSGCLS: TM
      TMMSGTYPE: CREATE\_PDP\_CONTEXT\_REQUEST
      CRTPDPREQ: COMMON\_FLAGS
      UPDPDPREQ: COMMON\_FLAGS
      CMFLG: YES
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开IPv4v6双栈接入特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 开启IPv4v6双栈接入功能。

```jinja2
{%- for item in set_smfunc_list -%}
    SET SMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.DUALFLAG is not none -%}
        DUALFLAG={{item.DUALFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**增加签约数据纠正参数。如果S6a口连接的HSS支持IPv4v6双栈，则不需要执行此步骤；若不支持IPv4v6双栈，需要执行此步骤。

```jinja2
{%- if is_optional_subscribed_data_correction_parameter -%}
    {%- for item in add_smsubdata_list -%}
        ADD SMSUBDATA:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        TYPE={{item.TYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CORRECTAPNNI is not none -%}
            CORRECTAPNNI={{item.CORRECTAPNNI}},
        {%- endif -%}
        {%- if item.NEWPDPTYPE is not none -%}
            NEWPDPTYPE={{item.NEWPDPTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=SUBSCRIBED_PARAMETER 时必选 --- -#}
        {%- if item.TYPE == 'SUBSCRIBED_PARAMETER' -%}
            APNNIRANGE={{item.APNNIRANGE}},
        {%- endif -%}
        {#- --- 条件必选：TYPE=SUBSCRIBED_PARAMETER 时必选 --- -#}
        {%- if item.TYPE == 'SUBSCRIBED_PARAMETER' -%}
            PDPTYPE={{item.PDPTYPE}},
        {%- endif -%}
        {#- --- 条件必选：PDPTYPE=IPV4/IPV4V6/IPV4/IPV6 时必选 --- -#}
        {%- if item.PDPTYPE in ['IPV4', 'IPV4V6', 'IPV4/IPV6'] -%}
            IPV4PDPADDRTYPE={{item.IPV4PDPADDRTYPE}},
        {%- endif -%}
        {#- --- 条件必选：NEWPDPTYPE=IPV4/IPV4V6/IPV4/IPV6 时必选 --- -#}
        {%- if item.NEWPDPTYPE in ['IPV4', 'IPV4V6', 'IPV4/IPV6'] -%}
            NEWIPV4PDPADDRTYPE={{item.NEWIPV4PDPADDRTYPE}},
        {%- endif -%}
        {#- --- 条件必选：NEWPDPTYPE=IPV6/IPV4V6/IPV4/IPV6 时必选 --- -#}
        {%- if item.NEWPDPTYPE in ['IPV6', 'IPV4V6', 'IPV4/IPV6'] -%}
            NEWIPV6PDPADDRTYPE={{item.NEWIPV6PDPADDRTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**增加GTP-C V0/V1协议兼容性配置。

### “TMMSGTYPE”设置为“CREATE\_PDP\_CONTEXT\_REQUEST”或者“UPDATE\_PDP\_CONTEXT\_REQUEST”。

### 可通过**LST GTPCCMPT**命令查看当前配置，如果携带方式被设置为不携带Common Flags信元时则需要重新配置。

### 在“MML命令行-UEG”窗口上执行命令

```jinja2
{%- if is_optional_gtpc_v0v1_compatibility_config -%}
    {%- for item in mod_gtpccmpt_list -%}
        MOD GTPCCMPT:
        {#- --- 必选参数 --- -#}
        MSGCLS={{item.MSGCLS}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MSGCLS=TM 时必选 --- -#}
        {%- if item.MSGCLS == 'TM' -%}
            TMMSGTYPE={{item.TMMSGTYPE}},
        {%- endif -%}
        {#- --- 条件必选：TMMSGTYPE=CREATE_PDP_CONTEXT_REQUEST 时必选 --- -#}
        {%- if item.TMMSGTYPE == 'CREATE_PDP_CONTEXT_REQUEST' -%}
            CRTPDPREQ={{item.CRTPDPREQ}},
        {%- endif -%}
        {#- --- 条件必选：TMMSGTYPE=UPDATE_PDP_CONTEXT_REQUEST 时必选 --- -#}
        {%- if item.TMMSGTYPE == 'UPDATE_PDP_CONTEXT_REQUEST' -%}
            UPDPDPREQ={{item.UPDPDPREQ}},
        {%- endif -%}
        {#- --- 条件必选：CRTPDPREQ=COMMON_FLAGS 时必选 --- -#}
        {%- if item.CRTPDPREQ == 'COMMON_FLAGS' -%}
            CMFLG={{item.CMFLG}},
        {#- --- 条件必选：UPDPDPREQ=COMMON_FLAGS 时必选 --- -#}
        {%- elif item.UPDPDPREQ == 'COMMON_FLAGS' -%}
            CMFLG={{item.CMFLG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

