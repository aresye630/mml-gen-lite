---
id: ''
name: 配置容灾模式（热备）
ne_type: UEG
type: feature
description: 为避免单点故障造成业务中断，需部署两套UEG进行容灾。两套UEG间采用热备容灾模式时，需要参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","配置实例（虚机容器）","配置容灾模式（热备）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST DRCOUPLINGRESET')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为避免单点故障造成业务中断，需部署两套UEG进行容灾。两套UEG间采用热备容灾模式时，需要参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

* 已完成两套UEG初始配置与调测。
* 已完成UEG间容灾消息传输使用的外联口IP及路由数据
* 已完成加载License，热备容灾对应license为：82200FFV LKV3G5SLHB01 会话热备容灾会话数（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_drcouplingreset_list:
      type: items
      properties:
        COUPLINGRESET:
          name: '是否使能负荷分担容灾功能'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    set_drkeynf_list:
      type: items
      properties:
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '需要根据规划，监控UEG上部署的服务。'
          data_source: '本端规划'
          pattern: ''
          default: NO
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_drtlsmode_list:
      type: items
      properties:
        TLSMODE:
          name: '容灾控制通道TLS模式'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: '-'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
    set_faultcheckbyfabric_list:
      type: items
      properties:
        ENABLE:
          name: '故障快速检测开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROTECTDURATION:
          name: '防震荡保护时长 (分)'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: '固定取值，如需修改此值请联系华为继续支持。'
          pattern: ''
          default: 10
        WAITRPTDURATION:
          name: '等待上报时长 (毫秒)'
          type: integer
          minimum: 100
          maximum: 10000
          required: false
          description: ''
          data_source: '固定取值，如需修改此值请联系华为继续支持。'
          pattern: ''
          default: 3000
    set_drgroupablement_list:
      type: items
      properties:
        DRGROUPABLEMENT:
          name: '是否使能热备容灾组'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ISAUTOACTIVE:
          name: '是否自动升主'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_drgroupinfo_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '两套UEG采用热备容灾时，容灾组标识+容灾组名称取值必须一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DRGROUPNAME:
          name: '容灾组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LDRINSTID:
          name: '本端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '两套UEG上该参数必须不同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTMODE:
          name: '本端默认运行模式'
          type: string
          enum:
          - ACTIVE
          - STANDBY
          required: true
          description: '主用UEG上设置为ACTIVE，备用UEG上设置为STANDBY。  ACTIVE和STANDBY为网元的配置状态，非实际运行态。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDRINSTID:
          name: '对端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '对端UEG上的容灾实例标识。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '对端容灾控制通道IP地址版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '配置容灾控制通道1。  当“对端容灾控制通道IP地址版本号”为IPV4时，需配置IPV4地址，当“对端容灾控制通道IP地址版本号”为IPV6时，需配置IPV6地址，不可同时配置。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PGRCIP:
          name: '对端容灾控制通道IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '从对端获取，为对端OM登录IP，本端默认使用OM登录IP。'
          pattern: ''
          default: ''
        PGRCIPV6:
          name: '对端容灾控制通道IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '从对端获取，为对端OM登录IP，本端默认使用OM登录IP。'
          pattern: ''
          default: ''
    set_drhbnegotimer_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HELLOINTERVAL:
          name: '心跳消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '心跳消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为对端网元故障。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        NEGOINTERVAL:
          name: '协商消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '协商消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为容灾组协商失败。'
          data_source: '与对端协商，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        TIMES:
          name: '重传次数'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: 'UEG间发送心跳和协商消息的重传次数。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        OMHBTIMES:
          name: 'OM通道心跳重传次数'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: '配置容灾控制通道1故障探测时长。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        OMHBINTERVAL:
          name: 'OM通道心跳探测时长(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
    set_drautoswover_list:
      type: items
      properties:
        AUTOSWOVER:
          name: '自动倒回功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '在热备容灾模式下开启自动倒回功能。  注：功能开启后，“默认运行状态”为ACTIVE的UEG网元故障后再恢复时，会发生自动倒换由该UEG网元继续做为主用网元。  由于UEG\_L中带有融合数据网元：   1. 2个UEG内的UDM/HSS、PCF/PCRF网元均会和IMS网元对接。IMS网元会优选1个UEG内的UDM/HSS、PCF/PCRF网元，为了防止UEG内的AMF/MME、SMF/GWC选择的UDM/HSS、PCF/PCRF网元和IMS网元选择不一致，导致融合数据处理冲突，因此需开启自动倒回功能。 2. 2个UEG内的UDR均会和营帐对接。营帐会固定选择1个UEG内的UDR进行开户，为了防止倒换后，无法进行开户操作，因此需开启自动倒回功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_drdci_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置容灾控制通道2。  两套UEG上，该参数取值必须一致。  DC间通信通道采用IPv4时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LDCIP:
          name: '本端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划，本端DRDCI IP地址。'
          pattern: ''
          default: ''
        PDCIP:
          name: '对端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划，对端DRDCI IP地址。'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '引用**ADD VPNINST**定义的VPN实例名称VRF\_PS\_Signal。可通过**LST VPNINST**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DATABKMODE:
          name: '数据备份模式'
          type: string
          enum:
          - Active-Standby
          - Active-Standby_Hot_Backup
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: Active-Standby
        HBINTERVAL:
          name: '心跳探测时长(100ms)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '心跳探测时长\*心跳重传次数=DC间容灾控制通道故障探测时长。'
          data_source: '全网规划'
          pattern: ''
          default: 10
        HBTIMES:
          name: '心跳重传次数'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 6
        LDCIPV6:
          name: '本端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划，本端DRDCI IP地址。'
          pattern: ''
          default: ''
        PDCIPV6:
          name: '对端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划，对端DRDCI IP地址。'
          pattern: ''
          default: ''
    set_drcouplingreset_list_1:
      type: items
      properties:
        COUPLINGRESET:
          name: '是否使能负荷分担容灾功能'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    set_drkeynf_list_1:
      type: items
      properties:
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '需要根据规划，监控UEG上部署的服务。'
          data_source: '本端规划'
          pattern: ''
          default: NO
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
    set_faultcheckbyfabric_list_1:
      type: items
      properties:
        ENABLE:
          name: '故障快速检测开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PROTECTDURATION:
          name: '防震荡保护时长 (分)'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: '固定取值，如需修改此值请联系华为继续支持。'
          pattern: ''
          default: 10
        WAITRPTDURATION:
          name: '等待上报时长 (毫秒)'
          type: integer
          minimum: 100
          maximum: 10000
          required: false
          description: ''
          data_source: '固定取值，如需修改此值请联系华为继续支持。'
          pattern: ''
          default: 3000
    set_drgroupablement_list_1:
      type: items
      properties:
        DRGROUPABLEMENT:
          name: '是否使能热备容灾组'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ISAUTOACTIVE:
          name: '是否自动升主'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_vpninst_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_drgroupinfo_list_1:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '两套UEG采用热备容灾时，容灾组标识+容灾组名称取值必须一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DRGROUPNAME:
          name: '容灾组名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LDRINSTID:
          name: '本端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '两套UEG上该参数必须不同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFTMODE:
          name: '本端默认运行模式'
          type: string
          enum:
          - ACTIVE
          - STANDBY
          required: true
          description: '主用UEG上设置为ACTIVE，备用UEG上设置为STANDBY。  ACTIVE和STANDBY为网元的配置状态，非实际运行态。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDRINSTID:
          name: '对端容灾实例标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '对端UEG上的容灾实例标识。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: '对端容灾控制通道IP地址版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '配置容灾控制通道1。  当“对端容灾控制通道IP地址版本号”为IPV4时，需配置IPV4地址，当“对端容灾控制通道IP地址版本号”为IPV6时，需配置IPV6地址，不可同时配置。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PGRCIP:
          name: '对端容灾控制通道IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '从对端获取，为对端OM登录IP，本端默认使用OM登录IP。'
          pattern: ''
          default: ''
        PGRCIPV6:
          name: '对端容灾控制通道IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '从对端获取，为对端OM登录IP，本端默认使用OM登录IP。'
          pattern: ''
          default: ''
    set_drhbnegotimer_list_1:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HELLOINTERVAL:
          name: '心跳消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '心跳消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为对端网元故障。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        NEGOINTERVAL:
          name: '协商消息传递间隔(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '协商消息达到“重传次数（TIMES）”参数值后，仍未收到响应消息时，则认为容灾组协商失败。'
          data_source: '与对端协商，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        TIMES:
          name: '重传次数'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: 'UEG间发送心跳和协商消息的重传次数。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        OMHBTIMES:
          name: 'OM通道心跳重传次数'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: '配置容灾控制通道1故障探测时长。'
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
        OMHBINTERVAL:
          name: 'OM通道心跳探测时长(100毫秒)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: '全网规划，建议使用此值，如需调整请联系华为技术支持。'
          pattern: ''
          default: ''
    set_drautoswover_list_1:
      type: items
      properties:
        AUTOSWOVER:
          name: '自动倒回功能开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '在热备容灾模式下开启自动倒回功能。  注：功能开启后，“默认运行状态”为ACTIVE的UEG网元故障后再恢复时，会发生自动倒换由该UEG网元继续做为主用网元。  由于UEG\_L中带有融合数据网元：   1. 2个UEG内的UDM/HSS、PCF/PCRF网元均会和IMS网元对接。IMS网元会优选1个UEG内的UDM/HSS、PCF/PCRF网元，为了防止UEG内的AMF/MME、SMF/GWC选择的UDM/HSS、PCF/PCRF网元和IMS网元选择不一致，导致融合数据处理冲突，因此需开启自动倒回功能。 2. 2个UEG内的UDR均会和营帐对接。营帐会固定选择1个UEG内的UDR进行开户，为了防止倒换后，无法进行开户操作，因此需开启自动倒回功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_drdci_list_1:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '引用**ADD DRGROUPINFO**定义的容灾组标识。可通过**LST DRGROUPINFO**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置容灾控制通道2。  两套UEG上，该参数取值必须一致。  DC间通信通道采用IPv4时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LDCIP:
          name: '本端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划，本端DRDCI IP地址。'
          pattern: ''
          default: ''
        PDCIP:
          name: '对端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划，对端DRDCI IP地址。'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '引用**ADD VPNINST**定义的VPN实例名称VRF\_PS\_Signal。可通过**LST VPNINST**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DATABKMODE:
          name: '数据备份模式'
          type: string
          enum:
          - Active-Standby
          - Active-Standby_Hot_Backup
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: Active-Standby
        HBINTERVAL:
          name: '心跳探测时长(100ms)'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: '心跳探测时长\*心跳重传次数=DC间容灾控制通道故障探测时长。'
          data_source: '全网规划'
          pattern: ''
          default: 10
        HBTIMES:
          name: '心跳重传次数'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 6
        LDCIPV6:
          name: '本端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划，本端DRDCI IP地址。'
          pattern: ''
          default: ''
        PDCIPV6:
          name: '对端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划，对端DRDCI IP地址。'
          pattern: ''
          default: ''
  examples:
    set_drcouplingreset_list:
    - COUPLINGRESET: NO
    set_drkeynf_list:
    - UPF: YES
      MME: YES
      AMF: YES
      HSS: YES
      UDM: YES
      SMF: YES
      GWC: YES
      PCF: YES
      PCRF: YES
      UDR: YES
    set_drtlsmode_list:
    - TLSMODE: OFF
    set_faultcheckbyfabric_list:
    - ENABLE: ON
      PROTECTDURATION: 10
      WAITRPTDURATION: 3000
    set_drgroupablement_list:
    - DRGROUPABLEMENT: ENABLE
      ISAUTOACTIVE: TRUE
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_DCI'
    add_drgroupinfo_list:
    - DRGROUPID: 1
      DRGROUPNAME: 'DRGROUP01'
      LDRINSTID: 1
      DFTMODE: ACTIVE
      PDRINSTID: 2
      IPVERSION: IPV4
      PGRCIP: '10.10.1.2'
      PGRCIPV6: 'fc00:3::2'
    set_drhbnegotimer_list:
    - DRGROUPID: 1
      HELLOINTERVAL: 5
      NEGOINTERVAL: 10
      TIMES: 5
      OMHBTIMES: 5
      OMHBINTERVAL: 5
    set_drautoswover_list:
    - AUTOSWOVER: ENABLE
    add_drdci_list:
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.198.8'
      PDCIP: '10.10.199.8'
      VPNINSTANCE: 'VPN_DCI'
      DATABKMODE: Active-Standby_Hot_Backup
      HBINTERVAL: 5
      HBTIMES: 4
      LDCIPV6: 'FC00::10:10:198:8'
      PDCIPV6: 'FC00::10:10:199:8'
    set_drcouplingreset_list_1:
    - COUPLINGRESET: NO
    set_drkeynf_list_1:
    - UPF: YES
      MME: YES
      AMF: YES
      HSS: YES
      UDM: YES
      SMF: YES
      GWC: YES
      PCF: YES
      PCRF: YES
      UDR: YES
    set_faultcheckbyfabric_list_1:
    - ENABLE: ON
      PROTECTDURATION: 10
      WAITRPTDURATION: 3000
    set_drgroupablement_list_1:
    - DRGROUPABLEMENT: ENABLE
      ISAUTOACTIVE: TRUE
    add_vpninst_list_1:
    - VPNINSTANCE: 'VPN_DCI'
    add_drgroupinfo_list_1:
    - DRGROUPID: 1
      DRGROUPNAME: 'DRGROUP01'
      LDRINSTID: 2
      DFTMODE: STANDBY
      PDRINSTID: 1
      IPVERSION: IPV4
      PGRCIP: '10.10.1.1'
      PGRCIPV6: 'fc00:3::1'
    set_drhbnegotimer_list_1:
    - DRGROUPID: 1
      HELLOINTERVAL: 5
      NEGOINTERVAL: 10
      TIMES: 5
      OMHBTIMES: 5
      OMHBINTERVAL: 5
    set_drautoswover_list_1:
    - AUTOSWOVER: ENABLE
    add_drdci_list_1:
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.199.8'
      PDCIP: '10.10.198.8'
      VPNINSTANCE: 'VPN_DCI'
      DATABKMODE: Active-Standby_Hot_Backup
      HBINTERVAL: 5
      HBTIMES: 4
      LDCIPV6: 'FC00::10:10:199:8'
      PDCIPV6: 'FC00::10:10:198:8'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在主用UEG进行配置，进入“MML命令行-UEG”窗口。

