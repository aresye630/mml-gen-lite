---
id: ''
name: 配置SMF服务化接口数据（N10/N11/N7）
ne_type: UEG
type: feature
description: '**接口介绍**  SMF的服务化接口为Nsmf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。  **表1** 服务化接口与参考点模式对应关系  | 参考点 | 网元间的交互 | 服务化接口 | | --- | --- | --- | | N10 | SMF<->UDM | Nsmf、Nudm | | N11 | AMF<->SMF | Namf、Nsmf |  **图1** 服务化接口协议栈图  服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  园区风筝M有两种运行模式：  * 正常模式：中心侧SMF对接中心侧UDM。 * 应急模式：应急SMF与园区内本地DC的UDM对接，使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。  本文配置仅关注应急SMF的配置。  **配置建议**  * SMF的服务化接口业务IP地址不能和SMF其他接口业务IP地址共用。 * SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。'
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置SMF","配置SMF服务化接口数据（N10/N11/N7）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**接口介绍**SMF的服务化接口为Nsmf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。**表1** 服务化接口与参考点模式对应关系| 参考点 | 网元间的交互 | 服务化接口 || --- | --- | --- || N10 | SMF<->UDM | Nsmf、Nudm || N11 | AMF<->SMF | Namf、Nsmf |**图1** 服务化接口协议栈图服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。园区风筝M有两种运行模式：* 正常模式：中心侧SMF对接中心侧UDM。* 应急模式：应急SMF与园区内本地DC的UDM对接，使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。本文配置仅关注应急SMF的配置。**配置建议*** SMF的服务化接口业务IP地址不能和SMF其他接口业务IP地址共用。* SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成部署组网路由配置。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Nsmf接口的逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '服务化接口规划两个IP地址，SMF作为客户端一个，作为服务端一个。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '配置Nsmf接口的HTTP本端端点组信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_httple_list:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置HTTP本端端点信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '与**ADD LOGICIP**命令中配置的IP地址需保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sbiaple_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置本端服务化接口接入点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeMBSMF
          - NFTypeNWDAF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端AMF实例概述信息。  “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。  风筝M园区双DC组网，本DC的应急SMF仅连接本DC内的AMF，因此本DC内配置仅有一个对端实例。'
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
          description: '配置对接的对端AMF的IP地址。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfservice_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端AMF的服务实例信息。'
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
          description: '增加对端AMF的PLMN信息，可以基于PLMN发现AMF。'
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
    add_pnfprofile_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端UDM实例概述信息。  园区双DC组网，本DC的应急SMF仅连接本DC内的UDM，因此本DC内配置仅有一个对端实例。'
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
          description: '-'
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
          description: '-'
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
          description: '配置对接的对端UDM的IP地址。'
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
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '双DC内的UDM的**PRIORITY**取值可以设置相同或不同，两者之间没有组网关系。'
          data_source: ''
          pattern: ''
          default: ''
    add_pnfservice_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端UDM的服务实例信息。'
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
    add_pnfplmn_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端UDM的实例信息，可以基于PLMN选择UDM。'
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
          description: '配置对端UDM支持的SUPI信息，可以基于SUPI选择UDM。'
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
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端UDM实例支持的服务切片信息，可以基于切片选择UDM。'
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
    set_chargectrl_list:
      type: items
      properties:
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.16.0.4'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR Server SBI'
    - IPVERSION: IPv4
      LOGICIPV4: '10.16.0.6'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR Server SBI'
    add_httplegrp_list:
    - INDEX: 2
      DESC: 'SMF'
    - INDEX: 2
      DESC: 'SMF'
    add_httple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 2
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.16.0.4'
      PORT: 8080
      VPNNAME: 'VPN_CN'
      TLSFLG: NO
      DESC: 'SMF Server'
    - INDEX: 3
      HTTPLEGRPIDX: 2
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.16.0.6'
      PORT: 8080
      VPNNAME: 'VPN_CN'
      TLSFLG: NO
      DESC: 'SMF Server'
    add_sbiaple_list:
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeSMF
      DESCRIPTION: 'SMF'
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeSMF
      DESCRIPTION: 'SMF'
    add_pnfprofile_list:
    - NFINSTANCEID: 'AMF_Instance_0'
      NFTYPE: NfAMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.1.5'
      PORT: 8080
    - NFINSTANCEID: 'AMF_Instance_1'
      NFTYPE: NfAMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.1.6'
      PORT: 8080
    add_pnfservice_list:
    - NFINSTANCEID: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    - NFINSTANCEID: 'AMF_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'AMF_Instance_0'
      MCC: '123'
      MNC: '03'
    - NFINSTANCEID: 'AMF_Instance_1'
      MCC: '123'
      MNC: '03'
    add_pnfprofile_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.179'
      PORT: 8080
      PRIORITY: 10
    - NFINSTANCEID: 'UDM_Instance_1'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.180'
      PORT: 8080
      PRIORITY: 10
    add_pnfservice_list_4:
    - NFINSTANCEID: 'UDM_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    - NFINSTANCEID: 'UDM_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      MCC: '123'
      MNC: '03'
    - NFINSTANCEID: 'UDM_Instance_1'
      MCC: '123'
      MNC: '03'
    add_pnfsupi_list:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100001'
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_1'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100001'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      SST: 1
      SD: '010101'
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_1'
      SST: 1
      SD: '010101'
    set_chargectrl_list:
    - HOMEONLINE: DISABLE
      HOMECONVERGED: DISABLE
      HOMEOFFLINE: DISABLE
      VISITONLINE: DISABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: DISABLE
      ROAMOFFLINE: DISABLE
      ROAMCONVERGED: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **配置SMF服务化接口数据**

