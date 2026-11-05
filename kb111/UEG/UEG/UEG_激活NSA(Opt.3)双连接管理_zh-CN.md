---
id: GWFD-025202
name: 激活NSA(Opt.3)双连接管理
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NSA(Opt.3)双连接管理的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-025200 5G NSA功能","GWFD-025202 NSA(Opt.3)双连接管理","激活NSA(Opt.3)双连接管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NSA(Opt.3)双连接管理的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025202 NSA(Opt.3)双连接管理。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_s1cmpt_list:
      type: items
      properties:
        NRSEC:
          name: '是否携带NR UE Security Capabilities信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置安全协商相关信元的携带情况'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nsactrl_list:
      type: items
      properties:
        NRUSERPT:
          name: 'NR流量上报'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置流量上报策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_sgwcharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - SPECIFIED
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MSK:
          name: 'IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECRATRPT:
          name: 'S-GW支持Secondary RAT Usage Data Report'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'MME IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECRATRPT:
          name: '是否携带Secondary RAT Usage Data Report信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmecharact_list_1:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: '配置Inter流程中对等网元间NSA用户信息传递策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'MME IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTARD:
          name: '是否携带扩展接入限制数据'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        UEASECCAP:
          name: '是否携带UE附加安全能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        BITRATE:
          name: '是否限制最大速率'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_sgsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_SGSN
          - SPECIAL_SGSN
          required: true
          description: '配置Inter流程中对等网元间NSA用户信息传递策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARD:
          name: '是否携带扩展接入限制数据'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
  examples:
    set_s1cmpt_list:
    - NRSEC: YES
    set_nsactrl_list:
    - NRUSERPT: YES
    add_sgwcharact_list:
    - RANGE: SPECIFIED
      IPT: IPV4
      IPV4: '10.10.10.10'
      IPV4MSK: '255.255.255.0'
      SECRATRPT: YES
      DESC: 'noname'
    add_mmecharact_list:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '10.20.10.13'
      MASKV4: '255.255.255.0'
      SECRATRPT: YES
      DESC: 'noname'
    add_mmecharact_list_1:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '10.20.10.15'
      MASKV4: '255.255.255.0'
      EXTARD: YES
      UEASECCAP: YES
      BITRATE: NO
    add_sgsncharact_list:
    - RANGE: SPECIAL_SGSN
      IPT: IPV4
      IPV4: '10.20.10.14'
      MASKV4: '255.255.255.0'
      ARD: YES
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置安全协商相关信元的携带情况。

```jinja2
{%- for item in set_s1cmpt_list -%}
    SET S1CMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.NRSEC is not none -%}
        NRSEC={{item.NRSEC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置流量上报策略。

#### 3.1 设置MME支持NR流量上报功能。

```jinja2
{%- for item in set_nsactrl_list -%}
    SET NSACTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.NRUSERPT is not none -%}
        NRUSERPT={{item.NRUSERPT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 设置给SGW携带Secondary RAT Usage Data Report信元。

```jinja2
{%- for item in add_sgwcharact_list -%}
    ADD SGWCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECRATRPT is not none -%}
        SECRATRPT={{item.SECRATRPT}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIFIED 时必选 --- -#}
    {%- if item.RANGE == 'SPECIFIED' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4MSK="{{item.IPV4MSK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 **可选：**设置给对端MME携带Secondary RAT Usage Data Report信元。如果对端网元支持NSA用户数据报告上报功能且支持处理Secondary RAT Usage Data Report信元时执行此步骤。

```jinja2
{%- if is_optional_set_peer_mme_secondary_rat_report -%}
    {%- for item in add_mmecharact_list -%}
        ADD MMECHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SECRATRPT is not none -%}
            SECRATRPT={{item.SECRATRPT}},
        {%- endif -%}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
        {%- if item.RANGE == 'SPECIAL_MME' -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV4' -%}
            MASKV4="{{item.MASKV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置Inter流程中对等网元间NSA用户信息传递策略。

```jinja2
{%- for item in add_mmecharact_list_1 -%}
    ADD MMECHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.EXTARD is not none -%}
        EXTARD={{item.EXTARD}},
    {%- endif -%}
    {%- if item.UEASECCAP is not none -%}
        UEASECCAP={{item.UEASECCAP}},
    {%- endif -%}
    {%- if item.BITRATE is not none -%}
        BITRATE={{item.BITRATE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_MME' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sgsncharact_list -%}
    ADD SGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ARD is not none -%}
        ARD={{item.ARD}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_SGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_SGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

