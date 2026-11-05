---
id: ''
name: 配置N26接口数据
ne_type: UEG
type: feature
description: '**接口介绍**  N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。  N26接口协议栈如图1所示。  **图1** N26接口协议栈  GTP-C版本为GTPv2。  MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。  * 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。 * 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。'
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置AMF","配置N26接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**接口介绍**N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。N26接口协议栈如图1所示。**图1** N26接口协议栈GTP-C版本为GTPv2。MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。* 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。* 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 已完成组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置N26接口数据。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    add_gtpclegrp_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gtpclegrpmem_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPN:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gtpcintf_list:
      type: items
      properties:
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - E_GTPCINTF_ITFS11
          - E_GTPCINTF_ITFN26
          - E_GTPCINTF_ITFS5_S
          - E_GTPCINTF_ITFS8_S
          - S5_P_OR_GN
          - S8_P_OR_GP
          - PROXY_SGSN_GP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ngdns_list:
      type: items
      properties:
        ANALYSETYPE:
          name: 'DNS解析方式'
          type: string
          enum:
          - HOSTFILE_SERVER
          - SERVER_HOSTFILE
          required: false
          description: '配置AMF选择MME参数。  如果没有DNS Server，DNS查询时优先使用本地配置数据，包含：   * 在4G到5G的移动注册更新流程中AMF根据GUMMEI找MME的时候的DNSN记录。 * 在Inter Handover流程中AMF根据eNodeB的TAC值选择MME使用的DNSN记录。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPPLCY:
          name: 'N26接口本网IP地址选择策略'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV6PRE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMESWITCH:
          name: '优选融合MME开关'
          type: string
          enum:
          - MME_ON
          - MME_OFF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngdnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: '该参数需已通过ADD NGIPV4DNSH命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - MME
          - NG
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - N26
          - SBI
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_n26mmechar_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - SPECIAL_MME
          - COMB_MME
          required: true
          description: '增加对端MME的属性信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPV4:
          name: 'MME IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMECAP:
          name: 'MME能力'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.154.23'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR N26'
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.154.24'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR N26'
    add_gtpclegrp_list:
    - GROUPID: 3
      DESC: 'n26'
    - GROUPID: 3
      DESC: 'n26'
    add_gtpclegrpmem_list:
    - GROUPID: 3
      IPTYPE: IPv4
      IPV4ADDR: '10.2.154.23'
      VPN: 'VPN_CN'
      DESC: 'n26'
    - GROUPID: 3
      IPTYPE: IPv4
      IPV4ADDR: '10.2.154.24'
      VPN: 'VPN_CN'
      DESC: 'n26'
    add_gtpcintf_list:
    - INTFTYPE: E_GTPCINTF_ITFN26
      GROUPID: 3
    - INTFTYPE: E_GTPCINTF_ITFN26
      GROUPID: 3
    set_ngdns_list:
    - ANALYSETYPE: HOSTFILE_SERVER
      IPPLCY: IPV4
      MMESWITCH: MME_ON
    - ANALYSETYPE: HOSTFILE_SERVER
      IPPLCY: IPV4
      MMESWITCH: MME_ON
    add_ngipv4dnsh_list:
    - HSINDEX: 7
      HOSTNAME: 'topon.mme-s10.mmec01.mmegi8001.mme.epc.mnc003.mcc123.3gppnetwork.org'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.10.1'
    - HSINDEX: 8
      HOSTNAME: 'topon.mme-s10.mmec02.mmegi8001.mme.epc.mnc003.mcc123.3gppnetwork.org'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.10.3'
    add_ngdnsn_list:
    - FQDN: 'tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org'
      HSINDEX: 7
      ENTITY: MME
      INTYPE: N26
    - FQDN: 'tac-lb01.tac-hb26.tac.epc.mnc003.mcc123.3gppnetwork.org'
      HSINDEX: 8
      ENTITY: MME
      INTYPE: N26
    add_n26mmechar_list:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '172.16.0.5'
      MASKV4: '255.255.255.255'
      MMECAP: NONIPPDN
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '172.16.0.6'
      MASKV4: '255.255.255.255'
      MMECAP: NONIPPDN
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**配置GTP数据配置N26接口的IP地址。

#### 2.1 //DC1

```jinja2
{%- if is_optional_n26_interface_ip_address -%}
    {%- for item in add_logicip_list -%}
        ADD LOGICIP:
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
            LOGICIPV4="{{item.LOGICIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置GTP数据。

#### 3.1 配置AMF的N26接口的GTP-C本地实体组和实体组成员信息。

##### 3.1.1 //DC1

```jinja2
{%- if is_optional_gtp_data -%}
    {%- for item in add_gtpclegrp_list -%}
        ADD GTPCLEGRP:
        {#- --- 必选参数 --- -#}
        GROUPID={{item.GROUPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_gtp_data -%}
    {%- for item in add_gtpclegrpmem_list -%}
        ADD GTPCLEGRPMEM:
        {#- --- 必选参数 --- -#}
        GROUPID={{item.GROUPID}},
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPN is not none -%}
            VPN="{{item.VPN}}",
        {%- endif -%}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置N26 GTPC接口信息，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 //DC1

```jinja2
{%- if is_optional_gtp_data -%}
    {%- for item in add_gtpcintf_list -%}
        ADD GTPCINTF:
        {#- --- 必选参数 --- -#}
        INTFTYPE={{item.INTFTYPE}},
        GROUPID={{item.GROUPID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置MME选择参数。

#### 4.2 //（可选）本地Hostfile配置MME解析数据

```jinja2
{%- if is_optional_local_hostfile_mme_resolution -%}
    {%- for item in set_ngdns_list -%}
        SET NGDNS:
        {#- --- 可选参数 --- -#}
        {%- if item.ANALYSETYPE is not none -%}
            ANALYSETYPE={{item.ANALYSETYPE}},
        {%- endif -%}
        {%- if item.IPPLCY is not none -%}
            IPPLCY={{item.IPPLCY}},
        {%- endif -%}
        {%- if item.MMESWITCH is not none -%}
            MMESWITCH={{item.MMESWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 //配置AMF的DNS Client数据,用于寻址MME。

```jinja2
{%- for item in add_ngipv4dnsh_list -%}
    ADD NGIPV4DNSH:
    {#- --- 必选参数 --- -#}
    HSINDEX={{item.HSINDEX}},
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRSECTION={{item.ADDRSECTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR1 is not none -%}
        IPV4ADDR1="{{item.IPV4ADDR1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngdnsn_list -%}
    ADD NGDNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
    ;
{%- endfor -%}
```

### 5 配置支持UE在LTE与5G SA网络间互操作。

#### 5.1 //DC1

```jinja2
{%- for item in add_n26mmechar_list -%}
    ADD N26MMECHAR:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MMECAP is not none -%}
        MMECAP={{item.MMECAP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_MME' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

