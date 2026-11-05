---
id: ''
name: 配置离线计费参数
ne_type: UDG
type: feature
description: 本指导描述UNC离线计费模板相关参数的配置过程。离线计费参数可基于User Profile、APN、Charge Characteristic、全局多个层次进行配置，优先级依次降低。如果高一级的计费参数模板没有配置，则取用下一级的计费参数配置模板。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","离线计费配置","离线计费模板及交互配置","配置离线计费参数"]
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
          required: false
          description: '离线计费模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TQM:
          name: '时长配额机制'
          type: string
          required: false
          description: '配置时长计费方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QCTVALUE:
          name: 'QCT时长（秒）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QHTVALUE:
          name: 'QHT时长（秒）'
          type: string
          required: false
          description: '配置QHT时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GCDRVERSION:
          name: 'G-CDR版本'
          type: string
          required: false
          description: '配置话单协议版本  说明：  如果部署GUL切换网络，话单版本应该配置为R8及以后的版本。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PGWCDRVERSION:
          name: 'PGW-CDR版本'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SGWCDRVERSION:
          name: 'SGW-CDR版本'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RECORDSEQNUMBER:
          name: 'Record Sequence Number字段起始值'
          type: string
          required: false
          description: 'Record Sequence Number字段起始值。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CDRTIMEFORMAT:
          name: '话单时间格式'
          type: string
          required: false
          description: '配置话单时间格式。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_ofcthreshold_list:
      type: items
      properties:
        OFCTEMPLATENAME:
          name: '离线计费模板名'
          type: string
          required: false
          description: '配置控制话单生成条件中的计费阈值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        THRESHINHERIT:
          name: '继承上一级配置'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONDITIONCHANGE:
          name: '计费条件改变阈值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLUMETHRESHOLD:
          name: '流量阈值（千字节）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MINVOLTHRESHOLD:
          name: '最小流量阈值（千字节）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMETHRESHOLD:
          name: '时长阈值（分）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVINGNODECHNG:
          name: 'Serving Node改变次数阈值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXSVCCONTAINER:
          name: '最大携带的业务容器数量'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        TIMETHRESHCCFH:
          name: '在线计费转离线计费后的时长阈值（分钟）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLTHRESHCCFH:
          name: '在线计费转离线计费后的流量阈值（千字节）'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECRUTHRESHOLD:
          name: 'RAN-SecondaryRAT-Usage-Report生成话单的阈值'
          type: string
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
          required: false
          description: '配置话单产生条件。通过话单生成条件配置可以区分不同条件生成中间话单，达到区分不同条件收取不同费率的。另外通过话单产生条件和话单阈值结合可以控制话单生成速率。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CDRTRIGRATCHNG:
          name: 'CDR RAT更新'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CDRTRIGRATPRIOR:
          name: 'RAT更新优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGSNCHNG:
          name: 'Serving Node更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGSNPRIOR:
          name: 'Serving Node更新优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGMAXCHNG:
          name: '计费条件改变'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIMAXCHGPRI:
          name: '计费条件改变优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGTIMEZONE:
          name: 'MS时区更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGPLMNCHNG:
          name: 'Serving Node PLMN标识更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGPLMNPRIO:
          name: 'Serving Node PLMN标识优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGMOEXC:
          name: 'CDR MO Exception Data Counter更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CDRTRIGMOEXCPRI:
          name: 'MO Exception Data Counter更新优先级'
          type: string
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
          required: false
          description: '配置话单容器产生条件。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CONTTRIGRATCHNG:
          name: 'Container RAT更新'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONTTRIGQOSCHNG:
          name: 'QoS更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCCINIT:
          name: 'PCRF发起的QoS更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGSNCHNG:
          name: 'Serving Node更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGCGISAI:
          name: 'CGI/SAI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGECGI:
          name: 'ECGI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGTAI:
          name: 'TAI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGULI:
          name: 'ULI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGPLMNID:
          name: 'Container Serving Node PLMN标识更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGRAI:
          name: 'RAI更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGTARRIF:
          name: '费率切换'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONTTRIGENB:
          name: 'eNodeB更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPLANECHNG:
          name: '用户面更新'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPLMNRATECHNG:
          name: '服务PLMN控制速率改变'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECHNG:
          name: 'APN控制速率改变'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNRATECHNGCLOSECAUSE:
          name: 'APN速率控制改变流量容器关闭原因值'
          type: string
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
          required: false
          description: '为User Profile对象绑定离线计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNOFCTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
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
          required: false
          description: '为APN实例绑定离线计费模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWOFCTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWOFCTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNOFCTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
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
          required: false
          description: '基于Charge Characteristic配置全局离线计费模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCMASK:
          name: 'CCMASK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: 'CCPRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
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
          required: false
          description: '配置GLOBAL类型的全局离线计费模板。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PGWTEMPLATE:
          name: 'PGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SGWTEMPLATE:
          name: 'SGW离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GGSNTEMPLATE:
          name: 'GGSN离线计费模板名'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        SPCDRCONTROL:
          name: 'SPCDRCONTROL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ofctemplate_list:
    - OFCTEMPLATENAME: offlinecharge-test
      TQM: QCT
      QCTVALUE: '0'
      QHTVALUE: '0'
      GCDRVERSION: R10_PGW_CDR
      PGWCDRVERSION: R10_PGW_CDR
      SGWCDRVERSION: R10_SGW_CDR
      RECORDSEQNUMBER: '1'
      CDRTIMEFORMAT: LOCAL_TIME
    set_ofcthreshold_list:
    - OFCTEMPLATENAME: offlinecharge-test
      THRESHINHERIT: NON_INHERIT
      CONDITIONCHANGE: '3'
      VOLUMETHRESHOLD: '10240'
      MINVOLTHRESHOLD: '20'
      TIMETHRESHOLD: '120'
      SERVINGNODECHNG: '3'
      MAXSVCCONTAINER: '20'
      TIMETHRESHCCFH: '4294967295'
      VOLTHRESHCCFH: '9000000001'
      SECRUTHRESHOLD: '3'
    set_cdrtrigger_list:
    - OFCTEMPLATENAME: offlinecharge-test
      CDRTRIGRATCHNG: ENABLE
      CDRTRIGRATPRIOR: '-'
      CDRTRIGSNCHNG: ENABLE
      CDRTRIGSNPRIOR: '-'
      CDRTRIGMAXCHNG: ENABLE
      CDRTRIMAXCHGPRI: '-'
      CDRTRIGTIMEZONE: ENABLE
      CDRTRIGPLMNCHNG: ENABLE
      CDRTRIGPLMNPRIO: '-'
      CDRTRIGMOEXC: ENABLE
      CDRTRIGMOEXCPRI: '-'
    set_containertrigger_list:
    - OFCTEMPLATENAME: offlinecharge-test
      CONTTRIGRATCHNG: ENABLE
      CONTTRIGQOSCHNG: ENABLE
      PCCINIT: DISABLE
      CONTTRIGSNCHNG: ENABLE
      CONTTRIGCGISAI: DISABLE
      CONTTRIGECGI: DISABLE
      CONTTRIGTAI: DISABLE
      CONTTRIGULI: DISABLE
      CONTTRIGPLMNID: ENABLE
      CONTTRIGRAI: DISABLE
      CONTTRIGTARRIF: ENABLE
      CONTTRIGENB: ENABLE
      USERPLANECHNG: ENABLE
      SPLMNRATECHNG: ENABLE
      APNRATECHNG: ENABLE
      APNRATECHNGCLOSECAUSE: SERVINGPLMN_RATE_CONTROL_CHANGE
    set_usrprofcharge_list:
    - USRPROFNAME: up-test
      PGWOFCTEMPLATE: offlinecharge-test
      SGWOFCTEMPLATE: offlinecharge-test
      GGSNOFCTEMPLATE: offlinecharge-test
    set_apnchargectrl_list:
    - APN: apn-test
      PGWOFCTEMPLATE: offlinecharge-test
      SGWOFCTEMPLATE: offlinecharge-test
      GGSNOFCTEMPLATE: offlinecharge-test
    add_glbofctemplate_list:
    - GLOBALFLAG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      CCMASK: '0xFFFF'
      CCPRIORITY: '1'
      PGWTEMPLATE: offlinecharge-test
      SGWTEMPLATE: offlinecharge-test
      GGSNTEMPLATE: offlinecharge-test
    add_glbofctemplate_list_1:
    - GLOBALFLAG: GLOBAL
      PGWTEMPLATE: offlinecharge-test
      SGWTEMPLATE: offlinecharge-test
      GGSNTEMPLATE: offlinecharge-test
    set_ofccdrpara_list:
    - SPCDRCONTROL: PGW-CDR
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置离线计费模板下的计费参数。

