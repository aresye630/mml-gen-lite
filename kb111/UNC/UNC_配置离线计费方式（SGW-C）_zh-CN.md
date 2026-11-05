---
id: ''
name: 配置离线计费方式（SGW-C）
ne_type: UNC
type: feature
description: SGW-C的离线计费方式通过本地配置决定，本地配置有两种粒度：APN和计费属性CC。这些方式的优先级依次降低。如图1所示为SGW-C的离线计费方式选择图。  **图1** SGW-C的离线计费方式选择  适用于SGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置离线计费方式（SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
SGW-C的离线计费方式通过本地配置决定，本地配置有两种粒度：APN和计费属性CC。这些方式的优先级依次降低。如图1所示为SGW-C的离线计费方式选择图。**图1** SGW-C的离线计费方式选择适用于SGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sgwchargecfg_list:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该命令仅适用于UNC产品用作S-GW网元。  SGW计费配置，包括本地离线计费、漫游离线计费、拜访离线计费、使用本地CG或使用PGW携带的CG。  一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访用户离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SGWCGFLAG:
          name: 'SGW CG IP选择'
          type: string
          enum:
          - USE_LOCAL
          - USE_PGW
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngsgwplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '（可选）配置SGW-C的Home PLMN。当PGW-C与SGW-C部署在同一台设备上：   * 期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效），当SGW-C用户的IMSI中的PLMN未匹配到**ADD NGSGWPLMN**配置时判断用户为漫游用户。 * 期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_sgwchgmeth_list:
      type: items
      properties:
        CHARGECHAR:
          name: '计费属性'
          type: string
          enum:
          - DEFAULT
          - FLAT_BILLING
          - HOT_BILLING
          - NORMAL
          - PREPAID
          - SPECIFIC_VALUE
          required: true
          description: '配置SGW-C计费方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: '是否离线计费'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCMASK:
          name: '计费属性掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: '计费属性优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGECHARVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN。可通过**LST APN**命令查询已经配置的APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_sgwapnchgmeth_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '设置SGW APN计费方式   * OFFLINE默认值都是INHERIT。 * 在APN中配置INHERIT则计费方式继承基于计费属性的配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OFFLINE:
          name: 'APN离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subscriberidseggrp_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV号段组名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN/IMEISV号码段组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI/MSISDN/IMEISV号段名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: '号段类型'
          type: string
          enum:
          - IMEISV
          - IMSIMSISDN
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sgwseggchgmeth_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号段组名称'
          type: string
          maxLength: 31
          required: true
          description: '设置SGW-C基于号段组的计费方式。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'IMSI/MSISDN号段组优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: 'IMSI/MSISDN号段组离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        SPCDRCONTROL:
          name: 'SP合一网关话单控制'
          type: string
          enum:
          - PGW_CDR
          - PGW_SGW_CDR
          required: false
          description: '配置SP合一用户产生SGW话单。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_sgwchargecfg_list:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
      SGWCGFLAG: USE_LOCAL
    add_ngsgwplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '68'
      DESC: 'sgw homeplmn1'
    set_sgwchgmeth_list:
    - CHARGECHAR: DEFAULT
      OFFLINEFLAG: ENABLE
      CCMASK: ''
      CCPRIORITY: ''
      CHARGECHARVALUE: ''
    add_apn_list:
    - APN: 'apn-test'
    set_sgwapnchgmeth_list:
    - APN: 'apn-test'
      OFFLINE: ENABLE
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: IMSI
      SEGSTART: '13900100100'
      SEGEND: '13900100199'
      WILDCARDSEG: ''
    add_subscriberidseggrp_list:
    - SEGGROUPNAME: 'testmsisdngr1'
      SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: IMSIMSISDN
    add_sgwseggchgmeth_list:
    - SEGGROUPNAME: 'testmsisdngr1'
      PRIORITY: 2
      OFFLINEFLAG: ENABLE
    set_ofccdrpara_list:
    - SPCDRCONTROL: PGW_SGW_CDR
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性（本地用户、漫游用户、拜访用户）使能SGW-C的离线计费方式。

```jinja2
{%- for item in set_sgwchargecfg_list -%}
    SET SGWCHARGECFG:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    {%- if item.SGWCGFLAG is not none -%}
        SGWCGFLAG={{item.SGWCGFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。

### 2 **可选：**配置SGW-C的Home PLMN。

```jinja2
{%- if is_optional_sgw_c_home_plmn -%}
    {%- for item in add_ngsgwplmn_list -%}
        ADD NGSGWPLMN:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当PGW-C与SGW-C部署在同一台设备上，期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效）。期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。

### 3 配置使能SGW-C的离线计费方式。

#### 3.1 基于用户计费属性使能SGW-C的离线计费方式。

```jinja2
{%- for item in set_sgwchgmeth_list -%}
    SET SGWCHGMETH:
    {#- --- 必选参数 --- -#}
    CHARGECHAR={{item.CHARGECHAR}},
    OFFLINEFLAG={{item.OFFLINEFLAG}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CHARGECHAR=SPECIFIC_VALUE 时必选 --- -#}
    {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
        CHARGECHARVALUE="{{item.CHARGECHARVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CHARGECHAR=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHARGECHAR=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 基于APN使能SGW-C的离线计费方式。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_sgwapnchgmeth_list -%}
    SET SGWAPNCHGMETH:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    OFFLINE={{item.OFFLINE}},
    ;
{%- endfor -%}
```

### 4 设置SGW-C基于号段组的计费方式。

#### 4.1 配置IMSI及MSISDN号码段。

```jinja2
{%- for item in add_imsimsisdnseg_list -%}
    ADD IMSIMSISDNSEG:
    {#- --- 必选参数 --- -#}
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGSTART="{{item.SEGSTART}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGEND="{{item.SEGEND}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
        WILDCARDSEG="{{item.WILDCARDSEG}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置IMSI/MSISDN/IMEISV号码段组。

```jinja2
{%- for item in add_subscriberidseggrp_list -%}
    ADD SUBSCRIBERIDSEGGRP:
    {#- --- 必选参数 --- -#}
    SEGGROUPNAME="{{item.SEGGROUPNAME}}",
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    ;
{%- endfor -%}
```

#### 4.3 设置SGW-C基于号段组的计费方式。

```jinja2
{%- for item in add_sgwseggchgmeth_list -%}
    ADD SGWSEGGCHGMETH:
    {#- --- 必选参数 --- -#}
    SEGGROUPNAME="{{item.SEGGROUPNAME}}",
    PRIORITY={{item.PRIORITY}},
    OFFLINEFLAG={{item.OFFLINEFLAG}},
    ;
{%- endfor -%}
```

### 5 **可选**：配置SP合一用户产生SGW话单。

```jinja2
{%- if is_optional_sp_combined_user_sgw_cdr -%}
    {%- for item in set_ofccdrpara_list -%}
        SET OFCCDRPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.SPCDRCONTROL is not none -%}
            SPCDRCONTROL={{item.SPCDRCONTROL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

