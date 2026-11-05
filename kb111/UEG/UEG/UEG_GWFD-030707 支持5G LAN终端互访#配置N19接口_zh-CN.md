---
id: GWFD-030707
name: 配置N19接口
ne_type: UEG
type: feature
description: '* 两个UPF是负荷分担关系，且连接到同一对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF间的VxLAN隧道（VxLAN N19）或UPF间的N19接口（3GPP N19）实现。 * 两个UPF是负荷分担关系，且连接到不同对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF与DCGW/VxLAN交换机之间的VxLAN隧道或UPF间的N19接口（3GPP N19）实现。  两个UPF是负荷分担关系，通过UPF间的VxLAN隧道（VxLAN N19）或UPF间的N19接口（3GPP N19）实现同一5G LAN组内成员跨UPF的互访时，需要参考本章节进行配置。  两个UPF是负荷分担关系，通过UPF与DCGW/VxLAN交换机之间的VxLAN隧道实现同一5G LAN组内成员跨UPF的互访时，在UPF仅需上完成配置5G LAN基本功能中的配置支持网络侧基于VXLAN的以太通信，不需要配置本章节，但该方案要求不同对DCGW/VxLAN交换机之间能够互通。'
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","GWFD-030707 支持5G LAN终端互访","配置N19接口"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST UPGTPPATH')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 两个UPF是负荷分担关系，且连接到同一对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF间的VxLAN隧道（VxLAN N19）或UPF间的N19接口（3GPP N19）实现。* 两个UPF是负荷分担关系，且连接到不同对DCGW/VxLAN交换机时，同一5G LAN组内成员跨UPF的互访可通过UPF与DCGW/VxLAN交换机之间的VxLAN隧道或UPF间的N19接口（3GPP N19）实现。两个UPF是负荷分担关系，通过UPF间的VxLAN隧道（VxLAN N19）或UPF间的N19接口（3GPP N19）实现同一5G LAN组内成员跨UPF的互访时，需要参考本章节进行配置。两个UPF是负荷分担关系，通过UPF与DCGW/VxLAN交换机之间的VxLAN隧道实现同一5G LAN组内成员跨UPF的互访时，在UPF仅需上完成配置5G LAN基本功能中的配置支持网络侧基于VXLAN的以太通信，不需要配置本章节，但该方案要求不同对DCGW/VxLAN交换机之间能够互通。

## 必备事项
前提条件

