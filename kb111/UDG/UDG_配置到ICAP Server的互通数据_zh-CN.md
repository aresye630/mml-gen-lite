---
id: GWFD-110471
name: 配置到ICAP Server的互通数据
ne_type: UDG
type: feature
description: 部署URL过滤基本功能特性时，需要配置UDG与ICAP Server的互通数据。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","业务感知功能","GWFD-110471 URL过滤基本功能","激活URL过滤基本功能","配置到ICAP Server的互通数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
部署URL过滤基本功能特性时，需要配置UDG与ICAP Server的互通数据。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110471 URL过滤基本功能。
* ICAP Server上的基础数据已搭建完毕。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置逻辑接口。'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD VPNINST**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_icapserver_list:
      type: items
      properties:
        ICAPSERVERNAME:
          name: 'ICAP服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置ICAP Server。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ICAPSERVERTYPE:
          name: 'ICAP服务器类型'
          type: string
          enum:
          - URL_FILTERING
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ICAPSVRIPTYPE:
          name: 'ICAP 服务器IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ICAPSERVERIPV4:
          name: 'ICAP服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD ICAPSERVER**配置，与**ADD LOGICINF**中配置的**VPNINSTANCE**保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TCPRETRYTIME:
          name: 'TCP尝试建链间隔（秒）'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        ICAPSERVERIPV6:
          name: 'ICAP服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_icaplocalinfo_list:
      type: items
      properties:
        ICAPSERVERTYPE:
          name: 'ICAP服务器类型'
          type: string
          enum:
          - URL_FILTERING
          required: true
          description: '已通过**ADD ICAPSERVER**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERAGENT:
          name: 'User Agent'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_icapsvrgrp_list:
      type: items
      properties:
        ICAPSVRGRPNAME:
          name: 'ICAP服务器组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置ICAP服务器组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ICAPSERVERTYPE:
          name: 'ICAP服务器类型'
          type: string
          enum:
          - URL_FILTERING
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_icapsvrbindisg_list:
      type: items
      properties:
        ICAPSVRGRPNAME:
          name: 'ICAP服务器组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD ICAPSVRGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ICAPSERVERNAME:
          name: 'ICAP服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过**ADD ICAPSERVER**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn-gcfif'
    add_logicinf_list:
    - NAME: 'gcfif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn-gcfif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_icapserver_list:
    - ICAPSERVERNAME: 'icapserver1'
      ICAPSERVERTYPE: URL_FILTERING
      ICAPSVRIPTYPE: IPV4
      ICAPSERVERIPV4: '172.16.39.136'
      VPNINSTANCE: 'vpn-gcfif'
      TCPRETRYTIME: 5
      ICAPSERVERIPV6: ''
    add_icaplocalinfo_list:
    - ICAPSERVERTYPE: URL_FILTERING
      USERAGENT: 'test'
    add_icapsvrgrp_list:
    - ICAPSVRGRPNAME: 'icapsvrgrp1'
      ICAPSERVERTYPE: URL_FILTERING
    add_icapsvrbindisg_list:
    - ICAPSVRGRPNAME: 'icapsvrgrp1'
      ICAPSERVERNAME: 'icapserver1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 添加VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 2 配置UDG与ICAP Server间逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置ICAP Server信息。

#### 3.1 配置ICAP Server。

```jinja2
{%- for item in add_icapserver_list -%}
    ADD ICAPSERVER:
    {#- --- 必选参数 --- -#}
    ICAPSERVERNAME="{{item.ICAPSERVERNAME}}",
    ICAPSERVERTYPE={{item.ICAPSERVERTYPE}},
    ICAPSVRIPTYPE={{item.ICAPSVRIPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ICAPSVRIPTYPE=IPV4 时必选 --- -#}
    {%- if item.ICAPSVRIPTYPE == 'IPV4' -%}
        ICAPSERVERIPV4="{{item.ICAPSERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：ICAPSVRIPTYPE=IPV6 时必选 --- -#}
    {%- if item.ICAPSVRIPTYPE == 'IPV6' -%}
        ICAPSERVERIPV6="{{item.ICAPSERVERIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ICAPSERVERTYPE=URL_FILTERING 时可选 --- -#}
    {%- if item.ICAPSERVERTYPE == 'URL_FILTERING' -%}
        {%- if item.TCPRETRYTIME is not none -%}
            TCPRETRYTIME={{item.TCPRETRYTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置UDG与ICAP Server间逻辑接口相关的标识信息。

```jinja2
{%- for item in add_icaplocalinfo_list -%}
    ADD ICAPLOCALINFO:
    {#- --- 必选参数 --- -#}
    ICAPSERVERTYPE={{item.ICAPSERVERTYPE}},
    USERAGENT="{{item.USERAGENT}}",
    ;
{%- endfor -%}
```

### 4 配置ICAP服务器组。

```jinja2
{%- for item in add_icapsvrgrp_list -%}
    ADD ICAPSVRGRP:
    {#- --- 必选参数 --- -#}
    ICAPSVRGRPNAME="{{item.ICAPSVRGRPNAME}}",
    ICAPSERVERTYPE={{item.ICAPSERVERTYPE}},
    ;
{%- endfor -%}
```

### 5 配置ICAP服务器绑定关系。

```jinja2
{%- for item in add_icapsvrbindisg_list -%}
    ADD ICAPSVRBINDISG:
    {#- --- 必选参数 --- -#}
    ICAPSVRGRPNAME="{{item.ICAPSVRGRPNAME}}",
    ICAPSERVERNAME="{{item.ICAPSERVERNAME}}",
    ;
{%- endfor -%}
```

