---
id: GWFD-022906
name: 基于SMF分配地址
ne_type: UEG
type: feature
description: 运营商规划用户面网元（UPF/PGW-U）基于SMF为UE分配IP地址时，可激活本特性。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IPv6功能","GWFD-022906 IPv6 Prefix Delegation","激活本地地址池分配的IPv6 Prefix Delegation功能","基于SMF分配地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商规划用户面网元（UPF/PGW-U）基于SMF为UE分配IP地址时，可激活本特性。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-022906 IPv6 Prefix Delegation。
* UEG本端已完成数据面逻辑接口（Sa/Sc/Pa）和N4/Sxa/Sxb逻辑接口的配置，配置过程可参考初始配置手册的配置业务数据。
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
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处绑定的VPN实例与业务APN绑定的VPN实例一致。'
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
          description: 'APN/DNN实例应该全网规划，UEG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。'
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
          description: '如下三者绑定的VPN实例必须一致。   * 地址池绑定的VPN实例 * 用户激活使用的APN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
          description: '规划使能Routing Behind MS功能的APN实例，已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
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
          description: '配置指定APN是否支持IPV4地址。'
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
          description: '配置指定APN是否支持IPV6地址。'
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
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
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
          description: '前缀长度范围为49~64，当前缀长度小于64时，则表示该地址池采用IPv6 Prefix Delegation方式分配。'
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
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv4地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv6地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLGROUP**命令进行查询。'
          data_source: '已配置数据中获取'
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
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: '地址池组下绑定多个地址池时，支持按地址池优先级分配地址。只有同类地址池之间才有优先级比较，不同类型的地址池间（IPv4和IPv6）没有优先级比较。'
          data_source: '本端规划'
          pattern: ''
          default: 16
    add_conflictipv6_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        V6PREFIX:
          name: '冲突IPv6地址前缀'
          type: string
          maxLength: 39
          required: true
          description: '如果地址池中某一个IPv6地址+前缀长度已经使用，不可用于用户地址分配，则需要配置该冲突IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXLENGTH:
          name: 'IPv6前缀长度'
          type: integer
          minimum: 49
          maximum: 64
          required: false
          description: '该参数必须与地址池的前缀长度一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: 64
    add_cpnodeid_list:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4NODEID:
          name: 'IPv4地址类型的Node Id'
          type: string
          maxLength: 15
          required: false
          description: '不同SMF实例的SMF NodeID不可以相同。该参数要与对端SMF上的配置取值一致。'
          data_source: '对端获取'
          pattern: ''
          default: ''
        IPV6NODEID:
          name: 'IPv6地址类型的Node Id'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        FQDNNODEID:
          name: 'FQDN类型的Node Id'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '对端获取'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
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
        SMF:
          name: 'SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '可以使用查询命令**LST CPNODEID**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLGROUP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        FIRSTRULESW:
          name: '第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第一规则优先级默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: '第一级规则'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: '第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第二规则优先级默认不使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: '第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第三规则优先级默认不使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnipallocrule_list:
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
    set_ipallocbysmfglbsw_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocbysmfsw_list:
      type: items
      properties:
        SMF:
          name: 'SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfv3_list:
      type: items
      properties:
        PROCID:
          name: 'OSPFv3进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN的名称'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        ROUTERID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: true
          description: '须知：  Router ID必须全网唯一。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: 'VNF支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPFv3路由引入失败。'
          data_source: '固定取值'
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。'
          data_source: '全网规划'
          pattern: ''
          default: TRUE
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
    add_ospfv3interface_list:
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
          name: 'OSPFv3区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: '根据手机下行路由的外联口规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DRPRI:
          name: '指定路由器优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。'
          data_source: '-'
          pattern: ''
          default: 1
        VIRTUALSYSFLAG:
          name: 'OSPFv3共网段虚拟系统使能标志'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。'
          data_source: '-'
          pattern: ''
          default: FALSE
        CFGROUTERIDFLAG:
          name: 'OSPFv3虚拟路由器标识使能标识'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
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
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5P6PD01'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_apn_list:
    - APN: 'apn-test2'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    set_apnaddressattr_list:
    - APN: 'apn-test2'
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
    add_pool_list:
    - POOLNAME: 'testpool3'
      POOLTYPE: LOCAL
      IPVERSION: IPV6
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_section_list:
    - POOLNAME: 'testpool3'
      SECTIONNUM: 1
      IPVERSION: IPV6
      V6PREFIXSTART: 'fc00:0000:0000:fcee:0000:0000:0000:0000'
      V6PREFIXEND: 'fc00:0000:0000:fcef:ffff:ffff:ffff:ffff'
      V6PREFIXLENGTH: 63
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup3'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup3'
      POOLNAME: 'testpool3'
      PRIORITY: 10
    add_conflictipv6_list:
    - POOLNAME: 'testpool3'
      V6PREFIX: 'fc00:0000:0000:fcee:0000:0000:0000:0001'
      V6PREFIXLENGTH: 63
    add_cpnodeid_list:
    - CPNAME: 'smfnode1'
      IPV4NODEID: '10.0.0.1'
      IPV6NODEID: 'FC00:1111:1001:0001:0100:1100:0000:0001'
      FQDNNODEID: 'consumer.huawei.com'
      CPNODEIDTYPE: ''
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping3'
      SMF: 'smfnode1'
      POOLGROUPNAME: 'poolgroup3'
    set_ipallocrule_list:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-0&LOCATION-0&SMF-1
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
    set_apnipallocrule_list:
    - APN: ''
    set_ipallocbysmfglbsw_list:
    - SWITCH: ENABLE
    set_ipallocbysmfsw_list:
    - SMF: ''
    add_ospfv3_list:
    - PROCID: 6
      VRFNAME: 'vpn1'
      ROUTERID: '10.8.25.1'
      BFDALLINTFFLG: TRUE
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
    add_ospfv3area_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
    add_ospfv3interface_list:
    - PROCID: 6
      AREAID: '0.0.0.5'
      IFNAME: 'Eth-trunk1.1'
      DRPRI: 0
      VIRTUALSYSFLAG: TRUE
      CFGROUTERIDFLAG: FALSE
    add_ospfv3importroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 基于APN/DNN实例使能地址分配属性。

