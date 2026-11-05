---
id: ''
name: 配置费率切换
ne_type: UDG
type: feature
description: UNC支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在UNC上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。  UNC支持如下粒度配置费率切换：“User Profile实例 > APN实例 > 计费属性 > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","离线计费配置","配置费率切换"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持节假日、星期及其费率时段的灵活设置，增强话单的计费信息收集功能。运营商可以在UNC上针对节日、周末和工作日的特定时间段设置不同的计费标准，从而吸引移动用户消费，增加运营商收入。UNC支持如下粒度配置费率切换：“User Profile实例 > APN实例 > 计费属性 > 整机”，优先级依次降低，如果高一优先级的参数没有配置，则默认继承低一优先级的参数配置。

## 必备事项
前提条件

* 请仔细阅读融合计费原理和Ga/Gy接口离线/在线计费。
* 完成加载License。
* 本操作任务涉及的APN/DNN、User Profile、User Profile group已经创建完成，并完成User Profile group与APN/DNN的绑定。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_festival_list:
      type: items
      properties:
        GLOBALFLG:
          name: '全局配置'
          type: string
          required: false
          description: '配置指定日期的费率类型为节假日。   * 该命令可以基于计费属性配置，“CCVALUE”不能取值为“0x0200”，因为统一费率类型的用户费率不变，不会发生费率切换。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性的节假日信息优先级高于全局计费属性的节假日信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MONTH:
          name: '节假日月份'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAY:
          name: '节假日日期'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_weekday_list:
      type: items
      properties:
        GLOBALFLG:
          name: '全局配置'
          type: string
          required: false
          description: '配置计费星期表记录，指定每周日期的费率类型为工作日或周末。   * 该命令可以基于计费属性配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的计费类型不包括统一费率计费。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性的计费星期表记录优先级高于全局计费属性的计费星期表记录。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DAYOFWEEK:
          name: '周日期'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TARIFFTYPE:
          name: '费率类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tariffgroup_list:
      type: items
      properties:
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          required: false
          description: '配置费率切换点。   * 该命令可以基于计费属性配置。 * 由于统一费率计费不涉及费率切换，因此该命令中的“CCVALUE”不能取值为“0x0200”。 * “GLOBALFLG”取值可以为：   + “GLOBAL”：全局计费属性。   + “CHARGE\_CHARACT”：特殊计费属性。 基于特殊计费属性配置的费率切换点优先级高于全局计费属性的费率切换点。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GLOBALFLG:
          name: '全局配置'
          type: string
          required: false
          description: ''
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
        TARIFFTYPE:
          name: '费率类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STARTTIME:
          name: '费率切换起始时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDTIME:
          name: '费率切换终止时间'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_glbtariffgroup_list:
      type: items
      properties:
        GLBTARIFFGRP:
          name: '费率切换组名'
          type: string
          required: false
          description: '配置全局费率切换组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          required: false
          description: '每个DNN只能绑定一个费率切换组。如果DNN已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET APNCHARGECTRL**命令修改原来的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '每个User Profile只能绑定一个费率切换组。如果User Profile下已绑定了费率切换组，要修改为绑定其他的费率切换组，必须先执行**SET USRPROFCHARGE**命令修改原来的绑定关系。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TARIFFGRPNAME:
          name: '费率切换组名'
          type: string
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_festival_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      MONTH: '8'
      DAY: '1'
    add_weekday_list:
    - GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      DAYOFWEEK: MONDAY
      TARIFFTYPE: WORKDAY
    add_tariffgroup_list:
    - TARIFFGRPNAME: tar_nb
      GLOBALFLG: CHARGE_CHARACT
      CCVALUE: '0x0800'
      TARIFFTYPE: WORKDAY
      STARTTIME: 07&00
      ENDTIME: 23&00
    set_glbtariffgroup_list:
    - GLBTARIFFGRP: tar_nb
    set_apnchargectrl_list:
    - APN: apn-test
      TARIFFGRPNAME: tar_nb
    set_usrprofcharge_list:
    - USRPROFNAME: up-test
      TARIFFGRPNAME: tar_nb
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置费率切换。

#### 1.1 配置节假日信息，即设置指定日期的费率类型为节假日。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_festival_list的变量区（command: ADD FESTIVAL） -#}
<!-- MISSING_MACRO: command=ADD FESTIVAL list_name=add_festival_list step_id=1.1 -->
```

#### 1.2 配置星期表信息，即设置指定星期的费率类型为工作日或周末。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_weekday_list的变量区（command: ADD WEEKDAY） -#}
<!-- MISSING_MACRO: command=ADD WEEKDAY list_name=add_weekday_list step_id=1.2 -->
```

#### 1.3 配置节假日，工作日或周末的费率时间段。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tariffgroup_list的变量区（command: ADD TARIFFGROUP） -#}
<!-- MISSING_MACRO: command=ADD TARIFFGROUP list_name=add_tariffgroup_list step_id=1.3 -->
```

### 2 配置全局费率切换组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_glbtariffgroup_list的变量区（command: SET GLBTARIFFGROUP） -#}
<!-- MISSING_MACRO: command=SET GLBTARIFFGROUP list_name=set_glbtariffgroup_list step_id=2 -->
```

### 3 为APN实例绑定费率切换组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnchargectrl_list的变量区（command: SET APNCHARGECTRL） -#}
<!-- MISSING_MACRO: command=SET APNCHARGECTRL list_name=set_apnchargectrl_list step_id=3 -->
```

### 4 为User Profile实例绑定费率切换组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_usrprofcharge_list的变量区（command: SET USRPROFCHARGE） -#}
<!-- MISSING_MACRO: command=SET USRPROFCHARGE list_name=set_usrprofcharge_list step_id=4 -->
```

