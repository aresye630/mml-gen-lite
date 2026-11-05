---
id: GWFD-030703
name: 激活IGMP Snooping
ne_type: UEG
type: feature
description: 5G LAN支持基于IGMP Snooping实现层二动态组播功能时，需要配置本页面。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-030700 5G LAN基本功能","可选功能","GWFD-030703 支持IGMP Snooping","激活IGMP Snooping"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
5G LAN支持基于IGMP Snooping实现层二动态组播功能时，需要配置本页面。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-030703 支持IGMP Snooping特性概述。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
* 已完成配置5G LAN基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IGMPSNOOPINGSW:
          name: 'IGMP Snooping开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'UPF支持基于IGMP Snooping实现5G LAN层二动态组播功能时，设置为“ENABLE”，否则设置为“DISABLE”。  例如，UPF替代楼宇IGMP Snooping交换机时需要设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upethsrvpara_list:
      type: items
      properties:
        UPETHSRVSW:
          name: '用户面以太业务开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '环路检测方式采用主动检测或UPF作为IGMP查询器时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: '此处配置的是UPF发送query报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_igmpsnoopingattr_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QUERIERSW:
          name: 'IGMP Snooping查询器开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '网络中不存在IGMP查询器时，规划UPF作为查询器时，使用样例值。  UPF作为IGMP查询器时，仅支持在一个UPF上开启。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QUERYINTERVAL:
          name: '普遍组查询报文发送时间间隔'
          type: integer
          minimum: 30
          maximum: 65535
          required: false
          description: '开启IGMP Snooping查询器开关后，设置的UPF发送query报文的时间间隔（单位是秒）、UPF等待query响应报文的最大时间（单位是秒）及UPF发送query报文的次数。  以样例值为例，UPF在t时刻发送第一次query报文，在t+60s时发送第二次query报文，在t+60\*2s时发送第三次query报文，如在t+60\*2s+10s时间内未收到某个成员的IGMPv2 join消息（IGMP Version 2 Membership Report），则会将该成员从组播组删除。'
          data_source: '本端规划'
          pattern: ''
          default: 60
        MAXRSPTIME:
          name: '普遍组查询最大响应时间'
          type: integer
          minimum: 1
          maximum: 25
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 10
        ROBUSTCOUNT:
          name: 'IGMP健壮系数'
          type: integer
          minimum: 2
          maximum: 5
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 2
        SOURCEADDR:
          name: '普遍组查询的源IP地址'
          type: string
          maxLength: 15
          required: false
          description: 'UPF发送的普遍组查询报文的源IP地址。缺省值为192.168.0.1，当该IP地址已被网络中的其他设备占用时，需要执行本命令配置为其他IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_igmpsnoopingattr_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QUERIERSW:
          name: 'IGMP Snooping查询器开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '网络中其他设备作为IGMP查询器时，使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QUERYINTERVAL:
          name: '普遍组查询报文发送时间间隔'
          type: integer
          minimum: 30
          maximum: 65535
          required: false
          description: 'UPF上设置的查询参数取值需要与IGMP查询器上的参数值一致，用于维护IGMP组成员。  在t时刻发送第一次查询报文，则在t+60\*2s+10s内未收到某个成员的IGMPv2 join消息（IGMP Version 2 Membership Report），则会将该成员从组播组删除。'
          data_source: '从对端获取'
          pattern: ''
          default: 60
        MAXRSPTIME:
          name: '普遍组查询最大响应时间'
          type: integer
          minimum: 1
          maximum: 25
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: 10
        ROBUSTCOUNT:
          name: 'IGMP健壮系数'
          type: integer
          minimum: 2
          maximum: 5
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: 2
    add_multicastsource_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCSOURCETYPE:
          name: '组播源类型'
          type: string
          enum:
          - IMSI
          - DFSRPAIR
          required: true
          description: '组播源是单个用户时需要配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSI:
          name: '组播源标识'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    mod_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      IGMPSNOOPINGSW: ENABLE
    set_upethsrvpara_list:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    set_igmpsnoopingattr_list:
    - VNINSTANCE: '000003e9-460-08-01'
      QUERIERSW: ENABLE
      QUERYINTERVAL: 60
      MAXRSPTIME: 10
      ROBUSTCOUNT: 2
      SOURCEADDR: '192.168.0.1'
    set_igmpsnoopingattr_list_1:
    - VNINSTANCE: '000003e9-460-08-01'
      QUERIERSW: DISABLE
      QUERYINTERVAL: 60
      MAXRSPTIME: 10
      ROBUSTCOUNT: 2
    add_multicastsource_list:
    - VNINSTANCE: '000003e9-460-08-01'
      MCSOURCETYPE: IMSI
      IMSI: '460123123456787'
      DFSRPAIRID: 10
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 开启IGMP Snooping功能开关。

