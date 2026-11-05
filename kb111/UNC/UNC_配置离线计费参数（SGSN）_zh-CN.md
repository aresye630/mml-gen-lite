---
id: ''
name: 配置离线计费参数（SGSN）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活话单生成和传输功能的操作过程。  SGSN能够按照3GPP协议规范采用ASN.1（Abstract Syntax Notation）编码格式输出CDR（Call Detail Record）。SGSN可以设置产生CDR的条件并能够定制CDR的内容，将生成的CDR通过Ga接口发送到CG。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置离线计费参数（SGSN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活话单生成和传输功能的操作过程。SGSN能够按照3GPP协议规范采用ASN.1（Abstract Syntax Notation）编码格式输出CDR（Call Detail Record）。SGSN可以设置产生CDR的条件并能够定制CDR的内容，将生成的CDR通过Ga接口发送到CG。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读离线计费话单（SGSN）。
* 无特殊前提条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chgplmnchar_list:
      type: items
      properties:
        PLMN:
          name: 'PLMN 类型'
          type: string
          enum:
          - HPLMN
          - VPLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgplmncfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - CELL_PLMNID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgplmnchar_list_1:
      type: items
      properties:
        PLMN:
          name: 'PLMN 类型'
          type: string
          enum:
          - HPLMN
          - VPLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgimsicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          required: true
          description: '抑制特定用户的S-CDR话单生成。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITTYPE:
          name: '拜访类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '计费属性'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: '生成S-CDR'
          type: string
          enum:
          - DFT
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DFT
    set_chgcdr_list:
      type: items
      properties: {}
    set_chgcdr_list_1:
      type: items
      properties: {}
    set_chgchar_list:
      type: items
      properties:
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgapn_list:
      type: items
      properties:
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgdchar_list:
      type: items
      properties:
        ST:
          name: '用户类型'
          type: string
          enum:
          - ROAMING
          - VISITING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
    set_chgplmnchar_list_2:
      type: items
      properties:
        PLMN:
          name: 'PLMN 类型'
          type: string
          enum:
          - HPLMN
          - VPLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_chgplmnchar_list:
    - PLMN: ''
    add_chgplmncfg_list:
    - SUBRANGE: ''
      APNNI: ''
      MCC: ''
      MNC: ''
    set_chgplmnchar_list_1:
    - PLMN: ''
    add_chgimsicfg_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      VISITTYPE: ROAMING-1
      APNNI: 'huawei.com'
      CC: NORMAL_BILLING-1
      SP: NO
    set_chgcdr_list:
    - {}
    set_chgcdr_list_1:
    - {}
    set_chgchar_list:
    - CC: ''
    add_chgapn_list:
    - APNNI: ''
    add_chgdchar_list:
    - ST: ''
      MCC: ''
      MNC: ''
    set_chgplmnchar_list_2:
    - PLMN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 可选：基于PLMN和APN NI共同配置生成S-CDR策略。

### 进入“MML命令行-UNC”窗口。

### 2 配置生成S-CDR话单。

```jinja2
{%- for item in set_chgplmnchar_list -%}
    SET CHGPLMNCHAR:
    {#- --- 必选参数 --- -#}
    PLMN={{item.PLMN}},
    ;
{%- endfor -%}
```

### 3 基于PLMN和APN NI共同配置生成S-CDR策略。

