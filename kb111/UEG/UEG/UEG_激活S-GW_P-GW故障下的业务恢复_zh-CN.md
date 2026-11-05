---
id: GWFD-025503
name: 激活S-GW/P-GW故障下的业务恢复
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活S-GW/P-GW故障下的业务恢复的操作过程。  在S-GW/P-GW故障或重启场景下，MME能感知网关故障，协助用户及时恢复VoLTE语音业务，实现网关设备的容灾功能。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-025500 VoLTE业务快速恢复","GWFD-025503 S-GW/P-GW故障下的业务恢复","激活S-GW/P-GW故障下的业务恢复"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST GTPPUB')
- getParameterValue('LST GTPCAUSE')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活S-GW/P-GW故障下的业务恢复的操作过程。在S-GW/P-GW故障或重启场景下，MME能感知网关故障，协助用户及时恢复VoLTE语音业务，实现网关设备的容灾功能。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025503 S-GW/P-GW故障下的业务恢复特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_gwoffloadpara_list:
      type: items
      properties:
        DELAYTIMER:
          name: '批量迁移延迟时长'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: '配置本特性批量业务恢复功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RATE:
          name: '批量迁移速率'
          type: integer
          minimum: 0
          maximum: 500
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ITFOFFLOADSW:
          name: '接口故障迁移开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gwrestorapn_list:
      type: items
      properties:
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcv2cmpt_list:
      type: items
      properties:
        IDX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置S-GW网元故障重选特性相关信元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSGCLS:
          name: '消息分类'
          type: string
          enum:
          - MM
          - PM
          - SV
          - TM
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CTX_RSP
          - FWD_RLC_REQ
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTXRSP:
          name: 'Context Response的信元类型'
          type: string
          enum:
          - INDICATION
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTXRSPIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gtppub_list:
      type: items
      properties:
        DNSGTPCPATHFILTERSW:
          name: '过滤故障状态的GTPC路径开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '查询过滤故障状态的GTP-C路径开关是否已经打开。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V2EI:
          name: '发送GTPv2 Echo请求间隔(s)'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_sgwcharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - SPECIFIED
          required: true
          description: '配置MME与S-GW间PRN功能以及MME ID传递功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MSK:
          name: 'IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRN:
          name: 'S-GW支持PRN功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: NO
        MMEID:
          name: 'S-GW支持MME ID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_pgwcharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL
          - FOREIGN
          - HOME
          - SPECIFIC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcause_list:
      type: items
      properties:
        GTPVERSION:
          name: 'GTP版本'
          type: string
          enum:
          - GTPV0V1
          - GTPV2
          required: true
          description: '配置特定原因失败重选P-GW功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REJCAUSE:
          name: '拒绝原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_sgwcharact_list_1:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - SPECIFIED
          required: true
          description: '配置MME与S-GW间PRN功能以及MME ID传递功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MSK:
          name: 'IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRN:
          name: 'S-GW支持PRN功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: NO
        MMEID:
          name: 'S-GW支持MME ID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_gtpcv2cmpt_list_1:
      type: items
      properties:
        IDX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置S-GW网元故障重选特性相关信元。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSGCLS:
          name: '消息分类'
          type: string
          enum:
          - MM
          - PM
          - SV
          - TM
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CTX_RSP
          - FWD_RLC_REQ
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTXRSP:
          name: 'Context Response的信元类型'
          type: string
          enum:
          - INDICATION
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTXRSPIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gtppub_list_1:
      type: items
      properties:
        DNSGTPCPATHFILTERSW:
          name: '过滤故障状态的GTPC路径开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '查询过滤故障状态的GTP-C路径开关是否已经打开。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V2EI:
          name: '发送GTPv2 Echo请求间隔(s)'
          type: integer
          minimum: 60
          maximum: 3600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gtpcause_list_1:
      type: items
      properties:
        GTPVERSION:
          name: 'GTP版本'
          type: string
          enum:
          - GTPV0V1
          - GTPV2
          required: true
          description: '配置特定原因失败重选P-GW功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REJCAUSE:
          name: '拒绝原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_sgwcharact_list_2:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - SPECIFIED
          required: true
          description: '配置MME与S-GW间PRN功能以及MME ID传递功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MSK:
          name: 'IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRN:
          name: 'S-GW支持PRN功能'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: NO
        MMEID:
          name: 'S-GW支持MME ID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_pgwcharact_list_1:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL
          - FOREIGN
          - HOME
          - SPECIFIC
          required: true
          description: ''
          data_source: ''
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
          description: '打开本特性的License配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_gwoffloadpara_list:
    - DELAYTIMER: 3
      RATE: 200
      ITFOFFLOADSW: ON
    add_gwrestorapn_list:
    - APNNI: ''
    add_gtpcv2cmpt_list:
    - IDX: 0
      MSGCLS: MM
      MMMSGTYPE: CTX_RSP
      CTXRSP: INDICATION
      CTXRSPIND: SRNI-1
    set_gtppub_list:
    - DNSGTPCPATHFILTERSW: ON
      V2EI: 60
    add_sgwcharact_list:
    - RANGE: SPECIFIED
      IPT: IPV4
      IPV4: 'IPV4地址'
      IPV4MSK: '255.255.255.255'
      PRN: YES
      MMEID: YES
    add_pgwcharact_list:
    - RANGE: ''
    add_gtpcause_list:
    - GTPVERSION: GTPV2
      REJCAUSE: 100
    add_sgwcharact_list_1:
    - RANGE: SPECIFIED
      IPT: IPV4
      IPV4: 'IPV4地址'
      IPV4MSK: '255.255.255.255'
      PRN: YES
      MMEID: YES
    add_gtpcv2cmpt_list_1:
    - IDX: 0
      MSGCLS: MM
      MMMSGTYPE: CTX_RSP
      CTXRSP: INDICATION
      CTXRSPIND: SRNI-1
    set_gtppub_list_1:
    - DNSGTPCPATHFILTERSW: ON
      V2EI: 60
    add_gtpcause_list_1:
    - GTPVERSION: GTPV2
      REJCAUSE: 100
    add_sgwcharact_list_2:
    - RANGE: SPECIFIED
      IPT: IPV4
      IPV4: 'IPV4地址'
      IPV4MSK: '255.255.255.255'
      PRN: YES
      MMEID: YES
    add_pgwcharact_list_1:
    - RANGE: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2SRGF01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置本特性批量业务恢复功能。

