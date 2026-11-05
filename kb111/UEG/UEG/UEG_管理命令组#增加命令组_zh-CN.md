---
id: ''
name: 增加命令组
ne_type: UEG
type: feature
description: 在ADMINISTRATOR管理员增加CUSTOM级别的操作员时，如果不使用系统默认的命令组，可以使用该操作增加自定义的命令组，通过命令组控制操作员的命令执行权限。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理命令组","增加命令组"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在ADMINISTRATOR管理员增加CUSTOM级别的操作员时，如果不使用系统默认的命令组，可以使用该操作增加自定义的命令组，通过命令组控制操作员的命令执行权限。

## 必备事项
前提条件

只有具有管理员权限的操作员才能增加命令组。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ccg_list:
      type: items
      properties:
        SYSNO:
          name: 'SYSNO'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CG:
          name: 'CG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CMD:
          name: 'CMD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ccg_list:
    - SYSNO: '1'
      CG: G_8
      CMD: LST_LOG
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**ADD CCG**增加命令组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ccg_list的变量区（command: ADD CCG） -#}
<!-- MISSING_MACRO: command=ADD CCG list_name=add_ccg_list step_id=2 -->
```

### 可以通过执行命令**LST CCG**查询增加的命令组。

