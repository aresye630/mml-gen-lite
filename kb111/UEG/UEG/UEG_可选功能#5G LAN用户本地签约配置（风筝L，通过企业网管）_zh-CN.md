---
id: ''
name: 5G LAN用户本地签约配置（风筝L，通过企业网管）
ne_type: UEG
type: feature
description: 企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。  产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需要灵活调整时，可通过企业网管调整用户所属的5G LAN组。  通过基于华为API文档开发的企业网管调整用户所属的5G LAN组时，还需要提前在UEG（风筝L）上完成本页面的配置。  * 本章节描述的5G LAN用户本地签约配置，指的仅是调整5G LAN用户本地所属的5G LAN组ID，不包括其他参数调整。 * 开启5G LAN用5G户本地签约功能后，5G LAN用户本地签约的5G LAN组ID，优先级高于UDM上开户时签约的5G LAN组ID。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","5G LAN用户本地签约配置（风筝L，通过企业网管）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD MEPTLSPARA')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
企业产线部署5G LAN业务后，存在根据业务实际需要，灵活调整CPE（5G模组）/5G LAN终端（5G模组）签约的5G LAN组的需求。产线需要灵活调整时，若仅依赖在UDM上修改5G LAN组签约数据，则存在申请周期较长等问题。故需要灵活调整时，可通过企业网管调整用户所属的5G LAN组。通过基于华为API文档开发的企业网管调整用户所属的5G LAN组时，还需要提前在UEG（风筝L）上完成本页面的配置。* 本章节描述的5G LAN用户本地签约配置，指的仅是调整5G LAN用户本地所属的5G LAN组ID，不包括其他参数调整。* 开启5G LAN用5G户本地签约功能后，5G LAN用户本地签约的5G LAN组ID，优先级高于UDM上开户时签约的5G LAN组ID。

## 必备事项
前提条件

