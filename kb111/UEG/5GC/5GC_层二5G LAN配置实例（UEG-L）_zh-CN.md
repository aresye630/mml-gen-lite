---
id: ''
name: 层二5G LAN配置实例（UEG-L）
ne_type: UEG
type: feature
description: 园区部署两套UEG-L，两套UEG-L是负荷分担容灾模式或主备容灾模式。不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，图1~图8中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。 * DCGW与UPF之间建立VXLAN隧道的场景，图2~图8中的Firewall、LSW仅用于举例，5G LAN业务对Firewall、LSW数量无特殊要求。  **表1** 5G LAN组网及报文路径  | 业务场景 | 负荷分担容灾模式 | 主备容灾模式（冷备/热备） | | --- | --- | --- | | 场景一：5G LAN层二终端与Server（Main PLC/MES/...）互通 | 组网如图1/图2所示。  负荷分担容灾模式时，两个UEG-L均处理业务，5G LAN层二终端通过某一UEG-L与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 组网如图6所示。  主备容灾模式时，同一时刻，只有一套UEG-L处理业务，5G LAN层二终端通过运行状态为主的UEG-L与Server（Main PLC/MES/...）互通。另一套UEG-L不处理业务（冷备状态）。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | | 场景二：同一5G LAN组的层二终端之间互通 | 组网如图3所示。  两套UEG-L是负荷分担容灾模式时，同一5G LAN组下不同终端通过**同一UEG-L或不同UEG-L**接入。如同一5G LAN组下无线接入的终端通过不同UPF互通：  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。 * DCGW与UPF之间建立VXLAN隧道的场景，两个UPF对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图3以两对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 组网如图8所示。  两套UEG-L是主备容灾模式时，同一5G LAN组下无线接入的终端可通过同一UPF直接互通，不需要经过LSW/DCGW。  说明：  同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 |  当存在如下情况时，可以参考本页面进行配置。  * CPE下挂多个终端（最多16个）。 * 同一个二层广播域内的终端IP必须不同。 * 支持如下几种典型业务场景：   + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。      Server（Main PLC/MES/...）部署在N6侧。   + 同一5G LAN组层二终端之间通过同一UPF互通。   + 同一5G LAN组层二终端之间通过不同UPF互通。     - 企业侧交换机与UPF之间建立VXLAN隧道的场景        该业务场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。        两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。     - DCGW与UPF之间建立VXLAN隧道的场景        两个UPF是负荷分担关系，且仅对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。  **图1** UEG-L负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）  **图2** UEG-L负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）  **图3** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，企业侧交换机与UPF之间建立VXLAN隧道）  * 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。 * 两组LSW之间，通过直连线互通或者其他LSW互通。  **图4** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，DCGW与UPF之间建立VXLAN隧道）  * 两个UPF是负荷分担关系，且连接到不同对DCGW时，5G LAN成员之间跨UPF的互访可通过UPF与DCGW之间的VxLAN隧道实现。 * 两组DCGW之间，通过直连线互通或通过其他LSW互通。  **图5** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，UPF与另一UPF之间建立VXLAN隧道）  两个UPF是负荷分担关系，且仅对接一对DCGW/企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  **图6** UEG-L主备组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）  **图7** UEG-L主备组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）  **图8** UEG-L主备组网（同一5G LAN组的层二终端之间互通）
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","配置实例","层二5G LAN配置实例（UEG-L）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
园区部署两套UEG-L，两套UEG-L是负荷分担容灾模式或主备容灾模式。不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。* 企业侧交换机与UPF之间建立VXLAN隧道的场景，图1~图8中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。* DCGW与UPF之间建立VXLAN隧道的场景，图2~图8中的Firewall、LSW仅用于举例，5G LAN业务对Firewall、LSW数量无特殊要求。**表1** 5G LAN组网及报文路径| 业务场景 | 负荷分担容灾模式 | 主备容灾模式（冷备/热备） || --- | --- | --- || 场景一：5G LAN层二终端与Server（Main PLC/MES/...）互通 | 组网如图1/图2所示。  负荷分担容灾模式时，两个UEG-L均处理业务，5G LAN层二终端通过某一UEG-L与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 组网如图6所示。  主备容灾模式时，同一时刻，只有一套UEG-L处理业务，5G LAN层二终端通过运行状态为主的UEG-L与Server（Main PLC/MES/...）互通。另一套UEG-L不处理业务（冷备状态）。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 || 场景二：同一5G LAN组的层二终端之间互通 | 组网如图3所示。  两套UEG-L是负荷分担容灾模式时，同一5G LAN组下不同终端通过**同一UEG-L或不同UEG-L**接入。如同一5G LAN组下无线接入的终端通过不同UPF互通：  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。 * DCGW与UPF之间建立VXLAN隧道的场景，两个UPF对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图3以两对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 组网如图8所示。  两套UEG-L是主备容灾模式时，同一5G LAN组下无线接入的终端可通过同一UPF直接互通，不需要经过LSW/DCGW。  说明：  同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 |当存在如下情况时，可以参考本页面进行配置。* CPE下挂多个终端（最多16个）。* 同一个二层广播域内的终端IP必须不同。* 支持如下几种典型业务场景：  + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。    Server（Main PLC/MES/...）部署在N6侧。  + 同一5G LAN组层二终端之间通过同一UPF互通。  + 同一5G LAN组层二终端之间通过不同UPF互通。    - 企业侧交换机与UPF之间建立VXLAN隧道的场景      该业务场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。      两个UPF仅对接一对企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。    - DCGW与UPF之间建立VXLAN隧道的场景      两个UPF是负荷分担关系，且仅对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。**图1** UEG-L负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）**图2** UEG-L负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）**图3** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，企业侧交换机与UPF之间建立VXLAN隧道）* 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。* 两组LSW之间，通过直连线互通或者其他LSW互通。**图4** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，DCGW与UPF之间建立VXLAN隧道）* 两个UPF是负荷分担关系，且连接到不同对DCGW时，5G LAN成员之间跨UPF的互访可通过UPF与DCGW之间的VxLAN隧道实现。* 两组DCGW之间，通过直连线互通或通过其他LSW互通。**图5** UEG-L负荷分担组网（同一5G LAN组的层二终端之间互通，UPF与另一UPF之间建立VXLAN隧道）两个UPF是负荷分担关系，且仅对接一对DCGW/企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。**图6** UEG-L主备组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）**图7** UEG-L主备组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）**图8** UEG-L主备组网（同一5G LAN组的层二终端之间互通）

## 必备事项
前提条件

前提条件

* 除5G LAN业务外，UEG-L支持的5G SA业务运行正常。
* 企业侧交换机与UPF之间建立VXLAN隧道的场景，UPF和LSW之间的VXLAN隧道路径中存在防火墙时，防火墙需要放通VXLAN隧道IP地址（端口any，动态分配端口）对应的流量。
* 5GC与N6侧网络环境已构建完成。
  + 企业侧交换机与UPF之间建立VXLAN隧道的场景

    两个UEG-L是负荷分担容灾模式，且同一5G LAN组内的终端存在互通诉求时，若LSW不支持将通过VXLAN隧道接收的报文再通过VXLAN隧道转发出去，则每个UEG-L需对接2个LSW用于建立VXLAN隧道，那么两个UEG-L需要4个LSW。如图3所示。
  + DCGW与UPF之间建立VXLAN隧道的场景

    两个UPF是负荷分担关系，且仅对接一对DCGW/企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。
