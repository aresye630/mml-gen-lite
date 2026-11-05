---
id: ''
name: 配置和SMSC对接（直连）
ne_type: UNC
type: feature
description: SMSF与SMSC之间采用M3UA进行通信，寻址方式为DPC。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMSF","配置和SMSC对接","配置和SMSC对接（直连）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
SMSF与SMSC之间采用M3UA进行通信，寻址方式为DPC。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经获取网设LLD文档。
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
          description: ''
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
        STPF:
          name: '信令转接点功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
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
        NMD:
          name: '网络模式'
          type: string
          enum:
          - EXCLUSIVE
          - INCLUSIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EXCLUSIVE
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
        PKGERRFAULT:
          name: '错包率故障门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        PKGERRRECOVER:
          name: '错包率恢复门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        MINRECVPKGNUM:
          name: '单偶联最小收包数'
          type: integer
          minimum: 10
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
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
        ASF:
          name: '主备标识'
          type: string
          enum:
          - ACT
          - STD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ACT
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
        CONSTHD:
          name: '拥塞开始门限'
          type: integer
          minimum: 60
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CONETHD:
          name: '拥塞结束门限'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CROSSIP:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        EXCHGMODE:
          name: '交换模式'
          type: string
          enum:
          - DOUBLE
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
    add_mscopc_list:
      type: items
      properties:
        OPX:
          name: 'MSC信令点索引'
          type: integer
          minimum: 1
          maximum: 2
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
        MSCN:
          name: '本局MSC号'
          type: string
          maxLength: 16
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTER:
          name: '是否主用信令点'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_sccpopc_list_2:
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
    add_smsfopc_list:
      type: items
      properties:
        OPX:
          name: 'SMSF信令点索引'
          type: integer
          minimum: 1
          maximum: 10
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
        SMSFN:
          name: '本局SMSF号'
          type: string
          maxLength: 16
          required: true
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
        MASTER:
          name: '是否主用信令点'
          type: string
          enum:
          - NO
          - YES
          required: true
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
        SS7T:
          name: '协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ITUT_SS7
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
        DPN:
          name: '目的信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
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
    add_sccpssn_list_4:
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
    set_smsfssn_list:
      type: items
      properties:
        SSN:
          name: '子系统号'
          type: string
          enum:
          - MSC
          - SGSN
          - VLR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpgt_list:
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
    add_sccpgt_list_2:
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
      SERVICEIPV4: '10.2.180.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list:
    - LEX: 1
      NI: NAT
      OPC: '0x017701'
      LET: ASP
      LEN: 'SMSF1'
    add_m3de_list:
    - DEX: 1
      LEX: 1
      DPC: '0x240011'
      SLSSM: B0000
      STPF: DISABLE
      DET: SP
      ADJF: TRUE
      NMD: EXCLUSIVE
      PVER: RFC3332
      DEN: 'SMSC1'
    add_m3lks_list:
    - LSX: 1
      DEX: 1
      SLSM: B0011
      WM: ASP
      TM: LOADSHARE
      LSN: 'SMSC1'
    add_m3rt_list:
    - RTX: 1
      DEX: 1
      LSX: 1
      PRI: 0
      RTN: 'SMSC1'
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      SCTPPARANAME: 'sctname'
      PKGERRFAULT: 5
      PKGERRRECOVER: 3
      MINRECVPKGNUM: 100
    add_m3lnk_list:
    - LNK: 1
      VPNNAME: 'VPN_SIG'
      IPT: IPV4
      LOCIPV41: '10.2.180.1'
      LOCIPV42: '10.2.180.2'
      LOCPORT: 17171
      PEERIPV41: '10.50.0.202'
      PEERIPV42: '10.50.0.203'
      PEERPORT: 17171
      CS: C
      LSX: 1
      ASF: ACT
      PRI: 0
      CONSTHD: 80
      CONETHD: 40
      CROSSIP: NO
      EXCHGMODE: SINGLE
      LKN: 'To SMSC1'
      SCTPINDX: 0
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x17701'
      SPN: COREONLY
      SGSNN: '861390211101'
      OPN: 'SMSF1'
    add_mscopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x17701'
      MSCN: '861390211101'
      MASTER: YES
    add_sccpopc_list_2:
    - OPX: 1
      NI: NAT
      OPC: '0x17701'
      SPN: COREONLY
      SGSNN: '861390211101'
      OPN: 'SMSF1'
    add_smsfopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x17702'
      SMSFN: '861390211101'
      OPN: 'SMSF1'
      MASTER: YES
    add_sccpdpc_list:
    - DPX: 1
      OPX: 1
      DPC: '0x240011'
      SS7T: ITUT_SS7
      LDP: BACKUP
      BDPX: 2
      DPN: 'SMSC1'
      SDPX: ''
    add_sccpssn_list:
    - SSNX: 1
      SSN: SCMG
      NI: NAT
      DPC: '0x017701'
      OPC: '0x017701'
      SSNNAME: 'SGSN_BER1-SSN'
    add_sccpssn_list_2:
    - SSNX: 5
      SSN: SCMG
      NI: NAT
      DPC: '0x240011'
      OPC: '0x017701'
      SSNNAME: 'SCMG-SSN1'
    add_sccpssn_list_4:
    - SSNX: 7
      SSN: MSC
      NI: NAT
      DPC: '0x240011'
      OPC: '0x017701'
      SSNNAME: 'MSC-SSN1'
    set_smsfssn_list:
    - SSN: MSC
    add_sccpgt_list:
    - GTX: 1
      NI: NAT
      RT: DPC
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '861390211101'
      DPC: '0x17701'
      NAME: 'SGSN_BER1-GT'
      TT: ANSI9
      NGTX: ''
      SSN: ''
    add_sccpgt_list_2:
    - GTX: 3
      NI: NAT
      RT: DPCGT
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '86139177010000'
      DPC: '0x240011'
      NAME: 'SMSC'
      TT: ANSI9
      NGTX: ''
      SSN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 增加SMSF业务接口IP地址，用于和SMSC的对接。

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

