---
id: ''
name: 配置UPF数据
ne_type: UEG
type: feature
description: '## 操作场景  总部园区部署两套UEG-L，两套UEG-L是负荷分担容灾模式。子园区UEG-S均故障后，不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。  子园区交换机与UPF之间建立VXLAN隧道的场景，图1~图3中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。  **表1** 5G LAN组网及报文路径  | 业务场景 | 负荷分担容灾模式 | | --- | --- | | 场景一：子园区5G LAN层二终端与子园区Server（Main PLC/MES/...）互通 | 组网如图1所示。  子园区UEG-S均故障后，总部园区UEG-L之间采用负荷分担容灾模式，两个UEG-L均处理子园区用户数据业务，5G LAN层二终端通过某一UEG-L与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区侧VXLAN交换机上或独立的网关设备上。 | | 场景二：同一5G LAN组的层二终端互通 | * 组网如图2所示。子园区UEG-S均故障后，总部园区UEG-L之间采用负荷分担容灾模式，子园区用户在总部园区UEG-L上激活，同一5G LAN组下不同终端通过**同一UEG-L或不同UEG-L**接入。 * 组网如图3所示。子园区UEG-S故障恢复后，子园区用户在子园区UEG-S激活，子园区UEG-S故障恢复前在UEG-L上激活的用户还未下线，同一5G LAN组下不同终端通过**UEG-L与UEG-S**接入。   子园区交换机与总部、子园区UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。总部园区和子园区UPF仅对接一对子园区企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图2以2对LSW为例。图3以1对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区企业侧VXLAN交换机上或独立的网关设备上。 * 两组LSW之间，通过直连线互通或者其他LSW互通。 |  当存在如下情况时，可以参考本页面进行配置。  * CPE下挂多个终端（最多16个）。 * 同一个二层广播域内的终端IP必须不同。 * 支持如下几种典型业务场景：   + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。      Server（Main PLC/MES/...）部署在N6侧。   + 同一5G LAN组层二终端之间通过同一UPF互通。   + 同一5G LAN组层二终端之间通过不同UPF互通，即总部园区2个UEG-L之间、总部园区UEG-L与子园区各UEG-S之间。      子园区交换机与UPF之间建立VXLAN隧道的场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。      两个UPF仅对接一对子园区侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  **图1** 子园区UEG-S均故障时，5G LAN层二终端与子园区Server（Main PLC/MES/...）互通）  **图2** 子园区UEG-S故障时，同一5G LAN组的层二终端在总部园区UEG-L互通  **图3** 子园区UEG-S恢复，同一5G LAN组的层二终端在总部园区UEG-L与子园区UEG-S之间互通'
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（跨级容灾，仅适用于海外）","新建方案配置","可选业务配置（5G LAN）","在UEG-L配置5G LAN终端互访功能（UEG L虚机）","子园区UPF负荷分担容灾","配置UPF数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
## 操作场景总部园区部署两套UEG-L，两套UEG-L是负荷分担容灾模式。子园区UEG-S均故障后，不同业务场景下，5G LAN相关组网及报文路径差异如表1所示。子园区交换机与UPF之间建立VXLAN隧道的场景，图1~图3中的DCGW、Firewall仅用于举例，5G LAN业务对DCGW、Firewall数量无特殊要求。**表1** 5G LAN组网及报文路径| 业务场景 | 负荷分担容灾模式 || --- | --- || 场景一：子园区5G LAN层二终端与子园区Server（Main PLC/MES/...）互通 | 组网如图1所示。  子园区UEG-S均故障后，总部园区UEG-L之间采用负荷分担容灾模式，两个UEG-L均处理子园区用户数据业务，5G LAN层二终端通过某一UEG-L与Server（Main PLC/MES/...）互通。  说明：  5G LAN层二终端与Server（Main PLC/MES/...）在不同网段时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区侧VXLAN交换机上或独立的网关设备上。 || 场景二：同一5G LAN组的层二终端互通 | * 组网如图2所示。子园区UEG-S均故障后，总部园区UEG-L之间采用负荷分担容灾模式，子园区用户在总部园区UEG-L上激活，同一5G LAN组下不同终端通过**同一UEG-L或不同UEG-L**接入。 * 组网如图3所示。子园区UEG-S故障恢复后，子园区用户在子园区UEG-S激活，子园区UEG-S故障恢复前在UEG-L上激活的用户还未下线，同一5G LAN组下不同终端通过**UEG-L与UEG-S**接入。   子园区交换机与总部、子园区UPF之间建立VXLAN隧道的场景，则需要根据LSW的能力判断是否需要多对LSW。总部园区和子园区UPF仅对接一对子园区企业侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。  说明：  * LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要两对LSW。图2以2对LSW为例。图3以1对LSW为例。 * 同一5G LAN层二终端IP在不同网段且存在互通诉求时，层二终端所在PC上需要配置网关IP，网关IP配置在子园区企业侧VXLAN交换机上或独立的网关设备上。 * 两组LSW之间，通过直连线互通或者其他LSW互通。 |当存在如下情况时，可以参考本页面进行配置。* CPE下挂多个终端（最多16个）。* 同一个二层广播域内的终端IP必须不同。* 支持如下几种典型业务场景：  + 5G LAN层二终端与Server（Main PLC/MES/...）需要互通。    Server（Main PLC/MES/...）部署在N6侧。  + 同一5G LAN组层二终端之间通过同一UPF互通。  + 同一5G LAN组层二终端之间通过不同UPF互通，即总部园区2个UEG-L之间、总部园区UEG-L与子园区各UEG-S之间。    子园区交换机与UPF之间建立VXLAN隧道的场景下，需要根据LSW的能力判断是否需要多对LSW（用于建立VXLAN隧道）。LSW支持VXLAN进VXLAN出（接收VXLAN报文，处理后重新封装成VXLAN报文发出）时，可只部署一对LSW。否则，需要每台UEG对接一对LSW。    两个UPF仅对接一对子园区侧VXLAN交换机时，可通过UPF间的VXLAN隧道实现跨UPF的终端互访。**图1** 子园区UEG-S均故障时，5G LAN层二终端与子园区Server（Main PLC/MES/...）互通）**图2** 子园区UEG-S故障时，同一5G LAN组的层二终端在总部园区UEG-L互通**图3** 子园区UEG-S恢复，同一5G LAN组的层二终端在总部园区UEG-L与子园区UEG-S之间互通

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '缺省PCC规则，“USERPROFILENAME”必须和SMF配置一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
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
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '已配置数据中获取'
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
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
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
          description: '规划一个独立的外联口，用于子园区5G LAN终端接入。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IFMTU:
          name: '接口最大传输单元（byte）'
          type: integer
          minimum: 46
          maximum: 9600
          required: false
          description: '-'
          data_source: '固定值'
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
          description: '规划一个独立的APN，接入5G LAN业务。  AMF、SMF、UDM部署5G LAN业务时，需关注该规划原则。'
          data_source: '全网规划'
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
          description: '该参数必须和UDM上配置的5G LAN组ID一致。'
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
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '规划一个独立的VPN，用于子园区5G LAN终端接入。'
          data_source: '本端规划'
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
          description: '配置VXLAN逻辑接口。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: '配置VXLAN隧道组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '配置VXLAN隧道组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
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
          description: '* 总部园区UEG-L与子园区UEG-S必须对接同一套子园区的交换机。 * 总部园区部署两套负荷分担UEG-L，也可以部署一套UEG-L。'
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
          description: '所有VXLAN隧道远端端点都和本端端点绑定在一个VXLAN组内。一个VXLAN组最多绑8个VTEP。'
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
    add_vtep_list_1:
      type: items
      properties:
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '* 总部园区UEG-L与子园区UEG-S必须对接同一套子园区的交换机。 * 总部园区部署两套负荷分担UEG-L，也可以部署一套UEG-L。'
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
    add_vtepbindgrp_list_1:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '所有VXLAN隧道远端端点都和本端端点绑定在一个VXLAN组内。一个VXLAN组最多绑8个VTEP。'
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
    add_ngvnbindvxlan_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '5GLAN组绑定VXLAN隧道组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LANB01'
      SWITCH: ENABLE
    set_nglanfunc_list:
    - NGLANSW: ENABLE
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
      FILTERNAME: 'any_ipv6'
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
    mod_interface_list:
    - IFNAME: 'Eth-trunk1.100'
      IFMTU: 1600
    add_upapn_list:
    - APN: 'dnn5glan01'
    add_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      MACIDLESW: DISABLE
      IGMPSNOOPINGSW: DISABLE
      IGMPPARSESW: DISABLE
      MULTIFLOODSW: DISABLE
      BCASTFLOWCTRLSW: ENABLE
      UNICASTFLOODSW: DISABLE
      N6MACIDLESW: DISABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_Enterprise'
    add_logicinf_list:
    - NAME: 'vxlanif2/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.50.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VRF_Enterprise'
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
    - VTEPNAME: 'VTEPA'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEPA'
      PRIFLAG: PRIMARY
    add_vtep_list_1:
    - VTEPNAME: 'VTEP2'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.51.1'
    - VTEPNAME: 'VTEPA1'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.60.1'
    add_vtepbindgrp_list_1:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP2'
      PRIFLAG: PRIMARY
    add_ngvnbindvxlan_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VXLANGRPNAME: 'vxlan_01'
      VNI: 5010
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 公共5G LAN配置。

