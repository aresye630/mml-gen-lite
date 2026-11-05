---
id: ''
name: 配置与NSSF对接数据
ne_type: UNC
type: feature
description: '* 如果网络中部署了NRF，则需执行配置到NRF的数据。 * 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行可选：本地配置到NSSF的对接数据。    当网络中既部署了NRF，又本地配置了本地配置到NSSF的对接数据时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认为优先选择本地配置的NSSF。'
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF非容灾组网","AMF配置","配置与NSSF对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* 如果网络中部署了NRF，则需执行配置到NRF的数据。* 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行可选：本地配置到NSSF的对接数据。  当网络中既部署了NRF，又本地配置了本地配置到NSSF的对接数据时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认为优先选择本地配置的NSSF。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF的地址信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'NRF的服务端地址信息。'
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'NRF的服务端端口信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF协议参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ON
    add_subcondition_list:
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
          data_source: ''
          pattern: ''
          default: ''
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrf_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 0
    add_nrfaddr_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF的地址信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'NRF的服务端地址信息。'
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'NRF的服务端端口信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF协议参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ON
    add_subcondition_list_1:
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
          data_source: ''
          pattern: ''
          default: ''
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
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
          description: '打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    act_nfonline_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '激活AMF向NRF注册。'
          data_source: '全网规划'
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
          description: '配置周边NF的Profile信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: '全网规划'
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
          description: '配置周边NF的服务信息。'
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
  examples:
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: FALSE
      PRIORITY: 0
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    add_subcondition_list:
    - NFTYPE: NfSMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    add_nrf_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.26.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    add_nrfpara_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    add_subcondition_list_1:
    - NFTYPE: NfSMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
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

### 1 **可选：配置到NRF的数据**

### 如果网络中未部署NRF，则无法执行本步骤，需手工配置AMF与周边NF的逻辑连接，配置步骤参见配置与NSSF对接数据。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 配置NRF信息。

```jinja2
{%- if is_optional_config_nrf_data -%}
    {%- for item in add_nrf_list -%}
        ADD NRF:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        TLS={{item.TLS}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置NRF的地址信息。

```jinja2
{%- if is_optional_config_nrf_data -%}
    {%- for item in add_nrfaddr_list -%}
        ADD NRFADDR:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
        {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
            PORT={{item.PORT}},
        {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 **可选：**配置NRF协议参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

```jinja2
{%- if is_optional_config_nrf_data and is_optional_config_nrf_proto_para -%}
    {%- for item in add_nrfpara_list -%}
        ADD NRFPARA:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.WAITINTERVAL is not none -%}
            WAITINTERVAL={{item.WAITINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRETRYTIMES is not none -%}
            MAXRETRYTIMES={{item.MAXRETRYTIMES}},
        {%- endif -%}
        {%- if item.LOADCARRYINHB is not none -%}
            LOADCARRYINHB={{item.LOADCARRYINHB}},
        {%- endif -%}
        {%- if item.SUBSCRISWITCH is not none -%}
            SUBSCRISWITCH={{item.SUBSCRISWITCH}},
        {%- endif -%}
        {%- if item.OAUTH2SWITCH is not none -%}
            OAUTH2SWITCH={{item.OAUTH2SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_nrf_data and is_optional_config_nrf_proto_para -%}
    {%- for item in add_subcondition_list -%}
        ADD SUBCONDITION:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CONDITION is not none -%}
            CONDITION={{item.CONDITION}},
        {%- endif -%}
        {%- if item.REQNOTIFEVENT is not none -%}
            REQNOTIFEVENT={{item.REQNOTIFEVENT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 **可选：**当网络中规划了双主或者主备NRF时，需要配置本步骤。双主NRF场景下，NF对接的优先级高的NRF为本地DC的NRF；主备NRF场景下，NF对接的优先级高的NRF为主NRF。

```jinja2
{%- if is_optional_config_nrf_data and is_optional_dual_active_nrf -%}
    {%- for item in add_nrf_list_1 -%}
        ADD NRF:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        TLS={{item.TLS}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_nrf_data and is_optional_dual_active_nrf -%}
    {%- for item in add_nrfaddr_list_1 -%}
        ADD NRFADDR:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
        {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
            PORT={{item.PORT}},
        {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_nrf_data and is_optional_dual_active_nrf -%}
    {%- for item in add_nrfpara_list_1 -%}
        ADD NRFPARA:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.WAITINTERVAL is not none -%}
            WAITINTERVAL={{item.WAITINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRETRYTIMES is not none -%}
            MAXRETRYTIMES={{item.MAXRETRYTIMES}},
        {%- endif -%}
        {%- if item.LOADCARRYINHB is not none -%}
            LOADCARRYINHB={{item.LOADCARRYINHB}},
        {%- endif -%}
        {%- if item.SUBSCRISWITCH is not none -%}
            SUBSCRISWITCH={{item.SUBSCRISWITCH}},
        {%- endif -%}
        {%- if item.OAUTH2SWITCH is not none -%}
            OAUTH2SWITCH={{item.OAUTH2SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_nrf_data and is_optional_dual_active_nrf -%}
    {%- for item in add_subcondition_list_1 -%}
        ADD SUBCONDITION:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CONDITION is not none -%}
            CONDITION={{item.CONDITION}},
        {%- endif -%}
        {%- if item.REQNOTIFEVENT is not none -%}
            REQNOTIFEVENT={{item.REQNOTIFEVENT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.1 请保证已完成AMF到双主或者主备NRF的路由数据配置。

##### 1.5.2 请提前规划**ADD NRFPARA**中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保AMF对NRF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。AMF探测时长请参考WSFD-114002 NRF双活容灾特性概述中“原理概述”>“可靠性机制”小节。

#### 1.6 打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。

```jinja2
{%- if is_optional_config_nrf_data -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.7 激活AMF向NRF注册。

```jinja2
{%- if is_optional_config_nrf_data -%}
    {%- for item in act_nfonline_list -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **可选：本地配置到NSSF的对接数据**

#### 2.1 配置到NSSF的数据，包括NSSF的Profile、Service等信息。

```jinja2
{%- if is_optional_local_config_nssf_data -%}
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
{%- endif -%}
```

```jinja2
{%- if is_optional_local_config_nssf_data -%}
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
{%- endif -%}
```

