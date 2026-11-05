---
id: ''
name: 配置“主锚点UPF双主负荷分担部署模式”
ne_type: UEG
type: feature
description: 本操作指导介绍“主锚点UPF双主负荷分担部署模式”容灾组网配置的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UNC特性指南","WSFD-108004 MEC冗余模式故障保护","配置“主锚点UPF双主负荷分担部署模式”"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍“主锚点UPF双主负荷分担部署模式”容灾组网配置的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-108004 MEC冗余模式故障保护。
* 已完成加载License。
* 以下配置过程是基于SMF和**主锚点UPF**的对接配置已完成情况下的操作。且需要在**主锚点UPF双主负荷分担部署模式**下确保SMF对每个主锚点UPF配置相同的DNN、位置区选择策略。SMF和主锚点UPF的对接配置参见N4接口配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UP唯一标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '**配置主锚点UPF双主负荷分担部署模式****下的故障保护机制**。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UP位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcppara_list:
      type: items
      properties:
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: ''
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
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 30
        HBT1:
          name: '心跳消息超时间隔(秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        HBN1:
          name: '心跳消息发送次数阈值'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
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
          default: ENABLE
        DACTINTERVAL:
          name: '去活间隔(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 900
    set_deactiverate_list:
      type: items
      properties:
        RATE:
          name: '去活速率'
          type: integer
          minimum: 10
          maximum: 2000
          required: true
          description: ''
          data_source: '本端规划'
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
    mod_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
    set_pfcppara_list:
    - HBINTERVAL: 30
      HBT1: 3
      HBN1: 5
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
    add_upfpfcppara_list:
    - UPFINSTANCEID: 'UPF_Instance_1'
      HBINTERVAL: 60
      HBT1: 5
      HBN1: 3
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
    set_deactiverate_list:
    - RATE: 1000
    set_licenseswitch_list:
    - LICITEM: 'LKV2DMECFP01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **配置主锚点UPF双主负荷分担部署模式****下的故障保护机制**。

#### 2.1 确认UPF模式位置特征为Central模式。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

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

#### 2.3 配置UPF粒度的SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

```jinja2
{%- for item in add_upfpfcppara_list -%}
    ADD UPFPFCPPARA:
    {#- --- 必选参数 --- -#}
    UPFINSTANCEID="{{item.UPFINSTANCEID}}",
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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEACTIVEFLAG=ENABLE 时必选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        DACTINTERVAL={{item.DACTINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置故障场景下对用户会话的去活速率。

```jinja2
{%- for item in set_deactiverate_list -%}
    SET DEACTIVERATE:
    {#- --- 必选参数 --- -#}
    RATE={{item.RATE}},
    ;
{%- endfor -%}
```

### 3 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

