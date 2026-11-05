---
id: ''
name: 激活DHCPv6地址分配
ne_type: UEG
type: feature
description: DHCP属于网络层协议，它采用Client/Server模式。DHCP Server负责客户端IP地址的管理和分配，SMF作为Client端，代替UE向DHCP Server申请和租用IP地址。  适用于GGSN、SGW-C、PGW-C、SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC 用户IP地址管理（公共）","DHCPv6分配IP地址","激活DHCPv6分配IP地址功能","激活DHCPv6地址分配"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
DHCP属于网络层协议，它采用Client/Server模式。DHCP Server负责客户端IP地址的管理和分配，SMF作为Client端，代替UE向DHCP Server申请和租用IP地址。适用于GGSN、SGW-C、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读DHCPv6分配IP地址流程。
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
          description: '配置VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_addrpoolgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置DHCP地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_addrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名'
          type: string
          required: false
          description: '配置DHCP地址池。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          required: false
          description: ''
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolbindgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '已通过**ADD ADDRPOOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '地址池优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 16
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置地址池里的地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: 'Section序号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFGRPTYPE:
          name: 'UPF组类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Local
    add_upfbindgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置UPF和UPF组的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '配置APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          required: false
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_agentip_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 63
          - 65535
          required: false
          description: '配置DHCP地址池的地址段。'
          data_source: '本端规划'
          pattern: ''
          default: 65535
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6AGENTIP:
          name: 'IPv6代理地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_dhcpservergrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置DHCP服务器组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
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
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dhcpserver_list:
      type: items
      properties:
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置DHCP服务器。'
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
        ISPRIMARY:
          name: '是否是主DHCP服务器'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6IPADDRESS:
          name: 'DHCPv6服务器IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_dhcpserver_list_1:
      type: items
      properties:
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置DHCP服务器。'
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
        ISPRIMARY:
          name: '是否是主DHCP服务器'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6IPADDRESS:
          name: 'DHCPv6服务器IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_dhcpbindpoolgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置DHCP服务器组与地址池组绑定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCTYPE:
          name: 'IPV6分配方式'
          type: string
          required: false
          description: '配置地址分配属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6RADIUSPRIOR:
          name: 'IPV6优先使用AAA下发地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        IPV6FIRSTRULESW:
          name: 'IPv6第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置地址分配规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPv6第一级规则'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninst_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ospfv3_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: '须知：  Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfv3area_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: 'OSPFv3区域标识'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3importroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议号'
          type: string
          enum:
          - bgp
          - direct
          - ospfv3
          - static
          - wlr
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn6_dhcp'
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLGRPTYPE: DHCP
    add_addrpool_list:
    - POOLNAME: remotepool
      POOLTYPE: DHCP
      HASVPN: ENABLE
      VPNINSTANCE: vpn6_dhcp
      IPVERSION: IPV6
    add_poolbindgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLNAME: 'remotepool'
      PRIORITY: 15
    add_section_list:
    - POOLNAME: 'remotepool'
      SECTIONNUM: 2
      IPVERSION: IPv6
      V6PREFIXSTART: '2001:DB8:0001:0001:0:0:0:0'
      V6PREFIXEND: '2001:DB8:0001:0001:0:0:0:10'
      V6PREFIXLENGTH: 64
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgrp1'
      UPFGRPTYPE: DHCP
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgrp1'
      UPFID: 'upf_instance_1'
    add_apn_list:
    - APN: 'apn-test'
    add_poolgrpmap_list:
    - MAPPINGNAME: one
      POOLGRPNAME: poolgroup1
      APN: apn-test
      UPFGRPNAME: upfgrp1
    add_agentip_list:
    - POOLNAME: 'remotepool'
      SECTIONNUM: 0
      IPVERSION: IPV6
      V6AGENTIP: '2001:DB8:0001:0001:0:0:0:1'
    add_dhcpservergrp_list:
    - GROUPNAME: 'dv6grp'
      IPVERSION: IPV6
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn6_dhcp'
    add_dhcpserver_list:
    - GROUPNAME: 'dv6grp'
      ISPRIMARY: ENABLE
      IPVERSION: IPV6
      V6IPADDRESS: '2001:DB8:0002:0001:0:0:0:1'
    add_dhcpserver_list_1:
    - GROUPNAME: 'dv6grp'
      ISPRIMARY: DISABLE
      IPVERSION: IPV6
      V6IPADDRESS: '2001:DB8:0003:0001:0:0:0:1'
    add_dhcpbindpoolgrp_list:
    - POOLGRPNAME: 'poolgrp1'
      GROUPNAME: 'dv6grp'
    set_apnaddressattr_list:
    - APN: apn-test
      IPV6ALLOCTYPE: DHCP
      IPV6RADIUSPRIOR: ENABLE
    set_ipallocrule_list:
    - IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&UPNODE-1
    add_vpninst_list_1:
    - VPNINSTANCE: 'vpn6_dhcp'
    add_l3vpninst_list:
    - VRFNAME: 'vpn6_dhcp'
    add_vpninstaf_list:
    - VRFNAME: 'vpn6_dhcp'
      AFTYPE: ipv6uni
    add_ospfv3_list:
    - VRFNAME: 'vpn6_dhcp'
      PROCID: 1
      ROUTERID: '10.10.10.1'
    add_ospfv3area_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
    add_ospfnetwork_list:
    - PROCID: ''
      AREAID: ''
      IPADDRESS: ''
      WILDCARDMASK: ''
    add_ospfv3importroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: wlr
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在SMF上执行如下命令：

