---
id: ''
name: 激活动态分流规则匹配（UPF）
ne_type: UEG
type: feature
description: 当运营商想要用户通过动态Traffic Rule、动态DNS Rule或者静态DNS Rule将数据业务分流到本地边缘APP时，需要执行以下操作，开启规则开关，支持对应规则的报文匹配。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC APP业务访问控制（公共）","动态分流（MPF/UPF）","配置动态分流","激活动态分流规则匹配（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商想要用户通过动态Traffic Rule、动态DNS Rule或者静态DNS Rule将数据业务分流到本地边缘APP时，需要执行以下操作，开启规则开关，支持对应规则的报文匹配。适用于UPF。

## 必备事项
前提条件

请仔细阅读动态分流规则匹配（UPF）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apptrafficpara_list:
      type: items
      properties:
        TRAFFICRULESW:
          name: '应用流量规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '当“规则来源”设置为“DYNAMIC\_TRAFFIC\_RULE”，表示使用动态Traffic Rule进行规则匹配，携带IP地址的数据报文命中动态Traffic Rule进行本地分流。此时，DNS Rule衍生的基于目的IP地址本地分流功能不生效。  当“规则来源”设置为“DNS\_RULE\_EXTENDED”，表示使用DNS Rule衍生的IP地址匹配，携带IP地址的数据报文命中DNS Rule的IP地址进行本地分流。此时，动态Traffic Rule不生效。  说明：  基于动态Traffic Rule的分流功能和DNS Rule衍生的基于目的IP的本地分流功能不能同时生效，默认配置为“DYNAMIC\_TRAFFIC\_RULE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULESOURCE:
          name: '规则来源'
          type: string
          enum:
          - DNS_RULE_EXTENDED
          - DYNAMIC_TRAFFIC_RULE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_dnslitepara_list:
      type: items
      properties:
        DNSLMATCHSW:
          name: '轻量DNS规则匹配开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，表示开启DNS Rule开关，支持DNS Rule匹配功能。动态DNS Rule和静态DNS Rule均支持。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSLPOLICYSW:
          name: '轻量DNS策略执行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，如果DNS Rule匹配成功，则支持UE发起DNS查询并响应。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apptrafficpara_list_1:
      type: items
      properties:
        TRAFFICRULESW:
          name: '应用流量规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '当“规则来源”设置为“DYNAMIC\_TRAFFIC\_RULE”，表示使用动态Traffic Rule进行规则匹配，携带IP地址的数据报文命中动态Traffic Rule进行本地分流。此时，DNS Rule衍生的基于目的IP地址本地分流功能不生效。  当“规则来源”设置为“DNS\_RULE\_EXTENDED”，表示使用DNS Rule衍生的IP地址匹配，携带IP地址的数据报文命中DNS Rule的IP地址进行本地分流。此时，动态Traffic Rule不生效。  说明：  基于动态Traffic Rule的分流功能和DNS Rule衍生的基于目的IP的本地分流功能不能同时生效，默认配置为“DYNAMIC\_TRAFFIC\_RULE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULESOURCE:
          name: '规则来源'
          type: string
          enum:
          - DNS_RULE_EXTENDED
          - DYNAMIC_TRAFFIC_RULE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_dnslitepara_list_1:
      type: items
      properties:
        DNSLMATCHSW:
          name: '轻量DNS规则匹配开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，表示开启DNS Rule开关，支持DNS Rule匹配功能。动态DNS Rule和静态DNS Rule均支持。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSLPOLICYSW:
          name: '轻量DNS策略执行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '本参数配置为“ENABLE”后，如果DNS Rule匹配成功，则支持UE发起DNS查询并响应。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSRULESTATSW:
          name: 'DNS规则状态控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数仅对静态DNS Rule生效，即静态DNS规则是否通过命令控制。   * 本参数配置为“ENABLE”后，则支持由命令控制静态DNS Rule的激活状态，MPF初次会将DNS Rule置为去激活状态，后续通过**ACT DNSRULE**命令激活状态、**DEA DNSRULE**命令去激活状态。 * 本参数配置为DISABLE后，则静态DNS Rule为激活状态，状态不会改变。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dnsrule_list:
      type: items
      properties:
        APPLICATIONID:
          name: '应用标识'
          type: string
          maxLength: 63
          required: true
          description: '与对端SMF协商一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DNSRULENAME:
          name: 'DNS规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'UPF本地配置的静态DNS Rule。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAIN:
          name: '域名'
          type: string
          maxLength: 63
          required: true
          description: 'APP域名。'
          data_source: '与对端协商'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'APP的IP地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DNSTTL:
          name: 'DNS TTL'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 86400
    set_apptrafficpara_list_2:
      type: items
      properties:
        TRAFFICRULESW:
          name: '应用流量规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '当“规则来源”设置为“DYNAMIC\_TRAFFIC\_RULE”，表示使用动态Traffic Rule进行规则匹配，携带IP地址的数据报文命中动态Traffic Rule进行本地分流。此时，DNS Rule衍生的基于目的IP地址本地分流功能不生效。  当“规则来源”设置为“DNS\_RULE\_EXTENDED”，表示使用DNS Rule衍生的IP地址匹配，携带IP地址的数据报文命中DNS Rule的IP地址进行本地分流。此时，动态Traffic Rule不生效。  说明：  基于动态Traffic Rule的分流功能和DNS Rule衍生的基于目的IP的本地分流功能不能同时生效，默认配置为“DYNAMIC\_TRAFFIC\_RULE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULESOURCE:
          name: '规则来源'
          type: string
          enum:
          - DNS_RULE_EXTENDED
          - DYNAMIC_TRAFFIC_RULE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_apptrafficpara_list:
    - TRAFFICRULESW: ENABLE
      RULESOURCE: DYNAMIC_TRAFFIC_RULE
    set_dnslitepara_list:
    - DNSLMATCHSW: ENABLE
      DNSLPOLICYSW: ENABLE
    set_apptrafficpara_list_1:
    - TRAFFICRULESW: ENABLE
      RULESOURCE: DYNAMIC_TRAFFIC_RULE
    set_dnslitepara_list_1:
    - DNSLMATCHSW: ENABLE
      DNSLPOLICYSW: ENABLE
      DNSRULESTATSW: DISABLE
    add_dnsrule_list:
    - APPLICATIONID: 'app3'
      DNSRULENAME: 'rule3'
      DOMAIN: 'example.com'
      IPVERSION: IPV4
      IPV4ADDRESS: '10.1.1.1'
      DNSTTL: 3
    set_apptrafficpara_list_2:
    - TRAFFICRULESW: ENABLE
      RULESOURCE: DYNAMIC_TRAFFIC_RULE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置使用动态Traffic Rule进行业务匹配

