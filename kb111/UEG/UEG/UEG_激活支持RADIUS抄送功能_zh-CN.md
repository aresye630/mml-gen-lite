---
id: GWFD-024304
name: 激活支持RADIUS抄送功能
ne_type: UEG
type: feature
description: 当运营商部署分组交换网，在将RADIUS消息发往计费AAA Server时，需要将用户信息同时发给多个AAA抄送服务器，需要激活支持RADIUS抄送功能。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024304 支持Radius功能抄送功能","激活支持RADIUS抄送功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商部署分组交换网，在将RADIUS消息发往计费AAA Server时，需要将用户信息同时发给多个AAA抄送服务器，需要激活支持RADIUS抄送功能。适用于PGW-C、SMF

## 必备事项
前提条件

* 当UEG的产品形态为风筝L时，请仔细阅读GWFD-024304 支持Radius抄送功能特性概述。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 当UEG的产品形态为风筝L时，完成**ADD CPAPN**。
* 完成激活RADIUS功能。
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
          description: '使用的RADIUS组，已通过命令**ADD RDSSVRGRP**配置，可以使用命令**LST RDSSVRGRP**进行查询。'
          data_source: '本端规划'
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
          data_source: ''
          pattern: ''
          default: MASTER_SLAVE
        SIGOPTACCTMSG:
          name: '支持可选计费消息'
          type: string
          enum:
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_cpvpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_uplist4rds_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UP实例标识'
          type: string
          maxLength: 36
          required: true
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
          description: '与AAA计费服务器的IP地址保持一致。'
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
          data_source: '本端规划'
          pattern: ''
          default: IPV4
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPVPNINS**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
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
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
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
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '已通过命令**ADD RDSSVRGRP**配置，可以使用**LST RDSSVRGRP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'isprg'
      MODE: MASTER_SLAVE
      SIGOPTACCTMSG: DISABLE
    add_cpvpninst_list:
    - VPNINSTANCE: 'vpntest'
    add_uplist4rds_list:
    - UPLISTNAME: ''
      UPINSTANCEID: ''
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      PRIFLAG: PRIMARY
      SERVERIPV4: '192.168.8.181'
      PORT: 1819
      VPNINSTANCE: 'vpntest'
      CIPHERKEY: '*****'
      CIPHERKEYCNFM: ''
    add_cpapn_list:
    - APN: 'apn-test'
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

### 3 创建VPN实例。

### 当UEG的产品形态为风筝L时，**ADD CPVPNINST**

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_cpvpninst_list -%}
        ADD CPVPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置UP列表。

```jinja2
{%- if is_optional_up_list -%}
    {%- for item in add_uplist4rds_list -%}
        ADD UPLIST4RDS:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置AAA计费服务器。

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

### 如需配置多个服务器，则需要执行该命令多次。

### 6 配置APN下绑定AAA服务器组。

### 当UEG的产品形态为风筝L时，**ADD CPAPN**

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_l -%}
    {%- for item in add_apnrdssvrgrp_list -%}
        ADD APNRDSSVRGRP:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

