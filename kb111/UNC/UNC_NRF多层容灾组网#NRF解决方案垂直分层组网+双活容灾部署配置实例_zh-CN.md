---
id: ''
name: NRF解决方案垂直分层组网+双活容灾部署配置实例
ne_type: UNC
type: feature
description: '* NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。 * 主备NRF上的号段信息配置已完成，且主备配置一致。 * 对于大型运营商网络，为了便于实现灵活自动化网络管理，需要分层部署NRF，最高层NRF实现运营商网络内所有NF/NFS管理。    本章节以双层组网为例，如图1所示。    **图1** 双层+容灾组网举例'
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","4/5G融合部署","NRF多层容灾组网","NRF解决方案垂直分层组网+双活容灾部署配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。* 主备NRF上的号段信息配置已完成，且主备配置一致。* 对于大型运营商网络，为了便于实现灵活自动化网络管理，需要分层部署NRF，最高层NRF实现运营商网络内所有NF/NFS管理。  本章节以双层组网为例，如图1所示。  **图1** 双层+容灾组网举例

## 必备事项
前提条件

* 各组NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。
* 各个NRF的基础配置和NF基本功能、NF发现配置已完成，详细参考NRF解决方案基本功能配置实例的NRF侧配置。
* 主备NRF上的号段信息配置已完成，且号段信息配置一致。
* 安全相关配置已完成，访问授权和Token认证只需要在L-NRF层配置（Token分配只可能发生在目标NF注册的NRF上），TLS认证需要在所有NRF上配置，详细参考NRF解决方案安全配置实例（NRF容灾+NF访问授权&NF认证）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ngmno_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    add_nfuuid_list:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_1:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
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
    add_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - Undiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservice_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
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
          - SrvNameINVALID
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
          - NpcfSmPlcCtrl
          - NpcfPlcauth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgmt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - Nnef3gppAsSessionWithQos
          - Nnef3gppMonEvent
          - NnwdafDataManagement
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
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
    add_nfservicever_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
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
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfregnrf_list:
      type: items
      properties:
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - NRF
          - NON_NRF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
    act_nfonline_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfgroup_list:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_1:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list_1:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    set_licenseswitch_list_3:
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
    add_nfuuid_list_1:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_2:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_2:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_3:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_5:
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
    add_nrf_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nfprofile_list_1:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - Undiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservice_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
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
          - SrvNameINVALID
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
          - NpcfSmPlcCtrl
          - NpcfPlcauth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgmt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - Nnef3gppAsSessionWithQos
          - Nnef3gppMonEvent
          - NnwdafDataManagement
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
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
    add_nfservicever_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
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
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfregnrf_list_2:
      type: items
      properties:
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - NRF
          - NON_NRF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
    act_nfonline_list_1:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfgroup_list_1:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_2:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_2:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list_2:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    set_licenseswitch_list_6:
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
    add_nfuuid_list_2:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_4:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_4:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_5:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_8:
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
    add_nrf_list_4:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list_4:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_4:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nfprofile_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - Undiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservice_list_4:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
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
          - SrvNameINVALID
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
          - NpcfSmPlcCtrl
          - NpcfPlcauth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgmt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - Nnef3gppAsSessionWithQos
          - Nnef3gppMonEvent
          - NnwdafDataManagement
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
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
    add_nfservicever_list_4:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
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
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfregnrf_list_4:
      type: items
      properties:
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - NRF
          - NON_NRF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
    act_nfonline_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfgroup_list_2:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_4:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_3:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list_3:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    set_licenseswitch_list_9:
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
    add_nfuuid_list_3:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_6:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list_3:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_6:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_7:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list_3:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_11:
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
    add_nrf_list_6:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list_6:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_6:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nfprofile_list_3:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - Undiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservice_list_5:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
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
          - SrvNameINVALID
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
          - NpcfSmPlcCtrl
          - NpcfPlcauth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgmt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - Nnef3gppAsSessionWithQos
          - Nnef3gppMonEvent
          - NnwdafDataManagement
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
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
    add_nfservicever_list_5:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
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
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfregnrf_list_6:
      type: items
      properties:
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - NRF
          - NON_NRF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
    act_nfonline_list_3:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfgroup_list_3:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_6:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_4:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list_4:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    set_licenseswitch_list_12:
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
    add_nfuuid_list_4:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_8:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list_4:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_8:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_9:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list_4:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_14:
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
    add_nrf_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nrfgroup_list_4:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_8:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_nrfgroup_list_6:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_12:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfamfregidrt_list:
      type: items
      properties:
        AMFREGID:
          name: 'AMF区域标识'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTNRFGRPNAME:
          name: '归属NRF组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrffuncsw_list:
      type: items
      properties:
        LNRFGRPERRSW:
          name: '南向NRF实例组分层路由配置错误告警上报开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_5:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list_5:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
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
    set_licenseswitch_list_15:
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
    add_nfuuid_list_5:
      type: items
      properties:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_10:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httplegrp_list_5:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_10:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list_11:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
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
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list_5:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_17:
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
    add_nrf_list_12:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list_12:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_12:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nrfgroup_list_8:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_16:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_nrfgroup_list_10:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDMODE:
          name: '转发模式'
          type: string
          enum:
          - ITERATION
          - RECURSION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfbindgrp_list_20:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfamfregidrt_list_2:
      type: items
      properties:
        AMFREGID:
          name: 'AMF区域标识'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTNRFGRPNAME:
          name: '归属NRF组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrffuncsw_list_1:
      type: items
      properties:
        LNRFGRPERRSW:
          name: '南向NRF实例组分层路由配置错误告警上报开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrf_list_16:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list_16:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_16:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
    set_licenseswitch_list_18:
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
    act_nfonline_list_4:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrf_list_18:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1：NRF\_Instancename\_l1 * L-NRF2：NRF\_Instancenm\_l2 * L-NRF3：NRF\_Instance\_l3 * L-NRF4：NRF\_l4 * H-NRF1：Instancename\_h1\_NRF * H-NRF2：Instance\_h2\_NRF'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list_18:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1：172.16.0.7 * NRF\_Instancenm\_l2：172.17.0.7 * NRF\_Instance\_l3：172.18.0.7 * NRF\_l4：172.19.0.7  * Instancename\_h1\_NRF：10.10.0.7 * Instance\_h2\_NRF：10.20.0.7'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_18:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
    set_licenseswitch_list_20:
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
    act_nfonline_list_5:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instancename_l1'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_1:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      TLS: FALSE
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      TLS: FALSE
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nfprofile_list:
    - NFINSTANCENAME: 'NRF_Instancename_l1'
      NFTYPE: NfNRF
      NFSTATUS: Registered
      PRIORITY: 1
    add_nfservice_list:
    - NFINSTANCENAME: 'NRF_Instancename_l1'
      SRVINSTANCEID: 'service_instance_l1_0'
      SERVICENAME: NrfNfm
      NFSERVICESTATUS: REGISTERED
    add_nfservicever_list:
    - NFINSTANCENAME: 'NRF_Instancename_l1'
      SRVINSTANCEID: 'service_instance_l1_0'
      APIFULLVERSION: '1.0.0.0'
    add_nfregnrf_list:
    - NFTYPE: NRF
      NRFINSTANCENAME: 'Instancename_h1_NRF'
      PRIORITY: 1
    act_nfonline_list:
    - NFINSTANCENAME: 'NRF_Instancename_l1'
    add_nrfgroup_list:
    - GROUPNAME: 'HGP1'
      GROUPATTR: HNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list:
    - NRFINSTNAME: 'Instancename_h1_NRF'
      GROUPNAME: 'HGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_ngmno_list_1:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_1:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list_1:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instancenm_l2'
    add_logicip_list_2:
    - IPVERSION: IPv4
      LOGICIPV4: '172.17.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_1:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_2:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.17.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_3:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.17.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_1:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_5:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list_2:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      TLS: FALSE
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      TLS: FALSE
    add_nrfaddr_list_2:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_2:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nfprofile_list_1:
    - NFINSTANCENAME: 'NRF_Instancenm_l2'
      NFTYPE: NfNRF
      NFSTATUS: Registered
      PRIORITY: 2
    add_nfservice_list_2:
    - NFINSTANCENAME: 'NRF_Instancenm_l2'
      SRVINSTANCEID: 'service_instance_l2_0'
      SERVICENAME: NrfNfm
      NFSERVICESTATUS: REGISTERED
    add_nfservicever_list_2:
    - NFINSTANCENAME: 'NRF_Instancenm_l2'
      SRVINSTANCEID: 'service_instance_l2_0'
      APIFULLVERSION: '1.0.0.0'
    add_nfregnrf_list_2:
    - NFTYPE: NRF
      NRFINSTANCENAME: 'Instancename_h1_NRF'
      PRIORITY: 1
    act_nfonline_list_1:
    - NFINSTANCENAME: 'NRF_Instancenm_l2'
    add_nrfgroup_list_1:
    - GROUPNAME: 'HGP1'
      GROUPATTR: HNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_2:
    - NRFINSTNAME: 'Instancename_h1_NRF'
      GROUPNAME: 'HGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_ngmno_list_2:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_2:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list_6:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list_2:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instance_l3'
    add_logicip_list_4:
    - IPVERSION: IPv4
      LOGICIPV4: '172.18.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_2:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_4:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.18.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_5:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.18.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_2:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_8:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list_4:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      TLS: FALSE
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      TLS: FALSE
    add_nrfaddr_list_4:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_4:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nfprofile_list_2:
    - NFINSTANCENAME: 'NRF_Instance_l3'
      NFTYPE: NfNRF
      NFSTATUS: Registered
      PRIORITY: 1
    add_nfservice_list_4:
    - NFINSTANCENAME: 'NRF_Instance_l3'
      SRVINSTANCEID: 'service_instance_l3_0'
      SERVICENAME: NrfNfm
      NFSERVICESTATUS: REGISTERED
    add_nfservicever_list_4:
    - NFINSTANCENAME: 'NRF_Instance_l3'
      SRVINSTANCEID: 'service_instance_l3_0'
      APIFULLVERSION: '1.0.0.0'
    add_nfregnrf_list_4:
    - NFTYPE: NRF
      NRFINSTANCENAME: 'Instancename_h1_NRF'
      PRIORITY: 1
    act_nfonline_list_2:
    - NFINSTANCENAME: 'NRF_Instance_l3'
    add_nrfgroup_list_2:
    - GROUPNAME: 'HGP1'
      GROUPATTR: HNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_4:
    - NRFINSTNAME: 'Instancename_h1_NRF'
      GROUPNAME: 'HGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_ngmno_list_3:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_3:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list_9:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list_3:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_l4'
    add_logicip_list_6:
    - IPVERSION: IPv4
      LOGICIPV4: '172.19.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_3:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_6:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.19.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_7:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.19.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_3:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_11:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list_6:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      TLS: FALSE
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      TLS: FALSE
    add_nrfaddr_list_6:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_6:
    - NRFINSTANCENAME: 'Instancename_h1_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'Instance_h2_NRF'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nfprofile_list_3:
    - NFINSTANCENAME: 'NRF_l4'
      NFTYPE: NfNRF
      NFSTATUS: Registered
      PRIORITY: 2
    add_nfservice_list_5:
    - NFINSTANCENAME: 'NRF_l4'
      SRVINSTANCEID: 'service_instance_l4_0'
      SERVICENAME: NrfNfm
      NFSERVICESTATUS: REGISTERED
    add_nfservicever_list_5:
    - NFINSTANCENAME: 'NRF_l4'
      SRVINSTANCEID: 'service_instance_l4_0'
      APIFULLVERSION: '1.0.0.0'
    add_nfregnrf_list_6:
    - NFTYPE: NRF
      NRFINSTANCENAME: 'Instancename_h1_NRF'
      PRIORITY: 1
    act_nfonline_list_3:
    - NFINSTANCENAME: 'NRF_l4'
    add_nrfgroup_list_3:
    - GROUPNAME: 'HGP1'
      GROUPATTR: HNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_6:
    - NRFINSTNAME: 'Instancename_h1_NRF'
      GROUPNAME: 'HGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_ngmno_list_4:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_4:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list_12:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list_4:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'Instancename_h1_NRF'
    add_logicip_list_8:
    - IPVERSION: IPv4
      LOGICIPV4: '10.10.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_4:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_8:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.10.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_9:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '10.10.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_4:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_14:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_l4'
      TLS: FALSE
    add_nrfaddr_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.18.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l4'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.19.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_l4'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nrfgroup_list_4:
    - GROUPNAME: 'LGP1'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    - GROUPNAME: 'LGP2'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_8:
    - NRFINSTNAME: 'NRF_Instancename_l1'
      GROUPNAME: 'LGP1'
      ISREGED: TRUE
      NRFINSTID: '123e4567-e89b-12d3-a456-426655440000'
      PRIORITY: 1
    - NRFINSTNAME: 'NRF_Instance_l3'
      GROUPNAME: 'LGP2'
      ISREGED: TRUE
      NRFINSTID: '123e4567-e89b-12d3-a456-426655440010'
      PRIORITY: 1
    add_nrfgroup_list_6:
    - GROUPNAME: 'LGP1'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    - GROUPNAME: 'LGP2'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_12:
    - NRFINSTNAME: 'NRF_Instancename_l1'
      GROUPNAME: 'LGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    - NRFINSTNAME: 'NRF_Instance_l3'
      GROUPNAME: 'LGP2'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_nrfamfregidrt_list:
    - AMFREGID: '01'
      NEXTNRFGRPNAME: 'LGP1'
    set_nrffuncsw_list:
    - LNRFGRPERRSW: FUNC_ON
    add_ngmno_list_5:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_5:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list_15:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    add_nfuuid_list_5:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'Instance_h2_NRF'
    add_logicip_list_10:
    - IPVERSION: IPv4
      LOGICIPV4: '10.20.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_5:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_10:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.20.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_11:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '10.20.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NSSF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_5:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_licenseswitch_list_17:
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nrf_list_12:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_l4'
      TLS: FALSE
    add_nrfaddr_list_12:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.18.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l4'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.19.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_12:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_l4'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nrfgroup_list_8:
    - GROUPNAME: 'LGP1'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    - GROUPNAME: 'LGP2'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_16:
    - NRFINSTNAME: 'NRF_Instancename_l1'
      GROUPNAME: 'LGP1'
      ISREGED: TRUE
      NRFINSTID: '123e4567-e89b-12d3-a456-426655440000'
      PRIORITY: 1
    - NRFINSTNAME: 'NRF_Instance_l3'
      GROUPNAME: 'LGP2'
      ISREGED: TRUE
      NRFINSTID: '123e4567-e89b-12d3-a456-426655440010'
      PRIORITY: 1
    add_nrfgroup_list_10:
    - GROUPNAME: 'LGP1'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    - GROUPNAME: 'LGP2'
      GROUPATTR: LNRF
      FWDMODE: RECURSION
    add_nrfbindgrp_list_20:
    - NRFINSTNAME: 'NRF_Instancename_l1'
      GROUPNAME: 'LGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    - NRFINSTNAME: 'NRF_Instance_l3'
      GROUPNAME: 'LGP2'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_nrfamfregidrt_list_2:
    - AMFREGID: '01'
      NEXTNRFGRPNAME: 'LGP1'
    set_nrffuncsw_list_1:
    - LNRFGRPERRSW: FUNC_ON
    add_nrf_list_16:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      TLS: FALSE
      PRIORITY: 0
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list_16:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_16:
    - NRFINSTANCENAME: 'NRF_Instancename_l1'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_Instancenm_l2'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list_18:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list_4:
    - NFINSTANCENAME: 'AMF_Instance_1'
    add_nrf_list_18:
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      TLS: FALSE
      PRIORITY: 0
    - NRFINSTANCENAME: 'NRF_l4'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list_18:
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.18.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l4'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.19.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_18:
    - NRFINSTANCENAME: 'NRF_Instance_l3'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_l4'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list_20:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list_5:
    - NFINSTANCENAME: 'AMF_Instance_2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 NRF分层组网配置

