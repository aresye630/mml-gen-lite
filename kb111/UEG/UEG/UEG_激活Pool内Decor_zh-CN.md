---
id: GWFD-020912
name: 激活Pool内Decor
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活Pool内DECOR功能的操作过程。  在支持DCNR（Dual connectivity with New Radio）能力的MME和不支持DCNR能力的MME组Pool的场景下，对于支持DCNR能力的终端接入到不支持DCNR能力的MME上的场景，UNC支持将其重定向到Pool内支持DCNR能力的MME上进行服务。  适用于MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020912 DECOR功能","GWFD-020912 Pool内Decor","激活Pool内Decor"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD MMERESELPLCY')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活Pool内DECOR功能的操作过程。在支持DCNR（Dual connectivity with New Radio）能力的MME和不支持DCNR能力的MME组Pool的场景下，对于支持DCNR能力的终端接入到不支持DCNR能力的MME上的场景，UNC支持将其重定向到Pool内支持DCNR能力的MME上进行服务。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-208003 Pool内Decor。
* eNodeB的配置已经具备，具体请参见该特性页面的应用场景部分描述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_mmegp_list:
      type: items
      properties:
        MMEGPIDX:
          name: 'MME群组索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '增加MME群组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmegpmem_list:
      type: items
      properties:
        MMEGPIDX:
          name: 'MME群组索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '增加MME群组成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
    add_ueusgtypegp_list:
      type: items
      properties:
        UEUSGTYPEGPID:
          name: 'UE USAGE TYPE群组标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '增加UE Usage Type群组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_ueusgtypegpmem_list:
      type: items
      properties:
        UEUSGTYPEGPID:
          name: 'UE USAGE TYPE群组标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '增加UE USAGE TYPE群组成员。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BGNUEUSGTYPE:
          name: '起始UE USAGE TYPE'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDUEUSGTYPE:
          name: '终止UE USAGE TYPE'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmereselplcy_list:
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
          description: '设置重选策略。'
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
        RESELSW:
          name: '重选开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESELPLCY:
          name: '重选策略'
          type: string
          enum:
          - REROUTE_NAS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESELCOND:
          name: '重选条件'
          type: string
          enum:
          - DCNR
          - DCNR_UUT_INCLUDE
          - DCNR_UUT_NOT_INCLUDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEUSGTYPEGPID:
          name: 'UE USAGE TYPE群组标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TMMEGPIDX:
          name: '目标MME组索引'
          type: integer
          minimum: 0
          maximum: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dcnctrl_list:
      type: items
      properties:
        RESELECTPLCY:
          name: '重选策略'
          type: string
          enum:
          - DELAY
          - IMMEDIATE
          required: false
          description: '设置DCN控制参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONTAINUEUSGTYPE:
          name: '携带UE Usage Type'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEUSGTYPECONPLCY:
          name: 'UE USAGE TYPE携带策略'
          type: string
          enum:
          - SUBSCRIBE
          - USED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dmcmpt_list:
      type: items
      properties:
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
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
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dmcmpt_list_1:
      type: items
      properties:
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list_1:
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
          description: ''
          data_source: ''
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
    add_dmcmptbyimsi_list_3:
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
          description: ''
          data_source: ''
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
    add_dmcmptbyimsi_list_5:
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
          description: ''
          data_source: ''
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
        SF2:
          name: '特性列表2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmcmptbyimsi_list_6:
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
          description: ''
          data_source: ''
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
    str_dcnoffload_list:
      type: items
      properties:
        OFFLOADTYPE:
          name: '迁移用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI
          - IMSI_PRE
          required: false
          description: '启动DCN迁移任务。'
          data_source: '本端规划'
          pattern: ''
          default: ALL_USER
  examples:
    add_mmegp_list:
    - MMEGPIDX: 0
      MCC: '123'
      MNC: '03'
      MMEGI: '0001'
      DESC: 'NSA'
    add_mmegpmem_list:
    - MMEGPIDX: 0
      MMEC: '01'
      CAP: 10
    add_ueusgtypegp_list:
    - UEUSGTYPEGPID: 10
      DESC: 'NSA'
    add_ueusgtypegpmem_list:
    - UEUSGTYPEGPID: 10
      BGNUEUSGTYPE: 130
      ENDUEUSGTYPE: 150
    add_mmereselplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      RESELSW: ON
      RESELPLCY: REROUTE_NAS
      RESELCOND: DCNR_UUT_INCLUDE
      UEUSGTYPEGPID: 10
      TMMEGPIDX: 0
    set_dcnctrl_list:
    - RESELECTPLCY: IMMEDIATE
      CONTAINUEUSGTYPE: YES
      UEUSGTYPECONPLCY: USED
    set_dmcmpt_list:
    - SF2: FLSTID2_BIT20-1
    add_dmcmptbyimsi_list:
    - SUBRANGE: HOME_USER
      NOID: 0
      SF2: FLSTID2_BIT20-1
    set_dmcmpt_list_1:
    - SF2: FLSTID2_BIT20-0
    add_dmcmptbyimsi_list_1:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '46123'
      SF2: FLSTID2_BIT20-1
    add_dmcmptbyimsi_list_3:
    - SUBRANGE: HOME_USER
      NOID: 运营商标识
      SF2: 特性列表
      HSIMSVOPS: BY_SYS_CAP
    add_dmcmptbyimsi_list_5:
    - SUBRANGE: FOREIGN_USER
      NOID: 运营商标识
      SF2: 特性列表
    add_dmcmptbyimsi_list_6:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: 'IMSI前缀'
      SF2: 特性列表
    set_licenseswitch_list:
    - LICITEM: 'LKV2DECOR02'
      SWITCH: ENABLE
    str_dcnoffload_list:
    - OFFLOADTYPE: ALL_USER
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 规划支持DCNR能力的MME群组信息。

