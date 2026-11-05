---
id: GWFD-026107
name: 激活Non-IP数据传输
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活Non-IP数据传输特性的操作过程。当Non-IP用户接入网络时，需要在UEG上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。  适用于SGW-U、PGW-U。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","物联网功能","NB-IoT","GWFD-026107 Non-IP数据传输","激活Non-IP数据传输"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Non-IP数据传输特性的操作过程。当Non-IP用户接入网络时，需要在UEG上开启Non-IP功能开关，并且为Non-IP用户配置目的服务器的地址。适用于SGW-U、PGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-026107 Non-IP数据传输。
* 已开启NB-IoT基本接入功能（详见激活NB-IoT终端标准接入）。
* 完成激活基于信令面的数据传输。
* 完成加载License（本特性完整的功能需要同时在用户面和控制面开启License，如果有需求，请联系华为技术支持工程师处理）。
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnnonipfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '已通过**ADD POOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        NONIPSWITCH:
          name: 'APN Non-IP功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERPORT:
          name: '用户端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5NOIP01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'apnnonip'
    set_apnnonipfunc_list:
    - APN: 'apnnonip'
      NONIPSWITCH: ENABLE
      USERPORT: 1010
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 配置Non-IP数据传输所使用的APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 使能指定APN下的Non-IP功能开关。

```jinja2
{%- for item in set_apnnonipfunc_list -%}
    SET APNNONIPFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NONIPSWITCH is not none -%}
        NONIPSWITCH={{item.NONIPSWITCH}},
    {%- endif -%}
    {%- if item.USERPORT is not none -%}
        USERPORT={{item.USERPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.1 本特性分成全局、非全局两种场景，当使用**SET APNNONIPFUNC**配置之后，全局场景转变为非全局场景。

##### 3.1.1 全局场景下，不打开/打开License，全局默认关闭/开启该Non-IP功能。

##### 3.1.2 非全局场景下，打开License并使用**SET APNNONIPFUNC**命令配置指定APN的Non-IP功能之后，全局开启Non-IP功能转变为仅对特定的APN开启：NONIPSWITCH参数取值为**“ENABLE”**的APN才具有Non-IP功能。必须先打开License该命令配置才能生效。

#### 3.2 需要在控制面上配置相同APN并使能Non-IP功能开关。

#### 3.3 当UEG作为PGW-U时必须配置APN下的Non-IP功能开关。

