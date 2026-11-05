---
id: ''
name: 激活EPS Fallback
ne_type: UEG
type: feature
description: EPS Fallback（Evolved Packet System Fallback）是指在无线网络没有部署VoNR（Voice over NR，NR网络语音业务）的情况下，当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会通过切换或者重定向的方式回落到4G网络通过VoLTE进行通话。它是VoLTE向VoNR演进的过渡语音方案。  适用于AMF、SMF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","5G网络语音业务","激活EPS Fallback"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
EPS Fallback（Evolved Packet System Fallback）是指在无线网络没有部署VoNR（Voice over NR，NR网络语音业务）的情况下，当UE从5G网络接入时，允许其在IMS域注册，但是当UE要进行通话时，会通过切换或者重定向的方式回落到4G网络通过VoLTE进行通话。它是VoLTE向VoNR演进的过渡语音方案。适用于AMF、SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-025702 EPS Fallback特性概述。
* 已完成加载License。
* 完成N26接口配置，并完成基于N26接口5GC互操作的新建部署。
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
    set_ngimsvops_list:
      type: items
      properties:
        AMFHOMO:
          name: 'AMF是否支持IMS语音'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - UNSPECIFIED
          required: false
          description: '设置VoPS配置'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DCVOPS:
          name: 'Data Centric类型终端支持VoPS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: '设置允许Data Centric终端使用5G语音功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
    set_licenseswitch_list_1:
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
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置IMS网络的APN'
          data_source: '全网规划  -'
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
          description: ''
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        PCSCFIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: LOCAL
    add_pcscfimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        MPCSCFGRPIPV4:
          name: '主IPv4 P-CSCF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
    set_smtimer_list:
      type: items
      properties:
        TEPSFB:
          name: 'EPS Fallback保护定时器时长(秒)'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2EFBAM01'
      SWITCH: ENABLE
    set_ngimsvops_list:
    - AMFHOMO: SUPPORT
      DCVOPS: SUPPORT
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 330
      VALUE: VALUE_1
      POSITION: 2
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2EFBSM01'
      SWITCH: ENABLE
    add_cpapn_list:
    - APN: 'ims'
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
    set_smtimer_list:
    - TEPSFB: 5
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 以下步骤适用于AMF。

### 进入“MML命令行-UEG”窗口。-AMF

### 2 打开AMF该功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置系统支持IMS Voice Over PS服务。

```jinja2
{%- for item in set_ngimsvops_list -%}
    SET NGIMSVOPS:
    {#- --- 可选参数 --- -#}
    {%- if item.AMFHOMO is not none -%}
        AMFHOMO={{item.AMFHOMO}},
    {%- endif -%}
    {%- if item.DCVOPS is not none -%}
        DCVOPS={{item.DCVOPS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置EPS Fallback回落后，TAU过程DOWNLINK NAS TRANSPORT消息携带UE的SRVCC能力。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

### 5 以下步骤适用于SMF。

### 进入“MML命令行-UEG”窗口。-SMF

### 6 打开SMF该功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 7 配置IMS网络APN。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 8 修改APN参数。

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

### 9 添加P-CSCF组配置。

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

### 10 添加P-CSCF地址配置。

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

### 11 增加IMSI和MSISDN号段

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

### 12 添加P-CSCF组和APN的绑定关系，可以整APN绑定，或者按照IMSI/MSISDN号段绑定。

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

### 13 设置EPS Fallback保护定时器时长，该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。

```jinja2
{%- for item in set_smtimer_list -%}
    SET SMTIMER:
    {#- --- 可选参数 --- -#}
    {%- if item.TEPSFB is not none -%}
        TEPSFB={{item.TEPSFB}},
    {%- endif -%}
    ;
{%- endfor -%}
```

