---
id: ''
name: 配置用户跟踪净荷长度
ne_type: UNC
type: feature
description: UNC消息跟踪默认为不上报任何用户个人数据，建议运营商遵从所在国家的相关法律决定是否配置用户跟踪净荷长度。
risk_level: ''
doc_source: ["网络部署","安全配置","UNC安全配置","安全配置建议","可选配置","数据安全配置","配置用户跟踪净荷长度"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC消息跟踪默认为不上报任何用户个人数据，建议运营商遵从所在国家的相关法律决定是否配置用户跟踪净荷长度。

## 必备事项
前提条件

* 请仔细阅读个人隐私数据保护。
* 操作用户权限为管理员权限。
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

### 1 进入“MML命令行-UNC”窗口。

### 2 设置GTPU消息长度。

### ****SET TRC\_CFG****

