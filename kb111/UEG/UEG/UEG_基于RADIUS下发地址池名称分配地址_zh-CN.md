---
id: GWFD-020805
name: 基于RADIUS下发地址池名称分配地址
ne_type: UEG
type: feature
description: RADIUS下发地址池名称给SMF，SMF将地址池名称发送给UPF，由UPF从指定地址池内为用户分配IP地址。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-020800 基本业务","GWFD-020805 用户面地址分配","激活用户面地址分配","基于RADIUS下发地址池名称分配地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
RADIUS下发地址池名称给SMF，SMF将地址池名称发送给UPF，由UPF从指定地址池内为用户分配IP地址。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020805 用户面地址分配特性概述。
* UEG本端已完成数据面逻辑接口（Sa/Sc/Pa）和N4/Sxa/Sxb逻辑接口的配置，配置过程可参考初始配置手册的配置业务接口数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: 'VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。'
          data_source: '全网规划'
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
          description: '设置指定VPN实例下的地址族。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upapn_list:
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
          description: '如下三者绑定的VPN实例必须一致。  * 地址池绑定的VPN实例 * 用户激活使用的APN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
          description: '已通过**ADD UPAPN**命令配置，可以使用**LST UPAPN**命令进行查询。'
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
        IGNOREV4POOLID:
          name: '忽略IPV4地址池名开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN支持SMF下发的地址池名字。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IGNOREV6POOLID:
          name: '忽略IPV6地址池名开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_addressattr_list:
      type: items
      properties:
        V4POOLWILDCARDSW:
          name: 'IPv4地址池通配功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于指定地址池名称是否使能通配功能的开关。控制在AAA未下发地址池通配符的情况下是否开启通配功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6POOLWILDCARDSW:
          name: 'IPv6地址池通配功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
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
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '如下三者绑定的VPN实例必须一致。  * 用户激活使用的APN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_conflictip_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESS:
          name: '冲突IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: '如果某IPv4地址已经分配给用户，此时通过该命令配置这一IPv4地址为冲突地址，命令依然可以执行成功，但是配置是在下次分配该地址的时候生效，即不再给用户分配该地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upapn_list_1:
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
          description: '如下三者绑定的VPN实例必须一致。  * 地址池绑定的VPN实例 * 用户激活使用的APN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
          description: '可以使用查询命令**LST UPAPN**进行查询。'
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
      properties: {}
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
        ALLOCATTR:
          name: 'IPv4分配属性'
          type: string
          enum:
          - INHERIT
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST L3VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: 'Schema路由器标识'
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
          name: 'OSPF进程号'
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
          name: 'OSPF进程号'
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
    add_l3vpninst_list:
    - VRFNAME: 'vpn1'
    add_vpninstaf_list:
    - VRFNAME: 'vpn1'
      AFTYPE: ipv4uni
      VRFRD: '100:1'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_upapn_list:
    - APN: 'apn-test1'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    set_apnaddressattr_list:
    - APN: 'apn-test1'
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      IGNOREV4POOLID: DISABLE
      IGNOREV6POOLID: DISABLE
    set_addressattr_list:
    - V4POOLWILDCARDSW: ENABLE
      V6POOLWILDCARDSW: ENABLE
    add_uppool_list:
    - POOLNAME: 'testpool1'
      POOLTYPE: LOCAL
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_section_list:
    - POOLNAME: 'testpool1'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.10'
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool1'
    add_conflictip_list:
    - POOLNAME: 'testpool1'
      IPADDRESS: '10.1.1.1'
    add_upapn_list_1:
    - APN: 'apn-test1'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      APN: 'apn-test1'
      POOLGROUPNAME: 'poolgroup1'
    set_ipallocrule_list:
    - {}
    set_apnipallocrule_list:
    - APN: 'apn-test1'
      ALLOCATTR: LOCAL
      FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
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

### 1 基于RADUIS下发地址池名称使能地址分配属性。

#### 1.1 创建L3VPN实例。

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
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
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

#### 1.3 配置APN/DNN实例。

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
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

#### 1.4 使能基于RADIUS下发的地址池名称分配地址功能。

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
    {%- if item.IGNOREV4POOLID is not none -%}
        IGNOREV4POOLID={{item.IGNOREV4POOLID}},
    {%- endif -%}
    {%- if item.IGNOREV6POOLID is not none -%}
        IGNOREV6POOLID={{item.IGNOREV6POOLID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_addressattr_list -%}
    SET ADDRESSATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.V4POOLWILDCARDSW is not none -%}
        V4POOLWILDCARDSW={{item.V4POOLWILDCARDSW}},
    {%- endif -%}
    {%- if item.V6POOLWILDCARDSW is not none -%}
        V6POOLWILDCARDSW={{item.V6POOLWILDCARDSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置地址池绑定到地址池组。

#### 2.1 配置LOCAL类型地址池。

```jinja2
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
        {%- if item.HASVPN is not none -%}
            HASVPN={{item.HASVPN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 配置本地地址池的时候，选择参数“LOCAL”类型。

#### 2.2 配置地址池里的地址段。

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

#### 2.3 配置地址池组。

```jinja2
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    ;
{%- endfor -%}
```

#### 2.4 配置地址池绑定到地址池组。

```jinja2
{%- for item in add_poolbindgroup_list -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

#### 2.5 （可选）配置本地地址池中的冲突IPv4地址，标识为冲突状态的IPv4地址不会分配给用户。

```jinja2
{%- if is_optional_local_pool_conflict_ipv4_address -%}
    {%- for item in add_conflictip_list -%}
        ADD CONFLICTIP:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        IPADDRESS="{{item.IPADDRESS}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置APN与地址池组的映射关系。

#### 3.1 配置APN/DNN实例信息。

```jinja2
{%- for item in add_upapn_list_1 -%}
    ADD UPAPN:
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

#### 3.2 配置APN/DNN实例与地址池组的映射关系。

```jinja2
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
```

### 4 配置地址分配规则。

### 地址分配规则支持两级控制：基于全局和基于APN。默认使用全局地址分配规则。如果配置了使用基于APN的地址分配规则，则使用APN的地址分配规则。

#### 4.1 配置全局地址分配规则。

```jinja2
SET IPALLOCRULE:
;
```

#### 4.2 如果某一APN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

```jinja2
{%- if is_scenario_apn_based_alloc_rule -%}
    {%- for item in set_apnipallocrule_list -%}
        SET APNIPALLOCRULE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ALLOCATTR is not none -%}
            ALLOCATTR={{item.ALLOCATTR}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.FIRSTRULESW == 'ENABLE' -%}
            FIRSTRULE={{item.FIRSTRULE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
        {%- if item.ALLOCATTR == 'LOCAL' -%}
            {%- if item.FIRSTRULESW is not none -%}
                FIRSTRULESW={{item.FIRSTRULESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
        {%- if item.ALLOCATTR == 'LOCAL' -%}
            {%- if item.SECONDRULESW is not none -%}
                SECONDRULESW={{item.SECONDRULESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ALLOCATTR=LOCAL 时可选 --- -#}
        {%- if item.ALLOCATTR == 'LOCAL' -%}
            {%- if item.THIRDRULESW is not none -%}
                THIRDRULESW={{item.THIRDRULESW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，此处设置的规则需要与地址池的映射条件一致。例如此处按照APN（APN-1&LOCATION-0&SMF-0）设置条件，则规划的地址池组需绑定APN。

### 5 配置手机下行路由。

#### 5.1 启动OSPF进程。

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

#### 5.2 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 5.3 配置运行OSPF协议的接口。

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

#### 5.4 引入WLR路由。

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

