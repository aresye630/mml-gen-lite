---
id: ''
name: 配置SMF与NCG/CHF(OCS)交互的条件和内容
ne_type: UDG
type: feature
description: 本指导描述在UNC上配置与NCG/CHF(OCS)交互的条件及内容的相关操作过程。配置SMF与NCG/CHF(OCS)交互的条件及内容，即配置：  * 用户激活时是否需要到NCG/CHF(OCS)交互。 * SMF在什么情况下向NCG/CHF(OCS)发送ChargingDataRequest消息。 * SMF向NCG/CHF(OCS)发送ChargingDataRequest消息时携带预申请配额的RG。  ChargingDataRequest触发条件可以由NCG/CHF(OCS)在ChargingDataResponse消息中携带，也可以在SMF上本地配置。NCG/CHF(OCS)下发的优先级比SMF本地配置的高。  ChargingDataRequest有多种触发场景，融合计费过程中，当其中任一个触发条件满足时，都会触发ChargingDataRequest上报。  为了避免SMF和NCG/CHF(OCS)频繁交互所带来的高负荷对网络和网元造成影响，建议保证每个用户上报Charging Data Request的间隔大于30秒。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案三：部署NCG且基于服务化接口的纯离线计费组网方案（N40接口）","SMF配置","融合计费模板及交互配置（N40接口）","配置SMF与NCG/CHF(OCS)交互的条件和内容"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述在UNC上配置与NCG/CHF(OCS)交互的条件及内容的相关操作过程。配置SMF与NCG/CHF(OCS)交互的条件及内容，即配置：* 用户激活时是否需要到NCG/CHF(OCS)交互。* SMF在什么情况下向NCG/CHF(OCS)发送ChargingDataRequest消息。* SMF向NCG/CHF(OCS)发送ChargingDataRequest消息时携带预申请配额的RG。ChargingDataRequest触发条件可以由NCG/CHF(OCS)在ChargingDataResponse消息中携带，也可以在SMF上本地配置。NCG/CHF(OCS)下发的优先级比SMF本地配置的高。ChargingDataRequest有多种触发场景，融合计费过程中，当其中任一个触发条件满足时，都会触发ChargingDataRequest上报。为了避免SMF和NCG/CHF(OCS)频繁交互所带来的高负荷对网络和网元造成影响，建议保证每个用户上报Charging Data Request的间隔大于30秒。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
* 已完成融合数据模板、User Profile创建，已配置融合计费费率标识。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chfinit_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '配置建立PDU会话时是否发送ChargingDataRqueset与NCG/CHF(OCS)交互。  如果需要为全局融合计费模板配置与NCG/CHF(OCS)交互参数，则“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CHFINIT:
          name: 'CHF交互使能开关'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '初始RG个数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAITCHFRESP:
          name: 'CHF交互等待CHF响应开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGSOURCE:
          name: 'RG来源'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ctxstartrating_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '使用**ADD USERPROFILE**命令定义的“USERPROFILENAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CTXRURRGRPNAME1:
          name: '初始请求URR组名称1'
          type: string
          required: false
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pdutrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '配置Session级Trigger。如果需要为全局融合计费模板配置Session级Trigger，则使用**MOD PDUTRIGGER**命令，“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCHG:
          name: '用户位置更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRACHG:
          name: '区域用户位置上报更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSDATAOFFCHG:
          name: 'PS数据关闭状态更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UETZCHG:
          name: '用户时区更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNCHG:
          name: 'PLMN更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATCHG:
          name: 'RAT更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDUPF:
          name: '添加UPF'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMELIMIT:
          name: '时间阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTLIMIT:
          name: '事件阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXNUMCCC:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UCITIMER:
          name: '业务停止时长'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INSERTISMF:
          name: '插入ISMF'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOVALISMF:
          name: '删除ISMF'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHANGEISMF:
          name: '更新ISMF'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSAMBRCHG:
          name: 'Session AMBR更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVPLMNRTCTCHG:
          name: '服务PLMN速率控制更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECTRLCHG:
          name: 'APN速率控制更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGISAICHG:
          name: 'CGISAI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAICHG:
          name: 'RAI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAICHG:
          name: '跟踪区标识更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rgtrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          required: false
          description: '配置RG级Trigger。  如果需要为全局融合计费模板配置RG级Trigger，则使用**MOD RGTRIGGER**命令，“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCHG:
          name: '用户位置更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRACHG:
          name: '区域用户位置上报更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSDATAOFFCHG:
          name: 'PS数据关闭状态更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UETZCHG:
          name: '用户时区更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNCHG:
          name: 'PLMN更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATCHG:
          name: 'RAT更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMELIMIT:
          name: '时间阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTLIMIT:
          name: '事件阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTATHRESHOLD:
          name: '配额阈值'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VT:
          name: '配额有效时长'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QHT:
          name: '配额保持时长'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVPLMNRTCTCHG:
          name: '服务PLMN速率控制更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECTRLCHG:
          name: 'APN速率控制更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAICHG:
          name: '跟踪区标识更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_rgresctrl_list:
      type: items
      properties:
        ONLRGAGESW:
          name: '在线计费RG老化控制'
          type: string
          required: false
          description: '控制在线计费RG老化功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLAGETIMER:
          name: '在线计费RG老化时长 (分)'
          type: string
          required: false
          description: '控制在线计费RG老化时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLBLKTIMER:
          name: '在线计费全局业务阻塞处理时间间隔 (分)'
          type: string
          required: false
          description: '配置全局业务阻塞或重定向的时长，从阻塞或重定向开始经过这段时间以后，进行RG老化。  当配置为0时，表示阻塞时长无效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFLRGAGESW:
          name: '离线计费RG老化控制'
          type: string
          required: false
          description: '控制离线计费RG老化功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFLAGETIMER:
          name: '离线计费RG老化时长 (分)'
          type: string
          required: false
          description: '控制离线计费RG老化时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXCSRVLMTACT:
          name: '超出业务最大规格处理动作'
          type: string
          required: false
          description: '控制新业务上报时，RG超过最大规格时SMF的处理方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_n40msgctrl_list:
      type: items
      properties:
        ROAMOFFSTARTSW:
          name: '国际漫游场景更新流程中仅离线新业务预申请上报CHF开关'
          type: string
          required: false
          description: '设置N40接口消息的控制参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFID23G:
          name: 'GERAN/UTRAN接入场景携带UPFID'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRAINFO23G:
          name: 'GERAN/UTRAN接入场景携带Presence Reporting Area Information'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SLICINGINFO23G:
          name: 'GERAN/UTRAN接入场景携带Network Slicing Information'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE23G:
          name: 'GERAN/UTRAN接入场景携带SSC Mode'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNSELMODE23G:
          name: 'GERAN/UTRAN接入场景携带DNN Selection Mode'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STOPINDICTR23G:
          name: 'GERAN/UTRAN接入场景携带Session Stop Indicator'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UCITIMER23G:
          name: 'GERAN/UTRAN接入场景携带Unit Count Inactivity Timer'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FINALREPORT:
          name: '去活消息中usedUnitContainer中triggerType支持填写FINAL'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_chfinit_list:
    - CCTMPLTNAME: cct_test
      CHFINIT: SENDREQ
      CCRINITRGNUM: '5'
      WAITCHFRESP: ENABLE
      RGSOURCE: DEFAULT
    set_ctxstartrating_list:
    - USERPROFILENAME: up_test
      CTXRURRGRPNAME1: urrgroup_test
    add_pdutrigger_list:
    - CCTMPLTNAME: cct-test
      QOSCHG: DEFERRED
      ULCHG: DEFERRED
      SRVNDCHG: DEFERRED
      PRACHG: DEFERRED
      PSDATAOFFCHG: DEFERRED
      UETZCHG: IMMEDIATE
      PLMNCHG: IMMEDIATE
      RATCHG: IMMEDIATE
      ADDUPF: IMMEDIATE
      TIMELIMIT: IMMEDIATE
      VOLUMELIMIT: IMMEDIATE
      EVENTLIMIT: IMMEDIATE
      MAXNUMCCC: IMMEDIATE
      UCITIMER: IMMEDIATE
      INSERTISMF: NONREPORT
      REMOVALISMF: NONREPORT
      CHANGEISMF: NONREPORT
      SESSAMBRCHG: IMMEDIATE
      SERVPLMNRTCTCHG: DEFERRED
      APNRATECTRLCHG: DEFERRED
      CGISAICHG: DEFERRED
      RAICHG: DEFERRED
      TAICHG: NONREPORT
    add_rgtrigger_list:
    - CCTMPLTNAME: cct_test
      QOSCHG: DEFERRED
      ULCHG: DEFERRED
      SRVNDCHG: DEFERRED
      PRACHG: DEFERRED
      PSDATAOFFCHG: DEFERRED
      UETZCHG: IMMEDIATE
      PLMNCHG: IMMEDIATE
      RATCHG: IMMEDIATE
      TIMELIMIT: DEFERRED
      VOLUMELIMIT: DEFERRED
      EVENTLIMIT: DEFERRED
      QUOTATHRESHOLD: IMMEDIATE
      VT: IMMEDIATE
      QHT: IMMEDIATE
      SERVPLMNRTCTCHG: DEFERRED
      APNRATECTRLCHG: DEFERRED
      TAICHG: NONREPORT
    set_rgresctrl_list:
    - ONLRGAGESW: ENABLE
      ONLAGETIMER: '20'
      ONLBLKTIMER: '0'
      OFLRGAGESW: ENABLE
      OFLAGETIMER: '20'
      EXCSRVLMTACT: BLOCK
    set_n40msgctrl_list:
    - ROAMOFFSTARTSW: DISABLE
      UPFID23G: ENABLE
      PRAINFO23G: ENABLE
      SLICINGINFO23G: ENABLE
      SSCMODE23G: ENABLE
      DNNSELMODE23G: ENABLE
      STOPINDICTR23G: ENABLE
      UCITIMER23G: ENABLE
      FINALREPORT: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **可选：**配置建立PDU会话时是否发送ChargingDataRequest与NCG/CHF(OCS)交互。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_chfinit_list的变量区（command: SET CHFINIT） -#}
