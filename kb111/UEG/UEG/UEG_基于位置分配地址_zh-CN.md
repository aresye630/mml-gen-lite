---
id: GWFD-023101
name: 基于位置分配地址
ne_type: UEG
type: feature
description: 运营商规划UEG基于位置区为UE分配IP地址时，可激活本特性。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-023100 组网能力增强","GWFD-023101 基于位置的地址分配","激活基于位置的地址分配","基于位置分配地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商规划UEG基于位置区为UE分配IP地址时，可激活本特性。适用于PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-023101 基于位置的地址分配。
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
          description: '如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_tacgroup_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定S1TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'S1Tac 段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'S1Tac 起始ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACENDID:
          name: 'S1TAC截止ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_n2tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定N2TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'N2Tac 段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'N2Tac 起始ID'
          type: string
          minLength: 0
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACENDID:
          name: 'N2TAC截止ID'
          type: string
          minLength: 0
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_lacgroup_list:
      type: items
      properties:
        LACGROUPNAME:
          name: '指定LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_lacid_list:
      type: items
      properties:
        LACGROUPNAME:
          name: '指定LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACSECNUM:
          name: 'LAC 段编号'
          type: integer
          minimum: 0
          maximum: 23999
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LACSTARTID:
          name: 'LAC起始ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LACENDID:
          name: 'LAC截止ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
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
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          required: false
          description: '可以使用查询命令**LST LACGROUP**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
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
          name: 'IPv4第一级规则开关'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: 'IPv4第二级规则开关'
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
          name: 'IPv4第三级规则开关'
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
    set_ipallocbylocglbsw_list:
      type: items
      properties:
        SWITCH:
          name: 'IPv4 开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置IPv4地址使能基于位置区分配，IPv6地址不使能基于位置区分配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipallocbylocsw_list:
      type: items
      properties:
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
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
          description: '可以使用**LST VPNINST**命令进行查询。'
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
    add_adrlocwhitelst_list:
      type: items
      properties:
        MSISDN:
          name: 'MSISDN号'
          type: string
          minLength: 0
          maxLength: 15
          required: true
          description: '位于白名单中的用户不基于位置区分配IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LBAA01'
      SWITCH: ENABLE
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
    add_uppool_list:
    - POOLNAME: 'testpool1'
      POOLTYPE: LOCAL
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_section_list:
    - POOLNAME: 'testpool1'
      SECTIONNUM: 0
      IPVERSION: IPV4
      V6PREFIXSTART: '10.10.1.11'
      V6PREFIXEND: '10.10.1.20'
      V4STARTIP: '10.10.1.11'
      V4ENDIP: '10.10.1.20'
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool1'
    add_tacgroup_list:
    - TACGROUPNAME: ''
    add_s1tacid_list:
    - TACGROUPNAME: ''
      TACSECNUM: ''
      TACSTARTID: ''
      TACENDID: ''
    add_n2tacid_list:
    - TACGROUPNAME: ''
      TACSECNUM: ''
      TACSTARTID: ''
      TACENDID: ''
    add_lacgroup_list:
    - LACGROUPNAME: 'lac1'
    add_lacid_list:
    - LACGROUPNAME: 'lac1'
      LACSECNUM: 2
      LACSTARTID: '0x000a'
      LACENDID: '0x000b'
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      LOCATIONGRPTYPE: LAC
      LOCATIONGRPNAME: 'lac1'
      POOLGROUPNAME: 'poolgroup1'
    set_ipallocrule_list:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-0&LOCATION-1&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
    set_apnipallocrule_list:
    - APN: ''
    set_ipallocbylocglbsw_list:
    - SWITCH: ENABLE
    set_ipallocbylocsw_list:
    - LOCATIONGRPTYPE: ''
      LOCATIONGRPNAME: ''
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
    add_adrlocwhitelst_list:
    - MSISDN: '123456'
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

#### UEG本地分配双栈地址时，需要在本地分别规划配置IPv4类型和IPv6类型的POOL。

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

#### 3.3 配置地址池组。

```jinja2
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
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
    ;
{%- endfor -%}
```

### 4 （可选）基于TAC位置区分配地址的时候需要配置本步骤。配置TAC位置区组。

