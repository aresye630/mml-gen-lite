---
id: ''
name: 激活DHCP地址分配
ne_type: UDG
type: feature
description: DHCP属于网络层协议，它采用Client/Server模式。DHCP Server负责客户端IP地址的管理和分配，SMF作为Client端，代替UE向DHCP Server申请和租用IP地址。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 用户IP地址管理解决方案","DHCP分配IP地址","激活DHCP分配IP地址功能","激活DHCP地址分配"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
DHCP属于网络层协议，它采用Client/Server模式。DHCP Server负责客户端IP地址的管理和分配，SMF作为Client端，代替UE向DHCP Server申请和租用IP地址。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读DHCP分配IP地址流程。
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
          required: false
          description: '配置DHCP地址池组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGRPTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
        IPVERSION:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
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
    add_poolbindgrp_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          required: false
          description: '已通过**ADD ADDRPOOLGRP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          required: false
          description: '已通过**ADD ADDRPOOL**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'PRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        V4STARTIP:
          name: 'IPv4起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
          type: string
          maxLength: 15
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
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置逻辑IP地址。此逻辑IP地址为DHCP代理IP，被**ADD AGENTIP**命令引用。  代理IP同DHCP地址池里的地址段属于同一网段，DHCP服务器从与该代理IP相同网段的地址池中为用户分配一个IP地址。  当地址池有多个网段时，代理IP也要配置多个。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 1500
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
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
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          required: false
          description: '配置UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFGRPTYPE:
          name: 'UPF组类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfbindgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          required: false
          description: '配置UPF和UPF组的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          required: false
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
          name: 'POOLNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: string
          required: false
          description: '配置DHCP地址池的代理IP。代理IP需要先通过**ADD LOGICIP**配置。'
          data_source: '本端规划'
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
        V4AGENTIP:
          name: 'IPv4代理地址'
          type: string
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
          required: false
          description: '配置DHCP服务器组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        REQLEASETIME:
          name: 'REQLEASETIME'
          type: string
          required: false
          description: ''
          data_source: ''
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dhcpserver_list:
      type: items
      properties:
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          required: false
          description: '配置DHCP服务器。'
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
        ISPRIMARY:
          name: '是否是主DHCP服务器'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
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
        V4IPADDRESS:
          name: 'DHCPv4服务器IP地址'
          type: string
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
          required: false
          description: '配置DHCP服务器。'
          data_source: '从已配数据中获取'
          pattern: ''
          default: ''
        ISPRIMARY:
          name: '是否是主DHCP服务器'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
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
        V4IPADDRESS:
          name: 'DHCPv4服务器IP地址'
          type: string
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
          required: false
          description: '配置DHCP服务器组与地址池组绑定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: 'DHCP服务器组名称'
          type: string
          required: false
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
        IPV4ALLOCTYPE:
          name: 'IPV4分配方式'
          type: string
          required: false
          description: '配置地址分配属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4RADIUSPRIOR:
          name: 'IPV4优先使用AAA下发地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        IPV4FIRSTRULESW:
          name: 'IPv4第一级规则开关'
          type: string
          required: false
          description: '配置地址分配规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4FIRSTRULE:
          name: 'IPv4第一级规则'
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
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: '须知：  Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
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
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9DHCP12'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'vpna'
    add_addrpoolgrp_list:
    - POOLGRPNAME: poolgroup1
      POOLGRPTYPE: DHCP
    add_addrpool_list:
    - POOLNAME: citya
      IPVERSION: IPV4
      POOLTYPE: DHCP
      HASVPN: ENABLE
      VPNINSTANCE: vpna
    add_poolbindgrp_list:
    - POOLGRPNAME: poolgroup1
      POOLNAME: citya
      PRIORITY: '15'
    add_section_list:
    - POOLNAME: 'citya'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.0.1.1'
      V4ENDIP: '10.0.1.10'
      V6PREFIXEND: ''
      V6PREFIXLENGTH: ''
      V6PREFIXSTART: ''
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.0.1.1'
      IPV4MTU: 1500
      VPNINSTNAME: 'vpna'
      DESC: 'dhcp agent ip'
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_addrupgroup_list:
    - UPFGRPNAME: upfgrp1
      UPFGRPTYPE: DHCP
    add_upfbindgrp_list:
    - UPFGRPNAME: upfgrp1
      UPFID: upf_instance_1
    add_apn_list:
    - APN: 'apn-test'
    add_poolgrpmap_list:
    - MAPPINGNAME: one
      POOLGRPNAME: poolgroup1
      APN: apn-test
      UPFGRPNAME: upfgrp1
    add_agentip_list:
    - POOLNAME: citya
      SECTIONNUM: '0'
      IPVERSION: IPV4
      V4AGENTIP: 10.0.1.1
    add_dhcpservergrp_list:
    - GROUPNAME: dgrp
      IPVERSION: IPV4
      REQLEASETIME: '25'
      HASVPN: ENABLE
      VPNINSTANCE: vpna
    add_dhcpserver_list:
    - GROUPNAME: dgrp
      ISPRIMARY: ENABLE
      IPVERSION: IPV4
      V4IPADDRESS: 10.1.4.51
    add_dhcpserver_list_1:
    - GROUPNAME: dgrp
      ISPRIMARY: DISABLE
      IPVERSION: IPV4
      V4IPADDRESS: 10.1.4.52
    add_dhcpbindpoolgrp_list:
    - POOLGRPNAME: spoolgrp1
      GROUPNAME: dgrp
    set_apnaddressattr_list:
    - APN: apn-test
      IPV4ALLOCTYPE: DHCP
      IPV4RADIUSPRIOR: ENABLE
    set_ipallocrule_list:
    - IPV4FIRSTRULESW: ENABLE
      IPV4FIRSTRULE: APN-1&UPNODE-1
    add_vpninst_list_1:
    - VPNINSTANCE: 'vpna'
    add_l3vpninst_list:
    - VRFNAME: 'vpna'
    add_vpninstaf_list:
    - VRFNAME: 'vpna'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'vpna'
      SCHEMAROUID: '10.10.10.1'
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      LSAARRINTVFLAG: FALSE
    add_ospfarea_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
    add_ospfnetwork_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
      IPADDRESS: '10.13.21.0'
      WILDCARDMASK: '0.0.0.255'
    add_ospfimportroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: wlr
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在SMF上执行如下命令：

