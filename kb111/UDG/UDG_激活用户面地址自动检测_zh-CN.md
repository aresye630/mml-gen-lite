---
id: GWFD-010108
name: 激活用户面地址自动检测
ne_type: UDG
type: feature
description: 运营商规划使用用户面分配地址，在进行业务调测、版本升级、地址扩容或有用户业务访问异常投诉时，需要检查UDG到PDN/DN侧服务器之间的路由连通性，可激活本特性。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010108 用户面地址自动检测","激活用户面地址自动检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商规划使用用户面分配地址，在进行业务调测、版本升级、地址扩容或有用户业务访问异常投诉时，需要检查UDG到PDN/DN侧服务器之间的路由连通性，可激活本特性。适用于PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-010108 用户面地址自动检测。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pdnroutetstpath_list:
      type: items
      properties:
        PATHNAME:
          name: '路径名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定用于连通性探测的路径名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PATHTYPE:
          name: '路径类型'
          type: string
          enum:
          - DNS
          required: true
          description: '用于指定路径类型。'
          data_source: '本端规划'
          pattern: ''
          default: DNS
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '地址池的名称。'
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
          description: '指定IP地址类型，枚举取值：   * IPV4：IPv4地址类型。 * IPV6：IPv6地址类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSTIPV4ADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '在“IPVERSION”配置为“IPV4”时，指定探测目的PDN Server的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TESTMETHOD:
          name: '路由探测方式'
          type: string
          enum:
          - DNS
          - PING
          - TRACERT
          required: false
          description: '指定探测方式。枚举取值：   * PING：PING探测方式。 * DNS：DNS探测方式。 * TRACERT：TRACERT探测方式。'
          data_source: '全网规划'
          pattern: ''
          default: PING
        DSCPV:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6PREFIX:
          name: '目的IPv6前缀地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCV:
          name: 'Traffic-Class值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LENGTH:
          name: '报文净荷长度'
          type: integer
          minimum: 20
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    str_pdnroutetst_list:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOL**命令进行查询。'
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
        DSTIPV4ADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '探测目的IP地址是PDN/DN侧的目的服务器IP地址。对于DNS探测方式，探测目的IP地址必须是DNS Server IP地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        TESTMETHOD:
          name: '探测方式'
          type: string
          enum:
          - DNS
          - PING
          - TRACERT
          required: false
          description: 'UDG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
          data_source: '本端规划'
          pattern: ''
          default: PING
        WHOLEDETECT:
          name: '全量探测'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于指定是否启动全量探测。Tracert探测方式不支持全量探测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: '* 该参数在“WHOLEDETECT”配置为“ENABLE”时为可选参数。 * 通过**ADD SECTION** 命令配置的地址段号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UDG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UDG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于指定DNS探测方式下的域名。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSCPV:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6PREFIX:
          name: '目的IPv6前缀地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPV6PREFIX:
          name: '源IPv6前缀地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCV:
          name: 'Traffic-Class值'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LENGTH:
          name: '报文净荷长度'
          type: integer
          minimum: 20
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
  examples:
    add_pdnroutetstpath_list:
    - PATHNAME: 'test'
      PATHTYPE: DNS
      IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: PING
      DSCPV: ''
      DSTIPV6PREFIX: ''
      TCV: ''
      DOMAINVALUE: ''
      LENGTH: 100
    str_pdnroutetst_list:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: PING
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
      SRCIPV4ADDR: '10.10.1.1'
      DOMAINVALUE: 'www.example.com'
      DSCPV: ''
      DSTIPV6PREFIX: ''
      SRCIPV6PREFIX: ''
      TCV: ''
      LENGTH: 100
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加网元向服务器发送探测消息的探测路径。

```jinja2
{%- for item in add_pdnroutetstpath_list -%}
    ADD PDNROUTETSTPATH:
    {#- --- 必选参数 --- -#}
    PATHNAME="{{item.PATHNAME}}",
    PATHTYPE={{item.PATHTYPE}},
    IPPOOL="{{item.IPPOOL}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.TESTMETHOD is not none -%}
        TESTMETHOD={{item.TESTMETHOD}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        DSTIPV4ADDR="{{item.DSTIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        DSTIPV6PREFIX="{{item.DSTIPV6PREFIX}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
    {%- if item.TESTMETHOD == 'DNS' -%}
        {%- if item.DOMAINVALUE is not none -%}
            DOMAINVALUE="{{item.DOMAINVALUE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.DSCPV is not none -%}
            DSCPV={{item.DSCPV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TESTMETHOD=PING 时可选 --- -#}
    {%- if item.TESTMETHOD == 'PING' -%}
        {%- if item.LENGTH is not none -%}
            LENGTH={{item.LENGTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.TCV is not none -%}
            TCV={{item.TCV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 启动PDN/DN侧路由探测功能。

```jinja2
{%- for item in str_pdnroutetst_list -%}
    STR PDNROUTETST:
    {#- --- 必选参数 --- -#}
    IPPOOL="{{item.IPPOOL}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.TESTMETHOD is not none -%}
        TESTMETHOD={{item.TESTMETHOD}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        DSTIPV4ADDR="{{item.DSTIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        DSTIPV6PREFIX="{{item.DSTIPV6PREFIX}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TESTMETHOD=DNS/PING 时可选 --- -#}
    {%- if item.TESTMETHOD in ['DNS', 'PING'] -%}
        {%- if item.WHOLEDETECT is not none -%}
            WHOLEDETECT={{item.WHOLEDETECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：WHOLEDETECT=ENABLE 时可选 --- -#}
    {%- if item.WHOLEDETECT == 'ENABLE' -%}
        {%- if item.SECTIONNUM is not none -%}
            SECTIONNUM={{item.SECTIONNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.SRCIPV4ADDR is not none -%}
            SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
    {%- if item.TESTMETHOD == 'DNS' -%}
        {%- if item.DOMAINVALUE is not none -%}
            DOMAINVALUE="{{item.DOMAINVALUE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.DSCPV is not none -%}
            DSCPV={{item.DSCPV}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TESTMETHOD=PING 时可选 --- -#}
    {%- if item.TESTMETHOD == 'PING' -%}
        {%- if item.LENGTH is not none -%}
            LENGTH={{item.LENGTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.SRCIPV6PREFIX is not none -%}
            SRCIPV6PREFIX="{{item.SRCIPV6PREFIX}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.TCV is not none -%}
            TCV={{item.TCV}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 在同一时间，只能执行一个探测命令，如果同时执行多个探测命令，后边执行的探测会失败。

### 同一时间只支持一个APN下的探测，未完成当前探测时，不允许再执行命令下发探测任务。

### 当出现误操作或者异常情况下路由探测时间过长，可执行**STP PDNROUTETST**强制终止路由探测。

### 建议使用UDG地址池中的空闲IP地址作为探测源进行探测，如果被探测路由网段中的IP地址都被占用时，执行此命令可能会导致极少数（几个或者几十个）在线用户被去激活，请谨慎使用。

### TRACERT探测方式，在没有回全部探测响应的场景下，大概需要450秒左右才会返回探测的结果。

### 建议设备空载环境使用。

### 全量探测时，探测时长会成倍增加，此时探测任务最多探测5分钟；如果有未探测到的子段可以使用指定section的全量探测。

### 3 查询PDN/DN侧路由探测结果。

