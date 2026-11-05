---
id: ''
name: 配置计费属性CC（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: CC可以由RADIUS Server下发，可以在HLR/HSS上签约，也可以在UNC上本地配置，UNC支持基于UserProfile、APN、全局配置三种计费属性Charging Characteristics（CC）。其中，RADIUS Server下发CC优先级大于UNC本地配置，UNC上CC的优先级从高到低依次是：UserProflie下的配置 > APN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的参数没有配置，则依次向下使用低一级别的参数取值。图1呈现了CC的选择逻辑图。  * 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。 * 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。    + 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带CC（MME从HSS获取的签约CC）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带CC（MME从HSS获取的签约CC），当UNC单独作为PGW-C时由左侧SGW-C携带CC（SGW-C通过MME得到签约CC）。即4G网络中签约CC由左侧MME/SGW-C携带。   + 2/3G网络中，UNC作为GGSN，由左侧SGSN携带签约CC（SGSN从HLR获取得签约CC）。  **图1** Charging Characteristics选择图  * 在线计费适用于GGSN、PGW-C。 * 离线计费适用于SGW-C、PGW-C、GGSN。 * 对于特定用户，无论是只做在线计费、离线计费，还是离线计费和在线计费都做，一个用户只会对应一个计费属性CC。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置计费属性CC（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
CC可以由RADIUS Server下发，可以在HLR/HSS上签约，也可以在UNC上本地配置，UNC支持基于UserProfile、APN、全局配置三种计费属性Charging Characteristics（CC）。其中，RADIUS Server下发CC优先级大于UNC本地配置，UNC上CC的优先级从高到低依次是：UserProflie下的配置 > APN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的参数没有配置，则依次向下使用低一级别的参数取值。图1呈现了CC的选择逻辑图。* 当左侧网元携带签约CC、并且本地基于UserProfile、APN配置CC场景下，本地、漫游、拜访用户选择CC由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地配置的CC。* 当左侧网元携带签约CC、并且本地基于全局配置CC场景下，本地、漫游、拜访用户选择CC由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制，当对应参数配置为ENABLE时，表示使用签约下发的CC，当配置为DISABLE时，表示使用本地全局配置的CC。  + 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带CC（MME从HSS获取的签约CC）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带CC（MME从HSS获取的签约CC），当UNC单独作为PGW-C时由左侧SGW-C携带CC（SGW-C通过MME得到签约CC）。即4G网络中签约CC由左侧MME/SGW-C携带。  + 2/3G网络中，UNC作为GGSN，由左侧SGSN携带签约CC（SGSN从HLR获取得签约CC）。**图1** Charging Characteristics选择图* 在线计费适用于GGSN、PGW-C。* 离线计费适用于SGW-C、PGW-C、GGSN。* 对于特定用户，无论是只做在线计费、离线计费，还是离线计费和在线计费都做，一个用户只会对应一个计费属性CC。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）或配置到OCS的数据(静态路由+BFD组网)。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_glbchargechar_list:
      type: items
      properties:
        HOME:
          name: '本地用户计费类型'
          type: string
          maxLength: 6
          required: false
          description: '配置全局CC。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAM:
          name: '漫游用户计费类型'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISIT:
          name: '拜访用户计费类型'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOMESGSN:
          name: '本地用户使用SGSN计费属性标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMSGSN:
          name: '漫游用户使用SGSN计费属性标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITSGSN:
          name: '拜访用户使用SGSN计费属性标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chargechar_list:
      type: items
      properties:
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: true
          description: '配置CC实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOME:
          name: '本地用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        ROAM:
          name: '漫游用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        VISIT:
          name: '拜访用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        HOMESGSN:
          name: '本地用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ROAMSGSN:
          name: '漫游用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        VISITSGSN:
          name: '拜访用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '将CC绑定到APN上。每个APN只能绑定一个计费属性。如果APN已绑定了计费属性，要绑定其他的计费属性，必须调用**SET APNCHARGECTRL**命令修改绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_chargechar_list_1:
      type: items
      properties:
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: true
          description: '配置CC实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOME:
          name: '本地用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        ROAM:
          name: '漫游用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        VISIT:
          name: '拜访用户计费属性'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '0x0800'
        HOMESGSN:
          name: '本地用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ROAMSGSN:
          name: '漫游用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        VISITSGSN:
          name: '拜访用户使用Serving Node计费属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
          description: '将CC绑定到UserProflie上。每个UserProflie只能绑定一个计费属性。如果UserProflie已绑定了计费属性，要绑定其他的计费属性，必须调用**SET USRPROFCHARGE**命令修改绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_glbchargechar_list:
    - HOME: '0x0100'
      ROAM: '0x0100'
      VISIT: '0x0100'
      HOMESGSN: ENABLE
      ROAMSGSN: ENABLE
      VISITSGSN: ENABLE
    add_chargechar_list:
    - CCNAME: 'testchgcha'
      HOME: '0x0800'
      ROAM: '0x0800'
      VISIT: '0x0800'
      HOMESGSN: ENABLE
      ROAMSGSN: ENABLE
      VISITSGSN: ENABLE
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      VPNINSTANCE: ''
      VPNINSTANCEIPV6: ''
      PDTNSWITCH: DISABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      CCNAME: 'testchgcha'
    add_chargechar_list_1:
    - CCNAME: 'testchgcha'
      HOME: '0x0800'
      ROAM: '0x0800'
      VISIT: '0x0800'
      HOMESGSN: ENABLE
      ROAMSGSN: ENABLE
      VISITSGSN: ENABLE
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      CCNAME: 'testchgcha'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置全局CC。

