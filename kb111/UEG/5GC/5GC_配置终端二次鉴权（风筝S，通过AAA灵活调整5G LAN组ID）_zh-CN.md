---
id: ''
name: 配置终端二次鉴权（风筝S，通过AAA灵活调整5G LAN组ID）
ne_type: UEG
type: feature
description: 基于AAA服务器实现5G LAN组ID的灵活调整时，依赖二次鉴权流程。  如图1所示，SMF与AAA不能直接互通，需经由UPF中转二次鉴权消息的场景，需要配置本页面。  **图1** 非直连方式组网示意
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UEG特性指南","可选功能","本地调整5G LAN组ID","配置终端二次鉴权（风筝S，通过AAA灵活调整5G LAN组ID）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
基于AAA服务器实现5G LAN组ID的灵活调整时，依赖二次鉴权流程。如图1所示，SMF与AAA不能直接互通，需经由UPF中转二次鉴权消息的场景，需要配置本页面。**图1** 非直连方式组网示意

## 必备事项
前提条件

* 二次鉴权消息经由UPF中转时，还需申请并加载License控制项“LKV3G5SAFT01 终端二次鉴权”。
* 已完成N6外联口及路由配置，UPF通过该N6外联口与AAA互通。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_networkinstvpnmap_list:
      type: items
      properties:
        NETWORKINSTANCE:
          name: '网络实例名称'
          type: string
          minLength: 0
          maxLength: 100
          required: true
          description: 'SMF上与AAA互通的Gi接口绑定的VPN实例。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '固定取值。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'UPF上与AAA互通的N6接口绑定的VPN实例。'
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
    add_conflictip_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: 'AAA服务器IP与UPF上某个IP地址池中的IP地址冲突时需要配置。  配置后，该IP不会再分配给用户。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESS:
          name: '冲突IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5SAFT01'
      SWITCH: ENABLE
    add_networkinstvpnmap_list:
    - NETWORKINSTANCE: 'VRF_AAA'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_LocalDN'
      HASVPNIPV6: DISABLE
    add_conflictip_list:
    - POOLNAME: 'ippool01'
      IPADDRESS: '10.168.10.1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //开启终端二次鉴权的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //配置网络实例数据。

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
    ;
{%- endfor -%}
```

### 3 //配置冲突IP数据。

```jinja2
{%- for item in add_conflictip_list -%}
    ADD CONFLICTIP:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    IPADDRESS="{{item.IPADDRESS}}",
    ;
{%- endfor -%}
```

