---
id: ''
name: 配置到CHF的数据（GGSN/PGW-C/SMF）
ne_type: UNC
type: feature
description: 当运营商网络完成了融合计费接口改造，网络中部署了CHF/NCG，UNC与CHF/NCG对接实现对用户实现融合计费时，需要配置N40接口与CHF/NCG对接。  **图1** 服务化接口协议栈图  N40接口是服务化接口，服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  **配置建议**  * GGSN/PGW-C/SMF的服务化接口业务IP地址不能和GGSN/PGW-C/SMF其他接口业务IP地址共用。 * GGSN/PGW-C/SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置SMF&PGW-C&SGW-C&GGSN","公共配置","配置到计费系统和策略控制网元的对接（Ga/Gy/N40/Gx/N7）","配置到CHF的数据（GGSN/PGW-C/SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商网络完成了融合计费接口改造，网络中部署了CHF/NCG，UNC与CHF/NCG对接实现对用户实现融合计费时，需要配置N40接口与CHF/NCG对接。**图1** 服务化接口协议栈图N40接口是服务化接口，服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。**配置建议*** GGSN/PGW-C/SMF的服务化接口业务IP地址不能和GGSN/PGW-C/SMF其他接口业务IP地址共用。* GGSN/PGW-C/SMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81202714 LKV2V6IF01 逻辑接口支持IPv6”。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: '配置GGSN/PGW-C/SMF到CHF/NCG的N40接口逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          description: '配置N40接口的HTTP本端端点组信息。'
          data_source: '本端规划'
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
          description: '配置HTTP本端端点信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: '-'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '全网规划'
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '配置本端服务化接口接入点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HttpLEGRP索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
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
          description: '-'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERSERVICE:
          name: '目的NF服务'
          type: string
          enum:
          - Nchf_ConvCharg
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
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
    set_httpconf_list:
      type: items
      properties:
        SERVERRCVBDTMT:
          name: '服务端接收HTTP请求消息体超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: '配置HTTP协议层的属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERSNDRSPTMT:
          name: '服务端回复HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXBODYSIZE:
          name: '最大消息体大小(MBytes)'
          type: integer
          minimum: 2
          maximum: 16
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAXJSONLEAFNUM:
          name: 'JSON数据最多叶子节点个数'
          type: integer
          minimum: 16000
          maximum: 512000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tnfins_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '配置主备CHF实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
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
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_tnfinsip_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置CHF组。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tnfbindgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '将CHF实例绑定到CHF组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_glbdftchfgroup_list:
      type: items
      properties:
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置全局默认CHF组，避免出现选择不到CHF组的情况。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selectchfgbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '配置基于计费属性选择CHF。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selchfgbimsiseg_list:
      type: items
      properties:
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '配置基于号段选择CHF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
    add_pnfgpsi_list:
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
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 64
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
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.17.0.6'
      VPNINSTNAME: 'VRF_CHF'
      DESC: 'FOR Server SBI'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'SMF For CHF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.17.0.6'
      PORT: 8080
      VPNNAME: 'VRF_CHF'
      TLSFLG: NO
      DESC: 'SMF Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeSMF
      PEERNFTYPE: Nchf
      PEERSERVICE: Nchf_ConvCharg
      DESCRIPTION: 'SMF For CHF'
      CHFPEERNFTYPE: ''
    set_httpconf_list:
    - SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 15
      MAXJSONLEAFNUM: 100000
    add_tnfins_list:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
      FQDN: 'chf1.hw.com'
    add_tnfinsip_list:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfgrp_list:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    set_glbdftchfgroup_list:
    - PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup1'
    add_selectchfgbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x0800'
      MASK: '0xffff'
      PRIORITY: 2
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_selchfgbimsiseg_list:
    - SEGSTART: '12345678901'
      SEGEND: '12345678905'
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_pnfsupi_list:
    - INDEX: ''
      NFINSTANCEID: ''
      QUERYTYPE: ''
      PATTERN: ''
      RANGEEND: ''
      RANGESTART: ''
    add_pnfgpsi_list:
    - INDEX: ''
      NFINSTANCEID: ''
      QUERYTYPE: ''
      PATTERN: ''
      RANGEEND: ''
      RANGESTART: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加N40接口的IP地址。当需要通过FQDN信息获取其他NF的IP信息时，无需配置此步骤。

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

