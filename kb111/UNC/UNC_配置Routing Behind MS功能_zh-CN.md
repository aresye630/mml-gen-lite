---
id: ''
name: 配置Routing Behind MS功能
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员完成一跳入家所需要的Routing Behind MS功能。本方案中，只需从Radius AAA服务器获取后路由信息，SMF本地无需配置后路由。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网SMF","配置Routing Behind MS功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员完成一跳入家所需要的Routing Behind MS功能。本方案中，只需从Radius AAA服务器获取后路由信息，SMF本地无需配置后路由。

## 必备事项
前提条件

已完成**Routing Behind MS**功能的License加载。
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
          description: '打开Routing Behind MS的License。'
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
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划使能Routing Behind MS功能的APN实例，已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN是否允许手机后路由用户接入。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9RBMS12'
      SWITCH: ENABLE
    set_apnaddressattr_list:
    - APN: 'home.dnn'
      FRAMEDROUTE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //使能该APN的Routing Behind MS功能。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FRAMEDROUTE is not none -%}
        FRAMEDROUTE={{item.FRAMEDROUTE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

