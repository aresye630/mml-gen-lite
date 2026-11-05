---
id: ''
name: 激活本地PDU会话重建特性
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活本地PDU会话重建操作过程。AMF和SMF上分别实现了本地PDU会话重建功能，AMF和SMF上完成一种配置即可实现此特性的激活任务，如果AMF上和SMF上都进行了配置，系统默认使用SMF的实现。  适用于AMF、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网关选择功能","WSFD-205011 本地PDU会话重建","激活本地PDU会话重建特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活本地PDU会话重建操作过程。AMF和SMF上分别实现了本地PDU会话重建功能，AMF和SMF上完成一种配置即可实现此特性的激活任务，如果AMF上和SMF上都进行了配置，系统默认使用SMF的实现。适用于AMF、SMF。

## 必备事项
前提条件

前提条件

* AMF侧使用NF Instance ID识别非本地SMF的PDU会话连接方式，运营商网络中NF Instance ID的规划满足以下条件：
  + NF Instance ID命名规则采用通用唯一标识符(UUID) 4版本格式。
  + NF Instance ID的node部分使用固定的字符表示指定的区域。
* 请仔细阅读WSFD-205011 本地PDU会话重建特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    add_smfresel_list:
      type: items
      properties:
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'AMF通过比较AMF和SMF的NF Instance ID进行本地SMF重选策略。  对于需要重建的PDU会话，UE进入CM-IDLE状态达到60秒，且处于00:02:00~00:04:00之间时间段时才进行PDU会话重建操作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISNSSAI:
          name: '是否匹配S-NSSAI'
          type: string
          enum:
          - YES
          - NO
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESELCOND:
          name: '重选条件'
          type: string
          enum:
          - NFINSTANCEID
          - ISMF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NFINSTANCEID
        NBEGIN:
          name: '区域标识起始位置'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEND:
          name: '区域标识终止位置'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CMIDLETIME:
          name: 'CM-IDLE状态时间阈值(秒)'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ST:
          name: '起始时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM&SS'
        ET:
          name: '结束时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM&SS'
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfresel_list_1:
      type: items
      properties:
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'AMF通过比较AMF和SMF的NF Instance ID进行本地SMF重选策略。  对于需要重建的PDU会话，UE进入CM-IDLE状态达到60秒，且处于00:02:00~00:04:00之间时间段时才进行PDU会话重建操作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISNSSAI:
          name: '是否匹配S-NSSAI'
          type: string
          enum:
          - YES
          - NO
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESELCOND:
          name: '重选条件'
          type: string
          enum:
          - NFINSTANCEID
          - ISMF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NFINSTANCEID
        NBEGIN:
          name: '区域标识起始位置'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEND:
          name: '区域标识终止位置'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CMIDLETIME:
          name: 'CM-IDLE状态时间阈值(秒)'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ST:
          name: '起始时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM&SS'
        ET:
          name: '结束时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 'HH&MM&SS'
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfpdureact_list:
      type: items
      properties:
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'SMF跨区域PDU会话重建策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISNSSAI:
          name: '是否匹配S-NSSAI'
          type: string
          enum:
          - YES
          - NO
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBEGIN:
          name: '区域标识起始位置'
          type: integer
          minimum: 1
          maximum: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NEND:
          name: '区域标识终止位置'
          type: integer
          minimum: 1
          maximum: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smfselplcy_list:
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAISW:
          name: '是否使用TAI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '支持AMF基于UE位置选择SMF，使用UE当前所驻留的TAI作为目标SMF的选择条件。'
          data_source: '全网规划'
          pattern: ''
          default: NO
        ISMFSW:
          name: '是否支持I-SMF选择'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCDISCOPTSW:
          name: '本地服务发现SMF调优开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSSW:
          name: '是否携带Serving Scope'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfloc_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfAMF
          - NfSMF
          required: true
          description: 'AMF配置优选区域信息，服务发现时选择优选区域的目标NF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREFERLOC:
          name: '优选区域'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCTYPE:
          name: '位置类型'
          type: string
          enum:
          - LOCALITY
          - PREFERRED_LOCALITY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PREFERRED_LOCALITY
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2AMFLS01'
      SWITCH: ENABLE
    add_smfresel_list:
    - DNN: 'IMS'
      ISNSSAI: NO
      RESELCOND: NFINSTANCEID
      NBEGIN: 5
      NEND: 6
      CMIDLETIME: 60
      ST: '00:02:00'
      ET: '00:04:00'
      SD: ''
      SST: ''
    add_smfresel_list_1:
    - DNN: 'IMS'
      ISNSSAI: NO
      RESELCOND: NFINSTANCEID
      NBEGIN: 5
      NEND: 6
      CMIDLETIME: 60
      ST: '00:02:00'
      ET: '00:04:00'
      SD: ''
      SST: ''
    add_smfpdureact_list:
    - DNN: 'IMS'
      ISNSSAI: NO
      NBEGIN: 5
      NEND: 6
      SD: ''
      SST: ''
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1059
      VALUE: VALUE_1
      POSITION: 29
      BYTENUM: ''
      BYTEPOSITION: ''
    add_smfselplcy_list:
    - SUBRANGE: ALL_USER
      TAISW: YES
      ISMFSW: NO
      IMSIPRE: ''
      LOCDISCOPTSW: ''
      SSSW: ''
    add_nfloc_list:
    - NFTYPE: AMF
      PREFERLOC: 'Area2'
      LOCTYPE: PREFERRED_LOCALITY
    add_pnfprofile_list:
    - NFINSTANCEID: ''
      NFTYPE: ''
      FQDN: ''
      SCHEME: HTTPS
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置PDU会话重选策略。

