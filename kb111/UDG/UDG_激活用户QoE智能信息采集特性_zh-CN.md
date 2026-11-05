---
id: GWFD-111526
name: 激活用户QoE智能信息采集特性
ne_type: UDG
type: feature
description: 当运营商需要采集签约了业务体验感知套餐的重点用户和普通抽样用户这两类用户群的智能业务体验感知信息时，需要配置本页面。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","重点业务体验保障功能","GWFD-111526 用户QoE智能信息采集","激活用户QoE智能信息采集特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要采集签约了业务体验感知套餐的重点用户和普通抽样用户这两类用户群的智能业务体验感知信息时，需要配置本页面。

## 必备事项
前提条件

* 请仔细阅读GWFD-111525 重点用户QoE智能监测和保障特性概述。
* 使用用户QoE智能信息采集特性时，需要确保已完成CoreMind与IISA可选服务的安装，请参考安装CoreMind服务、安装IISA服务。
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
          description: '开启用户QoE智能信息采集的License控制项。'
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
    set_qoebasicfunc_list:
      type: items
      properties:
        QOESWITCH:
          name: 'QoE分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置基于智能业务感知进行QoE推理。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        INQOESWITCH:
          name: 'QoE智能分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ENABLE
        MODE:
          name: '运行模式'
          type: string
          enum:
          - SSU
          - IISA
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: SSU
    set_iisabasicfunc_list:
      type: items
      properties:
        SWITCH:
          name: '分析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置智能业务感知智能推理开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_expbasicfunc_list:
      type: items
      properties:
        SWITCH:
          name: '体验分析基本功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置开启体验业务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANARPTPERIOD:
          name: '体验业务上报周期（秒）'
          type: integer
          minimum: 30
          maximum: 600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVPORT:
          name: '体验业务上报的服务器端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CATEGORYRPT:
          name: '应用大类上报'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置基于应用大类的上报体验单据的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXPSAMPLEPERIOD:
          name: '体验单据采集周期（秒）'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5EXPQ01'
      SWITCH: ENABLE
    set_qoebasicfunc_list:
    - QOESWITCH: ENABLE
      INQOESWITCH: ENABLE
      MODE: IISA
    set_iisabasicfunc_list:
    - SWITCH: ENABLE
    set_expbasicfunc_list:
    - SWITCH: ENABLE
      ANARPTPERIOD: 300
      SRVPORT: 15000
      CATEGORYRPT: ENABLE
      EXPSAMPLEPERIOD: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 打开QoE模型子类开关。

```jinja2
{%- for item in set_qoebasicfunc_list -%}
    SET QOEBASICFUNC:
    {#- --- 必选参数 --- -#}
    QOESWITCH={{item.QOESWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：QOESWITCH=ENABLE 时可选 --- -#}
    {%- if item.QOESWITCH == 'ENABLE' -%}
        {%- if item.INQOESWITCH is not none -%}
            INQOESWITCH={{item.INQOESWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：QOESWITCH=ENABLE 时可选 --- -#}
    {%- if item.QOESWITCH == 'ENABLE' -%}
        {%- if item.MODE is not none -%}
            MODE={{item.MODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开业务识别模型子类开关。

```jinja2
{%- for item in set_iisabasicfunc_list -%}
    SET IISABASICFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 开启应用大类模型子类相关配置。

```jinja2
{%- for item in set_expbasicfunc_list -%}
    SET EXPBASICFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.ANARPTPERIOD is not none -%}
            ANARPTPERIOD={{item.ANARPTPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.SRVPORT is not none -%}
            SRVPORT={{item.SRVPORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.CATEGORYRPT is not none -%}
            CATEGORYRPT={{item.CATEGORYRPT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.EXPSAMPLEPERIOD is not none -%}
            EXPSAMPLEPERIOD={{item.EXPSAMPLEPERIOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

