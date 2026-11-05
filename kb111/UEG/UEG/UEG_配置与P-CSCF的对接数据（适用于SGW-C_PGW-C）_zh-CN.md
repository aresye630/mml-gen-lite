---
id: ''
name: 配置与P-CSCF的对接数据（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍了SGW-C/PGW-C与P-CSCF的对接配置，用于部署LTE语音业务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","配置与P-CSCF的对接数据（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍了SGW-C/PGW-C与P-CSCF的对接配置，用于部署LTE语音业务。

## 必备事项
前提条件

已完成基础网路部署，如Sv接口，SGs接口对接。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_pcscfgroup_list:
      type: items
      properties:
        GROUPNAME:
          name: 'P-CSCF组名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置P-CSCF分组信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPV4
    add_pcscfip_list:
      type: items
      properties:
        GROUPNAME:
          name: 'P-CSCF组名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置P-CSCF服务器。  “P-CSCF组名”从**ADD PCSCFGROUP**中已配置的数据获取，可通过**LST PCSCFGROUP**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCSCFIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 1
        ALLOCTYPE:
          name: 'P-CSCF获取方式'
          type: string
          enum:
          - LOCAL
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOCAL
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pcscfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '将指定的主备P-CSCF分组绑定到APN下。   * “APN名称”从**ADD CPAPN**中已配置的数据获取，可通过**LST CPAPN**查询。 * “主IPv4P-CSCF组”和“备IPv4P-CSCF组”从**ADD PCSCFGROUP**中已配置的数据获取，可通过**LST PCSCFGROUP**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MPCSCFGRPIPV4:
          name: '主IPv4P-CSCF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SPCSCFGRPIPV4:
          name: '备IPv4P-CSCF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_pcscfgroup_list:
    - GROUPNAME: 'pcg_test1'
      IPVERSION: IPV4
    add_pcscfip_list:
    - GROUPNAME: 'pcg_test1'
      IPVERSION: IPV4
      PCSCFIPV4: '192.168.254.251'
      WEIGHT: 1
      ALLOCTYPE: LOCAL
    add_cpapn_list:
    - APN: 'ims'
    add_pcscfgrpbndapn_list:
    - APN: 'ims'
      DEFAULTFLAG: DEFAULT
      MPCSCFGRPIPV4: 'pcg_test1'
      SPCSCFGRPIPV4: 'pcg_test2'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置P-CSCF分组。

```jinja2
{%- for item in add_pcscfgroup_list -%}
    ADD PCSCFGROUP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置P-CSCF服务器。

```jinja2
{%- for item in add_pcscfip_list -%}
    ADD PCSCFIP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PCSCFIPV4="{{item.PCSCFIPV4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCTYPE=LOCAL 时可选 --- -#}
    {%- if item.ALLOCTYPE == 'LOCAL' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 在配置P-CSCF服务器时，为了更好的实现负荷分担功能，请按照如下原则配置：

### 所有服务器都需要配置到主备Group中。

### 主备Group的配置顺序不能一致。

### 比如说有A、B、C、D四台服务器，主备Group都需要配置四台服务器，主Group的顺序为A、B、C、D，备Group的顺序为B、A、D、C。

### 4 指定APN实例。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 5 将指定的主备P-CSCF分组绑定到APN下。

```jinja2
{%- for item in add_pcscfgrpbndapn_list -%}
    ADD PCSCFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    {#- --- 可选参数 --- -#}
    {%- if item.MPCSCFGRPIPV4 is not none -%}
        MPCSCFGRPIPV4="{{item.MPCSCFGRPIPV4}}",
    {%- endif -%}
    {%- if item.SPCSCFGRPIPV4 is not none -%}
        SPCSCFGRPIPV4="{{item.SPCSCFGRPIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

