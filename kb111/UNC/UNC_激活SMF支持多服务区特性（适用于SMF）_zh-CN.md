---
id: ''
name: 激活SMF支持多服务区特性（适用于SMF）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活SMF支持多服务区特性过程。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网关选择功能","WSFD-205015 SMF支持多服务区","激活SMF支持多服务区特性（适用于SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活SMF支持多服务区特性过程。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-205015 SMF支持多服务区特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_nfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '可使用“LST NFPROFILE”命令查看目前SMF实例的优先级，通过“MOD NFPROFILE”确保服务注册消息中smfInfo的priority值小于smfInfoList中smfInfo的priority值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
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
    add_smfinfo_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置SMF实例信息，如SMF名称、FQDN等信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMFNAME:
          name: 'SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERPLMNFQDN:
          name: 'PLMN间SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACCESSTYPE:
          name: '接入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nftai_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiList信息，添加SMF实例支持的TAI信息。'
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
        TAC:
          name: '跟踪区域码'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tacrange_list:
      type: items
      properties:
        INDEX:
          name: '索引标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置**taiRangeList**对应的TAC range。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tairangelist_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiRangeList信息，添加SMF实例支持的taiRangeList信息。'
          data_source: '全网规划'
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
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
        TACRANGEINDEX:
          name: 'TAC区域标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nftai_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiList信息，添加SMF实例支持的TAI信息。'
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
        TAC:
          name: '跟踪区域码'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tacrange_list_1:
      type: items
      properties:
        INDEX:
          name: '索引标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置**taiRangeList**对应的TAC range。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tairangelist_list_1:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiRangeList信息，添加SMF实例支持的taiRangeList信息。'
          data_source: '全网规划'
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
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
        TACRANGEINDEX:
          name: 'TAC区域标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nftai_list_4:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfoList**中taiList信息。添加SMF实例支持的TAI信息，并关联到**SMFINFOEXT**。'
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
        TAC:
          name: '跟踪区域码'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BINDSMFINFOID:
          name: '绑定的SMFINFO ID'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tacrange_list_2:
      type: items
      properties:
        INDEX:
          name: '索引标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置**taiRangeList**对应的TAC range。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tairangelist_list_2:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiRangeList信息，添加SMF实例支持的taiRangeList信息。'
          data_source: '全网规划'
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
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
        TACRANGEINDEX:
          name: 'TAC区域标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BINDSMFINFOID:
          name: '绑定的SMFINFO ID'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nftai_list_6:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfoList**中taiList信息。添加SMF实例支持的TAI信息，并关联到**SMFINFOEXT**。'
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
        TAC:
          name: '跟踪区域码'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BINDSMFINFOID:
          name: '绑定的SMFINFO ID'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tacrange_list_3:
      type: items
      properties:
        INDEX:
          name: '索引标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置**taiRangeList**对应的TAC range。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: 'TAC区域起点值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: 'TAC区域结束值'
          type: string
          minLength: 4
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tairangelist_list_3:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置**smfInfo**中taiRangeList信息，添加SMF实例支持的taiRangeList信息。'
          data_source: '全网规划'
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
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
        TACRANGEINDEX:
          name: 'TAC区域标识'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BINDSMFINFOID:
          name: '绑定的SMFINFO ID'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smfinfoext_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '增加**smfInfo扩展**的信息。一条**smfInfo扩展**对应SMF实例中一个smfInfo，如果smfInfoList中包含多个smfInfo，则需要配置多条**smfInfo扩展**信息。命令中的priority，代表smfInfoList中该smfInfo的priority信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ID:
          name: 'SMFINFOID'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65536
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 65536
    set_mulsmfpdureepol_list:
      type: items
      properties:
        MULSMFPDUREESUP:
          name: '是否支持多SMFInfo下会话重建'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '多smfInfo场景下的PDU会话重建策略  注意：  如果要使用会话重建功能，必须增加**smfInfo扩展**的信息时配置有效**优先级**。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    mod_nfprofile_list:
    - NFINSTANCENAME: 'smf1'
      PRIORITY: 1
    add_smfinfo_list:
    - SMFINSTANCENAME: 'smf1'
      SMFNAME: 'smf1.cluster1.net1.smf.5gc'
      INTERPLMNFQDN: 'smf1.cluster1.net1.smf.5gc.mnc012.mcc345.3gppnetwork.org'
      ACCESSTYPE: AccessType3GPP_ACCESS
    add_nftai_list:
    - NFINSTANCENAME: 'smf1'
      MCC: '345'
      MNC: '012'
      TAC: '000001'
    add_tacrange_list:
    - INDEX: 11
      RANGESTART: '000011'
      RANGEEND: '000019'
    add_tairangelist_list:
    - NFINSTANCENAME: 'smf1'
      NFTYPE: NfSMF
      MCC: '460'
      MNC: '01'
      TACRANGEINDEX: 11
    add_nftai_list_2:
    - NFINSTANCENAME: 'smf2'
      MCC: '345'
      MNC: '012'
      TAC: '000002'
    add_tacrange_list_1:
    - INDEX: 21
      RANGESTART: '000021'
      RANGEEND: '000029'
    add_tairangelist_list_1:
    - NFINSTANCENAME: 'smf2'
      NFTYPE: NfSMF
      MCC: '460'
      MNC: '01'
      TACRANGEINDEX: 21
    add_nftai_list_4:
    - NFINSTANCENAME: 'smf1'
      MCC: '345'
      MNC: '012'
      TAC: '000002'
      BINDSMFINFOID: 'Area2'
    add_tacrange_list_2:
    - INDEX: 21
      RANGESTART: '000021'
      RANGEEND: '000029'
    add_tairangelist_list_2:
    - NFINSTANCENAME: 'smf1'
      NFTYPE: NfSMF
      MCC: '460'
      MNC: '01'
      TACRANGEINDEX: 21，BINDSMFINFOID="Area2"
      BINDSMFINFOID: 'Area2'
    add_nftai_list_6:
    - NFINSTANCENAME: 'smf2'
      MCC: '345'
      MNC: '012'
      TAC: '000001'
      BINDSMFINFOID: 'Area1'
    add_tacrange_list_3:
    - INDEX: 11
      RANGESTART: '000011'
      RANGEEND: '000019'
    add_tairangelist_list_3:
    - NFINSTANCENAME: 'smf2'
      NFTYPE: NfSMF
      MCC: '460'
      MNC: '01'
      TACRANGEINDEX: 11
      BINDSMFINFOID: 'Area1'
    add_smfinfoext_list:
    - SMFINSTANCENAME: 'smf1'
      ID: 'Area2'
      PRIORITY: 10
    set_mulsmfpdureepol_list:
    - MULSMFPDUREESUP: Support
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在涉及的各SMF上都执行步骤2~8的操作。

