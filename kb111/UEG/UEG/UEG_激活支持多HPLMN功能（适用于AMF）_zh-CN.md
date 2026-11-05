---
id: GWFD-023102
name: 激活支持多HPLMN功能（适用于AMF）
ne_type: UEG
type: feature
description: 随着5G网络部署的普及，越来越多的用户将会选择5G UE，运营商将会面对5G签约用户数量激增的场景，若单一HPLMN内的用户号段资源无法满足激增的5G签约用户数量，则需要开启本特性，UEG为拥有多个HPLMN的运营商服务，使运营商具备为多个PLMN内用户提供归属地业务服务的能力，从而扩展运营商的用户号段资源。本特性可以帮助运营商配置签署漫游协议的互联网络，同时为互联网络中的用户提供服务。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-023100 组网能力增强","GWFD-023102 支持多HPLMN功能","激活支持多HPLMN功能（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST NGMNO')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
随着5G网络部署的普及，越来越多的用户将会选择5G UE，运营商将会面对5G签约用户数量激增的场景，若单一HPLMN内的用户号段资源无法满足激增的5G签约用户数量，则需要开启本特性，UEG为拥有多个HPLMN的运营商服务，使运营商具备为多个PLMN内用户提供归属地业务服务的能力，从而扩展运营商的用户号段资源。本特性可以帮助运营商配置签署漫游协议的互联网络，同时为互联网络中的用户提供服务。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-023102 支持多HPLMN功能特性概述。
* 已完成加载License。
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
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: 'HPLMN相关参数'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngconnectplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '互联PLMN相关参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2MHAM01'
      SWITCH: ENABLE
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '002'
      DESC: '00'
    add_ngconnectplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '12'
      DESC: '0'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License开关。

#### 2.1 //打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 查询MNO信息，UEG在初配过程中已使用**ADD MNO**命令添加了一条缺省MNO记录，通过本步骤可获取该缺省MNO的相关参数信息。

### ****LST NGMNO****

### 4 通过本步骤在查询到的MNO上增加HPLMN记录，使得该MNO可以接入新增加的HPLMN网络用户。

### ****ADD NGHPLMN****

#### 4.1 //添加两条HPLMN记录。

```jinja2
{%- set LST_NGMNO=getParameterValue('LST NGMNO') -%}
{%- if LST_NGMNO -%}
    {%- for item in add_nghplmn_list -%}
        ADD NGHPLMN:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**增加互联PLMN配置信息。若运营商需要为互联网络中的漫游用户提供接入服务，则需要该步骤来增加该MNO上可服务的互联网络信息。

### ****ADD NGCONNECTPLMN****

```jinja2
{%- if is_optional_add_connect_plmn and LST_NGMNO -%}
    {%- for item in add_ngconnectplmn_list -%}
        ADD NGCONNECTPLMN:
        {#- --- 必选参数 --- -#}
        MNC="{{item.MNC}}",
        MCC="{{item.MCC}}",
        NOID={{item.NOID}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

