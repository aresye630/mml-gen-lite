---
id: ''
name: 配置SAE-HSS鉴权数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS鉴权数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","SAE-HSS用户数据配置","配置SAE-HSS鉴权数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，完成SAE-HSS鉴权数据的配置。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成SAE-HSS的用户数据规划。
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

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD AMF**命令设置AMF值。

### 3 执行**ADD K4**命令设置用于加密KI的K4值。

### 4 如果USIM卡中烧制了OP，执行**ADD OP**命令设置OP值。

### 在WCDMA/TD-SCDMA网络中，设置OP值时，要注意以下几点：

#### 4.1 USIM卡中烧制了OP时，要设置OP值。

#### 4.2 USIM卡中烧制了OPC时，不用设置OP值。

### 5 执行**ADD KI**命令加载KI。

#### 5.1 参数“卡类型”设置为“USIM”。

#### 5.2 参数“鉴权算法类型”根据实际需求进行设置。

### 如果需要进行批量操作，编写KI批操作文件，并上传到PGW Server指定位置。

### 编写KI批操作文件时，要注意以下几点：

#### 5.3 KI批操作文件的格式和上传位置请参见批操作管理。

#### 使用MILENAGE算法时:

##### 5.3.1 USIM卡中烧制了OPC时，KI批操作文件中要包含参数OPC。

##### 5.3.2 USIM卡中烧制了OP时，KI批操作文件中不包含参数OPC。

#### 5.4 KI批操作文件的上传方法请参见管理文件。

