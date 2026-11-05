---
id: ''
name: SMSF典型配置实例
ne_type: UNC
type: feature
description: 本任务实例实现以下场景配置：  UNC（作为SMSF）与周边NF（本例中包含AMF、NRF、UDM、SMSC）通过OSPF动态路由绑定动态BFD实现网络互通。  * 网络形态：5G网络 * 网元形态：SMSF * 路由协议：OSPF动态路由 * 组网IP格式：IPv4组网 * 接入用户：IPv4单栈用户
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core SMSF解决方案","SMSF功能部署","部署基础网络","部署UNC网元数据","部署SMSF对接数据","SMSF典型配置实例"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本任务实例实现以下场景配置：UNC（作为SMSF）与周边NF（本例中包含AMF、NRF、UDM、SMSC）通过OSPF动态路由绑定动态BFD实现网络互通。* 网络形态：5G网络* 网元形态：SMSF* 路由协议：OSPF动态路由* 组网IP格式：IPv4组网* 接入用户：IPv4单栈用户

## 必备事项
前提条件

* 请了解UNC各类接口的类型及命名规范，可参见业务组网与逻辑接口介绍。
* 基础数据配置、IP路由组网和业务接口配置子任务在前述章节已有详细描述，可参见基础数据配置、配置VNF侧IP路由数据（非SDN）、配置AMF，本文针对典型的任务场景举例说明整网脚本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_autoconfig_list:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_bfd_list:
      type: items
      properties:
        BFDENABLE:
          name: 'BFD使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstaf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        LSAARRINTV:
          name: '接收时间间隔（ms）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAG:
          name: '标签'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '引入路由类型'
          type: integer
          minimum: 1
          maximum: 2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_autoscalingservice_list:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTENABLE:
          name: '使能出方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        OSPFCOST:
          name: 'OSPF开销'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFDEADTIMER:
          name: '邻居失效的时间（s）'
          type: integer
          minimum: 0
          maximum: 235926000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFGRPENABLE:
          name: '使能OSPF进程组'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFHELLOTIMER:
          name: '邻居发送Hello包时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        OSPFINSTID:
          name: 'OSPF实例ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINLINKFLAG:
          name: '入方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINNAME:
          name: '入方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPOUTLINKFLAG:
          name: '出方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTNAME:
          name: '出方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstaf_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospf_list_1:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        LSAARRINTV:
          name: '接收时间间隔（ms）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfarea_list_1:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfimportroute_list_1:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAG:
          name: '标签'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '引入路由类型'
          type: integer
          minimum: 1
          maximum: 2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_autoscalingservice_list_2:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTENABLE:
          name: '使能出方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        OSPFCOST:
          name: 'OSPF开销'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFDEADTIMER:
          name: '邻居失效的时间（s）'
          type: integer
          minimum: 0
          maximum: 235926000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFGRPENABLE:
          name: '使能OSPF进程组'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFHELLOTIMER:
          name: '邻居发送Hello包时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        OSPFINSTID:
          name: 'OSPF实例ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINLINKFLAG:
          name: '入方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINNAME:
          name: '入方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPOUTLINKFLAG:
          name: '出方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTNAME:
          name: '出方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l3vpninst_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vpninstaf_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospf_list_2:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: '路由器标识'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BFDALLINTFFLG:
          name: '使能BFD'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRINTVFLAG:
          name: '取消使用智能定时器配置LSA接收的间隔时间'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        LSAARRMAXINTV:
          name: '接收最长间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1000
        LSAARRSTARINTV:
          name: '接收初始间隔时间（ms）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        LSAARRHLDINTV:
          name: '接收基数间隔时间（ms）'
          type: integer
          minimum: 1
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        VPNINSCAPSIMFLG:
          name: '去使能VPN路由环路检测'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        VIRTUALSYSFLAG:
          name: 'OSPF共网段虚拟系统使能标志'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        LSAARRINTV:
          name: '接收时间间隔（ms）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfarea_list_2:
      type: items
      properties:
        PROCID:
          name: '进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospfimportroute_list_2:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMPTCOSTCFG:
          name: '引入路由开销值配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTAGCFG:
          name: '引入路由标签配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IMPTTYPECFG:
          name: '引入路由类型配置'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        COST:
          name: '路径Cost值'
          type: integer
          minimum: 0
          maximum: 16777214
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAG:
          name: '标签'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '引入路由类型'
          type: integer
          minimum: 1
          maximum: 2
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PERMITIBGPCFG:
          name: '允许BGP配置'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        PROTOCOLPROCID:
          name: '协议进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
    add_autoscalingservice_list_4:
      type: items
      properties:
        SERVICENAME:
          name: '服务名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPALLOCTYPE4:
          name: 'IPv4地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        VNICID:
          name: '虚拟网卡ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VLANID:
          name: 'VLAN ID'
          type: integer
          minimum: 0
          maximum: 4094
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        BEGINADDR4:
          name: '起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDADDR4:
          name: '结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLEN:
          name: '地址池掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFENABLE:
          name: '使能OSPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFPROCID:
          name: 'OSPF进程ID'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFAREAID:
          name: 'OSPF区域ID'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINENABLE:
          name: '使能入方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTENABLE:
          name: '使能出方向的流量策略'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        IPALLOCTYPE6:
          name: 'IPv6地址分配方式'
          type: string
          enum:
          - DHCP
          - USER_CONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USER_CONFIG
        AUTOCFGIFTYPE:
          name: '自动化配置接口类型'
          type: string
          enum:
          - ETHTRUNK
          - VNIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VNIC
        OSPFCOST:
          name: 'OSPF开销'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFDEADTIMER:
          name: '邻居失效的时间（s）'
          type: integer
          minimum: 0
          maximum: 235926000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OSPFGRPENABLE:
          name: '使能OSPF进程组'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        OSPFHELLOTIMER:
          name: '邻居发送Hello包时间间隔（s）'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        OSPFINSTID:
          name: 'OSPF实例ID'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPINLINKFLAG:
          name: '入方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPINNAME:
          name: '入方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TPOUTLINKFLAG:
          name: '出方向的流量策略链接标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        TPOUTNAME:
          name: '出方向的流量策略名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_autoconfig_list_1:
      type: items
      properties:
        SWITCHFLAG:
          name: '自动配置开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_ngmno_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nghplmn_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngsrvplmn_list:
      type: items
      properties:
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
        NOID:
          name: '运营商标识'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
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
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
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
    add_httplegrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httple_list:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sbiaple_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFTYPE:
          name: '本端NF类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeMBSMF
          - NFTypeNWDAF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfuuid_list:
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
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfprofile_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - Undiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
    add_nfservice_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - SrvNameINVALID
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmPlcCtrl
          - NpcfPlcauth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgmt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - Nnef3gppAsSessionWithQos
          - Nnef3gppMonEvent
          - NnwdafDataManagement
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservicever_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APIFULLVERSION:
          name: 'API版本信息'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
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
          - NoneIP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
    add_subcondition_list:
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
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrf_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
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
          - NoneIP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SUBSCRISWITCH:
          name: '订阅流程开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: OFF
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ON
    add_subcondition_list_1:
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
        CONDITION:
          name: '订阅条件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REQNOTIFEVENT:
          name: '通知事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    act_nfonline_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
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
        IPV4ADDRESS2:
          name: 'IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS3:
          name: 'IPV4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS4:
          name: 'IPV4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPV6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPV6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS3:
          name: 'IPV6地址3'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS4:
          name: 'IPV6地址4'
          type: string
          maxLength: 39
          required: false
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
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HTTPS
    add_pnfservice_list:
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
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
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
    add_pnfsupi_list:
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
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfplmn_list:
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
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list_1:
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
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Registered
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
        IPV4ADDRESS2:
          name: 'IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS3:
          name: 'IPV4地址3'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS4:
          name: 'IPV4地址4'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: 'IPV6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: 'IPV6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS3:
          name: 'IPV6地址3'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS4:
          name: 'IPV6地址4'
          type: string
          maxLength: 39
          required: false
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
        SCHEME:
          name: '协议模式'
          type: string
          enum:
          - HTTP
          - HTTPS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HTTPS
    add_pnfservice_list_2:
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
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REGISTERED
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
    add_pnfsupi_list_1:
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
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfplmn_list_1:
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
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
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
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_m3le_list:
      type: items
      properties:
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本地实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LET:
          name: '本地实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEN:
          name: '本地实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3de_list:
      type: items
      properties:
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的实体编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSSM:
          name: '链路集选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        STPF:
          name: '信令转接点功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DET:
          name: '目的实体类型'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          - SP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADJF:
          name: '相邻标记'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TRUE
        NMD:
          name: '网络模式'
          type: string
          enum:
          - EXCLUSIVE
          - INCLUSIVE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: EXCLUSIVE
        PVER:
          name: 'M3UA协议版本'
          type: string
          enum:
          - DRAFT10
          - RFC3332
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RFC3332
        DEN:
          name: '目的实体名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3lks_list:
      type: items
      properties:
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SLSM:
          name: '链路选择掩码'
          type: string
          enum:
          - B0000
          - B0001
          - B0010
          - B0011
          - B0100
          - B0101
          - B0110
          - B0111
          - B1000
          - B1001
          - B1010
          - B1011
          - B1100
          - B1101
          - B1110
          - B1111
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: B0000
        WM:
          name: '工作模式'
          type: string
          enum:
          - ASP
          - IPSP
          - SGP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TM:
          name: '业务模式'
          type: string
          enum:
          - LOADSHARE
          - OVERRIDE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOADSHARE
        LSN:
          name: '链路集名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_m3rt_list:
      type: items
      properties:
        RTX:
          name: '路由索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEX:
          name: '目的实体索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        RTN:
          name: '信令路由名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPPARANAME:
          name: 'SCTP协议参数名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        PKGERRFAULT:
          name: '错包率故障门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        PKGERRRECOVER:
          name: '错包率恢复门限'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        MINRECVPKGNUM:
          name: '单偶联最小收包数'
          type: integer
          minimum: 10
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_m3lnk_list:
      type: items
      properties:
        LNK:
          name: '链路号'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
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
        IPT:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        LOCIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV42:
          name: '本地IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        PEERIPV41:
          name: '对端IP地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV42:
          name: '对端IP地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: '255.255.255.255'
        PEERPORT:
          name: '对端端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 2905
        CS:
          name: 'C/S模式'
          type: string
          enum:
          - C
          - S
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LSX:
          name: '链路集索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ASF:
          name: '主备标识'
          type: string
          enum:
          - ACT
          - STD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ACT
        PRI:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CONSTHD:
          name: '拥塞开始门限'
          type: integer
          minimum: 60
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 80
        CONETHD:
          name: '拥塞结束门限'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 40
        CROSSIP:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        EXCHGMODE:
          name: '交换模式'
          type: string
          enum:
          - DOUBLE
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
        LKN:
          name: '链路名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        SCTPINDX:
          name: 'SCTP 参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV61:
          name: '对端IP地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV62:
          name: '对端IP地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpopc_list:
      type: items
      properties:
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: '信令点用途'
          type: string
          enum:
          - COREONLY
          - IUANDCORE
          - IUONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: COREONLY
        SGSNN:
          name: '本局SGSN号'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sccpdpc_list:
      type: items
      properties:
        DPX:
          name: '目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPX:
          name: '本局信令点索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SS7T:
          name: '协议类型'
          type: string
          enum:
          - ANSI_SS7
          - ITUT_SS7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ITUT_SS7
        LDP:
          name: '负荷分担类型'
          type: string
          enum:
          - BACKUP
          - LOADSHARE
          - MULTIDPCLOADSHARE
          - NOUSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NOUSE
        DPN:
          name: '目的信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        BDPX:
          name: '备用目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDPX:
          name: '负荷分担目的信令点索引'
          type: integer
          minimum: 0
          maximum: 1279
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_smsfopc_list:
      type: items
      properties:
        OPX:
          name: 'SMSF信令点索引'
          type: integer
          minimum: 1
          maximum: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMSFN:
          name: '本局SMSF号'
          type: string
          maxLength: 16
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPN:
          name: '本局信令点名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        MASTER:
          name: '是否主用信令点'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sccpssn_list:
      type: items
      properties:
        SSNX:
          name: '子系统索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPC:
          name: '本局信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSNNAME:
          name: '子系统名'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_sccpgt_list:
      type: items
      properties:
        GTX:
          name: 'GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RT:
          name: '翻译结果类型'
          type: string
          enum:
          - DPC
          - DPCGT
          - DPCNEWGT
          - DPCSSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GTEXP:
          name: 'GT码表示语'
          type: string
          enum:
          - FOUR
          - SIX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FOUR
        NP:
          name: '编号计划'
          type: string
          enum:
          - DATA
          - ISDNMS
          - ISDNP
          - PMS
          - SMS
          - TELEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ISDNP
        ADDREXP:
          name: '地址性质表示语'
          type: string
          enum:
          - FREE
          - INTDN
          - NSU
          - NVU
          - SUBDN
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INTDN
        ADDR:
          name: '地址信息'
          type: string
          maxLength: 20
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DPC:
          name: '目的信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'SCCP GT名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        TT:
          name: '翻译类型'
          type: string
          enum:
          - ANSI10
          - ANSI9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ANSI9
        NGTX:
          name: '新GT码索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SSN:
          name: '子系统号'
          type: string
          enum:
          - BSSAP
          - BSSAP+
          - CAP
          - EIR
          - GGSN
          - GMLC
          - HLR
          - INAP
          - MAP
          - MSC
          - NODEFINE
          - OMAP
          - RANAP
          - SCMG
          - SGSN
          - STANDBY0
          - STANDBY1
          - VLR
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_autoconfig_list:
    - SWITCHFLAG: FALSE
    set_bfd_list:
    - BFDENABLE: TRUE
    add_l3vpninst_list:
    - VRFNAME: 'VRF_SBI'
    add_vpninstaf_list:
    - VRFNAME: 'VRF_SBI'
      AFTYPE: ipv4uni
    add_ospf_list:
    - PROCID: 6
      VRFNAME: 'VRF_SBI'
      SCHEMAROUID: '192.168.35.210'
      BFDALLINTFFLG: TRUE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list:
    - PROCID: 6
      AREAID: '10.0.0.5'
    add_ospfimportroute_list:
    - PROCID: 6
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: ''
      TAG: ''
      TYPE: ''
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
    add_autoscalingservice_list:
    - SERVICENAME: 'VRF_SBI_100'
      VPNNAME: 'VRF_SBI'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      VNICID: 4
      VLANID: 100
      BEGINADDR4: '192.168.89.2'
      ENDADDR4: '192.168.89.14'
      MASKLEN: 28
      OSPFENABLE: TRUE
      OSPFPROCID: 6
      OSPFAREAID: '10.0.0.5'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    add_l3vpninst_list_1:
    - VRFNAME: 'VRF_MME'
    add_vpninstaf_list_1:
    - VRFNAME: 'VRF_MME'
      AFTYPE: ipv4uni
    add_ospf_list_1:
    - PROCID: 7
      VRFNAME: 'VRF_MME'
      SCHEMAROUID: '192.168.36.210'
      BFDALLINTFFLG: TRUE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list_1:
    - PROCID: 7
      AREAID: '10.0.0.6'
    add_ospfimportroute_list_1:
    - PROCID: 7
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: ''
      TAG: ''
      TYPE: ''
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
    add_autoscalingservice_list_2:
    - SERVICENAME: 'VRF_MME_103'
      VPNNAME: 'VRF_MME'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      VNICID: 6
      VLANID: 103
      BEGINADDR4: '192.168.86.2'
      ENDADDR4: '192.168.86.14'
      MASKLEN: 28
      OSPFENABLE: TRUE
      OSPFPROCID: 7
      OSPFAREAID: '10.0.0.6'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    add_l3vpninst_list_2:
    - VRFNAME: 'VRF_Access'
    add_vpninstaf_list_2:
    - VRFNAME: 'VRF_Access'
      AFTYPE: ipv4uni
    add_ospf_list_2:
    - PROCID: 8
      VRFNAME: 'VRF_Access'
      SCHEMAROUID: '192.168.36.210'
      BFDALLINTFFLG: TRUE
      LSAARRINTVFLAG: FALSE
      LSAARRMAXINTV: 1000
      LSAARRSTARINTV: 500
      LSAARRHLDINTV: 500
      VPNINSCAPSIMFLG: TRUE
      VIRTUALSYSFLAG: TRUE
      LSAARRINTV: ''
    add_ospfarea_list_2:
    - PROCID: 8
      AREAID: '10.0.0.6'
    add_ospfimportroute_list_2:
    - PROCID: 8
      TOPOID: 0
      PROTOCOL: wlr
      IMPTCOSTCFG: FALSE
      IMPTTAGCFG: FALSE
      IMPTTYPECFG: FALSE
      COST: ''
      TAG: ''
      TYPE: ''
      PERMITIBGPCFG: FALSE
      PROTOCOLPROCID: 1
    add_autoscalingservice_list_4:
    - SERVICENAME: 'VRF_Access_104'
      VPNNAME: 'VRF_Access'
      AFTYPE: IPv4
      IPALLOCTYPE4: USER_CONFIG
      VNICID: 8
      VLANID: 104
      BEGINADDR4: '192.168.85.2'
      ENDADDR4: '192.168.85.14'
      MASKLEN: 28
      OSPFENABLE: TRUE
      OSPFPROCID: 8
      OSPFAREAID: '10.0.0.6'
      TPINENABLE: FALSE
      TPOUTENABLE: FALSE
      IPALLOCTYPE6: USER_CONFIG
      AUTOCFGIFTYPE: VNIC
      OSPFCOST: ''
      OSPFDEADTIMER: ''
      OSPFGRPENABLE: FALSE
      OSPFHELLOTIMER: ''
      OSPFINSTID: ''
      TPINLINKFLAG: FALSE
      TPINNAME: ''
      TPOUTLINKFLAG: FALSE
      TPOUTNAME: ''
    set_autoconfig_list_1:
    - SWITCHFLAG: TRUE
    mod_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_ngsrvplmn_list:
    - PLMNIDX: 0
      NOID: 0
      MCC: '123'
      MNC: '03'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.180.15'
      VPNINSTNAME: '_public_'
      DESC: 'FOR SBI'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 6
      DESC: 'SMSF'
    add_httple_list:
    - INDEX: 11
      HTTPLEGRPIDX: 6
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.2.180.15'
      PORT: 8080
      VPNNAME: '_public_'
      TLSFLG: NO
      DESC: 'SMSF_Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 6
      HTTPLEGRPIDX: 6
      NFTYPE: NFTypeSMSF
      DESCRIPTION: 'SMSF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_nfuuid_list:
    - NFTYPE: NfSMSF
      NFINSTANCENAME: 'SMSF_Instance_0'
    add_nfprofile_list:
    - NFINSTANCENAME: 'SMSF_Instance_0'
      NFTYPE: NfSMSF
      NFSTATUS: Registered
    add_nfservice_list:
    - NFINSTANCENAME: 'SMSF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmsfSms
    add_nfservicever_list:
    - NFINSTANCENAME: 'SMSF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: FALSE
      PRIORITY: 0
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    add_subcondition_list:
    - NFTYPE: NfAMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    add_nrf_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.26.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    add_subcondition_list_1:
    - NFTYPE: NfAMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    act_nfonline_list:
    - NFINSTANCENAME: 'SMSF_Instance_0'
    add_pnfprofile_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.50.0.213'
      PORT: 8080
      PRIORITY: 0
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      FQDN: ''
      SCHEME: HTTPS
    add_pnfservice_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
      PRIORITY: 0
    add_pnfsupi_list:
    - INDEX: 2
      NFINSTANCEID: 'UDM_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123030000000000'
      RANGEEND: '123031000000000'
      PATTERN: ''
    add_pnfplmn_list:
    - NFINSTANCEID: 'UDM_Instance_0'
      MCC: '123'
      MNC: '03'
    add_pnfprofile_list_1:
    - NFINSTANCEID: 'AMF_Instance_0'
      NFTYPE: NfAMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.50.0.212'
      PORT: 8080
      PRIORITY: 0
      IPV4ADDRESS2: ''
      IPV4ADDRESS3: ''
      IPV4ADDRESS4: ''
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6ADDRESS3: ''
      IPV6ADDRESS4: ''
      FQDN: ''
      SCHEME: HTTPS
    add_pnfservice_list_2:
    - NFINSTANCEID: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
      PRIORITY: 0
    add_pnfsupi_list_1:
    - INDEX: 1
      NFINSTANCEID: 'AMF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123030000000000'
      RANGEEND: '123031000000000'
      PATTERN: ''
    add_pnfplmn_list_1:
    - NFINSTANCEID: 'AMF_Instance_0'
      MCC: '123'
      MNC: '03'
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.2.180.1'
      VPNINSTNAME: 'VPN_SIG'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_m3le_list:
    - LEX: 1
      NI: NAT
      OPC: '0x017701'
      LET: ASP
      LEN: 'SMSC'
    add_m3de_list:
    - DEX: 1
      LEX: 1
      DPC: '0x240011'
      SLSSM: B0000
      STPF: DISABLE
      DET: SGP
      ADJF: TRUE
      NMD: EXCLUSIVE
      PVER: RFC3332
      DEN: 'SMSC'
    add_m3lks_list:
    - LSX: 1
      DEX: 1
      SLSM: B0000
      WM: ASP
      TM: LOADSHARE
      LSN: 'SMSC'
    add_m3rt_list:
    - RTX: 1
      DEX: 1
      LSX: 1
      PRI: 0
      RTN: 'SMSC'
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      SCTPPARANAME: 'sctname'
      PKGERRFAULT: 5
      PKGERRRECOVER: 3
      MINRECVPKGNUM: 100
    add_m3lnk_list:
    - LNK: 1
      VPNNAME: 'VPN_SIG'
      IPT: IPV4
      LOCIPV41: '10.2.180.1'
      LOCIPV42: '10.255.255.255'
      LOCPORT: 17171
      PEERIPV41: '10.50.0.202'
      PEERIPV42: '10.255.255.255'
      PEERPORT: 17171
      CS: C
      LSX: 1
      ASF: ACT
      PRI: 0
      CONSTHD: 80
      CONETHD: 40
      CROSSIP: NO
      EXCHGMODE: SINGLE
      LKN: 'To SMSC'
      SCTPINDX: 0
      LOCIPV61: ''
      LOCIPV62: ''
      PEERIPV61: ''
      PEERIPV62: ''
    add_sccpopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x17701'
      SPN: COREONLY
      SGSNN: '861390211101'
      OPN: 'SMSC'
    add_sccpdpc_list:
    - DPX: 1
      OPX: 1
      DPC: '0x240011'
      SS7T: ITUT_SS7
      LDP: NOUSE
      DPN: 'rnc'
      BDPX: ''
      SDPX: ''
    add_smsfopc_list:
    - OPX: 1
      NI: NAT
      OPC: '0x17701'
      SMSFN: '861390211101'
      OPN: 'peklin'
      MASTER: YES
    add_sccpssn_list:
    - SSNX: 1
      SSN: SCMG
      NI: NAT
      DPC: '0x017701'
      OPC: '0x017701'
      SSNNAME: 'SGSN_BER1-SSN'
    add_sccpgt_list:
    - GTX: 1
      NI: NAT
      RT: DPC
      GTEXP: FOUR
      NP: ISDNP
      ADDREXP: INTDN
      ADDR: '861390211101'
      DPC: '0x17701'
      NAME: 'SGSN_BER1-GT'
      TT: ANSI9
      NGTX: ''
      SSN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 全部展开

