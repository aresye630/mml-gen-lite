---
id: ''
name: 配置费率切换
ne_type: UEG
type: feature
description: SMF支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在SMF上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。  SMF支持如下粒度配置费率切换：“UserProfile实例 > APN实例 > 计费属性CC > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置业务数据（风筝M）","配置业务数据（UEG）","计费功能配置","部署应急SMF","配置费率切换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
SMF支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在SMF上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。SMF支持如下粒度配置费率切换：“UserProfile实例 > APN实例 > 计费属性CC > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_tariffgroup_list:
      type: items
      properties:
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          maxLength: 31
          required: true
          description: '配置费率切换点。   * 该命令可以基于计费CC配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的**计费属性CC值**不能取值为**0x0200**。**global**参数用于为全局用户配置费率切换。如果没有为用户指定费率切换点，则使用全局的费率切换点信息。SMF根据计费类型获取费率切换点信息。如果对应某一计费类型的费率切换点没有配置，将使用全局的费率切换点信息。'
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
  examples:
    add_festival_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      MONTH: 8
      DAY: 1
    add_weekday_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      DAYOFWEEK: MONDAY
      TARIFFTYPE: WORKDAY
    add_tariffgroup_list:
    - TARIFFGRPNAME: 'tar_nb'
      GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      TARIFFTYPE: WORKDAY
      STARTTIME: '06&00'
      ENDTIME: '17&00'
    set_n40quotactrl_list:
    - TCMODE: Default
    set_glbtariffgroup_list:
    - GLBTARIFFGRP: 'tar_nb'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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
    ;
{%- endfor -%}
```

#### 1.4 **可选**：配置费率切换模式。

```jinja2
{%- if is_optional_rate_switch_mode -%}
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

#### 当“TCMODE”参数配置为“Default”时，表示费率切换发生的时间点按照**ADD TARIFFGROUP**命令配置的费率切换生效。

#### 当“TCMODE”参数配置为“Daily”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，每天00：00再强制进行费率切换，生效范围为所有用户。

#### 当“TCMODE”参数配置为“Monthly”时，表示在**ADD TARIFFGROUP**命令的费率切换配置基础上，月初第一天00：00再强制进行费率切换，生效范围为所有用户。

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

