---
id: ''
name: 配置到OCS的数据(静态路由+BFD组网)
ne_type: UDG
type: feature
description: 当部署在线计费实现对用户的实时计费时，需要配置与OCS的互通数据。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","在线计费配置","在线计费对接配置","配置到OCS的数据(静态路由+BFD组网)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署在线计费实现对用户的实时计费时，需要配置与OCS的互通数据。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见**《UNC产品手册》：UNC初始配置与调测->了解组网架构与原理->业务组网与逻辑接口介绍**。
* 操作员了解UNC与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
* 已根据配置在线计费模板完成在线计费模板创建和绑定。
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
          minLength: 0
          maxLength: 31
          required: true
          description: '创建VPN实例。'
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
          description: '创建L3VPN实例。'
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
          description: '配置VPN实例下的地址族。'
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
    mod_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: '修改设备上VPN实例下配置的地址族参数。  RD（Route Distinguisher）用来唯一标识一个VPN。'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        GYCONCENMODE:
          name: 'Gy集中点模式'
          type: string
          required: false
          description: '配置Gy应用集中点模式。  说明：  本示例以“LOCALPORT”为例，请根据业务实际需要进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Gy接口逻辑IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置组级Gy逻辑接口1。'
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
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已在该配置任务中通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
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
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
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
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: '配置Gy应用的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          required: false
          description: '配置OCS的设备信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPNINSTANCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '该命令用于在指定UNC与指定OCS之间建立一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          required: false
          description: '增加Diameter链路对端的地址信息，配置Diameter链路对端的地址类型、IP、端口号或端点信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALPORT:
          name: 'LOCALPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: 'PEERADDRTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: 'PEERIPV4ADDR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: 'PEERPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          required: false
          description: '配置主OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          required: false
          description: '把OCS加入到OCS组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '为DCC模板配置主备OCS组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_dcctemplate_list:
      type: items
      properties: {}
    set_ceaorighostchk_list:
      type: items
      properties:
        CEAORIGHOSTCHK:
          name: '检查Gy的CEA消息中的Origin-Host'
          type: string
          required: false
          description: 'Diameter应用控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_tctimer_list:
      type: items
      properties:
        TCTIMERLEN:
          name: 'TC定时器时长（单位500ms）'
          type: string
          required: false
          description: '配置TC定时器时长，控制当UNC与OCS等Diameter对端断链后，重建链接的间隔时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TCMODE:
          name: '定时器模式'
          type: string
          required: false
          description: '配置TC定时器的模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_twtimer_list:
      type: items
      properties:
        TWTIMERLEN:
          name: 'TW定时器时长（秒）'
          type: string
          required: false
          description: '配置Tw定时器时长。当Tw定时器超时后，UNC会向OCS等Diameter对端发送DWR消息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TWNORESPTIMES:
          name: 'DWR消息响应超时次数上限'
          type: string
          required: false
          description: '配置DWR消息响应超时次数上限。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TWRSTTCP:
          name: '超时次数达到上限复位连接'
          type: string
          required: false
          description: '配置当DWR消息超时次数达到“TWNORESPTIMES”配置的上限是否复位TCP连接。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_gy'
    add_l3vpninst_list:
    - VRFNAME: 'vpn_gy'
    add_vpninstaf_list:
    - VRFNAME: 'vpn_gy'
      AFTYPE: ipv4uni
    mod_vpninstaf_list:
    - VRFNAME: 'vpn_gy'
      AFTYPE: ipv4uni
      VRFRD: '2050:1'
    set_concenpoint_list:
    - GYCONCENMODE: LOCALPORT
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.20.1'
      VPNINSTNAME: 'vpn_gy'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'Gyif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gy'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_diamlocinfo_list:
    - HOSTNAME: pgw1
      REALMNAME: huawei.com
      PRODUCTNAME: unc@huawei.com
    add_ocs_list:
    - OCSHOSTNAME: ocs1
      REALMNAME: huawei.com
      VPNINSTANCE: vpn_gy
    add_diamconngrp_list:
    - CONNGROUPNAME: dia1
      LOCALHOSTNAME: pgw1
      APPLICATION: GY
      PEERHOSTNAME: ocs1
      SELECTMODE: MASTER_SLAVE
    add_diampeeraddr_list:
    - HOSTNAME: ocs1
      ADDRTYPE: IPv4
      IPV4ADDRESS: 10.11.21.59
      PORT: '3868'
    add_diamconnection_list:
    - DIAMCONNGRP: dia1
      LOCINTERFACE: Gyif1/0/0
      LOCALPORT: '13201'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: 10.11.21.59
      PEERPORT: '3868'
    add_ocsgroup_list:
    - OCSGRPNAME: og-test1
    add_ocsbinding_list:
    - OCSGRPNAME: og-test1
      OCSHOSTNAME: ocs1
    add_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      PRIOCSGRPNAME: og-test1
      SECOCSGRPNAME: og-test2
    mod_dcctemplate_list:
    - {}
    set_ceaorighostchk_list:
    - CEAORIGHOSTCHK: ENABLE
    set_tctimer_list:
    - TCTIMERLEN: '1'
      TCMODE: MULTIPLY
    set_twtimer_list:
    - TWTIMERLEN: '30'
      TWNORESPTIMES: '3'
      TWRSTTCP: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 参考**《UNC产品手册》：UNC初始配置与调测->****组网路由配置->****配置VNF侧IP路由数据（非SDN）->****手动部署****->****配置静态路由+BFD组网（IPv4）**配置对应的组网。

