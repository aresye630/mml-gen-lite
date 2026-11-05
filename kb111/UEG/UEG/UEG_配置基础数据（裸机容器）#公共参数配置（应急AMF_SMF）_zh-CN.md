---
id: ''
name: 公共参数配置（应急AMF/SMF）
ne_type: UEG
type: feature
description: 本章节用于指导应急AMF和应急SMF的公共数据配置，包括运营商、切片、DNN等信息。园区应急AMF、应急SMF和中心侧网络的AMF、SMF公共参数保持一致。  以下配置数据以及步骤均以UEG-M双DC组网场景的配置规划为例进行介绍。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置基础数据（裸机容器）","公共参数配置（应急AMF/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本章节用于指导应急AMF和应急SMF的公共数据配置，包括运营商、切片、DNN等信息。园区应急AMF、应急SMF和中心侧网络的AMF、SMF公共参数保持一致。以下配置数据以及步骤均以UEG-M双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_ngmno_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置运营商信息。  由于整系统中初始默认存在一条“NOID”为0的记录，且整机仅支持配置一条记录，因此不能再执行**ADD NGMNO**命令修改运营商全称和简称信息，只能通过**MOD NGMNO**命令修改初始的运营商全称和简称信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置运营商签约用户的Home PLMN信息。  当前UEG中默认存在一条“NOID”为0的记录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '园区AMF和SMF的PLMN配置需要和中心网络保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngsrvplmn_list:
      type: items
      properties:
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '配置运营商的Serving PLMN信息。该PLMN标识设备所使用的PLMN，用于和无线对接时使用。  **园区应急AMF的PLMN配置需要和中心网络AMF的PLMN保持一致。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '其中参数NOID已通过**ADD NGMNO**命令配置，此处引用已配置的NOID。  当前UEG中默认存在一条“NOID”为0的记录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '**园区应急AMF的PLMN配置需要和中心网络AMF的PLMN保持一致。**'
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
    add_cpmnclen_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '配置各MCC值所对应的MNC长度。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNCLEN:
          name: '对应MCC的MNC长度'
          type: integer
          minimum: 2
          maximum: 3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 2
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置园区Serving PLMN下支持的网络切片。  **园区的PLMN配置需要和中心网络的PLMN保持一致。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '已通过**ADD NGSRVPLMN**命令配置，可以通过**LST NGSRVPLMN**命令查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置园区切片信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_guami_list:
      type: items
      properties:
        INDEX:
          name: 'GUAMI索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置AMF支持的GUAMI列表。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '已通过**ADD NGSRVPLMN**命令配置，可以通过**LST NGSRVPLMN**命令查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFREGIONID:
          name: 'AMF区域标识'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: '园区内双DC内的两个AMF的AMF Region ID和AMF Set ID需要和中心网络保持一致。  因为园区的无线基站连接中心网络和本园区的AMF，不会连接其他园区的AMF，因此**园区AMF的AMFPOINTER必须和中心网络的不同，但不同园区的AMFPOINTER可以相同。园区内双DC的2个AMF的AMFPOINTER必须不同。**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFPOINTER:
          name: 'AMF指示符'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: '全网规划'
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
          description: '配置应急AMF和SMF实例信息。  该命令中“NFINSTANCEID”的最后12位为NodeID，运营商可以根据规划自定义输入，最后自动生成NF实例标识UUID。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpnfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置AMF和SMF的Profile信息。'
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: ''
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
          - Undiscoverable
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Registered
    add_amfinfo_list:
      type: items
      properties:
        AMFINSTANCENAME:
          name: 'AMF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置AMF实例信息，如AMF名称、开放给互联运营商的FQDN等信息。  **园区应急AMF的CAPACITY固定配置为0。**  **双DC内的两个AMF的CAPACITY配置相同的取值0，用于组成AMF Pool，进行负荷分担。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFNAME:
          name: 'AMF名称'
          type: string
          minLength: 0
          maxLength: 150
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 255
    add_smfinfo_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置SMF的SMFINO信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMFNAME:
          name: 'SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpnfservice_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置AMF提供的Service服务实例信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nfservicever_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置AMF和SMF提供的Service版本信息。'
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
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
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
          description: '配置AMF和SMF支持的本园区的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '已通过**ADD PLMNNS**配置，可以通过**LST PLMNNS**查询。'
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
          description: '配置园区DNN信息。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '增加网络切片支持的DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_globaldns_list:
      type: items
      properties:
        MDNSSERVERV4:
          name: 'IPv4主DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BDNSSERVERV4:
          name: 'IPv4备DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_cpaddressattr_list:
      type: items
      properties:
        ALLOCPRECEDENCE:
          name: 'UE地址分配属性'
          type: string
          enum:
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: '-'
          data_source: '全局规划'
          pattern: ''
          default: ''
    set_ngmmpara_list:
      type: items
      properties:
        T3512:
          name: 'T3512(min)'
          type: integer
          minimum: 1
          maximum: 310
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器(min)'
          type: integer
          minimum: 2
          maximum: 322
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_ngsrvplmn_list:
    - PLMNIDX: 0
      NOID: 0
      MCC: '123'
      MNC: '03'
    - PLMNIDX: 0
      NOID: 0
      MCC: '123'
      MNC: '03'
    add_cpmnclen_list:
    - MCC: '123'
      MNCLEN: 2
    - MCC: '123'
      MNCLEN: 2
    add_plmnns_list:
    - NSIDX: 0
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
    - NSIDX: 0
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
    add_guami_list:
    - INDEX: 0
      PLMNIDX: 0
      AMFREGIONID: '00'
      AMFSETID: '001'
      AMFPOINTER: '01'
    - INDEX: 0
      PLMNIDX: 0
      AMFREGIONID: '00'
      AMFSETID: '001'
      AMFPOINTER: '02'
    add_nfuuid_list:
    - NFTYPE: NfAMF
      NFINSTANCENAME: 'AMF_Instance_0'
    - NFTYPE: NfAMF
      NFINSTANCENAME: 'AMF_Instance_1'
    add_cpnfprofile_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      NFTYPE: NfAMF
      NFSTATUS: Registered
    - NFINSTANCENAME: 'AMF_Instance_1'
      NFTYPE: NfAMF
      NFSTATUS: Registered
    add_amfinfo_list:
    - AMFINSTANCENAME: 'AMF_Instance_0'
      AMFNAME: 'amf0.cluster1.net2.amf.5gc.mnc003.mcc123.3gppnetwork.org'
      CAPACITY: 0
    - AMFINSTANCENAME: 'AMF_Instance_1'
      AMFNAME: 'amf1.cluster1.net2.amf.5gc.mnc003.mcc123.3gppnetwork.org'
      CAPACITY: 0
    add_smfinfo_list:
    - SMFINSTANCENAME: 'SMF_Instance_0'
      SMFNAME: 'SMF01'
    - SMFINSTANCENAME: 'SMF_Instance_1'
      SMFNAME: 'SMF02'
    add_cpnfservice_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
    - NFINSTANCENAME: 'AMF_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
    add_nfservicever_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    - NFINSTANCENAME: 'AMF_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 0
    add_cpapn_list:
    - APN: 'huawei.com'
      VIRTUALAPN: DISABLE
      HASVPN: DISABLE
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'huawei.com'
    set_globaldns_list:
    - MDNSSERVERV4: '10.10.10.1'
      BDNSSERVERV4: '10.10.10.2'
    set_cpaddressattr_list:
    - ALLOCPRECEDENCE: UPF_FIRST
    set_ngmmpara_list:
    - T3512: 15
      RCHTMR: 20
    - T3512: 15
      RCHTMR: 20
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置运营商基础信息。