### 如果要配置v4v6双栈类型的服务化接口，该服务化接口的业务逻辑IP地址需要配置v4和v6类型的IP地址（通过**ADD LOGICIP**配置），相应的HTTP链路也需要配置v4和v6类型IP地址（通过**ADD HTTPLE**配置）。

### 当本端以及对端都配置了v4v6双栈类型的IP地址时，UNC侧可以通过将软参**DWORD1 BIT24**设置为**“1”**来确保在业务流程中优选IPv6地址进行建链。

#### 1.1 增加SMF服务化接口的IP地址。

##### 1.1.1 //DC1

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置SMF服务化接口的HTTP本端端点组及其包含的分别作为HTTP服务的服务端和客户端的本端端点信息。

##### 1.2.1 配置HTTP本端端点组信息。

###### 1.2.1.1 //DC1

```jinja2
{%- for item in add_httplegrp_list -%}
    ADD HTTPLEGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

###### 1.2.2.1 //DC1

```jinja2
{%- for item in add_httple_list -%}
    ADD HTTPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    LETYPE={{item.LETYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置SMF服务化接口接入点信息。

##### 1.3.1 //DC1

```jinja2
{%- for item in add_sbiaple_list -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **配置SMF到AMF的服务化接口**

#### 2.1 配置到AMF的数据，包括AMF的Profile、Service、PLMN等信息。

#### SMF可以基于DNN、DNAI、切片、TAI、PLMN选择AMF，园区可以基于规划的选择条件进行配置，此处以PLMN为例说明配置过程。

##### 2.1.1 //DC1

```jinja2
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
    ;
{%- endfor -%}
```

```jinja2
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
```

```jinja2
{%- for item in add_pnfplmn_list -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

### 3 **配置SMF到UDM的服务化接口**

#### 3.1 配置到UDM的数据，包括UDM的Profile、Service、PLMN信息、支持的SUPI范围等信息。

#### UEG中AMF和SMF共部署，如果在配置AMF的时候已经配置和UDM的对接配置，则本步骤无需重复配置。

#### SMF可以基于DNN、DNAI、切片、TAI、PLMN、SUPI、GPSI、RouteID、GroupID选择UDM，园区可以基于规划的选择条件进行配置，此处以PLMN、SUPI为例说明配置过程。

##### 3.1.1 //DC1

```jinja2
{%- for item in add_pnfprofile_list_2 -%}
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
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfservice_list_4 -%}
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
```

```jinja2
{%- for item in add_pnfplmn_list_2 -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

```jinja2
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
    ;
{%- endfor -%}
```

```jinja2
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
```

### 4 **关闭计费功能**

### 园区风筝方案不进行计费，需要关闭计费功能。

#### 4.1 关闭计费功能。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEONLINE is not none -%}
        HOMEONLINE={{item.HOMEONLINE}},
    {%- endif -%}
    {%- if item.HOMECONVERGED is not none -%}
        HOMECONVERGED={{item.HOMECONVERGED}},
    {%- endif -%}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.VISITONLINE is not none -%}
        VISITONLINE={{item.VISITONLINE}},
    {%- endif -%}
    {%- if item.VISITCONVERGED is not none -%}
        VISITCONVERGED={{item.VISITCONVERGED}},
    {%- endif -%}
    {%- if item.ROAMONLINE is not none -%}
        ROAMONLINE={{item.ROAMONLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMCONVERGED is not none -%}
        ROAMCONVERGED={{item.ROAMCONVERGED}},
    {%- endif -%}
    ;
{%- endfor -%}
```