* 已加载License文件，且包含如下License控制项：
  + UDM：LKQ7UDMBE15 5G LAN签约用户数
  + SMF：LKV2SALANSM01 5G LAN业务基本功能-USM
  + UPF：LKV3G5LANB01 5G LAN基础功能

    如下几个License控制项需基于实际业务申请：
    - LKV3G5L2SMUL 层二静态组播
    - LKV3G5LADFSR 5G LAN双发选收会话数
    - LKV3G5LAN2LE 5G LAN层二环路消除
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQI:
          name: '5QI'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '是否允许抢占低优先级业务的资源'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '是否允许资源被高优先级业务抢占'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGQIPRILEVEL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnnqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          maxLength: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          enum:
          - SSC_MODE_1
          - SSC_MODE_2
          - SSC_MODE_3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: integer
          minimum: 1
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          enum:
          - bps
          - Kbps
          - Mbps
          - Gbps
          - Tbps
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smdata_list:
      type: items
      properties:
        IMSI:
          name: 'CPE IMSI'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        SNSSAI:
          name: 'SNSSAI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          required: false
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        DEFAULT:
          name: 'DEFAULT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: 'DNNQOSTPLID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vngroup_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INGROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 10
          maxLength: 38
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        EXTGROUPID:
          name: '外部组ID'
          type: string
          minLength: 3
          maxLength: 128
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  不同UDM上，外部组ID不能重复。外部组ID格式为：<*name*>@<*domain*>   * *<name>*建议企业内部按照group01，group02进行规划。企业内部有多个5G LAN组，不同5G LAN组的*<name>*值不能重复。 * *<domain>*建议使用企业域名。'
          data_source: ''
          pattern: ''
          default: ''
        SHAREDID:
          name: '共享数据ID'
          type: string
          maxLength: 64
          required: true
          description: '规划多个5G LAN组时，不同UDM该参数不能相同。  建议不同行政区分段，行政区内不同UDM该参数也必须不同。'
          data_source: ''
          pattern: ''
          default: ''
        SNSSAI:
          name: '切片标识'
          type: string
          minLength: 1
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          maxLength: 64
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        PDUTYPES:
          name: 'PDU类型'
          type: string
          enum:
          - IPV4V6
          - IPV4
          - IPV6
          - UNSTR
          - ETHER
          required: true
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ''
    add_groupid_list:
      type: items
      properties:
        IMSI:
          name: 'CPE IMSI'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        INGROUPID:
          name: '5G LAN组ID'
          type: string
          required: false
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfns_list:
      type: items
      properties:
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnsdnn_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CORRECTTYPE:
          name: '纠正类型'
          type: string
          enum:
          - NS_CORRECTION
          - DNN_CORRECTION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        DNNPLCY:
          name: 'DNN纠正策略'
          type: string
          enum:
          - Default_DNN_preferred
          - Only_The_Configured_DNN
          - Configured_DNN_Preferred
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISFAILPLCY:
          name: 'SMF发现失败处理策略'
          type: string
          enum:
          - STANDARD_MODEL
          - RETRY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STANDARD_MODEL
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    set_smffunc_list:
      type: items
      properties:
        NGLANSWITCH:
          name: '是否支持建立5G LAN会话'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upselectflag_list:
      type: items
      properties:
        NGLANUPFSELSW:
          name: '5G LAN UPF选择开关'
          type: string
          enum:
          - LOCALABILITY
          - GCOMABILITY
          - LOCALANDGCOM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_plmnns_list_1:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNIDX:
          name: 'PLMN索引'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATE:
          name: '状态'
          type: string
          enum:
          - INACTIVE
          - ACTIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfns_list_1:
      type: items
      properties:
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
          - NfNWDAF
          - NfTypeMAX
          - NfMBSMF
          - NfCBCF
          - NfSCF
          - NfSPF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '采用独立的APN接入5G LAN业务时，SST、SD参数可以和其他业务的SST、SD复用。复用时不需要重复规划及配置。  UDM上的SNSSAI参数取值是SST-SD，即：SNSSAI="1-010101"。'
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片ID'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    add_pnfdnn_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        DNN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        NGLANSW:
          name: '是否支持5G LAN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREATYPE:
          name: 'UPF服务区类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务器绑定的TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '复用时不需要规划及配置。'
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务器绑定的TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '复用时不需要规划及配置。'
          data_source: ''
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: '对端UPF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '复用已有的UPF节点时，可通过LST PNFPROFILE命令查询获取。'
          data_source: ''
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_grpnglanfunc_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        LDRSW:
          name: '环路检测开关'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINESW:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpurr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpurrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cppccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_usrprofgroup_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpuserprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: PCC
        UPSPECTYPE:
          name: '用户模板规格类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFICATION_LIMITED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upbindupg_list:
      type: items
      properties:
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPBINDTYPE:
          name: '用户模板绑定类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFIC
          - ULCL
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALPCCSELECT:
          name: '本地PCC策略选择模式'
          type: string
          enum:
          - INHERIT
          - LOCAL_PCC_ACTIVE
          - LOCAL_PCC_DEACTIVE
          - LOCAL_PCC_NO_CRBN_ACT
          - LOCAL_PCC_NO_RULE_ACT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cprule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        RULERANGE:
          name: '规则生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
        RULESPECTYPE:
          name: '规则规格类型'
          type: string
          enum:
          - DEFAULT
          - SPECIFICATION_LIMITED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cprulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upapn_list:
      type: items
      properties:
        APN:
          name: 'APN/DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划一个独立的APN，接入5G LAN业务。   * AMF、SMF、UPF、UDM部署5G LAN业务时，需关注该规划原则。 * 对于风筝S/M，一个5G LAN组可以和多个中心SMF（UNC）相关联，即支持5G LAN SMF-UPF Fullmesh组网，用于SMF容灾。多个SMF上的5G LAN配置相同。'
          data_source: ''
          pattern: ''
          default: ''
    add_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDU类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ETHERNET
        MACIDLESW:
          name: 'N3学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IGMPSNOOPINGSW:
          name: 'IGMP Snooping开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        IGMPPARSESW:
          name: 'IGMP消息解析开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        MULTIFLOODSW:
          name: '组播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        MULTIFLOODRATE:
          name: '组播泛洪速率'
          type: integer
          minimum: 1
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 50
        BCASTFLOWCTRLSW:
          name: '广播流控开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        UNICASTFLOODSW:
          name: '单播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        N6MACIDLESW:
          name: 'N6学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'VXLAN隧道端点IP（UPF）'
          type: string
          maxLength: 15
          required: false
          description: 'UPF上的vxlanif接口的IP地址。   * UEG裸机容器+UEG热备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须相同。 * UEG裸机容器+UEG冷备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须不同。   UEG虚机容器+每个UEG对接一对DCGW时，两个UPF上的vxlan逻辑接口IP地址可以相同，可以不同。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list_1:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'VXLAN隧道端点IP（UPF）'
          type: string
          maxLength: 15
          required: false
          description: 'UPF上的vxlanif接口的IP地址。   * UEG裸机容器+UEG热备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须相同。 * UEG裸机容器+UEG冷备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须不同。   UEG虚机容器+每个UEG对接一对DCGW时，两个UPF上的vxlan逻辑接口IP地址可以相同，可以不同。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VXLAN接口绑定的VPN实例（UPF）'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '此处以复用N6接口的VPN实例为例。  如使用独立的VPN实例，则：参考N6接口配置，配置对应的外联口IP、路由数据。  * 参考N6接口重新规划一套外联口IP和路由数据（外联口绑定的VPN与VXLAN接口绑定的VPN相同）。 * 需要执行**ADD VPNINST**命令增加规划的VPN实例。'
          data_source: ''
          pattern: ''
          default: ''
    add_vxlangrp_list:
      type: items
      properties:
        GRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEARTBEAT:
          name: '健康检查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 6
        HEARTSUCCLIMIT:
          name: '健康检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        HEARTFAILLIMIT:
          name: '健康检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
    add_vxlangrp_list_1:
      type: items
      properties:
        GRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEARTBEAT:
          name: '健康检查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_vtep_list:
      type: items
      properties:
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        VTEPIPV4:
          name: 'VXLAN隧道端点IP（LSW/DCGW）'
          type: string
          maxLength: 15
          required: false
          description: 'LSW/DCGW上用于和UPF建立VXLAN隧道的IP。   * UEG裸机容器+UEG热备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的VTEP IP地址必须相同。 * UEG虚机容器+每个UEG对接一对DCGW时，两个UPF上的VTEP IP地址可以相同，可以不同。'
          data_source: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VTEP名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
    add_ngvnbindvxlan_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Byte
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHARGEFLAG:
          name: '事件计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHGPOINT:
          name: '事件计费点'
          type: string
          enum:
          - FINISH
          - REQUEST
          - RESPONSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RESPONSE
        MMSCHARGETYPE:
          name: '彩信计费类型'
          type: string
          enum:
          - MULTI
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        SIGNALASSOCIATE:
          name: '信令关联计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        TOKENFUNCFLAG:
          name: 'Token检测功能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERCONFIG
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TCPCHGPROFLAG:
          name: 'TCP重传计费标识'
          type: string
          enum:
          - CHARGING
          - NOCHARGING
          - NOTCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: '缺省信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upethsrvpara_list:
      type: items
      properties:
        UPETHSRVSW:
          name: '用户面以太业务开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC地址'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngvnvif_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        VIFIPTYPE:
          name: '虚拟接口IP地址类型'
          type: string
          enum:
          - IPV4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        VIFIPV4ADDR:
          name: '虚拟接口IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_interface_list_2:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_multicastgrp_list:
      type: items
      properties:
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCASTMACADDR:
          name: '组播MAC地址'
          type: string
          minLength: 0
          maxLength: 17
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngbindmcastgrp_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mcastgrpmem_list:
      type: items
      properties:
        MCASTGRPNAME:
          name: '组播组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMTYPE:
          name: '成员类型'
          type: string
          enum:
          - IMSI
          - VTEP
          - DFSRPAIR
          - ETHERNETPDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMSI
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngvnuemutacc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        N9AUE2UEUNIPOL:
          name: 'N9A口单播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N9AUE2UEMULPOL:
          name: 'N9A口组播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N9AUE2UEBROPOL:
          name: 'N9A口广播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_uemutaccwlist_list:
      type: items
      properties:
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4START:
          name: 'IPV4起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4END:
          name: 'IPV4截止地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngbinduemutwl_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upsoftpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_3:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngloopdetfunc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        ETHLOOPDETECTSW:
          name: '环路检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMETHOD:
          name: '环路检测方式'
          type: string
          enum:
          - SEND_DETECT_MSG
          - MAC_FLAP_NUM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upethsrvpara_list_1:
      type: items
      properties:
        UPETHSRVSW:
          name: '用户面以太业务开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC地址'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_4:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngloopdetfunc_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        ETHLOOPDETECTSW:
          name: '环路检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETECTMETHOD:
          name: '环路检测方式'
          type: string
          enum:
          - SEND_DETECT_MSG
          - MAC_FLAP_NUM
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MACFLAPNUM:
          name: 'MAC地址漂移次数'
          type: integer
          minimum: 3
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_5:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngdfsrfunc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        DFSRSWITCH:
          name: '双发选收功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dfsrattr_list:
      type: items
      properties:
        NEPRIFLAG:
          name: '网元主备用标识'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dfsrpair_list:
      type: items
      properties:
        DFSRPAIRID:
          name: 'DFSRPAIRID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFSRMODE:
          name: 'DFSRMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAIRDESCRIPTION:
          name: 'PAIRDESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dfsrpairmem_list:
      type: items
      properties:
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngbinddfsrpair_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dfsrattr_list_1:
      type: items
      properties:
        NEPRIFLAG:
          name: '网元主备用标识'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAIRUEACTTIME:
          name: '双发选收结对内用户激活时长'
          type: integer
          minimum: 3
          maximum: 300
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDU类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: '层二5G LAN采用以太类型；层三5G LAN采用IP类型。'
          data_source: ''
          pattern: ''
          default: ''
        IGMPSNOOPINGSW:
          name: 'IGMP Snooping开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_igmpsnoopingattr_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        QUERIERSW:
          name: '查询器功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYINTERVAL:
          name: '普遍组查询时间间隔（秒）'
          type: integer
          minimum: 30
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        MAXRSPTIME:
          name: '普遍组查询的最大响应时间（秒）'
          type: integer
          minimum: 1
          maximum: 25
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        ROBUSTCOUNT:
          name: 'IGMP健壮系数'
          type: integer
          minimum: 2
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
    set_upethsrvpara_list_2:
      type: items
      properties:
        UPETHSRVSW:
          name: '用户面以太业务开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC地址'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_igmpsnoopingattr_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        QUERIERSW:
          name: '查询器功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYINTERVAL:
          name: '普遍组查询时间间隔（秒）'
          type: integer
          minimum: 30
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 60
        MAXRSPTIME:
          name: '普遍组查询的最大响应时间（秒）'
          type: integer
          minimum: 1
          maximum: 25
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        ROBUSTCOUNT:
          name: 'IGMP健壮系数'
          type: integer
          minimum: 2
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2
        SOURCEADDR:
          name: 'IGMP普遍组查询报文的源IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_multicastsource_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        MCSOURCETYPE:
          name: '组播源类型'
          type: string
          enum:
          - IMSI
          - DFSRPAIR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_multicastsource_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组ID'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '规划多个5G LAN组时，该参数不能相同。  一个Server（Main PLC/MES/...）下的所有用户规划到同一个5G LAN组中。  对于UDM NF，5G LAN组ID对应的参数是INGROUPID。  UDM上，5G LAN组ID格式为“Group service ID-PLMNID-Local-Group-ID”。其中，Group service ID是十进制格式，PLMNID=MCC+MNC，Local-Group-ID是十六进制。  UPF上，5G LAN组ID格式为“GroupServiceID-MCC-MNC-LocalGroupID”，“GroupServiceID”是十六进制格式，“LocalGroupID”是十六进制格式。'
          data_source: ''
          pattern: ''
          default: ''
        MCSOURCETYPE:
          name: '组播源类型'
          type: string
          enum:
          - IMSI
          - DFSRPAIR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngcqostpl_list:
    - HLRSN: 1
      TPLID: 1
      TPLNAME: 'tp5glan01'
      NGQI: 9
      ARPPRILEVEL: 1
      PREEMPTIONCAP: TRUE
      PREEMPTIONVUL: FALSE
      NGQIPRILEVEL: 1
    add_dnnqostpl_list:
    - HLRSN: 1
      TPLID: 2
      TPLNAME: 'tp5glan01'
      PDUTYPE: ETHER
      SSCMODE: SSC_MODE_1
      NGCQOSTPLID: 1
      AMBRUP: 5
      UPUNIT: Gbps
      AMBRDW: 5
      DWUNIT: Gbps
      CHARGE: '0800'
    add_smdata_list:
    - IMSI: '460081000000001'
      SNSSAI: 1-010101
      DNN: dnn5glan01
      DEFAULT: TRUE
      DNNQOSTPLID: '2'
    add_vngroup_list:
    - HLRSN: 1
      INGROUPID: '1001-46008-01'
      EXTGROUPID: 'group01@huawei.com'
      SHAREDID: '46008-huawei01'
      SNSSAI: '1-010101'
      DNN: 'dnn5glan01'
      PDUTYPES: ETHER
    add_groupid_list:
    - IMSI: '460081000000001'
      INGROUPID: 1001-46008-01
    add_plmnns_list:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 1
    add_localnsdnn_list:
    - SUBRANGE: HOME_USER
      CORRECTTYPE: DNN_CORRECTION
      SST: 1
      SD: '010101'
      DNN: 'dnn5glan01'
      DNNPLCY: Default_DNN_preferred
      DISFAILPLCY: STANDARD_MODEL
      DESC: '5GLAN_DNN_Correction'
    add_pnfdnn_list:
    - INDEX: 5
      NFINSTANCEID: 'SMF_Instance_1'
      DNN: 'dnn5glan01'
    add_pnfns_list:
    - INDEX: 5
      NFINSTANCEID: 'SMF_Instance_1'
      SST: 1
      SD: '010101'
    set_smffunc_list:
    - NGLANSWITCH: Support
    set_upselectflag_list:
    - NGLANUPFSELSW: LOCALABILITY
    set_pfcppvtext_list:
    - FEATURE: NGLAN
      SWITCH: ENABLE
    add_plmnns_list_1:
    - NSIDX: 1
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
    add_nfns_list_1:
    - NFTYPE: NfSMF
      NSIDX: 1
    add_cpapn_list:
    - APN: 'dnn5glan01'
    add_nsdnn_list:
    - NSIDX: 1
      DNN: 'dnn5glan01'
    add_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      LOCATION: Central
      UPFUNCTION: None
      VPNNAME: 'VRF_CN'
    add_pnfprofile_list:
    - NFINSTANCEID: 'upf_instance_1'
      NFTYPE: NfUPF
      FQDN: '5glan01.upf'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.5.52.2'
      PORT: 8805
    add_pnfns_list_1:
    - INDEX: 1
      NFINSTANCEID: 'upf_instance_1'
      SST: 1
      SD: '010101'
    add_pnfdnn_list_1:
    - INDEX: 0
      NFINSTANCEID: 'upf_instance_1'
      DNN: 'dnn5glan01'
      PNFNSINDEX: 1
    mod_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      NGLANSW: ENABLE
    add_uparea_list:
    - AREANAME: 'area01'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'area01'
      N2BEGINTAI: '46008000000'
      N2ENDTAI: '46008FFFFFF'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'upf_instance_1'
      SMFSERVINGAREA: 'area01'
    add_grpnglanfunc_list:
    - GROUPID: '000003e9-460-08-01'
      LDRSW: SUPPORT
    set_apnpccfunc_list:
    - APN: 'dnn5glan01'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    set_apnchargectrl_list:
    - APN: 'dnn5glan01'
      ONLINESW: DISABLE
      OFFLINESW: DISABLE
      CONVERGEDSW: DISABLE
    add_cpurr_list:
    - URRNAME: '5glan_urr_offline'
      URRID: 2222
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 2222
      OFFMETERINGTYPE: VOLUME
      N40AGESW: ENABLE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 1111
      ONLMETERINGTYPE: VOLUME
      VOLUMERSUVALUE: 0
    add_cpurrgroup_list:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr_offline'
      DOWNURRNAME1: '5glan_urr_offline'
      UPURRNAME2: '5glan_urr_online'
      DOWNURRNAME2: '5glan_urr_online'
    add_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      URRGROUPNAME: '5glan_urrgroup'
      FUPSESSIONEXC: DISABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'profilegroupfglan'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      UPTYPE: PCC
      UPSPECTYPE: DEFAULT
    add_upbindupg_list:
    - USERPROFGNAME: 'profilegroupfglan'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'fglan_u_p_any'
      LOCALPCCSELECT: INHERIT
    add_apnusrprofg_list:
    - APN: 'dnn5glan01'
      USERPROFGNAME: 'profilegroupfglan'
    add_cprule_list:
    - RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
      POLICYNAME: 'pccpolicy_group'
      PRIORITY: 65535
      RULERANGE: ALL
      RULESPECTYPE: DEFAULT
    add_cprulebinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LANB01'
      SWITCH: ENABLE
    set_nglanfunc_list:
    - NGLANSW: ENABLE
    add_upapn_list:
    - APN: 'dnn5glan01'
    add_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      MACIDLESW: DISABLE
      IGMPSNOOPINGSW: DISABLE
      IGMPPARSESW: DISABLE
      MULTIFLOODSW: ENABLE
      MULTIFLOODRATE: 20
      BCASTFLOWCTRLSW: ENABLE
      UNICASTFLOODSW: DISABLE
      N6MACIDLESW: DISABLE
    add_logicinf_list:
    - NAME: 'vxlanif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.50.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: '_public_'
    add_logicinf_list_1:
    - NAME: 'vxlanif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.50.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_LocalDN01'
    add_vxlangrp_list:
    - GRPNAME: 'vxlan_01'
      SRCINTF: 'vxlanif1/1/0'
      HEARTBEAT: ENABLE
      TIMETHRESHOLD: 6
      HEARTSUCCLIMIT: 3
      HEARTFAILLIMIT: 3
      TIMEOUT: 2
    add_vxlangrp_list_1:
    - GRPNAME: 'vxlan_01'
      SRCINTF: 'vxlanif1/1/0'
      HEARTBEAT: DISABLE
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
    - VTEPNAME: 'VTEP2'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.50.2'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP1'
      PRIFLAG: PRIMARY
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP2'
      PRIFLAG: PRIMARY
    add_ngvnbindvxlan_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VXLANGRPNAME: 'vxlan_01'
      VNI: 5010
    add_urr_list:
    - URRNAME: '5glan_urr_offline'
      URRID: 2222
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
    add_urrgroup_list:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr_offline'
      DOWNURRNAME1: '5glan_urr_offline'
      UPURRNAME2: '5glan_urr_online'
      DOWNURRNAME2: '5glan_urr_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: '5glan_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: '5glan_urrgroup'
      SIGURRGRPNAME: 'ycll_01_ch_p'
    add_filter_list:
    - FILTERNAME: 'any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_filteripv6_list:
    - FILTERNAME: 'any_ipv6'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_flowfilter_list:
    - FLOWFILTERNAME: 'any_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'any_f_f'
      FILTERNAME: 'any'
    add_rule_list:
    - RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'any_f_f'
      POLICYNAME: '5glan_pcc_p_g'
    add_userprofile_list:
    - USERPROFILENAME: 'fglan_u_p_any'
    add_rulebinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      TCPCHGPROFLAG: NOTCONFIG
      DFTSIGURRGNAME: 'ycll_01_ch_p'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    set_upethsrvpara_list:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    add_ngvnvif_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VIFIPTYPE: IPV4
      VIFIPV4ADDR: '10.99.99.99'
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFMTU: 1600
    mod_interface_list_2:
    - IFNAME: 'Eth-trunk1'
      IFMTU: 1600
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5L2SMUL'
      SWITCH: ENABLE
    - LICITEM: 'LKV3G5L2SMUL'
      SWITCH: ENABLE
    add_multicastgrp_list:
    - MCASTGRPNAME: 'MCASTGRP01'
      MCASTMACADDR: '11-11-11-11-11-fc'
    add_ngbindmcastgrp_list:
    - VNINSTANCE: '000003e9-460-08-01'
      MCASTGRPNAME: 'MCASTGRP01'
    add_mcastgrpmem_list:
    - MCASTGRPNAME: 'MCASTGRP01'
      MEMTYPE: IMSI
      IMSI: '123456789'
      VTEPNAME: 'VTEP1'
    set_ngvnuemutacc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      N9AUE2UEUNIPOL: WHITELIST_FWD
      N9AUE2UEMULPOL: WHITELIST_FWD
      N9AUE2UEBROPOL: WHITELIST_FWD
    add_uemutaccwlist_list:
    - WLISTNAME: 'I-UPF-01'
      IPVERSION: IPV4
      IPV4START: '192.168.111.1'
      IPV4END: '192.168.111.1'
    add_ngbinduemutwl_list:
    - VNINSTANCE: '000003e9-460-08-01'
      WLISTNAME: 'I-UPF-01'
    set_upsoftpara_list:
    - DT: BIT
      BITNUM: 2539
      BITVALUE: 1
    set_licenseswitch_list_3:
    - LICITEM: 'LKV3G5LAN2LE'
      SWITCH: ENABLE
    set_ngloopdetfunc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      ETHLOOPDETECTSW: ENABLE
      DETECTMETHOD: SEND_DETECT_MSG
    set_upethsrvpara_list_1:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    set_licenseswitch_list_4:
    - LICITEM: 'LKV3G5LAN2LE'
      SWITCH: ENABLE
    set_ngloopdetfunc_list_1:
    - VNINSTANCE: '000003e9-460-08-02'
      ETHLOOPDETECTSW: ENABLE
      DETECTMETHOD: MAC_FLAP_NUM
      MACFLAPNUM: 10
    set_licenseswitch_list_5:
    - LICITEM: 'LKV3G5LADFSR'
      SWITCH: ENABLE
    - LICITEM: 'LKV3G5LADFSR'
      SWITCH: ENABLE
    set_ngdfsrfunc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRSWITCH: ENABLE
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRSWITCH: ENABLE
    set_dfsrattr_list:
    - NEPRIFLAG: PRIMARY
    add_dfsrpair_list:
    - DFSRPAIRID: '10'
      DFSRMODE: FRER_PAIR
      PAIRDESCRIPTION: pair
    - DFSRPAIRID: '10'
      DFSRMODE: FRER_PAIR
      PAIRDESCRIPTION: pair
    add_dfsrpairmem_list:
    - DFSRPAIRID: 10
      IMSI: '86123456789'
    - DFSRPAIRID: 10
      IMSI: '86123456789'
    add_ngbinddfsrpair_list:
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRPAIRID: 10
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRPAIRID: 10
    set_dfsrattr_list_1:
    - NEPRIFLAG: SECONDARY
      PAIRUEACTTIME: 30
    mod_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      IGMPSNOOPINGSW: ENABLE
    set_igmpsnoopingattr_list:
    - VNINSTANCE: '000003e9-460-08-01'
      QUERIERSW: DISABLE
      QUERYINTERVAL: 60
      MAXRSPTIME: 10
      ROBUSTCOUNT: 2
    set_upethsrvpara_list_2:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    set_igmpsnoopingattr_list_1:
    - VNINSTANCE: '000003e9-460-08-01'
      QUERIERSW: ENABLE
      QUERYINTERVAL: 60
      MAXRSPTIME: 10
      ROBUSTCOUNT: 2
      SOURCEADDR: '192.168.0.1'
    add_multicastsource_list:
    - VNINSTANCE: '000003e9-460-08-01'
      MCSOURCETYPE: IMSI
      IMSI: '460123123456787'
    add_multicastsource_list_1:
    - VNINSTANCE: '000003e9-460-08-01'
      MCSOURCETYPE: DFSRPAIR
      DFSRPAIRID: 10
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置UDM数据

