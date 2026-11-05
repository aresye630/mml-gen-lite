---
id: ''
name: 配置SMF与CHF交互的条件和内容
ne_type: UNC
type: feature
description: 配置SMF与CHF交互的条件及内容，即配置：  * 用户激活时是否需要到CHF交互。 * SMF在什么情况下向CHF发送ChargingDataRequest消息。 * SMF向CHF发送ChargingDataRequest消息时携带预申请配额的RG。  ChargingDataRequest触发条件可以由CHF在ChargingDataResponse消息中携带，也可以在SMF上本地配置。CHF下发的优先级比SMF本地配置的高。  ChargingDataRequest有多种触发场景，融合计费过程中，当其中任一个触发条件满足时，都会触发ChargingDataRequest上报。  * 适用于SMF。 * 为了避免SMF和CHF频繁交互所带来的高负荷对网络和网元造成影响，建议交互条件及内容的配置结果能保证每个用户上报Charging Data Request的间隔大于30秒。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","配置SMF与CHF交互的条件和内容"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
配置SMF与CHF交互的条件及内容，即配置：* 用户激活时是否需要到CHF交互。* SMF在什么情况下向CHF发送ChargingDataRequest消息。* SMF向CHF发送ChargingDataRequest消息时携带预申请配额的RG。ChargingDataRequest触发条件可以由CHF在ChargingDataResponse消息中携带，也可以在SMF上本地配置。CHF下发的优先级比SMF本地配置的高。ChargingDataRequest有多种触发场景，融合计费过程中，当其中任一个触发条件满足时，都会触发ChargingDataRequest上报。* 适用于SMF。* 为了避免SMF和CHF频繁交互所带来的高负荷对网络和网元造成影响，建议交互条件及内容的配置结果能保证每个用户上报Charging Data Request的间隔大于30秒。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
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
          description: '配置建立PDU会话时是否发送ChargingDataRqueset与CHF交互。  CCT模板的配置请参见配置融合计费模板。'
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
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: 'SMF和UPF上的URR标识需要一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: '根据业务套餐情况，确定使用RG还是（RG，SID）作为费率标识。  此处以使用RG作为费率标识为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: '根据业务套餐情况，确定使用免费、按时长计费、按流量计费，还是按照流量+时长计费。  此处以按流量计费为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLINESID:
          name: '在线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVENTRSUVALUE:
          name: '事件配额值（次）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMERSUVALUE:
          name: '时间配额值（秒）'
          type: integer
          minimum: 0
          maximum: 3600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URR**命令定义的“URRNAME”。  上行和下行可以使用相同的URR名称，也可以使用不同的URR名称。  上行URR名称不能相同，下行URR名称不能相同。  根据业务套餐规划，至少配置1个名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pdutrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置Session级Trigger。  CCT模板的配置请参见配置融合计费模板。'
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
    add_rgtrigger_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: 'CCT模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置RG级Trigger。  CCT模板的配置请参见配置融合计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ULCHG:
          name: '用户位置更新'
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
    add_urr_list:
    - URRNAME: 'urr_test'
      URRID: 1111
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 111
      ONLMETERINGTYPE: VOLUME
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      OFFMETERINGTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgroup_test'
      UPURRNAME1: 'urr_test'
      DOWNURRNAME1: 'urr_test'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_ctxstartrating_list:
    - USERPROFILENAME: 'up_test'
      CTXRURRGRPNAME1: 'urrgroup_test'
    add_pdutrigger_list:
    - CCTMPLTNAME: 'cct-test'
      QOSCHG: IMMEDIATE
      SRVNDCHG: DEFERRED
      RATCHG: IMMEDIATE
      PRACHG: DEFERRED
      ADDUPF: IMMEDIATE
      INSERTISMF: DEFERRED
      CGISAICHG: DEFERRED
      RAICHG: DEFERRED
    add_rgtrigger_list:
    - CCTMPLTNAME: 'cct_test'
      ULCHG: NONREPORT
      PRACHG: IMMEDIATE
      PSDATAOFFCHG: IMMEDIATE
    set_rgresctrl_list:
    - ONLRGAGESW: ENABLE
      ONLAGETIMER: 20
      ONLBLKTIMER: 0
      OFLRGAGESW: ENABLE
      OFLAGETIMER: 20
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

