---
id: ''
name: 配置离线计费费率切换（SGSN）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持节假日、星期、费率时间段设置特性的操作过程。  SGSN支持节假日、星期、费率时间段及对应费率的灵活设置，可以记录用户在不同的费率时间段的流量，增强话单的计费信息收集功能。  * 计费节假日表用于指定国家的法定节假日以及对应的计费属性。 * 计费星期表用于指定一周中某天的费率类型为工作日费率还是周末假日费率以及对应的计费属性。 * 费率时间段表与计费节假日表和计费星期表一起使用，用于指定节假日或周末假日使用优惠费率的时间段，可以指定多个时间段，但是具有相同计费属性的时间段不允许重叠。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置离线计费费率切换（SGSN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持节假日、星期、费率时间段设置特性的操作过程。SGSN支持节假日、星期、费率时间段及对应费率的灵活设置，可以记录用户在不同的费率时间段的流量，增强话单的计费信息收集功能。* 计费节假日表用于指定国家的法定节假日以及对应的计费属性。* 计费星期表用于指定一周中某天的费率类型为工作日费率还是周末假日费率以及对应的计费属性。* 费率时间段表与计费节假日表和计费星期表一起使用，用于指定节假日或周末假日使用优惠费率的时间段，可以指定多个时间段，但是具有相同计费属性的时间段不允许重叠。适用于SGSN。

## 必备事项
前提条件

* 无特殊前提条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_chgholi_list:
      type: items
      properties:
        YEAR:
          name: '年'
          type: integer
          minimum: 1998
          maximum: 2099
          required: true
          description: '增加节假日配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MONTH:
          name: '月'
          type: integer
          minimum: 1
          maximum: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DAY:
          name: '日'
          type: integer
          minimum: 1
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgwkdy_list:
      type: items
      properties:
        WKDAY:
          name: '星期序号'
          type: string
          enum:
          - FRI
          - MON
          - SAT
          - SUN
          - THURS
          - TUES
          - WED
          required: true
          description: '设置星期配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TT:
          name: '费率类型'
          type: string
          enum:
          - WEEKEND
          - WORK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgtari_list:
      type: items
      properties:
        TT:
          name: '费率类型'
          type: string
          enum:
          - FESTIVAL
          - WEEKEND
          - WORK
          required: true
          description: '增加费率时间段配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ST:
          name: '开始时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        ET:
          name: '结束时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_chgholi_list:
    - YEAR: 2010
      MONTH: 10
      DAY: 1
      CC: NORMAL
    set_chgwkdy_list:
    - WKDAY: FRI
      CC: HOTBILLING
      TT: WEEKEND
    add_chgtari_list:
    - TT: WORK
      ST: '18&00&00'
      ET: '21&30&00'
      CC: PREPAID
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**增加节假日配置。

```jinja2
{%- if is_optional_add_holiday_config -%}
    {%- for item in add_chgholi_list -%}
        ADD CHGHOLI:
        {#- --- 必选参数 --- -#}
        YEAR={{item.YEAR}},
        MONTH={{item.MONTH}},
        DAY={{item.DAY}},
        CC={{item.CC}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**设置星期配置。

```jinja2
{%- if is_optional_set_weekday_config -%}
    {%- for item in set_chgwkdy_list -%}
        SET CHGWKDY:
        {#- --- 必选参数 --- -#}
        WKDAY={{item.WKDAY}},
        CC={{item.CC}},
        TT={{item.TT}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**增加费率时段配置。

```jinja2
{%- if is_optional_add_rate_period_config -%}
    {%- for item in add_chgtari_list -%}
        ADD CHGTARI:
        {#- --- 必选参数 --- -#}
        TT={{item.TT}},
        ST={{item.ST}},
        ET={{item.ET}},
        CC={{item.CC}},
        ;
    {%- endfor -%}
{%- endif -%}
```

