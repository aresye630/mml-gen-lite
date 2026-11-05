---
id: ''
name: AMF典型配置实例
ne_type: UNC
type: feature
description: 本任务实例实现以下场景配置：  UNC（作为AMF）与周边NF（本例中包含SMF、NRF、NSSF、MME、gNodeB）通过OSPF动态路由绑定动态BFD实现网络互通。  * 网络形态：5G网络 * 网元形态：AMF * 路由协议：OSPF动态路由 * 组网IP格式：IPv4组网 * 接入用户：IPv4单栈用户
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","典型配置实例","AMF典型配置实例"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST AUTOCONFIG')
- getParameterValue('DSP OPSASSISTSTATE')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本任务实例实现以下场景配置：UNC（作为AMF）与周边NF（本例中包含SMF、NRF、NSSF、MME、gNodeB）通过OSPF动态路由绑定动态BFD实现网络互通。* 网络形态：5G网络* 网元形态：AMF* 路由协议：OSPF动态路由* 组网IP格式：IPv4组网* 接入用户：IPv4单栈用户

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
    add_ngmno_list:
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
    add_amfinfo_list:
      type: items
      properties:
        AMFINSTANCENAME:
          name: 'AMF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFNAME:
          name: 'AMF名称'
          type: string
          minLength: 0
          maxLength: 150
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPACITY:
          name: '相对容量'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
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
    add_guami_list:
      type: items
      properties:
        INDEX:
          name: 'GUAMI索引'
          type: integer
          minimum: 0
          maximum: 255
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
        AMFREGIONID:
          name: 'AMF区域标识'
          type: string
          minLength: 2
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFSETID:
          name: 'AMF集合标识'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFPOINTER:
          name: 'AMF指示符'
          type: string
          minLength: 2
          maxLength: 2
          required: true
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
        CHKSUMTX:
          name: '发送消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        CHKSUMRX:
          name: '接收消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
    add_sctplegrp_list:
      type: items
      properties:
        SCTPGROUPID:
          name: 'SCTP 本端实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sctple_list:
      type: items
      properties:
        SCTPLEIDX:
          name: 'SCTP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本端实体组索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV42:
          name: '本地IPv4地址2'
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
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 38412
        SCTPPARAIDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV61:
          name: '本地IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCALIPV62:
          name: '本地IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngappara_list:
      type: items
      properties:
        NGAPPARAIDX:
          name: 'NGAP协议参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMFCFGUPTTMR:
          name: 'AMF Configuration Update消息超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        AMFCFGUPTCNT:
          name: 'AMF Configuration Update消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        RESETTMR:
          name: 'Reset超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 20
        RESETCNT:
          name: 'Reset消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        TIMETOWAITFLG:
          name: '等待时间指示器'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: No
        TIMETOWAITTMR:
          name: '重发NG SETUP REQUEST时长 (s)'
          type: string
          enum:
          - One
          - Two
          - Five
          - Ten
          - Twenty
          - Sixty
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Sixty
    add_ngaple_list:
      type: items
      properties:
        NGAPLEIDX:
          name: 'NGAP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本端实体组索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NGAPPARAIDX:
          name: 'NGAP参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
    set_ngdns_list:
      type: items
      properties:
        ANALYSETYPE:
          name: 'DNS解析方式'
          type: string
          enum:
          - HOSTFILE_SERVER
          - SERVER_HOSTFILE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '服务器组ID'
          type: integer
          minimum: 0
          maximum: 37
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPPLCY:
          name: 'N26接口本网IP地址选择策略'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV6PRE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMESWITCH:
          name: '优选融合MME开关'
          type: string
          enum:
          - MME_ON
          - MME_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngdnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - MME
          - NG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - N26
          - SBI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_2:
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
    add_gtpclegrp_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_gtpclegrpmem_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
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
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPN:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcintf_list:
      type: items
      properties:
        INTFTYPE:
          name: '接口类型'
          type: string
          enum:
          - E_GTPCINTF_ITFS11
          - E_GTPCINTF_ITFN26
          - E_GTPCINTF_ITFS5_S
          - E_GTPCINTF_ITFS8_S
          - S5_P_OR_GN
          - S8_P_OR_GP
          - PROXY_SGSN_GP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
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
    set_ngmmpara_list:
      type: items
      properties:
        T3522:
          name: 'T3522(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3522:
          name: 'N3522(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3550:
          name: 'T3550(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3550:
          name: 'N3550(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3560:
          name: 'T3560(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3560:
          name: 'N3560(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3570:
          name: 'T3570(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3570:
          name: 'N3570(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3512:
          name: 'T3512(min)'
          type: integer
          minimum: 1
          maximum: 310
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3502:
          name: 'T3502(min)'
          type: integer
          minimum: 1
          maximum: 186
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3513:
          name: 'T3513(s)'
          type: integer
          minimum: 3
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3513:
          name: 'N3513(times)'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGINGDELTA:
          name: '重寻呼间隔递增值(s)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPT3513:
          name: '高优先级业务的T3513(s)'
          type: integer
          minimum: 2
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPN3513:
          name: '高优先级业务的N3513(times)'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPPAGINGDELTA:
          name: '高优先级业务的重寻呼间隔递增值(s)'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCHTMR:
          name: '移动可达定时器(min)'
          type: integer
          minimum: 2
          maximum: 322
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMDTCHTMR:
          name: '不可达用户隐式去注册定时器(min)'
          type: integer
          minimum: 0
          maximum: 322
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTITMR:
          name: 'GUTI重分配定时器(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTIREALLOC:
          name: 'GUTI重分配'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOPRETMR:
          name: 'Handover准备定时器(s)'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPSRCTMR:
          name: '源侧Handover完成定时器(s)'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOCMPTGTTMR:
          name: '目标侧Handover完成定时器(s)'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3:
          name: 'T3定时器(s)'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTITMRFORDEBUG:
          name: '测试用GUTI重分配定时器(m)'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOT3:
          name: '切换流程资源释放定时器(s)'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GUTIREALLOCTMR:
          name: 'GUTI重分配最大间隔(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngtalst_list:
      type: items
      properties:
        TALISTID:
          name: '跟踪区列表标识'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAI:
          name: '跟踪区标识'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ngmmfunc_list:
      type: items
      properties:
        RESELTYPE:
          name: 'AMF重选方式'
          type: string
          enum:
          - RE_ROUTE
          - RE_DIRECT
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
    add_ngmno_list:
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
    add_plmnns_list:
    - NSIDX: 0
      PLMNIDX: 0
      SST: 1
      SD: '010101'
      STATE: ACTIVE
    add_nfuuid_list:
    - NFTYPE: NfAMF
      NFINSTANCENAME: 'AMF_Instance_0'
    add_nfprofile_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      NFTYPE: NfAMF
      NFSTATUS: Registered
    add_amfinfo_list:
    - AMFINSTANCENAME: 'AMF_Instance_0'
      AMFNAME: 'amf1.cluster1.net2.amf.5gc.mnc003.mcc123.3gppnetwork.org'
      CAPACITY: 255
    add_nfservice_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NamfComm
    add_nfservicever_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    add_guami_list:
    - INDEX: 0
      PLMNIDX: 0
      AMFREGIONID: '00'
      AMFSETID: '001'
      AMFPOINTER: '01'
    add_nfns_list:
    - NFTYPE: NfAMF
      NSIDX: 0
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.1.4'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 1
      DESC: 'AMF'
    add_httple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.1.4'
      PORT: 8080
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'AMF Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      NFTYPE: NFTypeAMF
      DESCRIPTION: 'AMF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: FALSE
      PRIORITY: 0
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
    add_subcondition_list:
    - NFTYPE: NfSMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '172.16.2.5'
      VPNINSTNAME: 'VRF_Access'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_sctppara_list:
    - SCTPPARAINDEX: 0
      CHKSUMTX: YES
      CHKSUMRX: NO
    add_sctplegrp_list:
    - SCTPGROUPID: 1
    add_sctple_list:
    - SCTPLEIDX: 0
      SCTPGROUPID: 1
      IPVERSION: IPV4
      LOCALIPV41: '172.16.2.5'
      LOCALIPV42: '172.16.2.6'
      PORT: 38412
      SCTPPARAIDX: 0
      LOCALIPV61: ''
      LOCALIPV62: ''
    add_ngappara_list:
    - NGAPPARAIDX: 1
      AMFCFGUPTTMR: 20
      AMFCFGUPTCNT: 3
      RESETTMR: 20
      RESETCNT: 3
      TIMETOWAITFLG: Yes
      TIMETOWAITTMR: Sixty
    add_ngaple_list:
    - NGAPLEIDX: 1
      SCTPGROUPID: 1
      NGAPPARAIDX: 1
    set_ngdns_list:
    - ANALYSETYPE: HOSTFILE_SERVER
      GRPID: 7
      IPPLCY: IPV4
      MMESWITCH: MME_OFF
    add_ngipv4dnsh_list:
    - HSINDEX: 10
      HOSTNAME: 'topon.mme-s10.MMEC12.MMEGI8001.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.2.3.4'
    add_ngdnsn_list:
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC003.MCC460.3GPPNETWORK.ORG'
      HSINDEX: 10
      ENTITY: MME
      INTYPE: N26
    add_logicip_list_2:
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.154.24'
      VPNINSTNAME: '_public_'
      DESC: 'FOR N26'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_gtpclegrp_list:
    - GROUPID: 3
      DESC: 'N26'
    add_gtpclegrpmem_list:
    - GROUPID: 3
      IPTYPE: IPv4
      IPV4ADDR: '10.2.154.24'
      VPN: 'VRF_MME'
      DESC: 'n26'
      IPV6ADDR: ''
    add_gtpcintf_list:
    - INTFTYPE: E_GTPCINTF_ITFN26
      GROUPID: 3
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2NRLSAM01'
      SWITCH: ENABLE
    set_ngmmpara_list:
    - T3522: 6
      N3522: 4
      T3550: 6
      N3550: 4
      T3560: 6
      N3560: 4
      T3570: 6
      N3570: 4
      T3512: 54
      T3502: 12
      T3513: 6
      N3513: 2
      PAGINGDELTA: 0
      HPT3513: 2
      HPN3513: 4
      HPPAGINGDELTA: 0
      RCHTMR: 58
      IMDTCHTMR: 60
      GUTITMR: 0
      GUTIREALLOC: INIT_REG
      HOPRETMR: 10
      HOCMPSRCTMR: 10
      HOCMPTGTTMR: 10
      T3: 10
      GUTITMRFORDEBUG: 0
      HOT3: 2
      GUTIREALLOCTMR: 0
    add_ngtalst_list:
    - TALISTID: 1
      TAI: '12301000101'
    set_ngmmfunc_list:
    - RESELTYPE: RE_DIRECT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 关闭自动配置开关。