#### 1.1 配置UPF 5G LAN全局参数。总部园区5G LAN终端接入功能已配置，则无需重复配置。

##### 1.1.1 //开启5G LAN特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 1.1.2 //开启5G LAN功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

#### 1.2 配置5G LAN业务的缺省PCC规则。如总部园区5G LAN终端接入功能已配置规则，则不需要重复配置。推荐复用。

##### 1.2.1 //配置URR。

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

##### 1.2.2 //预定义规则场景，配置流过滤器，any-to-any。

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

##### 1.2.3 //配置5G LAN业务相关的rule和userprofile。

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

#### 1.3 DCGW与UEG之间建立VXLAN隧道的场景，修改外联口MTU值。如下IFNAME值仅为举例，实际请修改为传输VXLAN隧道报文的外联口名称。

##### 1.3.1 //Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

```jinja2
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
```

### 2 新增一个子园区UPF的5G LAN配置。

#### 2.1 配置UPF支持的DNN（APN）信息。

##### 2.1.1 //支持层二 5G LAN业务的DNN（APN）不需要绑定VPN实例。该APN为子园区用于5G LAN业务的专有DNN（APN）。

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 2.2 配置UPF支持的5G LAN组。

##### 2.2.1 //如下仅配置1个5G LAN组。规划多个5G LAN组时，“VNINSTANCE”取值必须不同。

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