#### 1.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.2 配置DHCP地址池组。

```jinja2
{%- for item in add_addrpoolgrp_list -%}
    ADD ADDRPOOLGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLGRPTYPE is not none -%}
        POOLGRPTYPE={{item.POOLGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置DHCP地址池。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpool_list的变量区（command: ADD ADDRPOOL） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOL list_name=add_addrpool_list step_id=1.3 -->
```

#### 1.4 绑定地址池组和地址池。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 配置地址池里的IPv6地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 配置UPF组。

```jinja2
{%- for item in add_addrupgroup_list -%}
    ADD ADDRUPGROUP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPFGRPTYPE is not none -%}
        UPFGRPTYPE={{item.UPFGRPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 配置UPF和UPF组的绑定关系。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    ;
{%- endfor -%}
```

#### 1.8 配置APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 1.9 为该UPF组绑定本地地址池组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=1.9 -->
```

#### 1.10 配置DHCP地址池的IPv6地址段。

```jinja2
{%- for item in add_agentip_list -%}
    ADD AGENTIP:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECTIONNUM is not none -%}
        SECTIONNUM={{item.SECTIONNUM}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6AGENTIP="{{item.V6AGENTIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.11 配置DHCP服务器组。

```jinja2
{%- for item in add_dhcpservergrp_list -%}
    ADD DHCPSERVERGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.12 配置主用DHCP服务器的IP地址。

```jinja2
{%- for item in add_dhcpserver_list -%}
    ADD DHCPSERVER:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ISPRIMARY={{item.ISPRIMARY}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6IPADDRESS="{{item.V6IPADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.13 **可选：**配置备用DHCP服务器的IP地址。

```jinja2
{%- if is_optional_backup_dhcp_server_ip -%}
    {%- for item in add_dhcpserver_list_1 -%}
        ADD DHCPSERVER:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        ISPRIMARY={{item.ISPRIMARY}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6IPADDRESS="{{item.V6IPADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.14 配置DHCP服务器组与地址池绑定关系。

```jinja2
{%- for item in add_dhcpbindpoolgrp_list -%}
    ADD DHCPBINDPOOLGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

#### 1.15 配置IP地址分配方式为DHCP分配。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list step_id=1.15 -->
```

#### 1.16 配置地址分配规则。

```jinja2
{%- for item in set_ipallocrule_list -%}
    SET IPALLOCRULE:
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6FIRSTRULESW is not none -%}
        IPV6FIRSTRULESW={{item.IPV6FIRSTRULESW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPV6FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.IPV6FIRSTRULESW == 'ENABLE' -%}
        IPV6FIRSTRULE={{item.IPV6FIRSTRULE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 在UPF上执行如下命令：

#### 2.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list_1 -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 2.2 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

#### 2.3 启动OSPF进程。

```jinja2
{%- for item in add_ospfv3_list -%}
    ADD OSPFV3:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    ROUTERID="{{item.ROUTERID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 添加OSPF区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 2.5 配置运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    AREAID="{{item.AREAID}}",
    PROCID={{item.PROCID}},
    ;
{%- endfor -%}
```

#### 2.6 引入WLR路由。

```jinja2
{%- for item in add_ospfv3importroute_list -%}
    ADD OSPFV3IMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 采用路由策略方式发布路由时，不能只选择发布WLR\_SP或者WLR\_UD路由，必须选择WLR方式发布所有路由。

