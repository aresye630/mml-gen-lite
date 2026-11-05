---
id: ''
name: 激活NAS信令加密与完整性保护（适用于4G）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NAS信令加密和完整性保护特性的操作过程。  NAS（Non-Access-Stratum）协议是UE-MME之间的协议，支持核心网和UE之间业务和信令消息的传输。  NAS信令加密和完整性保护可以对NAS信令进行加密及完整性保护，提高系统的安全性。  适用于MME
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于4G）"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NAS信令加密和完整性保护特性的操作过程。NAS（Non-Access-Stratum）协议是UE-MME之间的协议，支持核心网和UE之间业务和信令消息的传输。NAS信令加密和完整性保护可以对NAS信令进行加密及完整性保护，提高系统的安全性。适用于MME

## 必备事项
前提条件

* 请仔细阅读GWFD-021505 NAS信令加密与完整性保护特性概述（适用于4G）。
* EPS网络中各网元系统及操作维护台运行正常。
* 用户在HSS中已签约EPS业务。
* UE支持Null Ciphering Algorithm、SNOW 3G、AES或ZUC加密算法。
* UE支持Null Integrity Algorithm、SNOW 3G、AES或ZUC完整性算法。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_s1usrsecpara_list:
      type: items
      properties:
        USRRANGE:
          name: '用户范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECPLC:
          name: '安全策略'
          type: string
          enum:
          - AUTHANDPROTECTED
          - AUTHONLY
          - NEVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPTINTAGTH:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPTCIPHAGTH:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1algpriority_list:
      type: items
      properties:
        ALGTYPE:
          name: '算法类型'
          type: string
          enum:
          - CIPH
          - INTE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGCIPH:
          name: '加密算法'
          type: string
          enum:
          - EEA0
          - EEA1
          - EEA2
          - EEA3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGPRI:
          name: '算法优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALGINTE:
          name: '完整性算法'
          type: string
          enum:
          - EIA0
          - EIA1
          - EIA2
          - EIA3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '以使用AES算法为例，打开对应的License配置开关。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_s1usrsecpara_list:
    - USRRANGE: DEFAULT
      SECPLC: AUTHANDPROTECTED
      SUPTINTAGTH: EIA0-1&EIA2-1&EIA3-1
      SUPTCIPHAGTH: EEA0-1&EEA2-1&EEA3-1
    add_s1algpriority_list:
    - ALGTYPE: CIPH
      ALGCIPH: EEA0
      ALGPRI: 2
      ALGINTE: EIA0
    set_licenseswitch_list:
    - LICITEM: 'LKV2AES02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开加密算法和完整性算法开关。

```jinja2
{%- for item in mod_s1usrsecpara_list -%}
    MOD S1USRSECPARA:
    {#- --- 必选参数 --- -#}
    USRRANGE={{item.USRRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECPLC is not none -%}
        SECPLC={{item.SECPLC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.SUPTINTAGTH is not none -%}
            SUPTINTAGTH={{item.SUPTINTAGTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SECPLC=AUTHANDPROTECTED 时可选 --- -#}
    {%- if item.SECPLC == 'AUTHANDPROTECTED' -%}
        {%- if item.SUPTCIPHAGTH is not none -%}
            SUPTCIPHAGTH={{item.SUPTCIPHAGTH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### “用户范围”固定选择“DEFAULT”（缺省）

### “安全策略”固定选择“AUTHANDPROTECTED”(鉴权并保护)

### 3 配置加密算法和完整性算法的算法优先级。

```jinja2
{%- for item in add_s1algpriority_list -%}
    ADD S1ALGPRIORITY:
    {#- --- 必选参数 --- -#}
    ALGTYPE={{item.ALGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ALGTYPE=CIPH 时必选 --- -#}
    {%- if item.ALGTYPE == 'CIPH' -%}
        ALGCIPH={{item.ALGCIPH}},
    {%- endif -%}
    {#- --- 条件必选：ALGTYPE=CIPH/INTE 时必选 --- -#}
    {%- if item.ALGTYPE in ['CIPH', 'INTE'] -%}
        ALGPRI={{item.ALGPRI}},
    {%- endif -%}
    {#- --- 条件必选：ALGTYPE=INTE 时必选 --- -#}
    {%- if item.ALGTYPE == 'INTE' -%}
        ALGINTE={{item.ALGINTE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

