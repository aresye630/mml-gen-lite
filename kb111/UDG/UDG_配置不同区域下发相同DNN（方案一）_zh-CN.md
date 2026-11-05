---
id: ''
name: 配置不同区域下发相同DNN（方案一）
ne_type: UDG
type: feature
description: 该任务旨在指导操作人员在5G网络中配置不同区域下发相同DNN，配置独立开户模板。  * 运营商大网SMF POOL业务均质，POOL中所有SMF作为智能分流SMF时，UDM使用此章节方式进行配置。 * 如果现网已配置5G用户数据，无需执行此章节的步骤。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UDM","配置5G用户签约","配置不同区域下发相同DNN（方案一）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在5G网络中配置不同区域下发相同DNN，配置独立开户模板。* 运营商大网SMF POOL业务均质，POOL中所有SMF作为智能分流SMF时，UDM使用此章节方式进行配置。* 如果现网已配置5G用户数据，无需执行此章节的步骤。

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
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '本端规划'
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
        NGQI:
          name: '5QI'
          type: string
          required: false
          description: '用于标识5G QoS特性的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
          type: string
          required: false
          description: '用于标识用户在网络资源拥塞时的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dnnqostpl_list:
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
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          required: false
          description: '用于标识默认PDU会话类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          required: false
          description: '用于标识默认会话和业务连续性模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          required: false
          description: '用于标识其它允许的会话和业务连续性模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: '是否签约EPS互操作'
          type: string
          required: false
          description: '用于标识是否签约EPS互操作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LADN:
          name: '是否为LADN'
          type: string
          required: false
          description: '用于标识是否支持本地数据网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LBO:
          name: '是否允许Local Break Out'
          type: string
          required: false
          description: '用于标识漫游场景下是否允许使用漫游地网关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: string
          required: false
          description: '用于标识5GC QoS模板ID。该参数必须先由**ADD NGCQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: string
          required: false
          description: '用于标识DNN级别上行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          required: false
          description: '用于标识DNN级别上行速率单位的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: string
          required: false
          description: '用于标识DNN级别下行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          required: false
          description: '用于标识DNN级别下行速率单位的参数。'
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
        UPINTEGR:
          name: '用户面完整性保护策略'
          type: string
          required: false
          description: '用于标识用户面完整性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPCONFID:
          name: '用户面机密性保护策略'
          type: string
          required: false
          description: '用于标识用户面机密性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDARYAUTH:
          name: '是否需要二次认证授权'
          type: string
          required: false
          description: '用于标识SMF在用户PDU会话建立时是否需要二次认证授权。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AAAIPALLOCATION:
          name: 'PDU会话建立是否需要SMF向DN-AAA请求UE的IP地址'
          type: string
          required: false
          description: '用于标识PDU会话建立流程中SMF是否需要向DN-AAA请求UE的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SAMESMFIND:
          name: '到相同DNN和S-NSSAI的多个PDU会话是否需要相同的SMF'
          type: string
          required: false
          description: '用于标识到相同DNN和S-NSSAI的多个PDU会话是否要求SMF相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smdatatpl_list:
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
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFSNSSAI:
          name: '是否默认S-NSSAI'
          type: string
          required: false
          description: '用于标识签约的S-NSSAI数据是否为默认S-NSSAI数据。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQOS模板ID'
          type: string
          required: false
          description: '用于标识用户待签约的5GS DNNQoS模板ID。该参数必须由**ADD DNNQOSTPL**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_smdatatpl_list:
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
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '用于标识修改5G会话信息模板的操作类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQOS模板ID'
          type: string
          required: false
          description: '用于标识5GS DNNQOS模板ID。该参数必须由**ADD DNNQOSTPL**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否为默认DNN'
          type: string
          required: false
          description: '用于标识签约的DNN数据是否为默认DNN数据。'
          data_source: '固定配置'
          pattern: ''
          default: ''
    add_ngsusertpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '已配置数据中获取  用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '本端规划'
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
          description: '用于标识5GS用户模板在系统中的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'UE级别上行速率'
          type: string
          required: false
          description: '用于标识UE级别上行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'UE级别上行速率单位'
          type: string
          required: false
          description: '用于标识“UE级别上行速率”的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'UE级别下行速率'
          type: string
          required: false
          description: '用于标识UE级别下行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'UE级别下行速率单位'
          type: string
          required: false
          description: '用于标识“UE级别下行速率”的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RFSPINDEX:
          name: '无线频率选择优先级'
          type: string
          required: false
          description: '用于标识无线频率选择优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBSREGTIMER:
          name: '周期注册定时器'
          type: string
          required: false
          description: '用于标识周期注册定时器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MPS:
          name: '是否支持多媒体优先级服务'
          type: string
          required: false
          description: '用于标识是否提供多媒体优先级服务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACTIVETIME:
          name: '激活时间定时器'
          type: string
          required: false
          description: '用于标识UE在PSM模式开启时，从进入IDLE态开始到进入PSM态的定时器时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DLBUFFERIND:
          name: '提供签约高延迟通信时的下行缓存大小'
          type: string
          required: false
          description: '用于标识当签约高延迟通信时，是否提供下行缓存的大小。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: '用于标识鉴权方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MICOALLOWED:
          name: '是否支持MICO模式'
          type: string
          required: false
          description: '用于标识是否支持MICO模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCS:
          name: '是否支持关键任务优先级服务'
          type: string
          required: false
          description: '用于标识是否提供关键任务优先级服务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMDATATPLID:
          name: '会话信息模板ID'
          type: string
          required: false
          description: '用于标识会话信息模板ID。该参数必须先由**ADD SMDATATPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SMSSUBSCRIBED:
          name: '是否允许SMS over NAS'
          type: string
          required: false
          description: '用于标识是否允许使用5G NAS短消息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tplngs_list:
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
        NGSUSERTPLID:
          name: '5GS用户数据模板'
          type: string
          required: false
          description: '用于标识5GS用户数据模板号。该参数必须先由**ADD NGSUSERTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_tplngs_list:
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
        NGSUSERTPLID:
          name: '5GS用户数据模板'
          type: string
          required: false
          description: '用于标识5GS用户数据模板号。该参数必须先由**ADD NGSUSERTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: '1'
      TPLID: '5'
      NGQI: '1'
      ARPPRILEVEL: '1'
    add_dnnqostpl_list:
    - HLRSN: '1'
      TPLID: '5'
      PDUTYPE: IPV4
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2&SSC_MODE_3
      IWKEPSIND: TRUE
      LADN: FALSE
      LBO: FALSE
      NGCQOSTPLID: '5'
      AMBRUP: '104857600'
      UPUNIT: bps
      AMBRDW: '1073741824'
      DWUNIT: bps
      CHARGE: '0400'
      UPINTEGR: NOT_NEEDED
      UPCONFID: NOT_NEEDED
      SECONDARYAUTH: ABSENT
      AAAIPALLOCATION: ABSENT
      SAMESMFIND: ABSENT
    add_smdatatpl_list:
    - HLRSN: '1'
      TPLID: '5'
      SNSSAI: 1-000000
      DEFSNSSAI: TRUE
      DNN: common.dnn
      DNNQOSTPLID: '5'
    mod_smdatatpl_list:
    - HLRSN: '1'
      TPLID: '5'
      SNSSAI: 1-000000
      PROV: ADD_DNN
      DNN: stjwt.gd
      DNNQOSTPLID: '6'
      DEFAULT: FALSE
    add_ngsusertpl_list:
    - HLRSN: '1'
      TPLID: '6'
      TPLNAME: 5G开通
      AMBRUP: '150'
      UPUNIT: Mbps
      AMBRDW: '2'
      DWUNIT: Gbps
      RFSPINDEX: '0'
      SUBSREGTIMER: '0'
      MPS: FALSE
      ACTIVETIME: '0'
      DLBUFFERIND: NOT_REQUESTED
      AUTHTYPE: 5G-AKA
      MICOALLOWED: FALSE
      MCS: FALSE
      SMDATATPLID: '5'
      SMSSUBSCRIBED: FALSE
    add_tplngs_list:
    - IMSI: '46100000912345'
      NGSUSERTPLID: '6'
    mod_tplngs_list:
    - IMSI: '46100000912345'
      NGSUSERTPLID: '6'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD NGCQOSTPL**命令增加5GS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcqostpl_list的变量区（command: ADD NGCQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD NGCQOSTPL list_name=add_ngcqostpl_list step_id=2 -->
