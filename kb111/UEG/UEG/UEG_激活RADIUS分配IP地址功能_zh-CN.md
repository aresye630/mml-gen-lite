---
id: ''
name: 激活RADIUS分配IP地址功能
ne_type: UEG
type: feature
description: 可以在本地配置静态IP地址网段与UPF的绑定关系，当用户接入网络时，对静态IP地址用户、Radius分配IP地址用户可以基于配置的网段绑定关系为用户选择指定的UPF。  适用于GGSN、PGW-C、SMF、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC 用户IP地址管理（公共）","RADIUS分配IP地址","激活RADIUS分配IP地址功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
可以在本地配置静态IP地址网段与UPF的绑定关系，当用户接入网络时，对静态IP地址用户、Radius分配IP地址用户可以基于配置的网段绑定关系为用户选择指定的UPF。适用于GGSN、PGW-C、SMF、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读RADIUS分配IP地址流程。
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
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
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
          description: 'APN/DNN实例应该全网规划，UPF配置的APN/DNN实例应该与SMF配置的APN/DNN实例一致。'
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
          description: '如下三者绑定的VPN实例必须一致。   * 地址池绑定的VPN实例 * 用户激活使用的APN/DNN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
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
          description: '已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
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
          description: '配置指定APN/DNN是否支持IPV4地址。'
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
          description: '配置指定APN下是否支持CP使用主机地址接入。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: LOCAL
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_addrpool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名'
          type: string
          required: false
          description: '为采用静态地址分配方式的用户配置对应的地址池。'
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
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_section_list_1:
      type: items
      properties:
        POOLNAME:
          name: 'Pool名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置UDM类型地址池里的地址段。'
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
          name: 'IPV4开始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPV4结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置地址池组。'
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
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置静态地址用户使用的UPF。  已通过**ADD PNFPROFILE**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    add_addrupgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '配置静态地址用户使用的UPF组。'
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
          description: '-'
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
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFID:
          name: 'UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过**ADD UPNODE**配置。'
          data_source: '已配置数据中获取'
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
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          required: false
          description: '已通过**ADD ADDRUPGROUP**配置。'
          data_source: '已配置数据中获取'
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
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_apn_list:
    - APN: 'apn-test2'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    set_apnaddressattr_list:
    - APN: 'apn-test2'
      SUPPORTIPV4: ENABLE
      HOSTROUTEIP: ENABLE
    add_pool_list:
    - POOLNAME: 'pool01'
      POOLTYPE: EXTERNAL
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_section_list:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
    add_addrpool_list:
    - POOLNAME: pool01
      IPVERSION: IPv4
      POOLTYPE: Radius
      CHECKIPVALID: Enable
    add_poolbindapn_list:
    - APN: 'huawei.com'
      POOLNAME: 'pool01'
    add_section_list_1:
    - POOLNAME: 'pool01'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLGRPTYPE: Radius
    add_poolbindgrp_list:
    - POOLGRPNAME: 'poolgroup1'
      POOLNAME: 'pool01'
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_1'
      ADDRALLOCMODE: INHERIT
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFGRPTYPE: Radius
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFID: 'UPF_Instance_1'
    add_poolgrpmap_list:
    - MAPPINGNAME: mapping01
      POOLGRPNAME: poolgroup1
      UPFGRPNAME: upfgroup1
    add_l3vpninst_list:
    - VRFNAME: 'vpn1'
    add_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'vpn1'
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
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在UPF上执行如下命令：

#### 1.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.2 配置APN/DNN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
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

#### 1.3 使能该APN/DNN的地址分配属性。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPPORTIPV4 is not none -%}
        SUPPORTIPV4={{item.SUPPORTIPV4}},
    {%- endif -%}
    {%- if item.HOSTROUTEIP is not none -%}
        HOSTROUTEIP={{item.HOSTROUTEIP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置EXTERNAL类型地址池。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POOLTYPE is not none -%}
        POOLTYPE={{item.POOLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
    {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 配置地址池里的IPv4地址段。

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
    ;
{%- endfor -%}
```

#### 如需配置主机路由，请联系华为技术支持。

### 2 在SMF上执行如下命令：

#### 2.1 创建本地静态地址地址池。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpool_list的变量区（command: ADD ADDRPOOL） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOL list_name=add_addrpool_list step_id=2.1 -->
```

#### 2.2 如果需要开启静态地址用户的白名单检查功能，需要配置地址池与APN/DNN的绑定关系。接入该APN的静态地址用户激活时，根据用户地址查找对应的地址池，然后根据地址池为用户选择对应的UPF。

```jinja2
{%- for item in add_poolbindapn_list -%}
    ADD POOLBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

#### 2.3 配置本地地址池里的地址段。

```jinja2
{%- for item in add_section_list_1 -%}
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
    ;
{%- endfor -%}
```

#### 本地地址池：本地负责分配地址的地址池。本地地址池下需要配置地址段，一个本地地址池最多可以配置64个地址段。

#### 配置地址池后，必须配置地址段。如果不配置地址段，将导致用户激活失败。

#### 2.4 配置地址池组名称。

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

#### 2.5 配置地址池与地址池组绑定。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

#### 2.6 配置静态地址用户使用的UPF。

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 配置静态地址用户使用的UPF组。

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

#### 2.8 配置UPF与UPF组绑定。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    ;
{%- endfor -%}
```

#### 2.9 配置地址池组与UPF组绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=2.9 -->
```

### 3 在UPF上执行如下命令：

#### 3.1 配置VPN实例。

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

#### 3.2 启动OSPF进程。

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

#### 3.3 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 3.4 配置运行OSPF协议的接口。

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

#### 3.5 引入WLR路由。

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
    ;
{%- endfor -%}
```

#### 采用路由策略方式发布路由时，不能只选择发布WLR\_SP或者WLR\_UD路由，必须选择WLR方式发布所有路由。

