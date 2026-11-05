---
id: GWFD-020412
name: AAA下发L2TP属性方式激活L2TP VPN
ne_type: UDG
type: feature
description: 在UDG与企业LNS之间部署L2TP组网，且PGW-C/SMF支持AAA鉴权，AAA Server在access accept消息中下发LNS信息时，需要配置本页面。其中，AAA下发L2TP属性方式下PGW-U/UPF本地不需要配置L2TP组，直接使用AAA通过PGW-C/SMF下发的LNS信息。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","组网功能","GWFD-020412 L2TP VPN","激活L2TP VPN","AAA下发L2TP属性方式激活L2TP VPN"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG与企业LNS之间部署L2TP组网，且PGW-C/SMF支持AAA鉴权，AAA Server在access accept消息中下发LNS信息时，需要配置本页面。其中，AAA下发L2TP属性方式下PGW-U/UPF本地不需要配置L2TP组，直接使用AAA通过PGW-C/SMF下发的LNS信息。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-020412 L2TP VPN。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_globall2tp_list:
      type: items
      properties:
        LOCALNAME:
          name: '隧道本端的名称'
          type: string
          minLength: 0
          maxLength: 30
          required: false
          description: '设置L2TP的缺省属性，包括：L2TP隧道本端名称、HELLO报文发送开关、HELLO报文重发间隔和报文重发次数等。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HELLOINTERVALSW:
          name: 'HELLO报文开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HELLOINTERVAL:
          name: 'HELLO报文间隔(秒)'
          type: integer
          minimum: 60
          maximum: 10000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RETRYTIMES:
          name: '报文重发次数'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PPPMAGICNUMBER:
          name: '是否支持Magic-Number协商'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MAXSENDWINSIZE:
          name: '发送窗口上限'
          type: integer
          minimum: 4
          maximum: 128
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        INITTUNNELNUM:
          name: '初始隧道个数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXSESSIONNUM:
          name: '每条隧道承载的会话个数上限'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnl2tpattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置APN的L2TP相关信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        L2TPSWITCH:
          name: 'APN支持L2TP功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置指定APN是否支持L2TP功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: 'l2tp支持ipv6功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制是否支持L2TP内层IPv6，默认不使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSLNSMODE:
          name: 'RADIUS服务器返回多LNS的工作模式'
          type: string
          enum:
          - REDUNDANCY
          - TUNNEL_PREFER
          required: false
          description: '指定RADIUS鉴权服务器返回多LNS时LNS的工作模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ICRQ_CALLINGNO:
          name: 'ICRQ携带Calling-number AVP值'
          type: string
          enum:
          - IMEI
          - IMSI
          - MSISDN
          required: false
          description: '指定系统发送的ICRQ消息中Calling-number AVP中携带的是MSISDN。根据需求，还可配置为IMSI或IMEI。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ICCN_AUTH:
          name: 'ICCN携带鉴权信元开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当PPP鉴权开关为不鉴权时，ICCN消息中不携带鉴权相关信元。  当PPP鉴权开关为鉴权时，且用户需要进行鉴权的情况下，ICCN消息中携带鉴权相关信元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPCP_NEGO:
          name: '发起IPCP协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制系统是否主动发起IPCP协商。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINNAMEACT:
          name: '增加或剥离域名'
          type: string
          enum:
          - ADD_DISABLE_STRIP_DISABLE
          - ADD_DISABLE_STRIP_ENABLE
          - ADD_ENABLE_STRIP_DISABLE
          required: false
          description: 'ICCN\CHAP\PAP消息中的用户名是否支持增加或剥离域名功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINNAMEPOS:
          name: '域名位置'
          type: string
          enum:
          - PREFIX
          - SUFFIX
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ICCN_LCPNEGO:
          name: 'ICCN携带LCP CONFREQ信元开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICCN_PGROUPID:
          name: 'ICCN携带PrivateGroupId AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICCN_TXSPEED:
          name: 'ICCN携带TxConnectSpeed值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICRQ_BEARER:
          name: 'ICRQ携带Bearer Type AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L2TPGROUPID:
          name: 'L2TP组号'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT2:
          name: '软参记录数据类型'
          type: string
          enum:
          - BYTE
          - DWORD
          required: true
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
        BYTEPOSITION:
          name: 'Byte软参BIT位位置'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 1
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
        DWORDPOSITION:
          name: 'Dword软参BIT位位置'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 1
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
          description: 'Giif接口。'
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
          description: 'Giif接口绑定的VPN实例与APN绑定的VPN实例一致。  已通过**ADD VPNINST**命令配置，可以使用**LST VPNINST**命令进行查询。'
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
    add_l2tprdsclient_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '在APN上绑定指定的源端Gi接口。  在AAA返回L2TP属性启动L2TP业务场景，该接口可用做系统与LNS进行交互时的源端接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INTERFACENAME:
          name: '接口名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_pppcfg_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '配置系统进行PPP协商时所使用的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MRU:
          name: '最大接收单元'
          type: integer
          minimum: 64
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMEOUT:
          name: '超时时间（秒）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnpppaccess_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置APN的PPP相关信息，支持PPP鉴权功能。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AUTHENTICATION:
          name: '鉴权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_l2tpn4key_list:
      type: items
      properties:
        N4KEYVALUE:
          name: 'N4密钥'
          type: string
          minLength: 0
          maxLength: 432
          required: false
          description: '若不配置，即明文携带L2TP私有信元，存在一定安全风险，建议和对端SMF同时配置加密功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CFMN4KEYVALUE:
          name: '确认N4密钥'
          type: string
          minLength: 0
          maxLength: 432
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5L2TP01'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_l2tp'
    set_globall2tp_list:
    - LOCALNAME: 'huawei'
      HELLOINTERVALSW: ENABLE
      HELLOINTERVAL: 60
      RETRYTIMES: 3
      PPPMAGICNUMBER: DISABLE
      MAXSENDWINSIZE: 64
      INITTUNNELNUM: 1
      MAXSESSIONNUM: 32767
    add_apn_list:
    - APN: 'apn-l2tp'
    set_apnl2tpattr_list:
    - APN: 'apn-l2tp'
      L2TPSWITCH: ENABLE
      SUPPORTIPV6: DISABLE
      RDSLNSMODE: REDUNDANCY
      ICRQ_CALLINGNO: MSISDN
      ICCN_AUTH: ENABLE
      IPCP_NEGO: ENABLE
      DOMAINNAMEACT: ADD_ENABLE_STRIP_DISABLE
      DOMAINNAMEPOS: PREFIX
      ICCN_LCPNEGO: ''
      ICCN_PGROUPID: ''
      ICCN_TXSPEED: ''
      ICRQ_BEARER: ''
      L2TPGROUPID: ''
    set_softparaofbit_list:
    - DT2: BYTE
      BYTENUM: 671
      BYTEPOSITION: 7
      BYTEVALUE: 1
      DWORDNUM: ''
      DWORDPOSITION: ''
      DWORDVALUE: ''
    add_logicinf_list:
    - NAME: 'giif1/0/1'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.20.2'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_l2tp'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_l2tprdsclient_list:
    - APN: 'apn-l2tp'
      INTERFACENAME: 'giif1/0/1'
    set_pppcfg_list:
    - HOSTNAME: 'UPF'
      MRU: 1500
      TIMEOUT: 3
    set_apnpppaccess_list:
    - APN: 'apn-l2tp'
      AUTHENTICATION: ENABLE
    set_l2tpn4key_list:
    - N4KEYVALUE: '*****'
      CFMN4KEYVALUE: '*****'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 配置L2TP的缺省参数。

