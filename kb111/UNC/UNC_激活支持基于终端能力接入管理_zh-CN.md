---
id: ''
name: 激活支持基于终端能力接入管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持基于终端能力接入管理的操作过程。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NSA业务基本功能","WSFD-011503 支持基于终端能力接入管理","激活支持基于终端能力接入管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持基于终端能力接入管理的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-011503 支持基于终端能力接入管理特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_nsactrlplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: 'NSA接入控制策略。 说明：  运营商标识（NOID）可通过以下命令查询，   * ****LST MNO****：该参数配置为0或128～254之间的值时。 * ****LST MVNO****：若该参数需要配置为1～64之间的值时'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISDCNR:
          name: '是否支持DC-NR接入'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSECRATRPTSGW:
          name: '是否在使用数据报告中置位IRSGW标志'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        ISSECRATRPT:
          name: '是否在使用数据报告中置位IRPGW标志'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        ISGUUPSEL:
          name: '是否支持GU接入选择用户面'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        RPTPSCELLID:
          name: '是否指示eNodeB上报PS Cell ID信息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
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
          description: 'GTP-C V2协议兼容性'
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
        TMMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CRT_SES_REQ
          - MOD_BR_REQ
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRTSESREQ:
          name: 'Create Session Request的信元类型'
          type: string
          enum:
          - INDICATION
          - UPSELIND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSELFLAG:
          name: 'UP功能选择指示'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRTSESREQIND:
          name: 'Indication Bit位'
          type: string
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        SVMSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - PS_TO_CS_REQ
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MODBRREQ:
          name: 'Modify Bearer Request的信元类型'
          type: string
          enum:
          - BCMOD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPELTEM:
          name: '是否支持LTE-M类型的RAT TYPE'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    set_s1cmpt_list:
      type: items
      properties:
        NRR:
          name: '是否携带NR Restriction信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: 'S1接口兼容性'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_dmcmpt_list:
      type: items
      properties: {}
    add_dmcmptbyimsi_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '指定用户范围的S6a接口兼容性策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSIMSVOPS:
          name: 'Homogeneous Support of IMS VoPS信元'
          type: string
          enum:
          - BY_SYS_CAP
          - BY_UE_CAP
          - NOT_CARRY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: BY_SYS_CAP
        NODCNR:
          name: '未签约DCNR是否允许DCNR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        NOIMSVOPS:
          name: '不允许IMS VoPS的用户处理'
          type: string
          enum:
          - NOT_CARRY
          - NOT_SUPPORT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOT_SUPPORT
        UECAPMATCH:
          name: '用户能力匹配模式'
          type: string
          enum:
          - EXACT
          - FAST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FAST
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_nsactrlplcy_list:
    - SUBRANGE: FOREIGN_USER
      NOID: 2
      ISDCNR: YES
      ISSECRATRPTSGW: YES
      ISSECRATRPT: YES
      ISGUUPSEL: YES
      RPTPSCELLID: NO
      IMSIPRE: ''
    add_gtpcv2cmpt_list:
    - IDX: 0
      MSGCLS: TM
      TMMSGTYPE: CRT_SES_REQ
      CRTSESREQ: UPSELIND
      UPSELFLAG: DCNR-1
      CRTSESREQIND: ''
      MMMSGTYPE: ''
      SVMSGTYPE: ''
      MODBRREQ: ''
      RATTYPELTEM: NO
    set_s1cmpt_list:
    - NRR: YES
    set_dmcmpt_list:
    - {}
    add_dmcmptbyimsi_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '460123'
      SF2: FLSTID2_BIT27-1
      HSIMSVOPS: BY_SYS_CAP
      NODCNR: YES
      NOIMSVOPS: NOT_SUPPORT
      UECAPMATCH: FAST
      NOID: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 增加NSA控制策略。

