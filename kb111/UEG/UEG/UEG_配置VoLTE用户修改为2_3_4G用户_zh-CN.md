---
id: GWFD-025805
name: 配置VoLTE用户修改为2/3/4G用户
ne_type: UEG
type: feature
description: 该任务指导操作人员配置VoLTE用户改造为GSM/UMTS/EPS融合用户。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-025800 UDM语音基本功能","GWFD-025805 支持VoLTE","特性配置","配置VoLTE用户修改为2/3/4G用户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员配置VoLTE用户改造为GSM/UMTS/EPS融合用户。

## 必备事项
前提条件

* 操作人员已完全了解支持VoLTE特性。
* 已完成VoLTE用户的业务发放。
* 准备去签约IMS数据的用户已经开户。
* 操作人员具有业务发放权限。
* 操作人员具有PGW Web LMT的用户名和密码
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_optgprs_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识IMSI号码。'
          data_source: ''
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        CNTXID:
          name: 'PDP/PDN上下文索引值'
          type: string
          required: false
          description: 'PDP/PDN上下文索引值，每个PDP/PDN上下文的索引值不能相同，值域为1～50。'
          data_source: ''
          pattern: ''
          default: ''
    mod_icsind_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识IMSI号码。'
          data_source: ''
          pattern: ''
          default: ''
        ICSIND:
          name: '是否具备ICS能力'
          type: string
          required: false
          description: '用户是否具备ICS能力。  * TRUE：具备 * FALSE：不具备'
          data_source: ''
          pattern: ''
          default: ''
    rmv_hhsssub_list:
      type: items
      properties:
        SUBID:
          name: 'SUBID'
          type: string
          required: false
          description: '用于指定需要删除哪一个签约用户的所有信息。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_optgprs_list:
    - IMSI: '460000009123456'
      PROV: RMVPDPCNTX
      CNTXID: '2'
    mod_icsind_list:
    - IMSI: '460000009123456'
      ICSIND: FALSE
    rmv_hhsssub_list:
    - SUBID: '+8613912345678'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**MOD OPTGPRS**命令删除IMS数据和信令承载APN。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_optgprs_list的变量区（command: MOD OPTGPRS） -#}
<!-- MISSING_MACRO: command=MOD OPTGPRS list_name=mod_optgprs_list step_id=2 -->
```

### 3 执行**MOD ICSIND**命令去签约ICS能力。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_icsind_list的变量区（command: MOD ICSIND） -#}
<!-- MISSING_MACRO: command=MOD ICSIND list_name=mod_icsind_list step_id=3 -->
```

### 4 登录“IMS-HSS业务管理”窗口。

### 5 执行**RMV HHSSSUB**命令删除IMS-HSS开户数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该rmv_hhsssub_list的变量区（command: RMV HHSSSUB） -#}
<!-- MISSING_MACRO: command=RMV HHSSSUB list_name=rmv_hhsssub_list step_id=5 -->
```

