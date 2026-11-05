---
id: GWFD-024702
name: 配置EAP-AKA'鉴权特性
ne_type: UEG
type: feature
description: 本任务旨在指导操作人员配置5G的EAP-AKA'鉴权特性功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-024700 AUSF基本功能","GWFD-024702 EAP-AKA'鉴权","配置EAP-AKA'鉴权特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本任务旨在指导操作人员配置5G的EAP-AKA'鉴权特性功能。

## 必备事项
前提条件

* 请仔细阅读EAP-AKA'鉴权特性功能。
* 操作人员具有PGW Web LMT的操作权限。
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
          description: '已在UDM本局数据配置中通过**ADD HLRSN**命令配置，可以使用**LST HLRSN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '用于标识AMF序列号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFVALUE:
          name: 'AMF值'
          type: string
          required: false
          description: '鉴权管理域，用于计算MAC。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_k4_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '已在UDM本局数据配置中通过**ADD HLRSN**命令配置，可以使用**LST HLRSN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '用于标识K4序列号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEYTYPE:
          name: 'K4密钥输入方式'
          type: string
          required: false
          description: '用于标识K4密钥输入方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALGTYPE:
          name: '算法类型'
          type: string
          required: false
          description: '用于标识K4值的加密算法类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        K4VALUE:
          name: 'K4值'
          type: string
          required: false
          description: '用于标识K4密钥。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ki_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '已在UDM本局数据配置中通过**ADD HLRSN**命令配置，可以使用**LST HLRSN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用户的IMSI号码。  说明：   * 5GC网络中的SUPI等同于IMSI。 * 若使用加密SUCI作为用户标识，则需要签约隐私保护标识功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KIVALUE:
          name: 'KI值'
          type: string
          required: false
          description: '用于标识KI值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        K4SNO:
          name: 'K4序列号'
          type: string
          required: false
          description: '与**ADD K4**命令中定义的“K4序列号”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用户卡类型为USIM卡。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ALG:
          name: '鉴权算法类型'
          type: string
          required: false
          description: '使用MILENAGE鉴权算法类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OPCVALUE:
          name: 'OPC值'
          type: string
          required: false
          description: 'OPC值为对OP以KI为密钥进行加密，然后再以K4为密钥进行加密计算得到的结果。   * USIM卡中烧制了OPC时配置，烧制了OP时无需配置。 * 配置的OPC值与USIM卡中烧制的OPC值一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFSNO:
          name: 'AMF序列号'
          type: string
          required: false
          description: '用于标识AMF序列号。已在鉴权管理域配置中通过**ADD AMF**命令配置，可以使用**LST AMF**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_sub_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '已在UDM本局数据配置中通过**ADD HLRSN**命令配置，可以使用**LST HLRSN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用户的MSISDN号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用户卡类型为USIM卡。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NAM:
          name: '网络接入模式'
          type: string
          required: false
          description: '根据运营商现网的实际业务要求统一规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '提供EPS业务。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DEFAULTCALL:
          name: '缺省呼叫类型'
          type: string
          required: false
          description: '对没有携带呼叫类型参数的入呼设定缺省的呼叫类型。缺省值为TS11。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: string
          required: false
          description: 'UE最大的上传速率。  单位：bit/s'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: string
          required: false
          description: 'UE最大的下载速率。  单位：bit/s'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_amdata_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供AM签约数据'
          type: string
          required: false
          description: '提供或修改用户的AMF签约数据。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'UE级别上行速率'
          type: string
          required: false
          description: 'UE级别上行速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'UE级别上行速率单位'
          type: string
          required: false
          description: '设置“UE级别上行速率”后该参数必须设置，用于标识UE级别上行速率单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'UE级别下行速率'
          type: string
          required: false
          description: 'UE级别下行速率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'UE级别下行速率单位'
          type: string
          required: false
          description: '设置“UE级别下行速率”后该参数必须设置，用于标识UE级别下行速率单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: '用户的鉴权方式为EAP-AKA''鉴权。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sucikey_list:
      type: items
      properties:
        KEYNAME:
          name: 'Key名称'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: 'SUCI私钥的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEYTYPE:
          name: 'SUCI 密钥类型'
          type: string
          enum:
          - PROFILEA
          - PROFILEB
          required: true
          description: 'SUCI私钥的加密方式类型，目前针对SUCI的加密算法有两种，一种是PROFILEA类型，一种是PROFILEB类型。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        KEYID:
          name: 'SUCI 密钥ID'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: 'SUCI私钥的ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SAVEMODE:
          name: '保存方式'
          type: string
          enum:
          - LOCAL
          - HSM
          required: true
          description: 'SUCI私钥的保存方式。'
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
        KEYVALUE:
          name: 'SUCI密钥值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: 'SUCI私钥的取值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_amf_list:
    - HLRSN: '1'
      AMFSNO: '1'
      AMFVALUE: '1111'
    add_k4_list:
    - HLRSN: '1'
      K4SNO: '1'
      KEYTYPE: ClearKey
      ALGTYPE: AES256
      K4VALUE: '*****'
    add_ki_list:
    - HLRSN: '1'
      IMSI: '460011365811110'
      KIVALUE: '*****'
      K4SNO: '1'
      CARDTYPE: USIM
      ALG: MILENAGE
      OPCVALUE: '*****'
      AMFSNO: '1'
    add_sub_list:
    - HLRSN: '1'
      IMSI: '460011365811110'
      ISDN: '8611365801020'
      CARDTYPE: USIM
      NAM: BOTH
      EPS: TRUE
      DEFAULTCALL: TS11
      AMBRMAXUL: '50000000'
      AMBRMAXDL: '50000000'
    mod_amdata_list:
    - IMSI: '460011365811110'
      PROV: TRUE
      AMBRUP: '50000000'
      UPUNIT: bps
      AMBRDW: '50000000'
      DWUNIT: bps
      AUTHTYPE: EAP-AKA'
    add_sucikey_list:
    - KEYNAME: 'key1'
      KEYTYPE: PROFILEA
      KEYID: 1
      SAVEMODE: LOCAL
      KEYVALUE: '*****'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 执行**ADD AMF**配置鉴权管理域。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amf_list的变量区（command: ADD AMF） -#}
