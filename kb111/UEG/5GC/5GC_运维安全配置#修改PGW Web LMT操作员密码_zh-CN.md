---
id: ''
name: 修改PGW Web LMT操作员密码
ne_type: UEG
type: feature
description: '* 在开局结束后，系统管理员必须及时修改PGW Web LMT操作员的密码，确保系统安全。 * 在日常维护中，系统管理员必须定期修改PGW Web LMT操作员的密码，确保系统安全。'
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","运维安全配置","修改PGW Web LMT操作员密码"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 在开局结束后，系统管理员必须及时修改PGW Web LMT操作员的密码，确保系统安全。* 在日常维护中，系统管理员必须定期修改PGW Web LMT操作员的密码，确保系统安全。

## 必备事项
前提条件

首次登录请参考LLD文档中“账号管理设计”页签获取登录密码，之后维护请向系统管理员获取PGW Web LMT的admin帐号的密码。
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
  examples:
    mod_opr_list:
    - SYSNO: 系统序列号
      OPNAME: 操作员名称
      PWD: 密码
      CFM: 确认密码
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 使用admin帐号登录PGW Web LMT，登录PGW Web LMT MML命令界面。用户的默认密码请参见USCDB应用用户默认帐号。

### 2 在PGW Web LMT主界面点击“个人设置”按钮，进入个人设置页面。

### **图1** PGW Web LMT主界面

### 3 在个人设置页面，如图2所示，点击“修改密码”按钮，修改当前登录的操作员密码。

### **图2** 个人设置页面

### 4 未登录的普通操作员可通执行**MOD OPR**命令修改密码。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_opr_list的变量区（command: MOD OPR） -#}
<!-- MISSING_MACRO: command=MOD OPR list_name=mod_opr_list step_id=4 -->
```

### “系统序列号”和“操作员名称”必须已通过**ADD OPR**命令添加。

