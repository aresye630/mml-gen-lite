---
id: ''
name: 修改用户状态
ne_type: UEG
type: feature
description: 在日常的管理和维护中，系统管理员可以根据实际需要修改用户状态，即控制是否允许用户登录PGW系统。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理用户权限","修改用户状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在日常的管理和维护中，系统管理员可以根据实际需要修改用户状态，即控制是否允许用户登录PGW系统。

## 必备事项
前提条件

只有具有管理员权限的用户才能修改用户状态。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_opr_list:
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
        OPNAME:
          name: 'OPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUS:
          name: 'STATUS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_opr_list:
    - SYSNO: '1'
      OPNAME: pgwguest
      STATUS: INACTIVE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**MOD OPR**修改操作员状态。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_opr_list的变量区（command: MOD OPR） -#}
<!-- MISSING_MACRO: command=MOD OPR list_name=mod_opr_list step_id=2 -->
```

### 通过参数“操作员状态”设置操作员的状态。