<!-- MISSING_MACRO: command=ADD AMF list_name=add_amf_list step_id=2 -->
```

### 3 执行**ADD K4**设置KI的传输密钥K4。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_k4_list的变量区（command: ADD K4） -#}
<!-- MISSING_MACRO: command=ADD K4 list_name=add_k4_list step_id=3 -->
```

### 4 执行**ADD KI**配置用户鉴权密钥，为用户加载KI。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ki_list的变量区（command: ADD KI） -#}
<!-- MISSING_MACRO: command=ADD KI list_name=add_ki_list step_id=4 -->
```

### 5 执行**ADD SUB**为用户开户。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_sub_list的变量区（command: ADD SUB） -#}
<!-- MISSING_MACRO: command=ADD SUB list_name=add_sub_list step_id=5 -->
```

### 6 执行**MOD AMDATA**为用户签约5G数据，配置用户的鉴权策略为5G的EAP-AKA'鉴权。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_amdata_list的变量区（command: MOD AMDATA） -#}
<!-- MISSING_MACRO: command=MOD AMDATA list_name=mod_amdata_list step_id=6 -->
```

### 7 （可选）执行**ADD SUCIKEY**增加SUCI私钥。

```jinja2
{%- if is_optional_add_sucikey -%}
    {%- for item in add_sucikey_list -%}
        ADD SUCIKEY:
        {#- --- 必选参数 --- -#}
        KEYNAME="{{item.KEYNAME}}",
        KEYTYPE={{item.KEYTYPE}},
        KEYID={{item.KEYID}},
        SAVEMODE={{item.SAVEMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SAVEMODE=LOCAL 时必选 --- -#}
        {%- if item.SAVEMODE == 'LOCAL' -%}
            KEYVALUE="{{item.KEYVALUE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 若AUSF/UDM接收到的消息中，用户标识为SUCI，并且加密类型是PROFILEA或PROFILEB时，执行本命令增加SUCI私钥。

