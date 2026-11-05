---
id: GWFD-021103
name: 激活支持SA国际漫游接入
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活支持SA国际漫游接入的操作过程。当运营商之间签订漫游协议，期望支持漫游用户漫入时，可以使用本特性。  国际漫游是指终端用户在归属运营商网络以外的国家或地区使用业务的场景。5G SA组网场景下，用户离开归属PLMN的覆盖范围时，UEG支持用户从拜访地网络接入使用业务，保证业务的连续性。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021100 移动性管理","GWFD-021103 支持SA国际漫游接入","激活支持SA国际漫游接入"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021100 移动性管理","GWFD-021103 支持SA国际漫游接入","激活支持SA国际漫游接入"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持SA国际漫游接入的操作过程。当运营商之间签订漫游协议，期望支持漫游用户漫入时，可以使用本特性。国际漫游是指终端用户在归属运营商网络以外的国家或地区使用业务的场景。5G SA组网场景下，用户离开归属PLMN的覆盖范围时，UEG支持用户从拜访地网络接入使用业务，保证业务的连续性。

## 必备事项
前提条件

* 请仔细阅读GWFD-021103 支持SA国际漫游接入特性概述。
* 完成加载License。
* 已配置AMF和SMF实体功能。详细请参考UEG产品文档 -> “初始配置与调测 -> 配置实例 -> 配置AMF/SMF/MME/SGW-C/PGW-C”。
* 本特性不影响逻辑组网，业务组网上需要增加如下接口配置。如表1所示。

  **表1** 特性新增接口

  | VPLMN |  | HPLMN |  |
  | --- | --- | --- | --- |
  | NF | 接口 | NF | 接口 |
  | AMF | SBI（N12） | AUSF | SBI（N12） |
  | AMF | SBI（N8） | UDM | SBI（N8） |
  | SMF | SBI（N16a） | SMF | SBI（N16a） |
  | UPF | N9c | UPF | N9a |

  新增了AMF/SMF的SBI接口与外部（非本PLMN）NF接口互通诉求，需要将VPLMN的AMF/SMF的SBI接口IP对外发布，HPLMN可以学到路由达到业务互通诉求。同理UPF的N9c也需要对外发布路由。因此上述接口的IP地址都需要向运营商进行申请。业务组网规划如表2所示。

  **表2** 业务组网规划

  | 逻辑接口 | 网元侧VRF（建议），以客户定义为准 | 地址数量（单栈） | VLAN(建议) | 地址类型 | 对接的设备 | 对接路由 |
  | --- | --- | --- | --- | --- | --- | --- |
  | SBI(N8/N10/N16a) | VRF\_PS\_Signal | AMF:2个  SMF:2个  需要向运营商申请 | 2001 | IPv4/IPv6 | DCGW/传输设备 | 1. 静态路由+BFD；  2. OSPF；  3. eBGP over静态路由/直连路由+单臂BFD； |
  | N9c | VRF\_PS\_Gn | 1个  需要向运营商申请 | 2002 | IPv4/IPv6 | DCGW/传输设备 | 1. 静态路由+BFD；  2. OSPF；  3. eBGP over静态路由/直连路由+单臂BFD； |
  | S6a | VRF\_PS\_Signal | 2个  需要向运营商申请  SCTP双链路 | 2001 | IPv4/IPv6 | DCGW/传输设备 | 1. 静态路由+BFD；  2. OSPF；  3. eBGP over静态路由/直连路由+单臂BFD； |
  | S8-S | VRF\_PS\_Gn | 1个  需要向运营商申请 | 2002 | IPv4/IPv6 | DCGW/传输设备 | 1. 静态路由+BFD；  2. OSPF；  3. eBGP over静态路由/直连路由+单臂BFD； |

  已经部署UEG再激活本特性场景下，需要重新向运营商申请所需接口IP地址，并替换原有配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: ''
          data_source: ''
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
    set_roamcommplcy_list:
      type: items
      properties:
        ROUTEMODE:
          name: '漫游路由模式'
          type: string
          enum:
          - SEPP
          - SCP
          - DIRECT
          required: true
          description: '配置跨PLMN的网元之间的通信策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEPPMODE:
          name: '信令汇聚模式'
          type: string
          enum:
          - HTTPPROXY
          - TARGETAPIROOT
          required: false
          description: ''
          data_source: ''
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
          description: '配置和SEPP的对接。'
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
          name: 'IP地址'
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
          data_source: ''
          pattern: ''
          default: ''
        CAPACITY:
          name: '协议模式容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NFDESCNAME:
          name: 'NF描述名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCHEME:
          name: 'SCHEME'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: HTTPS
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
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngconnectplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置与本运营商签定了漫游协议的其它运营商的PLMN。'
          data_source: '本端规划'
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
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIFIED_IMSI_RANGE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_amfroamnsmap_list:
      type: items
      properties:
        HMCC:
          name: '归属地移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '配置漫游用户切片映射。将漫游用户切片映射为本地切片。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HMNC:
          name: '归属地移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSST:
          name: '归属地切片服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSD:
          name: '归属地切片细分标识'
          type: string
          minLength: 1
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VMCC:
          name: '拜访地移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VMNC:
          name: '拜访地移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VSST:
          name: '拜访地切片服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VSD:
          name: '拜访地切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置对端NF的Profile信息。 拜访地提供接入能力，接入策略信息。由归属地提供用户签约数据，会话策略信息和会话锚点。'
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
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
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
          data_source: ''
          pattern: ''
          default: ''
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
    add_pnfservice_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端NF的服务信息。'
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          description: '配置对端NF的PLMN信息。'
          data_source: ''
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
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
          description: '配置对端NF支持的SUPI信息。'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfrouteind_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: '配置到AUSF的路由信息。'
          data_source: ''
          pattern: ''
          default: ''
        ROUTINGIND:
          name: '路由指示'
          type: string
          minLength: 0
          maxLength: 4
          required: true
          description: ''
          data_source: ''
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
          description: '配置对端NF的Profile信息。 拜访地提供接入能力，接入策略信息。由归属地提供用户签约数据，会话策略信息和会话锚点。'
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
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
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
          data_source: ''
          pattern: ''
          default: ''
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
    add_pnfservice_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端NF的服务信息。'
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: REGISTERED
    add_pnfplmn_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端NF的PLMN信息。'
          data_source: ''
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
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfsupi_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端NF支持的SUPI信息。'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
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
          description: '配置对端NF实例支持的服务切片信息。'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    add_pnfprofile_list_3:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置对端NF的Profile信息。 拜访地提供接入能力，接入策略信息。由归属地提供用户签约数据，会话策略信息和会话锚点。'
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
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
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
          data_source: ''
          pattern: ''
          default: ''
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
    add_pnfservice_list_3:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端NF的服务信息。'
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          description: '配置对端NF的PLMN信息。'
          data_source: ''
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
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
          description: '配置对端NF实例支持的DNN及其归属切片的信息。'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端NF实例支持的服务切片信息。'
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    set_ngmmfunc_list:
      type: items
      properties:
        ROAMINGSW:
          name: '漫游服务功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '打开漫游功能支持开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        VSMFSUPPORT:
          name: 'V-SMF特性开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '打开漫游功能支持开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SAIRA01'
      SWITCH: ENABLE
    set_roamcommplcy_list:
    - ROUTEMODE: SEPP
      SEPPMODE: HTTPPROXY
    add_pnfprofile_list:
    - NFINSTANCEID: 'SEPP_Instance_0'
      NFTYPE: NfSEPP
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.182'
      PORT: 80
      CAPACITY: 100
      NFDESCNAME: 'Roaming_SEPP_00'
      SCHEME: HTTP
      FQDN: 'sepp1.cluster1.net2.amf.5gc.mnc000.mcc123.3gppnetwork.org'
      INTERPLMNFQDN: 'roaming.sepp1.cluster1.net2.amf.5gc.mnc000.mcc123.3gppnetwork.org'
    add_ngconnectplmn_list:
    - NOID: 0
      MCC: '456'
      MNC: '010'
      SUBRANGE: SPECIFIED_IMSI_RANGE
      IMSIPRE: '4560106789'
      DESC: 'for MNO B'
    add_amfroamnsmap_list:
    - HMCC: '456'
      HMNC: '010'
      HSST: 1
      HSD: '123FFF'
      VMCC: '123'
      VMNC: '000'
      VSST: 1
      VSD: 'FFFFFF'
    add_pnfprofile_list_1:
    - NFINSTANCEID: 'AUSF_Instance_0'
      NFTYPE: NfAUSF
      NFSTATUS: Registered
      FQDN: 'udm1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      INTERPLMNFQDN: 'udm1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      PORT: 8080
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.180'
    add_pnfservice_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NausfAuth
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      MCC: '456'
      MNC: '010'
    add_pnfsupi_list:
    - INDEX: 2
      NFINSTANCEID: 'AUSF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '456010170100001'
      RANGEEND: '456010170100001'
    add_pnfrouteind_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      ROUTINGIND: '0000'
    add_pnfprofile_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      FQDN: 'udm1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      INTERPLMNFQDN: 'udm1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      PORT: 8080
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.180'
    add_pnfservice_list_1:
    - NFINSTANCEID: 'UDM_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_1:
    - NFINSTANCEID: 'UDM_Instance_0'
      MCC: '456'
      MNC: '010'
    add_pnfsupi_list_1:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '4560101200100001'
      RANGEEND: '4560101200100001'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfprofile_list_3:
    - NFINSTANCEID: 'SMF_Instance_0'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      FQDN: 'smf1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      INTERPLMNFQDN: 'smf1.cluster1.net2.amf.5gc.mnc010.mcc456.3gppnetwork.org'
      PORT: 8080
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.180'
    add_pnfservice_list_3:
    - NFINSTANCEID: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_2:
    - NFINSTANCEID: 'SMF_Instance_0'
      MCC: '456'
      MNC: '010'
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      DNN: 'huawei.com'
    add_pnfns_list_1:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      SST: 1
      SD: '010101'
    set_ngmmfunc_list:
    - ROAMINGSW: ON
    set_smffunc_list:
    - VSMFSUPPORT: Support
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置与SEPP的对接。