### + **ADD NGCQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令中的“NGCQOSTPLID”参数索引**ADD NGCQOSTPL**命令中的“TPLID”参数值。

### + **ADD SMDATA**命令中的“DNNQOSTPLID”参数索引**ADD DNNQOSTPL**命令中的“TPLID”参数值。

### 5G LAN QoS参数（5QI、ARP等）仅用于举例，实际请根据具体业务模型规划。

### 在“UDM业务管理”窗口下执行**LST NGS**命令和**LST VNGROUP**可查询5G LAN用户的“SNSSAI”、“DNN”、“INGROUPID”、“SHAREDID”、“PDUTYPES”等开户信息。

### 2~5是在“UDM业务管理”窗口下执行。具体为：先登录PGW WEBUI，然后在“应用类型”下拉框选择“UDM业务管理”。

### 从中心UDM（UDM）同步用户数据时，中心UDM（UDM）和园区UDM（UEG）配置说明如表5所示。

### **表5** 中心UDM（UDM）/园区UDM（UEG）配置说明

### | 配置项 | 中心UDM（UDM） | 园区UDM（UEG） |

### | --- | --- | --- |

### | 开启5G LAN License、配置5G LAN使用的DNN信息（5G QoS模板、DNN QoS模板） | 需要配置 | 需要配置 |

