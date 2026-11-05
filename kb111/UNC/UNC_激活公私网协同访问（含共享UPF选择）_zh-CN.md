---
id: ''
name: 激活公私网协同访问（含共享UPF选择）
ne_type: UNC
type: feature
description: 本操作指导介绍部署公私网协同访问特性的操作过程。  如果在初始配置中已经规划SMF是与主锚点、辅锚点和UL CL UPF合一部署的UPF对接，如下准备数据和配置步骤可能在初始配置中就已完成，此时无需重复配置。本章节通过以下准备数据和配置步骤与任务示例说明与该合一UPF对接的配置逻辑。  SMF支持用户通过同一个DNN（Data Network Name）访问公网和私网业务，同时私网之间业务隔离。SMF将为用户优先选择主锚点、辅锚点和UL CL UPF合一部署的UPF，分别建立到主锚点和辅锚点UPF的N4会话，同时访问公网和私网业务。SMF针对不同用户策略配置不同DNAI（Data Network Access Identifier），UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别不同的辅锚点N4会话，实现私网之间业务隔离。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","分布式网络功能","WSFD-223002 公私网协同访问（含共享UPF选择）","激活公私网协同访问（含共享UPF选择）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍部署公私网协同访问特性的操作过程。如果在初始配置中已经规划SMF是与主锚点、辅锚点和UL CL UPF合一部署的UPF对接，如下准备数据和配置步骤可能在初始配置中就已完成，此时无需重复配置。本章节通过以下准备数据和配置步骤与任务示例说明与该合一UPF对接的配置逻辑。SMF支持用户通过同一个DNN（Data Network Name）访问公网和私网业务，同时私网之间业务隔离。SMF将为用户优先选择主锚点、辅锚点和UL CL UPF合一部署的UPF，分别建立到主锚点和辅锚点UPF的N4会话，同时访问公网和私网业务。SMF针对不同用户策略配置不同DNAI（Data Network Access Identifier），UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别不同的辅锚点N4会话，实现私网之间业务隔离。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-223002 公私网协同访问（含共享UPF选择）特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: 'SMF本端配置共享UPF。'
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
          name: 'IP地址'
          type: string
          maxLength: 15
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
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置共享UPF支持的服务切片信息。'
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
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置共享UPF支持的DNN。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_pnfdnai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置共享UPF支持的DNAI。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PNFDNNINDEX:
          name: '对端NF的DNN索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置共享UPF的属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UP位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UP支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        SHAREDUPFSW:
          name: 'UPF共享开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '共享UPF场景下本参数取值为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        PSACOMBINEULCL:
          name: '主锚点与分流节点合设功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SUPULCLBPONLY:
          name: '是否仅支持作为分流UPF'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_virtualupfid_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置虚拟UPF实例标识和DNAI的绑定关系。  共享UPF场景下通过配置虚拟UPF标识辅锚点会话，并且为虚拟UPF配置DNAI，UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vupfidbinddnai_list:
      type: items
      properties:
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '配置位置区域。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'AREA类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '为位置区添加区域范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
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
          description: '配置共享UPF支持的区域。'
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
          data_source: ''
          pattern: ''
          default: ''
    add_dnaiupfinfo_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnarea_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREATYPE:
          name: 'DNAI服务区域类型'
          type: string
          enum:
          - N2TAI
          - N2CID
          - S1TAI
          - S1CID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'DNAI服务区名称支持5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'DNAI服务区名称支持5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnaibinddnarea_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREANAME:
          name: 'DNAI服务区域名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnaiupselply_list:
      type: items
      properties:
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SUPFS01'
      SWITCH: ENABLE
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      SCHEME: HTTPS
    add_pnfns_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '000001'
    add_pnfdnn_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'Huawei.com'
    add_pnfdnai_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      DNAI: 'testdnai'
      PNFDNNINDEX: 3
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: UlClAndBp
      SHAREDUPFSW: ENABLE
      PSACOMBINEULCL: DISABLE
      SUPULCLBPONLY: ''
    add_virtualupfid_list:
    - UPFINSTANCEID: 'UPF_Instance_0'
      VUPFINSTANCEID: 'v_UPF_Instance_0'
    add_vupfidbinddnai_list:
    - VUPFINSTANCEID: 'v_UPF_Instance_0'
      DNAI: 'testdnai'
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12303260101'
      N2ENDTAI: '12303260110'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    add_dnaiupfinfo_list:
    - DNAI: ''
      UPFINSTANCEID: ''
    add_dnarea_list:
    - AREANAME: 'DNAREA1'
      AREATYPE: N2TAI
    add_dnareabindn2tai_list:
    - AREANAME: 'DNAREA1'
      N2BEGINTAI: '12303260101'
      N2ENDTAI: '12303260103'
    add_dnaibinddnarea_list:
    - DNAI: 'stadiumdnai'
      AREANAME: 'DNAREA1'
    set_apnupselply_list:
    - APN: ''
    add_dnaiupselply_list:
    - DNAI: ''
    set_pfcppvtext_list:
    - FEATURE: DNAI
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 SMF本端配置共享UPF。

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