```jinja2
{%- for item in set_globall2tp_list -%}
    SET GLOBALL2TP:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCALNAME is not none -%}
        LOCALNAME="{{item.LOCALNAME}}",
    {%- endif -%}
    {%- if item.HELLOINTERVALSW is not none -%}
        HELLOINTERVALSW={{item.HELLOINTERVALSW}},
    {%- endif -%}
    {%- if item.RETRYTIMES is not none -%}
        RETRYTIMES={{item.RETRYTIMES}},
    {%- endif -%}
    {%- if item.PPPMAGICNUMBER is not none -%}
        PPPMAGICNUMBER={{item.PPPMAGICNUMBER}},
    {%- endif -%}
    {%- if item.MAXSENDWINSIZE is not none -%}
        MAXSENDWINSIZE={{item.MAXSENDWINSIZE}},
    {%- endif -%}
    {%- if item.INITTUNNELNUM is not none -%}
        INITTUNNELNUM={{item.INITTUNNELNUM}},
    {%- endif -%}
    {%- if item.MAXSESSIONNUM is not none -%}
        MAXSESSIONNUM={{item.MAXSESSIONNUM}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HELLOINTERVALSW=ENABLE 时必选 --- -#}
    {%- if item.HELLOINTERVALSW == 'ENABLE' -%}
        HELLOINTERVAL={{item.HELLOINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 当PGW-C/SMF下发L2TP私有扩展信元，即PGW-C/SMF支持AAA鉴权，AAA在access accept消息中下发LNS信息时，PGW-U/UPF根据鉴权服务器返回的属性创建L2TP隧道。AAA返回的L2TP属性中不包含Client-Auth-ID（即LAC名称）属性场景，系统将使用本命令设置的缺省本端名称发起隧道连接；隧道创建后将使用本命令设置的缺省HELLO报文重发间隔发送HELLO报文以检测隧道的连通性。

### 4 使能L2TP。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnl2tpattr_list -%}
    SET APNL2TPATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    L2TPSWITCH={{item.L2TPSWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DOMAINNAMEACT=ADD_ENABLE_STRIP_DISABLE 时必选 --- -#}
    {%- if item.DOMAINNAMEACT == 'ADD_ENABLE_STRIP_DISABLE' -%}
        DOMAINNAMEPOS={{item.DOMAINNAMEPOS}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.SUPPORTIPV6 is not none -%}
            SUPPORTIPV6={{item.SUPPORTIPV6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICRQ_CALLINGNO is not none -%}
            ICRQ_CALLINGNO={{item.ICRQ_CALLINGNO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICCN_AUTH is not none -%}
            ICCN_AUTH={{item.ICCN_AUTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.IPCP_NEGO is not none -%}
            IPCP_NEGO={{item.IPCP_NEGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.DOMAINNAMEACT is not none -%}
            DOMAINNAMEACT={{item.DOMAINNAMEACT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICCN_LCPNEGO is not none -%}
            ICCN_LCPNEGO={{item.ICCN_LCPNEGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICCN_PGROUPID is not none -%}
            ICCN_PGROUPID={{item.ICCN_PGROUPID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICCN_TXSPEED is not none -%}
            ICCN_TXSPEED={{item.ICCN_TXSPEED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.ICRQ_BEARER is not none -%}
            ICRQ_BEARER={{item.ICRQ_BEARER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.L2TPGROUPID is not none -%}
            L2TPGROUPID={{item.L2TPGROUPID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：L2TPSWITCH=ENABLE 时可选 --- -#}
    {%- if item.L2TPSWITCH == 'ENABLE' -%}
        {%- if item.RDSLNSMODE is not none -%}
            RDSLNSMODE={{item.RDSLNSMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 通过**SET APNL2TPATTR**命令使能L2TP，并通过配置参数“RDSLNSMODE”指定RADIUS鉴权服务器返回多LNS时LNS的工作模式。

### 当配置“RDSLNSMODE”为“REDUNDANCY”，消息中携带的两个LNS的Tunnel-Preference取值相同，也作为主备方式。

### 当配置“RDSLNSMODE”为“TUNNEL\_PREFER”，消息中携带的两个LNS的Tunnel-Preference取值不同，则认为是主备方式。

### 当配置“RDSLNSMODE”为“TUNNEL\_PREFER”，并且消息中携带的多个LNS的Tunnel-Preference取值相同，则认为是负荷分担方式。

### 5 关闭快速流表功能，将Byte671的bit7设置为1。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT2={{item.DT2}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDPOSITION={{item.DWORDPOSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置Giif接口。

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

### 7 将APN绑定指定源端接口。

```jinja2
{%- for item in add_l2tprdsclient_list -%}
    ADD L2TPRDSCLIENT:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    INTERFACENAME="{{item.INTERFACENAME}}",
    ;
{%- endfor -%}
```

### 8 **可选：**配置系统进行PPP协商时所使用的参数。

```jinja2
{%- if is_optional_ppp_negotiation_params -%}
    {%- for item in set_pppcfg_list -%}
        SET PPPCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.HOSTNAME is not none -%}
            HOSTNAME="{{item.HOSTNAME}}",
        {%- endif -%}
        {%- if item.MRU is not none -%}
            MRU={{item.MRU}},
        {%- endif -%}
        {%- if item.TIMEOUT is not none -%}
            TIMEOUT={{item.TIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 **可选**：配置指定APN支持PPP鉴权功能。

```jinja2
{%- if is_optional_apn_ppp_auth -%}
    {%- for item in set_apnpppaccess_list -%}
        SET APNPPPACCESS:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        AUTHENTICATION={{item.AUTHENTICATION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 **可选**：配置L2TP业务加密功能，增强N4接口传输安全。

```jinja2
{%- if is_optional_l2tp_encryption -%}
    {%- for item in set_l2tpn4key_list -%}
        SET L2TPN4KEY:
        {#- --- 可选参数 --- -#}
        {%- if item.N4KEYVALUE is not none -%}
            N4KEYVALUE="{{item.N4KEYVALUE}}",
        {%- endif -%}
        {%- if item.CFMN4KEYVALUE is not none -%}
            CFMN4KEYVALUE="{{item.CFMN4KEYVALUE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 对端SMF需同时配置该功能，并且配置相同密钥，否则会导致L2TP业务失败。