### NRF双层组网的L-NRF和H-NRF的网络位置及规划如图2所示，其中L-NRF支持向H-NRF注册。

### **图2** 不同层NRF的网络位置和南北向NRF组

### 其中，**AMF区域标识的路由信息：**

### H-NRF1和H-NRF2上AMF区域标识的路由信息：

### AMF区域标识为01的AMF实例组归属LGP1，

### AMF区域标识为02的AMF实例组归属LGP2。

### 所以，例如L-NRF1处管辖的AMF发现区域标识为02的AMF时，路由顺序为：L-NRF1（L-NRF1本身和配置路由都查不到，向上层查询）→H-NRF1（H-NRF1根据配置查询到AMF区域标识为02的AMF实例组归属LGP2，即L-NRF3/L-NRF4）→L-NRF3

### 2 NRF侧配置

#### 2.1 /*- - - - - - - - - - - - - - - - L-NRF1上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.1.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.1.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.1.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.1.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.1.1.7 //增加NRF服务化接口的IP地址。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.1.8 //配置Nnrf接口的HTTP信息。

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

###### 2.1.1.9 //增加NRF作为服务器端的HTTP本端实体。

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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_1 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.1.2 //二、配置NRF分层组网。

###### 2.1.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.1.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.2.6 //配置L-NRF1的Profile和Service信息，用于携带向上层NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfprofile_list -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservice_list -%}
        ADD NFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservicever_list -%}
        ADD NFSERVICEVER:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        APIFULLVERSION="{{item.APIFULLVERSION}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.1.2.7 //在L-NRF1上配置向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfregnrf_list -%}
        ADD NFREGNRF:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.1.2.8 //触发L-NRF1向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in act_nfonline_list -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.1.2.11 //在L-NRF1上配置对应的北向H-NRF组HGP1信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 /*- - - - - - - - - - - - - - - - L-NRF2上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.2.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.2.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list_1 -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list_1 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.2.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list_3 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.2.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_1 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.2.1.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_2 -%}
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.2.1.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_1 -%}
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

