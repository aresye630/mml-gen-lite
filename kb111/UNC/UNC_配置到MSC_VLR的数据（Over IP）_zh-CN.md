---
id: ''
name: 配置到MSC/VLR的数据（Over IP）
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MSC/VLR或SGSN时，在配置完成SGSN到MSC/VLR的路由数据后，可通过配置M3UA链路数据建立SGSN到MSC/VLR的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到MSC/VLR的数据","配置到MSC/VLR的数据（Over IP）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MSC/VLR或SGSN时，在配置完成SGSN到MSC/VLR的路由数据后，可通过配置M3UA链路数据建立SGSN到MSC/VLR的逻辑连接。

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
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '打开支持Gs接口特性的License配置开关。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: '配置本局信令网属性。'
          data_source: ''
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
          description: '配置MSC/VLR业务IP。'
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
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NA:
          name: '网络外貌'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
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
        RC:
          name: '路由上下文'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
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
        SGSNN:
          name: '本局SGSN号'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sccpdpc_list:
      type: items
      properties:
        DPX:
          name: '目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: '配置SCCP信令数据。'
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
        DPN:
          name: '子系统号'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
          description: '配置SCCP信令数据。'
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
    add_sccpgt_list:
      type: items
      properties:
        GTX:
          name: 'GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '配置GT翻译数据。'
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
        RT:
          name: '翻译结果类型'
          type: string
          enum:
          - DPC
          - DPCGT
          - DPCNEWGT
          - DPCSSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTEXP:
          name: 'GT码表示语'
          type: string
          enum:
          - FOUR
          - SIX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FOUR
        NP:
          name: '编号计划'
          type: string
          enum:
          - DATA
          - ISDNMS
          - ISDNP
          - PMS
          - SMS
          - TELEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ISDNP
        ADDREXP:
          name: '地址性质表示语'
          type: string
          enum:
          - FREE
          - INTDN
          - NSU
          - NVU
          - SUBDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INTDN
        ADDR:
          name: '地址信息'
          type: string
          maxLength: 20
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
        NAME:
          name: 'SCCP GT名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        TT:
          name: '翻译类型'
          type: string
          enum:
          - ANSI10
          - ANSI9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANSI9
        NGTX:
          name: '新GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpgt_list_1:
      type: items
      properties:
        GTX:
          name: 'GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
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
        RT:
          name: '翻译结果类型'
          type: string
          enum:
          - DPC
          - DPCGT
          - DPCNEWGT
          - DPCSSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTEXP:
          name: 'GT码表示语'
          type: string
          enum:
          - FOUR
          - SIX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FOUR
        NP:
          name: '编号计划'
          type: string
          enum:
          - DATA
          - ISDNMS
          - ISDNP
          - PMS
          - SMS
          - TELEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ISDNP
        ADDR:
          name: '地址信息'
          type: string
          maxLength: 20
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
        NAME:
          name: 'SCCP GT名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ADDREXP:
          name: '地址性质表示语'
          type: string
          enum:
          - FREE
          - INTDN
          - NSU
          - NVU
          - SUBDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INTDN
        TT:
          name: '翻译类型'
          type: string
          enum:
          - ANSI10
          - ANSI9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANSI9
        NGTX:
          name: '新GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vlr_list:
      type: items
      properties:
        VN:
          name: 'VLR号'
          type: string
          maxLength: 15
          required: true
          description: '配置VLR相关数据。'
          data_source: ''
          pattern: ''
          default: ''
        VNM:
          name: 'VLR名称'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_laivlr_list:
      type: items
      properties:
        BGNLAI:
          name: 'LAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLRNO:
          name: 'VLR号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nra_list:
      type: items
      properties:
        LAI:
          name: 'LAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: 'RAC'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2GSINTF02'
      SWITCH: ENABLE
    set_sigattr_list:
    - IF: LABEL24
      IRF: LABEL14
      NF: LABEL14
      NRF: LABEL14
      M3UASTPF: DISABLE
      BSSAPPF: ENABLE
      BSSAPPNO: 252
      BSSAPPNI: DISUSED
      MAPNI: NAT
      SS7T: ITUT_SS7
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.151.113'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list:
    - LEX: 0
      NI: NAT
      OPC: '0x1064'
      LET: IPSP
      RC: 123456
      NA: 789456
      LEN: 'SGSN_Gs'
    add_m3de_list:
    - DEX: 0
      LEX: 0
      DPC: '0x106a'
      SLSSM: B0000
      DET: IPSP
      ADJF: TRUE
      RC: 123456
      PVER: RFC3332
      DEN: 'MSC'
    add_m3lks_list:
    - LSX: 0
      DEX: 0
      SLSM: B0001
      WM: IPSP
      TM: LOADSHARE
      LSN: 'To MSC'
    add_m3rt_list:
    - RTX: 0
      DEX: 0
      LSX: 0
      PRI: 0
      RTN: 'To MSC'
    add_m3lnk_list:
    - LNK: 1
      VPNNAME: 'VPN_SIG'
      IPT: IPV4
      LOCIPV41: '10.10.151.113'
      LOCIPV42: '10.10.151.114'
      PEERIPV41: '10.22.133.143'
      PEERIPV42: '10.22.133.144'
      PEERPORT: 2905
      CS: C
      LSX: 0
      SCTPINDX: 2
      LKN: 'To MSC/VLR'
      LOCPORT: 2906
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x1064'
      SPN: COREONLY
      SGSNN: '8613912345'
      OPN: 'TO RNC AND SS7'
    add_sccpdpc_list:
    - DPX: 1
      OPX: 1
      DPC: '0x106a'
      DPN: 'MSC'
      LDP: NOUSE
      BDPX: ''
      SDPX: ''
    add_sccpssn_list:
    - SSNX: 1
      SSN: SCMG
      NI: NAT
      DPC: '0x1064'
      OPC: '0x1064'
      SSNNAME: 'SGSN internal'
    add_sccpssn_list_2:
    - SSNX: 3
      SSN: SCMG
      NI: NAT
      DPC: '0x106a'
      OPC: '0x1064'
      SSNNAME: 'TO MSC'
    add_sccpgt_list:
    - GTX: 0
      NI: NAT
      RT: DPC
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '8613912345'
      DPC: '0x1064'
      NAME: 'SGSN'
      TT: ANSI9
      NGTX: ''
      SSN: ''
    add_sccpgt_list_1:
    - GTX: 1
      NI: NAT
      RT: DPC
      GTEXP: FOUR
      NP: ISDNP
      ADDR: '861390111'
      DPC: '0x106a'
      NAME: 'TO MSC'
      ADDREXP: INTDN
      TT: ANSI9
      NGTX: ''
      SSN: ''
    add_vlr_list:
    - VN: '861390111'
      VNM: 'noname'
    add_laivlr_list:
    - BGNLAI: '460001234'
      VLRNO: '861390111'
    add_nra_list:
    - LAI: '460001234'
      RAC: '01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开支持Gs接口特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置本局信令属性。

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

