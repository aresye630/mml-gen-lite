---
id: ''
name: 激活负荷动态调整
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活负荷动态调整特性的操作过程。  适用于GGSN、SGW-C、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","可靠性功能","WSFD-010005 负荷动态调整","激活负荷动态调整"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活负荷动态调整特性的操作过程。适用于GGSN、SGW-C、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读WSFD-010005 负荷动态调整特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_tokenallocwt_list:
      type: items
      properties:
        SERVICETYPE:
          name: '服务类型'
          type: string
          enum:
          - UAM_0
          - USM_0
          required: true
          description: '设置服务类型为USM\_0的微服务的Token分配权重管理策略为动态策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WEIGHTPOLICY:
          name: '权重策略'
          type: string
          enum:
          - DEFAULT
          - STATIC
          - DYNAMIC
          - DEFAULTHET
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_dynamicpolicy_list:
      type: items
      properties:
        SERVICETYPE:
          name: '服务类型'
          type: string
          required: false
          description: '设置服务类型为USM\_0的微服务的动态权重调整相关参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADJUSTTHRESHOLD:
          name: '调整阈值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GAPTHRESHOLD:
          name: '差值门限'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GLBBASEOST:
          name: '基础消耗'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GAPBUSY:
          name: '忙时差值门限'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONFIRM:
          name: 'CONFIRM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpuabilitycfg_list:
      type: items
      properties:
        CPUTYPE:
          name: 'CPU类型'
          type: string
          required: false
          description: '可选，增加不同CPU类型的能力系数和基础消耗。  须知：  如果配置不合理会导致会动态权重失效以及token迁移不能处于稳态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPUGENERATE:
          name: 'CPU代际'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPUFREQUENCY:
          name: 'CPU主频'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        COEFFICIENT:
          name: '能力系数'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BASECOST:
          name: '基础消耗'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONFIRM:
          name: 'CONFIRM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_tokenallocwt_list:
    - SERVICETYPE: USM_0
      WEIGHTPOLICY: DYNAMIC
    set_dynamicpolicy_list:
    - SERVICETYPE: USM_0
      ADJUSTTHRESHOLD: '75'
      GAPTHRESHOLD: '6'
      GLBBASEOST: '5'
      GAPBUSY: '10'
      CONFIRM: Y
    add_cpuabilitycfg_list:
    - CPUTYPE: X86_64
      CPUGENERATE: '1'
      CPUFREQUENCY: '2'
      COEFFICIENT: '500'
      BASECOST: '0'
      CONFIRM: Y
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置服务类型为USM\_0的微服务的Token分配权重管理策略为动态策略。

```jinja2
{%- for item in set_tokenallocwt_list -%}
    SET TOKENALLOCWT:
    {#- --- 必选参数 --- -#}
    SERVICETYPE={{item.SERVICETYPE}},
    WEIGHTPOLICY={{item.WEIGHTPOLICY}},
    ;
{%- endfor -%}
```

### 3 设置服务类型为USM\_0的微服务的动态权重调整相关参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_dynamicpolicy_list的变量区（command: SET DYNAMICPOLICY） -#}
<!-- MISSING_MACRO: command=SET DYNAMICPOLICY list_name=set_dynamicpolicy_list step_id=3 -->
```

### 4 增加不同CPU类型的能力系数和基础消耗。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cpuabilitycfg_list的变量区（command: ADD CPUABILITYCFG） -#}
<!-- MISSING_MACRO: command=ADD CPUABILITYCFG list_name=add_cpuabilitycfg_list step_id=4 -->
```

