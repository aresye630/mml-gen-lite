---
id: ''
name: 激活网络侧发起的5G位置定位服务
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活网络侧发起的5G位置定位服务特性的操作过程。  网络侧发起的5G位置定位服务是移动通信网络通过无线信号测量来确定UE地理位置信息及其移动速度的技术，本特性中也称为LCS（Location Services）。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","位置业务管理","WSFD-106701 网络侧发起的5G位置定位服务","激活网络侧发起的5G位置定位服务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活网络侧发起的5G位置定位服务特性的操作过程。网络侧发起的5G位置定位服务是移动通信网络通过无线信号测量来确定UE地理位置信息及其移动速度的技术，本特性中也称为LCS（Location Services）。适用于AMF。

## 必备事项
前提条件

请仔细阅读WSFD-106701 网络侧发起的5G位置定位服务特性概述。
已完成AMF初始配置，包括IP路由数据以及AMF基础数据配置参见《UNC初始配置与调测》>组网对接配置。
已完成配置AMF和LMF/GMLC对接。
完成包含此特性的License文件加载。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '当现网在UEG-S上部署LCS功能，且AMF网元版本为20.13.2及以上，UEG-S网元版本低于20.13.2时，AMF必须配置SET AMFSOFTPARAOFBIT命令的各参数按固定取值，用于关闭对ReportingAmount和ReportingInterval信元的校验。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_nglcspara_list:
      type: items
      properties:
        LCSSW:
          name: '定位服务功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置AMF的定位服务功能的相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POSEXPR:
          name: '5G位置信息表老化定时器'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LCSPLCY:
          name: '5G定位服务策略'
          type: string
          enum:
          - PROTOCOL_POSITION
          - NO_LMF_POSITION
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LRC:
          name: '启用连接态LRC流程'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUAMINOTIFY:
          name: '是否携带GUAMI信息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LCSIDCHK:
          name: '是否校验LCS Correlation ID'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LMFRETRY:
          name: '是否重选LMF'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nglcspara_list_1:
      type: items
      properties:
        LCSSW:
          name: '定位服务功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '设置AMF的定位服务功能的相关参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        POSEXPR:
          name: '5G位置信息表老化定时器'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LCSPLCY:
          name: '5G定位服务策略'
          type: string
          enum:
          - PROTOCOL_POSITION
          - NO_LMF_POSITION
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LRC:
          name: '启用连接态LRC流程'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUAMINOTIFY:
          name: '是否携带GUAMI信息'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LCSIDCHK:
          name: '是否校验LCS Correlation ID'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LMFRETRY:
          name: '是否重选LMF'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '当现网在UEG-S上部署LCS功能，且AMF网元版本为20.13.2及以上，UEG-S网元版本低于20.13.2时，AMF必须配置SET AMFSOFTPARAOFBIT命令的各参数按固定取值，用于关闭对ReportingAmount和ReportingInterval信元的校验。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_allowsername_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '只允许指定网元访问AMF的Namf\_Location服务。（本特性以GMLC访问为例）'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 60
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALADDR:
          name: '本端地址'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERADDR:
          name: '对端地址'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '对端GMLC的地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_lcspermitcfg_list:
      type: items
      properties:
        OPTYPE:
          name: '定位服务操作类型'
          type: string
          enum:
          - Namf_Location_ProvidePositioningInfo
          - Namf_Location_ProvideLocationInfo
          - Namf_Location_EventNotify
          required: true
          description: '用于AMF对收到的GMLC的定位请求时检查GMLC的定位请求是否越权，对越权的GMLC，AMF拒绝其定位请求。  “USRGRPID”参数来源于**ADD NGUSRGRP**，并且用户群组成员已通过**ADD NGUSRGRPMEM**完成配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USRGRPID:
          name: '用户群组标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngprdregtimednn_list:
      type: items
      properties:
        DNNNI:
          name: 'DNN网络标识'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该命令用于增加基于DNN配置周期性注册时长。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TIMEPLCY:
          name: '周期性注册时长获取策略'
          type: string
          enum:
          - UDMSUB
          - LOCAL
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        T3512:
          name: 'T3512(min)'
          type: integer
          minimum: 1
          maximum: 780
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器(min)'
          type: integer
          minimum: 2
          maximum: 792
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 68
      VALUE: VALUE_1
      POSITION: 32
    set_nglcspara_list:
    - LCSSW: ON
      POSEXPR: 30
      LCSPLCY: PROTOCOL_POSITION
      LRC: YES
      GUAMINOTIFY: NO
      LCSIDCHK: NO
      LMFRETRY: NO
    set_nglcspara_list_1:
    - LCSSW: ON
      POSEXPR: 30
      LCSPLCY: NO_LMF_POSITION
      LRC: YES
      GUAMINOTIFY: NO
      LCSIDCHK: NO
      LMFRETRY: NO
    set_amfsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: 63
      VALUE: VALUE_1
      POSITION: 1
    add_allowsername_list:
    - INDEX: 0
      NFINSTANCEID: 'AMF_Instance_0'
      SERVICENAME: 'namf-loc'
      LOCALADDR: '10.16.1.5'
      PEERADDR: '10.112.1.5'
    add_lcspermitcfg_list:
    - OPTYPE: Namf_Location_ProvidePositioningInfo
      IPTYPE: IPTypeV4
      IPV4ADDRESS: '10.112.1.5'
      USRGRPID: 20
      IPV6ADDRESS: ''
    add_ngprdregtimednn_list:
    - DNNNI: 'abc'
      TIMEPLCY: LOCAL
      T3512: 780
      RCHTMR: 792
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**当现网在UEG-S上部署LCS功能，且AMF网元版本为20.13.2及以上，UEG-S网元版本低于20.13.2时，需关闭对周期定位的ReportingAmount和ReportingInterval信元的校验。

