---
id: ''
name: 修改用户操作权限
ne_type: UEG
type: feature
description: 在PGW日常的管理和维护中，当需要重新调整一个操作员的权限（提高或减少操作员权限）时可以执行此操作，以赋予操作员相应的权限。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理用户权限","修改用户操作权限"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在PGW日常的管理和维护中，当需要重新调整一个操作员的权限（提高或减少操作员权限）时可以执行此操作，以赋予操作员相应的权限。

## 必备事项
前提条件

只有具有管理员权限的用户才能修改用户的操作权限。
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
        UG:
          name: 'UG'
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
  examples:
    mod_opr_list:
    - SYSNO: '1'
      OPNAME: pgwuser
      UG: CUSTOM
      CG: G_8
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**MOD OPR**修改用户的操作权限。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_opr_list的变量区（command: MOD OPR） -#}
<!-- MISSING_MACRO: command=MOD OPR list_name=mod_opr_list step_id=2 -->
```

### 通过参数“操作员级别”和“命令组”对用户的操作权限进行控制。

### 如果修改操作员的级别为“CUSTOM”，则需要设置参数“命令组”。

### G\_8～G\_127的命令组信息可以通过命令**ADD CCG**进行增加。

