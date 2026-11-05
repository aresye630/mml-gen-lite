---
id: ''
name: 配置Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U)接口数据
ne_type: UDG
type: feature
description: 运营商在部署2/3/4/5融合组网时新增PSA UPF/PGW-U中的任一独立设备或融合设备，在完成配置UDG到ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG的路由数据后，可在UDG上配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）接口数据使UDG与ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG/SGSN建立逻辑连接。  * 考虑到4G/5G互操作和平滑演进，5GC需要支持4G/5G融合接入和互操作，因此协议规定了三类网元需要原生融合部署。   + 用户数据：HSS+UDM融合，保证用户数据一致性。   + 策略数据：PCRF+PCF融合，保证策略一致性、连续性。   + 会话管理锚点：SMF+PGW-C融合，UPF+PGW-U融合，锚点不变保证数据连续性。从简化网络拓扑，优化转发路径考虑，一般建议EPC侧SGW-C融合到SMF+PGW-C、SGW-U融合到UPF+PGW-U。    因此部署4G/5G互操作的网络时，PSA UPF、PGW-U需要融合部署在同一VNF上。 * 考虑到4G/5G互操作时数据锚点不变，PSA UPF+PGW-U融合部署时N9a、S5-P/S8-P的接口地址必须相同，因此UDG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5-P/S8-P接口。
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","组网对接配置","配置业务接口数据","配置Pa(N9a/S5-P/S8-P/S2b/Gn-U/Gp-U)接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商在部署2/3/4/5融合组网时新增PSA UPF/PGW-U中的任一独立设备或融合设备，在完成配置UDG到ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG的路由数据后，可在UDG上配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）接口数据使UDG与ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG/SGSN建立逻辑连接。* 考虑到4G/5G互操作和平滑演进，5GC需要支持4G/5G融合接入和互操作，因此协议规定了三类网元需要原生融合部署。  + 用户数据：HSS+UDM融合，保证用户数据一致性。  + 策略数据：PCRF+PCF融合，保证策略一致性、连续性。  + 会话管理锚点：SMF+PGW-C融合，UPF+PGW-U融合，锚点不变保证数据连续性。从简化网络拓扑，优化转发路径考虑，一般建议EPC侧SGW-C融合到SMF+PGW-C、SGW-U融合到UPF+PGW-U。  因此部署4G/5G互操作的网络时，PSA UPF、PGW-U需要融合部署在同一VNF上。* 考虑到4G/5G互操作时数据锚点不变，PSA UPF+PGW-U融合部署时N9a、S5-P/S8-P的接口地址必须相同，因此UDG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5-P/S8-P接口。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 请了解UDG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍。
* 请阅读并熟悉特性GWFD-010234 Single IP。
* 已完成组网路由配置。
* 部署Direct Tunnel功能且使用BGP over静态路由方案生成PGW-U到RNC的IP路由时，若PGW-U到RNC、到Gn网络使用相同的VPN，但DCGW到RNC、到Gn网络使用不同的VPN，则需要在PGW-U上配置到DCGW和RNC互通的VPN对应的BGP IP的路由，但不配置该路由对应的默认路由。
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
          minLength: 0
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UDG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5/S8-P、S2b、Gn-U、Gp-U接口。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口”。'
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
          description: '如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER\_ALL”，分别配置IPv4和IPv6地址。  需要使用不同的IP地址与ULCL UPF/BP UPF/I-UPF/SGW-U/ePDG/SGSN建立逻辑连接时，请规划多个Paif接口。Paif接口编号为Paif1/1/N，N取值范围为0~31。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口IP”。'
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
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。'
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
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
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
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Pa'
    add_logicinf_list:
    - NAME: 'Paif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.3.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Pa'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UDG”窗口。

### 2 配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 3 配置Pa（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）逻辑接口。

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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
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
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### UDG上只支持使用合一抽象接口配置Paif，不支持独立配置N9a、S5/S8-P、S2b接口。

