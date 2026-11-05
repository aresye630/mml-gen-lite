---
id: ''
name: 配置与PCRF对接数据
ne_type: UNC
type: feature
description: 当部署PCC基本功能，实现通过PCRF为用户指定控制策略，则需要配置UNC到PCRF的互通数据。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109101 PCC基本功能","PCC基本功能（2G/3G/4G，基于Gx接口）","激活PCC基本功能","配置与PCRF对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当部署PCC基本功能，实现通过PCRF为用户指定控制策略，则需要配置UNC到PCRF的互通数据。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 操作员了解UNC各类接口的类型及命名规范，具体内容请参见SGW-C、PGW-C、GGSN。
* 操作员了解UNC与对端网元互通时可以采用的各种组网方式，以及每种组网方式的实现及特点等信息。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
* 需要配置逻辑接口的PBU正常运行，且PBU上无用户存在。当PBU还未启动或正在启动过程中，将无法在该PBU上配置逻辑接口。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '创建VPN实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_concenpoint_list:
      type: items
      properties:
        GXCONCENMODE:
          name: 'Gx集中点模式'
          type: string
          enum:
          - LOCALIP_PEER
          - LOCALPORT
          required: false
          description: 'Diameter应用集中点模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '组级Gx逻辑接口。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD VPNINST**配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 128
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamlocinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C的本端信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: '本端域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRODUCTNAME:
          name: '产品名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: 'PCRF信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    set_pcctimer_list:
      type: items
      properties: {}
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: 'GGSN/PGW-C与pcrf\_1之间构建一条IP链路，pcrf\_1的IP地址为10.11.21.59。GGSN/PGW-C与pcrf\_2之间构建两条IP链路，pcrf\_2上的两个IP地址为10.11.21.60和10.11.21.61。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_diamconngrp_list:
      type: items
      properties:
        CONNGROUPNAME:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '该命令用于指定GGSN/PGW-C与指定PCRF之间建立一组Diameter链路。本端主机名和对端主机名唯一确定了一组Diameter链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6b
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERHOSTNAME:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SELECTMODE:
          name: '链路选择模式'
          type: string
          enum:
          - MASTER_SLAVE
          - ROUND_ROBIN
          - SESSION_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: SESSION_ID
    add_diamconnection_list:
      type: items
      properties:
        DIAMCONNGRP:
          name: 'Diameter链路组名'
          type: string
          maxLength: 31
          required: true
          description: '增加Diameter链路。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCINTERFACE:
          name: '本端接口名'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERADDRTYPE:
          name: '对端地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PEERIPV4ADDR:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LOCALPORT:
          name: '本端端口'
          type: integer
          minimum:
          - 0
          - 13200
          - 16400
          - 19765
          maximum:
          - 0
          - 13263
          - 16463
          - 19784
          required: false
          description: '**SET CONCENPOINT**命令中的“GXCONCENMODE”为“LOCALPORT”时，此处必须配置“本端端口”为非0的有效值；否则不配置“本端端口”或配置为“0”。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        PEERIPV6ADDR:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERSCTPENDPT:
          name: '对端SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REVERSEIP:
          name: 'SCTP建链交换本端IP地址'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_localhostgrp_list:
      type: items
      properties:
        LOCGRPNAME:
          name: 'Diameter本端信息组名称'
          type: string
          maxLength: 63
          required: true
          description: 'Diameter本端主机组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_localhostbind_list:
      type: items
      properties:
        LOCGRPNAME:
          name: 'Diameter本端信息组名'
          type: string
          maxLength: 63
          required: true
          description: '将Diameter本端主机添加到Diameter本端主机组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCHOSTNAME:
          name: 'Diameter本端主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_gxupfgroup_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 32
          required: true
          description: 'Gx UPF组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfbindgxupfgrp_list:
      type: items
      properties:
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 32
          required: true
          description: '将对接的UPF主机名添加到UPF组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          maxLength: 36
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_upfglocgbndgrp_list:
      type: items
      properties:
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: true
          description: '规划多个时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upfgbindlocg_list:
      type: items
      properties:
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: true
          description: '同一PGW-C对接多个PGW-U，不同PGW-U下的用户IP存在相同或重叠时，则同时满足上述2个条件的PGW-U对应的PGW-U组必须绑定不同的Diameter本端主机组。  例如，upf1和upf2满足上述条件，则upf1和upf2对应的Diameter本端主机名必须不同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPFGRPNAME:
          name: 'Gx UPF组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DIAMLOCGRPNAME:
          name: 'Diameter本端信息组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: true
          description: '值越小，优先级越高。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: '基于APN配置PCC本端主机名选择模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCSLCTMODE:
          name: '本端主机名选择模式'
          type: string
          enum:
          - INHERIT
          - LOADSHARING
          - SPECIFIC
          - UPFGRP
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: INHERIT
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCCTEMPLATE:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_pccfunc_list:
      type: items
      properties:
        LOCSLCTMODE:
          name: 'PCC本端主机名选择模式'
          type: string
          enum:
          - LOADSHARING
          - SPECIFIC
          - UPFGRP
          required: false
          description: '基于全局配置PCC本端主机名选择模式。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        UPFGLOCGBNDGNAME:
          name: 'UPF组与Diameter本端主机组的绑定关系组名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCALHOSTNAME:
          name: '本端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nbiotratvalue_list:
      type: items
      properties:
        PCRF:
          name: '和PCRF交互使用的RAT值'
          type: string
          enum:
          - EUTRAN
          - EUTRAN_NB_IOT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCF:
          name: '和PCF交互使用的RAT值'
          type: string
          enum:
          - EUTRAN
          - EUTRAN_NB_IOT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ltemratvalue_list:
      type: items
      properties:
        PCRF:
          name: '和PCRF交互使用的RAT值'
          type: string
          enum:
          - EUTRAN
          - LTE_M
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCF:
          name: '和PCF交互使用的RAT值'
          type: string
          enum:
          - EUTRAN
          - LTE_M
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_gxif'
    set_concenpoint_list:
    - GXCONCENMODE: LOCALPORT
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.8.10.1'
      VPNINSTNAME: 'vpn_gxif'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_logicinf_list:
    - NAME: 'gxif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.8.10.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_gxif'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
    add_diamlocinfo_list:
    - HOSTNAME: 'pgw_1'
      REALMNAME: 'huawei.com'
      PRODUCTNAME: 'unc@huawei.com'
    add_pcrf_list:
    - HOSTNAME: 'pcrf_1'
      REALMNAME: 'example.com'
      VPNINSTANCE: 'vpn_gxif'
      SUPFEANEGOSW: ENABLE
      FEATURELIST: RELEASE8-1&RELEASE9-1&RELEASE10-1
      CARRYSUPFEASW: ENABLE
    set_pcctimer_list:
    - {}
    add_diampeeraddr_list:
    - HOSTNAME: 'pcrf_1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.11.21.59'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_diamconngrp_list:
    - CONNGROUPNAME: 'dconn_pcrf1'
      LOCALHOSTNAME: 'pgw_1'
      APPLICATION: GX
      PEERHOSTNAME: 'pcrf_1'
      SELECTMODE: SESSION_ID
    add_diamconnection_list:
    - DIAMCONNGRP: 'dconn_pcrf1'
      LOCINTERFACE: 'gxif1/0/0'
      PEERADDRTYPE: IPv4
      PEERIPV4ADDR: '10.11.21.59'
      LOCALPORT: 16450
      PEERIPV6ADDR: ''
      PEERPORT: ''
      PEERSCTPENDPT: ''
      REVERSEIP: DISABLE
    add_localhostgrp_list:
    - LOCGRPNAME: 'pgwc_host_group_01'
    add_localhostbind_list:
    - LOCGRPNAME: 'pgwc_host_group_01'
      LOCHOSTNAME: 'pgwc_1'
    add_gxupfgroup_list:
    - UPFGRPNAME: 'upfgrp_01'
    add_upfbindgxupfgrp_list:
    - UPFGRPNAME: 'upfgrp_01'
      UPFINSTANCEID: 'upf_instance_01'
    add_upfglocgbndgrp_list:
    - UPFGLOCGBNDGNAME: 'test'
    add_upfgbindlocg_list:
    - UPFGLOCGBNDGNAME: 'test'
      UPFGRPNAME: 'upfgrp_01'
      DIAMLOCGRPNAME: 'pgwc_host_group_01'
      PRIORITY: 10
    add_pcctemplate_list:
    - PCCTEMPNAME: 'pcctemplate_01'
      LOCSLCTMODE: UPFGRP
      UPFGLOCGBNDGNAME: 'test'
      LOCALHOSTNAME: ''
    set_apnpccfunc_list:
    - APN: 'apn-op'
      PCCTEMPLATE: 'pcctemplate_01'
    set_pccfunc_list:
    - LOCSLCTMODE: UPFGRP
      UPFGLOCGBNDGNAME: 'test'
      LOCALHOSTNAME: ''
    set_nbiotratvalue_list:
    - PCRF: EUTRAN\_NB\_IOT
      PCF: EUTRAN\_NB\_IOT
    set_ltemratvalue_list:
    - PCRF: LTE\_M
      PCF: LTE\_M
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置外联口IP及路由数据，详细请参见组网路由配置。

