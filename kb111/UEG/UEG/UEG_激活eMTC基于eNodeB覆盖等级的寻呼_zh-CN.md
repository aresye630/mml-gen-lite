---
id: GWFD-026303
name: 激活eMTC基于eNodeB覆盖等级的寻呼
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活eMTC基于eNodeB覆盖等级的寻呼的操作过程。  基于eNodeB覆盖等级的寻呼，指MME根据eNodeB上报的推荐寻呼的eNodeB进行寻呼优化，并在寻呼消息中将eNodeB上报的推荐寻呼的小区和小区覆盖等级通过寻呼辅助信息传给eNodeB，用以支持eNodeB覆盖等级的寻呼。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026300 eMTC基本功能","GWFD-026303 eMTC基于eNodeB覆盖等级的寻呼","激活eMTC基于eNodeB覆盖等级的寻呼"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活eMTC基于eNodeB覆盖等级的寻呼的操作过程。基于eNodeB覆盖等级的寻呼，指MME根据eNodeB上报的推荐寻呼的eNodeB进行寻呼优化，并在寻呼消息中将eNodeB上报的推荐寻呼的小区和小区覆盖等级通过寻呼辅助信息传给eNodeB，用以支持eNodeB覆盖等级的寻呼。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026303 eMTC基于eNodeB覆盖等级的寻呼特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_m2mctrl_list:
      type: items
      properties:
        CHK_ENB_CE_SW:
          name: 'eNodeB覆盖增强检查开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1cmpt_list:
      type: items
      properties:
        NPAS:
          name: 'Next Paging Area Scope开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_m2mctrl_list:
    - CHK_ENB_CE_SW: ON
    set_s1cmpt_list:
    - NPAS: YES
    set_licenseswitch_list:
    - LICITEM: 'LKV2CELP02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**配置“eNodeB覆盖增强检查开关”为“打开”。

```jinja2
{%- if is_optional_enb_coverage_enhancement_check_switch -%}
    {%- for item in set_m2mctrl_list -%}
        SET M2MCTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.CHK_ENB_CE_SW is not none -%}
            CHK_ENB_CE_SW={{item.CHK_ENB_CE_SW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当“eNodeB覆盖增强检查开关”为“打开”时，MME只向支持覆盖增强寻呼的eNodeB下发携带寻呼辅助信息（Assistance Data for Paging）信元的寻呼请求。关于此参数的详细说明请参考**SET M2MCTRL**。

### 3 **可选：**配置“Next Paging Area Scope开关”为“YES”。

```jinja2
{%- if is_optional_next_paging_area_scope_switch -%}
    {%- for item in set_s1cmpt_list -%}
        SET S1CMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.NPAS is not none -%}
            NPAS={{item.NPAS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

