---
id: GWFD-010155
name: 配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）
ne_type: UDG
type: feature
description: 适用于PGW-U。  UDG与ePDG互通，用于部署WiFi用户接入EPC网络。  * 逻辑接口：Paif接口。 * 路由：OSPF动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010155 Untrusted Non-3GPP网络用户接入","激活Untrusted Non-3GPP网络用户接入功能","配置PGW-U到Untrusted Non-3GPP GW的数据（VPN+OSPF动态路由组网）（虚机容器）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
适用于PGW-U。UDG与ePDG互通，用于部署WiFi用户接入EPC网络。* 逻辑接口：Paif接口。* 路由：OSPF动态路由，各接口对外发布的路由优先级相同，作为等价路由实现物理链路的负荷分担。

## 必备事项
前提条件

* 请仔细阅读IPFD-015001 VRF功能和IPFD-014001 支持OSPF特性概述。
* UDG与网络实体之间的网络环境已经构建完成。
* 操作员了解UDG各类接口的类型及命名规范。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '配置VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: 'BFD使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '设置BFD全局属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: 'UDG到ePDG动态路由的OSPF进程号。  说明：  路由器的Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_ospf_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '在OSPF进程下创建区域。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfareaauth_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHENMODE:
          name: '认证模式'
          type: string
          enum:
          - hmac-md5
          - hmac-sha256
          - keychain
          - md5
          - simple
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTMD5:
          name: 'MD5/HMAC-MD5/HMAC-SHA256 密码'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTSIMPLE:
          name: '简单认证密码'
          type: string
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHTEXTTYPE:
          name: '密文口令类型'
          type: string
          enum:
          - cipher
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: cipher
        KEYCHAINNAME:
          name: 'KeyChain名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYID:
          name: '密文验证字标识符'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '在OSPF进程下的区域增加一个网段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfinterface_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域标识'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          description: '将外部路由引入到OSPF域中，并在OSPF域中发布引入的路由信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAG:
          name: '标签'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '引入路由类型'
          type: integer
          minimum: 1
          maximum: 2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '创建Paif接口。'
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
  examples:
    add_l3vpninst_list:
    - VRFNAME: 'vpn-s2b'
    add_vpninstaf_list:
    - VRFNAME: 'vpn-s2b'
      AFTYPE: ipv4uni
      VRFRD: '100:1'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn-s2b'
    set_bfd_list:
    - BFDENABLE: TRUE
    add_ospf_list:
    - PROCID: 6
      VRFNAME: 'vpn-s2b'
      SCHEMAROUID: '10.8.20.1'
    mod_ospf_list:
    - PROCID: 6
      BFDALLINTFFLG: TRUE
    add_ospfarea_list:
    - PROCID: 6
      AREAID: '0.0.0.1'
    add_ospfareaauth_list:
    - PROCID: ''
      AREAID: ''
      AUTHENMODE: ''
      AUTHTEXTMD5: ''
      AUTHTEXTSIMPLE: ''
      AUTHTEXTTYPE: cipher
      KEYCHAINNAME: ''
      KEYID: ''
    add_ospfnetwork_list:
    - PROCID: 6
      AREAID: '0.0.0.1'
      IPADDRESS: '10.8.7.0'
      WILDCARDMASK: '0.0.0.15'
    add_ospfinterface_list:
    - PROCID: ''
      AREAID: ''
      IFNAME: ''
    add_ospfimportroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: ''
      TAG: ''
      TYPE: ''
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
    add_logicinf_list:
    - NAME: 'Paif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.10.10.10'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn-s2b'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 参考初始配置中**配置动态路由OSPF+BFD组网（IPv4）**对应组网配置。

### 2 创建L3VPN实例。

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

### 3 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 4 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用输入，使用默认值即可。

### 5 创建OSPF进程。

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