### | 签约会话管理数据、创建5G LAN组和增加5G LAN组成员 | 需要配置 | 不需要配置 |

#### 1.1 检查5G LAN License项是否开启。

##### 1.1.1 //显示信息中存在“LKQ7UDMBE15”控制项且取值不为0时，说明已开启5G LAN License。

#### 1.2 配置5G LAN使用的DNN信息。

##### 1.2.1 //创建5G QoS模板。

```jinja2
{%- for item in add_ngcqostpl_list -%}
    ADD NGCQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    NGQI={{item.NGQI}},
    ARPPRILEVEL={{item.ARPPRILEVEL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.PREEMPTIONCAP is not none -%}
        PREEMPTIONCAP={{item.PREEMPTIONCAP}},
    {%- endif -%}
    {%- if item.PREEMPTIONVUL is not none -%}
        PREEMPTIONVUL={{item.PREEMPTIONVUL}},
    {%- endif -%}
    {%- if item.NGQIPRILEVEL is not none -%}
        NGQIPRILEVEL={{item.NGQIPRILEVEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 //创建DNN QoS模板。

```jinja2
{%- for item in add_dnnqostpl_list -%}
    ADD DNNQOSTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    PDUTYPE={{item.PDUTYPE}},
    SSCMODE={{item.SSCMODE}},
    NGCQOSTPLID={{item.NGCQOSTPLID}},
    AMBRUP={{item.AMBRUP}},
    UPUNIT={{item.UPUNIT}},
    AMBRDW={{item.AMBRDW}},
    DWUNIT={{item.DWUNIT}},
    {#- --- 可选参数 --- -#}
    {%- if item.TPLNAME is not none -%}
        TPLNAME="{{item.TPLNAME}}",
    {%- endif -%}
    {%- if item.CHARGE is not none -%}
        CHARGE="{{item.CHARGE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 签约会话管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdata_list的变量区（command: ADD SMDATA） -#}
<!-- MISSING_MACRO: command=ADD SMDATA list_name=add_smdata_list step_id=1.3 -->
```

#### 1.4 创建5G LAN组。

##### 1.4.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“INGROUPID”、“EXTGROUPID”、“SHAREDID”取值必须不同。

```jinja2
{%- for item in add_vngroup_list -%}
    ADD VNGROUP:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    INGROUPID="{{item.INGROUPID}}",
    EXTGROUPID="{{item.EXTGROUPID}}",
    SHAREDID="{{item.SHAREDID}}",
    SNSSAI="{{item.SNSSAI}}",
    DNN="{{item.DNN}}",
    PDUTYPES={{item.PDUTYPES}},
    ;
{%- endfor -%}
```

#### 1.5 增加5G LAN组成员。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_groupid_list的变量区（command: ADD GROUPID） -#}
<!-- MISSING_MACRO: command=ADD GROUPID list_name=add_groupid_list step_id=1.5 -->
```

### 2 配置AMF数据

### AMF上配置的切片参数SST、SD与UDM开户时切片参数一致。可以复用已有切片，复用已有切片时，不需要执行如下配置。可通过**LST PLMNNS**查询。

#### 2.1 配置PLMN支持的切片。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_plmnns_list -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置AMF切片信息。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

#### 2.3 配置AMF对5G LAN切片下的DNN纠正。如现网已涉及DNN纠正功能（可通过**LST LOCALNSDNN**查询），则需要执行如下配置；否则，请跳过如下配置。

##### 2.3.1 //用户请求APN与签约APN不匹配时，优先纠正为签约数据中的Default DNN，如果未签约Default DNN，则纠正为dnn5glan01。

```jinja2
{%- for item in add_localnsdnn_list -%}
    ADD LOCALNSDNN:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    CORRECTTYPE={{item.CORRECTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    {#- --- 条件必选：CORRECTTYPE=DNN_CORRECTION 时必选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        DNNPLCY={{item.DNNPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CORRECTTYPE=NS_CORRECTION/DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE in ['NS_CORRECTION', 'DNN_CORRECTION'] -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CORRECTTYPE=DNN_CORRECTION 时可选 --- -#}
    {%- if item.CORRECTTYPE == 'DNN_CORRECTION' -%}
        {%- if item.DISFAILPLCY is not none -%}
            DISFAILPLCY={{item.DISFAILPLCY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置对端SMF实例支持的DNN。可以基于DNN选择SMF。

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 2.5 配置对端SMF实例支持的切片。可以基于切片选择SMF。复用已有切片时，不需要重复配置。

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SMF数据

### + **ADD PNFNS**命令存在多条时，“INDEX”不能重复。

### + **ADD PNFDNN**命令存在多条时，“INDEX”不能重复。

### + **ADD PNFDNN**命令中的“PNFNSINDEX”取值与**ADD PNFNS**命令定义的“INDEX”参数值一致。

#### 3.1 检查5G LAN License项是否开启。

##### 3.1.1 //显示信息中存在“LKV2SALANSM01”控制项时，说明已开启5G LAN License。

#### 3.2 配置SMF 5G LAN全局参数。

##### 3.2.1 //配置支持建立5G LAN会话。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSWITCH is not none -%}
        NGLANSWITCH={{item.NGLANSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.2 //配置对5G LAN UPF的选择机制。

```jinja2
{%- for item in set_upselectflag_list -%}
    SET UPSELECTFLAG:
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANUPFSELSW is not none -%}
        NGLANUPFSELSW={{item.NGLANUPFSELSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.3 //配置5G LAN关键信元。

```jinja2
{%- for item in set_pfcppvtext_list -%}
    SET PFCPPVTEXT:
    {#- --- 必选参数 --- -#}
    FEATURE={{item.FEATURE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置5G LAN使用的切片和专用DNN信息。

##### 3.3.1 //配置SMF支持的切片信息。可以复用已有切片，复用已有切片时，不需要执行如下配置。可通过**LST PLMNNS**查询。

```jinja2
{%- for item in add_plmnns_list_1 -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    {%- if item.STATE is not none -%}
        STATE={{item.STATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nfns_list_1 -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

##### 3.3.2 //配置SMF支持的DNN（APN）信息。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

##### 3.3.3 //配置网络切片支持DNN。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 3.4 配置支持5G LAN的SMF对端UPF实例信息。

##### 3.4.1 //配置对端UPF节点信息。同一个UPF对端只能配置一条ADD PNFPROFILE记录。如已配置对应的UPF节点信息，则不需要重复配置。

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {%- if item.UPFUNCTION is not none -%}
        UPFUNCTION={{item.UPFUNCTION}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfprofile_list -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
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

##### 3.4.2 //配置对端UPF支持的切片信息。如复用已有的对端UPF的切片信息，则不需要重复配置。推荐复用。

```jinja2
{%- for item in add_pnfns_list_1 -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.4.3 //配置对端UPF支持的DNN信息。

```jinja2
{%- for item in add_pnfdnn_list_1 -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PNFNSINDEX is not none -%}
        PNFNSINDEX={{item.PNFNSINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.4.4 //配置对端UPF支持5G LAN功能。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NGLANSW is not none -%}
        NGLANSW={{item.NGLANSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.4.5 //配置对端UPF的位置区域信息。如已配置的对端UPF的位置区域信息包含5G LAN业务对应的基站的TAI范围，则不需要重复配置。一个UPF服务区域可以绑定多个TAI范围，如利旧UPF服务区，且需要增加TAI范围，则可只通过**ADD UPAREABINDN2TAI**命令增加TAI范围。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

##### 3.4.6 //配置对端UPF的SMF服务区域信息。如利旧UPF服务区（area01），则不需要重复配置。一个UPF实例可以和多个UPF服务区绑定。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

#### 3.5 UPF上开启基于5G LAN组的粒度的层二环路消除功能时，开启环路检测开关。“GROUPID”取值与UPF上开启层二环路消除功能的5G LAN组名称一致。

```jinja2
{%- for item in add_grpnglanfunc_list -%}
    ADD GRPNGLANFUNC:
    {#- --- 必选参数 --- -#}
    GROUPID="{{item.GROUPID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LDRSW is not none -%}
        LDRSW={{item.LDRSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 配置5G LAN业务的缺省PCC规则。

##### 3.6.1 //关闭动态PCC功能。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.6.2 //关闭计费功能。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ONLINESW is not none -%}
        ONLINESW={{item.ONLINESW}},
    {%- endif -%}
    {%- if item.OFFLINESW is not none -%}
        OFFLINESW={{item.OFFLINESW}},
    {%- endif -%}
    {%- if item.CONVERGEDSW is not none -%}
        CONVERGEDSW={{item.CONVERGEDSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.6.3 //配置本地PCC策略。此处仅用于举例，如已配置本地PCC策略，则不需要重复配置。推荐复用。

```jinja2
{%- for item in add_cpurr_list -%}
    ADD CPURR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
        RG={{item.RG}},
    {%- endif -%}
    {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
    {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
        ONLINERG={{item.ONLINERG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
        {%- if item.N40AGESW is not none -%}
            N40AGESW={{item.N40AGESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
    {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
        {%- if item.VOLUMERSUVALUE is not none -%}
            VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cpurrgroup_list -%}
    ADD CPURRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cppccpolicygrp_list -%}
    ADD CPPCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.6.4 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- for item in add_usrprofgroup_list -%}
    ADD USRPROFGROUP:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cpuserprofile_list -%}
    ADD CPUSERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.UPSPECTYPE is not none -%}
        UPSPECTYPE={{item.UPSPECTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upbindupg_list -%}
    ADD UPBINDUPG:
    {#- --- 必选参数 --- -#}
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    UPBINDTYPE={{item.UPBINDTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPBINDTYPE=SPECIFIC/DEFAULT/ULCL 时必选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT', 'ULCL'] -%}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPBINDTYPE=SPECIFIC/DEFAULT 时可选 --- -#}
    {%- if item.UPBINDTYPE in ['SPECIFIC', 'DEFAULT'] -%}
        {%- if item.LOCALPCCSELECT is not none -%}
            LOCALPCCSELECT={{item.LOCALPCCSELECT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

##### 3.6.5 //配置规则和用户模板绑定。“POLICYNAME”采用**ADD CPPCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{%- for item in add_cprule_list -%}
    ADD CPRULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {%- if item.RULESPECTYPE is not none -%}
        RULESPECTYPE={{item.RULESPECTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.RULERANGE is not none -%}
            RULERANGE={{item.RULERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cprulebinding_list -%}
    ADD CPRULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置UPF数据

### 企业侧交换机与UPF之间建立VXLAN隧道的场景，两个VXLAN交换机是堆叠组网或M-LAG组网时，两个VXLAN交换机都是只需要提供一个VTEP IP。DCGW与UPF之间建立VXLAN隧道的场景，一对DCGW是M-LAG组网，一对DCGW只需要提供一个VTEP IP。

### 两个UPF是负荷分担容灾关系，且仅对接一对企业侧VXLAN交换机/DCGW时，支持两个UPF之间建立VXLAN隧道，用于实现跨UPF的终端互访。两个UPF之间建立VXLAN隧道时，需要分别在两个UPF上进行配置，VTEP IP是另一UPF的VXLAN隧道IP，如下以配置一个UPF为例。

### 不同的5G LAN组共用VTEP，一个5G LAN组对应一个VNI。如图9所示，VNI为5010和VNI为5011的两个VNI共用VTEP。

### **图9** VXLAN隧道数据规划图

#### 4.1 配置UPF 5G LAN全局参数。

##### 4.1.1 //开启5G LAN特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 4.1.2 //开启5G LAN功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

#### 4.2 配置UPF支持的DNN（APN）信息。

##### 4.2.1 //支持层二 5G LAN业务的DNN（APN）不需要绑定VPN实例。

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 4.3 配置UPF支持的5G LAN组。

##### 4.3.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“VNINSTANCE”取值必须不同。

```jinja2
{%- for item in add_ngvninstance_list -%}
    ADD NGVNINSTANCE:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNTYPE is not none -%}
        PDNTYPE={{item.PDNTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.MACIDLESW is not none -%}
            MACIDLESW={{item.MACIDLESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.IGMPSNOOPINGSW is not none -%}
            IGMPSNOOPINGSW={{item.IGMPSNOOPINGSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IGMPSNOOPINGSW=DISABLE 时可选 --- -#}
    {%- if item.IGMPSNOOPINGSW == 'DISABLE' -%}
        {%- if item.IGMPPARSESW is not none -%}
            IGMPPARSESW={{item.IGMPPARSESW}},
        {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- elif item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.IGMPPARSESW is not none -%}
            IGMPPARSESW={{item.IGMPPARSESW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.MULTIFLOODSW is not none -%}
            MULTIFLOODSW={{item.MULTIFLOODSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MULTIFLOODSW=ENABLE 时可选 --- -#}
    {%- if item.MULTIFLOODSW == 'ENABLE' -%}
        {%- if item.MULTIFLOODRATE is not none -%}
            MULTIFLOODRATE={{item.MULTIFLOODRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.BCASTFLOWCTRLSW is not none -%}
            BCASTFLOWCTRLSW={{item.BCASTFLOWCTRLSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.UNICASTFLOODSW is not none -%}
            UNICASTFLOODSW={{item.UNICASTFLOODSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PDNTYPE=ETHERNET 时可选 --- -#}
    {%- if item.PDNTYPE == 'ETHERNET' -%}
        {%- if item.N6MACIDLESW is not none -%}
            N6MACIDLESW={{item.N6MACIDLESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 配置VXLAN隧道。

##### 4.4.2 DCGW与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”必须设置为“\_public\_”。

##### 不存在绑定VPN实例为“\_public\_”的外联口及路由数据时，可参考N6接口配置用于传输UPF和DCGW之间VXLAN报文的外联口IP、路由数据（VPN实例为“\_public\_”）。

```jinja2
{%- if is_scenario_dcgw_vxlan_tunnel -%}
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

##### 4.4.3 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。此处以“VRF\_LocalDN01”为例。

##### 此处以复用N6接口的VPN实例为例。如使用独立的VPN实例，则需要执行**ADD VPNINST**命令及参考N6接口配置对应的外联口IP、路由数据（外联口绑定的VPN与VXLAN接口绑定的VPN相同）。

```jinja2
{%- if is_scenario_enterprise_switch_vxlan_tunnel -%}
    {%- for item in add_logicinf_list_1 -%}
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

##### 4.4.4 DCGW与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”必须设置为“\_public\_”。

##### 4.4.5 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。

##### 4.4.6 UPF与另一UPF之间建立VXLAN隧道的场景，复用UPF与DCGW/企业侧交换机之间建立VXLAN隧道的vxlanif接口。

##### 4.4.8 路径中的网络设备和对端都支持心跳消息（PING报文）时，请执行：

```jinja2
{%- if is_scenario_heartbeat_supported -%}
    {%- for item in add_vxlangrp_list -%}
        ADD VXLANGRP:
        {#- --- 必选参数 --- -#}
        GRPNAME="{{item.GRPNAME}}",
        SRCINTF="{{item.SRCINTF}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HEARTBEAT is not none -%}
            HEARTBEAT={{item.HEARTBEAT}},
        {%- endif -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
        {%- if item.HEARTSUCCLIMIT is not none -%}
            HEARTSUCCLIMIT={{item.HEARTSUCCLIMIT}},
        {%- endif -%}
        {%- if item.HEARTFAILLIMIT is not none -%}
            HEARTFAILLIMIT={{item.HEARTFAILLIMIT}},
        {%- endif -%}
        {%- if item.TIMEOUT is not none -%}
            TIMEOUT={{item.TIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.4.9 路径中的网络设备或对端不支持心跳消息（PING报文）时，请执行：

```jinja2
{%- if is_scenario_heartbeat_unsupported -%}
    {%- for item in add_vxlangrp_list_1 -%}
        ADD VXLANGRP:
        {#- --- 必选参数 --- -#}
        GRPNAME="{{item.GRPNAME}}",
        SRCINTF="{{item.SRCINTF}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HEARTBEAT is not none -%}
            HEARTBEAT={{item.HEARTBEAT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.4.10 //配置VXLAN隧道远端端点（VTEP：VXLAN交换机/DCGW），VTEPIPV4为远端端点IP，来源于企业侧交换机/DCGW的VXLAN隧道端点IP地址。

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

##### 4.4.11 //配置VXLAN隧道端点绑定VXLAN隧道组。存在多个负荷分担的VTEP时，“PRIFLAG”设置为“PRIMARY”。

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

#### 4.5 绑定5G LAN组与VXLAN隧道组。不同5G LAN组共用VXLAN隧道时，VNI必须不同。

```jinja2
{%- for item in add_ngvnbindvxlan_list -%}
    ADD NGVNBINDVXLAN:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    VXLANGRPNAME="{{item.VXLANGRPNAME}}",
    VNI={{item.VNI}},
    ;
{%- endfor -%}
```

#### 4.6 配置5G LAN业务的缺省PCC规则。

##### 4.6.1 //配置URR。如已配置，则不需要重复配置。推荐复用。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAPARA is not none -%}
            DFTQUOTAPARA={{item.DFTQUOTAPARA}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    {%- if item.EVENTCHARGEFLAG is not none -%}
        EVENTCHARGEFLAG={{item.EVENTCHARGEFLAG}},
    {%- endif -%}
    {%- if item.EVENTCHGPOINT is not none -%}
        EVENTCHGPOINT={{item.EVENTCHGPOINT}},
    {%- endif -%}
    {%- if item.MMSCHARGETYPE is not none -%}
        MMSCHARGETYPE={{item.MMSCHARGETYPE}},
    {%- endif -%}
    {%- if item.SIGNALASSOCIATE is not none -%}
        SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
    {%- endif -%}
    {%- if item.ADCMUTEFLAG is not none -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {%- if item.HTTP2DEGRADESW is not none -%}
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
    {%- endif -%}
    {%- if item.TOKENFUNCFLAG is not none -%}
        TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
    {%- endif -%}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.SIGURRGRPNAME is not none -%}
        SIGURRGRPNAME="{{item.SIGURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.6.2 //预定义规则场景，配置流过滤器，any-to-any。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_filteripv6_list -%}
    ADD FILTERIPV6:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPEV6={{item.L34PROTTYPEV6}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPEV6=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    {%- if item.FLOWFILTERTYPE is not none -%}
        FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

##### 4.6.3 //配置5G LAN业务相关的rule和userprofile。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TCPCHGPROFLAG is not none -%}
        TCPCHGPROFLAG={{item.TCPCHGPROFLAG}},
    {%- endif -%}
    {%- if item.DFTSIGURRGNAME is not none -%}
        DFTSIGURRGNAME="{{item.DFTSIGURRGNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 4.7 配置故障定界所需数据（执行**NGVNVIFPING**获取时延时依赖的数据）。

##### 4.7.1 //此处配置的是UPF发送的ping探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。

```jinja2
{%- for item in set_upethsrvpara_list -%}
    SET UPETHSRVPARA:
    {#- --- 必选参数 --- -#}
    UPETHSRVSW={{item.UPETHSRVSW}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UPETHSRVSW=ENABLE 时必选 --- -#}
    {%- if item.UPETHSRVSW == 'ENABLE' -%}
        UPETHSRVMAC="{{item.UPETHSRVMAC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.7.2 //基于5G LAN组配置ping探测报文的源IP地址。从DHCP Server获取，该IP地址等同于DHCP Server分配给5G LAN层二终端的IP地址，与5G LAN层二终端的IP地址在同一网段，且不能与5G LAN层二终端的IP地址冲突。

```jinja2
{%- for item in add_ngvnvif_list -%}
    ADD NGVNVIF:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    VIFIPTYPE={{item.VIFIPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：VIFIPTYPE=IPV4 时必选 --- -#}
    {%- if item.VIFIPTYPE == 'IPV4' -%}
        VIFIPV4ADDR="{{item.VIFIPV4ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.8 DCGW/企业侧交换机与UPF之间建立VXLAN隧道的场景，修改外联口MTU值。

##### 4.8.2 Ethernet接口组网时：

```jinja2
{%- if is_scenario_ethernet_if -%}
    {%- for item in mod_interface_list -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.8.3 Eth-trunk接口组网时：

```jinja2
{%- if is_scenario_eth_trunk_if -%}
    {%- for item in mod_interface_list_2 -%}
        MOD INTERFACE:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IFMTU is not none -%}
            IFMTU={{item.IFMTU}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.9 通过静态组播组实现层二5G LAN组播功能时，配置静态组播组。局点规划支持静态组播功能时（例如电力场景）需要配置，否则请跳过本步骤。

##### 4.9.1 //开启5G LAN层二静态组播的License配置开关。

```jinja2
{%- if is_scenario_static_multicast -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.9.2 //5G LAN终端发送组播报文时，报文中的目的MAC必须与此处配置的组播MAC（11-11-11-11-11-fc）一致。

```jinja2
{%- if is_scenario_static_multicast -%}
    {%- for item in add_multicastgrp_list -%}
        ADD MULTICASTGRP:
        {#- --- 必选参数 --- -#}
        MCASTGRPNAME="{{item.MCASTGRPNAME}}",
        MCASTMACADDR="{{item.MCASTMACADDR}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_multicast -%}
    {%- for item in add_ngbindmcastgrp_list -%}
        ADD NGBINDMCASTGRP:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        MCASTGRPNAME="{{item.MCASTGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_static_multicast -%}
    {%- for item in add_mcastgrpmem_list -%}
        ADD MCASTGRPMEM:
        {#- --- 必选参数 --- -#}
        MCASTGRPNAME="{{item.MCASTGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.MEMTYPE is not none -%}
            MEMTYPE={{item.MEMTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MEMTYPE=IMSI 时必选 --- -#}
        {%- if item.MEMTYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：MEMTYPE=VTEP 时必选 --- -#}
        {%- if item.MEMTYPE == 'VTEP' -%}
            VTEPNAME="{{item.VTEPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.10 禁止通过N9口实现终端互访的场景，配置漫游5G LAN终端通过白名单实现与同一5G LAN组内的其他终端互访。

##### 4.10.1 //此处以基于5G LAN组+白名单方案允许漫游5G LAN终端与该5G LAN组中的其他终端互访，互访报文包括单播、组播和广播为例。

```jinja2
{%- for item in set_ngvnuemutacc_list -%}
    SET NGVNUEMUTACC:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.N9AUE2UEUNIPOL is not none -%}
        N9AUE2UEUNIPOL={{item.N9AUE2UEUNIPOL}},
    {%- endif -%}
    {%- if item.N9AUE2UEMULPOL is not none -%}
        N9AUE2UEMULPOL={{item.N9AUE2UEMULPOL}},
    {%- endif -%}
    {%- if item.N9AUE2UEBROPOL is not none -%}
        N9AUE2UEBROPOL={{item.N9AUE2UEBROPOL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.10.2 //此处以允许漫游5G LAN终端通过5个I-UPF的N9口与锚点UPF交互为例，实际请根据局点实际业务规划配置白名单。白名单中的IP地址，是与锚点UPF互通的I-UPF的N9口IP。

```jinja2
{%- for item in add_uemutaccwlist_list -%}
    ADD UEMUTACCWLIST:
    {#- --- 必选参数 --- -#}
    WLISTNAME="{{item.WLISTNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4START="{{item.IPV4START}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4END="{{item.IPV4END}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngbinduemutwl_list -%}
    ADD NGBINDUEMUTWL:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    WLISTNAME="{{item.WLISTNAME}}",
    ;
{%- endfor -%}
```

#### 4.11 配置UPF对上行5G LAN层二报文的VLAN0进行剥除。

```jinja2
{%- for item in set_upsoftpara_list -%}
    SET UPSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.12 配置基于5G LAN组粒度的层二环路消除功能。

##### 4.12.1 CPE支持UPF发送的主动检测环路的报文，该场景下，推荐采用主动检测方案。

###### 4.12.1.1 //开启License开关。主动检测和被动检测时均需要配置。

```jinja2
{%- if is_scenario_active_detection -%}
    {%- for item in set_licenseswitch_list_3 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 4.12.1.2 //开启主动检测开关。

```jinja2
{%- if is_scenario_active_detection -%}
    {%- for item in set_ngloopdetfunc_list -%}
        SET NGLOOPDETFUNC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ETHLOOPDETECTSW is not none -%}
            ETHLOOPDETECTSW={{item.ETHLOOPDETECTSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ETHLOOPDETECTSW=ENABLE 时可选 --- -#}
        {%- if item.ETHLOOPDETECTSW == 'ENABLE' -%}
            {%- if item.DETECTMETHOD is not none -%}
                DETECTMETHOD={{item.DETECTMETHOD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 4.12.1.3 //此处配置的是UPF发送的环路探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。

```jinja2
{%- if is_scenario_active_detection -%}
    {%- for item in set_upethsrvpara_list_1 -%}
        SET UPETHSRVPARA:
        {#- --- 必选参数 --- -#}
        UPETHSRVSW={{item.UPETHSRVSW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPETHSRVSW=ENABLE 时必选 --- -#}
        {%- if item.UPETHSRVSW == 'ENABLE' -%}
            UPETHSRVMAC="{{item.UPETHSRVMAC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.12.2 CPE不支持UPF发送的主动检测环路报文，该场景下，可采用被动检测方案。

###### 4.12.2.1 //开启License开关。主动检测和被动检测时均需要配置。

```jinja2
{%- if is_scenario_passive_detection -%}
    {%- for item in set_licenseswitch_list_4 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 4.12.2.2 //配置被动检测参数。

```jinja2
{%- if is_scenario_passive_detection -%}
    {%- for item in set_ngloopdetfunc_list_1 -%}
        SET NGLOOPDETFUNC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ETHLOOPDETECTSW is not none -%}
            ETHLOOPDETECTSW={{item.ETHLOOPDETECTSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ETHLOOPDETECTSW=ENABLE 时可选 --- -#}
        {%- if item.ETHLOOPDETECTSW == 'ENABLE' -%}
            {%- if item.DETECTMETHOD is not none -%}
                DETECTMETHOD={{item.DETECTMETHOD}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DETECTMETHOD=MAC_FLAP_NUM 时可选 --- -#}
        {%- if item.DETECTMETHOD == 'MAC_FLAP_NUM' -%}
            {%- if item.MACFLAPNUM is not none -%}
                MACFLAPNUM={{item.MACFLAPNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.13 配置FRER双发选收功能。工业冗余协议交换机支持FRER冗余协议时，UPF支持FRER双发选收功能。

##### 4.13.1 //在主用UPF上开启本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list_5 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 4.13.2 //在主用UPF上进行如下配置：

```jinja2
{%- for item in set_ngdfsrfunc_list -%}
    SET NGDFSRFUNC:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    DFSRSWITCH={{item.DFSRSWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_dfsrattr_list -%}
    SET DFSRATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.NEPRIFLAG is not none -%}
        NEPRIFLAG={{item.NEPRIFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dfsrpair_list的变量区（command: ADD DFSRPAIR） -#}
<!-- MISSING_MACRO: command=ADD DFSRPAIR list_name=add_dfsrpair_list step_id=4.13.2 -->
```

```jinja2
{%- for item in add_dfsrpairmem_list -%}
    ADD DFSRPAIRMEM:
    {#- --- 必选参数 --- -#}
    DFSRPAIRID={{item.DFSRPAIRID}},
    IMSI="{{item.IMSI}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngbinddfsrpair_list -%}
    ADD NGBINDDFSRPAIR:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    DFSRPAIRID={{item.DFSRPAIRID}},
    ;
{%- endfor -%}
```

##### 4.13.4 //在备用UPF上进行如下配置：

```jinja2
{%- for item in set_dfsrattr_list_1 -%}
    SET DFSRATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.NEPRIFLAG is not none -%}
        NEPRIFLAG={{item.NEPRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NEPRIFLAG=SECONDARY 时必选 --- -#}
    {%- if item.NEPRIFLAG == 'SECONDARY' -%}
        PAIRUEACTTIME={{item.PAIRUEACTTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.14 通过IGMP动态组播组实现层二5G LAN组播功能时，配置IGMP Snooping。局点规划支持IGMP动态组播功能时需要配置，否则请跳过本步骤。

##### 4.14.1 //开启IGMP Snooping功能开关。

```jinja2
{%- if is_scenario_igmp_multicast -%}
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
            {%- if item.IGMPSNOOPINGSW is not none -%}
                IGMPSNOOPINGSW={{item.IGMPSNOOPINGSW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.14.2 //网络中其他设备作为查询器时，在UPF上配置Query参数。UPF作为查询器时，请跳过本步骤。

```jinja2
{%- if is_scenario_igmp_multicast -%}
    {%- for item in set_igmpsnoopingattr_list -%}
        SET IGMPSNOOPINGATTR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        QUERIERSW={{item.QUERIERSW}},
        {#- --- 可选参数 --- -#}
        {%- if item.QUERYINTERVAL is not none -%}
            QUERYINTERVAL={{item.QUERYINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRSPTIME is not none -%}
            MAXRSPTIME={{item.MAXRSPTIME}},
        {%- endif -%}
        {%- if item.ROBUSTCOUNT is not none -%}
            ROBUSTCOUNT={{item.ROBUSTCOUNT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.14.3 //网络中无查询器时，在UPF上配置Query功能。网络中其他设备作为查询器时，请跳过本步骤。

```jinja2
{%- if is_scenario_igmp_multicast -%}
    {%- for item in set_upethsrvpara_list_2 -%}
        SET UPETHSRVPARA:
        {#- --- 必选参数 --- -#}
        UPETHSRVSW={{item.UPETHSRVSW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：UPETHSRVSW=ENABLE 时必选 --- -#}
        {%- if item.UPETHSRVSW == 'ENABLE' -%}
            UPETHSRVMAC="{{item.UPETHSRVMAC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_igmp_multicast -%}
    {%- for item in set_igmpsnoopingattr_list_1 -%}
        SET IGMPSNOOPINGATTR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        QUERIERSW={{item.QUERIERSW}},
        {#- --- 可选参数 --- -#}
        {%- if item.QUERYINTERVAL is not none -%}
            QUERYINTERVAL={{item.QUERYINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRSPTIME is not none -%}
            MAXRSPTIME={{item.MAXRSPTIME}},
        {%- endif -%}
        {%- if item.ROBUSTCOUNT is not none -%}
            ROBUSTCOUNT={{item.ROBUSTCOUNT}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QUERIERSW=ENABLE 时可选 --- -#}
        {%- if item.QUERIERSW == 'ENABLE' -%}
            {%- if item.SOURCEADDR is not none -%}
                SOURCEADDR="{{item.SOURCEADDR}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.14.4 //组播源在N3侧且组播源是IMSI时需要配置，否则不需要配置。

```jinja2
{%- if is_scenario_igmp_multicast -%}
    {%- for item in add_multicastsource_list -%}
        ADD MULTICASTSOURCE:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        MCSOURCETYPE={{item.MCSOURCETYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MCSOURCETYPE=IMSI 时必选 --- -#}
        {%- if item.MCSOURCETYPE == 'IMSI' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.14.5 //组播源在N3侧且播源是双发选收结对时需要配置，否则不需要配置。

```jinja2
{%- if is_scenario_igmp_multicast -%}
    {%- for item in add_multicastsource_list_1 -%}
        ADD MULTICASTSOURCE:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        MCSOURCETYPE={{item.MCSOURCETYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：MCSOURCETYPE=DFSRPAIR 时必选 --- -#}
        {%- if item.MCSOURCETYPE == 'DFSRPAIR' -%}
            DFSRPAIRID={{item.DFSRPAIRID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置LSW/DCGW数据

### 企业侧交换机与UPF之间建立VXLAN隧道的场景

### 请参考配置企业DN侧交换机。

### DCGW与UPF之间建立VXLAN隧道的场景

### 请参考对应型号的DCGW的配置。

### 6 配置无线基站数据

### 请参考配置无线基站。

### 7 配置CPE数据

### 请参考配置CPE终端。

