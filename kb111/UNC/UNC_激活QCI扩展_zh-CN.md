---
id: ''
name: 激活QCI扩展
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活QCI扩展特性的操作过程。  适用于SGW-C、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-109204 QCI 扩展","激活QCI扩展"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活QCI扩展特性的操作过程。适用于SGW-C、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-109204 QCI 扩展特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
    set_5gcqoscorrt_list:
      type: items
      properties:
        AMBRDL:
          name: '下行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '配置5G QoS缺省参数，用于纠错。当SMF收到UE或UDM消息中携带的QoS字段不合法时，使用该配置作为纠错后的QoS参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIVEQI:
          name: '5QI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: 'ARP值'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_defepsqos_list:
      type: items
      properties:
        QOSCLASSID:
          name: 'QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '配置EPS QoS缺省参数，用于纠错。当UNC收到GTPv2版本消息中携带的QoS字段不合法时，使用该配置作为缺省值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: 'ARP值'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRDL:
          name: '下行APN AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNAMBRUL:
          name: '上行APN AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 2000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_stdqosid_list:
      type: items
      properties:
        QOSIDTYPE:
          name: 'QoS ID类型'
          type: string
          enum:
          - QCI
          - FIVEQI
          required: true
          description: '用于增加标准QCI配置。  根据3GPP协议规定，最初的标准QCI/5QI只有1~9，后续协议演进增加了其他的数值作为标准QoS ID，当需要支持其他的数值作为标准QoS ID时可以通过本命令增加。  说明：  标准QoS ID需要整网规划，通过本命令配置新增的标准QCI/5QI以后，这些标准QCI/5QI就可能通过各个接口发送给对端的不同设备，因此需要同时确认对端设备已支持相应的数值，否则可能会造成业务对接失败。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSIDSV:
          name: 'QoS ID起始值'
          type: integer
          minimum: 10
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSIDEV:
          name: 'QoS ID结束值'
          type: integer
          minimum: 10
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESOURCETYPE:
          name: '标准QoS ID的资源类型'
          type: string
          enum:
          - NONGBR
          - GBR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_extenqciattr_list:
      type: items
      properties:
        QCICTRLFLAG:
          name: '用户接入的扩展QCI控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置扩展QCI和标准QCI的映射关系的缺省值，以及配置控制网关对扩展QCI的资源的管理，包括：  * 是否允许漫游用户使用扩展QCI进行接入网络 * 控制Ga接口话单消息里是用标准QCI还是用扩展QCI * 控制Gy接口CCR消息是用标准QCI还是用扩展QCI * 控制Radius鉴权和计费请求消息里是用标准QCI还是用扩展QCI * 控制N40接口请求消息是用标准QCI还是用扩展QCI'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GASHOWFLAG:
          name: 'Ga接口话单的扩展QCI控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GYSHOWFLAG:
          name: 'Gy接口CCR消息的扩展QCI控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIUSSHOWFLAG:
          name: 'Radius请求信令的扩展QCI控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40SHOWFLAG:
          name: 'N40接口请求消息的扩展QCI控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTQCIMAPDEFQCI:
          name: '扩展QCI映射为标准QCI的缺省值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_extendqcimap_list:
      type: items
      properties:
        EXTENDQCI:
          name: '扩展QCI的值'
          type: integer
          minimum: 10
          maximum: 255
          required: true
          description: '配置/新增扩展QCI和标准QCI的映射关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        STANDARDQCI:
          name: '标准QCI的值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_epsqci2prer8_list:
      type: items
      properties:
        QCI:
          name: 'QCI'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: 'QCI到Pre-R8 QoS参数的映射关系。  说明：  用户通过GnGp SGSN接入UNC，由于GnGp SGSN和UNC之间交互的是GTPv0和GTPv1信令，故UNC需将QCI映射至Pre Rel-8 QoS参数，保证系统正常运行。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TRAFFICCLASS:
          name: '业务类型'
          type: string
          enum:
          - CONVERSATIONAL
          - STREAMING
          - INTERACTIVE
          - BACKGROUND
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THP:
          name: '通信处理优先级'
          type: string
          enum:
          - NA
          - HIGH
          - NORMAL
          - LOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALIND:
          name: '信令传输优化'
          type: string
          enum:
          - DONT_OPTIMIZE
          - OPTIMIZE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCSTATDESC:
          name: '源统计描述'
          type: string
          enum:
          - UNKNOWN
          - SPEECH
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qoschars_list:
      type: items
      properties:
        FQI:
          name: '5QI或QCI'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '当PCF向SMF发送的N7接口消息中未包含qosChars信元时，需配置扩展QCI的QoS特征。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESOURCETYPE:
          name: 'QoS资源类型'
          type: string
          enum:
          - NON_GBR
          - NON_CRITICAL_GBR
          - CRITICAL_GBR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITYLEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PACKETDELBUDGET:
          name: '包时延预算(毫秒)'
          type: integer
          minimum: 1
          maximum: 1000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PACKETERRRATE:
          name: '包错误率'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AVERWINDOW:
          name: '平均窗口(毫秒)'
          type: integer
          minimum: 1
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXDATABURSTVOL:
          name: '最大数据突发量(字节)'
          type: integer
          minimum: 1
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2UNCQCI1'
      SWITCH: ENABLE
    set_5gcqoscorrt_list:
    - AMBRDL: 20000
      AMBRUL: 20000
      FIVEQI: 5
      ARPVALUE: 3
      GFBRUL: 4000
      GFBRDL: 4000
      MFBRDL: 5000
      MFBRUL: 5000
      QOS5QIPL: 10
    set_defepsqos_list:
    - QOSCLASSID: 6
      ARPVALUE: 1
      GBRUL: 230
      GBRDL: 200
      MBRDL: 300
      MBRUL: 300
      APNAMBRDL: 1000
      APNAMBRUL: 1000
    add_stdqosid_list:
    - QOSIDTYPE: QCI
      QOSIDSV: 65
      QOSIDEV: 67
      RESOURCETYPE: GBR
    set_extenqciattr_list:
    - QCICTRLFLAG: ENABLE
      GASHOWFLAG: ENABLE
      GYSHOWFLAG: ENABLE
      RADIUSSHOWFLAG: ENABLE
      N40SHOWFLAG: ENABLE
      EXTQCIMAPDEFQCI: 1
    add_extendqcimap_list:
    - EXTENDQCI: 128
      STANDARDQCI: 8
    set_epsqci2prer8_list:
    - QCI: 6
      TRAFFICCLASS: CONVERSATIONAL
      THP: HIGH
      SIGNALIND: OPTIMIZE
      SRCSTATDESC: SPEECH
    add_qoschars_list:
    - FQI: 128
      RESOURCETYPE: NON_CRITICAL_GBR
      PRIORITYLEVEL: 10
      PACKETDELBUDGET: 1
      PACKETERRRATE: '4E-6'
      AVERWINDOW: 1
      MAXDATABURSTVOL: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### SGW-C和PGW-C分离场景，可能存在PGW-C有扩展QCI的license但是SGW-C无扩展QCI的license的情况。此情况下SGW-C收到携带扩展QCI的专有承载创建请求时的处理受软参控制：

