---
id: ''
name: 配置SMF/GW-C公共数据
ne_type: UEG
type: feature
description: 用于配置SMF/GW-C与UPF/GW-U对接公共数据。  新增子园区请参考本章节中对接子园区UPF/GW-U部分的配置。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（跨级容灾，仅适用于海外）","新建方案配置","基础业务数据配置","在UEG-L配置与UEG-S对接（UEG L裸机）","配置SMF/GW-C数据","配置SMF/GW-C公共数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用于配置SMF/GW-C与UPF/GW-U对接公共数据。新增子园区请参考本章节中对接子园区UPF/GW-U部分的配置。

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
          description: 'SMF/GW-C本端添加UPF/GW-U信息。  子园区UPF/GW-U的“优先级（PRIORITY）”必须大于总部园区UPF/GW-U的“优先级（PRIORITY）”参数值，则SMF/GW-C优先选择子园区UPF/GW-U用于数据接入。'
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
          description: 'SMF/GW-C按照优先级选择UPF/GW-U。'
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
    add_pnfprofile_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: 'SMF/GW-C本端添加UPF/GW-U信息。  子园区UPF/GW-U的“优先级（PRIORITY）”必须大于总部园区UPF/GW-U的“优先级（PRIORITY）”参数值，则SMF/GW-C优先选择子园区UPF/GW-U用于数据接入。'
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
    add_upnode_list_1:
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
    add_pnfns_list_1:
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
          description: '配置UPF/GW-U的DNN/APN属性，用于在用户会话激活时基于用户的DNN/APN选择UPF/GW-U。  总部园区UPF/GW-U支持同时接入总部园区及子园区业务。其中总部园区及各子园区UPF/GW-U可以分别采用不同DNN/APN，也可以采用相同DNN/APN。当总部园区与各子园区UPF/GW-U采用不同DNN/APN时，则不支持用户跨园区访问。'
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
          name: 'UPF服务区名称支持的5GTAI范围的起始值'
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
    add_uparea_list_1:
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
    add_pnfsmfserarea_list_2:
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
    add_pnfupfinfo_list_1:
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
      PRIORITY: 200
    set_upselectflag_list:
    - PRIORITYFLAG: ENABLE
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    add_pnfns_list:
    - INDEX: 2
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '010101'
    add_pnfupfinfo_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
    add_pnfprofile_list_1:
    - NFINSTANCEID: 'UPF_Instance_A0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upfa00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
      PRIORITY: 6
    add_upnode_list_1:
    - NFINSTANCENAME: 'UPF_Instance_A0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    add_pnfns_list_1:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_A0'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 6
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'APN1'
      PNFNSINDEX: 2
    - INDEX: 7
      NFINSTANCEID: 'UPF_Instance_A0'
      DNN: 'APN1'
      PNFNSINDEX: 3
    add_uparea_list:
    - AREANAME: 'UPAREA2'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA2'
      N2BEGINTAI: '12301000003'
      N2ENDTAI: '12301000004'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA2'
    add_uparea_list_1:
    - AREANAME: 'GWUAREA2'
      AREATYPE: S1TAI
    add_upareabinds1tai_list:
    - AREANAME: 'GWUAREA2'
      S1BEGINTAI: '123010002'
      S1ENDTAI: '123010003'
    add_pnfsmfserarea_list_2:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'GWUAREA2'
    add_pnfupfinfo_list_1:
    - NFINSTANCEID: 'UPF_Instance_A0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 公共配置。

#### 1.1 配置用户面节点实例。

##### 1.1.1 //配置Profile实例。

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

##### 1.1.2 //开启基于优先级选择UPF/GW-U。

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

#### 1.2 配置用户面节点的位置特征和分流能力。

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

#### 1.3 配置用户面节点支持的切片。

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

#### 1.4 配置用户面与EPS的互通以及支持的PDU会话类型。

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

### 2 新增一个子园区UPF/GW-U配置。如果子园区仅一套UEG-S，则参考一个UPF实例UPF_Instance_A0的配置即可。

#### 2.1 配置用户面节点实例。配置Profile实例。

```jinja2
{%- if is_scenario_add_subpark -%}
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
{%- endif -%}
```

#### 2.2 配置用户面节点的位置特征和分流能力。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_upnode_list_1 -%}
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
{%- endif -%}
```

#### 2.3 配置用户面节点支持的切片。

```jinja2
{%- if is_scenario_add_subpark -%}
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

#### 2.4 配置用户面节点支持的DNN/APN信息。

##### 2.4.1 //配置总部园区UPF/GW-U支持的DNN/APN信息，必须支持所有子园区的DNN/APN。

```jinja2
{%- if is_scenario_add_subpark -%}
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

#### 2.5 配置5G用户面节点的位置区信息，将位置区与TAI绑定。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_uparea_list -%}
        ADD UPAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_upareabindn2tai_list -%}
        ADD UPAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 配置5G用户面节点支持的为SMF提供服务区域的信息。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_pnfsmfserarea_list -%}
        ADD PNFSMFSERAREA:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 配置4G用户面节点的位置区信息，将位置区与TAI绑定。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_uparea_list_1 -%}
        ADD UPAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_upareabinds1tai_list -%}
        ADD UPAREABINDS1TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        S1BEGINTAI="{{item.S1BEGINTAI}}",
        S1ENDTAI="{{item.S1ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 配置4G用户面节点支持的为GW-C提供服务区域的信息。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_pnfsmfserarea_list_2 -%}
        ADD PNFSMFSERAREA:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 配置用户面与EPS的互通以及支持的PDU会话类型。

```jinja2
{%- if is_scenario_add_subpark -%}
    {%- for item in add_pnfupfinfo_list_1 -%}
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
{%- endif -%}
```

