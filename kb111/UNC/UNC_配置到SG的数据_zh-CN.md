---
id: ''
name: 配置到SG的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增SG或SGSN时，在配置完成SGSN到SG的路由数据后，可通过配置M3UA链路数据建立SGSN到SG的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到SG的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增SG或SGSN时，在配置完成SGSN到SG的路由数据后，可通过配置M3UA链路数据建立SGSN到SG的逻辑连接。

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
          description: '增加业务IP。'
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
        DPN:
          name: '子系统号'
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
    add_imsigt_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '配置GT翻译数据。'
          data_source: ''
          pattern: ''
          default: ''
        GT:
          name: '国家代码\_网络接入号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsigt_list_1:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: '配置GT翻译数据。'
          data_source: ''
          pattern: ''
          default: ''
        GT:
          name: '国家代码\_网络接入号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNNAME:
          name: '移动网络名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
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
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        EXCLUSIVEPLMN:
          name: '专属互连PLMN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
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
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.133.95.5'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    set_sigattr_list:
    - IF: INVALID
      IRF: INVALID
      NF: LABEL14
      NRF: LABEL14
      M3UASTPF: DISABLE
      BSSAPPF: DISABLE
      BSSAPPNO: 252
      BSSAPPNI: NAT
      MAPNI: NAT
      SS7T: ITUT_SS7
    add_m3le_list:
    - LEX: 0
      NI: NAT
      OPC: '0x1064'
      LET: ASP
      LEN: 'SGSN_Gr'
    add_m3de_list:
    - DEX: 1
      LEX: 0
      DPC: '0x101a'
      SLSSM: B0000
      DET: SGP
      ADJF: TRUE
      PVER: RFC3332
      DEN: 'SG_A'
    add_m3lks_list:
    - LSX: 1
      DEX: 1
      SLSM: B0001
      WM: ASP
      TM: LOADSHARE
      LSN: 'To SG_A'
    add_m3rt_list:
    - RTX: 1
      DEX: 1
      LSX: 1
      PRI: 0
      RTN: 'To SG_A'
    add_sctppara_list:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'sctppara1'
    add_m3lnk_list:
    - LNK: 1
      VPNNAME: 'VPN_SIG'
      IPT: IPV4
      LOCIPV41: '10.133.95.5'
      LOCIPV42: '10.133.95.6'
      LOCPORT: 2905
      PEERIPV41: '10.10.137.143'
      PEERIPV42: '10.10.137.207'
      PEERPORT: 2905
      CS: C
      LSX: 1
      SCTPINDX: 1
      LKN: 'To SG_A'
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x1064'
      SPN: COREONLY
      SGSNN: '86139000704'
      OPN: 'For Gr'
    add_sccpdpc_list:
    - DPX: 2
      OPX: 1
      DPC: '0x101a'
      LDP: LOADSHARE
      SDPX: 2
      DPN: 'SG_A'
      BDPX: ''
    add_sccpssn_list:
    - SSNX: 0
      SSN: SGSN
      NI: NAT
      DPC: '0x1064'
      OPC: '0x1064'
      SSNNAME: 'SGSN internal'
    add_sccpssn_list_2:
    - SSNX: 7
      SSN: SCMG
      NI: NAT
      DPC: '0x101a'
      OPC: '0x1064'
      SSNNAME: 'TO SG_A'
    add_imsigt_list:
    - IMSIPRE: '46000'
      GT: '86139'
    add_imsigt_list_1:
    - IMSIPRE: '60100'
      GT: '213639'
      MNNAME: 'MOBILE'
    add_hplmn_list:
    - MCC: '460'
      MNC: '00'
      CC: '86'
    add_connectplmn_list:
    - MCC: '601'
      MNC: '00'
      CC: '213'
      NOID: 0
      SM: YES
      SMS: NO
      EXCLUSIVEPLMN: NO
      MAXSMNUM: 11
      SMSCR: NO
    add_sccpgt_list:
    - GTX: 0
      NI: NAT
      RT: DPC
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '86139000704'
      DPC: '0x1064'
      NAME: 'SGSN'
      TT: ANSI9
      NGTX: ''
      SSN: ''
    add_sccpgt_list_1:
    - GTX: 25
      NI: NAT
      RT: DPCGT
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '9'
      DPC: '0x101b'
      NAME: 'TO SG_B'
      TT: ANSI9
      NGTX: ''
      SSN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置SG业务IP。

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

### 3 配置SGSN网元上的本局信令网属性。

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

#### 4.3 本局新增两个相邻的信令点SG A、SG B，配置两条信令链路集，分别到SG A和SG B，链路集的工作模式为ASP，业务模式为负荷分担模式，即到某一目的信令点（如HLR）的信令通过SG A和SG B负荷分担。

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

#### 4.4 配置M3UA路由，分别到SG A和SG B。

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

#### 4.6 配置M3UA信令链路，到SG A和SG B均增加两条M3UA链路，两条信令链路实现负荷分担，并由对应框的物理链路来承载信令链路，每条链路均采用SCTP多归属方式，本地和对端端口号均为2905，本端为客户端模式。

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
        {%- if item.LOCPORT is not none -%}
            LOCPORT={{item.LOCPORT}},
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
    {#- --- 条件必选：LDP=LOADSHARE 时必选 --- -#}
    {%- if item.LDP == 'LOADSHARE' -%}
        SDPX={{item.SDPX}},
    {%- endif -%}
    {#- --- 条件必选：LDP=BACKUP 时必选 --- -#}
    {%- if item.LDP == 'BACKUP' -%}
        BDPX={{item.BDPX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置SCCP本局子系统。

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

#### 5.4 配置到不同SG的SCCP子系统，均为SCMG子系统。

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

### 6 配置GT翻译数据。

#### 6.1 配置到本地HLR的IMSI-GT转换关系。

```jinja2
{%- for item in add_imsigt_list -%}
    ADD IMSIGT:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    GT="{{item.GT}}",
    ;
{%- endfor -%}
```

#### 6.2 配置到外网HLR的IMSI-GT转换关系。

```jinja2
{%- for item in add_imsigt_list_1 -%}
    ADD IMSIGT:
    {#- --- 必选参数 --- -#}
    IMSIPRE="{{item.IMSIPRE}}",
    GT="{{item.GT}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MNNAME is not none -%}
        MNNAME="{{item.MNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.3 配置SGSN归属于一个PLMN。

```jinja2
{%- for item in add_hplmn_list -%}
    ADD HPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.4 配置SGSN归属的PLMN，实现用户在不同PLMN的漫游。

```jinja2
{%- for item in add_connectplmn_list -%}
    ADD CONNECTPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.NOID is not none -%}
        NOID={{item.NOID}},
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.EXCLUSIVEPLMN is not none -%}
        EXCLUSIVEPLMN={{item.EXCLUSIVEPLMN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 为了寻址HLR，需要配置IMSI-GT转换关系。如果本网中规划与多个PLMN中的多个HLR互连，实现在多个不同PLMN之间用户的漫游，需要配置多条IMSI-GT转换关系，并相应配置互联PLMN。

#### 6.5 配置本局GT翻译数据。

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

#### 6.6 配置到SG的GT翻译数据，由于SG A与SG B为负荷分担信令点，DPC为两者之一即可。

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