* 已完成配置5G LAN基本功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vtep_list:
      type: items
      properties:
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VXLAN隧道端点名称，网元内不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '5G LAN业务中，地址类型只支持配置为IPv4。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VTEPIPV4:
          name: '隧道端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '另一UPF的VXLAN隧道IP地址，用于两个UPF之间建立VXLAN隧道。  在另一UPF上执行**LST LOGICINF**查询到的vxlanif接口IP。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_vtepbindgrp_list:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VTEP绑定VXLAN隧道组。  VXLAN组名称复用N6侧VXLAN隧道组名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VTEP名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: PRIMARY
    set_nglanfunc_list:
      type: items
      properties:
        NGLANSW:
          name: '5G LAN功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        N19FORWARDSW:
          name: 'N19数据转发开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '通过N19接口实现跨UPF的终端互访时，使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
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
          description: '需要使用不同的IP地址与对接UPF建立逻辑连接时，请规划多个N19if接口。N19if接口编号为N19if1/1/N，N取值范围为0~31。'
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
          description: '如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER\_ALL”，分别配置IPv4和IPv6地址。'
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
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > VRF”。  请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。  已配置数据中获取'
          pattern: ''
          default: ''
    mod_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '层二5G LAN组时，必须设置为“ETHERNET”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PDNCONNECTTYPE:
          name: 'PDN连接类型'
          type: string
          enum:
          - VXLAN
          - ETHTERNET
          required: false
          description: '通过N19接口实现同一5G LAN组内成员跨UPF的互访时，使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VXLANINTERWORK:
          name: 'UPF间Vxlan隧道互通'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '同时部署N6侧VxLAN隧道和N19接口时，如两个UPF下的终端能够通过N6侧VXLAN隧道互通，则设置为“YES”；否则设置为“NO”。   * 设置为“YES”时，通过N6侧VXLAN转发上行未知单播消息、上行未知组播消息、上行已知组播消息（组播组中包含N6侧组播成员及N19下组播成员）、上行广播消息。 * 设置为“NO”时，通过N6侧VXLAN/N19接口转发上行未知单播消息、上行未知组播消息、上行已知组播消息（组播组中包含N6侧组播成员及N19下组播成员）、上行广播消息。   此处以设置为“NO”为例。  基于12的探测结果设置，能互通时，设置为“YES”；否则设置为“NO”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ULUKNUCASTFWNX:
          name: '上行未知单播转N6/N19'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '用于在单播泛洪开关关闭以及单播泛洪开关开启但已达到流控阈值场景下，配置上行未知单播消息是否通过N6/N19接口发送。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULUKNMCASTFWNX:
          name: '上行未知组播转N6/N19'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '用于在组播泛洪开关关闭以及组播泛洪开关开启但已达到流控阈值场景下，配置上行未知组播消息是否通过N6/N19接口发送。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ULBCASTFWNX:
          name: '上行广播转N6/N19'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '用于配置在广播达到流控阈值场景下上行广播消息是否通过N6/N19接口发送。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MACRPTMODE:
          name: 'MAC地址上报模式'
          type: string
          enum:
          - SINGLE_MAC_RPT
          - ALL_MAC_RPT
          required: false
          description: '采用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_echoiplist_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
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
        IPV4MASK:
          name: 'IP掩码'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    tst_ngvxlanconnect_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERUPFVIFIPV4:
          name: '对端UPF 5G LAN组虚拟接口IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vtep_list:
    - VTEPNAME: 'VTEP2'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.50.2'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP2'
      PRIFLAG: PRIMARY
    set_nglanfunc_list:
    - NGLANSW: ENABLE
      N19FORWARDSW: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N19'
    add_logicinf_list:
    - NAME: 'N19if1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.19.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_N19'
    mod_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      PDNCONNECTTYPE: VXLAN
      VXLANINTERWORK: NO
      ULUKNUCASTFWNX: ENABLE
      ULUKNMCASTFWNX: ENABLE
      ULBCASTFWNX: ENABLE
      MACRPTMODE: ALL_MAC_RPT
    add_echoiplist_list:
    - IPVERSION: IPV4
      IPV4ADDR: '10.3.3.3'
      IPV4MASK: 32
    tst_ngvxlanconnect_list:
    - VNINSTANCE: ''
      PEERUPFVIFIPV4: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 通过UPF间的VxLAN隧道（VxLAN N19）实现跨UPF的终端互访

### 配置VXLAN隧道端点（VTEP）。

