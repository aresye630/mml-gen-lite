---
id: GWFD-020905
name: 激活请求信息纠正功能
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活请求信息纠正功能特性的操作过程。  在激活PDP上下文/PDN连接的过程中，UEG会检查用户请求的APN、PDP/PDN类型和PDP/PDN地址三元组与HLR/HSS中签约的三元组是否一致，如果两者不一致，则拒绝用户的激活请求。这种不一致通常是用户对手机参数设置或签约数据重复等错误引起的，所以，UEG提供了请求信息纠正的功能，减少由于手机参数设置或签约数据重复等错误造成的激活失败。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020905 请求信息纠正功能（适用于SGSN、MME）","激活请求信息纠正功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活请求信息纠正功能特性的操作过程。在激活PDP上下文/PDN连接的过程中，UEG会检查用户请求的APN、PDP/PDN类型和PDP/PDN地址三元组与HLR/HSS中签约的三元组是否一致，如果两者不一致，则拒绝用户的激活请求。这种不一致通常是用户对手机参数设置或签约数据重复等错误引起的，所以，UEG提供了请求信息纠正的功能，减少由于手机参数设置或签约数据重复等错误造成的激活失败。适用于SGSN、MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-020905 请求信息纠正功能特性概述（适用于SGSN、MME）。
* 完成加载License。
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
    add_pdpapn_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          enum:
          - PT_ALL
          - PT_IPV4
          - PT_IPV4_IPV6
          - PT_IPV6
          - PT_PPP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_publicapnni_list:
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
    add_imsiapnconvert_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDAPN:
          name: '请求APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEWAPN:
          name: '转换APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smactctrl_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_UETYPE
          - SPECIAL_USER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNTYPE:
          name: 'UE请求的APNNI'
          type: string
          enum:
          - ALL_APN
          - NOT_NULL_APN
          - NULL_APN
          - SPECIAL_APN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICY:
          name: '处理策略'
          type: string
          enum:
          - MATCH_FAIL_CORRECT
          - MATCH_FAIL_NOTCORRECT
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MATCH_FAIL_CORRECT
        CORRPDPTYPE:
          name: 'PDP Type纠正'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CORRTIP:
          name: 'PDP Address纠正'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SINGLESUB:
          name: '单组签约数据'
          type: string
          enum:
          - NO
          - SELECT_LOC_APN_FIRST
          - SELECT_LOC_APN_ONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        CORRMAPNSUB:
          name: '多组签约数据'
          type: string
          enum:
          - NO
          - SELECT_DEF_APN_FIRST
          - SELECT_LOC_APN_FIRST
          - SELECT_LOC_APN_ONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        WILDCARDPLCY:
          name: '野卡签约数据策略'
          type: string
          enum:
          - CUSTOMIZATION
          - REJECT
          - STANDARD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD
    add_smactimeilib_list:
      type: items
      properties:
        IMEITAC:
          name: '设备型号核准号码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbimeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_iuimeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_s1imeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smactctrl_list_4:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_UETYPE
          - SPECIAL_USER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNTYPE:
          name: 'UE请求的APNNI'
          type: string
          enum:
          - ALL_APN
          - NOT_NULL_APN
          - NULL_APN
          - SPECIAL_APN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICY:
          name: '处理策略'
          type: string
          enum:
          - MATCH_FAIL_CORRECT
          - MATCH_FAIL_NOTCORRECT
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MATCH_FAIL_CORRECT
        WILDCARDPLCY:
          name: '野卡签约数据策略'
          type: string
          enum:
          - CUSTOMIZATION
          - REJECT
          - STANDARD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD
    add_localapnnigp_list:
      type: items
      properties:
        APNNIGRPID:
          name: '本地APNNI组号'
          type: integer
          minimum: 0
          maximum: 127
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
        PRI:
          name: 'APNNI优先级'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfunc_list:
      type: items
      properties:
        APNNISOURCE:
          name: '下发给UE的APN-NI来源'
          type: string
          enum:
          - APNNI_AFTER_SUBDATA_MATCH
          - UE_REQUEST_APNNI
          - UE_REQUEST_APNNI_AFTER_CORRECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2RINCOR02'
      SWITCH: ENABLE
    add_pdpapn_list:
    - SUBRANGE: ALL_USER
      PDPTYPE: PT_IPV4
      APNNI: 'a'
    add_publicapnni_list:
    - APNNI: 'CNNET'
    add_imsiapnconvert_list:
    - SUBRANGE: ''
      OLDAPN: ''
      NEWAPN: ''
    add_smactctrl_list:
    - SUBRANGE: ALL_USER
      APNTYPE: ALL_APN
      POLICY: MATCH_FAIL_CORRECT
      CORRPDPTYPE: NO
      CORRTIP: NO
      SINGLESUB: SELECT_LOC_APN_FIRST
      CORRMAPNSUB: NO
      WILDCARDPLCY: STANDARD
    add_smactimeilib_list:
    - IMEITAC: '12345678'
      UETYPE: BLACKBERRY
    mod_gbimeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEI
    mod_iuimeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEI
    mod_s1imeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEI
    add_smactctrl_list_4:
    - SUBRANGE: SPECIAL_UETYPE
      UETYPE: BLACKBERRY
      APNTYPE: NULL_APN
      POLICY: MATCH_FAIL_NOTCORRECT
      WILDCARDPLCY: REJECT
    add_localapnnigp_list:
    - APNNIGRPID: ''
      APNNI: ''
      PRI: ''
    set_smfunc_list:
    - APNNISOURCE: APNNI_AFTER_SUBDATA_MATCH
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选：**根据IMSI、PDP Type配置Local APNNI。