### 2 进入“MML命令行-UNC”窗口。

### 3 修改SMF实例概述信息。

```jinja2
{%- for item in mod_nfprofile_list -%}
    MOD NFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置SMF实例信息。

```jinja2
{%- for item in add_smfinfo_list -%}
    ADD SMFINFO:
    {#- --- 必选参数 --- -#}
    SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SMFNAME is not none -%}
        SMFNAME="{{item.SMFNAME}}",
    {%- endif -%}
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.ACCESSTYPE is not none -%}
        ACCESSTYPE={{item.ACCESSTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 添加SMF实例支持的TAI信息。如果相同优先级的TAC区域为连续区域，使用**“ADD TAIRANGELIST”**命令（需先配置“**ADD TACRANGE**”），否则使用**“ADD NFTAI”**命令。

```jinja2
{%- if is_scenario_non_contiguous_tac -%}
    {%- for item in add_nftai_list -%}
        ADD NFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TAC="{{item.TAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tacrange_list -%}
        ADD TACRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        RANGESTART="{{item.RANGESTART}}",
        RANGEEND="{{item.RANGEEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tairangelist_list -%}
        ADD TAIRANGELIST:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TACRANGEINDEX={{item.TACRANGEINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_contiguous_tac -%}
    {%- for item in add_nftai_list_2 -%}
        ADD NFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TAC="{{item.TAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tacrange_list_1 -%}
        ADD TACRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        RANGESTART="{{item.RANGESTART}}",
        RANGEEND="{{item.RANGEEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tairangelist_list_1 -%}
        ADD TAIRANGELIST:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TACRANGEINDEX={{item.TACRANGEINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 添加SMF实例支持的TAI信息，并关联到**SMFINFOEXT（smfInfo扩展）**。如果相同优先级的TAC区域为连续区域，使用**“ADD TAIRANGELIST”**命令（需先配置“**ADD TACRANGE**”），否则使用**“ADD NFTAI”**命令。

```jinja2
{%- if is_scenario_non_contiguous_tac -%}
    {%- for item in add_nftai_list_4 -%}
        ADD NFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TAC="{{item.TAC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.BINDSMFINFOID is not none -%}
            BINDSMFINFOID="{{item.BINDSMFINFOID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tacrange_list_2 -%}
        ADD TACRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        RANGESTART="{{item.RANGESTART}}",
        RANGEEND="{{item.RANGEEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tairangelist_list_2 -%}
        ADD TAIRANGELIST:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TACRANGEINDEX={{item.TACRANGEINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.BINDSMFINFOID is not none -%}
            BINDSMFINFOID="{{item.BINDSMFINFOID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_contiguous_tac -%}
    {%- for item in add_nftai_list_6 -%}
        ADD NFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TAC="{{item.TAC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.BINDSMFINFOID is not none -%}
            BINDSMFINFOID="{{item.BINDSMFINFOID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tacrange_list_3 -%}
        ADD TACRANGE:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        RANGESTART="{{item.RANGESTART}}",
        RANGEEND="{{item.RANGEEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_contiguous_tac -%}
    {%- for item in add_tairangelist_list_3 -%}
        ADD TAIRANGELIST:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        TACRANGEINDEX={{item.TACRANGEINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.BINDSMFINFOID is not none -%}
            BINDSMFINFOID="{{item.BINDSMFINFOID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 增加**smfInfo扩展**的信息。一条**smfInfo扩展**对应SMF实例中一个smfInfo，如果smfInfoList中包含多个smfInfo，则需要配置多条smfInfo扩展信息。

```jinja2
{%- for item in add_smfinfoext_list -%}
    ADD SMFINFOEXT:
    {#- --- 必选参数 --- -#}
    SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
    ID="{{item.ID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置多smfInfo场景下的PDU会话重建策略。

```jinja2
{%- for item in set_mulsmfpdureepol_list -%}
    SET MULSMFPDUREEPOL:
    {#- --- 可选参数 --- -#}
    {%- if item.MULSMFPDUREESUP is not none -%}
        MULSMFPDUREESUP={{item.MULSMFPDUREESUP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

