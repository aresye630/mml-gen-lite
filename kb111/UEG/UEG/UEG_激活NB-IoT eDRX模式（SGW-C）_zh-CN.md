---
id: GWFD-026104
name: 激活NB-IoT eDRX模式（SGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活NB-IoT eDRX模式特性的操作过程。  适用于SGW-C
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026104 NB-IoT eDRX模式（SGW-C）","激活NB-IoT eDRX模式（SGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NB-IoT eDRX模式特性的操作过程。适用于SGW-C

## 必备事项
前提条件

* 请仔细阅读GWFD-026104 NB-IoT eDRX模式特性概述（SGW-C）。
* 完成加载License。
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
    set_smfglbdlbuftime_list:
      type: items
      properties:
        NBIOTUSER:
          name: 'NB-IoT用户下行数据缓存时长'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '全局的NB-IoT用户下行报文缓存时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smfapndlbuftime_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '指定APN下的NB-IoT用户下行报文缓存时长。'
          data_source: ''
          pattern: ''
          default: ''
        NBIOTUSER:
          name: 'NB-IoT用户下行报文缓存时长(秒)'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 6
    set_pfcpcmpt_list:
      type: items
      properties:
        BAR:
          name: '是否支持BAR信元'
          type: string
          enum:
          - SUPPORT
          - NOT_SUPPORT
          required: false
          description: '控制PFCP接口是否支持BAR（Buffering Action Rule）信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WNBDRX11'
      SWITCH: ENABLE
    set_smfglbdlbuftime_list:
    - NBIOTUSER: 200
    add_smfapndlbuftime_list:
    - APN: 'test'
      NBIOTUSER: 200
    set_pfcpcmpt_list:
    - BAR: SUPPORT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选：**配置下行数据到达S-GW时，全局的NB-IoT用户下行报文缓存时长。

```jinja2
{%- if is_optional_global_nbiot_downlink_buffer_time -%}
    {%- for item in set_smfglbdlbuftime_list -%}
        SET SMFGLBDLBUFTIME:
        {#- --- 可选参数 --- -#}
        {%- if item.NBIOTUSER is not none -%}
            NBIOTUSER={{item.NBIOTUSER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置下行数据到达S-GW时，指定APN下的NB-IoT用户下行报文缓存时长。

```jinja2
{%- for item in add_smfapndlbuftime_list -%}
    ADD SMFAPNDLBUFTIME:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NBIOTUSER is not none -%}
        NBIOTUSER={{item.NBIOTUSER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置下行数据到达S-GW时，PFCP接口支持BAR（Buffering Action Rule）信元。

### ****SET PFCPCMPT****

```jinja2
{%- for item in set_pfcpcmpt_list -%}
    SET PFCPCMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.BAR is not none -%}
        BAR={{item.BAR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