### 1 **可选：**配置建立PDU会话时是否发送ChargingDataRequest与CHF交互。

```jinja2
{%- if is_optional_chf_interaction -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **可选：**配置SMF在建立计费会话的ChargingDataRequest中携带的为哪些RG申请预配额。

#### 2.1 配置URR组合URR，指定需预申请配额的RG。

```jinja2
{%- if is_optional_rg_pre_quota -%}
    {%- for item in add_urr_list -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
            ONLINERG={{item.ONLINERG}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
            MONITORINGKEY="{{item.MONITORINGKEY}}",
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
            ONLINESID={{item.ONLINESID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.ONLMETERINGTYPE is not none -%}
                ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=EVENT/EVENT_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['EVENT', 'EVENT_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.EVENTRSUVALUE is not none -%}
                EVENTRSUVALUE={{item.EVENTRSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.N40AGESW is not none -%}
                N40AGESW={{item.N40AGESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFCSRVTMPLNAME is not none -%}
                OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFFMETERINGTYPE is not none -%}
                OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.REDIRENDTOKEN is not none -%}
                REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=TIME/VOLUME_TIME/EVENT_TIME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['TIME', 'VOLUME_TIME', 'EVENT_TIME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.TIMERSUVALUE is not none -%}
                TIMERSUVALUE={{item.TIMERSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.VOLUMERSUVALUE is not none -%}
                VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_rg_pre_quota -%}
    {%- for item in add_urrgroup_list -%}
        ADD URRGROUP:
        {#- --- 必选参数 --- -#}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.UPURRNAME1 is not none -%}
            UPURRNAME1="{{item.UPURRNAME1}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME1 is not none -%}
            DOWNURRNAME1="{{item.DOWNURRNAME1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置UserProfile。

```jinja2
{%- if is_optional_rg_pre_quota -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
        {%- if item.UPTYPE == 'PCC' -%}
            {%- if item.PROFILERANGE is not none -%}
                PROFILERANGE={{item.PROFILERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 绑定UserProfile与URR组，从而使SMF在与CHF建立计费会话时，为该用户模板的用户携带相应的URR组中的RG。

```jinja2
{%- if is_optional_rg_pre_quota -%}
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
        {%- if item.SRVNDCHG is not none -%}
            SRVNDCHG={{item.SRVNDCHG}},
        {%- endif -%}
        {%- if item.RATCHG is not none -%}
            RATCHG={{item.RATCHG}},
        {%- endif -%}
        {%- if item.PRACHG is not none -%}
            PRACHG={{item.PRACHG}},
        {%- endif -%}
        {%- if item.ADDUPF is not none -%}
            ADDUPF={{item.ADDUPF}},
        {%- endif -%}
        {%- if item.INSERTISMF is not none -%}
            INSERTISMF={{item.INSERTISMF}},
        {%- endif -%}
        {%- if item.CGISAICHG is not none -%}
            CGISAICHG={{item.CGISAICHG}},
        {%- endif -%}
        {%- if item.RAICHG is not none -%}
            RAICHG={{item.RAICHG}},
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
        {%- if item.ULCHG is not none -%}
            ULCHG={{item.ULCHG}},
        {%- endif -%}
        {%- if item.PRACHG is not none -%}
            PRACHG={{item.PRACHG}},
        {%- endif -%}
        {%- if item.PSDATAOFFCHG is not none -%}
            PSDATAOFFCHG={{item.PSDATAOFFCHG}},
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

### 终端用户访问业务匹配到某个RG后，即使后续不再访问该业务，用户更新或时间流量阈值等场景触发向CHF上报用量时，会上报该RG的用量且用量为零，用户长时间在线会造成N40接口的消息变大，同时造成RG及URR等资源浪费。QHT功能可以删除已停止访问业务的RG，但该功能依赖于CHF配合下发QHT Trigger。通过****SET RGRESCTRL****命令配置RG老化时长，可以保证在QHT功能不使能或QHT使能但QHT值为0场景下，保证已停止访问业务的RG老化，携带Trigger类型为Final，避免大量RG在线造成消息过大。

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