### 2 创建VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 创建L3VPN实例。

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

```jinja2
{%- for item in mod_vpninstaf_list -%}
    MOD VPNINSTAF:
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

### 4 **可选：**配置Gy接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_concenpoint_list的变量区（command: SET CONCENPOINT） -#}
<!-- MISSING_MACRO: command=SET CONCENPOINT list_name=set_concenpoint_list step_id=4 -->
```

### 5 配置Gy逻辑接口。

#### 5.1 配置逻辑IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置Gy逻辑接口。

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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
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
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### **ADD LOGICINF**中的“IP地址+VPN实例名称”和**ADD LOGICIP**命令中的“IP地址+VPN实例名称”必须一致。

### 6 配置在线计费中的本端设备标识。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_diamlocinfo_list的变量区（command: ADD DIAMLOCINFO） -#}
<!-- MISSING_MACRO: command=ADD DIAMLOCINFO list_name=add_diamlocinfo_list step_id=6 -->
```

### UNC的Gx应用和Gy应用的本端主机名可以相同，但是同时要求“REALMNAME”参数和“PRODUCTNAME”参数也必须相同。

### 7 配置在线计费中的OCS信息。

#### 7.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ocs_list的变量区（command: ADD OCS） -#}
<!-- MISSING_MACRO: command=ADD OCS list_name=add_ocs_list step_id=7.1 -->
```

#### OCS Server绑定的VPN实例必须和Gy逻辑接口绑定的VPN实例一致。

#### 7.2 Diameter链路信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_diamconngrp_list的变量区（command: ADD DIAMCONNGRP） -#}
<!-- MISSING_MACRO: command=ADD DIAMCONNGRP list_name=add_diamconngrp_list step_id=7.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_diampeeraddr_list的变量区（command: ADD DIAMPEERADDR） -#}
<!-- MISSING_MACRO: command=ADD DIAMPEERADDR list_name=add_diampeeraddr_list step_id=7.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_diamconnection_list的变量区（command: ADD DIAMCONNECTION） -#}
<!-- MISSING_MACRO: command=ADD DIAMCONNECTION list_name=add_diamconnection_list step_id=7.2 -->
```

#### 当“GYCONCENMODE”通过**SET CONCENPOINT**命令选择为“LOCALPORT”时，可使用**ADD DIAMCONNECTION**命令设置本端的端口号。

#### 7.3 配置在线计费系统的OCS组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ocsgroup_list的变量区（command: ADD OCSGROUP） -#}
<!-- MISSING_MACRO: command=ADD OCSGROUP list_name=add_ocsgroup_list step_id=7.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ocsbinding_list的变量区（command: ADD OCSBINDING） -#}
<!-- MISSING_MACRO: command=ADD OCSBINDING list_name=add_ocsbinding_list step_id=7.3 -->
```

#### UNC支持配置OCS group，group间是主备关系，group内绑定的OCS间是负荷分担关系。其中负荷分担又分为以下几种情况。

##### 7.3.1 OCS平均负荷分担

##### 同一group内的所有OCS平均负荷分担用户的在线计费消息处理。默认情况下采用此种方式。

##### 7.3.2 基于用户号段进行OCS负荷分担

##### 可以通过以下方式实现基于用户号段选择OCS：

###### 7.3.2.1 根据用户的MSISDN/IMSI号段选择UserProfile，再根据UserProfile下绑定的在线计费模板来选择不同的OCS，实现将用户分布在不同的OCS上进行在线计费处理，降低对单个OCS性能的要求。

###### 7.3.2.2 根据用户的MSISDN/IMSI号段直接选择OCS，实现将用户分布在不同的OCS上进行在线计费处理。

##### 一般情况下，尽量避免同时配置上述两种方式选择OCS。当两种条件都满足的情况下，优先根据UserProfile下关联的OCS进行在线计费处理。

##### 7.3.3 基于百分比例进行OCS负荷分担

##### 根据预先设置的百分比例选择OCS，百分比例的基数是累计选择此OCS的次数，实现将用户按比例分布在不同的OCS上进行在线计费，这是实现根据单个OCS性能选择OCS的一种方式。

#### 7.4 配置主备OCS组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list step_id=7.4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list step_id=7.4 -->
```

### 8 **可选：**配置Diameter应用相关功能，即设置UNC是否检查OCS返回的CEA消息中携带的Origin-Host AVP。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ceaorighostchk_list的变量区（command: SET CEAORIGHOSTCHK） -#}
<!-- MISSING_MACRO: command=SET CEAORIGHOSTCHK list_name=set_ceaorighostchk_list step_id=8 -->
```

### 9 **可选：**配置UNC与对端OCS重建TCP链接的间隔时长。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_tctimer_list的变量区（command: SET TCTIMER） -#}
<!-- MISSING_MACRO: command=SET TCTIMER list_name=set_tctimer_list step_id=9 -->
```

### 10 **可选：**配置DWR消息响应超时次数达到上限后UNC的处理动作。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_twtimer_list的变量区（command: SET TWTIMER） -#}
<!-- MISSING_MACRO: command=SET TWTIMER list_name=set_twtimer_list step_id=10 -->
```

