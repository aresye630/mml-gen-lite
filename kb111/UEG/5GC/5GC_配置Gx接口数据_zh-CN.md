---
id: ''
name: 配置Gx接口数据
ne_type: UEG
type: feature
description: Gx接口是PGW与PCRF之间的接口，基于Diameter协议进行通信。主要用于PGW-C和PCRF间信令交互实现PCC策略控制功能。  由于N7接口不支持传递PTT业务的策略，部署PTT业务时，需要配置该页面。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置SMF/SGW-C/PGW-C","配置Gx接口数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置SMF/SGW-C/PGW-C","配置Gx接口数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置SMF/SGW-C/PGW-C","配置Gx接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
Gx接口是PGW与PCRF之间的接口，基于Diameter协议进行通信。主要用于PGW-C和PCRF间信令交互实现PCC策略控制功能。由于N7接口不支持传递PTT业务的策略，部署PTT业务时，需要配置该页面。

## 必备事项
前提条件

* 操作员了解UEG各类接口的类型及命名规范。
* 操作员了解UEG与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 需要配置逻辑接口的PBU正常运行，且PBU上无用户存在。当PBU还未启动或正在启动过程中，将无法在该PBU上配置逻辑接口。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPV4最大传输单元'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 1500
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '组级Gx逻辑接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VENDORID:
          name: '设备提供商标识'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 10415
        FIRMWAREREV:
          name: 'Firmware-Revision AVP值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        ORIGINSTATEID:
          name: 'Origin-State-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        SUPPORTVENDORID:
          name: 'Supported-Vendor-Id AVP使能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_cppcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '对接的CPPCRF信息。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DSCPV:
          name: 'DSCP值'
          type: integer
          minimum:
          - 0
          - 255
          maximum:
          - 63
          - 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 255
        WALVALUE:
          name: 'wal值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ENABLE
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C与PCRF之间构建一条IP链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3868
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_pcrfgroup_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '添加pcrf组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOADBALANCEMODE:
          name: '负荷分担模式'
          type: string
          enum:
          - LOAD_BALANCE
          - MASTER_SLAVE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MASTER_SLAVE
        FAILOVERSW:
          name: '宕机备份开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_pcrfbindgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '将PCRF绑定到PCRF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFHOSTNAME:
          name: 'PCRF主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_masterpcrf_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '添加主pcrf。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MASTERPCRF:
          name: '主用PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 13200
          - 16400
          - 19765
          - 20349
          maximum:
          - 0
          - 13263
          - 16463
          - 19784
          - 20368
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
    add_pcrfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'pcrf group绑定到APN下。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '设置APN PCC功能，打开PCC开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_policymode_list:
      type: items
      properties:
        TMACCTYPE:
          name: '指定终端和接入类型'
          type: string
          enum:
          - UE5G_RAT4G
          - UENON5G_RAT4G
          - RAT2G
          - RATNBIOT
          - NON_3GPP
          - RATLTEM
          - RAT3G
          required: true
          description: '控制选择4G Gx口，此命令可控制SMF选择Gx接口或N7接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BY5GSIWKI:
          name: '按5GS互操作指示选择策略接口'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FORCED:
          name: '全局计费模式'
          type: string
          enum:
          - Npcf
          - Gx
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.200.200.88'
      IPV4MTU: 1500
      DESC: 'Gx'
    - IPVERSION: IPv4
      LOGICIPV4: '10.201.200.88'
      IPV4MTU: 1500
      DESC: 'Gx'
    add_cplogicinf_list:
    - NAME: 'gxif1/0/0'
      IPV4ADDRESS1: '10.200.200.88'
      IPV4MASK1: '255.255.255.255'
      IPVERSION: IPV4
    - NAME: 'gxif1/0/0'
      IPV4ADDRESS1: '10.201.200.88'
      IPV4MASK1: '255.255.255.255'
      IPVERSION: IPV4
    add_diamlocinfo_list:
    - HOSTNAME: 'smf01'
      REALMNAME: 'smf01.huawei.com'
      PRODUCTNAME: 'smf'
      VENDORID: 10415
      FIRMWAREREV: 0
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    - HOSTNAME: 'smf02'
      REALMNAME: 'smf02.huawei.com'
      PRODUCTNAME: 'smf'
      VENDORID: 10415
      FIRMWAREREV: 0
      ORIGINSTATEID: DISABLE
      SUPPORTVENDORID: DISABLE
    add_cppcrf_list:
    - HOSTNAME: 'upcf01.huawei.com'
      REALMNAME: 'huawei.com'
      SUPFEANEGOSW: DISABLE
      FEATURELIST: ADC-0&CNO_ULI-0&EXTENDED_BW_NR-0&NETLOC-0&PCSCF_RESTORATION_ENHANCEMENT-0&PENDINGTRANSACTION-0&PROVAFSIGNALFL-0&RELEASE10-0&RELEASE8-1&RELEASE9-1&SGW_REST-0&UMCH-0
      DSCPV: 255
      WALVALUE: 0
      CARRYSUPFEASW: ENABLE
    - HOSTNAME: 'upcf02.huawei.com'
      REALMNAME: 'huawei.com'
      SUPFEANEGOSW: DISABLE
      FEATURELIST: ADC-0&CNO_ULI-0&EXTENDED_BW_NR-0&NETLOC-0&PCSCF_RESTORATION_ENHANCEMENT-0&PENDINGTRANSACTION-0&PROVAFSIGNALFL-0&RELEASE10-0&RELEASE8-1&RELEASE9-1&SGW_REST-0&UMCH-0
      DSCPV: 255
      WALVALUE: 0
      CARRYSUPFEASW: ENABLE
    add_diampeeraddr_list:
    - HOSTNAME: 'upcf01.huawei.com'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.200.200.87'
      PORT: 3868
    - HOSTNAME: 'upcf02.huawei.com'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.201.200.87'
      PORT: 3868
    add_diamconngrp_list:
    - CONNGROUPNAME: 'upcf01.huawei.com'
      LOCALHOSTNAME: 'smf01'
      APPLICATION: GX
      PEERHOSTNAME: 'upcf01.huawei.com'
      SELECTMODE: SESSION_ID
    - CONNGROUPNAME: 'upcf02.huawei.com'
      LOCALHOSTNAME: 'smf02'
      APPLICATION: GX
      PEERHOSTNAME: 'upcf02.huawei.com'
      SELECTMODE: SESSION_ID
    add_pcrfgroup_list:
    - PCRFGRPNAME: 'upcf01.huawei.com'
      LOADBALANCEMODE: MASTER_SLAVE
      FAILOVERSW: DISABLE
    - PCRFGRPNAME: 'upcf02.huawei.com'
      LOADBALANCEMODE: MASTER_SLAVE
      FAILOVERSW: DISABLE
    add_pcrfbindgrp_list:
    - PCRFGRPNAME: 'upcf01.huawei.com'
      PCRFHOSTNAME: 'upcf01.huawei.com'
    - PCRFGRPNAME: 'upcf02.huawei.com'
      PCRFHOSTNAME: 'upcf02.huawei.com'
    set_masterpcrf_list:
    - PCRFGRPNAME: 'upcf01.huawei.com'
      MASTERPCRF: 'upcf01.huawei.com'
    - PCRFGRPNAME: 'upcf02.huawei.com'
      MASTERPCRF: 'upcf02.huawei.com'
    add_diamconnection_list:
    - DIAMCONNGRP: 'upcf01.huawei.com'
      LOCINTERFACE: 'gxif1/0/0'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.200.200.87'
      PEERPORT: 3868
      LOCALPORT: 0
    - DIAMCONNGRP: 'upcf02.huawei.com'
      LOCINTERFACE: 'gxif1/0/0'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.201.200.87'
      PEERPORT: 3868
      LOCALPORT: 0
    add_pcrfgrpbndapn_list:
    - APN: 'ptt.voice'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'upcf01.huawei.com'
    - APN: 'ptt.voice'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'upcf02.huawei.com'
    set_apnpccfunc_list:
    - APN: 'ptt.voice'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    - APN: 'ptt.voice'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    set_policymode_list:
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: DISABLE
      FORCED: Gx
    - TMACCTYPE: UE5G_RAT4G
      BY5GSIWKI: DISABLE
      FORCED: Gx
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置Gx逻辑接口。

