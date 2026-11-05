---
id: ''
name: EPS用户开户
ne_type: UEG
type: feature
description: 该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，通过模板开户方式完成SAE-HSS开户数据的配置。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG UDM用户管理（风筝L）","用户数据配置（EPS网络）","SAE-HSS用户数据配置","EPS用户开户"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该操作指导工程师在开局阶段，新建UDM作为SAE-HSS网元时，通过模板开户方式完成SAE-HSS开户数据的配置。

## 必备事项
前提条件

* 已经完成UDM的OMU侧的硬件数据和基础数据的配置。
* 已经完成SAE-HSS的用户数据规划。
* 已经完成SAE-HSS的全局数据、模板数据、鉴权数据的配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_subtpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        TPLTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: '–'
          data_source: ''
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '–'
          data_source: ''
          pattern: ''
          default: ''
        NAM:
          name: '网络接入模式'
          type: string
          required: false
          description: '为EPS用户开户时，该参数必须设置为“NONE”。'
          data_source: ''
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '–'
          data_source: ''
          pattern: ''
          default: ''
        TS:
          name: '电信业务'
          type: string
          required: false
          description: '–'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: string
          required: false
          description: '工程设计输出。  为EPS用户开户时，该参数必须设置。'
          data_source: ''
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: string
          required: false
          description: '工程设计输出。  为EPS用户开户时，该参数必须设置。'
          data_source: ''
          pattern: ''
          default: ''
        NON3GPPSUPP:
          name: '是否支持Non-3GPP接入'
          type: string
          required: false
          description: '如果要同时为Non-3GPP接入的EPS用户开户，则该参数需要设置为“TRUE”。'
          data_source: ''
          pattern: ''
          default: ''
        VOWIFI_TAG:
          name: 'VoWIFI用户标志'
          type: string
          required: false
          description: '由运营商根据需要选择。  取值范围：   * VoWIFI：用户支持VoWIFI时，配置该值。 * Non\_VoWIFI：用户不支持VoWIFI时，配置该值。'
          data_source: ''
          pattern: ''
          default: ''
    mod_nonsub_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        NON3GPPSUPP:
          name: '是否支持Non-3GPP接入'
          type: string
          required: false
          description: '如果要同时为Non-3GPP接入的EPS用户开户，则该参数需要设置为“TRUE”。'
          data_source: ''
          pattern: ''
          default: ''
        VOWIFI_TAG:
          name: 'VoWIFI用户标志'
          type: string
          required: false
          description: '由运营商根据需要选择。  取值范围：   * VoWIFI：用户支持VoWIFI时，配置该值。 * Non\_VoWIFI：用户不支持VoWIFI时，配置该值。'
          data_source: ''
          pattern: ''
          default: ''
    add_tplsub_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '工程设计输出。'
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
    mod_tploptgprs_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        PROV:
          name: '是否提供优化GPRS/EPS业务'
          type: string
          required: false
          description: '根据运营商要求配置。'
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '优化GPRS/EPS模板ID'
          type: string
          required: false
          description: '引用**ADD OPTGPRSTPL**命令中定义的优化EPS模板ID。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_subtpl_list:
    - HLRSN: '1'
      TPLID: '300'
      TPLTYPE: NORMAL
      CARDTYPE: USIM
      NAM: NONE
      EPS: TRUE
      TS: TS11
      AMBRMAXUL: '1000000000'
      AMBRMAXDL: '2000000000'
      NON3GPPSUPP: TRUE
      VOWIFI_TAG: VoWIFI
    mod_nonsub_list:
    - IMSI: '460000009123456'
      NON3GPPSUPP: TRUE
      VOWIFI_TAG: VoWIFI
    add_tplsub_list:
    - HLRSN: '1'
      IMSI: '460000009123456'
      TPLID: '300'
      ISDN: '8613912345678'
    mod_tploptgprs_list:
    - IMSI: '460000009123456'
      PROV: TRUE
      TPLID: '50'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD SUBTPL**命令，制作开户模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_subtpl_list的变量区（command: ADD SUBTPL） -#}
<!-- MISSING_MACRO: command=ADD SUBTPL list_name=add_subtpl_list step_id=2 -->
```

### 将一个开户用户的业务信息进行模板化。

### 参数“AMBRMAXUL”和“AMBRMAXDL”必须设置，这样**MOD OPTGPRS**命令才能为EPS用户签约APN信息。

### 为EPS用户开户，参数“网络接入模式”必须设置为“NONE”。

### 如果需要同时为Non-3GPP接入的EPS用户开户，则参数“是否支持Non-3GPP接入”需要设置为“TRUE”。

### 3 **可选：**执行**MOD NONSUB**命令，修改EPS用户的Non-3GPP接入属性。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nonsub_list的变量区（command: MOD NONSUB） -#}
<!-- MISSING_MACRO: command=MOD NONSUB list_name=mod_nonsub_list step_id=3 -->
```

### 当2中的参数“是否支持Non-3GPP接入”未设置为“TRUE”时，如果需要同时为Non-3GPP接入的EPS用户开户，执行该步骤。

### 4 执行**ADD TPLSUB**命令进行模板开户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tplsub_list的变量区（command: ADD TPLSUB） -#}
<!-- MISSING_MACRO: command=ADD TPLSUB list_name=add_tplsub_list step_id=4 -->
```

### 一批用户签约同样的业务信息，通过模板开户的方式使用同一开户模板为用户开户。

### 5 执行**MOD TPLOPTGPRS**命令，使用优化EPS模板来签约EPS业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_tploptgprs_list的变量区（command: MOD TPLOPTGPRS） -#}
<!-- MISSING_MACRO: command=MOD TPLOPTGPRS list_name=mod_tploptgprs_list step_id=5 -->
```

### 为用户签约多条APN信息，或需要为大量用户签约相同的APN信息，使用此命令进行模板签约。

