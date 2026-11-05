---
id: ''
name: 激活支持VoWiFi到EPS Fallback的切换
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活VoWiFi到VoNR切换支持EPS Fallback特性的操作过程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-201305 支持VoWiFi到EPS Fallback的切换","激活支持VoWiFi到EPS Fallback的切换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活VoWiFi到VoNR切换支持EPS Fallback特性的操作过程。适用于SMF。

## 必备事项
前提条件

前提条件

请仔细阅读WSFD-201305 支持VoWiFi到EPS Fallback的切换特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        WLANHONREPSFBSW:
          name: 'WLAN切换NG-RAN失败转EPS FallBack功能开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '支持WLAN切换NG-RAN失败转EPS FallBack功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_smffunc_list:
    - WLANHONREPSFBSW: Support
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置支持WLAN切换NG-RAN失败转EPS FallBack功能。

#### 2.1 //配置支持WLAN切换NG-RAN失败转EPS FallBack功能。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.WLANHONREPSFBSW is not none -%}
        WLANHONREPSFBSW={{item.WLANHONREPSFBSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

