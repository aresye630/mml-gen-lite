---
id: ''
name: 激活模块级KPI异常检测与恢复
ne_type: UNC
type: feature
description: 本操作用于指导在运行网络中激活模块级KPI异常检测与恢复特性。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","可靠性功能","WSFD-010808 模块级KPI异常检测与恢复","激活模块级KPI异常检测与恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在运行网络中激活模块级KPI异常检测与恢复特性。

## 必备事项
前提条件

* 请仔细阅读WSFD-010808 模块级KPI异常检测与恢复特性概述。
* 已完成网元License加载。
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    set_cfshealctrl_list:
      type: items
      properties:
        SGLSUBHEALTHSW:
          name: '模块级KPI异常检测与恢复功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '用于控制由于网元内单主机出现Fabric丢包/cpu过载故障而导致KPI下降满足阈值时做对应自愈隔离处理的功能开关。  说明：  本开关和License必须同时打开，模块级KPI异常检测与恢复功能才能开启。若只打开本开关，则触发CE信令风暴检测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DETNUM:
          name: '连续检测周期'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIFFTHR:
          name: '差值（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FAULTTHR:
          name: '异常阈值（%）'
          type: integer
          minimum: 50
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGLISOMODE:
          name: '模块级KPI异常检测与恢复功能隔离策略'
          type: string
          enum:
          - MANUAL
          - AUTOMATIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGLSUBWAITTIME:
          name: '诊断隔离处理等待时间（秒）'
          type: integer
          minimum: 1
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2MKEDAR01'
      SWITCH: ENABLE
    set_cfshealctrl_list:
    - SGLSUBHEALTHSW: ENABLE
      DETNUM: ''
      DIFFTHR: ''
      FAULTTHR: ''
      SGLISOMODE: ''
      SGLSUBWAITTIME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 开启License项配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 开启模块级KPI异常检测与恢复功能。

```jinja2
{%- for item in set_cfshealctrl_list -%}
    SET CFSHEALCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.SGLSUBHEALTHSW is not none -%}
        SGLSUBHEALTHSW={{item.SGLSUBHEALTHSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SGLSUBHEALTHSW=ENABLE 时可选 --- -#}
    {%- if item.SGLSUBHEALTHSW == 'ENABLE' -%}
        {%- if item.DETNUM is not none -%}
            DETNUM={{item.DETNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SGLSUBHEALTHSW=ENABLE 时可选 --- -#}
    {%- if item.SGLSUBHEALTHSW == 'ENABLE' -%}
        {%- if item.DIFFTHR is not none -%}
            DIFFTHR={{item.DIFFTHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SGLSUBHEALTHSW=ENABLE 时可选 --- -#}
    {%- if item.SGLSUBHEALTHSW == 'ENABLE' -%}
        {%- if item.FAULTTHR is not none -%}
            FAULTTHR={{item.FAULTTHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SGLSUBHEALTHSW=ENABLE 时可选 --- -#}
    {%- if item.SGLSUBHEALTHSW == 'ENABLE' -%}
        {%- if item.SGLISOMODE is not none -%}
            SGLISOMODE={{item.SGLISOMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SGLSUBHEALTHSW=ENABLE 时可选 --- -#}
    {%- if item.SGLSUBHEALTHSW == 'ENABLE' -%}
        {%- if item.SGLSUBWAITTIME is not none -%}
            SGLSUBWAITTIME={{item.SGLSUBWAITTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

