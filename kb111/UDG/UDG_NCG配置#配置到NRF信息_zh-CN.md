---
id: ''
name: 配置到NRF信息
ne_type: UDG
type: feature
description: 该任务主要用于NCG向NRF发现OCS等周边NF并订阅后者的状态信息。在对接真实NRF的场景下，需要执行该任务。  NCG信息在SMF本地配置，SMF暂不向NRF查询NCG信息。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","NCG配置","配置到NRF信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务主要用于NCG向NRF发现OCS等周边NF并订阅后者的状态信息。在对接真实NRF的场景下，需要执行该任务。NCG信息在SMF本地配置，SMF暂不向NRF查询NCG信息。

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
    add_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          required: false
          description: '配置NRF信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          required: false
          description: '该命令用于添加NRF实例地址信息。在对接真实NRF的场景下，需要配置该命令。'
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'Ipv6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfaddr_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          required: false
          description: '该命令用于添加NRF实例地址信息。在对接真实NRF的场景下，需要配置该命令。'
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'Ipv6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          required: false
          description: '配置NRF协议参数。'
          data_source: ''
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nfnrfmgmtpara_list:
      type: items
      properties:
        SWITCHMASTERNRF:
          name: '切换主用NRF开关'
          type: string
          required: false
          description: '该命令用于配置NF与NRF间的管理参数。'
          data_source: ''
          pattern: ''
          default: ''
    add_subcondition_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          required: false
          description: '该命令用于增加订阅的目标NF信息。此示例是订阅OCS的状态和信息变更通知。'
          data_source: ''
          pattern: ''
          default: ''
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_agffuncpara_list:
      type: items
      properties:
        OCSRETRYCNT:
          name: '计费消息重发次数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OCSDISCPLCY:
          name: 'OCS选择策略'
          type: string
          required: false
          description: '该命令用于设置AGF的功能参数。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_nrf_list:
    - NRFINSTANCENAME: NRF_Instance_0
      TLS: FALSE
      PRIORITY: '1'
    add_nrfaddr_list:
    - NRFINSTANCENAME: NRF_Instance_0
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: 172.16.1.15
      PORT: '8080'
      IPV6ADDRESS: fd00:f111:2222:3333:4444:5555:2111:151
    add_nrfaddr_list_2:
    - NRFINSTANCENAME: NRF_Instance_1
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: 172.16.1.16
      PORT: '8080'
      IPV6ADDRESS: fd00:f111:2222:3333:4444:5555:2111:152
    add_nrfpara_list:
    - NRFINSTANCENAME: NRF_Instance_0
      WAITINTERVAL: '5'
      MAXRETRYTIMES: '3'
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    set_nfnrfmgmtpara_list:
    - SWITCHMASTERNRF: ON
    add_subcondition_list:
    - NFTYPE: NfCUSTOM_OCS
      CONDITION: NfInstanceId-1&NFType-1&ServiceName-1&AmfRegionId-1&AmfSetId-1&GuamiList-1&PlmnId-1&NetworkSlice-1&NfGroup-1&Rev1-1&Rev2-1&Rev3-1
      REQNOTIFEVENT: NF_REGISTERED-1&NF_DEREGISTERED-1&NF_PROFILE_CHANGED-1
    set_agffuncpara_list:
    - OCSRETRYCNT: '0'
      OCSDISCPLCY: SUPI-0&GPSI-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置主NRF和备NRF实例。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nrf_list的变量区（command: ADD NRF） -#}
<!-- MISSING_MACRO: command=ADD NRF list_name=add_nrf_list step_id=1 -->
```

### 执行ADD NRF命令时严禁配置FQDN参数，不支持SBI接口使用FQDN。

### 2 配置主NRF业务地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nrfaddr_list的变量区（command: ADD NRFADDR） -#}
<!-- MISSING_MACRO: command=ADD NRFADDR list_name=add_nrfaddr_list step_id=2 -->
```

### 3 配置备NRF业务地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nrfaddr_list_2的变量区（command: ADD NRFADDR） -#}
<!-- MISSING_MACRO: command=ADD NRFADDR list_name=add_nrfaddr_list_2 step_id=3 -->
```

### 4 配置与主NRF和备NRF的对接参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_nrfpara_list的变量区（command: ADD NRFPARA） -#}
<!-- MISSING_MACRO: command=ADD NRFPARA list_name=add_nrfpara_list step_id=4 -->
```

### 请提前规划**ADD NRFPARA**中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF对NRF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考UNC产品文档中“网络部署 > 特性部署 > UNC特性指南 > 容灾功能 > WSFD-114002 NRF双活容灾 > WSFD-114002 NRF双活容灾特性概述”中原理概述的可靠性机制。

### 5 配置切换主用NRF开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_nfnrfmgmtpara_list的变量区（command: SET NFNRFMGMTPARA） -#}
<!-- MISSING_MACRO: command=SET NFNRFMGMTPARA list_name=set_nfnrfmgmtpara_list step_id=5 -->
```

### 在NRF主备组网情况下，通过设置“SWITCHMASTERNRF”参数让NF实时感知主用NRF的状态，当主用NRF恢复后，NF切换到主用NRF。

### 6 配置NCG订阅CHF(OCS)等周边NF的状态和信息变更通知。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_subcondition_list的变量区（command: ADD SUBCONDITION） -#}
<!-- MISSING_MACRO: command=ADD SUBCONDITION list_name=add_subcondition_list step_id=6 -->
```

### 7 配置OCS寻址策略。

### 配置通过GPSI寻址OCS。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_agffuncpara_list的变量区（command: SET AGFFUNCPARA） -#}
<!-- MISSING_MACRO: command=SET AGFFUNCPARA list_name=set_agffuncpara_list step_id=7 -->
```

### “OCSRETRYCNT”取值范围为0~1。值为0时，请求消息超时不进行重传，直接查找备OCS。值为1时，请求消息超时后重传1次，再次超时则查找备OCS。

### 如上所示配置表示通过GPSI寻址OCS。

