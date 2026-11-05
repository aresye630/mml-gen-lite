---
id: ''
name: 配置到GnGp SGSN的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到Gn/Gp SGSN的路由数据后，可通过配置Gn接口数据建立MME到Gn/Gp SGSN的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到GnGp SGSN的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到Gn/Gp SGSN的路由数据后，可通过配置Gn接口数据建立MME到Gn/Gp SGSN的逻辑连接。

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
          description: '融合配置时，各GTP接口的本端地址是统一配置。'
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
    set_gtppub_list:
      type: items
      properties:
        PRVEXT:
          name: '发送私有信息'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        ECHOSIG:
          name: '发送ECHO Request的路径'
          type: string
          enum:
          - ALL
          - NONE
          - SPECIFIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EI:
          name: '发送Echo请求间隔（s）'
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
        PEID:
          name: '企业号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PE:
          name: '私有信息'
          type: string
          maxLength: 255
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
        GTPSUPEXTLIST:
          name: '检查GTP扩展头列表个数上限'
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
        PEERRECOVERYSW:
          name: '对端Recovery处理开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHDOWNDEASW:
          name: 'GTPC路径断去激活开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UDPCHKSW:
          name: 'GTPC报文校验功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpule_list:
      type: items
      properties:
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
        LEIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpuintfattr_list:
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 31
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
        INTFTP1:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - Iu
          - S11
          - S4
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
          description: '* 配置SGSN的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。  * HOSTNAME格式定义详见配置Hostfile数据。'
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
          name: '主机地址段号'
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
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list_1:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '* 配置SGSN的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。  * HOSTNAME格式定义详见配置Hostfile数据。'
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
          name: '主机地址段号'
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
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.0.1'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.10.0.1'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
    add_gtpcintfattr_list:
    - SUBRANGE: ''
      GRPID: ''
      IMSIPRE: ''
      INTFTP: ''
      INTFTP2: ''
      NOID: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    set_gtppub_list:
    - PRVEXT: ON
      ECHOSIG: ALL
      EI: 239
      OTSIE: DENY
      POTHD: 85
      PNTHD: 80
      PCTHD: 95
      PRTHD: 90
      PEID: 2011
      PE: 'USN'
      GTPEXT: 10
      GTPSUPEXTLIST: 100
      GTPEXLEN: 100
      GTPVER: GTPv2
      PEERRECOVERYSW: OFF
      PATHDOWNDEASW: OFF
      UDPCHKSW: ON
    add_gtpule_list:
    - IPTYPE: ''
      LEIPV4: ''
      LEIPV6: ''
    add_gtpuintfattr_list:
    - SUBRANGE: ''
      GRPID: ''
      IMSIPRE: ''
      INTFTP1: ''
      INTFTP2: ''
      NOID: ''
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'RAC002B.LAC02D9.MNC001.MCC123.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.2'
    add_ipv4dnsh_list_1:
    - HSINDEX: 7
      HOSTNAME: 'RNC025B.MNC001.MCC123.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置Gn接口业务IP。

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

#### 3.1 配置GTPC业务IP。

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

#### 3.2 **可选：**如果需要将Gn接口和其他接口分离部署，配置Gn接口GTPC逻辑接口隔离。

```jinja2
{%- if is_optional_gtpc_logic_interface_isolation -%}
    {%- for item in add_gtpcintfattr_list -%}
        ADD GTPCINTFATTR:
        {#- --- 必选参数 --- -#}
        GRPID={{item.GRPID}},
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP={{item.INTFTP}},
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

#### 3.3 **可选：**配置GTP路径管理参数。

```jinja2
{%- if is_optional_gtp_path_management -%}
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

```jinja2
{%- if is_optional_gtp_path_management -%}
    {%- for item in set_gtppub_list -%}
        SET GTPPUB:
        {#- --- 可选参数 --- -#}
        {%- if item.PRVEXT is not none -%}
            PRVEXT={{item.PRVEXT}},
        {%- endif -%}
        {%- if item.ECHOSIG is not none -%}
            ECHOSIG={{item.ECHOSIG}},
        {%- endif -%}
        {%- if item.EI is not none -%}
            EI={{item.EI}},
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
        {%- if item.PEID is not none -%}
            PEID={{item.PEID}},
        {%- endif -%}
        {%- if item.PE is not none -%}
            PE="{{item.PE}}",
        {%- endif -%}
        {%- if item.GTPEXT is not none -%}
            GTPEXT={{item.GTPEXT}},
        {%- endif -%}
        {%- if item.GTPSUPEXTLIST is not none -%}
            GTPSUPEXTLIST={{item.GTPSUPEXTLIST}},
        {%- endif -%}
        {%- if item.GTPEXLEN is not none -%}
            GTPEXLEN={{item.GTPEXLEN}},
        {%- endif -%}
        {%- if item.GTPVER is not none -%}
            GTPVER={{item.GTPVER}},
        {%- endif -%}
        {%- if item.PEERRECOVERYSW is not none -%}
            PEERRECOVERYSW={{item.PEERRECOVERYSW}},
        {%- endif -%}
        {%- if item.PATHDOWNDEASW is not none -%}
            PATHDOWNDEASW={{item.PATHDOWNDEASW}},
        {%- endif -%}
        {%- if item.UDPCHKSW is not none -%}
            UDPCHKSW={{item.UDPCHKSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 **可选：**配置GTPU本地实体。

```jinja2
{%- if is_optional_gtpu_local_entity -%}
    {%- for item in add_gtpule_list -%}
        ADD GTPULE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
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

#### 3.5 **可选：**如果需要将Gn接口和其他接口分离部署，配置Gn接口GTPU逻辑隔离。

```jinja2
{%- if is_optional_gtpu_logic_interface_isolation -%}
    {%- for item in add_gtpuintfattr_list -%}
        ADD GTPUINTFATTR:
        {#- --- 必选参数 --- -#}
        GRPID={{item.GRPID}},
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP1={{item.INTFTP1}},
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

#### 3.6 **可选：**配置DNS服务器的数据。

#### 如果现网已经完成DNS服务器的数据配置，则无需执行本步骤。

#### 配置了GTP-C IP的UNC必须同时配置DNS客户端IP才能进行相关的业务。

#### 此IP地址为UNC中定义的IP地址。

### 4 配置SGSN的解析数据，增加Hostfile文件的A解析记录。

#### 4.1 Attach/TAU/NACC流程配置GnGp网元的DNS记录。

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

#### 4.2 Handover流程配置GnGp网元的DNS记录。

```jinja2
{%- for item in add_ipv4dnsh_list_1 -%}
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

