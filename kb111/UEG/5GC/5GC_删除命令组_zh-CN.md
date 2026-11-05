---
id: ''
name: 删除命令组
ne_type: UEG
type: feature
description: 当添加的自定义命令组不再被任何用户使用时，ADMINISTRATOR管理员可以执行该操作删除自定义的命令组，以提高系统的安全性。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理命令组","删除命令组"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理命令组","删除命令组"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理命令组","删除命令组"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理命令组","删除命令组"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当添加的自定义命令组不再被任何用户使用时，ADMINISTRATOR管理员可以执行该操作删除自定义的命令组，以提高系统的安全性。

## 必备事项
前提条件

* 只有具有管理员权限的操作员才能删除命令组。
* 系统中默认添加的命令组G\_0～G\_7不能被删除。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_ccg_list:
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
  examples:
    rmv_ccg_list:
    - SYSNO: '1'
      CG: G_8
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**RMV CCG**删除命令组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该rmv_ccg_list的变量区（command: RMV CCG） -#}
<!-- MISSING_MACRO: command=RMV CCG list_name=rmv_ccg_list step_id=2 -->
```

