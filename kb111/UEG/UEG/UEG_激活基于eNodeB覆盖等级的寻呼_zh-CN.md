---
id: GWFD-026110
name: 激活基于eNodeB覆盖等级的寻呼
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活基于eNodeB覆盖等级的寻呼的操作过程。  随着物联网的广泛应用，智能终端也广泛部署在各种环境中，例如智能停车、智能抄表等大都部署在信号较弱或者没有信号的偏远郊区或者地下室，这就要求IoT基站深覆盖。目前IoT基站能够实现比LTE基站增强20dB寻呼终端，满足深覆盖需要。但并不是所有的终端都是位于覆盖较差的地方，若基站都是使用高覆盖等级进行寻呼，会导致容量下降，终端功耗增加。因此通过基于eNodeB覆盖等级(Coverage Enhancement Level)寻呼技术，将小区划分为不同的覆盖等级，根据小区信号进行等级寻呼，可节约空口资源，保证业务质量，节省终端电量。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026110 基于eNodeB覆盖等级的寻呼","激活基于eNodeB覆盖等级的寻呼"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于eNodeB覆盖等级的寻呼的操作过程。随着物联网的广泛应用，智能终端也广泛部署在各种环境中，例如智能停车、智能抄表等大都部署在信号较弱或者没有信号的偏远郊区或者地下室，这就要求IoT基站深覆盖。目前IoT基站能够实现比LTE基站增强20dB寻呼终端，满足深覆盖需要。但并不是所有的终端都是位于覆盖较差的地方，若基站都是使用高覆盖等级进行寻呼，会导致容量下降，终端功耗增加。因此通过基于eNodeB覆盖等级(Coverage Enhancement Level)寻呼技术，将小区划分为不同的覆盖等级，根据小区信号进行等级寻呼，可节约空口资源，保证业务质量，节省终端电量。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-026110 基于eNodeB覆盖等级的寻呼特性概述。
* 部署WSFD-206001 精准寻呼特性

  若与WSFD-206001 精准寻呼特性一起部署，需要在MME上部署LTE精准寻呼特性，且**ADD S1PAGINGRULE**的参数“ACTGRP”配置包含“NEIGH\_ENODEB（邻接eNodeB）”，会基于eNodeB进行寻呼。单独部署时，会基于TA List进行寻呼。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_m2mctrl_list:
      type: items
      properties:
        CHK_ENB_CE_SW:
          name: 'eNodeB覆盖增强检查开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1cmpt_list:
      type: items
      properties:
        NPAS:
          name: 'Next Paging Area Scope开关'
          type: string
          enum:
          - NO
          - YES
          required: false
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
    add_s1pagingrule_list:
      type: items
      properties:
        GRPTYPE:
          name: '用户群类型'
          type: string
          enum:
          - ALL_USER
          - IMEI_TAC
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRTYPE:
          name: '业务类型'
          type: string
          enum:
          - OTHER
          - S102_PAGING
          - S11_DOWNLINK
          - S6A_IDR_PAGING
          - SGS_PAGING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNIND:
          name: 'APN指示'
          type: string
          enum:
          - ALL_APN
          - SPEC_APN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN NI'
          type: string
          maxLength: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTGRP:
          name: '寻呼动作组合'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nbemm_list:
      type: items
      properties:
        N3413:
          name: 'N3413（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1pagingctrl_list:
      type: items
      properties:
        SUBT3413:
          name: 'SUB_T3413（s）'
          type: integer
          minimum: 2
          maximum: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
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
  examples:
    set_m2mctrl_list:
    - CHK_ENB_CE_SW: ON
    set_s1cmpt_list:
    - NPAS: YES
    set_licenseswitch_list:
    - LICITEM: 'LKV2CELP01'
      SWITCH: ENABLE
    add_s1pagingrule_list:
    - GRPTYPE: ALL_USER
      SVRTYPE: S11_DOWNLINK
      APNIND: SPEC_APN
      MCC: '123'
      MNC: '03'
      APN: 'NBIOT.HUAWEI.COM'
      ACTGRP: LAST_ENODEB-1&NEIGH_ENODEB-1&LAST_TAI-1
    set_nbemm_list:
    - N3413: 3
    set_s1pagingctrl_list:
    - SUBT3413: 5
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2PRPG02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**配置“eNodeB覆盖增强检查开关”为“打开”。

```jinja2
{%- if is_optional_enb_coverage_check_switch -%}
    {%- for item in set_m2mctrl_list -%}
        SET M2MCTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.CHK_ENB_CE_SW is not none -%}
            CHK_ENB_CE_SW={{item.CHK_ENB_CE_SW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当“eNodeB覆盖增强检查开关”为“打开”时，MME只向支持覆盖增强寻呼的eNodeB下发携带寻呼辅助信息（Assistance Data for Paging）信元的寻呼请求。关于此参数的详细说明请参考**SET M2MCTRL**。

### 3 **可选：**配置“Next Paging Area Scope开关”为“YES”。

```jinja2
{%- if is_optional_next_paging_area_scope -%}
    {%- for item in set_s1cmpt_list -%}
        SET S1CMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.NPAS is not none -%}
            NPAS={{item.NPAS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_s1pagingrule_list -%}
    ADD S1PAGINGRULE:
    {#- --- 必选参数 --- -#}
    GRPTYPE={{item.GRPTYPE}},
    SVRTYPE={{item.SVRTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ACTGRP is not none -%}
        ACTGRP={{item.ACTGRP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SVRTYPE=S11_DOWNLINK 时必选 --- -#}
    {%- if item.SVRTYPE == 'S11_DOWNLINK' -%}
        APNIND={{item.APNIND}},
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {#- --- 条件必选：APNIND=SPEC_APN 时必选 --- -#}
    {%- if item.APNIND == 'SPEC_APN' -%}
        APN="{{item.APN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_nbemm_list -%}
    SET NBEMM:
    {#- --- 可选参数 --- -#}
    {%- if item.N3413 is not none -%}
        N3413={{item.N3413}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_s1pagingctrl_list -%}
    SET S1PAGINGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.SUBT3413 is not none -%}
        SUBT3413={{item.SUBT3413}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

