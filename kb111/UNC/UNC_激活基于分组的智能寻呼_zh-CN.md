---
id: ''
name: 激活基于分组的智能寻呼
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于分组的智能寻呼功能的操作过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-206010 基于分组的智能寻呼","激活基于分组的智能寻呼"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于分组的智能寻呼功能的操作过程。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-206010 基于分组的智能寻呼。
* 已完成License加载，对应License项为"82200JAM LKV2SGPPG01 基于分组的智能寻呼"。
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
          description: '开启License项配置开关。'
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
    add_ngpeipsplcy_list:
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
          - SPECIFIC_IMSI
          required: true
          description: '配置基于分组的智能寻呼策略的用户范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 14
          required: false
          description: '当“用户范围（SUBRANGE）”为“IMSI\_PREFIX”时，该参数用于指定具体的IMSI前缀信息。'
          data_source: ''
          pattern: ''
          default: ''
        FEATURECOND:
          name: '特征条件组合'
          type: string
          enum:
          - NONE
          - DNN
          - NSSAI
          - DNN_NSSAI
          - PAGINGPRO
          required: true
          description: '配置基于分组的智能寻呼策略的特征条件的组合。'
          data_source: ''
          pattern: ''
          default: ''
        PAGINGPRO:
          name: '寻呼概率'
          type: string
          enum:
          - P00
          - P05
          - P10
          - P15
          - P20
          - P25
          - P30
          - P35
          - P40
          - P45
          - P50
          - P55
          - P60
          - P65
          - P70
          - P75
          - P80
          - P85
          - P90
          - P95
          - P100
          required: false
          description: '配置特性条件中的终端寻呼概率。'
          data_source: ''
          pattern: ''
          default: ''
        PAGINGGRPSRC:
          name: '寻呼分组来源'
          type: string
          enum:
          - USE_CONFIG
          - USE_UE_REQUEST
          required: false
          description: '配置下发给UE和NG-RAN使用的寻呼分组取值来源。'
          data_source: ''
          pattern: ''
          default: ''
        PAGINGGRPID:
          name: '寻呼分组标识'
          type: integer
          minimum: 0
          maximum: 7
          required: false
          description: '配置下发给UE和NG-RAN的寻呼分组标识。'
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置特性条件中的DNN信息。'
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '配置特性条件中的切片信息中的切片业务类型。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: '配置特性条件中的切片信息中的切片细分标识。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsbicmpt_list:
      type: items
      properties:
        SNDPEIPSINFO:
          name: 'N14接口是否携带PEIPS信元以及寻呼分组标识'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带PEIPS信元以及寻呼分组标识。  说明：  当AMF Pool内有异厂商AMF时，需要将本参数设置为“NO（否）”。  当AMF Pool内无异厂商AMF且本AMF支持PEIPS特性时，建议将本参数设置为“YES（是）”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SBITYPE:
          name: '服务化接口类型'
          type: string
          enum:
          - N8
          - N11
          - N12
          - N14
          - N15
          - N17
          - N20
          - N22
          - N50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMPCFNI:
          name: '是否携带动态NI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVTGNBLST:
          name: 'N14接口是否携带GlobalGnbIdList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVTPERIOD:
          name: 'N14接口是否携带repPeriod'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HAMPCFID:
          name: 'N15接口是否携带hpcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N11MSGTYPE:
          name: 'N11接口消息类型'
          type: string
          enum:
          - UPDATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDAMPLCYTRIG:
          name: 'N14接口是否携带amPolicyReqTriggerList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDAMPLCYURI:
          name: 'N14接口是否携带pcfAmPolicyUri'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDHPCFID:
          name: 'N14接口是否携带hpcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDPCFID:
          name: 'N14接口是否携带pcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDPCFSETID:
          name: 'N14接口是否携带pcfSetId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDSMFSELINFO:
          name: 'N14接口是否携带smfSelInfo'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDUEPLCYTRIG:
          name: 'N14接口是否携带uePolicyReqTriggerList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDUEPLCYURI:
          name: 'N14接口是否携带pcfUePolicyUri'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOCAPPAGING:
          name: '是否携带UE Radio Capability for Paging'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDPCFRFSP:
          name: '是否携带PcfRfsp'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDPRVEDRXINFO:
          name: '是否携带eDRX私有信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDRATTYPE:
          name: '是否给SMSF携带RATTYPE'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDREDCAPIND:
          name: '是否携带RedCap指示'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRSPN2CLASS:
          name: '是否携带N2InformationClass'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmfunc_list:
      type: items
      properties:
        PAGINGENSW:
          name: '寻呼增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置寻呼UE时，如果用户的新TAILIST和旧TAILIST都有效时，是否要针对旧TAILIST做增强处理。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2SGPPG01'
      SWITCH: ENABLE
    add_ngpeipsplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12305'
      FEATURECOND: PAGINGPRO
      PAGINGPRO: P95
      PAGINGGRPSRC: USE_CONFIG
      PAGINGGRPID: 0
      DNN: 'huawei.com'
      SST: 1
      SD: '010101'
      IMSI: ''
    set_amfsbicmpt_list:
    - SNDPEIPSINFO: YES
      SBITYPE: ''
      AMPCFNI: ''
      EVTGNBLST: ''
      EVTPERIOD: ''
      HAMPCFID: ''
      N11MSGTYPE: ''
      OLDAMPLCYTRIG: ''
      OLDAMPLCYURI: ''
      OLDHPCFID: ''
      OLDPCFID: ''
      OLDPCFSETID: ''
      OLDSMFSELINFO: ''
      OLDUEPLCYTRIG: ''
      OLDUEPLCYURI: ''
      RADIOCAPPAGING: ''
      SNDPCFRFSP: ''
      SNDPRVEDRXINFO: ''
      SNDRATTYPE: ''
      SNDREDCAPIND: ''
      SUBRSPN2CLASS: ''
    set_ngmmfunc_list:
    - PAGINGENSW: ON
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 开启License项配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置基于分组的智能寻呼策略。

