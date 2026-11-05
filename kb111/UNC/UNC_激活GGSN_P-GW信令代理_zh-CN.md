---
id: ''
name: 激活GGSN/P-GW信令代理
ne_type: UNC
type: feature
description: 当运营商需要GGSN/P-GW承担Proxy的作用，将漫游用户的激活上下文请求消息路由到归属地的GGSN/P-GW，由归属地GGSN/P-GW直接处理漫游用户的激活请求以及随后的各种业务时，需要配置GGSN/P-GW信令代理特性。  适用于GGSN、PGW-C
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-205107 GGSN/P-GW信令代理","激活GGSN/P-GW信令代理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要GGSN/P-GW承担Proxy的作用，将漫游用户的激活上下文请求消息路由到归属地的GGSN/P-GW，由归属地GGSN/P-GW直接处理漫游用户的激活请求以及随后的各种业务时，需要配置GGSN/P-GW信令代理特性。适用于GGSN、PGW-C

## 必备事项
前提条件

* 请仔细阅读WSFD-205107 GGSN/P-GW信令代理。
* Proxy GGSN/P-GW与归属地GGSN/P-GW之间的路由可用。
* 获取要进行信令代理的APN、IMSI/MSISDN号段规划或计费属性和归属地GGSN/P-GW的IP地址。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
    add_apngwproxyfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '基于APN控制是否打开Proxy功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROXYSW:
          name: '网关Proxy开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN实例名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'APN实例名称'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
    set_gwproxyfunc_list:
      type: items
      properties:
        PROXYSW:
          name: 'Proxy功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '网关Proxy功能'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_primsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: 'IMSI/MSISDN号码段信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - MSISDN
          - IMSIWILDCARD
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          minLength: 0
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_primsimsisdng_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号段组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: 'IMSI/MSISDN号段组信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_homegroup_list:
      type: items
      properties:
        HOMEGROUPINDX:
          name: 'home group的编号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: 'HomeGroup信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIMSISDNGRPNM:
          name: 'home group绑定的用户号码段组名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCGROUPNAME:
          name: 'home group绑定的计费属性组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ccgroup_list:
      type: items
      properties:
        CCGROUPNAME:
          name: '计费属性组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '计费属性组信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ccvalue_list:
      type: items
      properties:
        CCGROUPNAME:
          name: '计费特征组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          minLength: 1
          maxLength: 6
          required: true
          description: '计费属性值信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_homegroup_list:
      type: items
      properties:
        HOMEGROUPINDX:
          name: 'home group的编号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: 'HomeGroup信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIMSISDNGRPNM:
          name: 'home group绑定的用户号码段组名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCGROUPNAME:
          name: 'home group绑定的计费属性组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCGROUPSW:
          name: '选择计费属性组'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSISDNSW:
          name: '选择IMSI/MSISDN组开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_homeip_list:
      type: items
      properties:
        HOMEGROUPINDX:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: 'Home GGSN/P-GW IP地址信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOMEIPID:
          name: 'home-ip的编号'
          type: integer
          minimum: 1
          maximum: 10
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOMEIPV4:
          name: 'Home IPv4'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEIPV6:
          name: 'Home IPv6'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRODUCTTYPE:
          name: '产品类型'
          type: string
          enum:
          - PGW
          - GGSN
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: PGW
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_homegrpbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN实例名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '将home-group绑定到指定的APN'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        HOMEGROUPINDX:
          name: 'Home group的编号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9GPSP11'
      SWITCH: ENABLE
    add_apngwproxyfunc_list:
    - APN: 'apn-test'
      PROXYSW: ENABLE
    add_apn_list:
    - APN: 'apn-test'
    set_gwproxyfunc_list:
    - PROXYSW: ENABLE
    add_primsimsisdnseg_list:
    - SEGMENTNAME: 'msisdn-test'
      SEGMENTTYPE: MSISDN
      SEGSTART: '138'
      SEGEND: '139'
      WILDCARDSEG: ''
    add_primsimsisdng_list:
    - SEGGROUPNAME: 'group-test'
      SEGMENTNAME: 'msisdn-test'
    add_homegroup_list:
    - HOMEGROUPINDX: 1
      IMSIMSISDNGRPNM: 'group-test'
      CCGROUPNAME: 'cc_group1'
    add_ccgroup_list:
    - CCGROUPNAME: 'cc_group1'
    add_ccvalue_list:
    - CCGROUPNAME: '计费属性组名称'
      CCVALUE: '0x0010'
    mod_homegroup_list:
    - HOMEGROUPINDX: 1
      IMSIMSISDNGRPNM: 'group-test'
      CCGROUPNAME: 'cc_group1'
      CCGROUPSW: ''
      IMSIMSISDNSW: ''
    add_homeip_list:
    - HOMEGROUPINDX: 1
      HOMEIPID: 1
      HOMEIPV4: 192.168.1.1
      HOMEIPV6: fc01:1111:2222:3333:ff:ff:ff:ff
      PRODUCTTYPE: pgw
      IPVERSION: IPV4
    add_homegrpbindapn_list:
    - APN: 'apn-test'
      HOMEGROUPINDX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 以下命令在“MML命令行 - UNC”窗口上执行。打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 如需开启指定APN的Proxy 功能，配置基于APN控制是否打开网关Proxy功能。**ADD APNGWPROXYFUNC**:APN=APN，PROXYSW=基于APN控制的网关Proxy开关； 如果未配置本步骤，则会使用全局控制是否打开网关Proxy功能。

