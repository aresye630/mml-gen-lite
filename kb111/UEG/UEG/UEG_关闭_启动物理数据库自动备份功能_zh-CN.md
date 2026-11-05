---
id: ''
name: 关闭/启动物理数据库自动备份功能
ne_type: UEG
type: feature
description: 系统默认启动物理数据库自动备份功能，缺省情况下物理库备份默认启动时间在每天04:00:00。  系统升级时，需要关闭物理数据库自动备份功能，该操作在升级时会自动设定关闭，无需单独设定。  在完成手动操作之后，需要重新打开物理数据库自动备份功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG USCDB数据备份与恢复（风筝L）","备份与恢复用户手册","备份与恢复原理及基本操作","物理数据库备份与恢复","基本操作","自动备份配置调整","关闭/启动物理数据库自动备份功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
系统默认启动物理数据库自动备份功能，缺省情况下物理库备份默认启动时间在每天04:00:00。系统升级时，需要关闭物理数据库自动备份功能，该操作在升级时会自动设定关闭，无需单独设定。在完成手动操作之后，需要重新打开物理数据库自动备份功能。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_backup_list:
      type: items
      properties:
        BAKSWH:
          name: '自动备份开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_backup_list:
    - BAKSWH: ON/OFF（开/关）
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 执行**MOD BACKUP**命令关闭/启动物理数据库自动备份功能。

```jinja2
{%- for item in mod_backup_list -%}
    MOD BACKUP:
    {#- --- 可选参数 --- -#}
    {%- if item.BAKSWH is not none -%}
        BAKSWH={{item.BAKSWH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**LST BACKUP**命令查询备份开关状态是否与2操作结果一致。

### **相关命令**

### * **MOD BACKUP**

### * **LST BACKUP**

