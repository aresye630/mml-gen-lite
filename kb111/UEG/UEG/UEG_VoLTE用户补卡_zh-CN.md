---
id: GWFD-025805
name: VoLTE用户补卡
ne_type: UEG
type: feature
description: 用户因手机丢失、USIM卡损坏等原因需要补办手机卡时，需要对用户进行补卡配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-025800 UDM语音基本功能","GWFD-025805 支持VoLTE","特性配置","VoLTE用户补卡"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用户因手机丢失、USIM卡损坏等原因需要补办手机卡时，需要对用户进行补卡配置。

## 必备事项
前提条件

* 操作人员已完全了解支持VoLTE特性。
* 已完成VoLTE用户的业务发放。
* 操作人员具有业务发放权限。
* 已完成IMS网络、CS网络、HLR/HSS数据库以及EPC网络各网元的基本数据配置和对接数据配置，各网元运行正常。
* 操作人员具有PGW Web LMT的用户名和密码
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
          name: 'HLR序列号'
          type: string
          required: false
          description: 'HLR序列号，有效值域为1～255。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用户标识。'
          data_source: ''
          pattern: ''
          default: ''
        KIVALUE:
          name: 'KI值'
          type: string
          required: false
          description: 'KI值，32位的十六进制数字组成的字符串。'
          data_source: ''
          pattern: ''
          default: ''
        K2SNO:
          name: 'K2SNO'
          type: string
          required: false
          description: '该值已通过**ADD K2**命令添加。'
          data_source: ''
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '卡的类型，值域为SIM与USIM。   * SIM：SIM卡用户，采用GSM鉴权的2G用户。 * USIM：USIM卡用户，采用UMTS鉴权的3G用户或EPS-AKA鉴权，EAP-AKA，EAP-AKA''鉴权的4G用户。'
          data_source: ''
          pattern: ''
          default: ''
        ALG:
          name: '鉴权算法类型'
          type: string
          required: false
          description: '此处填写为MILENAGE算法。'
          data_source: ''
          pattern: ''
          default: ''
        OPCVALUE:
          name: 'OPC值'
          type: string
          required: false
          description: 'OPC值为对OP以KI为密钥进行加密，然后再以K4为密钥进行加密计算得到的结果，32位的十六进制数字组成的字符串。'
          data_source: ''
          pattern: ''
          default: ''
    mod_imsi_list:
      type: items
      properties:
        IMSI:
          name: '旧IMSI'
          type: string
          required: false
          description: '用来标识补卡前的IMSI值。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMSI:
          name: '新IMSI'
          type: string
          required: false
          description: '用来指定新的IMSI值。'
          data_source: ''
          pattern: ''
          default: ''
    mod_hhssimsi_list:
      type: items
      properties:
        IMPI:
          name: 'IMPI'
          type: string
          required: false
          description: '用于指定需要修改的旧的IMPI(IMS)。'
          data_source: ''
          pattern: ''
          default: ''
        IMPU:
          name: 'IMPU'
          type: string
          required: false
          description: '用于指定需要修改的旧的T-IMPU(IMS)。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPI:
          name: '新的IMPI'
          type: string
          required: false
          description: '用于指定一个新的IMPI(IMS)。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPIAUTHTYPE:
          name: '新的IMPI的鉴权类型'
          type: string
          required: false
          description: '表示IMPI(IMS)支持Early AKA鉴权。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '这里关联到补卡后的新IMSI值。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPU:
          name: '新的IMPU'
          type: string
          required: false
          description: '用于指定一个新的T-IMPU(IMS)。'
          data_source: ''
          pattern: ''
          default: ''
        IMPI2:
          name: 'IMPI2'
          type: string
          required: false
          description: '用于指定需要修改的旧的IMPI(ICS)。'
          data_source: ''
          pattern: ''
          default: ''
        IMPU2:
          name: 'IMPU2'
          type: string
          required: false
          description: '用于指定需要修改的旧的T-IMPU(ICS)。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPI2:
          name: '新的IMPI2'
          type: string
          required: false
          description: '用于指定一个新的IMPI(ICS)。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPI2AUTHTYPE:
          name: '新的IMPI2的鉴权类型'
          type: string
          required: false
          description: '表示IMPI(ICS)支持TAA鉴权。'
          data_source: ''
          pattern: ''
          default: ''
        NEWIMPU2:
          name: '新的IMPU2'
          type: string
          required: false
          description: '用于指定一个新的T-IMPU(ICS)。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ki_list:
    - HLRSN: '1'
      IMSI: '46009000000123'
      KIVALUE: '*****'
      K2SNO: '0'
      CARDTYPE: USIM
      ALG: MILENAGE
      OPCVALUE: '*****'
    mod_imsi_list:
    - IMSI: '46009876543210'
      NEWIMSI: '46009000000123'
    mod_hhssimsi_list:
    - IMPI: 46009876543210@ims.mnc000.mcc460.3gppnetwork.org
      IMPU: sip:46009876543210@ims.mnc000.mcc460.3gppnetwork.org
      NEWIMPI: 46009000000123@ims.mnc000.mcc460.3gppnetwork.org
      NEWIMPIAUTHTYPE: EAA
      IMSI: '46009000000123'
      NEWIMPU: sip:46009000000123@ims.mnc000.mcc460.3gppnetwork.org
      IMPI2: 46009876543210@ics.mnc000.mcc460.3gppnetwork.org
      IMPU2: sip:46009876543210@ics.mnc000.mcc460.3gppnetwork.org
      NEWIMPI2: 46009000000123@ics.mnc000.mcc460.3gppnetwork.org
      NEWIMPI2AUTHTYPE: TAA
      NEWIMPU2: sip:46009000000123@ics.mnc000.mcc460.3gppnetwork.org
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD KI**命令为新的IMSI号码增加鉴权数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=2 -->
```

### 3 执行**MOD IMSI**命令为用户关联新的IMSI。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_imsi_list的变量区（command: MOD IMSI） -#}
<!-- MISSING_MACRO: command=MOD IMSI list_name=mod_imsi_list step_id=3 -->
```

### 4 登录“IMS-HSS业务管理”窗口。

### 5 执行**MOD HHSSIMSI**命令为用户关联新的IMSI、IMPI和IMPU。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_hhssimsi_list的变量区（command: MOD HHSSIMSI） -#}
<!-- MISSING_MACRO: command=MOD HHSSIMSI list_name=mod_hhssimsi_list step_id=5 -->
```

