---
id: ''
name: 配置业务报表功能
ne_type: UDG
type: feature
description: 当需要在报表服务器上查询UDG的各种业务报表时，需要在UDG上激活业务报表功能。激活此功能后，在报表服务器上可基于APN、位置、用户、应用、终端、服务器、接入网多个维度对业务做流量分析或者TOPN分析，满足运营商对网络可视化的需求。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG报表功能专题","报表功能部署","激活报表功能","配置业务报表功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要在报表服务器上查询UDG的各种业务报表时，需要在UDG上激活业务报表功能。激活此功能后，在报表服务器上可基于APN、位置、用户、应用、终端、服务器、接入网多个维度对业务做流量分析或者TOPN分析，满足运营商对网络可视化的需求。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-111301 智能分析记录生成、GWFD-111302 业务全样分析上报、GWFD-111303 阻塞流量分析上报、GWFD-111304 TCP/UDP传输分析上报、GWFD-111305 用户实时位置分析上报、GWFD-111306 VOIP业务分析上报、GWFD-111307 Web业务分析上报、GWFD-111308 VoLTE业务质量上报、GWFD-111309 PCC规则报表上报、GWFD-111310 QUIC业务分析上报、GWFD-111311 业务分析上报订阅、GWFD-111312 系统级智能分析记录生成、GWFD-111313 业务实时分析上报、GWFD-111315 VoNR业务质量上报。
* 完成业务感知配置。
* 完成配置到报表服务器的数据。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
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
    set_rptglbcfg_list:
      type: items
      properties:
        GLOBALSWITCH:
          name: '全局业务报表上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置报表功能全局开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNSINSIGHTSW:
          name: 'DNS业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TCPINSIGHTSW:
          name: 'TCP业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UDPINSIGHTSW:
          name: 'UDP业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBSPOLICYSW:
          name: '订阅策略开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBSCONFIGSW:
          name: '配置策略开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CACHESW:
          name: '缓存开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SIPINSIGHTSW:
          name: 'SIP上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VOLTEINSIGHTSW:
          name: 'VoLTE语音质量分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VONRINSIGHTSW:
          name: 'VoNR语音质量分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rptpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置指定策略的业务报表功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '业务报表开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - GLOBAL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERSELPLYTYPE:
          name: '用户选择策略类型'
          type: string
          enum:
          - ANY
          - SPECIFIC
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERSELPLYNAME:
          name: '用户选择策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_rptglbpara_list:
      type: items
      properties:
        FLOWSAMPLERATE:
          name: '流的识别抽样率'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: '设置报表功能全局参数。  说明：  抽样率配置越大对性能影响越大，修改抽样率前请联系华为技术支持评估对系统性能的影响。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NEID:
          name: '网元标识'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TCPINSIGHTSAMRT:
          name: 'TCP业务分析上报功能流抽样率'
          type: integer
          minimum: 1
          maximum: 1000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_sacommonpara_list:
      type: items
      properties:
        QUICSASW:
          name: 'Quic SA协议确定后进行匹配的开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置在QUIC SA协议识别状态确定后进行策略匹配的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rptbasicreccfg_list:
      type: items
      properties:
        USERINFOSW:
          name: '用户信息开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置基础单据上报配置开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERSTATSSW:
          name: '用户统计开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        APPSTATSSW:
          name: 'APP统计开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESOUCESW:
          name: '资源开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnvoltemonfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已在配置普通APN中通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SWITCH:
          name: 'VoLTE语音质量监控功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: 'VoLTE业务质量检测。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_volteswalbrk_list:
      type: items
      properties:
        SWITCH:
          name: '功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BREAKWIN:
          name: '断续滑窗大小'
          type: integer
          minimum: 6
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BREAKWINTHD:
          name: '断续的滑窗阈值'
          type: integer
          minimum: 6
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWALLOWWIN:
          name: '吞字滑窗大小'
          type: integer
          minimum: 5
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWALLOWWINTHD:
          name: '吞字的滑窗阈值'
          type: integer
          minimum: 5
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_volteonewaysil_list:
      type: items
      properties: {}
    set_apnvonrmonfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已在配置普通APN中通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SWITCH:
          name: 'VoNR语音质量监控功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '使能VoNR语音质量监控功能开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_vonrabnormos_list:
      type: items
      properties:
        MOSABNORMTHD:
          name: 'VoNR MOS值的异常门限'
          type: integer
          minimum: 5
          maximum: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_vonrmosclass_list:
      type: items
      properties: {}
    set_vonrmosfactor_list:
      type: items
      properties:
        MOSCODEC:
          name: '语音编解码类型'
          type: string
          enum:
          - MOS_CODEC_ALL
          - MOS_CODEC_AMR_NB
          - MOS_CODEC_AMR_WB
          - MOS_CODEC_EVS_AMR
          - MOS_CODEC_EVS_FB
          - MOS_CODEC_EVS_NB
          - MOS_CODEC_EVS_SWB
          - MOS_CODEC_EVS_WB
          - MOS_CODEC_G711
          - MOS_CODEC_G722
          - MOS_CODEC_G729
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_vonronewaysil_list:
      type: items
      properties: {}
    set_vonrperftdelay_list:
      type: items
      properties: {}
    set_vonrswalbrk_list:
      type: items
      properties:
        SWITCH:
          name: '功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BREAKWIN:
          name: '断续滑窗大小'
          type: integer
          minimum: 6
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BREAKWINTHD:
          name: '断续的滑窗阈值'
          type: integer
          minimum: 6
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWALLOWWIN:
          name: '吞字滑窗大小'
          type: integer
          minimum: 5
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWALLOWWINTHD:
          name: '吞字的滑窗阈值'
          type: integer
          minimum: 5
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5IARG01'
      SWITCH: ENABLE
    set_rptglbcfg_list:
    - GLOBALSWITCH: ENABLE
      DNSINSIGHTSW: ENABLE
      TCPINSIGHTSW: ENABLE
      UDPINSIGHTSW: ENABLE
      SUBSPOLICYSW: ENABLE
      SUBSCONFIGSW: ENABLE
      CACHESW: ENABLE
      SIPINSIGHTSW: ENABLE
      VOLTEINSIGHTSW: ENABLE
      VONRINSIGHTSW: ENABLE
    add_rptpolicy_list:
    - POLICYNAME: 'policy01'
      SWITCH: ENABLE
      USERSELPLYTYPE: ANY
      USERSELPLYNAME: ''
    set_rptglbpara_list:
    - FLOWSAMPLERATE: 1000
      NEID: 1
      TCPINSIGHTSAMRT: 1000
    set_sacommonpara_list:
    - QUICSASW: ENABLE
    set_rptbasicreccfg_list:
    - USERINFOSW: ENABLE
      USERSTATSSW: ENABLE
      APPSTATSSW: ENABLE
      RESOUCESW: ENABLE
    set_apnvoltemonfunc_list:
    - APN: 'apn.internet'
      SWITCH: ENABLE
    set_volteswalbrk_list:
    - SWITCH: ''
      BREAKWIN: ''
      BREAKWINTHD: ''
      SWALLOWWIN: ''
      SWALLOWWINTHD: ''
    set_volteonewaysil_list:
    - {}
    set_apnvonrmonfunc_list:
    - APN: 'apn.internet'
      SWITCH: ENABLE
    set_vonrabnormos_list:
    - MOSABNORMTHD: ''
    set_vonrmosclass_list:
    - {}
    set_vonrmosfactor_list:
    - MOSCODEC: ''
    set_vonronewaysil_list:
    - {}
    set_vonrperftdelay_list:
    - {}
    set_vonrswalbrk_list:
    - SWITCH: ''
      BREAKWIN: ''
      BREAKWINTHD: ''
      SWALLOWWIN: ''
      SWALLOWWINTHD: ''
    set_softpara_list:
    - DT: BIT
      BITNUM: 1557
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置智能分析记录生成/业务全样分析上报/阻塞流量分析上报/TCP/UDP传输分析上报/用户实时位置分析上报/VOIP业务分析上报/Web业务分析上报/VoLTE业务质量上报/PCC规则报表/QUIC业务分析上报/业务分析上报订阅/系统级智能分析记录生成/业务实时分析上报/VoNR业务质量上报等特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置全局报表功能开关。

