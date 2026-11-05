---
id: ''
name: 配置CCR触发场景
ne_type: UNC
type: feature
description: GGSN/PGW-C和OCS都可以指定CCR触发场景，OCS可以通过CCA消息携带的信元Trigger AVP指定触发CCR上报的场景，GGSN/PGW-C本地也可以配置CCR触发场景，OCS下发优先级更高。  GGSN/PGW-C在多种场景下支持向OCS发起CCR更新流程，配置的时候可以根据需要选择配置。在线计费过程中，当其中一个条件满足时，便会触发CCR上报。建议配置的配额门限的大小适度，要满足CCR与CCA之间下次新配额申请时使用。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109001 Gy/Diameter在线计费","激活Gy/Diameter在线计费","配置在线计费模板","配置CCR触发场景"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/PGW-C和OCS都可以指定CCR触发场景，OCS可以通过CCA消息携带的信元Trigger AVP指定触发CCR上报的场景，GGSN/PGW-C本地也可以配置CCR触发场景，OCS下发优先级更高。GGSN/PGW-C在多种场景下支持向OCS发起CCR更新流程，配置的时候可以根据需要选择配置。在线计费过程中，当其中一个条件满足时，便会触发CCR上报。建议配置的配额门限的大小适度，要满足CCR与CCA之间下次新配额申请时使用。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到OCS的数据(静态路由+BFD组网)。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '新增DCC在线计费模板，用于配置在线计费相关属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHT:
          name: '配额空闲时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 3600
          - 4294967295
          required: false
          description: '配额空闲时间监控业务暂停的时长。QHT=0表示QHT不生效。  说明：  如果OCS支持接收QHT超时触发的CCR消息，建议QHT不小于60秒。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VQT:
          name: '流量阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余流量配额达到VQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        TQT:
          name: '时间阈值触发百分比（%）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 50
          - 4294967295
          required: false
          description: '标识业务剩余时长配额达到TQT时，触发GGSN/PGW-C上报CCR消息请求新配额，收到新配额后可以继续之前的业务。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        VALIDTIME:
          name: '在线配额有效时长（分）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 1440
          - 4294967295
          required: false
          description: '标识配额有效时长，超时后触发GGSN/PGW-C上报CCR消息。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        RATTRIGGER:
          name: 'Rat变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'RAT改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SGSNTRIGGER:
          name: 'SGSN变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'SGSN/SGW地址改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        QOSTRIGGER:
          name: 'QoS变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'QoS改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        ULITRIGGER:
          name: 'ULI变化触发使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'ULI改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SERVICETRIGGER:
          name: '业务触发请求使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '应用新业务是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        QCT:
          name: '配额空耗时间门限值（秒）'
          type: integer
          minimum:
          - 0
          - 5
          - 4294967295
          maximum:
          - 0
          - 200
          - 4294967295
          required: false
          description: '配额空耗时间标识如何统计业务时长。QCT=0表示连续统计业务时长。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        CCRINITRGNUM:
          name: '指定CCR-I消息中携带RG的个数'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 10
          - 4294967295
          required: false
          description: '用户激活时发送的CCR-I消息中携带RG的个数。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        MCCTRIGGER:
          name: 'MCC变化触发重授权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'MCC改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        MNCTRIGGER:
          name: 'MNC变化触发重授权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'MNC改变是否发送CCR.'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        LACTRIGGER:
          name: 'LAC变化触发重授权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: 'LAC改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        UETZTRIGGER:
          name: 'UE TimeZone改变触发重授权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '终端时区改变是否发送CCR。'
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
    set_ocsinit_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '当用户激活触发DCC会话时，“OCSINIT”取值必须设置为“ENABLE”，即支持用户激活时与OCS交互。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        OCSINIT:
          name: 'OCS交互使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITOCSRESP:
          name: 'OCS交互等待OCS响应开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
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
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          maxLength: 31
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
          description: ''
          data_source: ''
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
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN实例绑定DCC Template模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DCCTEMPLATE:
          name: 'DCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCCONFIGMODE:
          name: '计费属性配置模式'
          type: string
          enum:
          - FLATBILLING
          - HOTBILLING
          - NORMAL
          - PREPAID
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEISVSEGNAME:
          name: 'IMEISV号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSSEGNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        LOCGROUPNAME:
          name: '位置组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAT:
          name: 'RAT'
          type: string
          enum:
          - EMTC
          - EUTRAN
          - GAN
          - GERAN
          - HSPA
          - NBIOT
          - NONE
          - NR
          - REDCAP
          - UTRAN
          - WLAN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游属性'
          type: string
          enum:
          - HOME
          - NONE
          - ROAMING
          - VISITING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGGROUPNAME:
          name: 'IMSI/MSISDN/IMEISV 号段组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_dcctemplate_list:
    - DCCTMPLTNAME: ''
    add_dcctemplate_list:
    - DCCTMPLTNAME: 'dcc-test'
      QHT: 0
      VQT: 0
      TQT: 20
      VALIDTIME: 30
      RATTRIGGER: ENABLE
      SGSNTRIGGER: ENABLE
      QOSTRIGGER: ENABLE
      ULITRIGGER: ENABLE
      SERVICETRIGGER: ENABLE
      QCT: 0
      CCRINITRGNUM: 5
      MCCTRIGGER: ENABLE
      MNCTRIGGER: ENABLE
      LACTRIGGER: ENABLE
      UETZTRIGGER: ENABLE
    set_ocsinit_list:
    - DCCTMPLTNAME: 'dcc-test'
      OCSINIT: ENABLE
      WAITOCSRESP: ''
    add_urr_list:
    - URRNAME: 'onlineURR'
      URRID: 1100
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 100
      ONLMETERINGTYPE: TIME
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
    - URRGROUPNAME: 'urrgroup1'
      UPURRNAME1: 'onlineURR'
      DOWNURRNAME1: 'onlineURR'
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'up-test'
      DFTURRGRPNAME: 'urrgroup1'
    set_ctxstartrating_list:
    - USERPROFILENAME: 'up-test'
      CTXRURRGRPNAME1: 'urrgroup1'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      DCCTEMPLATE: 'dcc-test'
    add_usrprofgroup_list:
    - USERPROFGNAME: 'upg-test'
    add_upbindupg_list:
    - USERPROFGNAME: 'upg_test'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'up_test'
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
    add_apnusrprofg_list:
    - APN: 'apn-test'
      USERPROFGNAME: 'upg-test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置UNC Gy接口与OCS之间的DCC会话建立方式。

