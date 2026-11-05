---
id: ''
name: 配置SMF业务数据
ne_type: UEG
type: feature
description: 本场景用于在SMF上配置DNN和APN相关的基础数据和静态路由冗余数据。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（跨级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置SMF数据","配置SMF业务数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（跨级）+主备+静态签约地址（GRE冗余备份）","配置数据","配置SMF数据","配置SMF业务数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本场景用于在SMF上配置DNN和APN相关的基础数据和静态路由冗余数据。

## 必备事项
前提条件

需要与UPF配合使用，要求SMF上配置的用户静态地址网段信息必须在包含在UPF上配置的地址池内，如果对端UPF是华为UEG产品，详细请参考**静态地址用户路由冗余**特性。
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
          description: '增加VPN实例名。'
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
          description: '增加APN信息。'
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpvpninst_list:
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
    add_cpapn_list:
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
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '* 增加DNN切片绑定关系。 * 参数“NSIDX”由命令**LST NFNS**查询结果中的“网络切片索引”获取。当存在切片发放场景时，此参数引用切片发放对应的参数。 * 参数“DNN”已在**ADD APN**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'PCC功能基于现网业务规划，参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '配置服务区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务区名称支持的5GTAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5GTAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置SMF本端主锚点UPF所覆盖的区域。 * 参数“NFINSTANCEID”已在**ADD UPNODE**中定义。 * 参数“SMFSERVINGAREA”已在**ADD UPAREABINDN2TAI**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '配置将UserProfile Group绑定到APN。参数“APN”已在**ADD APN**中定义，参数“USERPROFGNAME”已在PCC业务配置的**ADD USRPROFGROUP**命令中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置主锚点UPF的DNN属性。 * 参数“NFINSTANCEID”已在**ADD UPNODE**中定义。 * 参数“DNN”已在**ADD APN**中定义。 * 参数“PNFNSINDEX”已在**ADD PNFNS**中定义，当存在切片发放场景时，此参数引用切片发放对应的参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: 0
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHECKIPVALID:
          name: '白名单检查开关'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpaddrpool_list:
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
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Local
        CHECKIPVALID:
          name: '白名单检查开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolbindapn_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '开启静态地址用户的白名单检查功能，需要配置地址池与APN的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
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
          data_source: '本端规划'
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
          name: 'IPv4开始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
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
    add_cpsection_list:
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
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4STARTIP:
          name: 'IPv4起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
          type: string
          maxLength: 15
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
          name: '地址池组类型'
          type: string
          enum:
          - Local
          - UDM
          - Radius
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
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
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 255
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
    add_cppoolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'UPF组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_apn_list:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_cpvpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_cpapn_list:
    - APN: 'APN1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'APN1'
    set_apnpccfunc_list:
    - APN: 'APN1'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    add_uparea_list:
    - AREANAME: 'huzhou_12A303'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'huzhou_12A303'
      N2BEGINTAI: '4600312A301'
      N2ENDTAI: '4600312A303'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'huzhou_12A303'
    add_apnusrprofg_list:
    - APN: 'APN1'
      USERPROFGNAME: 'up_group_iot5g'
    add_pnfdnn_list:
    - INDEX: 100
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'APN1'
      PNFNSINDEX: 3
    add_addrpool_list:
    - POOLNAME: pool_ipv4_APN1
      IPVERSION: IPv4
      POOLTYPE: UDM
      CHECKIPVALID: Enable
      HASVPN: ENABLE
      VPNINSTANCE: VRF_N6_Local_2B_APP
    add_cpaddrpool_list:
    - POOLNAME: 'pool_ipv4_APN1'
      IPVERSION: IPv4
      POOLTYPE: UDM
      CHECKIPVALID: Enable
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_poolbindapn_list:
    - POOLNAME: 'pool_ipv4_APN1'
      APN: 'APN1'
    add_section_list:
    - POOLNAME: 'pool_ipv4_APN1'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.0.0.0'
      V4ENDIP: '10.1.2.3'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    add_cpsection_list:
    - POOLNAME: 'pool_ipv4_APN1'
      SECTIONNUM: 1
      IPVERSION: IPv4
      V4STARTIP: '10.0.0.0'
      V4ENDIP: '10.1.2.3'
      V6PREFIXSTART: 'fc00:1::1'
      V6PREFIXEND: 'fc00:1::1111'
      V6PREFIXLENGTH: 64
    add_addrpoolgrp_list:
    - POOLGRPNAME: 'pool_APN1'
      POOLGRPTYPE: UDM
    add_poolbindgrp_list:
    - POOLGRPNAME: 'pool_APN1'
      POOLNAME: 'pool_ipv4_APN1'
    add_addrupgroup_list:
    - UPFGRPNAME: 'upfgroupp1'
      UPFGRPTYPE: UDM
    add_upfbindgrp_list:
    - UPFGRPNAME: 'upfgroup1'
      UPFID: 'UPF_Instance_0'
      PRIORITY: 0
    add_poolgrpmap_list:
    - MAPPINGNAME: mapping01
      POOLGRPNAME: pool_APN1
      UPFGRPNAME: upfgroup1
    add_cppoolgrpmap_list:
    - MAPPINGNAME: 'mapping01'
      POOLGRPNAME: 'pool_APN1'
      UPFGRPNAME: 'upfgroup1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置APN信息。

