---
id: ''
name: 配置PGW Web LMT的安全策略
ne_type: UEG
type: feature
description: 当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置PGW Web LMT的安全策略。  PGW Web LMT的安全策略包括以下两个方面：  * 完善的密码安全措施，通过限制登录次数和返回固定错误消息等方式防止非授权人员进行密码暴力破解、非授权人员非法接入系统和密码遭盗窃。 * 用户登录PGW Web LMT时的安全性检查和配置，用于防止非法用户登录PGW Web LMT，保证系统的安全访问。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置PGW Web LMT的安全策略"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置PGW Web LMT的安全策略"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置PGW Web LMT的安全策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当USCDB与业务发放系统均完成硬件数据和基础数据的配置后，需要配置PGW Web LMT的安全策略。PGW Web LMT的安全策略包括以下两个方面：* 完善的密码安全措施，通过限制登录次数和返回固定错误消息等方式防止非授权人员进行密码暴力破解、非授权人员非法接入系统和密码遭盗窃。* 用户登录PGW Web LMT时的安全性检查和配置，用于防止非法用户登录PGW Web LMT，保证系统的安全访问。

## 必备事项
前提条件

向系统管理员获取OM Portal和PGW Web LMT帐号的密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_secpolicy_list:
      type: items
      properties:
        OPLCK:
          name: 'OPLCK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRYTIME:
          name: 'TRYTIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLEAR:
          name: 'CLEAR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERVAL:
          name: 'INTERVAL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTOUNLCK:
          name: 'AUTOUNLCK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCKTIME:
          name: 'LCKTIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECURITY:
          name: 'SECURITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FSTLOG:
          name: 'FSTLOG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HISRECORD:
          name: 'HISRECORD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINLEN:
          name: 'MINLEN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMPLEX:
          name: 'COMPLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNUMS:
          name: 'CNUMS'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARTYPE:
          name: 'CHARTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMEMOD:
          name: 'TIMEMOD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALIDDAY:
          name: 'VALIDDAY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROMPTDAY:
          name: 'PROMPTDAY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_secpolicy_list:
    - OPLCK: TRUE
      TRYTIME: '1'
      CLEAR: TRUE
      INTERVAL: '10'
      AUTOUNLCK: TRUE
      LCKTIME: '30'
      SECURITY: TRUE
      FSTLOG: TRUE
      HISRECORD: '5'
      MINLEN: '8'
      COMPLEX: CHAR-1&NOID-0&NOORD-0
      CNUMS: '3'
      CHARTYPE: UPPER-1&LOWER-1
      TIMEMOD: TRUE
      VALIDDAY: '90'
      PROMPTDAY: '5'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 使用admin帐号登录PGW Web LMT MML命令界面。用户的默认密码请参见USCDB应用用户默认帐号。

### 2 执行**SET SECPOLICY**命令，设置PGW Web LMT系统的安全策略。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_secpolicy_list的变量区（command: SET SECPOLICY） -#}
<!-- MISSING_MACRO: command=SET SECPOLICY list_name=set_secpolicy_list step_id=2 -->
```

### 执行**MOD OPR**命令可设置单个用户的安全策略信息。

