---
id: ''
name: N26接口配置
ne_type: UNC
type: feature
description: '**接口介绍**  N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。  N26接口协议栈如图1所示。  **图1** N26接口协议栈  * MME的S10和AMF的N26接口地址独立场景下，需要分别完成MME的S10接口和AMF的N26接口的数据配置。 * MME的S10和AMF的N26接口地址合一场景下，如果已经完成MME的S10接口配置，则无需重复配置AMF的N26接口数据。  GTP-C版本为GTPv2。'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置AMF","N26接口配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
**接口介绍**N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。N26接口协议栈如图1所示。**图1** N26接口协议栈* MME的S10和AMF的N26接口地址独立场景下，需要分别完成MME的S10接口和AMF的N26接口的数据配置。* MME的S10和AMF的N26接口地址合一场景下，如果已经完成MME的S10接口配置，则无需重复配置AMF的N26接口数据。GTP-C版本为GTPv2。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '配置N26接口数据  说明：  如果开启MME的S10和AMF的N26接口地址合一功能，已经完成MME的S10的接口数据配置，则无需重复配置AMF的N26接口数据。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
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
          description: ''
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
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
        IPV6:
          name: 'MME IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: 'IPv6子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmmsubdata_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: '增加用户接入和移动性限制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATRESTRICT:
          name: 'RAT限制'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CORERESTRICT:
          name: '网络限制'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCS:
          name: 'MCS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPS:
          name: 'MPS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPSMCSPRI:
          name: 'MPSMCS优先级'
          type: string
          enum:
          - CFG_FIRST
          - SUB_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CFG_FIRST
    set_amfn26plcy_list:
      type: items
      properties:
        N26ITFMODE:
          name: 'AMF N26接口部署方式'
          type: string
          enum:
          - SEPARATE
          - COMBINE
          required: false
          description: '仅开启MME的S10和AMF的N26接口地址合一功能场景下，配置该命令。  MME的S10和AMF的N26接口地址独立功能场景下，使用默认配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTRAIWK:
          name: '是否支持UAM内部互操作'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_n26mmechar_list_1:
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
        IPV6:
          name: 'MME IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: 'IPv6子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmmsubdata_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: '增加用户接入和移动性限制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RATRESTRICT:
          name: 'RAT限制'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CORERESTRICT:
          name: '网络限制'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCS:
          name: 'MCS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPS:
          name: 'MPS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPSMCSPRI:
          name: 'MPSMCS优先级'
          type: string
          enum:
          - CFG_FIRST
          - SUB_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CFG_FIRST
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.215.24'
      VPNINSTNAME: '_public_'
      DESC: 'FOR N26'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_gtpclegrp_list:
    - GROUPID: 3
      DESC: 'n26'
    add_gtpclegrpmem_list:
    - GROUPID: 3
      IPTYPE: IPv4
      IPV4ADDR: '10.2.215.24'
      VPN: '_public_'
      DESC: 'n26'
      IPV6ADDR: ''
    add_gtpcintf_list:
    - INTFTYPE: E_GTPCINTF_ITFN26
      GROUPID: 3
    add_n26mmechar_list:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '172.16.0.6'
      MASKV4: '255.255.255.255'
      MMECAP: NONIPPDN
      IPV6: ''
      MASKV6: ''
    add_ngmmsubdata_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      RATRESTRICT: EUTRA-1
      CORERESTRICT: EPC-1
      IMSI: ''
      MCS: 'NULL'
      MPS: 'NULL'
      MPSMCSPRI: CFG_FIRST
    set_amfn26plcy_list:
    - N26ITFMODE: COMBINE
      INTRAIWK: ''
    add_n26mmechar_list_1:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '172.16.0.6'
      MASKV4: '255.255.255.255'
      MMECAP: NONIPPDN
      IPV6: ''
      MASKV6: ''
    add_ngmmsubdata_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      RATRESTRICT: EUTRA-1
      CORERESTRICT: EPC-1
      IMSI: ''
      MCS: 'NULL'
      MPS: 'NULL'
      MPSMCSPRI: CFG_FIRST
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **MME的S10和AMF的N26接口地址独立场景**

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置N26接口的IP地址。

