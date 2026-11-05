---
id: ''
name: 用户面选择结果验证
ne_type: UNC
type: feature
description: 当需要观察是否为用户选择到了预期的用户面时，需要对选择用户面功能进行验证，确保功能可以正常使用。
risk_level: ''
doc_source: ["网络部署","业务专题","UNC UPF选择专题","用户面选择结果验证"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要观察是否为用户选择到了预期的用户面时，需要对选择用户面功能进行验证，确保功能可以正常使用。

## 必备事项
前提条件

* 请仔细阅读5G用户访问5G网络时的用户面选择、5G用户访问4/5G互操作网络时的用户面选择、基于位置信息优选UPF容灾场景的用户面选择。
* 已经在SMF上完成和用户面的对接配置，参考不同部署场景下的UPF选择配置。
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

### 1 终端使用位置信息“123260101”接入网络，创建PDU会话。

### 2 进入“MML命令行-UNC”窗口。

### 3 查询用户PDU会话的会话ID。

### 预期结果：查询到PDU会话ID作为后续详细查询的PDU会话输入参数。

### RETCODE = 0  操作成功

### 结果如下

### --------------

### IMSI             PDU会话ID  APN或者DNN  请求的APN名称/DNN名称  无线接入类型  QoS流ID  QCI或者5QI  QoS流ARP优先级  QoS流ARP抢占能力  QoS流ARP被抢占能力  SNssaiSst/SNssaiSd  QosFlow 5QI 优先级

### 123000123456789  5          huawei1.com  huawei1.com             NR            1        5           1               MAY_PREEMPT       PREEMPTABLE         1/010101            NULL

### (结果个数 = 1)

### ---    END

### 4 查询用户PDU会话的用户面信息。

### 预期结果：PDU会话信息中的用户面地址是预期为用户选择的UPF地址。

### RETCODE = 0  操作成功

### 结果如下

### --------------

### 国际移动用户标识 = 123000123456789

### ...

### 用户位置信息TAI = 123260101

### ...

### UPF ID = UPF_Instance_PSA-INM1

### ...

### UP的PFCP IPv4地址 = 192.168.9.52

### ...

### (结果个数 = 1)

### ---    END

