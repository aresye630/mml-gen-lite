---
id: ''
name: 配置MME基础数据
ne_type: UNC
type: feature
description: 执行该任务的场景如下：  * 开局 * 扩容
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置MME基础数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
执行该任务的场景如下：* 开局* 扩容

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sys_list:
      type: items
      properties:
        DESC:
          name: '系统描述'
          type: string
          maxLength: 64
          required: false
          description: '配置系统基本信息。'
          data_source: '整网规划'
          pattern: ''
          default: ''
        ID:
          name: '系统标识'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NM:
          name: '系统名称'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRV:
          name: '服务描述'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROVER:
          name: '协议版本'
          type: string
          enum:
          - R4
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNID:
          name: '核心网标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置PLMN。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置互联PLMN，用于支持不同PLMN之间的用户漫游。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MATCHIMSI:
          name: '匹配IMSI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        EXCLUSIVEPLMN:
          name: '专属互连PLMN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        SMSCT:
          name: '纠正后的短消息中心'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmeid_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置MMEID。'
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码（起始值）'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_sys_list:
    - DESC: 'HCGPBER1'
      ID: 0
      NM: 'HCGPBER1'
      SRV: 'prsBER1'
      MNC: '00'
      MCC: '123'
      PROVER: R4
      CNID: 0
    add_hplmn_list:
    - MCC: '123'
      MNC: '00'
      CC: '86'
      SM: YES
      MAXSMNUM: 7
      SMS: NO
      S5S8TYPE: GTP
      PLMNN: 'noname_1'
      SMSCR: NO
    add_connectplmn_list:
    - MCC: '123'
      MNC: '00'
      MATCHIMSI: '1234'
      CC: '860'
      SM: YES
      SMS: YES
      SMSCR: NO
      EXCLUSIVEPLMN: YES
      EMCBS: YES
      MAXSMNUM: 11
      SMSCT: ''
    add_mmeid_list:
    - MCC: '123'
      MNC: '00'
      MMEGI: '8001'
      MMEC: '01'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置系统基本信息。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.ID is not none -%}
        ID={{item.ID}},
    {%- endif -%}
    {%- if item.NM is not none -%}
        NM="{{item.NM}}",
    {%- endif -%}
    {%- if item.SRV is not none -%}
        SRV="{{item.SRV}}",
    {%- endif -%}
    {%- if item.MNC is not none -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {%- if item.MCC is not none -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {%- if item.PROVER is not none -%}
        PROVER={{item.PROVER}},
    {%- endif -%}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Home PLMN。

```jinja2
{%- for item in add_hplmn_list -%}
    ADD HPLMN:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CC is not none -%}
        CC="{{item.CC}}",
    {%- endif -%}
    {%- if item.SM is not none -%}
        SM={{item.SM}},
    {%- endif -%}
    {%- if item.SMS is not none -%}
        SMS={{item.SMS}},
    {%- endif -%}
    {%- if item.S5S8TYPE is not none -%}
        S5S8TYPE={{item.S5S8TYPE}},
    {%- endif -%}
    {%- if item.PLMNN is not none -%}
        PLMNN="{{item.PLMNN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SM=YES 时可选 --- -#}
    {%- if item.SM == 'YES' -%}
        {%- if item.MAXSMNUM is not none -%}
            MAXSMNUM={{item.MAXSMNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMS=YES 时可选 --- -#}
    {%- if item.SMS == 'YES' -%}
        {%- if item.SMSCR is not none -%}
            SMSCR={{item.SMSCR}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **可选：**配置互联PLMN，用于支持不同PLMN之间的用户漫游。

```jinja2
{%- if is_optional_connect_plmn -%}
    {%- for item in add_connectplmn_list -%}
        ADD CONNECTPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MATCHIMSI is not none -%}
            MATCHIMSI="{{item.MATCHIMSI}}",
        {%- endif -%}
        {%- if item.CC is not none -%}
            CC="{{item.CC}}",
        {%- endif -%}
        {%- if item.SM is not none -%}
            SM={{item.SM}},
        {%- endif -%}
        {%- if item.SMS is not none -%}
            SMS={{item.SMS}},
        {%- endif -%}
        {%- if item.EXCLUSIVEPLMN is not none -%}
            EXCLUSIVEPLMN={{item.EXCLUSIVEPLMN}},
        {%- endif -%}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SMSCR=YES 时必选 --- -#}
        {%- if item.SMSCR == 'YES' -%}
            SMSCT="{{item.SMSCT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SMS=YES 时可选 --- -#}
        {%- if item.SMS == 'YES' -%}
            {%- if item.SMSCR is not none -%}
                SMSCR={{item.SMSCR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SM=YES 时可选 --- -#}
        {%- if item.SM == 'YES' -%}
            {%- if item.MAXSMNUM is not none -%}
                MAXSMNUM={{item.MAXSMNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置MMEID。

```jinja2
{%- for item in add_mmeid_list -%}
    ADD MMEID:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    MMEC="{{item.MMEC}}",
    ;
{%- endfor -%}
```

