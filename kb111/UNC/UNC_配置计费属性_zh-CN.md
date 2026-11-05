---
id: ''
name: 配置计费属性
ne_type: UNC
type: feature
description: 本指导描述计费属性的相关配置过程。  计费属性Charging Characteristics（CC）是3GPP协议定义的一种用户签约付费属性，不属于计费功能。计费属性的取值有热计费(Hot Billing 0x0100)、统一费率（Flat Rate 0x0200）、预付费（Prepaid Service 0x0400）、普通计费(Normal Billing 0x0800)和自定义取值。  计费属性可以由RADIUS Server下发，可以在UDM\HSS\HLR上签约，也可以在UNC上本地配置，UNC支持基于User Profile、DNN、全局配置三种计费属性。其中，RADIUS Server下发计费属性优先级高于UNC本地配置（通过配置可以决定使用签约的计费属性还是本地配置的计费属性），UNC上配置的计费属性的优先级从高到低依次是：UserProflie下的配置 > DNN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的计费属性没有配置，则依次使用低一级别的计费属性。  图1呈现了计费属性的选择逻辑图。  **图1** Charging Characteristics选择图  * 当UDM下发签约计费属性（或者2/3/4G会话激活请求中携带了计费属性）、并且本地基于User Profile、DNN配置计费属性场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约的计费属性。当对应参数配置为ENABLE时，表示使用UDM签约下发的计费属性（或者2/3/4G会话激活请求中携带了计费属性）；当配置为DISABLE时，表示使用本地配置的计费属性。 * 当UDM下发签约计费属性（或者2/3/4G会话激活请求中携带了计费属性）、并且本地基于全局配置计费属性场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约的计费属性。当对应参数配置为ENABLE时，表示使用UDM签约下发的计费属性（或者2/3/4G会话激活请求中携带了计费属性）；当配置为DISABLE时，表示使用本地全局配置的计费属性。  * SMF根据本地配置的计费属性选择NCG/CHF(OCS)时，需要配置计费属性。 * 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带计费属性（MME从HSS获取的签约计费属性）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带计费属性（MME从HSS获取的签约计费属性），当UNC单独作为PGW-C时由左侧SGW-C携带计费属性（SGW-C通过MME得到签约计费属性）。即4G网络中签约计费属性由左侧MME/SGW-C携带。 * 2/3G网络中，UNC作为GGSN，由左侧SGSN携带签约计费属性（SGSN从HLR获取得签约计费属性）。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","SMF配置","配置计费属性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述计费属性的相关配置过程。计费属性Charging Characteristics（CC）是3GPP协议定义的一种用户签约付费属性，不属于计费功能。计费属性的取值有热计费(Hot Billing 0x0100)、统一费率（Flat Rate 0x0200）、预付费（Prepaid Service 0x0400）、普通计费(Normal Billing 0x0800)和自定义取值。计费属性可以由RADIUS Server下发，可以在UDM\HSS\HLR上签约，也可以在UNC上本地配置，UNC支持基于User Profile、DNN、全局配置三种计费属性。其中，RADIUS Server下发计费属性优先级高于UNC本地配置（通过配置可以决定使用签约的计费属性还是本地配置的计费属性），UNC上配置的计费属性的优先级从高到低依次是：UserProflie下的配置 > DNN下的配置 > 全局配置 > normal（缺省：普通计费）。如果高级别的计费属性没有配置，则依次使用低一级别的计费属性。图1呈现了计费属性的选择逻辑图。**图1** Charging Characteristics选择图* 当UDM下发签约计费属性（或者2/3/4G会话激活请求中携带了计费属性）、并且本地基于User Profile、DNN配置计费属性场景下，由**ADD CHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约的计费属性。当对应参数配置为ENABLE时，表示使用UDM签约下发的计费属性（或者2/3/4G会话激活请求中携带了计费属性）；当配置为DISABLE时，表示使用本地配置的计费属性。* 当UDM下发签约计费属性（或者2/3/4G会话激活请求中携带了计费属性）、并且本地基于全局配置计费属性场景下，由**SET GLBCHARGECHAR**命令的HOMESGSN、ROAMSGSN、VISITSGSN控制本地、漫游、拜访用户是否使用签约的计费属性。当对应参数配置为ENABLE时，表示使用UDM签约下发的计费属性（或者2/3/4G会话激活请求中携带了计费属性）；当配置为DISABLE时，表示使用本地全局配置的计费属性。* SMF根据本地配置的计费属性选择NCG/CHF(OCS)时，需要配置计费属性。* 4G网络中，在SP合设场景，即UNC作为SGW-C和PGW-C时，由左侧MME携带计费属性（MME从HSS获取的签约计费属性）；在SP分离部署场景，当UNC单独作为SGW-C时由左侧MME携带计费属性（MME从HSS获取的签约计费属性），当UNC单独作为PGW-C时由左侧SGW-C携带计费属性（SGW-C通过MME得到签约计费属性）。即4G网络中签约计费属性由左侧MME/SGW-C携带。* 2/3G网络中，UNC作为GGSN，由左侧SGSN携带签约计费属性（SGSN从HLR获取得签约计费属性）。

## 必备事项
前提条件

* 请仔细阅读融合计费原理和Ga/Gy接口离线/在线计费。
* 完成加载License。
* 已完成APN、User Profile创建。
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
          description: '配置全局计费属性。'
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
          description: '配置计费属性实例。'
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
          description: '* 当配置为ENABLE时，表示使用UDM下发的计费属性。 * 当配置为DISABLE时，表示使用本地配置的计费属性。'
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '将计费属性绑定到DNN上。每个DNN只能绑定一个计费属性。如果DNN已绑定了计费属性，要绑定其他的计费属性，必须调用**SET APNCHARGECTRL**命令修改绑定关系。'
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
          description: '配置计费属性实例。'
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
          description: '* 当配置为ENABLE时，表示使用UDM下发的计费属性。 * 当配置为DISABLE时，表示使用本地配置的计费属性。'
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
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将计费属性绑定到User Proflie上。每个User Proflie只能绑定一个计费属性。如果User Proflie已绑定了计费属性，要绑定其他的计费属性，必须调用**SET USRPROFCHARGE**命令修改绑定关系。'
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
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      CCNAME: 'testchgcha'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置全局计费属性。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置全局计费属性。如已配置全局计费属性，请跳过该步骤。

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

### 2 配置DNN下的计费属性。

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 配置计费属性实例。

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

#### 2.3 将计费属性绑定到DNN上。

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

### 3 配置User Profile下的计费属性。

#### 3.1 进入“MML命令行-UNC”窗口。

#### 3.2 配置计费属性实例。

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

#### 3.3 将计费属性绑定到User Profile上。

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

