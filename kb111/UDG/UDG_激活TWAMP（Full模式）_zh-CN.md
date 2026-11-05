---
id: GWFD-110921
name: 激活TWAMP（Full模式）
ne_type: UDG
type: feature
description: IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。  适用于SGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能运维功能","GWFD-110921 支持TWAMP","激活TWAMP（Full模式）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
IP传输场景下，线路带宽不稳定，运营商可以部署TWAMP功能检测网元间的传输网络QoS，如丢包、时延、抖动，实时在线监控传输网络QoS的变化。适用于SGW-U、UPF。

## 必备事项
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
          description: '**ADD TWAMPLOGICINF**   * 逻辑接口使用N3/S1-U接口。 * “VRFNAME”已通过**ADD TWAMPVPNINST**配置。 * 如果与业务的N3/S1-U接口共用IP地址，**ADD TWAMPLOGICINF**命令中“SHAREDTYPE”需设置为“TRUE”。 * 如果与业务的N3/S1-U接口不共用IP地址，**ADD TWAMPLOGICINF**命令中“SHAREDTYPE”需设置为“FALSE”。'
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
    add_twampresponder_list:
      type: items
      properties:
        RESPONDERID:
          name: '响应端索引'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: '**ADD TWAMPRESPONDER**  ServWait：控制连接建立时，如果本端在该时间内没有收到与该连接相关的数据包时，则本端删除与Client端建立的所有测试会话，并释放与Client端的控制连接。  RefWait：启动测试会话后，如果本端在该时间内，没有收到任何一个测试会话的Sender-Test报文，则认为故障，删除当前控制连接下的所有的测试会话。'
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
        TWAMPARCH:
          name: 'TWAMP架构'
          type: string
          enum:
          - FULL
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LOCALIPV4:
          name: '本端IPv4'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVWAIT:
          name: '协商等待时间'
          type: integer
          minimum: 10
          maximum: 1800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 900
        REFWAIT:
          name: '测试等待时间'
          type: integer
          minimum: 10
          maximum: 1800
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 900
    set_tcpkeepalivecfg_list:
      type: items
      properties:
        KEEPALIVETIME:
          name: '保活时间'
          type: integer
          minimum: 30
          maximum: 7200
          required: false
          description: '**SET TCPKEEPALIVECFG**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERVAL:
          name: '保活间隔'
          type: integer
          minimum: 10
          maximum: 300
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RETRY:
          name: '保活重试'
          type: integer
          minimum: 3
          maximum: 20
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
    - NAME: 'n3if1/1/1'
      AFTYPE: IPV4
      IPV4ADDRESS: '10.1.1.10'
      IPV4MASK: '255.255.255.255'
      VRFNAME: 'VPN_CN'
      SHAREDTYPE: TRUE
    add_twampresponder_list:
    - RESPONDERID: 1
      AFTYPE: IPV4
      TWAMPARCH: FULL
      LOCALIPV4: '10.1.1.10'
      SERVWAIT: 900
      REFWAIT: 900
    set_tcpkeepalivecfg_list:
    - KEEPALIVETIME: 90
      INTERVAL: 30
      RETRY: 9
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

### 3 配置本端探测逻辑接口，UPF与gNodeB之间采用N3/S1-U接口进行探测。

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

### 4 配置TWAMP Full模式响应端。

```jinja2
{%- for item in add_twampresponder_list -%}
    ADD TWAMPRESPONDER:
    {#- --- 必选参数 --- -#}
    RESPONDERID={{item.RESPONDERID}},
    AFTYPE={{item.AFTYPE}},
    TWAMPARCH={{item.TWAMPARCH}},
    LOCALIPV4="{{item.LOCALIPV4}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SERVWAIT is not none -%}
        SERVWAIT={{item.SERVWAIT}},
    {%- endif -%}
    {%- if item.REFWAIT is not none -%}
        REFWAIT={{item.REFWAIT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置TCP保活参数。

```jinja2
{%- for item in set_tcpkeepalivecfg_list -%}
    SET TCPKEEPALIVECFG:
    {#- --- 可选参数 --- -#}
    {%- if item.KEEPALIVETIME is not none -%}
        KEEPALIVETIME={{item.KEEPALIVETIME}},
    {%- endif -%}
    {%- if item.INTERVAL is not none -%}
        INTERVAL={{item.INTERVAL}},
    {%- endif -%}
    {%- if item.RETRY is not none -%}
        RETRY={{item.RETRY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

