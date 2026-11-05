---
id: ''
name: 配置SMF公共数据
ne_type: UEG
type: feature
description: 本操作用于指导在两个**分流UPF**间采用负荷分担的容灾组网模式下的配置过程，假定**两个分流UPF**的实例标识分别为UPF_Instance_0，UPF_Instance_1。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（同级）+负荷分担+动态分配地址","配置数据","配置SMF数据","配置SMF公共数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+分流UPF（同级）+负荷分担+动态分配地址","配置数据","配置SMF数据","配置SMF公共数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作用于指导在两个**分流UPF**间采用负荷分担的容灾组网模式下的配置过程，假定**两个分流UPF**的实例标识分别为UPF_Instance_0，UPF_Instance_1。

## 必备事项
前提条件

无
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
          description: '添加**分流UPF**实例信息。'
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
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置UPF支持的服务切片信息，负荷分担的两个UPF需要配置相同的切片属性。'
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
          description: '配置用户面节点支持的DNN及其归属切片的信息，负荷分担的两个UPF需要配置相同的DNN及其归属切片信息。'
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
    add_pnfdnai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '添加**分流UPF**的DNAI信息**。**'
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
        PRISWITCH:
          name: '优先级配置功能'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
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
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过命令**ADD PNFPROFILE**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特性'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: None
        APSAMIGFUNC:
          name: '辅锚点UPF故障迁移功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '一个UPF只归属于一个VPN。 UPF的“VPNNAME”与**LST CPPOINT**中的查询结果一致。'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: '位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'ARE类型'
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
          name: 'UP位置区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过命令**ADD UPAREA**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
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
          description: '添加**分流UPF**所服务的位置区域信息。'
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
    set_pfcppara_list:
      type: items
      properties:
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: '配置负荷分担部署模式下的故障保护机制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HBT1:
          name: '心跳消息超时间隔(秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBN1:
          name: '心跳消息发送次数阈值'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEACTIVEFLAG:
          name: '去活用户开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DACTINTERVAL:
          name: '去活间隔(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upfaultoperpara_list:
      type: items
      properties:
        UPMIGRATE:
          name: '故障迁移速率（个/秒）'
          type: integer
          minimum: 100
          maximum: 5000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        IPV6LOCALUP:
          name: 'IPv6本地UP分流策略'
          type: string
          enum:
          - BpPrefer
          - UlClPrefer
          required: false
          description: '配置IPv6会话场景下的分流策略。  如果是IPv6会话，系统默认选择Bp分流模式，如果是UL CL分流需要修改配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
    add_pnfns_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '000001'
    add_pnfdnn_list:
    - INDEX: 5
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'APN1'
      PNFNSINDEX: 3
    add_pnfdnai_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      DNAI: 'testdnai'
      PNFDNNINDEX: 3
      PRISWITCH: SPECIFIC
      PRIORITY: 1
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: UlClAndBp
      APSAMIGFUNC: ENABLE
      VPNNAME: 'VRF_CP'
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12301000001'
      N2ENDTAI: '12301123456'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    add_pnfupfinfo_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
    set_pfcppara_list:
    - HBINTERVAL: 30
      HBT1: 3
      HBN1: 5
      DEACTIVEFLAG: ENABLE
      DACTINTERVAL: 900
    set_upfaultoperpara_list:
    - UPMIGRATE: 1000
    set_smffunc_list:
    - IPV6LOCALUP: UlClPrefer
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //配置用户面Profile实例。

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

### 2 //配置用户面节点支持的切片与DNN信息。

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

```jinja2
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
```

### 3 //为UL CL UPF添加DNAI信息**。**

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
    {%- if item.PRISWITCH is not none -%}
        PRISWITCH={{item.PRISWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
    {%- if item.PRISWITCH == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置用户面节点的位置特征和分流能力。

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
    {%- if item.APSAMIGFUNC is not none -%}
        APSAMIGFUNC={{item.APSAMIGFUNC}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //配置用户面节点的位置区信息，将位置区与TAI绑定。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

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

### 6 //配置用户面节点支持的为SMF提供服务区域的信息。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 7 //配置用户面与EPS的互通以及支持的PDU会话类型。

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

### 8 //配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

```jinja2
{%- for item in set_pfcppara_list -%}
    SET PFCPPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.HBT1 is not none -%}
        HBT1={{item.HBT1}},
    {%- endif -%}
    {%- if item.HBN1 is not none -%}
        HBN1={{item.HBN1}},
    {%- endif -%}
    {%- if item.DEACTIVEFLAG is not none -%}
        DEACTIVEFLAG={{item.DEACTIVEFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEACTIVEFLAG=ENABLE 时可选 --- -#}
    {%- if item.DEACTIVEFLAG == 'ENABLE' -%}
        {%- if item.DACTINTERVAL is not none -%}
            DACTINTERVAL={{item.DACTINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 //配置故障场景下对用户会话的去活速率。

```jinja2
{%- for item in set_upfaultoperpara_list -%}
    SET UPFAULTOPERPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.UPMIGRATE is not none -%}
        UPMIGRATE={{item.UPMIGRATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 //配置IPv6会话场景下的分流策略。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.IPV6LOCALUP is not none -%}
        IPV6LOCALUP={{item.IPV6LOCALUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

