---
id: ''
name: 配置“园区内UPF和园区外UPF冗余模式”
ne_type: UEG
type: feature
description: 本操作指导介绍“园区内UPF和园区外UPF冗余模式”容灾组网配置的操作过程。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UNC特性指南","WSFD-108004 MEC冗余模式故障保护","配置“园区内UPF和园区外UPF冗余模式”"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍“园区内UPF和园区外UPF冗余模式”容灾组网配置的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-108004 MEC冗余模式故障保护特性原理概述。
* 已完成加载license。
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
          description: '**SMF本端添加UL CL UPF**。'
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
    add_virtualupfid_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '**配置虚拟UPF实例标识**。'
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
          description: '**配置虚拟UPF实例标识的DNAI。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
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
          description: '**配置用户面支持的服务切片信息**。'
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
          description: '**配置UL CL UPF的DNN属性，用于在用户会话激活时基于用户的DNN选择UL CL UPF。**'
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
          description: '**为UL CL UPF添加DNAI信息。**'
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
          description: '**配置UL CL UPF的属性。**'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        APSAMIGFUNC:
          name: '辅锚点UPF故障迁移功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '**配置用于SMF本端判定UL CL UPF归属区域的区域类型，如TA类型。**'
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
          description: '**为UPAREA1添加区域范围。**'
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
          description: '**SMF本端配置UL CL UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UL CL UPF。**'
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
    set_pfcppara_list:
      type: items
      properties:
        HBINTERVAL:
          name: '心跳间隔(秒)'
          type: integer
          minimum: 15
          maximum: 300
          required: false
          description: '**配置UPF****故障场景下的保护机制**。'
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
        MIGINTERVAL:
          name: '迁移间隔（秒）'
          type: integer
          minimum: 0
          maximum: 300
          required: false
          description: ''
          data_source: '全网规划'
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
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
    add_virtualupfid_list:
    - UPFINSTANCEID: 'UPF_Instance_0'
      VUPFINSTANCEID: 'UPF_Instance_0_v1'
    add_vupfidbinddnai_list:
    - VUPFINSTANCEID: 'UPF_Instance_0_v1'
      DNAI: 'testdnai1'
    add_pnfns_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '000001'
    add_pnfdnn_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'Huawei1.com'
    add_pnfdnai_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      DNAI: 'testdnai'
      PNFDNNINDEX: 3
      PRISWITCH: SPECIFIC
      PRIORITY: 2
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Central
      UPFUNCTION: UlClAndBp
      SHAREDUPFSW: ENABLE
      APSAMIGFUNC: ENABLE
    add_uparea_list:
    - AREANAME: 'UPAREA0'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA0'
      N2BEGINTAI: '12303260000'
      N2ENDTAI: '12303261111'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA0'
    set_pfcppara_list:
    - HBINTERVAL: 30
      HBT1: 3
      HBN1: 5
      MIGINTERVAL: 60
    set_upfaultoperpara_list:
    - UPMIGRATE: 1000
    set_licenseswitch_list:
    - LICITEM: 'LKV2DMECFP01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 //**SMF本端添加UPF**。

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

### 2 //**配置园区外UPF辅锚点的虚拟DNAI**。

```jinja2
{%- for item in add_virtualupfid_list -%}
    ADD VIRTUALUPFID:
    {#- --- 必选参数 --- -#}
    UPFINSTANCEID="{{item.UPFINSTANCEID}}",
    VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vupfidbinddnai_list -%}
    ADD VUPFIDBINDDNAI:
    {#- --- 必选参数 --- -#}
    VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
    DNAI="{{item.DNAI}}",
    ;
{%- endfor -%}
```

### 3 //**配置用户面支持的服务切片信息**。

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

### 4 //**配置UPF的DNN属性**。

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

### 5 //**为UL CL UPF添加DNAI信息。**

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

### 6 //**配置UPF的属性。**

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
    {%- if item.APSAMIGFUNC is not none -%}
        APSAMIGFUNC={{item.APSAMIGFUNC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 //**配置用于SMF本端判定UPF归属区域的区域类型**。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

### 8 //**配置UL CL UPF归属区域对应的区域范围。**

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

### 9 //**SMF本端配置UPF所覆盖的区域**。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

### 10 **//配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。**

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
    {%- if item.MIGINTERVAL is not none -%}
        MIGINTERVAL={{item.MIGINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 **//配置故障场景下批量迁移故障UPF上用户会话的速率**。

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

### 12 **//打开本功能的License配置开关。**

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