### 4 配置共享UPF支持的服务切片信息。

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

### 5 配置共享UPF支持的DNN。

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

### 6 配置共享UPF支持的DNAI信息。

```jinja2
{%- for item in add_pnfdnai_list -%}
    ADD PNFDNAI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DNAI is not none -%}
        DNAI="{{item.DNAI}}",
    {%- endif -%}
    {%- if item.PNFDNNINDEX is not none -%}
        PNFDNNINDEX={{item.PNFDNNINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置共享UPF的属性。

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
    {%- if item.SHAREDUPFSW is not none -%}
        SHAREDUPFSW={{item.SHAREDUPFSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCATION=Central/CentralOnly 时可选 --- -#}
    {%- if item.LOCATION in ['Central', 'CentralOnly'] -%}
        {%- if item.PSACOMBINEULCL is not none -%}
            PSACOMBINEULCL={{item.PSACOMBINEULCL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LOCATION=Central/CentralOnly 时可选 --- -#}
    {%- if item.LOCATION in ['Central', 'CentralOnly'] -%}
        {%- if item.SUPULCLBPONLY is not none -%}
            SUPULCLBPONLY={{item.SUPULCLBPONLY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置虚拟UPF实例标识和DNAI的绑定关系。

#### 8.1 配置虚拟UPF实例。

```jinja2
{%- for item in add_virtualupfid_list -%}
    ADD VIRTUALUPFID:
    {#- --- 必选参数 --- -#}
    UPFINSTANCEID="{{item.UPFINSTANCEID}}",
    VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
    ;
{%- endfor -%}
```

#### 8.2 配置虚拟UPF实例和DNAI的绑定关系。

```jinja2
{%- for item in add_vupfidbinddnai_list -%}
    ADD VUPFIDBINDDNAI:
    {#- --- 必选参数 --- -#}
    VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

### 9 配置共享UPF的服务区域。

#### 9.1 配置用于SMF本端判定共享UPF归属区域的区域类型。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

#### 9.2 配置共享UPF归属区域对应的区域范围。

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

#### 9.3 SMF本端配置共享UPF所覆盖的区域。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 10 **可选：**配置为指定ULCL用户选择特性共享UPF。当ULCL用户从5G网络接入时，如果要求SMF能够为ULCL用户（例如某校园网用户）优选特性的共享UPF避免N9流量过大时，可以执行本步骤。

#### 10.1 配置指定DNAI的UPF信息。

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in add_dnaiupfinfo_list -%}
        ADD DNAIUPFINFO:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in add_dnarea_list -%}
        ADD DNAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in add_dnareabindn2tai_list -%}
        ADD DNAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in add_dnaibinddnarea_list -%}
        ADD DNAIBINDDNAREA:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        AREANAME="{{item.AREANAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 10.2 在APN下开启SMF在分流场景下优先共享UPF开关。设置“SHAREDPRIFLAG”为“ENABLE”。

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in set_apnupselply_list -%}
        SET APNUPSELPLY:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 10.3 配置DNAI粒度的优选共享UPF的开关。如果在2中已经开启APN粒度的优选共享UPF开关，此时本步骤中的“SHAREDPRIFLAG”设置为“INHERIT”即可，如果2中没有设置，需要将本步骤中的“SHAREDPRIFLAG”设置为“ENABLE”。

```jinja2
{%- if is_optional_select_shared_upf_for_ulcl -%}
    {%- for item in add_dnaiupselply_list -%}
        ADD DNAIUPSELPLY:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 配置N4接口下发DNAI信元。

```jinja2
{%- for item in set_pfcppvtext_list -%}
    SET PFCPPVTEXT:
    {#- --- 必选参数 --- -#}
    FEATURE={{item.FEATURE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