### 批量业务恢复会造成网元间的信令增加，可能导致网络拥塞。运营商需根据网络中VoLTE用户数量以及周边网元能力等因素，通过配置以下3个参数来避免在批量业务恢复过程中导致网络拥塞。

```jinja2
{%- for item in set_gwoffloadpara_list -%}
    SET GWOFFLOADPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.DELAYTIMER is not none -%}
        DELAYTIMER={{item.DELAYTIMER}},
    {%- endif -%}
    {%- if item.RATE is not none -%}
        RATE={{item.RATE}},
    {%- endif -%}
    {%- if item.ITFOFFLOADSW is not none -%}
        ITFOFFLOADSW={{item.ITFOFFLOADSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**配置容灾APN特征参数。

```jinja2
{%- if is_optional_disaster_recovery_apn_params -%}
    {%- for item in add_gwrestorapn_list -%}
        ADD GWRESTORAPN:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当需要为IMS和紧急呼叫之外的其他APN提供容灾备份功能时，需要执行本命令。

### 此APN为支持容灾备份的APN，必须和UEG系统中配置的一致。否则可能导致主被叫业务无法一次恢复。

### UEG默认支持IMS和紧急呼叫业务的恢复，无需对这两种业务额外配置APN。

### 4 配置S-GW/P-GW故障场景下的业务恢复功能，运营商可根据实际需求进行如下配置。

#### 4.1 MME向S-GW发送Echo消息的间隔周期可通过配置参数“V2EI”(**SET GTPPUB**)来调整。为缩短VoLTE业务恢复时长，建议将UEG以及对端S-GW上的该参数值同时配置为“60s”。

