---
id: GWFD-024303
name: 配置RADIUS功能
ne_type: UEG
type: feature
description: 提供如下基于RADIUS的丰富功能：  * 提供RADIUS鉴权功能。 * 提供RADIUS计费功能。 * 提供3GPP扩展信元的定制功能。    适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024303 Radius功能","激活RADIUS功能","配置RADIUS功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
提供如下基于RADIUS的丰富功能：* 提供RADIUS鉴权功能。* 提供RADIUS计费功能。* 提供3GPP扩展信元的定制功能。  适用于PGW-C、SMF

## 必备事项
前提条件

* 当UEG的产品形态为风筝L时，请仔细阅读GWFD-024303 Radius功能特性概述
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 当UEG的产品形态为风筝L时，完成**ADD CPAPN**。
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
          description: '配置AAA服务器组、RADIUS消息超时的时间和重发次数。'
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
        ACCTTIMEOUT:
          name: 'Radius Accounting Request超时时间(秒)'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3
        ACCTRETRANSMIT:
          name: 'Radius Accounting Request重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3
        AUTHTIMEOUT:
          name: 'Radius Authentication Request超时时间(秒)'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3
        AUTHRETRANSMIT:
          name: 'Radius Authentication Request重发次数'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 3
        ACCTSVRTOUT:
          name: 'Radius Accounting超时时长(秒)'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 12
        ACCTSVRDTIME:
          name: 'Radius计费服务器Down状态保持时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 180
        AUTHSVRTOUT:
          name: 'Radius鉴权服务器超时时长(秒)'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 12
        AUTHSVRDTIME:
          name: 'Radius鉴权服务器Down状态保持时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 180
    add_rdssvr_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '与AAA鉴权服务器的IP地址保持一致。'
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
          data_source: '全网规划'
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
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '在“配置到AAA Server的数据”中当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '* 鉴权和计费AAA服务器的密钥可以不同 * 同一个IP+VPN的Server在不同组里的密钥也不需要进行限制'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        PRIORITY:
          name: '服务器优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
          data_source: '与对端协商'
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
    add_rdssvr_list_1:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '与计费AAA服务器的IP地址保持一致。'
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
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: '在“配置到AAA Server的数据”中当UEG的产品形态为风筝L时，已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
        CIPHERKEY:
          name: '服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '* 鉴权和计费AAA服务器的密钥可以不同 * 同一个IP+VPN的Server在不同组里的密钥也不需要进行限制'
          data_source: '与对端协商'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
        PRIORITY:
          name: '服务器优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIPHERKEYCNFM:
          name: '确认服务器密钥（加密的）'
          type: string
          maxLength: 109
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_rdsacctreqvsa_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '计费/鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        THREEGPP:
          name: '支持3gpp私有扩展属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置是否支持3GPP计费扩展属性。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        THREEGPP2:
          name: '支持3gpp2私有扩展属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_rdsacctreqattr_list:
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
    set_rdsauthreqvsa_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'RADIUS服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_rdssvrgrp_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnrdsclientip_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '鉴权或计费请求消息的radius client ip。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHORACCT:
          name: '鉴权或计费'
          type: string
          enum:
          - ACCOUNTING
          - ACCT_AND_AUTH
          - AUTHENTICATION
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          maxLength: 13
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPLOGICINF**配置，可以使用****LST CPLOGICINF****命令进行查询。'
          data_source: '已配置数据中获取'
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
          description: 'APN下绑定AAA服务器组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnrdsacctctrl_list:
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
        TIMETHRESHOLD:
          name: '时间阈值（分）'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: 'AAA的计费阈值'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMETHRESHOLD:
          name: '流量阈值（千字节）'
          type: integer
          minimum:
          - 0
          - 20
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTACCTRSP:
          name: '等待计费开始响应消息后才回应激活成功应答消息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置是否等待计费响应消息后激活用户。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTACCTUPD:
          name: 'MME或SGSN/SGW发起PDP上下文更新时是否支持发送计费更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATTRIGGER:
          name: 'RAT变化触发计费更新消息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRVTRIGGER:
          name: '业务报文（通过3/4层规则配置）时触发计费请求消息 '
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置业务触发RADIUS消息发送时的业务报文延时时间'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BUFFERTIMEVALUE:
          name: '业务报文延时时间（秒）'
          type: integer
          minimum: 0
          maximum: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnauthattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DISCONNECT:
          name: 'DM开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置是否支持RADIUS PoD功能'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_apnradiusattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '当UEG的产品形态为风筝L时，已通过**ADD CPAPN**配置，可以使用****LST CPAPN****命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOMAINNAMEACT:
          name: '增加或剥离域名'
          type: string
          enum:
          - ADD_DISABLE_STRIP_DISABLE
          - ADD_ENABLE_STRIP_DISABLE
          - ADD_DISABLE_STRIP_ENABLE
          required: false
          description: '配置是否支持域名增加或剥离'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DOMAINNAMEPOS:
          name: '域名位置'
          type: string
          enum:
          - 'NULL'
          - PREFIX
          - SUFFIX
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_fhbypass_list:
      type: items
      properties: {}
    set_rdsrspaddrchk_list:
      type: items
      properties: {}
  examples:
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'isprg'
      MODE: MASTER_SLAVE
      SIGOPTACCTMSG: DISABLE
      ACCTTIMEOUT: 10
      ACCTRETRANSMIT: 5
      AUTHTIMEOUT: 10
      AUTHRETRANSMIT: 5
      ACCTSVRTOUT: 12
      ACCTSVRDTIME: 180
      AUTHSVRTOUT: 12
      AUTHSVRDTIME: 180
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      VPNINSTANCE: 'vpn1'
      PORT: 1812
      CIPHERKEY: '*****'
      PRIFLAG: PRIMARY
      PRIORITY: 1
      CIPHERKEYCNFM: '*****'
    add_uplist4rds_list:
    - UPLISTNAME: ''
      UPINSTANCEID: ''
    add_rdssvr_list_1:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: ACCOUNTING
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      VPNINSTANCE: 'vpn1'
      PORT: 1813
      CIPHERKEY: '*****'
      PRIFLAG: PRIMARY
      PRIORITY: 1
      CIPHERKEYCNFM: '*****'
    set_rdsacctreqvsa_list:
    - RDSSVRGRPNAME: 'isprg'
      THREEGPP: ENABLE
      THREEGPP2: DISABLE
    set_rdsacctreqattr_list:
    - RDSSVRGRPNAME: ''
    set_rdsauthreqvsa_list:
    - RDSSVRGRPNAME: ''
    mod_rdssvrgrp_list:
    - RDSSVRGRPNAME: ''
    add_apnrdsclientip_list:
    - APN: 'apn-test'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/1'
    add_apnrdssvrgrp_list:
    - APN: 'apn-test'
      RDSSVRGRPNAME: 'isprg'
    set_apnrdsacctctrl_list:
    - APN: 'apn-test'
      TIMETHRESHOLD: 30
      VOLUMETHRESHOLD: 20
      SUPPORTACCTRSP: ENABLE
      SUPPORTACCTUPD: ENABLE
      RATTRIGGER: ENABLE
      SRVTRIGGER: ENABLE
      BUFFERTIMEVALUE: 2
    set_apnauthattr_list:
    - APN: 'apn-test'
      DISCONNECT: ENABLE
    set_apnradiusattr_list:
    - APN: 'apn-test'
      DOMAINNAMEACT: ADD_ENABLE_STRIP_DISABLE
      DOMAINNAMEPOS: SUFFIX
    set_fhbypass_list:
    - {}
    set_rdsrspaddrchk_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置AAA服务器组以及RADIUS消息的重发次数和超时的时间。

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
    {%- if item.ACCTTIMEOUT is not none -%}
        ACCTTIMEOUT={{item.ACCTTIMEOUT}},
    {%- endif -%}
    {%- if item.ACCTRETRANSMIT is not none -%}
        ACCTRETRANSMIT={{item.ACCTRETRANSMIT}},
    {%- endif -%}
    {%- if item.AUTHTIMEOUT is not none -%}
        AUTHTIMEOUT={{item.AUTHTIMEOUT}},
    {%- endif -%}
    {%- if item.AUTHRETRANSMIT is not none -%}
        AUTHRETRANSMIT={{item.AUTHRETRANSMIT}},
    {%- endif -%}
    {%- if item.ACCTSVRTOUT is not none -%}
        ACCTSVRTOUT={{item.ACCTSVRTOUT}},
    {%- endif -%}
    {%- if item.ACCTSVRDTIME is not none -%}
        ACCTSVRDTIME={{item.ACCTSVRDTIME}},
    {%- endif -%}
    {%- if item.AUTHSVRTOUT is not none -%}
        AUTHSVRTOUT={{item.AUTHSVRTOUT}},
    {%- endif -%}
    {%- if item.AUTHSVRDTIME is not none -%}
        AUTHSVRDTIME={{item.AUTHSVRDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置鉴权AAA服务器。

### 根据鉴权AAA服务器的接收能力，执行如下命令，通过设置**WALVALUE**参数以限制向鉴权AAA服务器发送的消息数，具体请参见激活系统过载控制功能（适用于SPGW-C）。

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PRIFLAG=PRIMARY 时可选 --- -#}
    {%- if item.PRIFLAG == 'PRIMARY' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
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

### 5 **可选：**配置AAA计费服务器。

### 根据AAA计费服务器的接收能力，执行如下命令，通过设置**WALVALUE**参数以限制向计费AAA服务器发送的消息数，具体请参见激活系统过载控制功能（适用于SPGW-C）。

```jinja2
{%- if is_optional_aaa_billing_server -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PRIFLAG=PRIMARY 时可选 --- -#}
        {%- if item.PRIFLAG == 'PRIMARY' -%}
            {%- if item.PRIORITY is not none -%}
                PRIORITY={{item.PRIORITY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置RADIUS参数。

#### 6.1 配置计费AAA服务器组的私有扩展属性。

```jinja2
{%- for item in set_rdsacctreqvsa_list -%}
    SET RDSACCTREQVSA:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    THREEGPP={{item.THREEGPP}},
    THREEGPP2={{item.THREEGPP2}},
    ;
{%- endfor -%}
```

#### 6.2 **可选：**配置计费AAA服务器的可选消息属性。

```jinja2
{%- if is_optional_billing_aaa_msg_attr -%}
    {%- for item in set_rdsacctreqattr_list -%}
        SET RDSACCTREQATTR:
        {#- --- 必选参数 --- -#}
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 **可选：**配置鉴权请求携带的私有扩展属性

```jinja2
{%- if is_optional_auth_req_private_ext_attr -%}
    {%- for item in set_rdsauthreqvsa_list -%}
        SET RDSAUTHREQVSA:
        {#- --- 必选参数 --- -#}
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.4 **可选：**配置RADIUS Server Group的可选计费消息属性。

```jinja2
{%- if is_optional_radius_svrgrp_billing_msg_attr -%}
    {%- for item in mod_rdssvrgrp_list -%}
        MOD RDSSVRGRP:
        {#- --- 必选参数 --- -#}
        RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.5 配置APN下绑定Client IP。

```jinja2
{%- for item in add_apnrdsclientip_list -%}
    ADD APNRDSCLIENTIP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    AUTHORACCT={{item.AUTHORACCT}},
    INTFNAME="{{item.INTFNAME}}",
    ;
{%- endfor -%}
```

#### 如果没有配置Client IP，则该APN用户激活失败。

#### 6.6 配置APN下绑定AAA服务器组。

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

#### 6.7 **可选：**配置指定APN实例的RADIUS计费AAA服务器的流量阈值、时间阈值以及其他AAA客户端的计费信令控制属性。

```jinja2
{%- if is_optional_apn_radius_billing_threshold_ctrl -%}
    {%- for item in set_apnrdsacctctrl_list -%}
        SET APNRDSACCTCTRL:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
        {%- if item.VOLUMETHRESHOLD is not none -%}
            VOLUMETHRESHOLD={{item.VOLUMETHRESHOLD}},
        {%- endif -%}
        {%- if item.SUPPORTACCTRSP is not none -%}
            SUPPORTACCTRSP={{item.SUPPORTACCTRSP}},
        {%- endif -%}
        {%- if item.SUPPORTACCTUPD is not none -%}
            SUPPORTACCTUPD={{item.SUPPORTACCTUPD}},
        {%- endif -%}
        {%- if item.SRVTRIGGER is not none -%}
            SRVTRIGGER={{item.SRVTRIGGER}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUPPORTACCTUPD=ENABLE 时可选 --- -#}
        {%- if item.SUPPORTACCTUPD == 'ENABLE' -%}
            {%- if item.RATTRIGGER is not none -%}
                RATTRIGGER={{item.RATTRIGGER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SRVTRIGGER=ENABLE 时可选 --- -#}
        {%- if item.SRVTRIGGER == 'ENABLE' -%}
            {%- if item.BUFFERTIMEVALUE is not none -%}
                BUFFERTIMEVALUE={{item.BUFFERTIMEVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.8 **可选：**开启RADIUS PoD功能。

```jinja2
{%- if is_optional_radius_pod -%}
    {%- for item in set_apnauthattr_list -%}
        SET APNAUTHATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DISCONNECT is not none -%}
            DISCONNECT={{item.DISCONNECT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.9 **可选：**配置APN是否支持增加域名功能（即当用户去鉴权AAA服务器鉴权时，是否携带域名），以及是否支持剥离域名功能。如果需要同时开启这两个功能，则执行该命令两次。

```jinja2
{%- if is_optional_apn_domain_add_strip -%}
    {%- for item in set_apnradiusattr_list -%}
        SET APNRADIUSATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DOMAINNAMEACT is not none -%}
            DOMAINNAMEACT={{item.DOMAINNAMEACT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE 时必选 --- -#}
        {%- if item.DOMAINNAMEACT == 'ADD_ENABLE_STRIP_DISABLE' -%}
            DOMAINNAMEPOS={{item.DOMAINNAMEPOS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 域名做为用户名的一部分，通过前缀或者后缀的形式与用户名连接。

#### 域名做为前缀时，域名+前缀分隔符+用户名（当UEG的产品形态为风筝L时，前缀分隔符由****SET CPDOMAINSEPARATOR****命令配置）。

#### 域名做为后缀时，用户名+后缀分隔符+域名（当UEG的产品形态为风筝L时，后缀分隔符由****SET CPDOMAINSEPARATOR****命令配置）。

### 7 **可选：****故障场景紧急处理：**配置RADIUS鉴权超时无响应或计费AAA服务器无响应时的一键放通功能。

```jinja2
{%- if is_optional_fault_bypass -%}
    SET FHBYPASS:
    ;
{%- endif -%}
```

### 本命令优先级高于**SET APNAUTHATTR**的**“AAANORSPCTRL”**和**SET APNRDSACCTCTRL**的**“****DEACTIVE”**。

### 由于配置**SET FHBYPASS**将影响用户的激活状态，只有在取得了客户的书面认可后方可使用。

### 通过**SET FHBYPASS**“HOLDINGTIME”控制故障恢复后对放通用户的后续处理，即永久在线或去激活。

### 8 **可选：**配置Specific APN。

### 当UEG的产品形态为风筝L时，**ADD CPSPECIFICAPNVAL**

### 其中“ONLYROAMSWITCH”为可选参数，当UEG的产品形态为风筝L时，配置**ADD CPSPECIFICAPNVAL**命令的生效范围：仅对漫游用户生效。

### 在上报APN时，不仅能携带Request APN/Service APN，UEG支持上报指定的APN，该APN可以是系统中配置的任一APN实例名称或者APN别名的名称。

### 当配置了Specific APN时，在上报APN时，Specific APN优先级最高，其次是别名APN、虚拟APN、真实APN。

### 9 **可选：**配置是否检查RADIUS响应消息源端口。

```jinja2
{%- if is_optional_check_radius_rsp_src_port -%}
    SET RDSRSPADDRCHK:
    ;
{%- endif -%}
```

### 该功能默认开启。如果组网中部署了防火墙或NAT设备，或AAA响应消息会修改IP和Port，RADIUS响应消息端口默认检查功能会失效，因此需要关闭该功能。