```jinja2
{%- for item in set_rptglbcfg_list -%}
    SET RPTGLBCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.GLOBALSWITCH is not none -%}
        GLOBALSWITCH={{item.GLOBALSWITCH}},
    {%- endif -%}
    {%- if item.DNSINSIGHTSW is not none -%}
        DNSINSIGHTSW={{item.DNSINSIGHTSW}},
    {%- endif -%}
    {%- if item.TCPINSIGHTSW is not none -%}
        TCPINSIGHTSW={{item.TCPINSIGHTSW}},
    {%- endif -%}
    {%- if item.UDPINSIGHTSW is not none -%}
        UDPINSIGHTSW={{item.UDPINSIGHTSW}},
    {%- endif -%}
    {%- if item.SUBSPOLICYSW is not none -%}
        SUBSPOLICYSW={{item.SUBSPOLICYSW}},
    {%- endif -%}
    {%- if item.SUBSCONFIGSW is not none -%}
        SUBSCONFIGSW={{item.SUBSCONFIGSW}},
    {%- endif -%}
    {%- if item.CACHESW is not none -%}
        CACHESW={{item.CACHESW}},
    {%- endif -%}
    {%- if item.SIPINSIGHTSW is not none -%}
        SIPINSIGHTSW={{item.SIPINSIGHTSW}},
    {%- endif -%}
    {%- if item.VOLTEINSIGHTSW is not none -%}
        VOLTEINSIGHTSW={{item.VOLTEINSIGHTSW}},
    {%- endif -%}
    {%- if item.VONRINSIGHTSW is not none -%}
        VONRINSIGHTSW={{item.VONRINSIGHTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置指定策略的业务报表功能开关。

```jinja2
{%- for item in add_rptpolicy_list -%}
    ADD RPTPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    SWITCH={{item.SWITCH}},
    USERSELPLYTYPE={{item.USERSELPLYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERSELPLYTYPE=SPECIFIC 时必选 --- -#}
    {%- if item.USERSELPLYTYPE == 'SPECIFIC' -%}
        USERSELPLYNAME="{{item.USERSELPLYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 在报表功能开关被关闭的情况下，所有报表配置都将无效，所以要开启此特性，需要使用**SET RPTGLBCFG**和**ADD RPTPOLICY**命令打开报表功能开关。

### 4 配置流抽样率。

```jinja2
{%- for item in set_rptglbpara_list -%}
    SET RPTGLBPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWSAMPLERATE is not none -%}
        FLOWSAMPLERATE={{item.FLOWSAMPLERATE}},
    {%- endif -%}
    {%- if item.NEID is not none -%}
        NEID={{item.NEID}},
    {%- endif -%}
    {%- if item.TCPINSIGHTSAMRT is not none -%}
        TCPINSIGHTSAMRT={{item.TCPINSIGHTSAMRT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 当业务全样分析上报特性的License开关关闭时，缺省抽样率为10%，当**SET RPTGLBPARA**命令配置的抽样率超过10%时，则按照抽样率为10%进行抽样，配置的抽样率小于10%时就按照命令配置的抽样率进行抽样。

### 当业务全样分析上报特性的License开关打开时，按照**SET RPTGLBPARA**命令配置的抽样率进行抽样。

### 5 **可选：**配置在QUIC SA协议识别状态确定后进行策略匹配的开关。

```jinja2
{%- if is_optional_quic_sa_policy_match -%}
    {%- for item in set_sacommonpara_list -%}
        SET SACOMMONPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.QUICSASW is not none -%}
            QUICSASW={{item.QUICSASW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 设置基础单据上报配置开关。

```jinja2
{%- for item in set_rptbasicreccfg_list -%}
    SET RPTBASICRECCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.USERINFOSW is not none -%}
        USERINFOSW={{item.USERINFOSW}},
    {%- endif -%}
    {%- if item.APPSTATSSW is not none -%}
        APPSTATSSW={{item.APPSTATSSW}},
    {%- endif -%}
    {%- if item.RESOUCESW is not none -%}
        RESOUCESW={{item.RESOUCESW}},
    {%- endif -%}
    {%- if item.USERSTATSSW is not none -%}
        USERSTATSSW={{item.USERSTATSSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **可选：**开启VoLTE业务质量上报功能。

#### 7.1 开启VoLTE业务质量检测功能。

```jinja2
{%- if is_optional_volte_qos_report -%}
    {%- for item in set_apnvoltemonfunc_list -%}
        SET APNVOLTEMONFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 **可选：**开启VoLTE吞字断续检测和上报功能。

```jinja2
{%- if is_optional_volte_qos_report and is_optional_volte_swallow_break_detect -%}
    {%- for item in set_volteswalbrk_list -%}
        SET VOLTESWALBRK:
        {#- --- 必选参数 --- -#}
        SWITCH={{item.SWITCH}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.BREAKWIN is not none -%}
                BREAKWIN={{item.BREAKWIN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.BREAKWINTHD is not none -%}
                BREAKWINTHD={{item.BREAKWINTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.SWALLOWWIN is not none -%}
                SWALLOWWIN={{item.SWALLOWWIN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.SWALLOWWINTHD is not none -%}
                SWALLOWWINTHD={{item.SWALLOWWINTHD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.3 **可选：**开启单通检测功能。

```jinja2
{%- if is_optional_volte_qos_report and is_optional_oneway_detect -%}
    SET VOLTEONEWAYSIL:
    ;
{%- endif -%}
```

### 8 **可选：**开启VoNR业务质量上报功能。

#### 8.1 设置VoNR语音质量监控功能开关。

```jinja2
{%- if is_optional_vonr_qos_report -%}
    {%- for item in set_apnvonrmonfunc_list -%}
        SET APNVONRMONFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 **可选：**指定MOS值的异常门限值。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_mos_abnormal_threshold -%}
    {%- for item in set_vonrabnormos_list -%}
        SET VONRABNORMOS:
        {#- --- 必选参数 --- -#}
        MOSABNORMTHD={{item.MOSABNORMTHD}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.3 **可选：**配置MOS分类的区间值。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_mos_class_range -%}
    SET VONRMOSCLASS:
    ;
{%- endif -%}
```

#### 8.4 **可选：**设置MOS计算值的补偿因子。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_mos_compensation_factor -%}
    {%- for item in set_vonrmosfactor_list -%}
        SET VONRMOSFACTOR:
        {#- --- 必选参数 --- -#}
        MOSCODEC={{item.MOSCODEC}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.5 **可选：**设置单通检测信息。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_oneway_detect_info -%}
    SET VONRONEWAYSIL:
    ;
{%- endif -%}
```

#### 8.6 **可选：**配置理想到达报文的最小时延偏差、固定传输时延。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_ideal_packet_delay -%}
    SET VONRPERFTDELAY:
    ;
{%- endif -%}
```

#### 8.7 **可选：**设置VoLTE滑窗相关的参数。

```jinja2
{%- if is_optional_vonr_qos_report and is_optional_volte_sliding_window -%}
    {%- for item in set_vonrswalbrk_list -%}
        SET VONRSWALBRK:
        {#- --- 必选参数 --- -#}
        SWITCH={{item.SWITCH}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.BREAKWIN is not none -%}
                BREAKWIN={{item.BREAKWIN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.BREAKWINTHD is not none -%}
                BREAKWINTHD={{item.BREAKWINTHD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.SWALLOWWIN is not none -%}
                SWALLOWWIN={{item.SWALLOWWIN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            {%- if item.SWALLOWWINTHD is not none -%}
                SWALLOWWINTHD={{item.SWALLOWWINTHD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 可选：配置软参“BIT1557”为1，向CloudUDN上报的报表UFDR单据包含Charging TLV、QoS TLV、Charging\_ID TLV、GTP\_Path TLV相关字段。

```jinja2
{%- if is_optional_softpara_bit1557 -%}
    {%- for item in set_softpara_list -%}
        SET SOFTPARA:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=BIT 时必选 --- -#}
        {%- if item.DT == 'BIT' -%}
            BITNUM={{item.BITNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=BIT 时必选 --- -#}
        {%- if item.DT == 'BIT' -%}
            BITVALUE={{item.BITVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=BYTE 时必选 --- -#}
        {%- if item.DT == 'BYTE' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=BYTE 时必选 --- -#}
        {%- if item.DT == 'BYTE' -%}
            BYTEVALUE={{item.BYTEVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=DWORD 时必选 --- -#}
        {%- if item.DT == 'DWORD' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=DWORD 时必选 --- -#}
        {%- if item.DT == 'DWORD' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=STRING 时必选 --- -#}
        {%- if item.DT == 'STRING' -%}
            STRINGNUM={{item.STRINGNUM}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DT=STRING 时可选 --- -#}
        {%- if item.DT == 'STRING' -%}
            {%- if item.STRINGVALUE is not none -%}
                STRINGVALUE="{{item.STRINGVALUE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

