---
id: GWFD-023203
name: 激活CHR功能
ne_type: UEG
type: feature
description: 本操作指导介绍配置UEG和CHR服务器的对接，以及激活CHR功能的操作过程。  * 完成UEG上IP路由数据的配置，具体流程参见《UEG初始配置与调测》手册>配置VNF侧IP路由数据。 * (可选)安装部署IPsec，建议部署IPSec保证传输通道安全、数据安全。 * 配置UCF与CHR服务器对接数据。 * 开启CHR功能，配置CHR服务器类型以及发送策略。  **图1** 操作过程
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-023200 超高带宽业务质量保障","GWFD-023203 CHR功能","激活CHR功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍配置UEG和CHR服务器的对接，以及激活CHR功能的操作过程。* 完成UEG上IP路由数据的配置，具体流程参见《UEG初始配置与调测》手册>配置VNF侧IP路由数据。* (可选)安装部署IPsec，建议部署IPSec保证传输通道安全、数据安全。* 配置UCF与CHR服务器对接数据。* 开启CHR功能，配置CHR服务器类型以及发送策略。**图1** 操作过程

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-023203 CHR功能特性概述（适用于GGSN/SGW-C/PGW-C/SMF）。
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
          description: '配置UCF报表本地IP资源池、UCF报表使用的协议类型、UCF报表地址的端口号等信息。'
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
        IPV4:
          name: 'UCF服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
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
    set_glbchrfunc_list:
      type: items
      properties:
        CHRREPORTSW:
          name: 'CHR上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '全局粒度的整系统CHR单据上报开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnchrfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: 'APN粒度的整系统CHR单据上报开关。   * APN使用真实APN，且必须已经通过命令ADD APN配置。 * CHRREPORTSW（CHR上报开关）设置为“INHERIT（继承全局）”时表示使用**SET GLBCHRFUNC**中配置的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHRREPORTSW:
          name: 'CHR上报开关'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_sessnchrprctmpl_list:
      type: items
      properties:
        TMPLIDX:
          name: '流程模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSNCHRFAILPRC:
          name: 'NG会话CHR失败流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'OTHER-1&UEINITCREATESMCTX-1&PDUSESSNMOD-1&PDUSESSNREL-1&ACTUP-1&DEACTUP-1&MOBILREGUPDATE-1&XNHO-1&N2HO-1&SYSCHG-1&N4REPROT-1&AMFEVTRPT-1&RESERVED1-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1'
    set_sessnchrcfg_list:
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
    set_sessnchrstorecfg_list:
      type: items
      properties:
        CHRFAILSAVE:
          name: 'UCF保存异常CHR开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHRALLSAVE:
          name: 'UCF保存整系统CHR开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sessnchrstorecfg_list_1:
      type: items
      properties:
        CHRSPESUBSAVE:
          name: '小范围CHR使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '小范围CHR单据上报开关。'
          data_source: '本端规划'
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
    add_cpchrrptsubid_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 1
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TMPLIDX:
          name: '流程模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chrrptlocinfo_list:
      type: items
      properties:
        LOCTYPE:
          name: '位置类型'
          type: string
          required: false
          description: '配置需要本地存储小范围CHR的用户位置过滤条件，包括N2TAC、S1TAC、LACRAC、eNodeB、gNodeB。  说明：  开启基于位置信息的小范围CHR用户上报时，一定要开启软参流控。软参流控的配置参考如下：   * DWORD1016 BIT24~BIT26 控制是否进行CHR流控及流控的上限，设置值为1(bit26: 0, Bit25: 0, bit24: 1)。 * DWORD509 BIT20~BIT22 控制是否进行Gx接口消息的CHR流控及流控的上限，设置值为1(bit22: 0, Bit21: 0, bit20: 1)。 * DWORD509 BIT23~BIT25 控制是否进行Gy接口消息的CHR流控及流控的上限，设置值为1(bit25: 0, Bit24: 0, bit23: 1)。 * DWORD509 BIT26~BIT28 控制是否进行Gi接口消息的CHR流控及流控的上限，设置值为1(bit28: 0, Bit27: 0, bit26: 1)。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TAC:
          name: 'TAC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2TAC:
          name: 'N2TAC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sessnchrprctmpl_list_1:
      type: items
      properties:
        TMPLIDX:
          name: '流程模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSNCHRFAILPRC:
          name: 'NG会话CHR失败流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'OTHER-1&UEINITCREATESMCTX-1&PDUSESSNMOD-1&PDUSESSNREL-1&ACTUP-1&DEACTUP-1&MOBILREGUPDATE-1&XNHO-1&N2HO-1&SYSCHG-1&N4REPROT-1&AMFEVTRPT-1&RESERVED1-1&RESERVED2-1&RESERVED3-1&RESERVED4-1&RESERVED5-1&RESERVED6-1'
    add_sessnchrprctmpl_list_2:
      type: items
      properties:
        TMPLIDX:
          name: '流程模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSNCHRSUCCPRC:
          name: 'NG会话CHR成功流程上报选项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chrrptsubapn_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该命令仅用于通用DNN的会话创建和会话释放流程开启CHR上报。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TMPLIDX:
          name: '流程模板索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHRFAILSAVE:
          name: '失败流程CHR单据的存储路径'
          type: string
          enum:
          - SAVE_OMU
          - SAVE_UCF
          - SAVE_OMU_AND_UCF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHRALLSAVE:
          name: '成功流程CHR单据的存储路径'
          type: string
          enum:
          - SAVE_OMU
          - SAVE_UCF
          - SAVE_OMU_AND_UCF
          required: true
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
      SVRPORT: 10500
      IPV4: '10.80.128.1'
    set_licenseswitch_list:
    - LICITEM: 'LKV2CHR04'
      SWITCH: ENABLE
    set_glbchrfunc_list:
    - CHRREPORTSW: ENABLE
    add_apnchrfunc_list:
    - APN: 'HUAWEI.COM'
      CHRREPORTSW: ENABLE
    add_sessnchrprctmpl_list:
    - TMPLIDX: 10
      SESSNCHRFAILPRC: PDUSESSNREL-1&MOBILREGUPDATE-1
    set_sessnchrcfg_list:
    - HISRVPRCTMPLIDX: 10
    set_sessnchrstorecfg_list:
    - CHRFAILSAVE: ENABLE
      CHRALLSAVE: DISABLE
    set_sessnchrstorecfg_list_1:
    - CHRSPESUBSAVE: ENABLE
      CHRSAVEPATH: SAVE_OMU
    add_cpchrrptsubid_list:
    - IMSI: '460030123456789'
      TMPLIDX: 11
    add_chrrptlocinfo_list:
    - LOCTYPE: N2TAC
      TAC: '123123'
      N2TAC: N2TAC
    add_sessnchrprctmpl_list_1:
    - TMPLIDX: 11
      SESSNCHRFAILPRC: PDUSESSNREL-1&MOBILREGUPDATE-1
    add_sessnchrprctmpl_list_2:
    - TMPLIDX: 2
      SESSNCHRSUCCPRC: UEINITCREATESMCTX-1&PDUSESSNREL-1
    add_chrrptsubapn_list:
    - APN: 'HUAWEI.COM'
      TMPLIDX: 2
      CHRFAILSAVE: SAVE_OMU
      CHRALLSAVE: SAVE_UCF
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

