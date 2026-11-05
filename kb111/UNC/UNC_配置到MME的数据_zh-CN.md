---
id: ''
name: 配置到MME的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到MME的路由数据后，可通过配置S10接口数据建立MME到MME的逻辑连接。  由于MME上S10接口与N26接口共用同一个接口实现，所以如果已经配置N26接口，不需要再配置S10接口。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到MME的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到MME的路由数据后，可通过配置S10接口数据建立MME到MME的逻辑连接。由于MME上S10接口与N26接口共用同一个接口实现，所以如果已经配置N26接口，不需要再配置S10接口。

## 必备事项
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
          description: '配置业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
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
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTPC本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list_1:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTPC本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list_1:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcintfattr_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_NOID
          required: true
          description: '配置S10接口分离。'
          data_source: ''
          pattern: ''
          default: ''
        INTFTP:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - S10
          - S11
          - S3
          - S4
          - SV
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTFTP2:
          name: '接口类型2'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - S11
          - S4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置MME的解析数据。如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置ADD IPV4DNSH和ADD DNSN。如果采用IPv6组网，则使用ADD IPV6DNSH命令替代ADD IPV4DNSH命令。HOSTNAME及FQDN格式定义详见配置Hostfile数据。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1~IPv4地址8'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR2:
          name: 'IPv4地址1~IPv4地址8'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: '全称标准规范的域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.17'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcle_list_1:
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    set_ugtp_list_1:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP: S10
      GRPID: 3
      IMSIPRE: ''
      INTFTP2: ''
      NOID: ''
    add_ipv4dnsh_list:
    - HSINDEX: 4
      HOSTNAME: 'topon.eth6.mmec14.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.1'
      IPV4ADDR2: '10.10.1.2'
    add_dnsn_list:
    - FQDN: 'MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 4
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 18
      WEIGHT: 112
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置S10接口业务IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置GTP数据。

#### 3.1 配置S10接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。

##### 3.1.1 配置MME在S10接口的GTPC IP。

```jinja2
{%- if is_scenario_s10_co_deploy -%}
    {%- for item in add_gtpcle_list -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
            LEIPV6="{{item.LEIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 配置GTP路径管理参数。

```jinja2
{%- if is_scenario_s10_co_deploy -%}
    {%- for item in set_ugtp_list -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要将S10接口与其他接口分离部署时，配置S10接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 配置MME在S10接口的GTPC IP。

```jinja2
{%- if is_scenario_s10_separate_deploy -%}
    {%- for item in add_gtpcle_list_1 -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV6 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV6' -%}
            LEIPV6="{{item.LEIPV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 配置GTP路径管理参数。

```jinja2
{%- if is_scenario_s10_separate_deploy -%}
    {%- for item in set_ugtp_list_1 -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置GTPC接口属性。

```jinja2
{%- if is_scenario_s10_separate_deploy -%}
    {%- for item in add_gtpcintfattr_list -%}
        ADD GTPCINTFATTR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        GRPID={{item.GRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP={{item.INTFTP}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE/SPECIAL_NOID 时必选 --- -#}
        {%- if item.SUBRANGE in ['SPECIAL_IMSIPRE', 'SPECIAL_NOID'] -%}
            INTFTP2={{item.INTFTP2}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_NOID 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_NOID' -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置对端MME的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

```jinja2
{%- if is_optional_peer_mme_dns_data -%}
    {%- for item in add_ipv4dnsh_list -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        {%- if item.IPV4ADDR2 is not none -%}
            IPV4ADDR2="{{item.IPV4ADDR2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_peer_mme_dns_data -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

