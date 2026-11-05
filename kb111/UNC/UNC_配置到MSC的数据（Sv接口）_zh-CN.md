---
id: ''
name: 配置到MSC的数据（Sv接口）
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC的路由数据后，可通过配置Sv接口数据建立MME到MSC的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到MSC的数据（Sv接口）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到MSC的路由数据后，可通过配置Sv接口数据建立MME到MSC的逻辑连接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
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
          description: 'Sv接口本、对端的GTPC IP地址不能与SGs接口重复。'
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
          description: '设置GTP-C路径扫描参数。'
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
          description: '设置GTP-C协议参数。'
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
        POOLSRCPORTSW:
          name: '缺省SGSN透传源端口号开关'
          type: string
          enum:
          - OFF
          - ON
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
        PATHVERDETECTSW:
          name: 'V0版本GTPC路径尝试使用V1版本探测开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSGTPCPATHFILTERSW:
          name: '过滤故障状态的GTPC路径开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRECOVERYSW:
          name: '本端recovery更新开关'
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
    add_gtpcle_list_1:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: 'Sv接口本、对端的GTPC IP地址不能与SGs接口重复。'
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
          description: '设置GTP-C路径扫描参数。'
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
    set_gtppub_list_1:
      type: items
      properties:
        PRVEXT:
          name: '发送私有信息'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置GTP-C协议参数。'
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
        POOLSRCPORTSW:
          name: '缺省SGSN透传源端口号开关'
          type: string
          enum:
          - OFF
          - ON
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
        PATHVERDETECTSW:
          name: 'V0版本GTPC路径尝试使用V1版本探测开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSGTPCPATHFILTERSW:
          name: '过滤故障状态的GTPC路径开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRECOVERYSW:
          name: '本端recovery更新开关'
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
          description: '为增加网络安全性，建议将Sv接口和S10/S11接口分离部署。  * Sv接口采用单独的IP地址，并绑定到VRF中。 * VRF建议包括S6a/S6d/Gb/Iu\_c(IP)/Gr/Sv接口。'
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
    set_mscselplcy_list:
      type: items
      properties:
        DNSPLCY:
          name: 'Sv接口域名解析策略'
          type: string
          enum:
          - LAI
          - RAI
          required: false
          description: '设置MSC域名解析策略。'
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
          description: '配置IPV4 DNS Hostfile记录。'
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
        IPV4ADDR2:
          name: 'IPv4地址2'
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
          description: '增加Hostfile文件的NAPTR解析记录。'
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
      SERVICEIPV4: '10.10.1.3'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.10.1.3'
      VPNNAME: 'VPN_SIG'
      LEIPV6: ''
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
      GMSI: 60
    set_gtppub_list:
    - PRVEXT: OFF
      ECHOSIG: ALL
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
      POOLSRCPORTSW: ON
      PEERRECOVERYSW: OFF
      PATHDOWNDEASW: OFF
      PATHVERDETECTSW: ON
      DNSGTPCPATHFILTERSW: ON
      LOCRECOVERYSW: ON
      UDPCHKSW: ON
    add_gtpcle_list_1:
    - GROUPID: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.10.1.3'
      VPNNAME: 'VPN_SIG'
      LEIPV6: ''
    set_ugtp_list_1:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
      GMSI: 60
    set_gtppub_list_1:
    - PRVEXT: OFF
      ECHOSIG: ALL
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
      POOLSRCPORTSW: ON
      PEERRECOVERYSW: OFF
      PATHDOWNDEASW: OFF
      PATHVERDETECTSW: ON
      DNSGTPCPATHFILTERSW: ON
      LOCRECOVERYSW: ON
      UDPCHKSW: ON
    add_gtpcintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP: SV
      GRPID: 1
      IMSIPRE: ''
      INTFTP2: ''
      NOID: ''
    set_mscselplcy_list:
    - DNSPLCY: LAI
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'topon.sv.eth7.mnc001.mcc123.org'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.22.133.145'
      IPV4ADDR2: '10.22.133.146'
    add_dnsn_list:
    - FQDN: 'LAC5101.LAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: MSC
      INTYPE: Sv
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置Sv接口业务IP。

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

#### 3.1 配置Sv接口与其他接口共部署时，GTPC本端实体对应的组号配置为0。

##### 3.1.1 配置MME在Sv接口的GTPC IP。

