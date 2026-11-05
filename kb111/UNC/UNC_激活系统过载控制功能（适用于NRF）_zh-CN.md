---
id: ''
name: 激活系统过载控制功能（适用于NRF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。  适用于NRF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010801 系统过载控制功能","系统过载控制功能（适用于NRF）","激活系统过载控制功能（适用于NRF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活系统过载控制功能的操作过程。适用于NRF。

## 必备事项
前提条件

前提条件

请仔细阅读WSFD-010801系统过载控制功能特性概述（适用于NRF）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_fcparam_list:
      type: items
      properties:
        SERVICETYPE:
          name: '服务类型'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICEID:
          name: '实例组ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CASEID:
          name: '流控套餐ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARAMCAT:
          name: '参数类别'
          type: string
          enum:
          - GENERAL
          - WEIGHTS
          - THRESHOLD
          - TARGETCPU
          - OVERLOADLEVEL
          - STOPALGO
          - BPBACKEND
          - BPFRONTEND
          - WALPARAMETER
          - GCCPUCONFIG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINTOKEN:
          name: '最小令牌数'
          type: integer
          minimum:
          - 10
          - 4294967295
          maximum:
          - 50000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXTOKEN:
          name: '最大令牌数'
          type: integer
          minimum:
          - 10
          - 4294967295
          maximum:
          - 50000
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BPMUTYPE:
          name: '反压MU值计算方式'
          type: string
          enum:
          - UAVG
          - UMID
          - UMAX
          - UMIN
          - NOTSET
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTCPUSTOPALGO:
          name: '容器cpu停控算法'
          type: string
          enum:
          - AVERAGE
          - CONTINUE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CNTLOWERTH:
          name: '容器cpu停控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTLOWTHDELTA:
          name: '容器cpu停控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTMILDOVERLOAD:
          name: '容器轻度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTMODEOVERLOAD:
          name: '容器中度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTSEROVERLAOD:
          name: '容器重度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTTARGETCPU:
          name: '容器目标cpu'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTTHOFNODE:
          name: '节点cpu的容器cpu阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTUPPERTH:
          name: '容器cpu起控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNTUPTHDELTA:
          name: '容器cpu起控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CT:
          name: 'CPU常量(CT)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEBPBACKEND:
          name: '启用后端反压'
          type: string
          enum:
          - NOTSET
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLEBPFRONT:
          name: '启用前端反压'
          type: string
          enum:
          - NOTSET
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLECALREFTFC:
          name: '校准GC CPU时参考消息量'
          type: string
          enum:
          - NOTSET
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENABLECNTTH:
          name: '启用节点cpu参考容器cpu'
          type: string
          enum:
          - NOTSET
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPECTSUCCRATE:
          name: '反压预期成功率'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GCCALIBRATEMODE:
          name: '校准GC的模式(CalibrateMode)'
          type: string
          enum:
          - CALIBRATEGCJUMPMODE
          - CALIBRATEGCAVGMODE
          - NOTSET
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KAPPAD:
          name: '微分常数(KAPPAD)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KAPPAP:
          name: '比例常数(KAPPAP)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAMBDA:
          name: '反压MU值调整比例'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MILDOVERLOAD:
          name: '节点轻度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINBPRATIO:
          name: '前端反压最小令牌比例'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MODEROVERLOAD:
          name: '节点中度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODECPUSTOPALGO:
          name: '节点cpu停控算法'
          type: string
          enum:
          - AVERAGE
          - CONTINUE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        NODELOWERTH:
          name: '节点cpu停控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODELOWTHDELTA:
          name: '节点cpu停控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODEUPPERTH:
          name: '节点cpu起控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODEUPTHDELTA:
          name: '节点cpu起控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PHI:
          name: '反压前端MU值调整比例'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODCPUSTOPALGO:
          name: 'Pod cpu停控算法'
          type: string
          enum:
          - AVERAGE
          - CONTINUE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        PODLOWERTH:
          name: 'Pod cpu停控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODLOWTHDELTA:
          name: 'Pod cpu停控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODMILDOVERLOAD:
          name: 'Pod轻度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODMODEOVERLOAD:
          name: 'Pod中度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODSEROVERLOAD:
          name: 'Pod重度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODTARGETCPU:
          name: 'Pod目标cpu'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODUPPERTH:
          name: 'Pod cpu起控阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PODUPTHDELTA:
          name: 'Pod cpu起控时长'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 300
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RHOH:
          name: '算法控制参数(RHOH)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RHOL:
          name: '算法控制参数(RHOL)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEVEREOVERLOAD:
          name: '节点重度过载阈值'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTBP:
          name: '反压起控条件'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STOPBP:
          name: '反压停控条件'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TARGETCPU:
          name: '节点目标cpu'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TARGETSUCCRATE:
          name: '反压MU值目标成功率'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 100
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPN:
          name: '导致成功率低的前N项消息'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRAFFICDELTARAT:
          name: '冲击消息量的增量比例(DeltaRatio)'
          type: integer
          minimum:
          - 10
          - 4294967295
          maximum:
          - 102400
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRAFFICFILLEN:
          name: '基础消息量的干扰数据长度(TrafficFilterLen)'
          type: integer
          minimum:
          - 5
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRAFFICSAMLEN:
          name: '基础消息量采样长度(TrafficSampleLen)'
          type: integer
          minimum:
          - 15
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAL0DATAFILLEN:
          name: '干扰数据长度(WAL0DATAFILLEN)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAL0DATASAMLEN:
          name: '数据基线长度(WAL0DATASAMLEN)'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 60
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEIGHTMETHOD:
          name: '业务权重获取方式'
          type: string
          enum:
          - SERVICE
          - FCLEARN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fcswitch_list:
      type: items
      properties:
        SWITCH:
          name: '开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置基于CPU过载的流控开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrffuncsw_list:
      type: items
      properties:
        NFMFCSWITCH:
          name: '管理类消息流控开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '开启针对管理类消息和发现类消息的自保流控功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISCFCSWITCH:
          name: '发现类消息流控开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrffcpara_list:
      type: items
      properties:
        FCLEVEL:
          name: '流控等级'
          type: string
          enum:
          - LOW
          - MEDIUM
          - HIGH
          required: true
          description: '设置不同流控级别对应的流控响应。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FCRSP:
          name: '流控响应'
          type: string
          enum:
          - TooManyRequest_429
          - ServiceUnavailable_503
          - NoResponse
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nrfnotifyfcpara_list:
      type: items
      properties:
        NFCHGCACHETHD:
          name: 'NF更新事件缓冲最长时长(秒)'
          type: integer
          minimum: 1
          maximum: 3600
          required: false
          description: '设置NRF针对同一频繁变更的NF的多长时间内的变更事件合并。  设置多长时间内同一个NF超过1次变更就识别此NF为频繁变更，需要对其变更通知做抑制合并。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFCHGCACHETIME:
          name: 'NF更新事件最短缓冲时长(秒)'
          type: integer
          minimum: 0
          maximum: 1800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_httpfixedfcmsg_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - NSMF_PDUSESSION_SMCONTEXTSCREATE
          - NSMF_PDUSESSION_RETRIEVESMCONTEXT
          - NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY
          - NAMF_COMMUNICATION_UECONTEXTTRANSFER
          - NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION
          - NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION
          - NNSSF_NSSELECTION_NSSELECTIONGET
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST
          - NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION
          - NSMSF_SMSERVICESERVICEAPI_SENDSMS
          - NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE
          - NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE
          - NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE
          - NUPF_EVENTEXPOSURE_NOTIFY
          - NSMF_EVENTEXPOSURE_NOTIFY
          - NAMF_EVENTEXPOSURE_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_SUBSCRIBER
          - NUDN_RAILWAYSAMPLEDATARECORDR
          required: true
          description: '设置服务化接口上指定消息类型固定速率流控信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_fcparam_list:
    - SERVICETYPE: 'UesmCtrlSvc'
      SERVICEID: 999
      CASEID: 0
      PARAMCAT: GENERAL
      MINTOKEN: 30
      MAXTOKEN: 5000
      BPMUTYPE: ''
      CNTCPUSTOPALGO: DISABLE
      CNTLOWERTH: ''
      CNTLOWTHDELTA: ''
      CNTMILDOVERLOAD: ''
      CNTMODEOVERLOAD: ''
      CNTSEROVERLAOD: ''
      CNTTARGETCPU: ''
      CNTTHOFNODE: ''
      CNTUPPERTH: ''
      CNTUPTHDELTA: ''
      CT: ''
      ENABLEBPBACKEND: ''
      ENABLEBPFRONT: ''
      ENABLECALREFTFC: ''
      ENABLECNTTH: ''
      EXPECTSUCCRATE: ''
      GCCALIBRATEMODE: ''
      KAPPAD: ''
      KAPPAP: ''
      LAMBDA: ''
      MILDOVERLOAD: ''
      MINBPRATIO: ''
      MODEROVERLOAD: ''
      NODECPUSTOPALGO: DISABLE
      NODELOWERTH: ''
      NODELOWTHDELTA: ''
      NODEUPPERTH: ''
      NODEUPTHDELTA: ''
      PHI: ''
      PODCPUSTOPALGO: DISABLE
      PODLOWERTH: ''
      PODLOWTHDELTA: ''
      PODMILDOVERLOAD: ''
      PODMODEOVERLOAD: ''
      PODSEROVERLOAD: ''
      PODTARGETCPU: ''
      PODUPPERTH: ''
      PODUPTHDELTA: ''
      RHOH: ''
      RHOL: ''
      SEVEREOVERLOAD: ''
      STARTBP: ''
      STOPBP: ''
      TARGETCPU: ''
      TARGETSUCCRATE: ''
      TOPN: ''
      TRAFFICDELTARAT: ''
      TRAFFICFILLEN: ''
      TRAFFICSAMLEN: ''
      WAL0DATAFILLEN: ''
      WAL0DATASAMLEN: ''
      WEIGHTMETHOD: ''
    set_fcswitch_list:
    - SWITCH: ENABLE
    set_nrffuncsw_list:
    - NFMFCSWITCH: FUNC_ON
      DISCFCSWITCH: FUNC_ON
    set_nrffcpara_list:
    - FCLEVEL: LOW
      FCRSP: TooManyRequest_429
    set_nrfnotifyfcpara_list:
    - NFCHGCACHETHD: 900
      NFCHGCACHETIME: 50
    set_httpfixedfcmsg_list:
    - MSGTYPE: NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES
      FCSWITCH: ON
      THRESHOLD: 4000
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 添加具体实例的流控参数。

