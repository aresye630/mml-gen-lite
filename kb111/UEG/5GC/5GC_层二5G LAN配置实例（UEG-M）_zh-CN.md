---
id: ''
name: 层二5G LAN配置实例（UEG-M）
ne_type: UEG
type: feature
description: 园区部署两套UEG-M，非应急场景下，两套UEG-M是负荷分担组网或主备容灾组网；应急场景下，两套UEG-M是负荷分担容灾模式。不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。 * 企业侧交换机与UPF之间建立VXLAN隧道的场景，图1~图8中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。 * DCGW与UPF之间建立VXLAN隧道的场景，图2~图8中的Firewall、LSW仅用于举例，5G LAN业务对Firewall、LSW数量无特殊要求。  **表1** 5G LAN组网及报文路径  | 业务场景 | 负荷分担容灾模式 | 主备容灾模式 | | --- | --- | --- | | 场景一：5G LAN层二终端与Server（Main PLC/MES/...）互通 | 组网如图1/图2所示。  负荷分担容灾组网时，两个UEG-M均处理业务，5G LAN层二终端通过某一UEG-M与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 仅非应急场景下支持，风筝M应急场景下仅支持负荷分担容灾模式。  组网如图6所示。  主备容灾组网时，同一时刻，只有一套UEG-M处理业务，5G LAN层二终端通过主用UPF与Server（Main PLC/MES/...）互通。另一套UEG-M不处理业务（冷备状态）。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | | 场景二：同一5G LAN组的层二终端之间互通 | 组网如图3所示。  两套UEG-M是负荷分担容灾组网时，同一5G LAN组下不同终端通过同一UEG-M或不同UEG-M接入。如同一5G LAN组下无线接入的终端通过不同UPF互通：  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。 * DCGW与UPF之间建立VXLAN隧道的场景，若两个UPF仅对接一对DCGW，可通过UPF之间的VxLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图3以两对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 仅非应急场景下支持，风筝M应急场景下仅支持负荷分担容灾模式。  组网如图8所示。  两套UEG-M是主备容灾组网时，同一5G LAN组下无线接入的终端可通过同一UPF直接互通，不需要经过LSW/DCGW。  说明：  * 两套UEG-M是主备容灾组网时，容灾恢复场景需要手动执行**DEA SESSION**将备用UPF上的5G LAN用户去活。若无层二5G LAN终端互通诉求，则容灾恢复场景下不需要在备用UPF上去活5G LAN用户。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 |  当存在如下情况时，可以参考本页面进行配置。  * CPE下挂多个终端（最多16个）。 * 同一个二层广播域内的终端IP必须不同。 * 支持如下几种典型业务场景：   + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。      Server（Main PLC/MES/...）部署在N6侧。   + 同一5G LAN组的层二终端之间通过同一UPF互通。   + 同一5G LAN组的层二终端之间通过不同UPF互通。     - 企业侧交换机与UPF之间建立VXLAN隧道的场景        该业务场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。     - DCGW与UPF之间建立VXLAN隧道的场景        两个UPF是负荷分担关系，且仅对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。  **图1** UEG-M负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）  **图2** UEG-M负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）  **图3** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，企业侧交换机与UPF之间建立VXLAN隧道）  * 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。 * 两组LSW之间，通过直连线互通或者其他LSW互通。  **图4** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，DCGW与UPF之间建立VXLAN隧道）  * 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。 * 两组DCGW之间，通过直连线互通或通过其他LSW互通。  **图5** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，UPF与另一UPF之间建立VXLAN隧道）  两个UPF是负荷分担关系，且仅对接一对DCGW/企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  **图6** UEG-M主备组网（非应急场景下，5G LAN层二终端与APP Server互通，企业侧交换机与UPF之间建立VXLAN隧道）  **图7** UEG-M主备组网（非应急场景下，5G LAN层二终端与APP Server互通，DCGW与UPF之间建立VXLAN隧道）  **图8** UEG-M主备组网（非应急场景下，同一5G LAN组的层二终端之间互通）
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","配置实例","层二5G LAN配置实例（UEG-M）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
园区部署两套UEG-M，非应急场景下，两套UEG-M是负荷分担组网或主备容灾组网；应急场景下，两套UEG-M是负荷分担容灾模式。不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。* 企业侧交换机与UPF之间建立VXLAN隧道的场景，图1~图8中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。* DCGW与UPF之间建立VXLAN隧道的场景，图2~图8中的Firewall、LSW仅用于举例，5G LAN业务对Firewall、LSW数量无特殊要求。**表1** 5G LAN组网及报文路径| 业务场景 | 负荷分担容灾模式 | 主备容灾模式 || --- | --- | --- || 场景一：5G LAN层二终端与Server（Main PLC/MES/...）互通 | 组网如图1/图2所示。  负荷分担容灾组网时，两个UEG-M均处理业务，5G LAN层二终端通过某一UEG-M与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 仅非应急场景下支持，风筝M应急场景下仅支持负荷分担容灾模式。  组网如图6所示。  主备容灾组网时，同一时刻，只有一套UEG-M处理业务，5G LAN层二终端通过主用UPF与Server（Main PLC/MES/...）互通。另一套UEG-M不处理业务（冷备状态）。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 || 场景二：同一5G LAN组的层二终端之间互通 | 组网如图3所示。  两套UEG-M是负荷分担容灾组网时，同一5G LAN组下不同终端通过同一UEG-M或不同UEG-M接入。如同一5G LAN组下无线接入的终端通过不同UPF互通：  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。 * DCGW与UPF之间建立VXLAN隧道的场景，若两个UPF仅对接一对DCGW，可通过UPF之间的VxLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图3以两对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 | 仅非应急场景下支持，风筝M应急场景下仅支持负荷分担容灾模式。  组网如图8所示。  两套UEG-M是主备容灾组网时，同一5G LAN组下无线接入的终端可通过同一UPF直接互通，不需要经过LSW/DCGW。  说明：  * 两套UEG-M是主备容灾组网时，容灾恢复场景需要手动执行**DEA SESSION**将备用UPF上的5G LAN用户去活。若无层二5G LAN终端互通诉求，则容灾恢复场景下不需要在备用UPF上去活5G LAN用户。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在企业侧VXLAN交换机上或独立的网关设备上。 |当存在如下情况时，可以参考本页面进行配置。* CPE下挂多个终端（最多16个）。* 同一个二层广播域内的终端IP必须不同。* 支持如下几种典型业务场景：  + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。    Server（Main PLC/MES/...）部署在N6侧。  + 同一5G LAN组的层二终端之间通过同一UPF互通。  + 同一5G LAN组的层二终端之间通过不同UPF互通。    - 企业侧交换机与UPF之间建立VXLAN隧道的场景      该业务场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。    - DCGW与UPF之间建立VXLAN隧道的场景      两个UPF是负荷分担关系，且仅对接一对DCGW时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。**图1** UEG-M负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，企业侧交换机与UPF之间建立VXLAN隧道）**图2** UEG-M负荷分担组网（5G LAN层二终端与Server（Main PLC/MES/...）互通，DCGW与UPF之间建立VXLAN隧道）**图3** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，企业侧交换机与UPF之间建立VXLAN隧道）* 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。* 两组LSW之间，通过直连线互通或者其他LSW互通。**图4** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，DCGW与UPF之间建立VXLAN隧道）* 两个UPF是负荷分担关系，且连接到不同对企业侧VXLAN交换机时，5G LAN成员之间跨UPF的互访可通过UPF与企业侧VXLAN交换机之间的VxLAN隧道实现。* 两组DCGW之间，通过直连线互通或通过其他LSW互通。**图5** UEG-M负荷分担组网（同一5G LAN组的层二终端之间互通，UPF与另一UPF之间建立VXLAN隧道）两个UPF是负荷分担关系，且仅对接一对DCGW/企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。**图6** UEG-M主备组网（非应急场景下，5G LAN层二终端与APP Server互通，企业侧交换机与UPF之间建立VXLAN隧道）**图7** UEG-M主备组网（非应急场景下，5G LAN层二终端与APP Server互通，DCGW与UPF之间建立VXLAN隧道）**图8** UEG-M主备组网（非应急场景下，同一5G LAN组的层二终端之间互通）

