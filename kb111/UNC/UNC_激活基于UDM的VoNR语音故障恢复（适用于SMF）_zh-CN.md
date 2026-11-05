---
id: ''
name: 激活基于UDM的VoNR语音故障恢复（适用于SMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于UDM的VoNR语音故障恢复的操作过程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-221002 基于UDM的VoNR语音故障恢复","激活基于UDM的VoNR语音故障恢复（适用于SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于UDM的VoNR语音故障恢复的操作过程。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-221002 基于UDM的VoNR语音故障恢复特性概述。
* 已完成加载License“82200DHD LKV2UDMVTR01 基于UDM的VoNR语音故障恢复”。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_globalims_list:
      type: items
      properties:
        UDMPCSCF:
          name: '基于UDM的P-CSCF Restoration功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '打开SMF支持基于UDM进行P-CSCF故障恢复的功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDMPCSCFMODE:
          name: '基于UDM的P-CSCF Restoration功能模式'
          type: string
          enum:
          - PDUREACTIVATE
          - PCSCFADDRUPDATE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_globalims_list:
    - UDMPCSCF: ENABLE
      UDMPCSCFMODE: PCSCFADDRUPDATE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置支持SMF基于UDM的VoNR语音故障恢复特性。

```jinja2
{%- for item in set_globalims_list -%}
    SET GLOBALIMS:
    {#- --- 可选参数 --- -#}
    {%- if item.UDMPCSCF is not none -%}
        UDMPCSCF={{item.UDMPCSCF}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UDMPCSCF=ENABLE 时可选 --- -#}
    {%- if item.UDMPCSCF == 'ENABLE' -%}
        {%- if item.UDMPCSCFMODE is not none -%}
            UDMPCSCFMODE={{item.UDMPCSCFMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

