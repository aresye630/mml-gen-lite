---
id: ''
name: 配置NSSF主备容灾
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活NSSF主备容灾的操作过程，组网请见NSSF双活容灾组网。  NSSF通过跨DC（Data Center）建立主备容灾组，将主用NSSF中的业务数据在备用NSSF中进行备份，所有AMF将通过配置高低优先级决定主用NSSF和备用NSSF，实现容灾管理。当主用NSSF网元故障，AMF检测到主用NSSF故障则将业务选择到备用NSSF，备用NSSF网元能够接管故障主用NSSF的业务，保证业务连续性。NSSF故障恢复后，AMF会自动回切主用NSSF进行业务。  适用于AMF、NSSF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF容灾组网","配置NSSF主备容灾"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP DRINFO')
- getParameterValue('ADD DRINST')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活NSSF主备容灾的操作过程，组网请见NSSF双活容灾组网。NSSF通过跨DC（Data Center）建立主备容灾组，将主用NSSF中的业务数据在备用NSSF中进行备份，所有AMF将通过配置高低优先级决定主用NSSF和备用NSSF，实现容灾管理。当主用NSSF网元故障，AMF检测到主用NSSF故障则将业务选择到备用NSSF，备用NSSF网元能够接管故障主用NSSF的业务，保证业务连续性。NSSF故障恢复后，AMF会自动回切主用NSSF进行业务。适用于AMF、NSSF。

## 必备事项
前提条件

前提条件

* 已完成加载License。
* 请仔细阅读NSSF容灾原理。
* 已按照自身组网完成双活NSSF之间的路由配置，对于IPv4组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 已按照自身组网完成双活NSSF之间的路由配置，对于IPv6组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_drinst_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例标识'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '配置容灾实例信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DRINSTNAME:
          name: '容灾实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_drcomm_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例标识'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '配置容灾实例通信地址信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - COMM_IPV4
          - COMM_IPV6
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        COMMIPV4:
          name: '通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        COMMIPV6:
          name: '通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
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
    rst_nodebatch_list:
      type: items
      properties:
        APPID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
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
        PRIORITY:
          name: '优先级'
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
          description: ''
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
  examples:
    add_drinst_list:
    - DRINSTID: 0
      DRINSTNAME: 'DR1'
    add_drcomm_list:
    - DRINSTID: 0
      IPVERSION: COMM_IPV4
      COMMIPV4: '10.5.5.1'
      VPNNAME: 'DR_VPN'
      COMMIPV6: '2001:db8:1::'
    set_licenseswitch_list:
    - LICITEM: 'LKV2ASNSSR01'
      SWITCH: DISABLE
    rst_nodebatch_list:
    - APPID: 0
    add_pnfprofile_list:
    - NFINSTANCEID: 'NSSF_Instance_0'
      NFTYPE: NfNSSF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.182'
      PORT: 8080
      PRIORITY: 0
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
    - NFINSTANCEID: 'NSSF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NnssfNsSel
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置NSSF：每个NSSF都按如下操作配置

#### 1.1 完成NSSF基础配置，具体步骤与非容灾组网完全一致，请参考NSSF配置。

#### 1.2 进入“MML命令行-UNC”窗口。

#### 1.3 配置主、备NSSF的容灾实例信息。

```jinja2
{%- for item in add_drinst_list -%}
    ADD DRINST:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DRINSTNAME is not none -%}
        DRINSTNAME="{{item.DRINSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置容灾实例通信地址信息。

```jinja2
{%- for item in add_drcomm_list -%}
    ADD DRCOMM:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    IPVERSION={{item.IPVERSION}},
    VPNNAME="{{item.VPNNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=COMM_IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV4' -%}
        COMMIPV4="{{item.COMMIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=COMM_IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV6' -%}
        COMMIPV6="{{item.COMMIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 等待30秒后查询容灾信息，若数据备份状态为容灾准备状态，则执行下一步，否则请收集信息并寻求技术支持。

#### 1.6 在主、备NSSF上分别进行“关闭”和“打开”本特性的License配置开关，确保容灾功能成功激活。

```jinja2
{%- set DSP_DRINFO=getParameterValue('DSP DRINFO') -%}
{%- if DSP_DRINFO=='容灾准备状态' -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.7 复位NSSF。

#### “容灾实例标识”为0时，不需要复位NSSF。

```jinja2
{%- set ADD_DRINST=getParameterValue('ADD DRINST') -%}
{%- if not (ADD_DRINST=='0') -%}
    {%- for item in rst_nodebatch_list -%}
        RST NODEBATCH:
        {#- --- 必选参数 --- -#}
        APPID={{item.APPID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置AMF

### NSSF主备容灾组网下需要在AMF本地分别配置对接高低优先级的NSSF（本大区部署的NSSF为高优先级，对端大区部署的NSSF为低优先级）。

### 其他配置与NSSF非容灾组网完全一致，请参考AMF配置。

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