## 必备事项
前提条件

前提条件

* 除5G LAN业务外，UEG-M支持的5G SA业务运行正常。
* 企业侧交换机与UPF之间建立VXLAN隧道的场景，UPF和LSW之间的VXLAN隧道路径中存在防火墙时，防火墙需要放通VXLAN隧道IP地址（端口any，动态分配端口）对应的流量。
* 5GC与N6侧网络环境已构建完成。
  + 企业侧交换机与UPF之间建立VXLAN隧道的场景

    两个UEG-M是负荷分担容灾模式，且同一5G LAN组内的终端存在互通诉求时，若LSW不支持将通过VXLAN隧道接收的报文再通过VXLAN转发出去，则每个UPF需对接2个LSW用于建立VXLAN隧道，那么两个UPF就需要4个LSW。如图3所示。
  + DCGW与UPF之间建立VXLAN隧道的场景

    两个UPF是负荷分担关系，且仅对接一对DCGW时，可通过UPF之间的VxlAN隧道实现跨UPF的终端互访。每个UPF独自对接一对DCGW时，可通过DCGW与UPF之间的VXLAN隧道实现跨UPF的终端互访。
* 已加载License文件，且包含如下License控制项：
  + UDM：LKQ7UDMBE15 5G LAN签约用户数
  + SMF：LKV2SALANSM01 5G LAN业务基本功能-USM、LKV2CUFMN01 CU FullMesh组网
  + UPF：LKV3G5LANB01 5G LAN基础功能、LKV3G5CUFM01 CU Full Mesh组网

    如下几个License控制项需基于实际业务申请：
    - LKV3G5L2SMUL 层二静态组播
    - LKV3G5LADFSR 5G LAN双发选收会话数
  + PCF：LRM0PCFTC137 N7接口（使用HTTP协议）策略控制
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
          name: 'IMSI'
          type: string
          required: false
          description: ''
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
          name: 'DNN'
          type: string
          required: false
          description: ''
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
          name: '内部组ID'
          type: string
          minLength: 10
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTGROUPID:
          name: '外部组ID'
          type: string
          minLength: 3
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHAREDID:
          name: '共享数据ID'
          type: string
          maxLength: 64
          required: true
          description: ''
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
          name: '数据网名称'
          type: string
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDUTYPES:
          name: '允许的PDU类型'
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
    add_groupid_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INGROUPID:
          name: 'INGROUPID'
          type: string
          required: false
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
        DNN:
          name: 'DNN'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
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
    add_cfgsnssai_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: 'SST'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: 'SD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISACTIVE:
          name: 'ISACTIVE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: 'DESC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tacgroupinnssf_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TACGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTART:
          name: 'TACSTART'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACEND:
          name: 'TACEND'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_amfsetid_list:
      type: items
      properties:
        INDEX:
          name: 'INDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: 'SST'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: 'SD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: 'MCC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: 'MNC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGIONID:
          name: 'REGIONID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMFSETID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TACGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
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
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
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
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
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
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
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
    add_pnfdnn_list_2:
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
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
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
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
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
          name: 'UPF服务区名称支持的5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
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
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITYFLAG:
          name: '基于优先级优选UPF开关'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COMBINEDSELSTG:
          name: '选择合一UPF的优先级和容量策略'
          type: string
          enum:
          - TAIPRI
          - APNPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apnuprecover_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTERUPFID:
          name: '主UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HANDLINGMODE:
          name: 'UP链路故障恢复处理模式'
          type: string
          enum:
          - NOHANDLING
          - BACKMIGRATION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BACKUPFID:
          name: '备UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upcscanrate_list:
      type: items
      properties:
        SCANTYPE:
          name: '扫描任务类型'
          type: string
          enum:
          - DEACTIVE
          - CHECK
          - DAILYCHECK
          - MIGRATE
          - ADDRDEACTIVE
          - INERTIALOPERATION
          - UPPATHFAULT
          - GTPUPATHFAULT
          - APNFAULT
          - PATHFAULTMIGRATE
          - PATHMIGRATE
          - BACKMIGRATION
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATE:
          name: '扫描速率(个/秒)'
          type: integer
          minimum: 0
          maximum: 300
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTERVAL:
          name: '扫描间隔（秒）'
          type: integer
          minimum: 1
          maximum: 60
          required: false
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
          description: ''
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
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
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
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    set_apnpccfunc_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
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
        PCFSELECTMODE:
          name: '选择PCF方式'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfdnn_list_4:
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
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnchargectrl_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
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
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    set_apnchargectrl_list_2:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
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
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: 'URRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URRID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: 'USAGERPTMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: 'OFFCOMPOUNDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RG:
          name: 'RG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: 'OFFMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40AGESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: 'ONLCOMPOUNDTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINERG:
          name: 'ONLINERG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: 'ONLMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: 'VOLUMERSUVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_pccpolicygrp_list_1:
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
    add_cppccpolicygrp_list_1:
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
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPTYPE:
          name: 'UPTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSPECTYPE:
          name: 'UPSPECTYPE'
          type: string
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
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
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
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrprofgroup_list_1:
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
    add_upbindupg_list_1:
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
    add_apnusrprofg_list_1:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: ''
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
    set_cpurrgrpbinding_list:
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
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: 'POLICYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: 'PRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: 'RULERANGE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULESPECTYPE:
          name: 'RULESPECTYPE'
          type: string
          required: false
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
          required: false
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
    add_conditiongroup_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_condition_list:
      type: items
      properties:
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONNAME:
          name: 'CONDITIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OBJECTATTRIBUTE:
          name: 'OBJECTATTRIBUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPERATOR:
          name: 'OPERATOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUETYPE:
          name: 'RIGHTVALUETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RIGHTVALUE:
          name: 'RIGHTVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaction_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list_10:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list_13:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: 'VOLUMEUSAGEROUNDING'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ruleconditiongroup_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONDITIONGROUPNAME:
          name: 'CONDITIONGROUPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulengaction_list:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policy_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policyrule_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policytrigger_list:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICETYPE:
          name: 'SERVICETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: 'ACTIVATEDBY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QOSMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: 'SUBSCRIPTIONFORCED'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROBILLDATE:
          name: 'PROBILLDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: 'QUOTAALLOCATIONMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: 'ISSETSHAREDMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: 'ISGROUPSERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: 'ISTEMPLATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: 'ISRECUSRLOC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APNMATCHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: 'HASBASESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: 'CALCVALIDFORDYNSUBGROUP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: 'CUSTOMIZEDRESET'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTER2MASTERSHARESERVICE:
          name: 'MASTER2MASTERSHARESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_servicepolicy_list:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngaction_list_10:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngactionattr_list_34:
      type: items
      properties:
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ATTRNAME:
          name: 'ATTRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: 'VALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list_3:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMEUSAGEROUNDING:
          name: 'VOLUMEUSAGEROUNDING'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDR:
          name: 'EDR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RELATION:
          name: 'RELATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulengaction_list_2:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIONNAME:
          name: 'ACTIONNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policy_list_1:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policyrule_list_2:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_policytrigger_list_1:
      type: items
      properties:
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRIGGERNAME:
          name: 'TRIGGERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_service_list_1:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICETYPE:
          name: 'SERVICETYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACTIVATEDBY:
          name: 'ACTIVATEDBY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRECEDENCE:
          name: 'PRECEDENCE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSMODE:
          name: 'QOSMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBSCRIPTIONFORCED:
          name: 'SUBSCRIPTIONFORCED'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: 'DESCRIPTION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROBILLDATE:
          name: 'PROBILLDATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUOTAALLOCATIONMODE:
          name: 'QUOTAALLOCATIONMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISSETSHAREDMODE:
          name: 'ISSETSHAREDMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RESUBSCRIPTIONOPERATION:
          name: 'RESUBSCRIPTIONOPERATION'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISGROUPSERVICE:
          name: 'ISGROUPSERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISTEMPLATE:
          name: 'ISTEMPLATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISRECUSRLOC:
          name: 'ISRECUSRLOC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNMATCHTYPE:
          name: 'APNMATCHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HASBASESERVICE:
          name: 'HASBASESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDONLEVEL:
          name: 'ADDONLEVEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALCVALIDFORDYNSUBGROUP:
          name: 'CALCVALIDFORDYNSUBGROUP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CUSTOMIZEDRESET:
          name: 'CUSTOMIZEDRESET'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTER2MASTERSHARESERVICE:
          name: 'MASTER2MASTERSHARESERVICE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_servicepolicy_list_1:
      type: items
      properties:
        SERVICENAME:
          name: 'SERVICENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
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
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngvninstance_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: ''
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
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
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
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
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
          name: '隧道对端端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
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
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
    add_pccpolicygrp_list_2:
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
    add_rule_list_4:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: 'POLICYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: 'FILTERINGMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: 'FLOWFILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list_1:
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
    add_urr_list_4:
      type: items
      properties:
        URRNAME:
          name: 'URRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URRID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: 'USAGERPTMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: 'OFFMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: 'ONLMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAPARA:
          name: 'DFTQUOTAPARA'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list_2:
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
    add_urr_list_6:
      type: items
      properties:
        URRNAME:
          name: 'URRNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRID:
          name: 'URRID'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: 'USAGERPTMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: 'OFFMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLMETERINGTYPE:
          name: 'ONLMETERINGTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAPARA:
          name: 'DFTQUOTAPARA'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list_3:
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
    add_pccpolicygrp_list_3:
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
    add_filter_list_1:
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
    add_filteripv6_list_1:
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
    add_flowfilter_list_1:
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
    add_fltbindflowf_list_2:
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
    add_rule_list_5:
      type: items
      properties:
        RULENAME:
          name: 'RULENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: 'POLICYTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: 'FILTERINGMODE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: 'FLOWFILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: 'POLICYNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list_2:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list_2:
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
    set_urrgrpbinding_list_1:
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
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
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
    set_refreshsrv_list_1:
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
    set_nglanchgctrl_list:
      type: items
      properties:
        OFFLOCCHGPLYSW:
          name: '5G LAN本地离线计费策略开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
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
          name: '5G LAN组名称'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - ETHERNET
          - IP
          required: false
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: ''
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
    add_cfgsnssai_list:
    - INDEX: '1'
      MCC: '123'
      MNC: '03'
      SST: '1'
      SD: '010101'
      ISACTIVE: TRUE
      DESC: 5G_LAN
    add_tacgroupinnssf_list:
    - INDEX: '1'
      TACGROUPNAME: 1-010101
      TACSTART: '290100'
      TACEND: '290110'
    add_amfsetid_list:
    - INDEX: '1'
      SST: '1'
      SD: '010101'
      MCC: '123'
      MNC: '03'
      REGIONID: 08
      AMFSETID: 088
      TACGROUPNAME: 1-010101
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
    add_apn_list:
    - APN: 'dnn5glan01'
    add_cpapn_list:
    - APN: 'dnn5glan01'
    add_nsdnn_list:
    - NSIDX: 1
      DNN: 'dnn5glan01'
    add_pnfprofile_list:
    - NFINSTANCEID: 'upf_instance_1'
      NFTYPE: NfUPF
      FQDN: '5glan01.upf1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '119.5.52.2'
      PORT: 8805
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'upf_instance_1'
      SST: 1
      SD: '010101'
    add_pnfdnn_list:
    - INDEX: 0
      NFINSTANCEID: 'upf_instance_1'
      DNN: 'dnn5glan01'
      PNFNSINDEX: 1
    add_pnfdnn_list_2:
    - INDEX: 0
      NFINSTANCEID: 'upf_instance_1'
      DNN: 'dnn5glan01'
      PNFNSINDEX: 1
      PRISWITCH: SPECIFIC
      PRIORITY: 1
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
    set_apnupselply_list:
    - APN: 'dnn5glan01'
      PRIORITYFLAG: ENABLE
      COMBINEDSELSTG: APNPRI
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1066
      VALUE: VALUE_1
      POSITION: 29
    add_apnuprecover_list:
    - APN: 'dnn5glan01'
      MASTERUPFID: 'upf_instance_1'
      HANDLINGMODE: BACKMIGRATION
      BACKUPFID: 'upf_instance_2'
    set_upcscanrate_list:
    - SCANTYPE: BACKMIGRATION
      RATE: 10
      INTERVAL: 5
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
    set_apnpccfunc_list_1:
    - APN: 'dnn5glan01'
      HOMEPCCSWITCH: ENABLE
      PCFSELECTMODE: DNN-1&GPSI-0&IMSI-0&NFLOC-0&PLMN-0&SERVINGSCOPE-0&SNSSAIS-0
    add_pnfdnn_list_4:
    - INDEX: 10
      NFINSTANCEID: 'PCF_Instance_1'
      DNN: 'dnn5glan01'
    set_apnchargectrl_list_1:
    - APN: 'dnn5glan01'
      CONVERGEDSW: ENABLE
      RGAPPLIED: OFFLINERGONLY
    set_apnpccfunc_list_2:
    - APN: 'dnn5glan01'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    set_apnchargectrl_list_2:
    - APN: 'dnn5glan01'
      CONVERGEDSW: ENABLE
      RGAPPLIED: OFFLINERGONLY
    add_urr_list:
    - URRNAME: 5glan_urr_offline
      URRID: '2222'
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: '2222'
      OFFMETERINGTYPE: VOLUME
      N40AGESW: ENABLE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: '1111'
      ONLMETERINGTYPE: VOLUME
      VOLUMERSUVALUE: '0'
    add_urrgroup_list:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr_offline'
      DOWNURRNAME1: '5glan_urr_offline'
      UPURRNAME2: '5glan_urr_online'
      DOWNURRNAME2: '5glan_urr_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      URRGROUPNAME: '5glan_urrgroup'
      FUPSESSIONEXC: DISABLE
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      FUPSESSIONEXC: DISABLE
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
    add_cppccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'pccpolicy_group'
      FUPSESSIONEXC: DISABLE
    add_usrprofgroup_list:
    - USERPROFGNAME: 'profilegroupfglan'
    add_userprofile_list:
    - USERPROFILENAME: fglan_u_p_any
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
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      DFTURRGRPNAME: '5glan_urrgroup'
    add_usrprofgroup_list_1:
    - USERPROFGNAME: 'profilegroupfglan'
    add_cpuserprofile_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      UPTYPE: PCC
      UPSPECTYPE: DEFAULT
    add_upbindupg_list_1:
    - USERPROFGNAME: 'profilegroupfglan'
      UPBINDTYPE: DEFAULT
      USERPROFILENAME: 'fglan_u_p_any'
      LOCALPCCSELECT: INHERIT
    add_apnusrprofg_list_1:
    - APN: 'dnn5glan01'
      USERPROFGNAME: 'profilegroupfglan'
    set_cpurrgrpbinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      DFTURRGRPNAME: '5glan_urrgroup'
    add_rule_list:
    - RULENAME: fglan_r_any
      POLICYTYPE: PCC
      POLICYNAME: pccpolicy_group
      PRIORITY: '65535'
      RULERANGE: ALL
      RULESPECTYPE: DEFAULT
    add_rulebinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
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
    add_conditiongroup_list:
    - CONDITIONGROUPNAME: 5glan_CG
      RELATION: AND
    add_condition_list:
    - CONDITIONGROUPNAME: 5glan_CG
      CONDITIONNAME: 5glan_Condition
      OBJECTATTRIBUTE: SmfSession.Dnn
      OPERATOR: Equal
      RIGHTVALUETYPE: Value
      RIGHTVALUE: dnn5glan01
      DESCRIPTION: dnn5glan01
    add_ngaction_list:
    - ACTIONNAME: 5glan_FlowDescription1
      TYPE: FlowDescription
      DESCRIPTION: any to any
    add_ngactionattr_list:
    - ACTIONNAME: 5glan_FlowDescription1
      ATTRNAME: sourceIP
      TYPE: Value
      VALUE: any
    add_ngactionattr_list_10:
    - ACTIONNAME: 5glan_offline_cg
      ATTRNAME: ratingGroup
      TYPE: Value
      VALUE: '2222'
    add_ngactionattr_list_13:
    - ACTIONNAME: 5glan_arp1
      ATTRNAME: priorityLevel
      TYPE: Object Attribute
      VALUE: SmfSession.SubsDefQosPriorityLevel
    add_rule_list_1:
    - RULENAME: 5glan_DyPccRule1
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      DESCRIPTION: any to any的兜底规则
      EDR: OFF
      RELATION: AND
    add_ruleconditiongroup_list:
    - RULENAME: 5glan_DyPccRule1
      CONDITIONGROUPNAME: 5glan_CG
    add_rulengaction_list:
    - RULENAME: 5glan_DyPccRule1
      ACTIONNAME: 5glan_DynamicPccRule1
    add_policy_list:
    - POLICYNAME: 5glan_policy1
      TYPE: N7 Policy
      DESCRIPTION: 基础的any to any规则
    add_policyrule_list:
    - POLICYNAME: 5glan_policy1
      RULENAME: 5glan_DyPccRule1
    add_policytrigger_list:
    - POLICYNAME: 5glan_policy1
      TRIGGERNAME: IPCAN_EST
    add_service_list:
    - SERVICENAME: 5glan_Service1
      SERVICETYPE: VALUE_ADDED_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
      DESCRIPTION: any to any的动态PCC规则
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list:
    - SERVICENAME: 5glan_Service1
      POLICYNAME: 5glan_policy1
    add_ngaction_list_10:
    - ACTIONNAME: any_lan_PredefinedPCCrule
      TYPE: PredefinedPccRule
      DESCRIPTION: any_lan
    add_ngactionattr_list_34:
    - ACTIONNAME: any_lan_PredefinedPCCrule
      ATTRNAME: pccRuleId
      TYPE: Value
      VALUE: fglan_u_p_any
    add_rule_list_3:
    - RULENAME: any_lan_PredefinedPCCrule
      TYPE: Smf Pcc Rule 5G
      PRECEDENCE: '0'
      VOLUMEUSAGEROUNDING: No
      EDR: OFF
      RELATION: AND
    add_rulengaction_list_2:
    - RULENAME: any_lan_PredefinedPCCrule
      ACTIONNAME: any_lan_PredefinedPCCrule
    add_policy_list_1:
    - POLICYNAME: any_lan_policy
      TYPE: N7 Policy
      DESCRIPTION: any_lan
    add_policyrule_list_2:
    - POLICYNAME: any_lan_policy
      RULENAME: any_lan_PredefinedPCCrule
    add_policytrigger_list_1:
    - POLICYNAME: any_lan_policy
      TRIGGERNAME: IPCAN_EST
    add_service_list_1:
    - SERVICENAME: any_lan_service
      SERVICETYPE: VALUE_ADDED_SERVICE
      ACTIVATEDBY: PCEF
      PRECEDENCE: '0'
      QOSMODE: Replace
      SUBSCRIPTIONFORCED: Yes
      DESCRIPTION: any_lan
      PROBILLDATE: No
      QUOTAALLOCATIONMODE: None
      ISSETSHAREDMODE: No
      RESUBSCRIPTIONOPERATION: 'NULL'
      ISGROUPSERVICE: No
      ISTEMPLATE: No
      ISRECUSRLOC: No
      APNMATCHTYPE: Full Matching
      HASBASESERVICE: No
      ADDONLEVEL: Exhaust
      CALCVALIDFORDYNSUBGROUP: No
      CUSTOMIZEDRESET: No
      MASTER2MASTERSHARESERVICE: No
    add_servicepolicy_list_1:
    - SERVICENAME: any_lan_service
      POLICYNAME: any_lan_policy
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
    add_pccpolicygrp_list_2:
    - PCCPOLICYGRPNM: '5glan_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
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
    add_rule_list_4:
    - RULENAME: fglan_r_any
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: any_f_f
      POLICYNAME: 5glan_pcc_p_g
    add_userprofile_list_1:
    - USERPROFILENAME: fglan_u_p_any
    add_rulebinding_list_1:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_urr_list_4:
    - URRNAME: 5glan_urr_offline
      URRID: '2222'
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
    add_urrgroup_list_2:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr_offline'
      DOWNURRNAME1: '5glan_urr_offline'
      UPURRNAME2: '5glan_urr_online'
      DOWNURRNAME2: '5glan_urr_online'
    add_urr_list_6:
    - URRNAME: 5glan_urr_offline
      URRID: '2222'
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
    add_urrgroup_list_3:
    - URRGROUPNAME: '5glan_urrgroup'
      UPURRNAME1: '5glan_urr_offline'
      DOWNURRNAME1: '5glan_urr_offline'
      UPURRNAME2: '5glan_urr_online'
      DOWNURRNAME2: '5glan_urr_online'
    add_pccpolicygrp_list_3:
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
    add_filter_list_1:
    - FILTERNAME: 'any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_filteripv6_list_1:
    - FILTERNAME: 'any_ipv6'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'any_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list_2:
    - FLOWFILTERNAME: 'any_f_f'
      FILTERNAME: 'any'
    add_rule_list_5:
    - RULENAME: fglan_r_any
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: any_f_f
      POLICYNAME: 5glan_pcc_p_g
    add_userprofile_list_2:
    - USERPROFILENAME: fglan_u_p_any
    add_rulebinding_list_2:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
    set_urrgrpbinding_list_1:
    - USERPROFILENAME: 'fglan_u_p_any'
      DFTURRGRPNAME: '5glan_urrgroup'
      TCPCHGPROFLAG: NOTCONFIG
      DFTSIGURRGNAME: 'ycll_01_ch_p'
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
    set_nglanchgctrl_list:
    - OFFLOCCHGPLYSW: ENABLE
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