###### 2.2.1.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_2 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.2.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_3 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list_1 -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.2.2 //二、配置NRF分层组网。

###### 2.2.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_5 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.2.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list_2 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list_2 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list_2 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.2.2.7 //配置L-NRF2的Profile和Service信息，用于携带向上层NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfprofile_list_1 -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservice_list_2 -%}
        ADD NFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservicever_list_2 -%}
        ADD NFSERVICEVER:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        APIFULLVERSION="{{item.APIFULLVERSION}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.2.8 //在L-NRF2上配置向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfregnrf_list_2 -%}
        ADD NFREGNRF:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.2.9 //触发L-NRF2向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in act_nfonline_list_1 -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.2.12 //在L-NRF2上配置对应的北向H-NRF组HGP1信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_1 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_2 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 /*- - - - - - - - - - - - - - - - L-NRF3上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.3.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.3.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list_2 -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list_2 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.3.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list_6 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.3.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_2 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.3.1.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_4 -%}
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.3.1.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_2 -%}
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

###### 2.3.1.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_4 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.3.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_5 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list_2 -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.3.2 //二、配置NRF分层组网。

###### 2.3.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_8 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.3.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list_4 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list_4 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list_4 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.3.2.7 //配置L-NRF3的Profile和Service信息，用于携带向上层NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfprofile_list_2 -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservice_list_4 -%}
        ADD NFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservicever_list_4 -%}
        ADD NFSERVICEVER:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        APIFULLVERSION="{{item.APIFULLVERSION}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.3.2.8 //在L-NRF3上配置向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfregnrf_list_4 -%}
        ADD NFREGNRF:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.3.2.9 //触发L-NRF3向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in act_nfonline_list_2 -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.3.2.12 //在L-NRF3上配置对应的北向H-NRF组HGP1信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_2 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_4 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 /*- - - - - - - - - - - - - - - - L-NRF4上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.4.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.4.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list_3 -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list_3 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.4.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list_9 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.4.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_3 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.4.1.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_6 -%}
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.4.1.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_3 -%}
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

