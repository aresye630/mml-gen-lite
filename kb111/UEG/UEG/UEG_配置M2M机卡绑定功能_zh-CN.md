---
id: GWFD-024504
name: 配置M2M机卡绑定功能
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员通过PGW Web LMT设置M2M用户的机卡绑定功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-024500 UDM BE基本功能","GWFD-024504 M2M应用","配置M2M机卡绑定功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员通过PGW Web LMT设置M2M用户的机卡绑定功能。

## 必备事项
前提条件

* 已完成对接数据配置。
* 操作人员已完全了解WHFD-220000 M2M应用特性概述。
* 操作人员具有业务发放权限。
* 已完成开户数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_mapserv_list:
      type: items
      properties:
        EPC_CHECK_IMEI:
          name: 'EPC_CHECK_IMEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_mapconf_list:
      type: items
      properties:
        UPLFAILED_NOIMEI:
          name: 'UPLFAILED_NOIMEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_udmserv_list:
      type: items
      properties:
        NGC_CHECK_IMEI:
          name: 'NGC_CHECK_IMEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGC_FAILED_NOIMEI:
          name: 'NGC_FAILED_NOIMEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imeibind_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OPTIONTYPE:
          name: 'OPTIONTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEI:
          name: 'IMEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DELAYCANCEL:
          name: 'DELAYCANCEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_mapserv_list:
    - EPC_CHECK_IMEI: Check_S6aS6d
    set_mapconf_list:
    - UPLFAILED_NOIMEI: FALSE
    set_udmserv_list:
    - NGC_CHECK_IMEI: TRUE
      NGC_FAILED_NOIMEI: FALSE
    mod_imeibind_list:
    - IMSI: '460000000000000'
      OPTIONTYPE: PROVIDE
      IMEI: '12345678901234'
      DELAYCANCEL: FALSE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 根据现网实际情况，开启EPS域或5GC域IMEI检查。

#### 2.1 EPS域

##### 2.1.1 执行**SET MAPSERV**命令，设置开启EPS域IMEI检查。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list step_id=2.1.1 -->
```

##### 2.1.2 执行**SET MAPCONF**命令，设置用户位置更新不携带IMEI时，位置更新流程返回成功响应。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapconf_list的变量区（command: SET MAPCONF） -#}
<!-- MISSING_MACRO: command=SET MAPCONF list_name=set_mapconf_list step_id=2.1.2 -->
```

#### 2.2 5GC域

#### 执行**SET UDMSERV**命令，设置开启5GC域IMEI检查，并设置AMF未携带PEI时允许用户接入5GC网络。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=2.2 -->
```

### 3 执行**MOD IMEIBIND**命令为用户签约M2M绑定业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_imeibind_list的变量区（command: MOD IMEIBIND） -#}
<!-- MISSING_MACRO: command=MOD IMEIBIND list_name=mod_imeibind_list step_id=3 -->
```