```jinja2
{%- for item in add_nsactrlplcy_list -%}
    ADD NSACTRLPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    ISDCNR={{item.ISDCNR}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISGUUPSEL is not none -%}
        ISGUUPSEL={{item.ISGUUPSEL}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
    {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
        NOID={{item.NOID}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ISDCNR=YES 时可选 --- -#}
    {%- if item.ISDCNR == 'YES' -%}
        {%- if item.ISSECRATRPTSGW is not none -%}
            ISSECRATRPTSGW={{item.ISSECRATRPTSGW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ISDCNR=YES 时可选 --- -#}
    {%- if item.ISDCNR == 'YES' -%}
        {%- if item.ISSECRATRPT is not none -%}
            ISSECRATRPT={{item.ISSECRATRPT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ISDCNR=YES 时可选 --- -#}
    {%- if item.ISDCNR == 'YES' -%}
        {%- if item.RPTPSCELLID is not none -%}
            RPTPSCELLID={{item.RPTPSCELLID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置GTP-C V2协议兼容性。

```jinja2
{%- for item in add_gtpcv2cmpt_list -%}
    ADD GTPCV2CMPT:
    {#- --- 必选参数 --- -#}
    IDX={{item.IDX}},
    MSGCLS={{item.MSGCLS}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MSGCLS=TM 时必选 --- -#}
    {%- if item.MSGCLS == 'TM' -%}
        TMMSGTYPE={{item.TMMSGTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TMMSGTYPE=CRT_SES_REQ 时必选 --- -#}
    {%- if item.TMMSGTYPE == 'CRT_SES_REQ' -%}
        CRTSESREQ={{item.CRTSESREQ}},
    {%- endif -%}
    {#- --- 条件必选：CRTSESREQ=UPSELIND 时必选 --- -#}
    {%- if item.CRTSESREQ == 'UPSELIND' -%}
        UPSELFLAG={{item.UPSELFLAG}},
    {%- endif -%}
    {#- --- 条件必选：CRTSESREQ=INDICATION 时必选 --- -#}
    {%- if item.CRTSESREQ == 'INDICATION' -%}
        CRTSESREQIND={{item.CRTSESREQIND}},
    {%- endif -%}
    {#- --- 条件必选：MSGCLS=MM 时必选 --- -#}
    {%- if item.MSGCLS == 'MM' -%}
        MMMSGTYPE={{item.MMMSGTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TMMSGTYPE=MOD_BR_REQ 时必选 --- -#}
    {%- if item.TMMSGTYPE == 'MOD_BR_REQ' -%}
        MODBRREQ={{item.MODBRREQ}},
    {%- endif -%}
    {#- --- 条件必选：MSGCLS=SV 时必选 --- -#}
    {%- if item.MSGCLS == 'SV' -%}
        SVMSGTYPE={{item.SVMSGTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MMMSGTYPE=FWD_RLC_REQ/CTX_RSP 时可选 --- -#}
    {%- if item.MMMSGTYPE in ['FWD_RLC_REQ', 'CTX_RSP'] -%}
        {%- if item.RATTYPELTEM is not none -%}
            RATTYPELTEM={{item.RATTYPELTEM}},
        {%- endif -%}
    {#- --- 条件可选：TMMSGTYPE=CRT_SES_REQ/MOD_BR_REQ 时可选 --- -#}
    {%- elif item.TMMSGTYPE in ['CRT_SES_REQ', 'MOD_BR_REQ'] -%}
        {%- if item.RATTYPELTEM is not none -%}
            RATTYPELTEM={{item.RATTYPELTEM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置S1接口兼容性。

```jinja2
{%- for item in set_s1cmpt_list -%}
    SET S1CMPT:
    {#- --- 可选参数 --- -#}
    {%- if item.NRR is not none -%}
        NRR={{item.NRR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置Update Location Request消息携带NR as Secondary RAT信元给HSS。

#### 5.1 若配置整系统支持Update Location Request消息携带NR as Secondary RAT信元给HSS，则执行如下步骤。

```jinja2
{%- if is_scenario_whole_system -%}
    SET DMCMPT:
    ;
{%- endif -%}
```

#### 5.2 若配置指定范围的用户配置Update Location Request消息携带NR as Secondary RAT信元给HSS，则执行如下步骤。

##### 5.2.1 查询DMCMPT配置

##### 命令**ADD DMCMPTBYIMSI**与**SET DMCMPT**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。

##### 5.2.2 配置指定范围的用户配置Update Location Request消息携带NR as Secondary RAT信元给HSS

```jinja2
{%- if is_scenario_specified_user_range -%}
    {%- for item in add_dmcmptbyimsi_list -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {%- if item.HSIMSVOPS is not none -%}
            HSIMSVOPS={{item.HSIMSVOPS}},
        {%- endif -%}
        {%- if item.NODCNR is not none -%}
            NODCNR={{item.NODCNR}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：HSIMSVOPS=BY_UE_CAP 时可选 --- -#}
        {%- if item.HSIMSVOPS == 'BY_UE_CAP' -%}
            {%- if item.NOIMSVOPS is not none -%}
                NOIMSVOPS={{item.NOIMSVOPS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：HSIMSVOPS=BY_UE_CAP 时可选 --- -#}
        {%- if item.HSIMSVOPS == 'BY_UE_CAP' -%}
            {%- if item.UECAPMATCH is not none -%}
                UECAPMATCH={{item.UECAPMATCH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

