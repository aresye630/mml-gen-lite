---
id: GWFD-021504
name: 激活用户身份保密性功能（适用于4G）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活用户身份保密特性的操作过程。  用户身份保密性功能是通过GUTI的分配来实现。分配GUTI（Globally Unique Temporary UE Identity）的目的是为入网的用户提供一个临时标识，同时这个标识不会展现用户的永久性标识。  适用于MME
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-021500 数据安全管理","GWFD-021504 用户身份保密性功能","激活用户身份保密性功能（适用于4G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活用户身份保密特性的操作过程。用户身份保密性功能是通过GUTI的分配来实现。分配GUTI（Globally Unique Temporary UE Identity）的目的是为入网的用户提供一个临时标识，同时这个标识不会展现用户的永久性标识。适用于MME

## 必备事项
前提条件

* 请仔细阅读GWFD-021504 用户身份保密性功能特性概述（适用于4G）。
* EPS网络中各网元系统及操作维护台运行正常。
* UE成功在UEG上附着。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_emm_list:
      type: items
      properties:
        GUTITMR:
          name: 'GUTI重分配定时器'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: '重分配GUTI的相关参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUTIREALLOC:
          name: 'Attach或TAU中重分配GUTI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUTIREALLOCTMR:
          name: 'GUTI重分配最大间隔(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_cpsys_list:
      type: items
      properties:
        TMSIALLOC:
          name: 'TMSI资源分配方式'
          type: string
          enum:
          - ENHAN
          - UNENHAN
          required: false
          description: 'TMSI资源分配方式'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_emm_list:
    - GUTITMR: 1
      GUTIREALLOC: YES
      GUTIREALLOCTMR: 1
    set_cpsys_list:
    - TMSIALLOC: ENHAN
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置GUTI重分配策略。

### 进入“MML命令行-UEG”窗口。

```jinja2
{%- for item in set_emm_list -%}
    SET EMM:
    {#- --- 可选参数 --- -#}
    {%- if item.GUTITMR is not none -%}
        GUTITMR={{item.GUTITMR}},
    {%- endif -%}
    {%- if item.GUTIREALLOC is not none -%}
        GUTIREALLOC={{item.GUTIREALLOC}},
    {%- endif -%}
    {%- if item.GUTIREALLOCTMR is not none -%}
        GUTIREALLOCTMR={{item.GUTIREALLOCTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置GUTI分配方式。

### 系统默认采用增强TMSI分配方式，只有当增强算法存在无法解决的问题时，才使用非增强算法。为确保GUTI分配方式在各业务VM上的一致性，当执行此步骤修改GUTI分配方式后，需立即整系统重启。

### 进入“MML命令行-UEG”窗口。

### ****SET CPSYS****

```jinja2
{%- for item in set_cpsys_list -%}
    SET CPSYS:
    {#- --- 可选参数 --- -#}
    {%- if item.TMSIALLOC is not none -%}
        TMSIALLOC={{item.TMSIALLOC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

