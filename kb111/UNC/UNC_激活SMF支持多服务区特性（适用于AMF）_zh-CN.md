---
id: ''
name: 激活SMF支持多服务区特性（适用于AMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活SMF支持多服务区操作过程。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网关选择功能","WSFD-205015 SMF支持多服务区","激活SMF支持多服务区特性（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活SMF支持多服务区操作过程。适用于AMF。

## 必备事项
前提条件

请仔细阅读WSFD-205015 SMF支持多服务区特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nfdiscplcy_list:
      type: items
      properties:
        SMFINFOLISTPLCY:
          name: 'SmfInfoList匹配策略'
          type: string
          enum:
          - FORBIDDEN
          - RESTRICTED
          - UNRESTRICTED
          required: false
          description: '发现SMF时，支持使用的smfInfoList信元匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nfdiscplcy_list_1:
      type: items
      properties:
        CFGTAIPRISW:
          name: '本地发现TAI优先级优选开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '根据TAI从本地服务发现时，开启根据TAI优先级优选功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置对端SMF实例概述信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HTTPS
    add_pnftai_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '本地配置用户接入位置TAC为000001时，smf1的优先级。  说明：  + 网络中没有部署NRF，或对端SMF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置对端SMF的场景下，配置对端SMF实例相关的信息。 + AMF在为用户匹配使用的SMF时，SMF范围既包括smfInfo，也包括smfInfoList。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAI:
          name: '跟踪区标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnftairange_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '本地配置用户接入位置TAC为000011~000019时，smf1的优先级。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家代码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list_1:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置对端SMF实例概述信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: Registered
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HTTPS
    add_pnftai_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '本地配置用户接入位置TAC为000002时，smf2的优先级。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAI:
          name: '跟踪区标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnftairange_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '本地配置用户接入位置TAC为000021~000029时，smf2的优先级。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家代码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_nfdiscplcy_list:
    - SMFINFOLISTPLCY: RESTRICTED
    set_nfdiscplcy_list_1:
    - CFGTAIPRISW: ON
    add_pnfprofile_list:
    - NFINSTANCEID: 'smf1'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      PRIORITY: 1
      FQDN: ''
      SCHEME: HTTPS
    add_pnftai_list:
    - NFINSTANCEID: 'smf1'
      TAI: '345012000001'
      PRISWITCH: INHERIT
      CAPSWITCH: INHERIT
      PRIORITY: 10
      CAPACITY: ''
    add_pnftairange_list:
    - INDEX: 11
      NFINSTANCEID: 'smf1'
      MCC: '345'
      MNC: '012'
      QUERYTYPE: START_END
      RANGESTART: '000011'
      RANGEEND: '000019'
      PRISWITCH: INHERIT
      CAPSWITCH: INHERIT
      PRIORITY: 10
      CAPACITY: ''
      PATTERN: ''
    add_pnfprofile_list_1:
    - NFINSTANCEID: 'smf2'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      PRIORITY: 1
      FQDN: ''
      SCHEME: HTTPS
    add_pnftai_list_4:
    - NFINSTANCEID: 'smf2'
      TAI: '345012000002'
      PRISWITCH: INHERIT
      CAPSWITCH: INHERIT
      PRIORITY: 10
      CAPACITY: ''
    add_pnftairange_list_2:
    - INDEX: 21
      NFINSTANCEID: 'smf2'
      MCC: '345'
      MNC: '012'
      QUERYTYPE: START_END
      RANGESTART: '000021'
      RANGEEND: '000029'
      PRISWITCH: INHERIT
      CAPSWITCH: INHERIT
      PRIORITY: 10
      CAPACITY: ''
      PATTERN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开开关，AMF发现SMF时，支持使用的smfInfoList信元匹配。

```jinja2
{%- if is_scenario_discover_smf_via_nrf -%}
    {%- for item in set_nfdiscplcy_list -%}
        SET NFDISCPLCY:
        {#- --- 可选参数 --- -#}
        {%- if item.SMFINFOLISTPLCY is not none -%}
            SMFINFOLISTPLCY={{item.SMFINFOLISTPLCY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in set_nfdiscplcy_list_1 -%}
        SET NFDISCPLCY:
        {#- --- 可选参数 --- -#}
        {%- if item.CFGTAIPRISW is not none -%}
            CFGTAIPRISW={{item.CFGTAIPRISW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 如果本地配置目标SMF，则执行此步骤。

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnfprofile_list -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
        {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
            {%- if item.SCHEME is not none -%}
                SCHEME={{item.SCHEME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
        {%- if (item.NFTYPE == 'NfUPF') -%}
            FQDN="{{item.FQDN}}",
        {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
            {%- if item.FQDN is not none -%}
                FQDN="{{item.FQDN}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnftai_list -%}
        ADD PNFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        TAI="{{item.TAI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRISWITCH is not none -%}
            PRISWITCH={{item.PRISWITCH}},
        {%- endif -%}
        {%- if item.CAPSWITCH is not none -%}
            CAPSWITCH={{item.CAPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.PRISWITCH == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：CAPSWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.CAPSWITCH == 'SPECIFIC' -%}
            CAPACITY={{item.CAPACITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnftairange_list -%}
        ADD PNFTAIRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRISWITCH is not none -%}
            PRISWITCH={{item.PRISWITCH}},
        {%- endif -%}
        {%- if item.CAPSWITCH is not none -%}
            CAPSWITCH={{item.CAPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.PRISWITCH == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：CAPSWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.CAPSWITCH == 'SPECIFIC' -%}
            CAPACITY={{item.CAPACITY}},
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnfprofile_list_1 -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
        {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
            {%- if item.SCHEME is not none -%}
                SCHEME={{item.SCHEME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
        {%- if (item.NFTYPE == 'NfUPF') -%}
            FQDN="{{item.FQDN}}",
        {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
            {%- if item.FQDN is not none -%}
                FQDN="{{item.FQDN}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnftai_list_4 -%}
        ADD PNFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        TAI="{{item.TAI}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRISWITCH is not none -%}
            PRISWITCH={{item.PRISWITCH}},
        {%- endif -%}
        {%- if item.CAPSWITCH is not none -%}
            CAPSWITCH={{item.CAPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.PRISWITCH == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：CAPSWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.CAPSWITCH == 'SPECIFIC' -%}
            CAPACITY={{item.CAPACITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_local_config_target_smf -%}
    {%- for item in add_pnftairange_list_2 -%}
        ADD PNFTAIRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRISWITCH is not none -%}
            PRISWITCH={{item.PRISWITCH}},
        {%- endif -%}
        {%- if item.CAPSWITCH is not none -%}
            CAPSWITCH={{item.CAPSWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.PRISWITCH == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选：CAPSWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.CAPSWITCH == 'SPECIFIC' -%}
            CAPACITY={{item.CAPACITY}},
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

