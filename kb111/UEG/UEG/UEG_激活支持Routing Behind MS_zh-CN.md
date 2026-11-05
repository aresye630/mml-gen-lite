---
id: GWFD-024101
name: 激活支持Routing Behind MS
ne_type: UEG
type: feature
description: 当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个MS/UE接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活UEG的Routing Behind MS功能。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","基本接入功能","GWFD-024101 支持Routing Behind MS","激活支持Routing Behind MS"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商需要开展移动VPN业务，使多台终端设备（PC）可以通过一个MS/UE接入PDN或Intranet网络，并使用独立的IP地址与网络侧设备进行双向数据业务时，需要激活UEG的Routing Behind MS功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-024101 支持Routing Behind MS。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
    set_apnflowmaxnum_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FDMAXNUM:
          name: 'APN最大五元组节点数'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '某个APN下允许创建的五元组的最大数目，即单用户所有业务可以使用五元组个数上限。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_srvcommonpara_list:
      type: items
      properties:
        FDMAXNUM:
          name: '用户session的五元组节点最大数量'
          type: integer
          minimum: 1
          maximum: 2550
          required: false
          description: '全局配置的单用户所有业务可以使用五元组个数上限。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERFLOWADJSW:
          name: '单用户最大流表数动态调整开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5RBMS01'
      SWITCH: ENABLE
    set_apnaddressattr_list:
    - APN: 'apn1'
      FRAMEDROUTE: ENABLE
    set_apnflowmaxnum_list:
    - APN: 'apn1'
      FDMAXNUM: 800
    set_srvcommonpara_list:
    - FDMAXNUM: 800
      USERFLOWADJSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 使能该APN的Routing Behind MS功能。

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

### 3 配置APN下单用户所有业务允许创建的五元组的最大数目。

```jinja2
{%- for item in set_apnflowmaxnum_list -%}
    SET APNFLOWMAXNUM:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    FDMAXNUM={{item.FDMAXNUM}},
    ;
{%- endfor -%}
```

### 4 配置全局单用户所有业务可以使用五元组个数上限，并打开自动调整用户五元组上限功能开关。

```jinja2
{%- for item in set_srvcommonpara_list -%}
    SET SRVCOMMONPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FDMAXNUM is not none -%}
        FDMAXNUM={{item.FDMAXNUM}},
    {%- endif -%}
    {%- if item.USERFLOWADJSW is not none -%}
        USERFLOWADJSW={{item.USERFLOWADJSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 单个用户的默认五元组个数为600，如果现网有超过该默认值的情况，需要配置该步骤。

