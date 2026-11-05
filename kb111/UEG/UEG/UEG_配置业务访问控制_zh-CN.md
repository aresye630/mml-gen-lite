---
id: GWFD-030203
name: 配置业务访问控制
ne_type: UEG
type: feature
description: '**地市共享UPF组网**场景下，分流到本地DN的数据包和转发到Internet的数据包需要通过绑定不同VPN进行区分。  适用于UPF。'
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","本地分流功能","GWFD-030203 业务访问控制","配置业务访问控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**地市共享UPF组网**场景下，分流到本地DN的数据包和转发到Internet的数据包需要通过绑定不同VPN进行区分。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读业务访问控制特性概述。
* UEG完成与周边网元的对接。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_dnai_list:
      type: items
      properties:
        DNAI:
          name: '数据网络接入标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '在SMF上会配置UPF、UL CL属性和DNAI的映射关系，SMF通过N4接口下发给UL CL+辅锚点UPF，UPF上的DNAI需要与SMF上的DNAI配置保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当接入用户为IPv4单栈或IPv4v6双栈用户时，要绑定IPv4类型的VPN。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '配置DNAI和VPN的映射关系。VPN实例名称已通过**ADD VPNINST**命令配置。此VPN实例名不能与DNN（APN）下配置的VPN实例名相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当接入用户为IPv6单栈或IPv4v6双栈用户时，要绑定IPv6类型的VPN。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    add_dnai_list:
    - DNAI: 'test_dnai_01'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_Co'
      HASVPNIPV6: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 基于DNAI配置VPN。

#### 1.1 //配置DNAI与VPN的绑定关系。

```jinja2
{%- for item in add_dnai_list -%}
    ADD DNAI:
    {#- --- 必选参数 --- -#}
    DNAI="{{item.DNAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### UPF上的DNAI需要与SMF上的DNAI配置保持一致。

### SMF下发给UL CL+辅锚点UPF的DNAI必须配置VPN，并且跟用户激活所在DNN（APN）下绑定的VPN不同。如果SMF针对同一用户下发多个DNAI，则对这些DNAI需要配置相同的VPN。

