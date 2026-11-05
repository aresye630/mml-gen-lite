---
id: ''
name: 激活基于DNN插入I-UPF
ne_type: UNC
type: feature
description: 本操作指导介绍激活基于DNN插入I-UPF特性的操作过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","MEC解决方案","WSFD-223006 基于DNN插入I-UPF","激活基于DNN插入I-UPF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍激活基于DNN插入I-UPF特性的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-223006 基于DNN插入I-UPF特性概述。
* 以下配置过程是基于SMF和园区所在地UPF的对接配置已完成情况下的操作。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_iupfapndpmode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加I-UPF在特定园区专用APN下的部署模式配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NGDEPLOYMODE:
          name: '5G下的I-UPF部署模式'
          type: string
          enum:
          - ALLOWIUPF
          - NOIUPF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ALLOWIUPF
        NGFAILNASCAUSE:
          name: '5G禁止I-UPF插入时返回的失败NAS原因值'
          type: string
          enum:
          - INSUFFICIENT_RESOURCES
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
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN
    add_iupfapndpmode_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加I-UPF在特定园区专用APN下的部署模式配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NGDEPLOYMODE:
          name: '5G下的I-UPF部署模式'
          type: string
          enum:
          - ALLOWIUPF
          - NOIUPF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ALLOWIUPF
  examples:
    add_iupfapndpmode_list:
    - APN: 'special1.com'
      NGDEPLOYMODE: NOIUPF
      NGFAILNASCAUSE: INSUFFICIENT_RESOURCES_FOR_SPECIFIC_SLICE_AND_DNN
    add_iupfapndpmode_list_1:
    - APN: 'special2.com'
      NGDEPLOYMODE: ALLOWIUPF
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 增加APN1的I-UPF部署模式配置为NOIUPF。

#### 2.1 //APN special1.com下，禁止插入I-UPF，并且在会话创建失败或修改失败的响应消息中，携带的NAS拒绝原因值为“特定切片和DNN的资源不足”。

```jinja2
{%- for item in add_iupfapndpmode_list -%}
    ADD IUPFAPNDPMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NGDEPLOYMODE is not none -%}
        NGDEPLOYMODE={{item.NGDEPLOYMODE}},
    {%- endif -%}
    {%- if item.NGFAILNASCAUSE is not none -%}
        NGFAILNASCAUSE={{item.NGFAILNASCAUSE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加APN2的I-UPF部署模式配置为ALLOWIUPF。

#### 3.1 //APN special1.com下，允许插入I-UPF。

```jinja2
{%- for item in add_iupfapndpmode_list_1 -%}
    ADD IUPFAPNDPMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NGDEPLOYMODE is not none -%}
        NGDEPLOYMODE={{item.NGDEPLOYMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

