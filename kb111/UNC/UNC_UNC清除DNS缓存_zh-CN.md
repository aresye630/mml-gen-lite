---
id: ''
name: UNC清除DNS缓存
ne_type: UNC
type: feature
description: DNS缓存（DNS Cache）是指使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。无线割接、应急执行等场景下，会涉及清除DNS缓存。  清除DNS缓存会导致系统的CPU负荷增大，系统向DNS服务的查询次数可能会增加。
risk_level: ''
doc_source: ["网络运维","日常维护","UNC基础运维操作","UNC清除DNS缓存"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
DNS缓存（DNS Cache）是指使用DNS服务器解析时查找到的域名和IP地址信息在系统中的缓存，用于快速解析域名。无线割接、应急执行等场景下，会涉及清除DNS缓存。清除DNS缓存会导致系统的CPU负荷增大，系统向DNS服务的查询次数可能会增加。

## 必备事项
前提条件

已登录OM Portal。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    clr_dnsc_list:
      type: items
      properties:
        CACHETYPE:
          name: 'Cache类型'
          type: string
          enum:
          - ALL
          - L1CACHE
          - L2CACHE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        SERVICETYPE:
          name: '服务名称'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSQUERYMODE:
          name: 'DNS查询方式'
          type: string
          enum:
          - AAAA/A
          - NAPTR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROCESSNO:
          name: '进程号'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    clr_ngdnscache_list:
      type: items
      properties:
        QUERYTYPE:
          name: 'DNS查询类型'
          type: string
          enum:
          - QUERY_TYPE_A
          - QUERY_TYPE_NAPTR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLEARMANNER:
          name: '清除方式'
          type: string
          enum:
          - All
          - BYDOMAINNAME
          - SUBSTRMATCH
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAINNAME:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    clr_dnsc_list_1:
      type: items
      properties:
        CACHETYPE:
          name: 'Cache类型'
          type: string
          enum:
          - ALL
          - L1CACHE
          - L2CACHE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        SERVICETYPE:
          name: '服务名称'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSQUERYMODE:
          name: 'DNS查询方式'
          type: string
          enum:
          - AAAA/A
          - NAPTR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROCESSNO:
          name: '进程号'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    clr_dnsc_list_2:
      type: items
      properties:
        CACHETYPE:
          name: 'Cache类型'
          type: string
          enum:
          - ALL
          - L1CACHE
          - L2CACHE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        SERVICETYPE:
          name: '服务名称'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSQUERYMODE:
          name: 'DNS查询方式'
          type: string
          enum:
          - AAAA/A
          - NAPTR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROCESSNO:
          name: '进程号'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    clr_ngdnscache_list_1:
      type: items
      properties:
        QUERYTYPE:
          name: 'DNS查询类型'
          type: string
          enum:
          - QUERY_TYPE_A
          - QUERY_TYPE_NAPTR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLEARMANNER:
          name: '清除方式'
          type: string
          enum:
          - All
          - BYDOMAINNAME
          - SUBSTRMATCH
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAINNAME:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    clr_dnsc_list:
    - CACHETYPE: L2CACHE
      SERVICETYPE: 'LINK_VNFC'
      DNSQUERYMODE: ''
      PROCESSNO: ''
    clr_ngdnscache_list:
    - QUERYTYPE: QUERY_TYPE_NAPTR
      CLEARMANNER: All
      DOMAINNAME: ''
    clr_dnsc_list_1:
    - CACHETYPE: ALL
      SERVICETYPE: 'LINK_VNFC'
      DNSQUERYMODE: ''
      PROCESSNO: ''
    clr_dnsc_list_2:
    - CACHETYPE: ALL
      SERVICETYPE: 'LINK_VNFC'
      DNSQUERYMODE: ''
      PROCESSNO: ''
    clr_ngdnscache_list_1:
    - QUERYTYPE: QUERY_TYPE_NAPTR
      CLEARMANNER: All
      DOMAINNAME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //清AMF侧DNS缓存使服务器记录生效。

```jinja2
{%- if is_scenario_amf -%}
    {%- for item in clr_dnsc_list -%}
        CLR DNSC:
        {#- --- 必选参数 --- -#}
        SERVICETYPE="{{item.SERVICETYPE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CACHETYPE is not none -%}
            CACHETYPE={{item.CACHETYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.DNSQUERYMODE is not none -%}
                DNSQUERYMODE={{item.DNSQUERYMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.PROCESSNO is not none -%}
                PROCESSNO={{item.PROCESSNO}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_amf -%}
    {%- for item in clr_ngdnscache_list -%}
        CLR NGDNSCACHE:
        {#- --- 必选参数 --- -#}
        QUERYTYPE={{item.QUERYTYPE}},
        CLEARMANNER={{item.CLEARMANNER}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CLEARMANNER=BYDOMAINNAME/SUBSTRMATCH 时必选 --- -#}
        {%- if item.CLEARMANNER in ['BYDOMAINNAME', 'SUBSTRMATCH'] -%}
            DOMAINNAME="{{item.DOMAINNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 //清MME&SGSN侧DNS缓存使服务器记录生效。

```jinja2
{%- if is_scenario_mme_sgsn -%}
    {%- for item in clr_dnsc_list_1 -%}
        CLR DNSC:
        {#- --- 必选参数 --- -#}
        SERVICETYPE="{{item.SERVICETYPE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CACHETYPE is not none -%}
            CACHETYPE={{item.CACHETYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.DNSQUERYMODE is not none -%}
                DNSQUERYMODE={{item.DNSQUERYMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.PROCESSNO is not none -%}
                PROCESSNO={{item.PROCESSNO}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 //清AMF&MME&SGSN侧DNS缓存使服务器记录生效。

```jinja2
{%- if is_scenario_amf_mme_sgsn -%}
    {%- for item in clr_dnsc_list_2 -%}
        CLR DNSC:
        {#- --- 必选参数 --- -#}
        SERVICETYPE="{{item.SERVICETYPE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CACHETYPE is not none -%}
            CACHETYPE={{item.CACHETYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.DNSQUERYMODE is not none -%}
                DNSQUERYMODE={{item.DNSQUERYMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CACHETYPE=L1CACHE 时可选 --- -#}
        {%- if item.CACHETYPE == 'L1CACHE' -%}
            {%- if item.PROCESSNO is not none -%}
                PROCESSNO={{item.PROCESSNO}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_amf_mme_sgsn -%}
    {%- for item in clr_ngdnscache_list_1 -%}
        CLR NGDNSCACHE:
        {#- --- 必选参数 --- -#}
        QUERYTYPE={{item.QUERYTYPE}},
        CLEARMANNER={{item.CLEARMANNER}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CLEARMANNER=BYDOMAINNAME/SUBSTRMATCH 时必选 --- -#}
        {%- if item.CLEARMANNER in ['BYDOMAINNAME', 'SUBSTRMATCH'] -%}
            DOMAINNAME="{{item.DOMAINNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

