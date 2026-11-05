---
id: ''
name: 激活VoWIFI紧急呼叫
ne_type: UEG
type: feature
description: 在UEG上激活VoWiFi紧急呼叫功能，将紧急呼叫的用户接入WIFI网络。  目前UEG支持VoWiFi紧急呼叫功能，可以通过**ADD APN**的“EMERGENCYSWITCH”和“S6BEMERGCYSERVICE”参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是：在3GPP网络覆盖下，UE发起紧急呼叫时优先回落CS域进行处理。  适用于PGW-C。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoWIFI紧急呼叫"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上激活VoWiFi紧急呼叫功能，将紧急呼叫的用户接入WIFI网络。目前UEG支持VoWiFi紧急呼叫功能，可以通过**ADD APN**的“EMERGENCYSWITCH”和“S6BEMERGCYSERVICE”参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是：在3GPP网络覆盖下，UE发起紧急呼叫时优先回落CS域进行处理。适用于PGW-C。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 完成激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）。
* 完成加载License。
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMERGENCYSWITCH:
          name: '支持紧急呼叫'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        S6BEMERGCYSERVICE:
          name: 'S6b Emergency Service 标识'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
  examples:
    add_cpapn_list:
    - APN: 'sos'
      EMERGENCYSWITCH: ENABLE
      S6BEMERGCYSERVICE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置S/PGW-C数据

### 使能VoWiFi紧急呼叫功能。

### 在“MML命令行-UEG”窗口上执行命令

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.EMERGENCYSWITCH is not none -%}
        EMERGENCYSWITCH={{item.EMERGENCYSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：EMERGENCYSWITCH=ENABLE 时可选 --- -#}
    {%- if item.EMERGENCYSWITCH == 'ENABLE' -%}
        {%- if item.S6BEMERGCYSERVICE is not none -%}
            S6BEMERGCYSERVICE={{item.S6BEMERGCYSERVICE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。

### 2 配置MME数据

### 请参考激活LTE和WiFi网络之间的紧急呼叫切换

