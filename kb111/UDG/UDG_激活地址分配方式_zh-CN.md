---
id: GWFD-010104
name: 激活地址分配方式
ne_type: UDG
type: feature
description: 用户在激活过程中获取IP地址后可以进行数据业务。本章节以外部地址分配方式举例，用户面地址分配方式配置请参考基于APN/DNN分配地址。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010104 地址分配方式","激活地址分配方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户在激活过程中获取IP地址后可以进行数据业务。本章节以外部地址分配方式举例，用户面地址分配方式配置请参考基于APN/DNN分配地址。适用于PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-010104 地址分配方式。
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
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_poolgroup_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '-'
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
        ALARMSWITCH:
          name: '告警特性是否使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        IPLEASE:
          name: '地址租约使能标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RELEASETIME:
          name: '地址租期（秒）'
          type: integer
          minimum: 0
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        SINGLEIPFLAG:
          name: '小地址池标志'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
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
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLBINDGROUP**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '可以使用查询APN配置（LST APN）命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLBINDGROUP**命令进行查询。'
          data_source: '本端规划'
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
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
    add_pool_list:
    - POOLNAME: 'testpool'
      POOLTYPE: EXTERNAL
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
      ALARMSWITCH: DISABLE
      CHECKIPVALID: DISABLE
      IMSSW: ENABLE
      IPLEASE: DISABLE
      IPVERSION: IPV4
      REDUNDFUNC: DISABLE
      RELEASETIME: 10
      SINGLEIPFLAG: DISABLE
    add_section_list:
    - POOLNAME: 'testpool'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
      V6PREFIXEND: ''
      V6PREFIXLENGTH: ''
      V6PREFIXSTART: ''
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool'
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    set_apnaddressattr_list:
    - APN: 'apn-test'
      HOSTROUTEIP: ENABLE
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      APN: 'apn-test'
      POOLGROUPNAME: 'poolgroup1'
    add_l3vpninst_list:
    - VRFNAME: 'vpn1'
    add_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'vpn1'
      SCHEMAROUID: '10.10.10.1'
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

### 1 **可选：**配置白名单检测功能。

#### 1.1 配置VPN实例。

```jinja2
{%- if is_optional_whitelist_detection -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 配置地址池组。

```jinja2
{%- if is_optional_whitelist_detection -%}
    {%- for item in add_poolgroup_list -%}
        ADD POOLGROUP:
        {#- --- 必选参数 --- -#}
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置EXTERNAL类型地址池。

```jinja2
{%- if is_optional_whitelist_detection -%}
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
        {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'LOCAL' -%}
            {%- if item.ALARMSWITCH is not none -%}
                ALARMSWITCH={{item.ALARMSWITCH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.CHECKIPVALID is not none -%}
                CHECKIPVALID={{item.CHECKIPVALID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IMSSW is not none -%}
                IMSSW={{item.IMSSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'LOCAL' -%}
            {%- if item.IPLEASE is not none -%}
                IPLEASE={{item.IPLEASE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.REDUNDFUNC is not none -%}
                REDUNDFUNC={{item.REDUNDFUNC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'LOCAL' -%}
            {%- if item.RELEASETIME is not none -%}
                RELEASETIME={{item.RELEASETIME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'LOCAL' -%}
            {%- if item.SINGLEIPFLAG is not none -%}
                SINGLEIPFLAG={{item.SINGLEIPFLAG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果需要开启静态地址的白名单检测功能，需将该命令的“CHECKIPVALID”设置为“ENABLE”。

#### 1.4 配置地址池里的IPv4地址段。

```jinja2
{%- if is_optional_whitelist_detection -%}
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
{%- endif -%}
```

#### 1.5 将地址池绑定地址池组。

```jinja2
{%- if is_optional_whitelist_detection -%}
    {%- for item in add_poolbindgroup_list -%}
        ADD POOLBINDGROUP:
        {#- --- 必选参数 --- -#}
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        POOLNAME="{{item.POOLNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 配置APN名称。

```jinja2
{%- if is_optional_whitelist_detection -%}
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
{%- endif -%}
```

#### 1.7 配置指定APN下支持使用主机地址接入。

```jinja2
{%- if is_optional_whitelist_detection -%}
    {%- for item in set_apnaddressattr_list -%}
        SET APNADDRESSATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HOSTROUTEIP is not none -%}
            HOSTROUTEIP={{item.HOSTROUTEIP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.8 配置地址池组与APN的映射关系。

```jinja2
{%- if is_optional_whitelist_detection -%}
    {%- for item in add_poolgrpmap_list -%}
        ADD POOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APN is not none -%}
            APN="{{item.APN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置手机下行路由。

#### 2.1 配置VPN实例。

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

#### 2.2 启动OSPF进程。

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
    ;
{%- endfor -%}
```

#### 2.3 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 2.4 配置运行OSPF协议的接口。

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

#### 2.5 引入WLR路由。

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

