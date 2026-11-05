---
id: ''
name: 配置到NRF信息
ne_type: UNC
type: feature
description: 该任务主要用于NCG向NRF发现OCS等周边NF并订阅后者的状态信息。在对接真实NRF的场景下，需要执行该任务。  NCG信息在SMF本地配置，SMF暂不向NRF查询NCG信息。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案","NCG配置","配置到NRF信息"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务主要用于NCG向NRF发现OCS等周边NF并订阅后者的状态信息。在对接真实NRF的场景下，需要执行该任务。NCG信息在SMF本地配置，SMF暂不向NRF查询NCG信息。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF信息。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '该命令用于添加NRF实例地址信息。在对接真实NRF的场景下，需要配置该命令。'
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfaddr_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '该命令用于添加NRF实例地址信息。在对接真实NRF的场景下，需要配置该命令。'
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - NoneIP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF协议参数。'
          data_source: ''
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
    set_nfnrfmgmtpara_list:
      type: items
      properties:
        SWITCHMASTERNRF:
          name: '切换主用NRF开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该命令用于配置NF与NRF间的管理参数。'
          data_source: ''
          pattern: ''
          default: ''
    add_subcondition_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: '该命令用于增加订阅的目标NF信息。此示例是订阅OCS的状态和信息变更通知。'
          data_source: ''
          pattern: ''
          default: ''
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_agffuncpara_list:
      type: items
      properties:
        OCSRETRYCNT:
          name: '计费消息重发次数'
          type: integer
          minimum: 0
          maximum: 1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OCSDISCPLCY:
          name: 'OCS选择策略'
          type: string
          required: false
          description: '该命令用于设置AGF的功能参数。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.1.15'
      PORT: 8080
      IPV6ADDRESS: 'fd00:f111:2222:3333:4444:5555:2111:151'
    add_nrfaddr_list_2:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.1.16'
      PORT: 8080
      IPV6ADDRESS: 'fd00:f111:2222:3333:4444:5555:2111:152'
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    set_nfnrfmgmtpara_list:
    - SWITCHMASTERNRF: ON
    add_subcondition_list:
    - NFTYPE: NfCUSTOM_OCS
      CONDITION: NfInstanceId-1&NFType-1&ServiceName-1&AmfRegionId-1&AmfSetId-1&GuamiList-1&PlmnId-1&NetworkSlice-1&NfGroup-1&Rev1-1&Rev2-1&Rev3-1
      REQNOTIFEVENT: NF_REGISTERED-1&NF_DEREGISTERED-1&NF_PROFILE_CHANGED-1
    set_agffuncpara_list:
    - OCSRETRYCNT: 0
      OCSDISCPLCY: SUPI-0&GPSI-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置主NRF和备NRF实例。

```jinja2
{%- for item in add_nrf_list -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 执行ADD NRF命令时严禁配置FQDN参数，不支持SBI接口使用FQDN。

### 2 配置主NRF业务地址。

```jinja2
{%- for item in add_nrfaddr_list -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置备NRF业务地址。

```jinja2
{%- for item in add_nrfaddr_list_2 -%}
    ADD NRFADDR:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
    {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置与主NRF和备NRF的对接参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

```jinja2
{%- for item in add_nrfpara_list -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    {%- if item.LOADCARRYINHB is not none -%}
        LOADCARRYINHB={{item.LOADCARRYINHB}},
    {%- endif -%}
    {%- if item.SUBSCRISWITCH is not none -%}
        SUBSCRISWITCH={{item.SUBSCRISWITCH}},
    {%- endif -%}
    {%- if item.OAUTH2SWITCH is not none -%}
        OAUTH2SWITCH={{item.OAUTH2SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 请提前规划**ADD NRFPARA**中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF对NRF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考UNC产品文档中“网络部署 > 特性部署 > UNC特性指南 > 容灾功能 > WSFD-114002 NRF双活容灾 > WSFD-114002 NRF双活容灾特性概述”中原理概述的可靠性机制。

### 5 配置切换主用NRF开关。

```jinja2
{%- for item in set_nfnrfmgmtpara_list -%}
    SET NFNRFMGMTPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCHMASTERNRF is not none -%}
        SWITCHMASTERNRF={{item.SWITCHMASTERNRF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 在NRF主备组网情况下，通过设置“SWITCHMASTERNRF”参数让NF实时感知主用NRF的状态，当主用NRF恢复后，NF切换到主用NRF。

### 6 配置NCG订阅CHF(OCS)等周边NF的状态和信息变更通知。

```jinja2
{%- for item in add_subcondition_list -%}
    ADD SUBCONDITION:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CONDITION is not none -%}
        CONDITION={{item.CONDITION}},
    {%- endif -%}
    {%- if item.REQNOTIFEVENT is not none -%}
        REQNOTIFEVENT={{item.REQNOTIFEVENT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置OCS寻址策略。

### 配置通过GPSI寻址OCS。

```jinja2
{%- for item in set_agffuncpara_list -%}
    SET AGFFUNCPARA:
    {#- --- 必选参数 --- -#}
    OCSRETRYCNT={{item.OCSRETRYCNT}},
    {#- --- 可选参数 --- -#}
    {%- if item.OCSDISCPLCY is not none -%}
        OCSDISCPLCY={{item.OCSDISCPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### “OCSRETRYCNT”取值范围为0~1。值为0时，请求消息超时不进行重传，直接查找备OCS。值为1时，请求消息超时后重传1次，再次超时则查找备OCS。

### 如上所示配置表示通过GPSI寻址OCS。

