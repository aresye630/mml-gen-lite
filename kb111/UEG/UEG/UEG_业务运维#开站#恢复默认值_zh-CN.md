---
id: ''
name: 恢复默认值
ne_type: UEG
type: feature
description: 清空开站配置，恢复默认值。  如果恢复默认值时比极简开站时加载的补丁版本低，请联系华为技术支持协助操作。
tags: []
risk_level: ''
doc_source: ["日常维护","UEG 基础运维操作（风筝S，虚机容器）","业务运维","开站","恢复默认值"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
清空开站配置，恢复默认值。如果恢复默认值时比极简开站时加载的补丁版本低，请联系华为技术支持协助操作。

## 必备事项
前提条件

* 已登录 OM Portal。
* 操作员拥有系统管理员权限。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 选择“应用配置”> “业务运维”，在左侧导航栏中选择“开站”-> "恢复默认值"，进入“配置恢复”界面，如图1。

### **图1** 配置恢复

### 2 单击“一键清除开站信息”，弹出“警告”确认框，如图2。

### **图2** 清空开站配置提示信息确认框

### 3 确认当前环境符合提示信息，单击“确定”。

