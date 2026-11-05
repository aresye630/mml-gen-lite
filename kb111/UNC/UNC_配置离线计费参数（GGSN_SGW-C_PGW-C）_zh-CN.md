---
id: ''
name: 配置离线计费参数（GGSN/SGW-C/PGW-C）
ne_type: UNC
type: feature
description: GGSN/SGW-C/PGW-C上离线计费参数可基于UserProfile、APN、Charge Characteristic、全局多个层次进行配置，优先级依次降低。如果高一级的计费参数模板没有配置，则取用下一级的计费参数配置模板。  适用于SGW-C、PGW-C、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011201 支持离线计费","激活离线计费","配置离线计费参数（GGSN/SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
GGSN/SGW-C/PGW-C上离线计费参数可基于UserProfile、APN、Charge Characteristic、全局多个层次进行配置，优先级依次降低。如果高一级的计费参数模板没有配置，则取用下一级的计费参数配置模板。适用于SGW-C、PGW-C、GGSN。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 完成配置到CG的数据（GGSN/SGW-C/PGW-C）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ofctemplate_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: '计费模板'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TQM:
          name: '时长配额机制'
          type: string
          enum:
          - CTP
          - OPERATOR_CTP
          - QCT
          required: false
          description: '计费方式'
          data_source: '本端规划'
          pattern: ''
          default: QCT
        QCTVALUE:
          name: 'QCT时长（秒）'
          type: integer
          minimum: 0
          maximum: 200
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        QHTVALUE:
          name: 'QHT时长（秒）'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: '定时器信息'
          data_source: '本端规划'
          pattern: ''
          default: 0
        GCDRVERSION:
          name: 'G-CDR版本'
          type: string
          enum:
          - R10_PGW_CDR
          - R4V440
          - R5V560
          - R6V660_EGCDR
          - R6V660_GCDR
          - R7V740_EGCDR
          - R7V740_GCDR
          - R8V850_PGW_CDR
          - R98V760
          - R98_CMCCV130
          - R99V390
          - R99V3A0
          - R9V950_PGW_CDR
          required: false
          description: '话单协议版本  说明：  如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。'
          data_source: '全网规划'
          pattern: ''
          default: R7V740_EGCDR
        PGWCDRVERSION:
          name: 'PGW-CDR版本'
          type: string
          enum:
          - R10_PGW_CDR
          - R8V850_PGW_CDR
          - R9V950_PGW_CDR
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: R8V850_PGW_CDR
        SGWCDRVERSION:
          name: 'SGW-CDR版本'
          type: string
          enum:
          - R10_SGW_CDR
          - R8V850_SGW_CDR
          - R9V950_SGW_CDR
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: R8V850_SGW_CDR
        RECORDSEQNUMBER:
          name: 'Record Sequence Number字段起始值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: 'Record Sequence Number字段起始值'
          data_source: '本端规划'
          pattern: ''
          default: 0
        BTIVALUE:
          name: 'BTI时长（秒）'
          type: integer
          minimum: 60
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
    set_ofcthreshold_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: '配置控制话单生成条件中的计费阈值'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        THRESHINHERIT:
          name: '继承上一级配置'
          type: string
          enum:
          - INHERIT
          - NON_INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONDITIONCHANGE:
          name: '计费条件改变阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMETHRESHOLD:
          name: '流量阈值（千字节）'
          type: integer
          minimum:
          - 0
          - 20
          maximum:
          - 0
          - 9000000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMETHRESHOLD:
          name: '时长阈值（分）'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVINGNODECHNG:
          name: 'Serving Node改变次数阈值'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: integer
          minimum: 1
          maximum: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINVOLTHRESHOLD:
          name: '最小流量阈值（千字节）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report生成话单的阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMETHRESHCCFH:
          name: '在线计费转离线计费后的时长阈值（分钟）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 1440
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLTHRESHCCFH:
          name: '在线计费转离线计费后的流量阈值（千字节）'
          type: integer
          minimum:
          - 0
          - 20
          - 9000000001
          maximum:
          - 0
          - 9000000000
          - 9000000001
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cdrtrigger_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: '话单产生条件'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CDRTRIGRATCHNG:
          name: 'CDR RAT更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIGTIMEZONE:
          name: 'MS时区更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIGPLMNCHNG:
          name: 'Serving Node PLMN标识更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIGSNCHNG:
          name: 'Serving Node更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIGMAXCHNG:
          name: '计费条件改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIMAXCHGPRI:
          name: '计费条件改变优先级'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGPLMNPRIO:
          name: 'Serving Node PLMN标识优先级'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGRATPRIOR:
          name: 'RAT更新优先级'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGSNPRIOR:
          name: 'Serving Node更新优先级'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGTZPRIOR:
          name: 'MS时区优先级'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_containertrigger_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          maxLength: 63
          required: true
          description: '话单容器产生条件'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CONTTRIGRATCHNG:
          name: 'Container RAT更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONTTRIGQOSCHNG:
          name: 'QoS更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCCINIT:
          name: 'PCRF发起的QoS更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
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
          description: '配置UserProfile'
          data_source: '全网规划'
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
          data_source: '全网规划'
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
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProfile对象绑定OFCTemplate模板'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
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
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置APN，可以使用命令**LST APN**查询。'
          data_source: '全网规划'
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
          description: '配置APN实例绑定OFCTemplate模板'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_chargechar_list:
      type: items
      properties:
        CCNAME:
          name: '计费属性名称'
          type: string
          maxLength: 31
          required: true
          description: '增加计费属性'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_glbofctemplate_list:
      type: items
      properties:
        GLOBALFLAG:
          name: '全局记录'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '配置Charge Characteristic类型的全局离线模板'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCMASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        GGSNTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_glbofctemplate_list_1:
      type: items
      properties:
        GLOBALFLAG:
          name: '全局记录'
          type: string
          enum:
          - CHARGE_CHARACT
          - GLOBAL
          required: true
          description: '配置GLOBAL类型的全局离线模板'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PGWTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CCMASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ofctemplate_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      TQM: QCT
      QCTVALUE: 0
      QHTVALUE: 30
      GCDRVERSION: R7V740_GCDR
      PGWCDRVERSION: R8V850_PGW_CDR
      SGWCDRVERSION: R8V850_SGW_CDR
      RECORDSEQNUMBER: 0
      BTIVALUE: 60
    set_ofcthreshold_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      THRESHINHERIT: NON_INHERIT
      CONDITIONCHANGE: 3
      VOLUMETHRESHOLD: 20
      TIMETHRESHOLD: 30
      SERVINGNODECHNG: 5
      MAXSVCCONTAINER: ''
      MINVOLTHRESHOLD: ''
      SECRUTHRESHOLD: ''
      TIMETHRESHCCFH: ''
      VOLTHRESHCCFH: ''
    set_cdrtrigger_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      CDRTRIGRATCHNG: DISABLE
      CDRTRIGTIMEZONE: DISABLE
      CDRTRIGPLMNCHNG: ENABLE
      CDRTRIGSNCHNG: ENABLE
      CDRTRIGMAXCHNG: ENABLE
      CDRTRIMAXCHGPRI: ''
      CDRTRIGPLMNPRIO: ''
      CDRTRIGRATPRIOR: ''
      CDRTRIGSNPRIOR: ''
      CDRTRIGTZPRIOR: ''
    set_containertrigger_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      CONTTRIGRATCHNG: DISABLE
      CONTTRIGQOSCHNG: DISABLE
      PCCINIT: ''
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      PGWOFCTEMPLATE: 'offlinecharge-test'
      SGWOFCTEMPLATE: 'offlinecharge-test'
    add_usrprofgroup_list:
    - USERPROFGNAME: ''
    add_upbindupg_list:
    - USERPROFGNAME: ''
      UPBINDTYPE: ''
      CCCONFIGMODE: ''
      IMEISVSEGNAME: ''
      IMSIMSSEGNAME: ''
      LOCALPCCSELECT: INHERIT
      LOCGROUPNAME: ''
      PRIORITY: ''
      RAT: ''
      ROAMING: ''
      SEGGROUPNAME: ''
      USERPROFILENAME: ''
    add_apnusrprofg_list:
    - APN: ''
      USERPROFGNAME: ''
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      PGWOFCTEMPLATE: 'offlinecharge-test'
      SGWOFCTEMPLATE: 'offlinecharge-test'
    add_chargechar_list:
    - CCNAME: 'testchgcha'
    add_glbofctemplate_list:
    - GLOBALFLAG: CHARGE_CHARACT
      CCVALUE: '0x3'
      CCMASK: '0x3'
      CCPRIORITY: 1
      PGWTEMPLATE: 'offlinecharge-test'
      SGWTEMPLATE: 'offlinecharge-test'
      GGSNTEMPLATE: ''
    add_glbofctemplate_list_1:
    - GLOBALFLAG: GLOBAL
      PGWTEMPLATE: 'offlinecharge-test'
      SGWTEMPLATE: 'offlinecharge-test'
      CCMASK: ''
      CCPRIORITY: ''
      CCVALUE: ''
      GGSNTEMPLATE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置OFCTemplate模板下的计费参数。