### 配置全局通用参数DCC模板，DCC模板名称。“DCCTMPLTNAME”=“global”

```jinja2
{%- for item in mod_dcctemplate_list -%}
    MOD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    ;
{%- endfor -%}
```

### 2 配置DCC模板。

```jinja2
{%- for item in add_dcctemplate_list -%}
    ADD DCCTEMPLATE:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.QHT is not none -%}
        QHT={{item.QHT}},
    {%- endif -%}
    {%- if item.VQT is not none -%}
        VQT={{item.VQT}},
    {%- endif -%}
    {%- if item.TQT is not none -%}
        TQT={{item.TQT}},
    {%- endif -%}
    {%- if item.VALIDTIME is not none -%}
        VALIDTIME={{item.VALIDTIME}},
    {%- endif -%}
    {%- if item.RATTRIGGER is not none -%}
        RATTRIGGER={{item.RATTRIGGER}},
    {%- endif -%}
    {%- if item.SGSNTRIGGER is not none -%}
        SGSNTRIGGER={{item.SGSNTRIGGER}},
    {%- endif -%}
    {%- if item.QOSTRIGGER is not none -%}
        QOSTRIGGER={{item.QOSTRIGGER}},
    {%- endif -%}
    {%- if item.ULITRIGGER is not none -%}
        ULITRIGGER={{item.ULITRIGGER}},
    {%- endif -%}
    {%- if item.SERVICETRIGGER is not none -%}
        SERVICETRIGGER={{item.SERVICETRIGGER}},
    {%- endif -%}
    {%- if item.CCRINITRGNUM is not none -%}
        CCRINITRGNUM={{item.CCRINITRGNUM}},
    {%- endif -%}
    {%- if item.LACTRIGGER is not none -%}
        LACTRIGGER={{item.LACTRIGGER}},
    {%- endif -%}
    {%- if item.MCCTRIGGER is not none -%}
        MCCTRIGGER={{item.MCCTRIGGER}},
    {%- endif -%}
    {%- if item.MNCTRIGGER is not none -%}
        MNCTRIGGER={{item.MNCTRIGGER}},
    {%- endif -%}
    {%- if item.QCT is not none -%}
        QCT={{item.QCT}},
    {%- endif -%}
    {%- if item.UETZTRIGGER is not none -%}
        UETZTRIGGER={{item.UETZTRIGGER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.1 配置CCR-I消息中允许携带的RG的最大个数。配置参数“CCRINITRGNUM”

#### 2.2 配置剩余流量配额小于VQT后向OCS发起CCR。配置参数“VQT”

#### 2.3 配置剩余时长配额小于TQT后向OCS发起CCR。配置参数“TQT”

#### “VQT”和“TQT”配置值不建议小于20，建议保持默认配置。

#### 2.4 配置剩余事件配额小于UQT后向OCS发起CCR。配置参数“UQT”

#### 2.5 配置配额能使用的有效时长超时后向OCS发起CCR。配置参数“VALIDTIME”

#### 2.6 配置当用户数据包停止传送时长超过QHT后向OCS发起CCR。配置参数“QHT”

##### 2.6.1 如果不想使用该功能，即无论用户停止数据传送多长时间也不触发CCR，则可以在OCS上指定CCA中携带的Quota-Holding-Time AVP值为0，或CCA中不携带Quota-Holding-Time AVP，且GGSN/PGW-C本地配置QHT为0。

##### 2.6.2 在没有明确需求的情况下建议不使用QHT，配置为0。

##### 2.6.3 当QHT不为0时QHT必须大于QCT（Quota Consumption Time）。

#### 2.7 尚未申请过配额的新业务触发向OCS发起CCR。配置参数“SERVICETRIGGER”

#### 以下为配置PDP上下文/EPS承载更新场景（RAT改变、SGSN/S-GW地址改变、QoS改变、用户位置信息ULI改变（包括用户MCC、MNC改变）、终端时区改变触发的PDP上下文/EPS承载更新）触发CCR。

#### 2.8 配置RAT改变发送CCR。配置参数“RATTRIGGER”

#### 2.9 配置SGSN/S-GW地址改变发送CCR。配置参数“SGSNTRIGGER”

#### 2.10 配置QoS改变发送CCR。配置参数“QOSTRIGGER”

#### 2.11 配置ULI改变发送CCR。配置参数“ULITRIGGER”

#### 2.12 配置终端时区改变发送CCR。配置参数“UETZTRIGGER”

#### 2.13 配置终端的MCC改变发送CCR。配置参数“MCCTRIGGER”

#### 2.14 配置终端的MNC改变发送CCR。配置参数“MNCTRIGGER”

#### 2.15 配置终端的LAC改变发送CCR。配置参数“LACTRIGGER”

#### 2.16 配置终端的eNodeB改变发送CCR。配置参数“ENBTRIGGER”

#### 2.17 配置终端的RAC改变发送CCR。配置参数“RACTRIGGER”

#### 2.18 配置终端的CellID改变发送CCR。配置参数“CELLIDTRIGGER”

### 3 配置PDP上下文/EPS承载激活时发送CCR-I与OCS交互。

#### 3.1 配置在线计费用户激活时候需要与OCS交互。

```jinja2
{%- for item in set_ocsinit_list -%}
    SET OCSINIT:
    {#- --- 必选参数 --- -#}
    DCCTMPLTNAME="{{item.DCCTMPLTNAME}}",
    OCSINIT={{item.OCSINIT}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：OCSINIT=ENABLE 时可选 --- -#}
    {%- if item.OCSINIT == 'ENABLE' -%}
        {%- if item.WAITOCSRESP is not none -%}
            WAITOCSRESP={{item.WAITOCSRESP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置用户激活时CCR-I消息要携带的费率标识（RG），具体步骤请参见配置在线计费的费率标识。

##### 3.2.1 配置URR。

```jinja2
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
```

##### 3.2.2 配置上行和下行发起的业务对应的URR。

```jinja2
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
```

```jinja2
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
```

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DFTURRGRPNAME is not none -%}
        DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置在线计费用户激活时CCR-I消息中携带指定的费率标识。

```jinja2
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
```

#### 此命令只对内容计费用户生效，PDP级别计费用户不适用该命令。PDP级别计费用户CCR-Initial中携带UserProfile下或者全局下配置的默认计费属性，其中UserProfile优先。如果UserProfile下没有配置CCR-Initial的计费属性，则使用配置在全局下的CCR-Initial的计费属性。如果全局下没有配置CCR-Initial的计费属性，则CCR-Initial不携带计费属性。

#### **ADD DCCTEMPLATE**命令配置CCR-I消息中允许携带的RG的最大个数时要与**SET CTXSTARTRATING**命令配合使用。如果在**SET CTXSTARTRATING**命令中指定了N个RG，则**ADD DCCTEMPLATE**命令配置CCR-I消息中允许携带的RG的最大个数至少要配置为N，才能使得上述N个RG都能被CCR-I消息带上申请配额。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCCTEMPLATE is not none -%}
        DCCTEMPLATE="{{item.DCCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.CCCONFIGMODE is not none -%}
            CCCONFIGMODE={{item.CCCONFIGMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMEISVSEGNAME is not none -%}
            IMEISVSEGNAME="{{item.IMEISVSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.IMSIMSSEGNAME is not none -%}
            IMSIMSSEGNAME="{{item.IMSIMSSEGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.LOCGROUPNAME is not none -%}
            LOCGROUPNAME="{{item.LOCGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.RAT is not none -%}
            RAT={{item.RAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC 时可选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        {%- if item.SEGGROUPNAME is not none -%}
            SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

