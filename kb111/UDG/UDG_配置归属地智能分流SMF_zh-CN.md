---
id: ''
name: 配置归属地智能分流SMF
ne_type: UDG
type: feature
description: 本操作用于指导在智能分流SMF上基于专用DNN配置园区内专网UPF分流功能。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置用户在园区内专网UPF分流（可选）","基于专用DNN配置","配置归属地智能分流SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在智能分流SMF上基于专用DNN配置园区内专网UPF分流功能。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apnarea_list:
      type: items
      properties:
        AREANAME:
          name: 'APN相关服务区域'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'APN服务区域类型'
          type: string
          required: false
          description: '通用DNN漫游分流方案仅支持5G会话专网UPF分流，服务区域类型需为5G TAI类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnareabndn2tai_list:
      type: items
      properties:
        AREANAME:
          name: '服务区域名称'
          type: string
          required: false
          description: '一个AREANAME可以绑定多个5G TAI区域范围。同一个AREANAME下TAI区域不能有交叠，不同AREANAME下TAI区域不做限制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: '服务区名称支持5GTAI范围的起始值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: '服务区名称支持5GTAI范围的结束值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_muldnnbindarea_list:
      type: items
      properties:
        DEDDNN:
          name: '智能分流专网DNN'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREANAME:
          name: '服务区域名称'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_muldnnulclmode_list:
      type: items
      properties:
        DEDDNN:
          name: '智能分流专网DNN'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULCLDEPLOYMODE:
          name: 'ULCL部署模式'
          type: string
          required: false
          description: '指定区域优先专网UPF分流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_virtualupfid_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          required: false
          description: '该实例为智能分流UPF与专网UPF合一部署的实例ID。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vupfidbindfunc_list:
      type: items
      properties:
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          required: false
          description: '该参数通过**LST VIRTUALUPFID**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FUNCNAME:
          name: '功能名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_apnarea_list:
    - AREANAME: dnarea1
      AREATYPE: N2TAI
    add_apnareabndn2tai_list:
    - AREANAME: dnarea1
      N2BEGINTAI: '123003000001'
      N2ENDTAI: '123003123456'
    add_muldnnbindarea_list:
    - DEDDNN: stjwt.gd
      AREANAME: dnarea1
    add_muldnnulclmode_list:
    - DEDDNN: stjwt.gd
      ULCLDEPLOYMODE: AREADEDUPFPREFER
    add_virtualupfid_list:
    - UPFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E1313000001
      VUPFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E131300000A
    add_vupfidbindfunc_list:
    - VUPFINSTANCEID: 5EA7F228-47CC-2032-03A3-0E131300000A
      FUNCNAME: MulDNN
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加5G类型的TAI服务区域。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnarea_list的变量区（command: ADD APNAREA） -#}
<!-- MISSING_MACRO: command=ADD APNAREA list_name=add_apnarea_list step_id=1 -->
```

### 2 增加服务区域的TAI绑定范围。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apnareabndn2tai_list的变量区（command: ADD APNAREABNDN2TAI） -#}
<!-- MISSING_MACRO: command=ADD APNAREABNDN2TAI list_name=add_apnareabndn2tai_list step_id=2 -->
```

### 3 绑定专网DNN和服务区域。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_muldnnbindarea_list的变量区（command: ADD MULDNNBINDAREA） -#}
<!-- MISSING_MACRO: command=ADD MULDNNBINDAREA list_name=add_muldnnbindarea_list step_id=3 -->
```

### 4 配置智能分流专网DNN的ULCL部署模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_muldnnulclmode_list的变量区（command: ADD MULDNNULCLMODE） -#}
<!-- MISSING_MACRO: command=ADD MULDNNULCLMODE list_name=add_muldnnulclmode_list step_id=4 -->
```

### 5 配置UPF虚拟实例标识。请使用LST VIRTUALUPFID查询UPF是否有配置虚拟实例ID，“UPFINSTANCEID”为智能分流UPF和专网UPF的实例ID。

### 若未配置虚拟实例ID则执行ADD VIRTUALUPFID和ADD VUPFIDBINDFUNC配置虚拟实例ID和开启多DNN开关。

### 若已配置虚拟实例ID则执行ADD VUPFIDBINDFUNC开启多DNN开关，虚拟实例ID请使用LST VIRTUALUPFID命令查询到的“虚拟UPF实例标识”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_virtualupfid_list的变量区（command: ADD VIRTUALUPFID） -#}
<!-- MISSING_MACRO: command=ADD VIRTUALUPFID list_name=add_virtualupfid_list step_id=5 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vupfidbindfunc_list的变量区（command: ADD VUPFIDBINDFUNC） -#}
<!-- MISSING_MACRO: command=ADD VUPFIDBINDFUNC list_name=add_vupfidbindfunc_list step_id=5 -->
```