```jinja2
{%- if is_scenario_dynamic_traffic_rule -%}
    {%- for item in set_apptrafficpara_list -%}
        SET APPTRAFFICPARA:
        {#- --- 必选参数 --- -#}
        TRAFFICRULESW={{item.TRAFFICRULESW}},
        {#- --- 可选参数 --- -#}
        {%- if item.RULESOURCE is not none -%}
            RULESOURCE={{item.RULESOURCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置使用动态DNS Rule进行业务匹配。

```jinja2
{%- if is_scenario_dynamic_dns_rule -%}
    {%- for item in set_dnslitepara_list -%}
        SET DNSLITEPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.DNSLMATCHSW is not none -%}
            DNSLMATCHSW={{item.DNSLMATCHSW}},
        {%- endif -%}
        {%- if item.DNSLPOLICYSW is not none -%}
            DNSLPOLICYSW={{item.DNSLPOLICYSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_dynamic_dns_rule -%}
    {%- for item in set_apptrafficpara_list_1 -%}
        SET APPTRAFFICPARA:
        {#- --- 必选参数 --- -#}
        TRAFFICRULESW={{item.TRAFFICRULESW}},
        {#- --- 可选参数 --- -#}
        {%- if item.RULESOURCE is not none -%}
            RULESOURCE={{item.RULESOURCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置使用静态DNS Rule进行业务匹配。

```jinja2
{%- if is_scenario_static_dns_rule -%}
    {%- for item in set_dnslitepara_list_1 -%}
        SET DNSLITEPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.DNSLMATCHSW is not none -%}
            DNSLMATCHSW={{item.DNSLMATCHSW}},
        {%- endif -%}
        {%- if item.DNSLPOLICYSW is not none -%}
            DNSLPOLICYSW={{item.DNSLPOLICYSW}},
        {%- endif -%}
        {%- if item.DNSRULESTATSW is not none -%}
            DNSRULESTATSW={{item.DNSRULESTATSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_dns_rule -%}
    {%- for item in add_dnsrule_list -%}
        ADD DNSRULE:
        {#- --- 必选参数 --- -#}
        APPLICATIONID="{{item.APPLICATIONID}}",
        DNSRULENAME="{{item.DNSRULENAME}}",
        DOMAIN="{{item.DOMAIN}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.DNSTTL is not none -%}
            DNSTTL={{item.DNSTTL}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_dns_rule -%}
    {%- for item in set_apptrafficpara_list_2 -%}
        SET APPTRAFFICPARA:
        {#- --- 必选参数 --- -#}
        TRAFFICRULESW={{item.TRAFFICRULESW}},
        {#- --- 可选参数 --- -#}
        {%- if item.RULESOURCE is not none -%}
            RULESOURCE={{item.RULESOURCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

