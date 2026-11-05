---
id: ''
name: 激活NRF全故障业务逃生
ne_type: UNC
type: feature
description: 本操作指导介绍激活NRF全故障业务逃生的操作过程。  适用于AMF、SMF、NRF、NSSF、SMSF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","运维功能","WSFD-113013 NRF全故障业务逃生(Bypass)","激活NRF全故障业务逃生"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍激活NRF全故障业务逃生的操作过程。适用于AMF、SMF、NRF、NSSF、SMSF。

## 必备事项
前提条件

* 请仔细阅读13.1-WSFD-113013 NRF全故障业务逃生特性概述 。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nfdiscplcy_list:
      type: items
      properties:
        CACHESWITCH:
          name: '缓存开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '该参数用于指定是否开启缓存开关。缓存指的是从NRF中获得的远端NF信息缓存数据。开关设置为ON后，NF进行服务发现流程时可以在缓存中查找目标网元；反之则不会。'
          data_source: '本端规划'
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
          description: '该参数用于指定订阅的目标NF类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: '该参数用于指定订阅的条件类型。'
          data_source: '全网规划'
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
  examples:
    set_nfdiscplcy_list:
    - CACHESWITCH: ON
    add_subcondition_list:
    - NFTYPE: NfAMF
      CONDITION: NfInstanceId-1&NFType-0&ServiceName-0&AmfRegionId-0&AmfSetId-0&GuamiList-0&PlmnId-0&NetworkSlice-0&NfGroup-0&Rev1-0&Rev2-0&Rev3-0
      REQNOTIFEVENT: NF_REGISTERED-1&NF_DEREGISTERED-1&NF_PROFILE_CHANGED-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置缓存开关。

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.CACHESWITCH is not none -%}
        CACHESWITCH={{item.CACHESWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 订阅目标NF。

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

