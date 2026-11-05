---
id: ''
name: 增加媒体中继全局配置
ne_type: UDG
type: feature
description: 媒体中继业务需要在UPF上开启License，并设置媒体中继业务使用的IP地址等全局参数。本章节用于指导如何配置媒体中继业务的全局配置。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体中继全局配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
媒体中继业务需要在UPF上开启License，并设置媒体中继业务使用的IP地址等全局参数。本章节用于指导如何配置媒体中继业务的全局配置。

## 必备事项
前提条件

* 请提前了解媒体中继方案实现原理。
* 已完成License加载。
* 已完成框间级联部署及扩容。
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_relayippool_list:
      type: items
      properties:
        POOLNAME:
          name: 'IP池名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该参数为媒体在中继UPF与CDN交互时使用的Relay IP Pool地址池的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该参数需要与使用媒体中继的用户VPN相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_relayipsection_list:
      type: items
      properties:
        POOLNAME:
          name: 'IP池名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已通过  **ADD RELAYIPPOOL**完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECTIONID:
          name: 'IP段ID'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: 'IP地址池的地址段序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INSTID:
          name: '业务实例ID'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '该参数为媒体中继业务POD（relay-pod）的实例ID。可以通过**DSP POD**命令查询当前relay-pod的实例ID。  每个媒体中继业务POD都需要配置一个IP地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '全网规划'
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
        IPV4MASKLEN:
          name: 'IPv4掩码长度'
          type: integer
          minimum: 19
          maximum: 32
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
          description: '媒体中继UPF与CDN交互使用的Relay IP Pool地址池。该地址池IP不能与终端用户地址重复，不能与已配置的媒体中继相关IP地址重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6MASKLEN:
          name: 'IPv6掩码长度'
          type: integer
          minimum: 115
          maximum: 128
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_aggregateroute_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv6uni
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AGGREADDRESSV6:
          name: 'IPv6聚合地址'
          type: string
          maxLength: 39
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASKLENGTHV6:
          name: 'IPv6地址掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DETAILSUPPRESSED:
          name: '具体路由抑制'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        AGGREADDRESS:
          name: 'IPv4聚合地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ASSETENABLE:
          name: 'AS Set使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        ATTRIBUTEPOLICY:
          name: '属性策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: 'IPv4地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ORIGINPOLICY:
          name: '路由源策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPRESSPOLICY:
          name: '通告抑制策略'
          type: string
          maxLength: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_relaydnsserver_list:
      type: items
      properties:
        DNSSERVERNAME:
          name: 'DNS服务器名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该参数用于媒体中继UPF回源时查询CDN的IP地址时使用的DNS服务器的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该参数与用户访问业务使用的VPN保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MDNSSRVIPV4:
          name: 'IPv4主DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDNSSRVIPV4:
          name: 'IPv4备DNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: '运营商使用的内网DNS备服务器的IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MDNSSRVIPV6:
          name: 'IPv6主DNS服务器'
          type: string
          maxLength: 39
          required: false
          description: '运营商使用的内网DNS主服务器的IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SDNSSRVIPV6:
          name: 'IPv6备DNS服务器IP'
          type: string
          maxLength: 39
          required: false
          description: '运营商使用的内网DNS备服务器的IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNSDETECTSW:
          name: 'DNS探测功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: DISABLE
        DETECTDOMAINNM:
          name: '探测域名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPSELECTMODE:
          name: 'IP选择模式'
          type: string
          enum:
          - IPv4First
          - IPv6First
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: IPv6First
        DETECTTIMER:
          name: '探测功能定时器（秒）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 300
    set_dcsliveparas_list:
      type: items
      properties:
        LIVEAGINGPERIOD:
          name: '直播资源老化周期（m）'
          type: integer
          minimum: 1
          maximum: 720
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_fwsoftpara_list:
      type: items
      properties:
        PARAMETERSTYPE:
          name: '参数类型'
          type: string
          enum:
          - DWORD
          - DWORD_EX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDINDEX:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTENDDWORDINDEX:
          name: '扩展DWORD索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXTENDDWORDVALUE:
          name: '扩展DWORD取值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_glbrlystcpctrl_list:
      type: items
      properties:
        ICWND:
          name: '初始拥塞窗口大小（千字节）'
          type: integer
          minimum: 10
          maximum: 1024
          required: false
          description: '用于设置媒体中继业务使用的TCP协议栈的初始拥塞窗口大小。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_glbrlysparactl_list:
      type: items
      properties:
        VODMAXDATASIZE:
          name: '点播推流最大数据块（千字节）'
          type: integer
          minimum: 1
          maximum: 1024
          required: false
          description: '用于设置针对点播业务，媒体中继UPF每次给用户推送的最大数据块。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MAXDNSIDLETM:
          name: '回源DNS记录最大空闲时长（分钟）'
          type: integer
          minimum: 5
          maximum: 1440
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VODFSTPUSHLEN:
          name: '点播业务首次推送数据大小（千字节）'
          type: integer
          minimum: 100
          maximum: 4096
          required: false
          description: '用于设置针对点播业务，媒体中继UPF给用户首次推送数据大小。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VODPUSHACKNUM:
          name: '点播推流ACK间隔（次数）'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '用于设置针对点播业务，媒体中继UPF收到几个ACK后向用户进行推流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VODPRELOADLEN:
          name: '点播回源预加载数据大小（千字节）'
          type: integer
          minimum:
          - 100
          - 0
          maximum:
          - 10240
          - 0
          required: false
          description: '用于设置针对点播业务，媒体中继UPF从CDN回源时申请的数据大小。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIVEFSTPUSHLEN:
          name: '直播业务首次推送数据大小（千字节）'
          type: integer
          minimum: 100
          maximum: 10240
          required: false
          description: '用于设置针对直播业务，媒体中继UPF首次向用户推送的数据大小。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIVEPUSHACKNUM:
          name: '直播推流ACK间隔（次数）'
          type: integer
          minimum: 0
          maximum: 50
          required: false
          description: '用于设置针对直播业务，媒体中继UPF收到几个ACK后向用户进行推流。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_upglbchgpara_list:
      type: items
      properties:
        RELAYCHSW:
          name: '媒体中继计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当运营商需要进行计费一致性检查时，需要开启此功能。  该开关仅对N40计费生效，GaGy计费不生效。开启功能后，UPF单独上报媒体中继流量给SMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_relaypreconfun_list:
      type: items
      properties:
        PRECONSW:
          name: '预建链功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该参数用于开启媒体中继预建链功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LIVEMINCONNUM:
          name: '直播最小预建链个数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXUSEDTIME:
          name: '点播链路最长复用时间（分钟）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VODMAXRUDTIMES:
          name: '点播链路最大复用次数（次）'
          type: integer
          minimum: 0
          maximum: 1000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VODMINCONNUM:
          name: '点播最小预建链个数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_relaysalmpara_list:
      type: items
      properties:
        URLAUTHRPTTHD:
          name: 'URL鉴权告警上报阈值（万分比）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLAUTHRSTTHD:
          name: 'URL鉴权告警恢复阈值（万分比）'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLAUTHALMSW:
          name: 'URL鉴权失败告警开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list:
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: '用于控制拨测用户是否调度到同一个POD。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list_1:
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: '用于控制媒体中继UPF针对直播业务如何标识本地资源。取值为1时，以URL中unique\_id作为本地资源唯一标识。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT2:
          name: '软参记录数据类型（DT2）'
          type: string
          enum:
          - BYTE
          - DWORD
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参BIT位位置'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: '用于控制直播预取内容的老化时间。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDPOSITION:
          name: 'Dword软参BIT位位置'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: 'Bit7~9用于配置全流回源老化时间。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: '配置为1，表示全流回源老化时间为10s。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softpara_list_2:
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: '用于控制DNS域名解析结果的老化时间。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '配置为255时，表示不老化。'
          data_source: '固定取值'
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
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_upfservicetype_list:
      type: items
      properties:
        SERVICETYPE1:
          name: '可选服务类型1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该命令用于配置在网管上显示的UPF支持的可选服务类型。如果UPF同时支持其他可选服务类型需要一并配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_vvipextrpt_list:
      type: items
      properties:
        MEDIARELAYSW:
          name: '媒体中继用户标识开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置保障用户单据是否携带媒体中继用户标识。  请在对端NWDAF支持此消息解析时进行对应配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    set_expextrpt_list:
      type: items
      properties:
        MEDIARELAYSW:
          name: '媒体中继用户标识开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置体验用户单据是否携带媒体中继用户标识。  请在对端NWDAF支持此消息解析时进行对应配置。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5SMRB01'
      SWITCH: ENABLE
    add_relayippool_list:
    - POOLNAME: 'relay_ip_pool_cmnet'
      VPNNAME: 'VRF_Internet'
    add_relayipsection_list:
    - POOLNAME: 'relay_ip_pool_cmnet'
      SECTIONID: 0
      INSTID: 0
      IPVERSION: IPV4
      IPV4ADDR: '10.201.0.0'
      IPV4MASKLEN: 21
      IPV6ADDR: '2409:892B:A80:1000:1000:1000:1000:2000'
      IPV6MASKLEN: 115
    add_aggregateroute_list:
    - VRFNAME: 'VRF_Internet'
      AFTYPE: ipv6uni
      AGGREADDRESSV6: '2409:892B:A80::'
      MASKLENGTHV6: 48
      DETAILSUPPRESSED: TRUE
      AGGREADDRESS: ''
      ASSETENABLE: FALSE
      ATTRIBUTEPOLICY: ''
      MASKLENGTH: ''
      ORIGINPOLICY: ''
      SUPPRESSPOLICY: ''
    add_relaydnsserver_list:
    - DNSSERVERNAME: 'relay_dns_server'
      VPNNAME: 'VRF_Internet'
      MDNSSRVIPV4: '10.200.100.101'
      SDNSSRVIPV4: '10.200.100.102'
      MDNSSRVIPV6: '2409:8028:2000::3333'
      SDNSSRVIPV6: '2409:8028:2000::1111'
      DNSDETECTSW: ENABLE
      DETECTDOMAINNM: 'www.huawei.com'
      IPSELECTMODE: IPv6First
      DETECTTIMER: 300
    set_dcsliveparas_list:
    - LIVEAGINGPERIOD: 2
    set_fwsoftpara_list:
    - PARAMETERSTYPE: DWORD
      DWORDINDEX: 198
      DWORDVALUE: 3
      EXTENDDWORDINDEX: ''
      EXTENDDWORDVALUE: ''
    set_glbrlystcpctrl_list:
    - ICWND: 512
    set_glbrlysparactl_list:
    - VODMAXDATASIZE: 120
      MAXDNSIDLETM: 720
      VODFSTPUSHLEN: 2048
      VODPUSHACKNUM: 2
      VODPRELOADLEN: 512
      LIVEFSTPUSHLEN: 4096
      LIVEPUSHACKNUM: 2
    set_upglbchgpara_list:
    - RELAYCHSW: ENABLE
    set_relaypreconfun_list:
    - PRECONSW: ENABLE
      LIVEMINCONNUM: ''
      MAXUSEDTIME: ''
      VODMAXRUDTIMES: ''
      VODMINCONNUM: ''
    set_relaysalmpara_list:
    - URLAUTHRPTTHD: 1000
      URLAUTHRSTTHD: 500
      URLAUTHALMSW: ''
    set_softpara_list:
    - DT: BIT
      BITNUM: 2616
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    set_softpara_list_1:
    - DT: BIT
      BITNUM: 2680
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    set_softparaofbit_list:
    - DT2: BYTE
      BYTENUM: 1130
      BYTEPOSITION: 2
      BYTEVALUE: 1
      DWORDNUM: 134
      DWORDPOSITION: 9
      DWORDVALUE: 0
    set_softpara_list_2:
    - DT: BYTE
      BYTENUM: 1141
      BYTEVALUE: 255
      BITNUM: ''
      BITVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    set_upfservicetype_list:
    - SERVICETYPE1: 'Relay'
    set_vvipextrpt_list:
    - MEDIARELAYSW: ENABLE
    set_expextrpt_list:
    - MEDIARELAYSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //打开媒体中继基本功能License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //配置回源地址池，回源地址池IP地址段。

