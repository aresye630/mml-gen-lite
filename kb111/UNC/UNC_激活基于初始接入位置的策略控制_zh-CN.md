---
id: ''
name: 激活基于初始接入位置的策略控制
ne_type: UNC
type: feature
description: 运营商需要根据用户的初始接入位置信息对该类用户进行策略控制（例如带宽控制），缓解热点小区拥塞问题时，需要部署该特性。  用户在接入网络（PDP一次上下文激活/Attach）时，SGSN/MME/AMF将用户的初始接入位置信息上报给GGSN-C/PGW-C/SMF：  * 组网中有PCRF/PCF时，PCRF/PCF根据GGSN-C/PGW-C/SMF携带的初始接入位置信息决策并下发具体的带宽策略。完成初始配置即可，UNC上不需要新增单独配置。 * 组网中有PCRF/PCF时，PCRF/PCF根据GGSN-C/PGW-C/SMF携带的初始接入位置信息决策并下发预定义规则，请参考本页面在UNC进行配置。 * 组网中没有PCRF/PCF或回滚到本地PCC时，GGSN-C/PGW-C/SMF根据初始接入位置信息决策并下发带宽策略。请参考本页面在UNC进行配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-211001 基于初始接入位置的策略控制","激活基于初始接入位置的策略控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商需要根据用户的初始接入位置信息对该类用户进行策略控制（例如带宽控制），缓解热点小区拥塞问题时，需要部署该特性。用户在接入网络（PDP一次上下文激活/Attach）时，SGSN/MME/AMF将用户的初始接入位置信息上报给GGSN-C/PGW-C/SMF：* 组网中有PCRF/PCF时，PCRF/PCF根据GGSN-C/PGW-C/SMF携带的初始接入位置信息决策并下发具体的带宽策略。完成初始配置即可，UNC上不需要新增单独配置。* 组网中有PCRF/PCF时，PCRF/PCF根据GGSN-C/PGW-C/SMF携带的初始接入位置信息决策并下发预定义规则，请参考本页面在UNC进行配置。* 组网中没有PCRF/PCF或回滚到本地PCC时，GGSN-C/PGW-C/SMF根据初始接入位置信息决策并下发带宽策略。请参考本页面在UNC进行配置。

## 必备事项
前提条件

* 请仔细阅读WSFD-211001 基于初始接入位置的策略控制。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
* 完成**基于业务感知的带宽控制**。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    add_usrlocation_list:
      type: items
      properties:
        LOCATIONNAME:
          name: '位置名称'
          type: string
          maxLength: 63
          required: true
          description: '不同记录之间，位置名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCATIONTYPE:
          name: '位置类型'
          type: string
          enum:
          - CGI
          - ECGI
          - LAI
          - NCGI
          - PLMN
          - RAI
          - SAI
          - TAI
          required: true
          description: '2/3G时，选择CGI。  4G时，选择ECGI。  5G时，选择NCGI。'
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网络码'
          type: string
          maxLength: 3
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区码'
          type: string
          maxLength: 6
          required: false
          description: '**位置类型**为“CGI”时需要规划。'
          data_source: ''
          pattern: ''
          default: ''
        CI:
          name: '小区标识'
          type: string
          maxLength: 6
          required: false
          description: '**位置类型**为“CGI”时需要规划。'
          data_source: ''
          pattern: ''
          default: ''
        ECI:
          name: 'E-UTRAN小区标识'
          type: string
          maxLength: 9
          required: false
          description: '**位置类型**为“ECGI”时需要规划。'
          data_source: ''
          pattern: ''
          default: ''
        NCI:
          name: 'NR小区标识'
          type: string
          maxLength: 11
          required: false
          description: '**位置类型**为“NCGI”时需要规划。'
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SAC:
          name: '服务区码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAC:
          name: '跟踪区码'
          type: string
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrlocationgrp_list:
      type: items
      properties:
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: true
          description: '不同记录之间，位置组名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCATIONNAME:
          name: '位置名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD USRLOCATION**定义的位置名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD UPBINDUPG**命令定义，未定义时，直接使用**ADD UPBINDUPG**命令添加位置组、用户模板与用户模板组的绑定关系。'
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
          data_source: '固定取值'
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
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD USRLOCATIONGRP**定义的位置组名称。'
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
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
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
          description: '使用**ADD APN**命令中定义的APN名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**MOD UPBINDUPG**  命令中绑定的用户模板组名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PCIAL01'
      SWITCH: ENABLE
    add_usrlocation_list:
    - LOCATIONNAME: 'loc_test1'
      LOCATIONTYPE: CGI
      MCC: '333'
      MNC: '111'
      LAC: '0xFFFD'
      CI: '0xFFFD'
      ECI: '0xffffffd'
      NCI: '0xffffffffd'
      RAC: ''
      SAC: ''
      TAC: ''
    add_usrlocationgrp_list:
    - LOCGROUPNAME: 'locgrp_test'
      LOCATIONNAME: 'loc_test1'
    mod_upbindupg_list:
    - USERPROFGNAME: 'upg_test1'
      UPBINDTYPE: SPECIFIC
      USERPROFILENAME: 'up_test1'
      LOCGROUPNAME: 'locgrp_test'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_upbindupg_list:
    - USERPROFGNAME: ''
      UPBINDTYPE: ''
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
      USERPROFILENAME: ''
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg_test1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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

