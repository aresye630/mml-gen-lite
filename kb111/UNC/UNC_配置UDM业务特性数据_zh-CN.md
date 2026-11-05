---
id: ''
name: 配置UDM业务特性数据
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员配置UDM上的5G NAS短消息业务。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core SMSF解决方案","SMSF功能部署","部署业务特性数据","配置UDM业务特性数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员配置UDM上的5G NAS短消息业务。

## 必备事项
前提条件

前提条件

* 请仔细阅读**“UDM产品文档”**-->**“业务部署”**--> **“特性部署”** --> **“UDM 5G UDM FE基本特性” --> “****WHFD-450410 5G NAS短消息特性概述****”**。
* 操作人员具有PGW Web LMT的操作权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_amdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供AM签约数据'
          type: string
          required: false
          description: '固定取值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMSSUBSCRIBED:
          name: '是否允许SMS over NAS'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MTSMS:
          name: '是否允许被叫短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MTSMSBA:
          name: '是否闭锁被叫短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MTSMSBR:
          name: '是否闭锁被叫漫游短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MOSMS:
          name: '是否允许主叫短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MOSMSBA:
          name: '是否闭锁主叫短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MOSMSBR:
          name: '是否闭锁主叫漫游短信'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_udmserv_list:
      type: items
      properties:
        CANCELVLRATSMSFREG:
          name: 'SMSF和VLR单注册'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    mod_amdata_list:
    - IMSI: '123031200100003'
      PROV: TRUE
      SMSSUBSCRIBED: TRUE
      MTSMS: TRUE
      MTSMSBA: TRUE
      MTSMSBR: TRUE
      MOSMS: TRUE
      MOSMSBA: TRUE
      MOSMSBR: TRUE
    set_udmserv_list:
    - CANCELVLRATSMSFREG: TRUE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM业务管理”窗口，参考**“UDM产品文档”**-->**“OM参考”**--> **“PGW Web LMT”** --> **“UDM PGW Web LMT GUI参考” --> “****登录PGW Web LMT MML命令界面****”--> “****登录‘UDM业务管理’窗口****”**。

### 2 执行**MOD AMDATA**命令，为用户签约NAS短消息业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_amdata_list的变量区（command: MOD AMDATA） -#}
<!-- MISSING_MACRO: command=MOD AMDATA list_name=mod_amdata_list step_id=2 -->
```

### 3 执行 **SET UDMSERV**命令，设置UDM业务的“SMSF和VLR单注册”参数为“TRUE”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=3 -->
```

