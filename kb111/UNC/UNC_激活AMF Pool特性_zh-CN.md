---
id: ''
name: 激活AMF Pool特性
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活AMF Pool特性的操作过程。  AMF Pool是指多个AMF同时为相同的无线区域服务，Pool内的AMF与相应区域内所有gNodeB连接。Pool内AMF之间实现资源共享、业务负荷分担。gNodeB探测AMF的设备状态（是否可用）并获取AMF的负荷权重，根据设备状态及负荷权重来及时调整Pool的负荷均衡策略。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-104301 AMF Pool","激活AMF Pool特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活AMF Pool特性的操作过程。AMF Pool是指多个AMF同时为相同的无线区域服务，Pool内的AMF与相应区域内所有gNodeB连接。Pool内AMF之间实现资源共享、业务负荷分担。gNodeB探测AMF的设备状态（是否可用）并获取AMF的负荷权重，根据设备状态及负荷权重来及时调整Pool的负荷均衡策略。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-104301 AMF Pool特性概述。
* 在“初始配置 > 配置AMF”的时候，完成AMF全局标识配置，且Pool内所有AMF的“PLMNIDX”、“AMFREGIONID”和“AMFSETID”取值相同。
* 完成加载License。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2AMFPL01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

