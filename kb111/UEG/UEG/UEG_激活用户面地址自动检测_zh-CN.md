---
id: GWFD-020808
name: 激活用户面地址自动检测
ne_type: UEG
type: feature
description: 运营商规划使用用户面分配地址，在进行业务调测、版本升级、地址扩容或有用户业务访问异常投诉时，需要检查UEG到PDN/DN侧服务器之间的路由连通性，可激活本特性。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-020800 基本业务","GWFD-020808 用户面地址自动检测","激活用户面地址自动检测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商规划使用用户面分配地址，在进行业务调测、版本升级、地址扩容或有用户业务访问异常投诉时，需要检查UEG到PDN/DN侧服务器之间的路由连通性，可激活本特性。适用于PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-020808 用户面地址自动检测。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    str_pdnroutetst_list:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
          description: 'UEG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
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
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UEG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UEG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
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
    str_pdnroutetst_list_1:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UEG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UEG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
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
          description: 'UEG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
          data_source: '本端规划'
          pattern: ''
          default: PING
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
    str_pdnroutetst_list_2:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
          description: 'UEG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
          data_source: '本端规划'
          pattern: ''
          default: PING
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
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UEG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UEG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    str_pdnroutetst_list_3:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
          description: 'UEG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
          data_source: '本端规划'
          pattern: ''
          default: PING
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
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UEG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UEG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    str_pdnroutetst_list_4:
      type: items
      properties:
        IPPOOL:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
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
          description: 'UEG支持三种探测方式：   * PING探测方式 * DNS探测方式 * Tracert探测方式   默认使用PING的探测方式，当网络中存在防火墙禁止PING报文的情况时，可以选择DNS探测方式。  如果网络中出现故障，可以进一步使用Tracert探测方式，查看网络中出现故障的位置，为故障诊断提供依据。'
          data_source: '本端规划'
          pattern: ''
          default: PING
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '* 如果配置了该参数，地址池探测的时候源IP使用本参数。该参数建议是空闲IP地址，如果已经是在线用户IP，执行命令会导致在线的用户被去激活。 * 如果没有配置该参数，对于PING探测或者DNS探测，UEG从每一个路由网段内随机选取一个IP作为探测源IP；对于Tracert探测方式，由于探测时间稍长，UEG随机选取一个地址网段的IP作为探测源IP，不遍历所有的地址网段。'
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
  examples:
    add_pdnroutetstpath_list:
    - PATHNAME: 'test'
      PATHTYPE: DNS
      IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: PING
    str_pdnroutetst_list:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: PING
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
      SRCIPV4ADDR: '10.10.1.1'
      DOMAINVALUE: 'www.example.com'
    str_pdnroutetst_list_1:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      SRCIPV4ADDR: '10.10.1.1'
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: PING
      DOMAINVALUE: 'www.example.com'
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
    str_pdnroutetst_list_2:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: DNS
      DOMAINVALUE: 'www.example.com'
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
      SRCIPV4ADDR: '10.10.1.1'
    str_pdnroutetst_list_3:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: DNS
      DOMAINVALUE: 'www.example.com'
      SRCIPV4ADDR: '10.10.1.1'
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
    str_pdnroutetst_list_4:
    - IPPOOL: 'testpool'
      IPVERSION: IPV4
      DSTIPV4ADDR: '10.1.1.1'
      TESTMETHOD: TRACERT
      SRCIPV4ADDR: '10.10.1.1'
      DOMAINVALUE: 'www.example.com'
      WHOLEDETECT: ENABLE
      SECTIONNUM: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 增加网元项服务器发送探测小西点探测路径。

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
    ;
{%- endfor -%}
```

### 2 启动PDN/DN侧路由探测功能。

#### 2.1 任务一：以PING探测方式启动PDN/DN侧路由探测功能。

##### 2.1.1 //全量探测。

```jinja2
{%- if is_scenario_ping_probe -%}
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
        {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
        {%- if item.TESTMETHOD == 'DNS' -%}
            {%- if item.DOMAINVALUE is not none -%}
                DOMAINVALUE="{{item.DOMAINVALUE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.SRCIPV4ADDR is not none -%}
                SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.1.2 //非全量探测。

```jinja2
{%- if is_scenario_ping_probe -%}
    {%- for item in str_pdnroutetst_list_1 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.SRCIPV4ADDR is not none -%}
                SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：WHOLEDETECT=ENABLE 时可选 --- -#}
        {%- if item.WHOLEDETECT == 'ENABLE' -%}
            {%- if item.SECTIONNUM is not none -%}
                SECTIONNUM={{item.SECTIONNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
        {%- if item.TESTMETHOD == 'DNS' -%}
            {%- if item.DOMAINVALUE is not none -%}
                DOMAINVALUE="{{item.DOMAINVALUE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TESTMETHOD=DNS/PING 时可选 --- -#}
        {%- if item.TESTMETHOD in ['DNS', 'PING'] -%}
            {%- if item.WHOLEDETECT is not none -%}
                WHOLEDETECT={{item.WHOLEDETECT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 任务二：以DNS探测方式启动PDN/DN侧路由探测功能。

##### 2.2.1 //全量探测。

```jinja2
{%- if is_scenario_dns_probe -%}
    {%- for item in str_pdnroutetst_list_2 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
        {%- if item.TESTMETHOD == 'DNS' -%}
            {%- if item.DOMAINVALUE is not none -%}
                DOMAINVALUE="{{item.DOMAINVALUE}}",
            {%- endif -%}
        {%- endif -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 //非全量探测。

```jinja2
{%- if is_scenario_dns_probe -%}
    {%- for item in str_pdnroutetst_list_3 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
        {%- if item.TESTMETHOD == 'DNS' -%}
            {%- if item.DOMAINVALUE is not none -%}
                DOMAINVALUE="{{item.DOMAINVALUE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：WHOLEDETECT=ENABLE 时可选 --- -#}
        {%- if item.WHOLEDETECT == 'ENABLE' -%}
            {%- if item.SECTIONNUM is not none -%}
                SECTIONNUM={{item.SECTIONNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TESTMETHOD=DNS/PING 时可选 --- -#}
        {%- if item.TESTMETHOD in ['DNS', 'PING'] -%}
            {%- if item.WHOLEDETECT is not none -%}
                WHOLEDETECT={{item.WHOLEDETECT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.SRCIPV4ADDR is not none -%}
                SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 任务三：以Tracert探测方式启动PDN/DN侧路由探测功能。Tracert探测方式不支持全量探测。

```jinja2
{%- if is_scenario_tracert_probe -%}
    {%- for item in str_pdnroutetst_list_4 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：WHOLEDETECT=ENABLE 时可选 --- -#}
        {%- if item.WHOLEDETECT == 'ENABLE' -%}
            {%- if item.SECTIONNUM is not none -%}
                SECTIONNUM={{item.SECTIONNUM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TESTMETHOD=DNS 时可选 --- -#}
        {%- if item.TESTMETHOD == 'DNS' -%}
            {%- if item.DOMAINVALUE is not none -%}
                DOMAINVALUE="{{item.DOMAINVALUE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：TESTMETHOD=DNS/PING 时可选 --- -#}
        {%- if item.TESTMETHOD in ['DNS', 'PING'] -%}
            {%- if item.WHOLEDETECT is not none -%}
                WHOLEDETECT={{item.WHOLEDETECT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            {%- if item.SRCIPV4ADDR is not none -%}
                SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 在同一时间，只能执行一个探测命令，如果同时执行多个探测命令，后边执行的探测会失败。

### 同一时间只支持一个APN下的探测，未完成当前探测时，不允许再执行命令下发探测任务。

### 当出现误操作或者异常情况下路由探测时间过长，可执行**STP PDNROUTETST**强制终止路由探测。

### 建议使用UEG地址池中的空闲IP地址作为探测源进行探测，如果被探测路由网段中的IP地址都被占用时，执行此命令可能会导致极少数（几个或者几十个）在线用户被去激活，请谨慎使用。

### TRACERT探测方式，在没有回全部探测响应的场景下，大概需要450秒左右才会返回探测的结果。

### 建议设备空载环境使用。

### 全量探测时，探测时长会成倍增加，此时探测任务最多探测5分钟；如果有未探测到的子段可以使用指定section的全量探测。

### 3 查询PDN/DN侧路由探测结果。

#### 3.1 //所有的探测结果，包括探测成功的结果和探测失败的结果。

#### 3.2 //所有探测成功的结果。

