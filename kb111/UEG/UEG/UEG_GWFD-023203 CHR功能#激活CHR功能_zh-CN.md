---
id: GWFD-023203
name: 激活CHR功能
ne_type: UEG
type: feature
description: 本操作指导介绍配置UEG和CHR服务器的对接，以及激活CHR功能的操作过程。  * 完成UEG上IP路由数据的配置，具体流程参见《UEG初始配置与调测》手册>配置VNF侧IP路由数据。 * (可选)安装部署IPsec，建议部署IPSec保证传输通道安全、数据安全。 * 配置UCF与CHR服务器对接数据。 * 开启CHR功能，配置CHR服务器类型以及发送策略。操作过程  **图1** 操作过程
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-023200 超高带宽业务质量保障","GWFD-023203 CHR功能","激活CHR功能"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-023200 超高带宽业务质量保障","GWFD-023203 CHR功能","激活CHR功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍配置UEG和CHR服务器的对接，以及激活CHR功能的操作过程。* 完成UEG上IP路由数据的配置，具体流程参见《UEG初始配置与调测》手册>配置VNF侧IP路由数据。* (可选)安装部署IPsec，建议部署IPSec保证传输通道安全、数据安全。* 配置UCF与CHR服务器对接数据。* 开启CHR功能，配置CHR服务器类型以及发送策略。操作过程**图1** 操作过程

## 必备事项
前提条件