###### 2.4.1.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_6 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.4.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_7 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list_3 -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.4.2 //二、配置NRF分层组网。

###### 2.4.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_11 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.4.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list_6 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list_6 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list_6 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.4.2.7 //配置L-NRF4的Profile和Service信息，用于携带向上层NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfprofile_list_3 -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservice_list_5 -%}
        ADD NFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfservicever_list_5 -%}
        ADD NFSERVICEVER:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        APIFULLVERSION="{{item.APIFULLVERSION}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.4.2.8 //在L-NRF4上配置向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nfregnrf_list_6 -%}
        ADD NFREGNRF:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.4.2.9 //触发L-NRF4向H-NRF注册。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in act_nfonline_list_3 -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.4.2.12 //在L-NRF4上配置对应的北向H-NRF组HGP1信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_3 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_6 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 /*- - - - - - - - - - - - - - - - H-NRF1上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.5.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.5.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list_4 -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list_4 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.5.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list_12 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.5.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_4 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.5.1.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_8 -%}
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.5.1.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_4 -%}
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

###### 2.5.1.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_8 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.5.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_9 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list_4 -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.5.2 //二、配置NRF分层组网。

###### 2.5.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_14 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.5.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list_8 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list_8 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list_8 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.5.2.5 //在H-NRF1上配置对应的南向L-NRF组LGP1、LGP2信息。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_4 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_8 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.5.2.7 //在H-NRF1上配置对应的南向L-NRF组LGP1、LGP2信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_6 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_12 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.5.3 //三、配置NRF路由，用于跨NRF的NF查询。

