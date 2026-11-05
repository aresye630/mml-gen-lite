---
id: GWFD-024901
name: 配置LTE移动性管理
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员通过PGW Web LMT签约或去签约LTE移动性管理。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-024900 HSS FE基本功能","GWFD-024901 LTE移动性管理","特性配置","配置LTE移动性管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员通过PGW Web LMT签约或去签约LTE移动性管理。

## 必备事项
前提条件

* 操作人员已完全了解LTE移动性管理。
* 操作人员具有业务发放权限。
* 操作人员具有PGW Web LMT的用户名和密码。
* 准备签约EPS APN数据的用户已经开户。
* 准备去签约EPS APN数据的用户已经签约LTE移动性管理。
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
          description: '该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '1'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '运营商统一规划。'
          data_source: '100'
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: 'abc.com'
          pattern: ''
          default: ''
        PDNGWALLOCTYPE:
          name: 'PDN GW地址分配类型'
          type: string
          enum:
          - STATIC
          - DYNAMIC
          required: false
          description: '* STATIC：静态。 * DYNAMIC：动态。   说明：  * 当该参数为“STATIC”时，“PDN GW 主机名称”、“PDN GW 域名名称”、“PDN GW IPV4地址”和“PDN GW IPV6地址”参数可见。 * 当该参数为“DYNAMIC”时，“PDN GW 主机名称”、“PDN GW 域名名称”、“PDN GW IPV4地址”和“PDN GW IPV6地址”参数不可见。'
          data_source: 'STATIC'
          pattern: ''
          default: DYNAMIC
        MIPHAHOST:
          name: 'PDN GW主机名称'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: '运营商统一规划。'
          data_source: 'PDN-GW'
          pattern: ''
          default: ''
        MIPHAREALM:
          name: 'PDN GW域名名称'
          type: string
          minLength: 1
          maxLength: 127
          required: false
          description: ''
          data_source: 'abc.com'
          pattern: ''
          default: ''
        MIPHAADDRIPV4:
          name: 'PDN GW IPV4地址'
          type: string
          required: false
          description: ''
          data_source: '10.144.98.135'
          pattern: ''
          default: ''
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD APNTPL**设置的“HLR序列号”保持一致。'
          data_source: '1'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '100'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: ''
          data_source: 'EPS-QoS'
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '“QoS分类ID”数值越小，QoS等级越高。'
          data_source: '5'
          pattern: ''
          default: ''
        EXTQCI:
          name: '扩展QoS分类ID'
          type: string
          required: false
          description: '“扩展QoS分类ID”数值越小，QoS等级越高。'
          data_source: '130'
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: '用来设置用户在网络资源拥塞时的优先级，数值越小，优先级越高。'
          data_source: '1'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '业务数据流是否能够占有能力'
          type: string
          required: false
          description: '表示是否允许该业务数据流占有优先级相对较低的业务数据流的资源。  * ENABLE：允许。 * DISABLE：禁止。'
          data_source: 'ENABLE'
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '业务数据流是否能够被占有'
          type: string
          required: false
          description: '表示是否允许该业务数据流丢失分配给它的资源，用于接纳一个优先级相对较高的业务数据流。   * ENABLE：允许。 * DISABLE：禁止。'
          data_source: 'ENABLE'
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: '表示发送消息的最大带宽。'
          data_source: '100000'
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: '表示接收消息的最大带宽。'
          data_source: '200000'
          pattern: ''
          default: ''
    mod_eps_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: 'IMSI号码。'
          data_source: '460000009123456'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供EPS业务'
          type: string
          required: false
          description: '提供还是撤销EPS业务。   * TRUE：提供。 * FALSE：撤销。'
          data_source: 'TRUE'
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: string
          required: false
          description: 'UE最大的上传速率。  条件必选参数，如果是第一次给用户签约EPS业务，该参数必须存在。'
          data_source: '500000'
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: string
          required: false
          description: 'UE最大的下载速率。  条件必选参数，如果是第一次给用户签约EPS业务，该参数必须存在。'
          data_source: '100000'
          pattern: ''
          default: ''
    mod_optgprs_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: 'IMSI号码。'
          data_source: '460000009123456'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '* ADDPDPCNTX：增加新PDP/PDN上下文。 * RMVPDPCNTX：删除用户PDP/PDN上下文。'
          data_source: 'ADDPDPCNTX'
          pattern: ''
          default: ''
        CNTXID:
          name: 'PDP/PDN上下文索引值'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '1'
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: 'EPS域APN。'
          data_source: 'EPS\_APN'
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '该参数必须先由**ADD APNTPL**命令定义，然后才能在此处引用。'
          data_source: '100'
          pattern: ''
          default: ''
        DEFAULTCFGFLAG:
          name: '是否是默认APN'
          type: string
          required: false
          description: '是否将“APNTPLID”对应的APN模板设置为EPS APN的默认APN模板。   * TRUE：默认APN。 * FALSE：非默认APN。   说明：  * 系统将第一个EPS APN自动设置为默认APN模板。 * 系统中必须存在且只能存在一个默认APN模板。 * “操作类型”为“MODPDPCNTX”时不能把默认APN模板修改为非默认APN模板。 * 不能把PS类型APN设置为默认APN模板。'
          data_source: 'TRUE'
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '该参数必须先由**ADD EPSQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '100'
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: 'IPV6'
          pattern: ''
          default: ''
        ADDIND:
          name: 'PDP/PDN地址标识'
          type: string
          required: false
          description: 'PDP/PDN地址的动态、静态类型指示。   * STATIC：静态 。 * DYNAMIC：动态。'
          data_source: 'STATIC'
          pattern: ''
          default: ''
        PDPADD:
          name: 'PDP/PDN地址'
          type: string
          required: false
          description: '当“PDP/PDN地址标识”为“STATIC”时该参数可见。'
          data_source: '2001:0DB8:0000:034B:0034:0006:FFFF:0001'
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '* TRUE：允许用户从VPLMN访问PDP/PDN网络。 * FALSE：不允许用户从VPLMN访问PDP/PDN网络，只允许从HPLMN访问PDP/PDN网络。'
          data_source: 'FALSE'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '普通计费特性。'
          data_source: 'NORMAL'
          pattern: ''
          default: ''
  examples:
    add_apntpl_list:
    - HLRSN: 1
      TPLID: 100
      APN: 'abc.com'
      PDNGWALLOCTYPE: STATIC
      MIPHAHOST: 'PDN-GW'
      MIPHAREALM: 'abc.com'
      MIPHAADDRIPV4: '10.144.98.135'
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '100'
      TPLNAME: EPS-QoS
      QOSCLASUID: '5'
      EXTQCI: '130'
      PRILEVEL: '1'
      PREEMPTIONCAP: ENABLE
      PREEMPTIONVUL: ENABLE
      AMBRMAXREQBWUL: '100000'
      AMBRMAXREQBWDL: '200000'
    mod_eps_list:
    - IMSI: '460000009123456'
      PROV: TRUE
      AMBRMAXUL: '500000'
      AMBRMAXDL: '100000'
    mod_optgprs_list:
    - IMSI: '460000009123456'
      PROV: ADDPDPCNTX
      CNTXID: '1'
      APN_TYPE: EPS_APN
      APNTPLID: '100'
      DEFAULTCFGFLAG: TRUE
      EPS_QOSTPLID: '100'
      PDPTYPE: IPV6
      ADDIND: STATIC
      PDPADD: 2001:0DB8:0000:034B:0034:0006:FFFF:0001
      VPLMN: FALSE
      CHARGE: NORMAL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD APNTPL**命令，增加APN模板。

