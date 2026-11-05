---
id: ''
name: 手动解锁用户
ne_type: UEG
type: feature
description: 当用户登录PGW客户端，输入密码的次数超过限制的次数时，系统将自动锁定帐户。系统管理员可以执行该操作手工解锁用户。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理用户权限","手动解锁用户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当用户登录PGW客户端，输入密码的次数超过限制的次数时，系统将自动锁定帐户。系统管理员可以执行该操作手工解锁用户。

## 必备事项
前提条件

只有具有管理员权限的用户才能解锁被锁定的操作员。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_unlck_list:
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
    set_unlck_list:
    - SYSNO: '1'
      OPNAME: opr1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 在“应用类型”的下拉菜单中选择“系统管理”。

### 3 执行命令**SET UNLCK**手工解锁用户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_unlck_list的变量区（command: SET UNLCK） -#}
<!-- MISSING_MACRO: command=SET UNLCK list_name=set_unlck_list step_id=3 -->
```