### 双DC组网场景下，对于DC1和DC2中的AMF和SMF步骤1中的a~e配置完全相同。

#### 1.1 配置运营商信息。当前系统默认有一条“NOID”为0的记录，需使用MOD NGMNO命令增加运营商名称信息 。

##### 1.1.1 //DC1

```jinja2
{%- for item in mod_ngmno_list -%}
    MOD NGMNO:
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

#### 1.2 配置运营商签约用户的Home PLMN信息。

##### 1.2.1 //DC1

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

#### 1.3 配置运营商的Serving PLMN信息，该PLMN表示移动运营商网络中各设备使用的PLMN，AMF和无线对接时使用该PLMN。

##### 1.3.1 //DC1

```jinja2
{%- for item in add_ngsrvplmn_list -%}
    ADD NGSRVPLMN:
    {#- --- 必选参数 --- -#}
    PLMNIDX={{item.PLMNIDX}},
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 1.4 配置各MCC值所对应的MNC长度。

##### 1.4.1 //DC1

```jinja2
{%- for item in add_cpmnclen_list -%}
    ADD CPMNCLEN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MNCLEN is not none -%}
        MNCLEN={{item.MNCLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 配置运营商支持的网络切片。

##### 1.5.1 //DC1

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
    {%- if item.STATE is not none -%}
        STATE={{item.STATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 配置AMF全局标识。

##### 1.6.1 //DC1

```jinja2
{%- for item in add_guami_list -%}
    ADD GUAMI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    PLMNIDX={{item.PLMNIDX}},
    AMFREGIONID="{{item.AMFREGIONID}}",
    AMFSETID="{{item.AMFSETID}}",
    AMFPOINTER="{{item.AMFPOINTER}}",
    ;
{%- endfor -%}
```

### 2 配置AMF和SMF实例信息。

#### 2.1 配置AMF和SMF实例的名称。

##### 2.1.1 //DC1

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 2.2 配置AMF和SMF实例的Profile信息。

##### 2.2.1 //DC1

```jinja2
{%- for item in add_cpnfprofile_list -%}
    ADD CPNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置AMF和SMF的域名等信息。

##### 2.3.1 //DC1

```jinja2
{%- for item in add_amfinfo_list -%}
    ADD AMFINFO:
    {#- --- 必选参数 --- -#}
    AMFINSTANCENAME="{{item.AMFINSTANCENAME}}",
    AMFNAME="{{item.AMFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_smfinfo_list -%}
    ADD SMFINFO:
    {#- --- 必选参数 --- -#}
    SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SMFNAME is not none -%}
        SMFNAME="{{item.SMFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置AMF和SMF提供的服务实例及其版本信息。

##### 2.4.1 配置AMF和SMF提供的服务实例信息。

###### 2.4.1.1 //DC1

```jinja2
{%- for item in add_cpnfservice_list -%}
    ADD CPNFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    ;
{%- endfor -%}
```

##### 2.4.2 配置服务实例的版本信息。

###### 2.4.2.1 //DC1

```jinja2
{%- for item in add_nfservicever_list -%}
    ADD NFSERVICEVER:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    APIFULLVERSION="{{item.APIFULLVERSION}}",
    ;
{%- endfor -%}
```

### 3 配置AMF和SMF支持的网络切片。

#### 3.1 //DC1&DC2

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

### 4 配置SMF支持的APN、网络切片支持的DNN。

#### 4.1 //DC1&DC2

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 5 （可选）在使用DNS服务器场景下，配置业务层DNS信息。

#### 5.1 //DC1&DC2

```jinja2
{%- if is_optional_business_dns -%}
    {%- for item in set_globaldns_list -%}
        SET GLOBALDNS:
        {#- --- 可选参数 --- -#}
        {%- if item.MDNSSERVERV4 is not none -%}
            MDNSSERVERV4="{{item.MDNSSERVERV4}}",
        {%- endif -%}
        {%- if item.BDNSSERVERV4 is not none -%}
            BDNSSERVERV4="{{item.BDNSSERVERV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 l（可选）配置UE 动态IP地址分配策略为UPF分配(默认为UPF\_FIRST)。

#### 6.1 //DC1&DC2

```jinja2
{%- if is_optional_ue_ip_allocation_upf -%}
    {%- for item in set_cpaddressattr_list -%}
        SET CPADDRESSATTR:
        {#- --- 可选参数 --- -#}
        {%- if item.ALLOCPRECEDENCE is not none -%}
            ALLOCPRECEDENCE={{item.ALLOCPRECEDENCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置NG移动性管理相关的定时器参数，将周期TAU的时长设置为15min。

#### 7.1 //DC1

```jinja2
{%- for item in set_ngmmpara_list -%}
    SET NGMMPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.T3512 is not none -%}
        T3512={{item.T3512}},
    {%- endif -%}
    {%- if item.RCHTMR is not none -%}
        RCHTMR={{item.RCHTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

