---
id: ''
name: 更新物理数据库帐户密码
ne_type: UEG
type: feature
description: '* 在调测完成后，系统管理员必须及时更新物理数据库帐号的密码，确保系统安全。 * 在日常维护中，系统管理员必须定期更新物理数据库帐号的密码，确保系统安全。'
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","系统安全配置","更新物理数据库帐户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","系统安全配置","更新物理数据库帐户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","系统安全配置","更新物理数据库帐户密码"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","系统安全配置","更新物理数据库帐户密码"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 在调测完成后，系统管理员必须及时更新物理数据库帐号的密码，确保系统安全。* 在日常维护中，系统管理员必须定期更新物理数据库帐号的密码，确保系统安全。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_db_list:
      type: items
      properties:
        USERNAME:
          name: '用户名'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_db_list:
    - USERNAME: 'uscdb_acc'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 0 **更新pgw\_acc**、**uscdb\_acc**、**sys**、**uscdb**、**pgw**和**uscdb\_maintain**用户的密码。

### 1 登录“USCDB MML命令”界面。

### 2 执行**SET DB**命令，更新物理数据库用户的密码。

### 以更新“uscdb\_acc”用户初始密码为例：

```jinja2
{%- for item in set_db_list -%}
    SET DB:
    {#- --- 必选参数 --- -#}
    USERNAME="{{item.USERNAME}}",
    ;
{%- endfor -%}
```

