---
id: GWFD-024902
name: 配置EPS-AKA鉴权
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员通过PGW Web LMT配置EPS-AKA鉴权相关数据。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-024900 HSS FE基本功能","GWFD-024902 4G网络鉴权功能","特性配置","配置EPS-AKA鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员通过PGW Web LMT配置EPS-AKA鉴权相关数据。

## 必备事项
前提条件

* 操作人员已完全了解EPS-AKA鉴权功能。
* 已经完成基础数据的配置。
* 操作人员具有数据配置权限。
* 操作人员具有业务发放权限。
* 操作人员具有PGW Web LMT的用户名和密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_mapserv_list:
      type: items
      properties:
        AUTH_MILENAGE_C1:
          name: 'Milenage鉴权算法c1参数'
          type: string
          required: false
          description: '参数控制MILENAGE鉴权算法的计算细节，会对鉴权结果产生影响，配置前需要与运营商协商。'
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_C2:
          name: 'Milenage鉴权算法c2参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_C3:
          name: 'Milenage鉴权算法c3参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_C4:
          name: 'Milenage鉴权算法c4参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_C5:
          name: 'Milenage鉴权算法c5参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_R1:
          name: 'Milenage鉴权算法r1参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_R2:
          name: 'Milenage鉴权算法r2参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_R3:
          name: 'Milenage鉴权算法r3参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_R4:
          name: 'Milenage鉴权算法r4参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTH_MILENAGE_R5:
          name: 'Milenage鉴权算法r5参数'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LTESQNIND:
          name: 'EPS域SQN的IND取值'
          type: string
          required: false
          description: '用于设置EPS域SQN的IND取值。'
          data_source: ''
          pattern: ''
          default: ''
    set_mapconf_list:
      type: items
      properties:
        SENDALLQUINTUPLET:
          name: '是否一次返回全部五元组'
          type: string
          required: false
          description: '用于设置HLR是在一条取鉴权五元组响应消息中将所有请求的五元组返回给VLR/SGSN，还是分多条响应消息返回。  取值范围：  * TRUE：一次返回请求的全部五元组。 * FALSE：分多个响应消息返回请求的五元组。'
          data_source: ''
          pattern: ''
          default: ''
        AKSWITCH:
          name: '鉴权加密开关'
          type: string
          required: false
          description: '用于设置是否对SQN加密。  取值范围：  * TRUE：当需要通过加密SQN来提高网络安全性时配置。 * FALSE：当不需要加密SQN时配置。  说明：该参数需要与运营商协商后进行配置。'
          data_source: ''
          pattern: ''
          default: ''
    add_amf_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '配置EPS-AKA鉴权的用户所在“HLR序列号”。'
          data_source: ''
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '由运营商统一规划。  取值范围：1～65535。'
          data_source: ''
          pattern: ''
          default: ''
        AMFVALUE:
          name: 'AMF值'
          type: string
          required: false
          description: '鉴权管理域，用于计算MAC。  取值范围：0000～FFFF。'
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
          description: '配置EPS-AKA鉴权的用户所在“HLR序列号”。'
          data_source: ''
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '由运营商统一规划。  取值范围：1～65535。'
          data_source: ''
          pattern: ''
          default: ''
        KEYTYPE:
          name: 'K4密钥输入方式'
          type: string
          required: false
          description: '本端规划  用于标识K4密钥输入方式。'
          data_source: ''
          pattern: ''
          default: ''
        ALGTYPE:
          name: '算法类型'
          type: string
          required: false
          description: '本端规划  用于标识K4值的加密算法类型。'
          data_source: ''
          pattern: ''
          default: ''
        K4VALUE:
          name: 'K4值'
          type: string
          required: false
          description: '本端规划  用于标识K4密钥值。'
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
          description: '配置EPS-AKA鉴权的用户所在“HLR序列号”。'
          data_source: ''
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: '由运营商统一规划。  取值范围：1～16777215。'
          data_source: ''
          pattern: ''
          default: ''
        OPVALUE:
          name: 'OP值'
          type: string
          required: false
          description: 'MILENAGE鉴权算法的一个输入参数，需与USIM卡中烧制的OP值一致。  取值范围：32位的十六进制数字组成的字符串。'
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
          description: '用于标识本地HLR，由运营商统一规划。  该参数必须先由**ADD HLRSN**命令定义后，才能在此处引用。'
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
          description: '用于添加IMSI对应的KI值。'
          data_source: ''
          pattern: ''
          default: ''
        KIVALUE:
          name: 'KI值'
          type: string
          required: false
          description: '由运营商统一规划。  取值范围：32位的十六进制数字组成的字符串。'
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
          description: '采用EPS-AKA鉴权用户卡类型为USIM卡。'
          data_source: ''
          pattern: ''
          default: ''
        ALG:
          name: '鉴权算法类型'
          type: string
          required: false
          description: '选择EPS-AKA鉴权使用的算法。  由运营商根据实际需求进行设置，与USIM卡中烧制的鉴权算法保持一致。'
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
        OPC:
          name: 'OPC值'
          type: string
          required: false
          description: '可选，USIM卡中烧制了OPC时配置。  与USIM中烧制的OPC值一致。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_mapserv_list:
    - AUTH_MILENAGE_C1: '00000000000000000000000000000000'
      AUTH_MILENAGE_C2: '00000000000000000000000000000001'
      AUTH_MILENAGE_C3: '00000000000000000000000000000002'
      AUTH_MILENAGE_C4: '00000000000000000000000000000004'
      AUTH_MILENAGE_C5: 00000000000000000000000000000008
      AUTH_MILENAGE_R1: '40'
      AUTH_MILENAGE_R2: '00'
      AUTH_MILENAGE_R3: '20'
      AUTH_MILENAGE_R4: '40'
      AUTH_MILENAGE_R5: '60'
      LTESQNIND: '16'
    set_mapconf_list:
    - SENDALLQUINTUPLET: TRUE
      AKSWITCH: TRUE
    add_amf_list:
    - HLRSN: '1'
      AMFSNO: '1'
      AMFVALUE: '*****'
    add_k4_list:
    - HLRSN: '1'
      K4SNO: '1'
      KEYTYPE: ClearKey
      ALGTYPE: AES256
      K4VALUE: '*****'
    add_op_list:
    - HLRSN: '1'
      OPSNO: '1'
      OPVALUE: '*****'
    add_ki_list:
    - HLRSN: '1'
      IMSI: '460456303001002'
      OPERTYPE: ADD
      KIVALUE: '*****'
      K4SNO: '1'
      CARDTYPE: USIM
      ALG: MILENAGE
      OPSNO: '1'
      AMFSNO: '1'
      OPC: 无。
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**SET MAPSERV**命令设置与EPS-AKA鉴权相关的MAP业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list step_id=2 -->
```

### 3 执行**SET MAPCONF**命令设置与EPS-AKA鉴权相关的MAP功能流程数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapconf_list的变量区（command: SET MAPCONF） -#}
<!-- MISSING_MACRO: command=SET MAPCONF list_name=set_mapconf_list step_id=3 -->
```

