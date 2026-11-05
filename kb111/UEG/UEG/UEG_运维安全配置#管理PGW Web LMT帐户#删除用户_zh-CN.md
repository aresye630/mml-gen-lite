---
id: ''
name: 删除用户
ne_type: UEG
type: feature
description: 在日常的操作维护活动中，系统管理员可以删除不再使用或者已过期的用户，以提高系统的安全性。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","运维安全配置","管理PGW Web LMT帐户","删除用户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在日常的操作维护活动中，系统管理员可以删除不再使用或者已过期的用户，以提高系统的安全性。

## 必备事项
前提条件

只有具有管理员权限的用户才能删除其他用户。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_opr_list:
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
  examples:
    rmv_opr_list:
    - SYSNO: '1'
      OPNAME: pgwuser
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**RMV OPR**删除操作员。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该rmv_opr_list的变量区（command: RMV OPR） -#}
<!-- MISSING_MACRO: command=RMV OPR list_name=rmv_opr_list step_id=2 -->
```

