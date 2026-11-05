---
id: ''
name: 配置和SEPP对接
ne_type: UNC
type: feature
description: 5G SA国际漫游场景下NRF需要和SEPP对接，通过SEPP集中转发信令。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置NRF","配置和SEPP对接"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
5G SA国际漫游场景下NRF需要和SEPP对接，通过SEPP集中转发信令。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nrfconnplcy_list:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端NF类型'
          type: string
          enum:
          - NRF
          - NF
          required: true
          description: '配置漫游场景下路由模式以及信令汇聚模式。  说明：  * 在不启用TLS场景下，“国际漫游连接策略”配置为SBI\_TARGET\_APIROOT或HTTP\_PROXY无差异。 * 启用TLS场景下“国际漫游连接策略”只能选择SBI\_TARGET\_APIROOT。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONNPOLICY:
          name: '国际漫游连接策略'
          type: string
          enum:
          - DIRECT
          - SBI_TARGET_APIROOT
          - HTTP_PROXY
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nrfconnplcy_list_1:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端NF类型'
          type: string
          enum:
          - NRF
          - NF
          required: true
          description: '配置漫游场景下路由模式以及信令汇聚模式。  说明：  * 在不启用TLS场景下，“国际漫游连接策略”配置为SBI\_TARGET\_APIROOT或HTTP\_PROXY无差异。 * 启用TLS场景下“国际漫游连接策略”只能选择SBI\_TARGET\_APIROOT。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONNPOLICY:
          name: '国际漫游连接策略'
          type: string
          enum:
          - DIRECT
          - SBI_TARGET_APIROOT
          - HTTP_PROXY
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置与SEPP组网对接。 说明：  以SEPP主备容灾组网为例，NRF需要与两套SEPP对接。'
          data_source: '全网规划'
          pattern: ''
          default: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERPLMNFQDN:
          name: 'PLMN间域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 100
        NFDESCNAME:
          name: 'NF描述名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: HTTPS
        IPV4ADDRESS2:
          name: 'IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS3:
          name: 'IPV4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS4:
          name: 'IPV4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPV6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPV6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS3:
          name: 'IPV6地址3'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS4:
          name: 'IPV6地址4'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_seppbindgrp_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置SEPP绑定组关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 2
          maximum: 65
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_plmnbindseppgrp_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          minLength: 1
          maxLength: 3
          required: true
          description: '配置PLMN与SEPP组的绑定关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 1
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 2
          maximum: 65
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_nrfconnplcy_list:
    - PEERNFTYPE: NRF
      CONNPOLICY: HTTP_PROXY
    set_nrfconnplcy_list_1:
    - PEERNFTYPE: NF
      CONNPOLICY: HTTP_PROXY
    add_pnfprofile_list:
    - NFINSTANCEID: 'SEPP_Instance_0'
      NFTYPE: NfSEPP
      NFSTATUS: Registered
      FQDN: 'sepp1.cluster1.net2.nrf.5gc.mnc012.mcc345.3gppnetwork.org'
      INTERPLMNFQDN: 'roaming.sepp1.cluster1.net2.nrf.5gc.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.182'
      PORT: 80
      CAPACITY: 100
      NFDESCNAME: 'Roaming_SEPP_01'
      SCHEME: HTTP
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
    add_seppbindgrp_list:
    - NFINSTANCEID: 'SEPP_Instance_0'
      GROUPID: 2
    add_plmnbindseppgrp_list:
    - MCC: '*'
      MNC: '*'
      GROUPID: 2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 对接跨PLMN的I-NRF的路由模式以及信令汇聚模式策略，用于订阅、Token、服务发现等请求业务。

```jinja2
{%- for item in set_nrfconnplcy_list -%}
    SET NRFCONNPLCY:
    {#- --- 必选参数 --- -#}
    PEERNFTYPE={{item.PEERNFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CONNPOLICY is not none -%}
        CONNPOLICY={{item.CONNPOLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 对接跨PLMN的NF的路由模式以及信令汇聚模式策略，用于订阅通知请求业务。

```jinja2
{%- for item in set_nrfconnplcy_list_1 -%}
    SET NRFCONNPLCY:
    {#- --- 必选参数 --- -#}
    PEERNFTYPE={{item.PEERNFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CONNPOLICY is not none -%}
        CONNPOLICY={{item.CONNPOLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置与SEPP组网对接。

```jinja2
{%- for item in add_pnfprofile_list -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    {%- if item.INTERPLMNFQDN is not none -%}
        INTERPLMNFQDN="{{item.INTERPLMNFQDN}}",
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    {%- if item.NFDESCNAME is not none -%}
        NFDESCNAME="{{item.NFDESCNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
    {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
        {%- if item.SCHEME is not none -%}
            SCHEME={{item.SCHEME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        {%- if item.IPV4ADDRESS3 is not none -%}
            IPV4ADDRESS3="{{item.IPV4ADDRESS3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        {%- if item.IPV4ADDRESS4 is not none -%}
            IPV4ADDRESS4="{{item.IPV4ADDRESS4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
        {%- if item.IPV6ADDRESS3 is not none -%}
            IPV6ADDRESS3="{{item.IPV6ADDRESS3}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
        {%- if item.IPV6ADDRESS4 is not none -%}
            IPV6ADDRESS4="{{item.IPV6ADDRESS4}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
    {%- if (item.NFTYPE == 'NfUPF') -%}
        FQDN="{{item.FQDN}}",
    {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
        {%- if item.FQDN is not none -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_seppbindgrp_list -%}
    ADD SEPPBINDGRP:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    GROUPID={{item.GROUPID}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_plmnbindseppgrp_list -%}
    ADD PLMNBINDSEPPGRP:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    GROUPID={{item.GROUPID}},
    ;
{%- endfor -%}
```

