---
id: GWFD-030501
name: 激活终端二次鉴权
ne_type: UEG
type: feature
description: UPF下沉，DN-AAA部署到企业或园区，SMF与DN-AAA之间不能直接互通，需要UPF转发SMF与DN-AAA之间二次鉴权的消息。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","安全管理功能","GWFD-030501 终端二次鉴权","激活终端二次鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPF下沉，DN-AAA部署到企业或园区，SMF与DN-AAA之间不能直接互通，需要UPF转发SMF与DN-AAA之间二次鉴权的消息。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读终端二次鉴权特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_networkinstvpnmap_list:
      type: items
      properties:
        NETWORKINSTANCE:
          name: '网络实例名称'
          type: string
          minLength: 0
          maxLength: 100
          required: true
          description: '网络实例标识。客户进行网络部署时自行规划，与SMF端规划的网络实例保持一致。  取值范围：字符串类型，输入长度范围为1～100，单位是字节。由“\_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '用于指定IPv4 VPN实例名。本特性中该参数取值是与DN-AAA共同规划的VPN实例名称。  取值范围：字符串类型，输入长度范围为1～31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '用于指定IPv6 VPN实例名。本特性中该参数取值是与DN-AAA共同规划的VPN实例名称。  取值范围：字符串类型，输入长度范围为1～31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_networkinstvpnmap_list:
    - NETWORKINSTANCE: 'net1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN2auto'
      HASVPNIPV6: DISABLE
      VPNINSTANCEIPV6: 'vnp1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口

### 2 添加网络实例。用于规划UPF与DN-AAA之间的VPN。

#### 2.1 //添加一个新的网络实例。

```jinja2
{%- for item in add_networkinstvpnmap_list -%}
    ADD NETWORKINSTVPNMAP:
    {#- --- 必选参数 --- -#}
    NETWORKINSTANCE="{{item.NETWORKINSTANCE}}",
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
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