### 2 配置N40接口的HTTP本端端点组及其包含的分别作为HTTP服务的服务端和客户端的本端端点信息。

#### 2.1 配置HTTP本端端点组信息。

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

#### 2.2 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

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

### 3 配置N40接口接入点信息。

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
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERNFTYPE=Nchf 时可选 --- -#}
    {%- if item.PEERNFTYPE == 'Nchf' -%}
        {%- if item.PEERSERVICE is not none -%}
            PEERSERVICE={{item.PEERSERVICE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置HTTP属性。在超大报文场景下，可以通过合理设置接收HTTP响应/请求消息体的超时时间、HTTP响应/请求消息体的最大大小、请求消息中JSON数据的最大叶子节点个数等参数，避免发送/请求报文不完整，导致业务处理异常。

```jinja2
{%- for item in set_httpconf_list -%}
    SET HTTPCONF:
    {#- --- 可选参数 --- -#}
    {%- if item.SERVERRCVBDTMT is not none -%}
        SERVERRCVBDTMT={{item.SERVERRCVBDTMT}},
    {%- endif -%}
    {%- if item.SERVERSNDRSPTMT is not none -%}
        SERVERSNDRSPTMT={{item.SERVERSNDRSPTMT}},
    {%- endif -%}
    {%- if item.MAXBODYSIZE is not none -%}
        MAXBODYSIZE={{item.MAXBODYSIZE}},
    {%- endif -%}
    {%- if item.MAXJSONLEAFNUM is not none -%}
        MAXJSONLEAFNUM={{item.MAXJSONLEAFNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置CHF实例。

```jinja2
{%- for item in add_tnfins_list -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    {%- if item.FQDN is not none -%}
        FQDN="{{item.FQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置CHF实例IP。

```jinja2
{%- for item in add_tnfinsip_list -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置CHF组。

```jinja2
{%- for item in add_tnfgrp_list -%}
    ADD TNFGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFGRPNAME="{{item.TNFGRPNAME}}",
    ;
{%- endfor -%}
```

### 8 将CHF实例绑定到CHF组中。

```jinja2
{%- for item in add_tnfbindgrp_list -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

### 9 配置CHF选择策略。

#### 9.1 配置全局默认CHF组。建议配置全局默认组，避免出现选择不到CHF组的情况。

```jinja2
{%- for item in set_glbdftchfgroup_list -%}
    SET GLBDFTCHFGROUP:
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.2 配置基于计费属性选择CHF组。

```jinja2
{%- for item in add_selectchfgbycc_list -%}
    ADD SELECTCHFGBYCC:
    {#- --- 必选参数 --- -#}
    CCTYPE={{item.CCTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CCTYPE=VALUE 时必选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.3 配置基于号段选择CHF组。

```jinja2
{%- for item in add_selchfgbimsiseg_list -%}
    ADD SELCHFGBIMSISEG:
    {#- --- 必选参数 --- -#}
    SEGSTART="{{item.SEGSTART}}",
    SEGEND="{{item.SEGEND}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 9.4 基于NRF选择CHF，不需要专有配置。

#### 9.5 基于本地NRF配置选择CHF。

##### 9.5.1 选择支持特定SUPI的CHF：**ADD PNFSUPI**

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfsupi_list -%}
        ADD PNFSUPI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.5.2 选择支持特定GPSI的CHF：**ADD PNFGPSI**

```jinja2
{%- if is_scenario_nrf_not_deployed -%}
    {%- for item in add_pnfgpsi_list -%}
        ADD PNFGPSI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