#### 1.1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.2 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.3 配置DHCP地址池组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpoolgrp_list的变量区（command: ADD ADDRPOOLGRP） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOLGRP list_name=add_addrpoolgrp_list step_id=1.3 -->
```

#### 1.4 配置DHCP地址池。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpool_list的变量区（command: ADD ADDRPOOL） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOL list_name=add_addrpool_list step_id=1.4 -->
```

#### 1.5 绑定地址池组和地址池。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolbindgrp_list的变量区（command: ADD POOLBINDGRP） -#}
<!-- MISSING_MACRO: command=ADD POOLBINDGRP list_name=add_poolbindgrp_list step_id=1.5 -->
```

#### 1.6 配置地址池里的IPv4地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 配置逻辑IP地址。

#### 此逻辑IP地址为DHCP代理IP，被**ADD AGENTIP**命令引用。

#### 代理IP同DHCP地址池里的地址段属于同一网段，DHCP服务器从与该代理IP相同网段的地址池中为用户分配一个IP地址。

#### 当地址池有多个网段时，代理IP也要配置多个。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.8 配置UPF组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrupgroup_list的变量区（command: ADD ADDRUPGROUP） -#}
<!-- MISSING_MACRO: command=ADD ADDRUPGROUP list_name=add_addrupgroup_list step_id=1.8 -->
```

#### 1.9 配置UPF和UPF组的绑定关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upfbindgrp_list的变量区（command: ADD UPFBINDGRP） -#}
<!-- MISSING_MACRO: command=ADD UPFBINDGRP list_name=add_upfbindgrp_list step_id=1.9 -->
```

#### 1.10 配置APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 1.11 为该UPF组绑定本地地址池组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=1.11 -->
```

#### 1.12 配置DHCP地址池的代理IP。

#### 代理IP需要先通过**ADD LOGICIP**配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_agentip_list的变量区（command: ADD AGENTIP） -#}
<!-- MISSING_MACRO: command=ADD AGENTIP list_name=add_agentip_list step_id=1.12 -->
```

#### 1.13 配置DHCP服务器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dhcpservergrp_list的变量区（command: ADD DHCPSERVERGRP） -#}
<!-- MISSING_MACRO: command=ADD DHCPSERVERGRP list_name=add_dhcpservergrp_list step_id=1.13 -->
```

#### 1.14 配置主用DHCP服务器的IP地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dhcpserver_list的变量区（command: ADD DHCPSERVER） -#}
<!-- MISSING_MACRO: command=ADD DHCPSERVER list_name=add_dhcpserver_list step_id=1.14 -->
```

#### 1.15 **可选：**配置备用DHCP服务器的IP地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dhcpserver_list_1的变量区（command: ADD DHCPSERVER） -#}
<!-- MISSING_MACRO: command=ADD DHCPSERVER list_name=add_dhcpserver_list_1 step_id=1.15 -->
```

#### 1.16 配置DHCP服务器组与地址池组绑定关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dhcpbindpoolgrp_list的变量区（command: ADD DHCPBINDPOOLGRP） -#}
<!-- MISSING_MACRO: command=ADD DHCPBINDPOOLGRP list_name=add_dhcpbindpoolgrp_list step_id=1.16 -->
```

#### 1.17 配置IP地址分配方式为DHCP分配。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list step_id=1.17 -->
```

#### 1.18 配置地址分配规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ipallocrule_list的变量区（command: SET IPALLOCRULE） -#}
<!-- MISSING_MACRO: command=SET IPALLOCRULE list_name=set_ipallocrule_list step_id=1.18 -->
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
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
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
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

#### 2.6 引入WLR路由。

```jinja2
{%- for item in add_ospfimportroute_list -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
    {%- if item.PROTOCOL == 'BGP' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
    {%- if item.PROTOCOL == 'OSPF' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 采用路由策略方式发布路由时，不能只选择发布WLR\_SP或者WLR\_UD路由，必须选择WLR方式发布所有路由。