### UDM需支持给5G LAN用户签约离线计费属性，计费属性值以“0800”为例，可通过BOSS修改。

### + **ADD NGCQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令存在多条时，“TPLID”不能重复。

### + **ADD DNNQOSTPL**命令中的“NGCQOSTPLID” 参数索引**ADD NGCQOSTPL**命令中的“TPLID”参数值。

### + **ADD SMDATA**命令中的“DNNQOSTPLID”参数索引**ADD DNNQOSTPL**命令中的“TPLID”参数值。

### 5G LAN QoS参数（5QI、ARP等）仅用于举例，实际请根据具体业务模型规划。

### 在“UDM业务管理”窗口下执行**LST NGS**命令和**LST VNGROUP**可查询5G LAN用户的“SNSSAI”、“DNN”、“INGROUPID”、“SHAREDID”、“PDUTYPES”等开户信息。

### 2~5是在“UDM业务管理”窗口下执行。具体为：先登录PGW WEBUI，然后在“应用类型”下拉框选择“UDM业务管理”。

### 中心UDM（UDM）和园区UDM（UEG）配置说明如表5所示。

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

#### 2.1 配置PLMN支持的切片。

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

#### 2.2 配置AMF切片信息。

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

#### 2.3 用户请求APN与签约APN不匹配时，配置AMF对5G LAN切片下的DNN纠正。如现网已涉及DNN纠正功能（可通过**LST LOCALNSDNN**查询），则需要执行如下配置；否则，请跳过如下配置。

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