### 2 进入“MML命令行-UNC”窗口。

### 3 创建一个VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 4 **可选：**配置Gx接口Diameter应用集中点模式。缺省情况下，本端的端口号不可配，使用系统自动分配的端口号。

```jinja2
{%- if is_optional_gx_concentrator_mode -%}
    {%- for item in set_concenpoint_list -%}
        SET CONCENPOINT:
        {#- --- 可选参数 --- -#}
        {%- if item.GXCONCENMODE is not none -%}
            GXCONCENMODE={{item.GXCONCENMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置Gx逻辑接口。

#### 5.1 配置逻辑IP地址。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        LOGICIPV6="{{item.LOGICIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置Gx逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV6', 'IPVER_ALL'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### **ADD LOGICINF**中的“IP地址+VPN实例名称”和**ADD LOGICIP**命令中的“IP地址+VPN实例名称”必须一致。

### 6 配置GGSN/PGW-C的设备标识。

```jinja2
{%- for item in add_diamlocinfo_list -%}
    ADD DIAMLOCINFO:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    PRODUCTNAME="{{item.PRODUCTNAME}}",
    ;
{%- endfor -%}
```

### 7 配置PCRF的信息。

#### 7.1 配置PCRF的设备标识。

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {%- if item.SUPFEANEGOSW is not none -%}
        SUPFEANEGOSW={{item.SUPFEANEGOSW}},
    {%- endif -%}
    {%- if item.FEATURELIST is not none -%}
        FEATURELIST={{item.FEATURELIST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
    {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
        {%- if item.CARRYSUPFEASW is not none -%}
            CARRYSUPFEASW={{item.CARRYSUPFEASW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### PCRF绑定的VPN实例必须和Gx逻辑接口绑定的VPN实例一致。

#### 如果GGSN/PGW-C与PCRF之间在TCP传输模式下采用多Diameter链路组网模式，则需要配置多个PCRF IP地址和端口，并配置链路选择模式“SELECTMODE”。

#### 如果需要与指定PCRF进行Supported Features动态协商，则需要将**ADD PCRF**命令中的“SUPFEANEGOSW”参数设置为“ENABLE”，并选择对应的feature选项，且添加到同一个PCRF Group中的PCRF支持的feature能力必须一致。

#### 根据PCRF的接收能力，通过设置“WAL”参数以限制向PCRF发送的消息数。

#### 7.2 如果supported-features-negotiation功能使能，且需要定时或手工删除本地缓存的对端PCRF能力，需要配置动态协商定时器的时长，缺省使用默认值。

```jinja2
SET PCCTIMER:
;
```

#### 7.3 配置PCRF地址信息。

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置到PCRF的链路组信息。

```jinja2
{%- for item in add_diamconngrp_list -%}
    ADD DIAMCONNGRP:
    {#- --- 必选参数 --- -#}
    CONNGROUPNAME="{{item.CONNGROUPNAME}}",
    LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
    APPLICATION={{item.APPLICATION}},
    PEERHOSTNAME="{{item.PEERHOSTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SELECTMODE is not none -%}
        SELECTMODE={{item.SELECTMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置到PCRF的链路。

```jinja2
{%- for item in add_diamconnection_list -%}
    ADD DIAMCONNECTION:
    {#- --- 必选参数 --- -#}
    DIAMCONNGRP="{{item.DIAMCONNGRP}}",
    LOCINTERFACE="{{item.LOCINTERFACE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERADDRTYPE is not none -%}
        PEERADDRTYPE={{item.PEERADDRTYPE}},
    {%- endif -%}
    {%- if item.LOCALPORT is not none -%}
        LOCALPORT={{item.LOCALPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv4' -%}
        PEERIPV4ADDR="{{item.PEERIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'IPv6' -%}
        PEERIPV6ADDR="{{item.PEERIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：PEERADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.PEERADDRTYPE == 'SCTP' -%}
        PEERSCTPENDPT="{{item.PEERSCTPENDPT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEERADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.PEERADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PEERPORT is not none -%}
            PEERPORT={{item.PEERPORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERADDRTYPE=SCTP 时可选 --- -#}
    {%- if item.PEERADDRTYPE == 'SCTP' -%}
        {%- if item.REVERSEIP is not none -%}
            REVERSEIP={{item.REVERSEIP}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 配置链路时如果不选择地址类型，则表示本端接口与对端主机的全部地址建立链接。

### 当“Gx集中点模式”通过**SET CONCENPOINT**命令选择为“LOCALPORT”时，可使用**ADD DIAMCONNECTION**命令设置本端的端口号。

### **同一PGW-C对接多个PGW-U，且不同PGW-U下的用户IP存在相同时，必须执行步骤 10~步骤 16；IP地址不同时，可不配置步骤 10~步骤 16。**

### 10 配置Diameter本端主机组。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_localhostgrp_list -%}
        ADD LOCALHOSTGRP:
        {#- --- 必选参数 --- -#}
        LOCGRPNAME="{{item.LOCGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 配置Diameter本端主机与Diameter本端主机组的关联关系。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_localhostbind_list -%}
        ADD LOCALHOSTBIND:
        {#- --- 必选参数 --- -#}
        LOCGRPNAME="{{item.LOCGRPNAME}}",
        LOCHOSTNAME="{{item.LOCHOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 12 配置UPF组。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_gxupfgroup_list -%}
        ADD GXUPFGROUP:
        {#- --- 必选参数 --- -#}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 13 添加UPF到UPF组中。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_upfbindgxupfgrp_list -%}
        ADD UPFBINDGXUPFGRP:
        {#- --- 必选参数 --- -#}
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 14 配置UPF组与Diameter本端主机组的绑定关系组。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_upfglocgbndgrp_list -%}
        ADD UPFGLOCGBNDGRP:
        {#- --- 必选参数 --- -#}
        UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 15 配置UPF组与Diameter本端主机组的绑定关系。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_upfgbindlocg_list -%}
        ADD UPFGBINDLOCG:
        {#- --- 必选参数 --- -#}
        UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        UPFGRPNAME="{{item.UPFGRPNAME}}",
        DIAMLOCGRPNAME="{{item.DIAMLOCGRPNAME}}",
        PRIORITY={{item.PRIORITY}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 16 设置PCC本端主机名选择模式。

#### 16.1 基于APN设置PCC本端主机名选择模式。

##### 16.1.1 增加PCC模板。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in add_pcctemplate_list -%}
        ADD PCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        PCCTEMPNAME="{{item.PCCTEMPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.LOCSLCTMODE is not none -%}
            LOCSLCTMODE={{item.LOCSLCTMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOCSLCTMODE=UPFGRP 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'UPFGRP' -%}
            UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        {%- endif -%}
        {#- --- 条件必选：LOCSLCTMODE=SPECIFIC 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'SPECIFIC' -%}
            LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 16.1.2 将PCC模板与APN绑定。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in set_apnpccfunc_list -%}
        SET APNPCCFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PCCTEMPLATE is not none -%}
            PCCTEMPLATE="{{item.PCCTEMPLATE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 16.2 基于全局设置PCC本端主机名选择方式。

```jinja2
{%- if is_scenario_user_ip_overlap -%}
    {%- for item in set_pccfunc_list -%}
        SET PCCFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.LOCSLCTMODE is not none -%}
            LOCSLCTMODE={{item.LOCSLCTMODE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：LOCSLCTMODE=SPECIFIC 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'SPECIFIC' -%}
            LOCALHOSTNAME="{{item.LOCALHOSTNAME}}",
        {%- endif -%}
        {#- --- 条件必选：LOCSLCTMODE=UPFGRP 时必选 --- -#}
        {%- if item.LOCSLCTMODE == 'UPFGRP' -%}
            UPFGLOCGBNDGNAME="{{item.UPFGLOCGBNDGNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 17 **可选：**NB-IoT用户接入场景，设置PGW-C向PCRF/PCF发送消息时的RAT信元值。

```jinja2
{%- if is_optional_nb_iot_rat_value -%}
    {%- for item in set_nbiotratvalue_list -%}
        SET NBIOTRATVALUE:
        {#- --- 可选参数 --- -#}
        {%- if item.PCRF is not none -%}
            PCRF={{item.PCRF}},
        {%- endif -%}
        {%- if item.PCF is not none -%}
            PCF={{item.PCF}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 对接PCRF/PCF支持**EUTRAN-NB-IoT**类型时，“PCRF”/“PCF”设置为“EUTRAN\_NB\_IOT”，PGW-C向PCRF/PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN-NB-IOT”。系统初始值为“EUTRAN\_NB\_IOT”。

### 对接PCRF/PCF不支持**EUTRAN-NB-IoT**类型时，“PCRF”/“PCF”设置为“EUTRAN”，PGW-C向PCRF/PCF发送NB-IoT用户的相关消息时，RAT信元值为“EUTRAN”。“PCRF”设置为“EUTRAN”时，还需要开启PCRF免升级License，详细操作请参见激活PCRF免升级。

### 18 **可选：**LTE-M用户接入场景，设置PGW-C向PCRF/PCF发送消息时的RAT信元值。

```jinja2
{%- if is_optional_lte_m_rat_value -%}
    {%- for item in set_ltemratvalue_list -%}
        SET LTEMRATVALUE:
        {#- --- 可选参数 --- -#}
        {%- if item.PCRF is not none -%}
            PCRF={{item.PCRF}},
        {%- endif -%}
        {%- if item.PCF is not none -%}
            PCF={{item.PCF}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 对接PCRF/PCF支持**LTE-M**类型时，“PCRF”/“PCF”设置为“LTE\_M”，PGW-C向PCRF/PCF发送LTE-M用户的相关消息时，RAT信元值为“LTE-M”。系统初始值为“LTE\_M”。

### 对接PCRF/PCF不支持**LTE-M**类型时，“PCRF”/“PCF”设置为“EUTRAN”，PGW-C向PCRF/PCF发送LTE-M用户的相关消息时，RAT信元值为“EUTRAN”。

