---
id: ''
name: 配置费率切换
ne_type: UNC
type: feature
description: UNC支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在UNC上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。  UNC支持如下粒度配置费率切换：“User Profile实例 > APN实例 > 计费属性 > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案","SMF配置","配置费率切换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在UNC上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。UNC支持如下粒度配置费率切换：“User Profile实例 > APN实例 > 计费属性 > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。

## 必备事项
前提条件

* 请仔细阅读融合计费原理和Ga/Gy接口离线/在线计费。
* 完成加载License。
* 本操作任务涉及的APN/DNN、User Profile、User Profile group已经创建完成，并完成User Profile group与APN/DNN的绑定。
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
          description: '配置指定日期的费率类型为节假日。   * 该命令可以基于计费属性配置，“CCVALUE”不能取值为“0x0200”，因为统一费率类型的用户费率不变，不会发生费率切换。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性的节假日信息优先级高于全局计费属性的节假日信息。'
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
          description: '配置计费星期表记录，指定每周日期的费率类型为工作日或周末。   * 该命令可以基于计费属性配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性的计费星期表记录优先级高于全局计费属性的计费星期表记录。'
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
          description: '配置费率切换点。   * 该命令可以基于计费属性配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的“CCVALUE”不能取值为“0x0200”。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性配置的费率切换点优先级高于全局计费属性的费率切换点。'
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
          description: ''
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
    set_n40quotactrl_list:
      type: items
      properties:
        TCMODE:
          name: '费率切换模式'
          type: string
          enum:
          - DEFAULT
          - DAILY
          - MONTHLY
          required: false
          description: '费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。'
          data_source: '本端规划'
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
          description: '配置全局费率切换组。'
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
          description: '每个DNN只能绑定一个费率切换组。如果DNN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET APNCHARGECTRL**命令修改原来的绑定关系。'
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
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '每个User Profile只能绑定一个费率切换组。如果User Profile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET USRPROFCHARGE**命令修改原来的绑定关系。'
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
    - TARIFFGRPNAME: 'tar_nb'
      GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      TARIFFTYPE: WORKDAY
      STARTTIME: '07&00'
      ENDTIME: '23&00'
      CCMASK: ''
      CCPRIORITY: ''
    set_n40quotactrl_list:
    - TCMODE: DEFAULT
    set_glbtariffgroup_list:
    - GLBTARIFFGRP: 'tar_nb'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      TARIFFGRPNAME: 'tar_nb'
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      TARIFFGRPNAME: 'tar_nb'
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

#### 1.4 **可选**：配置费率切换模式。

```jinja2
{%- if is_optional_tariff_switch_mode -%}
    {%- for item in set_n40quotactrl_list -%}
        SET N40QUOTACTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.TCMODE is not none -%}
            TCMODE={{item.TCMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 当“TCMODE”参数配置为“DEFAULT”时，表示费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。

#### 当“TCMODE”参数配置为“DAILY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，每天00：00再强制进行费率切换，生效范围为所有用户。

#### 当“TCMODE”参数配置为“MONTHLY”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。

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

### 3 为APN实例绑定费率切换组。

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

### 4 为User Profile实例绑定费率切换组。

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

