---
id: ''
name: 配置离线计费费率切换（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: GGSN/SGW-C/PGW-C支持节假日、星期及其费率的灵活设置，运营商可以针对节日、周末和工作日的特定时间段设置不同的计费标准，吸引移动用户消费，增加运营商收入。  GGSN/SGW-C/PGW-C支持如下粒度配置费率切换：“UserProfile实例 > APN实例 > 计费属性CC > 整机 > 默认值”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置，如果都没有配置，则使用整机默认的缺省值。  适用于SGW-C、PGW-C、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置离线计费费率切换（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/SGW-C/PGW-C支持节假日、星期及其费率的灵活设置，运营商可以针对节日、周末和工作日的特定时间段设置不同的计费标准，吸引移动用户消费，增加运营商收入。GGSN/SGW-C/PGW-C支持如下粒度配置费率切换：“UserProfile实例 > APN实例 > 计费属性CC > 整机 > 默认值”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置，如果都没有配置，则使用整机默认的缺省值。适用于SGW-C、PGW-C、GGSN。

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
    add_festival_list:
      type: items
      properties:
        GLOBALFLG:
          name: '全局配置'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '配置指定日期的费率类型为节假日。   * 该命令可以基于计费CC配置，**计费属性CC值**不能取值为**0x0200**，因为统一费率类型的用户费率不变，不会发生费率切换。 * **global**表示全局配置，当没有配置基于CC值的节假日信息时，则对用户采用global所指定的节假日信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MONTH:
          name: '节假日月份'
          type: integer
          minimum: 1
          maximum: 12
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAY:
          name: '节假日日期'
          type: integer
          minimum: 1
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
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
        YEAR:
          name: '节假日年份'
          type: integer
          minimum: 2000
          maximum: 2099
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_weekday_list:
      type: items
      properties:
        GLOBALFLG:
          name: '全局配置'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '配置指定周日期的费率类型为工作日或周末。   * 该命令可以基于计费CC配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。**global**参数用于为全局用户配置费率切换。如果没有为用户指定工作日或周末，将使用全局的工作日或周末信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAYOFWEEK:
          name: '周日期'
          type: string
          enum:
          - FRIDAY
          - MONDAY
          - SATURDAY
          - SUNDAY
          - THURSDAY
          - TUESDAY
          - WEDNESDAY
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TARIFFTYPE:
          name: '费率类型'
          type: string
          enum:
          - WEEKEND
          - WORKDAY
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
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tariffgroup_list:
      type: items
      properties:
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GLOBALFLG:
          name: '全局配置'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '配置费率切换点。   * 该命令可以基于计费CC配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**GLOBAL**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TARIFFTYPE:
          name: '费率类型'
          type: string
          enum:
          - FESTIVAL
          - WEEKEND
          - WORKDAY
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STARTTIME:
          name: '费率切换起始时间'
          type: string
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM'
        ENDTIME:
          name: '费率切换终止时间'
          type: string
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM'
        CCMASK:
          name: 'Charge Characteristic掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glbtariffgroup_list:
      type: items
      properties:
        GLBTARIFFGRP:
          name: '费率切换组名'
          type: string
          maxLength: 31
          required: false
          description: '绑定全局费率切换组。'
          data_source: '本端规划'
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '每个APN只能绑定一个费率切换组。如果APN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET APNCHARGECTRL**命令修改原来的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          maxLength: 31
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
          description: '配置UserProfile。'
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
          description: '每个UserProfile只能绑定一个费率切换组。如果UserProfile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET USRPROFCHARGE**命令修改原来的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_festival_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      MONTH: 8
      DAY: 1
      CCMASK: ''
      CCPRIORITY: ''
      YEAR: ''
    add_weekday_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      DAYOFWEEK: MONDAY
      TARIFFTYPE: WORKDAY
      CCMASK: ''
      CCPRIORITY: ''
    add_tariffgroup_list:
    - TARIFFGRPNAME: 'testtariff'
      GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      TARIFFTYPE: WORKDAY
      STARTTIME: '06&00'
      ENDTIME: '17&00'
      CCMASK: ''
      CCPRIORITY: ''
    set_glbtariffgroup_list:
    - GLBTARIFFGRP: 'testtarif'
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      TARIFFGRPNAME: 'testtarif'
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      TARIFFGRPNAME: 'testtarif'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置费率切换。

#### 1.1 配置节假日信息，即设置指定日期的费率类型为节假日。

```jinja2
{%- for item in add_festival_list -%}
    ADD FESTIVAL:
    {#- --- 必选参数 --- -#}
    GLOBALFLG={{item.GLOBALFLG}},
    MONTH={{item.MONTH}},
    DAY={{item.DAY}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GLOBALFLG=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT/GLOBAL 时可选 --- -#}
    {%- if item.GLOBALFLG in ['CHARGE_CHARACT', 'GLOBAL'] -%}
        {%- if item.YEAR is not none -%}
            YEAR={{item.YEAR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置星期表信息，即设置指定星期的费率类型为工作日或周末。

```jinja2
{%- for item in add_weekday_list -%}
    ADD WEEKDAY:
    {#- --- 必选参数 --- -#}
    GLOBALFLG={{item.GLOBALFLG}},
    DAYOFWEEK={{item.DAYOFWEEK}},
    TARIFFTYPE={{item.TARIFFTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GLOBALFLG=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置节假日，工作日或周末的费率时间段。

```jinja2
{%- for item in add_tariffgroup_list -%}
    ADD TARIFFGROUP:
    {#- --- 必选参数 --- -#}
    TARIFFGRPNAME="{{item.TARIFFGRPNAME}}",
    GLOBALFLG={{item.GLOBALFLG}},
    TARIFFTYPE={{item.TARIFFTYPE}},
    STARTTIME={{item.STARTTIME}},
    ENDTIME={{item.ENDTIME}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GLOBALFLG=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLG == 'CHARGE_CHARACT' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置全局费率切换组。

```jinja2
{%- for item in set_glbtariffgroup_list -%}
    SET GLBTARIFFGROUP:
    {#- --- 可选参数 --- -#}
    {%- if item.GLBTARIFFGRP is not none -%}
        GLBTARIFFGRP="{{item.GLBTARIFFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置APN下的费率切换组。

#### 3.1 配置APN。如已配置APN，请跳过该步骤。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 3.2 配置APN实例下的费率切换组。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TARIFFGRPNAME is not none -%}
        TARIFFGRPNAME="{{item.TARIFFGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置UserProfile下的费率切换组。

#### 4.1 配置UserProfile。如已配置UserProfile，请跳过该步骤。

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

#### 4.2 配置UserProfile实例下的费率切换组。

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TARIFFGRPNAME is not none -%}
        TARIFFGRPNAME="{{item.TARIFFGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

