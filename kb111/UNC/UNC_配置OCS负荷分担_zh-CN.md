---
id: ''
name: 配置OCS负荷分担
ne_type: UNC
type: feature
description: UNC支持配置OCS group，group间是主备关系，group内绑定的OCS间是负荷分担关系。其中负荷分担又分为以下几种情况。  * OCS平均负荷分担    同一group内的所有OCS平均负荷分担用户的在线计费消息处理。默认情况下采用此种方式。 * 基于用户号段进行OCS负荷分担    可以通过以下方式实现基于用户号段选择OCS：    + 根据用户的MSISDN/IMSI号段选择UserProfile，再根据UserProfile下绑定的在线计费模板来选择不同的OCS，实现将用户分布在不同的OCS上进行在线计费处理，降低对单个OCS性能的要求。   + 根据用户的MSISDN/IMSI号段直接选择OCS，实现将用户分布在不同的OCS上进行在线计费处理。    一般情况下，尽量避免同时配置上述两种方式选择OCS。当两种条件都满足的情况下，优先根据UserProfile下关联的OCS进行在线计费处理。 * 基于百分比例进行OCS负荷分担    根据预先设置的百分比例选择OCS，百分比例的基数是累计选择此OCS的次数，实现将用户按比例分布在不同的OCS上进行在线计费，这是实现根据单个OCS性能选择OCS的一种方式。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置OCS组网可靠性配置实例","配置OCS负荷分担"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持配置OCS group，group间是主备关系，group内绑定的OCS间是负荷分担关系。其中负荷分担又分为以下几种情况。* OCS平均负荷分担  同一group内的所有OCS平均负荷分担用户的在线计费消息处理。默认情况下采用此种方式。* 基于用户号段进行OCS负荷分担  可以通过以下方式实现基于用户号段选择OCS：  + 根据用户的MSISDN/IMSI号段选择UserProfile，再根据UserProfile下绑定的在线计费模板来选择不同的OCS，实现将用户分布在不同的OCS上进行在线计费处理，降低对单个OCS性能的要求。  + 根据用户的MSISDN/IMSI号段直接选择OCS，实现将用户分布在不同的OCS上进行在线计费处理。  一般情况下，尽量避免同时配置上述两种方式选择OCS。当两种条件都满足的情况下，优先根据UserProfile下关联的OCS进行在线计费处理。* 基于百分比例进行OCS负荷分担  根据预先设置的百分比例选择OCS，百分比例的基数是累计选择此OCS的次数，实现将用户按比例分布在不同的OCS上进行在线计费，这是实现根据单个OCS性能选择OCS的一种方式。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocs_list:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置OCS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsgroup_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ocs_list_5:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置OCS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list_8:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置MSISDN号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subscriberidseggrp_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV号段组名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSIMSISDN号码段组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI/MSISDN/IMEISV号段名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: '号段类型'
          type: string
          enum:
          - IMEISV
          - IMSIMSISDN
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ocsgroup_list_3:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list_5:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号码段组名称'
          type: string
          maxLength: 31
          required: false
          description: 'OCS组绑定IMSI/MSISDN号段。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSIPRIORITY:
          name: 'IMSI/MSISDN号码段组优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ocs_list_9:
      type: items
      properties:
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置OCS。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Ocs域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list_12:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'OCS信息。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ocsgroup_list_5:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '配置OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ocsbinding_list_9:
      type: items
      properties:
        OCSGRPNAME:
          name: 'Ocs组名称'
          type: string
          maxLength: 63
          required: true
          description: '增加OCS绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSHOSTNAME:
          name: 'Ocs主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSPERCENTAGE:
          name: 'Ocs在OcsGroup中的负荷分担比'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '百分比例。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '主从OCS组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIOCSGRPNAME:
          name: '主OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECOCSGRPNAME:
          name: '备OCS组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_diamlocinfo_list:
    - HOSTNAME: 'pgw1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_ocs_list:
    - OCSHOSTNAME: 'ocs_host1'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list:
    - HOSTNAME: 'ocs_host1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.40.10'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_ocsgroup_list:
    - OCSGRPNAME: 'ocs_gra'
    add_ocsbinding_list:
    - OCSGRPNAME: 'ocs_gra'
      OCSHOSTNAME: 'ocs_host1'
    add_ocs_list_5:
    - OCSHOSTNAME: 'ocs_host1'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list_8:
    - HOSTNAME: 'ocs_host1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.40.10'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: MSISDN
      SEGSTART: '13900100100'
      SEGEND: '13900100199'
      WILDCARDSEG: ''
    add_subscriberidseggrp_list:
    - SEGGROUPNAME: 'testmsisdngr1'
      SEGMENTNAME: 'testmsisdn1'
      SEGMENTTYPE: IMSIMSISDN
    add_ocsgroup_list_3:
    - OCSGRPNAME: 'ocs_gra'
    add_ocsbinding_list_5:
    - OCSGRPNAME: 'ocs_gra'
      OCSHOSTNAME: 'ocs_host1'
      SEGGROUPNAME: 'testmsisdngr1'
      IMSIPRIORITY: 30
    add_ocs_list_9:
    - OCSHOSTNAME: 'ocs_host1'
      REALMNAME: 'ocs_realm'
    add_diampeeraddr_list_12:
    - HOSTNAME: 'ocs_host1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '192.168.40.10'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_ocsgroup_list_5:
    - OCSGRPNAME: 'ocs_gra'
    add_ocsbinding_list_9:
    - OCSGRPNAME: 'ocs_gra'
      OCSHOSTNAME: 'ocs_host1'
      OCSPERCENTAGE: 40
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      PRIOCSGRPNAME: 'ocs_gra'
      SECOCSGRPNAME: 'ocs_grb'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在线计费中GGSN/PGW-C的设备标识。