```jinja2
{%- if is_optional_local_apnni -%}
    {%- for item in add_pdpapn_list -%}
        ADD PDPAPN:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        PDPTYPE={{item.PDPTYPE}},
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”，“IMSI\_PREFIX（指定IMSI前缀）”或“IMSI\_RANGE（指定IMSI范围）”。此处以“IMSI\_PREFIX（指定IMSI前缀）”为例。

### 4 **可选：**配置公用APN。

```jinja2
{%- if is_optional_public_apn -%}
    {%- for item in add_publicapnni_list -%}
        ADD PUBLICAPNNI:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 根据不同场景选取不同的参数配置。

#### 5.1 **可选：**根据IMSI号段，直接纠正UE请求的APNNI为配置的APNNI取值。

```jinja2
{%- if is_optional_correct_apnni -%}
    {%- for item in add_imsiapnconvert_list -%}
        ADD IMSIAPNCONVERT:
        {#- --- 必选参数 --- -#}
        NEWAPN="{{item.NEWAPN}}",
        SUBRANGE={{item.SUBRANGE}},
        OLDAPN="{{item.OLDAPN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”，“IMSI\_PREFIX（指定IMSI前缀）”或“IMSI\_RANGE（指定IMSI范围）”。此处以“IMSI\_PREFIX（指定IMSI前缀）”为例。

#### 5.2 **可选：**根据IMSI号段增加激活过程控制参数。

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in add_smactctrl_list -%}
        ADD SMACTCTRL:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNTYPE={{item.APNTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.POLICY is not none -%}
            POLICY={{item.POLICY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT 时可选 --- -#}
        {%- if item.POLICY == 'MATCH_FAIL_CORRECT' -%}
            {%- if item.CORRPDPTYPE is not none -%}
                CORRPDPTYPE={{item.CORRPDPTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT 时可选 --- -#}
        {%- if item.POLICY == 'MATCH_FAIL_CORRECT' -%}
            {%- if item.CORRTIP is not none -%}
                CORRTIP={{item.CORRTIP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT 时可选 --- -#}
        {%- if item.POLICY == 'MATCH_FAIL_CORRECT' -%}
            {%- if item.SINGLESUB is not none -%}
                SINGLESUB={{item.SINGLESUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT 时可选 --- -#}
        {%- if item.POLICY == 'MATCH_FAIL_CORRECT' -%}
            {%- if item.CORRMAPNSUB is not none -%}
                CORRMAPNSUB={{item.CORRMAPNSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT/MATCH_FAIL_NOTCORRECT 时可选 --- -#}
        {%- if item.POLICY in ['MATCH_FAIL_CORRECT', 'MATCH_FAIL_NOTCORRECT'] -%}
            {%- if item.WILDCARDPLCY is not none -%}
                WILDCARDPLCY={{item.WILDCARDPLCY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in add_smactimeilib_list -%}
        ADD SMACTIMEILIB:
        {#- --- 必选参数 --- -#}
        IMEITAC="{{item.IMEITAC}}",
        UETYPE={{item.UETYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in mod_gbimeicfg_list -%}
        MOD GBIMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in mod_iuimeicfg_list -%}
        MOD IUIMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in mod_s1imeicfg_list -%}
        MOD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_activation_process_control -%}
    {%- for item in add_smactctrl_list_4 -%}
        ADD SMACTCTRL:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNTYPE={{item.APNTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.POLICY is not none -%}
            POLICY={{item.POLICY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_UETYPE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_UETYPE' -%}
            UETYPE={{item.UETYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICY=MATCH_FAIL_CORRECT/MATCH_FAIL_NOTCORRECT 时可选 --- -#}
        {%- if item.POLICY in ['MATCH_FAIL_CORRECT', 'MATCH_FAIL_NOTCORRECT'] -%}
            {%- if item.WILDCARDPLCY is not none -%}
                WILDCARDPLCY={{item.WILDCARDPLCY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 上述配置的参数说明如下：

##### 5.2.1 参数“SUBRANGE”（用户范围）根据实际情况选择“ALL\_USER（所有用户）”、“SPECIAL\_USER（指定用户）”或“SPECIAL\_UETYPE(指定终端类型)”。此处以“SPECIAL\_USER（指定用户）”为例。

##### 5.2.2 参数“POLICY”（处理策略）根据实际情况选择“REJECT(直接拒绝)”、“MATCH\_FAIL\_NOTCORRECT(签约数据匹配失败后不进行纠正)”或“MATCH\_FAIL\_CORRECT(签约数据匹配失败后进行纠正)”。此处以“MATCH\_FAIL\_CORRECT(签约数据匹配失败后进行纠正)”为例。

##### 5.2.3 参数“SINGLESUB”（单组签约数据）根据现网情况选择“SELECT\_LOC\_APN\_ONLY（只选Local APNNI）”或“SELECT\_LOC\_APN\_FIRST（优选Local APNNI）”。

##### 5.2.4 参数“CORRMAPNSUB”（多组签约数据）根据现网情况选择“SELECT\_LOC\_APN\_ONLY（只选Local APNNI）”或“SELECT\_LOC\_APN\_FIRST（优选Local APNNI）”或SELECT\_DEF\_APN\_FIRST（优选Default APNNI）。

##### 5.2.5 参数“WILDCARDPLCY”（野卡签约数据策略）根据现网情况选择“STANDARD（标准）”，“CUSTOMIZATION（定制）或REJECT（拒绝）”。

#### 在配置特定终端类型的请求信息纠正相关策略时，需要提前通过命令**ADD SMACTIMEILIB**配置终端类型与IMEI TAC的映射关系、通过命令**MOD GBIMEICFG**/**MOD IUIMEICFG**/**MOD S1IMEICFG**设置IMEI获取策略为获取IMEI或获取IMEISV。

### 6 **可选：**配置定制APN纠正。

### 开启定制APN纠正功能并配置APNNI组号。

### **ADD SMACTCTRL**中“是否启用定制APN纠正策略”为“YES(是)”，并配置“本地APNNI组号”。

### 配置本地APNNI组信息，定制APN纠正功能会引用该配置参数“本地APNNI组号”。

```jinja2
{%- if is_optional_customized_apn_correction -%}
    {%- for item in add_localapnnigp_list -%}
        ADD LOCALAPNNIGP:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        APNNIGRPID={{item.APNNIGRPID}},
        PRI={{item.PRI}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 设置MME下发给UE的APN-NI来源。

```jinja2
{%- for item in set_smfunc_list -%}
    SET SMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.APNNISOURCE is not none -%}
        APNNISOURCE={{item.APNNISOURCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 本参数配置后是否生效还取决于软参“DWORD\_EX34 BIT1”的设置，当软参“DWORD\_EX34 BIT1”取值为“1”时，系统将以该软参功能为准。

### 部分终端会因接收到的APN与请求的APN不一致而拒绝流程，导致业务失败，需要根据现网UE的实际情况进行参数配置。

