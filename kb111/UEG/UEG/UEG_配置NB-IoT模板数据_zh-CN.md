---
id: ''
name: 配置NB-IoT模板数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT模板数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","NB-IoT用户数据配置","配置NB-IoT模板数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成NB-IoT模板数据的配置。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成NB-IoT的用户数据规划。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_apntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          maxLength: 63
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        PDNGWALLOCTYPE:
          name: 'PDN GW地址分配类型'
          type: string
          enum:
          - STATIC
          - DYNAMIC
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: DYNAMIC
        NONIPDATADELMECH:
          name: 'Non-IP传输模式'
          type: string
          enum:
          - SGi_BASED_DATA_DELIVERY
          - SCEF_BASED_DATA_DELIVERY
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: SGi_BASED_DATA_DELIVERY
  examples:
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '10'
      TPLNAME: EPS-QoS
      QOSCLASUID: '5'
      PRILEVEL: '1'
      AMBRMAXREQBWUL: '100000'
      AMBRMAXREQBWDL: '200000'
    add_apntpl_list:
    - HLRSN: 1
      TPLID: 1
      APN: 'APN1'
      PDNGWALLOCTYPE: DYNAMIC
      NONIPDATADELMECH: SGi_BASED_DATA_DELIVERY
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD EPSQOSTPL**命令，增加EPS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=2 -->
```

### 参数“QoS分类ID”和“分配/保留优先级数据”必须同时存在，取值越小，优先级越高。

### 3 执行**ADD APNTPL**命令，增加APN模板。

```jinja2
{%- for item in add_apntpl_list -%}
    ADD APNTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NONIPDATADELMECH is not none -%}
        NONIPDATADELMECH={{item.NONIPDATADELMECH}},
    {%- endif -%}
    {%- if item.PDNGWALLOCTYPE is not none -%}
        PDNGWALLOCTYPE={{item.PDNGWALLOCTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“接入点名称”必须设置。