* 操作员拥有配置权限。
* 5G LAN业务已交付且运行正常。
* 5G LAN用户在UDM上已完成5G LAN组签约，且存在调整所属5G LAN组的诉求。
* CA证书和设备证书需要客户提前申请，申请操作请参考 风筝L的“证书获取与申请”章节。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_mpflogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置NGVN逻辑接口名称。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口”。'
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
          description: '配置IPv4类型的逻辑接口。  接口支持IPv4v6双栈，此处以IPv4单栈为例。  容灾关系的两个UPF，该IP必须不同。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: '逻辑接口的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口IP”。'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '此处复用N6接口的VPN实例，可以使用**LST VPNINST**命令进行查询。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
          pattern: ''
          default: ''
    add_meptlspara_list:
      type: items
      properties:
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '本端规划，存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: 'TLS协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '校验对端证书'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '此处以开启UPF的TLS证书鉴权功能为例。  不开启时，设置为“DISABLE”。  对端不支持携带证书时，设置为“DISABLE”。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VERIFYDEPTH:
          name: '校验深度'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DEVCERTSCENE:
          name: '设备证书场景'
          type: string
          enum:
          - INNER_DEV_CERT_SCENE
          - LE_DEV_CERT_SCENE
          - MP1_DEV_CERT_SCENE
          - MP2_DEV_CERT_SCENE
          - NOTIFY_EXTNE_DEV_CERT_SCENE
          - UAC_DEV_CERT_SCENE
          - NGVN_DEV_CERT_SCENE
          required: true
          description: '关联CSP Portal在“API网关NGVN设备证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CIPHERSUITES:
          name: 'TLS算法套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CACERTSCENE:
          name: 'CA证书场景'
          type: string
          enum:
          - INNER_CA_CERT_SCENE
          - LE_CA_CERT_SCENE
          - MP1_CA_CERT_SCENE
          - MP2_CA_CERT_SCENE
          - NOTIFY_EXTNE_CA_CERT_SCENE
          - UAC_CA_CERT_SCENE
          - NGVN_CA_CERT_SCENE
          required: false
          description: '“校验对端证书（VERIFYPEER）”设置为“ENABLE”时，需要规划CA证书，否则不需要。  关联CSP Portal在“API网关NGVN接口CA证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_mepservercommpara_list:
      type: items
      properties:
        PARANAME:
          name: 'HTTP服务端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通信参数推荐采用默认值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITREQHEADERTIMEOUT:
          name: '读取客户端请求头超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        WAITREQBODYTIMEOUT:
          name: '读取客户端请求体超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        SENDRSPTIMEOUT:
          name: '向客户端发送响应超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        KEEPALIVETIMEOUT:
          name: '连接保活超时时间'
          type: integer
          minimum: 1
          maximum: 7200
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 75
        KEEPALIVEMAXREQNUM:
          name: '保活连接可处理的最大请求数'
          type: integer
          minimum: 1
          maximum: 100000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 1000
    add_meptlspara_list_1:
      type: items
      properties:
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '本端规划，存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: 'TLS协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '校验对端证书'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '此处以开启UPF的TLS证书鉴权功能为例。  不开启时，设置为“DISABLE”。  对端不支持携带证书时，设置为“DISABLE”。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VERIFYDEPTH:
          name: '校验深度'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DEVCERTSCENE:
          name: '设备证书场景'
          type: string
          enum:
          - INNER_DEV_CERT_SCENE
          - LE_DEV_CERT_SCENE
          - MP1_DEV_CERT_SCENE
          - MP2_DEV_CERT_SCENE
          - NOTIFY_EXTNE_DEV_CERT_SCENE
          - UAC_DEV_CERT_SCENE
          - NGVN_DEV_CERT_SCENE
          required: true
          description: '关联CSP Portal在“API网关NGVN设备证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CIPHERSUITES:
          name: 'TLS算法套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CACERTSCENE:
          name: 'CA证书场景'
          type: string
          enum:
          - INNER_CA_CERT_SCENE
          - LE_CA_CERT_SCENE
          - MP1_CA_CERT_SCENE
          - MP2_CA_CERT_SCENE
          - NOTIFY_EXTNE_CA_CERT_SCENE
          - UAC_CA_CERT_SCENE
          - NGVN_CA_CERT_SCENE
          required: false
          description: '“校验对端证书（VERIFYPEER）”设置为“ENABLE”时，需要规划CA证书，否则不需要。  关联CSP Portal在“API网关NGVN接口CA证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_mepclientcommpara_list:
      type: items
      properties:
        PARANAME:
          name: 'HTTP客户端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通信参数推荐采用默认值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONNTIMEOUT:
          name: '与服务端建立连接超时时间'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        SENDREQTIMEOUT:
          name: '发送请求超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        WAITRSPTIMEOUT:
          name: '读取服务端响应超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
    add_mephttpservergrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'MEP HTTP服务端组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mephttpserver_list:
      type: items
      properties:
        SERVERNAME:
          name: 'MEP HTTP服务端名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPSERVERGRP:
          name: 'MEP HTTP服务端组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定归属的HTTP服务端组，已通过**ADD MEPHTTPSERVERGRP**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: 'MEP HTTP服务端类型'
          type: string
          enum:
          - FOR_EXTERNAL_NE
          - FOR_INTERNAL_NOTIFY_MES
          - FOR_INTERNAL_POLICY_MES
          required: true
          description: '用于指定UEG作为服务端向APP转发消息，选择“FOR\_EXTERNAL\_NE”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '使用NGVN接口IP地址，已通过**ADD MPFLOGICINF**命令配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '必须启用TLS证书鉴权。'
          data_source: '固定取值'
          pattern: ''
          default: ENABLE
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于指定使用的TLS证书，已通过**ADD MEPTLSPARA**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERCOMMPARANAME:
          name: 'HTTP服务端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '采用  **ADD MEPSERVERCOMMPARA**  命令配置的“HTTP服务端通信参数名称”参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mephttpclientgrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'MEP HTTP客户端组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mephttpclient_list:
      type: items
      properties:
        CLIENTNAME:
          name: 'MEP HTTP客户端名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPCLIENTGRP:
          name: 'MEP HTTP客户端组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定归属的HTTP客户端组，已通过**ADD MEPHTTPCLIENTGRP**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTTYPE:
          name: 'MEP HTTP客户单类型'
          type: string
          enum:
          - TO_CONNECT_EXTERNAL_NE
          - TO_CONNECT_INTERNAL_MES
          required: true
          description: '用于指定UEG作为客户端接收APP消息，选择“FOR\_EXTERNAL\_NE”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '使用NGVN接口IP地址，已通过**ADD MPFLOGICINF**命令配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '必须启用TLS证书鉴权。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于指定使用的TLS证书，已通过**ADD MEPTLSPARA**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTCOMMPARANAME:
          name: 'HTTP客户端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '采用**ADD MEPCLIENTCOMMPARA**命令配置的“HTTP客户端通信参数名称”参数值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERSERVICETAG:
          name: '对端服务标签'
          type: string
          enum:
          - LESERVICE
          - MEPSERVICE
          - MM5SERVICE
          - MP1SERVICE
          - MP2SERVICE
          - NGVNSERVICE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: MP1SERVICE
    add_mepreverseproxy_list:
      type: items
      properties:
        PROXYNAME:
          name: '反向代理名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPSERVERGRP:
          name: 'HTTP服务端索引组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD MEPHTTPSERVERGRP**命令配置的“MEP HTTP服务端组名称”参数值。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MEPHTTPCLIENTGRP:
          name: 'HTTP客户端索引组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '采用**ADD MEPHTTPCLIENTGRP**命令配置的“MEP HTTP客户端组名称”参数值。'
          data_source: '已配置数据中获取'
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
    set_apiauth_list:
      type: items
      properties:
        ISAUTH:
          name: '鉴权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_mepauthmode_list:
      type: items
      properties:
        AUTHMODE:
          name: '授权模式'
          type: string
          enum:
          - BYAPPD
          - BYLOCALPARA
          - BYMM5PARA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_authservlist_list:
      type: items
      properties:
        NAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_authserv_list:
      type: items
      properties:
        SERVICENAME:
          name: '授权服务名称'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICELISTNAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHVALIDTIME:
          name: '授权有效时间的截止时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'YYYY&MM&DD&HH&NN&SS'
    add_appauthinfo_list:
      type: items
      properties:
        APPID:
          name: 'APP标识'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APIKEY:
          name: 'APP访问凭证'
          type: string
          minLength: 0
          maxLength: 60
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVICELISTNAME:
          name: '授权服务列表名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_edgesmcommfunc_list:
      type: items
      properties:
        LOCVNSUBSW:
          name: '5G LAN本地签约功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'UEG支持本地调整5G LAN组ID时必须使用样例值。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_edgelocsubngvn_list:
      type: items
      properties:
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: '调整前的5G LAN组ID。即哪些5G LAN组用户允许本地调整归属的5G LAN组ID。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'DNN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '允许本地调整5G LAN组ID的用户签约的APN。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        GROUPNAME:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '5G LAN组ID的描述信息，方便识别5G LAN组属性。'
          data_source: '本地规划'
          pattern: ''
          default: ''
  examples:
    add_mpflogicinf_list:
    - NAME: 'ngvnif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS: '10.1.7.111'
      VPNINSTANCE: 'VRF_LocalDN'
    add_meptlspara_list:
    - TLSPARANAME: 'tls01-server5glan'
      PROTOCOL: TLSv12-1&TLSv13-1
      VERIFYPEER: ENABLE
      VERIFYDEPTH: 10
      DEVCERTSCENE: NGVN_DEV_CERT_SCENE
      CIPHERSUITES: TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1
      CACERTSCENE: NGVN_CA_CERT_SCENE
    add_mepservercommpara_list:
    - PARANAME: 'DefaultServerPara5GLAN'
      WAITREQHEADERTIMEOUT: 60
      WAITREQBODYTIMEOUT: 60
      SENDRSPTIMEOUT: 60
      KEEPALIVETIMEOUT: 75
      KEEPALIVEMAXREQNUM: 1000
    add_meptlspara_list_1:
    - TLSPARANAME: 'tls01-client5glan'
      PROTOCOL: TLSv12-1&TLSv13-1
      VERIFYPEER: ENABLE
      VERIFYDEPTH: 10
      DEVCERTSCENE: NGVN_DEV_CERT_SCENE
      CIPHERSUITES: TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1
      CACERTSCENE: NGVN_CA_CERT_SCENE
    add_mepclientcommpara_list:
    - PARANAME: 'DefaultClientPara5GLAN'
      CONNTIMEOUT: 60
      SENDREQTIMEOUT: 60
      WAITRSPTIMEOUT: 60
    add_mephttpservergrp_list:
    - GROUPNAME: 'servergrp01'
    add_mephttpserver_list:
    - SERVERNAME: 'ngvn-extNE'
      MEPHTTPSERVERGRP: 'servergrp01'
      SERVERTYPE: FOR_EXTERNAL_NE
      IPV4: '10.1.7.111'
      PORT: 8443
      TLSFLG: ENABLE
      TLSPARANAME: 'tls01-server5glan'
      SERVERCOMMPARANAME: 'DefaultServerPara5GLAN'
    add_mephttpclientgrp_list:
    - GROUPNAME: 'clientgrp01'
    add_mephttpclient_list:
    - CLIENTNAME: 'ngvn-extNE'
      MEPHTTPCLIENTGRP: 'clientgrp01'
      CLIENTTYPE: TO_CONNECT_EXTERNAL_NE
      IPV4: '10.1.7.111'
      TLSFLG: ENABLE
      TLSPARANAME: 'tls01-client5glan'
      CLIENTCOMMPARANAME: 'DefaultClientPara5GLAN'
      PEERSERVICETAG: MEPSERVICE
    add_mepreverseproxy_list:
    - PROXYNAME: 'proxy_5glan01'
      MEPHTTPSERVERGRP: 'servergrp01'
      MEPHTTPCLIENTGRP: 'clientgrp01'
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5APIG01'
      SWITCH: ENABLE
    set_apiauth_list:
    - ISAUTH: ENABLE
    set_mepauthmode_list:
    - AUTHMODE: BYLOCALPARA
    add_authservlist_list:
    - NAME: 'serviceList'
    add_authserv_list:
    - SERVICENAME: 'AseMaster'
      SERVICELISTNAME: 'serviceList'
      AUTHVALIDTIME: '2022&01&13&11&02&59'
    add_appauthinfo_list:
    - APPID: 'appid_123'
      APIKEY: '*****'
      SERVICELISTNAME: 'serviceList'
    set_edgesmcommfunc_list:
    - LOCVNSUBSW: ENABLE
    add_edgelocsubngvn_list:
    - GROUPID: '000003e9-460-08-01'
      APN: 'dnn5glan01'
      GROUPNAME: '5GLAN_for_localsub01'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录OM Portal。

