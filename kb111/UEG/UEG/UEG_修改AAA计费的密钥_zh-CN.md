---
id: GWFD-024303
name: 修改AAA计费的密钥
ne_type: UEG
type: feature
description: UEG上配置的计费密钥必须与计费服务器上配置的NAS（Network Access Server）端密钥保持一致，否则无法计费。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","调整AAA计费参数","修改AAA计费的密钥"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG上配置的计费密钥必须与计费服务器上配置的NAS（Network Access Server）端密钥保持一致，否则无法计费。适用于PGW-C、SMF

## 必备事项
前提条件

完成配置RADIUS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '**ADD RDSSVRGRP**'
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
          description: '**ADD RDSSVR**'
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
          data_source: '本端规划'
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
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: ''
          data_source: '与对端协商'
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
  examples:
    rmv_rdssvr_list:
    - RDSSVRGRPNAME: 'ss'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '192.168.4.26'
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'ss'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '192.168.4.26'
      CIPHERKEY: '123'
      CIPHERKEYCNFM: '123'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 删除同一VPN下IP地址相同的服务器。

```jinja2
{%- for item in rmv_rdssvr_list -%}
    RMV RDSSVR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 目前的版本不能直接修改密钥，需要先把这个RADIUS Server的配置删除，然后重配。

### 3 修改AAA计费密钥。

```jinja2
{%- for item in add_rdssvr_list -%}
    ADD RDSSVR:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    SERVERTYPE={{item.SERVERTYPE}},
    IPVERSION={{item.IPVERSION}},
    CIPHERKEY="{{item.CIPHERKEY}}",
    CIPHERKEYCNFM="{{item.CIPHERKEYCNFM}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

