---
id: ''
name: 配置接续时延优化
ne_type: UEG
type: feature
description: 该任务用于指导操作人员根据华为网优报告的操作建议配置基本数据，缩短用户从拨打电话到开始振铃之间的时延，以实现接续时延优化的目标。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","相关参考","VoLTE特性","基本呼叫","配置接续时延优化"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务用于指导操作人员根据华为网优报告的操作建议配置基本数据，缩短用户从拨打电话到开始振铃之间的时延，以实现接续时延优化的目标。

## 必备事项
前提条件

操作人员具有业务发放权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_optcfg_list:
      type: items
      properties:
        OT:
          name: 'OT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SAM:
          name: 'SAM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPUTHD1:
          name: 'CPUTHD1'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPUTHD2:
          name: 'CPUTHD2'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_optcfg_list:
    - OT: Q922
      SAM: SELFADAPT
      CPUTHD1: '10'
      CPUTHD2: '20'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置Q.922链路优化功能

### 进入OM Portal“应用管理>MML>UCN”窗口。

### 2 执行****MOD OPTCFG****命令，选择“优化类型”为“Q922(Q922)”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_optcfg_list的变量区（command: MOD OPTCFG） -#}
<!-- MISSING_MACRO: command=MOD OPTCFG list_name=mod_optcfg_list step_id=2 -->
```

### 3 选择“自适应模式”为“SELFADAPT(自适应)”。

### 4 选择“CPU阈值1”为“10”。

### 5 选择“CPU阈值2”为“20”。

