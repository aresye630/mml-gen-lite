---
id: ''
name: 配置NSSF服务化接口
ne_type: UNC
type: feature
description: '**接口介绍**  NSSF的服务化接口为Nnssf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。  **表1** 服务化接口与参考点模式对应关系  | 参考点 | 网元间的交互 | 服务化接口 | | --- | --- | --- | | N22 | AMF<->NSSF | Namf、Nnssf |  **图1** 服务化接口协议栈图  服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  **配置建议**  * NSSF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。'
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NSSF解决方案","NSSF功能部署","NSSF非容灾组网","NSSF配置","配置NSSF基本功能","配置NSSF服务化接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
**接口介绍**NSSF的服务化接口为Nnssf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。**表1** 服务化接口与参考点模式对应关系| 参考点 | 网元间的交互 | 服务化接口 || --- | --- | --- || N22 | AMF<->NSSF | Namf、Nnssf |**图1** 服务化接口协议栈图服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。**配置建议*** NSSF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见逻辑接口介绍。
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
          description: '配置Nnssf接口的逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 ->5G Core业务IP对接设计”。'
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
          description: '配置Nnssf接口的HTTP本端实体组及其包含的分别作为HTTP服务的服务端和客户端的本端实体信息。'
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
          description: '-'
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
          description: '配置Nnssf接入点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '全网规划'
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
          description: '-'
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
    set_httpconf_list:
      type: items
      properties:
        SERVERRCVBDTMT:
          name: '服务端接收HTTP请求消息体超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERSNDRSPTMT:
          name: '服务端回复HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXBODYSIZE:
          name: '最大消息体大小(MBytes)'
          type: integer
          minimum: 2
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXJSONLEAFNUM:
          name: 'JSON数据最多叶子节点个数'
          type: integer
          minimum: 16000
          maximum: 512000
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
          description: '配置NRF实例。'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置NRF的地址信息。'
          data_source: '参见“水平网设LLD文档 ->5G Core业务IP对接设计”。'
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
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'NRF的服务端地址信息。'
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'NRF的服务端端口信息。'
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
          description: '配置NRF协议参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 3
        HEARTBEATTIMER:
          name: '心跳时长'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
        LOADCARRYINHB:
          name: '心跳是否携带Load信息'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '与对端协商'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
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
          description: '配置NRF实例。'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置NRF的地址信息。'
          data_source: '参见“水平网设LLD文档 ->5G Core业务IP对接设计”。'
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
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'Ipv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'NRF的服务端地址信息。'
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'NRF的服务端端口信息。'
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
          description: '配置NRF协议参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
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
          data_source: '与对端协商'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ON
        HEARTBEATTIMER:
          name: '心跳时长'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 60
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
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '设置NSSF的NF认证功能的配置开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          description: '激活NF向NRF注册。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nssfsubtimer_list:
      type: items
      properties:
        NFTYPE:
          name: '网元类型'
          type: string
          enum:
          - AMF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBVALIDTIMER:
          name: '订阅有效时长(s)'
          type: integer
          minimum: 1
          maximum: 9223372036854775807
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR Server SBI'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NSSF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 8080
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NSSF Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNSSF
      DESCRIPTION: 'NSSF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_httpconf_list:
    - SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 15
      MAXJSONLEAFNUM: 100000
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
      HEARTBEATTIMER: 0
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
      IPV4ADDRESS: '172.26.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    add_nrfpara_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_1'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: ON
      OAUTH2SWITCH: OFF
      HEARTBEATTIMER: 0
    add_subcondition_list_1:
    - NFTYPE: NfAMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFANS01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'NSSF_Instance_0'
    set_nssfsubtimer_list:
    - NFTYPE: AMF
      SUBVALIDTIMER: 3600
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 **配置NSSF服务化接口数据**

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 **可选：**增加NSSF服务化接口的IP地址。

```jinja2
{%- if is_optional_add_ip_address -%}
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
{%- endif -%}
```

#### 1.3 配置NSSF服务化接口的HTTP信息。

##### 1.3.1 配置HTTP本端端点组信息。

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

##### 1.3.2 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

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

#### 1.4 配置NSSF服务化接口的接入点信息。

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

#### 1.5 **可选：**配置HTTP属性。在超大报文场景下，可以通过合理设置接收HTTP响应/请求消息体的超时时间、HTTP响应/请求消息体的最大大小、请求消息中JSON数据的最大叶子节点个数等参数，避免发送/请求报文不完整，导致业务处理异常。

```jinja2
{%- if is_optional_http_property -%}
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
{%- endif -%}
```

### 2 **可选：配置到NRF的数据**

### 如果运营商策略为AMF通过NRF发现和选择NSSF，需配置本步骤。否则，跳过本步骤。

#### 2.1 配置NRF信息。

```jinja2
{%- if is_optional_nrf_data -%}
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

#### 2.2 配置NRF的地址信息。

```jinja2
{%- if is_optional_nrf_data -%}
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

#### 2.3 **可选：**配置NRF协议参数。当开启订阅功能开关时，可以增加订阅条件。当目标NF触发订阅条件和通知事件时，NRF向源NF发送通知。

```jinja2
{%- if is_optional_nrf_data and is_optional_nrf_protocol_para -%}
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
        {%- if item.HEARTBEATTIMER is not none -%}
            HEARTBEATTIMER={{item.HEARTBEATTIMER}},
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
{%- if is_optional_nrf_data and is_optional_nrf_protocol_para -%}
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

#### 2.4 **可选：**当网络中规划了双主或者主备NRF时，需要配置本步骤。双主NRF场景下，NF对接的优先级高的NRF为本地DC的NRF；主备NRF场景下，NF对接的优先级高的NRF为主NRF。

```jinja2
{%- if is_optional_nrf_data and is_optional_dual_active_standby_nrf -%}
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
{%- if is_optional_nrf_data and is_optional_dual_active_standby_nrf -%}
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
{%- if is_optional_nrf_data and is_optional_dual_active_standby_nrf -%}
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
        {%- if item.HEARTBEATTIMER is not none -%}
            HEARTBEATTIMER={{item.HEARTBEATTIMER}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_nrf_data and is_optional_dual_active_standby_nrf -%}
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

##### 2.4.1 请保证已完成NF到双主或者主备NRF的路由数据配置。

##### 2.4.2 请提前规划**ADD NRFPARA**中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF对NRF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考WSFD-114002 NRF双活容灾特性概述中“原理概述”>“可靠性机制”小节。

#### 2.5 打开NSSF的NF认证功能的开关。

```jinja2
{%- if is_optional_nrf_data -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 激活NSSF向NRF注册。

```jinja2
{%- if is_optional_nrf_data -%}
    {%- for item in act_nfonline_list -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **配置订阅时长**

#### 3.1 配置AMF订阅NSSF切片可用性服务的有效期时长。

```jinja2
{%- for item in set_nssfsubtimer_list -%}
    SET NSSFSUBTIMER:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    SUBVALIDTIMER={{item.SUBVALIDTIMER}},
    ;
{%- endfor -%}
```

