---
id: ''
name: 配置SMF与NCG/CHF(OCS)交互的条件和内容
ne_type: UNC
type: feature
description: 本指导描述在UNC上配置与NCG/CHF(OCS)交互的条件及内容的相关操作过程。配置SMF与NCG/CHF(OCS)交互的条件及内容，即配置：  * 用户激活时是否需要到NCG/CHF(OCS)交互。 * SMF在什么情况下向NCG/CHF(OCS)发送ChargingDataRequest消息。 * SMF向NCG/CHF(OCS)发送ChargingDataRequest消息时携带预申请配额的RG。  ChargingDataRequest触发条件可以由NCG/CHF(OCS)在ChargingDataResponse消息中携带，也可以在SMF上本地配置。NCG/CHF(OCS)下发的优先级比SMF本地配置的高。  ChargingDataRequest有多种触发场景，融合计费过程中，当其中任一个触发条件满足时，都会触发ChargingDataRequest上报。  为了避免SMF和NCG/CHF(OCS)频繁交互所带来的高负荷对网络和网元造成影响，建议保证每个用户上报Charging Data Request的间隔大于30秒。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案四：部署NCG且基于服务化接口的离线+在线计费组网方案","SMF配置","融合计费模板及交互配置","配置SMF与NCG/CHF(OCS)交互的条件和内容"]
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
          minLength: 1
          maxLength: 63
          required: true
          description: '配置建立PDU会话时是否发送ChargingDataRqueset与NCG/CHF(OCS)交互。  如果需要为全局融合计费模板配置与NCG/CHF(OCS)交互参数，则“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CHFINIT:
          name: 'CHF交互使能开关'
          type: string
          enum:
          - SENDREQ
          - NOTSENDREQ
          - INITRGTRIGR
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCRINITRGNUM:
          name: '初始RG个数'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAITCHFRESP:
          name: 'CHF交互等待CHF响应开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RGSOURCE:
          name: 'RG来源'
          type: string
          enum:
          - DEFAULT
          - CTXSTARTRATING
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
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的“USERPROFILENAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CTXRURRGRPNAME1:
          name: '初始请求URR组名称1'
          type: string
          maxLength: 31
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
          minLength: 1
          maxLength: 63
          required: true
          description: '配置Session级Trigger。如果需要为全局融合计费模板配置Session级Trigger，则使用**MOD PDUTRIGGER**命令，“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DEFERRED
        ULCHG:
          name: '用户位置更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PRACHG:
          name: '区域用户位置上报更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PSDATAOFFCHG:
          name: 'PS数据关闭状态更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        UETZCHG:
          name: '用户时区更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        PLMNCHG:
          name: 'PLMN更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        RATCHG:
          name: 'RAT更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        ADDUPF:
          name: '添加UPF'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        TIMELIMIT:
          name: '时间阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        EVENTLIMIT:
          name: '事件阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        MAXNUMCCC:
          name: '计费条件改变阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        UCITIMER:
          name: '业务停止时长'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        INSERTISMF:
          name: '插入ISMF'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        REMOVALISMF:
          name: '删除ISMF'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        CHANGEISMF:
          name: '更新ISMF'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        SESSAMBRCHG:
          name: 'Session AMBR更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        SERVPLMNRTCTCHG:
          name: '服务PLMN速率控制更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        APNRATECTRLCHG:
          name: 'APN速率控制更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        CGISAICHG:
          name: 'CGISAI更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONREPORT
        RAICHG:
          name: 'RAI更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONREPORT
        TAICHG:
          name: '跟踪区标识更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONREPORT
    add_rgtrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置RG级Trigger。  如果需要为全局融合计费模板配置RG级Trigger，则使用**MOD RGTRIGGER**命令，“CCTMPLTNAME”为“global”。  融合计费模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        QOSCHG:
          name: 'QoS更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: DEFERRED
        ULCHG:
          name: '用户位置更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        SRVNDCHG:
          name: '服务节点更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PRACHG:
          name: '区域用户位置上报更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        PSDATAOFFCHG:
          name: 'PS数据关闭状态更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        UETZCHG:
          name: '用户时区更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        PLMNCHG:
          name: 'PLMN更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        RATCHG:
          name: 'RAT更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        TIMELIMIT:
          name: '时间阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        VOLUMELIMIT:
          name: '流量阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        EVENTLIMIT:
          name: '事件阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        QUOTATHRESHOLD:
          name: '配额阈值'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        VT:
          name: '配额有效时长'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        QHT:
          name: '配额保持时长'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMMEDIATE
        SERVPLMNRTCTCHG:
          name: '服务PLMN速率控制更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        APNRATECTRLCHG:
          name: 'APN速率控制更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFERRED
        TAICHG:
          name: '跟踪区标识更新'
          type: string
          enum:
          - NONREPORT
          - IMMEDIATE
          - DEFERRED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONREPORT
    set_rgresctrl_list:
      type: items
      properties:
        ONLRGAGESW:
          name: '在线计费RG老化控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制在线计费RG老化功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLAGETIMER:
          name: '在线计费RG老化时长 (分)'
          type: integer
          minimum:
          - 0
          - 10
          maximum:
          - 0
          - 1440
          required: false
          description: '控制在线计费RG老化时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLBLKTIMER:
          name: '在线计费全局业务阻塞处理时间间隔 (分)'
          type: integer
          minimum:
          - 0
          - 10
          maximum:
          - 0
          - 1440
          required: false
          description: '配置全局业务阻塞或重定向的时长，从阻塞或重定向开始经过这段时间以后，进行RG老化。  当配置为0时，表示阻塞时长无效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFLRGAGESW:
          name: '离线计费RG老化控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '控制离线计费RG老化功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFLAGETIMER:
          name: '离线计费RG老化时长 (分)'
          type: integer
          minimum:
          - 0
          - 10
          maximum:
          - 0
          - 1440
          required: false
          description: '控制离线计费RG老化时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXCSRVLMTACT:
          name: '超出业务最大规格处理动作'
          type: string
          enum:
          - BLOCK
          - PASS
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
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置N40接口消息的控制参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFID23G:
          name: 'GERAN/UTRAN接入场景携带UPFID'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRAINFO23G:
          name: 'GERAN/UTRAN接入场景携带Presence Reporting Area Information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SLICINGINFO23G:
          name: 'GERAN/UTRAN接入场景携带Network Slicing Information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE23G:
          name: 'GERAN/UTRAN接入场景携带SSC Mode'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNSELMODE23G:
          name: 'GERAN/UTRAN接入场景携带DNN Selection Mode'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STOPINDICTR23G:
          name: 'GERAN/UTRAN接入场景携带Session Stop Indicator'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UCITIMER23G:
          name: 'GERAN/UTRAN接入场景携带Unit Count Inactivity Timer'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FINALREPORT:
          name: '去活消息中usedUnitContainer中triggerType支持填写FINAL'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_chfinit_list:
    - CCTMPLTNAME: 'cct_test'
      CHFINIT: SENDREQ
      CCRINITRGNUM: 5
      WAITCHFRESP: ENABLE
      RGSOURCE: DEFAULT
    set_ctxstartrating_list:
    - USERPROFILENAME: 'up_test'
      CTXRURRGRPNAME1: 'urrgroup_test'
    add_pdutrigger_list:
    - CCTMPLTNAME: 'cct-test'
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
    - CCTMPLTNAME: 'cct_test'
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
      ONLAGETIMER: 20
      ONLBLKTIMER: 0
      OFLRGAGESW: ENABLE
      OFLAGETIMER: 20
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
{%- if is_optional_send_chargingdata_request -%}
    {%- for item in set_chfinit_list -%}
        SET CHFINIT:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CHFINIT is not none -%}
            CHFINIT={{item.CHFINIT}},
        {%- endif -%}
        {%- if item.CCRINITRGNUM is not none -%}
            CCRINITRGNUM={{item.CCRINITRGNUM}},
        {%- endif -%}
        {%- if item.WAITCHFRESP is not none -%}
            WAITCHFRESP={{item.WAITCHFRESP}},
        {%- endif -%}
        {%- if item.RGSOURCE is not none -%}
            RGSOURCE={{item.RGSOURCE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **可选：**配置SMF在建立计费会话的ChargingDataRequest中携带的为哪些RG申请预配额。

```jinja2
{%- if is_optional_preallocate_quota_rg -%}
    {%- for item in set_ctxstartrating_list -%}
        SET CTXSTARTRATING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CTXRURRGRPNAME1 is not none -%}
            CTXRURRGRPNAME1="{{item.CTXRURRGRPNAME1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置Session级/RG级Trigger。

#### 3.1 配置Session级Trigger。

```jinja2
{%- if is_optional_session_rg_trigger -%}
    {%- for item in add_pdutrigger_list -%}
        ADD PDUTRIGGER:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QOSCHG is not none -%}
            QOSCHG={{item.QOSCHG}},
        {%- endif -%}
        {%- if item.ULCHG is not none -%}
            ULCHG={{item.ULCHG}},
        {%- endif -%}
        {%- if item.SRVNDCHG is not none -%}
            SRVNDCHG={{item.SRVNDCHG}},
        {%- endif -%}
        {%- if item.PRACHG is not none -%}
            PRACHG={{item.PRACHG}},
        {%- endif -%}
        {%- if item.PSDATAOFFCHG is not none -%}
            PSDATAOFFCHG={{item.PSDATAOFFCHG}},
        {%- endif -%}
        {%- if item.UETZCHG is not none -%}
            UETZCHG={{item.UETZCHG}},
        {%- endif -%}
        {%- if item.PLMNCHG is not none -%}
            PLMNCHG={{item.PLMNCHG}},
        {%- endif -%}
        {%- if item.RATCHG is not none -%}
            RATCHG={{item.RATCHG}},
        {%- endif -%}
        {%- if item.ADDUPF is not none -%}
            ADDUPF={{item.ADDUPF}},
        {%- endif -%}
        {%- if item.TIMELIMIT is not none -%}
            TIMELIMIT={{item.TIMELIMIT}},
        {%- endif -%}
        {%- if item.VOLUMELIMIT is not none -%}
            VOLUMELIMIT={{item.VOLUMELIMIT}},
        {%- endif -%}
        {%- if item.EVENTLIMIT is not none -%}
            EVENTLIMIT={{item.EVENTLIMIT}},
        {%- endif -%}
        {%- if item.MAXNUMCCC is not none -%}
            MAXNUMCCC={{item.MAXNUMCCC}},
        {%- endif -%}
        {%- if item.UCITIMER is not none -%}
            UCITIMER={{item.UCITIMER}},
        {%- endif -%}
        {%- if item.INSERTISMF is not none -%}
            INSERTISMF={{item.INSERTISMF}},
        {%- endif -%}
        {%- if item.REMOVALISMF is not none -%}
            REMOVALISMF={{item.REMOVALISMF}},
        {%- endif -%}
        {%- if item.CHANGEISMF is not none -%}
            CHANGEISMF={{item.CHANGEISMF}},
        {%- endif -%}
        {%- if item.SESSAMBRCHG is not none -%}
            SESSAMBRCHG={{item.SESSAMBRCHG}},
        {%- endif -%}
        {%- if item.SERVPLMNRTCTCHG is not none -%}
            SERVPLMNRTCTCHG={{item.SERVPLMNRTCTCHG}},
        {%- endif -%}
        {%- if item.APNRATECTRLCHG is not none -%}
            APNRATECTRLCHG={{item.APNRATECTRLCHG}},
        {%- endif -%}
        {%- if item.CGISAICHG is not none -%}
            CGISAICHG={{item.CGISAICHG}},
        {%- endif -%}
        {%- if item.RAICHG is not none -%}
            RAICHG={{item.RAICHG}},
        {%- endif -%}
        {%- if item.TAICHG is not none -%}
            TAICHG={{item.TAICHG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置RG级Trigger。

```jinja2
{%- if is_optional_session_rg_trigger -%}
    {%- for item in add_rgtrigger_list -%}
        ADD RGTRIGGER:
        {#- --- 必选参数 --- -#}
        CCTMPLTNAME="{{item.CCTMPLTNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.QOSCHG is not none -%}
            QOSCHG={{item.QOSCHG}},
        {%- endif -%}
        {%- if item.ULCHG is not none -%}
            ULCHG={{item.ULCHG}},
        {%- endif -%}
        {%- if item.SRVNDCHG is not none -%}
            SRVNDCHG={{item.SRVNDCHG}},
        {%- endif -%}
        {%- if item.PRACHG is not none -%}
            PRACHG={{item.PRACHG}},
        {%- endif -%}
        {%- if item.PSDATAOFFCHG is not none -%}
            PSDATAOFFCHG={{item.PSDATAOFFCHG}},
        {%- endif -%}
        {%- if item.UETZCHG is not none -%}
            UETZCHG={{item.UETZCHG}},
        {%- endif -%}
        {%- if item.PLMNCHG is not none -%}
            PLMNCHG={{item.PLMNCHG}},
        {%- endif -%}
        {%- if item.RATCHG is not none -%}
            RATCHG={{item.RATCHG}},
        {%- endif -%}
        {%- if item.TIMELIMIT is not none -%}
            TIMELIMIT={{item.TIMELIMIT}},
        {%- endif -%}
        {%- if item.VOLUMELIMIT is not none -%}
            VOLUMELIMIT={{item.VOLUMELIMIT}},
        {%- endif -%}
        {%- if item.EVENTLIMIT is not none -%}
            EVENTLIMIT={{item.EVENTLIMIT}},
        {%- endif -%}
        {%- if item.QUOTATHRESHOLD is not none -%}
            QUOTATHRESHOLD={{item.QUOTATHRESHOLD}},
        {%- endif -%}
        {%- if item.VT is not none -%}
            VT={{item.VT}},
        {%- endif -%}
        {%- if item.QHT is not none -%}
            QHT={{item.QHT}},
        {%- endif -%}
        {%- if item.SERVPLMNRTCTCHG is not none -%}
            SERVPLMNRTCTCHG={{item.SERVPLMNRTCTCHG}},
        {%- endif -%}
        {%- if item.APNRATECTRLCHG is not none -%}
            APNRATECTRLCHG={{item.APNRATECTRLCHG}},
        {%- endif -%}
        {%- if item.TAICHG is not none -%}
            TAICHG={{item.TAICHG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置RG老化功能。

```jinja2
{%- for item in set_rgresctrl_list -%}
    SET RGRESCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.ONLRGAGESW is not none -%}
        ONLRGAGESW={{item.ONLRGAGESW}},
    {%- endif -%}
    {%- if item.OFLRGAGESW is not none -%}
        OFLRGAGESW={{item.OFLRGAGESW}},
    {%- endif -%}
    {%- if item.EXCSRVLMTACT is not none -%}
        EXCSRVLMTACT={{item.EXCSRVLMTACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ONLRGAGESW=ENABLE 时可选 --- -#}
    {%- if item.ONLRGAGESW == 'ENABLE' -%}
        {%- if item.ONLAGETIMER is not none -%}
            ONLAGETIMER={{item.ONLAGETIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLRGAGESW=ENABLE 时可选 --- -#}
    {%- if item.ONLRGAGESW == 'ENABLE' -%}
        {%- if item.ONLBLKTIMER is not none -%}
            ONLBLKTIMER={{item.ONLBLKTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OFLRGAGESW=ENABLE 时可选 --- -#}
    {%- if item.OFLRGAGESW == 'ENABLE' -%}
        {%- if item.OFLAGETIMER is not none -%}
            OFLAGETIMER={{item.OFLAGETIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 终端用户访问业务匹配到某个RG后，即使后续不再访问该业务，用户更新或时间流量阈值等场景触发向NCG/CHF(OCS)上报用量时，会上报该RG的用量且用量为零，用户长时间在线会造成N40接口的消息变大，同时造成RG及URR等资源浪费。QHT功能可以删除已停止访问业务的RG，但该功能依赖于NCG/CHF(OCS)配合下发QHT Trigger。通过****SET RGRESCTRL****命令配置RG老化时长，可以保证在QHT功能不使能或QHT使能但QHT值为0场景下，保证已停止访问业务的RG老化，携带Trigger类型为Final，避免大量RG在线造成消息过大。

### 5 设置N40接口消息的控制参数。

```jinja2
{%- for item in set_n40msgctrl_list -%}
    SET N40MSGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.ROAMOFFSTARTSW is not none -%}
        ROAMOFFSTARTSW={{item.ROAMOFFSTARTSW}},
    {%- endif -%}
    {%- if item.UPFID23G is not none -%}
        UPFID23G={{item.UPFID23G}},
    {%- endif -%}
    {%- if item.PRAINFO23G is not none -%}
        PRAINFO23G={{item.PRAINFO23G}},
    {%- endif -%}
    {%- if item.SLICINGINFO23G is not none -%}
        SLICINGINFO23G={{item.SLICINGINFO23G}},
    {%- endif -%}
    {%- if item.SSCMODE23G is not none -%}
        SSCMODE23G={{item.SSCMODE23G}},
    {%- endif -%}
    {%- if item.DNNSELMODE23G is not none -%}
        DNNSELMODE23G={{item.DNNSELMODE23G}},
    {%- endif -%}
    {%- if item.STOPINDICTR23G is not none -%}
        STOPINDICTR23G={{item.STOPINDICTR23G}},
    {%- endif -%}
    {%- if item.UCITIMER23G is not none -%}
        UCITIMER23G={{item.UCITIMER23G}},
    {%- endif -%}
    {%- if item.FINALREPORT is not none -%}
        FINALREPORT={{item.FINALREPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

