---
id: ''
name: 配置到PCF的数据（GGSN/PGW-C/SMF）
ne_type: UNC
type: feature
description: '## 操作场景  当运营商网络中部署了PCF，UNC通过Npcf接口与PCF对接实现对用户的策略控制时，需要在UNC本地配置N7接口与PCF对接。如果网络中没有部署NRF，或对端PCF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置PCF的场景下，还需要在本地配置PCF信息。  **图1** 服务化接口协议栈图  N7接口是服务化接口，服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  **配置建议**  * GGSN/PGW-C/SMF的服务化接口业务IP地址不能和GGSN/PGW-C/SMF其他接口业务IP地址共用。 * GGSN/PGW-C/SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7）","配置到PCF的数据（GGSN/PGW-C/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
## 操作场景当运营商网络中部署了PCF，UNC通过Npcf接口与PCF对接实现对用户的策略控制时，需要在UNC本地配置N7接口与PCF对接。如果网络中没有部署NRF，或对端PCF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置PCF的场景下，还需要在本地配置PCF信息。**图1** 服务化接口协议栈图N7接口是服务化接口，服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。**配置建议*** GGSN/PGW-C/SMF的服务化接口业务IP地址不能和GGSN/PGW-C/SMF其他接口业务IP地址共用。* GGSN/PGW-C/SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81202714 LKV2V6IF01 逻辑接口支持IPv6”。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加PCF实例概述信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: 'IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS3:
          name: 'IPV4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS4:
          name: 'IPV4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPV6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPV6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS3:
          name: 'IPV6地址3'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS4:
          name: 'IPV6地址4'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HTTPS
    add_pnfservice_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加PCF实例服务信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: REGISTERED
    add_pnfplmn_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加PCF的PLMN信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsupi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加PCF的SUPI信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfgpsi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加PCF的GPSI信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置PCF实例支持的服务切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'FFFFFF'
    add_pnfpcfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '增加本地配置的对端PCF实例信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RXDIAMHOST:
          name: 'Rx接口Diameter主机名'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RXDIAMREALM:
          name: 'Rx接口Diameter域名'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置的PCF实例支持的DNN及其归属切片的信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
    set_pccfunc_list:
      type: items
      properties:
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能全局用户动态PCC功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '基于DNN/APN配置PCC开关。  需要灵活选择PCF时，配置“选择PCF方式”参数。可以根据DNN、IMSI、GPSI、S-NSSAIs、PLMN、优选区域（使用**ADD NFPROFILE**命令配置）、ServingScope选择PCF。  例如，根据DNN和NFLOC选择PCF时，需要复选DNN和NFLOC；根据DNN和SUPI选择PCF时，需要复选DNN和SUPI；根据DNN和SERVINGSCOPE选择PCF时，需要复选DNN和SERVINGSCOPE。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCFSELECTMODE:
          name: '选择PCF方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcfsscope_list:
      type: items
      properties:
        SSCOPEID:
          name: '服务区标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: 'SMF需要根据SERVINGSCOPE选择PCF时需要规划。  与PCF向NRF注册时携带的服务区名称相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SSCOPENAME:
          name: '服务区名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrtairange_list:
      type: items
      properties:
        RANGENAME:
          name: '区域名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: 'SMF需要根据SERVINGSCOPE选择PCF时需要规划。  增加用户TAI区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网络码'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcfsscopebind_list:
      type: items
      properties:
        BINDNAME:
          name: '绑定名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: 'SMF需要根据SERVINGSCOPE选择PCF时需要规划。  配置PCF业务服务区与用户TAI区域的绑定关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SSCOPEID:
          name: '服务区标识'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BINDTYPE:
          name: '绑定类型'
          type: string
          enum:
          - USRTAIRANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USRTAIRANGENAME:
          name: '用户TAI区域名称'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置PCF实例的概述信息。当SMF需要根据优选区域选择PCF时，需要通过该命令配置PCF实例的位置信息。  与PCF向NRF注册时携带的位置信息相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALITY:
          name: '位置信息'
          type: string
          minLength: 0
          maxLength: 150
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      NFTYPE: NfPCF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.190'
      PORT: 8080
      FQDN: 'pcf01.node.mnc003.mcc123.3gppnetwork.org'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnfservice_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NpcfSmplcCtrl
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      MCC: '123'
      MNC: '03'
    add_pnfsupi_list:
    - INDEX: 11
      NFINSTANCEID: 'PCF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031340010001'
      RANGEEND: '123031340020001'
      PATTERN: ''
    add_pnfgpsi_list:
    - INDEX: 11
      NFINSTANCEID: 'PCF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031340010001'
      RANGEEND: '123031340020001'
      PATTERN: ''
    add_pnfns_list:
    - INDEX: 11
      NFINSTANCEID: 'PCF_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfpcfinfo_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      RXDIAMHOST: 'huawei.com'
      RXDIAMREALM: 'huawei.com'
    add_pnfdnn_list:
    - INDEX: 11
      NFINSTANCEID: 'PCF_Instance_0'
      DNN: 'huawei.com'
      PNFNSINDEX: 11
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    set_apnpccfunc_list:
    - APN: 'huawei.com'
      HOMEPCCSWITCH: INHERIT
      ROAMPCCSWITCH: INHERIT
      VISITPCCSWITCH: INHERIT
      PCFSELECTMODE: DNN-1&SERVINGSCOPE-1&NFLOC-1
    add_pcfsscope_list:
    - SSCOPEID: 'citya'
      SSCOPENAME: 'City_A'
    add_usrtairange_list:
    - RANGENAME: 'tai1'
      MCC: '123'
      MNC: '03'
      TACSTART: '1234'
      TACEND: '1239'
    add_pcfsscopebind_list:
    - BINDNAME: 'towna'
      SSCOPEID: 'citya'
      BINDTYPE: USRTAIRANGE
      USRTAIRANGENAME: 'tai1'
    add_nfprofile_list:
    - NFINSTANCENAME: 'PCF_Instance_0'
      NFTYPE: NfPCF
      LOCALITY: 'citya.dc1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 GGSN/PGW-C/SMF服务化接口本端信息配置参考配置SBI接口的•配置SMF服务化接口数据步骤。