#### 1.1 配置话单版本信息、产生话单的时间格式、Record Sequence Number字段的起始值、定时器QHT信息和计费方式等。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ofctemplate_list的变量区（command: ADD OFCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD OFCTEMPLATE list_name=add_ofctemplate_list step_id=1.1 -->
```

#### 1.2 配置阈值信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ofcthreshold_list的变量区（command: SET OFCTHRESHOLD） -#}
<!-- MISSING_MACRO: command=SET OFCTHRESHOLD list_name=set_ofcthreshold_list step_id=1.2 -->
```

#### 1.3 配置话单产生条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_cdrtrigger_list的变量区（command: SET CDRTRIGGER） -#}
<!-- MISSING_MACRO: command=SET CDRTRIGGER list_name=set_cdrtrigger_list step_id=1.3 -->
```

#### 1.4 配置话单容器产生条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_containertrigger_list的变量区（command: SET CONTAINERTRIGGER） -#}
<!-- MISSING_MACRO: command=SET CONTAINERTRIGGER list_name=set_containertrigger_list step_id=1.4 -->
```

### 2 配置离线计费模板绑定User Profile对象。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_usrprofcharge_list的变量区（command: SET USRPROFCHARGE） -#}
<!-- MISSING_MACRO: command=SET USRPROFCHARGE list_name=set_usrprofcharge_list step_id=2 -->
```

### 3 配置离线计费模板绑定APN对象。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3 -->
```

### 4 配置离线计费模板绑定计费属性CC。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_glbofctemplate_list的变量区（command: ADD GLBOFCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD GLBOFCTEMPLATE list_name=add_glbofctemplate_list step_id=4 -->
```

### 5 配置离线计费模板绑定全局。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_glbofctemplate_list_1的变量区（command: ADD GLBOFCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD GLBOFCTEMPLATE list_name=add_glbofctemplate_list_1 step_id=5 -->
```

### 6 配置SP合一用户只产生PGW-CDR还是同时产生SGW-CDR和PGW-CDR话单。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ofccdrpara_list的变量区（command: SET OFCCDRPARA） -#}
<!-- MISSING_MACRO: command=SET OFCCDRPARA list_name=set_ofccdrpara_list step_id=6 -->
```