```jinja2
{%- if is_scenario_co_deploy -%}
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
{%- if is_scenario_co_deploy -%}
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
        {%- if item.GMSI is not none -%}
            GMSI={{item.GMSI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_co_deploy -%}
    {%- for item in set_gtppub_list -%}
        SET GTPPUB:
        {#- --- 可选参数 --- -#}
        {%- if item.PRVEXT is not none -%}
            PRVEXT={{item.PRVEXT}},
        {%- endif -%}
        {%- if item.ECHOSIG is not none -%}
            ECHOSIG={{item.ECHOSIG}},
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
        {%- if item.POOLSRCPORTSW is not none -%}
            POOLSRCPORTSW={{item.POOLSRCPORTSW}},
        {%- endif -%}
        {%- if item.PEERRECOVERYSW is not none -%}
            PEERRECOVERYSW={{item.PEERRECOVERYSW}},
        {%- endif -%}
        {%- if item.PATHDOWNDEASW is not none -%}
            PATHDOWNDEASW={{item.PATHDOWNDEASW}},
        {%- endif -%}
        {%- if item.PATHVERDETECTSW is not none -%}
            PATHVERDETECTSW={{item.PATHVERDETECTSW}},
        {%- endif -%}
        {%- if item.DNSGTPCPATHFILTERSW is not none -%}
            DNSGTPCPATHFILTERSW={{item.DNSGTPCPATHFILTERSW}},
        {%- endif -%}
        {%- if item.LOCRECOVERYSW is not none -%}
            LOCRECOVERYSW={{item.LOCRECOVERYSW}},
        {%- endif -%}
        {%- if item.UDPCHKSW is not none -%}
            UDPCHKSW={{item.UDPCHKSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要将Sv接口与其他接口分离部署时，配置Sv接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 配置MME在Sv接口的GTPC IP。

```jinja2
{%- if is_scenario_separate_deploy -%}
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
{%- if is_scenario_separate_deploy -%}
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
        {%- if item.GMSI is not none -%}
            GMSI={{item.GMSI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_separate_deploy -%}
    {%- for item in set_gtppub_list_1 -%}
        SET GTPPUB:
        {#- --- 可选参数 --- -#}
        {%- if item.PRVEXT is not none -%}
            PRVEXT={{item.PRVEXT}},
        {%- endif -%}
        {%- if item.ECHOSIG is not none -%}
            ECHOSIG={{item.ECHOSIG}},
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
        {%- if item.POOLSRCPORTSW is not none -%}
            POOLSRCPORTSW={{item.POOLSRCPORTSW}},
        {%- endif -%}
        {%- if item.PEERRECOVERYSW is not none -%}
            PEERRECOVERYSW={{item.PEERRECOVERYSW}},
        {%- endif -%}
        {%- if item.PATHDOWNDEASW is not none -%}
            PATHDOWNDEASW={{item.PATHDOWNDEASW}},
        {%- endif -%}
        {%- if item.PATHVERDETECTSW is not none -%}
            PATHVERDETECTSW={{item.PATHVERDETECTSW}},
        {%- endif -%}
        {%- if item.DNSGTPCPATHFILTERSW is not none -%}
            DNSGTPCPATHFILTERSW={{item.DNSGTPCPATHFILTERSW}},
        {%- endif -%}
        {%- if item.LOCRECOVERYSW is not none -%}
            LOCRECOVERYSW={{item.LOCRECOVERYSW}},
        {%- endif -%}
        {%- if item.UDPCHKSW is not none -%}
            UDPCHKSW={{item.UDPCHKSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置GTPC接口属性。

```jinja2
{%- if is_scenario_separate_deploy -%}
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

#### 3.3 **可选：**配置Sv接口GTP路径白名单功能。

#### 如果MME与MSC存在不能互通的本端IP和对端IP地址，当SRVCC流程中选择了此类本、对端IP地址对时，SRVCC流程会失败。为保证此种组网下SRVCC流程成功，需要执行本步骤，指定Sv接口允许使用的GTP-C路径，可保证SRVCC流程成功。配置Sv接口GTP路径白名单功能后，本端IP地址选择如下：

##### 3.3.1 如果对端IP地址落入Sv接口GTP路径白名单范围内，只能选择对应白名单内的GTP路径。

##### 3.3.2 如果对端IP地址不在Sv接口GTP路径白名单范围内：

###### 3.3.2.1 - 若配置了Sv接口IP地址分离功能（执行了Sv接口与其他接口分离部署），则从Sv接口IP地址分离的配置中随机选择一个本端IP地址。

###### 3.3.2.2 - 若未配置Sv接口IP地址分离功能，则从3.a配置组号的GTP-C IP中随机选择一个本端IP地址。

### 4 **可选：**配置DNS服务器的数据。

### 如果现网已经完成DNS服务器的数据配置，则无需执行本步骤。

### **ADD DNSLE**命令中：

#### 4.1 配置了GTP-C IP的UNC必须同时配置DNS客户端IP才能进行相关的业务。

#### 4.2 此IP地址为UNC中定义的IP地址。

### 5 配置MSC解析数据。

#### 5.1 设置MSC域名解析策略。

```jinja2
{%- for item in set_mscselplcy_list -%}
    SET MSCSELPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.DNSPLCY is not none -%}
        DNSPLCY={{item.DNSPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 **可选：**增加位置区域DNS域名。

#### 当网络中存在连续的位置区和MSC对应时，建议执行本命令，简化域名配置。

#### 5.3 配置Hostfile记录，包含Hostfile文件的A解析记录及NAPTR解析记录。

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

```jinja2
{%- for item in add_dnsn_list -%}
    ADD DNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
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

