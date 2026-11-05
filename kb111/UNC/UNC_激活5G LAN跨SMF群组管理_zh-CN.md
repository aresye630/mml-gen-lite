---
id: ''
name: 激活5G LAN跨SMF群组管理
ne_type: UNC
type: feature
description: '* 新建CU FullMesh组网。 * 已有网络新改造成CU FullMesh组网。'
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","5G LAN解决方案","WSFD-225002 5G LAN跨SMF群组管理","激活5G LAN跨SMF群组管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* 新建CU FullMesh组网。* 已有网络新改造成CU FullMesh组网。

## 必备事项
前提条件

前提条件

前提条件

* 请仔细阅读WSFD-225002 5G LAN跨SMF群组管理特性概述。
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
    set_addressattr_list:
      type: items
      properties:
        ALLOCPRECEDENCE:
          name: 'UE地址分配属性'
          type: string
          enum:
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: '设置UE地址分配方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_reselectupcause_list:
      type: items
      properties:
        FAULTCAUSE:
          name: '故障原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '配置UPF重选的故障原因值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SALANSM01'
      SWITCH: ENABLE
    set_addressattr_list:
    - ALLOCPRECEDENCE: UPF_FIRST
    add_reselectupcause_list:
    - FAULTCAUSE: 75
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。对应的License控制项为“82200EDD LKV2SALANSM01 5G LAN业务基本功能-USM”、"82209930 LKV2CUFMN01 CU FullMesh组网"。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置地址分配方式。

```jinja2
{%- for item in set_addressattr_list -%}
    SET ADDRESSATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCPRECEDENCE is not none -%}
        ALLOCPRECEDENCE={{item.ALLOCPRECEDENCE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置UPF重选的故障原因值。

```jinja2
{%- for item in add_reselectupcause_list -%}
    ADD RESELECTUPCAUSE:
    {#- --- 必选参数 --- -#}
    FAULTCAUSE={{item.FAULTCAUSE}},
    ;
{%- endfor -%}
```