```jinja2
{%- for item in add_chgplmncfg_list -%}
    ADD CHGPLMNCFG:
    {#- --- 必选参数 --- -#}
    APNNI="{{item.APNNI}}",
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=CELL_PLMNID 时必选 --- -#}
    {%- if item.SUBRANGE == 'CELL_PLMNID' -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=CELL_PLMNID 时必选 --- -#}
    {%- if item.SUBRANGE == 'CELL_PLMNID' -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 可选：基于IMSI前缀、APN NI、漫游属性、计费属性来共同定制S-CDR话单生成策略。

### 配置生成S-CDR话单。

```jinja2
{%- if is_optional_imsi_scdr_policy -%}
    {%- for item in set_chgplmnchar_list_1 -%}
        SET CHGPLMNCHAR:
        {#- --- 必选参数 --- -#}
        PLMN={{item.PLMN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 基于IMSI前缀、APN NI、漫游属性、计费属性共同配置生成S-CDR策略。

```jinja2
{%- for item in add_chgimsicfg_list -%}
    ADD CHGIMSICFG:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC={{item.CC}},
    {%- endif -%}
    {%- if item.SP is not none -%}
        SP={{item.SP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        {%- if item.VISITTYPE is not none -%}
            VISITTYPE={{item.VISITTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.1 **SET CHGCDR**中的“PLMNCTRL”参数用于控制PLMN ID的获取来源。当PLMNCTRL=IMSI中的PLMNID，则话单生成策略为基于IMSI前缀、APN NI、拜访类型和计费属性共同配置的S-CDR话单生成策略；当PLMNCTRL=LOCINFO中的PLMNID，则话单生成策略为基于PLMN和APN NI共同配置的S-CDR话单生成策略。

#### 5.2 基于IMSI前缀、APN和计费属性共同配置生成S-CDR话单策略默认优先级由高到低的顺序为：基于IMSI前缀和APN NI共同配置结合计费属性生成S-CDR话单策略、基于计费属性生成S-CDR话单策略。

#### 5.3 基于PLMN和APN NI共同配置生成S-CDR话单策略默认优先级由高到低的顺序为：基于PLMN和APN NI共同配置生成S-CDR话单策略、基于计费属性S-CDR话单生成策略 。

### 6 可选：配置指定时间强制生成话单。

### 配置指定时间强制生成话单。

```jinja2
{%- if is_optional_forced_cdr_generation -%}
    SET CHGCDR:
    ;
{%- endif -%}
```

### 7 可选：配置全局计费属性参数。

### 配置全局计费属性参数。

```jinja2
{%- if is_optional_global_cc_params -%}
    SET CHGCDR:
    ;
{%- endif -%}
```

### 8 可选：配置特定计费属性的CDR参数。

### 配置特定计费属性的CDR参数。

```jinja2
{%- if is_optional_specific_cc_cdr_params -%}
    {%- for item in set_chgchar_list -%}
        SET CHGCHAR:
        {#- --- 必选参数 --- -#}
        CC={{item.CC}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.1 只有**ADD CHGCG**命令配置的CG，才能在**SET CHGCHAR**命令中生效。

#### 8.2 根据实际场景的不同选择性配置计费属性功能。用户计费属性的优先级由低到高的顺序如下：

#### - **SET CHGCDR**命令配置的计费属性。

#### - **SET CHGCHAR**命令配置的计费属性。

#### - 用户在HLR中签约的计费属性。

### 9 可选：配置特定APN用户的计费属性。

### 配置特定APN用户的计费属性。

```jinja2
{%- if is_optional_apn_user_cc -%}
    {%- for item in add_chgapn_list -%}
        ADD CHGAPN:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 可选：配置用户的缺省计费属性。

### 配置用户的缺省计费属性。

```jinja2
{%- if is_optional_user_default_cc -%}
    {%- for item in add_chgdchar_list -%}
        ADD CHGDCHAR:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ST={{item.ST}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 可选：配置特定PLMN的计费属性参数。

### 配置特定PLMN的计费属性参数。

```jinja2
{%- if is_optional_plmn_cc_params -%}
    {%- for item in set_chgplmnchar_list_2 -%}
        SET CHGPLMNCHAR:
        {#- --- 必选参数 --- -#}
        PLMN={{item.PLMN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 11.1 如果**SET CHGPLMNCHAR**命令配置了禁止生成某种话单，则无论命令**SET CHGCHAR**配置何种类型的值，都不生成话单。

#### 11.2 如果**SET CHGPLMNCHAR**命令配置了允许生成某种话单，则用户是否生成话单将由命令**ADD CHGIMSICFG**、**ADD CHGPLMNCFG**和**SET CHGCHAR**中的配置决定。

### 可选：激活话单传输功能，具体内容请参考**《UNC产品手册》：UNC初始配置与调测->2/3/4/5G融合组网对接配置->配置SGSN->配置到CG的数据。**

