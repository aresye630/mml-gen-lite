---
id: ''
name: 检查漫游用户数
ne_type: UDG
type: feature
description: 通过检查NF上漫游用户数，以确认国际漫游功能运行正常。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 国际漫游解决方案","例行维护","检查漫游用户数"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
通过检查NF上漫游用户数，以确认国际漫游功能运行正常。

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

### 4 查询SMF上的用户数。

### 预期结果：查询到漫入漫出的用户数相关信息。

### %%DSP SMUSERNUM: QRY_SCOPE=SUMMARY, QRY_CLASS=SUMMARY;%%

### RETCODE = 0  操作成功

### 结果如下

### --------

### 查询分类  =  汇总信息

### GTPv1用户数  =  123

### 本网签约并在本网接入的GTPv1用户数  =  123

### 异网漫入并在拜访地接入的GTPv1用户数  =  123

### 漫出并在回归属地激活的GTPv1用户数  =  123

### GTPv2用户数  =  123

### 本网签约并在本网接入的GTPv2用户数  =  123

### 异网漫入并在拜访地接入的GTPv2用户数  =  123

### 漫出并在回归属地激活的GTPv2用户数  =  123

### SA用户数  =  123

### 本网签约并在本网接入的SA用户数  =  123

### 异网漫入并在拜访地接入的SA用户数  =  123

### 漫出并在回归属地激活的SA用户数  =  123

### (结果个数 = 1)

### ---    END

### 5 登录**拜访地****AMF**的OM Portal。

### 6 进入“MML命令行-UNC”窗口。

### 7 查询AMF上的动态漫游用户数。

### 预期结果：AMF上的“动态漫游用户数”与实际规划一致。

### %%DSP NGUSERRESOURCE:QUERYSCOPE=SUMMARY,QUERYTYPE=SRVPLMN,MCC="123",MNC="00";%%

### RETCODE = 0  操作成功

### 结果如下

### ------------------------

### 移动国家码  =  123

### 移动网号  =  00

### 动态用户数  =  1000

### 动态漫游用户数  =  500

### (结果个数 = 1)

### ---    END

