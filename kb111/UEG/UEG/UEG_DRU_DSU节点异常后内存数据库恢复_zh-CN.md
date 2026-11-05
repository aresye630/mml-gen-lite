---
id: ''
name: DRU/DSU节点异常后内存数据库恢复
ne_type: UEG
type: feature
description: 同个Cluster中的一个DRU/DSU节点发生异常后，节点会自动重新启动，并按照以下次序自动加载数据：  1. 系统默认自动首先选择从Master节点进行内存数据库数据加载。     该方式最安全、最常用，也是推荐的方式，数据一致性最能得到保证。 2. 如果从Master节点加载异常则选择从虚拟机硬盘加载。 3. 在上面两种方式都无法执行的情况下会选择从指定目录进行加载。  DRU/DSU节点自动加载数据后可通过查询命令对节点的加载状态进行查询。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG USCDB数据备份与恢复（风筝L）","备份与恢复用户手册","系统异常时自动恢复","DRU/DSU节点异常后内存数据库恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
同个Cluster中的一个DRU/DSU节点发生异常后，节点会自动重新启动，并按照以下次序自动加载数据：1. 系统默认自动首先选择从Master节点进行内存数据库数据加载。   该方式最安全、最常用，也是推荐的方式，数据一致性最能得到保证。2. 如果从Master节点加载异常则选择从虚拟机硬盘加载。3. 在上面两种方式都无法执行的情况下会选择从指定目录进行加载。DRU/DSU节点自动加载数据后可通过查询命令对节点的加载状态进行查询。

## 必备事项
前提条件

DRU/DSU节点发生异常。
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

### 1 登录“USCDB MML命令”界面。

### 2 执行**DSP NODE**命令查看节点的数据加载状态。

### 查看各节点的“节点状态”信息：

### 如果为“初始化”、“加载中”、“加载完毕 ”或“初始化完成”表示节点还处在数据加载状态。

### 如果为“Master”或“Slave”表示节点的数据已经加载完。

