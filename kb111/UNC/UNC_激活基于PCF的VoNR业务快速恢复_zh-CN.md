---
id: ''
name: 激活基于PCF的VoNR业务快速恢复
ne_type: UNC
type: feature
description: 在UNC上激活基于PCF的VoNR业务快速恢复功能，降低P-CSCF服务器故障时，对用户业务的影响。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-221003 基于PCF的VoNR业务快速恢复","激活基于PCF的VoNR业务快速恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UNC上激活基于PCF的VoNR业务快速恢复功能，降低P-CSCF服务器故障时，对用户业务的影响。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-221003 基于PCF的VoNR业务快速恢复特性概述。
* 完成激活P-CSCF故障时IMS业务恢复。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        ITEM:
          name: 'ITEM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: 'SWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - ITEM: LKV2FRVNRPCF01
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_licenseswitch_list的变量区（command: SET LICENSESWITCH） -#}
<!-- MISSING_MACRO: command=SET LICENSESWITCH list_name=set_licenseswitch_list step_id=2 -->
```

