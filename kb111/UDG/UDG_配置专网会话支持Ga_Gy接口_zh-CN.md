---
id: ''
name: 配置专网会话支持Ga/Gy接口
ne_type: UDG
type: feature
description: 本章节用于指导配置在用户4G/5G NSA接入时，专网SMF基于Ga/Gy接口选择计费网元CG/OCS并完成对用户流量的计费。  根据用户接入网络类型的不同（4G/5G NSA/5G SA），用户的公网会话可以是4G会话，也可以是5G会话，但是在创建用户专网会话时，智能分流PGW-C会将默认将4G信息转换为5G信息，再触发专网会话的建立，因此用户专网会话默认都是5G会话。这种情况下，当运营商的计费网络未改造，仅支持Ga/Gy的组网方式，不支持基于5G SA的N40组网时，需要专网SMF能够基于Gy/Ga接口传递4G计费的关键信息给OCS或CG，如携带4G格式的位置信息/QoS信息/用户接入网元类型等。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置SMF","配置专网会话支持Ga/Gy接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节用于指导配置在用户4G/5G NSA接入时，专网SMF基于Ga/Gy接口选择计费网元CG/OCS并完成对用户流量的计费。根据用户接入网络类型的不同（4G/5G NSA/5G SA），用户的公网会话可以是4G会话，也可以是5G会话，但是在创建用户专网会话时，智能分流PGW-C会将默认将4G信息转换为5G信息，再触发专网会话的建立，因此用户专网会话默认都是5G会话。这种情况下，当运营商的计费网络未改造，仅支持Ga/Gy的组网方式，不支持基于5G SA的N40组网时，需要专网SMF能够基于Gy/Ga接口传递4G计费的关键信息给OCS或CG，如携带4G格式的位置信息/QoS信息/用户接入网元类型等。

## 必备事项
前提条件

* 已完成专网SMF基于Ga/Gy接口和CG/OCS的对接配置。
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
    add_apnchgmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          required: false
          description: '**该参数指示用户类型和其接入方式的对应关系，专网会话为5G会话，因此该参数取值UE5G\_RAT5G。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定的计费接口'
          type: string
          required: false
          description: '该参数表示在参数“TMACCTYPE”指示的组合方式下，专网SMF选择什么样接口类型的计费网元，如选择Ga/Gy接口类型的计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnga5greuseavp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAT:
          name: '无线接入技术'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的RAT信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULI:
          name: '用户位置信息'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的位置信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVINGNODETYPE:
          name: '服务节点类型'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的接入网元信息（如MME）给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apngy5greuseavp_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '对应园区专用DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAT:
          name: '无线接入技术'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的RAT信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULI:
          name: '用户位置信息'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的位置信息给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVINGNODETYPE:
          name: '服务节点类型'
          type: string
          required: false
          description: '该参数取值为ENABLE时，专网SMF会携带用户真实的接入网元信息（如MME）给计费网元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3EGAGY5G01'
      SWITCH: ENABLE
    add_apnchgmode_list:
    - APN: stjwt.gd
      TMACCTYPE: UE5G_RAT5G
      FORCED: GaGyMode
    add_apnga5greuseavp_list:
    - APN: stjwt.gd
      RAT: ENABLE
      ULI: ENABLE
      SERVINGNODETYPE: ENABLE
    add_apngy5greuseavp_list:
    - APN: stjwt.gd
      RAT: ENABLE
      ULI: ENABLE
      SERVINGNODETYPE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 激活5G SA计费的增强型GaGy接口的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置基于园区APN的计费接口选择方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnchgmode_list的变量区（command: ADD APNCHGMODE） -#}
<!-- MISSING_MACRO: command=ADD APNCHGMODE list_name=add_apnchgmode_list step_id=2 -->
```

### 3 配置Ga接口组网方式下专网SMF给CG携带计费信息类型。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnga5greuseavp_list的变量区（command: ADD APNGA5GREUSEAVP） -#}
<!-- MISSING_MACRO: command=ADD APNGA5GREUSEAVP list_name=add_apnga5greuseavp_list step_id=3 -->
```

### 4 配置Gy接口组网方式下专网SMF给OCS携带计费信息类型。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apngy5greuseavp_list的变量区（command: ADD APNGY5GREUSEAVP） -#}
<!-- MISSING_MACRO: command=ADD APNGY5GREUSEAVP list_name=add_apngy5greuseavp_list step_id=4 -->
```