#### 2.1 查询自动配置开关状态。

#### 如果自动配置开关值为“TRUE”，需要执行如下步骤关闭自动配置开关。

#### 2.2 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

#### 2.3 关闭自动配置开关。

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

### 3 全局激活BFD。

```jinja2
{%- for item in set_bfd_list -%}
    SET BFD:
    {#- --- 必选参数 --- -#}
    BFDENABLE={{item.BFDENABLE}},
    ;
{%- endfor -%}
```

### 4 配置UNC与对端SMF、NRF、NSSF的IP路由数据。

#### 4.1 配置外联口的VPN实例。

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

#### 4.2 配置OSPF路由。

##### 4.2.1 创建OSPF进程。

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

##### 4.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

##### 如果参数“AREATYPE（区域类型）”配置为“NSSA”时，需要配置Loopback地址，这样设备会自动选取该Loopback地址作为FA。当有其他设备存在多条开销值相同的路径到NSSA设备时，可以形成负载分担。

##### 4.2.3 设置OSPF引入路由类型。

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

#### 4.3 配置外联口自动部署模板。

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

### 5 配置UNC与对端MME的IP路由数据。

#### 5.1 配置VPN实例。

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

#### 5.2 配置OSPF路由。

##### 5.2.1 创建OSPF进程。

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

