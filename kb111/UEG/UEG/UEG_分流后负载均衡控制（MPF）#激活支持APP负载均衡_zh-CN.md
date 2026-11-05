---
id: ''
name: 激活支持APP负载均衡
ne_type: UEG
type: feature
description: 当运营商为了均衡APP的负荷，部署了多台APP Server进行负荷分担，采用负载均衡机制对外呈现单一的虚拟IP地址时，MPF需要部署负载均衡机制，将通过Nxu接口的VXLAN-GPE（Generic Protocol Extension for VXLAN）隧道转发到MPF上的数据报文分流到具体的APP Server。  适用于MPF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC APP业务访问控制（公共）","分流后负载均衡控制（MPF）","激活支持APP负载均衡"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商为了均衡APP的负荷，部署了多台APP Server进行负荷分担，采用负载均衡机制对外呈现单一的虚拟IP地址时，MPF需要部署负载均衡机制，将通过Nxu接口的VXLAN-GPE（Generic Protocol Extension for VXLAN）隧道转发到MPF上的数据报文分流到具体的APP Server。适用于MPF。

## 必备事项
前提条件

* 请仔细阅读负载均衡机制原理。
* 已完成加载License。
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
    set_ipfarmglobal_list:
      type: items
      properties:
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - IPMS
          - PCSCF
          - REDIRECT
          required: true
          description: '指定IP farm全局配置的类型为重定向。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 6
          maximum: 60
          required: false
          description: '两次心跳检测间的时间阈值，单位为秒。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHSUCCLIMIT:
          name: '健康检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '重定向Server的状态为down且心跳检测连续成功次数达到配置值时，将Server的状态置为up。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHFAILLIMIT:
          name: '健康检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '重定向Server的状态为up且心跳检测连续失败次数达到配置值时，将Server的状态置为down。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LBMETHOD:
          name: '负载均衡模式'
          type: string
          enum:
          - INVAILD
          - LEAST_LOAD
          - LEAST_RECENTLY_USED
          - ROUND_ROBIN
          required: false
          description: '支持三种方式：   * ROUND\_ROBIN：轮询方式 * LEAST\_RECENTLY\_USED：选择最久未被使用的Server * LEAST\_LOAD：选择最小负荷Server方式'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: true
          description: '配置VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '整机IP Farm心跳检测使用的接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '心跳检测的本端IP地址一般是从终端的地址池中获取，在配置地址池时需要预留一个IP地址用于IP Farm的心跳检测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '将逻辑接口与VPN绑定。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ipfarm_list:
      type: items
      properties:
        HEALTHCHECKFLAG:
          name: '健康检查标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - IPMS
          - PCSCF
          - REDIRECT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: REDIRECT
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VIRTUALIP:
          name: '虚拟IP地址'
          type: string
          maxLength: 15
          required: false
          description: '设置IP farm对应的虚拟IPv4地址，和**ADD FILTER**命令的服务器IP地址配置保持一致，通过该虚拟IP地址关联到唯一的IP farm。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERFACENAME:
          name: '心跳检测接口名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过**ADD LOGICINF**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ipfarmserver_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          maxLength: 31
          required: true
          description: '使用的IP Farm由**ADD IPFARM**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '负荷分担的APP Server的IP版本。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务器IPv4地址'
          type: string
          required: false
          description: '负荷分担的APP Server的真实IP地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          maxLength: 63
          required: true
          description: '通过匹配filter，实现三四层报文的分析，从而过滤出会触发负载均衡机制的数据报文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ANY
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: '配置APP对外呈现的虚拟IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASK:
          name: '服务器IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: '刷新Filter配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '配置负载均衡类型的Rule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - BWM
          - MTP
          - WEBPROXY
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用的IP Farm已通过**ADD IPFARM**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 65535
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置User Profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'User Profile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_localuserprof_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将User Profile指定为全局User Profile，即**ADD LOCALUSERPROF**命令的“USERPROFILENAME”和**ADD USERPROFILE**命令的“USERPROFILENAME”必须配置为相同值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 1920
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LBAN02'
      SWITCH: ENABLE
    set_ipfarmglobal_list:
    - SERVERTYPE: REDIRECT
      TIMETHRESHOLD: 6
      HEALTHSUCCLIMIT: 3
      HEALTHFAILLIMIT: 3
      LBMETHOD: ROUND_ROBIN
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_phif'
    add_logicinf_list:
    - NAME: 'phif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.10.10.10'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_phif'
    add_ipfarm_list:
    - HEALTHCHECKFLAG: ENABLE
      IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERTYPE: REDIRECT
      VPNINSTANCE: 'VPN_phif'
      VIRTUALIP: '10.1.1.1'
      INTERFACENAME: 'phif1/0/0'
    add_ipfarmserver_list:
    - IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERIPV4: 10.1.2.1
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '10.1.1.1'
      SVRIPMASKTYPE: IPTYPE
      SVRIPMASK: '0.0.0.0'
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flow-l34'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flow-l34'
      FILTERNAME: 'filter_test'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_rule_list:
    - RULENAME: 'rule_test1'
      POLICYTYPE: WEBPROXY
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flow-l34'
      POLICYNAME: 'farm_test'
      PRIORITY: 10
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test1'
    add_localuserprof_list:
    - USERPROFILENAME: 'up_test'
    set_softpara_list:
    - DT: BIT
      BITNUM: 596
      BITVALUE: 0
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

