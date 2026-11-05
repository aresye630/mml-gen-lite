---
id: ''
name: 修改用户操作时段
ne_type: UEG
type: feature
description: 在PGW日常的管理和维护中，当需要对操作员的操作时段进行控制时，系统管理员可以使用该操作修改用户的操作时段。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","管理PGW Web LMT权限","管理用户权限","修改用户操作时段"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在PGW日常的管理和维护中，当需要对操作员的操作时段进行控制时，系统管理员可以使用该操作修改用户的操作时段。

## 必备事项
前提条件

只有具有管理员权限的用户才能修改用户的操作时段。
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
        DATE:
          name: 'DATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTDATE:
          name: 'STARTDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDDATE:
          name: 'ENDDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIME:
          name: 'TIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STARTTIME:
          name: 'STARTTIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTIME:
          name: 'ENDTIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WEEK:
          name: 'WEEK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WK:
          name: 'WK'
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
      DATE: LIMIT
      STARTDATE: 2009&08&10
      ENDDATE: 2009&12&31
      TIME: LIMIT
      STARTTIME: 10&22&30
      ENDTIME: 20&22&32
      WEEK: LIMIT
      WK: SUN&TUE&THU&SAT
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW客户端。

### 登录方法请参见登录与退出PGW Web LMT。

### 2 执行命令**MOD OPR**修改用户操作时段。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_opr_list的变量区（command: MOD OPR） -#}
<!-- MISSING_MACRO: command=MOD OPR list_name=mod_opr_list step_id=2 -->
```

### 通过参数“日期限制开关”、“时间限制开关”和“星期限制开关”设置用户的操作时段。

