---
id: ''
name: 配置UPF数据
ne_type: UEG
type: feature
description: 层二终端组成员之间或层二终端组的成员和数据网络中的应用之间进行以太通信时，需要配置5G LAN功能。
tags: []
risk_level: ''
doc_source: ["原子能力&行业场景","原子能力","5GC toB 原子能力-5G LAN","网络部署","运营商","配置5GC网元","配置UPF数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
层二终端组成员之间或层二终端组的成员和数据网络中的应用之间进行以太通信时，需要配置5G LAN功能。

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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APN/DNN实例应该全网规划，UEG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。'
          data_source: '本端规划'
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
          description: 'APN/DNN实例应该全网规划，UEG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。'
          data_source: '本端规划'
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
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  UDM和UPF上，5G LAN标识进制不完全相同。对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识在相同机制格式下必须一致。'
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
          data_source: '本端规划'
          pattern: ''
          default: ETHERNET
        MACIDLESW:
          name: 'N3侧MAC地址空闲时长开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'UPF开启MAC地址老化功能时需要设置为“ENABLE”。'
          data_source: '本端规划'
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
          description: '需要UPF支持将未知组播消息泛洪处理时，设置为“ENABLE”。'
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
          description: '用于设置是否对广播报文进行流控。“BCASTFLOWCTRLSW”设置为“ENABLE”时，流控周期（1s）内上行广播报文数+下行广播报文数大于“BCASTDATARATE”参数值时进行流控，该流控周期内后续再收到的上下行广播报文均做丢弃处理。  此处以不开启流控为例，请以局点规划为准。'
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
          description: '该参数设置为“DISABLE”时，层二终端必须先发送过上行报文，才能正常接收下行单播报文。  推荐设置为“DISABLE”。  该参数仅用于控制N3侧未知单播是否泛洪转发。不控制到VTEP的未知单播泛洪处理。'
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
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。  说明：  * DCGW与UPF之间建立VXLAN隧道的场景，VXLAN逻辑接口绑定的“VPNINSTANCE”为默认VPN实例“\_public\_”。   采用默认VPN实例“\_public\_”时，不需要再执行**ADD VPNINST**命令。 * 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。   采用已存在的VPN实例时，不需要重复执行**ADD VPNINST**命令。'
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
    add_logicinf_list_1:
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
          description: '对端（DCGW/企业侧VXLAN交换机）的VXLAN隧道IP地址。'
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
    add_vtep_list_1:
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
          description: '另一UPF的VXLAN隧道IP地址，用于两个UPF之间建立VXLAN隧道。  两个UPF仅对接到同一对DCGW/企业侧VXLAN交换机时需要规划，否则不需要规划。'
          data_source: '与对端协商'
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
          minLength: 0
          maxLength: 37
          required: true
          description: '可通过**LST NGVNINSTANCE**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VIFIPTYPE:
          name: '虚拟接口IP地址类型'
          type: string
          enum:
          - IPV4
          required: true
          description: '当前仅支持IPv4。'
          data_source: '固定取值'
          pattern: ''
          default: IPV4
        VIFIPV4ADDR:
          name: '虚拟接口IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '此处规划的是探测源IP，从DHCP Server获取。  与DHCP Server工程师协商，该IP地址等同于DHCP Server分配给5G LAN层二终端的IP地址，与5G LAN层二终端的IP地址在同一网段，且不能与5G LAN层二终端的IP地址冲突。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LANB01'
      SWITCH: ENABLE
    set_nglanfunc_list:
    - NGLANSW: ENABLE
    add_apn_list:
    - APN: 'dnn5glan01'
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
      VPNINSTANCE: '_public_'
    add_logicinf_list_1:
    - NAME: 'vxlanif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.50.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_vxlan'
    add_vxlangrp_list:
    - GRPNAME: 'vxlan_01'
      SRCINTF: 'vxlanif1/1/0'
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP1'
    add_vtep_list_1:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.1.50.2'
    add_vtepbindgrp_list_1:
    - VXLANGRPNAME: 'vxlan_01'
      VTEPNAME: 'VTEP2'
      PRIFLAG: PRIMARY
    add_ngvnbindvxlan_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VXLANGRPNAME: 'vxlan_01'
      VNI: 5010
    set_nglanattr_list:
    - VNINSTANCE: '000003e9-460-08-01'
      TOTALMACNUM: 6000
    set_licenseswitch_list_1:
    - LICITEM: 'LKV3G5LAN2LE'
      SWITCH: ENABLE
    set_ngloopdetfunc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      ETHLOOPDETECTSW: ENABLE
      DETECTMETHOD: SEND_DETECT_MSG
    set_upethsrvpara_list:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    mod_interface_list:
    - IFNAME: 'Ethernet64/0/4'
      IFMTU: 1600
    mod_interface_list_2:
    - IFNAME: 'Eth-trunk1'
      IFMTU: 1600
    set_upethsrvpara_list_1:
    - UPETHSRVSW: ENABLE
      UPETHSRVMAC: 'FA-16-3E-A0-04-D6'
    add_ngvnvif_list:
    - VNINSTANCE: '000003e9-460-08-01'
      VIFIPTYPE: IPV4
      VIFIPV4ADDR: '10.99.99.99'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置UPF 5G LAN全局参数。

#### 1.1 //开启5G LAN特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.2 //开启5G LAN功能。

```jinja2
{%- for item in set_nglanfunc_list -%}
    SET NGLANFUNC:
    {#- --- 必选参数 --- -#}
    NGLANSW={{item.NGLANSW}},
    ;
{%- endfor -%}
```

### 2 配置UPF支持的DNN（APN）信息。

#### 2.1 UEG-S时：

```jinja2
{%- if is_scenario_ueg_s -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 UEG-M/UEG-L时：

```jinja2
{%- if is_scenario_ueg_m_l -%}
    {%- for item in add_upapn_list -%}
        ADD UPAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置UPF支持的5G LAN组。

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
    ;
{%- endfor -%}
```

### 4 配置5G LAN的VXLAN隧道。

#### 4.1 //配置vxlan逻辑接口所属的VPN实例。企业侧交换机与UPF之间建立VXLAN隧道场景按需配置；采用“\_public\_”的VPN实例时，不需要再执行**ADD VPNINST**命令。采用已存在的VPN实例时，不需要重复执行**ADD VPNINST**命令。

```jinja2
{%- if is_scenario_enterprise_switch_vxlan -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 DCGW与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”必须设置为“\_public\_”。

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

#### 4.4 企业侧交换机与UPF之间建立VXLAN隧道的场景，“VPNINSTANCE”按需配置。此处以“VRF\_LocalDN01”为例。

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

#### 4.5 //配置VXLAN隧道组。

```jinja2
{%- for item in add_vxlangrp_list -%}
    ADD VXLANGRP:
    {#- --- 必选参数 --- -#}
    GRPNAME="{{item.GRPNAME}}",
    SRCINTF="{{item.SRCINTF}}",
    ;
{%- endfor -%}
```

#### 4.6 //配置VXLAN隧道远端端点，VTEPIPV4为远端端点IP，来源于企业侧交换机的VTEP地址。

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

#### 4.7 //配置VXLAN隧道端点绑定VXLAN隧道组。

```jinja2
{%- for item in add_vtepbindgrp_list -%}
    ADD VTEPBINDGRP:
    {#- --- 必选参数 --- -#}
    VXLANGRPNAME="{{item.VXLANGRPNAME}}",
    VTEPNAME="{{item.VTEPNAME}}",
    ;
{%- endfor -%}
```

#### 4.8 //配置VXLAN隧道远端端点（VTEP：另一UPF）。两个UPF是负荷分担关系，且仅对接到同一对DCGW/企业侧VXLAN交换机场景，同一5G LAN组内成员跨UPF的互访通过UPF间的VxLAN隧道实现时需要配置，否则不需要配置。VTEPIPV4为远端端点IP，来源于另一UPF的VXLAN隧道端点IP地址。

```jinja2
{%- if is_scenario_two_upf_same_switch -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_two_upf_same_switch -%}
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
{%- endif -%}
```

#### 4.9 //绑定5G LAN组与VXLAN隧道组。

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

#### 4.10 //配置UPF基于5G LAN组粒度支持学习的总MAC地址数。

```jinja2
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
```

#### 4.11 //配置基于5G LAN组粒度的环路检测功能。此处以采用主动检测为例。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
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
```

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

#### 4.13 Ethernet接口组网时，主接口和子接口均需要修改：

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

#### 4.14 Eth-trunk接口组网时，主接口和子接口均需要修改：

##### 4.14.1 //Eth-trunk接口组网时，不需要修改成员接口的MTU值。若规划的成员接口在加入Eth-trunk前修改了MTU值，则会导致添加成员接口失败。

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

### 5 配置故障定界所需数据（执行**NGVNVIFPING**获取时延时依赖的数据）。

#### 5.1 //此处配置的是UPF发送的ping探测报文的源MAC地址，建议采用N3逻辑接口对应的物理接口的MAC地址，避免MAC地址冲突。可通过执行**LST LOGICINF**命令，获取N3if或Saif接口绑定的VPN实例，然后再执行**LST INTERFACE**命令获取对应的外联口的MAC地址。

```jinja2
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
```

#### 5.2 //基于5G LAN组配置ping探测报文的源IP地址。从DHCP Server获取，该IP地址等同于DHCP Server分配给5G LAN层二终端的IP地址，与5G LAN层二终端的IP地址在同一网段，且不能与5G LAN层二终端的IP地址冲突。

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

### 6 配置企业DN侧VXLAN隧道数据，请参考配置企业DN侧交换机。