### 3 配置M3UA信令数据。

#### 3.1 增加M3UA本地实体，信令点编码所在的网络为国内网，本地实体为ASP。

```jinja2
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
```

#### 3.2 配置M3UA目的信令点。

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
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.NMD is not none -%}
        NMD={{item.NMD}},
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

#### 3.3 配置到SMSC的M3UA信令链路集。

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

#### 3.4 配置M3UA信令路由。

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

#### 3.5 配置SCTP协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    {%- if item.PKGERRFAULT is not none -%}
        PKGERRFAULT={{item.PKGERRFAULT}},
    {%- endif -%}
    {%- if item.PKGERRRECOVER is not none -%}
        PKGERRRECOVER={{item.PKGERRRECOVER}},
    {%- endif -%}
    {%- if item.MINRECVPKGNUM is not none -%}
        MINRECVPKGNUM={{item.MINRECVPKGNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置M3UA信令链路。

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
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.ASF is not none -%}
        ASF={{item.ASF}},
    {%- endif -%}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.CONSTHD is not none -%}
        CONSTHD={{item.CONSTHD}},
    {%- endif -%}
    {%- if item.CONETHD is not none -%}
        CONETHD={{item.CONETHD}},
    {%- endif -%}
    {%- if item.CROSSIP is not none -%}
        CROSSIP={{item.CROSSIP}},
    {%- endif -%}
    {%- if item.EXCHGMODE is not none -%}
        EXCHGMODE={{item.EXCHGMODE}},
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
```

### 4 配置SCCP信令数据。

#### 4.1 配置SCCP本局信令点。

##### 4.1.1 适用于2/3G短消息。

```jinja2
{%- if is_scenario_2g_3g_sms -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_2g_3g_sms -%}
    {%- for item in add_mscopc_list -%}
        ADD MSCOPC:
        {#- --- 必选参数 --- -#}
        OPX={{item.OPX}},
        NI={{item.NI}},
        OPC="{{item.OPC}}",
        MSCN="{{item.MSCN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MASTER is not none -%}
            MASTER={{item.MASTER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 适用于5G短消息。

```jinja2
{%- if is_scenario_5g_sms -%}
    {%- for item in add_sccpopc_list_2 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_5g_sms -%}
    {%- for item in add_smsfopc_list -%}
        ADD SMSFOPC:
        {#- --- 必选参数 --- -#}
        OPX={{item.OPX}},
        NI={{item.NI}},
        OPC="{{item.OPC}}",
        SMSFN="{{item.SMSFN}}",
        MASTER={{item.MASTER}},
        {#- --- 可选参数 --- -#}
        {%- if item.OPN is not none -%}
            OPN="{{item.OPN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置SCCP目的信令点。

```jinja2
{%- for item in add_sccpdpc_list -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
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

#### 4.3 配置SCCP本局子系统。

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

#### 4.4 配置对端SMSC的SCCP子系统。

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

##### 4.4.1 //如果SMSC需要使用SSN号寻址则需要配置下面的脚本。

```jinja2
{%- for item in add_sccpssn_list_4 -%}
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

#### 4.5 配置SCCP层主叫地址中携带的SSN号。

```jinja2
{%- for item in set_smsfssn_list -%}
    SET SMSFSSN:
    {#- --- 可选参数 --- -#}
    {%- if item.SSN is not none -%}
        SSN={{item.SSN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置GT翻译数据。

#### 5.1 配置本局SCCP GT翻译数据。

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

#### 5.2 配置SMSC的SCCP GT翻译数据。

```jinja2
{%- for item in add_sccpgt_list_2 -%}
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