<!-- MISSING_MACRO: command=SET CHFINIT list_name=set_chfinit_list step_id=1 -->
```

### 2 **可选：**配置SMF在建立计费会话的ChargingDataRequest中携带的为哪些RG申请预配额。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ctxstartrating_list的变量区（command: SET CTXSTARTRATING） -#}
<!-- MISSING_MACRO: command=SET CTXSTARTRATING list_name=set_ctxstartrating_list step_id=2 -->
```

### 3 **可选：**配置Session级/RG级Trigger。

#### 3.1 配置Session级Trigger。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pdutrigger_list的变量区（command: ADD PDUTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD PDUTRIGGER list_name=add_pdutrigger_list step_id=3.1 -->
```

#### 3.2 配置RG级Trigger。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rgtrigger_list的变量区（command: ADD RGTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD RGTRIGGER list_name=add_rgtrigger_list step_id=3.2 -->
```

### 4 配置RG老化功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_rgresctrl_list的变量区（command: SET RGRESCTRL） -#}
<!-- MISSING_MACRO: command=SET RGRESCTRL list_name=set_rgresctrl_list step_id=4 -->
```

### 终端用户访问业务匹配到某个RG后，即使后续不再访问该业务，用户更新或时间流量阈值等场景触发向NCG/CHF(OCS)上报用量时，会上报该RG的用量且用量为零，用户长时间在线会造成N40接口的消息变大，同时造成RG及URR等资源浪费。QHT功能可以删除已停止访问业务的RG，但该功能依赖于NCG/CHF(OCS)配合下发QHT Trigger。通过****SET RGRESCTRL****命令配置RG老化时长，可以保证在QHT功能不使能或QHT使能但QHT值为0场景下，保证已停止访问业务的RG老化，携带Trigger类型为Final，避免大量RG在线造成消息过大。

### 5 设置N40接口消息的控制参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_n40msgctrl_list的变量区（command: SET N40MSGCTRL） -#}
<!-- MISSING_MACRO: command=SET N40MSGCTRL list_name=set_n40msgctrl_list step_id=5 -->
```

