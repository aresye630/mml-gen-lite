---
id: ''
name: NRF解决方案基本功能配置实例（NF注册/更新/去注册、NF订阅/通知）
ne_type: UNC
type: feature
description: NRF支持NF的自动注册、更新、去注册、NF订阅/通知。本章节介绍AMF如何通过配置实现到NRF的自动注册、更新、去注册、NF订阅/通知。  本章节只是举例重点介绍NF和NRF对接部署逻辑，具体各NF侧的详细配置详见各产品的“初始配置与调测”。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","4/5G融合部署","NRF单层非容灾组网","NRF解决方案基本功能配置实例（NF注册/更新/去注册、NF订阅/通知）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
NRF支持NF的自动注册、更新、去注册、NF订阅/通知。本章节介绍AMF如何通过配置实现到NRF的自动注册、更新、去注册、NF订阅/通知。本章节只是举例重点介绍NF和NRF对接部署逻辑，具体各NF侧的详细配置详见各产品的“初始配置与调测”。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 完成加载License。

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
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Nnrf接口的逻辑IP地址。'
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
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
          description: '配置Nnrf接口的HTTP本端端点组信息。'
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
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
    add_httple_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
          description: '配置Nnrf接入点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HttpLEGRP索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: ''
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
    set_httpconf_list:
      type: items
      properties:
        CLIENTRCVRSPTMT:
          name: '客户端接收HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_nrftimer_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - DEFAULT
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBTIMES:
          name: '心跳超时次数'
          type: integer
          minimum: 2
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEARTBEATTIMER:
          name: '心跳周期时长(秒)'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCVALIDTIMER:
          name: '服务发现缓存有效时长(秒)'
          type: integer
          minimum: 0
          maximum: 172800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBVALIDTIMER:
          name: '订阅有效时长(秒)'
          type: integer
          minimum: 1
          maximum: 604800
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
          description: '打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。'
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
    set_nrftakepararule_list:
      type: items
      properties:
        NFTYPE:
          name: '网元类型'
          type: string
          enum:
          - UDM
          - AMF
          - SMF
          - AUSF
          - PCF
          - UDR
          - BSF
          - CHF
          - CUSTOM_OCS
          - SMSF
          - NWDAF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOSEGGUARDSW:
          name: 'NF号段防呆开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOIPRANGESW:
          name: 'NF无IP处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOTAISW:
          name: 'NF无TAI处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MATCHALLSW:
          name: '全匹配开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REGUPDSW:
          name: '注册更新处理开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULE:
          name: '规则'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfimsdnn_list:
      type: items
      properties:
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sdrtrans_list:
      type: items
      properties:
        FLATTYPE:
          name: '通信平面类型'
          type: string
          enum:
          - BASE
          - FABRIC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TRANSABILITY:
          name: '传输能力类型'
          type: string
          enum:
          - RELIABILITY
          - SECURITY
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OPT:
          name: '选项开关'
          type: string
          enum:
          - DISABLEALL
          - ENABLEALL
          - NOTSET
          required: true
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
          description: '配置NRF协议参数。'
          data_source: ''
          pattern: ''
          default: ''
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
    add_ngmno_list_1:
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
    add_nghplmn_list_1:
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
    add_nfuuid_list_1:
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
    add_logicip_list_2:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Nnrf接口的逻辑IP地址。'
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
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
    add_httplegrp_list_1:
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
    add_httple_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
    add_sbiaple_list_1:
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
          description: '配置NRF信息。'
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。  全网规划'
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
          description: '配置NRF的地址信息。'
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
          description: '配置NRF协议参数。'
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
    set_licenseswitch_list_1:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。'
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
          description: '激活AMF向NRF注册。'
          data_source: ''
          pattern: ''
          default: ''
    add_nrfpara_list_2:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF协议参数。'
          data_source: ''
          pattern: ''
          default: ''
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
    add_gtpclegrp_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '配置N26接口数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: '本端规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_n26mmechar_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - SPECIAL_MME
          - COMB_MME
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
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
          name: 'MME IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV4:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMECAP:
          name: 'MME能力'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'MME IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKV6:
          name: 'IPv6子网前缀长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmmsubdata_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATRESTRICT:
          name: 'RAT限制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CORERESTRICT:
          name: '核心网类型限制'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCS:
          name: 'MCS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPS:
          name: 'MPS'
          type: string
          enum:
          - NOT_SUPPORT
          - SUPPORT
          - 'NULL'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'NULL'
        MPSMCSPRI:
          name: 'MPSMCS优先级'
          type: string
          enum:
          - CFG_FIRST
          - SUB_FIRST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CFG_FIRST
    add_ngmno_list_2:
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
    add_nghplmn_list_2:
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
    add_ngsrvplmn_list_1:
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
    add_plmnns_list_1:
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
    add_nfuuid_list_2:
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
    add_nfprofile_list_1:
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
    add_smfinfo_list:
      type: items
      properties:
        SMFINSTANCENAME:
          name: 'SMF实例名称'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFNAME:
          name: 'SMF名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWFQDN:
          name: 'PGW名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfservice_list_4:
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
    add_nfservicever_list_4:
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
    add_nfns_list_1:
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nsdnn_list:
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
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicip_list_5:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Nnrf接口的逻辑IP地址。'
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
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
    add_httplegrp_list_2:
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
    add_httple_list_4:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
    add_sbiaple_list_2:
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
    add_nrf_list_1:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF信息。'
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
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          name: '端口'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'NRF的服务端端口信息。'
          data_source: '全网规划'
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
    add_nrfpara_list_3:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '配置NRF协议参数。'
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
    set_licenseswitch_list_2:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '设置License配置开关**。**'
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
    act_nfonline_list_1:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'NF实例名称'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '激活SMF\_Instance\_0向NRF的注册。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gtpclegrp_list_1:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '配置S11/S5/S8-C接口数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_gtpclegrpmem_list_1:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
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
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: '本端规划'
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
    add_gtpcintf_list_1:
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        EBID:
          name: 'SMF是否支持向AMF分配EBID'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngmno_list_3:
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
    add_nghplmn_list_3:
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
    add_nfuuid_list_3:
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
    add_logicip_list_10:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置Nnrf接口的逻辑IP地址。'
          data_source: '参见“垂直网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
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
    add_httplegrp_list_3:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '配置Nnrf接口的HTTP本端端点组信息。'
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
    add_httple_list_6:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
    add_httple_list_7:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
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
          description: '-'
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
    add_sbiaple_list_3:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置Nnrf接入点信息。'
          data_source: ''
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HttpLEGRP索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: ''
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
    set_httpconf_list_2:
      type: items
      properties:
        CLIENTRCVRSPTMT:
          name: '客户端接收HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_nrftimer_list_2:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - DEFAULT
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HBTIMES:
          name: '心跳超时次数'
          type: integer
          minimum: 2
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEARTBEATTIMER:
          name: '心跳周期时长(秒)'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DISCVALIDTIMER:
          name: '服务发现缓存有效时长(秒)'
          type: integer
          minimum: 0
          maximum: 172800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBVALIDTIMER:
          name: '订阅有效时长(秒)'
          type: integer
          minimum: 1
          maximum: 604800
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nfgroup_list:
      type: items
      properties:
        NFGROUPID:
          name: 'NF实例组标识'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NRF
          - UDM
          - AMF
          - SMF
          - AUSF
          - NEF
          - PCF
          - SMSF
          - NSSF
          - UDR
          - LMF
          - GMLC
          - EIR_5G
          - SEPP
          - UPF
          - N3IWF
          - AF
          - UDSF
          - BSF
          - CHF
          - NWDAF
          - CUSTOM_OCS
          - SCP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GROUPDESC:
          name: 'NF实例组描述'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nfgroupmem_list:
      type: items
      properties:
        NFGROUPID:
          name: 'NF组标识'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 40
          required: true
          description: '* 此部分数据**可选**，运营商可能在NF注册时已经规划了对应的groupId并随注册上报到NRF，此时NF组与NF成员的关系自动对应，不需要再在NF组中重复添加NF实例。 * 号段NF的NF实例标识，可以在各NF上通过**LST NFUUID**命令查询获取。对于NRF而言，NF归属于哪个NF组，每个NF组支持的号段信息是统一通过全网规划获取的。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nfroutingind_list:
      type: items
      properties:
        NFGROUPID:
          name: 'NF组标识'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: 'NF组标识已通过**ADD NFGROUP**配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ROUTINGIND:
          name: '选路指示器'
          type: string
          minLength: 1
          maxLength: 4
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nfimsi_list:
      type: items
      properties:
        NFGROUPID:
          name: 'NF组标识'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: 'NF组标识已通过**ADD NFGROUP**配置。  说明：  IMSI号段为15位，如果配置的起始、结束字符串长度不足15位，则系统自动在起始字符串后面补0，结束字符串后面补9，补齐到15位。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
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
    syn_acspeercfg_list:
      type: items
      properties:
        OPERTYPE:
          name: '操作类型'
          type: string
          enum:
          - start
          - stop
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: start
        SYNSCOPE:
          name: '同步范围'
          type: string
          enum:
          - all
          - servicename
          - servicename_instanceid
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: all
        SERVICENAME:
          name: '服务名称'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SYNMODE:
          name: '同步方式'
          type: string
          enum:
          - incremental
          - full
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: incremental
        INSTANCEID:
          name: '实例ID'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    syn_acspeercfg_list_1:
      type: items
      properties:
        OPERTYPE:
          name: '操作类型'
          type: string
          enum:
          - start
          - stop
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: start
        SYNSCOPE:
          name: '同步范围'
          type: string
          enum:
          - all
          - servicename
          - servicename_instanceid
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: all
        SERVICENAME:
          name: '服务名称'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SYNMODE:
          name: '同步方式'
          type: string
          enum:
          - incremental
          - full
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: incremental
        INSTANCEID:
          name: '实例ID'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_nfuuid_list:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_INSTANCE_0'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 8080
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_1:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.16.0.8'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_httpconf_list:
    - CLIENTRCVRSPTMT: 15
      SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 10
      MAXJSONLEAFNUM: 100000
    set_nrftimer_list:
    - NFTYPE: AMF
      HBTIMES: 3
      HEARTBEATTIMER: 5
      DISCVALIDTIMER: 86400
      SUBVALIDTIMER: 86400
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    set_nrftakepararule_list:
    - NFTYPE: UDM
      NOSEGGUARDSW: FUNC_ON
      NOIPRANGESW: ''
      NOTAISW: ''
      MATCHALLSW: ''
      REGUPDSW: ''
      RULE: ''
    add_nrfimsdnn_list:
    - DNN: 'huawei.com'
    set_sdrtrans_list:
    - FLATTYPE: FABRIC
      TRANSABILITY: RELIABILITY
      OPT: NOTSET
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      SUBSCRISWITCH: ON
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      OAUTH2SWITCH: OFF
    add_ngmno_list_1:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_1:
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
    add_nfuuid_list_1:
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
    add_logicip_list_2:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.1.4'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.154.24'
      VPNINSTNAME: '_public_'
      DESC: 'FOR N26'
      IPV4MTU: ''
      IPV6MTU: ''
      LOGICIPV6: ''
    add_httplegrp_list_1:
    - INDEX: 1
      DESC: 'AMF'
    add_httple_list_2:
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
    add_sbiaple_list_1:
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
    add_nrfpara_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
    add_nrfpara_list_2:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      SUBSCRISWITCH: ON
    add_subcondition_list:
    - NFTYPE: NfSMF
      CONDITION: NfInstanceId-1
      REQNOTIFEVENT: NF_REGISTERED-1
    add_gtpclegrp_list:
    - GROUPID: 3
      DESC: 'n26'
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
    add_n26mmechar_list:
    - RANGE: SPECIAL_MME
      IPTYPE: IPV4
      IPV4: '172.16.0.6'
      MASKV4: '255.255.255.255'
      MMECAP: NONIPPDN
      IPV6: ''
      MASKV6: ''
    add_ngmmsubdata_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      RATRESTRICT: EUTRA-1
      CORERESTRICT: EPC-1
      IMSI: ''
      MCS: 'NULL'
      MPS: 'NULL'
      MPSMCSPRI: CFG_FIRST
    add_ngmno_list_2:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_2:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_ngsrvplmn_list_1:
    - PLMNIDX: 0
      NOID: 0
      MCC: '123'
      MNC: '03'
    add_plmnns_list_1:
    - NSIDX: 0
      PLMNIDX: 0
      SST: 1
      SD: '010101'
    add_nfuuid_list_2:
    - NFTYPE: NfSMF
      NFINSTANCENAME: 'SMF_Instance_0'
    add_nfprofile_list_1:
    - NFINSTANCENAME: 'SMF_Instance_0'
      NFTYPE: NfSMF
      NFSTATUS: Registered
    add_smfinfo_list:
    - SMFINSTANCENAME: 'SMF_Instance_0'
      SMFNAME: 'SMF01'
      PGWFQDN: 'HUAWEI1.COM.APN.EPC.MNC003.MCC123.3GPPNETWORK.ORG'
    add_nfservice_list_4:
    - NFINSTANCENAME: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
    add_nfservicever_list_4:
    - NFINSTANCENAME: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      APIFULLVERSION: '1.R15.0.0'
    add_nfns_list_1:
    - NFTYPE: NfAMF
      NSIDX: 0
    add_apn_list:
    - APN: 'huawei.com'
      VIRTUALAPN: DISABLE
      HASVPN: DISABLE
      VPNINSTANCE: ''
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'huawei.com'
    add_logicip_list_5:
    - IPVERSION: IPv4
      LOGICIPV4: '10.16.0.6'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR Server SBI'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    - IPVERSION: IPv4
      LOGICIPV4: '10.2.215.26'
      VPNINSTNAME: '_public_'
      DESC: 's11'
      IPV4MTU: ''
      IPV6MTU: ''
      LOGICIPV6: ''
    add_httplegrp_list_2:
    - INDEX: 2
      DESC: 'SMF'
    add_httple_list_4:
    - INDEX: 3
      HTTPLEGRPIDX: 2
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.16.0.6'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'SMF Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list_2:
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeSMF
      DESCRIPTION: 'SMF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_nrf_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: FALSE
      PRIORITY: 0
    add_nrfaddr_list_1:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_3:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2NFBSM01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRLSSM01'
      SWITCH: ENABLE
    act_nfonline_list_1:
    - NFINSTANCENAME: 'SMF_Instance_0'
    add_gtpclegrp_list_1:
    - GROUPID: 0
      DESC: 's11'
    add_gtpclegrpmem_list_1:
    - GROUPID: 0
      IPTYPE: IPv4
      IPV4ADDR: '10.2.215.26'
      VPN: 'VRF_GW'
      DESC: 's11'
      IPV6ADDR: ''
    add_gtpcintf_list_1:
    - INTFTYPE: E_GTPCINTF_ITFS11
      GROUPID: 0
    set_smffunc_list:
    - EBID: Support
    add_ngmno_list_3:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list_3:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    add_nfuuid_list_3:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_INSTANCE_0'
    add_logicip_list_10:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list_3:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list_6:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 8080
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_httple_list_7:
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.16.0.8'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    add_sbiaple_list_3:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_httpconf_list_2:
    - CLIENTRCVRSPTMT: 15
      SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 10
      MAXJSONLEAFNUM: 100000
    set_nrftimer_list_2:
    - NFTYPE: AMF
      HBTIMES: 3
      HEARTBEATTIMER: 5
      DISCVALIDTIMER: 86400
      SUBVALIDTIMER: 86400
    add_nfgroup_list:
    - NFGROUPID: 'nfgroup01'
      NFTYPE: AUSF
      GROUPDESC: 'AUSFgroup'
    add_nfgroupmem_list:
    - NFGROUPID: 'nfgroup01'
      NFINSTANCEID: '123e4567-e89b-12d3-a456-123456780000'
    add_nfroutingind_list:
    - NFGROUPID: 'nfgroup01'
      ROUTINGIND: '1000'
    add_nfimsi_list:
    - NFGROUPID: 'nfgroup01'
      SEGSTART: '152470000000000'
      SEGEND: '152479999999999'
    syn_acspeercfg_list:
    - OPERTYPE: start
      SYNSCOPE: servicename
      SERVICENAME: '1017'
      SYNMODE: full
      INSTANCEID: ''
    syn_acspeercfg_list_1:
    - OPERTYPE: start
      SYNSCOPE: servicename
      SERVICENAME: '1018'
      SYNMODE: full
      INSTANCEID: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 任务场景1：该任务用于指导AMF向NRF的注册/去注册/更新，NF的订阅/通知功能。