##### 5.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_1 -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

##### 5.2.3 设置OSPF引入路由类型。

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

#### 5.3 配置外联口自动部署模板。

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

### 6 配置UNC与对端gNodeB的IP路由数据。

#### 6.1 配置VPN实例。

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

#### 6.2 配置OSPF路由。

##### 6.2.1 创建OSPF进程。

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

##### 6.2.2 增加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list_2 -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

##### 6.2.3 设置OSPF引入路由类型。

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

#### 6.3 配置外联口自动部署模板。

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

### 7 打开IP路由自动配置开关。

```jinja2
{%- set DSP_OPSASSISTSTATE=getParameterValue('DSP OPSASSISTSTATE') -%}
{%- if DSP_OPSASSISTSTATE=='Ready' -%}
    {%- for item in set_autoconfig_list_1 -%}
        SET AUTOCONFIG:
        {#- --- 必选参数 --- -#}
        SWITCHFLAG={{item.SWITCHFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行****DSP OPSASSISTSTATE****命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

### 8 配置运营商基础数据。

#### 8.1 配置运营商信息。当前UNC中默认配置一条“NOID”为0的默认记录，不需单独配置。

```jinja2
{%- for item in add_ngmno_list -%}
    ADD NGMNO:
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

#### 8.2 配置运营商签约用户的Home PLMN。

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

