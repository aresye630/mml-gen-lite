---
id: ''
name: 配置和NF直连
ne_type: UNC
type: feature
description: '* 如果网络中部署了NRF，则需执行配置到NRF的数据。 * 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行本章节操作，手工配置SMF与周边NF的逻辑连接。 * 当网络中既部署了NRF，又本地配置了周边NF时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认为优先选择本地配置的NF。 * 下述以配置SMF到周边UDM、PCF、CHF及AMF为例，说明配置本地NRF功能的基本步骤。'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","配置SMF","配置和NF直连"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* 如果网络中部署了NRF，则需执行配置到NRF的数据。* 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行本章节操作，手工配置SMF与周边NF的逻辑连接。* 当网络中既部署了NRF，又本地配置了周边NF时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认为优先选择本地配置的NF。* 下述以配置SMF到周边UDM、PCF、CHF及AMF为例，说明配置本地NRF功能的基本步骤。

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
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端NF实例概述信息。  “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
          description: '增加对端NF服务实例信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
          description: '增加对端NF的PLMN信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
          description: '增加对端NF的SUPI信息。'
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
    add_pnfprofile_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端NF实例概述信息。  “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfservice_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端NF服务实例信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfplmn_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端NF的PLMN信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfsupi_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加对端NF的SUPI信息。'
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
          description: '配置的对端NF实例支持的DNN及其归属切片的信息。'
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
    add_pnfgpsi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加对端NF的GPSI信息。'
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
    add_pnfprofile_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端NF实例概述信息。  “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfservice_list_3:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端NF服务实例信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfsupi_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加对端NF的SUPI信息。'
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
    add_pnfgpsi_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加对端NF的GPSI信息。'
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
    add_pnfprofile_list_3:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端NF实例概述信息。  “NF类型”为“NfAMF”时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
    add_pnfservice_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加对端NF服务实例信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
          description: '增加对端NF的PLMN信息。  对端为AMF时，“NF实例标识”应为UUID格式，取值通过在AMF上运行**LST NFUUID**获取。'
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
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.180'
      PORT: 8080
      FQDN: 'udm01.node.mnc003.mcc123.3gppnetwork.org'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnfservice_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      MCC: '123'
      MNC: '03'
    add_pnfsupi_list:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200200001'
      PATTERN: ''
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfprofile_list_1:
    - NFINSTANCEID: 'PCF_Instance_0'
      NFTYPE: NfPCF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.181'
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
    add_pnfservice_list_2:
    - NFINSTANCEID: 'PCF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NpcfSmplcCtrl
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_1:
    - NFINSTANCEID: 'PCF_Instance_0'
      MCC: '123'
      MNC: '03'
    add_pnfsupi_list_1:
    - INDEX: 2
      NFINSTANCEID: 'PCF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031340010001'
      RANGEEND: '123031340020001'
      PATTERN: ''
    add_pnfpcfinfo_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      RXDIAMHOST: 'huawei.com'
      RXDIAMREALM: 'huawei.com'
    add_pnfdnn_list:
    - INDEX: 2
      NFINSTANCEID: 'PCF_Instance_0'
      DNN: 'huawei.com'
      PNFNSINDEX: 2
    add_pnfns_list_1:
    - INDEX: 2
      NFINSTANCEID: 'PCF_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfgpsi_list:
    - INDEX: 1
      NFINSTANCEID: 'PCF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031340010001'
      RANGEEND: '123031340020001'
      PATTERN: ''
    add_pnfprofile_list_2:
    - NFINSTANCEID: 'CHF_instance_0'
      NFTYPE: NfCHF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.134.66'
      PORT: 8080
      FQDN: 'chf01.node.mnc003.mcc123.3gppnetwork.org'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnfservice_list_3:
    - NFINSTANCEID: 'CHF_Instance_0'
      SRVINSTANCEID: 'Service_instance_0'
      SERVICENAME: NchfConvCharg
      SCHEMA: http
    add_pnfsupi_list_2:
    - INDEX: 3
      NFINSTANCEID: 'CHF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '12303170100001'
      RANGEEND: '12303170200001'
      PATTERN: ''
    add_pnfgpsi_list_1:
    - INDEX: 2
      NFINSTANCEID: 'CHF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031340010001'
      RANGEEND: '123031340020001'
      PATTERN: ''
    add_pnfprofile_list_3:
    - NFINSTANCEID: 'a6a61c6f-0d3a-4221-b1da-424eda3ccf67'
      NFTYPE: NfAMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.1.5'
      PORT: 8080
      FQDN: 'amf01.node.mnc003.mcc123.3gppnetwork.org'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnfservice_list_4:
    - NFINSTANCEID: 'a6a61c6f-0d3a-4221-b1da-424eda3ccf67'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_2:
    - NFINSTANCEID: 'a6a61c6f-0d3a-4221-b1da-424eda3ccf67'
      MCC: '123'
      MNC: '03'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置到UDM的数据，包括UDM的Profile、Service、PLMN信息、支持的SUPI范围等信息。

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
    {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
    {%- if item.QUERYTYPE == 'PATTERN' -%}
        PATTERN="{{item.PATTERN}}",
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

### 3 **可选：**配置到PCF的数据，包括PCF的Profile、Service、PLMN信息、支持的SUPI范围等信息。如果在配置与PCF对接数据中已完成该配置则跳过本步骤。

```jinja2
{%- if is_optional_pcf_data -%}
    {%- for item in add_pnfprofile_list_1 -%}
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

```jinja2
{%- if is_optional_pcf_data -%}
    {%- for item in add_pnfservice_list_2 -%}
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

```jinja2
{%- if is_optional_pcf_data -%}
    {%- for item in add_pnfplmn_list_1 -%}
        ADD PNFPLMN:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pcf_data -%}
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
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_pcf_data -%}
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

```jinja2
{%- if is_optional_pcf_data -%}
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

```jinja2
{%- if is_optional_pcf_data -%}
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
{%- endif -%}
```

```jinja2
{%- if is_optional_pcf_data -%}
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

### 4 配置到CHF的数据，包括CHF的Profile、Service、支持的SUPI范围等信息。

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
```

```jinja2
{%- for item in add_pnfservice_list_3 -%}
    ADD PNFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    SCHEMA={{item.SCHEMA}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsupi_list_2 -%}
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
```

```jinja2
{%- for item in add_pnfgpsi_list_1 -%}
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
```

### 5 配置到AMF的数据，包括AMF的Profile、Service、PLMN等信息。

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

