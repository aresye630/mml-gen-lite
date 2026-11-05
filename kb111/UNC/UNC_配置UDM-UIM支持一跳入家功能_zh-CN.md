---
id: ''
name: 配置UDM-UIM支持一跳入家功能
ne_type: UNC
type: feature
description: 本页面用于指导操作员配置UDM-UIM支持一跳入家功能。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置UDM-UIM（Non-SIM AAA）","配置UDM-UIM支持一跳入家功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本页面用于指导操作员配置UDM-UIM支持一跳入家功能。

## 必备事项
前提条件

操作人员具有登录OM Portal的操作权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_insp_list:
      type: items
      properties:
        INSPT:
          name: '软件参数类型'
          type: string
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        INSPN:
          name: '软件参数名称'
          type: string
          required: false
          description: '-'
          data_source: '固定配置'
          pattern: ''
          default: ''
        INSPV:
          name: '软件参数值'
          type: string
          required: false
          description: '用于标识需要修改的软件参数的参数值。  * 0：不支持一跳入家业务 * 1：支持一跳入家业务'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_insp_list:
    - INSPT: AAA
      INSPN: SUPP_TOHOME
      INSPV: '1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM MML命令”界面。

### 2 执行**MOD INSP**命令设置UDM-UIM支持一跳入家功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_insp_list的变量区（command: MOD INSP） -#}
<!-- MISSING_MACRO: command=MOD INSP list_name=mod_insp_list step_id=2 -->
```