```jinja2
{%- for item in set_glbchargechar_list -%}
    SET GLBCHARGECHAR:
    {#- --- 可选参数 --- -#}
    {%- if item.HOME is not none -%}
        HOME="{{item.HOME}}",
    {%- endif -%}
    {%- if item.ROAM is not none -%}
        ROAM="{{item.ROAM}}",
    {%- endif -%}
    {%- if item.VISIT is not none -%}
        VISIT="{{item.VISIT}}",
    {%- endif -%}
    {%- if item.HOMESGSN is not none -%}
        HOMESGSN={{item.HOMESGSN}},
    {%- endif -%}
    {%- if item.ROAMSGSN is not none -%}
        ROAMSGSN={{item.ROAMSGSN}},
    {%- endif -%}
    {%- if item.VISITSGSN is not none -%}
        VISITSGSN={{item.VISITSGSN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置APN下的CC。

#### 2.1 配置CC实例。

```jinja2
{%- for item in add_chargechar_list -%}
    ADD CHARGECHAR:
    {#- --- 必选参数 --- -#}
    CCNAME="{{item.CCNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOME is not none -%}
        HOME="{{item.HOME}}",
    {%- endif -%}
    {%- if item.ROAM is not none -%}
        ROAM="{{item.ROAM}}",
    {%- endif -%}
    {%- if item.VISIT is not none -%}
        VISIT="{{item.VISIT}}",
    {%- endif -%}
    {%- if item.HOMESGSN is not none -%}
        HOMESGSN={{item.HOMESGSN}},
    {%- endif -%}
    {%- if item.ROAMSGSN is not none -%}
        ROAMSGSN={{item.ROAMSGSN}},
    {%- endif -%}
    {%- if item.VISITSGSN is not none -%}
        VISITSGSN={{item.VISITSGSN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置APN。如已配置APN，请跳过该步骤。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
    {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
        {%- if item.PDTNSWITCH is not none -%}
            PDTNSWITCH={{item.PDTNSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 将CC绑定到APN上。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCNAME is not none -%}
        CCNAME="{{item.CCNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置UserProflie下的CC。

#### 3.1 配置CC实例。

```jinja2
{%- for item in add_chargechar_list_1 -%}
    ADD CHARGECHAR:
    {#- --- 必选参数 --- -#}
    CCNAME="{{item.CCNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOME is not none -%}
        HOME="{{item.HOME}}",
    {%- endif -%}
    {%- if item.ROAM is not none -%}
        ROAM="{{item.ROAM}}",
    {%- endif -%}
    {%- if item.VISIT is not none -%}
        VISIT="{{item.VISIT}}",
    {%- endif -%}
    {%- if item.HOMESGSN is not none -%}
        HOMESGSN={{item.HOMESGSN}},
    {%- endif -%}
    {%- if item.ROAMSGSN is not none -%}
        ROAMSGSN={{item.ROAMSGSN}},
    {%- endif -%}
    {%- if item.VISITSGSN is not none -%}
        VISITSGSN={{item.VISITSGSN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置UserProflie。如已配置UserProflie，请跳过该步骤。

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

#### 3.3 将CC绑定到UserProflie上。

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCNAME is not none -%}
        CCNAME="{{item.CCNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

