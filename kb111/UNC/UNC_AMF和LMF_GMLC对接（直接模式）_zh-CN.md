---
id: ''
name: AMF和LMF/GMLC对接（直接模式）
ne_type: UNC
type: feature
description: 本操作用于在AMF和LMF/GMLC采用直连方式对接场景，指导在AMF上如何进行配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","位置业务管理","WSFD-106701 网络侧发起的5G位置定位服务","配置AMF和LMF/GMLC对接","AMF和LMF/GMLC对接（直接模式）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于在AMF和LMF/GMLC采用直连方式对接场景，指导在AMF上如何进行配置。

## 必备事项
前提条件

已完成AMF初始配置，包括IP路由数据以及AMF基础数据配置参见《UNC初始配置与调测》>组网对接配置。
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
          description: '* AMF使用本地配置对接LMF、GMLC时的配置。   + AMF本地配置LMF/GMLC实例的概述信息、服务实例信息和服务实例回调信息。   + LMF和GMLC需要分别配置 * **ADD PNFSRVNTFSUBS**命令“回调URI（CALLBACKURI）”参数是在周期定位和NI-LR定位时使用，规划的是对端GMLC的地址。'
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
        LOCALITY:
          name: '位置信息'
          type: string
          minLength: 0
          maxLength: 150
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        CALLBACKURI:
          name: '回调URI'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list:
      type: items
      properties:
        POLICY:
          name: '服务发现策略'
          type: string
          enum:
          - LOCAL_FIRST
          - LOCAL_ONLY
          - REMOTE_ONLY
          - REMOTE_FIRST
          required: false
          description: 'AMF使用NRF进行服务发现LMF/GMLC。“服务发现策略”取值为非“LOCAL\_ONLY”时，都可能使用到NRF选择方式，此次仅为举例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      NFTYPE: NfLMF
      NFSTATUS: Registered
      FQDN: 'lmf0.huawei.com'
      INTERPLMNFQDN: 'lmf0.mcc460.mnc02.huawei.com'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.107.65.183'
      PORT: 8080
      LOCALITY: 'SHANGHAI'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnflmfinfo_list:
    - NFINSTANCEID: ''
    add_pnfgmlcinfo_list:
    - NFINSTANCEID: ''
    add_pnfservice_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NlmfLoc
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
      FQDN: 'lmf0.huawei.com'
      INTERPLMNFQDN: 'lmf0.mcc460.mnc02.huawei.com'
    add_pnfsrvntfsubs_list:
    - NFINSTANCEID: 'LMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      NTFICATIONTYPE: LocNty
      CALLBACKURI: 'http://10.60.103.60:19999/nlmf-loc/hlmf/v1/provide-location'
      N1MESSAGECLASS: Lpp
      N2INFOCLASS: Nrppa
    set_nfdiscplcy_list:
    - POLICY: REMOTE_ONLY
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**AMF使用本地配置方式，AMF本地配置LMF/GMLC实例和服务实例信息。

#### 2.1 AMF使用的LMF、GMLC可以通过本地配置方式对接，也可以通过NRF查找，需要根据实际现网规划选择对应的方式。2为本地配置方式，3为通过NRF查找时的可选配置。AMF通过**SET NFDISCPLCY**命令的“POLICY”参数取值来决定优先使用哪种方式选择LMF/GMLC。

#### 2.2 对于AMF选择LMF，AMF也可以通过SUPI/GPSI号段或切片信息本地选择LMF，对接配置请参考激活基于号段选择LMF、激活LMF选择功能，如果还需要配置特有信息、服务实例回调信息等，请参考本页面。

#### 2.3 AMF使用本地配置方式时需要配置 **ADD PNFPLMN**命令。

#### 2.4 如果不进行本地配置，AMF自动使用NRF查找方式根据LMF/GMLC的目标NFType选择。

#### 2.5 配置LMF/GMLC实例基础信息。

```jinja2
{%- if is_optional_local_config_lmf_gmlc -%}
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

#### 2.6 **可选：**配置LMF/GMLC实例特有信息。

#### 根据现网业务需要配置LMF/GMLC的特有属性信息，例如针对LMF/GMLC如果只支持某种特有外部客户端类型，则需要配置如下命令。

```jinja2
{%- if is_optional_local_config_lmf_gmlc and is_optional_lmf_gmlc_specific_info -%}
    {%- for item in add_pnflmfinfo_list -%}
        ADD PNFLMFINFO:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_local_config_lmf_gmlc and is_optional_lmf_gmlc_specific_info -%}
    {%- for item in add_pnfgmlcinfo_list -%}
        ADD PNFGMLCINFO:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 配置LMF/GMLC支持的服务实例信息。

```jinja2
{%- if is_optional_local_config_lmf_gmlc -%}
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
        {%- if item.FQDN is not none -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
        {%- if item.INTERPLMNFQDN is not none -%}
            INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 **可选：**配置LMF/GMLC支持的服务实例回调信息。

#### 此配置适用于订阅通知场景，如果LMF/GMLC订阅了AMF，则AMF通过此配置向对应的回调信息发送订阅通知。

```jinja2
{%- if is_optional_local_config_lmf_gmlc and is_optional_service_instance_callback_info -%}
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

### 3 **可选：**AMF使用NRF服务发现方式选择LMF/GMLC。

```jinja2
{%- if is_optional_nrf_service_discovery -%}
    {%- for item in set_nfdiscplcy_list -%}
        SET NFDISCPLCY:
        {#- --- 可选参数 --- -#}
        {%- if item.POLICY is not none -%}
            POLICY={{item.POLICY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

