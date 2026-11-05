---
id: GWFD-023003
name: 激活IP地址精简
ne_type: UEG
type: feature
description: UEG风筝L场景，UDM/HSS部署在园区网络时，如下场景下需要激活IP地址精简。  * 4G场景，规划S1-MME与S1-U逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。 * 5G场景，规划N2与N3逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。 * 4/5G融合部署场景，规划S1-MME、S1-U、N2、N3逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-023000 组网接口能力","GWFD-023003 IP地址精简","激活IP地址精简"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-023000 组网接口能力","GWFD-023003 IP地址精简","激活IP地址精简"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-023000 组网接口能力","GWFD-023003 IP地址精简","激活IP地址精简"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG风筝L场景，UDM/HSS部署在园区网络时，如下场景下需要激活IP地址精简。* 4G场景，规划S1-MME与S1-U逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。* 5G场景，规划N2与N3逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。* 4/5G融合部署场景，规划S1-MME、S1-U、N2、N3逻辑接口共用IP地址+VPN实例时，请参考本章节进行配置。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-023003 IP地址精简特性概述。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（风筝L）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_cusingleipattr_list:
      type: items
      properties:
        SWITCH:
          name: '功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '开启IP地址精简场景，设置为“ENABLE”；否则，设置为“DISABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置N2&S1-MME接口IP。'
          data_source: '本端规划'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpsctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_s1aple_list:
      type: items
      properties:
        LLEINDEX:
          name: '链路本地实体号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        LOCALIPV4_1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '同**ADD SERVICEIP**配置的IP地址及VPN实例名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 36412
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SCTPINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LLNAME:
          name: '链路本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPNNAME'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngappara_list:
      type: items
      properties:
        NGAPPARAIDX:
          name: 'NGAP协议参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFCFGUPTTMR:
          name: 'AMF Configuration Update消息超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        AMFCFGUPTCNT:
          name: 'AMF Configuration Update消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        RESETTMR:
          name: 'Reset超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        RESETCNT:
          name: 'Reset消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        TIMETOWAITTMR:
          name: '重发NG SETUP REQUEST时长 (s)'
          type: string
          enum:
          - One
          - Two
          - Five
          - Ten
          - Twenty
          - Sixty
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Sixty
        TIMETOWAITFLG:
          name: '等待时间指示器'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: No
    add_ngaple_list:
      type: items
      properties:
        NGAPLEIDX:
          name: 'NGAP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本端实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用**ADD SCTPLEGRP**配置的SCTPGROUPID参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPPARAIDX:
          name: 'NGAP参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: '采用**ADD NGAPPARA**命令配置的NGAPPARAIDX参数值。'
          data_source: '本端规划'
          pattern: ''
          default: 0
    add_sctplegrp_list:
      type: items
      properties:
        SCTPGROUPID:
          name: 'SCTP本地实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sctple_list:
      type: items
      properties:
        SCTPLEIDX:
          name: 'SCTP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本地实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用**ADD SCTPLEGRP**配置的SCTPGROUPID参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '同**ADD SERVICEIP**配置的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 38412
        CROSSIPFLG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - E_SCTP_CROSS_NO
          - E_SCTP_CROSS_YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: E_SCTP_CROSS_NO
        SCTPPARAIDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGE:
          name: '用途'
          type: string
          enum:
          - E_SCTP_USAGE_BOTH
          - E_SCTP_USAGE_NONUE
          - E_SCTP_USAGE_UE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: E_SCTP_USAGE_BOTH
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置N3&S1-U接口IP，该IP资源同**ADD SERVICEIP**。'
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
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
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
        SLICEATTRSW:
          name: '接口切片属性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_cusingleipattr_list:
    - SWITCH: ENABLE
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '172.20.1.29'
      VPNINSTNAME: 'VRF_Access'
      DESC: 'N2&S1-MME'
    add_cpsctppara_list:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'For_S1AP'
    add_s1aple_list:
    - LLEINDEX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '172.20.1.29'
      LOCALIPV4_2: '172.20.1.30'
      LOCALPORT: 36412
      CROSSIPFLAG: NO
      SCTPINDEX: 6
      LLNAME: 'S1AP-0'
      VPNNAME: 'VRF_Access'
    add_ngappara_list:
    - NGAPPARAIDX: 1
      AMFCFGUPTTMR: 20
      AMFCFGUPTCNT: 3
      RESETTMR: 20
      RESETCNT: 3
      TIMETOWAITTMR: Sixty
      TIMETOWAITFLG: Yes
    add_ngaple_list:
    - NGAPLEIDX: 1
      SCTPGROUPID: 1
      NGAPPARAIDX: 1
    add_sctplegrp_list:
    - SCTPGROUPID: 1
    add_sctple_list:
    - SCTPLEIDX: 1
      SCTPGROUPID: 1
      IPVERSION: IPV4
      LOCALIPV41: '172.20.1.29'
      LOCALIPV42: '172.20.1.30'
      PORT: 38412
      CROSSIPFLG: E_SCTP_CROSS_YES
      SCTPPARAIDX: 0
      USAGE: E_SCTP_USAGE_BOTH
      WEIGHT: 127
    add_logicinf_list:
    - NAME: 'saif1/1/0'
      IPV4ADDRESS1: '172.20.1.29'
      IPV4MASK1: '255.255.255.255'
      IPV4MTU: 1500
      VPNINSTANCE: 'VRF_Access'
      IPVERSION: IPV4
      SLICEATTRSW: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 开启IP地址精简开关。

