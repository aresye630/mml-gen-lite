---
id: ''
name: 配置S11-C/S5-C接口数据
ne_type: UEG
type: feature
description: '**接口介绍**  * S11接口    S11接口是MME与SGW-C间的信令面接口，主要用于MME和SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于SGW-C通知MME寻呼UE，恢复S1承载。S11接口协议栈如图1所示。    **图1** S11接口协议栈 * S5接口    S5接口可以作为SGW-C与PGW-C间的信令面接口，主要用于传递承载创建、更新及删除消息。对应的信令面接口协议栈如图2、图3所示。    **图2** PGW-C与S-GW/SGW-C间基于GTPv2协议的S5信令面接口协议栈    **图3** SGW-C与PGW-C间基于GTPv2协议的S5信令面接口协议栈  S11接口和S5接口都是基于GTP-C协议，采用GTPv2协议。  GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。  园区双DC组网场景下，对于S11-C接口，SGW-C需要和本DC以及对端DC内的MME全互联对接。对于S5-C接口，由于SGW-C和PGW-C的微服务是融合的，因此仅需要在本DC内互通即可，不做跨DC的全互联。  **配置建议**  * S11-C接口与S5-C接口不共用业务IP地址。'
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置SMF/SGW-C/PGW-C","配置S11-C/S5-C接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**接口介绍*** S11接口  S11接口是MME与SGW-C间的信令面接口，主要用于MME和SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于SGW-C通知MME寻呼UE，恢复S1承载。S11接口协议栈如图1所示。  **图1** S11接口协议栈* S5接口  S5接口可以作为SGW-C与PGW-C间的信令面接口，主要用于传递承载创建、更新及删除消息。对应的信令面接口协议栈如图2、图3所示。  **图2** PGW-C与S-GW/SGW-C间基于GTPv2协议的S5信令面接口协议栈  **图3** SGW-C与PGW-C间基于GTPv2协议的S5信令面接口协议栈S11接口和S5接口都是基于GTP-C协议，采用GTPv2协议。GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。园区双DC组网场景下，对于S11-C接口，SGW-C需要和本DC以及对端DC内的MME全互联对接。对于S5-C接口，由于SGW-C和PGW-C的微服务是融合的，因此仅需要在本DC内互通即可，不做跨DC的全互联。**配置建议*** S11-C接口与S5-C接口不共用业务IP地址。

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
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置S11-C/S5-C接口数据。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '分别规划配置S11-C、S5-S-C、S5-P-C的接口。  S11-C接口与S5-C接口不共用业务IP地址。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    add_gtpclegrp_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gtpclegrpmem_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPN:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gtpcintf_list:
      type: items
      properties:
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - E_GTPCINTF_ITFS11
          - E_GTPCINTF_ITFN26
          - E_GTPCINTF_ITFS5_S
          - E_GTPCINTF_ITFS8_S
          - S5_P_OR_GN
          - S8_P_OR_GP
          - PROXY_SGSN_GP
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.215.26'
      VPNINSTNAME: 'VPN_CN'
      DESC: 's11'
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.215.27'
      VPNINSTNAME: 'VPN_CN'
      DESC: 's11'
    add_gtpclegrp_list:
    - GROUPID: 0
      DESC: 's11'
    - GROUPID: 0
      DESC: 's11'
    add_gtpclegrpmem_list:
    - GROUPID: 0
      IPTYPE: IPv4
      IPV4ADDR: '10.2.215.26'
      VPN: 'VPN_CN'
      DESC: 's11'
    - GROUPID: 0
      IPTYPE: IPv4
      IPV4ADDR: '10.2.215.27'
      VPN: 'VPN_CN'
      DESC: 's11'
    add_gtpcintf_list:
    - INTFTYPE: E_GTPCINTF_ITFS11
      GROUPID: 0
    - INTFTYPE: E_GTPCINTF_ITFS11
      GROUPID: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置S11-C/S5-C接口的逻辑IP地址。

#### 2.1 //DC1

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置S11-C/S5-C接口的GTP-C本地实体组和实体组成员信息。

#### 3.1 //DC1

```jinja2
{%- for item in add_gtpclegrp_list -%}
    ADD GTPCLEGRP:
    {#- --- 必选参数 --- -#}
    GROUPID={{item.GROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gtpclegrpmem_list -%}
    ADD GTPCLEGRPMEM:
    {#- --- 必选参数 --- -#}
    GROUPID={{item.GROUPID}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPN is not none -%}
        VPN="{{item.VPN}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置S11-C/S5-C接口信息。

#### 4.1 //DC1

```jinja2
{%- for item in add_gtpcintf_list -%}
    ADD GTPCINTF:
    {#- --- 必选参数 --- -#}
    INTFTYPE={{item.INTFTYPE}},
    GROUPID={{item.GROUPID}},
    ;
{%- endfor -%}
```