### NRF侧配置

#### 1.3 //配置运营商信息。

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

#### 1.4 //配置运营商签约用户的Home PLMN

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

#### 1.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 1.7 //增加NRF服务化接口的IP地址。

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

#### 1.8 //配置Nnrf接口的HTTP信息。

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

#### 1.9 //增加NRF作为服务器端的HTTP本端实体。

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

#### 1.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_1 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
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

#### 1.11 //配置服务化接口的接入点信息。

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

#### 1.12 //配置HTTP属性。当NF Profile中包含信元的元素个数超多时，NF的注册、更新、发现等相关请求或响应都可能为产生超大报文，为了避免接收HTTP响应/请求消息体等超时时间内超大报文未发送完成导致业务失败的情况，此NF上可以通过规划配置HTTP属性，协助完成超大报文消息的成功发送，避免发送/请求报文不完整，导致业务处理异常。

```jinja2
{%- for item in set_httpconf_list -%}
    SET HTTPCONF:
    {#- --- 可选参数 --- -#}
    {%- if item.CLIENTRCVRSPTMT is not none -%}
        CLIENTRCVRSPTMT={{item.CLIENTRCVRSPTMT}},
    {%- endif -%}
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

#### 1.14 //修改NRF定时器。

```jinja2
{%- for item in set_nrftimer_list -%}
    SET NRFTIMER:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.HBTIMES is not none -%}
        HBTIMES={{item.HBTIMES}},
    {%- endif -%}
    {%- if item.HEARTBEATTIMER is not none -%}
        HEARTBEATTIMER={{item.HEARTBEATTIMER}},
    {%- endif -%}
    {%- if item.DISCVALIDTIMER is not none -%}
        DISCVALIDTIMER={{item.DISCVALIDTIMER}},
    {%- endif -%}
    {%- if item.SUBVALIDTIMER is not none -%}
        SUBVALIDTIMER={{item.SUBVALIDTIMER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.15 //打开NRF基本功能（NF注册/更新/去注册、NF订阅/通知）的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.16 //可选：如果号段类NF注册时没有携带支持的号段信息，在NRF上也没有通过配置命令或号段导入的方式配置支持的号段信息，NRF上可以配置这种号段类NF注册后不能被发现或检索，后续变更NRF也不会触发通知，避免由于号段未配置完成/漏配置被认为支持所有号段信息导致基本流程失败。

```jinja2
{%- if is_optional_segment_guard_rule -%}
    {%- for item in set_nrftakepararule_list -%}
        SET NRFTAKEPARARULE:
        {#- --- 必选参数 --- -#}
        NFTYPE={{item.NFTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：NFTYPE=UDM/UDR/AUSF/CUSTOM_OCS/CHF/PCF/SMSF 时可选 --- -#}
        {%- if item.NFTYPE in ['UDM', 'UDR', 'AUSF', 'CUSTOM_OCS', 'CHF', 'PCF', 'SMSF'] -%}
            {%- if item.NOSEGGUARDSW is not none -%}
                NOSEGGUARDSW={{item.NOSEGGUARDSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NOSEGGUARDSW=FUNC_OFF 时可选 --- -#}
        {%- if item.NOSEGGUARDSW == 'FUNC_OFF' -%}
            {%- if item.MATCHALLSW is not none -%}
                MATCHALLSW={{item.MATCHALLSW}},
            {%- endif -%}
        {#- --- 条件可选：NOIPRANGESW=FUNC_OFF 时可选 --- -#}
        {%- elif item.NOIPRANGESW == 'FUNC_OFF' -%}
            {%- if item.MATCHALLSW is not none -%}
                MATCHALLSW={{item.MATCHALLSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NFTYPE=BSF 时可选 --- -#}
        {%- if item.NFTYPE == 'BSF' -%}
            {%- if item.NOIPRANGESW is not none -%}
                NOIPRANGESW={{item.NOIPRANGESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NFTYPE=AMF/SMF/NWDAF 时可选 --- -#}
        {%- if item.NFTYPE in ['AMF', 'SMF', 'NWDAF'] -%}
            {%- if item.NOTAISW is not none -%}
                NOTAISW={{item.NOTAISW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NOSEGGUARDSW=FUNC_ON 时可选 --- -#}
        {%- if item.NOSEGGUARDSW == 'FUNC_ON' -%}
            {%- if item.REGUPDSW is not none -%}
                REGUPDSW={{item.REGUPDSW}},
            {%- endif -%}
        {#- --- 条件可选：NOTAISW=FUNC_ON 时可选 --- -#}
        {%- elif item.NOTAISW == 'FUNC_ON' -%}
            {%- if item.REGUPDSW is not none -%}
                REGUPDSW={{item.REGUPDSW}},
            {%- endif -%}
        {#- --- 条件可选：NOIPRANGESW=FUNC_ON 时可选 --- -#}
        {%- elif item.NOIPRANGESW == 'FUNC_ON' -%}
            {%- if item.REGUPDSW is not none -%}
                REGUPDSW={{item.REGUPDSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：NOSEGGUARDSW=FUNC_ON 时可选 --- -#}
        {%- if item.NOSEGGUARDSW == 'FUNC_ON' -%}
            {%- if item.RULE is not none -%}
                RULE={{item.RULE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.17 //可选：独立部署IMS的PCF支持全网号段的用户，不属于未配置/漏配号段信息的情况，针对这种PCF，NRF支持控制此类PCF注册后能够被发现、订阅/通知或检索，运营商需要提前在NRF上配置独立部署IMS的PCF支持的DNN以便NRF识别和控制其注册后可用。

```jinja2
{%- if is_optional_ims_pcf_dnn -%}
    {%- for item in add_nrfimsdnn_list -%}
        ADD NRFIMSDNN:
        {#- --- 必选参数 --- -#}
        DNN="{{item.DNN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.18 //配置可靠传输能力。

```jinja2
{%- for item in set_sdrtrans_list -%}
    SET SDRTRANS:
    {#- --- 必选参数 --- -#}
    FLATTYPE={{item.FLATTYPE}},
    TRANSABILITY={{item.TRANSABILITY}},
    OPT={{item.OPT}},
    ;
{%- endfor -%}
```

#### 1.19 //打开订阅流程开关。

```jinja2
{%- for item in add_nrfpara_list -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUBSCRISWITCH is not none -%}
        SUBSCRISWITCH={{item.SUBSCRISWITCH}},
    {%- endif -%}
    {%- if item.LOADCARRYINHB is not none -%}
        LOADCARRYINHB={{item.LOADCARRYINHB}},
    {%- endif -%}
    {%- if item.MAXRETRYTIMES is not none -%}
        MAXRETRYTIMES={{item.MAXRETRYTIMES}},
    {%- endif -%}
    {%- if item.OAUTH2SWITCH is not none -%}
        OAUTH2SWITCH={{item.OAUTH2SWITCH}},
    {%- endif -%}
    {%- if item.WAITINTERVAL is not none -%}
        WAITINTERVAL={{item.WAITINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### NF状态通知：NRF根据NF的订阅请求，当收到符合订阅条件的NF发生变化时，NRF自动触发状态通知，不需要额外配置。

### 2 AMF侧配置

#### 2.3 //配置运营商信息。

```jinja2
{%- for item in add_ngmno_list_1 -%}
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

#### 2.4 //配置运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_nghplmn_list_1 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 2.5 //配置运营商的Serving PLMN。

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

#### 2.6 //配置运营商支持的网络切片。

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
    ;
{%- endfor -%}
```

#### 2.8 //配置AMF实例的名称，此步骤配置后系统会为NF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_1 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 2.9 //配置AMF实例的Profile信息。

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

#### 2.10 //配置AMF的域名等信息。

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

#### 2.11 //配置AMF提供的服务实例及其版本信息。

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

#### 2.12 //配置全局AMF标识（GUAMI）和AMF支持的切片信息。

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

#### 2.14 //增加AMF服务化接口的IP地址。

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

#### 2.15 //配置Namf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_1 -%}
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
{%- for item in add_httple_list_2 -%}
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
{%- for item in add_sbiaple_list_1 -%}
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

#### 2.17 //配置NRF信息。

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

#### 2.18 //配置NRF的地址信息，对接的NRF地址信息为NRF本端端点作为服务端的IP。

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

#### 2.19 //配置NRF协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
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
```

#### 2.20 //打开NF注册/更新/去注册、订阅/通知基本功能开关。

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.21 //AMF服务就绪后，向NRF注册REGISTERED状态。

```jinja2
{%- for item in act_nfonline_list -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 2.22 //打开订阅流程开关。

```jinja2
{%- for item in add_nrfpara_list_2 -%}
    ADD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUBSCRISWITCH is not none -%}
        SUBSCRISWITCH={{item.SUBSCRISWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.23 //增加AMF订阅SMF的订阅条件。

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

#### 2.24 ……

#### 2.27 //配置N26接口信息。

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

#### 2.28 //配置支持UE在LTE与5G SA网络间互操作。设置对端MME支持non-IP类型PDN和UE接入限制。

```jinja2
{%- for item in add_n26mmechar_list -%}
    ADD N26MMECHAR:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MMECAP is not none -%}
        MMECAP={{item.MMECAP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_MME' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        MASKV4="{{item.MASKV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        MASKV6={{item.MASKV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngmmsubdata_list -%}
    ADD NGMMSUBDATA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.RATRESTRICT is not none -%}
        RATRESTRICT={{item.RATRESTRICT}},
    {%- endif -%}
    {%- if item.CORERESTRICT is not none -%}
        CORERESTRICT={{item.CORERESTRICT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        IMSI="{{item.IMSI}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MCS is not none -%}
            MCS={{item.MCS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MPS is not none -%}
            MPS={{item.MPS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUBRANGE=IMSI 时可选 --- -#}
    {%- if item.SUBRANGE == 'IMSI' -%}
        {%- if item.MPSMCSPRI is not none -%}
            MPSMCSPRI={{item.MPSMCSPRI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 SMF+GW-C侧

#### 3.3 //配置运营商信息。

```jinja2
{%- for item in add_ngmno_list_2 -%}
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

#### 3.4 //配置运营商签约用户的Home PLMN。

```jinja2
{%- for item in add_nghplmn_list_2 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 3.5 //配置运营商签约用户的Serving PLMN。

```jinja2
{%- for item in add_ngsrvplmn_list_1 -%}
    ADD NGSRVPLMN:
    {#- --- 必选参数 --- -#}
    PLMNIDX={{item.PLMNIDX}},
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 3.6 //配置运营商支持的网络切片。

```jinja2
{%- for item in add_plmnns_list_1 -%}
    ADD PLMNNS:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    PLMNIDX={{item.PLMNIDX}},
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.8 //配置SMF实例的名称，此步骤配置后系统会为NF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_2 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 3.9 //配置SMF实例的Profile信息。

```jinja2
{%- for item in add_nfprofile_list_1 -%}
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

#### 3.10 //配置SMF的域名等信息。

```jinja2
{%- for item in add_smfinfo_list -%}
    ADD SMFINFO:
    {#- --- 必选参数 --- -#}
    SMFINSTANCENAME="{{item.SMFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SMFNAME is not none -%}
        SMFNAME="{{item.SMFNAME}}",
    {%- endif -%}
    {%- if item.PGWFQDN is not none -%}
        PGWFQDN="{{item.PGWFQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.11 //配置SMF提供的服务实例及其版本信息。

```jinja2
{%- for item in add_nfservice_list_4 -%}
    ADD NFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nfservicever_list_4 -%}
    ADD NFSERVICEVER:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    APIFULLVERSION="{{item.APIFULLVERSION}}",
    ;
{%- endfor -%}
```

#### 3.12 //配置SMF支持的切片信息。

```jinja2
{%- for item in add_nfns_list_1 -%}
    ADD NFNS:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NSIDX={{item.NSIDX}},
    ;
{%- endfor -%}
```

#### 3.13 //配置SMF支持的APN/DNN、网络切片支持的DNN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 3.15 //增加SMF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_5 -%}
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

#### 3.16 //配置Nsmf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_2 -%}
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
{%- for item in add_httple_list_4 -%}
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
{%- for item in add_sbiaple_list_2 -%}
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

#### 3.18 //配置NRF信息。

```jinja2
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
```

#### 3.19 //配置NRF的地址信息。

```jinja2
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
```

#### 3.20 //配置NRF协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
{%- for item in add_nrfpara_list_3 -%}
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

#### 3.21 //打开NF注册、认证、发现等与NRF进行交互的基本功能的开关。

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 3.22 //激活SMF向NRF注册。

```jinja2
{%- for item in act_nfonline_list_1 -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 3.23 /*- - - - - - - - - -- - - - -以下为4/5G融合网络特有的接口和互操作配置- - - - - - - - - - - - - - */

#### 3.26 //配置S11/S5/S8-C接口的GTP-C本地实体组和实体组成员信息。

```jinja2
{%- for item in add_gtpclegrp_list_1 -%}
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
{%- for item in add_gtpclegrpmem_list_1 -%}
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

#### 3.27 //配置S11/S5/S8-C接口信息。

```jinja2
{%- for item in add_gtpcintf_list_1 -%}
    ADD GTPCINTF:
    {#- --- 必选参数 --- -#}
    INTFTYPE={{item.INTFTYPE}},
    GROUPID={{item.GROUPID}},
    ;
{%- endfor -%}
```

#### 3.29 //配置SMF+GW-C支持4G。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.EBID is not none -%}
        EBID={{item.EBID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 任务场景2：该任务用于指导AMF向NRF的手动注册/去注册/更新，NF的订阅/通知。

### 仅涉及NRF侧配置（NF不支持自动注册，注册信息在NRF上完成）

### **配置NRF侧基础信息**

#### 4.3 //配置运营商信息。

```jinja2
{%- for item in add_ngmno_list_3 -%}
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

#### 4.4 //配置运营商签约用户的Home PLMN

```jinja2
{%- for item in add_nghplmn_list_3 -%}
    ADD NGHPLMN:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

#### 4.5 //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list_3 -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 4.7 //增加NRF服务化接口的IP地址。

```jinja2
{%- for item in add_logicip_list_10 -%}
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

#### 4.8 //配置Nnrf接口的HTTP信息。

```jinja2
{%- for item in add_httplegrp_list_3 -%}
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

#### 4.9 //增加NRF作为服务器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_6 -%}
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

#### 4.10 //增加NRF作为客户器端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_7 -%}
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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
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

#### 4.11 //配置服务化接口的接入点信息。

```jinja2
{%- for item in add_sbiaple_list_3 -%}
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

#### 4.12 //配置HTTP属性。当NF Profile中包含信元的元素个数超多时，NF的注册、更新、发现等相关请求或响应都可能为产生超大报文，为了避免接收HTTP响应/请求消息体等超时时间内超大报文未发送完成导致业务失败的情况，此NF上可以通过规划配置HTTP属性，协助完成超大报文消息的成功发送，避免发送/请求报文不完整，导致业务处理异常。

```jinja2
{%- for item in set_httpconf_list_2 -%}
    SET HTTPCONF:
    {#- --- 可选参数 --- -#}
    {%- if item.CLIENTRCVRSPTMT is not none -%}
        CLIENTRCVRSPTMT={{item.CLIENTRCVRSPTMT}},
    {%- endif -%}
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

#### 4.14 //修改NRF定时器。

```jinja2
{%- for item in set_nrftimer_list_2 -%}
    SET NRFTIMER:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.HBTIMES is not none -%}
        HBTIMES={{item.HBTIMES}},
    {%- endif -%}
    {%- if item.HEARTBEATTIMER is not none -%}
        HEARTBEATTIMER={{item.HEARTBEATTIMER}},
    {%- endif -%}
    {%- if item.DISCVALIDTIMER is not none -%}
        DISCVALIDTIMER={{item.DISCVALIDTIMER}},
    {%- endif -%}
    {%- if item.SUBVALIDTIMER is not none -%}
        SUBVALIDTIMER={{item.SUBVALIDTIMER}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **配置NF手动注册：**

### NF不具备携带属性向NRF自动注册的能力，可以在NRF上手动配置NF Profile，完成手动注册后此NF可在网络中提供网络功能。

#### 5.1 根据此NF自身属性及提供的网络功能等信息，完成对应的NF Profile规划（NF Profile遵循3GPP协议），以JSON文件的格式准备。

#### 5.2 登录OM Portal。

#### 5.3 选择“System > File Transfer >  NRFStaticNFProfile”，单击“Add File”，在弹出的对话框中选择准备的JSON文件完成上传。

#### 5.4 进入“MML命令行-UNC”窗口。

#### 5.5 执行**ACT STCNFPROFILE**命令，完成NF的手动注册。

### 6 **配置NF手动去注册**：

### NF不具备自动向NRF去注册的能力，可以在NRF上手动去注册此NF，对应的命令为**DEACT STCNFPROFILE**。

### 7 **配置NF手动更新：**

### NF不具备自动向NRF更新的能力，需要更新时，采用NF手动注册的方式，加载上传更新后的NF Profile文件（NF Instance ID与之前手动注册相同），实现NF手动更新。

### 8 任务场景3：该任务用于指导在NRF上配置号段类NF支持的号段信息。

### 例如配置AUSF NF实例组：nfgroup01。

### 使用非配置文件的方式在NRF上为上述NF配置支持的号段信息：

### AUSF的NF组nfgroup01配置支持的IMSI号段信息为：152470000000000~152479999999999，AUSF的发现流程，请求方NF携带的IMSI属于此号段范围，就会对应找到此nfgroup01组。

### AUSF的NF组nfgroup01配置支持的Routing indicator为：1000，AUSF的发现流程，请求方NF携带的Routing indicator值为1000时，就会对应找到此nfgroup01组。

### 如图1所示。

### **图1** NF组支持的不同号段信息举例

### 号段类NF在注册携带号段信息时，此场景不需要配置。但号段类NF支持的号段信息量往往比较大，当号段类NF向NRF的注册信息超过64k时会对NRF造成处理冲击，建议采用在NRF上规划号段类NF的支持信息。

### 当运营商希望通过规划在NRF上配置服务提供方NF支持的号段信息时，需要配置此场景。

### 仅涉及NRF侧配置，NRF支持NF号段信息分为命令配置和百万号段导入两种方式，参考图2。

### **图2** NRF上配置号段类NF支持的号段信息

### **NRF侧命令配置方式（进行号段配置时，待配置号段量在30000内时推荐使用）**

#### 8.1 //配置AUSF实例组。

```jinja2
{%- if is_scenario_cmd_config -%}
    {%- for item in add_nfgroup_list -%}
        ADD NFGROUP:
        {#- --- 必选参数 --- -#}
        NFGROUPID="{{item.NFGROUPID}}",
        NFTYPE={{item.NFTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPDESC is not none -%}
            GROUPDESC="{{item.GROUPDESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 //可选：配置AUSF实例组中NF实例标识：当请求方NF在注册时上报了groupId时，不需要配置此步骤。当NF注册时，不支持groupId的上报或没有上报groupId，运营商希望通过NRF管理该NF的号段信息时，配置此步骤。

```jinja2
{%- if is_optional_nfgroup_member_id and is_scenario_cmd_config -%}
    {%- for item in add_nfgroupmem_list -%}
        ADD NFGROUPMEM:
        {#- --- 必选参数 --- -#}
        NFGROUPID="{{item.NFGROUPID}}",
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.3 //配置AUSF的NF组nfgroup01支持的Routing indicator为：1000。Routing indicator号段配置量较少，无号段配置文件的方式。

```jinja2
{%- if is_scenario_cmd_config -%}
    {%- for item in add_nfroutingind_list -%}
        ADD NFROUTINGIND:
        {#- --- 必选参数 --- -#}
        NFGROUPID="{{item.NFGROUPID}}",
        ROUTINGIND="{{item.ROUTINGIND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.4 //配置AUSF的NF组nfgroup01支持的IMSI号段信息为：152470000000000~152479999999999。

```jinja2
{%- if is_scenario_cmd_config -%}
    {%- for item in add_nfimsi_list -%}
        ADD NFIMSI:
        {#- --- 必选参数 --- -#}
        NFGROUPID="{{item.NFGROUPID}}",
        SEGSTART="{{item.SEGSTART}}",
        SEGEND="{{item.SEGEND}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 针对服务提供方NF支持的supi和gpsi在NRF上的配置要求：

#### - supi和gpsi的匹配原则为“或”的关系，即对于同一NF配置的IMSI号段或MSISDN号段，supi或gpsi匹配上任一配置即认为该NF支持此号段。

#### - 如果某NF的NF Profile中supi和gpsi号段规划为全支持，则必须对IMSI号段和MSISDN号段同时添加对应的全号段配置：

#### 例如IMSI号段长度如果为15位，全号段配置为：000000000000000~999999999999999；MSISDN号段长度如果为11位，全号段配置为：00000000000~99999999999。

#### 如果该类NF只涉及其中一类号段，则只需要添加相应类型的全号段配置，比如AUSF只涉及supi号段，则只需要对IMSI号段添加对应的全号段配置。

### 9 **NRF侧号段配置文件导入方式**

#### 9.1 - **xml文件导入方式****（新建局点，初始配置大量号段信息（大于30000条）时，推荐使用）**

##### 9.1.1 准备最新的号段配置文件。

##### 请按照号段配置文件的格式要求准备xml格式的号段配置文件（或对应的zip包），各种xml文件模板请参考附加信息。如有疑问请联系华为技术支持NRF支持人员。

##### 9.1.2 上传号段配置文件：在华为操作维护系统（OM Portal）中选择“系统 > 文件传输 > 原子配置服务” ，单击“添加文件”上传准备好的号段配置文件。

##### 9.1.3 导入号段配置文件：执行下面MML命令将文件导入到系统中，执行过程中可以观察到命令执行进度。

##### 9.1.4 导入号段配置文件完成后，启动NFM管理类微服务同步，对应微服务名称为1017，使号段配置文件在系统中生效：

##### 加载XML文件完成后，需要检查如下两种方式中的一种，满足条件后才可执行**SYN ACSPEERCFG：**

##### 查看设备上是否有“ALM-221257751 进程故障”告警，如果有等告警恢复后才可执行**SYN ACSPEERCFG**。

##### 执行**DSP PROCESSINFO**，“服务实例”填写“ACS”，“进程类型”填写“OMSVC”，查询OMSVC进程状态是否为“NORMAL”，如果不是等待状态恢复为“NORMAL”后才可执行**SYN ACSPEERCFG**。

##### 脚本参考如下：

```jinja2
{%- if is_scenario_file_import and is_scenario_xml_import -%}
    {%- for item in syn_acspeercfg_list -%}
        SYN ACSPEERCFG:
        {#- --- 必选参数 --- -#}
        OPERTYPE={{item.OPERTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OPERTYPE=start/stop 时必选 --- -#}
        {%- if item.OPERTYPE in ['start', 'stop'] -%}
            SYNSCOPE={{item.SYNSCOPE}},
        {%- endif -%}
        {#- --- 条件必选：SYNSCOPE=servicename/servicename_instanceid 时必选 --- -#}
        {%- if item.SYNSCOPE in ['servicename', 'servicename_instanceid'] -%}
            SERVICENAME="{{item.SERVICENAME}}",
        {%- endif -%}
        {#- --- 条件必选：SYNSCOPE=servicename_instanceid 时必选 --- -#}
        {%- if item.SYNSCOPE == 'servicename_instanceid' -%}
            INSTANCEID="{{item.INSTANCEID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPERTYPE=start 时可选 --- -#}
        {%- if item.OPERTYPE == 'start' -%}
            {%- if item.SYNMODE is not none -%}
                SYNMODE={{item.SYNMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.1.5 大约5~10分钟后，执行如下命令查询对应的微服务的同步情况，确保号段配置文件生效完成：

##### 如果4执行完后超过20分钟，执行**DSP ACSSYNCINFO**，“同步状态”显示仍不是“同步成功”，则需要联系华为技术支持NRF支持人员进行处理。

##### 脚本参考如下：

##### %%DSP ACSSYNCINFO: SERVICENAME="1017";%%

##### RETCODE = 0  操作成功

##### 操作结果如下

##### ------------------------

##### 服务名称  =  1017

##### 实例ID  =  nrf-pod-665c467d69-948nl172-234-0-210__1025__0

##### 远端设备IP地址  =  10.30.0.206

##### 远端设备IP端口号  =  21077

##### 同步状态  =  同步成功

##### 上一次同步结束时间  =  2021-04-27, 07:06:26:131

##### (结果个数 = 1)

##### ---    END

##### 9.1.6 导入号段配置文件完成后，启动DISC发现类微服务同步，对应微服务名称为1018，使号段配置文件在系统中生效：

##### 加载XML文件完成后，需要检查如下两种方式中的一种，满足条件后才可执行**SYN ACSPEERCFG：**

##### 查看设备上是否有“ALM-221257751 进程故障”告警，如果有等告警恢复后才可执行**SYN ACSPEERCFG**。

##### 执行**DSP PROCESSINFO**，“服务实例”填写“ACS”，“进程类型”填写“OMSVC”，查询OMSVC进程状态是否为“NORMAL”，如果不是等待状态恢复为“NORMAL”后才可执行**SYN ACSPEERCFG**。

##### 脚本参考如下：

```jinja2
{%- if is_scenario_file_import and is_scenario_xml_import -%}
    {%- for item in syn_acspeercfg_list_1 -%}
        SYN ACSPEERCFG:
        {#- --- 必选参数 --- -#}
        OPERTYPE={{item.OPERTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：OPERTYPE=start/stop 时必选 --- -#}
        {%- if item.OPERTYPE in ['start', 'stop'] -%}
            SYNSCOPE={{item.SYNSCOPE}},
        {%- endif -%}
        {#- --- 条件必选：SYNSCOPE=servicename/servicename_instanceid 时必选 --- -#}
        {%- if item.SYNSCOPE in ['servicename', 'servicename_instanceid'] -%}
            SERVICENAME="{{item.SERVICENAME}}",
        {%- endif -%}
        {#- --- 条件必选：SYNSCOPE=servicename_instanceid 时必选 --- -#}
        {%- if item.SYNSCOPE == 'servicename_instanceid' -%}
            INSTANCEID="{{item.INSTANCEID}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：OPERTYPE=start 时可选 --- -#}
        {%- if item.OPERTYPE == 'start' -%}
            {%- if item.SYNMODE is not none -%}
                SYNMODE={{item.SYNMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.1.7 大约5~10分钟后，执行如下命令查询对应的微服务的同步情况，确保号段配置文件生效完成：

##### 如果6执行完后超过20分钟，执行**DSP ACSSYNCINFO**，“同步状态”显示仍不是“同步成功”，则需要联系华为技术支持NRF支持人员进行处理。

##### 脚本参考如下：

##### %%DSP ACSSYNCINFO: SERVICENAME="1018";%%

##### RETCODE = 0  操作成功

##### 操作结果如下

##### ------------------------

##### 服务名称  =  1018

##### 实例ID  =  uncpod-0144-30-0-206__1026__0

##### 远端设备IP地址  =  10.30.0.206

##### 远端设备IP端口号 =  21029

##### 同步状态 =  同步成功

##### 上一次同步结束时间 =  2021-04-27, 07:06:21:535

##### (结果个数 = 1)

##### ---    END

##### 9.1.8 验证导入号段生效：规划待查询的导入号段，通过如下命令输入待查询号段（子集）或路由，确保导入的号段配置文件正常应用到NRF业务中。

##### 查询号段/路由匹配信息如下：

##### **DSP NRFIMSI**

##### **DSP NRFIMSIRT**

##### **DSP NRFMSISDN**

##### **DSP NRFMSISDNRT**

##### 查询号段/路由统计信息如下：

##### **DSP NRFIMSISTC**

##### **DSP NRFIMSIRTSTC**

##### **DSP NRFMSISDNSTC**

##### **DSP NRFMSISDNRTSTC**

#### 9.2 - **.dat文件导入方式**

##### 9.2.1 准备最新的号段配置文件。

##### 请按照号段配置文件的格式要求准备的.dat格式号段配置文件，详细请联系华为技术支持NRF支持人员。

##### 9.2.2 查看系统中号段配置文件的加载状态（仅适用于IMSI/MSISDN的号段配置文件）。

##### 9.2.3 **可选：**如果2中的“是否主表”取值为“FALSE”的备号段配置文件中有数据（“号段文件名称”不为“NULL”），则需要执行命令删除备用号段文件中的数据。

##### 9.2.4 导入号段配置文件：在华为操作维护系统（OM Portal）中选择“系统 > 文件传输 > NRF号段导入文件” ，单击“添加文件”上传准备好的号段配置文件。

##### 9.2.5 校验导入的号段配置文件是否成功，如果不成功，需要按提示信息修改号段至成功，再进行下一步操作。

##### 9.2.6 加载备用号段文件，使配置文件中的内容加载到NRF上。

##### 9.2.7 查看确保当前备用的号段配置文件加载成功。

##### 9.2.8 激活号段文件使新加载的备用号段文件生效。

##### 9.2.9 打开服务发现结果号段导入数据可用开关。

##### 9.2.10 **可选：**可以通过华为操作维护系统导出号段配置文件查看已加载的号段数据。

###### 9.2.10.1 导出号段配置文件。

###### 9.2.10.2 在华为操作维护系统（OM Portal）中选择“System > File Transfer > NrfSegExportFile”，可以看到新导出的号段文件，下载查看即可。

#### 对于已经导入的号段配置文件，可以通过**ADD SEGBLACKLIST**命令新增导入号段黑名单，快速使导入号段中的部分号段数据失效。

