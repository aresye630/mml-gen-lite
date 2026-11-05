---
id: ''
name: 激活支持NTP功能
ne_type: UNC
type: feature
description: 网元直连NTP服务器或者OMC同步时间信息场景，请参考本章节配置NTP服务器的地址和相关参数。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","运维功能","NPFD-010014 支持NTP功能","激活支持NTP功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网元直连NTP服务器或者OMC同步时间信息场景，请参考本章节配置NTP服务器的地址和相关参数。

## 必备事项
前提条件

* 请仔细阅读NPFD-010014 支持NTP功能。
* FusionStage和OMC已完成NTP相关配置，详细操作请参考对应产品文档。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ntpsvr_list:
      type: items
      properties:
        SVRNAME:
          name: 'NTP服务器名'
          type: string
          maxLength: 32
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        IPADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCOLVERSION:
          name: 'NTP协议版本'
          type: string
          enum:
          - NTPV4
          - NTPV3
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: NTPV4
        AUTHFLAG:
          name: '身份验证标志'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        KEYID:
          name: '身份验证密钥号'
          type: integer
          minimum: 1
          maximum: 65533
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SHASTRING:
          name: '密钥类型'
          type: string
          enum:
          - SHA256
          - SHA1
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: SHA256
        KEYSTRING:
          name: '密钥串'
          type: string
          minLength: 40
          maxLength: 128
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESS6:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ntpsvr_list:
    - SVRNAME: 'server3'
      IPTYPE: IPV4
      IPADDRESS: '192.168.156.12'
      PROTOCOLVERSION: NTPV4
      AUTHFLAG: YES
      KEYID: 32323
      SHASTRING: SHA256
      KEYSTRING: '*****'
      IPADDRESS6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在WebPortal上执行MML命令：**ADD NTPSVR**

#### 1.1 //配置NTP服务器地址和相关参数。

```jinja2
{%- for item in add_ntpsvr_list -%}
    ADD NTPSVR:
    {#- --- 必选参数 --- -#}
    SVRNAME="{{item.SVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    PROTOCOLVERSION={{item.PROTOCOLVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPADDRESS="{{item.IPADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLVERSION=NTPV4 时必选 --- -#}
    {%- if item.PROTOCOLVERSION == 'NTPV4' -%}
        AUTHFLAG={{item.AUTHFLAG}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        KEYID={{item.KEYID}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        SHASTRING={{item.SHASTRING}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        KEYSTRING="{{item.KEYSTRING}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPADDRESS6="{{item.IPADDRESS6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

