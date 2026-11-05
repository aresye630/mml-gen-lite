---
id: ''
name: 激活NSA自动开户
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活NSA自动开户特性的操作过程。  在5G NSA组网下，用户首次更换了5G终端，可以通过NSA自动开户实现在不换卡、不换号、无需人工操作的场景下开通5G NSA业务功能，更方便快捷地体验5G网络服务，加速5G的快速发展。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NSA业务基本功能","WSFD-011522 NSA自动开户","激活NSA自动开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NSA自动开户特性的操作过程。在5G NSA组网下，用户首次更换了5G终端，可以通过NSA自动开户实现在不换卡、不换号、无需人工操作的场景下开通5G NSA业务功能，更方便快捷地体验5G网络服务，加速5G的快速发展。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-011522 NSA自动开户特性概述。
* 本功能需要UNC和UDM配合使用，如果需要使用该特性，需要同时激活UDM的“NSA自动开户”特性，详细激活步骤请参考《UDM 20.9.0 产品文档》中“配置NSA自动开户特性”页面。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_dmcmpt_list:
      type: items
      properties:
        UEDCNRCAP:
          name: '是否支持UE-DCNR-Capability信元'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: 'MME上为本网用户配置NSA自动开户的功能。  说明：  **SET DMCMPT**与**ADD DMCMPTBYIMSI**命令均可对参数“是否支持UE-DCNR-Capability信元”进行配置。系统会首先匹配**ADD DMCMPTBYIMSI**命令的配置记录，若发现系统中不存在或不匹配**ADD DMCMPTBYIMSI**命令的配置记录才会匹配**SET DMCMPT**命令的配置记录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UEDCNRCAP:
          name: '是否支持UE-DCNR-Capability信元'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NOT_SUPPORT
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_dmcmpt_list:
    - UEDCNRCAP: NOT_SUPPORT
    add_dmcmptbyimsi_list:
    - SUBRANGE: HOME_USER
      UEDCNRCAP: SUPPORT
      IMSIPRE: ''
      NOID: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 针对一定范围的用户，配置NSA自动开户的功能。

#### 2.1 //针对本网用户，开启NSA自动开户功能。

```jinja2
{%- for item in set_dmcmpt_list -%}
    SET DMCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.UEDCNRCAP is not none -%}
        UEDCNRCAP={{item.UEDCNRCAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dmcmptbyimsi_list -%}
    ADD DMCMPTBYIMSI:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.UEDCNRCAP is not none -%}
        UEDCNRCAP={{item.UEDCNRCAP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
    {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
        NOID={{item.NOID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

