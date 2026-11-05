---
id: ''
name: 配置5G LAN基本功能
ne_type: UEG
type: feature
description: 同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信/IP通信时，需要配置5G LAN功能。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","基本功能","配置5G LAN基本功能"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST UPETHSRVPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
同一5G LAN终端组成员之间或5G LAN终端组的成员和数据网络中的应用之间进行以太通信/IP通信时，需要配置5G LAN功能。

## 必备事项
前提条件

* 请仔细阅读GWFD-030701 支持5G LAN组以太通信特性概述和GWFD-030702 支持网络侧基于VxLAN的以太通信特性概述。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
* UEG已完成与周边网元的对接。
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
    add_ngvninstance_list:
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
          default: ETHERNET
        MACIDLESW:
          name: 'N3学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'UPF开启从N3侧学习到的MAC地址老化功能时需要设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MULTIFLOODSW:
          name: '组播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '对于未匹配到组播组的组播消息，需要UPF泛洪转发时，设置为“ENABLE”，否则设置为“DISABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        MULTIFLOODRATE:
          name: '组播泛洪速率'
          type: integer
          minimum: 1
          maximum: 200
          required: false
          description: '“MULTIFLOODSW”设置为“ENABLE”时需要规划。用于控制每秒组播报文泛洪转发的报文数。'
          data_source: '本端规划'
          pattern: ''
          default: 50
        BCASTFLOWCTRLSW:
          name: '广播流控开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置是否对广播报文进行流控。“BCASTFLOWCTRLSW”设置为“ENABLE”时，流控周期（1s）内上行广播报文数+下行广播报文数大于“BCASTDATARATE”参数值时进行流控，该流控周期内后续再收到的上下行广播报文均做丢弃处理。  此处以开启流控为例，请以局点规划为准。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        UNICASTFLOODSW:
          name: '单播泛洪开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数设置为“DISABLE”时，层二终端必须先发送过上行报文，才能正常接收下行单播报文。  推荐设置为“DISABLE”。  该参数仅用于控制N3侧未知单播是否进行泛洪处理。不控制到VTEP的未知单播泛洪处理。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        N6MACIDLESW:
          name: 'N6学习的MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'UPF开启从VxLAN隧道学习到的MAC地址老化功能时需要设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MACIDLETIME:
          name: 'N3侧MAC地址空闲时长'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: '“MACIDLESW”设置为“ENABLE”时需要规划。  对应MAC地址的用户，空闲最大时长。超时后将删除该MAC地址。'
          data_source: '本端规划'
          pattern: ''
          default: 60
        BCASTDATARATE:
          name: '广播数据处理速率'
          type: integer
          minimum: 1
          maximum: 200
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 100
        UNIFLOODRATE:
          name: '单播泛洪速率'
          type: integer
          minimum: 1
          maximum: 200
          required: false
          description: '“UNICASTFLOODSW”设置为“ENABLE”时需要规划。用于控制每秒未知单播报文泛洪转发的报文数。'
          data_source: '本端规划'
          pattern: ''
          default: 100
        N6MACIDLETIME:
          name: 'N6学习的MAC地址空闲时长'
          type: integer
          minimum: 5
          maximum: 1440
          required: false
          description: '“N6MACIDLESW”设置为“ENABLE”时需要规划。  对应MAC地址的用户，空闲最大时长。超时后将删除该MAC地址。'
          data_source: '本端规划'
          pattern: ''
          default: 60
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。  说明：  * 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。   采用已存在的VPN实例时，不需要重复执行**ADD VPNINST**命令。 * DCGW与UPF之间建立VXLAN隧道的场景，VXLAN逻辑接口绑定的“VPNINSTANCE”为默认VPN实例“\_public\_”。   采用默认VPN实例“\_public\_”时，不需要再执行**ADD VPNINST**命令。'
          data_source: '请选中“虚拟机类型”为“ISU”/“ISU\_Cxx”且“子端口”为“group\_isu\_xxxx”的所有行，查找指定“逻辑接口”对应的“VRF”。'
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
          description: '不同接口的NAME取值不能重复。  UPF与另一UPF之间建立VXLAN隧道的场景，复用UPF与DCGW/企业侧交换机之间建立VXLAN隧道的vxlanif接口。'
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
          description: '仅支持IPv4类型的VTEP。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: '该IP用于和对端建立VXLAN隧道。   * UEG裸机容器+UEG热备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须相同。 * UEG裸机容器+UEG冷备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的vxlan逻辑接口IP地址必须不同。   UEG虚机容器+每个UEG对接一对DCGW时，两个UPF上的vxlan逻辑接口IP地址可以相同，可以不同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '采用**ADD VPNINST**命令定义的VPNINSTANCE。'
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
          description: 'VXLAN隧道组名称，网元内不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD LOGICINF**命令定义的NAME。'
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
          description: '路径中的网络设备和对端都支持心跳消息时，建议设置为“ENABLE”。路径中的网络设备或对端不支持心跳消息时，设置为“DISABLE”，否则可能影响报文正常转发。'
          data_source: '固定取值'
          pattern: ''
          default: ENABLE
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: '两次心跳检测间的时间阈值。'
          data_source: '本端规划'
          pattern: ''
          default: 6
        HEARTSUCCLIMIT:
          name: '心跳检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为up所需的心跳检测连续成功次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        HEARTFAILLIMIT:
          name: '心跳检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为down所需的心跳检测连续失败次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: '设置心跳检测的超时时长，该值需要小于“TIMETHRESHOLD”参数值。'
          data_source: '本端规划'
          pattern: ''
          default: 2
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
          description: '对端（DCGW/企业侧VXLAN交换机）的VXLAN隧道IP地址。   * UEG裸机容器+UEG热备容灾组网+两个UEG对接同一对VXLAN交换机/DCGW时，两个UPF上的VTEP IP地址必须相同。 * UEG虚机容器+每个UEG对接一对DCGW时，两个UPF上的VTEP IP地址可以相同，可以不同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        TYPE:
          name: 'VXLAN隧道对端的类型'
          type: string
          enum:
          - N6
          - N19
          required: false
          description: '与DCGW/企业侧VXLAN交换机建立VXLAN隧道时，采用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: N6
    add_vtepbindgrp_list:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VTEP绑定VXLAN隧道组。'
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
    add_ngvnbindvxlan_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD VXLANGRP**定义的GRPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: 'VXLAN隧道头中的VNI标识的值。  同一5G LAN组，UPF与VXLAN交换机两侧需要一致。  部署多个5G LAN组时，每个5G LAN组绑定的“VNI+VTEP IP”必须不同。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_nglanattr_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TOTALMACNUM:
          name: '支持的总MAC地址数'
          type: integer
          minimum:
          - 1024
          - 0
          maximum:
          - 8000
          - 0
          required: false
          description: '对于层二5G LAN，取值范围是1024~8000。  当超过设置的数量时，UPF会上报告警ALM-81247 5G LAN MAC地址超规格。  请根据5G LAN组下的实际5G LAN终端数量调整。'
          data_source: '本端规划'
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
          description: '层二5G LAN支持PING探测时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPETHSRVMAC:
          name: '用户面以太业务MAC'
          type: string
          minLength: 0
          maxLength: 17
          required: false
          description: '此处配置的是UPF发送PING报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngvnvif_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          required: false
          description: '可通过**LST NGVNINSTANCE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VIFIPTYPTE:
          name: '虚拟接口IP地址类型'
          type: string
          required: false
          description: '当前仅支持IPv4。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        VIFIPV4ADDR:
          name: '虚拟接口IPv4地址'
          type: string
          required: false
          description: '此处规划的是探测源IP，从DHCP Server获取。  与DHCP Server工程师协商，该IP地址等同于DHCP Server分配给5G LAN层二终端的IP地址，与5G LAN层二终端的IP地址在同一网段，且不能与5G LAN层二终端的IP地址冲突。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_licenseswitch_list_2:
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
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划使能Routing Behind MS功能的APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN允许手机后路由用户接入。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_cpapnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '规划使能Routing Behind MS功能的APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: '手机后路由'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN允许手机后路由用户接入。'
          data_source: '固定取值'
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
    add_rule_list_1:
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
    add_userprofile_list_1:
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LANB01'
      SWITCH: ENABLE
    set_nglanfunc_list:
    - NGLANSW: ENABLE
    add_ngvninstance_list:
    - VNINSTANCE: '000003e9-460-08-01'
      PDNTYPE: ETHERNET
      MACIDLESW: DISABLE
      MULTIFLOODSW: ENABLE
      MULTIFLOODRATE: 20
      BCASTFLOWCTRLSW: ENABLE
      UNICASTFLOODSW: DISABLE
      N6MACIDLESW: DISABLE
      MACIDLETIME: 60
      BCASTDATARATE: 100
      UNIFLOODRATE: 100
      N6MACIDLETIME: 60
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_vxlan'
    add_logicinf_list:
    - NAME: 'vxlanif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.50.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_vxlan'
    add_vxlangrp_list:
    - GRPNAME: 'vxlan_01'
      SRCINTF: 'vxlanif1/1/0'
      HEARTBEAT: ENABLE
      TIMETHRESHOLD: 6
      HEARTSUCCLIMIT: 3
      HEARTFAILLIMIT: 3
      TIMEOUT: 2
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
      TYPE: N6
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP1'
      PRIFLAG: PRIMARY
    add_ngvnbindvxlan_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VXLANGRPNAME: 'vxlan_01'
      VNI: 5010
    set_nglanattr_list:
    - VNINSTANCE: '000003e9-460-08-01'
      TOTALMACNUM: 6000
    set_upethsrvpara_list:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    add_ngvnvif_list:
    - VNINSTANCE: 000003e9-460-08-01
      VIFIPTYPTE: IPV4
      VIFIPV4ADDR: 10.99.99.99
    set_licenseswitch_list_2:
    - LICITEM: 'LKV3G5RBMS01'
      SWITCH: ENABLE
    set_apnaddressattr_list:
    - APN: 'apn-op1'
      FRAMEDROUTE: ENABLE
    set_cpapnaddressattr_list:
    - APN: 'apn-op1'
      FRAMEDROUTE: ENABLE
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFMTU: 1600
    set_nglanchgctrl_list:
    - OFFLOCCHGPLYSW: ENABLE
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
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
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
    add_pccpolicygrp_list_1:
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
    add_rule_list_1:
    - RULENAME: 'fglan_r_any'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'any_f_f'
      POLICYNAME: '5glan_pcc_p_g'
    add_userprofile_list_1:
    - USERPROFILENAME: 'fglan_u_p_any'
    add_rulebinding_list_1:
    - USERPROFILENAME: 'fglan_u_p_any'
      RULENAME: 'fglan_r_any'
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'fglan_u_p_any'
      TCPCHGPROFLAG: NOTCONFIG
      DFTSIGURRGNAME: 'ycll_01_ch_p'
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 可通过**LST LICENSESWITCH**命令查询“License项（LICITEM）”参数值。

