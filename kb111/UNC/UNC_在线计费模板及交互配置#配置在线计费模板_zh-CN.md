---
id: ''
name: 配置在线计费模板
ne_type: UNC
type: feature
description: 本指导描述在UNC上配置在线计费模板的相关操作过程。  在线计费模板是用来绑定在线计费本地配置参数的，在线计费DCC模板分为全局通用参数模板global和普通的模板DCC Template，前者用于配置整机通用的在线计费参数，后者用于配置特殊场景下的在线计费参数。  在线计费参数中，除了OCS的基本信息是基于全局配置的之外，其他的参数，如要使用的OCS服务器、CCR触发场景、DCC处理动作、CCR消息中携带的参数等都可以选择基于整机或特殊场景生效。  UNC支持以下几种粒度范围的在线计费参数配置：  * 支持配置整机通用参数。 * 支持根据用户计费属性Charging Characteristics配置在线计费参数。 * 支持根据APN配置在线计费参数。 * 支持根据User Profile配置在线计费参数。  上述几种粒度范围的优先级从高到低依次是：User Profile下的配置–〉APN下的配置–〉计费属性下的配置–〉整机通用参数。如果高级别的参数没有配置或者配置为inherit，则依次向下继承低一级别的参数取值。整机通用参数配置在global模板中，其他几种粒度都配置在DCC Template中，并进而跟随DCC Template绑定其生效的范围：某一计费属性、APN、或者User Profile。  在线计费参数的配置粒度，建议与在线计费使能的粒度保持一致，即如果基于APN开启在线计费功能，同样基于APN配置在线计费参数，这样可以避免各配置参数生效范围冲突和不一致。一旦确定了整个系统的在线计费参数配置粒度，则所有在线计费参数的配置原则上都必须统一使用该粒度。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述在UNC上配置在线计费模板的相关操作过程。在线计费模板是用来绑定在线计费本地配置参数的，在线计费DCC模板分为全局通用参数模板global和普通的模板DCC Template，前者用于配置整机通用的在线计费参数，后者用于配置特殊场景下的在线计费参数。在线计费参数中，除了OCS的基本信息是基于全局配置的之外，其他的参数，如要使用的OCS服务器、CCR触发场景、DCC处理动作、CCR消息中携带的参数等都可以选择基于整机或特殊场景生效。UNC支持以下几种粒度范围的在线计费参数配置：* 支持配置整机通用参数。* 支持根据用户计费属性Charging Characteristics配置在线计费参数。* 支持根据APN配置在线计费参数。* 支持根据User Profile配置在线计费参数。上述几种粒度范围的优先级从高到低依次是：User Profile下的配置–〉APN下的配置–〉计费属性下的配置–〉整机通用参数。如果高级别的参数没有配置或者配置为inherit，则依次向下继承低一级别的参数取值。整机通用参数配置在global模板中，其他几种粒度都配置在DCC Template中，并进而跟随DCC Template绑定其生效的范围：某一计费属性、APN、或者User Profile。在线计费参数的配置粒度，建议与在线计费使能的粒度保持一致，即如果基于APN开启在线计费功能，同样基于APN配置在线计费参数，这样可以避免各配置参数生效范围冲突和不一致。一旦确定了整个系统的在线计费参数配置粒度，则所有在线计费参数的配置原则上都必须统一使用该粒度。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
* 完成加载license。
* 已完成计费属性、APN、User Profile创建。
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
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。  说明：  如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
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
          description: '基于计费属性绑定在线计费模板。'
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '基于APN绑定DCC模板。  说明：  APN通过**ADD APN**命令创建。'
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
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '基于User Profile绑定DCC模板。  说明：  User Profile通过**ADD USERPROFILE**命令创建。'
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
  examples:
    mod_dcctemplate_list:
    - DCCTMPLTNAME: ''
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
    add_glbdcctemplate_list:
    - CHARGECHARACT: CHARGE_CHARACT
      SPECIFICCCVALUE: '0x0800'
      DCCTEMPLATENAME: 'dcc-test'
      MASK: ''
      PRIORITY: ''
    set_apnchargectrl_list:
    - APN: 'apn-test'
      DCCTEMPLATE: 'dcc-test'
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      DCCTEMPLATE: 'dcc-test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置DCC Template模板。重复执行本步骤可增加多个DCC Template模板。

#### 1.1 配置全局通用参数DCC模板。

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

### 2 配置DCC Template模板绑定到计费属性。

```jinja2
{%- if is_scenario_charging_characteristics -%}
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
{%- endif -%}
```

### 3 配置DCC Template模板绑定APN实例。

```jinja2
{%- if is_scenario_apn -%}
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
{%- endif -%}
```

### 4 配置DCC Template模板绑定User Profile实例。

```jinja2
{%- if is_scenario_user_profile -%}
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
{%- endif -%}
```

