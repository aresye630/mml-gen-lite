---
id: ''
name: 激活支持Routing Behind MS
ne_type: UNC
type: feature
description: 当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个MS/UE接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活UNC的Routing Behind MS功能。  适用于GGSN-C、SGW-C、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-205101 支持Routing Behind MS","激活支持Routing Behind MS"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个MS/UE接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活UNC的Routing Behind MS功能。适用于GGSN-C、SGW-C、PGW-C、SMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-205101 支持Routing Behind MS特性概述。
* 完成加载License。
* 本特性与UDG配合使用生效，请参考UDG中的**GWFD-110910 支持Routing Behind MS**。
* 如若本特性部署在新APN上，请参考章节配置会话管理参数完成APN信息配置。
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
    set_smcommfunc_list:
      type: items
      properties:
        RTBEHINDMSSW:
          name: '手机后路由功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '支持从本地配置中获取后路由。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_routingbehindms_list:
      type: items
      properties:
        IMSI:
          name: '用户IMSI号'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTEIP:
          name: '后路由IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTEMASK:
          name: '后路由掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9RBMS12'
      SWITCH: ENABLE
    set_apnaddressattr_list:
    - APN: 'huawei.com'
      FRAMEDROUTE: ENABLE
    set_smcommfunc_list:
    - RTBEHINDMSSW: ENABLE
    add_routingbehindms_list:
    - IMSI: '123000123456789'
      APN: 'huawei.com'
      FRAMEDROUTEIP: '192.168.1.0'
      FRAMEDROUTEMASK: '255.255.255.0'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 使能该APN的Routing Behind MS功能。

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

### 如果APN使能了L2TP功能，则无需开启Routing Behind MS功能。

### 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。

### 4 支持从本地配置中获取后路由。

```jinja2
{%- for item in set_smcommfunc_list -%}
    SET SMCOMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.RTBEHINDMSSW is not none -%}
        RTBEHINDMSSW={{item.RTBEHINDMSSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 本地配置手机后路由信息。AAA不返回后路由信息或未部署AAA服务器时，可使用本地配置的后路由信息。

```jinja2
{%- for item in add_routingbehindms_list -%}
    ADD ROUTINGBEHINDMS:
    {#- --- 必选参数 --- -#}
    IMSI="{{item.IMSI}}",
    APN="{{item.APN}}",
    FRAMEDROUTEIP="{{item.FRAMEDROUTEIP}}",
    FRAMEDROUTEMASK="{{item.FRAMEDROUTEMASK}}",
    ;
{%- endfor -%}
```

