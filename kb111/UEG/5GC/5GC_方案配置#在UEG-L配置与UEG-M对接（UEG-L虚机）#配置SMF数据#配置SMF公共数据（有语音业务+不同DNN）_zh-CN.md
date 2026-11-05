---
id: ''
name: 配置SMF公共数据（有语音业务+不同DNN）
ne_type: UEG
type: feature
description: 当企业部署语音业务时，且所有园区采用不同的DNN接入业务数据，所有园区采用一个DNN接入语音数据，参考本章节进行SMF与UPF对接公共数据配置。此处仅以一套UEG-L的SMF对接一个子园区主备UEG-M为例。新增子园区请参考本章节中对接子园区UPF部分的配置。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+M多园区方案（非跨级容灾）","方案配置","在UEG-L配置与UEG-M对接（UEG-L虚机）","配置SMF数据","配置SMF公共数据（有语音业务+不同DNN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当企业部署语音业务时，且所有园区采用不同的DNN接入业务数据，所有园区采用一个DNN接入语音数据，参考本章节进行SMF与UPF对接公共数据配置。此处仅以一套UEG-L的SMF对接一个子园区主备UEG-M为例。新增子园区请参考本章节中对接子园区UPF部分的配置。

## 必备事项
前提条件

无。
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
          description: 'SMF本端添加UPF。子园区UPF采用主备热备容灾，主备UPF使用一个业务IP对接SMF。'
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
          data_source: '本端规划'
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
          name: 'IPV4地址1'
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
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置UPF的属性。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面支持的服务切片信息。'
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
          description: '配置UPF的DNN属性，用于在用户会话激活时基于用户的DNN选择UPF。各园区推荐共DNN，如果各园区采用不同DNN，则不支持用户跨园区访问。'
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
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '新增5G 位置区，与ADD PNFSMFSERAREA中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
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
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '设置5G位置区范围，已通过命令ADD UPAREA配置。其中TAI由PLMN和TAC组成。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务区名称支持的5GTAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5GTAI范围的结束值'
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
          description: 'SMF本端配置UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UPF。'
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
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.125.11'
      PORT: 8080
    - NFINSTANCEID: 'UPF_Instance_A0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upfa00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    - NFINSTANCENAME: 'UPF_Instance_A0'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      ADDRALLOCMODE: INHERIT
      VPNNAME: 'VRF_PS_N4'
    add_pnfns_list:
    - INDEX: 2
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '010101'
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_A0'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 5
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'data.APN1'
      PNFNSINDEX: 2
    - INDEX: 6
      NFINSTANCEID: 'UPF_Instance_A0'
      DNN: 'data.APN2'
      PNFNSINDEX: 3
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    - AREANAME: 'UPAREA2'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12301000001'
      N2ENDTAI: '12301000002'
    - AREANAME: 'UPAREA2'
      N2BEGINTAI: '12301000003'
      N2ENDTAI: '12301000004'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    - NFINSTANCEID: 'UPF_Instance_A0'
      SMFSERVINGAREA: 'UPAREA2'
    add_pnfupfinfo_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
    - NFINSTANCEID: 'UPF_Instance_A0'
      IWKEPSIND: TRUE
      PDUSESSIONTYPE: IPV4-1&IPV6-1&IPV4V6-1&UNSTRUCTURED-1&ETHERNET-1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置用户面节点实例。配置Profile实例。

#### 1.1 //对接总部园区UPF配置

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

### 2 配置用户面节点的位置特征和分流能力。

#### 2.1 //对接总部园区UPF配置

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
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置用户面节点支持的切片与DNN信息。

#### 3.1 //对接总部园区UPF配置

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

### 4 配置5G用户面节点的位置区信息，将位置区与TAI绑定。

#### 4.1 //对接总部园区UPF配置

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

### 5 配置5G用户面节点支持的为SMF提供服务区域的信息。

#### 5.1 //对接总部园区UPF配置

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

#### 6.1 //对接总部园区UPF配置

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

