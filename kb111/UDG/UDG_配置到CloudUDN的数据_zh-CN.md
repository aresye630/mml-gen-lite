---
id: GWFD-111701
name: 配置到CloudUDN的数据
ne_type: UDG
type: feature
description: CloudUDN接收UDG上报的ADR单据，进行可视化呈现，用于分析用户业务故障原因、了解运营商网络、扩展运营商业务等场景。  UDG通过Router A与Router B，以静态路由或动态路由的组网方式与CloudUDN互联。如图1所示，以静态路由作为示例。  **图1** UDG与CloudUDN的组网对接示意图  与CloudUDN的对接支持IPv4和IPv6地址，该配置以IPv4地址举例。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","报表功能","GWFD-111701 拥塞小区分析","激活拥塞小区分析","配置到CloudUDN的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
CloudUDN接收UDG上报的ADR单据，进行可视化呈现，用于分析用户业务故障原因、了解运营商网络、扩展运营商业务等场景。UDG通过Router A与Router B，以静态路由或动态路由的组网方式与CloudUDN互联。如图1所示，以静态路由作为示例。**图1** UDG与CloudUDN的组网对接示意图与CloudUDN的对接支持IPv4和IPv6地址，该配置以IPv4地址举例。

## 必备事项
前提条件

已完成SSU可选服务的安装，请参考安装SSU服务。
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
          minLength: 0
          maxLength: 63
          required: true
          description: '配置Grp逻辑接口。'
          data_source: '固定取值'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
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
    add_rptsvr_list:
      type: items
      properties:
        RPTSVRNAME:
          name: '报表服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置报表服务器。   * SUBSCRIPTION：用于下发订阅消息。 * ADR：用于上报单据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RPTSVRTYPE:
          name: '报表消息类型'
          type: string
          enum:
          - ADR
          - ALLTYPE
          - BASIC
          - BTDR
          - SUBSCRIPTION
          - UFDR
          - EXP
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ALLTYPE
        SVRFUNC:
          name: '服务器功能'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: 'RPT-1&SSU-1'
    add_rptsvraddr_list:
      type: items
      properties:
        ACCESSNAME:
          name: '接入点名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置报表服务器IP接入点。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RPTSVRNAME:
          name: '报表服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4_ADDR:
          name: 'IPv4地址'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRPORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 10700
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '绑定VPN时需要确保该VPN已经通过**ADD VPNINST**配置。  如果**ADD LOGICINF**命令绑定了VPN实例，那么**ADD RPTSVRADDR**命令也必须绑定VPN实例，否则链路建立不成功。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6_ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_report'
    add_logicinf_list:
    - NAME: 'grpif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.1.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_report'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_rptsvr_list:
    - RPTSVRNAME: 'ADR_SERVER'
      RPTSVRTYPE: ADR
      SVRFUNC: SSU-1
    add_rptsvraddr_list:
    - ACCESSNAME: 'rpt_access1'
      RPTSVRNAME: 'ADR_SERVER'
      IPTYPE: IPv4
      IPV4_ADDR: 10.80.128.1
      SVRPORT: 10700
      VPNINSTANCE: 'VPN_report'
      IPV6_ADDR: ''
    - ACCESSNAME: 'rpt_access11'
      RPTSVRNAME: 'SUB_SERVER'
      IPTYPE: IPv4
      IPV4_ADDR: 10.80.128.1
      SVRPORT: 10700
      VPNINSTANCE: 'VPN_report'
      IPV6_ADDR: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置外联口物理IP、静态路由和BFD组网。

### 具体步骤请参见配置静态路由+BFD组网（IPv4）。

### 动态路由具体步骤请参见配置动态路由OSPF+BFD组网（IPv4）。

### 2 配置Grp逻辑接口。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

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

### 3 配置报表服务器。

```jinja2
{%- for item in add_rptsvr_list -%}
    ADD RPTSVR:
    {#- --- 必选参数 --- -#}
    RPTSVRNAME="{{item.RPTSVRNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RPTSVRTYPE is not none -%}
        RPTSVRTYPE={{item.RPTSVRTYPE}},
    {%- endif -%}
    {%- if item.SVRFUNC is not none -%}
        SVRFUNC={{item.SVRFUNC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置报表服务器的IP接入点。

#### 4.1 //配置ADR上报的报表服务器

```jinja2
{%- for item in add_rptsvraddr_list -%}
    ADD RPTSVRADDR:
    {#- --- 必选参数 --- -#}
    ACCESSNAME="{{item.ACCESSNAME}}",
    RPTSVRNAME="{{item.RPTSVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4_ADDR is not none -%}
        IPV4_ADDR="{{item.IPV4_ADDR}}",
    {%- endif -%}
    {%- if item.SVRPORT is not none -%}
        SVRPORT={{item.SVRPORT}},
    {%- endif -%}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6_ADDR="{{item.IPV6_ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

