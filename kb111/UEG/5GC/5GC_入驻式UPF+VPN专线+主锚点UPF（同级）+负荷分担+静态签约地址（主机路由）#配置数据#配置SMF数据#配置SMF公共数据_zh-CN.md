---
id: ''
name: 配置SMF公共数据
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中配置**双主锚点UPF负荷分担部署模式**下的的操作过程。  此配置页面中的命令仅在新建UPF时配置。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","业务发放","5GC toB DNN业务发放（专网，入驻式）","通过OMC发放","UEG虚机容器","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（同级）+负荷分担+静态签约地址（主机路由）","配置数据","配置SMF数据","配置SMF公共数据"]
  - ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB DNN业务发放（云网，带计算）","通过OMC发放","DNN发放操作","发放入驻式UPF+VPN专线","入驻式UPF+VPN专线+主锚点UPF（同级）+负荷分担+静态签约地址（主机路由）","配置数据","配置SMF数据","配置SMF公共数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置**双主锚点UPF负荷分担部署模式**下的的操作过程。此配置页面中的命令仅在新建UPF时配置。

## 必备事项
前提条件

以下配置过程是基于SMF和**主锚点UPF**的对接配置已完成情况下的操作。且需要在**主锚点UPF双主负荷分担部署模式**下确保SMF对每个主锚点UPF配置相同的DNN、位置区选择策略，以确保用户会话激活时每个UPF被选择机会均等。
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
          description: 'SMF本端添加负荷分担的两个UPF。'
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
          data_source: '本端规划'
          pattern: ''
          default: Central
        SUPULCLBPONLY:
          name: '是否仅支持作为分流UPF'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPFUNCTION:
          name: 'UPF支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: None
        LOCK:
          name: 'UPF锁'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: FALSE
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '一个UPF只归属于一个VPN。  UPF的“VPNNAME”与**LST CPPOINT**中的查询结果一致。'
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
          description: '配置用户面节点为SMF提供的服务区域。'
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
          description: '配置主锚点UPF双主/多主负荷分担部署模式下的故障保护机制。'
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
    set_deactiverate_list:
      type: items
      properties:
        RATE:
          name: '去活速率'
          type: integer
          minimum: 10
          maximum: 2000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_cpdeactiverate_list:
      type: items
      properties:
        RATE:
          name: '去活速率'
          type: integer
          minimum: 100
          maximum: 5000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upipdomain_list:
      type: items
      properties:
        UPNODE:
          name: 'UPF节点标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置UPF绑定到特定的IP Domain。当该UPF给用户分配的地址时，SMF内部会在此地址前加上该IP Domain前缀，并带给计费模块，用于扩展地址池。 参数“DNN”已在**ADD APN**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPDOMAIN:
          name: 'IP地址段归属的域'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNSWITCH:
          name: 'DNN开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
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
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      SUPULCLBPONLY: Enable
      UPFUNCTION: None
      LOCK: FALSE
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
    set_deactiverate_list:
    - RATE: 1000
    set_cpdeactiverate_list:
    - RATE: 1000
    add_upipdomain_list:
    - UPNODE: 'UPF_Instance_0'
      IPDOMAIN: 'APP-HDNJIHzjSAEGWC1BHW-08AHW011.zj.jih.node.epc.mnc000.mcc460.3gppnetwork.org'
      DNNSWITCH: ENABLE
      DNN: 'APN1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置用户面Profile实例。

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

### 2 配置用户面节点支持的切片与DNN信息。

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

### 3 配置用户面节点的位置特征和分流能力。

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
    {%- if item.LOCK is not none -%}
        LOCK={{item.LOCK}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCATION=Central/CentralOnly 时可选 --- -#}
    {%- if item.LOCATION in ['Central', 'CentralOnly'] -%}
        {%- if item.SUPULCLBPONLY is not none -%}
            SUPULCLBPONLY={{item.SUPULCLBPONLY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置用户面节点的位置区信息，将位置区与TAI绑定。

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

### 5 配置用户面节点支持的为SMF提供服务区域的信息。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 6 配置用户面与EPS的互通以及支持的PDU会话类型。

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

### 7 配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

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

### 8 配置故障场景下对用户会话的去活速率。

#### 8.1 //风筝S

```jinja2
{%- if is_scenario_kite_s -%}
    {%- for item in set_deactiverate_list -%}
        SET DEACTIVERATE:
        {#- --- 必选参数 --- -#}
        RATE={{item.RATE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 //风筝M或风筝L

```jinja2
{%- if is_scenario_kite_m_or_l -%}
    {%- for item in set_cpdeactiverate_list -%}
        SET CPDEACTIVERATE:
        {#- --- 可选参数 --- -#}
        {%- if item.RATE is not none -%}
            RATE={{item.RATE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 （可选）配置UPF绑定到特定的IP Domain，仅当UPF间地址池重叠时需要配置。请确保参数“DNN”已在**ADD APN**中定义。

```jinja2
{%- if is_optional_upf_ipdomain_binding -%}
    {%- for item in add_upipdomain_list -%}
        ADD UPIPDOMAIN:
        {#- --- 必选参数 --- -#}
        UPNODE="{{item.UPNODE}}",
        IPDOMAIN="{{item.IPDOMAIN}}",
        DNNSWITCH={{item.DNNSWITCH}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DNNSWITCH=ENABLE 时必选 --- -#}
        {%- if item.DNNSWITCH == 'ENABLE' -%}
            DNN="{{item.DNN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

