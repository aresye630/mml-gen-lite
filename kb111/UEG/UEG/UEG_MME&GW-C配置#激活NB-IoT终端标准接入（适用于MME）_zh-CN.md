---
id: ''
name: 激活NB-IoT终端标准接入（适用于MME）
ne_type: UEG
type: feature
description: 本特性支持NB-IoT（NarrowBand Internet of Things）制式终端通过NB-IoT RAN接入MME，实现对NB-IoT终端的移动性管理与会话管理。  适用于MME。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","NB-IoT功能配置","MME&GW-C配置","激活NB-IoT终端标准接入（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本特性支持NB-IoT（NarrowBand Internet of Things）制式终端通过NB-IoT RAN接入MME，实现对NB-IoT终端的移动性管理与会话管理。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026101 NB-IoT终端标准接入特性概述（适用于MME）。
* 已完成激活S-GW/P-GW拓扑选择特性和配置到MSC的数据（SGs接口）。
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
    set_dmcmpt_list:
      type: items
      properties:
        NBIOTRAT:
          name: '是否支持NBIoT RAT'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: '设置Diameter兼容性参数，保证网元间支持信元的兼容性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2NBPS01'
      SWITCH: ENABLE
    set_dmcmpt_list:
    - NBIOTRAT: SUPPORT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选：**配置S6a接口兼容性策略。

```jinja2
{%- if is_optional_s6a_interface_compatibility_policy -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.NBIOTRAT is not none -%}
            NBIOTRAT={{item.NBIOTRAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当对端HSS不支持NB-IoT RAT时，则将参数“NBIOTRAT（是否支持NBIoT RAT）”设置为“NOT\_SUPPORT”，此时系统对终端的接入控制将不考虑从HSS获取的签约数据。

