---
id: ''
name: 配置到SGSN的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增SGSN时，在配置完成到SGSN的路由数据后，可通过配置Gn接口数据建立SGSN到SGSN的逻辑连接。  S16 接口支持GTP-U协议栈，如果需要将S16 接口和其他接口分离部署，可以通过****ADD GTPULE****配置S16接口GTP-U IP，并通过****ADD GTPUINTFATTR****配置GTPU逻辑IP隔离。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到SGSN的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增SGSN时，在配置完成到SGSN的路由数据后，可通过配置Gn接口数据建立SGSN到SGSN的逻辑连接。S16 接口支持GTP-U协议栈，如果需要将S16 接口和其他接口分离部署，可以通过****ADD GTPULE****配置S16接口GTP-U IP，并通过****ADD GTPUINTFATTR****配置GTPU逻辑IP隔离。

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
          description: '配置Gn接口业务IP。'
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
          description: '配置GTPC IP。'
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
    add_gtpule_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTPU IP。'
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
          description: '配置RAI解析数据。'
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
        IPV4ADDR2:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sgsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_SGSN
          - SPECIAL_SGSN
          required: true
          description: '配置对端SGSN支持的协议版本。'
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSVER:
          name: 'SGSN支持的QoS版本'
          type: string
          enum:
          - R5QOS
          - R7QOS
          - R99QOS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R99QOS
        IPV6:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.0.1'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.0.1'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    add_gtpule_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.0.1'
      VPNNAME: 'VPN_CN'
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
      HOSTNAME: 'RAC0001.LAC5321.MNC000.MCC460.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '192.168.0.33'
      IPV4ADDR2: '192.168.0.34'
    add_sgsncharact_list:
    - RANGE: SPECIAL_SGSN
      IPT: IPV4
      IPV4: '192.168.0.33'
      MASKV4: '255.255.255.255'
      QOSVER: R5QOS
      IPV6: ''
      MASKV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置Gn接口业务IP

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

#### 3.1 配置GTPC IP。

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

#### 3.2 配置GTPU IP。

```jinja2
{%- for item in add_gtpule_list -%}
    ADD GTPULE:
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

#### 3.3 配置GTP路径管理参数。

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

### 4 配置SGSN上的数据。

#### 4.1 配置RAI解析数据。

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
    {%- if item.IPV4ADDR2 is not none -%}
        IPV4ADDR2="{{item.IPV4ADDR2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.2 配置对端SGSN支持的协议版本。

```jinja2
{%- for item in add_sgsncharact_list -%}
    ADD SGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.QOSVER is not none -%}
        QOSVER={{item.QOSVER}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_SGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_SGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