```jinja2
{%- if is_scenario_s10_n26_separate -%}
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
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            LOGICIPV6="{{item.LOGICIPV6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.IPV4MTU is not none -%}
                IPV4MTU={{item.IPV4MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.IPV6MTU is not none -%}
                IPV6MTU={{item.IPV6MTU}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置AMF的N26接口的GTP-C本地实体组和实体组成员信息。

```jinja2
{%- if is_scenario_s10_n26_separate -%}
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
{%- if is_scenario_s10_n26_separate -%}
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
        {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPv6' -%}
            IPV6ADDR="{{item.IPV6ADDR}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置N26接口信息。

```jinja2
{%- if is_scenario_s10_n26_separate -%}
    {%- for item in add_gtpcintf_list -%}
        ADD GTPCINTF:
        {#- --- 必选参数 --- -#}
        INTFTYPE={{item.INTFTYPE}},
        GROUPID={{item.GROUPID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置支持UE在LTE与5G SA网络间互操作。

##### 1.5.1 设置对端MME支持non-IP类型PDN。

```jinja2
{%- if is_scenario_s10_n26_separate -%}
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
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            IPV6="{{item.IPV6}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            MASKV6={{item.MASKV6}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.2 设置UE接入限制。

```jinja2
{%- if is_scenario_s10_n26_separate -%}
    {%- for item in add_ngmmsubdata_list -%}
        ADD NGMMSUBDATA:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.RATRESTRICT is not none -%}
            RATRESTRICT={{item.RATRESTRICT}},
        {%- endif -%}
        {%- if item.CORERESTRICT is not none -%}
            CORERESTRICT={{item.CORERESTRICT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MCS is not none -%}
                MCS={{item.MCS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MPS is not none -%}
                MPS={{item.MPS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MPSMCSPRI is not none -%}
                MPSMCSPRI={{item.MPSMCSPRI}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **MME的S10和AMF的N26接口地址合一场景（已完成MME的S10接口配置）**

#### 2.1 配置使用MME的S10和AMF的N26接口地址合一功能。

```jinja2
{%- if is_scenario_s10_n26_combine -%}
    {%- for item in set_amfn26plcy_list -%}
        SET AMFN26PLCY:
        {#- --- 可选参数 --- -#}
        {%- if item.N26ITFMODE is not none -%}
            N26ITFMODE={{item.N26ITFMODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：N26ITFMODE=SEPARATE 时可选 --- -#}
        {%- if item.N26ITFMODE == 'SEPARATE' -%}
            {%- if item.INTRAIWK is not none -%}
                INTRAIWK={{item.INTRAIWK}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置支持UE在LTE与5G SA网络间互操作。

##### 2.2.1 设置对端MME支持non-IP类型PDN。

```jinja2
{%- if is_scenario_s10_n26_combine -%}
    {%- for item in add_n26mmechar_list_1 -%}
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
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            IPV6="{{item.IPV6}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPV6' -%}
            MASKV6={{item.MASKV6}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 设置UE接入限制。

```jinja2
{%- if is_scenario_s10_n26_combine -%}
    {%- for item in add_ngmmsubdata_list_1 -%}
        ADD NGMMSUBDATA:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.RATRESTRICT is not none -%}
            RATRESTRICT={{item.RATRESTRICT}},
        {%- endif -%}
        {%- if item.CORERESTRICT is not none -%}
            CORERESTRICT={{item.CORERESTRICT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MCS is not none -%}
                MCS={{item.MCS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MPS is not none -%}
                MPS={{item.MPS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI' -%}
            {%- if item.MPSMCSPRI is not none -%}
                MPSMCSPRI={{item.MPSMCSPRI}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

