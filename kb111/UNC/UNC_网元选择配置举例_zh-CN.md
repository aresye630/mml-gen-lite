---
id: ''
name: 网元选择配置举例
ne_type: UNC
type: feature
description: 本操作指导以PDU会话建立中的AMF选择SMF为例，介绍各种网元选择方式的配置方法。  运营商要求AMF优先选择同大区同数据中心的SMF，且优先使用远端优先的选择方式（先在缓存查找满足服务发现条件的网元（如果缓存功能关闭，则跳过此步），如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找）。
risk_level: ''
doc_source: ["网络部署","业务专题","UNC网元选择专题","5G网络的网元选择","网元选择配置举例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导以PDU会话建立中的AMF选择SMF为例，介绍各种网元选择方式的配置方法。运营商要求AMF优先选择同大区同数据中心的SMF，且优先使用远端优先的选择方式（先在缓存查找满足服务发现条件的网元（如果缓存功能关闭，则跳过此步），如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找）。

## 必备事项
前提条件

* AMF、SMF已完成到NRF的注册。
* 如果SMF不具备向NRF自动注册的能力，NRF上支持手动配置NF Profile，完成手动注册后，SMF可以正常在网络中使用NRF方式发现和被发现。SMF手动注册请参考NRF解决方案。
* 完成包含“WSFD-113000 NF发现”特性的License加载。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: '几种网元选择方式中，远端优先，先在缓存查找满足服务发现条件的网元，如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfdiscplcy_list:
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
        POLICY:
          name: '服务发现策略'
          type: string
          enum:
          - LOCAL_FIRST
          - LOCAL_ONLY
          - REMOTE_ONLY
          - REMOTE_FIRST
          required: true
          description: '用于配置目标NF的服务发现策略。'
          data_source: '本端规划'
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
    add_nfloc_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '请求方NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: '目标NF类型。'
          data_source: '全网规划'
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: '“LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。'
          data_source: '全网规划'
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list_1:
      type: items
      properties:
        LOCSELECT:
          name: 'Locality优选的匹配策略'
          type: string
          enum:
          - LOCSELECT_INVALID
          - LOCSELECT_REGION
          - LOCSELECT_DATACENTER
          - LOCSELECT_SOURCEPOOL
          required: false
          description: '在"LOCTYPE"配置为"LOCALITY"时，选择同区域同数据中心的NF。'
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
          description: '配置对接SMF的Profile信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
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
          description: '配置对接SMF的服务信息。'
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
          description: '配置对接SMF的PLMN信息。'
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
          description: '配置对接SMF实例支持的DNN及其归属切片的信息。'
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
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对接SMF实例支持的服务切片信息。'
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
    add_nfloc_list_1:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: '基于运营商要求：选择同大区同数据中心的SMF。   * “LOCALITY（位置）”：将位置信息作为仅次于目标NF优先级的策略选择目标NF。 * 在"LOCTYPE"配置为"LOCALITY"时，选择同区域同数据中心的NF。'
          data_source: ''
          pattern: ''
          default: ''
        TGTNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - NF_ALL
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - SMSF
          - NSSF
          - LMF
          - GMLC
          - FIFTHG_EIR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NF_ALL
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PREFERRED_LOCALITY
        PREFERLOC:
          name: '优选位置'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list_2:
      type: items
      properties:
        LOCSELECT:
          name: 'Locality优选的匹配策略'
          type: string
          enum:
          - LOCSELECT_INVALID
          - LOCSELECT_REGION
          - LOCSELECT_DATACENTER
          - LOCSELECT_SOURCEPOOL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfdiscplcy_list_3:
      type: items
      properties:
        CACHESWITCH:
          name: '缓存开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: 'AMF侧开启缓存。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_nfdiscplcy_list:
    - POLICY: REMOTE_FIRST
    add_pnfdiscplcy_list:
    - NFTYPE: NfSMF
      POLICY: REMOTE_FIRST
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFDAM01'
      SWITCH: ENABLE
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2NFDNR01'
      SWITCH: ENABLE
    add_nfloc_list:
    - NFTYPE: NfAMF
      TGTNFTYPE: SMF
      LOCTYPE: LOCALITY
      PREFERLOC: ''
    set_nfdiscplcy_list_1:
    - LOCSELECT: LOCSELECT_DATACENTER
    add_pnfprofile_list:
    - NFINSTANCEID: 'SMF_Instance_0'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.0.6'
      PORT: 8080
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      FQDN: ''
      SCHEME: HTTPS
    add_pnfservice_list:
    - NFINSTANCEID: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'SMF_Instance_0'
      MCC: '123'
      MNC: '03'
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      DNN: 'huawei.com'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      SST: 1
      SD: '010101'
    add_nfloc_list_1:
    - NFTYPE: NfAMF
      TGTNFTYPE: SMF
      LOCTYPE: LOCALITY
      PREFERLOC: ''
    set_nfdiscplcy_list_2:
    - LOCSELECT: LOCSELECT_DATACENTER
    set_nfdiscplcy_list_3:
    - CACHESWITCH: ON
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置服务发现策略选择方式

#### 1.1 服务发现流程策略为远端优先。

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.POLICY is not none -%}
        POLICY={{item.POLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置目标NF的服务发现策略，如果同时配置**SET NFDISCPLCY**和**ADD PNFDISCPLY**命令，则目标NF以**ADD PNFDISCPLY**的服务发现策略为准。

```jinja2
{%- for item in add_pnfdiscplcy_list -%}
    ADD PNFDISCPLCY:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    POLICY={{item.POLICY}},
    ;
{%- endfor -%}
```

### 2 配置通过NRF选择方式选择

#### 2.1 配置AMF选择同区域同数据中心的SMF。

#### 2.2 打开本特性的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.3 打开本特性的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.4 AMF选择同区域同数据中心的SMF。

```jinja2
{%- for item in add_nfloc_list -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nfdiscplcy_list_1 -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCSELECT is not none -%}
        LOCSELECT={{item.LOCSELECT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置通过本地配置方式选择

#### 3.1 配置待选择的SMF的数据（注册时与AMF同locality），包括SMF的Profile、Service、PLMN信息、支持的DNN、支持的切片实例信息。

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

#### 3.2 配置基于同区域同数据中心选择SMF，即选择到上一步配置的SMF。

```jinja2
{%- for item in add_nfloc_list_1 -%}
    ADD NFLOC:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTNFTYPE is not none -%}
        TGTNFTYPE={{item.TGTNFTYPE}},
    {%- endif -%}
    {%- if item.LOCTYPE is not none -%}
        LOCTYPE={{item.LOCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
    {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
        {%- if item.PREFERLOC is not none -%}
            PREFERLOC="{{item.PREFERLOC}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nfdiscplcy_list_2 -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCSELECT is not none -%}
        LOCSELECT={{item.LOCSELECT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置通过缓存方式选择

#### 4.1 设置缓存开关为开启。

```jinja2
{%- for item in set_nfdiscplcy_list_3 -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.CACHESWITCH is not none -%}
        CACHESWITCH={{item.CACHESWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

