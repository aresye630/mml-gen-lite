---
id: ''
name: 配置S11-C接口数据
ne_type: UEG
type: feature
description: 当运营商在部署分组交换网，新增SGW-C或MME时，在配置完成MME到SGW-C的路由数据后，可通过配置S11接口数据建立MME到SGW-C的逻辑连接。  S11-C接口是MME与S-GW/SGW-C间的信令面接口，主要用于MME和S-GW/SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于S-GW/SGW-C通知MME寻呼UE，恢复S1承载。  S11-C接口协议栈如图1所示。  **图1** S11-C接口协议栈  GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。GTP-C版本为GTPv2。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。  双DC组网场景下，MME不仅需要和本DC内的SGW-C对接，也需要和另外一个DC的SGW-C对接。这样当用户业务接入时，MME会以负荷分担的方式选择其中一个DC的SGW-C进行业务，当其中一个DC故障时，另一个DC的SGW-C会承担园区内所有用户的业务。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置MME","配置S11-C接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增SGW-C或MME时，在配置完成MME到SGW-C的路由数据后，可通过配置S11接口数据建立MME到SGW-C的逻辑连接。S11-C接口是MME与S-GW/SGW-C间的信令面接口，主要用于MME和S-GW/SGW-C之间传递承载创建、更新及删除请求消息，以及UE处于ECM-IDLE态时，用于S-GW/SGW-C通知MME寻呼UE，恢复S1承载。S11-C接口协议栈如图1所示。**图1** S11-C接口协议栈GTP-C（GPRS Tunnelling Protocol for the control plane）：利用隧道协议在骨干网的GSN间传输信令。主要信令包括路径管理、隧道管理、移动管理、位置管理，实现骨干网通道维护、会话建立/修改/删除、用户信息交互。GTP-C版本为GTPv2。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。双DC组网场景下，MME不仅需要和本DC内的SGW-C对接，也需要和另外一个DC的SGW-C对接。这样当用户业务接入时，MME会以负荷分担的方式选择其中一个DC的SGW-C进行业务，当其中一个DC故障时，另一个DC的SGW-C会承担园区内所有用户的业务。

## 必备事项
前提条件

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
          description: '配置业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置本端的S11-C接口的GTP-C IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。'
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
    set_ugtp_list:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list_2:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置本端的S11-C接口的GTP-C IP。  GTP数据绑定的VPN实例与上面业务IP绑定的VPN实例相同。'
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
    set_ugtp_list_2:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcintfattr_list:
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
        INTFTP:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - S10
          - S11
          - S3
          - S4
          - SV
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '* 配置SGW-C的Hostfile数据，用于Attach/TAU/Handover流程中，根据TAI选择SGW-C。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '主机地址段号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: '全称标准规范的域名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    set_smfunc_list:
      type: items
      properties:
        TOPSELCFG:
          name: '拓扑选择开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置就近选择合一SGW-C/PGW-C策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gwselplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          - MSISDN_PREFIX
          - SPECIFIC_IMSI
          - SPECIFIC_MSISDN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLCTM:
          name: '选择方法'
          type: string
          enum:
          - CUSTOMIZE_APN-OI_REPLACEMENT
          - GGSN/P-GW_HSNAME
          - GGSN/P-GW_IP
          - STANDARD_SELECTION_MODE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD_SELECTION_MODE
        SELPLCY:
          name: '选择策略'
          type: string
          enum:
          - PGWFIRST
          - SGWFIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SGWFIRST
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.17'
      VPNINSTNAME: 'VPN_CN'
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.18'
      VPNINSTNAME: 'VPN_CN'
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.18'
      VPNNAME: 'VPN_CN'
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcle_list_2:
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.18'
      VPNNAME: 'VPN_CN'
    set_ugtp_list_2:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP: S11
      GRPID: 3
    - SUBRANGE: ALL_USER
      INTFTP: S11
      GRPID: 3
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'topon.eth1.gw32.nodes'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.2.215.26'
    - HSINDEX: 1
      HOSTNAME: 'topon.eth1.gw32.nodes'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.2.215.26'
    add_dnsn_list:
    - FQDN: 'TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: SGW
      INTYPE: S11
      PRIORITY: 10
      WEIGHT: 104
    - FQDN: 'TAC-LB01.TAC-HB11.TAC.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 1
      ENTITY: SGW
      INTYPE: S11
      PRIORITY: 10
      WEIGHT: 104
    set_smfunc_list:
    - TOPSELCFG: YES
    - TOPSELCFG: YES
    add_gwselplcy_list:
    - SUBRANGE: ALL_USER
      APNNI: 'huawei1.com'
      SLCTM: STANDARD_SELECTION_MODE
      SELPLCY: PGWFIRST
    - SUBRANGE: ALL_USER
      APNNI: 'huawei1.com'
      SLCTM: STANDARD_SELECTION_MODE
      SELPLCY: PGWFIRST
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置S11-C接口业务IP。

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

### 3 配置GTP数据。

#### 3.1 配置S11-C接口与其他GTPC接口共部署时，GTP-C本端实体对应的组号配置为0。

##### 3.1.1 配置MME在S11-C接口的GTP-C IP。

###### 3.1.1.1 //DC1

```jinja2
{%- if is_scenario_co_deploy -%}
    {%- for item in add_gtpcle_list -%}
        ADD GTPCLE:
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

##### 3.1.2 配置GTP路径管理参数。

###### 3.1.2.1 //DC1

```jinja2
{%- if is_scenario_co_deploy -%}
    {%- for item in set_ugtp_list -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要将S11-C接口与其他GTPC接口分离部署时，配置S11接口分离。此时将GTP-C本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 配置MME在S11-C接口的GTP-C IP。

###### 3.2.1.1 //DC1

```jinja2
{%- if is_scenario_separate_deploy -%}
    {%- for item in add_gtpcle_list_2 -%}
        ADD GTPCLE:
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

##### 3.2.2 配置GTP-C路径管理参数。

###### 3.2.2.1 //DC1

```jinja2
{%- if is_scenario_separate_deploy -%}
    {%- for item in set_ugtp_list_2 -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置GTP-C接口属性。

###### 3.2.3.1 //DC1

```jinja2
{%- if is_scenario_separate_deploy -%}
    {%- for item in add_gtpcintfattr_list -%}
        ADD GTPCINTFATTR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        GRPID={{item.GRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP={{item.INTFTP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置SGW-C解析数据。

#### 4.1 //DC1

```jinja2
{%- if is_optional_sgw_c_dns_data -%}
    {%- for item in add_ipv4dnsh_list -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_sgw_c_dns_data -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置就近选择合一SGW-C/PGW-C策略。

#### 5.1 //DC1

```jinja2
{%- for item in set_smfunc_list -%}
    SET SMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.TOPSELCFG is not none -%}
        TOPSELCFG={{item.TOPSELCFG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gwselplcy_list -%}
    ADD GWSELPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNNI="{{item.APNNI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SLCTM is not none -%}
        SLCTM={{item.SLCTM}},
    {%- endif -%}
    {%- if item.SELPLCY is not none -%}
        SELPLCY={{item.SELPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