### 1 配置IP路由数据

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 关闭自动配置开关。

##### 1.2.1 查询自动配置开关状态。

##### 如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。

##### 1.2.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

##### 1.2.3 关闭自动配置开关。

```jinja2
{%- set LST_AUTOCONFIG=getParameterValue('LST AUTOCONFIG') -%}
{%- if LST_AUTOCONFIG=='TRUE' -%}
    {%- for item in set_autoconfig_list -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

#### 1.4 配置UNC与对端AMF、NRF、UDM的IP路由数据。

##### 1.4.1 配置外联口的VPN实例。

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 1.4.2 配置OSPF路由。

###### 1.4.2.1 创建OSPF进程。

```jinja2
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
        LSAARRINTV={{item.LSAARRINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.4.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

###### 如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

###### 1.4.2.3 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTAGCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTAGCFG == 'TRUE' -%}
        TAG={{item.TAG}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTYPECFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTYPECFG == 'TRUE' -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
    {%- if item.PROTOCOL == 'BGP' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
    {%- if item.PROTOCOL == 'OSPF' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.4.3 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {%- if item.OSPFENABLE is not none -%}
        OSPFENABLE={{item.OSPFENABLE}},
    {%- endif -%}
    {%- if item.TPINENABLE is not none -%}
        TPINENABLE={{item.TPINENABLE}},
    {%- endif -%}
    {%- if item.TPOUTENABLE is not none -%}
        TPOUTENABLE={{item.TPOUTENABLE}},
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
        VNICID={{item.VNICID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFPROCID={{item.OSPFPROCID}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFAREAID="{{item.OSPFAREAID}}",
    {%- endif -%}
    {#- --- 条件必选：TPINENABLE=TRUE 时必选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        TPINNAME="{{item.TPINNAME}}",
    {%- endif -%}
    {#- --- 条件必选：TPOUTENABLE=TRUE 时必选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        TPOUTNAME="{{item.TPOUTNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFCOST is not none -%}
            OSPFCOST={{item.OSPFCOST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFDEADTIMER is not none -%}
            OSPFDEADTIMER={{item.OSPFDEADTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'FALSE' -%}
        {%- if item.OSPFGRPENABLE is not none -%}
            OSPFGRPENABLE={{item.OSPFGRPENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFHELLOTIMER is not none -%}
            OSPFHELLOTIMER={{item.OSPFHELLOTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFINSTID is not none -%}
            OSPFINSTID={{item.OSPFINSTID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPINENABLE=TRUE 时可选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        {%- if item.TPINLINKFLAG is not none -%}
            TPINLINKFLAG={{item.TPINLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPOUTENABLE=TRUE 时可选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        {%- if item.TPOUTLINKFLAG is not none -%}
            TPOUTLINKFLAG={{item.TPOUTLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 配置UNC与对端SMSC的IP路由数据。

##### 1.5.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_1 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_1 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 1.5.2 配置OSPF路由。

###### 1.5.2.1 创建OSPF进程。

```jinja2
{%- for item in add_ospf_list_1 -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
        LSAARRINTV={{item.LSAARRINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.5.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_1 -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

###### 1.5.2.3 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list_1 -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTAGCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTAGCFG == 'TRUE' -%}
        TAG={{item.TAG}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTYPECFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTYPECFG == 'TRUE' -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
    {%- if item.PROTOCOL == 'BGP' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
    {%- if item.PROTOCOL == 'OSPF' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.5.3 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list_2 -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {%- if item.OSPFENABLE is not none -%}
        OSPFENABLE={{item.OSPFENABLE}},
    {%- endif -%}
    {%- if item.TPINENABLE is not none -%}
        TPINENABLE={{item.TPINENABLE}},
    {%- endif -%}
    {%- if item.TPOUTENABLE is not none -%}
        TPOUTENABLE={{item.TPOUTENABLE}},
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
        VNICID={{item.VNICID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFPROCID={{item.OSPFPROCID}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFAREAID="{{item.OSPFAREAID}}",
    {%- endif -%}
    {#- --- 条件必选：TPINENABLE=TRUE 时必选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        TPINNAME="{{item.TPINNAME}}",
    {%- endif -%}
    {#- --- 条件必选：TPOUTENABLE=TRUE 时必选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        TPOUTNAME="{{item.TPOUTNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFCOST is not none -%}
            OSPFCOST={{item.OSPFCOST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFDEADTIMER is not none -%}
            OSPFDEADTIMER={{item.OSPFDEADTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'FALSE' -%}
        {%- if item.OSPFGRPENABLE is not none -%}
            OSPFGRPENABLE={{item.OSPFGRPENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFHELLOTIMER is not none -%}
            OSPFHELLOTIMER={{item.OSPFHELLOTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFINSTID is not none -%}
            OSPFINSTID={{item.OSPFINSTID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPINENABLE=TRUE 时可选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        {%- if item.TPINLINKFLAG is not none -%}
            TPINLINKFLAG={{item.TPINLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPOUTENABLE=TRUE 时可选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        {%- if item.TPOUTLINKFLAG is not none -%}
            TPOUTLINKFLAG={{item.TPOUTLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 配置UNC与对端IP-SM-GW的IP路由数据。

##### 1.6.1 配置VPN实例。

```jinja2
{%- for item in add_l3vpninst_list_2 -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninstaf_list_2 -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    ;
{%- endfor -%}
```

##### 1.6.2 配置OSPF路由。

###### 1.6.2.1 创建OSPF进程。

```jinja2
{%- for item in add_ospf_list_2 -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    {%- if item.BFDALLINTFFLG is not none -%}
        BFDALLINTFFLG={{item.BFDALLINTFFLG}},
    {%- endif -%}
    {%- if item.LSAARRINTVFLAG is not none -%}
        LSAARRINTVFLAG={{item.LSAARRINTVFLAG}},
    {%- endif -%}
    {%- if item.VPNINSCAPSIMFLG is not none -%}
        VPNINSCAPSIMFLG={{item.VPNINSCAPSIMFLG}},
    {%- endif -%}
    {%- if item.VIRTUALSYSFLAG is not none -%}
        VIRTUALSYSFLAG={{item.VIRTUALSYSFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRMAXINTV={{item.LSAARRMAXINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRSTARINTV={{item.LSAARRSTARINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=FALSE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'FALSE' -%}
        LSAARRHLDINTV={{item.LSAARRHLDINTV}},
    {%- endif -%}
    {#- --- 条件必选：LSAARRINTVFLAG=TRUE 时必选 --- -#}
    {%- if item.LSAARRINTVFLAG == 'TRUE' -%}
        LSAARRINTV={{item.LSAARRINTV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.6.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_2 -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

###### 1.6.2.3 设置OSPF引入路由类型。

```jinja2
{%- for item in add_ospfimportroute_list_2 -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    {%- if item.IMPTCOSTCFG is not none -%}
        IMPTCOSTCFG={{item.IMPTCOSTCFG}},
    {%- endif -%}
    {%- if item.IMPTTAGCFG is not none -%}
        IMPTTAGCFG={{item.IMPTTAGCFG}},
    {%- endif -%}
    {%- if item.IMPTTYPECFG is not none -%}
        IMPTTYPECFG={{item.IMPTTYPECFG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMPTCOSTCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTCOSTCFG == 'TRUE' -%}
        COST={{item.COST}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTAGCFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTAGCFG == 'TRUE' -%}
        TAG={{item.TAG}},
    {%- endif -%}
    {#- --- 条件必选：IMPTTYPECFG=TRUE 时必选 --- -#}
    {%- if item.IMPTTYPECFG == 'TRUE' -%}
        TYPE={{item.TYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROTOCOL=BGP 时可选 --- -#}
    {%- if item.PROTOCOL == 'BGP' -%}
        {%- if item.PERMITIBGPCFG is not none -%}
            PERMITIBGPCFG={{item.PERMITIBGPCFG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROTOCOL=OSPF 时可选 --- -#}
    {%- if item.PROTOCOL == 'OSPF' -%}
        {%- if item.PROTOCOLPROCID is not none -%}
            PROTOCOLPROCID={{item.PROTOCOLPROCID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.6.3 配置外联口自动部署模板。

```jinja2
{%- for item in add_autoscalingservice_list_4 -%}
    ADD AUTOSCALINGSERVICE:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.VLANID is not none -%}
        VLANID={{item.VLANID}},
    {%- endif -%}
    {%- if item.OSPFENABLE is not none -%}
        OSPFENABLE={{item.OSPFENABLE}},
    {%- endif -%}
    {%- if item.TPINENABLE is not none -%}
        TPINENABLE={{item.TPINENABLE}},
    {%- endif -%}
    {%- if item.TPOUTENABLE is not none -%}
        TPOUTENABLE={{item.TPOUTENABLE}},
    {%- endif -%}
    {%- if item.AUTOCFGIFTYPE is not none -%}
        AUTOCFGIFTYPE={{item.AUTOCFGIFTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTOCFGIFTYPE=VNIC 时必选 --- -#}
    {%- if item.AUTOCFGIFTYPE == 'VNIC' -%}
        VNICID={{item.VNICID}},
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        BEGINADDR4="{{item.BEGINADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        ENDADDR4="{{item.ENDADDR4}}",
    {%- endif -%}
    {#- --- 条件必选：IPALLOCTYPE4=USER_CONFIG 时必选 --- -#}
    {%- if item.IPALLOCTYPE4 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {#- --- 条件必选：IPALLOCTYPE6=USER_CONFIG 时必选 --- -#}
    {%- elif item.IPALLOCTYPE6 == 'USER_CONFIG' -%}
        MASKLEN={{item.MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFPROCID={{item.OSPFPROCID}},
    {%- endif -%}
    {#- --- 条件必选：OSPFENABLE=TRUE 时必选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        OSPFAREAID="{{item.OSPFAREAID}}",
    {%- endif -%}
    {#- --- 条件必选：TPINENABLE=TRUE 时必选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        TPINNAME="{{item.TPINNAME}}",
    {%- endif -%}
    {#- --- 条件必选：TPOUTENABLE=TRUE 时必选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        TPOUTNAME="{{item.TPOUTNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：AFTYPE=IPv4 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv4' -%}
        {%- if item.IPALLOCTYPE4 is not none -%}
            IPALLOCTYPE4={{item.IPALLOCTYPE4}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AFTYPE=IPv6 时可选 --- -#}
    {%- if item.AFTYPE == 'IPv6' -%}
        {%- if item.IPALLOCTYPE6 is not none -%}
            IPALLOCTYPE6={{item.IPALLOCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFCOST is not none -%}
            OSPFCOST={{item.OSPFCOST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFDEADTIMER is not none -%}
            OSPFDEADTIMER={{item.OSPFDEADTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=FALSE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'FALSE' -%}
        {%- if item.OSPFGRPENABLE is not none -%}
            OSPFGRPENABLE={{item.OSPFGRPENABLE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFHELLOTIMER is not none -%}
            OSPFHELLOTIMER={{item.OSPFHELLOTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：OSPFENABLE=TRUE 时可选 --- -#}
    {%- if item.OSPFENABLE == 'TRUE' -%}
        {%- if item.OSPFINSTID is not none -%}
            OSPFINSTID={{item.OSPFINSTID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPINENABLE=TRUE 时可选 --- -#}
    {%- if item.TPINENABLE == 'TRUE' -%}
        {%- if item.TPINLINKFLAG is not none -%}
            TPINLINKFLAG={{item.TPINLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TPOUTENABLE=TRUE 时可选 --- -#}
    {%- if item.TPOUTENABLE == 'TRUE' -%}
        {%- if item.TPOUTLINKFLAG is not none -%}
            TPOUTLINKFLAG={{item.TPOUTLINKFLAG}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 打开IP路由自动配置开关。

```jinja2
{%- for item in set_autoconfig_list_1 -%}
    SET AUTOCONFIG:
    {#- --- 必选参数 --- -#}
    SWITCHFLAG={{item.SWITCHFLAG}},
    ;
{%- endfor -%}
```

#### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 2 配置SMSF基础数据

### AMF寻呼用户的定时器默认为6秒，寻呼次数为3次；SMSF的HTTP接口等待响应超时定时器默认为5秒。

### 在空闲态UE的短信被叫流程中，如果UE不能在5秒之内响应寻呼，SMSF将认为UE不可达，并向短信中心返回SMS传输失败。短信中心再通过重传流程向UE下发短信。

#### 2.1 进入“MML命令行-UNC”窗口。

#### 2.2 配置运营商基础信息。

##### 2.2.1 增加运营商信息。

```jinja2
{%- for item in mod_ngmno_list -%}
    MOD NGMNO:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    {#- --- 可选参数 --- -#}
    {%- if item.FULLNAME is not none -%}
        FULLNAME="{{item.FULLNAME}}",
    {%- endif -%}
    {%- if item.SHORTNAME is not none -%}
        SHORTNAME="{{item.SHORTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.2.2 配置运营商签约用户的Home PLMN信息，用于识别用户是否为本网签约用户。

```jinja2
{%- for item in add_nghplmn_list -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

##### 2.2.3 配置运营商的Serving PLMN信息。

```jinja2
{%- for item in add_ngsrvplmn_list -%}
    ADD NGSRVPLMN:
    {#- --- 必选参数 --- -#}
    PLMNIDX={{item.PLMNIDX}},
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 2.3 增加SMSF服务化接口数据。

##### 2.3.1 增加SMSF服务化接口的IP地址，用于和AMF、UDM等NF的对接。

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
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

##### 2.3.2 配置SMSF服务化接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list -%}
    ADD HTTPLEGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.3.3 配置SMSF分别作为HTTP服务的服务端和客户端的本端端点信息。

```jinja2
{%- for item in add_httple_list -%}
    ADD HTTPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    LETYPE={{item.LETYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.3.4 配置SMSF服务化接口的接入点信息。

```jinja2
{%- for item in add_sbiaple_list -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SMSF到NRF的数据（网络中部署了NRF时需要执行）

#### 3.1 配置SMSF实例信息，用于后续向NRF注册。

##### 3.1.1 配置SMSF的实例名称，配置后系统会为SMSF自动分配InstanceID信息。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nfuuid_list -%}
        ADD NFUUID:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 配置SMSF实例的Profile信息，在SMSF向NRF进行注册/更新时携带。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nfprofile_list -%}
        ADD NFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.3 配置SMSF提供的服务实例及其版本信息。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nfservice_list -%}
        ADD NFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nfservicever_list -%}
        ADD NFSERVICEVER:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        APIFULLVERSION="{{item.APIFULLVERSION}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置NRF数据。

##### 3.2.1 配置NRF信息。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nrf_list -%}
        ADD NRF:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        TLS={{item.TLS}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 配置NRF的地址信息。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in add_nrfaddr_list -%}
        ADD NRFADDR:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
        {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
            PORT={{item.PORT}},
        {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 **可选**：配置NRF协议参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

```jinja2
{%- if is_optional_nrf_protocol_params and is_scenario_nrf_deployed -%}
    {%- for item in add_nrfpara_list -%}
        ADD NRFPARA:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.WAITINTERVAL is not none -%}
            WAITINTERVAL={{item.WAITINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRETRYTIMES is not none -%}
            MAXRETRYTIMES={{item.MAXRETRYTIMES}},
        {%- endif -%}
        {%- if item.LOADCARRYINHB is not none -%}
            LOADCARRYINHB={{item.LOADCARRYINHB}},
        {%- endif -%}
        {%- if item.SUBSCRISWITCH is not none -%}
            SUBSCRISWITCH={{item.SUBSCRISWITCH}},
        {%- endif -%}
        {%- if item.OAUTH2SWITCH is not none -%}
            OAUTH2SWITCH={{item.OAUTH2SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_nrf_protocol_params and is_scenario_nrf_deployed -%}
    {%- for item in add_subcondition_list -%}
        ADD SUBCONDITION:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CONDITION is not none -%}
            CONDITION={{item.CONDITION}},
        {%- endif -%}
        {%- if item.REQNOTIFEVENT is not none -%}
            REQNOTIFEVENT={{item.REQNOTIFEVENT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.4 **可选**：当网络中规划了双主或者主备NRF时，需要配置本步骤。双主NRF场景下，NF对接的优先级高的NRF为本地DC的NRF；主备NRF场景下，NF对接的优先级高的NRF为主NRF。

```jinja2
{%- if is_optional_nrf_active_standby and is_scenario_nrf_deployed -%}
    {%- for item in add_nrf_list_1 -%}
        ADD NRF:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        TLS={{item.TLS}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_nrf_active_standby and is_scenario_nrf_deployed -%}
    {%- for item in add_nrfaddr_list_1 -%}
        ADD NRFADDR:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV4' -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE == 'IPTypeV6' -%}
            IPV6ADDRESS="{{item.IPV6ADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 端口: 条件必选(IP地址类型=NoneIP) / 条件可选(IP地址类型=IPTypeV4|IPTypeV6) --- -#}
        {%- if (item.IPADDRESSTYPE == 'NoneIP') -%}
            PORT={{item.PORT}},
        {%- elif (item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV6']) -%}
            {%- if item.PORT is not none -%}
                PORT={{item.PORT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_nrf_active_standby and is_scenario_nrf_deployed -%}
    {%- for item in add_nrfpara_list_1 -%}
        ADD NRFPARA:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.WAITINTERVAL is not none -%}
            WAITINTERVAL={{item.WAITINTERVAL}},
        {%- endif -%}
        {%- if item.MAXRETRYTIMES is not none -%}
            MAXRETRYTIMES={{item.MAXRETRYTIMES}},
        {%- endif -%}
        {%- if item.LOADCARRYINHB is not none -%}
            LOADCARRYINHB={{item.LOADCARRYINHB}},
        {%- endif -%}
        {%- if item.SUBSCRISWITCH is not none -%}
            SUBSCRISWITCH={{item.SUBSCRISWITCH}},
        {%- endif -%}
        {%- if item.OAUTH2SWITCH is not none -%}
            OAUTH2SWITCH={{item.OAUTH2SWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_nrf_active_standby and is_scenario_nrf_deployed -%}
    {%- for item in add_subcondition_list_1 -%}
        ADD SUBCONDITION:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.CONDITION is not none -%}
            CONDITION={{item.CONDITION}},
        {%- endif -%}
        {%- if item.REQNOTIFEVENT is not none -%}
            REQNOTIFEVENT={{item.REQNOTIFEVENT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.5 SMSF向NRF发起注册，激活SMSF注册状态。

```jinja2
{%- if is_scenario_nrf_deployed -%}
    {%- for item in act_nfonline_list -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置本地NRF数据（网络中未部署NRF时需要执行）

### 如果网络中无NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF，则执行本步骤，手工配置SMSF与周边NF的逻辑连接。

### 当网络中既部署了NRF，又本地配置了周边NF时，可以通过**SET NFDISCPLCY**命令配置服务发现流程的策略，默认优先选择本地配置的NF。

### 下述以配置SMSF到周边UDM、AMF为例，说明本地NRF功能的基本步骤，如有其他NF对接需要，请参考进行配置。

#### 4.1 配置SMSF到UDM的数据，包括UDM的Profile、Service、SUPI和PLMN信息。

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfprofile_list -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.IPADDRESSTYPE is not none -%}
            IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {%- endif -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS2 is not none -%}
                IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS3 is not none -%}
                IPV4ADDRESS3="{{item.IPV4ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS4 is not none -%}
                IPV4ADDRESS4="{{item.IPV4ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS2 is not none -%}
                IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS3 is not none -%}
                IPV6ADDRESS3="{{item.IPV6ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS4 is not none -%}
                IPV6ADDRESS4="{{item.IPV6ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
        {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
            {%- if item.SCHEME is not none -%}
                SCHEME={{item.SCHEME}},
            {%- endif -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfservice_list -%}
        ADD PNFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        SCHEMA={{item.SCHEMA}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfsupi_list -%}
        ADD PNFSUPI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfplmn_list -%}
        ADD PNFPLMN:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置SMSF到AMF的数据，包括AMF的Profile、Service、SUPI和PLMN信息。

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfprofile_list_1 -%}
        ADD PNFPROFILE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSTATUS is not none -%}
            NFSTATUS={{item.NFSTATUS}},
        {%- endif -%}
        {%- if item.IPADDRESSTYPE is not none -%}
            IPADDRESSTYPE={{item.IPADDRESSTYPE}},
        {%- endif -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件必选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时必选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS2 is not none -%}
                IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS3 is not none -%}
                IPV4ADDRESS3="{{item.IPV4ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
            {%- if item.IPV4ADDRESS4 is not none -%}
                IPV4ADDRESS4="{{item.IPV4ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS2 is not none -%}
                IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS3 is not none -%}
                IPV6ADDRESS3="{{item.IPV6ADDRESS3}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPADDRESSTYPE=IPTypeV6/IPTypeV4V6 时可选 --- -#}
        {%- if item.IPADDRESSTYPE in ['IPTypeV6', 'IPTypeV4V6'] -%}
            {%- if item.IPV6ADDRESS4 is not none -%}
                IPV6ADDRESS4="{{item.IPV6ADDRESS4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NFTYPE=NfSEPP/NfSCP 时可选 --- -#}
        {%- if item.NFTYPE in ['NfSEPP', 'NfSCP'] -%}
            {%- if item.SCHEME is not none -%}
                SCHEME={{item.SCHEME}},
            {%- endif -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfservice_list_2 -%}
        ADD PNFSERVICE:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SRVINSTANCEID="{{item.SRVINSTANCEID}}",
        SERVICENAME={{item.SERVICENAME}},
        SCHEMA={{item.SCHEMA}},
        {#- --- 可选参数 --- -#}
        {%- if item.NFSERVICESTATUS is not none -%}
            NFSERVICESTATUS={{item.NFSERVICESTATUS}},
        {%- endif -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfsupi_list_1 -%}
        ADD PNFSUPI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfplmn_list_1 -%}
        ADD PNFPLMN:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置SMSF到SMSC的数据

#### 5.1 增加SMSF业务接口IP地址，用于和SMSC的对接。

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
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 配置M3UA信令数据。

##### 5.2.1 增加M3UA本地实体，信令点编码所在的网络为国内网，本地实体为ASP。

```jinja2
{%- for item in add_m3le_list -%}
    ADD M3LE:
    {#- --- 必选参数 --- -#}
    LEX={{item.LEX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    LET={{item.LET}},
    {#- --- 可选参数 --- -#}
    {%- if item.LEN is not none -%}
        LEN="{{item.LEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.2.2 配置M3UA目的信令点。

```jinja2
{%- for item in add_m3de_list -%}
    ADD M3DE:
    {#- --- 必选参数 --- -#}
    DEX={{item.DEX}},
    LEX={{item.LEX}},
    DPC="{{item.DPC}}",
    DET={{item.DET}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSSM is not none -%}
        SLSSM={{item.SLSSM}},
    {%- endif -%}
    {%- if item.STPF is not none -%}
        STPF={{item.STPF}},
    {%- endif -%}
    {%- if item.ADJF is not none -%}
        ADJF={{item.ADJF}},
    {%- endif -%}
    {%- if item.NMD is not none -%}
        NMD={{item.NMD}},
    {%- endif -%}
    {%- if item.PVER is not none -%}
        PVER={{item.PVER}},
    {%- endif -%}
    {%- if item.DEN is not none -%}
        DEN="{{item.DEN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.2.3 配置到SMSC的M3UA信令链路集。

```jinja2
{%- for item in add_m3lks_list -%}
    ADD M3LKS:
    {#- --- 必选参数 --- -#}
    LSX={{item.LSX}},
    DEX={{item.DEX}},
    WM={{item.WM}},
    {#- --- 可选参数 --- -#}
    {%- if item.SLSM is not none -%}
        SLSM={{item.SLSM}},
    {%- endif -%}
    {%- if item.TM is not none -%}
        TM={{item.TM}},
    {%- endif -%}
    {%- if item.LSN is not none -%}
        LSN="{{item.LSN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.2.4 配置M3UA信令路由。

```jinja2
{%- for item in add_m3rt_list -%}
    ADD M3RT:
    {#- --- 必选参数 --- -#}
    RTX={{item.RTX}},
    DEX={{item.DEX}},
    LSX={{item.LSX}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.RTN is not none -%}
        RTN="{{item.RTN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.2.5 配置SCTP协议参数。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.SCTPPARANAME is not none -%}
        SCTPPARANAME="{{item.SCTPPARANAME}}",
    {%- endif -%}
    {%- if item.PKGERRFAULT is not none -%}
        PKGERRFAULT={{item.PKGERRFAULT}},
    {%- endif -%}
    {%- if item.PKGERRRECOVER is not none -%}
        PKGERRRECOVER={{item.PKGERRRECOVER}},
    {%- endif -%}
    {%- if item.MINRECVPKGNUM is not none -%}
        MINRECVPKGNUM={{item.MINRECVPKGNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.2.6 配置M3UA信令链路。

```jinja2
{%- for item in add_m3lnk_list -%}
    ADD M3LNK:
    {#- --- 必选参数 --- -#}
    LNK={{item.LNK}},
    CS={{item.CS}},
    LSX={{item.LSX}},
    SCTPINDX={{item.SCTPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {%- if item.LOCPORT is not none -%}
        LOCPORT={{item.LOCPORT}},
    {%- endif -%}
    {%- if item.PEERPORT is not none -%}
        PEERPORT={{item.PEERPORT}},
    {%- endif -%}
    {%- if item.ASF is not none -%}
        ASF={{item.ASF}},
    {%- endif -%}
    {%- if item.PRI is not none -%}
        PRI={{item.PRI}},
    {%- endif -%}
    {%- if item.CONSTHD is not none -%}
        CONSTHD={{item.CONSTHD}},
    {%- endif -%}
    {%- if item.CONETHD is not none -%}
        CONETHD={{item.CONETHD}},
    {%- endif -%}
    {%- if item.CROSSIP is not none -%}
        CROSSIP={{item.CROSSIP}},
    {%- endif -%}
    {%- if item.EXCHGMODE is not none -%}
        EXCHGMODE={{item.EXCHGMODE}},
    {%- endif -%}
    {%- if item.LKN is not none -%}
        LKN="{{item.LKN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        LOCIPV41="{{item.LOCIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        PEERIPV41="{{item.PEERIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        LOCIPV61="{{item.LOCIPV61}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        PEERIPV61="{{item.PEERIPV61}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.LOCIPV42 is not none -%}
            LOCIPV42="{{item.LOCIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV4 时可选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        {%- if item.PEERIPV42 is not none -%}
            PEERIPV42="{{item.PEERIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.LOCIPV62 is not none -%}
            LOCIPV62="{{item.LOCIPV62}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPT=IPV6 时可选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        {%- if item.PEERIPV62 is not none -%}
            PEERIPV62="{{item.PEERIPV62}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 配置SCCP信令数据

##### 5.3.1 配置SCCP本局信令点（适用于2/3G短消息）。

```jinja2
{%- for item in add_sccpopc_list -%}
    ADD SCCPOPC:
    {#- --- 必选参数 --- -#}
    OPX={{item.OPX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.OPN is not none -%}
        OPN="{{item.OPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SPN=COREONLY/IUANDCORE 时必选 --- -#}
    {%- if item.SPN in ['COREONLY', 'IUANDCORE'] -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sccpdpc_list -%}
    ADD SCCPDPC:
    {#- --- 必选参数 --- -#}
    DPX={{item.DPX}},
    OPX={{item.OPX}},
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SS7T is not none -%}
        SS7T={{item.SS7T}},
    {%- endif -%}
    {%- if item.LDP is not none -%}
        LDP={{item.LDP}},
    {%- endif -%}
    {%- if item.DPN is not none -%}
        DPN="{{item.DPN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LDP=BACKUP 时必选 --- -#}
    {%- if item.LDP == 'BACKUP' -%}
        BDPX={{item.BDPX}},
    {%- endif -%}
    {#- --- 条件必选：LDP=LOADSHARE 时必选 --- -#}
    {%- if item.LDP == 'LOADSHARE' -%}
        SDPX={{item.SDPX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.3.2 配置SCCP本局信令点（适用于5G短消息）。

```jinja2
{%- for item in add_smsfopc_list -%}
    ADD SMSFOPC:
    {#- --- 必选参数 --- -#}
    OPX={{item.OPX}},
    NI={{item.NI}},
    OPC="{{item.OPC}}",
    SMSFN="{{item.SMSFN}}",
    MASTER={{item.MASTER}},
    {#- --- 可选参数 --- -#}
    {%- if item.OPN is not none -%}
        OPN="{{item.OPN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 5.3.3 配置SCCP本局子系统。

```jinja2
{%- for item in add_sccpssn_list -%}
    ADD SCCPSSN:
    {#- --- 必选参数 --- -#}
    SSNX={{item.SSNX}},
    SSN={{item.SSN}},
    NI={{item.NI}},
    DPC="{{item.DPC}}",
    OPC="{{item.OPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SSNNAME is not none -%}
        SSNNAME="{{item.SSNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.4 配置GT翻译数据。

```jinja2
{%- for item in add_sccpgt_list -%}
    ADD SCCPGT:
    {#- --- 必选参数 --- -#}
    GTX={{item.GTX}},
    NI={{item.NI}},
    RT={{item.RT}},
    ADDR="{{item.ADDR}}",
    DPC="{{item.DPC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GTEXP is not none -%}
        GTEXP={{item.GTEXP}},
    {%- endif -%}
    {%- if item.NAME is not none -%}
        NAME="{{item.NAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RT=DPCNEWGT 时必选 --- -#}
    {%- if item.RT == 'DPCNEWGT' -%}
        NGTX={{item.NGTX}},
    {%- endif -%}
    {#- --- 条件必选：RT=DPCSSN 时必选 --- -#}
    {%- if item.RT == 'DPCSSN' -%}
        SSN={{item.SSN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.NP is not none -%}
            NP={{item.NP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=FOUR 时可选 --- -#}
    {%- if item.GTEXP == 'FOUR' -%}
        {%- if item.ADDREXP is not none -%}
            ADDREXP={{item.ADDREXP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：GTEXP=SIX 时可选 --- -#}
    {%- if item.GTEXP == 'SIX' -%}
        {%- if item.TT is not none -%}
            TT={{item.TT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