### 2 **可选：**配置GGSN/PGW-C/SMF基于本地配置选择PCF。

### 用于在网络中没有部署NRF，或对端PCF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置PCF的场景。

#### 2.1 增加PCF实例概述信息。

```jinja2
{%- if is_optional_local_pcf_selection -%}
    {%- for item in add_pnfprofile_list -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.IPADDRESSTYPE is not none -%}
            IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {%- endif -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS2 is not none -%}
                IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS3 is not none -%}
                IPV4ADDRESS3="{{item.IPV4ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS4 is not none -%}
                IPV4ADDRESS4="{{item.IPV4ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS2 is not none -%}
                IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS3 is not none -%}
                IPV6ADDRESS3="{{item.IPV6ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS4 is not none -%}
                IPV6ADDRESS4="{{item.IPV6ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
        {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
            {%- if item.SCHEME is not none -%}
                SCHEME={{item.SCHEME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
        {%- if (item.NFTYPE == 'NfUPF') -%}
            FQDN="{{item.FQDN}}",
        {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
            {%- if item.FQDN is not none -%}
                FQDN="{{item.FQDN}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 增加PCF实例服务信息。

```jinja2
{%- if is_optional_local_pcf_selection -%}
    {%- for item in add_pnfservice_list -%}
        ADD PNFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        SCHEMA={{item.SCHEMA}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 **可选：**增加PCF实例的PLMN信息。

```jinja2
{%- if is_optional_local_pcf_selection and is_optional_pcf_plmn_info -%}
    {%- for item in add_pnfplmn_list -%}
        ADD PNFPLMN:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 **可选：**增加PCF实例的SUPI信息。

```jinja2
{%- if is_optional_local_pcf_selection and is_optional_pcf_supi_info -%}
    {%- for item in add_pnfsupi_list -%}
        ADD PNFSUPI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 **可选：**增加PCF实例的GPSI信息。

```jinja2
{%- if is_optional_local_pcf_selection and is_optional_pcf_gpsi_info -%}
    {%- for item in add_pnfgpsi_list -%}
        ADD PNFGPSI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 **可选：**配置PCF实例支持的服务切片信息。

```jinja2
{%- if is_optional_local_pcf_selection and is_optional_pcf_service_slice_info -%}
    {%- for item in add_pnfns_list -%}
        ADD PNFNS:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SST={{item.SST}},
        {#- --- 可选参数 --- -#}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 增加本地配置的对端PCF实例信息。

```jinja2
{%- if is_optional_local_pcf_selection -%}
    {%- for item in add_pnfpcfinfo_list -%}
        ADD PNFPCFINFO:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        RXDIAMHOST="{{item.RXDIAMHOST}}",
        RXDIAMREALM="{{item.RXDIAMREALM}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 **可选：**配置的PCF实例支持的DNN及其归属切片的信息。

```jinja2
{%- if is_optional_local_pcf_selection and is_optional_pcf_dnn_slice_info -%}
    {%- for item in add_pnfdnn_list -%}
        ADD PNFDNN:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        DNN="{{item.DNN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PNFNSINDEX is not none -%}
            PNFNSINDEX={{item.PNFNSINDEX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 使能全局用户动态PCC功能。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**基于DNN/APN配置PCC开关。需要灵活选择PCF时，配置“选择PCF方式”参数。

```jinja2
{%- if is_optional_dnn_apn_pcc_switch -%}
    {%- for item in set_apnpccfunc_list -%}
        SET APNPCCFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HOMEPCCSWITCH is not none -%}
            HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
        {%- endif -%}
        {%- if item.ROAMPCCSWITCH is not none -%}
            ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
        {%- endif -%}
        {%- if item.VISITPCCSWITCH is not none -%}
            VISITPCCSWITCH={{item.VISITPCCSWITCH}},
        {%- endif -%}
        {%- if item.PCFSELECTMODE is not none -%}
            PCFSELECTMODE={{item.PCFSELECTMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置按ServingScope选择PCF的相关配置。

#### 5.1 配置PCF的业务服务区。

```jinja2
{%- if is_optional_servingscope_pcf_selection -%}
    {%- for item in add_pcfsscope_list -%}
        ADD PCFSSCOPE:
        {#- --- 必选参数 --- -#}
        SSCOPEID="{{item.SSCOPEID}}",
        SSCOPENAME="{{item.SSCOPENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 增加用户TAI区域。

```jinja2
{%- if is_optional_servingscope_pcf_selection -%}
    {%- for item in add_usrtairange_list -%}
        ADD USRTAIRANGE:
        {#- --- 必选参数 --- -#}
        RANGENAME="{{item.RANGENAME}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TACSTART="{{item.TACSTART}}",
        TACEND="{{item.TACEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 配置PCF业务服务区与用户TAI区域的绑定关系。

```jinja2
{%- if is_optional_servingscope_pcf_selection -%}
    {%- for item in add_pcfsscopebind_list -%}
        ADD PCFSSCOPEBIND:
        {#- --- 必选参数 --- -#}
        BINDNAME="{{item.BINDNAME}}",
        SSCOPEID="{{item.SSCOPEID}}",
        BINDTYPE={{item.BINDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：BINDTYPE=USRTAIRANGE 时必选 --- -#}
        {%- if item.BINDTYPE == 'USRTAIRANGE' -%}
            USRTAIRANGENAME="{{item.USRTAIRANGENAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 **可选：**配置按优选区域选择PCF时PCF的位置信息。

```jinja2
{%- if is_optional_preferred_area_pcf_location -%}
    {%- for item in add_nfprofile_list -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOCALITY is not none -%}
            LOCALITY="{{item.LOCALITY}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

