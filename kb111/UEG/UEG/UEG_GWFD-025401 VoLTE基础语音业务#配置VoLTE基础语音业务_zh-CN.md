---
id: GWFD-025401
name: 配置VoLTE基础语音业务
ne_type: UEG
type: feature
description: 当部署GPRS/UMTS/EPC网络接入IMS域，需要配置VoLTE基础语音业务。  适用于SGW-U、PGW-U。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","语音功能","GWFD-025401 VoLTE基础语音业务","配置VoLTE基础语音业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当部署GPRS/UMTS/EPC网络接入IMS域，需要配置VoLTE基础语音业务。适用于SGW-U、PGW-U。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-025401 VoLTE基础语音业务。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
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
    add_apnimssigfltr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: 'IMS信令专用上下文的Filter。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4SPECTYPE:
          name: '源IPv4地址指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4MASKLEN:
          name: '源IPv4地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCPORTSPECTYPE:
          name: '源端口指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCPORTSTART:
          name: '源端口号开始'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCPORTEND:
          name: '源端口号结束'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROSPECTYPE:
          name: '协议指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议类型'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnimsattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令**LST APN**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSSWITCH:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '配置IMS功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5VLEF01'
      SWITCH: ENABLE
    add_apnimssigfltr_list:
    - APN: 'ims'
      PRIORITY: 1
      IPVERSION: IPV4
      SRCIPV4SPECTYPE: SPECIFY
      SRCIPV4ADDR: '10.1.1.1'
      SRCIPV4MASKLEN: 32
      SRCPORTSPECTYPE: SPECIFY
      SRCPORTSTART: 1
      SRCPORTEND: 2
      PROSPECTYPE: SPECIFY
      PROTOCOL: 6
    set_apnimsattr_list:
    - APN: 'ims'
      IMSSWITCH: ENABLE
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

### 2 基于APN配置IMS业务。

```jinja2
{%- for item in add_apnimssigfltr_list -%}
    ADD APNIMSSIGFLTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    PRIORITY={{item.PRIORITY}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SRCPORTSPECTYPE is not none -%}
        SRCPORTSPECTYPE={{item.SRCPORTSPECTYPE}},
    {%- endif -%}
    {%- if item.PROSPECTYPE is not none -%}
        PROSPECTYPE={{item.PROSPECTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SRCIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV4SPECTYPE == 'SPECIFY' -%}
        SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV4SPECTYPE == 'SPECIFY' -%}
        SRCIPV4MASKLEN={{item.SRCIPV4MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：SRCPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCPORTSPECTYPE == 'SPECIFY' -%}
        SRCPORTSTART={{item.SRCPORTSTART}},
    {%- endif -%}
    {#- --- 条件必选：SRCPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCPORTSPECTYPE == 'SPECIFY' -%}
        SRCPORTEND={{item.SRCPORTEND}},
    {%- endif -%}
    {#- --- 条件必选：PROSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.PROSPECTYPE == 'SPECIFY' -%}
        PROTOCOL={{item.PROTOCOL}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.SRCIPV4SPECTYPE is not none -%}
            SRCIPV4SPECTYPE={{item.SRCIPV4SPECTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。

```jinja2
{%- for item in set_apnimsattr_list -%}
    SET APNIMSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IMSSWITCH is not none -%}
        IMSSWITCH={{item.IMSSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

