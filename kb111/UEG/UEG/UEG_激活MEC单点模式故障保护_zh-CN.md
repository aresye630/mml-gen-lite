---
id: ''
name: 激活MEC单点模式故障保护
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活MEC单点模式故障保护特性的操作过程。  MEC单点模式是指位于边缘侧的“**ULCL UPF+辅锚点UPF**”的共部署节点只有一个，没有和它形成双主/多主负荷分担的其他UPF。该模式下当该单节点UPF故障，SMF能够感知故障并将该UPF从用户会话中删除，此时用户可通过**主锚点UPF**来访问本地DN和Internet大网。  ULCL UPF+辅锚点UPF表示ULCL UPF和辅锚点UPF共部署节点，以下用“**ULCL UPF+辅锚点UPF**”来表示。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UNC特性指南","WSFD-108005 MEC单点模式故障保护","激活MEC单点模式故障保护"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活MEC单点模式故障保护特性的操作过程。MEC单点模式是指位于边缘侧的“**ULCL UPF+辅锚点UPF**”的共部署节点只有一个，没有和它形成双主/多主负荷分担的其他UPF。该模式下当该单节点UPF故障，SMF能够感知故障并将该UPF从用户会话中删除，此时用户可通过**主锚点UPF**来访问本地DN和Internet大网。ULCL UPF+辅锚点UPF表示ULCL UPF和辅锚点UPF共部署节点，以下用“**ULCL UPF+辅锚点UPF**”来表示。

## 必备事项
前提条件

* 请仔细阅读WSFD-108005 MEC单点模式故障保护。
* 已完成加载License。
* 以下配置过程是基于SMF和**主锚点UPF**以及**“ULCL UPF+辅锚点UPF”**的对接配置已完成情况下的操作，SMF和主锚点UPF的对接配置参见N4接口配置，SMF和**“ULCL UPF+辅锚点UPF”**的对接配置参见配置SMF和“UL CL UPF+辅锚点UPF”对接。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_upfpfcppara_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: '**配置**SMF对“ULCL UPF+辅锚点UPF”的心跳探测机制**。'
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
    set_upfaultoperpara_list:
      type: items
      properties:
        UPMIGRATE:
          name: '故障迁移速率（个/秒）'
          type: integer
          minimum: 100
          maximum: 5000
          required: false
          description: '**“故障迁移速率（个/秒）”决定了“ULCL UPF+辅锚点UPF”单点部署模式下**UPF故障时SMF删除用户N4会话的速率。**'
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
    add_upfpfcppara_list:
    - UPFINSTANCEID: 'UPF_Instance_0'
      HBINTERVAL: 30
      HBT1: 5
      HBN1: 3
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
    set_upfaultoperpara_list:
    - UPMIGRATE: 1000
    set_licenseswitch_list:
    - LICITEM: 'LKV2SMECFP01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置UPF粒度的SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

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

### 3 **配置****“ULCL UPF+辅锚点UPF”单点部署模式下****UPF故障时SMF删除用户N4会话的速率。**

```jinja2
{%- for item in set_upfaultoperpara_list -%}
    SET UPFAULTOPERPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.UPMIGRATE is not none -%}
        UPMIGRATE={{item.UPMIGRATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

