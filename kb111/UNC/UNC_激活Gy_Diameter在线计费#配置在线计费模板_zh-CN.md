---
id: ''
name: 配置在线计费模板
ne_type: UNC
type: feature
description: 在线计费模板是用来绑定在线计费本地配置参数的，在线计费DCC模板分为全局通用参数模板dcc-global和普通的模板DCC Template，前者用于配置整机通用的在线计费参数，后者用于配置特殊场景下的在线计费参数。  在线计费参数中，除了OCS的基本信息是基于全局配置的之外，其他的参数，如要使用的OCS服务器、CCR触发场景、DCC处理动作、CCR消息中携带的参数等都可以选择基于整机或特殊场景生效。  GGSN/PGW-C支持以下几种粒度范围的在线计费参数配置：  * 支持配置整机通用参数。 * 支持根据用户计费属性Charging Characteristics配置在线计费参数。 * 支持根据APN配置在线计费参数。 * 支持根据UserProfile配置在线计费参数。  上述几种粒度范围的优先级从高到低依次是：UserProfile下的配置–〉APN下的配置–〉计费属性下的配置–〉整机通用参数。如果高级别的参数没有配置或者配置inherit，则依次向下继承低一级别的参数取值。整机通用参数绑定在dcc-global模板下，其他几种粒度都绑定在DCC Template下，并进而绑定其生效的范围：某一计费属性、APN、或者UserProfile。  在线计费参数的配置粒度，建议与配置离线/在线计费方式（GGSN/PGW-C）的配置粒度保持一致，即如果基于APN开启在线计费功能，同样基于APN配置在线计费参数，这样可以避免各配置参数生效范围冲突和不一致。一旦确定了整个系统的在线计费参数配置粒度，则所有在线计费参数的配置原则上都必须统一使用该粒度。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置在线计费模板"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在线计费模板是用来绑定在线计费本地配置参数的，在线计费DCC模板分为全局通用参数模板dcc-global和普通的模板DCC Template，前者用于配置整机通用的在线计费参数，后者用于配置特殊场景下的在线计费参数。在线计费参数中，除了OCS的基本信息是基于全局配置的之外，其他的参数，如要使用的OCS服务器、CCR触发场景、DCC处理动作、CCR消息中携带的参数等都可以选择基于整机或特殊场景生效。GGSN/PGW-C支持以下几种粒度范围的在线计费参数配置：* 支持配置整机通用参数。* 支持根据用户计费属性Charging Characteristics配置在线计费参数。* 支持根据APN配置在线计费参数。* 支持根据UserProfile配置在线计费参数。上述几种粒度范围的优先级从高到低依次是：UserProfile下的配置–〉APN下的配置–〉计费属性下的配置–〉整机通用参数。如果高级别的参数没有配置或者配置inherit，则依次向下继承低一级别的参数取值。整机通用参数绑定在dcc-global模板下，其他几种粒度都绑定在DCC Template下，并进而绑定其生效的范围：某一计费属性、APN、或者UserProfile。在线计费参数的配置粒度，建议与配置离线/在线计费方式（GGSN/PGW-C）的配置粒度保持一致，即如果基于APN开启在线计费功能，同样基于APN配置在线计费参数，这样可以避免各配置参数生效范围冲突和不一致。一旦确定了整个系统的在线计费参数配置粒度，则所有在线计费参数的配置原则上都必须统一使用该粒度。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_glbdcctemplate_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '计费属性绑定在线计费模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SPECIFICCCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DCCTEMPLATENAME:
          name: '在线计费模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MASK:
          name: '计费属性掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
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
          description: '配置APN，可以使用**LST APN**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN实例绑定DCC Template模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DCCTEMPLATE:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProflie。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'User Profile实例绑定DCC模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DCCTEMPLATE:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置用户模板组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '用户模板绑定到用户模板组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCCONFIGMODE:
          name: '计费属性配置模式'
          type: string
          enum:
          - FLATBILLING
          - HOTBILLING
          - NORMAL
          - PREPAID
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISVSEGNAME:
          name: 'IMEISV号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSSEGNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAT:
          name: 'RAT'
          type: string
          enum:
          - EMTC
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - NBIOT
          - NONE
          - NR
          - REDCAP
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游属性'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV 号段组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: 'UsrProfGroup绑定到APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_dcctemplate_list:
    - DCCTMPLTNAME: 'global'
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
    add_glbdcctemplate_list:
    - CHARGECHARACT: CHARGE_CHARACT
      SPECIFICCCVALUE: '0x0800'
      DCCTEMPLATENAME: 'dcc-test'
      MASK: ''
      PRIORITY: ''
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      DCCTEMPLATE: 'dcc-test'
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      DCCTEMPLATE: 'dcc-test'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg-test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg-test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up-test'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg-test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置DCC Template模板。重复执行本步骤可增加多个DCC Template模板。

#### 1.1 配置全局通用参数DCC模板，DCC模板名称。“DCCTMPLTNAME”=“global”

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

#### 1.2 配置DCC Template模板，以及触发CCR的各参数、CCR消息中携带的参数。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

#### 1.3 配置各计费参数，请见在线计费章节的后面小节。

##### 1.3.1 配置CCR触发场景

##### 1.3.2 配置CCR消息中携带的参数

##### 1.3.3 配置在线计费自动回切功能

### 2 配置DCC Template模板绑定到计费属性。

```jinja2
{%- for item in add_glbdcctemplate_list -%}
    ADD GLBDCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    CHARGECHARACT={{item.CHARGECHARACT}},
    DCCTEMPLATENAME="{{item.DCCTEMPLATENAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CHARGECHARACT=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.CHARGECHARACT == 'CHARGE_CHARACT' -%}
        SPECIFICCCVALUE="{{item.SPECIFICCCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CHARGECHARACT=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'CHARGE_CHARACT' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHARGECHARACT=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'CHARGE_CHARACT' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置DCC Template模板绑定APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置DCC Template模板绑定UserProfile实例。

#### 4.1 指定UserProfile实例。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置DCC Template模板绑定UserProfile实例。

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 配置UserProfileGroup。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 4.4 将UserProfile绑定到UserProfileGroup。

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.CCCONFIGMODE is not none -%}
            CCCONFIGMODE={{item.CCCONFIGMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMEISVSEGNAME is not none -%}
            IMEISVSEGNAME="{{item.IMEISVSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMSIMSSEGNAME is not none -%}
            IMSIMSSEGNAME="{{item.IMSIMSSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.LOCGROUPNAME is not none -%}
            LOCGROUPNAME="{{item.LOCGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.RAT is not none -%}
            RAT={{item.RAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.SEGGROUPNAME is not none -%}
            SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 将UserProfileGroup绑定到APN实例下。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