### 3 配置用户位置信息。

```jinja2
{%- for item in add_usrlocation_list -%}
    ADD USRLOCATION:
    {#- --- 必选参数 --- -#}
    LOCATIONNAME="{{item.LOCATIONNAME}}",
    LOCATIONTYPE={{item.LOCATIONTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOCATIONTYPE=PLMN/LAI/RAI/CGI/SAI/ECGI/NCGI/TAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE in ['PLMN', 'LAI', 'RAI', 'CGI', 'SAI', 'ECGI', 'NCGI', 'TAI'] -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=PLMN/LAI/RAI/CGI/SAI/ECGI/NCGI/TAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE in ['PLMN', 'LAI', 'RAI', 'CGI', 'SAI', 'ECGI', 'NCGI', 'TAI'] -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=LAI/RAI/CGI/SAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE in ['LAI', 'RAI', 'CGI', 'SAI'] -%}
        LAC="{{item.LAC}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=CGI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'CGI' -%}
        CI="{{item.CI}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=ECGI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'ECGI' -%}
        ECI="{{item.ECI}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=NCGI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'NCGI' -%}
        NCI="{{item.NCI}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=RAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'RAI' -%}
        RAC="{{item.RAC}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=SAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'SAI' -%}
        SAC="{{item.SAC}}",
    {%- endif -%}
    {#- --- 条件必选：LOCATIONTYPE=TAI 时必选 --- -#}
    {%- if item.LOCATIONTYPE == 'TAI' -%}
        TAC="{{item.TAC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置用户位置组信息。

```jinja2
{%- for item in add_usrlocationgrp_list -%}
    ADD USRLOCATIONGRP:
    {#- --- 必选参数 --- -#}
    LOCGROUPNAME="{{item.LOCGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATIONNAME is not none -%}
        LOCATIONNAME="{{item.LOCATIONNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 将多条用户位置信息绑定到一个位置组中。

### 5 将用户模板和用户位置组信息绑定到用户模板组。

### 在规则中配置策略动作（例如带宽控制），并将规则和用户模板绑定。

#### 5.1 用户模板和用户模板组已绑定时：

```jinja2
{%- if is_scenario_usertemplate_bound -%}
    {%- for item in mod_upbindupg_list -%}
        MOD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        UPBINDTYPE={{item.UPBINDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
        {%- endif -%}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            {%- if item.LOCGROUPNAME is not none -%}
                LOCGROUPNAME="{{item.LOCGROUPNAME}}",
            {%- endif -%}
        {%- endif -%}
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
{%- endif -%}
```

#### 5.2 用户模板和用户模板组未绑定时：

```jinja2
{%- if is_scenario_usertemplate_unbound -%}
    {%- for item in add_upbindupg_list -%}
        ADD UPBINDUPG:
        {#- --- 必选参数 --- -#}
        UPBINDTYPE={{item.UPBINDTYPE}},
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
        {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
        {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
            USERPROFILENAME="{{item.USERPROFILENAME}}",
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
{%- endif -%}
```

### 6 将用户模板组和APN/DNN绑定。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