#### 2.1 //DC1

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cplogicinf_list -%}
    ADD CPLOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置Diameter本端信息。

#### 3.1 //DC1

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VENDORID is not none -%}
        VENDORID={{item.VENDORID}},
    {%- endif -%}
    {%- if item.FIRMWAREREV is not none -%}
        FIRMWAREREV={{item.FIRMWAREREV}},
    {%- endif -%}
    {%- if item.ORIGINSTATEID is not none -%}
        ORIGINSTATEID={{item.ORIGINSTATEID}},
    {%- endif -%}
    {%- if item.SUPPORTVENDORID is not none -%}
        SUPPORTVENDORID={{item.SUPPORTVENDORID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 添加PCRF。

#### 4.1 //DC1

```jinja2
{%- for item in add_cppcrf_list -%}
    ADD CPPCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPFEANEGOSW is not none -%}
        SUPFEANEGOSW={{item.SUPFEANEGOSW}},
    {%- endif -%}
    {%- if item.FEATURELIST is not none -%}
        FEATURELIST={{item.FEATURELIST}},
    {%- endif -%}
    {%- if item.DSCPV is not none -%}
        DSCPV={{item.DSCPV}},
    {%- endif -%}
    {%- if item.WALVALUE is not none -%}
        WALVALUE={{item.WALVALUE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
    {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
        {%- if item.CARRYSUPFEASW is not none -%}
            CARRYSUPFEASW={{item.CARRYSUPFEASW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 添加对端信息。

#### 5.1 //DC1

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 添加Diameter链路组。

#### 6.1 //DC1

```jinja2
{%- for item in add_diamconngrp_list -%}
    ADD DIAMCONNGRP:
    {#- --- 必选参数 --- -#}
    CONNGROUPNAME="{{item.CONNGROUPNAME}}",
    LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
    PEERHOSTNAME="{{item.PEERHOSTNAME}}",
    APPLICATION={{item.APPLICATION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SELECTMODE is not none -%}
        SELECTMODE={{item.SELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 添加pcrf组。

#### 7.1 //DC1

```jinja2
{%- for item in add_pcrfgroup_list -%}
    ADD PCRFGROUP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOADBALANCEMODE is not none -%}
        LOADBALANCEMODE={{item.LOADBALANCEMODE}},
    {%- endif -%}
    {%- if item.FAILOVERSW is not none -%}
        FAILOVERSW={{item.FAILOVERSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 绑定PCRF到PCRF组。

#### 8.1 //DC1

```jinja2
{%- for item in add_pcrfbindgrp_list -%}
    ADD PCRFBINDGRP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    PCRFHOSTNAME="{{item.PCRFHOSTNAME}}",
    ;
{%- endfor -%}
```

### 9 添加主pcrf。

#### 9.1 //DC1

```jinja2
{%- for item in set_masterpcrf_list -%}
    SET MASTERPCRF:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    MASTERPCRF="{{item.MASTERPCRF}}",
    ;
{%- endfor -%}
```

### 10 增加Diameter链路。

#### 10.1 //DC1

```jinja2
{%- for item in add_diamconnection_list -%}
    ADD DIAMCONNECTION:
    {#- --- 必选参数 --- -#}
    DIAMCONNGRP="{{item.DIAMCONNGRP}}",
    LOCINTERFACE="{{item.LOCINTERFACE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERADDRTYPE is not none -%}
        PEERADDRTYPE={{item.PEERADDRTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv4' -%}
        PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEERADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.PEERADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PEERPORT is not none -%}
            PEERPORT={{item.PEERPORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 绑定pcrf group到APN下。

#### 11.1 //DC1

```jinja2
{%- for item in add_pcrfgrpbndapn_list -%}
    ADD PCRFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    ;
{%- endfor -%}
```

### 12 设置APN PCC功能，打开PCC开关。

#### 12.1 //DC1

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 控制走4G Gx口。

#### 13.1 //DC1

```jinja2
{%- for item in set_policymode_list -%}
    SET POLICYMODE:
    {#- --- 必选参数 --- -#}
    TMACCTYPE={{item.TMACCTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TMACCTYPE=UE5G_RAT4G/RATNBIOT 时可选 --- -#}
    {%- if item.TMACCTYPE in ['UE5G_RAT4G', 'RATNBIOT'] -%}
        {%- if item.BY5GSIWKI is not none -%}
            BY5GSIWKI={{item.BY5GSIWKI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 指定策略接口: 条件必选(指定终端和接入类型=RAT2G|NON_3GPP|RATLTEM|RAT3G) / 条件可选(指定终端和接入类型=UENON5G_RAT4G|UE5G_RAT4G|RATNBIOT) --- -#}
    {%- if (item.TMACCTYPE in ['RAT2G', 'NON_3GPP', 'RATLTEM', 'RAT3G']) -%}
        FORCED={{item.FORCED}},
    {%- elif (item.TMACCTYPE in ['UENON5G_RAT4G', 'UE5G_RAT4G', 'RATNBIOT']) -%}
        {%- if item.FORCED is not none -%}
            FORCED={{item.FORCED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

