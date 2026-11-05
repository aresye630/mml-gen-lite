---
id: ''
name: 配置鉴权数据
ne_type: UEG
type: feature
description: 园区UDM（风筝L）上需要配置鉴权数据（K4密钥和K4加密算法），用于和从中心UDM同步的用户鉴权参数（KIVALUE和OPCVALUE）配合实现网络与用户双向鉴权。  园区UDM（风筝L）配置的K4密钥和K4加密算法，需要与中心UDM完全一致。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置UDM/HSS","配置用户数据同步","配置鉴权数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
园区UDM（风筝L）上需要配置鉴权数据（K4密钥和K4加密算法），用于和从中心UDM同步的用户鉴权参数（KIVALUE和OPCVALUE）配合实现网络与用户双向鉴权。园区UDM（风筝L）配置的K4密钥和K4加密算法，需要与中心UDM完全一致。

## 必备事项
前提条件

操作人员具有PGW Web LMT的操作权限。
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
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '运营商统一规划。该参数在一个UDM内唯一，不能重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFVALUE:
          name: 'AMF值'
          type: string
          required: false
          description: '鉴权管理域，用于计算MAC。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONSTANTPROV:
          name: '是否使用Milenage鉴权算法的控制参数'
          type: string
          required: false
          description: '与中心UDM的值一致。   * TRUE：表示计算鉴权时使用本命令配置的C1~C5和R1~R5参数值。 * FALSE：表示计算鉴权时使用**SET MAPSERV**中配置的AUTH\_MILENAGE\_C1~C5和AUTH\_MILENAGE\_R1~R5参数值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        XRES_LENTH:
          name: 'Milenage算法XRES鉴权参数长度'
          type: string
          required: false
          description: '用于标识在鉴权消息中，当鉴权算法为Milenage或Milenage\_2算法时，UDM下发XRES鉴权参数的长度。支持4字节或8字节，此处以8字节为例。  系统初始值为255，即该参数失效，以**SET MAPCONF**命令中参数“是否支持下发4字节的XRES”为准。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NGCSQNIND:
          name: '5GC域SQN的IND取值'
          type: string
          required: false
          description: '与对端设备的SQN的IND值相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_amf_list_1:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '需通过命令**ADD HLRSN**添加后才可在此引用。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '运营商统一规划。该参数在一个UDM内唯一，不能重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMFVALUE:
          name: 'AMF值'
          type: string
          required: false
          description: '鉴权管理域，用于计算MAC。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONSTANTPROV:
          name: '是否使用Milenage鉴权算法的控制参数'
          type: string
          required: false
          description: '与中心UDM的值一致。   * TRUE：表示计算鉴权时使用本命令配置的C1~C5和R1~R5参数值。 * FALSE：表示计算鉴权时使用**SET MAPSERV**中配置的AUTH\_MILENAGE\_C1~C5和AUTH\_MILENAGE\_R1~R5参数值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        C1:
          name: 'Milenage鉴权算法c1参数'
          type: string
          required: false
          description: '**CONSTANTPROV**设置为“TRUE”时需要规划，与中心UDM的值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        C2:
          name: 'Milenage鉴权算法c2参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        C3:
          name: 'Milenage鉴权算法c3参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        C4:
          name: 'Milenage鉴权算法c4参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        C5:
          name: 'Milenage鉴权算法c5参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        R1:
          name: 'Milenage鉴权算法r1参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        R2:
          name: 'Milenage鉴权算法r2参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        R3:
          name: 'Milenage鉴权算法r3参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        R4:
          name: 'Milenage鉴权算法r4参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        R5:
          name: 'Milenage鉴权算法r5参数'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        XRES_LENTH:
          name: 'Milenage算法XRES鉴权参数长度'
          type: string
          required: false
          description: '用于标识在鉴权消息中，当鉴权算法为Milenage或Milenage\_2算法时，UDM下发XRES鉴权参数的长度。支持4字节或8字节，此处以8字节为例。  系统初始值为255，即该参数失效，以**SET MAPCONF**命令中参数“是否支持下发4字节的XRES”为准。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NGCSQNIND:
          name: '5GC域SQN的IND取值'
          type: string
          required: false
          description: '与对端设备的SQN的IND值相同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_k4_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD AMF**中的“HLR序列号”保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '与中心UDM的值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        KEYTYPE:
          name: 'K4密钥输入方式'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALGTYPE:
          name: '算法类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        K4VALUE:
          name: 'K4值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_op_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '与**ADD AMF**中的“HLR序列号”保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        OPSNO:
          name: 'OP序列号'
          type: string
          required: false
          description: '与中心UDM的值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OPVALUE:
          name: 'OP值'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_amf_list:
    - HLRSN: '1'
      AMFSNO: '1'
      AMFVALUE: '1111'
      CONSTANTPROV: FALSE
      XRES_LENTH: '255'
      NGCSQNIND: '18'
    add_amf_list_1:
    - HLRSN: '1'
      AMFSNO: '1'
      AMFVALUE: '1111'
      CONSTANTPROV: TRUE
      C1: '00000000000000000000000000000000'
      C2: '00000000000000000000000000000001'
      C3: '00000000000000000000000000000002'
      C4: '00000000000000000000000000000004'
      C5: 00000000000000000000000000000008
      R1: '40'
      R2: '00'
      R3: '20'
      R4: '40'
      R5: '60'
      XRES_LENTH: '8'
      NGCSQNIND: '18'
    add_k4_list:
    - HLRSN: '1'
      K4SNO: '1'
      KEYTYPE: ClearKey
      ALGTYPE: AES128
      K4VALUE: '*****'
    add_op_list:
    - HLRSN: '1'
      OPSNO: '1'
      OPVALUE: 1234567890abcdef1234567890abcde1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD AMF**命令设置AMF值。

#### 2.1 //计算鉴权时使用**SET MAPSERV**中配置的AUTH\_MILENAGE\_C1~C5和AUTH\_MILENAGE\_R1~R5参数值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amf_list的变量区（command: ADD AMF） -#}
<!-- MISSING_MACRO: command=ADD AMF list_name=add_amf_list step_id=2.1 -->
```

#### 2.2 //计算鉴权时使用本命令设置的C1~C5和R1~R5参数值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amf_list_1的变量区（command: ADD AMF） -#}
<!-- MISSING_MACRO: command=ADD AMF list_name=add_amf_list_1 step_id=2.2 -->
```

### 3 执行**ADD K4**命令设置用于加密KI的K4值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_k4_list的变量区（command: ADD K4） -#}
<!-- MISSING_MACRO: command=ADD K4 list_name=add_k4_list step_id=3 -->
```

### 4 USIM卡中烧制了OP时，执行**ADD OP**命令设置OP值。USIM卡中烧制了OPC时，请跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_op_list的变量区（command: ADD OP） -#}
<!-- MISSING_MACRO: command=ADD OP list_name=add_op_list step_id=4 -->
```

