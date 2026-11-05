---
id: ''
name: 激活支持不同PLMN切片能力差异化
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活支持不同PLMN下网络切片能力差异化功能的操作过程。运营商需根据实际情况来确定及规划多PLMN下的网络切片配置。  AMF、SMF支持多个PLMN，不同PLMN下的网络切片支持的能力可能不同，在业务识别时需要对不同PLMN下的网络切片进行区分，以满足运营商支持不同PLMN下网络切片能力差异化的需求。  适用于AMF、SMF、NRF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网络切片功能","WSFD-110009 支持不同PLMN切片能力差异化","激活支持不同PLMN切片能力差异化"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活支持不同PLMN下网络切片能力差异化功能的操作过程。运营商需根据实际情况来确定及规划多PLMN下的网络切片配置。AMF、SMF支持多个PLMN，不同PLMN下的网络切片支持的能力可能不同，在业务识别时需要对不同PLMN下的网络切片进行区分，以满足运营商支持不同PLMN下网络切片能力差异化的需求。适用于AMF、SMF、NRF。

## 必备事项
前提条件

请仔细阅读WSFD-110009 支持不同PLMN切片能力差异化特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nfnrfmgmtpara_list:
      type: items
      properties:
        REGPERPLMNNSSW:
          name: '注册携带PerPlmnSnssaiList开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置本端网元向NRF注册及更新时携带perPlmnSnssaiList信元。  说明：  需整网同时打开。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_nfdiscplcy_list:
      type: items
      properties:
        PERPLMNSELSW:
          name: 'NF缓存服务发现是否支持perPlmnSnssaiList开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置本端网元缓存服务发现时支持根据perPlmnSnssaiList匹配发现参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置运营商的Home PLMN1信息。 说明：  运营商需根据实际情况来配置Home PLMN信息。若运营商已配置了Home PLMN1，只需要增加Home PLMN2的配置即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngsrvplmn_list:
      type: items
      properties:
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '配置运营商的Serving PLMN1信息。  说明：  运营商需根据实际情况来配置Serving PLMN信息。若运营商已配置了Serving PLMN1，只需要增加Serving PLMN2的配置即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
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
          data_source: ''
          pattern: ''
          default: ''
    add_h2srvplmn_list:
      type: items
      properties:
        HMCC:
          name: 'Home PLMN移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '配置运营商Home PLMN1到Serving PLMN1的对应关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HMNC:
          name: 'Home PLMN移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVPLMNIDX:
          name: 'Serving PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '为Serving PLMN1配置网络切片1。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSSCOPE:
          name: '网络切片生效范围'
          type: string
          enum:
          - GLOBALNW
          - CAMPUSNW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GLOBALNW
    add_nghplmn_list_1:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置运营商的Home PLMN2信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngsrvplmn_list_1:
      type: items
      properties:
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '配置运营商的Serving PLMN2信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
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
          data_source: ''
          pattern: ''
          default: ''
    add_h2srvplmn_list_1:
      type: items
      properties:
        HMCC:
          name: 'Home PLMN移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: '配置运营商Home PLMN2到Serving PLMN2的对应关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HMNC:
          name: 'Home PLMN移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVPLMNIDX:
          name: 'Serving PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list_1:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '为Serving PLMN2配置网络切片2。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSSCOPE:
          name: '网络切片生效范围'
          type: string
          enum:
          - GLOBALNW
          - CAMPUSNW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GLOBALNW
    add_nfns_list:
      type: items
      properties:
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
          description: '为SMF配置其支持的网络切片1。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_nfnrfmgmtpara_list:
    - REGPERPLMNNSSW: ON
    set_nfdiscplcy_list:
    - PERPLMNSELSW: ON
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '68'
    add_ngsrvplmn_list:
    - PLMNIDX: 1
      NOID: 0
      MCC: '123'
      MNC: '68'
    add_h2srvplmn_list:
    - HMCC: '123'
      HMNC: '68'
      SRVPLMNIDX: 1
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 1
      SST: 1
      SD: '010101'
      STATE: ACTIVE
      NSSCOPE: GLOBALNW
    add_nghplmn_list_1:
    - NOID: 0
      MCC: '123'
      MNC: '69'
    add_ngsrvplmn_list_1:
    - PLMNIDX: 1
      NOID: 0
      MCC: '123'
      MNC: '69'
    add_h2srvplmn_list_1:
    - HMCC: '123'
      HMNC: '69'
      SRVPLMNIDX: 2
    add_plmnns_list_1:
    - NSIDX: 2
      PLMNIDX: 2
      SST: 1
      SD: '010111'
      STATE: ACTIVE
      NSSCOPE: GLOBALNW
    add_nfns_list:
    - NFTYPE: NfSMF
      NSIDX: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 开启本端网元向NRF注册及更新时携带perPlmnSnssaiList信元的功能。

