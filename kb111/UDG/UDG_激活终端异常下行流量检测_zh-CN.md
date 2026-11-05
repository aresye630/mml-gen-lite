---
id: GWFD-020305
name: 激活终端异常下行流量检测
ne_type: UDG
type: feature
description: 需要开启终端异常下行流量检测功能时，执行此任务。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","业务感知功能","GWFD-020305 终端异常下行流量检测","激活终端异常下行流量检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
需要开启终端异常下行流量检测功能时，执行此任务。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020305 终端异常下行流量检测特性概述。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
* 完成配置APN。
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
    add_abntrafficdt_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APN名称已经通过命令**ADD APN**进行配置。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TRAFFICBEHAVIORSWITCH:
          name: '基于流行为的检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5ADTD01'
      SWITCH: ENABLE
    add_abntrafficdt_list:
    - APN: 'apn1.com'
      SWITCH: ENABLE
      TRAFFICBEHAVIORSWITCH: ENABLE
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

### 2 配置APN下使能终端异常下行流量检测功能。

```jinja2
{%- for item in add_abntrafficdt_list -%}
    ADD ABNTRAFFICDT:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.TRAFFICBEHAVIORSWITCH is not none -%}
            TRAFFICBEHAVIORSWITCH={{item.TRAFFICBEHAVIORSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

