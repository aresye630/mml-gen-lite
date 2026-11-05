---
id: ''
name: 登录PGW Web LMT MML命令界面
ne_type: UEG
type: feature
description: “系统管理”界面用于执行USCDB的系统管理的命令。
tags: []
risk_level: ''
doc_source: ["参考信息","UEG 命令参考（风筝M&L，虚机&裸机容器）","PGW Web LMT","PGW Web LMT GUI参考","PGW Web LMT","登录PGW Web LMT MML命令界面"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
“系统管理”界面用于执行USCDB的系统管理的命令。

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

#### 1.1 在浏览器地址栏中输入**PGW的地址**，按“Enter”键。是否使用https安全协议登录由软参“WEBLMTHTTPSSWITCH”控制。如图1所示。

##### 1.1.1 当软参“WEBLMTHTTPSSWITCH”取值为“0”时，在浏览器的地址栏输入地址**http://*****PGW服务IP地址***。

##### 1.1.2 当软参“WEBLMTHTTPSSWITCH”取值为“1”时，在浏览器的地址栏输入地址**https://*****PGW服务IP地址:80***。

#### **图1** PGW Web LMT登录界面

##### 1.1.3 本文以完整模式下登录界面参数显示**MVNO**且“用户类型”选择为“Local”为例来说明。

##### 1.1.4 “PGW服务IP地址”为运营商规划数据，可以从运营商的操作维护人员处获得，也可以登录“USCDB MML命令”界面执行**LST SRVIPADDR**命令获得。

##### 1.1.5 MVNO为可选参数，当不输入该参数时，默认使用通过登录“USCDB MML命令”界面执行**SET SYSNO**命令设置的系统序列号。当输入该参数时，MVNO必须为通过PGW Web LMT上的**ADD SYSNO**命令添加的系统序列号或通过登录“USCDB MML命令”界面执行**SET SYSNO**命令设置的系统序列号。

##### 1.1.6 系统配置了默认的“用户名”为“admin”，“登录密码”请从运营商的操作维护人员处获得，“默认密码”请参考《USCDB应用用户默认账号》。

#### 1.2 在登录界面分别输入“MVNO”、“用户名”、“登录密码”和“验证码”，单击“立即登录”，进入PGW Web LMT MML界面，如图2所示。

#### 首次登录PGW Web LMT界面时不需要输入验证码，连续两次输入密码错误后再次登录需要输入验证码。

#### **图2** PGW Web LMT MML界面

