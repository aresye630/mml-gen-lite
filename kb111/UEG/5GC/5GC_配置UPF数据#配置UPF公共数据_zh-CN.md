---
id: ''
name: 配置UPF公共数据
ne_type: UEG
type: feature
description: 当终端是静态地址签约，且是主机路由方式下，用于在UPF上配置DNN和APN相关的基础数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（同级）+负荷分担+静态签约地址（主机路由）","配置数据","配置UPF数据","配置UPF公共数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（同级）+负荷分担+静态签约地址（主机路由）","配置数据","配置UPF数据","配置UPF公共数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当终端是静态地址签约，且是主机路由方式下，用于在UPF上配置DNN和APN相关的基础数据。

## 必备事项
前提条件

无
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '配置APN信息。'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
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
          description: ''
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
          description: '配置APN单通检测。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
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
          description: '配置APN地址分配属性。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
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
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: '分配单栈地址时返回的原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
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
          description: ''
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPv6 RA消息路由生命周期'
          type: integer
          minimum: 3600
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTROUTEIP:
          name: '主机地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置添加Tcp Mss配置。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'IPv4 TCP报文长度'
          type: integer
          minimum: 496
          maximum: 1500
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6TCPMSSVALUE:
          name: 'IPv6 TCP报文长度'
          type: integer
          minimum: 496
          maximum: 1500
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMINGTYPE:
          name: '用户漫游类型'
          type: string
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnuemutacc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置开启终端互访。如果需要开启终端互访则使用本命令。参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INNERAPNS:
          name: '同APN内的控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERAPNS:
          name: '不同APN间的控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_001'
    add_apn_list:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_001'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'VRF_N6_Local_2B_001'
      PSEUDOACTSWITCH: INHERIT
    set_apnsglpass_list:
    - APN: 'APN1'
      SWITCH: PF_ACT_ENABLE
    set_apnaddressattr_list:
    - APN: 'APN1'
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
    add_tcpmss_list:
    - APN: 'APN1'
      V4TCPMSSVALUE: 1380
      V6TCPMSSVALUE: 1300
      ROAMINGTYPE: HOME-1&ROAMING-1&VISITING-1
    set_apnuemutacc_list:
    - APN: 'APN1'
      INNERAPNS: DISABLE
      INTERAPNS: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置APN信息。

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

### 2 配置APN单通检测。

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置APN地址分配属性。

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
    ;
{%- endfor -%}
```

### 4 配置添加Tcp Mss配置。

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

### 5 配置开启终端互访（可选）。

```jinja2
{%- if is_optional_enable_terminal_interaccess -%}
    {%- for item in set_apnuemutacc_list -%}
        SET APNUEMUTACC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        INNERAPNS={{item.INNERAPNS}},
        INTERAPNS={{item.INTERAPNS}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置计费、PCC等相关业务。

### 业务发放后，还需要配置计费、PCC等相关业务配置，请参考“风筝S/M/L（UEG）> 业务配置”章节。

