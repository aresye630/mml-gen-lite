---
id: ''
name: 配置HTTP信令数据
ne_type: UEG
type: feature
description: 接入5G SA用户时，HTTP信令数据用于UDM和AMF/SMF对接。  园区UDM不支持与NRF通信，因此需要手动配置UDM和AMF之间的服务发现。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置UDM/HSS","配置HTTP信令数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
接入5G SA用户时，HTTP信令数据用于UDM和AMF/SMF对接。园区UDM不支持与NRF通信，因此需要手动配置UDM和AMF之间的服务发现。

## 必备事项
前提条件

* 已完成配置UDM基础数据。
* UDM和AMF之间外联口通信正常。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_udmdiscnfprof_list:
      type: items
      properties:
        NFINSNAME:
          name: '网元实例名称'
          type: string
          minLength: 0
          maxLength: 32
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
          - UDR
          - AMF
          - SCP
          - SEPP
          - SMF
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
          description: '用于标识服务发现网元实例的详细信息，该参数为JSON格式。   * "nfInstanceId"值与“NFINSID”取值一致。 * "ipv4Addresses"是AMF的服务化接口IP（服务端地址）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_udmdiscnfprof_list_1:
      type: items
      properties:
        NFINSNAME:
          name: '网元实例名称'
          type: string
          minLength: 0
          maxLength: 32
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
          - UDR
          - AMF
          - SCP
          - SEPP
          - SMF
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
          description: '用于标识服务发现网元实例的详细信息，该参数为JSON格式。   * "nfInstanceId"值与“NFINSID”取值一致。 * "ipv4Addresses"是AMF的服务化接口IP（服务端地址）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_udmdiscnfprof_list:
    - NFINSNAME: 'AMF01'
      NFINSID: '4947a69a-f6b8-4bc1-b9da-47c9c5d148fd'
      NFTYPE: AMF
      NFPROFILE: '{\"nfInstanceId\":\"4947a69a-f6b8-4bc1-b9da-47c9c5d148fd\",\"nfType\":\"AMF\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"172.16.1.5\"]}'
    add_udmdiscnfprof_list_1:
    - NFINSNAME: 'AMF02'
      NFINSID: '4947a69a-f6b8-4bc1-b9da-47c9c5d148fe'
      NFTYPE: AMF
      NFPROFILE: '{\"nfInstanceId\":\"4947a69a-f6b8-4bc1-b9da-47c9c5d148fe\",\"nfType\":\"AMF\",\"nfStatus\":\"REGISTERED\",\"ipv4Addresses\":[\"172.17.1.5\"]}'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 增加AMF服务发现网元实例信息。

#### 2.1 //DC1：

##### 2.1.1 //AMF01:

```jinja2
{%- for item in add_udmdiscnfprof_list -%}
    ADD UDMDISCNFPROF:
    {#- --- 必选参数 --- -#}
    NFINSNAME="{{item.NFINSNAME}}",
    NFINSID="{{item.NFINSID}}",
    NFTYPE={{item.NFTYPE}},
    NFPROFILE="{{item.NFPROFILE}}",
    ;
{%- endfor -%}
```

#### 2.2 //DC2：

##### 2.2.1 //AMF02:

```jinja2
{%- for item in add_udmdiscnfprof_list_1 -%}
    ADD UDMDISCNFPROF:
    {#- --- 必选参数 --- -#}
    NFINSNAME="{{item.NFINSNAME}}",
    NFINSID="{{item.NFINSID}}",
    NFTYPE={{item.NFTYPE}},
    NFPROFILE="{{item.NFPROFILE}}",
    ;
{%- endfor -%}
```

##### UDM无法与NRF通信，需要手动配置UDM与AMF的服务发现。

