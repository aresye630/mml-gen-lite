---
id: GWFD-024301
name: 激活基于原因值的UE行为调整（AMF）
ne_type: UEG
type: feature
description: 当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，AMF可以控制给终端下发的原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。  给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-024300 系统管理","GWFD-024301 基于原因值的UE行为调整（适用于AMF）","激活基于原因值的UE行为调整（AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，AMF可以控制给终端下发的原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。

## 必备事项
前提条件

请仔细阅读GWFD-024301 基于原因值的UE行为调整（适用于AMF）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_ngmmproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - AUSF_DISCOVERY
          - AIR
          - AUTHENTICATION
          - SMC
          - CHECK_IMEI
          - UDM_DISCOVERY
          - UDM_REGISTRATION
          - UDM_GET_SUBSCRIBER_DATA
          - UDM_SUBSCIBE
          - PCF_DISCOVERY
          - PCF_POLICY
          - OTHER_PROC
          - CAG
          required: true
          description: '**设置5G移动性管理流程对UE的调整参数**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUSFDISCNOFOUND:
          name: 'AUSF发现拒绝原因值(Not Found)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUSFDISCOTHER:
          name: 'AUSF发现拒绝原因值(其他原因)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHRESCHKFAIL:
          name: 'Authentication拒绝原因值(RES检查失败)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMACFAIL:
          name: 'Authentication拒绝原因值(UE返回MAC Failure)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHSYNCHFAIL:
          name: 'Authentication拒绝原因值(UE返回Synch Failure)'
          type: integer
          minimum: 0
          maximum: 111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_ngmmproctrl_list:
    - PROT: AUSF_DISCOVERY
      AUSFDISCNOFOUND: 27
      AUSFDISCOTHER: 27
      AUTHRESCHKFAIL: 27
      AUTHMACFAIL: 27
      AUTHSYNCHFAIL: 27
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **设置5G移动性管理流程对UE的调整参数**。

```jinja2
{%- for item in set_ngmmproctrl_list -%}
    SET NGMMPROCTRL:
    {#- --- 必选参数 --- -#}
    PROT={{item.PROT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROT=AUSF_DISCOVERY 时可选 --- -#}
    {%- if item.PROT == 'AUSF_DISCOVERY' -%}
        {%- if item.AUSFDISCNOFOUND is not none -%}
            AUSFDISCNOFOUND={{item.AUSFDISCNOFOUND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=AUSF_DISCOVERY 时可选 --- -#}
    {%- if item.PROT == 'AUSF_DISCOVERY' -%}
        {%- if item.AUSFDISCOTHER is not none -%}
            AUSFDISCOTHER={{item.AUSFDISCOTHER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
    {%- if item.PROT == 'AUTHENTICATION' -%}
        {%- if item.AUTHRESCHKFAIL is not none -%}
            AUTHRESCHKFAIL={{item.AUTHRESCHKFAIL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
    {%- if item.PROT == 'AUTHENTICATION' -%}
        {%- if item.AUTHMACFAIL is not none -%}
            AUTHMACFAIL={{item.AUTHMACFAIL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROT=AUTHENTICATION 时可选 --- -#}
    {%- if item.PROT == 'AUTHENTICATION' -%}
        {%- if item.AUTHSYNCHFAIL is not none -%}
            AUTHSYNCHFAIL={{item.AUTHSYNCHFAIL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

