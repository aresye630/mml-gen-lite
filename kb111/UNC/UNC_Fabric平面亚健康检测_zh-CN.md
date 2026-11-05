---
id: ''
name: Fabric平面亚健康检测
ne_type: UNC
type: feature
description: Pod间Fabric平面亚健康检测是基于Pod间的点到点探测结果，进行的网络亚健康诊断。  操作员可以开启网络亚健康检查开关，并设置检查参数和相关告警上报参数，使系统根据设置参数检查网络亚健康状态并上报相关告警。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","Service Fabric特性","Service Fabric可靠性","SFFD-010008 通信亚健康自愈","Fabric平面亚健康检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
Pod间Fabric平面亚健康检测是基于Pod间的点到点探测结果，进行的网络亚健康诊断。操作员可以开启网络亚健康检查开关，并设置检查参数和相关告警上报参数，使系统根据设置参数检查网络亚健康状态并上报相关告警。

## 必备事项
前提条件

请仔细阅读SFFD-010008 通信亚健康自愈。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_fabricsubhealthy_list:
      type: items
      properties:
        SUBHEALTHYINTERVAL:
          name: '亚健康探测周期（s）'
          type: integer
          minimum: 10
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBHEALTHYTHRESHOLD:
          name: '亚健康阈值'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: '设置Fabric平面的亚健康检测参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISLINKSWITCHENABLE:
          name: 'Fabric链路切换是否使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_fabricsubhealthy_list:
    - SUBHEALTHYINTERVAL: 30
      SUBHEALTHYTHRESHOLD: 50
      ISLINKSWITCHENABLE: TRUE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 已经登录OM Portal，或者已登录U2020，或者登录MAE并进入Access子系统。

### 2 使用**SET FABRICSUBHEALTHY**命令设置Fabric平面的Pod之间链路亚健康检测参数。

### Fabric平面亚健康可能会导致上报如下相关告警：

### **ALM-100339 Fabric链路出现亚健康**

### **ALM-100340 Fabric端口通信出现亚健康**

#### 2.1 //设置Fabric亚健康全局配置，包括亚健康阈值和亚健康检测周期。

```jinja2
{%- for item in set_fabricsubhealthy_list -%}
    SET FABRICSUBHEALTHY:
    {#- --- 可选参数 --- -#}
    {%- if item.SUBHEALTHYINTERVAL is not none -%}
        SUBHEALTHYINTERVAL={{item.SUBHEALTHYINTERVAL}},
    {%- endif -%}
    {%- if item.SUBHEALTHYTHRESHOLD is not none -%}
        SUBHEALTHYTHRESHOLD={{item.SUBHEALTHYTHRESHOLD}},
    {%- endif -%}
    {%- if item.ISLINKSWITCHENABLE is not none -%}
        ISLINKSWITCHENABLE={{item.ISLINKSWITCHENABLE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

