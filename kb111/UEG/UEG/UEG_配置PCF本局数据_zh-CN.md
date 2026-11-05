---
id: ''
name: 配置PCF本局数据
ne_type: UEG
type: feature
description: 开局时，配置PCF的本局数据。  如园区部署UDM，则不需要配置该页面。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置PCF/PCRF","配置PCF本局数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置PCF的本局数据。如园区部署UDM，则不需要配置该页面。

## 必备事项
前提条件

已完成配置PCF和USCDB对接数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_syshlrsn_list:
      type: items
      properties:
        SYSHLRSN:
          name: '系统HLR序列号'
          type: string
          required: false
          description: '该参数取值与USCDB MML命令界面上的**SET SYSNO**命令配置的“SYSTEMNO”参数的取值相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HLRNAME:
          name: '系统HLR名称'
          type: string
          required: false
          description: '统一规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        STATUS:
          name: '状态'
          type: string
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_syshlrsn_list:
    - SYSHLRSN: '1'
      HLRNAME: HLR01
      STATUS: MASTER
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW Web LMT MML命令界面。

### 此处以完整模式HLR（输入“HLRSN”“用户名”、“登录密码”）登录PGW Web LMT为例，详细操作请参见登录与退出PGW Web LMT。

### 2 增加系统序列号。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_syshlrsn_list的变量区（command: ADD SYSHLRSN） -#}
<!-- MISSING_MACRO: command=ADD SYSHLRSN list_name=add_syshlrsn_list step_id=2 -->
```