#### 4.1 配置TAC位置区组。

```jinja2
{%- if is_optional_tac_location_group -%}
    {%- for item in add_tacgroup_list -%}
        ADD TACGROUP:
        {#- --- 必选参数 --- -#}
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 （可选）在S1TAC组内绑定S1TAC号段。

```jinja2
{%- if is_optional_tac_location_group and is_optional_bind_s1tac_segment -%}
    {%- for item in add_s1tacid_list -%}
        ADD S1TACID:
        {#- --- 必选参数 --- -#}
        TACSECNUM={{item.TACSECNUM}},
        TACENDID="{{item.TACENDID}}",
        TACSTARTID="{{item.TACSTARTID}}",
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 （可选）在N2TAC组内绑定N2TAC号段。

```jinja2
{%- if is_optional_tac_location_group and is_optional_bind_n2tac_segment -%}
    {%- for item in add_n2tacid_list -%}
        ADD N2TACID:
        {#- --- 必选参数 --- -#}
        TACSECNUM={{item.TACSECNUM}},
        TACENDID="{{item.TACENDID}}",
        TACSTARTID="{{item.TACSTARTID}}",
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （可选）基于LAC位置区分配地址的时候需要配置本步骤。配置LAC位置区组。

#### 5.1 配置LAC位置区组。

```jinja2
{%- if is_optional_lac_location_group -%}
    {%- for item in add_lacgroup_list -%}
        ADD LACGROUP:
        {#- --- 必选参数 --- -#}
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 **可选：**在LAC组内添加一个LAC。

```jinja2
{%- if is_optional_lac_location_group and is_optional_add_lac -%}
    {%- for item in add_lacid_list -%}
        ADD LACID:
        {#- --- 必选参数 --- -#}
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        LACSECNUM={{item.LACSECNUM}},
        LACSTARTID="{{item.LACSTARTID}}",
        LACENDID="{{item.LACENDID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置TAC-Group/LAC-Group与地址池组的映射关系。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATIONGRPTYPE is not none -%}
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOCATIONGRPTYPE=TAC/LAC 时必选 --- -#}
    {%- if item.LOCATIONGRPTYPE in ['TAC', 'LAC'] -%}
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置地址分配规则。

### 地址分配规则支持两级控制：基于全局和基于APN。默认使用全局地址分配规则。如果配置了使用基于APN的地址分配规则，则使用APN的地址分配规则。

#### 7.1 配置全局地址分配规则。

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

#### 每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，此处设置的规则需要与地址池的映射条件一致。例如此处按照位置区（APN-0&LOCATION-1&SMF-0）设置条件，则规划的地址池组也需绑定LOC。

#### 7.2 （可选）如果某一APN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

```jinja2
{%- if is_optional_apn_ipalloc_rule -%}
    {%- for item in set_apnipallocrule_list -%}
        SET APNIPALLOCRULE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 配置基于位置区分配地址的开关。

### 基于位置区分配地址的开关支持两级控制：基于全局和指定位置区。

#### 8.1 配置基于位置区分配地址的全局开关。

```jinja2
{%- for item in set_ipallocbylocglbsw_list -%}
    SET IPALLOCBYLOCGLBSW:
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 （可选）如果某一指定位置区的地址分配开关不同于全局位置区地址分配开关，则需执行配置基于指定位置区分配地址的开关。

```jinja2
{%- if is_optional_location_ipalloc_switch -%}
    {%- for item in set_ipallocbylocsw_list -%}
        SET IPALLOCBYLOCSW:
        {#- --- 必选参数 --- -#}
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 配置手机下行路由。

#### 9.1 启动OSPF进程。

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

#### 9.2 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 9.3 配置运行OSPF协议的接口。

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

#### 9.4 引入WLR路由。

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

### 10 配置基于位置区分配IP地址的白名单，在白名单范围中的用户不参与基于位置区的IP地址分配。

```jinja2
{%- for item in add_adrlocwhitelst_list -%}
    ADD ADRLOCWHITELST:
    {#- --- 必选参数 --- -#}
    MSISDN="{{item.MSISDN}}",
    ;
{%- endfor -%}
```

