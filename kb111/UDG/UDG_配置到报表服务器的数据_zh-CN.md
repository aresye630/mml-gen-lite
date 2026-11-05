---
id: ''
name: 配置到报表服务器的数据
ne_type: UDG
type: feature
description: 报表服务器支持如下功能：  * 接收UDG上报的UFDR与ADR单据，生成相关报表，用于分析用户业务故障原因、了解运营商网络、扩展运营商业务等场景。 * 根据业务场景确定是否进行UFDR单据订阅，并下发订阅。  UDG通过Router A与Router B，以静态路由或动态路由的组网方式与报表服务器互联。如图1所示，以静态路由作为示例。  **图1** UDG与报表服务器的组网对接示意图  与报表服务器的对接支持IPv4和IPv6地址，该配置以IPv4地址举例。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG报表功能专题","报表功能部署","激活报表功能","配置到报表服务器的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
报表服务器支持如下功能：* 接收UDG上报的UFDR与ADR单据，生成相关报表，用于分析用户业务故障原因、了解运营商网络、扩展运营商业务等场景。* 根据业务场景确定是否进行UFDR单据订阅，并下发订阅。UDG通过Router A与Router B，以静态路由或动态路由的组网方式与报表服务器互联。如图1所示，以静态路由作为示例。**图1** UDG与报表服务器的组网对接示意图与报表服务器的对接支持IPv4和IPv6地址，该配置以IPv4地址举例。

## 必备事项
前提条件

已经完成**安装RPT服务**。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_rptsvr_list:
      type: items
      properties:
        RPTSVRNAME:
          name: '报表服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置报表服务器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RPTSVRTYPE:
          name: '报表话单消息格式'
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
          data_source: '本端规划'
          pattern: ''
          default: ALLTYPE
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
    mod_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'URR名称。  配置**MOD URR**的同时需要开启软参BIT1557 控制报表UFDR单据上报字段内容，以保证UPF上报的UFDR单据中包含Charging TLV相关字段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: false
          description: 'URR标识。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: false
          description: '该URR为在线计费应用的URR。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '* 在线计费时，和SMF上**ADD URR**命令的ONLINERG配置保持一致。 * 离线计费时，和SMF上**ADD URR**命令的RG配置保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SID:
          name: '业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '* 在线计费时，和SMF上**ADD URR**命令的ONLINESID配置保持一致。 * 离线计费时，和SMF上**ADD URR**命令的SID配置保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTATIME:
          name: '默认时长配额（秒）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 3600
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAVOLUME:
          name: '默认流量配额'
          type: integer
          minimum:
          - 0
          - 1000
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
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
          maximum: 3840
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
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_rptsvr_list:
    - RPTSVRNAME: 'UFDR_SERVER'
      RPTSVRTYPE: UFDR
    add_rptsvraddr_list:
    - ACCESSNAME: 'rpt_access1'
      RPTSVRNAME: 'UFDR_SERVER'
      IPTYPE: IPv4
      IPV4_ADDR: 10.80.128.1
      SVRPORT: 10700
      VPNINSTANCE: 'VPN_report'
      IPV6_ADDR: ''
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
    mod_urr_list:
    - URRNAME: 'urr_red'
      URRID: 1000
      USAGERPTMODE: ONLINE
      RG: 10
      SID: 20
      DFTQUOTAPARA: ''
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: ''
      ONLMETERINGTYPE: ''
    set_softpara_list:
    - DT: BIT
      BITNUM: 1557
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 已经完成**安装RPT服务**。

### 2 配置RPT的外联口物理IP、静态路由和BFD组网。

### 具体步骤请参见配置静态路由+BFD组网（IPv4）。

### 动态路由具体步骤请参见配置动态路由OSPF+BFD组网（IPv4）。

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
    ;
{%- endfor -%}
```

### 4 配置报表服务器的IP接入点。

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

### 报表服务器的UFDR接入点IP地址的默认端口为10700。

### 5 配置Grp逻辑接口。

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

### 6 可选：配置UFDR支持上报Charging TLV。

```jinja2
{%- if is_optional_ufdr_report_charging_tlv -%}
    {%- for item in mod_urr_list -%}
        MOD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRID is not none -%}
            URRID={{item.URRID}},
        {%- endif -%}
        {%- if item.USAGERPTMODE is not none -%}
            USAGERPTMODE={{item.USAGERPTMODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.RG is not none -%}
                RG={{item.RG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.SID is not none -%}
                SID={{item.SID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.DFTQUOTAPARA is not none -%}
                DFTQUOTAPARA={{item.DFTQUOTAPARA}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.DFTQUOTATIME is not none -%}
                DFTQUOTATIME={{item.DFTQUOTATIME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.DFTQUOTAVOLUME is not none -%}
                DFTQUOTAVOLUME={{item.DFTQUOTAVOLUME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFFMETERINGTYPE is not none -%}
                OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.ONLMETERINGTYPE is not none -%}
                ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_ufdr_report_charging_tlv -%}
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
        {#- --- 条件必选：DT=BYTE 时必选 --- -#}
        {%- if item.DT == 'BYTE' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=BYTE 时必选 --- -#}
        {%- if item.DT == 'BYTE' -%}
            BYTEVALUE={{item.BYTEVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=DWORD 时必选 --- -#}
        {%- if item.DT == 'DWORD' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=DWORD 时必选 --- -#}
        {%- if item.DT == 'DWORD' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=STRING 时必选 --- -#}
        {%- if item.DT == 'STRING' -%}
            STRINGNUM={{item.STRINGNUM}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DT=STRING 时可选 --- -#}
        {%- if item.DT == 'STRING' -%}
            {%- if item.STRINGVALUE is not none -%}
                STRINGVALUE="{{item.STRINGVALUE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当需要UFDR支持上报Charging TLV时，需要UPF本地配置**ADD URR**/**MOD URR**命令中的RG和SID参数，且RG和SID参数的配置和SMF上**ADD URR**/**MOD URR**命令对应的离线/在线（RG，SID）配置保持一致。同时需要开启软参BIT1557 控制报表UFDR单据上报字段内容，以保证UPF上报的UFDR单据中包含Charging TLV相关字段。

