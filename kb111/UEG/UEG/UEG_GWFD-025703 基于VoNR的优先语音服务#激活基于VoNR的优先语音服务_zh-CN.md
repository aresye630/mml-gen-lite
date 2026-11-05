---
id: GWFD-025703
name: 激活基于VoNR的优先语音服务
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于VoNR的优先语音服务的操作过程。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-025700 5G网络语音业务","GWFD-025703 基于VoNR的优先语音服务","激活基于VoNR的优先语音服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于VoNR的优先语音服务的操作过程。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-025703 基于VoNR的优先语音服务特性概述。
* 已部署VoNR基础语音业务，详细请参考GWFD-025701 VoNR基础语音业务。
* AMF上已根据PPI配置不同的寻呼定时器、重发次数和重呼间隔时间，生成差异化的寻呼策略，为语音业务配置高优先级的寻呼策略。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开启PPI（寻呼策略指示）功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PPISWITCH:
          name: 'PPI 功能开关'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    set_smffunc_list:
      type: items
      properties:
        PPISWITCH:
          name: 'PPI功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpapn_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开启PPI（寻呼策略指示）功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PPISWITCH:
          name: 'PPI 功能开关'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
  examples:
    add_cpapn_list:
    - APN: 'ims'
      PPISWITCH: ENABLE
    set_smffunc_list:
    - PPISWITCH: ENABLE
    add_cpapn_list_1:
    - APN: 'ims'
      PPISWITCH: INHERIT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**通过 **ADD CPAPN**命令开启PPI功能。

#### 2.1 //脚本一：直接通过ADD CPAPN命令开启PPI功能。

```jinja2
{%- if is_optional_enable_ppi -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PPISWITCH is not none -%}
            PPISWITCH={{item.PPISWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 通过 **ADD CPAPN**命令中继承**SET SMFFUNC**命令中的全局配置开启PPI功能。

#### 3.1 //脚本二：通过ADD CPAPN命令中继承SET SMFFUNC命令中的全局配置开启PPI功能。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.PPISWITCH is not none -%}
        PPISWITCH={{item.PPISWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cpapn_list_1 -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PPISWITCH is not none -%}
        PPISWITCH={{item.PPISWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

