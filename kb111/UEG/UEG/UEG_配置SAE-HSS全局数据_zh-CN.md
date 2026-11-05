---
id: ''
name: 配置SAE-HSS全局数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS全局数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","SAE-HSS用户数据配置","配置SAE-HSS全局数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS全局数据的配置。

## 必备事项
前提条件

前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成SAE-HSS的用户数据规划。
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
          description: '工程设计输出  该参数取值与USCDB MML命令界面上的**SET SYSNO**命令配置的“SYSTEMNO”参数的取值相同'
          data_source: ''
          pattern: ''
          default: ''
        HLRNAME:
          name: '系统HLR名称'
          type: string
          required: false
          description: '工程设计输出'
          data_source: ''
          pattern: ''
          default: ''
        STATUS:
          name: '状态'
          type: string
          required: false
          description: '单局点时，该参数固定取值为“MASTER”'
          data_source: ''
          pattern: ''
          default: ''
    add_vhlrsn_list:
      type: items
      properties:
        HLRSN:
          name: '虚拟HLR序列号'
          type: string
          required: false
          description: '工程设计输出'
          data_source: ''
          pattern: ''
          default: ''
        HLRNAME:
          name: '虚拟HLR名称'
          type: string
          required: false
          description: '工程设计输出'
          data_source: ''
          pattern: ''
          default: ''
    add_hlrsn_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '该参数的取值需要与系统管理MML命令界面上的**ADD VHLRSN**命令配置的“HLRSN”的取值一一对应'
          data_source: ''
          pattern: ''
          default: ''
        HLRNO:
          name: 'HLR号码'
          type: string
          required: false
          description: '根据运营商要求配置。容灾局的“HLR号码”会同步主用局的“HLR号码”。'
          data_source: ''
          pattern: ''
          default: ''
        STATUS:
          name: '状态'
          type: string
          required: false
          description: '单局点时，该参数固定取值为“MASTER”'
          data_source: ''
          pattern: ''
          default: ''
        CCODE:
          name: '国家码'
          type: string
          required: false
          description: '根据运营商要求配置'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_syshlrsn_list:
    - SYSHLRSN: '1'
      HLRNAME: HLR01
      STATUS: MASTER
    add_vhlrsn_list:
    - HLRSN: '1'
      HLRNAME: VHLR01
    add_hlrsn_list:
    - HLRSN: '1'
      HLRNO: '8613910000'
      STATUS: MASTER
      CCODE: '86'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录系统管理命令界面。

### 2 执行**ADD SYSHLRSN**命令增加系统HLR。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_syshlrsn_list的变量区（command: ADD SYSHLRSN） -#}
<!-- MISSING_MACRO: command=ADD SYSHLRSN list_name=add_syshlrsn_list step_id=2 -->
```

### 3 执行**ADD VHLRSN**命令增加虚拟HLR。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_vhlrsn_list的变量区（command: ADD VHLRSN） -#}
<!-- MISSING_MACRO: command=ADD VHLRSN list_name=add_vhlrsn_list step_id=3 -->
```

### 每个SYSHLRSN至少指定一个虚拟HLR。

### 4 登录“UDM业务管理”窗口。

### 5 执行**ADD HLRSN**命令增加HLR序列号。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_hlrsn_list的变量区（command: ADD HLRSN） -#}
<!-- MISSING_MACRO: command=ADD HLRSN list_name=add_hlrsn_list step_id=5 -->
```

