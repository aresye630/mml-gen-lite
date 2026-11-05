---
id: ''
name: 配置动态PCC功能（SMF）
ne_type: UEG
type: feature
description: 如已通过极简开站方式完成PCF对接配置，则无需执行本页面。  采用动态PCC且通过N7接口实现与PCF互通时，需要参考本页面进行SMF的配置。  采用动态PCC且通过Gx接口实现与PCF互通时，请参考配置Gx接口数据进行SMF的配置。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置基础业务","在UEG上配置业务数据","PCC规则配置","配置动态PCC","配置动态PCC功能（SMF）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置基础业务","在UEG上配置业务数据","PCC规则配置","配置动态PCC","配置动态PCC功能（SMF）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","PCC规则配置","配置动态PCC","配置动态PCC功能（SMF）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置业务数据（风筝L）","PCC规则配置","配置动态PCC","配置动态PCC功能（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
如已通过极简开站方式完成PCF对接配置，则无需执行本页面。采用动态PCC且通过N7接口实现与PCF互通时，需要参考本页面进行SMF的配置。采用动态PCC且通过Gx接口实现与PCF互通时，请参考配置Gx接口数据进行SMF的配置。

## 必备事项
前提条件

* 请仔细阅读特性概述。
* 完成加载License（开站后通过OM Portal可一键开启所有License项，IOPS场景无需手动开启）。
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'SMF作为客户端与PCF对接。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '使用统一规划的VPN。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httplegrp_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX（索引）'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '配置Nsmf接口的HTTP本端端点组信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: 'DESC（描述）'
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
          name: 'INDEX（索引）'
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
        DESC:
          name: 'DESC（描述）'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
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
          name: 'DESCRIPTION（描述）'
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
          description: '配置PCF的Profile信息。  SMF只连接本DC UEN内的业务网元，不跨UEN与对接DC的业务网元对接。因此这种模式下，仅有一个对端实例。'
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
          description: '配置对接的对端PCF的IP地址。'
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
          description: '配置PCF的服务信息。'
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
          description: '配置对端PCF的实例信息，可以基于PLMN发现PCF。'
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
          description: '配置对端PCF支持的SUPI信息，可以基于SUPI选择PCF。'
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
          description: '配置对端PCF实例支持的服务切片信息。'
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
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端PCF实例支持的DNN，可以基于DNN选择PCF。'
          data_source: '全网规划'
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
          name: 'DNN（数据网络名称）'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          description: '开启全局粒度的动态PCC功能。'
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
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: '用于指定SMF上本地PCC策略是否激活。   * LOCAL\_PCC\_DEACTIVE：本地PCC策略不激活。 * LOCAL\_PCC\_ACTIVE：本地PCC策略激活。   此处以本地PCC策略不激活为例，实际请以局点规划为准。'
          data_source: '本端规划'
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
          description: '开启APN粒度的动态PCC功能。  APN粒度的优先级高于全局粒度。  “APN”参数值通过**LST CPAPAN**获取，请修改为局点规划的数据。'
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
          data_source: '对端协商'
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
    add_cppccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: '需根据业务策略选择相应的策略类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD CPPCCPOLICYGRP**定义的PCCPOLICYGRPNM。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置SMF上的UserProfile。  该参数需要与PCF上的规则标识相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: PCC
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '将本地rule/预定义规则rule绑定到UserProfile上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_policymode_list:
      type: items
      properties:
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          enum:
          - UE5G_RAT4G
          - UENON5G_RAT4G
          - RAT2G
          - RATNBIOT
          - NON_3GPP
          - RATLTEM
          - RAT3G
          required: true
          description: '**SET POLICYMODE**设置的是全局粒度的策略接口选择开关。  **ADD APNPOLICYMODE**设置的是基于APN粒度的策略接口选择开关。  基于APN粒度的比基于全局粒度的优先级高。  此处以固定使用N7接口为例。  “APN”参数值通过**LST CPAPAN**获取，请修改为局点规划的数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORCED:
          name: '指定策略接口'
          type: string
          enum:
          - Npcf
          - Gx
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYIWKUEN5GR4G:
          name: '非5G终端4G接入按5GS互操作指示选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnpolicymode_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          enum:
          - UE5G_RAT4G
          - UENON5G_RAT4G
          - RAT2G
          - RATNBIOT
          - NON_3GPP
          - RATLTEM
          - RAT3G
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择策略接口开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        FORCED:
          name: '指定策略接口'
          type: string
          enum:
          - Npcf
          - Gx
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.200.200.8'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR Server SBI'
    add_httplegrp_list:
    - INDEX: 2
      DESC: 'SMF'
    add_httple_list:
    - INDEX: 4
      HTTPLEGRPIDX: 2
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '10.200.200.9'
      VPNNAME: 'VPN_CN'
      DESC: 'SMF Client'
      TLSFLG: NO
    add_sbiaple_list:
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeSMF
      DESCRIPTION: 'SMF'
    add_pnfprofile_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      NFTYPE: NfPCF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.0.0.28'
      PORT: 8080
    add_pnfservice_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NpcfSmplcCtrl
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      MCC: '460'
      MNC: '003'
    add_pnfsupi_list:
    - INDEX: 1
      NFINSTANCEID: 'PCF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100100'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'PCF_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'PCF_Instance_0'
      DNN: 'huawei.com'
    add_pnfpcfinfo_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      RXDIAMHOST: 'huawei.com'
      RXDIAMREALM: 'huawei.com'
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9SPCC11'
      SWITCH: ENABLE
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
      LOCALPCCSELECT: LOCAL_PCC_DEACTIVE
    set_apnpccfunc_list:
    - APN: 'huawei'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    add_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
    add_cprule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      PRIORITY: 65535
      POLICYNAME: 'pccpolicy_group'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
    add_cprulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test'
    set_policymode_list:
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: DISABLE
      FORCED: Npcf
      BYIWKUEN5GR4G: DISABLE
    add_apnpolicymode_list:
    - APN: 'huawei'
      TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: DISABLE
      FORCED: Npcf
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置SMF服务化接口。

