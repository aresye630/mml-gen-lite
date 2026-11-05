---
id: ''
name: 配置SWm接口对接数据（直联）
ne_type: UNC
type: feature
description: 专网UPF采用华为UDG产品，新增SWm接口用于与Non-SIM AAA UDM-UIM进行消息交互，目的是进行家庭网关的身份认证。  该任务旨在指导操作人员完成UPF的SWm接口对接配置。  * SWm接口当前版本仅支持IPv4栈类型。 * 专网UPF配置SWm接口时，不支持开启入不转板功能特性。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置一跳入家专网UPF","配置SWm接口对接数据（直联）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
专网UPF采用华为UDG产品，新增SWm接口用于与Non-SIM AAA UDM-UIM进行消息交互，目的是进行家庭网关的身份认证。该任务旨在指导操作人员完成UPF的SWm接口对接配置。* SWm接口当前版本仅支持IPv4栈类型。* 专网UPF配置SWm接口时，不支持开启入不转板功能特性。

## 必备事项
前提条件

前提条件

* UPF软件安装已完成。
* UPF初始配置已完成。
* 已完成一跳入家依赖功能的License加载。
* 已完成一跳入家要求的移动VPN相关配置。
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
          description: '-'
          data_source: '全网规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upconcenpoint_list:
      type: items
      properties:
        SWMCONCENMODE:
          name: 'Swm集中点模式'
          type: string
          required: false
          description: '-'
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
          description: '-'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    add_updiamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ORIGINSTATEID:
          name: 'ORIGINSTATEID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTVENDORID:
          name: 'SUPPORTVENDORID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiameteraaa_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_updiampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_updiamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          required: false
          description: '该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。'
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
          name: 'SELECTMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_updiamconn_list:
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
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          required: false
          description: '*-*'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: string
          required: false
          description: '*-*'
          data_source: '对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPV4地址'
          type: string
          required: false
          description: 'IPv4地址类型。不支持0.0.0.0和255.255.255.255。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: string
          required: false
          description: '取值范围19865~19928。'
          data_source: '对端协商'
          pattern: ''
          default: ''
    add_updiamaaagrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_updiamaaabndg_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORSEC:
          name: '主备用标记'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upapndiamaaag_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '专用DNN的APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPNAME:
          name: 'Diameter AAA组名'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Signaling'
    add_l3vpninst_list:
    - VRFNAME: 'VPN_Signaling'
    add_vpninstaf_list:
    - VRFNAME: 'VPN_Signaling'
      AFTYPE: ipv4uni
    set_upconcenpoint_list:
    - SWMCONCENMODE: LOCALPORT
    add_logicinf_list:
    - NAME: 'swmif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Signaling'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_updiamlocinfo_list:
    - HOSTNAME: udg_1
      REALMNAME: huawei.com
      PRODUCTNAME: udg@huawei.com
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_updiameteraaa_list:
    - HOSTNAME: 3gppaaa
      REALMNAME: 3gppaaa.huawei.com
      VPNINSTANCE: VPN_Signaling
    add_updiampeeraddr_list:
    - HOSTNAME: 3gppaaa
      ADDRTYPE: IPv4
      IPV4ADDRESS: 10.10.10.1
    add_updiamconngrp_list:
    - CONNGROUPNAME: groupname
      LOCALHOSTNAME: udg_1
      APPLICATION: SWM
      PEERHOSTNAME: 3gppaaa
      SELECTMODE: SESSION_ID
    add_updiamconn_list:
    - DIAMCONNGRP: groupname
      LOCINTERFACE: swmif1/0/0
      PEERADDRTYPE: IPv4
      PEERPORT: '3868'
      PEERIPV4ADDR: 10.10.10.1
      LOCALPORT: '19865'
    add_updiamaaagrp_list:
    - GROUPNAME: groupname
    add_updiamaaabndg_list:
    - GROUPNAME: groupname
      SERVERTYPE: PARA_3GPP
      HOSTNAME: 3gppaaa
      PRIORSEC: PRIMARY
    add_upapndiamaaag_list:
    - APN: 062apn1.com
      GROUPNAME: groupname
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 创建VPN实例。可选配置，如果已配置VPN跳过此步骤。

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_l3vpninst_list -%}
        ADD L3VPNINST:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_create_vpn_instance -%}
    {%- for item in add_vpninstaf_list -%}
        ADD VPNINSTAF:
        {#- --- 必选参数 --- -#}
        VRFNAME="{{item.VRFNAME}}",
        AFTYPE={{item.AFTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置SWm接口的集中点模式为本端端口模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_upconcenpoint_list的变量区（command: SET UPCONCENPOINT） -#}
<!-- MISSING_MACRO: command=SET UPCONCENPOINT list_name=set_upconcenpoint_list step_id=2 -->
```

### 3 配置SWm逻辑接口，VPN实例名称为VPN\_Signaling。

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
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
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
    ;
{%- endfor -%}
```

### 4 配置Diameter。

#### 4.1 配置本端端点的主机信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamlocinfo_list的变量区（command: ADD UPDIAMLOCINFO） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMLOCINFO list_name=add_updiamlocinfo_list step_id=4.1 -->
```

#### 4.2 配置Non-SIM AAA。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiameteraaa_list的变量区（command: ADD UPDIAMETERAAA） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMETERAAA list_name=add_updiameteraaa_list step_id=4.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiampeeraddr_list的变量区（command: ADD UPDIAMPEERADDR） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMPEERADDR list_name=add_updiampeeraddr_list step_id=4.2 -->
```

#### 4.3 建立本端与对端的链路组，并配置链路选择模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconngrp_list的变量区（command: ADD UPDIAMCONNGRP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONNGRP list_name=add_updiamconngrp_list step_id=4.3 -->
```

#### 4.4 配置到Non-SIM AAA的链路。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamconn_list的变量区（command: ADD UPDIAMCONN） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMCONN list_name=add_updiamconn_list step_id=4.4 -->
```

#### 4.5 设置Non-SIM AAA服务器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamaaagrp_list的变量区（command: ADD UPDIAMAAAGRP） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMAAAGRP list_name=add_updiamaaagrp_list step_id=4.5 -->
```

#### 4.6 指定主用Non-SIM AAA服务器组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_updiamaaabndg_list的变量区（command: ADD UPDIAMAAABNDG） -#}
<!-- MISSING_MACRO: command=ADD UPDIAMAAABNDG list_name=add_updiamaaabndg_list step_id=4.6 -->
```

#### 4.7 绑定Non-SIM AAA服务器组到APN。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_upapndiamaaag_list的变量区（command: ADD UPAPNDIAMAAAG） -#}
<!-- MISSING_MACRO: command=ADD UPAPNDIAMAAAG list_name=add_upapndiamaaag_list step_id=4.7 -->
```