#### 1.1 配置话单版本信息、产生话单的时间格式、Record Sequence Number字段的起始值、定时器QHT信息和计费方式。

```jinja2
{%- for item in add_ofctemplate_list -%}
    ADD OFCTEMPLATE:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TQM is not none -%}
        TQM={{item.TQM}},
    {%- endif -%}
    {%- if item.GCDRVERSION is not none -%}
        GCDRVERSION={{item.GCDRVERSION}},
    {%- endif -%}
    {%- if item.PGWCDRVERSION is not none -%}
        PGWCDRVERSION={{item.PGWCDRVERSION}},
    {%- endif -%}
    {%- if item.QHTVALUE is not none -%}
        QHTVALUE={{item.QHTVALUE}},
    {%- endif -%}
    {%- if item.RECORDSEQNUMBER is not none -%}
        RECORDSEQNUMBER={{item.RECORDSEQNUMBER}},
    {%- endif -%}
    {%- if item.SGWCDRVERSION is not none -%}
        SGWCDRVERSION={{item.SGWCDRVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TQM=QCT 时必选 --- -#}
    {%- if item.TQM == 'QCT' -%}
        QCTVALUE={{item.QCTVALUE}},
    {%- endif -%}
    {#- --- 条件必选：TQM=CTP/OPERATOR_CTP 时必选 --- -#}
    {%- if item.TQM in ['CTP', 'OPERATOR_CTP'] -%}
        BTIVALUE={{item.BTIVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置阈值信息。

```jinja2
{%- for item in set_ofcthreshold_list -%}
    SET OFCTHRESHOLD:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.THRESHINHERIT is not none -%}
        THRESHINHERIT={{item.THRESHINHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.VOLUMETHRESHOLD is not none -%}
            VOLUMETHRESHOLD={{item.VOLUMETHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.CONDITIONCHANGE is not none -%}
            CONDITIONCHANGE={{item.CONDITIONCHANGE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.SERVINGNODECHNG is not none -%}
            SERVINGNODECHNG={{item.SERVINGNODECHNG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.MAXSVCCONTAINER is not none -%}
            MAXSVCCONTAINER={{item.MAXSVCCONTAINER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.MINVOLTHRESHOLD is not none -%}
            MINVOLTHRESHOLD={{item.MINVOLTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.SECRUTHRESHOLD is not none -%}
            SECRUTHRESHOLD={{item.SECRUTHRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.TIMETHRESHCCFH is not none -%}
            TIMETHRESHCCFH={{item.TIMETHRESHCCFH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.VOLTHRESHCCFH is not none -%}
            VOLTHRESHCCFH={{item.VOLTHRESHCCFH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置话单产生条件。

```jinja2
{%- for item in set_cdrtrigger_list -%}
    SET CDRTRIGGER:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CDRTRIGRATCHNG is not none -%}
        CDRTRIGRATCHNG={{item.CDRTRIGRATCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGTIMEZONE is not none -%}
        CDRTRIGTIMEZONE={{item.CDRTRIGTIMEZONE}},
    {%- endif -%}
    {%- if item.CDRTRIGPLMNCHNG is not none -%}
        CDRTRIGPLMNCHNG={{item.CDRTRIGPLMNCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGMAXCHNG is not none -%}
        CDRTRIGMAXCHNG={{item.CDRTRIGMAXCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGSNCHNG is not none -%}
        CDRTRIGSNCHNG={{item.CDRTRIGSNCHNG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CDRTRIGPLMNCHNG=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGPLMNCHNG == 'ENABLE' -%}
        {%- if item.CDRTRIGPLMNPRIO is not none -%}
            CDRTRIGPLMNPRIO={{item.CDRTRIGPLMNPRIO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CDRTRIGRATCHNG=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGRATCHNG == 'ENABLE' -%}
        {%- if item.CDRTRIGRATPRIOR is not none -%}
            CDRTRIGRATPRIOR={{item.CDRTRIGRATPRIOR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CDRTRIGSNCHNG=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGSNCHNG == 'ENABLE' -%}
        {%- if item.CDRTRIGSNPRIOR is not none -%}
            CDRTRIGSNPRIOR={{item.CDRTRIGSNPRIOR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CDRTRIGTIMEZONE=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGTIMEZONE == 'ENABLE' -%}
        {%- if item.CDRTRIGTZPRIOR is not none -%}
            CDRTRIGTZPRIOR={{item.CDRTRIGTZPRIOR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CDRTRIGMAXCHNG=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGMAXCHNG == 'ENABLE' -%}
        {%- if item.CDRTRIMAXCHGPRI is not none -%}
            CDRTRIMAXCHGPRI={{item.CDRTRIMAXCHGPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置话单容器产生条件。

```jinja2
{%- for item in set_containertrigger_list -%}
    SET CONTAINERTRIGGER:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONTTRIGQOSCHNG is not none -%}
        CONTTRIGQOSCHNG={{item.CONTTRIGQOSCHNG}},
    {%- endif -%}
    {%- if item.CONTTRIGRATCHNG is not none -%}
        CONTTRIGRATCHNG={{item.CONTTRIGRATCHNG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONTTRIGQOSCHNG=ENABLE 时可选 --- -#}
    {%- if item.CONTTRIGQOSCHNG == 'ENABLE' -%}
        {%- if item.PCCINIT is not none -%}
            PCCINIT={{item.PCCINIT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置OFCTemplate模板绑定UserProfile对象。

#### 2.1 配置UserProfile。如已配置UserProfile，请跳过该步骤。

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

#### 2.2 配置UserProfile对象绑定OFCTemplate模板。

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PGWOFCTEMPLATE is not none -%}
        PGWOFCTEMPLATE="{{item.PGWOFCTEMPLATE}}",
    {%- endif -%}
    {%- if item.SGWOFCTEMPLATE is not none -%}
        SGWOFCTEMPLATE="{{item.SGWOFCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置UserProfileGroup。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

#### 2.4 将UserProfile绑定到UserProfileGroup。

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    UPBINDTYPE={{item.UPBINDTYPE}},
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.UPBINDTYPE == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
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

#### 2.5 将UserProfileGroup绑定到APN实例下。

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

### 3 配置OFCTemplate模板绑定APN对象。

#### 3.1 配置APN。如已配置APN，请跳过该步骤。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 3.2 配置APN实例绑定OFCTemplate模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PGWOFCTEMPLATE is not none -%}
        PGWOFCTEMPLATE="{{item.PGWOFCTEMPLATE}}",
    {%- endif -%}
    {%- if item.SGWOFCTEMPLATE is not none -%}
        SGWOFCTEMPLATE="{{item.SGWOFCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置OFCTemplate模板绑定计费属性CC。

#### 4.1 配置计费属性CC。如已配置CC，请跳过该步骤。

```jinja2
{%- for item in add_chargechar_list -%}
    ADD CHARGECHAR:
    {#- --- 必选参数 --- -#}
    CCNAME="{{item.CCNAME}}",
    ;
{%- endfor -%}
```

#### 4.2 配置计费属性CC绑定OFCTemplate模板。

```jinja2
{%- for item in add_glbofctemplate_list -%}
    ADD GLBOFCTEMPLATE:
    {#- --- 必选参数 --- -#}
    GLOBALFLAG={{item.GLOBALFLAG}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GLOBALFLAG=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GLOBALFLAG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.PGWTEMPLATE is not none -%}
            PGWTEMPLATE="{{item.PGWTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.SGWTEMPLATE is not none -%}
            SGWTEMPLATE="{{item.SGWTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.GGSNTEMPLATE is not none -%}
            GGSNTEMPLATE="{{item.GGSNTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置OFCTemplate模板绑定全局。

```jinja2
{%- for item in add_glbofctemplate_list_1 -%}
    ADD GLBOFCTEMPLATE:
    {#- --- 必选参数 --- -#}
    GLOBALFLAG={{item.GLOBALFLAG}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GLOBALFLAG=CHARGE_CHARACT 时必选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.PGWTEMPLATE is not none -%}
            PGWTEMPLATE="{{item.PGWTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.SGWTEMPLATE is not none -%}
            SGWTEMPLATE="{{item.SGWTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        {%- if item.CCMASK is not none -%}
            CCMASK="{{item.CCMASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG == 'CHARGE_CHARACT' -%}
        {%- if item.CCPRIORITY is not none -%}
            CCPRIORITY={{item.CCPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.GGSNTEMPLATE is not none -%}
            GGSNTEMPLATE="{{item.GGSNTEMPLATE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

