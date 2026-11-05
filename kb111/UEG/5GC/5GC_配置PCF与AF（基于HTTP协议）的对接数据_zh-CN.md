---
id: ''
name: 配置PCF与AF（基于HTTP协议）的对接数据
ne_type: UEG
type: feature
description: 当PCF接纳应用层业务请求时，例如应用服务器发起的带宽资源预留请求，PCF需要对接AF（Application Function）实体，以实现应用侧发起的策略控制功能。  * 园区PCF支持PTT业务，且PCF与PTT Server之间通过Rx接口对接时，请参考配置PCF与AF（基于Diameter协议）的对接数据进行配置。 * 园区PCF支持PTT业务，且PCF与PTT Server之间通过N5接口对接时，请参考本页面进行配置。  园区PCF不支持与NRF通信，因此需要手动配置PCF和AF（PTT Server）之间的服务发现。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置PCF/PCRF","配置PCF与AF（基于HTTP协议）的对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当PCF接纳应用层业务请求时，例如应用服务器发起的带宽资源预留请求，PCF需要对接AF（Application Function）实体，以实现应用侧发起的策略控制功能。* 园区PCF支持PTT业务，且PCF与PTT Server之间通过Rx接口对接时，请参考配置PCF与AF（基于Diameter协议）的对接数据进行配置。* 园区PCF支持PTT业务，且PCF与PTT Server之间通过N5接口对接时，请参考本页面进行配置。园区PCF不支持与NRF通信，因此需要手动配置PCF和AF（PTT Server）之间的服务发现。

## 必备事项
前提条件

本端及AF侧已完成基础数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_discnfprofile_list:
      type: items
      properties:
        NFINSNAME:
          name: '网元实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '用于标识一个服务发现网元实例的名称，该参数全局唯一，不能重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: '用于标识服务发现网元实例在系统中的序号，该参数为UUIDv4格式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: '网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          - PCF
          - UDR
          - AMF
          - SMF
          - NEF
          - AF
          - SMSF
          - BSF
          - CHF
          - SCP
          - NWDAF
          required: true
          description: '用于标识该服务发现网元实例的类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NFPROFILE:
          name: '网元实例信息'
          type: string
          minLength: 0
          maxLength: 8000
          required: true
          description: '用于标识服务发现网元实例的详细信息，该参数为JSON格式。   * "nfInstanceId"值与“NFINSID”取值一致。 * "ipv4Addresses"是AF的服务化接口IP（服务端地址）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_discnfprofile_list:
    - NFINSNAME: 'AF01'
      NFINSID: '4946a69a-f6b8-4bc1-b9da-47c9c5d148fd'
      NFTYPE: AF
      NFPROFILE: '{\"nfInstanceId\":\"4946a69a-f6b8-4bc1-b9da-47c9c5d148fd\",\"nfType\":\"AF\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"172.16.1.50\"]}'
    - NFINSNAME: 'AF02'
      NFINSID: '4946a69a-f6b8-4bc1-b9da-47c9c5d148fe'
      NFTYPE: AF
      NFPROFILE: '{\"nfInstanceId\":\"4946a69a-f6b8-4bc1-b9da-47c9c5d148fe\",\"nfType\":\"AF\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"172.17.1.50\"]}'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 增加AF服务发现网元实例信息。

#### 2.2 //AF01:

```jinja2
{%- for item in add_discnfprofile_list -%}
    ADD DISCNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSNAME="{{item.NFINSNAME}}",
    NFINSID="{{item.NFINSID}}",
    NFTYPE={{item.NFTYPE}},
    NFPROFILE="{{item.NFPROFILE}}",
    ;
{%- endfor -%}
```

#### 2.3 园区PCF无法与NRF通信，需要手动配置PCF与AF的服务发现。

