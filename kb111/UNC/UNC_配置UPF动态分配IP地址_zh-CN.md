---
id: ''
name: 配置UPF动态分配IP地址
ne_type: UNC
type: feature
description: 运营商规划UPF为UE分配IP地址，可基于APN/DNN、位置、SMF或其任意组合分配地址，在多DNN分流场景下，主要使用基于APN/DNN的IP地址分配。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UPF","配置UPF动态分配IP地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商规划UPF为UE分配IP地址，可基于APN/DNN、位置、SMF或其任意组合分配地址，在多DNN分流场景下，主要使用基于APN/DNN的IP地址分配。

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
          minLength: 1
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
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSEUDOACTSWITCH:
          name: '支持假激活用户开关'
          type: string
          enum:
          - ENABLE
          - INHERIT
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_pool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IPVERSION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPLEASE:
          name: 'IPLEASE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELEASETIME:
          name: 'RELEASETIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SINGLEIPFLAG:
          name: 'SINGLEIPFLAG'
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
          description: '如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN/DNN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ALARMSWITCH:
          name: 'ALARMSWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSSW:
          name: 'IMSSW'
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
          minLength: 1
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
          - IPv4
          - IPv6
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
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
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
          data_source: ''
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
    add_poolgroup_list:
      type: items
      properties:
        POOLGRPNAME:
          name: 'POOLGRPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCPRIALG:
          name: 'IPV6ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: 'POOLGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLNAME:
          name: 'POOLNAME'
          type: string
          required: false
          description: ''
          data_source: ''
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
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: 'MAPPINGNAME'
          type: string
          required: false
          description: ''
          data_source: ''
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
        POOLGROUPNAME:
          name: 'POOLGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnipallocrule_list:
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
        ALLOCATTR:
          name: 'ALLOCATTR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTRULESW:
          name: 'FIRSTRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTRULE:
          name: 'FIRSTRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'SECONDRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THIRDRULESW:
          name: 'THIRDRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCATTR:
          name: 'IPV6ALLOCATTR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULESW:
          name: 'IPV6FIRSTRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6FIRSTRULE:
          name: 'IPV6FIRSTRULE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6SECRULESW:
          name: 'IPV6SECRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6THIRDRULESW:
          name: 'IPV6THIRDRULESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_importroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPORTPROTOCOL:
          name: '路由协议'
          type: string
          enum:
          - direct
          - ospf
          - ospfv3
          - static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEDENABLE:
          name: '使能MED'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPORTPROCESSID:
          name: '路由进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MED:
          name: 'MED'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
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
    add_pool_list:
    - POOLNAME: pool_enterprise_ipv4
      POOLTYPE: LOCAL
      IPVERSION: IPV4
      IPLEASE: DISABLE
      RELEASETIME: '60'
      SINGLEIPFLAG: DISABLE
      HASVPN: ENABLE
      VPNINSTANCE: VRF_N6_Local_2B_APP
      ALARMSWITCH: ENABLE
      IMSSW: DISABLE
    add_section_list:
    - POOLNAME: 'pool_enterprise_ipv4'
      SECTIONNUM: 0
      IPVERSION: IPV4
      V4STARTIP: '10.1.1.0'
      V4ENDIP: '10.1.1.255'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    add_poolgroup_list:
    - POOLGRPNAME: pgrp_enterprise
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: pgrp_enterprise
      POOLNAME: pool_enterprise_ipv4
      PRIORITY: '10'
    add_poolgrpmap_list:
    - MAPPINGNAME: mapping_enterprise
      APN: stjwt.gd
      POOLGROUPNAME: pgrp_enterprise
    set_apnipallocrule_list:
    - APN: stjwt.gd
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
      IPV6ALLOCATTR: LOCAL
      IPV6FIRSTRULESW: ENABLE
      IPV6FIRSTRULE: APN-1&LOCATION-0&SMF-0
      IPV6SECRULESW: DISABLE
      IPV6THIRDRULESW: DISABLE
    add_importroute_list:
    - VRFNAME: 'VRF_N6_Local_2B_APP'
      AFTYPE: ipv4uni
      IMPORTPROTOCOL: wlr
      MEDENABLE: FALSE
      IMPORTPROCESSID: ''
      MED: ''
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

### 2 配置地址池和地址段。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pool_list的变量区（command: ADD POOL） -#}
<!-- MISSING_MACRO: command=ADD POOL list_name=add_pool_list step_id=2 -->
```

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4STARTIP="{{item.V4STARTIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        V4ENDIP="{{item.V4ENDIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXSTART="{{item.V6PREFIXSTART}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXEND="{{item.V6PREFIXEND}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置地址池组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgroup_list的变量区（command: ADD POOLGROUP） -#}
<!-- MISSING_MACRO: command=ADD POOLGROUP list_name=add_poolgroup_list step_id=3 -->
```

### 4 将地址池绑定到地址池组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolbindgroup_list的变量区（command: ADD POOLBINDGROUP） -#}
<!-- MISSING_MACRO: command=ADD POOLBINDGROUP list_name=add_poolbindgroup_list step_id=4 -->
```

### 5 配置APN与地址池组的映射关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=5 -->
```

### 6 配置地址分配规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnipallocrule_list的变量区（command: SET APNIPALLOCRULE） -#}
<!-- MISSING_MACRO: command=SET APNIPALLOCRULE list_name=set_apnipallocrule_list step_id=6 -->
```

### 7 （条件必选）当专网UPF通过VPN专线对接园区时，需要配置本步骤，引入wlr路由。

```jinja2
{%- if is_scenario_upf_vpn_campus -%}
    {%- for item in add_importroute_list -%}
        ADD IMPORTROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        IMPORTPROTOCOL={{item.IMPORTPROTOCOL}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {%- if item.MEDENABLE is not none -%}
            MEDENABLE={{item.MEDENABLE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IMPORTPROTOCOL=ospf/ospfv3 时必选 --- -#}
        {%- if item.IMPORTPROTOCOL in ['ospf', 'ospfv3'] -%}
            IMPORTPROCESSID={{item.IMPORTPROCESSID}},
        {%- endif -%}
        {#- --- 条件必选：MEDENABLE=TRUE 时必选 --- -#}
        {%- if item.MEDENABLE == 'TRUE' -%}
            MED={{item.MED}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

