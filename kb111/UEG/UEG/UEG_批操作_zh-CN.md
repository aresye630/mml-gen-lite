---
id: ''
name: 批操作
ne_type: UEG
type: feature
description: 该任务指导操作人员通过PGW Web LMT客户端完成批操作。  批操作可以完成以下任务：  * 同时为多个用户提供加载KI、开户、改号、补卡等业务操作 * 批量执行MML命令
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据维护","批操作管理","批操作"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务指导操作人员通过PGW Web LMT客户端完成批操作。批操作可以完成以下任务：* 同时为多个用户提供加载KI、开户、改号、补卡等业务操作* 批量执行MML命令

## 必备事项
前提条件

前提条件

连续/非连续号段批操作和文件批操作需要在执行任务前准备批操作文件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ki_list:
      type: items
      properties:
        HLRSN:
          name: 'HLRSN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FNAME:
          name: 'FNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4SNO'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CARDTYPE:
          name: 'CARDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ALG:
          name: 'ALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ki_list:
    - HLRSN: '1'
      FNAME: ADDKI.txt
      K4SNO: '2'
      CARDTYPE: SIM
      ALG: COMP128_3
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录PGW Web LMT MML命令界面。

### 2 执行批操作。

### 《用户管理》手册开户、销户、补卡、改号等页面提到的批操作，均可参考以下四种批操作之一。

#### 2.1 * **非连续号段批操作**

##### 2.1.1 单击“文件管理器”，上传批操作文件到指定目录。

##### 上传的具体操作请参见上传文件。

##### 如果需要下载或删除批操作文件，操作方法请参见下载文件或删除文件。

##### 2.1.2 执行批操作。

##### 当为多个非连续号段用户进行鉴权数据管理、用户管理以及签约各种业务时，执行相应命令，输入批操作文件名和其他相关参数。

##### 命令举例：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=2.1.2 -->
```

##### 上述举例完成为多个非连续号段用户通过批操作加载KI，批操作文件格式请参见**必备事项**中的**数据**。

#### 2.2 * **连续号段批操作**

#### 当为多个连续号段用户进行鉴权状态管理、用户管理以及签约各种业务时，执行相应命令，输入“IMSI”或“MSISDN”、“用户个数”和其他相关参数。

#### 命令举例：

#### 上述举例完成查询IMSI起始号码为460000009012345的10个连续号码用户的鉴权状态。

#### 2.3 * **文件批操作**

##### 2.3.1 单击“文件管理器”，上传批操作文件到指定目录。

##### 上传的具体操作请参见上传文件。

##### 如果需要下载或删除批操作文件，操作方法请参见下载文件或删除文件。

##### 2.3.2 执行**BAT**命令，输入“文件名”和“执行时间”。

#### 2.4 * **批处理MML**

#### PGW WebUI上的操作请参见批处理。