### 3 配置NSSF数据

### 同一区域内，不是所有AMF都支持5G LAN业务切片时，需配置NSSF数据。否则，不需要配置。

### AMF收到5G LAN业务报文后，如本AMF未配置5G LAN业务切片信息，则可通过与NSSF交互实现AMF重定向，即将5G LAN业务报文重定向到配置了5G LAN业务切片信息的AMF上。

#### 3.1 在NSSF上增加5G LAN业务切片信息。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_cfgsnssai_list的变量区（command: ADD CFGSNSSAI） -#}
<!-- MISSING_MACRO: command=ADD CFGSNSSAI list_name=add_cfgsnssai_list step_id=3.1 -->
```

#### 3.2 在跟踪区域码分组中增加跟踪区域码。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tacgroupinnssf_list的变量区（command: ADD TACGROUPINNSSF） -#}
<!-- MISSING_MACRO: command=ADD TACGROUPINNSSF list_name=add_tacgroupinnssf_list step_id=3.2 -->
```

#### 3.3 将切片、AMF、TAC组进行绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_amfsetid_list的变量区（command: ADD AMFSETID） -#}
<!-- MISSING_MACRO: command=ADD AMFSETID list_name=add_amfsetid_list step_id=3.3 -->
```

### 4 配置SMF数据

### + **ADD PNFNS**命令存在多条时，“INDEX”不能重复。

### + **ADD PNFDNN**命令存在多条时，“INDEX”不能重复。

### + **ADD PNFDNN**命令中的“PNFNSINDEX”取值与**ADD PNFNS**命令定义的“INDEX”参数值一致。

### 5G LAN SMF-UPF Fullmesh组网时，支持5G LAN的多个SMF上的5G LAN业务配置相同。

#### 4.1 检查5G LAN License项是否开启。

##### 4.1.1 //显示信息中存在“LKV2SALANSM01”控制项时，说明已开启5G LAN License。

#### 4.2 配置SMF 5G LAN全局参数。

##### 4.2.1 //配置支持建立5G LAN会话。

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

##### 4.2.2 //配置对5G LAN UPF的选择机制。

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

##### 4.2.3 //配置5G LAN关键信元。

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

#### 4.3 配置5G LAN使用的切片和专用DNN信息。

##### 4.3.1 //配置SMF支持的切片信息。可以复用已有切片，复用已有切片时，不需要执行如下配置。可通过**LST PLMNNS**查询。

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

##### 4.3.3 中心SMF（UNC）：

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.4 应急SMF（UEG）：

```jinja2
{%- if is_scenario_emergency_smf -%}
    {%- for item in add_cpapn_list -%}
        ADD CPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.3.5 //配置网络切片支持DNN。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 4.4 配置支持5G LAN的SMF对端UPF实例信息。

