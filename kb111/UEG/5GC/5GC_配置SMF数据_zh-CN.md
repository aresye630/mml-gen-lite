---
id: ''
name: 配置SMF数据
ne_type: UEG
type: feature
description: 本操作用于指导在SMF侧开通5G LAN相关业务，完成相关配置。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","运营商","配置5GC网元","配置SMF数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作用于指导在SMF侧开通5G LAN相关业务，完成相关配置。

## 必备事项
前提条件

* 操作人员已了解本功能的原理。
* 已完成加载License，可以通过**DSP LICENSE**命令查询确认，如果本特性的License在查询列表中可见，即可认为本特性License已加载成功。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_smffunc_list:
      type: items
      properties:
        NGLANSWITCH:
          name: '支持是否建立5G LAN会话'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '配置开启5G LAN功能开关。'
          data_source: '本端规划'
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
          description: '配置对5G LAN UPF的选择机制。  SMF根据本地配置判断UPF是否支持5G LAN功能时，设置为“LOCALABILITY”。  设置为“LOCALABILITY”后，SMF根据**ADD UPNODE**/**MOD UPNODE**中的“NGLANSW”配置判断某个UPF实例是否支持5G LAN功能，当“NGLANSW”值为“ENABLE”，则说明该UPF实例支持5G LAN功能。'
          data_source: '本端规划'
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
          description: '配置5G LAN关键信元。  涉及的关键信元请参见**SET PFCPPVTEXT**。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
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
          description: '增加SMF支持的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
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
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
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
    add_pnfdnn_list:
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
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置对端UPF支持5G LAN。  说明：  UPF实例与**ADD PNFPROFILE**命令中的“NF实例标识”参数取值保持一致。'
          data_source: '全网规划'
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
          data_source: '本端规划'
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
          name: 'UPF服务区名称支持的5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
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
    add_cpurr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_cpurrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
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
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
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
    add_chargemethod_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          enum:
          - DEFAULT
          - FLAT_BILLING
          - HOT_BILLING
          - NORMAL
          - PREPAID
          - SPECIFIC_VALUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINE:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        OFFLINE:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        CONVERGED:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        QBCSW:
          name: 'QBC计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: PCC
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
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: 'URRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URRID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: 'USAGERPTMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: 'OFFCOMPOUNDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RG:
          name: 'RG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: 'OFFMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40AGESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
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
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
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
    add_chargemethod_list_1:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          enum:
          - DEFAULT
          - FLAT_BILLING
          - HOT_BILLING
          - NORMAL
          - PREPAID
          - SPECIFIC_VALUE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINE:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        OFFLINE:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        CONVERGED:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
        QBCSW:
          name: 'QBC计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_usrprofgroup_list_1:
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
    add_upbindupg_list_1:
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
    add_apnusrprofg_list_1:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
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
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
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
  examples:
    set_smffunc_list:
    - NGLANSWITCH: Support
    set_upselectflag_list:
    - NGLANUPFSELSW: LOCALABILITY
    set_pfcppvtext_list:
    - FEATURE: NGLAN
      SWITCH: ENABLE
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
    add_nfns_list:
    - NFTYPE: NfSMF
      NSIDX: 1
    add_cpapn_list:
    - APN: 'dnn5glan01'
    add_apn_list:
    - APN: 'dnn5glan01'
    add_nsdnn_list:
    - NSIDX: 1
      DNN: 'dnn5glan01'
    add_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      LOCATION: Central
      UPFUNCTION: None
      VPNNAME: 'VRF_CN'
    add_pnfprofile_list:
    - NFINSTANCEID: 'upf_instance_1'
      NFTYPE: NfUPF
      FQDN: '5glan01.upf'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.5.52.2'
      PORT: 8805
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'upf_instance_1'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 0
      NFINSTANCEID: 'upf_instance_1'
      DNN: 'dnn5glan01'
      PNFNSINDEX: 1
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
    add_cpurr_list:
    - URRNAME: '5glan_urr'
      URRID: 2222
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 2222
      OFFMETERINGTYPE: VOLUME
      N40AGESW: ENABLE
    add_cpurrgroup_list:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr'
      DOWNURRNAME1: '5glan_urr'
    add_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      URRGROUPNAME: '5glan_urrgroup'
      FUPSESSIONEXC: DISABLE
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0800'
      ONLINE: DISABLE
      OFFLINE: ENABLE
      CONVERGED: ENABLE
      RGAPPLIED: OFFLINERGONLY
      QBCSW: ENABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'profilegroupfglan'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'testuserprofilename'
      UPTYPE: PCC
    add_upbindupg_list:
    - USERPROFGNAME: 'profilegroupfglan'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'testuserprofilename'
      LOCALPCCSELECT: INHERIT
    add_apnusrprofg_list:
    - APN: 'dnn5glan01'
      USERPROFGNAME: 'profilegroupfglan'
    add_cprule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      PRIORITY: 65535
      POLICYNAME: 'pccpolicy_group'
    add_cprulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'rule_test'
      POLICYTYPE: PCC
    add_urr_list:
    - URRNAME: 5glan_urr
      URRID: '2222'
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: '2222'
      OFFMETERINGTYPE: VOLUME
      N40AGESW: ENABLE
    add_urrgroup_list:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr'
      DOWNURRNAME1: '5glan_urr'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      URRGROUPNAME: '5glan_urrgroup'
      FUPSESSIONEXC: DISABLE
    add_chargemethod_list_1:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0800'
      ONLINE: DISABLE
      OFFLINE: ENABLE
      CONVERGED: ENABLE
      RGAPPLIED: OFFLINERGONLY
      QBCSW: ENABLE
    add_usrprofgroup_list_1:
    - USERPROFGNAME: 'profilegroupfglan'
    add_userprofile_list:
    - USERPROFILENAME: testuserprofilename
      UPTYPE: PCC
    add_upbindupg_list_1:
    - USERPROFGNAME: 'profilegroupfglan'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'testuserprofilename'
      LOCALPCCSELECT: INHERIT
    add_apnusrprofg_list_1:
    - APN: 'dnn5glan01'
      USERPROFGNAME: 'profilegroupfglan'
    add_rule_list:
    - RULENAME: 'rule_test'
      POLICYTYPE: PCC
      PRIORITY: 65535
      POLICYNAME: 'pccpolicy_group'
      FILTERINGMODE: ''
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'rule_test'
      POLICYTYPE: PCC
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置SMF 5G LAN全局参数。

