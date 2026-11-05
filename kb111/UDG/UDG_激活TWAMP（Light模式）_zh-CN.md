---
id: GWFD-110921
name: 激活TWAMP（Light模式）
ne_type: UDG
type: feature
description: IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。在Light模式下，N3/S1-U接口的IP性能检测仅可以由本网元发起，才能对N3/S1-U接口的IP性能进行检测。  适用于SGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能运维功能","GWFD-110921 支持TWAMP","激活TWAMP（Light模式）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。在Light模式下，N3/S1-U接口的IP性能检测仅可以由本网元发起，才能对N3/S1-U接口的IP性能进行检测。适用于SGW-U、UPF。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-110921 支持TWAMP特性概述。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
* TWAMP功能由IPAPM服务承载，请完成IPAPM安装，参见安装IPAPM服务。
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
    add_twampvpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '**ADD TWAMPVPNINST**  “VRFNAME”必须和外联口VPN实例一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_twamplogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '**ADD TWAMPLOGICINF**   * 逻辑接口使用N3/S1-U接口。 * “VRFNAME”已通过**ADD TWAMPVPNINST**配置。 * 如果逻辑接口与业务的N3/S1-U接口共用IP地址，**ADD TWAMPLOGICINF**命令中“SHAREDTYPE”需设置为“TRUE”。 * 如果逻辑接口与业务的N3/S1-U接口不共用IP地址，**ADD TWAMPLOGICINF**命令中“SHAREDTYPE”需设置为“FALSE”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - IPV4
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: '逻辑接口的IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK:
          name: '逻辑接口掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SHAREDTYPE:
          name: '是否共地址'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_twampclient_list:
      type: items
      properties:
        CLIENTID:
          name: '客户端会话ID'
          type: integer
          minimum: 1
          maximum: 12000
          required: true
          description: '**ADD TWAMPCLIENT**  “LOCALIPV4”必须和用于探测的逻辑接口IP地址一致。  “VRFNAME”已通过**ADD TWAMPVPNINST**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TWAMPARCH:
          name: 'TWAMP架构'
          type: string
          enum:
          - LIGHT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - IPV4
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIPV4:
          name: '本端IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERIPV4:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LLOCALUDPPORT:
          name: '本端UDP端口'
          type: integer
          minimum: 65450
          maximum: 65530
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LPEERUDPPORT:
          name: '对端UDP端'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_twampsender_list:
      type: items
      properties:
        CLIENTID:
          name: '客户端会话ID'
          type: integer
          minimum: 1
          maximum: 12000
          required: true
          description: '**ADD TWAMPSENDER**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TIMEOUT:
          name: '超时时间'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 5
    set_linkalmcfg_list:
      type: items
      properties:
        THRESHOLD:
          name: '阈值'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '**SET LINKALMCFG**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CLEARTHRESHOLD:
          name: '恢复阈值'
          type: integer
          minimum: 0
          maximum: 99
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PERIOD:
          name: '检测周期'
          type: integer
          minimum: 10
          maximum: 180
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TWMP01'
      SWITCH: ENABLE
    add_twampvpninst_list:
    - VRFNAME: 'VPN_CN'
    add_twamplogicinf_list:
    - NAME: 'n3if1/1/0'
      AFTYPE: IPV4
      IPV4ADDRESS: '10.1.1.5'
      IPV4MASK: '255.255.255.255'
      VRFNAME: 'VPN_CN'
      SHAREDTYPE: TRUE
    add_twampclient_list:
    - CLIENTID: 1
      TWAMPARCH: LIGHT
      AFTYPE: IPV4
      LOCALIPV4: '10.1.1.5'
      PEERIPV4: '10.2.2.5'
      LLOCALUDPPORT: 65450
      LPEERUDPPORT: 1025
      VRFNAME: 'VPN_CN'
    add_twampsender_list:
    - CLIENTID: 1
      TIMEOUT: 5
    set_linkalmcfg_list:
    - THRESHOLD: 30
      CLEARTHRESHOLD: 10
      PERIOD: 40
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 检查IPAPM是否已安装，若未安装，请完成IPAPM安装，参见安装IPAPM服务。

### 预期结果：“未就绪进程数”和“故障进程数”均为0。

### 2 打开本特性的Licence开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置本端探测逻辑接口。

```jinja2
{%- for item in add_twampvpninst_list -%}
    ADD TWAMPVPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_twamplogicinf_list -%}
    ADD TWAMPLOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    AFTYPE={{item.AFTYPE}},
    IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    IPV4MASK="{{item.IPV4MASK}}",
    SHAREDTYPE={{item.SHAREDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 使用命令**ADD TWAMPLOGICINF**配置本端探测逻辑接口时，若与业务的N3/S1-U接口共用IP地址，**ADD TWAMPLOGICINF**命令中“SHAREDTYPE”参数取值需配置为“TRUE”。

### 4 配置本端对端设备的探测路径。

```jinja2
{%- for item in add_twampclient_list -%}
    ADD TWAMPCLIENT:
    {#- --- 必选参数 --- -#}
    CLIENTID={{item.CLIENTID}},
    TWAMPARCH={{item.TWAMPARCH}},
    AFTYPE={{item.AFTYPE}},
    LOCALIPV4="{{item.LOCALIPV4}}",
    PEERIPV4="{{item.PEERIPV4}}",
    LLOCALUDPPORT={{item.LLOCALUDPPORT}},
    LPEERUDPPORT={{item.LPEERUDPPORT}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置探测路径对应的报文参数。

```jinja2
{%- for item in add_twampsender_list -%}
    ADD TWAMPSENDER:
    {#- --- 必选参数 --- -#}
    CLIENTID={{item.CLIENTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.TIMEOUT is not none -%}
        TIMEOUT={{item.TIMEOUT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置“ALM-100395 链路丢包率过高告警”上报的相关阈值。

```jinja2
{%- for item in set_linkalmcfg_list -%}
    SET LINKALMCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.THRESHOLD is not none -%}
        THRESHOLD={{item.THRESHOLD}},
    {%- endif -%}
    {%- if item.CLEARTHRESHOLD is not none -%}
        CLEARTHRESHOLD={{item.CLEARTHRESHOLD}},
    {%- endif -%}
    {%- if item.PERIOD is not none -%}
        PERIOD={{item.PERIOD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

