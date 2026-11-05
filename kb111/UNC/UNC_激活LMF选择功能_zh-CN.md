---
id: ''
name: 激活LMF选择功能
ne_type: UNC
type: feature
description: 本操作指导用于介绍AMF支持通过配置LMFId、用户切片信息选择LMF的激活过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","位置业务管理","WSFD-106407 LMF选择功能","激活LMF选择功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导用于介绍AMF支持通过配置LMFId、用户切片信息选择LMF的激活过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-106407 LMF选择功能特性概述。
* 基于网络侧发起的5G位置定位服务业务才会触发AMF选择LMF，所以，如果激活AMF选择LMF，还需要先完成激活网络侧发起的5G位置定位服务。
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
          description: '配置对端LMF1、LMF0的信息。'
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
          description: ''
          data_source: '全网规划'
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
    add_pnflmfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: 'AMF本地配置LMF支持的LMFID，后续符合LMFID条件的用户业务会直接选择到对应的LMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LMFID:
          name: 'LMF标识'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置对端LMF支持的服务切片信息，后续符合切片信息的用户业务会直接选择到对应的LMF。'
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
    set_nglcspara_list:
      type: items
      properties:
        CAMPLCSEN:
          name: '园区定位增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '开启园区定位增强开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NSSW:
          name: '是否使用切片'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '开启切片选择开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_allowsername_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '只允许指定网元访问AMF的Namf\_Location服务。（本特性以GMLC访问为例）'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 60
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALADDR:
          name: '本端地址'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERADDR:
          name: '对端地址'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '对端GMLC的地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_lcspermitcfg_list:
      type: items
      properties:
        OPTYPE:
          name: '定位服务操作类型'
          type: string
          enum:
          - Namf_Location_ProvidePositioningInfo
          - Namf_Location_ProvideLocationInfo
          - Namf_Location_EventNotify
          required: true
          description: '用于AMF对收到的GMLC的定位请求时检查GMLC的定位请求是否越权，对越权的GMLC，AMF拒绝其定位请求。  “USRGRPID”参数来源于**ADD NGUSRGRP**，并且用户群组成员已通过**ADD NGUSRGRPMEM**完成配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: ''
          data_source: '本端规划'
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
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'LMF_Instance_1'
      NFTYPE: NfLMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.18.0.2'
      PRIORITY: 100
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      FQDN: ''
      SCHEME: HTTPS
    add_pnflmfinfo_list:
    - NFINSTANCEID: 'LMF_Instance_1'
      LMFID: '0001'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'LMF_Instance_1'
      SST: 1
      SD: '010101'
    set_nglcspara_list:
    - CAMPLCSEN: ON
      NSSW: YES
    add_allowsername_list:
    - INDEX: 0
      NFINSTANCEID: 'AMF_Instance_0'
      SERVICENAME: 'namf-loc'
      LOCALADDR: '10.16.1.5'
      PEERADDR: '10.112.1.5'
    add_lcspermitcfg_list:
    - OPTYPE: Namf_Location_ProvidePositioningInfo
      IPTYPE: IPTypeV4
      IPV4ADDRESS: '10.112.1.5'
      USRGRPID: 20
      IPV6ADDRESS: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 AMF上配置对接的LMF基础信息。

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

### 2 **可选：**AMF上配置LMF支持的LMFID信息。

```jinja2
{%- if is_optional_lmf_lmfid_info -%}
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

### 3 **可选：**AMF上配置LMF支持的用户切片信息。

```jinja2
{%- if is_optional_lmf_user_slice_info -%}
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
{%- endif -%}
```

### 4 AMF上配置LMF选择功能开关。

```jinja2
{%- for item in set_nglcspara_list -%}
    SET NGLCSPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.CAMPLCSEN is not none -%}
        CAMPLCSEN={{item.CAMPLCSEN}},
    {%- endif -%}
    {%- if item.NSSW is not none -%}
        NSSW={{item.NSSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**位置定位安全加固配置。

#### 5.1 建议增加AMF的位置定位服务白名单配置，确保仅限于合法的GMLC访问。

```jinja2
{%- if is_optional_location_security_hardening -%}
    {%- for item in add_allowsername_list -%}
        ADD ALLOWSERNAME:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SERVICENAME="{{item.SERVICENAME}}",
        LOCALADDR="{{item.LOCALADDR}}",
        PEERADDR="{{item.PEERADDR}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 建议AMF和GMLC侧开启SBI接口加密，降低网络安全风险。

#### AMF侧开启SBI接口加密请参考激活SBI接口加密特性(CERT)。

#### GMLC侧开启SBI接口加密请参考对应的产品描述。

#### 5.3 建议增加定位服务权限，用于AMF收到GMLC的定位请求时检查GMLC的定位请求是否越权，对越权的GMLC，AMF拒绝其定位请求。（用于B2B场景）

```jinja2
{%- if is_optional_location_security_hardening -%}
    {%- for item in add_lcspermitcfg_list -%}
        ADD LCSPERMITCFG:
        {#- --- 必选参数 --- -#}
        OPTYPE={{item.OPTYPE}},
        IPTYPE={{item.IPTYPE}},
        USRGRPID={{item.USRGRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

