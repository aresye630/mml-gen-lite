---
id: ''
name: 配置在线计费自动回切功能
ne_type: UDG
type: feature
description: 本指导描述在线计费用户转离线计费后，是否可以自动切回在线计费的相关配置操作。  在线计费用户因OCS故障等原因转离线后，在holding-time超时前，OCS故障恢复，用户可以自动恢复为在线计费用户。  UNC支持在DCC template模板、DCC global模板下开启本功能，此处以前者为例说明功能激活过程。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","SMF配置","在线计费配置","在线计费模板及交互配置","配置在线计费模板","配置在线计费自动回切功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述在线计费用户转离线计费后，是否可以自动切回在线计费的相关配置操作。在线计费用户因OCS故障等原因转离线后，在holding-time超时前，OCS故障恢复，用户可以自动恢复为在线计费用户。UNC支持在DCC template模板、DCC global模板下开启本功能，此处以前者为例说明功能激活过程。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
* 在线转离线功能已经通过（可选）配置DCC处理动作开启。

  在线计费回切功能要求转离线功能中：

  + **SET OCSDOWNACTION**:“OCSDNACTION”需配置为“PERMIT。”
  + **ADD DCCTEMPLATE**:“CCFH”。
  + **ADD CMDRCACT**:“CMDRCACT”为“CONTINUE”。
* 完成加载license。
* 已完成计费属性、APN、User Profile创建。
* 已根据配置在线计费模板完成在线计费模板创建和绑定。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '配置在线计费自动回切功能。 说明：  * 用户转离线时如果配置了**SET HOLDINGTIME**命令的“HOLDINGTIME”，则UNC在*HOLDINGTIME*超时前一直按照**ADD DCCTEMPLATE**命令配置的“RECOVERINTERVAL”值定期尝试恢复在线计费；若未配置“HOLDINGTIME”，则视作该值无限大。 * 如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLCHGRECOVER:
          name: '在线计费自动恢复功能开关'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '在线计费自动恢复间隔 （分钟）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_dcctemplate_list:
      type: items
      properties:
        DCCTMPLTNAME:
          name: 'DCC模板名称'
          type: string
          required: false
          description: '配置在线计费自动回切功能。 说明：  * 用户转离线时如果配置了**SET HOLDINGTIME**命令的“HOLDINGTIME”，则UNC在*HOLDINGTIME*超时前一直按照**ADD DCCTEMPLATE**命令配置的“RECOVERINTERVAL”值定期尝试恢复在线计费；若未配置“HOLDINGTIME”，则视作该值无限大。 * 如果需要配置在线计费全局参数，则需要使用**MOD DCCTEMPLATE**命令，“DCCTMPLTNAME”参数值为“global”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ONLCHGRECOVER:
          name: '在线计费自动恢复功能开关'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        RECOVERINTERVAL:
          name: '在线计费自动恢复间隔 （分钟）'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      ONLCHGRECOVER: ENABLE
      RECOVERINTERVAL: '10'
    mod_dcctemplate_list:
    - DCCTMPLTNAME: dcc-test
      ONLCHGRECOVER: ENABLE
      RECOVERINTERVAL: '10'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置在线计费自动回切功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dcctemplate_list的变量区（command: ADD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=ADD DCCTEMPLATE list_name=add_dcctemplate_list step_id=1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_dcctemplate_list的变量区（command: MOD DCCTEMPLATE） -#}
<!-- MISSING_MACRO: command=MOD DCCTEMPLATE list_name=mod_dcctemplate_list step_id=1 -->
```

