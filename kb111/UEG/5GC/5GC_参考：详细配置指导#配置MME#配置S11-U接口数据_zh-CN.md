---
id: ''
name: 配置S11-U接口数据
ne_type: UEG
type: feature
description: 当运营商在部署NBIoT分组交换网，新增MME或SGW-U时，在配置完成MME到SGW-U的路由数据后，可通过配置S11-U接口数据建立MME到SGW-U的逻辑连接。  S11-U接口是MME与S-GW/SGW-U间的用户面接口，用于传递MME与S-GW/SGW-U间的上下行用户面数据，实现物联网业务。  S11-U接口协议栈如图1所示。  **图1** S11-U接口协议栈  GTP-U（GPRS Tunnelling Protocol for the user plane）：利用隧道协议在骨干网的GSN间传输用户数据，使用隧道协议传输数据，屏蔽上层协议影响，同时提供会话级的双向快速传输通道。GTP协议用户面除数据包外，还包括数据传输出错指示、Echo消息、支持的扩展头列表等用户面传输辅助信令。GTP-U版本为GTPv1。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置MME","配置S11-U接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署NBIoT分组交换网，新增MME或SGW-U时，在配置完成MME到SGW-U的路由数据后，可通过配置S11-U接口数据建立MME到SGW-U的逻辑连接。S11-U接口是MME与S-GW/SGW-U间的用户面接口，用于传递MME与S-GW/SGW-U间的上下行用户面数据，实现物联网业务。S11-U接口协议栈如图1所示。**图1** S11-U接口协议栈GTP-U（GPRS Tunnelling Protocol for the user plane）：利用隧道协议在骨干网的GSN间传输用户数据，使用隧道协议传输数据，屏蔽上层协议影响，同时提供会话级的双向快速传输通道。GTP协议用户面除数据包外，还包括数据传输出错指示、Echo消息、支持的扩展头列表等用户面传输辅助信令。GTP-U版本为GTPv1。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 已完成组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 如需在UE在4G网络附着选择合一SGW-C/PGW-C，则需要开通“S-GW/P-GW 拓扑选择”特性，即加载对应的License项“82205919 LKV2SELGW03 S-GW/P-GW 拓扑选择”。
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
          description: '配置业务IP参数。  S11-U和S11-C的VPN实例相同。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpule_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置本端的S11接口的GTP-U IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
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
    add_gtpule_list_2:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置本端的S11接口的GTP-U IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
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
    add_gtpuintfattr_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_NOID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTFTP1:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - Iu
          - S11
          - S4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.20'
      VPNINSTNAME: 'VRF_CN'
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.21'
      VPNINSTNAME: 'VRF_CN'
    add_gtpule_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.20'
      VPNNAME: 'VRF_CN'
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.21'
      VPNNAME: 'VRF_CN'
    add_gtpule_list_2:
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.20'
      VPNNAME: 'VRF_CN'
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.21'
      VPNNAME: 'VRF_IOT_CN'
    add_gtpuintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP1: S11
      GRPID: 3
    - SUBRANGE: ALL_USER
      INTFTP1: S11
      GRPID: 3
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **可选：**在NBIoT场景下，配置S11-U接口，用于MME与SGW-U传输用户面数据。

#### 2.1 配置S11-U接口业务IP。

##### 2.1.1 //DC1

```jinja2
{%- if is_optional_configure_s11u_interface -%}
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
{%- endif -%}
```

#### 2.2 配置GTP数据。

##### 2.2.1 配置S11-U接口与其他接口共部署时，GTPU本端实体对应的组号配置为0。

##### 配置MME在S11-U接口的GTP-U IP。

###### 2.2.1.1 //DC1

```jinja2
{%- if is_optional_configure_s11u_interface and is_scenario_co_deploy -%}
    {%- for item in add_gtpule_list -%}
        ADD GTPULE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 当需要将S11-U接口与其他接口分离部署时，配置S11-U接口分离。此时将GTPU本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

###### 2.2.2.1 配置MME在S11-U接口的GTP-U IP。

####### 2.2.2.1.1 //DC1

```jinja2
{%- if is_optional_configure_s11u_interface and is_scenario_separate_deploy -%}
    {%- for item in add_gtpule_list_2 -%}
        ADD GTPULE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.2.2 配置GTPU接口属性。

####### 2.2.2.2.1 //DC1

```jinja2
{%- if is_optional_configure_s11u_interface and is_scenario_separate_deploy -%}
    {%- for item in add_gtpuintfattr_list -%}
        ADD GTPUINTFATTR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        GRPID={{item.GRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP1={{item.INTFTP1}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

