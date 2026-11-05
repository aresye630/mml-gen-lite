---
id: ''
name: 配置到RNC的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增RNC或SGSN时，在配置完成SGSN到RNC的路由数据后，可通过配置Iu接口数据建立SGSN到RNC的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到RNC的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增RNC或SGSN时，在配置完成SGSN到RNC的路由数据后，可通过配置Iu接口数据建立SGSN到RNC的逻辑连接。

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
    set_sigattr_list:
      type: items
      properties:
        IF:
          name: '国际网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: '配置信令网属性。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        IRF:
          name: '国际备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NF:
          name: '国内网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRF:
          name: '国内备用网标志'
          type: string
          enum:
          - INVALID
          - LABEL14
          - LABEL24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        M3UASTPF:
          name: 'M3UA STP功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPF:
          name: '是否支持BSSAP+'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNO:
          name: 'BSSAP+子系统号'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BSSAPPNI:
          name: 'BSSAP+所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAPNI:
          name: 'MAP所在信令网'
          type: string
          enum:
          - DISUSED
          - INT
          - INTB
          - NAT
          - NATB
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '信令网协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
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
          description: '配置Iu接口业务IP。'
          data_source: ''
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
    add_m3le_list:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '配置M3UA信令数据。'
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lks_list:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TM:
          name: '业务模式'
          type: string
          enum:
          - LOADSHARE
          - OVERRIDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOADSHARE
        LSN:
          name: '链路集名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3rt_list:
      type: items
      properties:
        RTX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        RTN:
          name: '信令路由名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sctppara_list:
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
    add_m3lnk_list:
      type: items
      properties:
        LNK:
          name: '链路号'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
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
        IPT:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERIPV41:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV42:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        CS:
          name: 'C/S模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPINDX:
          name: 'SCTP 参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        LOCIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV61:
          name: '对端IP地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV62:
          name: '对端IP地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpopc_list:
      type: items
      properties:
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '配置SCCP信令数据。'
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: '信令点用途'
          type: string
          enum:
          - COREONLY
          - IUANDCORE
          - IUONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: COREONLY
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SGSNN:
          name: '本局SGSN号'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpdpc_list:
      type: items
      properties:
        DPX:
          name: '目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LDP:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - LOADSHARE
          - MULTIDPCLOADSHARE
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOUSE
        DPN:
          name: '目的信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        BDPX:
          name: '备用目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDPX:
          name: '负荷分担目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpssn_list:
      type: items
      properties:
        SSNX:
          name: '子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSNNAME:
          name: '子系统名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sccpssn_list_2:
      type: items
      properties:
        SSNX:
          name: '子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSNNAME:
          name: '子系统名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置RNC相关信息。'
          data_source: ''
          pattern: ''
          default: ''
        RNCN:
          name: 'RNC名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCID:
          name: 'RNC标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R6
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_iupaging_list:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_serviceip_list_4:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Iu接口用户面通道。'
          data_source: ''
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
    add_gtpule_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
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
  examples:
    set_sigattr_list:
    - IF: INVALID
      IRF: INVALID
      NF: LABEL24
      NRF: LABEL14
      M3UASTPF: DISABLE
      BSSAPPF: DISABLE
      BSSAPPNO: 252
      BSSAPPNI: NAT
      MAPNI: NAT
      SS7T: ITUT_SS7
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.29.147.113'
      VPNINSTNAME: 'VPN_Access'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list:
    - LEX: 0
      NI: NAT
      OPC: '0x1065'
      LET: IPSP
      LEN: 'SGSN_Iu-C'
    add_m3de_list:
    - DEX: 10
      LEX: 0
      DPC: '0x1094'
      SLSSM: B0000
      DET: IPSP
      ADJF: TRUE
      PVER: RFC3332
      DEN: 'RNC'
    add_m3lks_list:
    - LSX: 10
      DEX: 10
      SLSM: B0001
      WM: IPSP
      TM: LOADSHARE
      LSN: 'To RNC'
    add_m3rt_list:
    - RTX: 10
      DEX: 10
      LSX: 10
      PRI: 0
      RTN: 'To RNC'
    add_sctppara_list:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'sctppara1'
    add_m3lnk_list:
    - LNK: 0
      VPNNAME: 'VPN_Access'
      IPT: IPV4
      LOCIPV41: '10.29.147.113'
      LOCIPV42: '10.29.147.116'
      PEERIPV41: '10.29.139.141'
      PEERIPV42: '10.29.139.205'
      PEERPORT: 2905
      CS: C
      LSX: 10
      SCTPINDX: 1
      LKN: 'To RNC_0'
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x1065'
      SPN: IUONLY
      OPN: 'For Iu-C'
      SGSNN: ''
    add_sccpdpc_list:
    - DPX: 4
      OPX: 1
      DPC: '0x1094'
      LDP: NOUSE
      DPN: 'RNC'
      BDPX: ''
      SDPX: ''
    add_sccpssn_list:
    - SSNX: 1
      SSN: RANAP
      NI: NAT
      DPC: '0x1065'
      OPC: '0x1065'
      SSNNAME: 'SGSN'
    add_sccpssn_list_2:
    - SSNX: 5
      SSN: RANAP
      NI: NAT
      DPC: '0x1094'
      OPC: '0x1065'
      SSNNAME: 'RNC'
    add_rnc_list:
    - RNCX: 0
      RNCN: 'shanghai_RNC'
      RNCMCC: '460'
      RNCMNC: '00'
      RNCID: 3
      NI: NAT
      SPC: '0x1094'
      RNCVER: R5
      OFUTRAN: NO
      SPID: NO
    add_iupaging_list:
    - LAI: '460001155'
      RAC: '0x01'
      RNCINDEX: 0
    add_serviceip_list_4:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.29.147.131'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_gtpule_list:
    - GROUPID: 32
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '10.29.147.131'
      VPNNAME: 'VPN_CN'
      LEIPV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置本局信令属性。

