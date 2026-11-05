---
id: ''
name: 配置不同区域下发相同APN（方案一）
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员在4G网络中配置不同区域下发相同APN，配置独立开户模板。  * 运营商大网SMF POOL业务均质，POOL中所有SMF作为智能分流SMF时，UDM使用此章节方式进行配置。 * 如果现网已配置4G用户数据，无需执行此章节的步骤。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UDM","配置4G用户签约","配置不同区域下发相同APN（方案一）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在4G网络中配置不同区域下发相同APN，配置独立开户模板。* 运营商大网SMF POOL业务均质，POOL中所有SMF作为智能分流SMF时，UDM使用此章节方式进行配置。* 如果现网已配置4G用户数据，无需执行此章节的步骤。

## 必备事项
前提条件

* 已完成园区专网UDM的基础配置并与周边网元完成对接。

* 操作人员具有PGW Web LMT客户端业务发放权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          required: false
          description: '用于标识接入点名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNGWALLOCTYPE:
          name: 'PDN GW地址分配类型'
          type: string
          required: false
          description: '用于标识PDN GW地址分配类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NONIPDATADELMECH:
          name: 'Non-IP传输模式'
          type: string
          required: false
          description: '用于标识Non-IP PDN类型的APN数据传输给MME时的传输模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '用于标识QoS分类ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTQCI:
          name: '扩展QoS分类ID'
          type: string
          required: false
          description: '用于标识扩展QoS分类ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: '用于标识用户在网络资源拥塞时的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '业务数据流是否能够占有能力'
          type: string
          required: false
          description: '用于标识是否允许该业务数据流占有优先级相对较低的业务数据流的资源。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '业务数据流是否能够被占有'
          type: string
          required: false
          description: '用于标识是否允许该业务数据流丢失分配给它的资源，用于接纳一个优先级相对较高的业务数据流。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: '用于标识4G网络最大请求上行带宽，即发送消息的最大带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: '用于标识4G网络最大请求下行带宽，即接受消息的最大带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_optgprstpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待修改模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: '用于标识APN类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '用于标识APN模板ID。该参数必须先由**ADD APNTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTCFGFLAG:
          name: '是否是默认APN'
          type: string
          required: false
          description: '用于标识是否将“APN模板ID”对应的APN模板设置为EPS APN的默认APN模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '用于标识EPS QoS模板ID。该参数必须先由**ADD EPSQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '用于标识数据业务的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '用于标识是否允许用户从VPLMN访问PDP/PDN网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '用于标识计费特性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IW5GSINDICATOR:
          name: '是否签约5GS互操作'
          type: string
          required: false
          description: '用于标识用户是否签约5GS互操作业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_optgprstpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待修改模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '用于新增、修改和删除用户PDP/PDN上下文。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: '用于标识APN类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '用于标识APN模板ID。该参数必须先由**ADD APNTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTCFGFLAG:
          name: '是否是默认APN'
          type: string
          required: false
          description: '用于标识是否将“APN模板ID”对应的APN模板设置为EPS APN的默认APN模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '用于标识EPS QoS模板ID。该参数必须先由**ADD EPSQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '用于标识数据业务的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '用于标识是否允许用户从VPLMN访问PDP/PDN网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '用于标识计费特性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IW5GSINDICATOR:
          name: '是否签约5GS互操作'
          type: string
          required: false
          description: '用于标识用户是否签约5GS互操作业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_tploptgprs_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供优化GPRS业务'
          type: string
          required: false
          description: '用于标识是否提供优化GPRS/EPS业务。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TPLID:
          name: '优化GPRS模板ID'
          type: string
          required: false
          description: '用于标识优化GPRS模板ID。该参数必须先由**ADD OPTGPRSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DELOLD:
          name: '是否删除已有的APN'
          type: string
          required: false
          description: '用于标识是否删除已有的APN。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_apntpl_list:
    - HLRSN: '1'
      TPLID: '111'
      TPLNAME: APN
      APN: common.dnn
      PDNGWALLOCTYPE: DYNAMIC
      NONIPDATADELMECH: SGi_BASED_DATA_DELIVERY
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '111'
      TPLNAME: EPSQOS
      QOSCLASUID: '9'
      EXTQCI: '130'
      PRILEVEL: '6'
      PREEMPTIONCAP: DISABLE
      PREEMPTIONVUL: ENABLE
      AMBRMAXREQBWUL: '104857600'
      AMBRMAXREQBWDL: '1073741824'
    add_optgprstpl_list:
    - HLRSN: '1'
      TPLID: '50'
      TPLNAME: OPTGPRSTPL
      APN_TYPE: EPS_APN
      APNTPLID: '111'
      DEFAULTCFGFLAG: TRUE
      EPS_QOSTPLID: '111'
      PDPTYPE: IPV4_OR_IPV6
      VPLMN: TRUE
      CHARGE: NORMAL
      IW5GSINDICATOR: SUBSCRIBED
    mod_optgprstpl_list:
    - HLRSN: '1'
      TPLID: '50'
      PROV: ADDPDPCNTX
      APN_TYPE: EPS_APN
      APNTPLID: '112'
      DEFAULTCFGFLAG: FALSE
      EPS_QOSTPLID: '111'
      PDPTYPE: IPV4_OR_IPV6
      VPLMN: TRUE
      CHARGE: NORMAL
      IW5GSINDICATOR: NOT-SUBSCRIBED
    mod_tploptgprs_list:
    - IMSI: '46100000912345'
      PROV: TRUE
      TPLID: '50'
      DELOLD: FALSE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM业务管理”窗口。

### /\*登录“UDM业务管理”窗口\*/

### 2 执行**ADD APNTPL**命令增加APN模板。

### /\*配置APN模板\*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apntpl_list的变量区（command: ADD APNTPL） -#}
<!-- MISSING_MACRO: command=ADD APNTPL list_name=add_apntpl_list step_id=2 -->
```

### 3 执行**ADD EPSQOSTPL**命令增加EPS QoS模板。

### /\*配置EPS QoS模板\*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=3 -->
```

### 4 执行**ADD OPTGPRSTPL**和**MOD OPTGPRSTPL**命令配置优化GPRS/EPS模板。

### /\*配置优化GPRS/EPS模板\*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_optgprstpl_list的变量区（command: ADD OPTGPRSTPL） -#}
<!-- MISSING_MACRO: command=ADD OPTGPRSTPL list_name=add_optgprstpl_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_optgprstpl_list的变量区（command: MOD OPTGPRSTPL） -#}
<!-- MISSING_MACRO: command=MOD OPTGPRSTPL list_name=mod_optgprstpl_list step_id=4 -->
```

### 5 执行**MOD TPLOPTGPRS**命令给用户签约优化GPRS/EPS业务。

### /\*执行MOD TPLOPTGPRS命令配置模板签约用户的EPS业务，包括common.dnn和stjwt.gd两个APN，其中默认APN为common.dnn\*/

### /\*对于新用户，需要先开户再执行该命令\*/

### /\*如果用户已开户，直接执行该命令，执行该命令UDM会下发IDR消息\*/

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_tploptgprs_list的变量区（command: MOD TPLOPTGPRS） -#}
<!-- MISSING_MACRO: command=MOD TPLOPTGPRS list_name=mod_tploptgprs_list step_id=5 -->
```

