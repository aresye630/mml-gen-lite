---
id: ''
name: 配置S1-MME接口数据
ne_type: UEG
type: feature
description: 当运营商在部署分组交换网，新增eNodeB或MME时，在配置完成MME到eNodeB的路由数据后，可通过配置S1-MME接口数据建立MME到eNodeB的逻辑连接。  S1-MME接口是eNodeB和MME之间的控制面接口，S1-MME接口的信令连接功能为无线网络信令提供可靠的传输。  **图1** S1-MME接口协议栈    * S1-AP (S1 Application Protocol)：eNodeB与MME之间的应用层协议。 * SCTP：此协议用于保证eNodeB与MME之间的信令消息传送。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。  建议在eNodeB和Router之间部署外置IPsec网关。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置MME","配置S1-MME接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增eNodeB或MME时，在配置完成MME到eNodeB的路由数据后，可通过配置S1-MME接口数据建立MME到eNodeB的逻辑连接。S1-MME接口是eNodeB和MME之间的控制面接口，S1-MME接口的信令连接功能为无线网络信令提供可靠的传输。**图1** S1-MME接口协议栈  * S1-AP (S1 Application Protocol)：eNodeB与MME之间的应用层协议。* SCTP：此协议用于保证eNodeB与MME之间的信令消息传送。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。建议在eNodeB和Router之间部署外置IPsec网关。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成组网路由配置。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置S1-MME接口的业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '由于S1-MME接口传输层的SCTP协议支持多连接，且同一连接也存在多路径，可以配置多个业务IP地址支持多条链路，此处以两个业务IP地址为例。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'UEG风筝形态对外接口组网时，需运营商统一规划IP，VPN。'
          data_source: ''
          pattern: ''
          default: ''
    add_cpsctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '* 用于配置SCTP协议参数。 * S1–MME接口的SCTP协议参数与S6a接口的SCTP协议参数分开配置，便于后续局点搬迁或扩容时，不影响互联网元配置。可以通过****LST SCTPPARA****来查询已存在的SCTP协议参数记录。'
          data_source: ''
          pattern: ''
          default: ''
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_s1aple_list:
      type: items
      properties:
        LLEINDEX:
          name: '链路本地实体号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '* 用于S1AP链路数据。 * 在S1–MME接口配置中，MME固定作为SCTP协议的Server端，所以MME只需配置S1AP本端信息，无需配置对端eNodeB的相关信息。eNodeB侧会配置MME的IP地址和端口号，系统起来后eNodeB会发起S1 setup流程建立S1口连接。 * MME支持S1-MME接口采用的SCTP端口号可配置。'
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TPTADDR_TYPE_IPV4
        LOCALIPV4_1:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV4_2:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CROSSIPFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SCTPINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LLNAME:
          name: '链路本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 36412
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.254.140.15'
      VPNINSTNAME: 'VPN_Access'
    - IPVERSION: IPv4
      SERVICEIPV4: '10.254.140.17'
      VPNINSTNAME: 'VPN_Access'
    add_cpsctppara_list:
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'For_S1AP'
    - SCTPPARAINDEX: 1
      SCTPPARANAME: 'For_S1AP'
    add_s1aple_list:
    - LLEINDEX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.254.140.15'
      LOCALIPV4_2: '10.254.140.16'
      CROSSIPFLAG: NO
      SCTPINDEX: 1
      LLNAME: 'To-eNodeB'
      VPNNAME: 'VPN_Access'
      LOCALPORT: 36412
    - LLEINDEX: 1
      IPTYPE: TPTADDR_TYPE_IPV4
      LOCALIPV4_1: '10.254.140.17'
      LOCALIPV4_2: '10.254.140.18'
      CROSSIPFLAG: NO
      SCTPINDEX: 1
      LLNAME: 'To-eNodeB'
      VPNNAME: 'VPN_Access'
      LOCALPORT: 36412
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置S1-MME接口的业务IP。

#### 2.1 //DC1

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SCTP参数。

#### 3.1 //DC1

```jinja2
{%- for item in add_cpsctppara_list -%}
    ADD CPSCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加S1AP链路本地实体，其中LOCALIPV4\_1为S1-MME接口的业务IP。

#### 4.1 //DC1

```jinja2
{%- for item in add_s1aple_list -%}
    ADD S1APLE:
    {#- --- 必选参数 --- -#}
    LLEINDEX={{item.LLEINDEX}},
    SCTPINDEX={{item.SCTPINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.CROSSIPFLAG is not none -%}
        CROSSIPFLAG={{item.CROSSIPFLAG}},
    {%- endif -%}
    {%- if item.LLNAME is not none -%}
        LLNAME="{{item.LLNAME}}",
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        LOCALIPV4_1="{{item.LOCALIPV4_1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPTYPE=TPTADDR_TYPE_IPV4 时可选 --- -#}
    {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
        {%- if item.LOCALIPV4_2 is not none -%}
            LOCALIPV4_2="{{item.LOCALIPV4_2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