### * 3.a和3.b只能配置其中一种方式。

### * 3.a、3.b和3.c分别为AMF和SMF侧的实现，配置时根据需要AMF侧和SMF侧选择一侧配置即可。如果AMF和SMF都进行了配置，系统默认使用SMF的实现。

#### 3.1 **可选：**AMF侧通过比较AMF和SMF的NF Instance ID方式配置PDU会话重建。

```jinja2
{%- if is_optional_amf_nf_instance_id and is_scenario_amf_nf_instance_id -%}
    {%- for item in add_smfresel_list -%}
        ADD SMFRESEL:
        {#- --- 必选参数 --- -#}
        DNN="{{item.DNN}}",
        ISNSSAI={{item.ISNSSAI}},
        {#- --- 可选参数 --- -#}
        {%- if item.RESELCOND is not none -%}
            RESELCOND={{item.RESELCOND}},
        {%- endif -%}
        {%- if item.CMIDLETIME is not none -%}
            CMIDLETIME={{item.CMIDLETIME}},
        {%- endif -%}
        {%- if item.ST is not none -%}
            ST={{item.ST}},
        {%- endif -%}
        {%- if item.ET is not none -%}
            ET={{item.ET}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RESELCOND=NFINSTANCEID 时必选 --- -#}
        {%- if item.RESELCOND == 'NFINSTANCEID' -%}
            NBEGIN={{item.NBEGIN}},
        {%- endif -%}
        {#- --- 条件必选：RESELCOND=NFINSTANCEID 时必选 --- -#}
        {%- if item.RESELCOND == 'NFINSTANCEID' -%}
            NEND={{item.NEND}},
        {%- endif -%}
        {#- --- 条件必选：ISNSSAI=YES 时必选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            SST={{item.SST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISNSSAI=YES 时可选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            {%- if item.SD is not none -%}
                SD="{{item.SD}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 **可选：**AMF侧通过判断I-SMF插入/修改方式配置PDU会话重建。

```jinja2
{%- if is_optional_amf_i_smf and is_scenario_amf_i_smf -%}
    {%- for item in add_smfresel_list_1 -%}
        ADD SMFRESEL:
        {#- --- 必选参数 --- -#}
        DNN="{{item.DNN}}",
        ISNSSAI={{item.ISNSSAI}},
        {#- --- 可选参数 --- -#}
        {%- if item.CMIDLETIME is not none -%}
            CMIDLETIME={{item.CMIDLETIME}},
        {%- endif -%}
        {%- if item.ET is not none -%}
            ET={{item.ET}},
        {%- endif -%}
        {%- if item.RESELCOND is not none -%}
            RESELCOND={{item.RESELCOND}},
        {%- endif -%}
        {%- if item.ST is not none -%}
            ST={{item.ST}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RESELCOND=NFINSTANCEID 时必选 --- -#}
        {%- if item.RESELCOND == 'NFINSTANCEID' -%}
            NBEGIN={{item.NBEGIN}},
        {%- endif -%}
        {#- --- 条件必选：RESELCOND=NFINSTANCEID 时必选 --- -#}
        {%- if item.RESELCOND == 'NFINSTANCEID' -%}
            NEND={{item.NEND}},
        {%- endif -%}
        {#- --- 条件必选：ISNSSAI=YES 时必选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            SST={{item.SST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISNSSAI=YES 时可选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            {%- if item.SD is not none -%}
                SD="{{item.SD}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 **可选：**SMF侧配置PDU会话重建。

```jinja2
{%- if is_optional_smf and is_scenario_smf -%}
    {%- for item in add_smfpdureact_list -%}
        ADD SMFPDUREACT:
        {#- --- 必选参数 --- -#}
        DNN="{{item.DNN}}",
        ISNSSAI={{item.ISNSSAI}},
        NBEGIN={{item.NBEGIN}},
        NEND={{item.NEND}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：ISNSSAI=YES 时必选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            SST={{item.SST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISNSSAI=YES 时可选 --- -#}
        {%- if item.ISNSSAI == 'YES' -%}
            {%- if item.SD is not none -%}
                SD="{{item.SD}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_smf and is_scenario_smf -%}
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
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTEPOSITION={{item.BYTEPOSITION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置AMF重选时选择同区域SMF。

### 以下场景至少选择一种，达到AMF重选选择同区域SMF的目的。

#### 4.1 **可选：**配置AMF根据UE位置选择SMF。

```jinja2
{%- if is_optional_amf_ue_location_select and is_scenario_ue_location -%}
    {%- for item in add_smfselplcy_list -%}
        ADD SMFSELPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ISMFSW is not none -%}
            ISMFSW={{item.ISMFSW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ISMFSW=NO 时可选 --- -#}
        {%- if item.ISMFSW == 'NO' -%}
            {%- if item.TAISW is not none -%}
                TAISW={{item.TAISW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=IMSI_PREFIX 时可选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            {%- if item.LOCDISCOPTSW is not none -%}
                LOCDISCOPTSW={{item.LOCDISCOPTSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBRANGE=ALL_USER/HOME_USER/FOREIGN_USER/IMSI_PREFIX 时可选 --- -#}
        {%- if item.SUBRANGE in ['ALL_USER', 'HOME_USER', 'FOREIGN_USER', 'IMSI_PREFIX'] -%}
            {%- if item.SSSW is not none -%}
                SSSW={{item.SSSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 **可选：**配置AMF根据位置优选SMF。

```jinja2
{%- if is_optional_amf_preferred_location and is_scenario_preferred_location -%}
    {%- for item in add_nfloc_list -%}
        ADD NFLOC:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOCTYPE is not none -%}
            LOCTYPE={{item.LOCTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：LOCTYPE=PREFERRED_LOCALITY 时可选 --- -#}
        {%- if item.LOCTYPE == 'PREFERRED_LOCALITY' -%}
            {%- if item.PREFERLOC is not none -%}
                PREFERLOC="{{item.PREFERLOC}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**当现网不存在NRF时 ，可以在AMF上直接配置同区域SMF的信息。

```jinja2
{%- if is_optional_no_nrf_direct_config -%}
    {%- for item in add_pnfprofile_list -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 条件可选参数 --- -#}
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
{%- endif -%}
```

