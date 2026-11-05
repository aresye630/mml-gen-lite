---
id: GWFD-111701
name: 激活拥塞小区分析
ne_type: UDG
type: feature
description: 当运营商想要激活拥塞小区分析功能时，需要配置本页面。  适用于UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","报表功能","GWFD-111701 拥塞小区分析","激活拥塞小区分析","激活拥塞小区分析"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商想要激活拥塞小区分析功能时，需要配置本页面。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-111701 拥塞小区分析特性概述。
* 已完成业务感知配置。
* 已完成配置到CloudUDN的数据。
* 已完成加载License。
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
          description: '小区拥塞优化  智能分析记录生成  业务全样分析上报  TCP/UDP传输分析上报  业务分析上报订阅  系统级智能分析记录生成  基于业务感知的带宽控制  基于业务的Shaping  TCP优化功能'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rptglbcfg_list:
      type: items
      properties:
        TCPINSIGHTSW:
          name: 'TCP业务分析上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '设置报表功能开关。'
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
    set_ssubigflowctrl_list:
      type: items
      properties:
        CCOFLOWRATE:
          name: 'CCO业务大流速率'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '整数类型，取值范围1～4294967295，缺省100，单位为KBytes。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_usrreallocnty_list:
      type: items
      properties:
        SWITCH:
          name: '主动触发用户位置实时通知功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '设置主动触发用户位置实时通知功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRSAMPLINGRATE:
          name: '用户抽样比'
          type: integer
          minimum: 1
          maximum: 100
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
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: '不检测，表示匹配该流过滤器无需检测Tethering属性，过滤器匹配时不区分是否Tethering用户。'
          data_source: '本端规划'
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: '设置FlowFilter类型为用户配置。'
          data_source: '本端规划'
          pattern: ''
          default: USERCONFIG
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置规则名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: '该规则用于通用Rule业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: '指定流过滤器作为过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '设置通用Rule下子策略名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5OBCCS1'
      SWITCH: ENABLE
    set_rptglbcfg_list:
    - TCPINSIGHTSW: ENABLE
      UDPINSIGHTSW: ENABLE
      SUBSPOLICYSW: ENABLE
      SUBSCONFIGSW: ENABLE
    add_rptpolicy_list:
    - POLICYNAME: 'policy01'
      SWITCH: ENABLE
      USERSELPLYTYPE: ANY
      USERSELPLYNAME: ''
    set_rptglbpara_list:
    - FLOWSAMPLERATE: 1000
      NEID: 1
      TCPINSIGHTSAMRT: 1000
    set_ssubigflowctrl_list:
    - CCOFLOWRATE: 100
    set_usrreallocnty_list:
    - SWITCH: ENABLE
      USRSAMPLINGRATE: 10
    set_softpara_list:
    - DT: BIT
      BITNUM: 1241
      BITVALUE: 1;//对于5G SA/NSA用户，需要开启该软参。
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_zxm'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_rule_list:
    - RULENAME: 'rule_zxm_to'
      POLICYTYPE: WORKER
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_zxm'
      WORKERNAME: 'to'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      POLICYNAME: ''
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERPARA: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置报表功能开关。

```jinja2
{%- for item in set_rptglbcfg_list -%}
    SET RPTGLBCFG:
    {#- --- 可选参数 --- -#}
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

### 当业务全样分析上报特性的License开关打开时，按照**SET RPTGLBPARA**命令配置的抽样率进行抽样。

### 5 配置小区拥塞优化业务大流速率。

```jinja2
{%- for item in set_ssubigflowctrl_list -%}
    SET SSUBIGFLOWCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.CCOFLOWRATE is not none -%}
        CCOFLOWRATE={{item.CCOFLOWRATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 设置主动触发用户位置实时通知功能。

```jinja2
{%- for item in set_usrreallocnty_list -%}
    SET USRREALLOCNTY:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.USRSAMPLINGRATE is not none -%}
            USRSAMPLINGRATE={{item.USRSAMPLINGRATE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **可选**：配置vTCP\_OPT功能，生效拥塞小区分析功能。

#### 7.1 完成**安装vTCP\_OPT服务**。

#### 7.2 对于5G SA/NSA用户，需要开启软参BIT1241 控制5G SA用户是否支持TCP优化、BIT1242 控制5G NSA用户是否支持TCP优化。

```jinja2
{%- if is_optional_vtcp_opt -%}
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

#### 7.3 配置一个空的FlowFilter，并绑定到子策略名称为to的Rule。

```jinja2
{%- if is_optional_vtcp_opt -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TETHERDETFLAG is not none -%}
            TETHERDETFLAG={{item.TETHERDETFLAG}},
        {%- endif -%}
        {%- if item.FLOWFILTERTYPE is not none -%}
            FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
        {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
            {%- if item.FILTERGRPNAME is not none -%}
                FILTERGRPNAME="{{item.FILTERGRPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_vtcp_opt -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            WORKERNAME="{{item.WORKERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ADC' -%}
            ADCMUTEFLAG={{item.ADCMUTEFLAG}},
        {%- endif -%}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
            FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
            RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
        {%- if item.POLICYTYPE == 'IPREDIR' -%}
            REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
        {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
            REMARKFPISEL={{item.REMARKFPISEL}},
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
        {%- if item.POLICYTYPE == 'LBO' -%}
            SRVLBOFLAG={{item.SRVLBOFLAG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WEBPROXY' -%}
            {%- if item.ALGSWITCH is not none -%}
                ALGSWITCH={{item.ALGSWITCH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            {%- if item.WORKERPARA is not none -%}
                WORKERPARA="{{item.WORKERPARA}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