#### 2.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 2.2 配置APN/DNN实例。

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

#### 2.3 使能该APN的地址分配属性。

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
    ;
{%- endfor -%}
```

### 3 配置地址池绑定到地址池组。

#### 3.1 配置LOCAL类型地址池。

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
```

#### 配置本地地址池的时候，选择参数“LOCAL”类型。

#### 3.2 配置地址池里的地址段。

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

#### 3.3 配置地址池组。

```jinja2
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ALLOCPRIALG is not none -%}
        IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
    {%- endif -%}
    {%- if item.IPV6ALLOCPRIALG is not none -%}
        IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 配置地址池绑定到地址池组。

```jinja2
{%- for item in add_poolbindgroup_list -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 （可选）配置本地地址池中的冲突IPv6地址，标识为冲突状态的IPv6地址不会分配给用户。

```jinja2
{%- if is_optional_local_pool_conflict_ipv6_address -%}
    {%- for item in add_conflictipv6_list -%}
        ADD CONFLICTIPV6:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        V6PREFIX="{{item.V6PREFIX}}",
        {#- --- 可选参数 --- -#}
        {%- if item.V6PREFIXLENGTH is not none -%}
            V6PREFIXLENGTH={{item.V6PREFIXLENGTH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置SMF与地址池组的映射关系。

#### 4.1 配置SMF实例信息。

```jinja2
{%- for item in add_cpnodeid_list -%}
    ADD CPNODEID:
    {#- --- 必选参数 --- -#}
    CPNAME="{{item.CPNAME}}",
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CPNODEIDTYPE=IPV4 时可选 --- -#}
    {%- if item.CPNODEIDTYPE == 'IPV4' -%}
        {%- if item.IPV4NODEID is not none -%}
            IPV4NODEID="{{item.IPV4NODEID}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CPNODEIDTYPE=IPV6 时可选 --- -#}
    {%- if item.CPNODEIDTYPE == 'IPV6' -%}
        {%- if item.IPV6NODEID is not none -%}
            IPV6NODEID="{{item.IPV6NODEID}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CPNODEIDTYPE=FQDN 时可选 --- -#}
    {%- if item.CPNODEIDTYPE == 'FQDN' -%}
        {%- if item.FQDNNODEID is not none -%}
            FQDNNODEID="{{item.FQDNNODEID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置SMF实例与地址池组的映射关系。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SMF is not none -%}
        SMF="{{item.SMF}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置地址分配规则。

### 地址分配规则支持两级控制：基于全局和基于APN。默认使用全局地址分配规则。如果配置了使用基于APN的地址分配规则，则使用APN的地址分配规则。

#### 5.1 配置全局地址分配规则。

```jinja2
{%- for item in set_ipallocrule_list -%}
    SET IPALLOCRULE:
    {#- --- 可选参数 --- -#}
    {%- if item.FIRSTRULESW is not none -%}
        FIRSTRULESW={{item.FIRSTRULESW}},
    {%- endif -%}
    {%- if item.SECONDRULESW is not none -%}
        SECONDRULESW={{item.SECONDRULESW}},
    {%- endif -%}
    {%- if item.THIRDRULESW is not none -%}
        THIRDRULESW={{item.THIRDRULESW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
    {%- if item.FIRSTRULESW == 'ENABLE' -%}
        FIRSTRULE={{item.FIRSTRULE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，此处设置的规则需要与地址池的映射条件一致。例如此处按照SMF+APN（APN-1&LOCATION-0&SMF-1）设置条件，则规划的地址池组需绑定SMF&APN。

#### 5.2 （可选）如果某一APN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

```jinja2
{%- if is_optional_apn_alloc_rule_priority -%}
    {%- for item in set_apnipallocrule_list -%}
        SET APNIPALLOCRULE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置基于SMF分配地址的开关。

### 基于SMF分配地址的开关支持两级控制：基于全局和指定SMF。

#### 6.1 配置基于SMF分配地址的全局开关。

```jinja2
{%- for item in set_ipallocbysmfglbsw_list -%}
    SET IPALLOCBYSMFGLBSW:
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 （可选）如果某一指定SMF的地址分配开关不同于全局SMF地址分配开关的使能状态，则需执行配置基于指定SMF分配地址的开关。

```jinja2
{%- if is_optional_smf_alloc_switch -%}
    {%- for item in set_ipallocbysmfsw_list -%}
        SET IPALLOCBYSMFSW:
        {#- --- 必选参数 --- -#}
        SMF="{{item.SMF}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置手机下行路由。

#### 7.1 创建OSPFv3进程。

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
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 增加OSPFv3区域。

```jinja2
{%- for item in add_ospfv3area_list -%}
    ADD OSPFV3AREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 7.3 配置运行OSPFv3协议的接口。

```jinja2
{%- for item in add_ospfv3interface_list -%}
    ADD OSPFV3INTERFACE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IFNAME="{{item.IFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DRPRI is not none -%}
        DRPRI={{item.DRPRI}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VIRTUALSYSFLAG=TRUE 时可选 --- -#}
    {%- if item.VIRTUALSYSFLAG == 'TRUE' -%}
        {%- if item.CFGROUTERIDFLAG is not none -%}
            CFGROUTERIDFLAG={{item.CFGROUTERIDFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.4 设置OSPFv3引入路由类型。

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