### 2 进入“MML命令行-UEG”窗口。

### 3 执行**ADD MPFLOGICINF**命令，配置NGVN逻辑接口。

```jinja2
{%- for item in add_mpflogicinf_list -%}
    ADD MPFLOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置TLS参数（TLS协议版本、算法套件、证书）。

#### 4.1 //作为服务端：

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_meptlspara_list -%}
        ADD MEPTLSPARA:
        {#- --- 必选参数 --- -#}
        TLSPARANAME="{{item.TLSPARANAME}}",
        PROTOCOL={{item.PROTOCOL}},
        VERIFYPEER={{item.VERIFYPEER}},
        DEVCERTSCENE={{item.DEVCERTSCENE}},
        CIPHERSUITES={{item.CIPHERSUITES}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
        {%- if item.VERIFYPEER == 'ENABLE' -%}
            VERIFYDEPTH={{item.VERIFYDEPTH}},
        {%- endif -%}
        {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
        {%- if item.VERIFYPEER == 'ENABLE' -%}
            CACERTSCENE={{item.CACERTSCENE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_mepservercommpara_list -%}
        ADD MEPSERVERCOMMPARA:
        {#- --- 必选参数 --- -#}
        PARANAME="{{item.PARANAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.WAITREQHEADERTIMEOUT is not none -%}
            WAITREQHEADERTIMEOUT={{item.WAITREQHEADERTIMEOUT}},
        {%- endif -%}
        {%- if item.WAITREQBODYTIMEOUT is not none -%}
            WAITREQBODYTIMEOUT={{item.WAITREQBODYTIMEOUT}},
        {%- endif -%}
        {%- if item.SENDRSPTIMEOUT is not none -%}
            SENDRSPTIMEOUT={{item.SENDRSPTIMEOUT}},
        {%- endif -%}
        {%- if item.KEEPALIVETIMEOUT is not none -%}
            KEEPALIVETIMEOUT={{item.KEEPALIVETIMEOUT}},
        {%- endif -%}
        {%- if item.KEEPALIVEMAXREQNUM is not none -%}
            KEEPALIVEMAXREQNUM={{item.KEEPALIVEMAXREQNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 //作为客户端

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_meptlspara_list_1 -%}
        ADD MEPTLSPARA:
        {#- --- 必选参数 --- -#}
        TLSPARANAME="{{item.TLSPARANAME}}",
        PROTOCOL={{item.PROTOCOL}},
        VERIFYPEER={{item.VERIFYPEER}},
        DEVCERTSCENE={{item.DEVCERTSCENE}},
        CIPHERSUITES={{item.CIPHERSUITES}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
        {%- if item.VERIFYPEER == 'ENABLE' -%}
            VERIFYDEPTH={{item.VERIFYDEPTH}},
        {%- endif -%}
        {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
        {%- if item.VERIFYPEER == 'ENABLE' -%}
            CACERTSCENE={{item.CACERTSCENE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_mepclientcommpara_list -%}
        ADD MEPCLIENTCOMMPARA:
        {#- --- 必选参数 --- -#}
        PARANAME="{{item.PARANAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CONNTIMEOUT is not none -%}
            CONNTIMEOUT={{item.CONNTIMEOUT}},
        {%- endif -%}
        {%- if item.SENDREQTIMEOUT is not none -%}
            SENDREQTIMEOUT={{item.SENDREQTIMEOUT}},
        {%- endif -%}
        {%- if item.WAITRSPTIMEOUT is not none -%}
            WAITRSPTIMEOUT={{item.WAITRSPTIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加MEP HTTP服务端组及MEP HTTP服务端。

```jinja2
{%- for item in add_mephttpservergrp_list -%}
    ADD MEPHTTPSERVERGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mephttpserver_list -%}
    ADD MEPHTTPSERVER:
    {#- --- 必选参数 --- -#}
    SERVERNAME="{{item.SERVERNAME}}",
    MEPHTTPSERVERGRP="{{item.MEPHTTPSERVERGRP}}",
    SERVERTYPE={{item.SERVERTYPE}},
    TLSFLG={{item.TLSFLG}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4 is not none -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.SERVERCOMMPARANAME is not none -%}
        SERVERCOMMPARANAME="{{item.SERVERCOMMPARANAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TLSFLG=ENABLE 时必选 --- -#}
    {%- if item.TLSFLG == 'ENABLE' -%}
        TLSPARANAME="{{item.TLSPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加MEP HTTP客户端组及MEP HTTP客户端。

```jinja2
{%- for item in add_mephttpclientgrp_list -%}
    ADD MEPHTTPCLIENTGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mephttpclient_list -%}
    ADD MEPHTTPCLIENT:
    {#- --- 必选参数 --- -#}
    CLIENTNAME="{{item.CLIENTNAME}}",
    MEPHTTPCLIENTGRP="{{item.MEPHTTPCLIENTGRP}}",
    CLIENTTYPE={{item.CLIENTTYPE}},
    TLSFLG={{item.TLSFLG}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4 is not none -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {%- if item.CLIENTCOMMPARANAME is not none -%}
        CLIENTCOMMPARANAME="{{item.CLIENTCOMMPARANAME}}",
    {%- endif -%}
    {%- if item.PEERSERVICETAG is not none -%}
        PEERSERVICETAG={{item.PEERSERVICETAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TLSFLG=ENABLE 时必选 --- -#}
    {%- if item.TLSFLG == 'ENABLE' -%}
        TLSPARANAME="{{item.TLSPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 增加反向代理配置。“校验对端证书（VERIFYPEER）”设置为“ENABLE”时需要配置，否则请跳过本配置。

```jinja2
{%- set ADD_MEPTLSPARA=getParameterValue('ADD MEPTLSPARA') -%}
{%- if ADD_MEPTLSPARA -%}
    {%- for item in add_mepreverseproxy_list -%}
        ADD MEPREVERSEPROXY:
        {#- --- 必选参数 --- -#}
        PROXYNAME="{{item.PROXYNAME}}",
        MEPHTTPSERVERGRP="{{item.MEPHTTPSERVERGRP}}",
        MEPHTTPCLIENTGRP="{{item.MEPHTTPCLIENTGRP}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 激活支持认证鉴权License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 9 打开Oauth2.0鉴权。

#### 9.1 //“SERVICENAME”参数值通过**DSP MECSERVICE**命令查询获取。

```jinja2
{%- for item in set_apiauth_list -%}
    SET APIAUTH:
    {#- --- 必选参数 --- -#}
    ISAUTH={{item.ISAUTH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_mepauthmode_list -%}
    SET MEPAUTHMODE:
    {#- --- 必选参数 --- -#}
    AUTHMODE={{item.AUTHMODE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_authservlist_list -%}
    ADD AUTHSERVLIST:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_authserv_list -%}
    ADD AUTHSERV:
    {#- --- 必选参数 --- -#}
    SERVICENAME="{{item.SERVICENAME}}",
    SERVICELISTNAME="{{item.SERVICELISTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHVALIDTIME is not none -%}
        AUTHVALIDTIME={{item.AUTHVALIDTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_appauthinfo_list -%}
    ADD APPAUTHINFO:
    {#- --- 必选参数 --- -#}
    APPID="{{item.APPID}}",
    APIKEY="{{item.APIKEY}}",
    SERVICELISTNAME="{{item.SERVICELISTNAME}}",
    ;
{%- endfor -%}
```

### 10 执行**SET EDGESMCOMMFUNC**命令，开启5G LAN用户本地签约功能。

```jinja2
{%- for item in set_edgesmcommfunc_list -%}
    SET EDGESMCOMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.LOCVNSUBSW is not none -%}
        LOCVNSUBSW={{item.LOCVNSUBSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 调整5G LAN用户本地签约的5G LAN组ID后，运营商可通过**LST RDSSTATICIPPARA**查询多个用户本地签约的5G LAN组ID。

### 11 执行**ADD EDGELOCSUBNGVN**命令，配置支持本地签约的5G LAN组。

```jinja2
{%- for item in add_edgelocsubngvn_list -%}
    ADD EDGELOCSUBNGVN:
    {#- --- 必选参数 --- -#}
    GROUPID="{{item.GROUPID}}",
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPNAME is not none -%}
        GROUPNAME="{{item.GROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

