---
id: ''
name: 配置离线计费参数
ne_type: UNC
type: feature
description: 本指导描述UNC离线计费模板相关参数的配置过程。离线计费参数可基于User Profile、APN、Charge Characteristic、全局多个层次进行配置，优先级依次降低。如果高一级的计费参数模板没有配置，则取用下一级的计费参数配置模板。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","SMF配置","离线计费配置","离线计费模板及交互配置","配置离线计费参数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述UNC离线计费模板相关参数的配置过程。离线计费参数可基于User Profile、APN、Charge Characteristic、全局多个层次进行配置，优先级依次降低。如果高一级的计费参数模板没有配置，则取用下一级的计费参数配置模板。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 已完成计费属性、APN、User Profile创建。
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
          description: '离线计费模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
          description: '配置话单协议版本  说明：  如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。'
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
        TQM:
          name: '时长配额机制'
          type: string
          enum:
          - CTP
          - OPERATOR_CTP
          - QCT
          required: false
          description: '配置时长计费方式。'
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
        RECORDSEQNUMBER:
          name: 'Record Sequence Number字段起始值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: 'Record Sequence Number字段起始值。'
          data_source: '与对端协商'
          pattern: ''
          default: 0
        CDRTIMEFORMAT:
          name: '话单时间格式'
          type: string
          enum:
          - LOCAL_TIME
          - UTC
          required: false
          description: '配置话单时间格式。'
          data_source: '与对端协商'
          pattern: ''
          default: LOCAL_TIME
        QHTVALUE:
          name: 'QHT时长（秒）'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: '配置QHT时长。'
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
          description: '配置控制话单生成条件中的计费阈值。'
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
        MINVOLTHRESHOLD:
          name: '最小流量阈值（千字节）'
          type: integer
          minimum: 0
          maximum: 65535
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
          data_source: '与对端协商'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report生成话单的阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置话单产生条件。通过话单生成条件配置可以区分不同条件生成中间话单，达到区分不同条件收取不同费率的。另外通过话单产生条件和话单阈值结合可以控制话单生成速率。'
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
        CDRTRIGSNCHNG:
          name: 'Serving Node更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGMOEXC:
          name: 'CDR MO Exception Data Counter更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
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
        CDRTRIGMOEXCPRI:
          name: 'MO Exception Data Counter更新优先级'
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
          description: '配置话单容器产生条件。'
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
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGSNCHNG:
          name: 'Serving Node更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGCGISAI:
          name: 'CGI/SAI更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGECGI:
          name: 'ECGI更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGTAI:
          name: 'TAI更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGULI:
          name: 'ULI更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGPLMNID:
          name: 'Container Serving Node PLMN标识更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGRAI:
          name: 'RAI更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGTARRIF:
          name: '费率切换'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
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
        CONTTRIGENB:
          name: 'eNodeB更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPLANECHNG:
          name: '用户面更新'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPLMNRATECHNG:
          name: '服务PLMN控制速率改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECHNG:
          name: 'APN控制速率改变'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECHNGCLOSECAUSE:
          name: 'APN速率控制改变流量容器关闭原因值'
          type: string
          enum:
          - APN_RATE_CONTROL_CHANGE
          - SERVINGPLMN_RATE_CONTROL_CHANGE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '为User Profile对象绑定离线计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNOFCTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
          maxLength: 63
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
          description: '为APN实例绑定离线计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNOFCTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '基于Charge Characteristic配置全局离线计费模板。'
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
          description: '配置GLOBAL类型的全局离线计费模板。'
          data_source: '固定取值'
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
    set_ofccdrpara_list:
      type: items
      properties:
        SPCDRCONTROL:
          name: 'SP合一网关话单控制'
          type: string
          enum:
          - PGW_CDR
          - PGW_SGW_CDR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ofctemplate_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      GCDRVERSION: R10_PGW_CDR
      PGWCDRVERSION: R10_PGW_CDR
      SGWCDRVERSION: R10_SGW_CDR
      TQM: QCT
      QCTVALUE: 0
      RECORDSEQNUMBER: 1
      CDRTIMEFORMAT: LOCAL_TIME
      QHTVALUE: 0
      BTIVALUE: 60
    set_ofcthreshold_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      THRESHINHERIT: NON_INHERIT
      TIMETHRESHOLD: 120
      VOLUMETHRESHOLD: 10240
      MINVOLTHRESHOLD: 20
      CONDITIONCHANGE: 3
      SERVINGNODECHNG: 3
      MAXSVCCONTAINER: 20
      TIMETHRESHCCFH: 4294967295
      VOLTHRESHCCFH: 9000000001
      SECRUTHRESHOLD: 3
    set_cdrtrigger_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      CDRTRIGRATCHNG: ENABLE
      CDRTRIGSNCHNG: ENABLE
      CDRTRIGMAXCHNG: ENABLE
      CDRTRIGTIMEZONE: ENABLE
      CDRTRIGPLMNCHNG: ENABLE
      CDRTRIGMOEXC: ENABLE
      CDRTRIGRATPRIOR: '-'
      CDRTRIGSNPRIOR: '-'
      CDRTRIMAXCHGPRI: '-'
      CDRTRIGPLMNPRIO: '-'
      CDRTRIGMOEXCPRI: '-'
      CDRTRIGTZPRIOR: ''
    set_containertrigger_list:
    - OFCTEMPLATENAME: 'offlinecharge-test'
      CONTTRIGRATCHNG: ENABLE
      CONTTRIGQOSCHNG: ENABLE
      CONTTRIGSNCHNG: ENABLE
      CONTTRIGCGISAI: DISABLE
      CONTTRIGECGI: DISABLE
      CONTTRIGTAI: DISABLE
      CONTTRIGULI: DISABLE
      CONTTRIGPLMNID: ENABLE
      CONTTRIGRAI: DISABLE
      CONTTRIGTARRIF: ENABLE
      PCCINIT: DISABLE
      CONTTRIGENB: ENABLE
      USERPLANECHNG: ENABLE
      SPLMNRATECHNG: ENABLE
      APNRATECHNG: ENABLE
      APNRATECHNGCLOSECAUSE: SERVINGPLMN_RATE_CONTROL_CHANGE
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      PGWOFCTEMPLATE: 'offlinecharge-test'
      SGWOFCTEMPLATE: 'offlinecharge-test'
      GGSNOFCTEMPLATE: 'offlinecharge-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      PGWOFCTEMPLATE: 'offlinecharge-test'
      SGWOFCTEMPLATE: 'offlinecharge-test'
      GGSNOFCTEMPLATE: 'offlinecharge-test'
    add_glbofctemplate_list:
    - GLOBALFLAG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      CCMASK: '0xFFFF'
      CCPRIORITY: 1
      PGWTEMPLATE: 'offlinecharge-test'
      SGWTEMPLATE: 'offlinecharge-test'
      GGSNTEMPLATE: 'offlinecharge-test'
    add_glbofctemplate_list_1:
    - GLOBALFLAG: GLOBAL
      PGWTEMPLATE: 'offlinecharge-test'
      SGWTEMPLATE: 'offlinecharge-test'
      GGSNTEMPLATE: 'offlinecharge-test'
      CCMASK: ''
      CCPRIORITY: ''
      CCVALUE: ''
    set_ofccdrpara_list:
    - SPCDRCONTROL: PGW-CDR
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置离线计费模板下的计费参数。