##### 4.4.1 //配置对端UPF节点信息。同一个UPF对端只能配置一条ADD PNFPROFILE记录。如已配置对应的UPF节点信息，则不需要重复配置。

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

##### 4.4.2 //配置对端UPF支持的切片信息。如复用已有的对端UPF的切片信息，则不需要重复配置。推荐复用。

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

##### 4.4.4 //两个UPF是负荷分担组网时，配置对端UPF支持的DNN信息。

```jinja2
{%- if is_scenario_load_sharing -%}
    {%- for item in add_pnfdnn_list -%}
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
{%- endif -%}
```

##### 4.4.5 //两个UPF是主备组网时，配置对端UPF支持的DNN信息。两个UPF是主备组网时，“PRIORITY”值必须不同，“PRIORITY”值越小优先级越高。

```jinja2
{%- if is_scenario_active_standby -%}
    {%- for item in add_pnfdnn_list_2 -%}
        ADD PNFDNN:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        DNN="{{item.DNN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PNFNSINDEX is not none -%}
            PNFNSINDEX={{item.PNFNSINDEX}},
        {%- endif -%}
        {%- if item.PRISWITCH is not none -%}
            PRISWITCH={{item.PRISWITCH}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
        {%- if item.PRISWITCH == 'SPECIFIC' -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.4.6 //配置对端UPF支持5G LAN功能。

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

##### 4.4.7 //配置对端UPF的位置区域信息。如已配置的对端UPF的位置区域信息包含5G LAN业务对应的基站的TAI范围，则不需要重复配置。一个UPF服务区域可以绑定多个TAI范围，如利旧UPF服务区，且需要增加TAI范围，则可只通过**ADD UPAREABINDN2TAI**命令增加TAI范围。此处以两个UPF的位置区域信息相同为例。

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

##### 4.4.8 //配置对端UPF的SMF服务区域信息。如利旧UPF服务区（area01），则不需要重复配置。一个UPF实例可以和多个UPF服务区绑定。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

##### 4.4.9 //配置按优先级选择UPF。

```jinja2
{%- for item in set_apnupselply_list -%}
    SET APNUPSELPLY:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITYFLAG is not none -%}
        PRIORITYFLAG={{item.PRIORITYFLAG}},
    {%- endif -%}
    {%- if item.COMBINEDSELSTG is not none -%}
        COMBINEDSELSTG={{item.COMBINEDSELSTG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.5 UPF主备容灾场景下，主用UPF故障恢复后，在中心SMF去激活备用UPF上的5G LAN会话。应急SMF仅选择本UEG内的UPF，故应急SMF上不需要配置。

##### 4.5.1 //配置软参DWORD1066 BIT29值为1，主UPF故障恢复后，删除备UPF上的5G LAN会话。

```jinja2
{%- if is_scenario_active_standby -%}
    {%- for item in set_smfsoftparaofbit_list -%}
        SET SMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            POSITION={{item.POSITION}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.5.2 //配置主UPF故障恢复处理模式。此处以主用UPF是upf\_instance\_1，备用UPF是upf\_instance\_2为例。

```jinja2
{%- if is_scenario_active_standby -%}
    {%- for item in add_apnuprecover_list -%}
        ADD APNUPRECOVER:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        MASTERUPFID="{{item.MASTERUPFID}}",
        HANDLINGMODE={{item.HANDLINGMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HANDLINGMODE=BACKMIGRATION 时必选 --- -#}
        {%- if item.HANDLINGMODE == 'BACKMIGRATION' -%}
            BACKUPFID="{{item.BACKUPFID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.5.3 //配置SMF上故障恢复回迁任务的控制扫描速率和扫描间隔。

```jinja2
{%- if is_scenario_active_standby -%}
    {%- for item in set_upcscanrate_list -%}
        SET UPCSCANRATE:
        {#- --- 必选参数 --- -#}
        SCANTYPE={{item.SCANTYPE}},
        RATE={{item.RATE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SCANTYPE=BACKMIGRATION 时必选 --- -#}
        {%- if item.SCANTYPE == 'BACKMIGRATION' -%}
            INTERVAL={{item.INTERVAL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.6 UPF上开启基于5G LAN组的粒度的层二环路消除功能时，开启环路检测开关。“GROUPID”取值与UPF上开启层二环路消除功能的5G LAN组名称一致。

```jinja2
{%- if is_scenario_l2_loop_elimination -%}
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
{%- endif -%}
```

#### 4.7 不计费场景，关闭动态PCC功能及计费功能。计费场景，请跳过本步骤。

##### 4.7.1 //关闭动态PCC功能。

```jinja2
{%- if is_scenario_non_billing -%}
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
{%- endif -%}
```

##### 4.7.2 //关闭计费功能。

```jinja2
{%- if is_scenario_non_billing -%}
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
{%- endif -%}
```

#### 4.8 计费场景且基于PCF下发的动态规则/预定义规则进行离线计费时，开启动态PCC功能及离线计费功能。不计费场景或基于本地PCC的默认规则进行离线计费时，请跳过本步骤。

##### 4.8.1 // 打开动态PCC功能。UEG 21.8.2及之前版本仅支持动态PCC功能中的动态规则（any to any）；UEG 21.9.0及之后版本，支持动态PCC功能中的动态规则（any to any）/预定义规则（any to any）。

```jinja2
{%- if is_scenario_billing and is_scenario_pcf_offline -%}
    {%- for item in set_apnpccfunc_list_1 -%}
        SET APNPCCFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HOMEPCCSWITCH is not none -%}
            HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
        {%- endif -%}
        {%- if item.PCFSELECTMODE is not none -%}
            PCFSELECTMODE={{item.PCFSELECTMODE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.8.2 //配置对端PCF实例支持的DNN。SMF基于DNN选择PCF时使用。

```jinja2
{%- if is_scenario_billing and is_scenario_pcf_offline -%}
    {%- for item in add_pnfdnn_list_4 -%}
        ADD PNFDNN:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        DNN="{{item.DNN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.8.3 // 仅打开离线计费开关。

```jinja2
{%- if is_scenario_billing and is_scenario_pcf_offline -%}
    {%- for item in set_apnchargectrl_list_1 -%}
        SET APNCHARGECTRL:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CONVERGEDSW is not none -%}
            CONVERGEDSW={{item.CONVERGEDSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.9 计费场景且基于本地PCC的默认规则进行离线计费时，关闭动态PCC功能及打开离线计费开关。不计费场景或基于PCF下发的动态规则/预定义规则进行离线计费时，请跳过本步骤。

##### 4.9.1 //关闭动态PCC功能。UEG 21.9.0及之后版本，支持基于本地PCC的默认规则进行离线计费。

```jinja2
{%- if is_scenario_billing and is_scenario_local_pcc_offline -%}
    {%- for item in set_apnpccfunc_list_2 -%}
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
{%- endif -%}
```

##### 4.9.2 // 仅打开离线计费开关。

```jinja2
{%- if is_scenario_billing and is_scenario_local_pcc_offline -%}
    {%- for item in set_apnchargectrl_list_2 -%}
        SET APNCHARGECTRL:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CONVERGEDSW is not none -%}
            CONVERGEDSW={{item.CONVERGEDSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.10 配置5G LAN业务的缺省PCC规则。

##### 4.10.2 中心SMF（UNC）：

##### 4.10.3 //计费场景，配置URR和URRGROUP。不计费场景，请跳过本配置。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list step_id=4.10.3 -->
```

```jinja2
{%- if is_scenario_center_smf and is_scenario_billing -%}
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
{%- endif -%}
```

##### 4.10.4 //计费场景，配置PCC策略组。

```jinja2
{%- if is_scenario_center_smf and is_scenario_billing -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
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
{%- endif -%}
```

##### 4.10.5 //不计费场景，配置PCC策略组。

```jinja2
{%- if is_scenario_center_smf and is_scenario_non_billing -%}
    {%- for item in add_pccpolicygrp_list_1 -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.6 应急SMF（UEG）：

##### 4.10.7 //计费场景，配置CPURR和CPURRGROUP。不计费场景，请跳过本配置。

```jinja2
{%- if is_scenario_emergency_smf and is_scenario_billing -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_emergency_smf and is_scenario_billing -%}
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
{%- endif -%}
```

##### 4.10.8 //计费场景，配置PCC策略组。

```jinja2
{%- if is_scenario_emergency_smf and is_scenario_billing -%}
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
{%- endif -%}
```

##### 4.10.9 //不计费场景，配置PCC策略组。

```jinja2
{%- if is_scenario_emergency_smf and is_scenario_non_billing -%}
    {%- for item in add_cppccpolicygrp_list_1 -%}
        ADD CPPCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.11 中心SMF（UNC）：

##### 4.10.12 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_usrprofgroup_list -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=4.10.12 -->
```

```jinja2
{%- if is_scenario_center_smf -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_apnusrprofg_list -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.13 //配置配置用户模板和URRGROUP绑定。计费场景，需要该配置；不计费场景，请跳过本配置。

```jinja2
{%- if is_scenario_center_smf and is_scenario_billing -%}
    {%- for item in set_urrgrpbinding_list -%}
        SET URRGRPBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DFTURRGRPNAME is not none -%}
            DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.14 应急SMF（UEG）：

##### 4.10.15 //配置5G LAN业务的APN与用户模板组绑定。

```jinja2
{%- if is_scenario_emergency_smf -%}
    {%- for item in add_usrprofgroup_list_1 -%}
        ADD USRPROFGROUP:
        {#- --- 必选参数 --- -#}
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_emergency_smf -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_emergency_smf -%}
    {%- for item in add_upbindupg_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_emergency_smf -%}
    {%- for item in add_apnusrprofg_list_1 -%}
        ADD APNUSRPROFG:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        USERPROFGNAME="{{item.USERPROFGNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.16 //配置配置用户模板和URRGROUP绑定。计费场景，需要该配置；不计费场景，请跳过本配置。

```jinja2
{%- if is_scenario_emergency_smf and is_scenario_billing -%}
    {%- for item in set_cpurrgrpbinding_list -%}
        SET CPURRGRPBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DFTURRGRPNAME is not none -%}
            DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.18 中心SMF（UNC）：

##### 4.10.19 //“POLICYNAME”采用**ADD PCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=4.10.19 -->
```

```jinja2
{%- if is_scenario_center_smf -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POLICYTYPE is not none -%}
            POLICYTYPE={{item.POLICYTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.10.20 应急SMF（UEG）：

##### 4.10.21 //“POLICYNAME”采用**ADD CPPCCPOLICYGRP**命令中的“PCCPOLICYGRPNM”参数值。

```jinja2
{%- if is_scenario_emergency_smf -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_emergency_smf -%}
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
{%- endif -%}
```

### 5 配置PCF数据

### 离线计费场景，基于PCF下发的动态规则/预定义规则进行离线计费时，需要配置PCF数据。否则不需要配置PCF数据。

### - 基于PCF下发的动态规则进行离线计费时，请执行1.a~1.f。

### - 基于PCF下发的预定义规则进行离线计费时，请执行1.a、1.g~1.h。

### 需在BOSS上签约业务后，如下配置的业务才能生效。

### 在CSP OM Portal执行1.a；在UPCF WEBUI界面的“系统管理>批处理>CLI导入”窗口执行1.b~1.h。

#### 5.1 检查5G LAN License项是否开启。

##### 5.1.1 //显示信息中存在“LRM0PCFTC137”控制项时，说明已开启N7接口（使用HTTP协议）策略控制的 License。

#### 5.2 配置条件，以DNN为条件。“RIGHTVALUE”取值是DNN/APN的名称。基于PCF下发的动态规则进行离线计费时，需要配置。基于PCF下发的预定义规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_conditiongroup_list的变量区（command: ADD CONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD CONDITIONGROUP list_name=add_conditiongroup_list step_id=5.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_condition_list的变量区（command: ADD CONDITION） -#}
<!-- MISSING_MACRO: command=ADD CONDITION list_name=add_condition_list step_id=5.2 -->
```

#### 5.3 配置动作及动作属性。基于PCF下发的动态规则进行离线计费时，需要配置。基于PCF下发的预定义规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list step_id=5.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list step_id=5.3 -->
```

#### 5.4 配置离线计费属性。基于PCF下发的动态规则进行离线计费时，需要配置。基于PCF下发的预定义规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_10的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_10 step_id=5.4 -->
```

#### 5.5 配置QoS属性。5QI、ARP等QoS参数使用SMF在create session request中携带的值，PCF不做修改。基于PCF下发的动态规则进行离线计费时，需要配置。基于PCF下发的预定义规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_13的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_13 step_id=5.5 -->
```

#### 5.6 配置缺省规则。基于PCF下发的动态规则进行离线计费时，需要配置。基于PCF下发的预定义规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_1的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_1 step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ruleconditiongroup_list的变量区（command: ADD RULECONDITIONGROUP） -#}
<!-- MISSING_MACRO: command=ADD RULECONDITIONGROUP list_name=add_ruleconditiongroup_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list step_id=5.6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list step_id=5.6 -->
```

#### 5.7 配置动作及动作属性。基于PCF下发的预定义规则进行离线计费时，需要配置。基于PCF下发的动态规则进行离线计费时，跳过本步骤。 VALUE参数值需要与SMF上配置的USERPROFILENAME参数值一致。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngaction_list_10的变量区（command: ADD NGACTION） -#}
<!-- MISSING_MACRO: command=ADD NGACTION list_name=add_ngaction_list_10 step_id=5.7 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngactionattr_list_34的变量区（command: ADD NGACTIONATTR） -#}
<!-- MISSING_MACRO: command=ADD NGACTIONATTR list_name=add_ngactionattr_list_34 step_id=5.7 -->
```

#### 5.8 配置缺省规则。基于PCF下发的预定义规则进行离线计费时，需要配置。基于PCF下发的动态规则进行离线计费时，跳过本步骤。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_3的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_3 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rulengaction_list_2的变量区（command: ADD RULENGACTION） -#}
<!-- MISSING_MACRO: command=ADD RULENGACTION list_name=add_rulengaction_list_2 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policy_list_1的变量区（command: ADD POLICY） -#}
<!-- MISSING_MACRO: command=ADD POLICY list_name=add_policy_list_1 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policyrule_list_2的变量区（command: ADD POLICYRULE） -#}
<!-- MISSING_MACRO: command=ADD POLICYRULE list_name=add_policyrule_list_2 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_policytrigger_list_1的变量区（command: ADD POLICYTRIGGER） -#}
<!-- MISSING_MACRO: command=ADD POLICYTRIGGER list_name=add_policytrigger_list_1 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_service_list_1的变量区（command: ADD SERVICE） -#}
<!-- MISSING_MACRO: command=ADD SERVICE list_name=add_service_list_1 step_id=5.8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_servicepolicy_list_1的变量区（command: ADD SERVICEPOLICY） -#}
<!-- MISSING_MACRO: command=ADD SERVICEPOLICY list_name=add_servicepolicy_list_1 step_id=5.8 -->
```

### 6 配置UPF数据

### 企业侧交换机与UPF之间建立VXLAN隧道的场景，两个VXLAN交换机是堆叠组网或M-LAG组网时，两个VXLAN交换机都是只需要提供一个VTEP IP。DCGW与UPF之间建立VXLAN隧道的场景，一对DCGW是M-LAG组网，一对DCGW只需要提供一个VTEP IP。

### 两个UPF是负荷分担容灾关系，且仅对接一对企业侧VXLAN交换机/DCGW时，支持两个UPF之间建立VXLAN隧道，用于实现跨UPF的终端互访。两个UPF之间建立VXLAN隧道时，需要分别在两个UPF上进行配置，VTEP IP是另一UPF的VXLAN隧道IP，如下以配置一个UPF为例。

### 不同的5G LAN组共用VTEP，一个5G LAN组对应一个VNI。如图9所示，VNI为5010和VNI为5011的两个VNI共用VTEP。

### **图9** VXLAN隧道数据规划图

#### 6.1 检查CU Fullmesh的License项是否开启。

##### 6.1.1 //显示信息中“LKV3G5CUFM01”控制项的“开关（SWITCH）”为“ENABLE”时，说明已开启5G LAN SMF-UPF Fullmesh License。

#### 6.2 配置UPF 5G LAN全局参数。

##### 6.2.1 //开启5G LAN特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 6.2.2 //开启5G LAN功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

#### 6.3 配置UPF支持的DNN（APN）信息。

##### 6.3.1 //支持层二 5G LAN业务的DNN（APN）不需要绑定VPN实例。

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 6.4 配置UPF支持的5G LAN组。

##### 6.4.1 //如下以配置2个5G LAN组为例。规划多个5G LAN组时，“VNINSTANCE”取值必须不同。

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

#### 6.5 配置VXLAN隧道。

##### 6.5.2 DCGW与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”必须设置为“\_public\_”。

##### 不存在绑定VPN实例为“\_public\_”的外联口及路由数据时，可参考N6接口配置用于传输UPF和DCGW之间VXLAN报文的外联口IP、路由数据（VPN实例为“\_public\_”）。

```jinja2
{%- if is_scenario_dcgw_vxlan -%}
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

##### 6.5.3 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。此处以“VRF\_LocalDN01”为例。

##### 此处以复用N6接口的VPN实例为例。如使用独立的VPN实例，则需要执行**ADD VPNINST**命令及参考N6接口配置对应的外联口IP、路由数据（外联口绑定的VPN与VXLAN接口绑定的VPN相同）。

```jinja2
{%- if is_scenario_enterprise_switch_vxlan -%}
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

##### 6.5.4 DCGW与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”必须设置为“\_public\_”。

##### 6.5.5 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。

##### 6.5.6 UPF与另一UPF之间建立VXLAN隧道的场景，复用UPF与DCGW/企业侧交换机之间建立VXLAN隧道的vxlanif接口。

##### 6.5.8 路径中的网络设备和对端都支持心跳消息（PING报文）时，请执行：

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

##### 6.5.9 路径中的网络设备或对端不支持心跳消息（PING报文）时，请执行：

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

##### 6.5.10 //配置VXLAN隧道远端端点，VTEPIPV4为远端端点IP，来源于企业侧交换机的VXLAN隧道端点IP地址。两个UPF是主备组网时，两个UPF上配置的VXLAN隧道远端端点IP（VTEPIPV4）相同。

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

##### 6.5.11 //配置VXLAN隧道端点绑定VXLAN隧道组。存在多个负荷分担的VTEP时，“PRIFLAG”设置为“PRIMARY”。

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

#### 6.6 绑定5G LAN组与VXLAN隧道组。不同5G LAN组共用VXLAN隧道时，VNI必须不同。

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

#### 6.7 不计费场景，配置缺省PCC规则。计费场景，请跳过本步骤。

##### 6.7.1 //配置PCC策略组。

```jinja2
{%- if is_scenario_non_billing -%}
    {%- for item in add_pccpolicygrp_list_2 -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.2 //配置流过滤器，any-to-any。

```jinja2
{%- if is_scenario_non_billing -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_billing -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_billing -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_billing -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.7.3 //配置5G LAN业务相关的rule和userprofile。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_4的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_4 step_id=6.7.3 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list_1的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list_1 step_id=6.7.3 -->
```

```jinja2
{%- if is_scenario_non_billing -%}
    {%- for item in add_rulebinding_list_1 -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_non_billing -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.8 配置离线计费策略和缺省PCC规则。

##### 6.8.1 //动态规则场景，配置URR。如已配置，则不需要重复配置。推荐复用。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list_4的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list_4 step_id=6.8.1 -->
```

```jinja2
{%- if is_scenario_dynamic_rule -%}
    {%- for item in add_urrgroup_list_2 -%}
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
{%- endif -%}
```

##### 6.8.2 //预定义规则场景，配置URR。如已配置，则不需要重复配置。推荐复用。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_urr_list_6的变量区（command: ADD URR） -#}
<!-- MISSING_MACRO: command=ADD URR list_name=add_urr_list_6 step_id=6.8.2 -->
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_urrgroup_list_3 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_pccpolicygrp_list_3 -%}
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
{%- endif -%}
```

##### 6.8.3 //预定义规则场景，配置流过滤器，any-to-any。

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_filter_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_filteripv6_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_flowfilter_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_fltbindflowf_list_2 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.8.4 //预定义规则场景，配置5G LAN业务相关的rule和userprofile。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_5的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_5 step_id=6.8.4 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list_2的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list_2 step_id=6.8.4 -->
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in add_rulebinding_list_2 -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in set_urrgrpbinding_list_1 -%}
        SET URRGRPBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DFTURRGRPNAME is not none -%}
            DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
        {%- endif -%}
        {%- if item.TCPCHGPROFLAG is not none -%}
            TCPCHGPROFLAG={{item.TCPCHGPROFLAG}},
        {%- endif -%}
        {%- if item.DFTSIGURRGNAME is not none -%}
            DFTSIGURRGNAME="{{item.DFTSIGURRGNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_predefined_rule -%}
    {%- for item in set_refreshsrv_list_1 -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.8.5 //开启离线本地计费策略开关。

```jinja2
{%- for item in set_nglanchgctrl_list -%}
    SET NGLANCHGCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLOCCHGPLYSW is not none -%}
        OFFLOCCHGPLYSW={{item.OFFLOCCHGPLYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.9 配置故障定界所需数据（执行**NGVNVIFPING**获取时延时依赖的数据）。

##### 6.9.1 //此处配置的是UPF发送的ping探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。

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

##### 6.9.2 //基于5G LAN组配置ping探测报文的源IP地址。从DHCP Server获取，该IP地址等同于DHCP Server分配给5G LAN层二终端的IP地址，与5G LAN层二终端的IP地址在同一网段，且不能与5G LAN层二终端的IP地址冲突。

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

#### 6.10 DCGW/企业侧交换机与UPF之间建立VXLAN隧道的场景，修改外联口MTU值。

##### 6.10.2 Ethernet接口组网时：

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

##### 6.10.3 Eth-trunk接口组网时：

##### 6.10.4 //Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

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

#### 6.11 通过静态组播组实现层二5G LAN组播功能时，配置静态组播组。局点规划支持静态组播功能时（例如电力场景）需要配置，否则请跳过本步骤。

##### 6.11.1 //开启5G LAN层二静态组播的License配置开关。

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

##### 6.11.2 //5G LAN终端发送组播报文时，报文中的目的MAC必须与此处配置的组播MAC（11-11-11-11-11-fc）一致。

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

#### 6.12 禁止通过N9口实现终端互访的场景，配置漫游5G LAN终端通过白名单实现与同一5G LAN组内的其他终端互访。

##### 6.12.1 //此处以基于5G LAN组+白名单方案允许漫游5G LAN终端与该5G LAN组中的其他终端互访，互访报文包括单播、组播和广播为例。

```jinja2
{%- if is_scenario_no_n9_inter_access -%}
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
{%- endif -%}
```

##### 6.12.2 //此处以允许漫游5G LAN终端通过5个I-UPF的N9口与锚点UPF交互为例，实际请根据局点实际业务规划配置白名单。白名单中的IP地址，是与锚点UPF互通的I-UPF的N9口IP。

```jinja2
{%- if is_scenario_no_n9_inter_access -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_no_n9_inter_access -%}
    {%- for item in add_ngbinduemutwl_list -%}
        ADD NGBINDUEMUTWL:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        WLISTNAME="{{item.WLISTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.13 配置UPF对上行5G LAN层二报文的VLAN0进行剥除。

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

#### 6.14 配置基于5G LAN组粒度的层二环路消除功能。

##### 6.14.1 CPE支持UPF发送的主动检测环路的报文，该场景下，推荐采用主动检测方案。

##### 6.14.2 //开启License开关。主动检测和被动检测时均需要配置。

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

##### 6.14.3 //开启主动检测开关。

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

##### 6.14.4 //此处配置的是UPF发送的环路探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。

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

##### 6.14.5 CPE不支持UPF发送的主动检测环路报文，该场景下，可采用被动检测方案。

##### 6.14.6 //开启License开关。主动检测和被动检测时均需要配置。

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

##### 6.14.7 //配置被动检测参数。

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

#### 6.15 配置FRER双发选收功能。工业冗余协议交换机支持FRER冗余协议时，UPF支持FRER双发选收功能。

##### 6.15.1 //在主用UPF上开启本特性的License配置开关。

```jinja2
{%- if is_scenario_frer_supported -%}
    {%- for item in set_licenseswitch_list_5 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.15.2 //在主用UPF上进行如下配置：

```jinja2
{%- if is_scenario_frer_supported -%}
    {%- for item in set_ngdfsrfunc_list -%}
        SET NGDFSRFUNC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        DFSRSWITCH={{item.DFSRSWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_frer_supported -%}
    {%- for item in set_dfsrattr_list -%}
        SET DFSRATTR:
        {#- --- 可选参数 --- -#}
        {%- if item.NEPRIFLAG is not none -%}
            NEPRIFLAG={{item.NEPRIFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dfsrpair_list的变量区（command: ADD DFSRPAIR） -#}
<!-- MISSING_MACRO: command=ADD DFSRPAIR list_name=add_dfsrpair_list step_id=6.15.2 -->
```

```jinja2
{%- if is_scenario_frer_supported -%}
    {%- for item in add_dfsrpairmem_list -%}
        ADD DFSRPAIRMEM:
        {#- --- 必选参数 --- -#}
        DFSRPAIRID={{item.DFSRPAIRID}},
        IMSI="{{item.IMSI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_frer_supported -%}
    {%- for item in add_ngbinddfsrpair_list -%}
        ADD NGBINDDFSRPAIR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        DFSRPAIRID={{item.DFSRPAIRID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 6.15.4 //在备用UPF上进行如下配置：

```jinja2
{%- if is_scenario_frer_supported -%}
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
{%- endif -%}
```

#### 6.16 通过IGMP动态组播组实现层二5G LAN组播功能时，配置IGMP Snooping。局点规划支持IGMP动态组播功能时需要配置，否则请跳过本步骤。

##### 6.16.1 //开启IGMP Snooping功能开关。

```jinja2
{%- if is_scenario_igmp_dynamic_multicast -%}
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

##### 6.16.2 //网络中其他设备作为查询器时，在UPF上配置Query参数。UPF作为查询器时，请跳过本步骤。

```jinja2
{%- if is_scenario_igmp_dynamic_multicast and is_scenario_other_device_querier -%}
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

##### 6.16.3 //网络中无查询器时，在UPF上配置Query功能。网络中其他设备作为查询器时，请跳过本步骤。

```jinja2
{%- if is_scenario_igmp_dynamic_multicast and is_scenario_no_querier -%}
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
{%- if is_scenario_igmp_dynamic_multicast and is_scenario_no_querier -%}
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

##### 6.16.4 //组播源在N3侧且组播源是IMSI时需要配置，否则不需要配置。

```jinja2
{%- if is_scenario_igmp_dynamic_multicast and is_scenario_mcast_source_imsi -%}
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

##### 6.16.5 //组播源在N3侧且播源是双发选收结对时需要配置，否则不需要配置。

```jinja2
{%- if is_scenario_igmp_dynamic_multicast and is_scenario_mcast_source_dfsrpair -%}
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

### 7 配置LSW/DCGW数据

#### 7.1 企业侧交换机与UPF之间建立VXLAN隧道的场景

#### 请参考配置企业DN侧交换机。

#### 7.2 DCGW与UPF之间建立VXLAN隧道的场景

#### 请参考对应型号的DCGW的配置。

### 8 配置无线基站数据

### 请参考配置无线基站。

### 9 配置CPE数据

### 请参考配置CPE终端。

