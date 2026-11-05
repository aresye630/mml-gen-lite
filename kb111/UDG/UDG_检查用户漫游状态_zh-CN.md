---
id: ''
name: 检查用户漫游状态
ne_type: UDG
type: feature
description: 通过检查漫游用户的状态，以确认国际漫游功能运行正常。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 国际漫游解决方案","例行维护","检查用户漫游状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过检查漫游用户的状态，以确认国际漫游功能运行正常。

## 必备事项
前提条件

已完成业务部署。
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

### 1 漫游终端接入本地拜访网络，创建PDU会话。

### 2 登录**拜访地SMF**的OM Portal。

### 3 进入“MML命令行-UNC”窗口。

### 4 查询用户PDU会话的会话ID。

### 预期结果：查询到PDU会话ID，用户成功创建PDU会话。

### RETCODE = 0  操作成功

### 结果如下

### --------------

### IMSI             PDU会话ID  APN或者DNN  请求的APN名称/DNN名称  无线接入类型  QoS流ID  QCI或者5QI  QoS流ARP优先级  QoS流ARP抢占能力  QoS流ARP被抢占能力  SNssaiSst/SNssaiSd  QosFlow 5QI 优先级

### 12300123456789  5          huawei1.com  huawei1.com             NR            1        5           1               MAY_PREEMPT       PREEMPTABLE         1/010101            NULL

### (结果个数 = 1)

### ---    END

### 5 查询会话管理的用户信息。

### 预期结果：查询漫游状态为“VISITING”的用户中有测试终端信息。

### %%DSP SMUSERINFO: APN="huawei1.com", ROAMING="VISITING";%%

### RETCODE = 0  操作成功

### 结果如下

### --------

### IMSI            IMEI   MSISDN         EBI或者NSAPI  PDU会话ID  用户IP类型  用户IPv4地址  用户IPv6地址  IPv4地址的域标识  POD名称

### 12300123456789  NULL  8612345678901    NULL          5          IPv4        192.168.0.1   ::            NULL              sm2-pod-0

### (结果个数 = 1)

### ---    END

### 6 登录**拜访地****AMF**的OM Portal。

### 7 进入“MML命令行-UNC”窗口。

### 8 查询用户的会话信息。

### 预期结果：查询到“归属SMF的Instance ID”为测试终端归属网络的SMF，“PDU会话的漫游类型”为“Home Routed”。

### %%DSP USRSESSIONCTX:PDUSESSIONID=5, IMSI="12300123456789";%%

### RETCODE = 0  操作成功

### 操作结果如下

### ------------

### PDU会话标识  切片信息  漫游用户归属地切片信息  DNN           RAB状态  EBI ARP映射关系  SM上下文索引  接入类型  归属SMF的Instance ID  拜访SMF的Instance ID  中间SMF的Instance ID  网络切片Instance ID  N11接口的容灾状态  	PDU会话的漫游类型

### 5            0-000000  0-000001                huawei.com    否       NULL             1234567890    3GPP接入  SMF_Instance_0       NULL                  NULL                  NULL                 NotTakeover                Home Routed

### (结果个数 = 1)

### ---    END

### 9 查询用户的5G移动性管理上下文相关信息。

### 预期结果：查询到用户的“漫游属性”为“漫游用户”。

### %%DSP NGMMCTX: QUERYOPT=IMSI, IMSI="12300123456789";%%

### RETCODE = 0  操作成功

### 结果如下

### ------------------------

### POD ID  =  uncpod-0

### IMSI  =  12300123456789

### MSISDN  =  8612345678901

### ...

### 漫游属性  =  漫游用户

### RM状态  =  已注册状态

### CM状态  =  已连接状态

### RRC状态  =  Connected

### 可达标志  =  可达

### ...

### 无线接入类型  =  5G接入

### (Number of results = 1)

### ---    END

### 10 查询5G漫游用户移动性管理上下文相关信息。

### 预期结果：查询到用户的移动性管理上下文相关信息。

### %%DSP NGROAMMMCTX: QUERYOPT=IMSI, IMSI="12300123456789";%%

### RETCODE = 0  Operation succeeded

### The result is as follows

### ------------------------

### MSISDN  =  8612345678901

### IMSI  =  12300123456789

### IMEI  =  NULL

### GUTI  =  12300000041405502F8

### 请求的网络切片  =  NULL

### 配置的网络切片  =  1-010101

### 允许的网络切片  =  1-010101

### 漫游切片映射关系  =  1-010101:2-010101;1-010102:2-010101

### (Number of results = 1)

### ---    END