#### 2.1 配置逻辑接口。

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

#### 2.2 配置Nsmf接口的HTTP本端端点组信息。

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

#### 2.3 配置HTTP本端端点信息。

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
    ;
{%- endfor -%}
```

#### 2.4 配置本端服务化接口接入点信息。

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

### 3 配置SMF到PCF的数据 。

#### 3.1 配置PCF的Profile信息。

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

#### 3.2 配置PCF的服务信息。

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

#### 3.3 配置对端PCF的实例信息，可以基于PLMN发现PCF。

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

#### 3.4 配置对端PCF支持的SUPI信息，可以基于SUPI选择PCF。

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

#### 3.5 配置对端PCF实例支持的服务切片信息。

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

#### 3.6 配置对端PCF实例支持的DNN，可以基于DNN选择PCF。

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

#### 3.7 增加本地配置的对端PCF实例信息。

```jinja2
{%- for item in add_pnfpcfinfo_list -%}
    ADD PNFPCFINFO:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    RXDIAMHOST="{{item.RXDIAMHOST}}",
    RXDIAMREALM="{{item.RXDIAMREALM}}",
    ;
{%- endfor -%}
```

### 4 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 5 使能SMF上的全局用户的PCC功能。

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
    {%- if item.LOCALPCCSELECT is not none -%}
        LOCALPCCSELECT={{item.LOCALPCCSELECT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 使能SMF上基于APN的PCC功能。如果有多个APN，则可以多次执行本步骤。

```jinja2
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
    ;
{%- endfor -%}
```

### 7 配置PCC策略组。用于动态PCC时的预定义规则。

```jinja2
{%- for item in add_cppccpolicygrp_list -%}
    ADD CPPCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    ;
{%- endfor -%}
```

### 8 配置SMF上的本地rule。用于动态PCC时的预定义规则。

```jinja2
{%- for item in add_cprule_list -%}
    ADD CPRULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置SMF上的UserProfile，将本地rule绑定到UserProfile上。用于动态PCC时的预定义规则组。

#### 9.1 配置UserProfile。

```jinja2
{%- for item in add_cpuserprofile_list -%}
    ADD CPUSERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    ;
{%- endfor -%}
```

#### 9.2 将rule绑定到UserProfile。

```jinja2
{%- for item in add_cprulebinding_list -%}
    ADD CPRULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

### 10 设置PGW-C/SMF与PCF之间的策略接口模式。

### 可只设置其中一种，也可以两种都设置。两种都设置时，基于APN的比基于全局的优先级高。请根据需要进行设置。

#### 10.1 设置全局的策略接口的选择模式。

```jinja2
{%- for item in set_policymode_list -%}
    SET POLICYMODE:
    {#- --- 必选参数 --- -#}
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/RATNBIOT 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'RATNBIOT'] -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G 时可选 --- -#}
    {%- if item.TMACCTYPE == 'UENON5G_RAT4G' -%}
        {%- if item.BYIWKUEN5GR4G is not none -%}
            BYIWKUEN5GR4G={{item.BYIWKUEN5GR4G}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 指定策略接口: 条件必选(指定终端和接入类型=RAT2G|NON_3GPP|RATLTEM|RAT3G) / 条件可选(指定终端和接入类型=UENON5G_RAT4G|UE5G_RAT4G|RATNBIOT) --- -#}
    {%- if (item.TMACCTYPE in ['RAT2G', 'NON_3GPP', 'RATLTEM', 'RAT3G']) -%}
        FORCED={{item.FORCED}},
    {%- elif (item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G', 'RATNBIOT']) -%}
        {%- if item.FORCED is not none -%}
            FORCED={{item.FORCED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 10.2 增加基于APN的策略接口的选择模式。

```jinja2
{%- for item in add_apnpolicymode_list -%}
    ADD APNPOLICYMODE:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UENON5G_RAT4G/UE5G_RAT4G/RATNBIOT 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G', 'RATNBIOT'] -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 指定策略接口: 条件必选(指定终端和接入类型=RAT2G|NON_3GPP|RATLTEM|RAT3G) / 条件可选(指定终端和接入类型=UENON5G_RAT4G|UE5G_RAT4G|RATNBIOT) --- -#}
    {%- if (item.TMACCTYPE in ['RAT2G', 'NON_3GPP', 'RATLTEM', 'RAT3G']) -%}
        FORCED={{item.FORCED}},
    {%- elif (item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G', 'RATNBIOT']) -%}
        {%- if item.FORCED is not none -%}
            FORCED={{item.FORCED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

