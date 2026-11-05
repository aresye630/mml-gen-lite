---
id: ''
name: 配置到S4 SGSN的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增S4 SGSN或MME时，在配置完成MME到S4 SGSN的路由数据后，可通过配置S3接口数据建立MME到S4 SGSN的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到S4 SGSN的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增S4 SGSN或MME时，在配置完成MME到S4 SGSN的路由数据后，可通过配置S3接口数据建立MME到S4 SGSN的逻辑连接。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81202714 LKV2V6IF01 逻辑接口支持IPv6”。
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
          description: '配置S3接口业务IP。'
          data_source: '整网规划。'
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
          description: '配置MME上的S3接口业务IP。'
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
        GMSI:
          name: 'GTPMAP路径空闲计数器'
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
    set_gtppub_list:
      type: items
      properties:
        ECHOSIG:
          name: '发送ECHO Request的路径'
          type: string
          enum:
          - ALL
          - NONE
          - SPECIFIED
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        V2EI:
          name: '发送GTPv2 Echo请求间隔（s）'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OTSIE:
          name: '乱序信元'
          type: string
          enum:
          - ALLOW
          - DENY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POTHD:
          name: '路径数过载门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PNTHD:
          name: '路径数过载恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTHD:
          name: '路径数拥塞门限（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRTHD:
          name: '路径数拥塞恢复（%）'
          type: integer
          minimum: 0
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPEXT:
          name: '检查GTP扩展头类型个数上限'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPEXLEN:
          name: '检查GTP扩展头类型长度上限'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTPVER:
          name: '本端可处理的请求消息的最高GTP版本'
          type: string
          enum:
          - GTPv0
          - GTPv1
          - GTPv2
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
          description: '配置S4 SGSN解析数据。'
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
          name: 'IPv4地址1'
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
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: '配置S4 SGSN解析数据。'
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
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_SIG'
      LEIPV6: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      GMSI: 60
      PATHVERCHKINT: 60
    set_gtppub_list:
    - ECHOSIG: ALL
      V2EI: 239
      OTSIE: DENY
      POTHD: 85
      PNTHD: 80
      PCTHD: 95
      PRTHD: 90
      GTPEXT: 10
      GTPEXLEN: 100
      GTPVER: GTPv2
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'topon.s3.eth6.mnc001.mcc308.gprs'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.80.47.1'
    add_dnsn_list:
    - FQDN: 'RAC002B.LAC02D9.RAC.EPC.MNC001.MCC308.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: SGSN
      INTYPE: S3
      PRIORITY: 10
      WEIGHT: 104
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置S3接口业务IP。

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

#### 3.1 配置MME上的S3接口业务IP。

```jinja2
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
```

#### 3.2 配置GTP路径管理参数。

```jinja2
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
    {%- if item.GMSI is not none -%}
        GMSI={{item.GMSI}},
    {%- endif -%}
    {%- if item.PATHVERCHKINT is not none -%}
        PATHVERCHKINT={{item.PATHVERCHKINT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_gtppub_list -%}
    SET GTPPUB:
    {#- --- 可选参数 --- -#}
    {%- if item.ECHOSIG is not none -%}
        ECHOSIG={{item.ECHOSIG}},
    {%- endif -%}
    {%- if item.V2EI is not none -%}
        V2EI={{item.V2EI}},
    {%- endif -%}
    {%- if item.OTSIE is not none -%}
        OTSIE={{item.OTSIE}},
    {%- endif -%}
    {%- if item.POTHD is not none -%}
        POTHD={{item.POTHD}},
    {%- endif -%}
    {%- if item.PNTHD is not none -%}
        PNTHD={{item.PNTHD}},
    {%- endif -%}
    {%- if item.PCTHD is not none -%}
        PCTHD={{item.PCTHD}},
    {%- endif -%}
    {%- if item.PRTHD is not none -%}
        PRTHD={{item.PRTHD}},
    {%- endif -%}
    {%- if item.GTPEXT is not none -%}
        GTPEXT={{item.GTPEXT}},
    {%- endif -%}
    {%- if item.GTPEXLEN is not none -%}
        GTPEXLEN={{item.GTPEXLEN}},
    {%- endif -%}
    {%- if item.GTPVER is not none -%}
        GTPVER={{item.GTPVER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置S4 SGSN解析数据。

```jinja2
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
    ;
{%- endfor -%}
```

```jinja2
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
```