```jinja2
{%- for item in set_cusingleipattr_list -%}
    SET CUSINGLEIPATTR:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置N2/S1-MME业务接口IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 4G或者4/5G融合场景，配置S1AP链路本地实体。

```jinja2
{%- if is_scenario_4g -%}
    {%- for item in add_cpsctppara_list -%}
        ADD CPSCTPPARA:
        {#- --- 必选参数 --- -#}
        SCTPPARAINDEX={{item.SCTPPARAINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.SCTPPARANAME is not none -%}
            SCTPPARANAME="{{item.SCTPPARANAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_4g -%}
    {%- for item in add_s1aple_list -%}
        ADD S1APLE:
        {#- --- 必选参数 --- -#}
        LLEINDEX={{item.LLEINDEX}},
        SCTPINDEX={{item.SCTPINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPTYPE is not none -%}
            IPTYPE={{item.IPTYPE}},
        {%- endif -%}
        {%- if item.LOCALPORT is not none -%}
            LOCALPORT={{item.LOCALPORT}},
        {%- endif -%}
        {%- if item.CROSSIPFLAG is not none -%}
            CROSSIPFLAG={{item.CROSSIPFLAG}},
        {%- endif -%}
        {%- if item.LLNAME is not none -%}
            LLNAME="{{item.LLNAME}}",
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LOCALIPV4_1="{{item.LOCALIPV4_1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            {%- if item.LOCALIPV4_2 is not none -%}
                LOCALIPV4_2="{{item.LOCALIPV4_2}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 5G或者4/5G融合场景，配置NGAP链路本地实体。

```jinja2
{%- if is_scenario_5g -%}
    {%- for item in add_ngappara_list -%}
        ADD NGAPPARA:
        {#- --- 必选参数 --- -#}
        NGAPPARAIDX={{item.NGAPPARAIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.AMFCFGUPTTMR is not none -%}
            AMFCFGUPTTMR={{item.AMFCFGUPTTMR}},
        {%- endif -%}
        {%- if item.AMFCFGUPTCNT is not none -%}
            AMFCFGUPTCNT={{item.AMFCFGUPTCNT}},
        {%- endif -%}
        {%- if item.RESETTMR is not none -%}
            RESETTMR={{item.RESETTMR}},
        {%- endif -%}
        {%- if item.RESETCNT is not none -%}
            RESETCNT={{item.RESETCNT}},
        {%- endif -%}
        {%- if item.TIMETOWAITTMR is not none -%}
            TIMETOWAITTMR={{item.TIMETOWAITTMR}},
        {%- endif -%}
        {%- if item.TIMETOWAITFLG is not none -%}
            TIMETOWAITFLG={{item.TIMETOWAITFLG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_5g -%}
    {%- for item in add_ngaple_list -%}
        ADD NGAPLE:
        {#- --- 必选参数 --- -#}
        NGAPLEIDX={{item.NGAPLEIDX}},
        SCTPGROUPID={{item.SCTPGROUPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.NGAPPARAIDX is not none -%}
            NGAPPARAIDX={{item.NGAPPARAIDX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置SCTP协议参数及SCTP本端实体。

```jinja2
{%- for item in add_sctplegrp_list -%}
    ADD SCTPLEGRP:
    {#- --- 必选参数 --- -#}
    SCTPGROUPID={{item.SCTPGROUPID}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctple_list -%}
    ADD SCTPLE:
    {#- --- 必选参数 --- -#}
    SCTPLEIDX={{item.SCTPLEIDX}},
    SCTPGROUPID={{item.SCTPGROUPID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.CROSSIPFLG is not none -%}
        CROSSIPFLG={{item.CROSSIPFLG}},
    {%- endif -%}
    {%- if item.SCTPPARAIDX is not none -%}
        SCTPPARAIDX={{item.SCTPPARAIDX}},
    {%- endif -%}
    {%- if item.USAGE is not none -%}
        USAGE={{item.USAGE}},
    {%- endif -%}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LOCALIPV41="{{item.LOCALIPV41}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.LOCALIPV42 is not none -%}
            LOCALIPV42="{{item.LOCALIPV42}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置N3/S1-U逻辑接口IP。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLICEATTRSW is not none -%}
        SLICEATTRSW={{item.SLICEATTRSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