```jinja2
{%- for item in set_sigattr_list -%}
    SET SIGATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.IF is not none -%}
        IF={{item.IF}},
    {%- endif -%}
    {%- if item.IRF is not none -%}
        IRF={{item.IRF}},
    {%- endif -%}
    {%- if item.NF is not none -%}
        NF={{item.NF}},
    {%- endif -%}
    {%- if item.NRF is not none -%}
        NRF={{item.NRF}},
    {%- endif -%}
    {%- if item.M3UASTPF is not none -%}
        M3UASTPF={{item.M3UASTPF}},
    {%- endif -%}
    {%- if item.BSSAPPF is not none -%}
        BSSAPPF={{item.BSSAPPF}},
    {%- endif -%}
    {%- if item.BSSAPPNO is not none -%}
        BSSAPPNO={{item.BSSAPPNO}},
    {%- endif -%}
    {%- if item.BSSAPPNI is not none -%}
        BSSAPPNI={{item.BSSAPPNI}},
    {%- endif -%}
    {%- if item.MAPNI is not none -%}
        MAPNI={{item.MAPNI}},
    {%- endif -%}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Iu接口业务IP。

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

### 4 **可选：**配置M3UA信令数据。

#### 4.1 配置M3UA本地实体。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_m3le_list -%}
        ADD M3LE:
        {#- --- 必选参数 --- -#}
        LEX={{item.LEX}},
        NI={{item.NI}},
        OPC="{{item.OPC}}",
        LET={{item.LET}},
        {#- --- 可选参数 --- -#}
        {%- if item.LEN is not none -%}
            LEN="{{item.LEN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置M3UA目的实体。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_m3de_list -%}
        ADD M3DE:
        {#- --- 必选参数 --- -#}
        DEX={{item.DEX}},
        LEX={{item.LEX}},
        DPC="{{item.DPC}}",
        DET={{item.DET}},
        {#- --- 可选参数 --- -#}
        {%- if item.SLSSM is not none -%}
            SLSSM={{item.SLSSM}},
        {%- endif -%}
        {%- if item.ADJF is not none -%}
            ADJF={{item.ADJF}},
        {%- endif -%}
        {%- if item.PVER is not none -%}
            PVER={{item.PVER}},
        {%- endif -%}
        {%- if item.DEN is not none -%}
            DEN="{{item.DEN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置M3UA信令链路集。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_m3lks_list -%}
        ADD M3LKS:
        {#- --- 必选参数 --- -#}
        LSX={{item.LSX}},
        DEX={{item.DEX}},
        WM={{item.WM}},
        {#- --- 可选参数 --- -#}
        {%- if item.SLSM is not none -%}
            SLSM={{item.SLSM}},
        {%- endif -%}
        {%- if item.TM is not none -%}
            TM={{item.TM}},
        {%- endif -%}
        {%- if item.LSN is not none -%}
            LSN="{{item.LSN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置M3UA路由。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_m3rt_list -%}
        ADD M3RT:
        {#- --- 必选参数 --- -#}
        RTX={{item.RTX}},
        DEX={{item.DEX}},
        LSX={{item.LSX}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRI is not none -%}
            PRI={{item.PRI}},
        {%- endif -%}
        {%- if item.RTN is not none -%}
            RTN="{{item.RTN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置SCTP协议参数。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_sctppara_list -%}
        ADD SCTPPARA:
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

#### 4.6 配置M3UA信令链路。

```jinja2
{%- if is_optional_m3ua_signaling_data -%}
    {%- for item in add_m3lnk_list -%}
        ADD M3LNK:
        {#- --- 必选参数 --- -#}
        LNK={{item.LNK}},
        CS={{item.CS}},
        LSX={{item.LSX}},
        SCTPINDX={{item.SCTPINDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {%- if item.IPT is not none -%}
            IPT={{item.IPT}},
        {%- endif -%}
        {%- if item.PEERPORT is not none -%}
            PEERPORT={{item.PEERPORT}},
        {%- endif -%}
        {%- if item.LKN is not none -%}
            LKN="{{item.LKN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            LOCIPV41="{{item.LOCIPV41}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            PEERIPV41="{{item.PEERIPV41}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            LOCIPV61="{{item.LOCIPV61}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            PEERIPV61="{{item.PEERIPV61}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            {%- if item.LOCIPV42 is not none -%}
                LOCIPV42="{{item.LOCIPV42}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            {%- if item.PEERIPV42 is not none -%}
                PEERIPV42="{{item.PEERIPV42}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            {%- if item.LOCIPV62 is not none -%}
                LOCIPV62="{{item.LOCIPV62}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
        {%- if item.IPT == 'IPV6' -%}
            {%- if item.PEERIPV62 is not none -%}
                PEERIPV62="{{item.PEERIPV62}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置SCCP信令数据。

#### 5.1 配置SCCP本局信令点。

```jinja2
{%- for item in add_sccpopc_list -%}
    ADD SCCPOPC:
    {#- --- 必选参数 --- -#}
    OPX={{item.OPX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.OPN is not none -%}
        OPN="{{item.OPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SPN=COREONLY/IUANDCORE 时必选 --- -#}
    {%- if item.SPN in ['COREONLY', 'IUANDCORE'] -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置SCCP目的信令点。

```jinja2
{%- for item in add_sccpdpc_list -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LDP is not none -%}
        LDP={{item.LDP}},
    {%- endif -%}
    {%- if item.DPN is not none -%}
        DPN="{{item.DPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LDP=BACKUP 时必选 --- -#}
    {%- if item.LDP == 'BACKUP' -%}
        BDPX={{item.BDPX}},
    {%- endif -%}
    {#- --- 条件必选：LDP=LOADSHARE 时必选 --- -#}
    {%- if item.LDP == 'LOADSHARE' -%}
        SDPX={{item.SDPX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置本局SCCP子系统。

```jinja2
{%- for item in add_sccpssn_list -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNX={{item.SSNX}},
    SSN={{item.SSN}},
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSNNAME is not none -%}
        SSNNAME="{{item.SSNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 配置SCCP子系统。

```jinja2
{%- for item in add_sccpssn_list_2 -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNX={{item.SSNX}},
    SSN={{item.SSN}},
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSNNAME is not none -%}
        SSNNAME="{{item.SSNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置RNC相关信息。

#### 6.1 配置RNC信息。

```jinja2
{%- for item in add_rnc_list -%}
    ADD RNC:
    {#- --- 必选参数 --- -#}
    RNCX={{item.RNCX}},
    RNCMCC="{{item.RNCMCC}}",
    RNCMNC="{{item.RNCMNC}}",
    RNCID={{item.RNCID}},
    NI={{item.NI}},
    SPC="{{item.SPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RNCN is not none -%}
        RNCN="{{item.RNCN}}",
    {%- endif -%}
    {%- if item.RNCVER is not none -%}
        RNCVER={{item.RNCVER}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
    {%- if item.RNCVER == 'R9+' -%}
        {%- if item.OFUTRAN is not none -%}
            OFUTRAN={{item.OFUTRAN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
    {%- if item.RNCVER in ['R8', 'R9+'] -%}
        {%- if item.SPID is not none -%}
            SPID={{item.SPID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置3G寻呼表。

```jinja2
{%- for item in add_iupaging_list -%}
    ADD IUPAGING:
    {#- --- 必选参数 --- -#}
    LAI="{{item.LAI}}",
    RAC="{{item.RAC}}",
    RNCINDEX={{item.RNCINDEX}},
    ;
{%- endfor -%}
```

### 7 配置Iu接口用户面通道。

#### 7.1 增加业务IP。

```jinja2
{%- for item in add_serviceip_list_4 -%}
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

#### 7.2 增加GTPU本地实体。

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

