---
id: GWFD-025807
name: 配置基于UDM的P-CSCF故障恢复特性
ne_type: UEG
type: feature
description: 该任务指导操作人员配置UDM支持P-CSCF恢复机制。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-025800 UDM语音基本功能","GWFD-025807 基于UDM的P-CSCF故障恢复","配置基于UDM的P-CSCF故障恢复特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置UDM支持P-CSCF恢复机制。

## 必备事项
前提条件

请仔细阅读GWFD-025807 基于UDM的P-CSCF故障恢复特性概述功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_hsystempara_list:
      type: items
      properties:
        P_CSCF_RESTORE_SUPP:
          name: '是否支持P-CSCF恢复机制'
          type: string
          required: false
          description: '用于标识HSS是否支持P-CSCF恢复机制。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_udmserv_list:
      type: items
      properties:
        NGC_PCSCF_RSD_MODE:
          name: 'P-CSCF容灾模式'
          type: string
          required: false
          description: '用于标识当UDM/UTA同时存储AMF和SMF上报的P-CSCF Restore Callback URI时，UDM/UTA向哪个网元发起P-CSCF故障恢复消息Nudm\_UECM\_PCscfRestoration通知。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_hsystempara_list:
    - P_CSCF_RESTORE_SUPP: TRUE
    set_udmserv_list:
    - NGC_PCSCF_RSD_MODE: SMF
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“IMS-HSS业务管理”窗口。

### 2 执行**SET HSYSTEMPARA**命令开启支持P-CSCF恢复机制。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=2 -->
```

### 3 执行**SET UDMSERV**命令配置P-CSCF容灾模式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=3 -->
```