```jinja2
{%- if is_scenario_vxlan_n19 -%}
    {%- for item in add_vtep_list -%}
        ADD VTEP:
        {#- --- 必选参数 --- -#}
        VTEPNAME="{{item.VTEPNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            VTEPIPV4="{{item.VTEPIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置VXLAN端点绑定VXLAN隧道组。

```jinja2
{%- if is_scenario_vxlan_n19 -%}
    {%- for item in add_vtepbindgrp_list -%}
        ADD VTEPBINDGRP:
        {#- --- 必选参数 --- -#}
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        VTEPNAME="{{item.VTEPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIFLAG is not none -%}
            PRIFLAG={{item.PRIFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 通过UPF间的N19（3GPP N19）实现跨UPF的终端互访

### 配置5G LAN基本配置。

### 详细配置请参见配置5G LAN基本功能，注意不能配置UPF之间的VXLAN隧道相关的内容。

### 4 开启5G LAN N19功能开关。

```jinja2
{%- if is_scenario_3gpp_n19 -%}
    {%- for item in set_nglanfunc_list -%}
        SET NGLANFUNC:
        {#- --- 必选参数 --- -#}
        NGLANSW={{item.NGLANSW}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：NGLANSW=ENABLE 时可选 --- -#}
        {%- if item.NGLANSW == 'ENABLE' -%}
            {%- if item.N19FORWARDSW is not none -%}
                N19FORWARDSW={{item.N19FORWARDSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置N19逻辑接口所属的VPN实例。N19逻辑接口与其他逻辑接口共用VPN实例时，请跳过本步骤。

```jinja2
{%- if is_scenario_3gpp_n19 -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 6 配置N19逻辑接口。

```jinja2
{%- if is_scenario_3gpp_n19 -%}
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
{%- endif -%}
```

### 7 修改5G LAN组配置。

```jinja2
{%- if is_scenario_3gpp_n19 -%}
    {%- for item in mod_ngvninstance_list -%}
        MOD NGVNINSTANCE:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PDNTYPE is not none -%}
            PDNTYPE={{item.PDNTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
        {%- if item.PDNTYPE == 'ETHERNET' -%}
            {%- if item.PDNCONNECTTYPE is not none -%}
                PDNCONNECTTYPE={{item.PDNCONNECTTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNCONNECTTYPE=VXLAN 时可选 --- -#}
        {%- if item.PDNCONNECTTYPE == 'VXLAN' -%}
            {%- if item.VXLANINTERWORK is not none -%}
                VXLANINTERWORK={{item.VXLANINTERWORK}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
        {%- if item.PDNTYPE == 'ETHERNET' -%}
            {%- if item.ULUKNUCASTFWNX is not none -%}
                ULUKNUCASTFWNX={{item.ULUKNUCASTFWNX}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
        {%- if item.PDNTYPE == 'ETHERNET' -%}
            {%- if item.ULUKNMCASTFWNX is not none -%}
                ULUKNMCASTFWNX={{item.ULUKNMCASTFWNX}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
        {%- if item.PDNTYPE == 'ETHERNET' -%}
            {%- if item.ULBCASTFWNX is not none -%}
                ULBCASTFWNX={{item.ULBCASTFWNX}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
        {%- if item.PDNTYPE == 'ETHERNET' -%}
            {%- if item.MACRPTMODE is not none -%}
                MACRPTMODE={{item.MACRPTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 3GPP N19之间的echo探测功能

### 查询路径相关属性。

#### 8.1 “EchoList 类型”取值为“白名单”时，执行9。

#### 8.2 “EchoList 类型”取值为“黑名单”时，不能执行9。

### 9 将对端UPF的N19接口IP添加到IP列表中。

```jinja2
{%- set LST_UPGTPPATH=getParameterValue('LST UPGTPPATH') -%}
{%- if is_scenario_3gpp_n19 and LST_UPGTPPATH=='白名单' -%}
    {%- for item in add_echoiplist_list -%}
        ADD ECHOIPLIST:
        {#- --- 必选参数 --- -#}
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDR="{{item.IPV4ADDR}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4MASK={{item.IPV4MASK}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 UPF间N6 VxLAN隧道互通探测

#### 10.1 本端UPF和对端UPF必须是基于同一个5G LAN组的互通探测。

#### 10.2 如下步骤需要在本端UPF和对端UPF上分别执行。

### 检查是否已配置以太业务MAC和5G LAN组虚接口。

### 如未配置，请参考配置5G LAN基本功能完成**SET UPETHSRVPARA**和**ADD NGVNVIF**配置。

### 11 查询5G LAN组会话是否已激活。

### 如未激活，需要先激活5G LAN组会话。

### 12 探测N6 VxLAN隧道能否互通。

```jinja2
{%- if is_scenario_3gpp_n19 -%}
    {%- for item in tst_ngvxlanconnect_list -%}
        TST NGVXLANCONNECT:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        PEERUPFVIFIPV4="{{item.PEERUPFVIFIPV4}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

