---
id: GWFD-020802
name: 激活路径管理（适用于SGW-C/PGW-C/SMF）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活路径管理特性的操作过程。  路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。  适用于SGW-C/PGW-C/SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-020800 基本业务","GWFD-020802 路径管理","激活路径管理（适用于SGW-C/PGW-C/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活路径管理特性的操作过程。路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。适用于SGW-C/PGW-C/SMF。

## 必备事项
前提条件

请仔细阅读WSFD-010600 路径管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_pfcppara_list:
      type: items
      properties:
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: '配置PFCP路径管理参数。 说明：  增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HBT1:
          name: '心跳消息超时间隔(秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBN1:
          name: '心跳消息发送次数阈值'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '去活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DACTINTERVAL:
          name: '去活间隔(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upfpfcppara_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例标识'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HBT1:
          name: '心跳消息超时间隔(秒)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBN1:
          name: '心跳消息发送次数阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '去活用户开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DACTINTERVAL:
          name: '去活间隔(秒)'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MIGINTERVAL:
          name: 'MIGINTERVAL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKFLAG:
          name: 'CHECKFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_pfcppara_list:
    - HBINTERVAL: 30
      HBT1: 3
      HBN1: 5
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
    add_upfpfcppara_list:
    - NFINSTANCENAME: UPF_Instance_1
      HBINTERVAL: '60'
      HBT1: '5'
      HBN1: '3'
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: '100'
      MIGINTERVAL: '60'
      CHECKFLAG: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

```jinja2
{%- for item in set_pfcppara_list -%}
    SET PFCPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.HBT1 is not none -%}
        HBT1={{item.HBT1}},
    {%- endif -%}
    {%- if item.HBN1 is not none -%}
        HBN1={{item.HBN1}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEACTIVEFLAG=ENABLE 时可选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        {%- if item.DACTINTERVAL is not none -%}
            DACTINTERVAL={{item.DACTINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置UPF粒度的SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upfpfcppara_list的变量区（command: ADD UPFPFCPPARA） -#}
<!-- MISSING_MACRO: command=ADD UPFPFCPPARA list_name=add_upfpfcppara_list step_id=3 -->
```