### 4 执行**ADD AMF**命令设置AMF值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amf_list的变量区（command: ADD AMF） -#}
<!-- MISSING_MACRO: command=ADD AMF list_name=add_amf_list step_id=4 -->
```

### 5 执行**ADD K4**命令设置KI的传输密钥K4。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_k4_list的变量区（command: ADD K4） -#}
<!-- MISSING_MACRO: command=ADD K4 list_name=add_k4_list step_id=5 -->
```

### 6 如果USIM卡中烧制了OP，执行**ADD OP**命令设置OP值。

### 如果USIM卡中烧制了OPC，则跳过此步骤，并在执行7时输入“OPC值”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_op_list的变量区（command: ADD OP） -#}
<!-- MISSING_MACRO: command=ADD OP list_name=add_op_list step_id=6 -->
```

### 7 执行**ADD KI**命令加载KI。

### 如果需要进行批量操作，编写KI批操作文件，并上传PGW Server指定位置。

### 编写KI批操作文件时，要注意以下几点：

### KI批操作文件的格式和上传位置请参见批操作管理。

### KI批操作文件的上传方法请参见管理文件。

### 如果USIM卡中烧制了OPC，KI批操作文件中要包含参数OPC；如果USIM卡中烧制了OP，KI批操作文件中不包含参数OPC。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=7 -->
```