### 配置的回源地址如果是内网IPv4/IPv6地址时，需要在防火墙上对这些地池段进行放通，并审视是否需要增加公网IP地址。

```jinja2
{%- for item in add_relayippool_list -%}
    ADD RELAYIPPOOL:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_relayipsection_list -%}
    ADD RELAYIPSECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONID={{item.SECTIONID}},
    INSTID={{item.INSTID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4MASKLEN={{item.IPV4MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        IPV6MASKLEN={{item.IPV6MASKLEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 //（条件必选）当路由器不支持小段路由发布时，需要配置回源地址路由聚合。

### 参考实际现网部署的聚合参数部署。

```jinja2
{%- if is_scenario_router_no_small_segment_route -%}
    {%- for item in add_aggregateroute_list -%}
        ADD AGGREGATEROUTE:
        {#- --- 必选参数 --- -#}
        AFTYPE={{item.AFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.VRFNAME is not none -%}
            VRFNAME="{{item.VRFNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            AGGREADDRESSV6="{{item.AGGREADDRESSV6}}",
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv6uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv6uni' -%}
            MASKLENGTHV6={{item.MASKLENGTHV6}},
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv4uni' -%}
            AGGREADDRESS="{{item.AGGREADDRESS}}",
        {%- endif -%}
        {#- --- 条件必选：AFTYPE=ipv4uni 时必选 --- -#}
        {%- if item.AFTYPE == 'ipv4uni' -%}
            MASKLENGTH={{item.MASKLENGTH}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
            {%- if item.DETAILSUPPRESSED is not none -%}
                DETAILSUPPRESSED={{item.DETAILSUPPRESSED}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
            {%- if item.ASSETENABLE is not none -%}
                ASSETENABLE={{item.ASSETENABLE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
            {%- if item.ATTRIBUTEPOLICY is not none -%}
                ATTRIBUTEPOLICY="{{item.ATTRIBUTEPOLICY}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
            {%- if item.ORIGINPOLICY is not none -%}
                ORIGINPOLICY="{{item.ORIGINPOLICY}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AFTYPE=ipv4uni/ipv6uni 时可选 --- -#}
        {%- if item.AFTYPE in ['ipv4uni', 'ipv6uni'] -%}
            {%- if item.SUPPRESSPOLICY is not none -%}
                SUPPRESSPOLICY="{{item.SUPPRESSPOLICY}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 //配置回源DNS服务器。

```jinja2
{%- for item in add_relaydnsserver_list -%}
    ADD RELAYDNSSERVER:
    {#- --- 必选参数 --- -#}
    DNSSERVERNAME="{{item.DNSSERVERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.MDNSSRVIPV4 is not none -%}
        MDNSSRVIPV4="{{item.MDNSSRVIPV4}}",
    {%- endif -%}
    {%- if item.SDNSSRVIPV4 is not none -%}
        SDNSSRVIPV4="{{item.SDNSSRVIPV4}}",
    {%- endif -%}
    {%- if item.MDNSSRVIPV6 is not none -%}
        MDNSSRVIPV6="{{item.MDNSSRVIPV6}}",
    {%- endif -%}
    {%- if item.SDNSSRVIPV6 is not none -%}
        SDNSSRVIPV6="{{item.SDNSSRVIPV6}}",
    {%- endif -%}
    {%- if item.DNSDETECTSW is not none -%}
        DNSDETECTSW={{item.DNSDETECTSW}},
    {%- endif -%}
    {%- if item.IPSELECTMODE is not none -%}
        IPSELECTMODE={{item.IPSELECTMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DNSDETECTSW=ENABLE 时必选 --- -#}
    {%- if item.DNSDETECTSW == 'ENABLE' -%}
        DETECTDOMAINNM="{{item.DETECTDOMAINNM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DNSDETECTSW=ENABLE 时可选 --- -#}
    {%- if item.DNSDETECTSW == 'ENABLE' -%}
        {%- if item.DETECTTIMER is not none -%}
            DETECTTIMER={{item.DETECTTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 //设置直播点播缓存参数。

```jinja2
{%- for item in set_dcsliveparas_list -%}
    SET DCSLIVEPARAS:
    {#- --- 可选参数 --- -#}
    {%- if item.LIVEAGINGPERIOD is not none -%}
        LIVEAGINGPERIOD={{item.LIVEAGINGPERIOD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_fwsoftpara_list -%}
    SET FWSOFTPARA:
    {#- --- 必选参数 --- -#}
    PARAMETERSTYPE={{item.PARAMETERSTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDINDEX={{item.DWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD_EX 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD_EX' -%}
        EXTENDDWORDINDEX={{item.EXTENDDWORDINDEX}},
    {%- endif -%}
    {#- --- 条件必选：PARAMETERSTYPE=DWORD_EX 时必选 --- -#}
    {%- if item.PARAMETERSTYPE == 'DWORD_EX' -%}
        EXTENDDWORDVALUE={{item.EXTENDDWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //设置媒体中继协议控制参数。

```jinja2
{%- for item in set_glbrlystcpctrl_list -%}
    SET GLBRLYSTCPCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.ICWND is not none -%}
        ICWND={{item.ICWND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 //设置媒体中继全局业务参数。

```jinja2
{%- for item in set_glbrlysparactl_list -%}
    SET GLBRLYSPARACTL:
    {#- --- 可选参数 --- -#}
    {%- if item.VODMAXDATASIZE is not none -%}
        VODMAXDATASIZE={{item.VODMAXDATASIZE}},
    {%- endif -%}
    {%- if item.MAXDNSIDLETM is not none -%}
        MAXDNSIDLETM={{item.MAXDNSIDLETM}},
    {%- endif -%}
    {%- if item.VODFSTPUSHLEN is not none -%}
        VODFSTPUSHLEN={{item.VODFSTPUSHLEN}},
    {%- endif -%}
    {%- if item.VODPUSHACKNUM is not none -%}
        VODPUSHACKNUM={{item.VODPUSHACKNUM}},
    {%- endif -%}
    {%- if item.VODPRELOADLEN is not none -%}
        VODPRELOADLEN={{item.VODPRELOADLEN}},
    {%- endif -%}
    {%- if item.LIVEFSTPUSHLEN is not none -%}
        LIVEFSTPUSHLEN={{item.LIVEFSTPUSHLEN}},
    {%- endif -%}
    {%- if item.LIVEPUSHACKNUM is not none -%}
        LIVEPUSHACKNUM={{item.LIVEPUSHACKNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 //（条件必选）当需要进行计费一致性检查时，开启媒体中继流量单独统计计费流量功能。

### 中继流量单独统计计费流量功能用于计费准确性测试场景进行Relay流量核减，需要SMF和CHF网元同时升级到20.16.2版本后才能开启。

```jinja2
{%- if is_scenario_billing_consistency_check -%}
    {%- for item in set_upglbchgpara_list -%}
        SET UPGLBCHGPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.RELAYCHSW is not none -%}
            RELAYCHSW={{item.RELAYCHSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 //开启媒体中继预建链功能。

```jinja2
{%- for item in set_relaypreconfun_list -%}
    SET RELAYPRECONFUN:
    {#- --- 可选参数 --- -#}
    {%- if item.PRECONSW is not none -%}
        PRECONSW={{item.PRECONSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PRECONSW=ENABLE 时可选 --- -#}
    {%- if item.PRECONSW == 'ENABLE' -%}
        {%- if item.LIVEMINCONNUM is not none -%}
            LIVEMINCONNUM={{item.LIVEMINCONNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PRECONSW=ENABLE 时可选 --- -#}
    {%- if item.PRECONSW == 'ENABLE' -%}
        {%- if item.MAXUSEDTIME is not none -%}
            MAXUSEDTIME={{item.MAXUSEDTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PRECONSW=ENABLE 时可选 --- -#}
    {%- if item.PRECONSW == 'ENABLE' -%}
        {%- if item.VODMAXRUDTIMES is not none -%}
            VODMAXRUDTIMES={{item.VODMAXRUDTIMES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PRECONSW=ENABLE 时可选 --- -#}
    {%- if item.PRECONSW == 'ENABLE' -%}
        {%- if item.VODMINCONNUM is not none -%}
            VODMINCONNUM={{item.VODMINCONNUM}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 //设置媒体中继相关告警参数。

```jinja2
{%- for item in set_relaysalmpara_list -%}
    SET RELAYSALMPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.URLAUTHALMSW is not none -%}
        URLAUTHALMSW={{item.URLAUTHALMSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLAUTHALMSW=ENABLE 时可选 --- -#}
    {%- if item.URLAUTHALMSW == 'ENABLE' -%}
        {%- if item.URLAUTHRPTTHD is not none -%}
            URLAUTHRPTTHD={{item.URLAUTHRPTTHD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：URLAUTHALMSW=ENABLE 时可选 --- -#}
    {%- if item.URLAUTHALMSW == 'ENABLE' -%}
        {%- if item.URLAUTHRSTTHD is not none -%}
            URLAUTHRSTTHD={{item.URLAUTHRSTTHD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 //配置拨测用户调度到同一个POD。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
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
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 //配置直播的域名标识，开启直播预取功能（全流回源时长10s，子流回源时长50s）。

```jinja2
{%- for item in set_softpara_list_1 -%}
    SET SOFTPARA:
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
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT2={{item.DT2}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT2=BYTE 时必选 --- -#}
    {%- if item.DT2 == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDPOSITION={{item.DWORDPOSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT2=DWORD 时必选 --- -#}
    {%- if item.DT2 == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 13 //配置DNS老化的TTL最小次数。

```jinja2
{%- for item in set_softpara_list_2 -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 14 //设置在网管上显示的UPF支持的可选服务类型。

```jinja2
{%- for item in set_upfservicetype_list -%}
    SET UPFSERVICETYPE:
    {#- --- 可选参数 --- -#}
    {%- if item.SERVICETYPE1 is not none -%}
        SERVICETYPE1="{{item.SERVICETYPE1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 15 //（条件必选）当网元与NWDAF对接上报保障用户或体验用户单据，需要用户单据携带媒体中继用户标识时，开启如下配置。

### 用户单据携带媒体中继用户标识，需要NWDAF升级到20.16.2后才能开启。

```jinja2
{%- if is_scenario_nwdaf_media_relay_flag -%}
    {%- for item in set_vvipextrpt_list -%}
        SET VVIPEXTRPT:
        {#- --- 可选参数 --- -#}
        {%- if item.MEDIARELAYSW is not none -%}
            MEDIARELAYSW={{item.MEDIARELAYSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_nwdaf_media_relay_flag -%}
    {%- for item in set_expextrpt_list -%}
        SET EXPEXTRPT:
        {#- --- 可选参数 --- -#}
        {%- if item.MEDIARELAYSW is not none -%}
            MEDIARELAYSW={{item.MEDIARELAYSW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