#### 1.1 //配置支持建立5G LAN会话。

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

#### 1.2 //配置对5G LAN UPF的选择机制。

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

#### 1.3 //配置5G LAN关键信元。

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

### 2 配置5G LAN使用的切片和专用DNN信息。

#### 2.1 //配置SMF支持的切片信息。

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

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

#### 2.2 //配置SMF支持的DNN（APN）信息。

##### 2.2.1 园区SMF（UEG-M/UEG-L）时：

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 中心SMF（UEG-S/UEG-M）时：

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 //配置网络切片支持DNN。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 3 配置支持5G LAN的SMF对端UPF实例信息。

#### 3.1 //配置对端UPF节点信息。同一个UPF对端只能配置一条ADD PNFPROFILE记录。如已配置对应的UPF节点信息，则不需要重复配置。

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {%- if item.UPFUNCTION is not none -%}
        UPFUNCTION={{item.UPFUNCTION}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
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

#### 3.2 //配置对端UPF支持的切片信息。如复用已有的对端UPF的切片信息，则不需要重复配置。推荐复用。

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

#### 3.3 //配置对端UPF支持的DNN信息。

```jinja2
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
```

#### 3.4 //配置对端UPF支持5G LAN功能。

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

#### 3.5 //配置对端UPF的位置区域信息。如已配置的对端UPF的位置区域信息包含5G LAN业务对应的基站的TAI范围，则不需要重复配置。一个UPF服务区域可以绑定多个TAI范围，如利旧UPF服务区，且需要增加TAI范围，则可只通过**ADD UPAREABINDN2TAI**命令增加TAI范围。

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

#### 3.6 //配置对端UPF的SMF服务区域信息。如利旧UPF服务区（area01），则不需要重复配置。一个UPF实例可以和多个UPF服务区绑定。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 4 配置5G LAN业务的缺省PCC规则。

#### 4.1 园区SMF（UEG-M/UEG-L）时：

##### 4.1.1 //配置离线计费策略。此处仅用于举例，如已配置离线计费策略且“CCVALUE”为“0x0800”、RG与计费网元上5G LAN业务的RG值一致，则不需要重复配置。推荐复用。

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cpurr_list -%}
        ADD CPURR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
            RG={{item.RG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFFMETERINGTYPE is not none -%}
                OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.N40AGESW is not none -%}
                N40AGESW={{item.N40AGESW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cpurrgroup_list -%}
        ADD CPURRGROUP:
        {#- --- 必选参数 --- -#}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.UPURRNAME1 is not none -%}
            UPURRNAME1="{{item.UPURRNAME1}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME1 is not none -%}
            DOWNURRNAME1="{{item.DOWNURRNAME1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cppccpolicygrp_list -%}
        ADD CPPCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_chargemethod_list -%}
        ADD CHARGEMETHOD:
        {#- --- 必选参数 --- -#}
        CHARGECHARACT={{item.CHARGECHARACT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ONLINE is not none -%}
            ONLINE={{item.ONLINE}},
        {%- endif -%}
        {%- if item.OFFLINE is not none -%}
            OFFLINE={{item.OFFLINE}},
        {%- endif -%}
        {%- if item.CONVERGED is not none -%}
            CONVERGED={{item.CONVERGED}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CHARGECHARACT=SPECIFIC_VALUE 时必选 --- -#}
        {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
            CCVALUE="{{item.CCVALUE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
        {%- if item.CONVERGED == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
        {%- if item.CONVERGED == 'ENABLE' -%}
            {%- if item.QBCSW is not none -%}
                QBCSW={{item.QBCSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cpuserprofile_list -%}
        ADD CPUSERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.3 //配置规则和用户模板绑定。“POLICYNAME”采用**ADD CPPCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{%- if is_scenario_campus_smf -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_campus_smf -%}
    {%- for item in add_cprulebinding_list -%}
        ADD CPRULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POLICYTYPE is not none -%}
            POLICYTYPE={{item.POLICYTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 中心SMF（UEG-S/UEG-M）时：

##### 4.2.1 //配置离线计费策略。此处仅用于举例，如已配置离线计费策略且“CCVALUE”为“0x0800”、RG与计费网元上5G LAN业务的RG值一致，则不需要重复配置。推荐复用。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list step_id=4.2.1 -->
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_urrgroup_list -%}
        ADD URRGROUP:
        {#- --- 必选参数 --- -#}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.UPURRNAME1 is not none -%}
            UPURRNAME1="{{item.UPURRNAME1}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME1 is not none -%}
            DOWNURRNAME1="{{item.DOWNURRNAME1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_chargemethod_list_1 -%}
        ADD CHARGEMETHOD:
        {#- --- 必选参数 --- -#}
        CHARGECHARACT={{item.CHARGECHARACT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ONLINE is not none -%}
            ONLINE={{item.ONLINE}},
        {%- endif -%}
        {%- if item.OFFLINE is not none -%}
            OFFLINE={{item.OFFLINE}},
        {%- endif -%}
        {%- if item.CONVERGED is not none -%}
            CONVERGED={{item.CONVERGED}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CHARGECHARACT=SPECIFIC_VALUE 时必选 --- -#}
        {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
            CCVALUE="{{item.CCVALUE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
        {%- if item.CONVERGED == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
        {%- if item.CONVERGED == 'ENABLE' -%}
            {%- if item.QBCSW is not none -%}
                QBCSW={{item.QBCSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_usrprofgroup_list_1 -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=4.2.2 -->
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_upbindupg_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_apnusrprofg_list_1 -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.3 //配置规则和用户模板绑定。“POLICYNAME”采用**ADD PCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_center_smf -%}
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
{%- endif -%}
```