```jinja2
{%- for item in add_fcparam_list -%}
    ADD FCPARAM:
    {#- --- 必选参数 --- -#}
    SERVICETYPE="{{item.SERVICETYPE}}",
    SERVICEID={{item.SERVICEID}},
    CASEID={{item.CASEID}},
    PARAMCAT={{item.PARAMCAT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PARAMCAT=GENERAL 时可选 --- -#}
    {%- if item.PARAMCAT == 'GENERAL' -%}
        {%- if item.MINTOKEN is not none -%}
            MINTOKEN={{item.MINTOKEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GENERAL 时可选 --- -#}
    {%- if item.PARAMCAT == 'GENERAL' -%}
        {%- if item.MAXTOKEN is not none -%}
            MAXTOKEN={{item.MAXTOKEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.BPMUTYPE is not none -%}
            BPMUTYPE={{item.BPMUTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=STOPALGO 时可选 --- -#}
    {%- if item.PARAMCAT == 'STOPALGO' -%}
        {%- if item.CNTCPUSTOPALGO is not none -%}
            CNTCPUSTOPALGO={{item.CNTCPUSTOPALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.CNTLOWERTH is not none -%}
            CNTLOWERTH={{item.CNTLOWERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.CNTLOWTHDELTA is not none -%}
            CNTLOWTHDELTA={{item.CNTLOWTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.CNTMILDOVERLOAD is not none -%}
            CNTMILDOVERLOAD={{item.CNTMILDOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.CNTMODEOVERLOAD is not none -%}
            CNTMODEOVERLOAD={{item.CNTMODEOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.CNTSEROVERLAOD is not none -%}
            CNTSEROVERLAOD={{item.CNTSEROVERLAOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=TARGETCPU 时可选 --- -#}
    {%- if item.PARAMCAT == 'TARGETCPU' -%}
        {%- if item.CNTTARGETCPU is not none -%}
            CNTTARGETCPU={{item.CNTTARGETCPU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.CNTTHOFNODE is not none -%}
            CNTTHOFNODE={{item.CNTTHOFNODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.CNTUPPERTH is not none -%}
            CNTUPPERTH={{item.CNTUPPERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.CNTUPTHDELTA is not none -%}
            CNTUPTHDELTA={{item.CNTUPTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.CT is not none -%}
            CT={{item.CT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.ENABLEBPBACKEND is not none -%}
            ENABLEBPBACKEND={{item.ENABLEBPBACKEND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPFRONTEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPFRONTEND' -%}
        {%- if item.ENABLEBPFRONT is not none -%}
            ENABLEBPFRONT={{item.ENABLEBPFRONT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GCCPUCONFIG 时可选 --- -#}
    {%- if item.PARAMCAT == 'GCCPUCONFIG' -%}
        {%- if item.ENABLECALREFTFC is not none -%}
            ENABLECALREFTFC={{item.ENABLECALREFTFC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.ENABLECNTTH is not none -%}
            ENABLECNTTH={{item.ENABLECNTTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.EXPECTSUCCRATE is not none -%}
            EXPECTSUCCRATE={{item.EXPECTSUCCRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GCCPUCONFIG 时可选 --- -#}
    {%- if item.PARAMCAT == 'GCCPUCONFIG' -%}
        {%- if item.GCCALIBRATEMODE is not none -%}
            GCCALIBRATEMODE={{item.GCCALIBRATEMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.KAPPAD is not none -%}
            KAPPAD={{item.KAPPAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.KAPPAP is not none -%}
            KAPPAP={{item.KAPPAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.LAMBDA is not none -%}
            LAMBDA={{item.LAMBDA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.MILDOVERLOAD is not none -%}
            MILDOVERLOAD={{item.MILDOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPFRONTEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPFRONTEND' -%}
        {%- if item.MINBPRATIO is not none -%}
            MINBPRATIO={{item.MINBPRATIO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.MODEROVERLOAD is not none -%}
            MODEROVERLOAD={{item.MODEROVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=STOPALGO 时可选 --- -#}
    {%- if item.PARAMCAT == 'STOPALGO' -%}
        {%- if item.NODECPUSTOPALGO is not none -%}
            NODECPUSTOPALGO={{item.NODECPUSTOPALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.NODELOWERTH is not none -%}
            NODELOWERTH={{item.NODELOWERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.NODELOWTHDELTA is not none -%}
            NODELOWTHDELTA={{item.NODELOWTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.NODEUPPERTH is not none -%}
            NODEUPPERTH={{item.NODEUPPERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.NODEUPTHDELTA is not none -%}
            NODEUPTHDELTA={{item.NODEUPTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.PHI is not none -%}
            PHI={{item.PHI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=STOPALGO 时可选 --- -#}
    {%- if item.PARAMCAT == 'STOPALGO' -%}
        {%- if item.PODCPUSTOPALGO is not none -%}
            PODCPUSTOPALGO={{item.PODCPUSTOPALGO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.PODLOWERTH is not none -%}
            PODLOWERTH={{item.PODLOWERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.PODLOWTHDELTA is not none -%}
            PODLOWTHDELTA={{item.PODLOWTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.PODMILDOVERLOAD is not none -%}
            PODMILDOVERLOAD={{item.PODMILDOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.PODMODEOVERLOAD is not none -%}
            PODMODEOVERLOAD={{item.PODMODEOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.PODSEROVERLOAD is not none -%}
            PODSEROVERLOAD={{item.PODSEROVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=TARGETCPU 时可选 --- -#}
    {%- if item.PARAMCAT == 'TARGETCPU' -%}
        {%- if item.PODTARGETCPU is not none -%}
            PODTARGETCPU={{item.PODTARGETCPU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.PODUPPERTH is not none -%}
            PODUPPERTH={{item.PODUPPERTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=THRESHOLD 时可选 --- -#}
    {%- if item.PARAMCAT == 'THRESHOLD' -%}
        {%- if item.PODUPTHDELTA is not none -%}
            PODUPTHDELTA={{item.PODUPTHDELTA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.RHOH is not none -%}
            RHOH={{item.RHOH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.RHOL is not none -%}
            RHOL={{item.RHOL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=OVERLOADLEVEL 时可选 --- -#}
    {%- if item.PARAMCAT == 'OVERLOADLEVEL' -%}
        {%- if item.SEVEREOVERLOAD is not none -%}
            SEVEREOVERLOAD={{item.SEVEREOVERLOAD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.STARTBP is not none -%}
            STARTBP={{item.STARTBP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.STOPBP is not none -%}
            STOPBP={{item.STOPBP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=TARGETCPU 时可选 --- -#}
    {%- if item.PARAMCAT == 'TARGETCPU' -%}
        {%- if item.TARGETCPU is not none -%}
            TARGETCPU={{item.TARGETCPU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.TARGETSUCCRATE is not none -%}
            TARGETSUCCRATE={{item.TARGETSUCCRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=BPBACKEND 时可选 --- -#}
    {%- if item.PARAMCAT == 'BPBACKEND' -%}
        {%- if item.TOPN is not none -%}
            TOPN={{item.TOPN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GCCPUCONFIG 时可选 --- -#}
    {%- if item.PARAMCAT == 'GCCPUCONFIG' -%}
        {%- if item.TRAFFICDELTARAT is not none -%}
            TRAFFICDELTARAT={{item.TRAFFICDELTARAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GCCPUCONFIG 时可选 --- -#}
    {%- if item.PARAMCAT == 'GCCPUCONFIG' -%}
        {%- if item.TRAFFICFILLEN is not none -%}
            TRAFFICFILLEN={{item.TRAFFICFILLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=GCCPUCONFIG 时可选 --- -#}
    {%- if item.PARAMCAT == 'GCCPUCONFIG' -%}
        {%- if item.TRAFFICSAMLEN is not none -%}
            TRAFFICSAMLEN={{item.TRAFFICSAMLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.WAL0DATAFILLEN is not none -%}
            WAL0DATAFILLEN={{item.WAL0DATAFILLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WALPARAMETER 时可选 --- -#}
    {%- if item.PARAMCAT == 'WALPARAMETER' -%}
        {%- if item.WAL0DATASAMLEN is not none -%}
            WAL0DATASAMLEN={{item.WAL0DATASAMLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PARAMCAT=WEIGHTS 时可选 --- -#}
    {%- if item.PARAMCAT == 'WEIGHTS' -%}
        {%- if item.WEIGHTMETHOD is not none -%}
            WEIGHTMETHOD={{item.WEIGHTMETHOD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置基于CPU过载流控开关。

```jinja2
{%- for item in set_fcswitch_list -%}
    SET FCSWITCH:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 4 开启针对管理类消息和发现类消息的自保流控功能。

```jinja2
{%- for item in set_nrffuncsw_list -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.NFMFCSWITCH is not none -%}
        NFMFCSWITCH={{item.NFMFCSWITCH}},
    {%- endif -%}
    {%- if item.DISCFCSWITCH is not none -%}
        DISCFCSWITCH={{item.DISCFCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置不同流控级别对应的流控响应。

```jinja2
{%- for item in set_nrffcpara_list -%}
    SET NRFFCPARA:
    {#- --- 必选参数 --- -#}
    FCLEVEL={{item.FCLEVEL}},
    FCRSP={{item.FCRSP}},
    ;
{%- endfor -%}
```

### 6 设置NF变更事件合并发送通知相关阈值。

```jinja2
{%- for item in set_nrfnotifyfcpara_list -%}
    SET NRFNOTIFYFCPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.NFCHGCACHETHD is not none -%}
        NFCHGCACHETHD={{item.NFCHGCACHETHD}},
    {%- endif -%}
    {%- if item.NFCHGCACHETIME is not none -%}
        NFCHGCACHETIME={{item.NFCHGCACHETIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 设置服务化接口上指定消息类型的固定速率。

```jinja2
{%- for item in set_httpfixedfcmsg_list -%}
    SET HTTPFIXEDFCMSG:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

