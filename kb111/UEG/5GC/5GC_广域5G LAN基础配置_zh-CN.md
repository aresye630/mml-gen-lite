---
id: ''
name: 广域5G LAN基础配置
ne_type: UEG
type: feature
description: 当存在如下情况时，可以参考本页面进行配置。  * CPE下挂多个终端（最多16个）。 * 同一个二层广播域内的终端IP必须不同。 * 支持如下几种典型业务场景：   + 同一5G LAN组的层二终端之间通过同一UPF互通。   + 同一5G LAN组的层二终端之间通过不同UPF互通。
tags: []
risk_level: ''
doc_source: ["专线（仅连接，地市共享式）","网络部署","5GC toB 部署边缘站点（广域5G LAN，共享式）","配置广域5G LAN","运营商侧配置","核心网侧广域5G LAN业务配置","广域5G LAN基础配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当存在如下情况时，可以参考本页面进行配置。* CPE下挂多个终端（最多16个）。* 同一个二层广播域内的终端IP必须不同。* 支持如下几种典型业务场景：  + 同一5G LAN组的层二终端之间通过同一UPF互通。  + 同一5G LAN组的层二终端之间通过不同UPF互通。

## 必备事项
前提条件

* 除5G LAN业务外，UEG-S支持的5G SA业务运行正常。
* 已加载License文件，且包含如下License控制项：
  + UDM：LKQ7UDMBE15 5G LAN签约用户数
  + SMF：LKV2SALANSM01 5G LAN业务基本功能-USM、LKV2CUFMN01 CU FullMesh组网
  + UPF：LKV3G5LANB01 5G LAN基础功能、LKV3G5CUFM01 CU Full Mesh组网
  + PCF：LRM0PCFTC137 N7接口（使用HTTP协议）策略控制
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQI:
          name: '5QI'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '是否允许抢占低优先级业务的资源'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '是否允许资源被高优先级业务抢占'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUTYPE:
          name: 'PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'CPE IMSI'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        SNSSAI:
          name: 'SNSSAI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          required: false
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        DEFAULT:
          name: 'DEFAULT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: 'DNNQOSTPLID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vngroup_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INGROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 10
          maxLength: 38
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        EXTGROUPID:
          name: '外部组ID'
          type: string
          minLength: 3
          maxLength: 128
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  不同UDM上，外部组ID不能重复。外部组ID格式为：<*name*>@<*domain*>   * *<name>*建议企业内部按照group01，group02进行规划。企业内部有多个5G LAN组，不同5G LAN组的*<name>*值不能重复。 * *<domain>*建议使用企业域名。'
          data_source: ''
          pattern: ''
          default: ''
        SHAREDID:
          name: '共享数据ID'
          type: string
          maxLength: 64
          required: true
          description: '规划多个5G LAN组时，不同UDM该参数不能相同。  建议不同行政区分段，行政区内不同UDM该参数也必须不同。'
          data_source: ''
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          maxLength: 64
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        PDUTYPES:
          name: 'PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ''
    add_groupid_list:
      type: items
      properties:
        IMSI:
          name: 'CPE IMSI'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        INGROUPID:
          name: '5G LAN组ID'
          type: string
          required: false
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfns_list:
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
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnsdnn_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CORRECTTYPE:
          name: '纠正类型'
          type: string
          enum:
          - NS_CORRECTION
          - DNN_CORRECTION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        DNNPLCY:
          name: 'DNN纠正策略'
          type: string
          enum:
          - Default_DNN_preferred
          - Only_The_Configured_DNN
          - Configured_DNN_Preferred
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISFAILPLCY:
          name: 'SMF发现失败处理策略'
          type: string
          enum:
          - STANDARD_MODEL
          - RETRY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD_MODEL
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
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
          description: ''
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
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    add_cfgsnssai_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: string
          required: false
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISACTIVE:
          name: 'ISACTIVE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: 'DESC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tacgroupinnssf_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TACGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTART:
          name: 'TACSTART'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACEND:
          name: 'TACEND'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_amfsetid_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: string
          required: false
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGIONID:
          name: 'REGIONID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMFSETID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TACGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        NGLANSWITCH:
          name: '是否支持建立5G LAN会话'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upselectflag_list:
      type: items
      properties:
        NGLANUPFSELSW:
          name: '5G LAN UPF选择开关'
          type: string
          enum:
          - LOCALABILITY
          - GCOMABILITY
          - LOCALANDGCOM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list_1:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfns_list_1:
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
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        NGLANSW:
          name: '是否支持5G LAN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务器绑定的TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '复用时不需要规划及配置。'
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务器绑定的TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '复用时不需要规划及配置。'
          data_source: ''
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITYFLAG:
          name: '基于优先级优选UPF开关'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMBINEDSELSTG:
          name: '选择合一UPF的优先级和容量策略'
          type: string
          enum:
          - TAIPRI
          - APNPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPTYPE:
          name: 'UPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSPECTYPE:
          name: 'UPSPECTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: 'POLICYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: 'PRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: 'RULERANGE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULESPECTYPE:
          name: 'RULESPECTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: false
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
    set_licenseswitch_list_1:
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
    set_nglanfunc_list:
      type: items
      properties:
        NGLANSW:
          name: '5G LAN功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list_1:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDU类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ETHERNET
        MACIDLESW:
          name: 'N3学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IGMPSNOOPINGSW:
          name: 'IGMP Snooping开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IGMPPARSESW:
          name: 'IGMP消息解析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        MULTIFLOODSW:
          name: '组播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        MULTIFLOODRATE:
          name: '组播泛洪速率'
          type: integer
          minimum: 1
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 50
        BCASTFLOWCTRLSW:
          name: '广播流控开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        UNICASTFLOODSW:
          name: '单播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        N6MACIDLESW:
          name: 'N6学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHARGEFLAG:
          name: '事件计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHGPOINT:
          name: '事件计费点'
          type: string
          enum:
          - FINISH
          - REQUEST
          - RESPONSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RESPONSE
        MMSCHARGETYPE:
          name: '彩信计费类型'
          type: string
          enum:
          - MULTI
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        SIGNALASSOCIATE:
          name: '信令关联计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        TOKENFUNCFLAG:
          name: 'Token检测功能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERCONFIG
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: 'POLICYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: 'FILTERINGMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: 'FLOWFILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'tp5glan01'
      NGQI: 9
      ARPPRILEVEL: 1
      PREEMPTIONCAP: TRUE
      PREEMPTIONVUL: FALSE
      NGQIPRILEVEL: 1
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 2
      TPLNAME: 'tp5glan01'
      PDUTYPE: ETHER
      SSCMODE: SSC_MODE_1
      NGCQOSTPLID: 1
      AMBRUP: 5
      UPUNIT: Gbps
      AMBRDW: 5
      DWUNIT: Gbps
      CHARGE: '0800'
    add_smdata_list:
    - IMSI: '460081000000001'
      SNSSAI: 1-010101
      DNN: dnn5glan01
      DEFAULT: TRUE
      DNNQOSTPLID: '2'
    add_vngroup_list:
    - HLRSN: 1
      INGROUPID: '1001-46008-01'
      EXTGROUPID: 'group01@huawei.com'
      SHAREDID: '46008-huawei01'
      SNSSAI: '1-010101'
      DNN: 'dnn5glan01'
      PDUTYPES: ETHER
    add_groupid_list:
    - IMSI: '460081000000001'
      INGROUPID: 1001-46008-01
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 1
    add_localnsdnn_list:
    - SUBRANGE: HOME_USER
      CORRECTTYPE: DNN_CORRECTION
      SST: 1
      SD: '010101'
      DNN: 'dnn5glan01'
      DNNPLCY: Default_DNN_preferred
      DISFAILPLCY: STANDARD_MODEL
      DESC: '5GLAN_DNN_Correction'
    add_pnfns_list:
    - INDEX: 5
      NFINSTANCEID: 'SMF_Instance_1'
      SST: 1
      SD: '010101'
    add_cfgsnssai_list:
    - INDEX: '1'
      MCC: '123'
      MNC: '03'
      SST: '1'
      SD: '010101'
      ISACTIVE: TRUE
      DESC: 5G_LAN
    add_tacgroupinnssf_list:
    - INDEX: '1'
      TACGROUPNAME: 1-010101
      TACSTART: '290100'
      TACEND: '290110'
    add_amfsetid_list:
    - INDEX: '1'
      SST: '1'
      SD: '010101'
      MCC: '123'
      MNC: '03'
      REGIONID: 08
      AMFSETID: 088
      TACGROUPNAME: 1-010101
    set_smffunc_list:
    - NGLANSWITCH: Support
    set_upselectflag_list:
    - NGLANUPFSELSW: LOCALABILITY
    set_pfcppvtext_list:
    - FEATURE: NGLAN
      SWITCH: ENABLE
    add_plmnns_list_1:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
    add_nfns_list_1:
    - NFTYPE: NfSMF
      NSIDX: 1
    add_apn_list:
    - APN: 'dnn5glan01'
    add_nsdnn_list:
    - NSIDX: 1
      DNN: 'dnn5glan01'
    add_pnfprofile_list:
    - NFINSTANCEID: 'upf_instance_1'
      NFTYPE: NfUPF
      FQDN: '5glan01.upf1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '119.5.52.2'
      PORT: 8805
    add_pnfns_list_1:
    - INDEX: 1
      NFINSTANCEID: 'upf_instance_1'
      SST: 1
      SD: '010101'
    mod_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      NGLANSW: ENABLE
    add_uparea_list:
    - AREANAME: 'area01'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'area01'
      N2BEGINTAI: '46008000000'
      N2ENDTAI: '46008FFFFFF'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'upf_instance_1'
      SMFSERVINGAREA: 'area01'
    set_apnupselply_list:
    - APN: 'dnn5glan01'
      PRIORITYFLAG: ENABLE
      COMBINEDSELSTG: APNPRI
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      FUPSESSIONEXC: DISABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'profilegroupfglan'
    add_userprofile_list:
    - USERPROFILENAME: fglan_u_p_any
      UPTYPE: PCC
      UPSPECTYPE: DEFAULT
    add_upbindupg_list:
    - USERPROFGNAME: 'profilegroupfglan'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'fglan_u_p_any'
      LOCALPCCSELECT: INHERIT
    add_apnusrprofg_list:
    - APN: 'dnn5glan01'
      USERPROFGNAME: 'profilegroupfglan'
    add_rule_list:
    - RULENAME: fglan_r_any
      POLICYTYPE: PCC
      POLICYNAME: pccpolicy_group
      PRIORITY: '65535'
      RULERANGE: ALL
      RULESPECTYPE: DEFAULT
    add_rulebinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5CUFM01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5LANB01'
      SWITCH: ENABLE
    set_nglanfunc_list:
    - NGLANSW: ENABLE
    add_apn_list_1:
    - APN: 'dnn5glan01'
    add_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      MACIDLESW: DISABLE
      IGMPSNOOPINGSW: DISABLE
      IGMPPARSESW: DISABLE
      MULTIFLOODSW: ENABLE
      MULTIFLOODRATE: 20
      BCASTFLOWCTRLSW: ENABLE
      UNICASTFLOODSW: DISABLE
      N6MACIDLESW: DISABLE
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: '5glan_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
    add_filter_list:
    - FILTERNAME: 'any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_filteripv6_list:
    - FILTERNAME: 'any_ipv6'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_flowfilter_list:
    - FLOWFILTERNAME: 'any_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'any_f_f'
      FILTERNAME: 'any'
    add_rule_list_1:
    - RULENAME: fglan_r_any
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: any_f_f
      POLICYNAME: 5glan_pcc_p_g
    add_userprofile_list_1:
    - USERPROFILENAME: fglan_u_p_any
    add_rulebinding_list_1:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置UDM数据

### 中心UDM（UDM）需支持给5G LAN用户签约离线计费属性，计费属性值以“0800”为例，可通过BOSS修改。请根据是否对5G LAN用户进行离线计费按需规划。

### + **ADD NGCQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令中的“NGCQOSTPLID” 参数索引**ADD NGCQOSTPL**命令中的“TPLID”参数值。

### + **ADD SMDATA**命令中的“DNNQOSTPLID”参数索引**ADD DNNQOSTPL**命令中的“TPLID”参数值。

### 5G LAN QoS参数（5QI、ARP等）仅用于举例，实际请根据具体业务模型规划。

### 在“UDM业务管理”窗口下执行**LST NGS**命令和**LST VNGROUP**可查询5G LAN用户的“SNSSAI”、“DNN”、“INGROUPID”、“SHAREDID”、“PDUTYPES”等开户信息。

### + 1.b~1.e是在“UDM业务管理”窗口下执行。具体为：先登录PGW WEBUI，然后在“应用类型”下拉框选择“UDM业务管理”。

#### 1.1 检查5G LAN License项是否开启。

##### 1.1.1 //显示信息中存在“LKQ7UDMBE15”控制项且取值不为0时，说明已开启5G LAN License。

#### 1.2 配置5G LAN使用的DNN信息。

##### 1.2.1 //创建5G QoS模板。

```jinja2
{%- for item in add_ngcqostpl_list -%}
    ADD NGCQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    NGQI={{item.NGQI}},
    ARPPRILEVEL={{item.ARPPRILEVEL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.PREEMPTIONCAP is not none -%}
        PREEMPTIONCAP={{item.PREEMPTIONCAP}},
    {%- endif -%}
    {%- if item.PREEMPTIONVUL is not none -%}
        PREEMPTIONVUL={{item.PREEMPTIONVUL}},
    {%- endif -%}
    {%- if item.NGQIPRILEVEL is not none -%}
        NGQIPRILEVEL={{item.NGQIPRILEVEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 //创建DNN QoS模板。

```jinja2
{%- for item in add_dnnqostpl_list -%}
    ADD DNNQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    PDUTYPE={{item.PDUTYPE}},
    SSCMODE={{item.SSCMODE}},
    NGCQOSTPLID={{item.NGCQOSTPLID}},
    AMBRUP={{item.AMBRUP}},
    UPUNIT={{item.UPUNIT}},
    AMBRDW={{item.AMBRDW}},
    DWUNIT={{item.DWUNIT}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.CHARGE is not none -%}
        CHARGE="{{item.CHARGE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 签约会话管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=1.3 -->
```

#### 1.4 创建5G LAN组。

##### 1.4.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“INGROUPID”、“EXTGROUPID”、“SHAREDID”取值必须不同。

```jinja2
{%- for item in add_vngroup_list -%}
    ADD VNGROUP:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    INGROUPID="{{item.INGROUPID}}",
    EXTGROUPID="{{item.EXTGROUPID}}",
    SHAREDID="{{item.SHAREDID}}",
    SNSSAI="{{item.SNSSAI}}",
    DNN="{{item.DNN}}",
    PDUTYPES={{item.PDUTYPES}},
    ;
{%- endfor -%}
```

#### 1.5 增加5G LAN组成员。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list step_id=1.5 -->
```

### 2 配置AMF数据

### AMF上配置的切片参数SST、SD与UDM开户时切片参数一致。可以复用已有切片，复用已有切片时，不需要执行如下配置。可通过**LST PLMNNS**查询。

#### 2.1 配置PLMN支持的切片。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_plmnns_list -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置AMF切片信息。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

#### 2.3 配置AMF对5G LAN切片下的DNN纠正。如现网已涉及DNN纠正功能（可通过**LST LOCALNSDNN**查询），则需要执行如下配置；否则，请跳过如下配置。

##### 2.3.1 //用户请求APN与签约APN不匹配时，优先纠正为签约数据中的Default DNN，如果未签约Default DNN，则纠正为dnn5glan01。

```jinja2
{%- for item in add_localnsdnn_list -%}
    ADD LOCALNSDNN:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    CORRECTTYPE={{item.CORRECTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNNPLCY={{item.DNNPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CORRECTTYPE=DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        {%- if item.DISFAILPLCY is not none -%}
            DISFAILPLCY={{item.DISFAILPLCY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置对端SMF实例支持的切片。可以基于切片选择SMF。复用已有切片时，不需要重复配置。

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

### 3 配置NSSF数据

### 同一区域内，不是所有AMF都支持5G LAN业务切片时，需配置NSSF数据。否则，不需要配置。

### AMF收到5G LAN业务报文后，如本AMF未配置5G LAN业务切片信息，则可通过与NSSF交互实现AMF重定向，即将5G LAN业务报文重定向到配置了5G LAN业务切片信息的AMF上。

#### 3.1 在NSSF上增加5G LAN业务切片信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cfgsnssai_list的变量区（command: ADD CFGSNSSAI） -#}
<!-- MISSING_MACRO: command=ADD CFGSNSSAI list_name=add_cfgsnssai_list step_id=3.1 -->
```

#### 3.2 在跟踪区域码分组中增加跟踪区域码。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tacgroupinnssf_list的变量区（command: ADD TACGROUPINNSSF） -#}
<!-- MISSING_MACRO: command=ADD TACGROUPINNSSF list_name=add_tacgroupinnssf_list step_id=3.2 -->
```

#### 3.3 将切片、AMF、TAC组进行绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amfsetid_list的变量区（command: ADD AMFSETID） -#}
<!-- MISSING_MACRO: command=ADD AMFSETID list_name=add_amfsetid_list step_id=3.3 -->
```

### 4 配置SMF数据

### + **ADD PNFNS**命令存在多条时，“INDEX”不能重复。

### 5G LAN SMF-UPF Fullmesh组网时，支持5G LAN的多个SMF上的5G LAN业务配置相同。

#### 4.1 检查5G LAN License项是否开启。

##### 4.1.1 //显示信息中存在“LKV2SALANSM01”控制项时，说明已开启5G LAN License。

#### 4.2 配置SMF 5G LAN全局参数。

##### 4.2.1 //配置支持建立5G LAN会话。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSWITCH is not none -%}
        NGLANSWITCH={{item.NGLANSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.2.2 //配置对5G LAN UPF的选择机制。

```jinja2
{%- for item in set_upselectflag_list -%}
    SET UPSELECTFLAG:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANUPFSELSW is not none -%}
        NGLANUPFSELSW={{item.NGLANUPFSELSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.2.3 //配置5G LAN关键信元。

```jinja2
{%- for item in set_pfcppvtext_list -%}
    SET PFCPPVTEXT:
    {#- --- 必选参数 --- -#}
    FEATURE={{item.FEATURE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 配置5G LAN使用的切片和专用DNN信息。

##### 4.3.1 //配置SMF支持的切片信息。可以复用已有切片，复用已有切片时，不需要执行如下配置。可通过**LST PLMNNS**查询。

```jinja2
{%- for item in add_plmnns_list_1 -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    {%- if item.STATE is not none -%}
        STATE={{item.STATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nfns_list_1 -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

##### 4.3.2 //配置SMF支持的DNN（APN）信息。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

##### 4.3.3 //配置网络切片支持DNN。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 4.4 配置支持5G LAN的SMF对端UPF实例信息。

##### 4.4.1 //配置对端UPF节点信息。同一个UPF对端只能配置一条ADD PNFPROFILE记录。如已配置对应的UPF节点信息，则不需要重复配置。

```jinja2
{%- for item in add_pnfprofile_list -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
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

##### 4.4.2 //配置对端UPF支持的切片信息。如复用已有的对端UPF的切片信息，则不需要重复配置。推荐复用。

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

##### 4.4.3 //配置对端UPF支持5G LAN功能。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSW is not none -%}
        NGLANSW={{item.NGLANSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.4.4 //配置对端UPF的位置区域信息。如已配置的对端UPF的位置区域信息包含5G LAN业务对应的基站的TAI范围，则不需要重复配置。一个UPF服务区域可以绑定多个TAI范围，如利旧UPF服务区，且需要增加TAI范围，则可只通过**ADD UPAREABINDN2TAI**命令增加TAI范围。此处以两个UPF的位置区域信息相同为例。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

##### 4.4.5 //配置对端UPF的SMF服务区域信息。如利旧UPF服务区（area01），则不需要重复配置。一个UPF实例可以和多个UPF服务区绑定。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

##### 4.4.6 //配置按优先级选择UPF。

```jinja2
{%- for item in set_apnupselply_list -%}
    SET APNUPSELPLY:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITYFLAG is not none -%}
        PRIORITYFLAG={{item.PRIORITYFLAG}},
    {%- endif -%}
    {%- if item.COMBINEDSELSTG is not none -%}
        COMBINEDSELSTG={{item.COMBINEDSELSTG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 配置5G LAN业务与用户模板组绑定。

##### 4.5.1 //配置PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.5.2 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=4.5.2 -->
```

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

##### 4.5.3 //配置规则和用户模板绑定。“POLICYNAME”采用**ADD PCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=4.5.3 -->
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置PCF数据

### 广域5G LAN使用离线计费，在离线计费场景下，基于PCF下发的预定义规则进行离线计费时，需要参考配置基于预定义规则的计费（推荐）页面中的PCF相关配置，否则不需要配置PCF数据。

### 需在BOSS上签约业务后，PCF配置的计费业务才能生效。

### 6 配置锚点UPF数据

#### 6.1 打开CU Fullmesh的License项。

##### 6.1.1 //开启CU Fullmesh的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 6.2 配置UPF 5G LAN全局参数。

##### 6.2.1 //开启5G LAN特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 6.2.2 //开启5G LAN功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

#### 6.3 配置UPF支持的DNN（APN）信息。

##### 6.3.1 //支持层二 5G LAN业务的DNN（APN）不需要绑定VPN实例。

```jinja2
{%- for item in add_apn_list_1 -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 6.4 配置UPF支持的5G LAN组。

##### 6.4.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“VNINSTANCE”取值必须不同。

```jinja2
{%- for item in add_ngvninstance_list -%}
    ADD NGVNINSTANCE:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNTYPE is not none -%}
        PDNTYPE={{item.PDNTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.MACIDLESW is not none -%}
            MACIDLESW={{item.MACIDLESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.IGMPSNOOPINGSW is not none -%}
            IGMPSNOOPINGSW={{item.IGMPSNOOPINGSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IGMPSNOOPINGSW=DISABLE 时可选 --- -#}
    {%- if item.IGMPSNOOPINGSW == 'DISABLE' -%}
        {%- if item.IGMPPARSESW is not none -%}
            IGMPPARSESW={{item.IGMPPARSESW}},
        {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- elif item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.IGMPPARSESW is not none -%}
            IGMPPARSESW={{item.IGMPPARSESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.MULTIFLOODSW is not none -%}
            MULTIFLOODSW={{item.MULTIFLOODSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MULTIFLOODSW=ENABLE 时可选 --- -#}
    {%- if item.MULTIFLOODSW == 'ENABLE' -%}
        {%- if item.MULTIFLOODRATE is not none -%}
            MULTIFLOODRATE={{item.MULTIFLOODRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.BCASTFLOWCTRLSW is not none -%}
            BCASTFLOWCTRLSW={{item.BCASTFLOWCTRLSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.UNICASTFLOODSW is not none -%}
            UNICASTFLOODSW={{item.UNICASTFLOODSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.N6MACIDLESW is not none -%}
            N6MACIDLESW={{item.N6MACIDLESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.5 配置缺省PCC规则。

##### 6.5.1 //配置PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list_1 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    {%- if item.EVENTCHARGEFLAG is not none -%}
        EVENTCHARGEFLAG={{item.EVENTCHARGEFLAG}},
    {%- endif -%}
    {%- if item.EVENTCHGPOINT is not none -%}
        EVENTCHGPOINT={{item.EVENTCHGPOINT}},
    {%- endif -%}
    {%- if item.MMSCHARGETYPE is not none -%}
        MMSCHARGETYPE={{item.MMSCHARGETYPE}},
    {%- endif -%}
    {%- if item.SIGNALASSOCIATE is not none -%}
        SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
    {%- endif -%}
    {%- if item.ADCMUTEFLAG is not none -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {%- if item.HTTP2DEGRADESW is not none -%}
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
    {%- endif -%}
    {%- if item.TOKENFUNCFLAG is not none -%}
        TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 6.5.2 //配置流过滤器，any-to-any。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_filteripv6_list -%}
    ADD FILTERIPV6:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPEV6={{item.L34PROTTYPEV6}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPEV6=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    {%- if item.FLOWFILTERTYPE is not none -%}
        FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

##### 6.5.3 //配置5G LAN业务相关的rule和userprofile。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_1的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_1 step_id=6.5.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list_1的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list_1 step_id=6.5.3 -->
```

```jinja2
{%- for item in add_rulebinding_list_1 -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