#### 2.3 配置VXLAN逻辑接口所属的VPN实例。该VPN为子园区用于5G LAN业务的独立VPN。此处以“VRF\_Enterprise”为例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 2.4 配置VXLAN逻辑接口。子园区交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。

#### UPF与另一UPF之间建立VXLAN隧道的场景，复用UPF与子园区交换机之间建立VXLAN隧道的vxlanif接口。

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

#### 2.5 配置VXLAN隧道组。

##### 2.5.1 路径中的网络设备和对端都支持心跳消息（PING报文）时，请执行：

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

##### 2.5.2 路径中的网络设备或对端不支持心跳消息（PING报文）时，请执行：

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

#### 2.6 配置VXLAN隧道远端端点（VTEP：子园区VXLAN交换机），VTEPIPV4为远端端点IP，来源于子园区交换机的VXLAN隧道端点IP地址。

##### 2.6.1 //远端为子园区交换机的VXLAN隧道端点IP地址。

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

##### 2.6.2 //配置VXLAN隧道端点绑定VXLAN隧道组。

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

#### 2.7 配置VXLAN隧道远端端点（VTEP：UPF），VTEPIPV4为远端端点IP，来源于隧道对端UPF的VXLAN隧道端点IP地址。对端UPF必须对接到同一对企业侧VXLAN交换机。

##### 2.7.1 //远端为总部园区UEG-L的VXLAN隧道端点IP地址。

```jinja2
{%- for item in add_vtep_list_1 -%}
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

##### 2.7.3 //配置VXLAN隧道端点绑定VXLAN隧道组。

```jinja2
{%- for item in add_vtepbindgrp_list_1 -%}
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

#### 2.8 绑定5G LAN组与VXLAN隧道组。

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

