---
id: ''
name: 媒体中继UPF选择结果验证
ne_type: UNC
type: feature
description: 当运营商部署媒体中继UPF选择功能时，需对该功能进行调测，确保该功能正常生效。
risk_level: ''
doc_source: ["网络部署","业务专题","UNC UPF选择专题","媒体中继UPF选择","媒体中继UPF选择结果验证"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商部署媒体中继UPF选择功能时，需对该功能进行调测，确保该功能正常生效。

## 必备事项
前提条件

完成媒体中继UPF选择配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties: {}
  examples: {}
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在OM Portal创建用户跟踪任务，在“定位条件”栏输入用户IMSI，在“消息类型”栏选择UP DATA、DOWN DATA和PFCP消息类型。同时在SMF侧开启对PFCP消息的跟踪任务。

### 2 测试终端使用“huawei.com”APN接入网络，并进行下行数据业务。媒体中继用户会话激活，并跟踪该用户消息。

### 3 查看SMF发送的消息中是否携带如下图所示的媒体中继标识。

### 是，请执行4。

### 否，请执行步骤 5。

### 4 使用**DSP PDUSESSION**命令查询用户上下文，查看“业务规则”是否包含用户签约的媒体中继规则。

### 是，则该功能调测完成。

### 否，请执行步骤 5。

### 5 收集问题信息并寻求技术支持。

#### 5.1 在镜像接口或服务器上开启第三方抓包工具，执行步骤 2并保存报文。

#### 5.2 在相应窗口下执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。

#### 5.3 收集并保存上述所有查询信息。

#### 5.4 归纳所有信息并联系华为技术支持解决。