### BIT844 控制SGW-C在无扩展QCI的license时，收到携带扩展QCI的专有承载激活请求是否允许激活成功。

### 取值为0时，允许激活成功，使用标准QCI。

### 取值为1时，不允许激活。

### 3 （可选）配置5G QoS缺省参数，用于纠错。

```jinja2
{%- if is_optional_5g_qos_default_params -%}
    {%- for item in set_5gcqoscorrt_list -%}
        SET 5GCQOSCORRT:
        {#- --- 可选参数 --- -#}
        {%- if item.AMBRDL is not none -%}
            AMBRDL={{item.AMBRDL}},
        {%- endif -%}
        {%- if item.AMBRUL is not none -%}
            AMBRUL={{item.AMBRUL}},
        {%- endif -%}
        {%- if item.ARPVALUE is not none -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- endif -%}
        {%- if item.FIVEQI is not none -%}
            FIVEQI={{item.FIVEQI}},
        {%- endif -%}
        {%- if item.GFBRDL is not none -%}
            GFBRDL={{item.GFBRDL}},
        {%- endif -%}
        {%- if item.GFBRUL is not none -%}
            GFBRUL={{item.GFBRUL}},
        {%- endif -%}
        {%- if item.MFBRDL is not none -%}
            MFBRDL={{item.MFBRDL}},
        {%- endif -%}
        {%- if item.MFBRUL is not none -%}
            MFBRUL={{item.MFBRUL}},
        {%- endif -%}
        {%- if item.QOS5QIPL is not none -%}
            QOS5QIPL={{item.QOS5QIPL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 （可选）配置EPS QoS缺省参数，用于纠错。

```jinja2
{%- if is_optional_eps_qos_default_params -%}
    {%- for item in set_defepsqos_list -%}
        SET DEFEPSQOS:
        {#- --- 可选参数 --- -#}
        {%- if item.APNAMBRDL is not none -%}
            APNAMBRDL={{item.APNAMBRDL}},
        {%- endif -%}
        {%- if item.APNAMBRUL is not none -%}
            APNAMBRUL={{item.APNAMBRUL}},
        {%- endif -%}
        {%- if item.ARPVALUE is not none -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- endif -%}
        {%- if item.GBRDL is not none -%}
            GBRDL={{item.GBRDL}},
        {%- endif -%}
        {%- if item.GBRUL is not none -%}
            GBRUL={{item.GBRUL}},
        {%- endif -%}
        {%- if item.MBRDL is not none -%}
            MBRDL={{item.MBRDL}},
        {%- endif -%}
        {%- if item.MBRUL is not none -%}
            MBRUL={{item.MBRUL}},
        {%- endif -%}
        {%- if item.QOSCLASSID is not none -%}
            QOSCLASSID={{item.QOSCLASSID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （可选）增加、查询标准QCI。

```jinja2
{%- if is_optional_add_query_std_qci -%}
    {%- for item in add_stdqosid_list -%}
        ADD STDQOSID:
        {#- --- 必选参数 --- -#}
        QOSIDSV={{item.QOSIDSV}},
        QOSIDTYPE={{item.QOSIDTYPE}},
        RESOURCETYPE={{item.RESOURCETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOSIDEV is not none -%}
            QOSIDEV={{item.QOSIDEV}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置扩展QCI和标准QCI的映射关系的缺省值以及扩展QCI的部分控制开关（例如漫游用户的扩展QCI开关）。

```jinja2
{%- for item in set_extenqciattr_list -%}
    SET EXTENQCIATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.QCICTRLFLAG is not none -%}
        QCICTRLFLAG={{item.QCICTRLFLAG}},
    {%- endif -%}
    {%- if item.GASHOWFLAG is not none -%}
        GASHOWFLAG={{item.GASHOWFLAG}},
    {%- endif -%}
    {%- if item.GYSHOWFLAG is not none -%}
        GYSHOWFLAG={{item.GYSHOWFLAG}},
    {%- endif -%}
    {%- if item.RADIUSSHOWFLAG is not none -%}
        RADIUSSHOWFLAG={{item.RADIUSSHOWFLAG}},
    {%- endif -%}
    {%- if item.N40SHOWFLAG is not none -%}
        N40SHOWFLAG={{item.N40SHOWFLAG}},
    {%- endif -%}
    {%- if item.EXTQCIMAPDEFQCI is not none -%}
        EXTQCIMAPDEFQCI={{item.EXTQCIMAPDEFQCI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### UNC漫游用户使用扩展QCI接入时，可以通过软参BIT\_1858 控制漫游用户使用扩展QCI接入时UNC是否将扩展QCI按照本地配置映射成为标准的QCI处理。

### 值为0时，按照本地配置映射成标准QCI处理。

### 值为1时，不按照本地配置映射。

### 7 配置/新增扩展QCI和标准QCI的映射关系。

```jinja2
{%- for item in add_extendqcimap_list -%}
    ADD EXTENDQCIMAP:
    {#- --- 必选参数 --- -#}
    EXTENDQCI={{item.EXTENDQCI}},
    STANDARDQCI={{item.STANDARDQCI}},
    ;
{%- endfor -%}
```

### 8 配置QCI到Pre-R8 QoS参数的映射规则。

```jinja2
{%- for item in set_epsqci2prer8_list -%}
    SET EPSQCI2PRER8:
    {#- --- 必选参数 --- -#}
    QCI={{item.QCI}},
    TRAFFICCLASS={{item.TRAFFICCLASS}},
    {#- --- 可选参数 --- -#}
    {%- if item.SIGNALIND is not none -%}
        SIGNALIND={{item.SIGNALIND}},
    {%- endif -%}
    {%- if item.SRCSTATDESC is not none -%}
        SRCSTATDESC={{item.SRCSTATDESC}},
    {%- endif -%}
    {%- if item.THP is not none -%}
        THP={{item.THP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 （可选）当PCF向SMF发送的N7接口消息中未包含qosChars信元时，需配置扩展QCI的QoS特征。

```jinja2
{%- if is_optional_ext_qci_qos_chars -%}
    {%- for item in add_qoschars_list -%}
        ADD QOSCHARS:
        {#- --- 必选参数 --- -#}
        FQI={{item.FQI}},
        RESOURCETYPE={{item.RESOURCETYPE}},
        PRIORITYLEVEL={{item.PRIORITYLEVEL}},
        PACKETDELBUDGET={{item.PACKETDELBUDGET}},
        PACKETERRRATE="{{item.PACKETERRRATE}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RESOURCETYPE=NON_CRITICAL_GBR/CRITICAL_GBR 时必选 --- -#}
        {%- if item.RESOURCETYPE in ['NON_CRITICAL_GBR', 'CRITICAL_GBR'] -%}
            AVERWINDOW={{item.AVERWINDOW}},
        {%- endif -%}
        {#- --- 条件必选：RESOURCETYPE=CRITICAL_GBR 时必选 --- -#}
        {%- if item.RESOURCETYPE == 'CRITICAL_GBR' -%}
            MAXDATABURSTVOL={{item.MAXDATABURSTVOL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 当软参DWORD506 BIT4的值为“1”时，无需配置**ADD QOSCHARS**。

