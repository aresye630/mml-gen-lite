---
id: ''
name: 激活PFC（仅用于Gb 模式）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活PFC（仅用于Gb模式）特性的操作过程。  PFC（Packet Flow Context）是指通过为同一用户的多个QoS相近的PDP分配相同的PFI（Packet Flow Identifier），实现数据流的捆绑传送。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-105101 PFC（仅用于Gb 模式）","激活PFC（仅用于Gb 模式）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活PFC（仅用于Gb模式）特性的操作过程。PFC（Packet Flow Context）是指通过为同一用户的多个QoS相近的PDP分配相同的PFI（Packet Flow Identifier），实现数据流的捆绑传送。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读WSFD-105101 PFC特性概述。
* 完成加载License。

* 需要对端网元PCU和GGSN激活PFC（仅用于Gb 模式）特性。
* 信令实体NSE（Network Service Entity）已经配置完成，具体步骤请参见配置到PCU的数据。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    mod_nse_list:
      type: items
      properties:
        NSEI:
          name: 'NSE标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PFC:
          name: '是否支持PFC'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARP:
          name: '是否携带ARP信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RACAP:
          name: '是否携带RA Capability信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PFC02'
      SWITCH: ENABLE
    mod_nse_list:
    - NSEI: 10
      PFC: YES
      ARP: ''
      RACAP: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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

### 3 修改信令实体，打开PFC开关。

```jinja2
{%- for item in mod_nse_list -%}
    MOD NSE:
    {#- --- 必选参数 --- -#}
    NSEI={{item.NSEI}},
    {#- --- 可选参数 --- -#}
    {%- if item.PFC is not none -%}
        PFC={{item.PFC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PFC=YES 时可选 --- -#}
    {%- if item.PFC == 'YES' -%}
        {%- if item.ARP is not none -%}
            ARP={{item.ARP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PFC=YES 时可选 --- -#}
    {%- if item.PFC == 'YES' -%}
        {%- if item.RACAP is not none -%}
            RACAP={{item.RACAP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“PFC”（是否支持PFC）选择“YES”（是）。

