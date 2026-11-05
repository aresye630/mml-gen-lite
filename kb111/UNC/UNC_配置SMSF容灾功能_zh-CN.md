---
id: ''
name: 配置SMSF容灾功能
ne_type: UNC
type: feature
description: 本操作指导介绍部署SMSF 1+1互备组网的操作过程。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core SMSF解决方案","SMSF功能部署","部署容灾网络","配置SMSF容灾功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍部署SMSF 1+1互备组网的操作过程。

## 必备事项
前提条件

* 请仔细阅读WSFD-130011 SMSF双活容灾特性概述。
* 已完成SMSF初始配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_commonsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - DwCom
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDCOMNUM:
          name: 'Common Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
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
    add_m3le_list:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        STPF:
          name: '信令转接点功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        NMD:
          name: '网络模式'
          type: string
          enum:
          - EXCLUSIVE
          - INCLUSIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EXCLUSIVE
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
  examples:
    set_commonsoftparaofbit_list:
    - DT: DwCom
      DWORDCOMNUM: 16
      VALUE: VALUE_1
      POSITION: 3
    add_pnfprofile_list:
    - NFINSTANCEID: 'SMSF_Instance_0'
      NFTYPE: NfSMSF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.2.180.15'
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
    add_m3le_list:
    - LEX: 1
      NI: NAT
      OPC: '0X017701'
      LET: ASP
      LEN: 'SMSC'
    add_m3de_list:
    - DEX: 1
      LEX: 1
      DPC: '0x240011'
      SLSSM: B0000
      STPF: DISABLE
      DET: SGP
      ADJF: TRUE
      NMD: EXCLUSIVE
      PVER: RFC3332
      DEN: 'SMSC'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置SMSF数据

#### 1.1 打开SMSF和UDM数据一致性检查功能。

```jinja2
{%- for item in set_commonsoftparaofbit_list -%}
    SET COMMONSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=DwCom 时必选 --- -#}
    {%- if item.DT == 'DwCom' -%}
        DWORDCOMNUM={{item.DWORDCOMNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置AMF数据

#### 2.1 配置AMF到SMSF的对接数据。

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

### 3 配置SMSC/STP数据

#### 3.1 配置SMSC/STP到SMSF的对接数据。

```jinja2
{%- for item in add_m3le_list -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_m3de_list -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DEX={{item.DEX}},
    LEX={{item.LEX}},
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.NMD is not none -%}
        NMD={{item.NMD}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

