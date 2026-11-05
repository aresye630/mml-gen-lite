---
id: ''
name: 激活基于TA List的寻呼自动流控（适用于MME）
ne_type: UNC
type: feature
description: 本操作指导在运行网络中激活基于TA List的寻呼自动流控功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010901 基于TA List的寻呼自动流控","WSFD-010901 基于TA List的寻呼自动流控（适用于MME）","激活基于TA List的寻呼自动流控（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导在运行网络中激活基于TA List的寻呼自动流控功能。

## 必备事项
前提条件

* 请仔细阅读WSFD-010901 基于TA List的寻呼自动流控特性概述（适用于MME）和实现原理（适用于MME）。
* MME已对接网管系统，并且在网管上创建5分钟周期的性能测量任务，并勾选如下指标和待监控的测量对象：
  + 117494562 指定TAI组的S1模式寻呼请求次数
  + 117494414 指定TAI组的S1模式寻呼成功率
  + 117494413 指定TAI组的S1模式二次寻呼请求次数
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_s1taipagmonpara_list:
      type: items
      properties:
        SWITCH:
          name: 'TAI寻呼异常监控开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: '设置S1 TAI组对象寻呼异常监控功能参数。  说明：  除“寻呼最大重试次数”、“语音业务TAI寻呼流控开关”和“告警开关”参数外，本命令的其它任何参数修改都会导致学习到的基准值被清除，已经发生的流控被取消，待MME重新检测到指标异常后再次进行流控。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAGSUCRATDEFVAL:
          name: 'S1模式TAI组寻呼成功率初始值（%）'
          type: integer
          minimum: 20
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MINPAGREQTHD:
          name: 'S1模式TAI组寻呼请求次数起始监控阈值'
          type: integer
          minimum: 100
          maximum: 100000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAGRATEEXPTHD:
          name: 'S1模式TAI组寻呼成功率降幅阈值（%）'
          type: integer
          minimum: 1
          maximum: 80
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAGREQEXPTHD:
          name: 'S1模式TAI组二次寻呼请求次数增幅阈值（%）'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAGEXPTIMESTHD:
          name: 'TAI寻呼消息启控连续异常周期个数'
          type: integer
          minimum: 1
          maximum: 5
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAGRETRYTIMES:
          name: '寻呼最大重试次数'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSPAGINGSW:
          name: '语音业务TAI寻呼流控开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALARMSW:
          name: '告警开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_s1taipagmonpara_list:
    - SWITCH: ON
      PAGSUCRATDEFVAL: 90
      MINPAGREQTHD: 1000
      PAGRATEEXPTHD: 5
      PAGREQEXPTHD: 50
      PAGEXPTIMESTHD: 1
      PAGRETRYTIMES: 0
      IMSPAGINGSW: ON
      ALARMSW: ON
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 参考激活分区域网络运维配置S1 TAI组测量对象。

### 2 设置S1 TAI组对象寻呼异常监控功能参数。

```jinja2
{%- for item in set_s1taipagmonpara_list -%}
    SET S1TAIPAGMONPARA:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PAGSUCRATDEFVAL is not none -%}
            PAGSUCRATDEFVAL={{item.PAGSUCRATDEFVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.MINPAGREQTHD is not none -%}
            MINPAGREQTHD={{item.MINPAGREQTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PAGRATEEXPTHD is not none -%}
            PAGRATEEXPTHD={{item.PAGRATEEXPTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PAGREQEXPTHD is not none -%}
            PAGREQEXPTHD={{item.PAGREQEXPTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PAGEXPTIMESTHD is not none -%}
            PAGEXPTIMESTHD={{item.PAGEXPTIMESTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.PAGRETRYTIMES is not none -%}
            PAGRETRYTIMES={{item.PAGRETRYTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.IMSPAGINGSW is not none -%}
            IMSPAGINGSW={{item.IMSPAGINGSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ON 时可选 --- -#}
    {%- if item.SWITCH == 'ON' -%}
        {%- if item.ALARMSW is not none -%}
            ALARMSW={{item.ALARMSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

