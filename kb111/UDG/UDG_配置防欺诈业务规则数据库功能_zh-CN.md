---
id: ''
name: 配置防欺诈业务规则数据库功能
ne_type: UDG
type: feature
description: 适用于PGW-U、UPF。  当运营商规划检测利用计费漏洞进行欺诈的用户行为时，需要配置防欺诈业务规则数据库功能，进而对欺诈行为进行评估和策略控制。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG防欺诈功能专题","HTTP计费防欺诈","激活HTTP计费防欺诈","配置防欺诈业务规则数据库功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
适用于PGW-U、UPF。当运营商规划检测利用计费漏洞进行欺诈的用户行为时，需要配置防欺诈业务规则数据库功能，进而对欺诈行为进行评估和策略控制。

## 必备事项
前提条件

前提条件

* 请仔细阅读HTTP计费防欺诈。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。

* 防欺诈业务规则数据库文件和防欺诈业务规则数据库数字签名文件已经上载到SSGCTRL容器下的“/opt/sf\_filetrans/SessionSGCtrlSvc”目录。
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
          description: '-'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    lod_afdb_list:
      type: items
      properties:
        VERSION:
          name: '防欺诈业务规则数据库版本号'
          type: string
          minLength: 0
          maxLength: 21
          required: true
          description: '加载防欺诈业务规则数据库。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_afdnsserver_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置防欺诈可信的DNS服务器IP，用于从DNS响应中学习应用服务器IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'DNS服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'DNS服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_afproxyserver_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置防欺诈可信的代理服务器的IP地址。当检测利用代理服务器进行计费欺诈的行为时，使用此命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: '代理服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: '代理服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_antifraud_list:
      type: items
      properties:
        HTTPAFSWITCH:
          name: 'HTTP防欺诈总开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启HTTP防欺诈。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaffunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '开启APN级的防欺诈功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ISENABLE:
          name: '防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Byte
        DFTQUOTATIME:
          name: '默认时长配额（秒）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 3600
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAVOLUME:
          name: '默认流量配额'
          type: integer
          minimum:
          - 0
          - 1000
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '对检测为欺诈的报文的计费。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '上行业务触发使用的URRName，已通过**ADD URR**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '下行业务触发使用的URRName，已通过**ADD URR**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccactionprop_list:
      type: items
      properties:
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '对检测为欺诈的报文的处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINITUPGATE:
          name: '上行发起上行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        UPINITDNGATE:
          name: '上行发起下行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        DNINITUPGATE:
          name: '下行发起上行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        DNINITDNGATE:
          name: '下行发起下行门控'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置PCC策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的URR组名称，已通过**ADD URRGROUP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCCACTPROPNAME:
          name: 'PCC动作属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的PCC动作属性，已通过**ADD PCCACTIONPROP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_afpolicy_list:
      type: items
      properties:
        AFPOLICYTYPE:
          name: '防欺诈策略类型'
          type: string
          enum:
          - DNS
          - HTTP
          - HTTPS
          required: true
          description: '配置HTTP欺诈用户的控制策略。   * 通过**ADD AFPOLICY**命令中的“PCCPOLICYGRPNM”参数配置针对欺诈用户的计费矫正策略；通过**ADD AFPOLICY**命令中的“CATEPROPNAME”参数配置针对欺诈用户的带宽控制策略。 * 两种策略可选其一，或多选，此处以计费策略为例。若不规划任何控制策略，则本步骤无需配置，此时仅支持防欺诈检测功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '欺诈用户的PCC策略组，已通过**ADD PCCPOLICYGRP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_specurrgrplist_list:
      type: items
      properties:
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加特殊URR组列表，选择对免费RG进行防欺诈判断，正常计费RG不需要进行判断。免费或优惠费率的URR组已通过**ADD URRGROUP**命令配置完成。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5HCAS01'
      SWITCH: ENABLE
    lod_afdb_list:
    - VERSION: '0001.01.0086.0001.001'
    add_afdnsserver_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.1'
      IPV6ADDR: ''
    add_afproxyserver_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.2'
      IPV6ADDR: ''
    set_antifraud_list:
    - HTTPAFSWITCH: ENABLE
    set_apnaffunc_list:
    - APN: 'apn-af'
      ISENABLE: ENABLE
    add_urr_list:
    - URRNAME: 'urr_test'
      URRID: 1000
      USAGERPTMODE: OFFLINE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'cp_test'
      UPURRNAME1: 'urr_test'
      DOWNURRNAME1: 'urr_test'
    add_pccactionprop_list:
    - PCCACTPROPNAME: 'pap_test'
      UPINITUPGATE: pass
      UPINITDNGATE: pass
      DNINITUPGATE: pass
      DNINITDNGATE: pass
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg_test'
      URRGROUPNAME: 'cp_test'
      PCCACTPROPNAME: 'pap_test'
    add_afpolicy_list:
    - AFPOLICYTYPE: HTTP
      PCCPOLICYGRPNM: 'ppg_test'
    add_specurrgrplist_list:
    - URRGROUPNAME: 'cp_free'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //加载防欺诈特征库。

