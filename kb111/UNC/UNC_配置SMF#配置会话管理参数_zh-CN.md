---
id: ''
name: 配置会话管理参数
ne_type: UNC
type: feature
description: 配置SMF本局数据的基本流程包括：开始→配置移动运营商信息→配置PLMN和切片→配置本端NFUUID→配置NF信息→结束。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","配置SMF","配置会话管理参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
配置SMF本局数据的基本流程包括：开始→配置移动运营商信息→配置PLMN和切片→配置本端NFUUID→配置NF信息→结束。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: '配置SMF的NFUUID。  该命令中“NFINSTANCEID”的最后12位为NodeID，运营商可以根据规划自定义输入，最后自动生成NF实例标识UUID。'
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
    add_nfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置SMF Profile信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '网元类型'
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
          name: '网元状态'
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
    add_smfinfo_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置SMF实例信息。  当SMF与PGW-C合一部署时，“PGW名称（PGWFQDN）”参数表示PGW-C的FQDN名称，必须配置，用于用户从EPC到5G互操作流程中，帮助AMF找到EPC承载所在的融合网关。'
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
        PGWFQDN:
          name: 'PGW名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nfservice_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置SMF的Service信息。'
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
          description: '添加服务版本信息。'
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
    add_tacrange_list:
      type: items
      properties:
        INDEX:
          name: '索引标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加TAC区域信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 1024
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tairangelist_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置SMF支持的TAI。'
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
        MCC:
          name: '移动国家代码'
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
        TACRANGEINDEX:
          name: 'TAC区域标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_smfinfoext_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置smfInfo实例扩展信息。  该命令中“PRIORITY”定义的是，针对绑定到此“SMFINFOEXT”的命令**ADD NFTAI**或**ADD TAIRANGELIST**定义的位置区，SMF提供服务的优先级。  说明：  请先配置**ADD NFTAI**或**ADD TAIRANGELIST**命令后，再配置**ADD SMFINFOEXT**命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ID:
          name: 'SMFINFOID'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65536
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 65536
    set_mulsmfpdureepol_list:
      type: items
      properties:
        MULSMFPDUREESUP:
          name: '是否支持多SMFInfo下会话重建'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '配置多smfInfo场景下的PDU会话重建策略。'
          data_source: '本端规划'
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
          description: '增加NF支持的网络切片。'
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN。'
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
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
    set_uednsbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MDNSSERVERV4:
          name: 'IPv4主DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BDNSSERVERV4:
          name: 'IPv4备DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_nfuuid_list:
    - NFTYPE: NfSMF
      NFINSTANCENAME: 'SMF_Instance_0'
    add_nfprofile_list:
    - NFINSTANCENAME: 'SMF_Instance_0'
      NFTYPE: NfSMF
      NFSTATUS: Registered
    add_smfinfo_list:
    - SMFINSTANCENAME: 'SMF_Instance_0'
      SMFNAME: 'SMF01'
      PGWFQDN: 'HUAWEI1.COM.APN.EPC.MNC003.MCC123.3GPPNETWORK.ORG'
    add_nfservice_list:
    - NFINSTANCENAME: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
    add_nfservicever_list:
    - NFINSTANCENAME: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    add_tacrange_list:
    - INDEX: 1
      RANGESTART: '101010'
      RANGEEND: '101019'
      DESC: 'TAC_example'
    add_tairangelist_list:
    - NFINSTANCENAME: 'SMF_Instance_0'
      NFTYPE: NfSMF
      MCC: '123'
      MNC: '03'
      TACRANGEINDEX: 1
    add_smfinfoext_list:
    - SMFINSTANCENAME: 'SMF_Instance_0'
      ID: 'SMFINFO_Instance_0'
      PRIORITY: 10
    set_mulsmfpdureepol_list:
    - MULSMFPDUREESUP: Support
    add_nfns_list:
    - NFTYPE: NfSMF
      NSIDX: 0
    add_apn_list:
    - APN: 'huawei.com'
      VIRTUALAPN: DISABLE
      HASVPN: DISABLE
      VPNINSTANCE: ''
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'huawei.com'
    set_uednsbindapn_list:
    - APN: 'huawei.com'
      MDNSSERVERV4: '10.10.1.1'
      BDNSSERVERV4: '10.10.1.2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置SMF实例信息。

#### 1.1 配置SMF实例的名称。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 1.2 配置SMF实例的Profile信息。

```jinja2
{%- for item in add_nfprofile_list -%}
    ADD NFPROFILE:
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

#### 1.3 **可选：**配置SMF的域名等信息。

```jinja2
{%- if is_optional_smf_domain_info -%}
    {%- for item in add_smfinfo_list -%}
        ADD SMFINFO:
        {#- --- 必选参数 --- -#}
        SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SMFNAME is not none -%}
            SMFNAME="{{item.SMFNAME}}",
        {%- endif -%}
        {%- if item.PGWFQDN is not none -%}
            PGWFQDN="{{item.PGWFQDN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置SMF提供的服务实例及其版本信息。

##### 1.4.1 配置SMF提供的服务实例信息。

```jinja2
{%- for item in add_nfservice_list -%}
    ADD NFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    ;
{%- endfor -%}
```

##### 1.4.2 配置服务实例的版本信息。

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

#### 1.5 配置SMF实例支持的TAI信息。

```jinja2
{%- for item in add_tacrange_list -%}
    ADD TACRANGE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    RANGESTART="{{item.RANGESTART}}",
    RANGEEND="{{item.RANGEEND}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tairangelist_list -%}
    ADD TAIRANGELIST:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    NFTYPE={{item.NFTYPE}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    TACRANGEINDEX={{item.TACRANGEINDEX}},
    ;
{%- endfor -%}
```

### 2 （可选）配置smfInfo实例扩展信息

```jinja2
{%- if is_optional_smf_info_ext -%}
    {%- for item in add_smfinfoext_list -%}
        ADD SMFINFOEXT:
        {#- --- 必选参数 --- -#}
        SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
        ID="{{item.ID}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 （可选）配置多smfInfo场景下的PDU会话重建策略。

```jinja2
{%- if is_optional_pdu_session_rebuild_policy -%}
    {%- for item in set_mulsmfpdureepol_list -%}
        SET MULSMFPDUREEPOL:
        {#- --- 可选参数 --- -#}
        {%- if item.MULSMFPDUREESUP is not none -%}
            MULSMFPDUREESUP={{item.MULSMFPDUREESUP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置SMF支持的网络切片。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

### 5 配置SMF支持的APN、网络切片支持的DNN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
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

### 6 在使用DNS服务器场景下，配置指定APN的DNS属性。

```jinja2
{%- for item in set_uednsbindapn_list -%}
    SET UEDNSBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MDNSSERVERV4 is not none -%}
        MDNSSERVERV4="{{item.MDNSSERVERV4}}",
    {%- endif -%}
    {%- if item.BDNSSERVERV4 is not none -%}
        BDNSSERVERV4="{{item.BDNSSERVERV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