#### 4.2 UEG上T3N3定时器的定时时长(T3RES\*N3REQ)(通过命令**SET T3N3**配置)需大于对端S-GW上该定时器的定时时长，否则当P-GW故障时，可能导致重选流程失败。

#### 4.3 配置仅针对S-GW故障场景下的业务恢复功能。

##### 4.3.1 配置Inter TAU过程中旧侧MME携带SGW Restoration Needed Indication至新侧MME功能。

```jinja2
{%- if is_scenario_sgw_fault -%}
    {%- for item in add_gtpcv2cmpt_list -%}
        ADD GTPCV2CMPT:
        {#- --- 必选参数 --- -#}
        IDX={{item.IDX}},
        MSGCLS={{item.MSGCLS}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MSGCLS=MM 时必选 --- -#}
        {%- if item.MSGCLS == 'MM' -%}
            MMMSGTYPE={{item.MMMSGTYPE}},
        {%- endif -%}
        {#- --- 条件必选：MMMSGTYPE=CTX_RSP 时必选 --- -#}
        {%- if item.MMMSGTYPE == 'CTX_RSP' -%}
            CTXRSP={{item.CTXRSP}},
        {%- endif -%}
        {#- --- 条件必选：CTXRSP=INDICATION 时必选 --- -#}
        {%- if item.CTXRSP == 'INDICATION' -%}
            CTXRSPIND={{item.CTXRSPIND}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.2 查询过滤故障状态的GTP-C路径开关是否已经打开。

###### 4.3.2.1 是，执行4.d。

###### 4.3.2.2 否，执行4.c。

##### 4.3.3 打开过滤故障状态的GTP-C路径开关。

```jinja2
{%- set LST_GTPPUB=getParameterValue('LST GTPPUB') -%}
{%- if is_scenario_sgw_fault and not LST_GTPPUB -%}
    {%- for item in set_gtppub_list -%}
        SET GTPPUB:
        {#- --- 可选参数 --- -#}
        {%- if item.DNSGTPCPATHFILTERSW is not none -%}
            DNSGTPCPATHFILTERSW={{item.DNSGTPCPATHFILTERSW}},
        {%- endif -%}
        {%- if item.V2EI is not none -%}
            V2EI={{item.V2EI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.4 配置本特性MME ID传递功能。

```jinja2
{%- if is_scenario_sgw_fault -%}
    {%- for item in add_sgwcharact_list -%}
        ADD SGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRN is not none -%}
            PRN={{item.PRN}},
        {%- endif -%}
        {%- if item.MMEID is not none -%}
            MMEID={{item.MMEID}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIFIED 时必选 --- -#}
        {%- if item.RANGE == 'SPECIFIED' -%}
            IPT={{item.IPT}},
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4MSK="{{item.IPV4MSK}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sgw_fault and is_scenario_separate_deployment -%}
    {%- for item in add_pgwcharact_list -%}
        ADD PGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 4.3.4.1 如果S-GW和P-GW合一部署，则本步骤仅需执行**ADD SGWCHARACT**命令即可。

###### 4.3.4.2 如果S-GW和P-GW非合一，则本步骤需要执行**ADD SGWCHARACT**和**ADD PGWCHARACT**两个命令。

#### 4.4 配置仅针对P-GW故障场景下的业务恢复功能。

##### 4.4.1 查询GTP原因值“REJCAUSE”是否为“100”。

###### 4.4.1.1 是，执行4.c。

###### 4.4.1.2 否，执行4.b。

##### 4.4.2 配置特定原因失败重选P-GW功能。

```jinja2
{%- set LST_GTPCAUSE=getParameterValue('LST GTPCAUSE') -%}
{%- if is_scenario_pgw_fault and not LST_GTPCAUSE -%}
    {%- for item in add_gtpcause_list -%}
        ADD GTPCAUSE:
        {#- --- 必选参数 --- -#}
        GTPVERSION={{item.GTPVERSION}},
        REJCAUSE={{item.REJCAUSE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.4.3 配置本特性MME与S-GW间PRN功能。

```jinja2
{%- if is_scenario_pgw_fault -%}
    {%- for item in add_sgwcharact_list_1 -%}
        ADD SGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRN is not none -%}
            PRN={{item.PRN}},
        {%- endif -%}
        {%- if item.MMEID is not none -%}
            MMEID={{item.MMEID}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIFIED 时必选 --- -#}
        {%- if item.RANGE == 'SPECIFIED' -%}
            IPT={{item.IPT}},
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4MSK="{{item.IPV4MSK}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置同时针对S-GW、P-GW故障场景下的业务恢复功能。

##### 4.5.1 配置Inter TAU过程中旧侧MME携带SGW Restoration Needed Indication至新侧MME功能。

```jinja2
{%- if is_scenario_sgw_pgw_fault -%}
    {%- for item in add_gtpcv2cmpt_list_1 -%}
        ADD GTPCV2CMPT:
        {#- --- 必选参数 --- -#}
        IDX={{item.IDX}},
        MSGCLS={{item.MSGCLS}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MSGCLS=MM 时必选 --- -#}
        {%- if item.MSGCLS == 'MM' -%}
            MMMSGTYPE={{item.MMMSGTYPE}},
        {%- endif -%}
        {#- --- 条件必选：MMMSGTYPE=CTX_RSP 时必选 --- -#}
        {%- if item.MMMSGTYPE == 'CTX_RSP' -%}
            CTXRSP={{item.CTXRSP}},
        {%- endif -%}
        {#- --- 条件必选：CTXRSP=INDICATION 时必选 --- -#}
        {%- if item.CTXRSP == 'INDICATION' -%}
            CTXRSPIND={{item.CTXRSPIND}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.5.2 查询过滤故障状态的GTP-C路径开关是否已经打开。

###### 4.5.2.1 是，执行4.f。

###### 4.5.2.2 否，执行4.e。

##### 4.5.3 打开过滤故障状态的GTP-C路径开关。

```jinja2
{%- if is_scenario_sgw_pgw_fault and not LST_GTPPUB -%}
    {%- for item in set_gtppub_list_1 -%}
        SET GTPPUB:
        {#- --- 可选参数 --- -#}
        {%- if item.DNSGTPCPATHFILTERSW is not none -%}
            DNSGTPCPATHFILTERSW={{item.DNSGTPCPATHFILTERSW}},
        {%- endif -%}
        {%- if item.V2EI is not none -%}
            V2EI={{item.V2EI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.5.4 查询GTP原因值“REJCAUSE”是否为“100”。

###### 4.5.4.1 是，执行4.f。

###### 4.5.4.2 否，执行4.e。

##### 4.5.5 配置特定原因失败重选P-GW功能。

```jinja2
{%- if is_scenario_sgw_pgw_fault and not LST_GTPCAUSE -%}
    {%- for item in add_gtpcause_list_1 -%}
        ADD GTPCAUSE:
        {#- --- 必选参数 --- -#}
        GTPVERSION={{item.GTPVERSION}},
        REJCAUSE={{item.REJCAUSE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.5.6 配置本特性MME与S-GW间PRN功能以及MME ID传递功能。

```jinja2
{%- if is_scenario_sgw_pgw_fault -%}
    {%- for item in add_sgwcharact_list_2 -%}
        ADD SGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRN is not none -%}
            PRN={{item.PRN}},
        {%- endif -%}
        {%- if item.MMEID is not none -%}
            MMEID={{item.MMEID}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RANGE=SPECIFIED 时必选 --- -#}
        {%- if item.RANGE == 'SPECIFIED' -%}
            IPT={{item.IPT}},
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4="{{item.IPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4MSK="{{item.IPV4MSK}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_sgw_pgw_fault and is_scenario_separate_deployment -%}
    {%- for item in add_pgwcharact_list_1 -%}
        ADD PGWCHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 4.5.6.1 如果S-GW和P-GW合一部署，则本步骤仅需执行**ADD SGWCHARACT**命令即可。

###### 4.5.6.2 如果S-GW和P-GW非合一，则本步骤需要执行**ADD SGWCHARACT**和**ADD PGWCHARACT**两个命令。

### 5 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