#### 8.3 配置运营商的Serving PLMN。

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

#### 8.4 配置运营商支持的网络切片。

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
    {%- if item.STATE is not none -%}
        STATE={{item.STATE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置AMF实例信息。

#### 9.1 配置AMF实例的名称。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 9.2 配置AMF实例的Profile信息。

```jinja2
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
```

#### 9.3 配置AMF的域名等信息。

```jinja2
{%- for item in add_amfinfo_list -%}
    ADD AMFINFO:
    {#- --- 必选参数 --- -#}
    AMFINSTANCENAME="{{item.AMFINSTANCENAME}}",
    AMFNAME="{{item.AMFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CAPACITY is not none -%}
        CAPACITY={{item.CAPACITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.4 配置AMF提供的服务实例及其版本信息。

```jinja2
{%- for item in add_nfservice_list -%}
    ADD NFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nfservicever_list -%}
    ADD NFSERVICEVER:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    APIFULLVERSION="{{item.APIFULLVERSION}}",
    ;
{%- endfor -%}
```

#### 9.5 配置全局AMF标识（GUAMI）和AMF支持的切片信息。

```jinja2
{%- for item in add_guami_list -%}
    ADD GUAMI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    PLMNIDX={{item.PLMNIDX}},
    AMFREGIONID="{{item.AMFREGIONID}}",
    AMFSETID="{{item.AMFSETID}}",
    AMFPOINTER="{{item.AMFPOINTER}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nfns_list -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

### 10 配置AMF服务化接口数据。

#### 10.1 增加AMF服务化接口的IP地址。

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

#### 10.2 配置Namf接口的HTTP信息。

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

### 11 配置AMF到NRF的数据。

#### 11.1 配置NRF信息。

```jinja2
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
```

#### 11.2 配置NRF的地址信息。

```jinja2
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
```

#### 11.3 配置NRF协议参数。

```jinja2
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
```

```jinja2
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
```

#### 11.4 打开NF注册、认证、发现等与NRF交互的基本功能开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 11.5 激活AMF向NRF注册。

```jinja2
{%- for item in act_nfonline_list -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

### 12 配置AMF到NG-RAN（N2接口）的数据。

#### 12.1 配置N2接口业务IP地址。

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

#### 12.2 配置SCTP协议参数及SCTP本端实体。

```jinja2
{%- for item in add_sctppara_list -%}
    ADD SCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.CHKSUMTX is not none -%}
        CHKSUMTX={{item.CHKSUMTX}},
    {%- endif -%}
    {%- if item.CHKSUMRX is not none -%}
        CHKSUMRX={{item.CHKSUMRX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctplegrp_list -%}
    ADD SCTPLEGRP:
    {#- --- 必选参数 --- -#}
    SCTPGROUPID={{item.SCTPGROUPID}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctple_list -%}
    ADD SCTPLE:
    {#- --- 必选参数 --- -#}
    SCTPLEIDX={{item.SCTPLEIDX}},
    SCTPGROUPID={{item.SCTPGROUPID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.SCTPPARAIDX is not none -%}
        SCTPPARAIDX={{item.SCTPPARAIDX}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LOCALIPV41="{{item.LOCALIPV41}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        LOCALIPV61="{{item.LOCALIPV61}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.LOCALIPV42 is not none -%}
            LOCALIPV42="{{item.LOCALIPV42}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.LOCALIPV62 is not none -%}
            LOCALIPV62="{{item.LOCALIPV62}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 12.3 配置NGAP本端地址及本端实体。

```jinja2
{%- for item in add_ngappara_list -%}
    ADD NGAPPARA:
    {#- --- 必选参数 --- -#}
    NGAPPARAIDX={{item.NGAPPARAIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.AMFCFGUPTTMR is not none -%}
        AMFCFGUPTTMR={{item.AMFCFGUPTTMR}},
    {%- endif -%}
    {%- if item.AMFCFGUPTCNT is not none -%}
        AMFCFGUPTCNT={{item.AMFCFGUPTCNT}},
    {%- endif -%}
    {%- if item.RESETTMR is not none -%}
        RESETTMR={{item.RESETTMR}},
    {%- endif -%}
    {%- if item.RESETCNT is not none -%}
        RESETCNT={{item.RESETCNT}},
    {%- endif -%}
    {%- if item.TIMETOWAITFLG is not none -%}
        TIMETOWAITFLG={{item.TIMETOWAITFLG}},
    {%- endif -%}
    {%- if item.TIMETOWAITTMR is not none -%}
        TIMETOWAITTMR={{item.TIMETOWAITTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngaple_list -%}
    ADD NGAPLE:
    {#- --- 必选参数 --- -#}
    NGAPLEIDX={{item.NGAPLEIDX}},
    SCTPGROUPID={{item.SCTPGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.NGAPPARAIDX is not none -%}
        NGAPPARAIDX={{item.NGAPPARAIDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 配置DNS数据，查询对端MME。

#### 13.1 配置DNS运行参数。

```jinja2
{%- for item in set_ngdns_list -%}
    SET NGDNS:
    {#- --- 可选参数 --- -#}
    {%- if item.ANALYSETYPE is not none -%}
        ANALYSETYPE={{item.ANALYSETYPE}},
    {%- endif -%}
    {%- if item.GRPID is not none -%}
        GRPID={{item.GRPID}},
    {%- endif -%}
    {%- if item.IPPLCY is not none -%}
        IPPLCY={{item.IPPLCY}},
    {%- endif -%}
    {%- if item.MMESWITCH is not none -%}
        MMESWITCH={{item.MMESWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 13.2 **可选：**如果不存在DNS Server，UNC自身提供了DNS Client功能，AMF可直接向UNC的DNS Client微服务查询MME。

```jinja2
{%- if is_optional_config_dns_query_mme -%}
    {%- for item in add_ngipv4dnsh_list -%}
        ADD NGIPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_config_dns_query_mme -%}
    {%- for item in add_ngdnsn_list -%}
        ADD NGDNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 14 配置到MME（N26接口）的数据。

#### 14.1 配置N26接口信息。

```jinja2
{%- for item in add_logicip_list_2 -%}
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

```jinja2
{%- for item in add_gtpclegrp_list -%}
    ADD GTPCLEGRP:
    {#- --- 必选参数 --- -#}
    GROUPID={{item.GROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gtpclegrpmem_list -%}
    ADD GTPCLEGRPMEM:
    {#- --- 必选参数 --- -#}
    GROUPID={{item.GROUPID}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPN is not none -%}
        VPN="{{item.VPN}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gtpcintf_list -%}
    ADD GTPCINTF:
    {#- --- 必选参数 --- -#}
    INTFTYPE={{item.INTFTYPE}},
    GROUPID={{item.GROUPID}},
    ;
{%- endfor -%}
```

#### 14.2 配置支持UE在LTE与5G SA网络间互操作。

```jinja2
{%- for item in set_licenseswitch_list_3 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 15 配置移动性管理数据。

#### 15.1 配置NG移动性管理相关的定时器参数。

```jinja2
{%- for item in set_ngmmpara_list -%}
    SET NGMMPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.T3522 is not none -%}
        T3522={{item.T3522}},
    {%- endif -%}
    {%- if item.N3522 is not none -%}
        N3522={{item.N3522}},
    {%- endif -%}
    {%- if item.T3550 is not none -%}
        T3550={{item.T3550}},
    {%- endif -%}
    {%- if item.N3550 is not none -%}
        N3550={{item.N3550}},
    {%- endif -%}
    {%- if item.T3560 is not none -%}
        T3560={{item.T3560}},
    {%- endif -%}
    {%- if item.N3560 is not none -%}
        N3560={{item.N3560}},
    {%- endif -%}
    {%- if item.T3570 is not none -%}
        T3570={{item.T3570}},
    {%- endif -%}
    {%- if item.N3570 is not none -%}
        N3570={{item.N3570}},
    {%- endif -%}
    {%- if item.T3512 is not none -%}
        T3512={{item.T3512}},
    {%- endif -%}
    {%- if item.T3502 is not none -%}
        T3502={{item.T3502}},
    {%- endif -%}
    {%- if item.T3513 is not none -%}
        T3513={{item.T3513}},
    {%- endif -%}
    {%- if item.N3513 is not none -%}
        N3513={{item.N3513}},
    {%- endif -%}
    {%- if item.PAGINGDELTA is not none -%}
        PAGINGDELTA={{item.PAGINGDELTA}},
    {%- endif -%}
    {%- if item.HPT3513 is not none -%}
        HPT3513={{item.HPT3513}},
    {%- endif -%}
    {%- if item.HPN3513 is not none -%}
        HPN3513={{item.HPN3513}},
    {%- endif -%}
    {%- if item.HPPAGINGDELTA is not none -%}
        HPPAGINGDELTA={{item.HPPAGINGDELTA}},
    {%- endif -%}
    {%- if item.RCHTMR is not none -%}
        RCHTMR={{item.RCHTMR}},
    {%- endif -%}
    {%- if item.IMDTCHTMR is not none -%}
        IMDTCHTMR={{item.IMDTCHTMR}},
    {%- endif -%}
    {%- if item.GUTITMR is not none -%}
        GUTITMR={{item.GUTITMR}},
    {%- endif -%}
    {%- if item.GUTIREALLOC is not none -%}
        GUTIREALLOC={{item.GUTIREALLOC}},
    {%- endif -%}
    {%- if item.HOPRETMR is not none -%}
        HOPRETMR={{item.HOPRETMR}},
    {%- endif -%}
    {%- if item.HOCMPSRCTMR is not none -%}
        HOCMPSRCTMR={{item.HOCMPSRCTMR}},
    {%- endif -%}
    {%- if item.HOCMPTGTTMR is not none -%}
        HOCMPTGTTMR={{item.HOCMPTGTTMR}},
    {%- endif -%}
    {%- if item.T3 is not none -%}
        T3={{item.T3}},
    {%- endif -%}
    {%- if item.GUTITMRFORDEBUG is not none -%}
        GUTITMRFORDEBUG={{item.GUTITMRFORDEBUG}},
    {%- endif -%}
    {%- if item.HOT3 is not none -%}
        HOT3={{item.HOT3}},
    {%- endif -%}
    {%- if item.GUTIREALLOCTMR is not none -%}
        GUTIREALLOCTMR={{item.GUTIREALLOCTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 15.2 增加跟踪区列表。

```jinja2
{%- for item in add_ngtalst_list -%}
    ADD NGTALST:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    TAI="{{item.TAI}}",
    ;
{%- endfor -%}
```

#### 15.3 配置AMF重选方式为重定向。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.RESELTYPE is not none -%}
        RESELTYPE={{item.RESELTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

