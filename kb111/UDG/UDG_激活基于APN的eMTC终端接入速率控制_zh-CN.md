---
id: GWFD-110646
name: 激活基于APN的eMTC终端接入速率控制
ne_type: UDG
type: feature
description: 在UDG上激活基于APN的eMTC终端接入速率控制，用于控制该UE的某PDN连接单位时间内可发送的上行和下行数据包数。  适用于SGW-U、PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","物联网功能","eMTC","GWFD-110646 基于APN的eMTC终端接入速率控制","激活基于APN的eMTC终端接入速率控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上激活基于APN的eMTC终端接入速率控制，用于控制该UE的某PDN连接单位时间内可发送的上行和下行数据包数。适用于SGW-U、PGW-U。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-110646 基于APN的eMTC终端接入速率控制。
* 完成加载License（本特性完整的功能需要同时在用户面和控制面开启License，如果有需求，请联系华为技术支持工程师处理）。
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '控制eMTC终端接入速率控制所使用的APN，需要与控制面规划一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5AMRC01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'apnespd'
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

### 需要同时在控制面上打开本特性开关，并配置CCR消息、APN Rate Control等信息。详情请见UNC相关章节。

### 2 配置基于APN的eMTC终端接入速率控制使用的APN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