### 4 **可选：**配置MSC/VLR业务IP。

```jinja2
{%- if is_optional_service_ip -%}
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
{%- endif -%}
```

### 5 配置M3UA信令数据。

#### 5.1 配置M3UA本地实体。

```jinja2
{%- for item in add_m3le_list -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.RC is not none -%}
        RC={{item.RC}},
    {%- endif -%}
    {%- if item.NA is not none -%}
        NA={{item.NA}},
    {%- endif -%}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置M3UA目的实体。

```jinja2
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
    {%- if item.RC is not none -%}
        RC={{item.RC}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置到MSC/VLR的信令链路集。

```jinja2
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
```

#### 5.4 配置到MSC/VLR的M3UA路由。

```jinja2
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
```

#### 5.5 配置M3UA信令链路。

```jinja2
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
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
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
```

### 6 配置SCCP信令数据。

#### 6.1 增加SCCP本局信令点。

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

#### 6.2 配置SCCP目的信令点。

```jinja2
{%- for item in add_sccpdpc_list -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DPN is not none -%}
        DPN="{{item.DPN}}",
    {%- endif -%}
    {%- if item.LDP is not none -%}
        LDP={{item.LDP}},
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

#### 6.3 增加SCCP本局子系统。

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

#### 6.4 配置SCCP子系统。

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

### 7 配置GT翻译数据

#### 7.1 增加本局GT翻译数据。

```jinja2
{%- for item in add_sccpgt_list -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    GTX={{item.GTX}},
    NI={{item.NI}},
    RT={{item.RT}},
    ADDR="{{item.ADDR}}",
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GTEXP is not none -%}
        GTEXP={{item.GTEXP}},
    {%- endif -%}
    {%- if item.NAME is not none -%}
        NAME="{{item.NAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RT=DPCNEWGT 时必选 --- -#}
    {%- if item.RT == 'DPCNEWGT' -%}
        NGTX={{item.NGTX}},
    {%- endif -%}
    {#- --- 条件必选：RT=DPCSSN 时必选 --- -#}
    {%- if item.RT == 'DPCSSN' -%}
        SSN={{item.SSN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.NP is not none -%}
            NP={{item.NP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.ADDREXP is not none -%}
            ADDREXP={{item.ADDREXP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=SIX 时可选 --- -#}
    {%- if item.GTEXP == 'SIX' -%}
        {%- if item.TT is not none -%}
            TT={{item.TT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.2 配置到MSC/VLR的GT翻译数据，翻译结果类型为DPC。

```jinja2
{%- for item in add_sccpgt_list_1 -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    GTX={{item.GTX}},
    NI={{item.NI}},
    RT={{item.RT}},
    ADDR="{{item.ADDR}}",
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GTEXP is not none -%}
        GTEXP={{item.GTEXP}},
    {%- endif -%}
    {%- if item.NAME is not none -%}
        NAME="{{item.NAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RT=DPCNEWGT 时必选 --- -#}
    {%- if item.RT == 'DPCNEWGT' -%}
        NGTX={{item.NGTX}},
    {%- endif -%}
    {#- --- 条件必选：RT=DPCSSN 时必选 --- -#}
    {%- if item.RT == 'DPCSSN' -%}
        SSN={{item.SSN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.NP is not none -%}
            NP={{item.NP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.ADDREXP is not none -%}
            ADDREXP={{item.ADDREXP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=SIX 时可选 --- -#}
    {%- if item.GTEXP == 'SIX' -%}
        {%- if item.TT is not none -%}
            TT={{item.TT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置VLR相关数据。

#### 8.1 配置VLR的号码。

```jinja2
{%- for item in add_vlr_list -%}
    ADD VLR:
    {#- --- 必选参数 --- -#}
    VN="{{item.VN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VNM is not none -%}
        VNM="{{item.VNM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 8.2 配置VLR的位置区。

```jinja2
{%- for item in add_laivlr_list -%}
    ADD LAIVLR:
    {#- --- 必选参数 --- -#}
    BGNLAI="{{item.BGNLAI}}",
    VLRNO="{{item.VLRNO}}",
    ;
{%- endfor -%}
```

#### 8.3 增加一个路由区标识为460001234的空路由区。

```jinja2
{%- for item in add_nra_list -%}
    ADD NRA:
    {#- --- 必选参数 --- -#}
    LAI="{{item.LAI}}",
    RAC="{{item.RAC}}",
    ;
{%- endfor -%}
```