```jinja2
{%- for item in add_apngwproxyfunc_list -%}
    ADD APNGWPROXYFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PROXYSW is not none -%}
        PROXYSW={{item.PROXYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 如需开启所有APN的Proxy 功能，配置基于全局控制是否打开网关Proxy功能。

```jinja2
{%- for item in set_gwproxyfunc_list -%}
    SET GWPROXYFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.PROXYSW is not none -%}
        PROXYSW={{item.PROXYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**配置将要对其进行信令代理操作IMSI/MSISDN号码段和号码段组。

#### 4.1 配置IMSI/MSISDN号码段。

```jinja2
{%- if is_optional_imsi_msisdn_segment_group -%}
    {%- for item in add_primsimsisdnseg_list -%}
        ADD PRIMSIMSISDNSEG:
        {#- --- 必选参数 --- -#}
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        SEGMENTTYPE={{item.SEGMENTTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGSTART="{{item.SEGSTART}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
            SEGEND="{{item.SEGEND}}",
        {%- endif -%}
        {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
            WILDCARDSEG="{{item.WILDCARDSEG}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置IMSI/MSISDN号码段组。

```jinja2
{%- if is_optional_imsi_msisdn_segment_group -%}
    {%- for item in add_primsimsisdng_list -%}
        ADD PRIMSIMSISDNG:
        {#- --- 必选参数 --- -#}
        SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置Home group。

```jinja2
{%- if is_optional_imsi_msisdn_segment_group -%}
    {%- for item in add_homegroup_list -%}
        ADD HOMEGROUP:
        {#- --- 必选参数 --- -#}
        HOMEGROUPINDX={{item.HOMEGROUPINDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.IMSIMSISDNGRPNM is not none -%}
            IMSIMSISDNGRPNM="{{item.IMSIMSISDNGRPNM}}",
        {%- endif -%}
        {%- if item.CCGROUPNAME is not none -%}
            CCGROUPNAME="{{item.CCGROUPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置将要对其进行信令代理操作的计费属性组信息。

#### 5.1 配置计费属性组。

```jinja2
{%- if is_optional_billing_attribute_group -%}
    {%- for item in add_ccgroup_list -%}
        ADD CCGROUP:
        {#- --- 必选参数 --- -#}
        CCGROUPNAME="{{item.CCGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 配置计费属性值。

```jinja2
{%- if is_optional_billing_attribute_group -%}
    {%- for item in add_ccvalue_list -%}
        ADD CCVALUE:
        {#- --- 必选参数 --- -#}
        CCGROUPNAME="{{item.CCGROUPNAME}}",
        CCVALUE="{{item.CCVALUE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 配置Home group。

```jinja2
{%- if is_optional_billing_attribute_group -%}
    {%- for item in mod_homegroup_list -%}
        MOD HOMEGROUP:
        {#- --- 必选参数 --- -#}
        HOMEGROUPINDX={{item.HOMEGROUPINDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.CCGROUPSW is not none -%}
            CCGROUPSW={{item.CCGROUPSW}},
        {%- endif -%}
        {%- if item.IMSIMSISDNSW is not none -%}
            IMSIMSISDNSW={{item.IMSIMSISDNSW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CCGROUPSW=ENABLE 时必选 --- -#}
        {%- if item.CCGROUPSW == 'ENABLE' -%}
            CCGROUPNAME="{{item.CCGROUPNAME}}",
        {%- endif -%}
        {#- --- 条件必选：IMSIMSISDNSW=ENABLE 时必选 --- -#}
        {%- if item.IMSIMSISDNSW == 'ENABLE' -%}
            IMSIMSISDNGRPNM="{{item.IMSIMSISDNGRPNM}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 在Home group下配置归属P-GW的IP地址。**ADD HOMEIP**:HOMEGROUPINDX=组号，HOMEIPID=home-ip的编号，IPVERSION=IP版本,HOMEIPv4=Home IPv4地址/HOMEIPv6=Home IPv6地址，PRODUCTTYPE=产品类型；

```jinja2
{%- for item in add_homeip_list -%}
    ADD HOMEIP:
    {#- --- 必选参数 --- -#}
    HOMEGROUPINDX={{item.HOMEGROUPINDX}},
    HOMEIPID={{item.HOMEIPID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEIPV4 is not none -%}
        HOMEIPV4="{{item.HOMEIPV4}}",
    {%- endif -%}
    {%- if item.PRODUCTTYPE is not none -%}
        PRODUCTTYPE={{item.PRODUCTTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        HOMEIPV6="{{item.HOMEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 将Home group绑定到指定的APN。

```jinja2
{%- for item in add_homegrpbindapn_list -%}
    ADD HOMEGRPBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    HOMEGROUPINDX={{item.HOMEGROUPINDX}},
    ;
{%- endfor -%}
```

