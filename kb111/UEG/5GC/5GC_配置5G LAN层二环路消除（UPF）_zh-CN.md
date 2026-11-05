---
id: GWFD-031104
name: 配置5G LAN层二环路消除（UPF）
ne_type: UEG
type: feature
description: 同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信时，可通过部署5G LAN层二环路消除，避免二层环路的危害。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","特性指南","UEG特性指南","可选功能","GWFD-031104 5G LAN层二环路消除","配置5G LAN层二环路消除","配置5G LAN层二环路消除（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信时，可通过部署5G LAN层二环路消除，避免二层环路的危害。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-031104 5G LAN层二环路消除特性概述。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
* 已完成配置5G LAN基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_ngloopdetfunc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ETHLOOPDETECTSW:
          name: '环路检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启环路检测时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DETECTMETHOD:
          name: '环路检测方式'
          type: string
          enum:
          - SEND_DETECT_MSG
          - MAC_FLAP_NUM
          required: false
          description: '* 推荐采用主动检测，主动检测时，使用样例值。 * 当CPE不支持UPF发送的主动环路检测消息等不兼容场景，可采用被动检测，“环路检测方式”参数值设置为“MAC\_FLAP\_NUM”。 * 主动检测和被动检测均不适用的特殊场景，需关闭环路检测开关。默认关闭环路检测开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MACFLAPNUM:
          name: 'MAC地址漂移次数'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '“环路检测方式”设置为“MAC\_FLAP\_NUM”时，UPF根据设置的MAC地址漂移次数阈值，判断是否去活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upethsrvpara_list:
      type: items
      properties:
        UPETHSRVSW:
          name: '用户面以太业务开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '环路检测方式采用主动检测时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: '此处配置的是UPF发送的环路探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。  可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ngloopdetfunc_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ETHLOOPDETECTSW:
          name: '环路检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启环路检测时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DETECTMETHOD:
          name: '环路检测方式'
          type: string
          enum:
          - SEND_DETECT_MSG
          - MAC_FLAP_NUM
          required: false
          description: '* 推荐采用主动检测，主动检测时，使用样例值。 * 当CPE不支持UPF发送的主动环路检测消息等不兼容场景，可采用被动检测，“环路检测方式”参数值设置为“MAC\_FLAP\_NUM”。 * 主动检测和被动检测均不适用的特殊场景，需关闭环路检测开关。默认关闭环路检测开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MACFLAPNUM:
          name: 'MAC地址漂移次数'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: '“环路检测方式”设置为“MAC\_FLAP\_NUM”时，UPF根据设置的MAC地址漂移次数阈值，判断是否去活会话。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LAN2LE'
      SWITCH: ENABLE
    set_ngloopdetfunc_list:
    - VNINSTANCE: '000003e9-460-08-02'
      ETHLOOPDETECTSW: ENABLE
      DETECTMETHOD: SEND_DETECT_MSG
      MACFLAPNUM: 10
    set_upethsrvpara_list:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    set_ngloopdetfunc_list_1:
    - VNINSTANCE: '000003e9-460-08-02'
      ETHLOOPDETECTSW: ENABLE
      DETECTMETHOD: MAC_FLAP_NUM
      MACFLAPNUM: 10
```

## 3 命令模板定义
<!-- @mml:block= commands -->

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

### 2 采用主动检测方案时，配置基于5G LAN组粒度的环路检测及环路消除功能。采用被动检测方案时，请跳过本步骤。

#### 2.1 配置环路检测方式。

```jinja2
{%- if is_scenario_active_detection -%}
    {%- for item in set_ngloopdetfunc_list -%}
        SET NGLOOPDETFUNC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ETHLOOPDETECTSW is not none -%}
            ETHLOOPDETECTSW={{item.ETHLOOPDETECTSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ETHLOOPDETECTSW=ENABLE 时可选 --- -#}
        {%- if item.ETHLOOPDETECTSW == 'ENABLE' -%}
            {%- if item.DETECTMETHOD is not none -%}
                DETECTMETHOD={{item.DETECTMETHOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DETECTMETHOD=MAC_FLAP_NUM 时可选 --- -#}
        {%- if item.DETECTMETHOD == 'MAC_FLAP_NUM' -%}
            {%- if item.MACFLAPNUM is not none -%}
                MACFLAPNUM={{item.MACFLAPNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置环路探测报文的源MAC地址。

```jinja2
{%- if is_scenario_active_detection -%}
    {%- for item in set_upethsrvpara_list -%}
        SET UPETHSRVPARA:
        {#- --- 必选参数 --- -#}
        UPETHSRVSW={{item.UPETHSRVSW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPETHSRVSW=ENABLE 时必选 --- -#}
        {%- if item.UPETHSRVSW == 'ENABLE' -%}
            UPETHSRVMAC="{{item.UPETHSRVMAC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 采用被动检测方案时，配置基于5G LAN组粒度的环路检测及环路消除功能。采用主动检测方案时，请跳过本步骤。

```jinja2
{%- if is_scenario_passive_detection -%}
    {%- for item in set_ngloopdetfunc_list_1 -%}
        SET NGLOOPDETFUNC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ETHLOOPDETECTSW is not none -%}
            ETHLOOPDETECTSW={{item.ETHLOOPDETECTSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ETHLOOPDETECTSW=ENABLE 时可选 --- -#}
        {%- if item.ETHLOOPDETECTSW == 'ENABLE' -%}
            {%- if item.DETECTMETHOD is not none -%}
                DETECTMETHOD={{item.DETECTMETHOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DETECTMETHOD=MAC_FLAP_NUM 时可选 --- -#}
        {%- if item.DETECTMETHOD == 'MAC_FLAP_NUM' -%}
            {%- if item.MACFLAPNUM is not none -%}
                MACFLAPNUM={{item.MACFLAPNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