```jinja2
{%- for item in lod_afdb_list -%}
    LOD AFDB:
    {#- --- 必选参数 --- -#}
    VERSION="{{item.VERSION}}",
    ;
{%- endfor -%}
```

### 3 //配置防欺诈判断规则。

```jinja2
{%- for item in add_afdnsserver_list -%}
    ADD AFDNSSERVER:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_afproxyserver_list -%}
    ADD AFPROXYSERVER:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 //配置HTTP防欺诈功能。

```jinja2
{%- for item in set_antifraud_list -%}
    SET ANTIFRAUD:
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPAFSWITCH is not none -%}
        HTTPAFSWITCH={{item.HTTPAFSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //配置APN防欺诈功能。

```jinja2
{%- for item in set_apnaffunc_list -%}
    SET APNAFFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ISENABLE={{item.ISENABLE}},
    ;
{%- endfor -%}
```

### 6 //配置欺诈用户的URR组和策略。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAPARA is not none -%}
            DFTQUOTAPARA={{item.DFTQUOTAPARA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTATIME is not none -%}
            DFTQUOTATIME={{item.DFTQUOTATIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAVOLUME is not none -%}
            DFTQUOTAVOLUME={{item.DFTQUOTAVOLUME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.RG is not none -%}
            RG={{item.RG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.SID is not none -%}
            SID={{item.SID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccactionprop_list -%}
    ADD PCCACTIONPROP:
    {#- --- 必选参数 --- -#}
    PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DNINITDNGATE is not none -%}
        DNINITDNGATE={{item.DNINITDNGATE}},
    {%- endif -%}
    {%- if item.DNINITUPGATE is not none -%}
        DNINITUPGATE={{item.DNINITUPGATE}},
    {%- endif -%}
    {%- if item.UPINITDNGATE is not none -%}
        UPINITDNGATE={{item.UPINITDNGATE}},
    {%- endif -%}
    {%- if item.UPINITUPGATE is not none -%}
        UPINITUPGATE={{item.UPINITUPGATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PCCACTPROPNAME is not none -%}
        PCCACTPROPNAME="{{item.PCCACTPROPNAME}}",
    {%- endif -%}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 //绑定欺诈用户的控制策略。

```jinja2
{%- for item in add_afpolicy_list -%}
    ADD AFPOLICY:
    {#- --- 必选参数 --- -#}
    AFPOLICYTYPE={{item.AFPOLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PCCPOLICYGRPNM is not none -%}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 //配置特殊URR组列表，选择对免费RG进行判断。

```jinja2
{%- for item in add_specurrgrplist_list -%}
    ADD SPECURRGRPLIST:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    ;
{%- endfor -%}
```