#### 2.1 增加MME群组

```jinja2
{%- for item in add_mmegp_list -%}
    ADD MMEGP:
    {#- --- 必选参数 --- -#}
    MMEGPIDX={{item.MMEGPIDX}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 为MME群组添加成员，如果群组中包含多个MME编码，则多次执行此步骤。

```jinja2
{%- for item in add_mmegpmem_list -%}
    ADD MMEGPMEM:
    {#- --- 必选参数 --- -#}
    MMEGPIDX={{item.MMEGPIDX}},
    MMEC="{{item.MMEC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**当4中重选条件中有需要使用UE Usage Type，则需要配置此步骤。

#### 3.1 添加UE Usage Type群组标识。配置该群组标识，用于配置本地的DNS记录。

```jinja2
{%- set ADD_MMERESELPLCY=getParameterValue('ADD MMERESELPLCY') -%}
{%- if is_optional_ue_usage_type_group and ADD_MMERESELPLCY -%}
    {%- for item in add_ueusgtypegp_list -%}
        ADD UEUSGTYPEGP:
        {#- --- 必选参数 --- -#}
        UEUSGTYPEGPID={{item.UEUSGTYPEGPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 添加UE Usage Type群组的成员列表。

```jinja2
{%- if is_optional_ue_usage_type_group and ADD_MMERESELPLCY -%}
    {%- for item in add_ueusgtypegpmem_list -%}
        ADD UEUSGTYPEGPMEM:
        {#- --- 必选参数 --- -#}
        UEUSGTYPEGPID={{item.UEUSGTYPEGPID}},
        BGNUEUSGTYPE={{item.BGNUEUSGTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENDUEUSGTYPE is not none -%}
            ENDUEUSGTYPE={{item.ENDUEUSGTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置重选策略。

```jinja2
{%- for item in add_mmereselplcy_list -%}
    ADD MMERESELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    RESELSW={{item.RESELSW}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：RESELSW=ON 时必选 --- -#}
    {%- if item.RESELSW == 'ON' -%}
        RESELPLCY={{item.RESELPLCY}},
    {%- endif -%}
    {#- --- 条件必选：RESELPLCY=REROUTE_NAS 时必选 --- -#}
    {%- if item.RESELPLCY == 'REROUTE_NAS' -%}
        RESELCOND={{item.RESELCOND}},
    {%- endif -%}
    {#- --- 条件必选：RESELCOND=DCNR_UUT_INCLUDE/DCNR_UUT_NOT_INCLUDE 时必选 --- -#}
    {%- if item.RESELCOND in ['DCNR_UUT_INCLUDE', 'DCNR_UUT_NOT_INCLUDE'] -%}
        UEUSGTYPEGPID={{item.UEUSGTYPEGPID}},
    {%- endif -%}
    {#- --- 条件必选：RESELPLCY=REROUTE_NAS 时必选 --- -#}
    {%- if item.RESELPLCY == 'REROUTE_NAS' -%}
        TMMEGPIDX={{item.TMMEGPIDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置DECOR相关控制参数

```jinja2
{%- for item in set_dcnctrl_list -%}
    SET DCNCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.RESELECTPLCY is not none -%}
        RESELECTPLCY={{item.RESELECTPLCY}},
    {%- endif -%}
    {%- if item.CONTAINUEUSGTYPE is not none -%}
        CONTAINUEUSGTYPE={{item.CONTAINUEUSGTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONTAINUEUSGTYPE=YES 时可选 --- -#}
    {%- if item.CONTAINUEUSGTYPE == 'YES' -%}
        {%- if item.UEUSGTYPECONPLCY is not none -%}
            UEUSGTYPECONPLCY={{item.UEUSGTYPECONPLCY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 当4中重选条件中包含UE Usage Type，则需要此步骤，向HSS获取UE Usage Type。

### 实际部署时，需要根据HSS是否支持本特性，组合如下命令进行配置，

#### 6.1 所有HSS都支持此特性：

```jinja2
{%- if is_scenario_all_hss_support and ADD_MMERESELPLCY -%}
    {%- for item in set_dmcmpt_list -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 本网所有的HSS支持此特性，外网所有HSS不支持此特性：

```jinja2
{%- if is_scenario_home_hss_support_only and ADD_MMERESELPLCY -%}
    {%- for item in add_dmcmptbyimsi_list -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_home_hss_support_only and ADD_MMERESELPLCY -%}
    {%- for item in set_dmcmpt_list_1 -%}
        SET DMCMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 仅46123和46321为IMSI前缀的用户注册的HSS支持此特性：

```jinja2
{%- if is_scenario_specific_imsi_prefix_hss and ADD_MMERESELPLCY -%}
    {%- for item in add_dmcmptbyimsi_list_1 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.4 查询系统中Diameter兼容性配置

#### 命令**ADD DMCMPTBYIMSI**与**SET DMCMPT**中除“用户范围”、“运营商标识”以及“IMSI前缀”外的其余参数功能均相同，且若系统中同时存在这两条命令的配置，系统会优先匹配命令**ADD DMCMPTBYIMSI**的配置。因此在配置**ADD DMCMPTBYIMSI**前需先执行**LST DMCMPT**查询系统中**SET DMCMPT**的配置记录，确保命令**ADD DMCMPTBYIMSI**的配置记录中所携带的参数默认值不影响系统已有配置。

#### 6.5 本网用户

```jinja2
{%- if is_scenario_home_user and ADD_MMERESELPLCY -%}
    {%- for item in add_dmcmptbyimsi_list_3 -%}
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.6 外网用户

```jinja2
{%- if is_scenario_foreign_user and ADD_MMERESELPLCY -%}
    {%- for item in add_dmcmptbyimsi_list_5 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.7 特定IMSI前缀的用户

```jinja2
{%- if is_scenario_specific_imsi_prefix_user and ADD_MMERESELPLCY -%}
    {%- for item in add_dmcmptbyimsi_list_6 -%}
        ADD DMCMPTBYIMSI:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SF2 is not none -%}
            SF2={{item.SF2}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 8 **可选：**配置专网用户迁移。需要将本MME的用户快速归属到各自DCN中时，执行此步骤。

```jinja2
{%- if is_optional_private_network_user_migration -%}
    {%- for item in str_dcnoffload_list -%}
        STR DCNOFFLOAD:
        {#- --- 可选参数 --- -#}
        {%- if item.OFFLOADTYPE is not none -%}
            OFFLOADTYPE={{item.OFFLOADTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

