---
id: ''
name: Fabric平面亚健康检测
ne_type: UDG
type: feature
description: Pod间Fabric平面亚健康检测是基于Pod间的点到点探测结果，进行的网络亚健康诊断。  操作员可以开启网络亚健康检查开关，并设置检查参数和相关告警上报参数，使系统根据设置参数检查网络亚健康状态并上报相关告警。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","Service Fabric特性（虚机）","Service Fabric可靠性","SFFD-010008 通信亚健康自愈","Fabric平面亚健康检测"]
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
    set_nodehealctrl_list:
      type: items
      properties:
        NPLINKFAULTSW:
          name: 'NP链路故障隔离控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置当由于NP与交换芯片间的多链路故障导致Fabric通信亚健康时，对其影响的Host进行隔离处理。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_fabricsubhealthy_list:
    - SUBHEALTHYINTERVAL: 30
      SUBHEALTHYTHRESHOLD: 50
      ISLINKSWITCHENABLE: TRUE
    set_nodehealctrl_list:
    - NPLINKFAULTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 已经登录OM Portal，或者已登录U2020，或者登录MAE并进入Access子系统。

### 2 使用**SET FABRICSUBHEALTHY**命令设置Fabric平面的Pod之间链路亚健康检测参数。

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

### Fabric平面亚健康可能会导致上报如下相关告警：

### **ALM-100339 Fabric链路出现亚健康**

### **ALM-100340 Fabric端口通信出现亚健康**

### 3 使用**SET NODEHEALCTRL**命令设置当由于NP与交换芯片间的多链路故障导致Fabric通信亚健康时，对其影响的Host进行隔离处理。对Host进行隔离处理后会上报**ALM-100384 Host Fabric平面故障**告警。

```jinja2
{%- for item in set_nodehealctrl_list -%}
    SET NODEHEALCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.NPLINKFAULTSW is not none -%}
        NPLINKFAULTSW={{item.NPLINKFAULTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