```jinja2
{%- for item in set_roamcommplcy_list -%}
    SET ROAMCOMMPLCY:
    {#- --- 必选参数 --- -#}
    ROUTEMODE={{item.ROUTEMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ROUTEMODE=SEPP/SCP 时必选 --- -#}
    {%- if item.ROUTEMODE in ['SEPP', 'SCP'] -%}
        SEPPMODE={{item.SEPPMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    {%- if item.NFDESCNAME is not none -%}
        NFDESCNAME="{{item.NFDESCNAME}}",
    {%- endif -%}
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
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
```

### 4 配置互联PLMN。

```jinja2
{%- for item in add_ngconnectplmn_list -%}
    ADD NGCONNECTPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUBRANGE is not none -%}
        SUBRANGE={{item.SUBRANGE}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=SPECIFIED_IMSI_RANGE 时必选 --- -#}
    {%- if item.SUBRANGE == 'SPECIFIED_IMSI_RANGE' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置漫游切片映射。

```jinja2
{%- for item in add_amfroamnsmap_list -%}
    ADD AMFROAMNSMAP:
    {#- --- 必选参数 --- -#}
    HMCC="{{item.HMCC}}",
    HMNC="{{item.HMNC}}",
    HSST={{item.HSST}},
    HSD="{{item.HSD}}",
    VMCC="{{item.VMCC}}",
    VMNC="{{item.VMNC}}",
    VSST={{item.VSST}},
    VSD="{{item.VSD}}",
    ;
{%- endfor -%}
```

### 6 配置和对端NF的对接。需要配置对端归属地运营商SMF、UDM、AUSF的信息，包含对端NF的Profile信息、服务信息、PLMN信息、支持的SUPI信息、支持的服务切片信息等。

```jinja2
{%- for item in add_pnfprofile_list_1 -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
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
{%- for item in add_pnfrouteind_list -%}
    ADD PNFROUTEIND:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    ROUTINGIND="{{item.ROUTINGIND}}",
    ;
{%- endfor -%}
```

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
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
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
```

```jinja2
{%- for item in add_pnfservice_list_1 -%}
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
{%- for item in add_pnfplmn_list_1 -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsupi_list_1 -%}
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

```jinja2
{%- for item in add_pnfprofile_list_3 -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
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
```

```jinja2
{%- for item in add_pnfservice_list_3 -%}
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
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfns_list_1 -%}
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

### 7 打开支持漫游功能开关。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.ROAMINGSW is not none -%}
        ROAMINGSW={{item.ROAMINGSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.VSMFSUPPORT is not none -%}
        VSMFSUPPORT={{item.VSMFSUPPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

