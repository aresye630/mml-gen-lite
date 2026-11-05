---
id: ''
name: 在UEG-S配置5G LAN终端互访功能
ne_type: UEG
type: feature
description: 不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。  子园区交换机与UPF之间建立VXLAN隧道的场景，图1~图3中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。  **表1** 5G LAN组网及报文路径  | 业务场景 | 负荷分担容灾模式 | | --- | --- | | 场景一：子园区5G LAN层二终端与子园区Server（Main PLC/MES/...）互通 | 组网如图1所示。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | | 场景二：同一5G LAN组的层二终端互通 | * 组网如图2所示。同一5G LAN组下不同终端通过**同一UEG-S**接入。 * 组网如图3所示。子园区UEG-S故障恢复后，子园区用户在子园区UEG-S激活，子园区UEG-S故障恢复前在UEG-L上激活的用户还未下线，同一5G LAN组下不同终端通过**UEG-S与UEG-L**接入。   子园区交换机与总部、子园区UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。总部园区和子园区UPF仅对接一对子园区企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图2和图3以1对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区企业侧VXLAN交换机上或独立的网关设备上。 * 两组LSW之间，通过直连线互通或者其他LSW互通。 |  当存在如下情况时，可以参考本页面进行配置。  * CPE下挂多个终端（最多16个）。 * 同一个二层广播域内的终端IP必须不同。 * 支持如下几种典型业务场景：   + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。      Server（Main PLC/MES/...）部署在N6侧。   + 同一5G LAN组层二终端之间通过同一UPF互通。   + 同一5G LAN组层二终端之间通过不同UPF互通，即总部园区2个UEG-L之间、总部园区UEG-L与子园区各UEG-S之间。      子园区交换机与UPF之间建立VXLAN隧道的场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。      两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  **图1** 子园区UEG-S正常运行，5G LAN层二终端与子园区Server（Main PLC/MES/...）互通  **图2** 子园区UEG-S正常运行，同一5G LAN组的层二终端在子园区UEG-S互通  **图3** 子园区UEG-S恢复，同一5G LAN组的层二终端在子园区UEG-S与总部园区UEG-L之间互通
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（跨级容灾，仅适用于海外）","新建方案配置","可选业务配置（5G LAN）","在UEG-S配置5G LAN终端互访功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。子园区交换机与UPF之间建立VXLAN隧道的场景，图1~图3中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。**表1** 5G LAN组网及报文路径| 业务场景 | 负荷分担容灾模式 || --- | --- || 场景一：子园区5G LAN层二终端与子园区Server（Main PLC/MES/...）互通 | 组网如图1所示。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 || 场景二：同一5G LAN组的层二终端互通 | * 组网如图2所示。同一5G LAN组下不同终端通过**同一UEG-S**接入。 * 组网如图3所示。子园区UEG-S故障恢复后，子园区用户在子园区UEG-S激活，子园区UEG-S故障恢复前在UEG-L上激活的用户还未下线，同一5G LAN组下不同终端通过**UEG-S与UEG-L**接入。   子园区交换机与总部、子园区UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。总部园区和子园区UPF仅对接一对子园区企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图2和图3以1对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区企业侧VXLAN交换机上或独立的网关设备上。 * 两组LSW之间，通过直连线互通或者其他LSW互通。 |当存在如下情况时，可以参考本页面进行配置。* CPE下挂多个终端（最多16个）。* 同一个二层广播域内的终端IP必须不同。* 支持如下几种典型业务场景：  + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。    Server（Main PLC/MES/...）部署在N6侧。  + 同一5G LAN组层二终端之间通过同一UPF互通。  + 同一5G LAN组层二终端之间通过不同UPF互通，即总部园区2个UEG-L之间、总部园区UEG-L与子园区各UEG-S之间。    子园区交换机与UPF之间建立VXLAN隧道的场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。    两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。**图1** 子园区UEG-S正常运行，5G LAN层二终端与子园区Server（Main PLC/MES/...）互通**图2** 子园区UEG-S正常运行，同一5G LAN组的层二终端在子园区UEG-S互通**图3** 子园区UEG-S恢复，同一5G LAN组的层二终端在子园区UEG-S与总部园区UEG-L之间互通

## 必备事项
前提条件

无。
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
          description: '* 总部园区UEG-L与子园区一套UEG-S必须对接同一套子园区的交换机。 * 总部园区部署两套负荷分担UEG-L，也可以部署一套UEG-L。 * 子园区部署一套UEG-S。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VTEPIPV4:
          name: '隧道对端端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '所有VXLAN隧道远端端点都和本端端点绑定在一个VXLAN组内。'
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
          data_source: ''
          pattern: ''
          default: PRIMARY
  examples:
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.50.1'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP1'
      PRIFLAG: PRIMARY
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置VXLAN隧道远端端点（VTEP：UPF），VTEPIPV4为远端端点IP，来源于另一UPF的VXLAN隧道端点IP地址。对端UPF必须对接到同一对企业侧VXLAN交换机。

#### 1.1 //远端为总部园区UEG-L的VXLAN隧道端点IP地址。

```jinja2
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
```

#### 1.2 //配置VXLAN隧道端点绑定VXLAN隧道组。

```jinja2
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
```

