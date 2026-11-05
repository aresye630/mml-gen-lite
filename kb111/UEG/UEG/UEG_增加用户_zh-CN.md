---
id: ''
name: 增加用户
ne_type: UEG
type: feature
description: PGW Web LMT系统默认的用户和超级管理员都具有新增用户的权限，并给新增的用户赋予不同的操作权限。默认的操作员的权限一般都很高，运营商可以通过创建新的操作员控制操作员的一些权限。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","运维安全配置","管理PGW Web LMT帐户","增加用户"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","运维安全配置","管理PGW Web LMT帐户","增加用户"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","运维安全配置","管理PGW Web LMT帐户","增加用户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PGW Web LMT系统默认的用户和超级管理员都具有新增用户的权限，并给新增的用户赋予不同的操作权限。默认的操作员的权限一般都很高，运营商可以通过创建新的操作员控制操作员的一些权限。

## 必备事项
前提条件

只有具有管理员权限的用户才能创建新的用户。
如果增加的是自定义级别的操作员，且使用自定义命令组，需要提前使用**ADD CCG**命令增加命令组。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_opr_list:
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
        DESC:
          name: 'DESC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWD:
          name: 'PWD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CFM:
          name: 'CFM'
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
        STATUS:
          name: 'STATUS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATP:
          name: 'ATP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_opr_list:
    - SYSNO: '1'
      OPNAME: pgwuser
      DESC: user in pgw system
      PWD: '*****'
      CFM: '*****'
      UG: USER
      STATUS: ACTIVE
      ATP: MAN-MACHINE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**ADD OPR**增加操作员。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_opr_list的变量区（command: ADD OPR） -#}
<!-- MISSING_MACRO: command=ADD OPR list_name=add_opr_list step_id=2 -->
```

### 若所增加的操作员级别为“CUSTOM”，则需要设置参数“命令组”。

### G\_8～G\_127的命令组信息可以通过命令**ADD CCG**进行增加。

### 可以通过执行命令**LST OPR**查询新增加的用户。