### 2 配置IPFarm全局参数。

```jinja2
{%- for item in set_ipfarmglobal_list -%}
    SET IPFARMGLOBAL:
    {#- --- 必选参数 --- -#}
    SERVERTYPE={{item.SERVERTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SERVERTYPE=PCSCF/REDIRECT/IPMS 时可选 --- -#}
    {%- if item.SERVERTYPE in ['PCSCF', 'REDIRECT', 'IPMS'] -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=PCSCF/REDIRECT/IPMS 时可选 --- -#}
    {%- if item.SERVERTYPE in ['PCSCF', 'REDIRECT', 'IPMS'] -%}
        {%- if item.HEALTHSUCCLIMIT is not none -%}
            HEALTHSUCCLIMIT={{item.HEALTHSUCCLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=PCSCF/REDIRECT/IPMS 时可选 --- -#}
    {%- if item.SERVERTYPE in ['PCSCF', 'REDIRECT', 'IPMS'] -%}
        {%- if item.HEALTHFAILLIMIT is not none -%}
            HEALTHFAILLIMIT={{item.HEALTHFAILLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SERVERTYPE=REDIRECT 时可选 --- -#}
    {%- if item.SERVERTYPE == 'REDIRECT' -%}
        {%- if item.LBMETHOD is not none -%}
            LBMETHOD={{item.LBMETHOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 负载均衡模式通过**SET IPFARMGLOBAL**命令的“LBMETHOD”参数配置：

### ROUND\_ROBIN：指定为轮询方式，即在一个IPfarm内对所有APP Server进行轮询，跳过状态为down的APP Server。

### LEAST\_LOAD：指定为选择最小负荷APP Server方式，即在一个IPfarm内，记录每个APP Server上的实时负荷量，当负荷分担时选择负荷量最小的APP Server。当有APP Server状态为down，则将该APP Server负荷量清零。

### LEAST\_RECENTLY\_USED：指定为选择最久未被使用的APP Server。在一个IPfarm内，记录每个APP Server被选择的时间，负荷分担时选择最久未被使用的APP Server，并更新其被选择的时间。当有APP Server状态为down，则将该APP Server的被选择时间清零。

### 3 配置IP Farm使用的心跳检测接口。

#### 3.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 3.2 配置IP Farm使用的心跳检测接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置IP Farm。

#### 4.1 创建重定向的IP Farm，不同IP Farm下的服务器需要配置不同的心跳检测接口。

```jinja2
{%- for item in add_ipfarm_list -%}
    ADD IPFARM:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.HEALTHCHECKFLAG is not none -%}
        HEALTHCHECKFLAG={{item.HEALTHCHECKFLAG}},
    {%- endif -%}
    {%- if item.SERVERTYPE is not none -%}
        SERVERTYPE={{item.SERVERTYPE}},
    {%- endif -%}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.VIRTUALIP is not none -%}
            VIRTUALIP="{{item.VIRTUALIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 心跳检测接口名称: 条件必选(健康检查标记=ENABLE) / 条件可选(健康检查标记=DISABLE) --- -#}
    {%- if (item.HEALTHCHECKFLAG == 'ENABLE') -%}
        INTERFACENAME="{{item.INTERFACENAME}}",
    {%- elif (item.HEALTHCHECKFLAG == 'DISABLE') -%}
        {%- if item.INTERFACENAME is not none -%}
            INTERFACENAME="{{item.INTERFACENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 为该ip-farm绑定已配置的心跳检测接口，通过该接口发送接收心跳检测消息。

```jinja2
{%- for item in add_ipfarmserver_list -%}
    ADD IPFARMServer:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SERVERIPV4 is not none -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### IP Farm配置完成后，可以执行命令**LST IPFARMSERVER**查询IP Farm中Server的状态。为确保业务正常进行，需保证至少有一个Server的状态为up。

### 5 配置触发负载均衡机制的三四层过滤条件。

#### 5.1 配置负载均衡机制使用的三四层过滤条件，IP地址为APP Server的虚拟IP地址。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRIPMODE is not none -%}
        SVRIPMODE={{item.SVRIPMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIP="{{item.SVRIP}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMASKTYPE=IPTYPE 时必选 --- -#}
    {%- if item.SVRIPMASKTYPE == 'IPTYPE' -%}
        SVRIPMASK="{{item.SVRIPMASK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置FlowFilter。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 5.3 将Filter绑定到FlowFilter。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 5.4 刷新Filter配置。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 6 配置负载均衡机制使用的规则。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=MTP/BWM/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['MTP', 'BWM', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置负载均衡机制使用的业务策略组合。

#### 7.1 配置User Profile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 7.2 将配置的Rule绑定到User Profile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 7.3 将User Profile指定为全局User Profile。

```jinja2
{%- for item in add_localuserprof_list -%}
    ADD LOCALUSERPROF:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### **ADD LOCALUSERPROF**命令的“USERPROFILENAME”和**ADD USERPROFILE**命令的“USERPROFILENAME”必须配置为相同值。

### 8 配置软参**BIT596**和**BIT1541**，保证用户业务报文可以采用负载均衡机制进行分流。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

