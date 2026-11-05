---
id: ''
name: 检查系统运行状态
ne_type: UEG
type: feature
description: 检查资源单元的状态，确保设备运行正常。
tags: []
risk_level: ''
doc_source:
  - ["日常维护","UEG 例行维护（风筝M，虚机容器）","例行维护操作指导","日维护","检查系统运行状态"]
  - ["日常维护","UEG 例行维护（风筝M，裸机容器）","例行维护操作指导","日维护","检查系统运行状态"]
  - ["日常维护","UEG 例行维护（风筝L，虚机容器）","例行维护操作指导","日维护","检查系统运行状态"]
  - ["日常维护","UEG 例行维护（风筝L，裸机容器）","例行维护操作指导","日维护","检查系统运行状态"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
检查资源单元的状态，确保设备运行正常。

## 必备事项
前提条件

已经登录OM Portal，或者登录MAE并进入Access子系统。
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

### 1 通过执行**DSP POD**命令查询当前系统中Pod运行情况。

### 预期结果：“Pod状态”为“Running”。

### 异常结果：“Pod状态”为其他值。请在FusionStage上查看是否存在本VNF项目的告警并处理。如果告警处理完毕后，状态仍然不符合预期，请收集相关信息并联系华为技术支持处理。

### 2 通过执行**LST VNFC**命令查询当前系统的所包含的VNFC实例，记录系统中每个VNFC实例的“管理代理标识”。

### 3 针对2中查询到的每个VNFC实例（VNFP除外），分别执行**DSP RU**和**DSP SERVICERUSTATE**命令查看资源单元（RU）运行情况。其中“SERVICEINSTANCE”参数为2中记录的“管理代理标识”。

### 预期结果：“运行状态”或“RU的状态”为“正常”。

### 异常结果：“运行状态”或“RU的状态”为其他值。请查看是否存在RU相关告警并处理。如果告警处理完毕后，状态仍然不符合预期，请收集相关信息并联系华为技术支持处理。

### **DSP RU**命令不支持查看“VNFC类型名称”为VNFP的RU状态查询。

### **DSP SERVICERUSTATE**命令不支持查看“VNFC类型名称”为VNFP、VNRS\_VNFC、ACS的RU状态查询。

### 4 针对2中查询到的每个VNFC实例，分别执行**DSP PROCESSINFO**查看其进程状态。其中“SERVICEINSTANCE”参数为2中记录的“管理代理标识”。

### 预期结果：“进程状态”为“NORMAL”。

### 异常结果：“运行状态”为“ABNORMAL”。请查看是否存在进程相关告警并处理。如果告警处理完毕后，状态仍然不符合预期，请收集相关信息并联系华为技术支持处理。

### **DSP PROCESSINFO**命令不支持查看“VNFC类型名称”为VNFP的RU状态查询。

### 5 通过**DSP CELLSTAT**命令查询当前系统中所有微服务进程的状态。

### 命令执行脚本参考：DSP CELLSTAT: OBJECT=VNF;

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

### 异常结果：“未就绪进程数”或“故障进程数”不为0。此时，请按以下步骤进行处理：

#### 5.1 通过**DSP CELLSTAT**命令查询当前系统中存在未就绪进程或故障进程的Pod对象，并记录其Pod名称。

#### 命令执行脚本参考：DSP CELLSTAT: OBJECT=PODTYPE;

#### 5.2 针对存在未就绪进程或故障进程的Pod对象，依次通过**DSP CELLINFO**命令查询进程故障原因。

#### 命令执行脚本参考：DSP CELLINFO: OBJECT=PODNAME, PODNAME="xxx"; //xxx为5.a查询到的Pod名称。

#### 5.3 保存上述MML执行结果信息，联系华为技术支持处理。

