---
id: GWFD-024301
name: 激活基于原因值的UE行为调整（SMF）
ne_type: UEG
type: feature
description: 当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，SMF可以控制给终端下发的NAS原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。  给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-024300 系统管理","GWFD-024301 基于原因值的UE行为调整（适用于SMF）","激活基于原因值的UE行为调整（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，SMF可以控制给终端下发的NAS原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。

## 必备事项
前提条件

请仔细阅读GWFD-024301 基于原因值的UE行为调整 （适用于SMF）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_smcausegrp_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '配置SMF原因值映射组'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSEGRPNM:
          name: '原因值组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_smfcausectrl_list:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          enum:
          - PDU_SESSION_EST_PROC
          - PDU_SESSION_MOD_PROC
          required: true
          description: '配置SMF流程中NAS原因值控制参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '异常来源'
          type: string
          enum:
          - UPF
          - CHG_3GPP
          - POLICY_PCF
          - INNER
          - RADIUS_AUTH
          - RADIUS_CHG
          - UDM
          - CHF_3GPP
          - INNER_EMG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSEGROUPID:
          name: 'NF拒绝导致流程拒绝原因值组号'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CAUSEEXPIRATION:
          name: '响应超时导致流程拒绝的NAS原因值'
          type: integer
          minimum: 0
          maximum: 112
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_smcausemap_list:
      type: items
      properties:
        CAUSEGRPID:
          name: '原因值组标识'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '配置SMF原因值映射关系'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAUSERANGE:
          name: '原因值范围'
          type: string
          enum:
          - DEFAULT
          - SPECIAL
          - SPECIAL_APP_ERR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCAUSE:
          name: '目标原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BGCAUSE:
          name: '起始原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDCAUSE:
          name: '终止原始原因值'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_smcausegrp_list:
    - CAUSEGRPID: 17
      CAUSEGRPNM: 'Default1'
    add_smfcausectrl_list:
    - PROCEDURETYPE: PDU_SESSION_EST_PROC
      NFTYPE: UPF
      CAUSEGROUPID: 17
      CAUSEEXPIRATION: 0
    add_smcausemap_list:
    - CAUSEGRPID: 17
      CAUSERANGE: DEFAULT
      TCAUSE: 27
      BGCAUSE: 0
      EDCAUSE: 200
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置SMF原因值映射组。

```jinja2
{%- for item in add_smcausegrp_list -%}
    ADD SMCAUSEGRP:
    {#- --- 必选参数 --- -#}
    CAUSEGRPID={{item.CAUSEGRPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.CAUSEGRPNM is not none -%}
        CAUSEGRPNM="{{item.CAUSEGRPNM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SMF流程中NAS原因值控制参数。

```jinja2
{%- for item in add_smfcausectrl_list -%}
    ADD SMFCAUSECTRL:
    {#- --- 必选参数 --- -#}
    PROCEDURETYPE={{item.PROCEDURETYPE}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=UPF/CHG_3GPP/POLICY_PCF/RADIUS_AUTH/RADIUS_CHG/UDM/CHF_3GPP 时可选 --- -#}
    {%- if item.NFTYPE in ['UPF', 'CHG_3GPP', 'POLICY_PCF', 'RADIUS_AUTH', 'RADIUS_CHG', 'UDM', 'CHF_3GPP'] -%}
        {%- if item.CAUSEGROUPID is not none -%}
            CAUSEGROUPID={{item.CAUSEGROUPID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=UPF/CHG_3GPP/POLICY_PCF/RADIUS_AUTH/RADIUS_CHG/UDM/CHF_3GPP 时可选 --- -#}
    {%- if item.NFTYPE in ['UPF', 'CHG_3GPP', 'POLICY_PCF', 'RADIUS_AUTH', 'RADIUS_CHG', 'UDM', 'CHF_3GPP'] -%}
        {%- if item.CAUSEEXPIRATION is not none -%}
            CAUSEEXPIRATION={{item.CAUSEEXPIRATION}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置SMF原因值映射关系。

```jinja2
{%- for item in add_smcausemap_list -%}
    ADD SMCAUSEMAP:
    {#- --- 必选参数 --- -#}
    CAUSEGRPID={{item.CAUSEGRPID}},
    CAUSERANGE={{item.CAUSERANGE}},
    TCAUSE={{item.TCAUSE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时必选 --- -#}
    {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
        BGCAUSE={{item.BGCAUSE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CAUSERANGE=SPECIAL/SPECIAL_APP_ERR 时可选 --- -#}
    {%- if item.CAUSERANGE in ['SPECIAL', 'SPECIAL_APP_ERR'] -%}
        {%- if item.EDCAUSE is not none -%}
            EDCAUSE={{item.EDCAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