#### 1.1 配置话单版本信息、产生话单的时间格式、Record Sequence Number字段的起始值、定时器QHT信息和计费方式等。

```jinja2
{%- for item in add_ofctemplate_list -%}
    ADD OFCTEMPLATE:
    {#- --- 必选参数 --- -#}
    OFCTEMPLATENAME="{{item.OFCTEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GCDRVERSION is not none -%}
        GCDRVERSION={{item.GCDRVERSION}},
    {%- endif -%}
    {%- if item.PGWCDRVERSION is not none -%}
        PGWCDRVERSION={{item.PGWCDRVERSION}},
    {%- endif -%}
    {%- if item.SGWCDRVERSION is not none -%}
        SGWCDRVERSION={{item.SGWCDRVERSION}},
    {%- endif -%}
    {%- if item.TQM is not none -%}
        TQM={{item.TQM}},
    {%- endif -%}
    {%- if item.RECORDSEQNUMBER is not none -%}
        RECORDSEQNUMBER={{item.RECORDSEQNUMBER}},
    {%- endif -%}
    {%- if item.CDRTIMEFORMAT is not none -%}
        CDRTIMEFORMAT={{item.CDRTIMEFORMAT}},
    {%- endif -%}
    {%- if item.QHTVALUE is not none -%}
        QHTVALUE={{item.QHTVALUE}},
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
        {%- if item.MINVOLTHRESHOLD is not none -%}
            MINVOLTHRESHOLD={{item.MINVOLTHRESHOLD}},
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
    {#- --- 条件可选：THRESHINHERIT=NON_INHERIT 时可选 --- -#}
    {%- if item.THRESHINHERIT == 'NON_INHERIT' -%}
        {%- if item.SECRUTHRESHOLD is not none -%}
            SECRUTHRESHOLD={{item.SECRUTHRESHOLD}},
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
    {%- if item.CDRTRIGSNCHNG is not none -%}
        CDRTRIGSNCHNG={{item.CDRTRIGSNCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGMAXCHNG is not none -%}
        CDRTRIGMAXCHNG={{item.CDRTRIGMAXCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGTIMEZONE is not none -%}
        CDRTRIGTIMEZONE={{item.CDRTRIGTIMEZONE}},
    {%- endif -%}
    {%- if item.CDRTRIGPLMNCHNG is not none -%}
        CDRTRIGPLMNCHNG={{item.CDRTRIGPLMNCHNG}},
    {%- endif -%}
    {%- if item.CDRTRIGMOEXC is not none -%}
        CDRTRIGMOEXC={{item.CDRTRIGMOEXC}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CDRTRIGMOEXC=ENABLE 时可选 --- -#}
    {%- if item.CDRTRIGMOEXC == 'ENABLE' -%}
        {%- if item.CDRTRIGMOEXCPRI is not none -%}
            CDRTRIGMOEXCPRI={{item.CDRTRIGMOEXCPRI}},
        {%- endif -%}
    {%- endif -%}
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
    {%- if item.CONTTRIGRATCHNG is not none -%}
        CONTTRIGRATCHNG={{item.CONTTRIGRATCHNG}},
    {%- endif -%}
    {%- if item.CONTTRIGQOSCHNG is not none -%}
        CONTTRIGQOSCHNG={{item.CONTTRIGQOSCHNG}},
    {%- endif -%}
    {%- if item.CONTTRIGSNCHNG is not none -%}
        CONTTRIGSNCHNG={{item.CONTTRIGSNCHNG}},
    {%- endif -%}
    {%- if item.CONTTRIGCGISAI is not none -%}
        CONTTRIGCGISAI={{item.CONTTRIGCGISAI}},
    {%- endif -%}
    {%- if item.CONTTRIGECGI is not none -%}
        CONTTRIGECGI={{item.CONTTRIGECGI}},
    {%- endif -%}
    {%- if item.CONTTRIGTAI is not none -%}
        CONTTRIGTAI={{item.CONTTRIGTAI}},
    {%- endif -%}
    {%- if item.CONTTRIGULI is not none -%}
        CONTTRIGULI={{item.CONTTRIGULI}},
    {%- endif -%}
    {%- if item.CONTTRIGPLMNID is not none -%}
        CONTTRIGPLMNID={{item.CONTTRIGPLMNID}},
    {%- endif -%}
    {%- if item.CONTTRIGRAI is not none -%}
        CONTTRIGRAI={{item.CONTTRIGRAI}},
    {%- endif -%}
    {%- if item.CONTTRIGTARRIF is not none -%}
        CONTTRIGTARRIF={{item.CONTTRIGTARRIF}},
    {%- endif -%}
    {%- if item.CONTTRIGENB is not none -%}
        CONTTRIGENB={{item.CONTTRIGENB}},
    {%- endif -%}
    {%- if item.USERPLANECHNG is not none -%}
        USERPLANECHNG={{item.USERPLANECHNG}},
    {%- endif -%}
    {%- if item.SPLMNRATECHNG is not none -%}
        SPLMNRATECHNG={{item.SPLMNRATECHNG}},
    {%- endif -%}
    {%- if item.APNRATECHNG is not none -%}
        APNRATECHNG={{item.APNRATECHNG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONTTRIGQOSCHNG=ENABLE 时可选 --- -#}
    {%- if item.CONTTRIGQOSCHNG == 'ENABLE' -%}
        {%- if item.PCCINIT is not none -%}
            PCCINIT={{item.PCCINIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：APNRATECHNG=ENABLE 时可选 --- -#}
    {%- if item.APNRATECHNG == 'ENABLE' -%}
        {%- if item.APNRATECHNGCLOSECAUSE is not none -%}
            APNRATECHNGCLOSECAUSE={{item.APNRATECHNGCLOSECAUSE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置离线计费模板绑定User Profile对象。

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
    {%- if item.GGSNOFCTEMPLATE is not none -%}
        GGSNOFCTEMPLATE="{{item.GGSNOFCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置离线计费模板绑定APN对象。

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
    {%- if item.GGSNOFCTEMPLATE is not none -%}
        GGSNOFCTEMPLATE="{{item.GGSNOFCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置离线计费模板绑定计费属性CC。

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

### 5 配置离线计费模板绑定全局。

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
    {#- --- 条件可选：GLOBALFLAG=GLOBAL/CHARGE_CHARACT 时可选 --- -#}
    {%- if item.GLOBALFLAG in ['GLOBAL', 'CHARGE_CHARACT'] -%}
        {%- if item.GGSNTEMPLATE is not none -%}
            GGSNTEMPLATE="{{item.GGSNTEMPLATE}}",
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
    ;
{%- endfor -%}
```

### 6 配置SP合一用户只产生PGW-CDR还是同时产生SGW-CDR和PGW-CDR话单。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.SPCDRCONTROL is not none -%}
        SPCDRCONTROL={{item.SPCDRCONTROL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