### 2 检查负荷分担容灾功能的使能开关是否为“NO”。

### “COUPLINGRESET”值为“YES”时，请执行3。

### “COUPLINGRESET”值为“NO”时，执行4。

### 3 关闭负荷分担容灾功能开关。

```jinja2
{%- set LST_DRCOUPLINGRESET=getParameterValue('LST DRCOUPLINGRESET') -%}
{%- if LST_DRCOUPLINGRESET=='YES' -%}
    {%- for item in set_drcouplingreset_list -%}
        SET DRCOUPLINGRESET:
        {#- --- 可选参数 --- -#}
        {%- if item.COUPLINGRESET is not none -%}
            COUPLINGRESET={{item.COUPLINGRESET}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 检查是否存在冗余的主备容灾模式的配置。

#### 4.1 执行**LST DRGROUPINFO**命令，查询是否存在容灾组信息。

#### 4.2 执行**LST DRDCI**命令，查询是否存在DCI通道信息。

### 存在冗余的主备容灾模式的配置，请执行5。

### 不存在冗余的主备容灾模式的配置，请执行9。

### 5 删除主备容灾模式配置。

#### 5.1 执行**RMV DRDCI**命令，删除DCI通道信息。

#### 5.2 执行**RMV DRGROUPINFO**命令，删除容灾组信息。

### 6 设置监控的关键部件信息。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 设置容灾控制通道TLS模式。

```jinja2
{%- for item in set_drtlsmode_list -%}
    SET DRTLSMODE:
    {#- --- 必选参数 --- -#}
    TLSMODE={{item.TLSMODE}},
    ;
{%- endfor -%}
```

### 8 设置快速故障检测。

```jinja2
{%- for item in set_faultcheckbyfabric_list -%}
    SET FAULTCHECKBYFABRIC:
    {#- --- 必选参数 --- -#}
    ENABLE={{item.ENABLE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ENABLE=ON 时必选 --- -#}
    {%- if item.ENABLE == 'ON' -%}
        PROTECTDURATION={{item.PROTECTDURATION}},
    {%- endif -%}
    {#- --- 条件必选：ENABLE=ON 时必选 --- -#}
    {%- if item.ENABLE == 'ON' -%}
        WAITRPTDURATION={{item.WAITRPTDURATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 使能热备容灾组。

```jinja2
{%- for item in set_drgroupablement_list -%}
    SET DRGROUPABLEMENT:
    {#- --- 必选参数 --- -#}
    DRGROUPABLEMENT={{item.DRGROUPABLEMENT}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISAUTOACTIVE is not none -%}
        ISAUTOACTIVE={{item.ISAUTOACTIVE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 增加VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 11 增加容灾组信息。

```jinja2
{%- for item in add_drgroupinfo_list -%}
    ADD DRGROUPINFO:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    DRGROUPNAME="{{item.DRGROUPNAME}}",
    LDRINSTID={{item.LDRINSTID}},
    DFTMODE={{item.DFTMODE}},
    PDRINSTID={{item.PDRINSTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PGRCIP="{{item.PGRCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PGRCIPV6="{{item.PGRCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 设置容灾定时器。

```jinja2
{%- for item in set_drhbnegotimer_list -%}
    SET DRHBNEGOTIMER:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.HELLOINTERVAL is not none -%}
        HELLOINTERVAL={{item.HELLOINTERVAL}},
    {%- endif -%}
    {%- if item.NEGOINTERVAL is not none -%}
        NEGOINTERVAL={{item.NEGOINTERVAL}},
    {%- endif -%}
    {%- if item.TIMES is not none -%}
        TIMES={{item.TIMES}},
    {%- endif -%}
    {%- if item.OMHBTIMES is not none -%}
        OMHBTIMES={{item.OMHBTIMES}},
    {%- endif -%}
    {%- if item.OMHBINTERVAL is not none -%}
        OMHBINTERVAL={{item.OMHBINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 使能自动倒回功能。

```jinja2
{%- for item in set_drautoswover_list -%}
    SET DRAUTOSWOVER:
    {#- --- 可选参数 --- -#}
    {%- if item.AUTOSWOVER is not none -%}
        AUTOSWOVER={{item.AUTOSWOVER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 14 增加DC间通信通道信息。

```jinja2
{%- for item in add_drdci_list -%}
    ADD DRDCI:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    IPVERSION={{item.IPVERSION}},
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DATABKMODE is not none -%}
        DATABKMODE={{item.DATABKMODE}},
    {%- endif -%}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.HBTIMES is not none -%}
        HBTIMES={{item.HBTIMES}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LDCIP="{{item.LDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PDCIP="{{item.PDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        LDCIPV6="{{item.LDCIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PDCIPV6="{{item.PDCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 15 在备用UEG进行配置，进入“MML命令行-UEG”窗口。

### 16 检查负荷分担容灾功能的使能开关是否为“NO”。

### “COUPLINGRESET”值为“YES”时，请执行17。

### “COUPLINGRESET”值为“NO”时，执行18。

### 17 关闭负荷分担容灾功能开关。

```jinja2
{%- if LST_DRCOUPLINGRESET=='YES' -%}
    {%- for item in set_drcouplingreset_list_1 -%}
        SET DRCOUPLINGRESET:
        {#- --- 可选参数 --- -#}
        {%- if item.COUPLINGRESET is not none -%}
            COUPLINGRESET={{item.COUPLINGRESET}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 18 检查是否存在冗余的主备容灾模式的配置。

#### 18.1 执行**LST DRDCI**命令，查询是否存在DCI通道信息。

#### 18.2 执行**LST DRGROUPINFO**命令，查询是否存在容灾组信息。

### 存在冗余的主备容灾模式的配置，请执行19。

### 不存在冗余的主备容灾模式的配置，请执行22。

### 19 删除主备容灾模式配置。

#### 19.1 执行**RMV DRDCI**命令，删除DCI通道信息。

#### 19.2 执行**RMV DRGROUPINFO**命令，删除容灾组信息。

### 20 设置监控的关键部件信息。

```jinja2
{%- for item in set_drkeynf_list_1 -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 21 设置快速故障检测。

```jinja2
{%- for item in set_faultcheckbyfabric_list_1 -%}
    SET FAULTCHECKBYFABRIC:
    {#- --- 必选参数 --- -#}
    ENABLE={{item.ENABLE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ENABLE=ON 时必选 --- -#}
    {%- if item.ENABLE == 'ON' -%}
        PROTECTDURATION={{item.PROTECTDURATION}},
    {%- endif -%}
    {#- --- 条件必选：ENABLE=ON 时必选 --- -#}
    {%- if item.ENABLE == 'ON' -%}
        WAITRPTDURATION={{item.WAITRPTDURATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 22 使能热备容灾组。

```jinja2
{%- for item in set_drgroupablement_list_1 -%}
    SET DRGROUPABLEMENT:
    {#- --- 必选参数 --- -#}
    DRGROUPABLEMENT={{item.DRGROUPABLEMENT}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISAUTOACTIVE is not none -%}
        ISAUTOACTIVE={{item.ISAUTOACTIVE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 23 增加VPN实例。

```jinja2
{%- for item in add_vpninst_list_1 -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 24 增加容灾组信息。

```jinja2
{%- for item in add_drgroupinfo_list_1 -%}
    ADD DRGROUPINFO:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    DRGROUPNAME="{{item.DRGROUPNAME}}",
    LDRINSTID={{item.LDRINSTID}},
    DFTMODE={{item.DFTMODE}},
    PDRINSTID={{item.PDRINSTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PGRCIP="{{item.PGRCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PGRCIPV6="{{item.PGRCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 25 设置容灾定时器。

```jinja2
{%- for item in set_drhbnegotimer_list_1 -%}
    SET DRHBNEGOTIMER:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.HELLOINTERVAL is not none -%}
        HELLOINTERVAL={{item.HELLOINTERVAL}},
    {%- endif -%}
    {%- if item.NEGOINTERVAL is not none -%}
        NEGOINTERVAL={{item.NEGOINTERVAL}},
    {%- endif -%}
    {%- if item.TIMES is not none -%}
        TIMES={{item.TIMES}},
    {%- endif -%}
    {%- if item.OMHBTIMES is not none -%}
        OMHBTIMES={{item.OMHBTIMES}},
    {%- endif -%}
    {%- if item.OMHBINTERVAL is not none -%}
        OMHBINTERVAL={{item.OMHBINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 26 使能自动倒回功能。

```jinja2
{%- for item in set_drautoswover_list_1 -%}
    SET DRAUTOSWOVER:
    {#- --- 可选参数 --- -#}
    {%- if item.AUTOSWOVER is not none -%}
        AUTOSWOVER={{item.AUTOSWOVER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 27 增加DC间通信通道信息。

```jinja2
{%- for item in add_drdci_list_1 -%}
    ADD DRDCI:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    IPVERSION={{item.IPVERSION}},
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DATABKMODE is not none -%}
        DATABKMODE={{item.DATABKMODE}},
    {%- endif -%}
    {%- if item.HBINTERVAL is not none -%}
        HBINTERVAL={{item.HBINTERVAL}},
    {%- endif -%}
    {%- if item.HBTIMES is not none -%}
        HBTIMES={{item.HBTIMES}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LDCIP="{{item.LDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PDCIP="{{item.PDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        LDCIPV6="{{item.LDCIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PDCIPV6="{{item.PDCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 备用UEG配置完成后会自动重启。重启后概率性出现“U2020到网元的配置同步失败”，请联系华为技术支持处理。