```jinja2
{%- for item in mod_ngvninstance_list -%}
    MOD NGVNINSTANCE:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNTYPE is not none -%}
        PDNTYPE={{item.PDNTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.IGMPSNOOPINGSW is not none -%}
            IGMPSNOOPINGSW={{item.IGMPSNOOPINGSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.1 网络中无查询器，UPF作为查询器时，请执行2。

#### 1.2 网络中其他设备作为查询器时，请执行3。

### 2 配置UPF支持Query功能。网络中无查询器时，在UPF上配置Query功能。

#### 2.1 配置Query消息的源MAC地址。

```jinja2
{%- if is_scenario_upf_as_querier -%}
    {%- for item in set_upethsrvpara_list -%}
        SET UPETHSRVPARA:
        {#- --- 必选参数 --- -#}
        UPETHSRVSW={{item.UPETHSRVSW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPETHSRVSW=ENABLE 时必选 --- -#}
        {%- if item.UPETHSRVSW == 'ENABLE' -%}
            UPETHSRVMAC="{{item.UPETHSRVMAC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 开启Query查询功能并设置查询参数。

```jinja2
{%- if is_scenario_upf_as_querier -%}
    {%- for item in set_igmpsnoopingattr_list -%}
        SET IGMPSNOOPINGATTR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        QUERIERSW={{item.QUERIERSW}},
        {#- --- 可选参数 --- -#}
        {%- if item.QUERYINTERVAL is not none -%}
            QUERYINTERVAL={{item.QUERYINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRSPTIME is not none -%}
            MAXRSPTIME={{item.MAXRSPTIME}},
        {%- endif -%}
        {%- if item.ROBUSTCOUNT is not none -%}
            ROBUSTCOUNT={{item.ROBUSTCOUNT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QUERIERSW=ENABLE 时可选 --- -#}
        {%- if item.QUERIERSW == 'ENABLE' -%}
            {%- if item.SOURCEADDR is not none -%}
                SOURCEADDR="{{item.SOURCEADDR}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 网络中其他设备作为查询器时，配置Query参数。基于query参数判断组播组成员的状态。

```jinja2
{%- if is_scenario_other_as_querier -%}
    {%- for item in set_igmpsnoopingattr_list_1 -%}
        SET IGMPSNOOPINGATTR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        QUERIERSW={{item.QUERIERSW}},
        {#- --- 可选参数 --- -#}
        {%- if item.QUERYINTERVAL is not none -%}
            QUERYINTERVAL={{item.QUERYINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRSPTIME is not none -%}
            MAXRSPTIME={{item.MAXRSPTIME}},
        {%- endif -%}
        {%- if item.ROBUSTCOUNT is not none -%}
            ROBUSTCOUNT={{item.ROBUSTCOUNT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置N3侧的组播源。组播源在N3侧时需要配置，组播源在N6侧/另一UPF下时，无需配置。

```jinja2
{%- if is_scenario_multicast_source_n3 -%}
    {%- for item in add_multicastsource_list -%}
        ADD MULTICASTSOURCE:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        MCSOURCETYPE={{item.MCSOURCETYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MCSOURCETYPE=IMSI 时必选 --- -#}
        {%- if item.MCSOURCETYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：MCSOURCETYPE=DFSRPAIR 时必选 --- -#}
        {%- if item.MCSOURCETYPE == 'DFSRPAIR' -%}
            DFSRPAIRID={{item.DFSRPAIRID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

