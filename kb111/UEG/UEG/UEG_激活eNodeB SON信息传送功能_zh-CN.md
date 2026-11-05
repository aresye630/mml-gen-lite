---
id: GWFD-023104
name: 激活eNodeB SON信息传送功能
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活eNodeB SON信息传送功能特性的操作过程。  适用于MME。  本场景应用于eNodeB全部支持SON流程自动发现X2地址的组网。  如图1所示，eNodeB2和eNodeB3连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与eNodeB2，eNodeB2与eNodeB3之间互为相邻，之间通过X2接口传递切换和eNodeB状态信息。  **图1** SON组网图
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-023104 eNodeB SON信息传送功能","激活信息传送功能","激活eNodeB SON信息传送功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活eNodeB SON信息传送功能特性的操作过程。适用于MME。本场景应用于eNodeB全部支持SON流程自动发现X2地址的组网。如图1所示，eNodeB2和eNodeB3连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与eNodeB2，eNodeB2与eNodeB3之间互为相邻，之间通过X2接口传递切换和eNodeB状态信息。**图1** SON组网图

## 必备事项
前提条件

* 请仔细阅读GWFD-023104 eNodeB SON信息传送功能特性概述。
* 完成加载License。
* MME、eNodeB网元上首先完成基本业务的数据配置。S1–MME、S10接口的数据配置，按网络规划配置数据进行，具体请参见配置到eNodeB的数据、配置到MME的数据，本文不再赘述。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: ''
      SWITCH: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

### 进入“MML命令行-UEG”窗口。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