#### 1.1 层二5G LAN组时，License名称从GWFD-030701 支持5G LAN组以太通信特性概述和GWFD-030702 支持网络侧基于VxLAN的以太通信特性概述获取。

#### 1.2 层三5G LAN组时，license名称从GWFD-030706 支持5G LAN组层三通信特性概述获取。

### 2 开启5G LAN功能开关。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

### 3 配置5G LAN组。

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
    {#- --- 条件可选：MACIDLESW=ENABLE 时可选 --- -#}
    {%- if item.MACIDLESW == 'ENABLE' -%}
        {%- if item.MACIDLETIME is not none -%}
            MACIDLETIME={{item.MACIDLETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BCASTFLOWCTRLSW=ENABLE 时可选 --- -#}
    {%- if item.BCASTFLOWCTRLSW == 'ENABLE' -%}
        {%- if item.BCASTDATARATE is not none -%}
            BCASTDATARATE={{item.BCASTDATARATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：N6MACIDLESW=ENABLE 时可选 --- -#}
    {%- if item.N6MACIDLESW == 'ENABLE' -%}
        {%- if item.N6MACIDLETIME is not none -%}
            N6MACIDLETIME={{item.N6MACIDLETIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UNICASTFLOODSW=ENABLE 时可选 --- -#}
    {%- if item.UNICASTFLOODSW == 'ENABLE' -%}
        {%- if item.UNIFLOODRATE is not none -%}
            UNIFLOODRATE={{item.UNIFLOODRATE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.1 层二5G LAN组时，“PDN类型（PDNTYPE）”设置为“ETHERNET”。

#### 支持网络侧基于VXLAN的以太通信时，还需要配置4和5。

#### 3.2 层三5G LAN组时，“PDN类型（PDNTYPE）”设置为“IP”。

#### 层三终端通过CPE接入网络时，还需要配置8。

### 4 配置VXLAN隧道。5G LAN层三通信时，请跳过本步骤。

#### 4.1 配置vxlan逻辑接口所属的VPN实例。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.1.1 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

##### 4.1.2 采用默认VPN实例“\_public\_”时，不需要再执行**ADD VPNINST**命令。

##### 4.1.3 采用已存在的VPN实例时，不需要重复执行**ADD VPNINST**命令。

#### 4.2 配置vxlan逻辑接口。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
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

#### 4.3 配置VXLAN隧道组。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
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

#### 4.4 配置VXLAN隧道端点（VTEP）。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
    {%- for item in add_vtep_list -%}
        ADD VTEP:
        {#- --- 必选参数 --- -#}
        VTEPNAME="{{item.VTEPNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.TYPE is not none -%}
            TYPE={{item.TYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            VTEPIPV4="{{item.VTEPIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置VXLAN端点绑定VXLAN隧道组。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
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

### 5 5G LAN组和VXLAN隧道组绑定。5G LAN层三通信时，请跳过本步骤。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
    {%- for item in add_ngvnbindvxlan_list -%}
        ADD NGVNBINDVXLAN:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        VNI={{item.VNI}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置UPF基于5G LAN粒度支持学习的总MAC地址数。5G LAN层三通信时，请跳过本步骤。

```jinja2
{%- if is_scenario_l2_5g_lan -%}
    {%- for item in set_nglanattr_list -%}
        SET NGLANATTR:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TOTALMACNUM is not none -%}
            TOTALMACNUM={{item.TOTALMACNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置故障定界所需数据。5G LAN层三通信时，请跳过本步骤。

### 5G LAN业务端到端时延超出预期时，可通过**NGVNVIFPING**命令获取UPF与对端之间的时延。但执行**NGVNVIFPING**命令时，依赖7.a~7.c配置，否则会执行命令失败。

#### 7.1 执行**LST UPETHSRVPARA**命令，查询UPF上是否已配置“用户面以太业务MAC”参数。

##### 7.1.1 是 => 请执行7.c。

##### 7.1.2 否 => 请执行7.b。

#### 7.2 配置设置用户面以太业务参数。配置的MAC地址可作为PING探测的源MAC地址。

```jinja2
{%- set LST_UPETHSRVPARA=getParameterValue('LST UPETHSRVPARA') -%}
{%- if is_scenario_l2_5g_lan and not LST_UPETHSRVPARA -%}
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
{%- endif -%}
```

#### 7.3 配置5G LAN组网关IP。配置的IP地址可作为PING探测的源IP地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngvnvif_list的变量区（command: ADD NGVNVIF） -#}
<!-- MISSING_MACRO: command=ADD NGVNVIF list_name=add_ngvnvif_list step_id=7.3 -->
```

### 8 层三终端通过CPE接入网络时，配置Routing Behind MS数据。5G LAN层二通信时，请跳过本步骤。

#### 8.1 打开Routing Behind MS特性的License配置开关。

```jinja2
{%- if is_scenario_l3_cpe -%}
    {%- for item in set_licenseswitch_list_2 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 （UPF）基于APN使能Routing Behind MS功能。

```jinja2
{%- if is_scenario_l3_cpe -%}
    {%- for item in set_apnaddressattr_list -%}
        SET APNADDRESSATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FRAMEDROUTE is not none -%}
            FRAMEDROUTE={{item.FRAMEDROUTE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.3 （SMF）基于APN使能Routing Behind MS功能。

```jinja2
{%- if is_scenario_l3_cpe -%}
    {%- for item in set_cpapnaddressattr_list -%}
        SET CPAPNADDRESSATTR:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FRAMEDROUTE is not none -%}
            FRAMEDROUTE={{item.FRAMEDROUTE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 DCGW/企业侧交换机与UPF之间建立VXLAN隧道的场景，修改接口MTU。

```jinja2
{%- if is_scenario_dcgw_vxlan -%}
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

### 10 风筝S/M场景，配置离线计费功能。

#### 10.1 开启离线计费功能开关。

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in set_nglanchgctrl_list -%}
        SET NGLANCHGCTRL:
        {#- --- 可选参数 --- -#}
        {%- if item.OFFLOCCHGPLYSW is not none -%}
            OFFLOCCHGPLYSW={{item.OFFLOCCHGPLYSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 10.2 配置离线计费规则。5G LAN UE会话不支持基于具体业务流的离线计费。

```jinja2
{%- if is_scenario_kite_sm -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
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

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in add_pccpolicygrp_list_1 -%}
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

```jinja2
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
    {%- for item in add_fltbindflowf_list_2 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in add_rule_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in add_userprofile_list_1 -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
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
{%- if is_scenario_kite_sm -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_kite_sm -%}
    {%- for item in set_refreshsrv_list_1 -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 详细请参见：配置业务数据 > 计费功能。

