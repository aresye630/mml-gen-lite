---
id: ''
name: 配置NB-IoT鉴权数据
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段， 新建UDM作为SAE-HSS网元时，完成NB-IoT鉴权数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","NB-IoT用户数据配置","配置NB-IoT鉴权数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段， 新建UDM作为SAE-HSS网元时，完成NB-IoT鉴权数据的配置。

## 必备事项
前提条件

前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成NB-IoT的用户数据规划。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_amf_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD KI**中的“HLR序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        AMFVALUE:
          name: 'AMF值'
          type: string
          required: false
          description: '鉴权管理域，用于计算MAC。'
          data_source: ''
          pattern: ''
          default: ''
    add_k4_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD KI**中的“HLR序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        K4VALUE:
          name: 'K4值'
          type: string
          required: false
          description: '用于标识K4密钥值。'
          data_source: ''
          pattern: ''
          default: ''
    add_op_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD KI**中的“HLR序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        OPVALUE:
          name: 'OP值'
          type: string
          required: false
          description: 'MILENAGE鉴权算法的一个输入参数，需与USIM卡中烧制的OP值一致。'
          data_source: ''
          pattern: ''
          default: ''
    add_ki_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: 'IMSI号码。'
          data_source: ''
          pattern: ''
          default: ''
        OPERTYPE:
          name: '操作类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        KIVALUE:
          name: 'KI值'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '与**ADD K4**中的“K4序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        ALG:
          name: '鉴权算法类型'
          type: string
          required: false
          description: '运营商统一规划。'
          data_source: ''
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: '与**ADD OP**中的“OP序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '与**ADD AMF**中的“AMF序列号”保持一致。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_amf_list:
    - HLRSN: '1'
      AMFSNO: '3'
      AMFVALUE: '1111'
    add_k4_list:
    - HLRSN: '1'
      K4SNO: '4'
      K4VALUE: 1234567890abcdef
    add_op_list:
    - HLRSN: '1'
      OPSNO: '1'
      OPVALUE: 1234567890abcdef1234567890abcde1
    add_ki_list:
    - HLRSN: '1'
      IMSI: '460000009123456'
      OPERTYPE: ADD
      KIVALUE: 1234567890ABCDEF1234567890ABCDEF
      K4SNO: '4'
      CARDTYPE: USIM
      ALG: MILENAGE
      OPSNO: '1'
      AMFSNO: '3'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD AMF**命令设置AMF值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amf_list的变量区（command: ADD AMF） -#}
<!-- MISSING_MACRO: command=ADD AMF list_name=add_amf_list step_id=2 -->
```

### 3 执行**ADD K4**命令设置用于加密KI的K4值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_k4_list的变量区（command: ADD K4） -#}
<!-- MISSING_MACRO: command=ADD K4 list_name=add_k4_list step_id=3 -->
```

### 4 如果USIM卡中烧制了OP，执行**ADD OP**命令设置OP值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_op_list的变量区（command: ADD OP） -#}
<!-- MISSING_MACRO: command=ADD OP list_name=add_op_list step_id=4 -->
```

### 在WCDMA/TD-SCDMA网络中，设置OP值时，要注意以下几点：

#### 4.1 USIM卡中烧制了OP时，要设置OP值。

#### 4.2 USIM卡中烧制了OPC时，不用设置OP值。

### 5 如果需要进行批量操作，编写KI批操作文件，并上传到PGW Server指定位置。

### 编写KI批操作文件时，要注意以下几点：

#### 5.1 KI批操作文件的格式和上传位置请参见批操作管理。

#### 使用MILENAGE算法时:

##### 5.1.1 USIM卡中烧制了OPC时，KI批操作文件中要包含参数OPC。

##### 5.1.2 USIM卡中烧制了OP时，KI批操作文件中不包含参数OPC。

#### 5.2 KI批操作文件的上传方法请参见管理文件。

### 6 执行**ADD KI**命令加载KI。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=6 -->
```

#### 6.1 参数“卡类型”设置为“USIM”。

#### 6.2 参数“鉴权算法类型”根据实际需求进行设置。

