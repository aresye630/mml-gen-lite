---
id: GWFD-025501
name: 激活P-CSCF故障时IMS业务恢复
ne_type: UEG
type: feature
description: 本操作指导介绍激活P-CSCF故障时IMS业务恢复功能，降低P-CSCF服务器故障时对用户业务的影响。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-025500 VoLTE业务快速恢复","GWFD-025501 P-CSCF故障时IMS业务恢复","激活P-CSCF故障时IMS业务恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍激活P-CSCF故障时IMS业务恢复功能，降低P-CSCF服务器故障时对用户业务的影响。适用于PGW-C、SMF

## 必备事项
前提条件

前提条件

* 已阅读GWFD-025501 P-CSCF故障时IMS业务恢复特性概述。
* 完成激活VoLTE基础语音业务（适用于SGW-C/PGW-C）。
* 完成激活PCC基本功能。
* 已确认周边网元支持P-CSCF故障恢复的处理。
* UEG上已完成IP FARM管理相关配置。
* 已完成加载License。
* 已完成IMS配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_cpapnimsattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置APN的IMS属性'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSSWITCH:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcscfgroup_list:
      type: items
      properties:
        GROUPNAME:
          name: 'P-CSCF组名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '添加P-CSCF组'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        ALLOCTYPE:
          name: 'P-CSCF获取方式'
          type: string
          enum:
          - LOCAL
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
    add_pcscfip_list:
      type: items
      properties:
        GROUPNAME:
          name: 'P-CSCF组名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '添加P-CSCF地址'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCSCFIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 1
        ALLOCTYPE:
          name: 'P-CSCF获取方式'
          type: string
          enum:
          - LOCAL
          - DHCP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
        PAIRID:
          name: '结对ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcscfimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN号码段'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - MSISDN
          - IMSIWILDCARD
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pcscfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '在APN下将某指定号段绑定到P-CSCF组。也可以将整个APN绑定到P-CSCF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MPCSCFGRPIPV4:
          name: '主IPv4P-CSCF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pnfntfplcy_list:
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
          description: '配置通知对端NF状态变化的抑制时间。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NTFTIME:
          name: '通知抑制时间(分钟)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: 'SMF形态基于UPF和PCF的PCSCF故障恢复，按照协议根据UE能力0012H(P-CSCF Re-selection support)选择是否重新激活会话。如果UE支持P-CSCF地址更新则发更新消息给UE，不重新激活会话；否则删除会话后UE重新接入激活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9IMSR11'
      SWITCH: ENABLE
    set_cpapnimsattr_list:
    - APN: 'ims'
      IMSSWITCH: ENABLE
    add_pcscfgroup_list:
    - GROUPNAME: 'vonr'
      IPVERSION: IPV4
      ALLOCTYPE: LOCAL
    add_pcscfip_list:
    - GROUPNAME: 'vonr'
      IPVERSION: IPV4
      PCSCFIPV4: '10.28.236.11'
      WEIGHT: 10
      ALLOCTYPE: LOCAL
      PAIRID: 1
    add_pcscfimsisdnseg_list:
    - SEGMENTNAME: 'vonr'
      SEGMENTTYPE: IMSI
      SEGSTART: '123031200100026'
      SEGEND: '123031200100027'
    add_pcscfgrpbndapn_list:
    - APN: 'ims'
      DEFAULTFLAG: DEFAULT
      MPCSCFGRPIPV4: 'vonr'
      IMSIMSISDNSEG: 'vonr'
      PRIORITY: 1
    set_pnfntfplcy_list:
    - NFTYPE: NfPCSCF
      NTFTIME: 1
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1017
      VALUE: VALUE_1
      POSITION: 29
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开该功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 修改APN参数。

```jinja2
{%- for item in set_cpapnimsattr_list -%}
    SET CPAPNIMSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IMSSWITCH is not none -%}
        IMSSWITCH={{item.IMSSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 添加P-CSCF组配置。

```jinja2
{%- for item in add_pcscfgroup_list -%}
    ADD PCSCFGROUP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {%- if item.ALLOCTYPE is not none -%}
        ALLOCTYPE={{item.ALLOCTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 添加P-CSCF地址配置。

```jinja2
{%- for item in add_pcscfip_list -%}
    ADD PCSCFIP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.ALLOCTYPE is not none -%}
        ALLOCTYPE={{item.ALLOCTYPE}},
    {%- endif -%}
    {%- if item.PAIRID is not none -%}
        PAIRID={{item.PAIRID}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PCSCFIPV4="{{item.PCSCFIPV4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ALLOCTYPE=LOCAL 时可选 --- -#}
    {%- if item.ALLOCTYPE == 'LOCAL' -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加IMSI和MSIDSN号段

```jinja2
{%- for item in add_pcscfimsisdnseg_list -%}
    ADD PCSCFIMSISDNSEG:
    {#- --- 必选参数 --- -#}
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGSTART="{{item.SEGSTART}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGEND="{{item.SEGEND}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 添加P-CSCF组和APN的绑定关系，可以整APN绑定，或者按照IMSI/MSISDN号段绑定。

```jinja2
{%- for item in add_pcscfgrpbndapn_list -%}
    ADD PCSCFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    {#- --- 可选参数 --- -#}
    {%- if item.MPCSCFGRPIPV4 is not none -%}
        MPCSCFGRPIPV4="{{item.MPCSCFGRPIPV4}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
    {%- endif -%}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置通知对端NF状态变化的抑制时间。

```jinja2
{%- for item in set_pnfntfplcy_list -%}
    SET PNFNTFPLCY:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NTFTIME={{item.NTFTIME}},
    ;
{%- endfor -%}
```

### 9 配置软参。将软参DWORD1017 BIT29、DWORD1017 BIT30取值设置为1。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

