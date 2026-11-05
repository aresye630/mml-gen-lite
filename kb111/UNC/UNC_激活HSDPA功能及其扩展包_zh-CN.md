---
id: ''
name: 激活HSDPA功能及其扩展包
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活HSDPA功能及其扩展包的操作过程。  HSDPA(High Speed Downlink Packet Access)功能, 2M-4M特性可以使终端用户可以享受新的应用业务和更快的下载速度。该特性可以使SGSN为UE提供的最大下行速率为4Mbit/s。  适用于SGSN、GGSN。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","高速数据连接功能","HSDPA功能及其扩展包","激活HSDPA功能及其扩展包"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活HSDPA功能及其扩展包的操作过程。HSDPA(High Speed Downlink Packet Access)功能, 2M-4M特性可以使终端用户可以享受新的应用业务和更快的下载速度。该特性可以使SGSN为UE提供的最大下行速率为4Mbit/s。适用于SGSN、GGSN。

## 必备事项
前提条件

* 请仔细阅读HSDPA功能及其扩展包特性概述。
* 完成加载License。

* 需要对端网元UE、RNC、GGSN、HLR支持HSDPA功能及其扩展包。
* 终端 (手机或者数据卡)支持协议版本R5及R5以上。
* SGSN、GGSN以及在HLR中的开户信息均需支持到用户希望的最大速率。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
    set_compatibility_list:
      type: items
      properties: {}
    mod_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_rnc_list_1:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_rnc_list_2:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCVER:
          name: 'RNC的协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R8
          - R9+
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFUTRAN:
          name: 'RNC是否支持Out Of UTRAN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPID:
          name: 'RNC是否支持SPID'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ggsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_GGSN
          - Gn_GGSN
          - Gp_GGSN
          - SPECIAL_GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        GGSNIPV4:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSVER:
          name: 'GGSN支持的QoS版本'
          type: string
          enum:
          - R5QOS
          - R7QOS
          - R99QOS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R99QOS
        GGSNIPV6:
          name: 'GGSN的信令面IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sgsncharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_SGSN
          - SPECIAL_SGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: '掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSVER:
          name: 'SGSN支持的QoS版本'
          type: string
          enum:
          - R5QOS
          - R7QOS
          - R99QOS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: R99QOS
        IPV6:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: '子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_3:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_4:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_5:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_imsismchar_list_6:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS2G:
          name: '是否配置2G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOS3G:
          name: '是否配置3G QoS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLKEX3G:
          name: '3G QoS扩展下行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLKEX3G:
          name: '3G QoS扩展下行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI2G:
          name: '2G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC2G:
          name: '2G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU2G:
          name: '2G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO2G:
          name: '2G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK2G:
          name: '2G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK2G:
          name: '2G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU2G:
          name: '2G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK2G:
          name: '2G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK2G:
          name: '2G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT2G:
          name: '2G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT6
          - MT7
          - MT8
          - MT9
          - PT5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI2G:
          name: '2G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT2G:
          name: '2G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI2G:
          name: '2G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER2G:
          name: '2G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC2G:
          name: '2G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER2G:
          name: '2G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC2G:
          name: '2G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD2G:
          name: '2G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI2G:
          name: '2G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPRI3G:
          name: '3G QoS分配保留优先级'
          type: string
          enum:
          - HIGHLEVELUSER
          - LOWLEVELUSER
          - NORMALUSER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DC3G:
          name: '3G QoS延迟等级'
          type: string
          enum:
          - DC1
          - DC2
          - DC3
          - DC4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESDU3G:
          name: '3G QoS发送错误SDU'
          type: string
          enum:
          - DELIVE
          - NDELIVE
          - NODT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DO3G:
          name: '3G QoS发送次序'
          type: string
          enum:
          - NORDER
          - ORDER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRDNLK3G:
          name: '3G QoS下行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLK3G:
          name: '3G QoS上行保证速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GBRUPLKEX3G:
          name: '3G QoS扩展上行保证速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXSDU3G:
          name: '3G QoS最大SDU长度'
          type: integer
          minimum: 1
          maximum: 153
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRDNLK3G:
          name: '3G QoS下行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLK3G:
          name: '3G QoS上行最大速率'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MBRUPLKEX3G:
          name: '3G QoS扩展上行最大速率'
          type: integer
          minimum: 0
          maximum: 250
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MT3G:
          name: '3G QoS平均吞吐量（octet/h）'
          type: string
          enum:
          - MT1
          - MT10
          - MT11
          - MT12
          - MT13
          - MT14
          - MT15
          - MT16
          - MT17
          - MT18
          - MT2
          - MT3
          - MT31
          - MT4
          - MT5
          - MT6
          - MT7
          - MT8
          - MT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRI3G:
          name: '3G QoS优先级'
          type: string
          enum:
          - HPRI
          - LPRI
          - NPRI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PT3G:
          name: '3G QoS最大吞吐量（octet/s）'
          type: string
          enum:
          - PT1
          - PT2
          - PT3
          - PT4
          - PT5
          - PT6
          - PT7
          - PT8
          - PT9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOPRI3G:
          name: '3G QoS无线优先级'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RBER3G:
          name: '3G QoS保留BER'
          type: string
          enum:
          - RBER1
          - RBER2
          - RBER3
          - RBER4
          - RBER5
          - RBER6
          - RBER7
          - RBER8
          - RBER9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC3G:
          name: '3G QoS可靠性'
          type: string
          enum:
          - ACKGTP
          - NACKGTP
          - NGTPLLC
          - NGTPLLCRLCP
          - NGTPLLCRLCU
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDUER3G:
          name: '3G QoSSDU误码率'
          type: string
          enum:
          - SDUER1
          - SDUER2
          - SDUER3
          - SDUER4
          - SDUER5
          - SDUER6
          - SDUER7
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TC3G:
          name: '3G QoS流量等级'
          type: string
          enum:
          - BC
          - CC
          - IC
          - SC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TD3G:
          name: '3G QoS传递时延'
          type: integer
          minimum: 1
          maximum: 62
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THPRI3G:
          name: '3G QoS发送控制优先级'
          type: string
          enum:
          - THPRI1
          - THPRI2
          - THPRI3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_3:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_4:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_5:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsismchar_list_6:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APNNI:
          name: 'APN网络标识'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEACCCAP:
          name: 'UE接入能力'
          type: string
          enum:
          - ALL_UE
          - EUTRAN_CAPABLE_UE
          - EUTRAN_INCAPABLE_UE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERSUBTYPE:
          name: '用户子类'
          type: string
          enum:
          - HOME_ALL_USER
          - HOME_LOCAL_USER
          - HOME_UNLOCAL_USER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2HD16M02'
      SWITCH: ENABLE
    set_compatibility_list:
    - {}
    mod_rnc_list:
    - RNCX: 1
      RNCVER: R99
      OFUTRAN: ''
      SPID: ''
    mod_rnc_list_1:
    - RNCX: 1
      RNCVER: R99
      OFUTRAN: ''
      SPID: ''
    mod_rnc_list_2:
    - RNCX: 1
      RNCVER: R99
      OFUTRAN: ''
      SPID: ''
    add_ggsncharact_list:
    - RANGE: SPECIAL_GGSN
      IPT: IPV4
      GGSNIPV4: '10.10.10.1'
      MASKV4: '255.255.255.255'
      QOSVER: R5QOS
      GGSNIPV6: ''
      MASKV6: ''
    add_sgsncharact_list:
    - RANGE: SPECIAL_SGSN
      IPT: IPV4
      IPV4: '10.10.11.1'
      MASKV4: '255.255.255.255'
      QOSVER: R5QOS
      IPV6: ''
      MASKV6: ''
    mod_imsismchar_list:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_1:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_2:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_3:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_4:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_5:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    mod_imsismchar_list_6:
    - SUBRANGE: ALL_USER
      APNNI: '000001'
      UEACCCAP: ALL_UE
      QOS2G: NO
      QOS3G: YES
      MBRDNLKEX3G: 183
      GBRDNLKEX3G: 183
      ARPRI2G: ''
      DC2G: ''
      DESDU2G: ''
      DO2G: ''
      GBRDNLK2G: ''
      GBRUPLK2G: ''
      MAXSDU2G: ''
      MBRDNLK2G: ''
      MBRUPLK2G: ''
      MT2G: ''
      PRI2G: ''
      PT2G: ''
      RADIOPRI2G: ''
      RBER2G: ''
      RC2G: ''
      SDUER2G: ''
      TC2G: ''
      TD2G: ''
      THPRI2G: ''
      ARPRI3G: ''
      DC3G: ''
      DESDU3G: ''
      DO3G: ''
      GBRDNLK3G: ''
      GBRUPLK3G: ''
      GBRUPLKEX3G: ''
      MAXSDU3G: ''
      MBRDNLK3G: ''
      MBRUPLK3G: ''
      MBRUPLKEX3G: ''
      MT3G: ''
      PRI3G: ''
      PT3G: ''
      RADIOPRI3G: ''
      RBER3G: ''
      RC3G: ''
      SDUER3G: ''
      TC3G: ''
      TD3G: ''
      THPRI3G: ''
      IMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_1:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_2:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_3:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_4:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_5:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
    add_imsismchar_list_6:
    - SUBRANGE: ''
      APNNI: ''
      UEACCCAP: ''
      BEGIMSI: ''
      ENDIMSI: ''
      IMSIPRE: ''
      NOID: ''
      USERSUBTYPE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本功能集的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **（可选）**不限定QoS为R5规定的最大下行速率。