```jinja2
{%- for item in set_nfnrfmgmtpara_list -%}
    SET NFNRFMGMTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.REGPERPLMNNSSW is not none -%}
        REGPERPLMNNSSW={{item.REGPERPLMNNSSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置控制本端网元缓存服务发现时支持根据perPlmnSnssaiList匹配发现参数。

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.PERPLMNSELSW is not none -%}
        PERPLMNSELSW={{item.PERPLMNSELSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加运营商的PLMN支持的网络切片（例如，运营商有PLMN1和PLMN2，PLMN1支持切片1，PLMN2支持切片2和3）。

#### 4.1 **增加运营商的PLMN1支持的网络切片1。**

##### 4.1.1 增加运营商的Home PLMN的信息。

```jinja2
{%- if is_scenario_plmn1 -%}
    {%- for item in add_nghplmn_list -%}
        ADD NGHPLMN:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.2 增加运营商Serving PLMN的信息。

```jinja2
{%- if is_scenario_plmn1 -%}
    {%- for item in add_ngsrvplmn_list -%}
        ADD NGSRVPLMN:
        {#- --- 必选参数 --- -#}
        PLMNIDX={{item.PLMNIDX}},
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.3 配置关联Serving PLMN与Home PLMN的对应关系。

```jinja2
{%- if is_scenario_plmn1 -%}
    {%- for item in add_h2srvplmn_list -%}
        ADD H2SRVPLMN:
        {#- --- 必选参数 --- -#}
        HMCC="{{item.HMCC}}",
        HMNC="{{item.HMNC}}",
        SRVPLMNIDX={{item.SRVPLMNIDX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.4 配置PLMN1支持的网络切片1。

```jinja2
{%- if is_scenario_plmn1 -%}
    {%- for item in add_plmnns_list -%}
        ADD PLMNNS:
        {#- --- 必选参数 --- -#}
        NSIDX={{item.NSIDX}},
        PLMNIDX={{item.PLMNIDX}},
        SST={{item.SST}},
        {#- --- 可选参数 --- -#}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
        {%- if item.STATE is not none -%}
            STATE={{item.STATE}},
        {%- endif -%}
        {%- if item.NSSCOPE is not none -%}
            NSSCOPE={{item.NSSCOPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 **增加运营商的PLMN2支持的网络切片2、3。**

##### 4.2.1 增加运营商的Home PLMN的信息。

```jinja2
{%- if is_scenario_plmn2 -%}
    {%- for item in add_nghplmn_list_1 -%}
        ADD NGHPLMN:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 增加运营商Serving PLMN的信息。

```jinja2
{%- if is_scenario_plmn2 -%}
    {%- for item in add_ngsrvplmn_list_1 -%}
        ADD NGSRVPLMN:
        {#- --- 必选参数 --- -#}
        PLMNIDX={{item.PLMNIDX}},
        NOID={{item.NOID}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.3 配置关联Serving PLMN与Home PLMN的对应关系。

```jinja2
{%- if is_scenario_plmn2 -%}
    {%- for item in add_h2srvplmn_list_1 -%}
        ADD H2SRVPLMN:
        {#- --- 必选参数 --- -#}
        HMCC="{{item.HMCC}}",
        HMNC="{{item.HMNC}}",
        SRVPLMNIDX={{item.SRVPLMNIDX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.4 配置PLMN2支持的网络切片2，3。

```jinja2
{%- if is_scenario_plmn2 -%}
    {%- for item in add_plmnns_list_1 -%}
        ADD PLMNNS:
        {#- --- 必选参数 --- -#}
        NSIDX={{item.NSIDX}},
        PLMNIDX={{item.PLMNIDX}},
        SST={{item.SST}},
        {#- --- 可选参数 --- -#}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
        {%- if item.STATE is not none -%}
            STATE={{item.STATE}},
        {%- endif -%}
        {%- if item.NSSCOPE is not none -%}
            NSSCOPE={{item.NSSCOPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置SMF支持的网络切片。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