### 配置在线计费中通信的GGSN/PGW-C的设备标识，重复执行本步骤可添加多个Gy应用的本地信息。

### UNC的Gx应用和Gy应用的本端主机名可以相同，但是同时要求“REALMNAME”参数和“PRODUCTNAME”参数也必须相同。

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    ;
{%- endfor -%}
```

### 2 配置平均进行OCS负荷分担。

#### 2.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- if is_scenario_average_load_sharing -%}
    {%- for item in add_ocs_list -%}
        ADD OCS:
        {#- --- 必选参数 --- -#}
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_average_load_sharing -%}
    {%- for item in add_diampeeraddr_list -%}
        ADD DIAMPEERADDR:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.ADDRTYPE == 'SCTP' -%}
            SCTPENDPOINT="{{item.SCTPENDPOINT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
        {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置OCS组。重复执行本步骤可增加多个OCS组信息。

```jinja2
{%- if is_scenario_average_load_sharing -%}
    {%- for item in add_ocsgroup_list -%}
        ADD OCSGROUP:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置平均选择在线计费系统的OCS，不配置可选参数即可实现。

```jinja2
{%- if is_scenario_average_load_sharing -%}
    {%- for item in add_ocsbinding_list -%}
        ADD OCSBINDING:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置基于用户号段进行OCS负荷分担。

#### 3.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_ocs_list_5 -%}
        ADD OCS:
        {#- --- 必选参数 --- -#}
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_diampeeraddr_list_8 -%}
        ADD DIAMPEERADDR:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.ADDRTYPE == 'SCTP' -%}
            SCTPENDPOINT="{{item.SCTPENDPOINT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
        {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置IMSI及MSISDN号码段。

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_imsimsisdnseg_list -%}
        ADD IMSIMSISDNSEG:
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

#### 3.3 配置IMSI及MSISDN号码段组。

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_subscriberidseggrp_list -%}
        ADD SUBSCRIBERIDSEGGRP:
        {#- --- 必选参数 --- -#}
        SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        SEGMENTTYPE={{item.SEGMENTTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置OCS组。重复执行本步骤可增加多个OCS组信息。

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_ocsgroup_list_3 -%}
        ADD OCSGROUP:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 配置基于用户号段IMSI/MSISDN选择在线计费系统的OCS。

```jinja2
{%- if is_scenario_user_segment_load_sharing -%}
    {%- for item in add_ocsbinding_list_5 -%}
        ADD OCSBINDING:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SEGGROUPNAME is not none -%}
            SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {%- endif -%}
        {%- if item.IMSIPRIORITY is not none -%}
            IMSIPRIORITY={{item.IMSIPRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置基于百分比例进行OCS负荷分担。

#### 4.1 配置OCS信息。重复执行本步骤可增加多个OCS信息。

```jinja2
{%- if is_scenario_percentage_load_sharing -%}
    {%- for item in add_ocs_list_9 -%}
        ADD OCS:
        {#- --- 必选参数 --- -#}
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_percentage_load_sharing -%}
    {%- for item in add_diampeeraddr_list_12 -%}
        ADD DIAMPEERADDR:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
        {%- if item.ADDRTYPE == 'IPv6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
        {%- if item.ADDRTYPE == 'SCTP' -%}
            SCTPENDPOINT="{{item.SCTPENDPOINT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
        {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置OCS组。重复执行本步骤可增加多个OCS组信息。

```jinja2
{%- if is_scenario_percentage_load_sharing -%}
    {%- for item in add_ocsgroup_list_5 -%}
        ADD OCSGROUP:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置基于百分比例选择在线计费系统的OCS。

```jinja2
{%- if is_scenario_percentage_load_sharing -%}
    {%- for item in add_ocsbinding_list_9 -%}
        ADD OCSBINDING:
        {#- --- 必选参数 --- -#}
        OCSGRPNAME="{{item.OCSGRPNAME}}",
        OCSHOSTNAME="{{item.OCSHOSTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.OCSPERCENTAGE is not none -%}
            OCSPERCENTAGE={{item.OCSPERCENTAGE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置主从OCS组。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIOCSGRPNAME is not none -%}
        PRIOCSGRPNAME="{{item.PRIOCSGRPNAME}}",
    {%- endif -%}
    {%- if item.SECOCSGRPNAME is not none -%}
        SECOCSGRPNAME="{{item.SECOCSGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

