---
id: ''
name: 配置话单可靠性保证（SGSN）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活话单可靠性保证功能的操作过程。  计费中心的计费依据是用户的话单记录，SGSN要保证话单无重复、无丢失和内容真实、可靠，从而来保证计费的准确性、可靠性和实时性。  适用于SGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置话单可靠性保证（SGSN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活话单可靠性保证功能的操作过程。计费中心的计费依据是用户的话单记录，SGSN要保证话单无重复、无丢失和内容真实、可靠，从而来保证计费的准确性、可靠性和实时性。适用于SGSN。

## 必备事项
前提条件

* 请仔细阅读离线计费话单（SGSN）。
* 无特殊前提条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chgcdr_list:
      type: items
      properties:
        LRSNP:
          name: '配置本地话单序列号'
          type: string
          enum:
          - ABSENT
          - PRESENT
          required: false
          description: '本地话单序列号'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_chgga_list:
      type: items
      properties:
        HDDFSL:
          name: '硬盘空间不足门限(%)'
          type: integer
          minimum: 50
          maximum: 90
          required: false
          description: '硬盘话单文件覆盖功能'
          data_source: ''
          pattern: ''
          default: ''
        CDROVERWRITE:
          name: '覆盖硬盘上话单文件'
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
    set_chgcdr_list:
    - LRSNP: PRESENT
    set_chgga_list:
    - HDDFSL: 90
      CDROVERWRITE: YES
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置本地话单序列号。

```jinja2
{%- for item in set_chgcdr_list -%}
    SET CHGCDR:
    {#- --- 可选参数 --- -#}
    {%- if item.LRSNP is not none -%}
        LRSNP={{item.LRSNP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“LRSNP”（配置本地话单序列号）固定选择“PRESENT”（有）。

### 3 配置硬盘话单文件覆盖功能。

```jinja2
{%- for item in set_chgga_list -%}
    SET CHGGA:
    {#- --- 可选参数 --- -#}
    {%- if item.HDDFSL is not none -%}
        HDDFSL={{item.HDDFSL}},
    {%- endif -%}
    {%- if item.CDROVERWRITE is not none -%}
        CDROVERWRITE={{item.CDROVERWRITE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“CDROVERWRITE”（覆盖硬盘上话单文件）固定选择“YES”（覆盖）。

