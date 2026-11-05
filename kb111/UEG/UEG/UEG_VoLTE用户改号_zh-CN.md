---
id: GWFD-025805
name: VoLTE用户改号
ne_type: UEG
type: feature
description: 当VoLTE用户希望换号不换卡时，需要对用户进行改号配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-025800 UDM语音基本功能","GWFD-025805 支持VoLTE","特性配置","VoLTE用户改号"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当VoLTE用户希望换号不换卡时，需要对用户进行改号配置。

## 必备事项
前提条件

* 操作人员已完全了解支持VoLTE特性。
* 已完成VoLTE用户的业务发放。
* 操作人员具有业务发放权限。
* 已完成IMS网络、CS网络、HLR/HSS数据库以及EPC网络各网元的基本数据配置和对接数据配置，各网元运行正常。
* 操作人员具有PGW Web LMT的用户名和密码
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_isdn_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEWISDN:
          name: '新MSISDN'
          type: string
          required: false
          description: '用于指定新的MSISDN。'
          data_source: ''
          pattern: ''
          default: ''
    mod_hhsstn_list:
      type: items
      properties:
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要修改的旧的MSISDN。'
          data_source: ''
          pattern: ''
          default: ''
        NEWISDN:
          name: '新的MSISDN'
          type: string
          required: false
          description: '用于指定新的MSISDN。'
          data_source: ''
          pattern: ''
          default: ''
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '用于标识改号前的IMPU。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPU:
          name: '新的IMPU'
          type: string
          required: false
          description: '用于指定新的IMPU。'
          data_source: ''
          pattern: ''
          default: ''
        IMPU2:
          name: 'IMPU2'
          type: string
          required: false
          description: '用于标识改号前的IMPU。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPU2:
          name: '新的IMPU2'
          type: string
          required: false
          description: '用于指定新的IMPU。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_isdn_list:
    - IMSI: '460030913121002'
      NEWISDN: '8613901384331'
    mod_hhsstn_list:
    - ISDN: '8613901384321'
      NEWISDN: '8613901384331'
      IMPU: sip:8613901384321@ims.mnc000.mcc460.3gppnetwork.org
      NEWIMPU: sip:8613901384331@ims.mnc000.mcc460.3gppnetwork.org
      IMPU2: sip:8613901384321@ics.mnc000.mcc460.3gppnetwork.org
      NEWIMPU2: sip:8613901384331@ics.mnc000.mcc460.3gppnetwork.org
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**MOD ISDN**命令，为用户关联新的MSISDN。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_isdn_list的变量区（command: MOD ISDN） -#}
<!-- MISSING_MACRO: command=MOD ISDN list_name=mod_isdn_list step_id=2 -->
```

### 3 登录“IMS-HSS业务管理”窗口。

### 4 执行**MOD HHSSTN**命令，为用户关联新的MSISDN和IMPU。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_hhsstn_list的变量区（command: MOD HHSSTN） -#}
<!-- MISSING_MACRO: command=MOD HHSSTN list_name=mod_hhsstn_list step_id=4 -->
```