```jinja2
{%- for item in add_apntpl_list -%}
    ADD APNTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNGWALLOCTYPE is not none -%}
        PDNGWALLOCTYPE={{item.PDNGWALLOCTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
    {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
        {%- if item.MIPHAHOST is not none -%}
            MIPHAHOST="{{item.MIPHAHOST}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
    {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
        {%- if item.MIPHAREALM is not none -%}
            MIPHAREALM="{{item.MIPHAREALM}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNGWALLOCTYPE=STATIC 时可选 --- -#}
    {%- if item.PDNGWALLOCTYPE == 'STATIC' -%}
        {%- if item.MIPHAADDRIPV4 is not none -%}
            MIPHAADDRIPV4="{{item.MIPHAADDRIPV4}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**ADD EPSQOSTPL**命令，增加EPS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=3 -->
```

### 4 执行**MOD EPS**命令，为用户签约/去签约LTE移动性管理。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_eps_list的变量区（command: MOD EPS） -#}
<!-- MISSING_MACRO: command=MOD EPS list_name=mod_eps_list step_id=4 -->
```

### 5 执行**MOD OPTGPRS**命令，为用户签约/去签约EPS APN数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_optgprs_list的变量区（command: MOD OPTGPRS） -#}
<!-- MISSING_MACRO: command=MOD OPTGPRS list_name=mod_optgprs_list step_id=5 -->
```

### 如果需要进行非连续用户的批操作，编写IMSIFILE或ISDNFILE批操作资源文件，并上传到PGW Server指定位置。

### ISDNFILE、IMSIFILE批操作资源文件的格式和上传位置请参见批操作管理。

### 批操作资源文件的上传方法请参见管理文件。

