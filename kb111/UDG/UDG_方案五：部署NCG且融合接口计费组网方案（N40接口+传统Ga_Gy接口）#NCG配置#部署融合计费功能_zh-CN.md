---
id: ''
name: 部署融合计费功能
ne_type: UDG
type: feature
description: 该任务用于指导操作人员完成5G融合计费所需的相关参数。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","NCG配置","部署融合计费功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务用于指导操作人员完成5G融合计费所需的相关参数。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ccpfot_list:
      type: items
      properties:
        FOTNM:
          name: 'Failover模板标识'
          type: string
          required: false
          description: '在线计费CC处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FOENABLE:
          name: '是否支持Failover开关'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        RESPPLCY:
          name: 'NCG代应答时的配额类型选择'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UVDQ:
          name: '默认上行流量额度(KB)'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DVDQ:
          name: '默认下行流量额度(KB)'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ccpccact_list:
      type: items
      properties:
        CCTYPE:
          name: 'CC类型'
          type: string
          required: false
          description: '离线计费CC处理动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CHGCHAR:
          name: '指定计费属性值'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        CHGCHARMASK:
          name: '指定计费属性掩码'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        FOTNM:
          name: 'Failover模板标识'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FWDOCSENABLE:
          name: '是否转发OCS'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ccprcact_list:
      type: items
      properties:
        RCTYPE:
          name: 'RC类型'
          type: string
          required: false
          description: '异常返回码处理动作。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CODETYPE:
          name: '指定异常返回码类型'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FOTNM:
          name: 'Failover模板标识'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERUNAVAILABLE:
          name: '代表对端不可用'
          type: string
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_agffuncpara_list:
      type: items
      properties:
        OCSRETRYCNT:
          name: '计费消息重发次数'
          type: string
          required: false
          description: '配置AGF的功能参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OCSDISCPLCY:
          name: 'OCS选择策略'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CDFIPKGPLCY:
          name: 'CDF I包抄送策略'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ccptimer_list:
      type: items
      properties:
        TID:
          name: '定时器标识'
          type: string
          required: false
          description: 'OCS超时时长配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '定时器的时长'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ccptimer_list_1:
      type: items
      properties:
        TID:
          name: '定时器标识'
          type: string
          required: false
          description: '尝试恢复OCS时长配置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '定时器的时长'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ccpfot_list:
    - FOTNM: FR1
      FOENABLE: TRUE
      RESPPLCY: TIME-0&SUMVOLUME-1
      UVDQ: '102400'
      DVDQ: '102400'
    add_ccpccact_list:
    - CCTYPE: VALUE
      CHGCHAR: '0x0400'
      CHGCHARMASK: '0xFFFF'
      FOTNM: FR1
      FWDOCSENABLE: TRUE
    add_ccprcact_list:
    - RCTYPE: VALUE
      CODETYPE: '408'
      FOTNM: FR1
      PEERUNAVAILABLE: FALSE
    set_agffuncpara_list:
    - OCSRETRYCNT: '0'
      OCSDISCPLCY: SUPI-0&GPSI-1
      CDFIPKGPLCY: TRUE
    set_ccptimer_list:
    - TID: CCTIMEOUT
      VALUE: '3'
    set_ccptimer_list_1:
    - TID: RECOVERINTERVAL
      VALUE: '300'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置默认Failover模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ccpfot_list的变量区（command: ADD CCPFOT） -#}
<!-- MISSING_MACRO: command=ADD CCPFOT list_name=add_ccpfot_list step_id=1 -->
```

### 2 配置基于CC值的处理模板

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ccpccact_list的变量区（command: ADD CCPCCACT） -#}
<!-- MISSING_MACRO: command=ADD CCPCCACT list_name=add_ccpccact_list step_id=2 -->
```

### 3 配置基于异常返回码的处理模板

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ccprcact_list的变量区（command: ADD CCPRCACT） -#}
<!-- MISSING_MACRO: command=ADD CCPRCACT list_name=add_ccprcact_list step_id=3 -->
```

### 4 配置AGF功能参数。此处配置create消息生成话单、NCG等待OCS计费响应超时后不重发响应超时的计费请求，根据GPSI选择OCS。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_agffuncpara_list的变量区（command: SET AGFFUNCPARA） -#}
<!-- MISSING_MACRO: command=SET AGFFUNCPARA list_name=set_agffuncpara_list step_id=4 -->
```

### 5 CHF(OCS)超时时长配置，默认值为3秒。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ccptimer_list的变量区（command: SET CCPTIMER） -#}
<!-- MISSING_MACRO: command=SET CCPTIMER list_name=set_ccptimer_list step_id=5 -->
```

### 6 主备CHF(OCS)故障后NCG再次尝试转发CHF(OCS)时长配置，默认值为5分钟。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ccptimer_list_1的变量区（command: SET CCPTIMER） -#}
<!-- MISSING_MACRO: command=SET CCPTIMER list_name=set_ccptimer_list_1 step_id=6 -->
```

