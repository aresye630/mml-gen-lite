---
id: ''
name: 激活基于延迟定时器的信令拥塞控制（PGW-C）
ne_type: UNC
type: feature
description: 当运营商需要部署基于延时定时器的信令拥塞控制功能时，需要对本功能进行配置，确保本功能可以正常使用。  适用于PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NB-IOT业务功能","WSFD-215201 基于延迟定时器的信令拥塞控制","WSFD-215201 基于延迟定时器的信令拥塞控制（PGW-C）","激活基于延迟定时器的信令拥塞控制（PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要部署基于延时定时器的信令拥塞控制功能时，需要对本功能进行配置，确保本功能可以正常使用。适用于PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-215201 基于延迟定时器的信令拥塞控制（PGW-C）特性概述。
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
    set_gbackofftime_list:
      type: items
      properties:
        BACKOFFTIMER:
          name: '全局Back-Off Time时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: true
          description: '设置全局Back-Off时长'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_backofftime_list:
      type: items
      properties:
        APNNAME:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '规划使能基于延迟定时器的信令拥塞控制功能的APN实例，已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OVERLOADSW:
          name: '系统过载场景下Backoff-time开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '系统过载时使用APN的Back-off time功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BACKOFFTIMER:
          name: 'Back-off时长 （秒）'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INHERIT:
          name: '是否继承全局Back-Off时长'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置PGW-C Backoff-time字段携带的时间长度。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WPSSBT11'
      SWITCH: ENABLE
    set_gbackofftime_list:
    - BACKOFFTIMER: 600
    set_backofftime_list:
    - APNNAME: 'apn-op'
      OVERLOADSW: ENABLE
      BACKOFFTIMER: 900
      INHERIT: NO
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

### 3 设置全局Back-Off时长。

```jinja2
{%- for item in set_gbackofftime_list -%}
    SET GBACKOFFTIME:
    {#- --- 必选参数 --- -#}
    BACKOFFTIMER={{item.BACKOFFTIMER}},
    ;
{%- endfor -%}
```

### 4 配置PGW-C Back-off time功能参数。

```jinja2
{%- for item in set_backofftime_list -%}
    SET BACKOFFTIME:
    {#- --- 必选参数 --- -#}
    APNNAME="{{item.APNNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OVERLOADSW is not none -%}
        OVERLOADSW={{item.OVERLOADSW}},
    {%- endif -%}
    {%- if item.INHERIT is not none -%}
        INHERIT={{item.INHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.BACKOFFTIMER is not none -%}
            BACKOFFTIMER={{item.BACKOFFTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

