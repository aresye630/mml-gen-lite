---
id: ''
name: 配置Gi接口数据
ne_type: UEG
type: feature
description: 当需要对园区用户进行二次鉴权时SMF需要和园区RADIUS server对接，可按照本操作指导执行。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。  双DC组网场景下，两个DC内的SMF均需要和企业的AAA Server对接。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","初始配置与调测","参考：详细配置指导","配置SMF","配置Gi接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当需要对园区用户进行二次鉴权时SMF需要和园区RADIUS server对接，可按照本操作指导执行。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。双DC组网场景下，两个DC内的SMF均需要和企业的AAA Server对接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成部署组网路由配置（裸机容器）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpvpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '使用园区统一规划的VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '逻辑接口使用的逻辑IP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置使用的逻辑接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '鉴权AAA服务器所属的VPN实例名。已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rdssvrgrp_list:
      type: items
      properties:
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '配置AAA服务器组。'
          data_source: '本端规划'
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
          description: '鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - ACCOUNTING
          - AUTHENTICATION
          required: true
          description: '-'
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
          description: '鉴权AAA服务器IP地址、端口号、密钥。'
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
          description: ''
          data_source: '与对端协商'
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
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '计费AAA服务器所属的VPN实例名。已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
    mod_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '已通过**ADD CPVPNINST**配置，可以使用**LST CPVPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REACWITHDEL:
          name: '去活消息携带reactivation-request开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - SPECIFIC_SCENE
          required: false
          description: '-'
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
          description: '已通过命令**ADD CPAPN**进行配置，可以使用命令**LST CPAPN**查询。'
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
          description: '-'
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
          description: '已通过命令**ADD CPAPN**进行配置，可以使用命令**LST CPAPN**查询。'
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
          description: '配置增加或剥离域名。'
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
    add_apnrdsclientip_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过命令**ADD CPAPN**进行配置，可以使用命令**LST CPAPN**查询。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTFNAME:
          name: '接口名称'
          type: string
          maxLength: 13
          required: true
          description: '已通过**ADD CPLOGICINF**进行配置，可以使用**LST CPLOGICINF**进行查询。'
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
          description: '已通过命令**ADD CPAPN**进行配置，可以使用命令**LST CPAPN**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RDSSVRGRPNAME:
          name: 'Radius Server Group名称'
          type: string
          maxLength: 31
          required: true
          description: '鉴权AAA服务器所在的AAA服务器组，已通过**ADD RDSSVRGRP**进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_cpvpninst_list:
    - VPNINSTANCE: 'VPN_CN'
    - VPNINSTANCE: 'VPN_CN'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'gi'
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.2'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'gi'
    add_cplogicinf_list:
    - NAME: 'giif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_CN'
    - NAME: 'giif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_CN'
    add_rdssvrgrp_list:
    - RDSSVRGRPNAME: 'isprg'
    - RDSSVRGRPNAME: 'isprg'
    add_rdssvr_list:
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.1'
      PORT: 1812
      CIPHERKEY: 'ispchina'
      VPNINSTANCE: 'VPN_CN'
      CIPHERKEYCNFM: 'ispchina'
      PRIFLAG: PRIMARY
    - RDSSVRGRPNAME: 'isprg'
      SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '10.168.10.2'
      PORT: 1812
      CIPHERKEY: 'ispchina'
      VPNINSTANCE: 'VPN_CN'
      CIPHERKEYCNFM: 'ispchina'
      PRIFLAG: PRIMARY
    mod_cpapn_list:
    - APN: 'huawei.com'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_CN'
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      REACWITHDEL: DISABLE
    - APN: 'huawei.com'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_CN'
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
      REACWITHDEL: DISABLE
    set_apnauthattr_list:
    - APN: 'huawei.com'
      DISCONNECT: ENABLE
    - APN: 'huawei.com'
      DISCONNECT: ENABLE
    set_apnradiusattr_list:
    - APN: 'huawei.com'
      DOMAINNAMEACT: ADD_DISABLE_STRIP_ENABLE
      DOMAINNAMEPOS: SUFFIX
    - APN: 'huawei.com'
      DOMAINNAMEACT: ADD_DISABLE_STRIP_ENABLE
      DOMAINNAMEPOS: SUFFIX
    add_apnrdsclientip_list:
    - APN: 'huawei.com'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    - APN: 'huawei.com'
      AUTHORACCT: AUTHENTICATION
      INTFNAME: 'giif1/0/0'
    add_apnrdssvrgrp_list:
    - APN: 'huawei.com'
      RDSSVRGRPNAME: 'isprg'
    - APN: 'huawei.com'
      RDSSVRGRPNAME: 'isprg'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置Gi逻辑接口。

#### 1.1 //DC1

```jinja2
{%- for item in add_cpvpninst_list -%}
    ADD CPVPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cplogicinf_list -%}
    ADD CPLOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置鉴权AAA服务器。

#### 2.1 配置AAA服务器组以及服务器的工作模式。

##### 2.1.1 //DC1

```jinja2
{%- for item in add_rdssvrgrp_list -%}
    ADD RDSSVRGRP:
    {#- --- 必选参数 --- -#}
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

#### 2.2 设置鉴权AAA服务器的IP地址、目的端口号、所属VPN、密钥。

##### 2.2.1 //DC1

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

#### 2.3 配置APN。

##### 2.3.1 //DC1

```jinja2
{%- for item in mod_cpapn_list -%}
    MOD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.REACWITHDEL is not none -%}
        REACWITHDEL={{item.REACWITHDEL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 **可选：**开启RADIUS Pod功能。

##### 2.4.1 //DC1

```jinja2
{%- if is_optional_enable_radius_pod -%}
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

#### 2.5 **可选：**配置APN是否支持增加域名功能（即用户去AAA服务器鉴权时，是否携带域名），以及是否支持剥离域名功能。如果需要同时开启这两个功能，则执行该命令两次。

##### 2.5.1 //DC1

```jinja2
{%- if is_optional_configure_apn_domain -%}
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

#### 2.6 配置APN下的Client-IP。

##### 2.6.1 //DC1

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

#### 2.7 APN实例下绑定RADIUS服务器组。

##### 2.7.1 //DC1

```jinja2
{%- for item in add_apnrdssvrgrp_list -%}
    ADD APNRDSSVRGRP:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    RDSSVRGRPNAME="{{item.RDSSVRGRPNAME}}",
    ;
{%- endfor -%}
```

### 3 配置激活RADIUS分配IP地址功能。

