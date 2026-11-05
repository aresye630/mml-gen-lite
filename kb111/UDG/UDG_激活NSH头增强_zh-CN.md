---
id: ''
name: 激活NSH头增强
ne_type: UDG
type: feature
description: 当需要将用户信息通过NSH封装方式传递给第三方APP时，需要部署此功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG头增强功能专题","NSH头增强功能","激活NSH头增强"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要将用户信息通过NSH封装方式传递给第三方APP时，需要部署此功能。适用于PGW-U、UPF。

## 必备事项
前提条件

请仔细阅NSH头增强原理描述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置需要进行NSH头增强功能的APN信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnnshheadenfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '基于APN粒度开启NSH头增强功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nshheaden_list:
      type: items
      properties:
        NSHNAME:
          name: 'NSH头增强名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DATATYPE:
          name: '数据类型'
          type: string
          enum:
          - IMEI1
          - IMSI1
          - MCC_MNC1
          - MSISDN1
          - RAT1
          - ULI1
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TAGVALUE:
          name: 'TAG编码'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENCRYALGORI:
          name: '加密算法标识'
          type: string
          enum:
          - NONE
          - SHA256
          required: false
          description: '注意：  **ENCRYALGORI**取值为NONE时表示不进行加密，有安全风险，不建议使用。'
          data_source: '本端规划'
          pattern: ''
          default: SHA256
        PSWDKEY:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 256
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSWDKEYCONFIRM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 256
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REMOVEDMCC:
          name: '需去除的移动国家码'
          type: string
          minLength: 0
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glbnshhdnply_list:
      type: items
      properties:
        NSHNAME:
          name: 'NSH头增强名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD NSHHEADEN**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REDIRIPVER:
          name: '重定向IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDIRIPV4:
          name: '重定向IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DSTSERVERPORT:
          name: 'NSH对端设备端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDIRIPV6:
          name: '重定向IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'apn-test'
    set_apnnshheadenfunc_list:
    - APN: 'apn-test'
      SWITCH: ENABLE
    add_nshheaden_list:
    - NSHNAME: 'nsh'
      DATATYPE: MSISDN1
      TAGVALUE: 1
      ENCRYALGORI: SHA256
      PSWDKEY: '123456'
      PSWDKEYCONFIRM: '123456'
      REMOVEDMCC: ''
    set_glbnshhdnply_list:
    - NSHNAME: 'nsh'
      REDIRIPVER: IPV4
      REDIRIPV4: '10.0.0.0'
      DSTSERVERPORT: 6633
      REDIRIPV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置需要进行NSH头增强功能的APN信息。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 2 基于APN粒度开启NSH头增强功能。

```jinja2
{%- for item in set_apnnshheadenfunc_list -%}
    SET APNNSHHEADENFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置NSH头增强功能参数。

```jinja2
{%- for item in add_nshheaden_list -%}
    ADD NSHHEADEN:
    {#- --- 必选参数 --- -#}
    NSHNAME="{{item.NSHNAME}}",
    DATATYPE={{item.DATATYPE}},
    TAGVALUE={{item.TAGVALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ENCRYALGORI=SHA256 时必选 --- -#}
    {%- if item.ENCRYALGORI == 'SHA256' -%}
        PSWDKEY="{{item.PSWDKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=SHA256 时必选 --- -#}
    {%- if item.ENCRYALGORI == 'SHA256' -%}
        PSWDKEYCONFIRM="{{item.PSWDKEYCONFIRM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DATATYPE=MSISDN1/IMSI1/IMEI1/RAT1/ULI1/MCC_MNC1 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'IMSI1', 'IMEI1', 'RAT1', 'ULI1', 'MCC_MNC1'] -%}
        {%- if item.ENCRYALGORI is not none -%}
            ENCRYALGORI={{item.ENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1 时可选 --- -#}
    {%- if item.DATATYPE == 'MSISDN1' -%}
        {%- if item.REMOVEDMCC is not none -%}
            REMOVEDMCC="{{item.REMOVEDMCC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置NSH头增强全局策略。

```jinja2
{%- for item in set_glbnshhdnply_list -%}
    SET GLBNSHHDNPLY:
    {#- --- 必选参数 --- -#}
    NSHNAME="{{item.NSHNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.REDIRIPVER is not none -%}
        REDIRIPVER={{item.REDIRIPVER}},
    {%- endif -%}
    {%- if item.DSTSERVERPORT is not none -%}
        DSTSERVERPORT={{item.DSTSERVERPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：REDIRIPVER=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.REDIRIPVER in ['IPV4', 'IPVER_ALL'] -%}
        REDIRIPV4="{{item.REDIRIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：REDIRIPVER=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.REDIRIPVER in ['IPV6', 'IPVER_ALL'] -%}
        REDIRIPV6="{{item.REDIRIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

