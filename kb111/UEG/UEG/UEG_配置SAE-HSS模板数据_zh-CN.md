---
id: ''
name: 配置SAE-HSS模板数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS模板数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","SAE-HSS用户数据配置","配置SAE-HSS模板数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS模板数据的配置。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成SAE-HSS的用户数据规划。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          maxLength: 63
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        APNOI:
          name: 'APN运营商标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_optgprstpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '与**ADD APNTPL**命令中的“模板ID”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '与**ADD EPSQOSTPL**命令中的“模板ID”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDN网络'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        IW5GSINDICATOR:
          name: '是否签约5GS互操作'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_plmntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRULE:
          name: '缺省漫游限制状态'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网络码'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        ISLOCAL:
          name: '是否本地PLMN'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        RULE:
          name: '漫游限制状态'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        LBO:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
    add_diamrrtpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTRULE:
          name: '缺省漫游限制状态'
          type: string
          enum:
          - PERMISSION
          - RESTRICT
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        DIAMIDENTITYTYPE:
          name: 'Diameter身份标识类型'
          type: string
          enum:
          - HOSTNAME
          - REALMNAME
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: HOSTNAME
        DIAMIDENTITY:
          name: 'Diameter身份标识'
          type: string
          minLength: 1
          maxLength: 127
          required: true
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        RULE:
          name: '漫游限制状态'
          type: string
          enum:
          - PERMISSION
          - RESTRICT
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: PERMISSION
  examples:
    add_apntpl_list:
    - HLRSN: 1
      TPLID: 30
      APN: 'abc.com'
      APNOI: 'APN1.EPC.MNC21.MCC460.3GPPNETWORK.ORG'
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '40'
      QOSCLASUID: '6'
      PRILEVEL: '1'
      AMBRMAXREQBWUL: '10000000'
      AMBRMAXREQBWDL: '20000000'
    add_optgprstpl_list:
    - HLRSN: '1'
      TPLID: '50'
      APN_TYPE: EPS_APN
      APNTPLID: '30'
      EPS_QOSTPLID: '40'
      PDPTYPE: IPV4
      VPLMN: TRUE
      CHARGE: HOT
      IW5GSINDICATOR: SUBSCRIBED
    add_plmntpl_list:
    - HLRSN: '1'
      TPLID: '60'
      DEFAULTRULE: PERMISSION
      MCC: '460'
      MNC: '03'
      ISLOCAL: TRUE
      RULE: PERMISSION
      LBO: PERMIT
    add_diamrrtpl_list:
    - HLRSN: 1
      TPLID: 70
      DEFAULTRULE: PERMISSION
      DIAMIDENTITYTYPE: HOSTNAME
      DIAMIDENTITY: 'test.huawei.com'
      RULE: PERMISSION
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD APNTPL**命令，增加APN模板。

```jinja2
{%- for item in add_apntpl_list -%}
    ADD APNTPL:
    {#- --- 必选参数 --- -#}
    TPLID={{item.TPLID}},
    HLRSN={{item.HLRSN}},
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.APNOI is not none -%}
        APNOI="{{item.APNOI}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 参数“接入点名称”必须设置。

### 3 执行**ADD EPSQOSTPL**命令，增加EPS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=3 -->
```

### 参数“QoS分类ID”和“分配/保留优先级数据”必须同时存在，取值越小，优先级越高。

### 4 执行**ADD OPTGPRSTPL**命令，增加优化GPRS/EPS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_optgprstpl_list的变量区（command: ADD OPTGPRSTPL） -#}
<!-- MISSING_MACRO: command=ADD OPTGPRSTPL list_name=add_optgprstpl_list step_id=4 -->
```

### 使用**ADD OPTGPRSTPL**命令增加优化GPRS/EPS模板，只能增加一条PDP/PDN上下文，如果用户需要签约多条PDP/PDN上下文，请使用**MOD OPTGPRSTPL**命令。

### 参数“APN类型”设置为“EPS\_APN”，表示该APN只能接入EPS域，配套Diameter信令配置。

### 5 执行**ADD PLMNTPL**命令，增加PLMN区域漫游模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_plmntpl_list的变量区（command: ADD PLMNTPL） -#}
<!-- MISSING_MACRO: command=ADD PLMNTPL list_name=add_plmntpl_list step_id=5 -->
```

### 参数“缺省漫游限制状态”设置为“PERMISSION”，当前的PLMN在模板中匹配不上时，允许用户漫游。

### 参数“是否本地PLMN”设置为“TRUE”，表示模板中添加的PLMN为本地PLMN，否则为非本地PLMN。

### 参数“移动国家码”和“移动网络码”为必须输入的参数。

### 6 执行**ADD DIAMRRTPL**命令，增加Diameter漫游限制模板。

```jinja2
{%- for item in add_diamrrtpl_list -%}
    ADD DIAMRRTPL:
    {#- --- 必选参数 --- -#}
    DEFAULTRULE={{item.DEFAULTRULE}},
    HLRSN={{item.HLRSN}},
    DIAMIDENTITY="{{item.DIAMIDENTITY}}",
    TPLID={{item.TPLID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DIAMIDENTITYTYPE is not none -%}
        DIAMIDENTITYTYPE={{item.DIAMIDENTITYTYPE}},
    {%- endif -%}
    {%- if item.RULE is not none -%}
        RULE={{item.RULE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 为了保证新增的Diameter漫游限制模板数据不重复，请先使用**LST DIAMRRTPL**命令来查询已有的Diameter漫游限制模板，以免新增数据和已有数据重复。

### 每个模板最多可以包含256个DIAMIDENTITY记录。

