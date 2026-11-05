---
id: ''
name: 配置专用DNN基本数据
ne_type: UDG
type: feature
description: 用户访问归属地园区业务时，数据会通过智能分流UPF转发至园区的专网UPF，从而使用户可以访问园区业务。本章节主要介绍在园区专网UPF上配置专用DNN的基本数据。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UPF","配置专用DNN基本数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户访问归属地园区业务时，数据会通过智能分流UPF转发至园区的专网UPF，从而使用户可以访问园区业务。本章节主要介绍在园区专网UPF上配置专用DNN的基本数据。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数用于指定APN实例名。'
          data_source: '本端规划。'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于指定是否给APN实例绑定IPv4 VPN。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该参数用于指定IPv4 VPN实例名。'
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
          description: '该参数用于指定是否给APN实例绑定IPv6 VPN。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该参数用于指定IPv6 VPN实例名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '该参数是用来配置APN是否支持假激活用户的开关。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    set_apnsglpass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数用于指定APN实例名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: '用户数据流量单通故障检测功能的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '指定APN实例名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '表明是否支持IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来配置指定APN是否允许手机后路由用户接入。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来配置指定APN的下行数据是否支持防欺诈功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来配置指定APN的上行数据是否支持防欺诈功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: '为双栈用户返回的地址类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: false
          description: '指定APN在用户请求IPv4v6双栈地址时，给用户分配双栈地址还是只分配IPv4地址或者只分配IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '指定当用户请求IPv4v6双栈地址，给用户只分配IPv4地址或者只分配IPv6地址时，激活响应消息中携带的原因值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPCTRL:
          name: '基于CP分配IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数在“IPTYPEFORDUALIP”配置为“IPV4V6”时为可选参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'RA携带MTU选项开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于配置IPv6的RA消息中是否支持携带MTU选项。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期(秒)'
          type: integer
          minimum: 3600
          maximum: 65535
          required: false
          description: '该参数用于配置IPv6 RA消息路由生命周期。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于配置指定APN下是否支持SMF/PGW-C使用UE IP地址激活PDU会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tcpmss_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数用于表示APN的名字。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMINGTYPE:
          name: '用户漫游类型'
          type: string
          required: true
          description: '该参数用于配置用户归属的属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'IPv4 TCP报文长度'
          type: integer
          minimum: 496
          maximum: 1500
          required: false
          description: '该参数用于表示对端能接收的最大报文段长度，用于IPv4用户。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6TCPMSSVALUE:
          name: 'IPv6 TCP报文长度'
          type: integer
          minimum: 496
          maximum: 1500
          required: false
          description: '该参数用于表示对端能接收的最大报文段长度， 用于IPv6用户。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnaffunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数用于表示APN的名字。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISENABLE:
          name: '防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '该参数用于指定APN防欺诈功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_apn_list:
    - APN: 'stjwt.gd'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_APP'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'VRF_N6_Local_2B_APP'
      PSEUDOACTSWITCH: INHERIT
    set_apnsglpass_list:
    - APN: 'stjwt.gd'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list:
    - APN: 'stjwt.gd'
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      FRAMEDROUTE: DISABLE
      ANTISPOOFINGDL: ENABLE
      ANTISPOOFINGUL: ENABLE
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: 1
      CPCTRL: DISABLE
      IPV6RAMTUSW: DISABLE
      IPV6RALIFETIME: 65535
      HOSTROUTEIP: ENABLE
      IPV6MTU: ''
    add_tcpmss_list:
    - APN: 'stjwt.gd'
      ROAMINGTYPE: HOME-1&ROAMING-1&VISITING-1
      V4TCPMSSVALUE: 1380
      V6TCPMSSVALUE: 1300
    set_apnaffunc_list:
    - APN: 'stjwt.gd'
      ISENABLE: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置VPN和DNN，如已完成VPN和专用DNN创建，请跳过本步骤。该VPN实例与专网UPF的N6接口VPN实例保持一致。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.PSEUDOACTSWITCH is not none -%}
        PSEUDOACTSWITCH={{item.PSEUDOACTSWITCH}},
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

### 2 设置APN单通检测开关。如果检测到用户数据流量发生单通故障，会触发设备内环回探测，开启用户数据跟踪，可以跟踪到探测报文。

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 对APN地址分配属性进行配置。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPPORTIPV4 is not none -%}
        SUPPORTIPV4={{item.SUPPORTIPV4}},
    {%- endif -%}
    {%- if item.SUPPORTIPV6 is not none -%}
        SUPPORTIPV6={{item.SUPPORTIPV6}},
    {%- endif -%}
    {%- if item.FRAMEDROUTE is not none -%}
        FRAMEDROUTE={{item.FRAMEDROUTE}},
    {%- endif -%}
    {%- if item.ANTISPOOFINGDL is not none -%}
        ANTISPOOFINGDL={{item.ANTISPOOFINGDL}},
    {%- endif -%}
    {%- if item.ANTISPOOFINGUL is not none -%}
        ANTISPOOFINGUL={{item.ANTISPOOFINGUL}},
    {%- endif -%}
    {%- if item.IPTYPEFORDUALIP is not none -%}
        IPTYPEFORDUALIP={{item.IPTYPEFORDUALIP}},
    {%- endif -%}
    {%- if item.SINGLEADDRCAUSE is not none -%}
        SINGLEADDRCAUSE={{item.SINGLEADDRCAUSE}},
    {%- endif -%}
    {%- if item.IPV6RAMTUSW is not none -%}
        IPV6RAMTUSW={{item.IPV6RAMTUSW}},
    {%- endif -%}
    {%- if item.IPV6RALIFETIME is not none -%}
        IPV6RALIFETIME={{item.IPV6RALIFETIME}},
    {%- endif -%}
    {%- if item.HOSTROUTEIP is not none -%}
        HOSTROUTEIP={{item.HOSTROUTEIP}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPEFORDUALIP=IPV4V6 时可选 --- -#}
    {%- if item.IPTYPEFORDUALIP == 'IPV4V6' -%}
        {%- if item.CPCTRL is not none -%}
            CPCTRL={{item.CPCTRL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPV6RAMTUSW=ENABLE 时可选 --- -#}
    {%- if item.IPV6RAMTUSW == 'ENABLE' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 开启APN的TCP MSS调整功能并配置TCP MSS的值。

```jinja2
{%- for item in add_tcpmss_list -%}
    ADD TCPMSS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ROAMINGTYPE={{item.ROAMINGTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.V4TCPMSSVALUE is not none -%}
        V4TCPMSSVALUE={{item.V4TCPMSSVALUE}},
    {%- endif -%}
    {%- if item.V6TCPMSSVALUE is not none -%}
        V6TCPMSSVALUE={{item.V6TCPMSSVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 开启计费防欺诈。

```jinja2
{%- for item in set_apnaffunc_list -%}
    SET APNAFFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ISENABLE={{item.ISENABLE}},
    ;
{%- endfor -%}
```

