---
id: ''
name: 配置SMF/GW-C公共数据（有语音业务+相同DNN/APN）
ne_type: UEG
type: feature
description: 当企业部署语音业务时，且所有园区仅采用2个DNN/APN接入业务，一个DNN/APN用于接入业务数据，一个DNN/APN用于接入语音数据，参考本章节进行SMF/GW-C与UPF/GW-U对接公共数据配置。此处仅以一套UEG-L的SMF/GW-C对接一个子园区主备UEG-L为例。新增子园区请参考本章节中对接子园区UPF/GW-U部分的配置。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（非跨级容灾）","方案配置","在UEG-L配置与UEG-S对接（UEG-L虚机）","子园区UPF主备冷备容灾","配置SMF/GW-C数据","配置SMF/GW-C公共数据（有语音业务+相同DNN/APN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当企业部署语音业务时，且所有园区仅采用2个DNN/APN接入业务，一个DNN/APN用于接入业务数据，一个DNN/APN用于接入语音数据，参考本章节进行SMF/GW-C与UPF/GW-U对接公共数据配置。此处仅以一套UEG-L的SMF/GW-C对接一个子园区主备UEG-L为例。新增子园区请参考本章节中对接子园区UPF/GW-U部分的配置。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: 'SMF/GW-C本端添加UPF/GW-U信息。子园区UPF/GW-U为主备容灾，SMF/GW-C根据“优先级（PRIORITY）”参数配置UPF/GW-U，其中主UPF/GW-U“优先级（PRIORITY）”参数值小于备UPF/GW-U“优先级（PRIORITY）”参数值。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
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
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_upselectflag_list:
      type: items
      properties:
        PRIORITYFLAG:
          name: '基于优先级优选UPF开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'SMF/GW-C按照主备优先级选择UPF/GW-U。'
          data_source: '固定取值'
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
          description: '配置UPF的属性。'
          data_source: '全网规划'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: None
        LOCK:
          name: 'UPF锁'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
    add_cptacgroup_list:
      type: items
      properties:
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '增加映射DNN/APN的5G位置区组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACTYPE:
          name: 'TAC类型'
          type: string
          enum:
          - S1Tac
          - N2Tac
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpn2tacid_list:
      type: items
      properties:
        TACSECNUM:
          name: 'TAC段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: '增加映射DNN/APN的5G位置区。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'TAC起始ID'
          type: string
          minLength: 3
          maxLength: 8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACENDID:
          name: 'TAC截止ID'
          type: string
          minLength: 3
          maxLength: 8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '5G位置区绑定位置区组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cptacgroup_list_1:
      type: items
      properties:
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '增加映射DNN/APN的4G位置区组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACTYPE:
          name: 'TAC类型'
          type: string
          enum:
          - S1Tac
          - N2Tac
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cps1tacid_list:
      type: items
      properties:
        TACSECNUM:
          name: 'TAC段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: '增加映射DNN/APN的4G位置区组下的位置区信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'TAC起始ID'
          type: string
          minLength: 3
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACENDID:
          name: 'TAC截止ID'
          type: string
          minLength: 3
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '4G位置区绑定位置区组。'
          data_source: '已配置数据中获取'
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
          description: '虚拟DNN/APN映射后的真实DNN/APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: 'Real.data.APN1绑定的用户模板和虚拟DNN/APN配置的用户模板一致。'
          data_source: '已配置数据中获取。'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取。'
          pattern: ''
          default: ''
    mod_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '用户签约的DNN/APN，使能DNN/APN的虚拟映射功能。该DNN/APN已完成基础业务配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_virtualapnrule_list:
      type: items
      properties:
        VIRTUALAPN:
          name: '虚拟APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置虚拟DNN/APN映射的位置区与真实DNN/APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAPPINGTYPE:
          name: '映射方式'
          type: string
          enum:
          - IMSI
          - MSISDN
          - RAT
          - PCO
          - RADIUS
          - LOAD_BALANCE
          - CHARGE_CHAR
          - REDUNDANCY
          - VDEFAULT_APN
          - IMEI
          - LAC_GROUP
          - TAC_GROUP
          - RAC_GROUP
          - PLMN
          - SERVING_GROUP
          - ROAMING
          - MULTIPARA
          - SELECTION_MODE
          - NS
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAPPINGVALUE:
          name: '映射值'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REALAPN:
          name: '真实APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALAPNSWITCH:
          name: '真实APN开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_virtualapnrule_list_2:
      type: items
      properties:
        VIRTUALAPN:
          name: '虚拟APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置虚拟DNN/APN默认映射的真实DNN/APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAPPINGTYPE:
          name: '映射方式'
          type: string
          enum:
          - IMSI
          - MSISDN
          - RAT
          - PCO
          - RADIUS
          - LOAD_BALANCE
          - CHARGE_CHAR
          - REDUNDANCY
          - VDEFAULT_APN
          - IMEI
          - LAC_GROUP
          - TAC_GROUP
          - RAC_GROUP
          - PLMN
          - SERVING_GROUP
          - ROAMING
          - MULTIPARA
          - SELECTION_MODE
          - NS
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALAPN:
          name: '真实APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REALAPNSWITCH:
          name: '真实APN开关'
          type: string
          enum:
          - Disable
          - Enable
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
          description: '配置用户面支持的服务切片信息。'
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
          description: '配置UPF/GW-U的DNN/APN属性，用于在用户会话激活时基于用户的DNN/APN选择UPF/GW-U。  各园区推荐共DNN/APN，如果各园区采用不同DNN/APN，则不支持用户跨园区访问。'
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
    set_cpapnreportattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '设置真实APN的上报属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AAAACCT:
          name: '上报给AAA计费的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AAAAUTH:
          name: '上报给AAA鉴权的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CG:
          name: '上报给CG的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DIAMETERAAA:
          name: '上报给Diameter AAA的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OCS:
          name: '上报给OCS的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHF:
          name: '上报给CHF的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCRF:
          name: '上报给PCRF的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCF:
          name: '上报给PCF的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PERFORMANCE:
          name: '上报给话统的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPF:
          name: '上报给用户面的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '新增5G 位置区，与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
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
          description: '设置5G位置区范围，已通过命令**ADD UPAREA**配置。其中TAI由PLMN和TAC组成。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: '(UPF服务区名称支持的5GTAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5GTAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
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
          description: 'SMF本端配置UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uparea_list_2:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '新增4G 位置区，与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabinds1tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '设置4G位置区范围，已通过命令**ADD UPAREA**配置。其中TAI由PLMN和TAC组成。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        S1BEGINTAI:
          name: 'UPF服务区名称绑定4GTAI范围起始值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        S1ENDTAI:
          name: 'UPF服务区名称绑定4GTAI范围结束值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfserarea_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'GW-C本端配置GW-U所覆盖的区域，用于在用户会话激活时基于用户位置区选择GW-U。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfupfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置用户面节点与EPS的互通以及支持的PDU会话类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: 'UPF是否支持与EPS的互通'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDUSESSIONTYPE:
          name: 'PDU会话类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1'
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.125.11'
      PORT: 8080
      PRIORITY: 0
    - NFINSTANCEID: 'UPF_Instance_A0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upfa00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
      PRIORITY: 0
    set_upselectflag_list:
    - PRIORITYFLAG: ENABLE
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    - NFINSTANCENAME: 'UPF_Instance_A0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    add_cptacgroup_list:
    - TACGROUPNAME: 'UPAREA1'
      TACTYPE: N2Tac
    add_cpn2tacid_list:
    - TACSECNUM: 0
      TACSTARTID: '0x000001'
      TACENDID: '0x000002'
      TACGROUPNAME: 'UPAREA1'
    add_cptacgroup_list_1:
    - TACGROUPNAME: 'GWUAREA1'
      TACTYPE: S1Tac
    add_cps1tacid_list:
    - TACSECNUM: 2
      TACSTARTID: '0x0000'
      TACENDID: '0x0001'
      TACGROUPNAME: 'GWUAREA1'
    add_cpapn_list:
    - APN: 'Real.data.APN1'
      VIRTUALAPN: DISABLE
    add_apnusrprofg_list:
    - APN: 'Real.data.APN1'
      USERPROFGNAME: 'data_apn1_userpro'
    mod_cpapn_list:
    - APN: 'data.APN1'
      VIRTUALAPN: ENABLE
    add_virtualapnrule_list:
    - VIRTUALAPN: 'data.APN1'
      MAPPINGTYPE: TAC_GROUP
      MAPPINGVALUE: 'UPAREA1'
      REALAPN: 'Real.data.APN1'
      REALAPNSWITCH: ''
    add_virtualapnrule_list_2:
    - VIRTUALAPN: 'data.APN1'
      MAPPINGTYPE: VDEFAULT_APN
      REALAPN: 'data.APN1'
      REALAPNSWITCH: ''
    add_pnfns_list:
    - INDEX: 2
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '010101'
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_A0'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 5
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'Real.data.APN1'
      PNFNSINDEX: 2
    - INDEX: 6
      NFINSTANCEID: 'UPF_Instance_A0'
      DNN: 'data.APN1'
      PNFNSINDEX: 3
    set_cpapnreportattr_list:
    - APN: 'Real.data.APN1'
      AAAACCT: REQUESTED
      AAAAUTH: REQUESTED
      CG: REQUESTED
      DIAMETERAAA: REQUESTED
      OCS: REQUESTED
      CHF: REQUESTED
      PCRF: REQUESTED
      PCF: REQUESTED
      PERFORMANCE: REQUESTED
      UPF: SERVICE
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    - AREANAME: 'UPAREA2'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12301000001'
      N2ENDTAI: '12301000002'
    - AREANAME: 'UPAREA2'
      N2BEGINTAI: '12301000003'
      N2ENDTAI: '12301000004'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA2'
    - NFINSTANCEID: 'UPF_Instance_A0'
      SMFSERVINGAREA: 'UPAREA2'
    add_uparea_list_2:
    - AREANAME: 'GWUAREA1'
      AREATYPE: S1TAI
    - AREANAME: 'GWUAREA2'
      AREATYPE: S1TAI
    add_upareabinds1tai_list:
    - AREANAME: 'GWUAREA1'
      S1BEGINTAI: '123010000'
      S1ENDTAI: '123010001'
    - AREANAME: 'GWUAREA2'
      S1BEGINTAI: '123010002'
      S1ENDTAI: '123010003'
    add_pnfsmfserarea_list_4:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'GWUAREA1'
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'GWUAREA2'
    - NFINSTANCEID: 'UPF_Instance_A0'
      SMFSERVINGAREA: 'GWUAREA2'
    add_pnfupfinfo_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
    - NFINSTANCEID: 'UPF_Instance_A0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置用户面节点实例。配置Profile实例。

#### 1.1 //对接总部园区UPF/GW-U配置

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
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
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

#### 1.2 //开启基于优先级选择UPF/GW-U

```jinja2
{%- for item in set_upselectflag_list -%}
    SET UPSELECTFLAG:
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITYFLAG is not none -%}
        PRIORITYFLAG={{item.PRIORITYFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置用户面节点的位置特征和分流能力。

#### 2.1 //对接总部园区UPF/GW-U配置

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
    {%- if item.LOCK is not none -%}
        LOCK={{item.LOCK}},
    {%- endif -%}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 总部园区部署语音业务后，配置总部园区数据业务DNN/APN（data.APN1）配置为虚拟DNN/APN，将data.APN1映射为Real.data.APN1。

#### 3.1 增加5G位置区映射信息。

##### 3.1.1 //对接总部园区UPF/GW-U配置

```jinja2
{%- for item in add_cptacgroup_list -%}
    ADD CPTACGROUP:
    {#- --- 必选参数 --- -#}
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACTYPE={{item.TACTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cpn2tacid_list -%}
    ADD CPN2TACID:
    {#- --- 必选参数 --- -#}
    TACSECNUM={{item.TACSECNUM}},
    TACSTARTID="{{item.TACSTARTID}}",
    TACENDID="{{item.TACENDID}}",
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    ;
{%- endfor -%}
```

#### 3.2 增加4G位置区映射信息。

##### 3.2.1 //对接总部园区UPF/GW-U配置

```jinja2
{%- for item in add_cptacgroup_list_1 -%}
    ADD CPTACGROUP:
    {#- --- 必选参数 --- -#}
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    TACTYPE={{item.TACTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cps1tacid_list -%}
    ADD CPS1TACID:
    {#- --- 必选参数 --- -#}
    TACSECNUM={{item.TACSECNUM}},
    TACSTARTID="{{item.TACSTARTID}}",
    TACENDID="{{item.TACENDID}}",
    TACGROUPNAME="{{item.TACGROUPNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 使能虚拟APN映射功能。

##### 3.3.1 //对接总部园区UPF/GW-U配置，其中Real.data.APN1与data.APN1绑定的用户模板一致。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
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

```jinja2
{%- for item in mod_cpapn_list -%}
    MOD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 增加虚拟DNN/APN（data.APN1）映射策略，将data.APN1映射为Real.data.APN1。

##### 3.4.1 //对接总部园区UPF/GW-U配置

```jinja2
{%- for item in add_virtualapnrule_list -%}
    ADD VIRTUALAPNRULE:
    {#- --- 必选参数 --- -#}
    VIRTUALAPN="{{item.VIRTUALAPN}}",
    MAPPINGTYPE={{item.MAPPINGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MAPPINGTYPE=IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP'] -%}
        MAPPINGVALUE="{{item.MAPPINGVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=CHARGE_CHAR/IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP/SELECTION_MODE/MULTIPARA/RAT/LOAD_BALANCE/ROAMING/REDUNDANCY/VDEFAULT_APN/NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'SELECTION_MODE', 'MULTIPARA', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY', 'VDEFAULT_APN', 'NS'] -%}
        REALAPN="{{item.REALAPN}}",
    {#- --- 条件必选：REALAPNSWITCH=Enable 时必选 --- -#}
    {%- elif item.REALAPNSWITCH == 'Enable' -%}
        REALAPN="{{item.REALAPN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 增加默认虚拟DNN/APN（data.APN1）映射策略。

##### 3.5.1 //对接总部园区UPF/GW-U配置

```jinja2
{%- for item in add_virtualapnrule_list_2 -%}
    ADD VIRTUALAPNRULE:
    {#- --- 必选参数 --- -#}
    VIRTUALAPN="{{item.VIRTUALAPN}}",
    MAPPINGTYPE={{item.MAPPINGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MAPPINGTYPE=CHARGE_CHAR/IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP/SELECTION_MODE/MULTIPARA/RAT/LOAD_BALANCE/ROAMING/REDUNDANCY/VDEFAULT_APN/NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'SELECTION_MODE', 'MULTIPARA', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY', 'VDEFAULT_APN', 'NS'] -%}
        REALAPN="{{item.REALAPN}}",
    {#- --- 条件必选：REALAPNSWITCH=Enable 时必选 --- -#}
    {%- elif item.REALAPNSWITCH == 'Enable' -%}
        REALAPN="{{item.REALAPN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置用户面节点支持的切片与DNN信息。

#### 4.1 //对接总部园区UPF/GW-U配置

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

### 5 配置映射后DNN/APN（Real.data.APN1）的上报属性。

#### 5.1 //对接总部园区UPF配置

```jinja2
{%- for item in set_cpapnreportattr_list -%}
    SET CPAPNREPORTATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AAAACCT is not none -%}
        AAAACCT={{item.AAAACCT}},
    {%- endif -%}
    {%- if item.AAAAUTH is not none -%}
        AAAAUTH={{item.AAAAUTH}},
    {%- endif -%}
    {%- if item.CG is not none -%}
        CG={{item.CG}},
    {%- endif -%}
    {%- if item.DIAMETERAAA is not none -%}
        DIAMETERAAA={{item.DIAMETERAAA}},
    {%- endif -%}
    {%- if item.OCS is not none -%}
        OCS={{item.OCS}},
    {%- endif -%}
    {%- if item.CHF is not none -%}
        CHF={{item.CHF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.PERFORMANCE is not none -%}
        PERFORMANCE={{item.PERFORMANCE}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置5G用户面节点的位置区信息，将位置区与TAI绑定。

#### 6.1 //对接总部园区UPF配置

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

### 7 配置5G用户面节点支持的为SMF提供服务区域的信息。

#### 7.1 //总部园区基站对接总部园区UPF配置（语音+数据）

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 8 配置4G用户面节点的位置区信息，将位置区与TAI绑定。

#### 8.1 //对接总部园区GW-U配置

```jinja2
{%- for item in add_uparea_list_2 -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upareabinds1tai_list -%}
    ADD UPAREABINDS1TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    S1BEGINTAI="{{item.S1BEGINTAI}}",
    S1ENDTAI="{{item.S1ENDTAI}}",
    ;
{%- endfor -%}
```

### 9 配置4G用户面节点支持的为GW-C提供服务区域的信息。

#### 9.1 //总部园区基站对接总部园区GW-U配置（语音+数据）

```jinja2
{%- for item in add_pnfsmfserarea_list_4 -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 10 配置用户面与EPS的互通以及支持的PDU会话类型。

#### 10.1 //对接总部园区UPF/GW-U配置

```jinja2
{%- for item in add_pnfupfinfo_list -%}
    ADD PNFUPFINFO:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    IWKEPSIND={{item.IWKEPSIND}},
    {#- --- 可选参数 --- -#}
    {%- if item.PDUSESSIONTYPE is not none -%}
        PDUSESSIONTYPE={{item.PDUSESSIONTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

