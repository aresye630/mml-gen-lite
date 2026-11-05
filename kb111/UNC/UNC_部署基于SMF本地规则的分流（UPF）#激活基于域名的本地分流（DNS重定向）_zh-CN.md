---
id: ''
name: 激活基于域名的本地分流（DNS重定向）
ne_type: UNC
type: feature
description: 部署基于域名的本地分流功能，且本地DN部署DNS服务器时，需要配置七层分流规则和DNS重定向。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core ULCL分流解决方案","分流业务部署","基于SMF本地规则的分流","功能部署","部署基于SMF本地规则的分流（UPF）","激活基于域名的本地分流（DNS重定向）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
部署基于域名的本地分流功能，且本地DN部署DNS服务器时，需要配置七层分流规则和DNS重定向。

## 必备事项
前提条件

* 请仔细阅读分流原理。
* 已完成与周边网元的对接。
* 完成协议识别库和解析库的加载。
* 已开启Web Proxy功能。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_colocatedlbo_list:
      type: items
      properties:
        ULCLSWITCH:
          name: 'ULCL功能开关'
          type: string
          required: false
          description: '配置UL CL与PSA1共部署的本地分流功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_host_list:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          required: false
          description: '配置触发分流的Host信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '流过滤器。  说明：  flowfilter_ulcl01用于DNS报文的匹配，flowfilter_ulcl02用于TCP报文的匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '配置三四层过滤条件。  说明：  匹配DNS报文的过滤条件，三四层协议只能配置为UDP。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRENDPORT:
          name: '服务器结束端口号'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          required: false
          description: 'Host配置名称已通过**ADD HOST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          required: false
          description: '匹配DNS报文的过滤条件需要配置七层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URLTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          required: false
          description: '该参数取值要和**ADD HOST**命令配置的域名保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '匹配DNS报文的过滤条件需要绑定七层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          required: false
          description: '七层过滤器名字已通过**ADD L7FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfiltergrp_list:
      type: items
      properties:
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          required: false
          description: '对应SMF下发的Application ID。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLWFLTRLOGICGRP:
          name: '流过滤器逻辑分组'
          type: string
          required: false
          description: '或组内的任何一个流过滤器命中，则执行分流流程。'
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
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipfarm_list:
      type: items
      properties:
        HEALTHCHECKFLAG:
          name: '健康检查标记'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERFACENAME:
          name: '心跳检测接口名称'
          type: string
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
          required: false
          description: '使用的IP Farm由**ADD IPFARM**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务器IPv4地址'
          type: string
          required: false
          description: '重定向目的地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '配置重定向规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '绑定的PCC策略组已通过**ADD IPFARMSERVER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '与SMF上配置的PCC用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_colocatedlbo_list:
    - ULCLSWITCH: ENABLE
    add_host_list:
    - HOSTNAME: host1
      DOMAINVALUE: www.huawei.com
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_ulcl01'
    add_filter_list:
    - FILTERNAME: filter_test01
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: '53'
      SVRENDPORT: '53'
      SVRIPMODE: HOSTNAME
      HOSTNAME: host1
    add_fltbindflowf_list:
    - FLOWFILTERNAME: flowfilter_ulcl01
      FILTERNAME: filter_test01
    add_l7filter_list:
    - L7FILTERNAME: l7filter-test
      SUBL7FLTNAME: sl7filter-test
      URLTYPE: URL
      URL: www.huawei.com
    add_protbindflowf_list:
    - FLOWFILTERNAME: flowfilter_ulcl01
      PROTOCOLNAME: dns
      L7FILTERNAME: l7filter-test
    add_flowfiltergrp_list:
    - FLWFLTRGRPNAME: flowfiltergrp_ulcl01
      FLOWFILTERNAME: flowfilter_ulcl01
      FLWFLTRLOGICGRP: OR
    add_logicinf_list:
    - NAME: 'phif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.10.10.10'
      IPV4MASK1: '255.255.255.255'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
      VPNINSTANCE: ''
    add_ipfarm_list:
    - HEALTHCHECKFLAG: ENABLE
      IPFARMNAME: farm_test
      IPVERSION: IPV4
      INTERFACENAME: phif1/0/0
    add_ipfarmserver_list:
    - IPFARMNAME: farm_test
      IPVERSION: IPV4
      SERVERIPV4: 192.168.253.251
    add_rule_list:
    - RULENAME: rule_dns01
      POLICYTYPE: WEBPROXY
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: flowfilter_ulcl01
      POLICYNAME: farm_test
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_dns01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UL CL与PSA1共部署的本地分流功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_colocatedlbo_list的变量区（command: SET COLOCATEDLBO） -#}
<!-- MISSING_MACRO: command=SET COLOCATEDLBO list_name=set_colocatedlbo_list step_id=1 -->
```

### 2 配置Host信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_host_list的变量区（command: ADD HOST） -#}
<!-- MISSING_MACRO: command=ADD HOST list_name=add_host_list step_id=2 -->
```

### 3 配置基于域名的本地分流过滤条件。

#### 3.1 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.2 配置三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=3.2 -->
```

#### 3.3 绑定三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=3.3 -->
```

#### 3.4 配置七层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_l7filter_list的变量区（command: ADD L7FILTER） -#}
<!-- MISSING_MACRO: command=ADD L7FILTER list_name=add_l7filter_list step_id=3.4 -->
```

#### 3.5 绑定七层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list step_id=3.5 -->
```

### 4 配置本地分流流过滤器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfiltergrp_list的变量区（command: ADD FLOWFILTERGRP） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTERGRP list_name=add_flowfiltergrp_list step_id=4 -->
```

### 流过滤器组对应SMF下发的AppID。一个流过滤器组中需要绑定基于域名的本地分流过滤条件，才能实现针对一个AppID的分流功能。

### 匹配中流过滤器组后，根据ApplD检索到分流PDR，然后按照PDR中的转发规则FAR、QoS规则QER执行策略动作。

### 5 配置IP Farm使用的心跳检测接口。

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
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置IP Farm。

#### 6.1 创建重定向的IP Farm。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ipfarm_list的变量区（command: ADD IPFARM） -#}
<!-- MISSING_MACRO: command=ADD IPFARM list_name=add_ipfarm_list step_id=6.1 -->
```

#### 6.2 配置IP farm服务器地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ipfarmserver_list的变量区（command: ADD IPFARMSERVER） -#}
<!-- MISSING_MACRO: command=ADD IPFARMSERVER list_name=add_ipfarmserver_list step_id=6.2 -->
```

#### IP Farm配置完成后，可以执行命令**DSP IPFARMSERVER**查询IP Farm中server的状态。为确保业务正常进行，需保证至少有一个server的状态为up。

### 7 配置重定向规则。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=7 -->
```

### 8 配置重定向规则与用户模板的绑定关系。

#### 8.1 创建UserProfile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 将已配置的rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

