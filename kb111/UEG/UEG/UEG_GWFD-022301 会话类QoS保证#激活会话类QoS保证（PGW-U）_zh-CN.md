---
id: GWFD-022301
name: 激活会话类QoS保证（PGW-U）
ne_type: UEG
type: feature
description: 当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。  适用于PGW-U。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","QoS功能","GWFD-022301 会话类QoS保证","激活会话类QoS保证（PGW-U）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当移动IP网络中部署了具有实时性特点的会话类业务时，要求移动IP网络转发时延低、抖动小，因此需要提供端到端的QoS保证。适用于PGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-022301 会话类QoS保证。
* 已申请特性所需的License控制项。
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
          description: '打开本特性的License配置开关。'
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '说明：  Tunnel marking与Alias marking同时配置时，Alias Marking不生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'Alias Marking使能标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPESWUL:
          name: '上行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEUL:
          name: '上行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPESWDL:
          name: '下行Qos开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEDL:
          name: '下行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_qoscar_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - HOME
          - ROAMING
          - VISITING
          required: true
          description: '建议默认开启QoSCar功能，避免出现异常大话单。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULRAT:
          name: '上行RAT类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_qosshape_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - HOME
          - ROAMING
          - VISITING
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULRAT:
          name: '上行RAT类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TCQS01'
      SWITCH: ENABLE
    add_userprofile_list:
    - USERPROFILENAME: 'profile1'
      ALIASMARKFLAG: ENABLE
    add_apn_list:
    - APN: 'apn1'
    set_apnqosattr_list:
    - APN: 'apn1'
      CARSHAPESWUL: ENABLE
      CARSHAPEUL: CAR
      CARSHAPESWDL: ENABLE
      CARSHAPEDL: CAR
    set_qoscar_list:
    - USERTYPE: ROAMING
      ULRAT: geran-1
    set_qosshape_list:
    - USERTYPE: VISITING
      ULRAT: geran-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置Alias Marking使能标记，缺省使用默认值。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ALIASMARKFLAG is not none -%}
        ALIASMARKFLAG={{item.ALIASMARKFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置带宽控制功能。

#### 3.1 配置APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 3.2 配置带宽控制功能。

```jinja2
{%- for item in set_apnqosattr_list -%}
    SET APNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CARSHAPESWUL is not none -%}
        CARSHAPESWUL={{item.CARSHAPESWUL}},
    {%- endif -%}
    {%- if item.CARSHAPESWDL is not none -%}
        CARSHAPESWDL={{item.CARSHAPESWDL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CARSHAPESWUL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWUL == 'ENABLE' -%}
        CARSHAPEUL={{item.CARSHAPEUL}},
    {%- endif -%}
    {#- --- 条件必选：CARSHAPESWDL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWDL == 'ENABLE' -%}
        CARSHAPEDL={{item.CARSHAPEDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**使能QoS的CAR功能。

```jinja2
{%- if is_optional_enable_qos_car -%}
    {%- for item in set_qoscar_list -%}
        SET QOSCAR:
        {#- --- 必选参数 --- -#}
        USERTYPE={{item.USERTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ULRAT is not none -%}
            ULRAT={{item.ULRAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置用户上下行shaping功能的全局开关。

```jinja2
{%- if is_optional_user_ul_dl_shaping_global_switch -%}
    {%- for item in set_qosshape_list -%}
        SET QOSSHAPE:
        {#- --- 必选参数 --- -#}
        USERTYPE={{item.USERTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ULRAT is not none -%}
            ULRAT={{item.ULRAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