```jinja2
{%- if is_optional_unlimited_qos_max_downlink_rate -%}
    SET COMPATIBILITY:
    ;
{%- endif -%}
```

### 本步骤仅需HSDPA扩展包3–6功能进行设置。

### 4 设置特定RNC的QoS支持版本。

#### 4.1 在HSDPA扩展包2中:**MOD RNC**

```jinja2
{%- if is_scenario_hsdpa_pkg2 -%}
    {%- for item in mod_rnc_list -%}
        MOD RNC:
        {#- --- 必选参数 --- -#}
        RNCX={{item.RNCX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RNCVER is not none -%}
            RNCVER={{item.RNCVER}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
        {%- if item.RNCVER == 'R9+' -%}
            {%- if item.OFUTRAN is not none -%}
                OFUTRAN={{item.OFUTRAN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
        {%- if item.RNCVER in ['R8', 'R9+'] -%}
            {%- if item.SPID is not none -%}
                SPID={{item.SPID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 在HSDPA扩展包3–6中:**MOD RNC**

```jinja2
{%- if is_scenario_hsdpa_pkg3_6 -%}
    {%- for item in mod_rnc_list_1 -%}
        MOD RNC:
        {#- --- 必选参数 --- -#}
        RNCX={{item.RNCX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RNCVER is not none -%}
            RNCVER={{item.RNCVER}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
        {%- if item.RNCVER == 'R9+' -%}
            {%- if item.OFUTRAN is not none -%}
                OFUTRAN={{item.OFUTRAN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
        {%- if item.RNCVER in ['R8', 'R9+'] -%}
            {%- if item.SPID is not none -%}
                SPID={{item.SPID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 在HSDPA扩展包3–6中:**MOD RNC**

```jinja2
{%- if is_scenario_hsdpa_pkg3_6 -%}
    {%- for item in mod_rnc_list_2 -%}
        MOD RNC:
        {#- --- 必选参数 --- -#}
        RNCX={{item.RNCX}},
        {#- --- 可选参数 --- -#}
        {%- if item.RNCVER is not none -%}
            RNCVER={{item.RNCVER}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：RNCVER=R9+ 时可选 --- -#}
        {%- if item.RNCVER == 'R9+' -%}
            {%- if item.OFUTRAN is not none -%}
                OFUTRAN={{item.OFUTRAN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：RNCVER=R8/R9+ 时可选 --- -#}
        {%- if item.RNCVER in ['R8', 'R9+'] -%}
            {%- if item.SPID is not none -%}
                SPID={{item.SPID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 设置特定GGSN的QoS支持版本。

```jinja2
{%- for item in add_ggsncharact_list -%}
    ADD GGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.QOSVER is not none -%}
        QOSVER={{item.QOSVER}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_GGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_GGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        GGSNIPV4="{{item.GGSNIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        GGSNIPV6="{{item.GGSNIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。

### 在HSDPA扩展包3–6中，设置GGSN支持的QoS版本为R7QoS，参数“QoSVER”（SGSN支持的QoS版本）固定选择“R7QoS”。

### 6 设置特定SGSN的QoS支持版本。

```jinja2
{%- for item in add_sgsncharact_list -%}
    ADD SGSNCHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.QOSVER is not none -%}
        QOSVER={{item.QOSVER}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_SGSN 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_SGSN' -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。

### 在HSDPA扩展包3–6中，设置SGSN支持的QoS版本为R7QoS，“QoSVER”（SGSN支持的QoS版本）固定选择“R7QoS”。

### 7 设置SGSN支持的下行速率和保证下行速率为用户所购买License所支持的最大值。

#### 7.1 **可选：**全部用户

##### 7.1.1 HSDPA功能, 2M-4M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_2m4m -%}
    {%- for item in mod_imsismchar_list -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.2 HSDPA扩展包1, 4M-8M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg1 -%}
    {%- for item in mod_imsismchar_list_1 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.3 HSDPA扩展包2, 8M-16M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg2 -%}
    {%- for item in mod_imsismchar_list_2 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.4 HSDPA扩展包3, 16M-32M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg3 -%}
    {%- for item in mod_imsismchar_list_3 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.5 HSDPA扩展包4, 32M-48M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg4 -%}
    {%- for item in mod_imsismchar_list_4 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.6 HSDPA扩展包5, 48M-84M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg5 -%}
    {%- for item in mod_imsismchar_list_5 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.1.7 HSDPA扩展包6, 84M-168M:

```jinja2
{%- if is_optional_all_users and is_scenario_hsdpa_pkg6 -%}
    {%- for item in mod_imsismchar_list_6 -%}
        MOD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        APNNI="{{item.APNNI}}",
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS2G is not none -%}
            QOS2G={{item.QOS2G}},
        {%- endif -%}
        {%- if item.QOS3G is not none -%}
            QOS3G={{item.QOS3G}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLKEX3G is not none -%}
                MBRDNLKEX3G={{item.MBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLKEX3G is not none -%}
                GBRDNLKEX3G={{item.GBRDNLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.ARPRI2G is not none -%}
                ARPRI2G={{item.ARPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.ARPRI3G is not none -%}
                ARPRI3G={{item.ARPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DC2G is not none -%}
                DC2G={{item.DC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DC3G is not none -%}
                DC3G={{item.DC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DESDU2G is not none -%}
                DESDU2G={{item.DESDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DESDU3G is not none -%}
                DESDU3G={{item.DESDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.DO2G is not none -%}
                DO2G={{item.DO2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.DO3G is not none -%}
                DO3G={{item.DO3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRDNLK2G is not none -%}
                GBRDNLK2G={{item.GBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRDNLK3G is not none -%}
                GBRDNLK3G={{item.GBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.GBRUPLK2G is not none -%}
                GBRUPLK2G={{item.GBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLK3G is not none -%}
                GBRUPLK3G={{item.GBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.GBRUPLKEX3G is not none -%}
                GBRUPLKEX3G={{item.GBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MAXSDU2G is not none -%}
                MAXSDU2G={{item.MAXSDU2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MAXSDU3G is not none -%}
                MAXSDU3G={{item.MAXSDU3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRDNLK2G is not none -%}
                MBRDNLK2G={{item.MBRDNLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRDNLK3G is not none -%}
                MBRDNLK3G={{item.MBRDNLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MBRUPLK2G is not none -%}
                MBRUPLK2G={{item.MBRUPLK2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLK3G is not none -%}
                MBRUPLK3G={{item.MBRUPLK3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MBRUPLKEX3G is not none -%}
                MBRUPLKEX3G={{item.MBRUPLKEX3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.MT2G is not none -%}
                MT2G={{item.MT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.MT3G is not none -%}
                MT3G={{item.MT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PRI2G is not none -%}
                PRI2G={{item.PRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PRI3G is not none -%}
                PRI3G={{item.PRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.PT2G is not none -%}
                PT2G={{item.PT2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.PT3G is not none -%}
                PT3G={{item.PT3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RADIOPRI2G is not none -%}
                RADIOPRI2G={{item.RADIOPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RADIOPRI3G is not none -%}
                RADIOPRI3G={{item.RADIOPRI3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RBER2G is not none -%}
                RBER2G={{item.RBER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RBER3G is not none -%}
                RBER3G={{item.RBER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.RC2G is not none -%}
                RC2G={{item.RC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.RC3G is not none -%}
                RC3G={{item.RC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.SDUER2G is not none -%}
                SDUER2G={{item.SDUER2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.SDUER3G is not none -%}
                SDUER3G={{item.SDUER3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TC2G is not none -%}
                TC2G={{item.TC2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TC3G is not none -%}
                TC3G={{item.TC3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.TD2G is not none -%}
                TD2G={{item.TD2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.TD3G is not none -%}
                TD3G={{item.TD3G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS2G=YES 时可选 --- -#}
        {%- if item.QOS2G == 'YES' -%}
            {%- if item.THPRI2G is not none -%}
                THPRI2G={{item.THPRI2G}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：QOS3G=YES 时可选 --- -#}
        {%- if item.QOS3G == 'YES' -%}
            {%- if item.THPRI3G is not none -%}
                THPRI3G={{item.THPRI3G}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。

#### 7.2 **可选：**部分用户

##### 7.2.1 HSDPA功能, 2M-4M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_2m4m -%}
    {%- for item in add_imsismchar_list -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.2 HSDPA扩展包1, 4M-8M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg1 -%}
    {%- for item in add_imsismchar_list_1 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.3 HSDPA扩展包2, 8M-16M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg2 -%}
    {%- for item in add_imsismchar_list_2 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.4 HSDPA扩展包3, 16M-32M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg3 -%}
    {%- for item in add_imsismchar_list_3 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.5 HSDPA扩展包4, 32M-48M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg4 -%}
    {%- for item in add_imsismchar_list_4 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.6 HSDPA扩展包5, 48M-84M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg5 -%}
    {%- for item in add_imsismchar_list_5 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.7 HSDPA扩展包6, 84M-168M:

```jinja2
{%- if is_optional_partial_users and is_scenario_hsdpa_pkg6 -%}
    {%- for item in add_imsismchar_list_6 -%}
        ADD IMSISMCHAR:
        {#- --- 必选参数 --- -#}
        APNNI="{{item.APNNI}}",
        SUBRANGE={{item.SUBRANGE}},
        UEACCCAP={{item.UEACCCAP}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'HOME_USER' -%}
            USERSUBTYPE={{item.USERSUBTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。

