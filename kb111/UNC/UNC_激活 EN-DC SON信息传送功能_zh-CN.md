---
id: ''
name: 激活 EN-DC SON信息传送功能
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活eNodeB与en-gNodeB之间通过EN-DC SON信息传送功能特性的操作过程。  EN-DC自组织网络SON（Self Organization Network）信息传送即eNodeB与相邻en-gNodeB之间通过MME消息交互，实现配置信息的传递。  适用于MME。  本场景应用于eNodeB与en-gNodeB之间通过EN-DC SON流程自动发现X2地址的组网。  如图1所示，eNodeB2和en-gNodeB连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与en-gNodeB，en-gNodeB与eNodeB2之间互为相邻，之间通过X2接口传递切换和eNodeB/en-gNodeB状态信息。  **图1** Intra MME地址学习场景下的EN-DC SON组网图  **图2** Inter MME地址学习场景下的EN-DC SON组网图
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","WSFD-104402 eNodeB SON信息传送功能","激活信息传送功能","激活 EN-DC SON信息传送功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活eNodeB与en-gNodeB之间通过EN-DC SON信息传送功能特性的操作过程。EN-DC自组织网络SON（Self Organization Network）信息传送即eNodeB与相邻en-gNodeB之间通过MME消息交互，实现配置信息的传递。适用于MME。本场景应用于eNodeB与en-gNodeB之间通过EN-DC SON流程自动发现X2地址的组网。如图1所示，eNodeB2和en-gNodeB连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与en-gNodeB，en-gNodeB与eNodeB2之间互为相邻，之间通过X2接口传递切换和eNodeB/en-gNodeB状态信息。**图1** Intra MME地址学习场景下的EN-DC SON组网图**图2** Inter MME地址学习场景下的EN-DC SON组网图

## 必备事项
前提条件

* 请仔细阅读WSFD-104402 eNodeB SON信息传送功能特性概述。
* 完成加载License。
* MME、eNodeB网元上首先完成基本业务的数据配置。S1–MME、S10接口的数据配置，按网络规划配置数据进行，具体请参见配置到eNodeB的数据、配置到MME的数据，本文不再赘述。
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
    set_s1cmpt_list:
      type: items
      properties:
        ENDCSON:
          name: '是否支持EN-DC SON'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SON02'
      SWITCH: ENABLE
    set_s1cmpt_list:
    - ENDCSON: SUPPORT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 执行**SET S1CMPT**命令打开EN-DC SON功能开关。

```jinja2
{%- for item in set_s1cmpt_list -%}
    SET S1CMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.ENDCSON is not none -%}
        ENDCSON={{item.ENDCSON}},
    {%- endif -%}
    ;
{%- endfor -%}
```

