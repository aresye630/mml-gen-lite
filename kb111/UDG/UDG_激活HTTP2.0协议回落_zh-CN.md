---
id: GWFD-110202
name: 激活HTTP2.0协议回落
ne_type: UDG
type: feature
description: 当运营商部署的网关设备不具备HTTP2.0处理能力或者网关设备需要与不具备HTTP2.0处理能力的周边网元配合共同完成业务部署时，需要开启HTTP2.0协议回落功能，对业务实施计费与策略控制。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","业务感知功能","GWFD-110202 HTTP2.0协议回落","激活HTTP2.0协议回落"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商部署的网关设备不具备HTTP2.0处理能力或者网关设备需要与不具备HTTP2.0处理能力的周边网元配合共同完成业务部署时，需要开启HTTP2.0协议回落功能，对业务实施计费与策略控制。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110202 HTTP2.0协议回落。
* UDG已完成与周边网元的对接。
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
    set_srvcommonpara_list:
      type: items
      properties:
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启全局HTTP2.0协议回落功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnhttp2dgrd_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启基于APN的HTTP2.0协议回落功能。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'APN HTTP2协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启基于rule级别的HTTP2.0协议回落功能。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5H2PF01'
      SWITCH: ENABLE
    set_srvcommonpara_list:
    - HTTP2DEGRADESW: ENABLE
    set_apnhttp2dgrd_list:
    - APN: 'apn-test'
      HTTP2DEGRADESW: INHERIT
    mod_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pcc-test'
      HTTP2DEGRADESW: INHERIT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 开启全局HTTP2.0协议回落功能开关。

```jinja2
{%- for item in set_srvcommonpara_list -%}
    SET SRVCOMMONPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.HTTP2DEGRADESW is not none -%}
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 当运营商需要基于APN级别进行控制时，开启基于APN级别的HTTP2.0协议回落功能开关。

```jinja2
{%- if is_scenario_apn_level -%}
    {%- for item in set_apnhttp2dgrd_list -%}
        SET APNHTTP2DGRD:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 当运营商需要基于rule级别进行控制时，开启基于rule级别的HTTP2.0协议回落功能开关。

```jinja2
{%- if is_scenario_rule_level -%}
    {%- for item in mod_pccpolicygrp_list -%}
        MOD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HTTP2DEGRADESW is not none -%}
            HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