```jinja2
{%- for item in add_ngpeipsplcy_list -%}
    ADD NGPEIPSPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    FEATURECOND={{item.FEATURECOND}},
    {#- --- 可选参数 --- -#}
    {%- if item.PAGINGGRPSRC is not none -%}
        PAGINGGRPSRC={{item.PAGINGGRPSRC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：FEATURECOND=PAGINGPRO 时必选 --- -#}
    {%- if item.FEATURECOND == 'PAGINGPRO' -%}
        PAGINGPRO={{item.PAGINGPRO}},
    {%- endif -%}
    {#- --- 条件必选：PAGINGGRPSRC=USE_CONFIG 时必选 --- -#}
    {%- if item.PAGINGGRPSRC == 'USE_CONFIG' -%}
        PAGINGGRPID={{item.PAGINGGRPID}},
    {%- endif -%}
    {#- --- 条件必选：FEATURECOND=DNN/DNN_NSSAI 时必选 --- -#}
    {%- if item.FEATURECOND in ['DNN', 'DNN_NSSAI'] -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：FEATURECOND=NSSAI/DNN_NSSAI 时必选 --- -#}
    {%- if item.FEATURECOND in ['NSSAI', 'DNN_NSSAI'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=SPECIFIC_IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'SPECIFIC_IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FEATURECOND=NSSAI/DNN_NSSAI 时可选 --- -#}
    {%- if item.FEATURECOND in ['NSSAI', 'DNN_NSSAI'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带PEIPS信元以及寻呼分组标识。

```jinja2
{%- for item in set_amfsbicmpt_list -%}
    SET AMFSBICMPT:
    {#- --- 必选参数 --- -#}
    SBITYPE={{item.SBITYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPEIPSINFO is not none -%}
            SNDPEIPSINFO={{item.SNDPEIPSINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.AMPCFNI is not none -%}
            AMPCFNI={{item.AMPCFNI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.EVTGNBLST is not none -%}
            EVTGNBLST={{item.EVTGNBLST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.EVTPERIOD is not none -%}
            EVTPERIOD={{item.EVTPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N15 时可选 --- -#}
    {%- if item.SBITYPE == 'N15' -%}
        {%- if item.HAMPCFID is not none -%}
            HAMPCFID={{item.HAMPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N11 时可选 --- -#}
    {%- if item.SBITYPE == 'N11' -%}
        {%- if item.N11MSGTYPE is not none -%}
            N11MSGTYPE={{item.N11MSGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDAMPLCYTRIG is not none -%}
            OLDAMPLCYTRIG={{item.OLDAMPLCYTRIG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDAMPLCYURI is not none -%}
            OLDAMPLCYURI={{item.OLDAMPLCYURI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDHPCFID is not none -%}
            OLDHPCFID={{item.OLDHPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDPCFID is not none -%}
            OLDPCFID={{item.OLDPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDPCFSETID is not none -%}
            OLDPCFSETID={{item.OLDPCFSETID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDSMFSELINFO is not none -%}
            OLDSMFSELINFO={{item.OLDSMFSELINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDUEPLCYTRIG is not none -%}
            OLDUEPLCYTRIG={{item.OLDUEPLCYTRIG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDUEPLCYURI is not none -%}
            OLDUEPLCYURI={{item.OLDUEPLCYURI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.RADIOCAPPAGING is not none -%}
            RADIOCAPPAGING={{item.RADIOCAPPAGING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPCFRFSP is not none -%}
            SNDPCFRFSP={{item.SNDPCFRFSP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPRVEDRXINFO is not none -%}
            SNDPRVEDRXINFO={{item.SNDPRVEDRXINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N20 时可选 --- -#}
    {%- if item.SBITYPE == 'N20' -%}
        {%- if item.SNDRATTYPE is not none -%}
            SNDRATTYPE={{item.SNDRATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDREDCAPIND is not none -%}
            SNDREDCAPIND={{item.SNDREDCAPIND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N50 时可选 --- -#}
    {%- if item.SBITYPE == 'N50' -%}
        {%- if item.SUBRSPN2CLASS is not none -%}
            SUBRSPN2CLASS={{item.SUBRSPN2CLASS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置寻呼UE时，如果用户的新TAILIST和旧TAILIST都有效时，是否要针对旧TAILIST做增强处理。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.PAGINGENSW is not none -%}
        PAGINGENSW={{item.PAGINGENSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

