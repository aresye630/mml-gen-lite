---
id: ''
name: 登录“UPCF 业务管理”窗口
ne_type: UEG
type: feature
description: UPCF“业务管理”界面用于执行UPCF的全局数据命令组和用户数据命令组的命令。
tags: []
risk_level: ''
doc_source: ["参考信息","UEG 命令参考（风筝M&L，虚机&裸机容器）","PGW Web LMT","PGW Web LMT GUI参考","登录“UPCF 业务管理”窗口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPCF“业务管理”界面用于执行UPCF的全局数据命令组和用户数据命令组的命令。

## 必备事项
前提条件

PGW Web LMT界面能正常登录和使用。
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

### 1 登录PGW Web LMT。

#### 1.1 打开浏览器，在浏览器的地址栏输入地址**http://***PGW（Provisioning Gateway）服务IP地址*后按“Enter”键，打开网页，进入PGW Web LMT的登录界面。如图1所示。

#### **图1** PGW Web LMT登录界面

#### “PGW服务IP地址”为运营商规划数据，可以从运营商的操作维护人员处获得，也可以登录“USCDB MML命令”界面执行**LST SRVIPADDR**命令获得。

#### 登录PGW Web LMT界面的默认用户名和密码请参见《USCDB应用用户默认帐号》。

#### 1.2 在登录界面分别输入“用户名”、“密码”和“验证码”，单击“登录”，进入PGW Web LMT MML命令界面，如图2所示。

#### 首次登录PGW Web LMT界面时不需要输入验证码，连续两次输入密码错误后再次登录需要输入验证码。

#### **图2** PGW Web LMT MML命令界面

#### 进入PGW Web LMT MML命令界面，系统默认登录“系统管理”界面。如图2所示。

### 2 登录UPCF“业务管理”界面。

### 在“MML导航树”下拉列表中选择“UPCF业务管理”选项，系统进入UPCF业务管理界面，如图3所示。

### **图3** UPCF业务管理界面

