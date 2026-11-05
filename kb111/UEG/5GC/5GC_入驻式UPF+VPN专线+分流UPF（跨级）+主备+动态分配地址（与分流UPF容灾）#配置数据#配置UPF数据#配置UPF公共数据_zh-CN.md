---
id: ''
name: 配置UPF公共数据
ne_type: UEG
type: feature
description: 本场景用于在分流UPF上配置DNN和APN相关的基础数据。容灾的两个UPF配置相同，仅一个UPF举例。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（跨级）+主备+动态分配地址（与分流UPF容灾）","配置数据","配置UPF数据","配置UPF公共数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（跨级）+主备+动态分配地址（与分流UPF容灾）","配置数据","配置UPF数据","配置UPF公共数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在分流UPF上配置DNN和APN相关的基础数据。容灾的两个UPF配置相同，仅一个UPF举例。

## 必备事项
前提条件

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
          description: '配置APN信息。  说明：  裸机容器模式下，容灾的两个UPF的VPN实例名称不能相同。'
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
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置辅锚点UPF的终端地址池，用于发布网段路由，地址段需要与主锚点UPF一致。  当存在多个主锚点时，辅锚点地址池是主锚点地址池并集。'
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
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_uppool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '配置辅锚点UPF的终端地址池，用于发布网段路由，地址段需要与主锚点UPF一致。  当存在多个主锚点时，辅锚点地址池是主锚点地址池并集。'
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
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: IPV4
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
          description: '配置本地地址池里的地址段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_colocatedlbo_list:
      type: items
      properties:
        ULCLSWITCH:
          name: 'ULCL功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启ULCL与PSA的共部署功能。'
          data_source: '固定取值'
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
        ROAMINGTYPE:
          name: '用户漫游类型'
          type: string
          required: true
          description: ''
          data_source: '全网规划'
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
    add_pool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_001'
    add_uppool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_001'
    add_section_list:
    - POOLNAME: 'pool_ipv4_APN1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.1.1.0'
      V4ENDIP: '10.1.1.225'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    set_colocatedlbo_list:
    - ULCLSWITCH: ENABLE
    add_tcpmss_list:
    - APN: 'APN1'
      ROAMINGTYPE: HOME-1&ROAMING-1&VISITING-1
      V4TCPMSSVALUE: 1380
      V6TCPMSSVALUE: 1300
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

### 3 配置地址池，用于发布网段路由，地址段需要与主锚点UPF一致。

#### 3.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
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
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_uppool_list -%}
        ADD UPPOOL:
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
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置本地地址池里的地址段。

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

### 5 配置ULCL功能开关。

```jinja2
{%- for item in set_colocatedlbo_list -%}
    SET COLOCATEDLBO:
    {#- --- 可选参数 --- -#}
    {%- if item.ULCLSWITCH is not none -%}
        ULCLSWITCH={{item.ULCLSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置添加Tcp Mss配置。

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

### 7 配置开启终端互访（可选）。

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

### 8 配置分流、计费、PCC等相关业务。

### 业务发放后，还需要配置计费、PCC等相关业务配置，请参考“风筝S/M/L（UEG）> 业务配置”章节。