```jinja2
{%- if is_optional_disable_reporting_validation -%}
    {%- for item in set_amfsoftparaofbit_list -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 在周期性定位或单次定位过程中，若期望AMF向LMF发送Nlmf\_Location\_DetermineLocation Request消息信元填充前不检查信元的有效性，需要将“DWORD68 BIT32”软参设置为“1”。

### 3 设置LCS定位（MT-LR）的参数。

```jinja2
{%- if is_scenario_standard_lcs -%}
    {%- for item in set_nglcspara_list -%}
        SET NGLCSPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.LCSSW is not none -%}
            LCSSW={{item.LCSSW}},
        {%- endif -%}
        {%- if item.POSEXPR is not none -%}
            POSEXPR={{item.POSEXPR}},
        {%- endif -%}
        {%- if item.LCSPLCY is not none -%}
            LCSPLCY={{item.LCSPLCY}},
        {%- endif -%}
        {%- if item.LRC is not none -%}
            LRC={{item.LRC}},
        {%- endif -%}
        {%- if item.GUAMINOTIFY is not none -%}
            GUAMINOTIFY={{item.GUAMINOTIFY}},
        {%- endif -%}
        {%- if item.LCSIDCHK is not none -%}
            LCSIDCHK={{item.LCSIDCHK}},
        {%- endif -%}
        {%- if item.LMFRETRY is not none -%}
            LMFRETRY={{item.LMFRETRY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_no_lmf -%}
    {%- for item in set_nglcspara_list_1 -%}
        SET NGLCSPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.LCSSW is not none -%}
            LCSSW={{item.LCSSW}},
        {%- endif -%}
        {%- if item.POSEXPR is not none -%}
            POSEXPR={{item.POSEXPR}},
        {%- endif -%}
        {%- if item.LCSPLCY is not none -%}
            LCSPLCY={{item.LCSPLCY}},
        {%- endif -%}
        {%- if item.LRC is not none -%}
            LRC={{item.LRC}},
        {%- endif -%}
        {%- if item.GUAMINOTIFY is not none -%}
            GUAMINOTIFY={{item.GUAMINOTIFY}},
        {%- endif -%}
        {%- if item.LCSIDCHK is not none -%}
            LCSIDCHK={{item.LCSIDCHK}},
        {%- endif -%}
        {%- if item.LMFRETRY is not none -%}
            LMFRETRY={{item.LMFRETRY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 如果采用3GPP协议定义的标准LCS组网（部署LMF），进行精准LCS定位，“LCSSW(定位服务功能开关)”为“ON（开启）”，“LCSPLCY(5G定位服务策略)”为“PROTOCOL\_POSITION（协议模式定位）”。

### 如果采用未部署LMF网元的LCS组网，进行较低精度的LCS定位，“LCSSW(定位服务功能开关)”为“ON（开启）”，“LCSPLCY(5G定位服务策略)”为“NO\_LMF\_POSITION（无LMF定位）”。

### 4 **可选：**若LMF不支持显示订阅LPP、NRPPA等类型时，需开启DWORD63 BIT1软参以保证定位流程正常运行。

```jinja2
{%- if is_optional_enable_dword63_bit1_softpara -%}
    {%- for item in set_amfsoftparaofbit_list_1 -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**位置定位安全加固配置。

#### 5.1 建议增加AMF的位置定位服务白名单配置，确保仅限于合法的GMLC访问。

```jinja2
{%- if is_optional_location_security_hardening -%}
    {%- for item in add_allowsername_list -%}
        ADD ALLOWSERNAME:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SERVICENAME="{{item.SERVICENAME}}",
        LOCALADDR="{{item.LOCALADDR}}",
        PEERADDR="{{item.PEERADDR}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 建议AMF和GMLC侧开启SBI接口加密，降低网络安全风险。

#### AMF侧开启SBI接口加密请参考激活SBI接口加密特性(CERT)。

#### GMLC侧开启SBI接口加密请参考对应的产品描述。

#### 5.3 建议增加定位服务权限，用于AMF收到GMLC的定位请求时检查GMLC的定位请求是否越权，对越权的GMLC，AMF拒绝其定位请求。（用于B2B场景）

```jinja2
{%- if is_optional_location_security_hardening -%}
    {%- for item in add_lcspermitcfg_list -%}
        ADD LCSPERMITCFG:
        {#- --- 必选参数 --- -#}
        OPTYPE={{item.OPTYPE}},
        IPTYPE={{item.IPTYPE}},
        USRGRPID={{item.USRGRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 **可选：**针对低功耗终端场景，配置周期性注册更新流程的超长时间间隔。

```jinja2
{%- if is_optional_configure_long_periodic_registration_interval -%}
    {%- for item in add_ngprdregtimednn_list -%}
        ADD NGPRDREGTIMEDNN:
        {#- --- 必选参数 --- -#}
        DNNNI="{{item.DNNNI}}",
        TIMEPLCY={{item.TIMEPLCY}},
        T3512={{item.T3512}},
        RCHTMR={{item.RCHTMR}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 对于低功耗终端，AMF不支持InterAMF切换操作中给基站下发基于DNN配置的T3512。

