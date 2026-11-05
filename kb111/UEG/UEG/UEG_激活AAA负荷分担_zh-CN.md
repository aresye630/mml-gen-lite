---
id: GWFD-024305
name: 激活AAA负荷分担
ne_type: UEG
type: feature
description: 部署多台负荷分担的AAA服务器，解决网络中AAA鉴权和计费的拥塞问题。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024305 AAA负荷分担","激活AAA负荷分担"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
部署多台负荷分担的AAA服务器，解决网络中AAA鉴权和计费的拥塞问题。适用于PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读GWFD-024305 AAA负荷分担特性概述。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 完成增加APN配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_rdssvrgrp_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置AAA服务器组。  已通过**ADD RDSSVRGRP**命令配置，可以使用**LST RDSSVRGRP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MODE:
          name: '模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: MASTER_SLAVE
        SIGOPTACCTMSG:
          name: '支持可选计费消息'
          type: string
          enum:
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置AAA鉴权服务器。与AAA鉴权服务器的IP地址保持一致。'
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
          data_source: '本端规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '已通过 **ADD CPVPNINST**命令配置，可以使用 **LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rdssvr_list_1:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置AAA计费服务器。与AAA计费服务器的IP地址保持一致。'
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
          data_source: '本端规划'
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
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '已通过 **ADD CPVPNINST**命令配置，可以使用 **LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - CARBON_COPY
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnrdssvrgrp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置APN下绑定AAA服务器组。  已通过 **ADD CPAPN**命令配置，可以使用 **LST CPAPN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过**ADD APNRDSSVRGRP**命令配置，可以使用**LST APNRDSSVRGRP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'isprg'
      MODE: ROUND_ROBIN
      SIGOPTACCTMSG: DISABLE
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '192.168.7.12'
      PORT: 1812
      VPNINSTANCE: 'vpn_Gi'
      CIPHERKEY: '*****'
      PRIFLAG: PRIMARY
      CIPHERKEYCNFM: '*****'
    add_rdssvr_list_1:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '192.168.7.14'
      PORT: 1813
      VPNINSTANCE: 'vpn_Gi'
      CIPHERKEY: '*****'
      PRIFLAG: PRIMARY
      CIPHERKEYCNFM: '*****'
    add_apnrdssvrgrp_list:
    - APN: 'apn-test'
      RDSSVRGRPNAME: 'isprg'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置AAA服务器组。

```jinja2
{%- for item in add_rdssvrgrp_list -%}
    ADD RDSSVRGRP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MODE is not none -%}
        MODE={{item.MODE}},
    {%- endif -%}
    {%- if item.SIGOPTACCTMSG is not none -%}
        SIGOPTACCTMSG={{item.SIGOPTACCTMSG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置AAA鉴权服务器及计费服务器。

#### 3.1 配置AAA鉴权服务器。

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
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置AAA计费服务器。

```jinja2
{%- for item in add_rdssvr_list_1 -%}
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
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置APN下绑定AAA服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