###### 2.5.3.2 //在H-NRF1上新增AMF区域标识的路由信息。AMF区域标识为01的AMF实例组归属LGP1，AMF区域标识为02的AMF实例组归属LGP2。

```jinja2
{%- for item in add_nrfamfregidrt_list -%}
    ADD NRFAMFREGIDRT:
    {#- --- 必选参数 --- -#}
    AMFREGID="{{item.AMFREGID}}",
    NEXTNRFGRPNAME="{{item.NEXTNRFGRPNAME}}",
    ;
{%- endfor -%}
```

##### 2.5.4 //四、支持寻址NRF路由冲突上报告警。

###### 2.5.4.1 //NRF南向寻址时，若SET NRFFUNCSW命令的告警上报开关“LNRFGRPERRSW”打开，支持寻址NRF路由冲突（相同路由配置存在于多个NRF实例组）时上报告警。打开“LNRFGRPERRSW”上报开关配置如下：

```jinja2
{%- for item in set_nrffuncsw_list -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.LNRFGRPERRSW is not none -%}
        LNRFGRPERRSW={{item.LNRFGRPERRSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 /*- - - - - - - - - - - - - - - - H-NRF2上的配置- - - - - - - - - - - - - - - - - - - - */

##### 2.6.1 //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

###### 2.6.1.3 //配置运营商信息、运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_ngmno_list_5 -%}
    ADD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nghplmn_list_5 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

###### 2.6.1.4 //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list_15 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.6.1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_5 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

###### 2.6.1.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_10 -%}
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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.6.1.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_5 -%}
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

###### 2.6.1.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_10 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.6.1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_11 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
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
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sbiaple_list_5 -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.6.2 //二、配置NRF分层组网。

###### 2.6.2.1 //在NRF上配置打开NRF分层组网的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_17 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 2.6.2.2 //配置NRF互联的NRF相关信息，为相邻且相连的NRF之间建立联系。

```jinja2
{%- for item in add_nrf_list_12 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfaddr_list_12 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nrfpara_list_12 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.6.2.5 //在H-NRF2上配置对应的南向L-NRF组LGP1、LGP2信息。

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_8 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_16 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.6.2.7 //在H-NRF2上配置对应的南向L-NRF组LGP1、LGP2信息。

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfgroup_list_10 -%}
        ADD NRFGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        GROUPATTR={{item.GROUPATTR}},
        {#- --- 可选参数 --- -#}
        {%- if item.FWDMODE is not none -%}
            FWDMODE={{item.FWDMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_registered_ns_relation -%}
    {%- for item in add_nrfbindgrp_list_20 -%}
        ADD NRFBINDGRP:
        {#- --- 必选参数 --- -#}
        NRFINSTNAME="{{item.NRFINSTNAME}}",
        GROUPNAME="{{item.GROUPNAME}}",
        ISREGED={{item.ISREGED}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
        {%- if (item.ISREGED == 'TRUE') -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- elif (item.ISREGED == 'FALSE') -%}
            {%- if item.NRFINSTID is not none -%}
                NRFINSTID="{{item.NRFINSTID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.6.3 //三、配置NRF路由，用于跨NRF的NF查询。

###### 2.6.3.2 //在H-NRF2上新增AMF区域标识的路由信息。AMF区域标识为01的AMF实例组归属LGP1，AMF区域标识为02的AMF实例组归属LGP2。

```jinja2
{%- for item in add_nrfamfregidrt_list_2 -%}
    ADD NRFAMFREGIDRT:
    {#- --- 必选参数 --- -#}
    AMFREGID="{{item.AMFREGID}}",
    NEXTNRFGRPNAME="{{item.NEXTNRFGRPNAME}}",
    ;
{%- endfor -%}
```

##### 2.6.4 //四、支持寻址NRF路由冲突上报告警。

###### 2.6.4.1 //NRF南向寻址时，若SET NRFFUNCSW命令的告警上报开关“LNRFGRPERRSW”打开，支持寻址NRF路由冲突（相同路由配置存在于多个NRF实例组）时上报告警。打开“LNRFGRPERRSW”上报开关配置如下：

```jinja2
{%- for item in set_nrffuncsw_list_1 -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.LNRFGRPERRSW is not none -%}
        LNRFGRPERRSW={{item.LNRFGRPERRSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 NF侧向L-NRF的注册、更新、去注册、订阅、发现配置。

### AMF侧（不同区域的NF向不同NRF注册，因此以上述2组L-NRF（L-NRF1-A/L-NRF1-S、L-NRF2-A/L-NRF2-S）为例，对应给出2个AMF的配置脚本示例）

#### 3.1 /*- - - - - - - - - - - - - - - - -AMF1上的配置- - - - - - - - - - - - - - - - - - - - */

##### 3.1.3 ……

##### 3.1.4 ……

##### 3.1.5 ……

##### 3.1.7 //配置L-NRF1信息。

```jinja2
{%- for item in add_nrf_list_16 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.8 //配置L-NRF1的地址信息。

```jinja2
{%- for item in add_nrfaddr_list_16 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.9 //配置L-NRF1协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
{%- for item in add_nrfpara_list_16 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    {%- if item.LOADCARRYINHB is not none -%}
        LOADCARRYINHB={{item.LOADCARRYINHB}},
    {%- endif -%}
    {%- if item.SUBSCRISWITCH is not none -%}
        SUBSCRISWITCH={{item.SUBSCRISWITCH}},
    {%- endif -%}
    {%- if item.OAUTH2SWITCH is not none -%}
        OAUTH2SWITCH={{item.OAUTH2SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.1.14 //打开NF注册/更新/去注册、发现与NRF交互的基本功能开关。

```jinja2
{%- for item in set_licenseswitch_list_18 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 3.1.15 //激活AMF1向NRF注册。

```jinja2
{%- for item in act_nfonline_list_4 -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 3.2 /*- - - - - - - - - - - - - - - - -AMF2上的配置- - - - - - - - - - - - - - - - - - - - */

##### 3.2.3 ……

##### 3.2.4 ……

##### 3.2.5 ……

##### 3.2.7 //配置L-NRF3信息。

```jinja2
{%- for item in add_nrf_list_18 -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.8 //配置L-NRF3的地址信息。

```jinja2
{%- for item in add_nrfaddr_list_18 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.9 //配置L-NRF3协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
{%- for item in add_nrfpara_list_18 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    {%- if item.LOADCARRYINHB is not none -%}
        LOADCARRYINHB={{item.LOADCARRYINHB}},
    {%- endif -%}
    {%- if item.SUBSCRISWITCH is not none -%}
        SUBSCRISWITCH={{item.SUBSCRISWITCH}},
    {%- endif -%}
    {%- if item.OAUTH2SWITCH is not none -%}
        OAUTH2SWITCH={{item.OAUTH2SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.14 //打开NF注册/更新/去注册、发现与NRF交互的基本功能开关。

```jinja2
{%- for item in set_licenseswitch_list_20 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 3.2.15 //激活AMF2向NRF注册。

```jinja2
{%- for item in act_nfonline_list_5 -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

