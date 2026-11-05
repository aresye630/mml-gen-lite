---
id: ''
name: 开启特性License开关
ne_type: UNC
type: feature
description: 本章节指导如何开启内生安全的特性License配置开关。  适用于AMF、SMF、NSSF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","安全管理功能","WSFD-219000 内生安全","激活内生安全","开启特性License开关"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节指导如何开启内生安全的特性License配置开关。适用于AMF、SMF、NSSF。

## 必备事项
前提条件

* 请仔细阅读内生安全概述、WSFD-219002 OS面入侵检测、WSFD-219003 恶意文件检测、WSFD-219004 资产风险管理和WSFD-219005 微隔离。
* 完成加载License。
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
          description: '开启内生安全的特性License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '开启内生安全的特性License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '开启内生安全的特性License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_3:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '开启内生安全的特性License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2OSDFUNC01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2MFDFUNC01'
      SWITCH: ENABLE
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2ARMFUNC01'
      SWITCH: ENABLE
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2MSFUNC01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 开启内生安全的特性License配置开关。

#### 2.2 //（可选）开启WSFD-219002 OS面入侵检测的License配置开关。

```jinja2
{%- if is_optional_os_intrusion_detection -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 //（可选）开启WSFD-219003 恶意文件检测的License配置开关。

```jinja2
{%- if is_optional_malware_detection -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 //（可选）开启WSFD-219004 资产风险管理的License配置开关。

```jinja2
{%- if is_optional_asset_risk_management -%}
    {%- for item in set_licenseswitch_list_2 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 //（可选）开启WSFD-219005 微隔离的License配置开关。

```jinja2
{%- if is_optional_micro_isolation -%}
    {%- for item in set_licenseswitch_list_3 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