```

### 3 执行**ADD DNNQOSTPL**命令增加5GS DNN QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dnnqostpl_list的变量区（command: ADD DNNQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD DNNQOSTPL list_name=add_dnnqostpl_list step_id=3 -->
```

### 4 执行**ADD SMDATATPL**和**MOD SMDATATPL**命令配置5G SMDATA模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdatatpl_list的变量区（command: ADD SMDATATPL） -#}
<!-- MISSING_MACRO: command=ADD SMDATATPL list_name=add_smdatatpl_list step_id=4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_smdatatpl_list的变量区（command: MOD SMDATATPL） -#}
<!-- MISSING_MACRO: command=MOD SMDATATPL list_name=mod_smdatatpl_list step_id=4 -->
```

### 5 执行**ADD NGSUSERTPL**命令增加5GS用户模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngsusertpl_list的变量区（command: ADD NGSUSERTPL） -#}
<!-- MISSING_MACRO: command=ADD NGSUSERTPL list_name=add_ngsusertpl_list step_id=5 -->
```

### 6 给用户签约会话管理数据。

#### 6.1 对于新用户，需要开户后再执行**ADD TPLNGS**命令签约5G数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tplngs_list的变量区（command: ADD TPLNGS） -#}
<!-- MISSING_MACRO: command=ADD TPLNGS list_name=add_tplngs_list step_id=6.1 -->
```

#### 6.2 如果用户已签约5G数据且在网，则使用**MOD TPLNGS**命令签约。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_tplngs_list的变量区（command: MOD TPLNGS） -#}
<!-- MISSING_MACRO: command=MOD TPLNGS list_name=mod_tplngs_list step_id=6.2 -->
```

