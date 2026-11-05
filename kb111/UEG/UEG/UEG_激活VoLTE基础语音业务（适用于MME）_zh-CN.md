---
id: ''
name: 激活VoLTE基础语音业务（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程，包括开通VoLTE业务和配置VoLTE寻呼重发优化数据。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE基础语音业务（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程，包括开通VoLTE业务和配置VoLTE寻呼重发优化数据。

## 必备事项
前提条件

* 请仔细阅读GWFD-025401 VoLTE基础语音业务特性概述
* 本特性受License控制，请先完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY1:
          name: '优先级1'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
        WEIGHT1:
          name: '权重1'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 127
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
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
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
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
    set_imsvops_list:
      type: items
      properties:
        MMEHOMO:
          name: 'MME侧全部支持PS域IMS语音'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - UNSPECIFIED
          required: false
          description: '配置系统支持VoLTE语音业务。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_s1smproctrl_list:
      type: items
      properties:
        PROT:
          name: '流程类型'
          type: string
          enum:
          - ATTACH_BEARER_ACT_PROC
          - BEARER_DEACT_PROC
          - BEARER_MODIFICATION_PROC
          - BEARER_RESOURCE_ALLOCTION_PROC
          - BEARER_RESOURCE_MOD_PROC
          - DEDICATED_BEARER_ACT_PROC
          - HSS_INIT_SUB_QOS_MOD_PROC
          - PDN_CONNECTIVITY_PROC
          required: true
          description: '当网络中SGW-C/SGW-U/PGW-C/PGW-U支持Create Bearer Request与Modify Bearer Request冲突处理时，配置本命令可以提高语音呼叫建立成功率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CBRCONFLICTMODE:
          name: 'CBR冲突处理模式'
          type: string
          enum:
          - BUFFER
          - DISCARD
          - REJECT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UBRCONFLICTMODE:
          name: 'UBR冲突处理模式'
          type: string
          enum:
          - BUFFER
          - DISCARD
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_emm_list:
      type: items
      properties:
        HPT3413:
          name: '高优先级业务的T3413(s)'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: '配置VoLTE寻呼优化参数。配置后这些参数的优先级会高于**SET EMM**中的普通寻呼参数“T3413(s)”、“N3413(times)”和“重寻呼间隔递增值(s) ”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HPN3413:
          name: '高优先级业务的N3413(times)'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HPPAGINGDELTA:
          name: '高优先级业务的重寻呼间隔递增值(s)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'TOPON.PGW2.4003.SLOT5.MNC001.MCC308.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.16.139.33'
      PRIORITY1: 127
      WEIGHT1: 127
    add_dnsn_list:
    - FQDN: 'IMS.APN.EPC.MNC001.MCC308.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: PGW
      INTYPE: S5
      PRIORITY: 1
      WEIGHT: 1
    set_licenseswitch_list:
    - LICITEM: 'LKV2VOLTE01'
      SWITCH: ENABLE
    set_imsvops_list:
    - MMEHOMO: SUPPORT
    set_s1smproctrl_list:
    - PROT: DEDICATED_BEARER_ACT_PROC
      CBRCONFLICTMODE: BUFFER
      UBRCONFLICTMODE: BUFFER
    set_emm_list:
    - HPT3413: 2
      HPN3413: 4
      HPPAGINGDELTA: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置到PGW-C的解析数据。（如果已配置可跳过）

```jinja2
{%- for item in add_ipv4dnsh_list -%}
    ADD IPV4DNSH:
    {#- --- 必选参数 --- -#}
    HSINDEX={{item.HSINDEX}},
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRSECTION={{item.ADDRSECTION}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4ADDR1 is not none -%}
        IPV4ADDR1="{{item.IPV4ADDR1}}",
    {%- endif -%}
    {%- if item.PRIORITY1 is not none -%}
        PRIORITY1={{item.PRIORITY1}},
    {%- endif -%}
    {%- if item.WEIGHT1 is not none -%}
        WEIGHT1={{item.WEIGHT1}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dnsn_list -%}
    ADD DNSN:
    {#- --- 必选参数 --- -#}
    FQDN="{{item.FQDN}}",
    HSINDEX={{item.HSINDEX}},
    ENTITY={{item.ENTITY}},
    INTYPE={{item.INTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 配置系统支持VoLTE语音业务。

```jinja2
{%- for item in set_imsvops_list -%}
    SET IMSVOPS:
    {#- --- 可选参数 --- -#}
    {%- if item.MMEHOMO is not none -%}
        MMEHOMO={{item.MMEHOMO}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**配置Create Bearer Request与Update Bearer Request的冲突处理模式为“缓存”。

```jinja2
{%- if is_optional_conflict_handling_mode -%}
    {%- for item in set_s1smproctrl_list -%}
        SET S1SMPROCTRL:
        {#- --- 必选参数 --- -#}
        PROT={{item.PROT}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PROT=DEDICATED_BEARER_ACT_PROC 时可选 --- -#}
        {%- if item.PROT == 'DEDICATED_BEARER_ACT_PROC' -%}
            {%- if item.CBRCONFLICTMODE is not none -%}
                CBRCONFLICTMODE={{item.CBRCONFLICTMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PROT=BEARER_MODIFICATION_PROC 时可选 --- -#}
        {%- if item.PROT == 'BEARER_MODIFICATION_PROC' -%}
            {%- if item.UBRCONFLICTMODE is not none -%}
                UBRCONFLICTMODE={{item.UBRCONFLICTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置寻呼优化参数。

```jinja2
{%- for item in set_emm_list -%}
    SET EMM:
    {#- --- 可选参数 --- -#}
    {%- if item.HPT3413 is not none -%}
        HPT3413={{item.HPT3413}},
    {%- endif -%}
    {%- if item.HPN3413 is not none -%}
        HPN3413={{item.HPN3413}},
    {%- endif -%}
    {%- if item.HPPAGINGDELTA is not none -%}
        HPPAGINGDELTA={{item.HPPAGINGDELTA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