#### 1.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_s -%}
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

#### 1.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_cpvpninst_list -%}
        ADD CPVPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
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

### 2 配置DNN切片绑定关系。

#### 2.1 /*需要使用命令LST NFNS查询SMF支持的网络切片索引。*/

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 3 配置指定APN的本地用户、漫游用户、拜访地用户动态PCC功能。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 （可选）配置服务区域。如果当前业务发放不涉及区域调整则无需随DNN开通时重复配置。

```jinja2
{%- if is_optional_service_area -%}
    {%- for item in add_uparea_list -%}
        ADD UPAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_service_area -%}
    {%- for item in add_upareabindn2tai_list -%}
        ADD UPAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （可选）配置SMF本端主锚点UPF所覆盖的区域。如果当前业务发放不涉及区域调整则无需随DNN开通时重复配置。

```jinja2
{%- if is_optional_smf_primary_anchor_upf_area -%}
    {%- for item in add_pnfsmfserarea_list -%}
        ADD PNFSMFSERAREA:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置将UserProfile Group绑定到APN。参数“USERPROFGNAME”已在PCC业务配置的**ADD USRPROFGROUP**命令中定义。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

### 7 （可选）配置主锚点UPF的DNN属性。如果新增业务场景需要新增DNN可通过本命令添加。参数“PNFNSINDEX”已在**ADD PNFNS**中定义，当存在切片发放场景时，此参数引用切片发放对应的参数。

```jinja2
{%- if is_optional_primary_anchor_upf_dnn -%}
    {%- for item in add_pnfdnn_list -%}
        ADD PNFDNN:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        DNN="{{item.DNN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PNFNSINDEX is not none -%}
            PNFNSINDEX={{item.PNFNSINDEX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 创建本地地址池。

#### 8.1 //风筝S

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_addrpool_list的变量区（command: ADD ADDRPOOL） -#}
<!-- MISSING_MACRO: command=ADD ADDRPOOL list_name=add_addrpool_list step_id=8.1 -->
```

#### 8.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_cpaddrpool_list -%}
        ADD CPADDRPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPVERSION is not none -%}
            IPVERSION={{item.IPVERSION}},
        {%- endif -%}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=Enable 时必选 --- -#}
        {%- if item.HASVPN == 'Enable' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POOLTYPE=UDM/Radius 时可选 --- -#}
        {%- if item.POOLTYPE in ['UDM', 'Radius'] -%}
            {%- if item.CHECKIPVALID is not none -%}
                CHECKIPVALID={{item.CHECKIPVALID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 开启静态地址用户的白名单检查功能。

```jinja2
{%- for item in add_poolbindapn_list -%}
    ADD POOLBINDAPN:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 10 配置本地地址池里的地址段。

#### 10.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
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
{%- endif -%}
```

#### 10.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_cpsection_list -%}
        ADD CPSECTION:
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
{%- endif -%}
```

### 11 配置地址池组名称。

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

### 12 配置地址池与地址池组绑定。

```jinja2
{%- for item in add_poolbindgrp_list -%}
    ADD POOLBINDGRP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

### 13 配置静态地址用户使用的UPF组。

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

### 14 配置主、备UPF与UPF组绑定。

```jinja2
{%- for item in add_upfbindgrp_list -%}
    ADD UPFBINDGRP:
    {#- --- 必选参数 --- -#}
    UPFGRPNAME="{{item.UPFGRPNAME}}",
    UPFID="{{item.UPFID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 15 配置地址池组与UPF组绑定。

#### 15.1 //风筝S

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_poolgrpmap_list的变量区（command: ADD POOLGRPMAP） -#}
<!-- MISSING_MACRO: command=ADD POOLGRPMAP list_name=add_poolgrpmap_list step_id=15.1 -->
```

#### 15.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in add_cppoolgrpmap_list -%}
        ADD CPPOOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.UPFGRPNAME is not none -%}
            UPFGRPNAME="{{item.UPFGRPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 16 配置计费、PCC相关业务。

### 业务发放后，还需要配置计费、PCC等相关业务配置，请参考“风筝S/M/L（UEG）> 业务配置”章节。

