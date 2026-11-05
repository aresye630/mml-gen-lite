---
id: ''
name: 配置AMF和LMF/GMLC对接（NLs/NLg，用于LCS）
ne_type: UEG
type: feature
description: 本章节用于指导AMF和LMF/GMLC的对接操作，LMF/GMLC主要用于LCS相关业务。  在总部园区为风筝L，子园区为风筝L的跨级容灾场景下，总部园区AMF除了需要跟本设备的LMF/GMLC对接，同时还需要和子园区的LMF/GMLC进行对接。  LCS通过网络设备控制面的信令流程来完成定位的交互，从而获取目标UE位置的定位方案，是基于通信网络实现的方案。LCS系统结构如图1所示。  **图1** LCS系统结构示意图  GMLC和LRF可以是融合部署，也可以独立部署。AMF通过NLg和NLs分别和GMLC以及LMF对接。  |  |  | | --- | --- | | LCS（Location Service） | 位置服务 | | LMF（Location Management Function） | 位置管理功能实体 | | GMLC（Gateway Mobile Location Centre） | 网关移动定位中心 | | LRF（Location Retrieval Function） | 位置获取功能实体 | | LCS Client | 位置服务客户端 |  从3GPP TS 23.273 V0.2.0起，协议规定AMF和LMF之间的NLs接口修改为NL1接口，AMF和GMLC之间的NLg接口修改为NL2接口。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置AMF","配置AMF和LMF/GMLC对接（NLs/NLg，用于LCS）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本章节用于指导AMF和LMF/GMLC的对接操作，LMF/GMLC主要用于LCS相关业务。在总部园区为风筝L，子园区为风筝L的跨级容灾场景下，总部园区AMF除了需要跟本设备的LMF/GMLC对接，同时还需要和子园区的LMF/GMLC进行对接。LCS通过网络设备控制面的信令流程来完成定位的交互，从而获取目标UE位置的定位方案，是基于通信网络实现的方案。LCS系统结构如图1所示。**图1** LCS系统结构示意图GMLC和LRF可以是融合部署，也可以独立部署。AMF通过NLg和NLs分别和GMLC以及LMF对接。|  |  || --- | --- || LCS（Location Service） | 位置服务 || LMF（Location Management Function） | 位置管理功能实体 || GMLC（Gateway Mobile Location Centre） | 网关移动定位中心 || LRF（Location Retrieval Function） | 位置获取功能实体 || LCS Client | 位置服务客户端 |从3GPP TS 23.273 V0.2.0起，协议规定AMF和LMF之间的NLs接口修改为NL1接口，AMF和GMLC之间的NLg接口修改为NL2接口。

## 必备事项
前提条件

完成LCS特性的License文件加载。
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
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
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
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
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
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
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
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALITY:
          name: '位置信息'
          type: string
          minLength: 0
          maxLength: 150
          required: false
          description: '* AMF使用本地对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置。 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfplmn_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加本地配置的对端NF实例支持的PLMN信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '增加本地配置的对端NF实例支持的PLMN信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: '增加本地配置的对端NF实例支持的PLMN信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnflmfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LMFID:
          name: 'LMF标识'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfgmlcinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLIENTTYPES:
          name: '外部客户端类型'
          type: string
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
          description: ''
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
    add_pnfsrvntfsubs_list:
      type: items
      properties:
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
        NTFICATIONTYPE:
          name: '回调URI通知类型'
          type: string
          enum:
          - NtfTypeINVALID
          - N1Msg
          - N2Info
          - LocNty
          - DataRmvNtf
          - DataChgNtf
          - NtfTypeMAX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CALLBACKURI:
          name: '回调URI'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N1MESSAGECLASS:
          name: 'N1消息类别'
          type: string
          enum:
          - EN1MsgINVALID
          - N1Mm
          - N1Sm
          - Lpp
          - Sms
          - N1Updp
          - N1Reserved1
          - EN1MsgMAX
          - Lcs
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2INFOCLASS:
          name: 'N2消息类别'
          type: string
          enum:
          - EN2MsgINVALID
          - N2Sm
          - Nrppa
          - Pws
          - PwsBcal
          - PwsRf
          - N2Ran
          - N2Reserved1
          - EN2MsgMAX
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      NFTYPE: NfLMF
      NFSTATUS: Registered
      FQDN: 'huawei.com'
      INTERPLMNFQDN: 'huawei1.com'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.107.65.183'
      PORT: 8080
      LOCALITY: 'SHANGHAI'
    add_pnfplmn_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      MCC: '460'
      MNC: '03'
    add_pnflmfinfo_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      LMFID: '0001'
    add_pnfgmlcinfo_list:
    - NFINSTANCEID: 'GMLC_Instance_0'
      CLIENTTYPES: EMERGENCY_SERVICES-0&PLMN_OPERATOR_SERVICES-0&LAWFUL_INTERCEPT_SERVICES-0&PLMN_OPERATOR_BROADCAST_SERVICES-0&PLMN_OPERATOR_OM-0&PLMN_OPERATOR_ANONYMOUS_STATISTI-0&PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT-0
    add_pnfservice_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NlmfLoc
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfsrvntfsubs_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      NTFICATIONTYPE: LocNty
      CALLBACKURI: 'http://10.60.103.60:19999/nlmf-loc/hlmf/v1/provide-location'
      N1MESSAGECLASS: Lpp
      N2INFOCLASS: Nrppa
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置LMF/GMLC实例基础信息。

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
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.LOCALITY is not none -%}
        LOCALITY="{{item.LOCALITY}}",
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
{%- for item in add_pnfplmn_list -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

### 3 **可选：**配置LMF/GMLC实例特有信息。

### 根据现网业务需要配置LMF/GMLC的特有属性信息，例如针对LMF/GMLC如果只支持某种特有外部客户端类型，则需要配置如下命令。

```jinja2
{%- if is_optional_lmf_gmlc_specific_info -%}
    {%- for item in add_pnflmfinfo_list -%}
        ADD PNFLMFINFO:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LMFID is not none -%}
            LMFID="{{item.LMFID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_lmf_gmlc_specific_info -%}
    {%- for item in add_pnfgmlcinfo_list -%}
        ADD PNFGMLCINFO:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CLIENTTYPES is not none -%}
            CLIENTTYPES={{item.CLIENTTYPES}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置LMF/GMLC支持的服务实例信息。

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

### 5 **可选：**配置LMF/GMLC支持的服务实例回调信息。

### 此配置适用于订阅通知场景，如果LMF/GMLC订阅了AMF，则AMF通过此配置向对应的回调信息发送订阅通知。

```jinja2
{%- if is_optional_service_instance_callback_info -%}
    {%- for item in add_pnfsrvntfsubs_list -%}
        ADD PNFSRVNTFSUBS:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        NTFICATIONTYPE={{item.NTFICATIONTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CALLBACKURI is not none -%}
            CALLBACKURI="{{item.CALLBACKURI}}",
        {%- endif -%}
        {%- if item.N1MESSAGECLASS is not none -%}
            N1MESSAGECLASS={{item.N1MESSAGECLASS}},
        {%- endif -%}
        {%- if item.N2INFOCLASS is not none -%}
            N2INFOCLASS={{item.N2INFOCLASS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 总部园区为UEGL、子园区为UEGL的多园区跨级容灾场景，当前设备为总部园区时，请参考步骤2~5配置总部园区AMF与子园区LMF/GMLC的对接。

