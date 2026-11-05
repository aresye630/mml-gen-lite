---
id: GWFD-022201
name: 配置AM策略和UE策略
ne_type: UEG
type: feature
description: 当需要配置AM策略和UE策略时，请参考本页面。  本版本AMF暂不支持与PCF交互。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-022200 智能策略控制基本功能","GWFD-022201 PCC基本功能","配置AM策略和UE策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当需要配置AM策略和UE策略时，请参考本页面。本版本AMF暂不支持与PCF交互。

## 必备事项
前提条件

* 请仔细阅读特性概述。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
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
    add_pcfselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - USER_GROUP
          - IMSI_PREFIX
          required: true
          description: 'AMF为指定用户群增加PCF的选择策略。此处以所有用户按照SUPI为例，实际请以规划为准。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TGTPLMNSW:
          name: '是否适用目标PLMN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        SUPISW:
          name: '是否适用SUPI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        GPSISW:
          name: '是否适用GPSI'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        NSSW:
          name: '是否适用网络切片'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        RETRYSW:
          name: '是否重选PCF'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: 'AMF在收到初选PCF的5xx原因值后，是否重选PCF再次重试AM策略和UE策略偶联创建流程。'
          data_source: '全网规划'
          pattern: ''
          default: YES
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: '自定义，便于运维即可。'
          data_source: ''
          pattern: ''
          default: ''
    add_amueplcyctrl_list:
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
          - MSISDN_PREFIX
          required: true
          description: '在AMF上配置AM策略和UE策略控制参数的用户范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NSGRPID:
          name: '网络切片群组标识'
          type: integer
          minimum: 0
          maximum: 16
          required: false
          description: '0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。'
          data_source: '全网规划'
          pattern: ''
          default: 0
        ISAMASSOC:
          name: '是否建立AM策略偶联'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: 'AMF与PCF无交互，使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: NO
        ISUEASSOC:
          name: '是否建立UE策略偶联'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: '描述配置AM策略和UE策略控制参数的用户（群），便于记忆。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngmmsubdata_list:
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
          - IMSI
          required: true
          description: '在AMF上配置哪些用户可使用本地RFSP索引。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RATRESTRICT:
          name: 'RAT限制'
          type: string
          required: false
          description: '此处以5G终端接入5G Core为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CORERESTRICT:
          name: '核心网类型限制'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RFSPPRI:
          name: 'RFSP优先级'
          type: string
          enum:
          - CFG_FIRST
          - SUB_FIRST
          required: false
          description: '* 设置为“CFG_FIRST”，无论用户是否签约RFSP ID，均使用本地配置的RFSP索引。该场景下本地的“RFSP索引”不能为“0”。 * 设置为“SUB_FIRST”时，优先使用用户签约的RFSP ID，如用户未签约RFSP ID，使用本地配置的RFSP索引。   AMF根据该配置，决策携带哪个RFSP索引 给PCF。后续处理为：   * PCF返回RFSP索引时，AMF将PCF返回的RFSP索引发送给无线侧。 * PCF未返回RFSP索引时，AMF将此处决策的RFSP索引发送给无线侧。'
          data_source: '全网规划'
          pattern: ''
          default: CFG_FIRST
        RFSPINDEX:
          name: 'RFSP索引'
          type: integer
          minimum: 0
          maximum: 256
          required: false
          description: '取值非0时，此处是本地配置的RFSP索引。  取值为0时，标识未配置本地的RFSP索引。'
          data_source: '全网规划'
          pattern: ''
          default: 0
    mod_cpnfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '根据NFLOC选择PCF时需要规划。'
          data_source: '-'
          pattern: ''
          default: ''
        LOCALITY:
          name: '位置信息'
          type: string
          minLength: 0
          maxLength: 150
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2PCCBF01'
      SWITCH: ENABLE
    add_pcfselplcy_list:
    - SUBRANGE: HOME_USER
      TGTPLMNSW: NO
      SUPISW: YES
      GPSISW: NO
      NSSW: NO
      RETRYSW: YES
      DESC: 'for home user'
    add_amueplcyctrl_list:
    - SUBRANGE: HOME_USER
      NSGRPID: 0
      ISAMASSOC: NO
      ISUEASSOC: NO
      DESC: 'Enable UE Policy for Home Subscribers'
    add_ngmmsubdata_list:
    - SUBRANGE: HOME_USER
      RATRESTRICT: EUTRA-0&NR-1
      CORERESTRICT: FIFTHGC
      RFSPPRI: CFG_FIRST
      RFSPINDEX: 5
    mod_cpnfprofile_list:
    - NFINSTANCENAME: 'SMF_Instance_0'
      LOCALITY: 'beijing'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置AMF选择PCF的策略信息。

```jinja2
{%- for item in add_pcfselplcy_list -%}
    ADD PCFSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.TGTPLMNSW is not none -%}
        TGTPLMNSW={{item.TGTPLMNSW}},
    {%- endif -%}
    {%- if item.SUPISW is not none -%}
        SUPISW={{item.SUPISW}},
    {%- endif -%}
    {%- if item.GPSISW is not none -%}
        GPSISW={{item.GPSISW}},
    {%- endif -%}
    {%- if item.NSSW is not none -%}
        NSSW={{item.NSSW}},
    {%- endif -%}
    {%- if item.RETRYSW is not none -%}
        RETRYSW={{item.RETRYSW}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置应用网络侧规划的AM策略/UE策略的用户群。

```jinja2
{%- for item in add_amueplcyctrl_list -%}
    ADD AMUEPLCYCTRL:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISAMASSOC is not none -%}
        ISAMASSOC={{item.ISAMASSOC}},
    {%- endif -%}
    {%- if item.ISUEASSOC is not none -%}
        ISUEASSOC={{item.ISUEASSOC}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
    {%- if item.SUBRANGE == 'ALL_USER' -%}
        NSGRPID={{item.NSGRPID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 默认情况下，未开启网络侧规划的AM策略/UE策略。

### 5 配置本地的RFSP索引。用户未签约RFSP ID，或签约的RFSP ID不适用时需要配置。

```jinja2
{%- for item in add_ngmmsubdata_list -%}
    ADD NGMMSUBDATA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.RATRESTRICT is not none -%}
        RATRESTRICT={{item.RATRESTRICT}},
    {%- endif -%}
    {%- if item.CORERESTRICT is not none -%}
        CORERESTRICT={{item.CORERESTRICT}},
    {%- endif -%}
    {%- if item.RFSPPRI is not none -%}
        RFSPPRI={{item.RFSPPRI}},
    {%- endif -%}
    {%- if item.RFSPINDEX is not none -%}
        RFSPINDEX={{item.RFSPINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置根据位置选择PCF。

```jinja2
{%- for item in mod_cpnfprofile_list -%}
    MOD CPNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCALITY is not none -%}
        LOCALITY="{{item.LOCALITY}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

