---
id: ''
name: 激活基于原因值的UE行为调整（SMF）
ne_type: UNC
type: feature
description: 当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，SMF可以控制给终端下发的NAS原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。  给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","基本接入功能","WSFD-011301 基于原因值的UE行为调整","WSFD-011301 基于原因值的UE行为调整（适用于SMF）","激活基于原因值的UE行为调整（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户接入5G网络，当系统内部以及周边网元异常导致流程失败时，SMF可以控制给终端下发的NAS原因值以调整终端的行为，辅助运营商实现对现网设备兼容性控制的需求。给UE下发的原因值变化可能会导致相应拒绝类话统指标的变化，并对终端行为产生影响，在部署前需要评估影响。关于不同原因值的含义及对终端行为的影响请参见协议3GPP TS 24.501。

## 必备事项
前提条件

请仔细阅读WSFD-011301 基于原因值的UE行为调整 （适用于SMF）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
        CAUSEAPNLOCK:
          name: 'APN锁定或整机锁定导致流程拒绝的NAS原因值'
          type: string
          enum:
          - SRVNOTSUPPORTED
          - INSUFFRES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SRVNOTSUPPORTED
        CAUSEEMG:
          name: '发送消息因紧急业务配置导致流程拒绝的NAS原因值'
          type: string
          enum:
          - 'NULL'
          - OPERATOR_DETERMINED_BARRING
          - MISSING_OR_UNKNOWN_DNN
          - UNKNOWN_PDU_SESSION_TYPE
          - USER_AUTHENTICATION_OR_AUTHORIZATION_FAILED
          - REQUEST_REJECTED_UNSPECIFIED
          - SERVICE_OPTION_NOT_SUPPORTED
          - REQUESTED_SERVICE_OPTION_NOT_SUBSCRIBED
          - PTI_ALREADY_IN_USE
          - REGULAR_DEACTIVATION
          - FIVEGS_QOS_NOT_ACCEPTED
          - NETWORK_FAILURE
          - REACTIVATION_REQUESTED
          - SEMANTIC_ERROR_IN_THE_TFT_OPERATION
          - SYNTACTICAL_ERROR_IN_THE_TFT_OPERATION
          - INVALID_PDU_SESSION_IDENTITY
          - SEMANTIC_ERRORS_IN_PACKET_FILTERS
          - SYNTACTICAL_ERROR_IN_PACKET_FILTER
          - OUT_OF_LADN_SERVICE_AREA
          - PTI_MISMATCH
          - PDU_SESSION_TYPE_IPV4_ONLY_ALLOWED
          - PDU_SESSION_TYPE_IPV6_ONLY_ALLOWED
          - PDU_SESSION_TYPE_DOES_NOT_EXIST
          - PDU_SESSION_TYPE_IPV4V6_ONLY_ALLOWED
          - PDU_TYPE_UNSTRUCTURED_ONLY_ALLOWED
          - PDU_SESSION_TYPE_ETHERNET_ONLY_ALLOWED
          - INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN
          - INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE
          - MISSING_OR_UNKNOWN_DNN_IN_A_SLICE
          - INVALID_PTI_VALUE
          - MAX_DATA_RATE_FOR_UP_INTEGRITY_PROTECTION_TOO_LOW
          - SEMANTIC_ERROR_IN_THE_QOS_OPERATION
          - SYNTACTICAL_ERROR_IN_THE_QOS_OPERATION
          - INVALID_MAPPED_EPS_BEARER_IDENTITY
          - SEMANTICALLY_INCORRECT_MESSAGE
          - INVALID_MANDATORY_INFORMATION
          - MESSAGE_TYPE_NONEXIST_OR_NOT_IMPLEMENTED
          - MESSAGE_TYPE_NOT_COMPATIBLE_WITH_PROTOCOL_STATE
          - INFORMATION_ELEMENT_NONEXISTENT_OR_NOT_IMPLEMENTED
          - CONDITIONAL_IE_ERROR
          - MESSAGE_NOT_COMPATIBLE_WITH_THE_PROTOCOL_STATE
          - PROTOCOL_ERROR_UNSPECIFIED
          - UNSUPPORTED_5QI_VALUE
          - NOT_SUPPORTED_SSC_MODE
          - INSUFFICIENT_RESOURCES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSEFC:
          name: '发送消息流控导致流程拒绝的NAS原因值'
          type: string
          enum:
          - REQUESTREJ
          - USERAUTHFAILED
          - INSUFFRES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REQUESTREJ
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
        APPERROR:
          name: '应用层错误'
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
      CAUSEAPNLOCK: SRVNOTSUPPORTED
      CAUSEEMG: ''
      CAUSEFC: REQUESTREJ
    add_smcausemap_list:
    - CAUSEGRPID: 17
      CAUSERANGE: DEFAULT
      TCAUSE: 27
      BGCAUSE: 0
      EDCAUSE: 200
      APPERROR: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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
    {#- --- 条件可选：NFTYPE=INNER 时可选 --- -#}
    {%- if item.NFTYPE == 'INNER' -%}
        {%- if item.CAUSEAPNLOCK is not none -%}
            CAUSEAPNLOCK={{item.CAUSEAPNLOCK}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=INNER_EMG 时可选 --- -#}
    {%- if item.NFTYPE == 'INNER_EMG' -%}
        {%- if item.CAUSEEMG is not none -%}
            CAUSEEMG={{item.CAUSEEMG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=POLICY_PCF 时可选 --- -#}
    {%- if item.NFTYPE == 'POLICY_PCF' -%}
        {%- if item.CAUSEFC is not none -%}
            CAUSEFC={{item.CAUSEFC}},
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
    {#- --- 条件必选：CAUSERANGE=SPECIAL_APP_ERR 时必选 --- -#}
    {%- if item.CAUSERANGE == 'SPECIAL_APP_ERR' -%}
        APPERROR={{item.APPERROR}},
    {%- endif -%}
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