* 请仔细阅读GWFD-023203 CHR功能特性概述（适用于SGSN/MME/AMF）。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ucfip_list:
      type: items
      properties:
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - FTP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置UCF报表本地IP资源池、UCF报表使用的协议类型、UCF报表地址的端口号等信息。  说明：  请确保配置ADD UCFIP的IP地址不与LST SERVICEIP和LST SERVICEIPMCR的IP地址重复，否则会导致链路概率性不通。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTSTART:
          name: '起始端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INDEX:
          name: '索引号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
    add_ucfsvrip_list:
      type: items
      properties:
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - FTP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCESSNAME:
          name: '接入点名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '配置报表服务器（CHR服务器）的接入点IP地址、服务器类型、协议类型等信息。 说明：  CHR服务器地址和UCF报表本地IP资源池不能在同一网段。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UCFSVRNAME:
          name: 'UCF服务器名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'UCF服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRPORT:
          name: 'UCF服务器端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chrcfg_list:
      type: items
      properties:
        GERANSUCC:
          name: 'Gb模式流程成功时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GERANFAIL:
          name: 'Gb模式流程失败时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UTRANSUCC:
          name: 'Iu模式流程成功时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UTRANFAIL:
          name: 'Iu模式流程失败时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSSUCC:
          name: 'S1模式流程成功时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSFAIL:
          name: 'S1模式流程失败时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RPTDEVNO:
          name: 'CHR单据设备号填充方式'
          type: string
          enum:
          - MMEID
          - SGSN_NUMBER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chrlowperfsvrsub_list:
      type: items
      properties:
        GERANSUCC:
          name: 'Gb模式流程成功时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GERANFAIL:
          name: 'Gb模式流程失败时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UTRANSUCC:
          name: 'Iu模式流程成功时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSSUCC:
          name: 'S1模式流程成功时上报选项'
          type: string
          required: false
          description: 'SGSN/MME：配置指定流程的单据上报到低性能CHR服务器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPSFAIL:
          name: 'S1模式流程失败时上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chrsndplcycfg_list:
      type: items
      properties:
        CHRSNDPLCYSELECT:
          name: 'CHR传输策略选择'
          type: string
          enum:
          - CUSTOMIZE
          - WHOLESYSTEM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOSUBSWITCH:
          name: '未获取签约数据场景CHR传输开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chrsndplcy_list:
      type: items
      properties:
        TYPE:
          name: 'CHR传输策略类型'
          type: string
          enum:
          - APNNI
          required: true
          description: 'SGSN/MME：增加CHR传输策略，满足CHR传输策略的用户的CHR才会传输给CloudUDN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngaccchrcfg_list:
      type: items
      properties:
        HISRVPRCTMPLIDX:
          name: '高性能服务器上报流程控制模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaccchrprctmpl_list:
      type: items
      properties:
        TMPLIDX:
          name: '流程控制模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPCHRSUCCPRC:
          name: 'NG接入CHR成功流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPCHRFAILPRC:
          name: 'NG接入CHR失败流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1'
        NGAPKEYSUCCSIG:
          name: 'NG接入成功信令事件上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPKEYFAILSIG:
          name: 'NG接入失败信令事件上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngsrchrcfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - SPECIFIC_IMSI
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 11
          maxLength: 15
          required: false
          description: '说明：  21.5.0版本中仅支持基于IMSI匹配来上报小范围CHR功能，TAC，gNodeB，切片+DNN维度放到后续版本规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TMPLIDX:
          name: '流程控制模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngaccchrprctmpl_list_1:
      type: items
      properties:
        TMPLIDX:
          name: '流程控制模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: 'AMF：配置5G接入CHR单据上报的流程。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPCHRSUCCPRC:
          name: 'NG接入CHR成功流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPCHRFAILPRC:
          name: 'NG接入CHR失败流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'OTHER-1&INITREG-1&MOBILREG-1&DEREG-1&SYSCHANGE-1&SRVREQ-1&PAGING-1&ANREL-1&N2HO-1&XNHO-1&PDUSESSNEST-1&PDUSESSNMOD-1&PDUSESSNREL-1&UECONUPD-1&LOCATIONREPORT-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1'
        NGAPKEYSUCCSIG:
          name: 'NG接入成功信令事件上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPKEYFAILSIG:
          name: 'NG接入失败信令事件上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngchrstorcfg_list:
      type: items
      properties:
        CHRSPESUBSAVE:
          name: '小范围CHR使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHRSAVEPATH:
          name: '小范围CHR存储路径'
          type: string
          enum:
          - SAVE_OMU
          - SAVE_UCF
          - SAVE_OMU_AND_UCF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srangechrcfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - E_SPECIAL_APNQCI
          - E_SPECIAL_ENB
          - E_SPECIAL_IMEI
          - E_SPECIAL_IMSI
          - E_SPECIAL_RAI
          - E_SPECIAL_TAI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QCI:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chrstorecfg_list:
      type: items
      properties:
        STOREALLFLAG:
          name: 'CHR存储开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STOREALLTYPE:
          name: '存储类型'
          type: string
          enum:
          - STORE_AND_SEND
          - STORE_ONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ucfip_list:
    - PROTOCOLTYPE: TCP
      IPTYPE: IPv4
      IPV4: '10.181.23.253'
      PORTSTART: 6000
      PORTEND: 6031
      INDEX: 1
      VPNNAME: 'public1'
    add_ucfsvrip_list:
    - PROTOCOLTYPE: TCP
      ACCESSNAME: 'ACCESS1'
      UCFSVRNAME: 'UCFSVR1'
      IPTYPE: IPv4
      IPV4: '10.80.128.1'
      SVRPORT: 10500
    set_licenseswitch_list:
    - LICITEM: 'LKV2CHR03'
      SWITCH: ENABLE
    set_chrcfg_list:
    - GERANSUCC: ATTACH-1
      GERANFAIL: ATTACH-1&RAU-1
      UTRANSUCC: ATTACH-1
      UTRANFAIL: ATTACH-1&RAU-1
      EPSSUCC: ATTACH-1
      EPSFAIL: ATTACH-1&TAU-1
      RPTDEVNO: SGSN_NUMBER
    set_chrlowperfsvrsub_list:
    - GERANSUCC: ATTACH-1
      GERANFAIL: ATTACH-1&RAU-1
      UTRANSUCC: ATTACH-1
      EPSSUCC: ATTACH
      EPSFAIL: ATTACH
    set_chrsndplcycfg_list:
    - CHRSNDPLCYSELECT: CUSTOMIZE
      NOSUBSWITCH: ON
    add_chrsndplcy_list:
    - TYPE: APNNI
      APNNI: 'huawei.com'
    set_ngaccchrcfg_list:
    - HISRVPRCTMPLIDX: 10
    add_ngaccchrprctmpl_list:
    - TMPLIDX: 10
      NGAPCHRSUCCPRC: INITREG-1
      NGAPCHRFAILPRC: INITREG-1
      NGAPKEYSUCCSIG: UPDSMCTX-1
      NGAPKEYFAILSIG: UPDSMCTX-1
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1
      VALUE: VALUE_0
      POSITION: 13
    add_ngsrchrcfg_list:
    - SUBRANGE: SPECIFIC_IMSI
      IMSIPRE: '12303000100'
      TMPLIDX: 0
    add_ngaccchrprctmpl_list_1:
    - TMPLIDX: 1
      NGAPCHRSUCCPRC: INITREG（Initial Registration）
      NGAPCHRFAILPRC: INITREG（Initial Registration）
      NGAPKEYSUCCSIG: UPDSMCTX（Nsmf_PDUSession_UpdateSMContext）
      NGAPKEYFAILSIG: UPDSMCTX（Nsmf_PDUSession_UpdateSMContext）
    set_ngchrstorcfg_list:
    - CHRSPESUBSAVE: ENABLE
      CHRSAVEPATH: SAVE_OMU
    add_srangechrcfg_list:
    - SUBRANGE: E_SPECIAL_APNQCI
      APNNI: 'Huawei.com'
      QCI: 2
    set_chrstorecfg_list:
    - STOREALLFLAG: ON
      STOREALLTYPE: STORE_AND_SEND
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 步骤一：（可选）安装部署IPsec

