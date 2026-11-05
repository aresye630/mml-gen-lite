---
id: ''
name: 配置计费属性CC
ne_type: UEG
type: feature
description: Charging Characteristics（CC）是3GPP协议定义的一种用户签约付费属性，不属于计费功能。CC的取值有热计费(Hot Billing 0x0100)、统一费率（Flat Rate 0x0200）、预付费（Prepaid Service 0x0400）、普通计费(Normal Billing 0x0800)和自定义取值。CC可以由RADIUS Server下发，可以在UDM上签约，也可以在SMF上本地配置，SMF支持基于UserProfile、DNN、全局配置三种计费属性CC。其中，RADIUS Server下发CC优先级大于SMF本地配置，SMF上CC的优先级从高到低依次是：UserProflie下的配置 > DNN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的计费属性没有配置，则依次使用低一级别的计费属性。图1呈现了CC的选择逻辑图。  * 当UDM下发签约CC、并且本地基于UserProfile、DNN配置CC场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。 * 当UDM下发签约CC、并且本地基于全局配置CC场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地全局配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。  **图1** Charging Characteristics选择图  * 适用于SMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","配置业务数据（UEG）","计费功能配置","部署应急SMF","配置计费属性CC"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
Charging Characteristics（CC）是3GPP协议定义的一种用户签约付费属性，不属于计费功能。CC的取值有热计费(Hot Billing 0x0100)、统一费率（Flat Rate 0x0200）、预付费（Prepaid Service 0x0400）、普通计费(Normal Billing 0x0800)和自定义取值。CC可以由RADIUS Server下发，可以在UDM上签约，也可以在SMF上本地配置，SMF支持基于UserProfile、DNN、全局配置三种计费属性CC。其中，RADIUS Server下发CC优先级大于SMF本地配置，SMF上CC的优先级从高到低依次是：UserProflie下的配置 > DNN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的计费属性没有配置，则依次使用低一级别的计费属性。图1呈现了CC的选择逻辑图。* 当UDM下发签约CC、并且本地基于UserProfile、DNN配置CC场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。* 当UDM下发签约CC、并且本地基于全局配置CC场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约下发的计费属性CC。当对应参数配置为ENABLE时，表示使用UDM签约下发的CC；当配置为DISABLE时，表示使用本地全局配置的CC。从UDM获取签约CC时，SMF直接动态获取计费属性信息，与本地配置CC无关。**图1** Charging Characteristics选择图* 适用于SMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          data_source: ''
          pattern: ''
          default: ''
        VISIT:
          name: '拜访用户计费类型'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
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
          description: '本地、漫游、拜访用户的计费属性。'
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
          description: '* 当配置为ENABLE时，表示使用UDM下发的CC。 * 当配置为DISABLE时，表示使用本地配置的CC。'
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
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置DNN。可通过**LST CPAPN**命令查询已经配置的DNN。'
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '将CC绑定到DNN上。每个DNN只能绑定一个计费属性。如果DNN已绑定了计费属性，要绑定其他的计费属性，必须调用**SET APNCHARGECTRL**命令修改绑定关系。'
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
          description: '本地、漫游、拜访用户的计费属性。'
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
          description: '* 当配置为ENABLE时，表示使用UDM下发的CC。 * 当配置为DISABLE时，表示使用本地配置的CC。'
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
    add_cpuserprofile_list:
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
          data_source: ''
          pattern: ''
          default: PCC
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
      HOMESGSN: DISABLE
      ROAMSGSN: DISABLE
      VISITSGSN: DISABLE
    add_chargechar_list:
    - CCNAME: 'testchgcha'
      HOME: '0x0800'
      ROAM: '0x0800'
      VISIT: '0x0800'
      HOMESGSN: DISABLE
      ROAMSGSN: DISABLE
      VISITSGSN: DISABLE
    add_cpapn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
    set_apnchargectrl_list:
    - APN: 'apn-test'
      CCNAME: 'testchgcha'
    add_chargechar_list_1:
    - CCNAME: 'testchgcha'
      HOME: '0x0800'
      ROAM: '0x0800'
      VISIT: '0x0800'
      HOMESGSN: DISABLE
      ROAMSGSN: DISABLE
      VISITSGSN: DISABLE
    add_cpuserprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      CCNAME: 'testchgcha'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置全局CC。

#### 1.1 配置全局CC。

```jinja2
{%- if is_scenario_global_cc -%}
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
{%- endif -%}
```

### 2 配置DNN下的CC。

#### 2.1 配置CC实例。

```jinja2
{%- if is_scenario_dnn_cc -%}
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
{%- endif -%}
```

#### 2.2 配置DNN。如已配置DNN，请跳过该步骤。

```jinja2
{%- if is_scenario_dnn_cc -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 将CC绑定到DNN上。

```jinja2
{%- if is_scenario_dnn_cc -%}
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
{%- endif -%}
```

### 3 配置UserProfile下的CC。

#### 3.1 配置CC实例。

```jinja2
{%- if is_scenario_userprofile_cc -%}
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
{%- endif -%}
```

#### 3.2 配置UserProfile。如已配置UserProfile，请跳过该步骤。

```jinja2
{%- if is_scenario_userprofile_cc -%}
    {%- for item in add_cpuserprofile_list -%}
        ADD CPUSERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 将CC绑定到UserProfile上。

```jinja2
{%- if is_scenario_userprofile_cc -%}
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
{%- endif -%}
```