### 3 步骤三：配置整系统CHR上报策略、存储策略以及CHR服务器类型。

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

#### 3.3 配置全局粒度的整系统CHR上报开关。

```jinja2
{%- for item in set_glbchrfunc_list -%}
    SET GLBCHRFUNC:
    {#- --- 必选参数 --- -#}
    CHRREPORTSW={{item.CHRREPORTSW}},
    ;
{%- endfor -%}
```

#### 3.4 APN粒度的整系统CHR上报开关。

```jinja2
{%- for item in add_apnchrfunc_list -%}
    ADD APNCHRFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CHRREPORTSW is not none -%}
        CHRREPORTSW={{item.CHRREPORTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置整系统CHR的成功/失败业务流程和信令事件。

```jinja2
{%- for item in add_sessnchrprctmpl_list -%}
    ADD SESSNCHRPRCTMPL:
    {#- --- 必选参数 --- -#}
    TMPLIDX={{item.TMPLIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SESSNCHRFAILPRC is not none -%}
        SESSNCHRFAILPRC={{item.SESSNCHRFAILPRC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置整系统CHR单据上报的高性能CHR服务器以及CHR单据中的设备号。

```jinja2
{%- for item in set_sessnchrcfg_list -%}
    SET SESSNCHRCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.HISRVPRCTMPLIDX is not none -%}
        HISRVPRCTMPLIDX={{item.HISRVPRCTMPLIDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.7 配置整系统正常CHR、整系统异常CHR是否保存至UCF。

```jinja2
{%- for item in set_sessnchrstorecfg_list -%}
    SET SESSNCHRSTORECFG:
    {#- --- 可选参数 --- -#}
    {%- if item.CHRFAILSAVE is not none -%}
        CHRFAILSAVE={{item.CHRFAILSAVE}},
    {%- endif -%}
    {%- if item.CHRALLSAVE is not none -%}
        CHRALLSAVE={{item.CHRALLSAVE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 步骤四：（可选）配置小范围CHR上报策略以及存储策略。

#### 4.1 进入“MML命令行-UEG”窗口。

#### 4.2 配置小范围CHR单据上报开关，并配置小范围CHR是否保存到OMU和UCF。

```jinja2
{%- if is_optional_small_scope_chr_reporting -%}
    {%- for item in set_sessnchrstorecfg_list_1 -%}
        SET SESSNCHRSTORECFG:
        {#- --- 可选参数 --- -#}
        {%- if item.CHRSPESUBSAVE is not none -%}
            CHRSPESUBSAVE={{item.CHRSPESUBSAVE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CHRSPESUBSAVE=ENABLE 时必选 --- -#}
        {%- if item.CHRSPESUBSAVE == 'ENABLE' -%}
            CHRSAVEPATH={{item.CHRSAVEPATH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置小范围CHR的过滤条件。

```jinja2
{%- if is_optional_small_scope_chr_reporting -%}
    {%- for item in add_cpchrrptsubid_list -%}
        ADD CPCHRRPTSUBID:
        {#- --- 必选参数 --- -#}
        IMSI="{{item.IMSI}}",
        TMPLIDX={{item.TMPLIDX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_chrrptlocinfo_list的变量区（command: ADD CHRRPTLOCINFO） -#}
<!-- MISSING_MACRO: command=ADD CHRRPTLOCINFO list_name=add_chrrptlocinfo_list step_id=4.3 -->
```

#### 4.4 配置小范围CHR单据上报的业务流程和信令事件。

```jinja2
{%- if is_optional_small_scope_chr_reporting -%}
    {%- for item in add_sessnchrprctmpl_list_1 -%}
        ADD SESSNCHRPRCTMPL:
        {#- --- 必选参数 --- -#}
        TMPLIDX={{item.TMPLIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.SESSNCHRFAILPRC is not none -%}
            SESSNCHRFAILPRC={{item.SESSNCHRFAILPRC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 步骤五：（可选）配置基于APN上报策略以及存储策略。

#### 5.1 进入“MML命令行-UEG”窗口。

#### 5.2 配置基于APN的CHR单据上报的业务流程和信令事件。

```jinja2
{%- if is_optional_apn_reporting -%}
    {%- for item in add_sessnchrprctmpl_list_2 -%}
        ADD SESSNCHRPRCTMPL:
        {#- --- 必选参数 --- -#}
        TMPLIDX={{item.TMPLIDX}},
        {#- --- 可选参数 --- -#}
        {%- if item.SESSNCHRSUCCPRC is not none -%}
            SESSNCHRSUCCPRC={{item.SESSNCHRSUCCPRC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 配置基于APN的CHR存储表单。

```jinja2
{%- if is_optional_apn_reporting -%}
    {%- for item in add_chrrptsubapn_list -%}
        ADD CHRRPTSUBAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        TMPLIDX={{item.TMPLIDX}},
        CHRFAILSAVE={{item.CHRFAILSAVE}},
        CHRALLSAVE={{item.CHRALLSAVE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