#### 1.1 安装IPsec服务，具体流程参见《UEG软件安装》手册>安装可选服务>安装IPSec服务。

#### 1.2 配置IPsec，具体参见《UEG安全配置》手册>可选配置>网络安全配置>配置IPsec功能。

### 2 步骤二：配置UCF和CHR服务器对接数据。

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 配置UCF报表本地IP资源池。

```jinja2
{%- for item in add_ucfip_list -%}
    ADD UCFIP:
    {#- --- 必选参数 --- -#}
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    IPTYPE={{item.IPTYPE}},
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTSTART={{item.PORTSTART}},
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTEND={{item.PORTEND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置UCF报表服务器接入点IP地址等信息。

```jinja2
{%- for item in add_ucfsvrip_list -%}
    ADD UCFSVRIP:
    {#- --- 必选参数 --- -#}
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    ACCESSNAME="{{item.ACCESSNAME}}",
    UCFSVRNAME="{{item.UCFSVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    SVRPORT={{item.SVRPORT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 步骤三：配置CHR服务器类型以及发送策略。

#### 3.1 进入“MML命令行-UEG”窗口。

#### 3.2 打开本特性的CHR功能License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### CHR License仅控制整系统的正常流程CHR单据。

#### 3.3 配置CHR服务器类型以及发送策略（适用于SGSN/MME）

##### 3.3.1 配置指定流程的单据上报到CHR服务器。

```jinja2
{%- if is_scenario_sgsn_mme -%}
    {%- for item in set_chrcfg_list -%}
        SET CHRCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.GERANSUCC is not none -%}
            GERANSUCC={{item.GERANSUCC}},
        {%- endif -%}
        {%- if item.GERANFAIL is not none -%}
            GERANFAIL={{item.GERANFAIL}},
        {%- endif -%}
        {%- if item.UTRANSUCC is not none -%}
            UTRANSUCC={{item.UTRANSUCC}},
        {%- endif -%}
        {%- if item.UTRANFAIL is not none -%}
            UTRANFAIL={{item.UTRANFAIL}},
        {%- endif -%}
        {%- if item.EPSSUCC is not none -%}
            EPSSUCC={{item.EPSSUCC}},
        {%- endif -%}
        {%- if item.EPSFAIL is not none -%}
            EPSFAIL={{item.EPSFAIL}},
        {%- endif -%}
        {%- if item.RPTDEVNO is not none -%}
            RPTDEVNO={{item.RPTDEVNO}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.2 配置指定流程的单据上报到低性能CHR服务器。

```jinja2
{%- if is_scenario_sgsn_mme -%}
    {%- for item in set_chrlowperfsvrsub_list -%}
        SET CHRLOWPERFSVRSUB:
        {#- --- 可选参数 --- -#}
        {%- if item.GERANSUCC is not none -%}
            GERANSUCC={{item.GERANSUCC}},
        {%- endif -%}
        {%- if item.GERANFAIL is not none -%}
            GERANFAIL={{item.GERANFAIL}},
        {%- endif -%}
        {%- if item.UTRANSUCC is not none -%}
            UTRANSUCC={{item.UTRANSUCC}},
        {%- endif -%}
        {%- if item.EPSFAIL is not none -%}
            EPSFAIL={{item.EPSFAIL}},
        {%- endif -%}
        {%- if item.EPSSUCC is not none -%}
            EPSSUCC={{item.EPSSUCC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.3 配置CHR传输策略控制参数。

```jinja2
{%- if is_scenario_sgsn_mme -%}
    {%- for item in set_chrsndplcycfg_list -%}
        SET CHRSNDPLCYCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.CHRSNDPLCYSELECT is not none -%}
            CHRSNDPLCYSELECT={{item.CHRSNDPLCYSELECT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CHRSNDPLCYSELECT=CUSTOMIZE 时可选 --- -#}
        {%- if item.CHRSNDPLCYSELECT == 'CUSTOMIZE' -%}
            {%- if item.NOSUBSWITCH is not none -%}
                NOSUBSWITCH={{item.NOSUBSWITCH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.4 增加CHR传输策略。

```jinja2
{%- if is_scenario_sgsn_mme -%}
    {%- for item in add_chrsndplcy_list -%}
        ADD CHRSNDPLCY:
        {#- --- 必选参数 --- -#}
        TYPE={{item.TYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TYPE=APNNI 时必选 --- -#}
        {%- if item.TYPE == 'APNNI' -%}
            APNNI="{{item.APNNI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置CHR服务器类型以及发送策略（适用于AMF）。

##### 3.4.1 配置5G接入CHR单据上报的高性能CHR服务器索引。

```jinja2
{%- if is_scenario_amf -%}
    {%- for item in set_ngaccchrcfg_list -%}
        SET NGACCCHRCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.HISRVPRCTMPLIDX is not none -%}
            HISRVPRCTMPLIDX={{item.HISRVPRCTMPLIDX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.4.2 配置5G接入CHR单据上报的业务流程和信令事件。

```jinja2
{%- if is_scenario_amf -%}
    {%- for item in add_ngaccchrprctmpl_list -%}
        ADD NGACCCHRPRCTMPL:
        {#- --- 必选参数 --- -#}
        TMPLIDX={{item.TMPLIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.NGAPCHRSUCCPRC is not none -%}
            NGAPCHRSUCCPRC={{item.NGAPCHRSUCCPRC}},
        {%- endif -%}
        {%- if item.NGAPCHRFAILPRC is not none -%}
            NGAPCHRFAILPRC={{item.NGAPCHRFAILPRC}},
        {%- endif -%}
        {%- if item.NGAPKEYSUCCSIG is not none -%}
            NGAPKEYSUCCSIG={{item.NGAPKEYSUCCSIG}},
        {%- endif -%}
        {%- if item.NGAPKEYFAILSIG is not none -%}
            NGAPKEYFAILSIG={{item.NGAPKEYFAILSIG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_amf -%}
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

### 4 步骤四：（可选）配置小范围CHR上报策略以及存储策略。

#### 4.1 进入“MML命令行-UEG”窗口。

#### 4.2 配置小范围CHR的过滤条件（适用于AMF）。

```jinja2
{%- if is_optional_small_range_chr_report_storage -%}
    {%- for item in add_ngsrchrcfg_list -%}
        ADD NGSRCHRCFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        TMPLIDX={{item.TMPLIDX}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=SPECIFIC_IMSI 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIFIC_IMSI' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置小范围CHR单据上报的业务流程和信令事件（适用于AMF）。

```jinja2
{%- if is_optional_small_range_chr_report_storage -%}
    {%- for item in add_ngaccchrprctmpl_list_1 -%}
        ADD NGACCCHRPRCTMPL:
        {#- --- 必选参数 --- -#}
        TMPLIDX={{item.TMPLIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.NGAPCHRFAILPRC is not none -%}
            NGAPCHRFAILPRC={{item.NGAPCHRFAILPRC}},
        {%- endif -%}
        {%- if item.NGAPCHRSUCCPRC is not none -%}
            NGAPCHRSUCCPRC={{item.NGAPCHRSUCCPRC}},
        {%- endif -%}
        {%- if item.NGAPKEYFAILSIG is not none -%}
            NGAPKEYFAILSIG={{item.NGAPKEYFAILSIG}},
        {%- endif -%}
        {%- if item.NGAPKEYSUCCSIG is not none -%}
            NGAPKEYSUCCSIG={{item.NGAPKEYSUCCSIG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置小范围CHR单据上报开关，并配置小范围CHR是否保存到OMU和UCF（适用于AMF）。

```jinja2
{%- if is_optional_small_range_chr_report_storage -%}
    {%- for item in set_ngchrstorcfg_list -%}
        SET NGCHRSTORCFG:
        {#- --- 可选参数 --- -#}
        {%- if item.CHRSPESUBSAVE is not none -%}
            CHRSPESUBSAVE={{item.CHRSPESUBSAVE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CHRSPESUBSAVE=ENABLE 时可选 --- -#}
        {%- if item.CHRSPESUBSAVE == 'ENABLE' -%}
            {%- if item.CHRSAVEPATH is not none -%}
                CHRSAVEPATH={{item.CHRSAVEPATH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置小范围CHR生成规则（适用于MME/SGSN）。

```jinja2
{%- if is_optional_small_range_chr_report_storage -%}
    {%- for item in add_srangechrcfg_list -%}
        ADD SRANGECHRCFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=E_SPECIAL_APNQCI 时必选 --- -#}
        {%- if item.SUBRANGE == 'E_SPECIAL_APNQCI' -%}
            APNNI="{{item.APNNI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUBRANGE=E_SPECIAL_APNQCI 时可选 --- -#}
        {%- if item.SUBRANGE == 'E_SPECIAL_APNQCI' -%}
            {%- if item.QCI is not none -%}
                QCI={{item.QCI}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_small_range_chr_report_storage -%}
    {%- for item in set_chrstorecfg_list -%}
        SET CHRSTORECFG:
        {#- --- 可选参数 --- -#}
        {%- if item.STOREALLFLAG is not none -%}
            STOREALLFLAG={{item.STOREALLFLAG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：STOREALLFLAG=ON 时可选 --- -#}
        {%- if item.STOREALLFLAG == 'ON' -%}
            {%- if item.STOREALLTYPE is not none -%}
                STOREALLTYPE={{item.STOREALLTYPE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

