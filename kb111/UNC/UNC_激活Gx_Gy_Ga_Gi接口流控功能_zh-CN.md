---
id: ''
name: 激活Gx/Gy/Ga/Gi接口流控功能
ne_type: UNC
type: feature
description: UNC的周边网元存在过载风险时，UNC能够基根据本地配置控制向各网元发送消息的速率，从而保护周边网元。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010802 周边网元过载保护","Gx/Gy/Ga/Gi接口流控功能","激活Gx/Gy/Ga/Gi接口流控功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC的周边网元存在过载风险时，UNC能够基根据本地配置控制向各网元发送消息的速率，从而保护周边网元。适用于GGSN、PGW-C。

## 必备事项
前提条件

请仔细阅读WSFD-010802 周边网元过载保护特性概述（Gx/Gy/Ga/Gi接口流控功能）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '设置UNC每秒发送给某PCRF的最大CCR消息数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名'
          type: string
          maxLength: 127
          required: true
          description: '设置UNC每秒发送给某OCS的最大消息数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cg_list:
      type: items
      properties:
        IPVERSION:
          name: 'CG IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '设置UNC每秒发送给CG的最大话单数。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        IPV4ADDR:
          name: 'CG IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: 'CG端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '等级'
          type: integer
          minimum: 0
          maximum: 100
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTYPE:
          name: '话单类型'
          type: string
          enum:
          - R10_ALL
          - R10_PGW
          - R10_SGW
          - R4
          - R5
          - R6
          - R7
          - R8_ALL
          - R8_PGW
          - R8_SGW
          - R98
          - R99
          - R9_ALL
          - R9_PGW
          - R9_SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'CG IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '设置UNC每秒发送某Radius计费服务器的最大消息数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - ACCOUNTING
          - AUTHENTICATION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
    set_smfsoftpara_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Bit
          - Byte
          - String
          required: true
          description: '配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 4000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 1
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pcrf_list:
    - HOSTNAME: 'pcrf1'
      REALMNAME: 'www.huawei.com'
      WALVALUE: 1000
    add_ocs_list:
    - OCSHOSTNAME: 'ocs1'
      REALMNAME: 'www.huawei.com'
      WALVALUE: 1000
    add_cg_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.2'
      PORT: 25009
      PRIORITY: 1
      CDRTYPE: R9_PGW
      WALVALUE: 1000
      IPV6ADDR: ''
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'rdsvr'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '192.168.10.3'
      PORT: 1813
      CIPHERKEY: '123'
      WALVALUE: 1000
      CIPHERKEYCNFM: '123'
      SERVERIPV6: ''
      WEIGHT: 255
    set_smfsoftpara_list:
    - DT: BYTE
      BYTENUM: 863
      BYTEVALUE: 40
      BITNUM: ''
      BITVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置UNC每秒发送给某PCRF的最大CCR消息数。

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置UNC每秒发送给某OCS的最大消息数。

```jinja2
{%- for item in add_ocs_list -%}
    ADD OCS:
    {#- --- 必选参数 --- -#}
    OCSHOSTNAME="{{item.OCSHOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置UNC每秒发送给CG的最大话单数

```jinja2
{%- for item in add_cg_list -%}
    ADD CG:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    PORT={{item.PORT}},
    PRIORITY={{item.PRIORITY}},
    CDRTYPE={{item.CDRTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置UNC每秒发送某Radius计费服务器的最大消息数。

```jinja2
{%- for item in add_rdssvr_list -%}
    ADD RDSSVR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    IPVERSION={{item.IPVERSION}},
    CIPHERKEY="{{item.CIPHERKEY}}",
    CIPHERKEYCNFM="{{item.CIPHERKEYCNFM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SERVERIPV6="{{item.SERVERIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SERVERTYPE=AUTHENTICATION 时可选 --- -#}
    {%- if item.SERVERTYPE == 'AUTHENTICATION' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **可选：**通过软参BYTE863配置Gx接口是否支持基于Gx集中点的WAL流控功能，以及流控阈值。

```jinja2
{%- if is_optional_gx_wal_flow_control -%}
    {%- for item in set_smfsoftpara_list -%}
        SET SMFSOFTPARA:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTEVALUE={{item.BYTEVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=Bit 时必选 --- -#}
        {%- if item.DT == 'Bit' -%}
            BITNUM={{item.BITNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Bit 时必选 --- -#}
        {%- if item.DT == 'Bit' -%}
            BITVALUE={{item.BITVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=String 时必选 --- -#}
        {%- if item.DT == 'String' -%}
            STRINGNUM={{item.STRINGNUM}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DT=String 时可选 --- -#}
        {%- if item.DT == 'String' -%}
            {%- if item.STRINGVALUE is not none -%}
                STRINGVALUE="{{item.STRINGVALUE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