```jinja2
{%- for item in mod_ospf_list -%}
    MOD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### UDG支持VPN多实例，需要取消环路检查，否则会导致OSPF路由引入失败。需要将“VPNINSCAPSIMFLG”配置为“TRUE”。

### 优选用户配置的Router ID。如果未配置，则选择OSPF进程所在VRF内或者公网内的最大接口IP地址。

### 如果需要为OSPF动态路由绑定BFD会话，通过**ADD OSPF**配置“使能BFD”为“TRUE”。

### 当OSPF路由配置共网段时，需**MOD OSPFAREA**将“VIRTUALSYSFLAG”配置为“TRUE”。

### 6 增加OSPF区域。

### 根据不同的验证类型选择不同的区域配置。

#### 6.1 不指定验证类型。

```jinja2
{%- if is_scenario_no_auth_type -%}
    {%- for item in add_ospfarea_list -%}
        ADD OSPFAREA:
        {#- --- 必选参数 --- -#}
        PROCID={{item.PROCID}},
        AREAID="{{item.AREAID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.1.1 “AERATYPE（区域类型）”可以设置为“NSSA”或“Normal”。

##### 6.1.2 如果参数“AERATYPE（区域类型）”配置为“NSSA”时, 必须配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

#### 6.2 指定验证类型。

```jinja2
{%- if is_scenario_with_auth_type -%}
    {%- for item in add_ospfareaauth_list -%}
        ADD OSPFAREAAUTH:
        {#- --- 必选参数 --- -#}
        AREAID="{{item.AREAID}}",
        AUTHENMODE={{item.AUTHENMODE}},
        PROCID={{item.PROCID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTHENMODE=keychain 时必选 --- -#}
        {%- if item.AUTHENMODE == 'keychain' -%}
            KEYCHAINNAME="{{item.KEYCHAINNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AUTHENMODE=hmac-sha256/md5/hmac-md5 时可选 --- -#}
        {%- if item.AUTHENMODE in ['hmac-sha256', 'md5', 'hmac-md5'] -%}
            {%- if item.AUTHTEXTMD5 is not none -%}
                AUTHTEXTMD5="{{item.AUTHTEXTMD5}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AUTHENMODE=simple 时可选 --- -#}
        {%- if item.AUTHENMODE == 'simple' -%}
            {%- if item.AUTHTEXTSIMPLE is not none -%}
                AUTHTEXTSIMPLE="{{item.AUTHTEXTSIMPLE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AUTHENMODE=hmac-sha256/simple/md5/hmac-md5 时可选 --- -#}
        {%- if item.AUTHENMODE in ['hmac-sha256', 'simple', 'md5', 'hmac-md5'] -%}
            {%- if item.AUTHTEXTTYPE is not none -%}
                AUTHTEXTTYPE={{item.AUTHTEXTTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AUTHENMODE=hmac-sha256/md5/hmac-md5 时可选 --- -#}
        {%- if item.AUTHENMODE in ['hmac-sha256', 'md5', 'hmac-md5'] -%}
            {%- if item.KEYID is not none -%}
                KEYID={{item.KEYID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 增加运行OSPF协议的接口。

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

### 8 **可选**：配置OSPF协议的接口属性。

```jinja2
{%- if is_optional_ospf_interface_attribute -%}
    {%- for item in add_ospfinterface_list -%}
        ADD OSPFINTERFACE:
        {#- --- 必选参数 --- -#}
        AREAID="{{item.AREAID}}",
        IFNAME="{{item.IFNAME}}",
        PROCID={{item.PROCID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 参数“NETWORKTYPE”（网络类型）选择“broadcast”、“nbma”、“p2p”或“p2mp”。

### 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。

### 9 设置OSPF引入路由类型。

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
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTAGCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTAGCFG == 'TRUE' -%}
        TAG={{item.TAG}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTYPECFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTYPECFG == 'TRUE' -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
    {%- if item.PROTOCOL == 'BGP' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
    {%- if item.PROTOCOL == 'OSPF' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 创建Paif接口。

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

