---
id: ''
name: 配置N4(N4/Sxa/Sxb)接口数据
ne_type: UEG
type: feature
description: 运营商在部署MEC解决方案或时新增UPF/SGW-U/PGW-U中的任一独立设备或融合设备，完成配置UEG到SMF/SGW-C/PGW-C的路由数据后，可通过配置N4（N4/Sxa/Sxb）接口使UEG与SMF/SGW-C/PGW-C建立逻辑连接。  * 考虑到4G/5G互操作和平滑演进，5GC需要支持4G/5G融合接入和互操作，因此协议规定了三类网元需要原生融合部署。   + 用户数据：HSS+UDM融合，保证用户数据一致性。   + 策略数据：PCRF+PCF融合，保证策略一致性、连续性。   + 会话管理锚点：SMF+PGW-C融合，UPF+PGW-U融合，锚点不变保证数据连续性。从简化网络拓扑，优化转发路径考虑，一般建议EPC侧SGW-C融合到SMF+PGW-C、SGW-U融合到UPF+PGW-U。    因此部署4G/5G互操作的网络时，SMF、PGW-C需要融合部署在同一VNF上。 * 考虑到4G/5G互操作时移动锚点不变，SMF+PGW-C融合部署时N4、Sxa、Sxb接口使用的协议相同，遵循3GPP TS 29.244标准。因此UEG上只支持使用合一抽象接口配置N4if，不支持独立配置Sxa、Sxb接口。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置主锚点UPF","配置N4(N4/Sxa/Sxb)接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商在部署MEC解决方案或时新增UPF/SGW-U/PGW-U中的任一独立设备或融合设备，完成配置UEG到SMF/SGW-C/PGW-C的路由数据后，可通过配置N4（N4/Sxa/Sxb）接口使UEG与SMF/SGW-C/PGW-C建立逻辑连接。* 考虑到4G/5G互操作和平滑演进，5GC需要支持4G/5G融合接入和互操作，因此协议规定了三类网元需要原生融合部署。  + 用户数据：HSS+UDM融合，保证用户数据一致性。  + 策略数据：PCRF+PCF融合，保证策略一致性、连续性。  + 会话管理锚点：SMF+PGW-C融合，UPF+PGW-U融合，锚点不变保证数据连续性。从简化网络拓扑，优化转发路径考虑，一般建议EPC侧SGW-C融合到SMF+PGW-C、SGW-U融合到UPF+PGW-U。  因此部署4G/5G互操作的网络时，SMF、PGW-C需要融合部署在同一VNF上。* 考虑到4G/5G互操作时移动锚点不变，SMF+PGW-C融合部署时N4、Sxa、Sxb接口使用的协议相同，遵循3GPP TS 29.244标准。因此UEG上只支持使用合一抽象接口配置N4if，不支持独立配置Sxa、Sxb接口。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（风筝M）。
* 请阅读并熟悉特性GWFD-021312 Single IP。
* SMF/PGW-C上要求UPF上必须配置N9接口才能作为主锚点UPF激活时，还需要在UPF上完成配置Pa(N9a/S5-P/S8-P/S2b)接口数据。
* 配置N4接口数据后，UEG上至少还需要存在一个数据面的逻辑接口IP（如Paif、Scif或s5-sif或n9cif、Saif或N3if或S1-Uif、S11-uif等），否则，SMF与UPF之间的N4偶联状态异常。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
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
          description: 'UEG上N4、Sxa、Sxb接口不支持独立配置，只支持使用合一抽象接口名称N4if进行配置。  N4接口名称唯一，为N4if1/0/0。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口”。  本端规划'
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
          description: '如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER_ALL”，分别配置IPv4和IPv6地址。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 逻辑接口IP”。  全网规划'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU_Cxx”且“子端口”为“group_isu_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
          pattern: ''
          default: ''
    set_upinfo_list:
      type: items
      properties:
        HOSTNAME:
          name: 'HostName'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: 'UPF标识。不同UPF，该参数不能相同。  如不配置该参数，则偶联会建立失败。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Signaling'
    add_logicinf_list:
    - NAME: 'N4if1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.6.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Signaling'
    set_upinfo_list:
    - HOSTNAME: 'UP_001'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置N4（N4/Sxa/Sxb）逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 3 配置N4（N4/Sxa/Sxb）逻辑接口。

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### UEG上N4、Sxa、Sxb接口不支持独立配置，只支持使用合一抽象接口名称N4if进行配置。

### 4 配置UEG信息。

```jinja2
{%- for item in set_upinfo_list -%}
    SET UPINFO:
    {#- --- 可选参数 --- -#}
    {%- if item.HOSTNAME is not none -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 （风筝M非应急场景）一个UPF对接多个SMF场景，还需要进行CU Full Mesh特性配置及相关License申请。

### CU Full Mesh特性配置的详细指导，请参见GWFD-021701 CU Full Mesh组网特性概述。

