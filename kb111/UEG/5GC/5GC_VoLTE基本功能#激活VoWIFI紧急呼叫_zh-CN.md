---
id: ''
name: 激活VoWIFI紧急呼叫
ne_type: UEG
type: feature
description: 在UEG上激活VoWiFi紧急呼叫功能，将紧急呼叫的用户接入WIFI网络。  目前UEG支持VoWiFi紧急呼叫功能，可以通过**ADD APN**的“EMERGENCYSWITCH”和“S6BEMERGCYSERVICE”参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是：在3GPP网络覆盖下，UE发起紧急呼叫时优先回落CS域进行处理。  适用于PGW-C。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoWIFI紧急呼叫"]
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

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 完成激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '规划使能紧急呼叫功能的APN实例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EMERGENCYSWITCH:
          name: '支持紧急呼叫'
          type: string
          required: false
          description: '是否使能VoWiFi紧急呼叫功能，默认值为“DISABLE”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        S6BEMERGCYSERVICE:
          name: 'S6b Emergency Service 标识'
          type: string
          required: false
          description: '该参数仅在EMERGENCYSWITCH开启才能生效'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: sos
      EMERGENCYSWITCH: ENABLE
      S6BEMERGCYSERVICE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置S/PGW-C数据

### 使能VoWiFi紧急呼叫功能。

### 在“MML命令行-UEG”窗口上执行命令

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apn_list的变量区（command: ADD APN） -#}
<!-- MISSING_MACRO: command=ADD APN list_name=add_apn_list step_id=1 -->
```

### 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。

### 2 配置MME数据

### 请参考激活LTE和WiFi网络之间的紧急呼叫切换

