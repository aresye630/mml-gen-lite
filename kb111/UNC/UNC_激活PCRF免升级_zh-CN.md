---
id: ''
name: 激活PCRF免升级
ne_type: UNC
type: feature
description: 在部署NB-IoT业务时，为实现PCRF免升级即可支持NB-IoT用户接入，需要开启该功能。  适用于PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-215302 PCRF免升级","激活PCRF免升级"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在部署NB-IoT业务时，为实现PCRF免升级即可支持NB-IoT用户接入，需要开启该功能。适用于PGW-C。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-215302 PCRF免升级特性概述。
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
    set_nbiotratvalue_list:
      type: items
      properties:
        PCRF:
          name: '和PCRF交互使用的RAT值'
          type: string
          enum:
          - EUTRAN
          - EUTRAN_NB_IOT
          required: false
          description: 'PCRF免升级功能'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WNPUNN11'
      SWITCH: ENABLE
    set_nbiotratvalue_list:
    - PCRF: EUTRAN
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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

### 3 配置开启PCRF免升级功能。

```jinja2
{%- for item in set_nbiotratvalue_list -%}
    SET NBIOTRATVALUE:
    {#- --- 可选参数 --- -#}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

