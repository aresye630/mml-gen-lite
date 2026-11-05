---
id: ''
name: 配置LDAP数字证书
ne_type: UEG
type: feature
description: 证书加载完成后，LDAP服务通过TLS协议与LDAP服务器通信时，如果是首次与对端系统进行对接，请根据如下操作完成配置。  如果已经配置过对端链路对接信息，本次操作仅替换已有信任证书时，请跳过该章节。
tags: []
risk_level: ''
doc_source:
  - ["日常维护","UEG 基础运维操作（风筝L，虚机容器）","证书管理","UPCF数字证书配置","配置LDAP数字证书"]
  - ["日常维护","UEG 基础运维操作（风筝L，裸机容器）","证书管理","UPCF数字证书配置","配置LDAP数字证书"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
证书加载完成后，LDAP服务通过TLS协议与LDAP服务器通信时，如果是首次与对端系统进行对接，请根据如下操作完成配置。如果已经配置过对端链路对接信息，本次操作仅替换已有信任证书时，请跳过该章节。

## 必备事项
前提条件

已完成设备证书或信任证书的加载。如需了解加载证书的场景，请参考UPCF证书应用场景；关于加载或更新网元证书的方法，请参考证书方案介绍。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_comtlscfg_list:
      type: items
      properties:
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSCFGNAME:
          name: 'TLS配置名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOLVER:
          name: '协议版本'
          type: string
          enum:
          - TLS1_2
          - TLS1_3
          - TLS1_2-TLS1_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRONGSUITE:
          name: 'TLS加密套件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ldaplnk_list:
      type: items
      properties:
        LINKID:
          name: '链路ID'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LNKNAME:
          name: '链路名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIP:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERNAME:
          name: '用户名'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWD:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSPRI:
          name: '数据源优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFUNC:
          name: 'TLS功能'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
        CERTSCENE:
          name: '证书应用场景'
          type: string
          enum:
          - UPCF_LDAP_certForLDAPLNK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRLPOLICY:
          name: 'CRL策略'
          type: string
          enum:
          - Check
          - NoCheck
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Check
        TLSCFGID:
          name: 'TLS配置ID'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_comtlscfg_list:
    - TLSCFGID: TLS配置ID
      TLSCFGNAME: 'TLS配置名称'
      PROTOCOLVER: 协议版本
      STRONGSUITE: TLS加密套件
    add_ldaplnk_list:
    - LINKID: 链路ID
      LNKNAME: '链路名称'
      IPVER: IPV4
      LOCALPORT: 本端端口
      PEERIP: '对端IPV4地址'
      PEERPORT: 对端端口
      USERNAME: '用户名'
      PWD: '密码'
      CFM: '确认密码'
      DSPRI: 数据源优先级
      TLSFUNC: ON
      CERTSCENE: UPCF_LDAP_certForLDAPLNK
      CRLPOLICY: CRL策略
      TLSCFGID: TLS配置ID
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在OM Portal界面选择“应用管理 > MML”，进入MML命令界面，选择UEG网元。

### 2 执行**ADD COMTLSCFG**命令，增加TLS配置信息。

```jinja2
{%- for item in add_comtlscfg_list -%}
    ADD COMTLSCFG:
    {#- --- 必选参数 --- -#}
    TLSCFGID={{item.TLSCFGID}},
    TLSCFGNAME="{{item.TLSCFGNAME}}",
    PROTOCOLVER={{item.PROTOCOLVER}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOLVER=TLS1_2/TLS1_2-TLS1_3 时可选 --- -#}
    {%- if item.PROTOCOLVER in ['TLS1_2', 'TLS1_2-TLS1_3'] -%}
        {%- if item.STRONGSUITE is not none -%}
            STRONGSUITE={{item.STRONGSUITE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**ADD LDAPLNK**命令，配置LDAP客户端数字证书。

### 选择“TLS功能”为“ON(打开)”，“证书应用场景”为“UPCF\_LDAP\_certForLDAPLNK(LDAP接口链路客户端证书)”进行配置。

```jinja2
{%- for item in add_ldaplnk_list -%}
    ADD LDAPLNK:
    {#- --- 必选参数 --- -#}
    LINKID={{item.LINKID}},
    IPVER={{item.IPVER}},
    LOCALPORT={{item.LOCALPORT}},
    PEERPORT={{item.PEERPORT}},
    USERNAME="{{item.USERNAME}}",
    PWD="{{item.PWD}}",
    CFM="{{item.CFM}}",
    DSPRI={{item.DSPRI}},
    {#- --- 可选参数 --- -#}
    {%- if item.LNKNAME is not none -%}
        LNKNAME="{{item.LNKNAME}}",
    {%- endif -%}
    {%- if item.TLSFUNC is not none -%}
        TLSFUNC={{item.TLSFUNC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        PEERIP="{{item.PEERIP}}",
    {%- endif -%}
    {#- --- 条件必选：TLSFUNC=ON 时必选 --- -#}
    {%- if item.TLSFUNC == 'ON' -%}
        CERTSCENE={{item.CERTSCENE}},
    {%- endif -%}
    {#- --- 条件必选：TLSFUNC=ON 时必选 --- -#}
    {%- if item.TLSFUNC == 'ON' -%}
        CRLPOLICY={{item.CRLPOLICY}},
    {%- endif -%}
    {#- --- 条件必选：TLSFUNC=ON 时必选 --- -#}
    {%- if item.TLSFUNC == 'ON' -%}
        TLSCFGID={{item.TLSCFGID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

