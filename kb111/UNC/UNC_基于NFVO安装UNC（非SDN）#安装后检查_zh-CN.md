---
id: ''
name: 安装后检查
ne_type: UNC
type: feature
description: 检查资源单元的状态，确保设备运行正常。
risk_level: ''
doc_source: ["网络部署","软件安装","基于NFVO安装UNC（非SDN）","安装后检查"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
检查资源单元的状态，确保设备运行正常。

## 必备事项
前提条件

已经登录OM Portal，或者已登录U2020，或者登录MAE并进入Access子系统。
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

### 1 在UNC OM portal，选择“监控分析 > 告警管理 > 活动告警”，查看系统是否上报如下告警，如果上报则处理相应告警。

### ALM-221257768 资源单元故障告警

### ALM-221257751 进程故障告警

### ALM-221257752 资源进程故障

### ALM-100145 实例化部分失败

### ALM-100001 进程故障告警

### 2 当MAE-VNF LCM为V100R024C10及之前版本时，查询VNFM鉴权用户名及密码有效期。

#### 2.1 通过**LST VNFMINFO**命令查询VNFM鉴权用户名。

#### 2.2 登录MAE-VNF LCM业务面客户端，单击图标，选择“系统 >安全管理 > 用户管理 > 用户”。

#### 2.3 单击目标用户，在“基本信息”页签中，单击“修改”，单击“高级设置”，查询“密码有效天数”。

#### 预期结果：“密码有效天数”为“0”。

#### 异常结果：“密码有效天数”为其他值。请勾选“启用密码修改时间策略”，设置“密码有效天数”为“0”，单击“确定”，将该用户密码设置为永不过期。

