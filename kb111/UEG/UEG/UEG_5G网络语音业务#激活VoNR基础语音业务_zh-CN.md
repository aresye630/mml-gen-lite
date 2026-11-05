---
id: ''
name: 激活VoNR基础语音业务
ne_type: UEG
type: feature
description: VoNR即Voice over NR，UE在NR覆盖下，采用VoNR技术直接在NR上拨打电话，专用QoS Flow也在NR上建立。通话过程中，如果UE移动到LTE网络覆盖下，EPC和5GC会负责把整个IMS DNN平滑到LTE中，并确保给终端分配的IP地址以及P-CSCF的地址不变，使得IMS并不感知。所以只要在NR上发起呼叫，无论通话中终端是否移动到LTE网络，均称为VoNR呼叫。  适用于AMF、SMF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","5G网络语音业务","激活VoNR基础语音业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
VoNR即Voice over NR，UE在NR覆盖下，采用VoNR技术直接在NR上拨打电话，专用QoS Flow也在NR上建立。通话过程中，如果UE移动到LTE网络覆盖下，EPC和5GC会负责把整个IMS DNN平滑到LTE中，并确保给终端分配的IP地址以及P-CSCF的地址不变，使得IMS并不感知。所以只要在NR上发起呼叫，无论通话中终端是否移动到LTE网络，均称为VoNR呼叫。适用于AMF、SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-025701 VoNR基础语音业务特性概述。
* 完成N26接口配置，并完成基于N26接口5GC互操作的新建部署。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngvoicedeploy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          required: true
          description: '指定用户范围'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFHOMO:
          name: 'AMF是否支持IMS语音'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - UNSPECIFIED
          required: false
          description: '指定AMF侧的所有跟踪区是否都支持PS域IMS语音能力'
          data_source: '全网规划'
          pattern: ''
          default: SUPPORT
        DCVOPS:
          name: 'Data Centric类型终端支持'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          required: false
          description: '指定Data Centric类型终端是否都支持IMS语音能力'
          data_source: '全网规划'
          pattern: ''
          default: SUPPORT
        UES1MODE:
          name: '是否检查用户S1Mode能力'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '指定是否检查用户的S1Mode能力'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VOICEDNN:
          name: '语音业务DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '指定语音业务DNN'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: '检查语音DNN是否支持EPS互操作'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '指定系统是否检查语音DNN支持EPS互操作能力'
          data_source: '全网规划'
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
    set_smtimer_list:
      type: items
      properties:
        TEPSFB:
          name: 'EPS Fallback保护定时器时长(秒)'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '设置EPS Fallback保护定时器时长  说明：  5G语音QoS Flow创建触发EPS Fallback流程后启动该定时器，如果定时器超时后，Handover流程/重定（TAU）还未启动，则SMF指示PCF，语音承载创建失败。  该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ngvoicedeploy_list:
    - SUBRANGE: FOREIGN_USER
      AMFHOMO: SUPPORT
      DCVOPS: SUPPORT
      UES1MODE: ON
      VOICEDNN: 'IMS-123'
      IWKEPSIND: ON
    set_ngimsvops_list:
    - AMFHOMO: SUPPORT
      DCVOPS: SUPPORT
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

### 进入“MML命令行-UEG”窗口。

### 2 增加UE使用5G网络接入时的IMS VoPS语音部署策略，可按照用户粒度区分配置不同的语音策略。

```jinja2
{%- for item in add_ngvoicedeploy_list -%}
    ADD NGVOICEDEPLOY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.AMFHOMO is not none -%}
        AMFHOMO={{item.AMFHOMO}},
    {%- endif -%}
    {%- if item.DCVOPS is not none -%}
        DCVOPS={{item.DCVOPS}},
    {%- endif -%}
    {%- if item.UES1MODE is not none -%}
        UES1MODE={{item.UES1MODE}},
    {%- endif -%}
    {%- if item.VOICEDNN is not none -%}
        VOICEDNN="{{item.VOICEDNN}}",
    {%- endif -%}
    {%- if item.IWKEPSIND is not none -%}
        IWKEPSIND={{item.IWKEPSIND}},
    {%- endif -%}
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

### **ADD NGVOICEDEPLOY**与**SET NGIMSVOPS**命令配合控制用户的PS域IMS语音业务策略。

### **ADD NGVOICEDEPLOY**命令优先级高于**SET NGIMSVOPS**。

### 4 以下步骤适用于SMF。

### 进入“MML命令行-UEG”窗口。

### 5 配置IMS网络APN。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 6 修改APN参数。

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

### 7 添加P-CSCF组配置。

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

### 8 添加P-CSCF地址配置。

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

### 9 增加IMSI和MSISDN号段。

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

### 10 添加P-CSCF组和APN的绑定关系，可以整APN绑定，或者按照IMSI/MSISDN号段绑定。

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

### 11 设置EPS Fallback保护定时器时长，该参数配置时应大于基站侧EPS Fallback的保护定时器时长，并小于IMS的AAR定时器时长。

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

