---
id: GWFD-022901
name: 激活IPv6承载上下文特性（适用于PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。  适用于PGW-C。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-022900 IPV6基本功能","GWFD-022901 IPv6承载上下文","GWFD-022901 IPv6承载上下文（MME、SGW-C/PGW-C）","激活IPv6承载上下文特性（适用于PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。适用于PGW-C。

## 必备事项
前提条件

* 请仔细阅读GWFD-022901 IPv6承载上下文特性概述（MME、S/PGW-C）。
* 完成加载License。
* APN的IP地址分配属性指定为本地分配地址。
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
    add_cpaddrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '本地地址池'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
    add_cpsection_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: 'IPv6地址前缀的地址段'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN实例名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'APN相关配置'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    set_cpapnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ALLOCTYPE:
          name: 'IPV6分配方式'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2IPV6SM01'
      SWITCH: ENABLE
    add_cpaddrpool_list:
    - POOLNAME: 'testpool'
      IPVERSION: IPv6
    add_cpsection_list:
    - POOLNAME: 'testpool'
      SECTIONNUM: 1
      IPVERSION: IPV6
      V6PREFIXSTART: 'fe80:1111:2222:3333:ff:ff:ff:ff'
      V6PREFIXEND: 'fe80:1111:2222:4444:ff:ff:ff:ff'
      V6PREFIXLENGTH: 64
    add_cpapn_list:
    - APN: 'apn-test'
    set_cpapnaddressattr_list:
    - APN: 'apn-test'
      IPV6ALLOCTYPE: Local
    add_poolbindapn_list:
    - APN: 'apn-test'
      POOLNAME: 'testpool'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开IPv6承载上下文特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置本地地址池分配IPv6地址。

#### 3.1 创建本地地址池。

```jinja2
{%- for item in add_cpaddrpool_list -%}
    ADD CPADDRPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### **ADD CPADDRPOOL**时，“IPVERSION”请选择“IPV6”参数。

#### 3.2 配置IPv6地址前缀的地址段。

```jinja2
{%- for item in add_cpsection_list -%}
    ADD CPSECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 指定APN实例名称。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 3.4 配置地址分配方式。

```jinja2
{%- for item in set_cpapnaddressattr_list -%}
    SET CPAPNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6ALLOCTYPE is not none -%}
        IPV6ALLOCTYPE={{item.IPV6ALLOCTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 为该APN绑定本地地址池。

#### ****ADD POOLBINDAPN****

```jinja2
{%- for item in add_poolbindapn_list -%}
    ADD POOLBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

