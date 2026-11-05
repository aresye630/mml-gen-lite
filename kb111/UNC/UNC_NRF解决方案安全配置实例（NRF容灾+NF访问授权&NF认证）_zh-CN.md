---
id: ''
name: NRF解决方案安全配置实例（NRF容灾+NF访问授权&NF认证）
ne_type: UNC
type: feature
description: '* FQDN为“huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org”的SMF通过在NRF上设置访问授权，设定只允许AMF访问。 * AMF与NRF之间使用TLS证书认证，保证传输层安全。 * AMF向NRF申请Token，NF间认证，保证应用层安全。NRF支持NF的Access Token申请，NF申请后使用Token进行NF认证。NF服务提供者对NF服务消费者进行认证，利用公钥来校验Access Token中的签名是否正确（NRF上使用私钥，NF上使用公钥）。为保证安全，NRF上使用的私钥是加密保存的。NRF上Access Token的签名算法和NRF上Access Token签名的私钥以及对应的NF侧密钥需要配置。    需要提前规划用于Token签名的公私钥对，NRF侧的私钥与此处NF侧配置的公钥配对。'
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","5G独立部署","NRF单层容灾组网","NRF解决方案安全配置实例（NRF容灾+NF访问授权&NF认证）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* FQDN为“huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org”的SMF通过在NRF上设置访问授权，设定只允许AMF访问。* AMF与NRF之间使用TLS证书认证，保证传输层安全。* AMF向NRF申请Token，NF间认证，保证应用层安全。NRF支持NF的Access Token申请，NF申请后使用Token进行NF认证。NF服务提供者对NF服务消费者进行认证，利用公钥来校验Access Token中的签名是否正确（NRF上使用私钥，NF上使用公钥）。为保证安全，NRF上使用的私钥是加密保存的。NRF上Access Token的签名算法和NRF上Access Token签名的私钥以及对应的NF侧密钥需要配置。  需要提前规划用于Token签名的公私钥对，NRF侧的私钥与此处NF侧配置的公钥配对。

## 必备事项
前提条件

前提条件

* 2个NRF基础配置已完成，详细请参考NRF主备容灾的NRF基础数据配置或者NRF双活容灾的NRF基础数据配置。
* 根据实际的容灾场景，NRF容灾组网已配置完成，详细请参考主备容灾组网配置或者双活容灾组网配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_nrffuncsw_list:
      type: items
      properties:
        AUTHSW:
          name: '授权功能开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_allowedobjname_list:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_allowedobj_list:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_allowednftypes_list:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDNFTYPE:
          name: '允许访问该对象的NF类型'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    cmt_allowplcy_list:
      type: items
      properties:
        CMTTYPE:
          name: '提交类型'
          type: string
          enum:
          - ALL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    set_nrffuncsw_list_1:
      type: items
      properties:
        AUTHSW:
          name: '授权功能开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_allowedobjname_list_1:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_allowedobj_list_1:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_allowednftypes_list_1:
      type: items
      properties:
        OBJNAME:
          name: '授权对象名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDNFTYPE:
          name: '允许访问该对象的NF类型'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    cmt_allowplcy_list_1:
      type: items
      properties:
        CMTTYPE:
          name: '提交类型'
          type: string
          enum:
          - ALL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_tlsscene_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCENE:
          name: '证书使用场景名称'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '场景类型'
          type: string
          enum:
          - SCENE_CA
          - SCENE_NE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '证书使用场景描述'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYLOCALCERT:
          name: '是否验证本端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tlspara_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'HTTP模式'
          type: string
          enum:
          - Client
          - Server
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFY:
          name: '是否验证对端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYCN:
          name: '域名校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '证书中的域名应当与网络规划的域名保持一致。开启域名校验开关后，如果校验失败将导致NF间建链失败。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CIPHER:
          name: '加密套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCAL:
          name: '协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的设备证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的CA证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CRLFLAG:
          name: 'CRL是否开启'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: '为了提升系统安全性，避免使用已被吊销的证书，建议开启证书吊销列表（CRL）功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '认证模式'
          type: string
          enum:
          - CERT
          - PSK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: CERT
        PSKGRPIDX:
          name: '预共享密钥组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VDEPTH:
          name: '校验深度'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYIP:
          name: 'IP校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYSNI:
          name: 'SNI校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYCNFULL:
          name: '域名校验全匹配'
          type: string
          enum:
          - YES
          - NO
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    add_httple_list_1:
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
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
    add_tlsscene_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCENE:
          name: '证书使用场景名称'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '场景类型'
          type: string
          enum:
          - SCENE_CA
          - SCENE_NE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '证书使用场景描述'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYLOCALCERT:
          name: '是否验证本端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tlspara_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'HTTP模式'
          type: string
          enum:
          - Client
          - Server
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFY:
          name: '是否验证对端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYCN:
          name: '域名校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '证书中的域名应当与网络规划的域名保持一致。开启域名校验开关后，如果校验失败将导致NF间建链失败。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CIPHER:
          name: '加密套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCAL:
          name: '协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的设备证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的CA证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CRLFLAG:
          name: 'CRL是否开启'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: '为了提升系统安全性，避免使用已被吊销的证书，建议开启证书吊销列表（CRL）功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '认证模式'
          type: string
          enum:
          - CERT
          - PSK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: CERT
        PSKGRPIDX:
          name: '预共享密钥组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VDEPTH:
          name: '校验深度'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYIP:
          name: 'IP校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYSNI:
          name: 'SNI校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYCNFULL:
          name: '域名校验全匹配'
          type: string
          enum:
          - YES
          - NO
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    add_httple_list_3:
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
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
    add_tlsscene_list_4:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 254
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCENE:
          name: '证书使用场景名称'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TYPE:
          name: '场景类型'
          type: string
          enum:
          - SCENE_CA
          - SCENE_NE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '证书使用场景描述'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYLOCALCERT:
          name: '是否验证本端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tlspara_list_4:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: 'HTTP模式'
          type: string
          enum:
          - Client
          - Server
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFY:
          name: '是否验证对端证书'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYCN:
          name: '域名校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: '证书中的域名应当与网络规划的域名保持一致。开启域名校验开关后，如果校验失败将导致NF间建链失败。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CIPHER:
          name: '加密套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCAL:
          name: '协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的设备证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: '该参数需要与**ADD TLSSCENE**中配置的CA证书场景的“索引”一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CRLFLAG:
          name: 'CRL是否开启'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: '为了提升系统安全性，避免使用已被吊销的证书，建议开启证书吊销列表（CRL）功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '认证模式'
          type: string
          enum:
          - CERT
          - PSK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: CERT
        PSKGRPIDX:
          name: '预共享密钥组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VDEPTH:
          name: '校验深度'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYIP:
          name: 'IP校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYSNI:
          name: 'SNI校验开关'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VERIFYCNFULL:
          name: '域名校验全匹配'
          type: string
          enum:
          - YES
          - NO
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
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
    add_httple_list_5:
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
          description: '该参数需要提前通过**ADD HTTPLEGRP**添加。'
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
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSSCENE**中配置的“索引”匹配。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: YES
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
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
    mod_nrf_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLS:
          name: 'TLS'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '全网规划'
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
    add_tokenexp_list:
      type: items
      properties:
        SCFGTYPE:
          name: '生效范围'
          type: string
          enum:
          - BYNFTYPE
          - BYFQDN
          required: true
          description: ''
          data_source: ''
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPTIME:
          name: '有效期时长(分钟)'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_tokenalg_list:
      type: items
      properties:
        ALGNAME:
          name: '算法'
          type: string
          enum:
          - RS256
          - RS384
          - RS512
          - ES256
          - ES384
          - ES512
          - PS256
          - PS384
          - PS512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfkey_list:
      type: items
      properties:
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEYINFO:
          name: '密钥密文'
          type: string
          minLength: 0
          maxLength: 4096
          required: true
          description: '公私钥对目前是客户提前准备提供。  原始密钥格式及对应格式解释如图1所示。用户在命令中使用时需要将原始密钥的**空行删除**，**换行转换为“#”**后，将整个密钥合并成一个字符串，即成为对应取值样例使用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHPWD:
          name: '密钥口令'
          type: string
          minLength: 8
          maxLength: 16
          required: true
          description: '请以实际规划为准，此参数输入时界面做了匿名化，务必保证输入参数与规划一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NRFKEYIDSW:
          name: 'NRF密钥ID开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NRFKEYID:
          name: 'NRF密钥ID'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: '如需修改NRFKEYID，则需先通过**ADD NRFKEY**新增包含所需NRFKEYID的NRFKEY，再通过**ACT NRFKEY**激活此NRFKEY，最后通过**RMV NRFKEY**删除不需要的NRFKEY。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    act_nrfkey_list:
      type: items
      properties:
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '激活指定NRF的密钥信息。'
          data_source: '本端规划'
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
    add_tokenexp_list_1:
      type: items
      properties:
        SCFGTYPE:
          name: '生效范围'
          type: string
          enum:
          - BYNFTYPE
          - BYFQDN
          required: true
          description: ''
          data_source: ''
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPTIME:
          name: '有效期时长(分钟)'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_tokenalg_list_1:
      type: items
      properties:
        ALGNAME:
          name: '算法'
          type: string
          enum:
          - RS256
          - RS384
          - RS512
          - ES256
          - ES384
          - ES512
          - PS256
          - PS384
          - PS512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfkey_list_1:
      type: items
      properties:
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEYINFO:
          name: '密钥密文'
          type: string
          minLength: 0
          maxLength: 4096
          required: true
          description: '公私钥对目前是客户提前准备提供。  原始密钥格式及对应格式解释如图1所示。用户在命令中使用时需要将原始密钥的**空行删除**，**换行转换为“#”**后，将整个密钥合并成一个字符串，即成为对应取值样例使用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHPWD:
          name: '密钥口令'
          type: string
          minLength: 8
          maxLength: 16
          required: true
          description: '请以实际规划为准，此参数输入时界面做了匿名化，务必保证输入参数与规划一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NRFKEYIDSW:
          name: 'NRF密钥ID开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NRFKEYID:
          name: 'NRF密钥ID'
          type: string
          minLength: 1
          maxLength: 128
          required: false
          description: '如需修改NRFKEYID，则需先通过**ADD NRFKEY**新增包含所需NRFKEYID的NRFKEY，再通过**ACT NRFKEY**激活此NRFKEY，最后通过**RMV NRFKEY**删除不需要的NRFKEY。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    act_nrfkey_list_1:
      type: items
      properties:
        KEYNAME:
          name: '密钥名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: '激活指定NRF的密钥信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_licenseswitch_list_4:
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
    mod_nrfpara_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OAUTH2SWITCH:
          name: 'OAUTH2鉴权开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: 'NF上开启Oauth2 Token鉴权。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httpoauthkey_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTSCENE:
          name: '认证场景'
          type: string
          enum:
          - NFSERV_ACCESS
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUZSVRID:
          name: '授权服务器标识'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PUBKEYID:
          name: '公钥标识'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '需与NRF侧**ADD NRFKEY**中的NRF密钥ID（NRFKEYID）一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PUBKEY:
          name: '公钥内容'
          type: string
          minLength: 0
          maxLength: 1024
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PUBKEYNAME:
          name: '公钥名称'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_nrffuncsw_list:
    - AUTHSW: FUNC_ON
    add_allowedobjname_list:
    - OBJNAME: 'objname001'
    add_allowedobj_list:
    - OBJNAME: 'objname001'
      FQDN: 'huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org'
    add_allowednftypes_list:
    - OBJNAME: 'objname001'
      ALLOWEDNFTYPE: AMF
    cmt_allowplcy_list:
    - CMTTYPE: ALL
    set_nrffuncsw_list_1:
    - AUTHSW: FUNC_ON
    add_allowedobjname_list_1:
    - OBJNAME: 'objname001'
    add_allowedobj_list_1:
    - OBJNAME: 'objname001'
      FQDN: 'huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org'
    add_allowednftypes_list_1:
    - OBJNAME: 'objname001'
      ALLOWEDNFTYPE: AMF
    cmt_allowplcy_list_1:
    - CMTTYPE: ALL
    add_tlsscene_list:
    - INDEX: 3
      SCENE: 'NESCENE'
      TYPE: SCENE_NE
      DESC: 'NRFNESCENE'
      VERIFYLOCALCERT: ''
    add_tlspara_list:
    - INDEX: 3
      MODE: Server
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 3
      CASCENE: 4
      CRLFLAG: CRL_ON
      AUTHMODE: CERT
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    - INDEX: 4
      MODE: Client
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 3
      CASCENE: 4
      CRLFLAG: CRL_ON
      AUTHMODE: ''
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    add_httplegrp_list:
    - INDEX: 2
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 2
      LETYPE: SERVER
      PORT: 30116
      TLSFLG: YES
      TLSIDX: 3
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      VPNNAME: '_public_'
      IPV6: ''
    add_httple_list_1:
    - INDEX: 4
      HTTPLEGRPIDX: 2
      LETYPE: CLIENT
      TLSIDX: 4
      IPTYPE: IPv4
      IPV4: '172.16.0.8'
      VPNNAME: '_public_'
      PORT: 30116
      TLSFLG: YES
      IPV6: ''
    add_sbiaple_list:
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_tlsscene_list_2:
    - INDEX: 3
      SCENE: 'NESCENE'
      TYPE: SCENE_NE
      DESC: 'NRFNESCENE'
      VERIFYLOCALCERT: ''
    add_tlspara_list_2:
    - INDEX: 3
      MODE: Server
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 3
      CASCENE: 4
      CRLFLAG: CRL_ON
      AUTHMODE: CERT
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    - INDEX: 4
      MODE: Client
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 3
      CASCENE: 4
      CRLFLAG: CRL_ON
      AUTHMODE: ''
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    add_httplegrp_list_1:
    - INDEX: 2
      DESC: 'NRF'
    add_httple_list_2:
    - INDEX: 3
      HTTPLEGRPIDX: 2
      LETYPE: SERVER
      PORT: 30116
      TLSFLG: YES
      TLSIDX: 3
      IPTYPE: IPv4
      IPV4: '172.26.0.7'
      VPNNAME: '_public_'
      IPV6: ''
    add_httple_list_3:
    - INDEX: 4
      HTTPLEGRPIDX: 2
      LETYPE: CLIENT
      TLSIDX: 4
      IPTYPE: IPv4
      IPV4: '172.26.0.8'
      VPNNAME: '_public_'
      PORT: 30116
      TLSFLG: YES
      IPV6: ''
    add_sbiaple_list_1:
    - INDEX: 2
      HTTPLEGRPIDX: 2
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_tlsscene_list_4:
    - INDEX: 1
      SCENE: 'NESCENE'
      TYPE: SCENE_NE
      DESC: 'AMFNESCENE'
      VERIFYLOCALCERT: ''
    add_tlspara_list_4:
    - INDEX: 1
      MODE: Server
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 1
      CASCENE: 2
      CRLFLAG: CRL_ON
      AUTHMODE: CERT
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    - INDEX: 2
      MODE: Client
      VERIFY: Yes
      VERIFYCN: Yes
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1
      PROTOCAL: TLS1_2-1&TLS1_3-1
      NESCENE: 1
      CASCENE: 2
      CRLFLAG: CRL_ON
      AUTHMODE: ''
      PSKGRPIDX: ''
      VDEPTH: ''
      VERIFYIP: ''
      VERIFYSNI: ''
      VERIFYCNFULL: ''
    add_httplegrp_list_2:
    - INDEX: 1
      DESC: 'AMF'
    add_httple_list_4:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      LETYPE: SERVER
      PORT: 30116
      TLSFLG: YES
      TLSIDX: 1
      IPTYPE: IPv4
      IPV4: '172.16.1.4'
      VPNNAME: '_public_'
      IPV6: ''
    add_httple_list_5:
    - INDEX: 2
      HTTPLEGRPIDX: 1
      LETYPE: CLIENT
      TLSIDX: 2
      IPTYPE: IPv4
      IPV4: '172.16.1.5'
      VPNNAME: '_public_'
      PORT: 30116
      TLSFLG: YES
      IPV6: ''
    add_sbiaple_list_2:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      NFTYPE: NFTypeAMF
      DESCRIPTION: 'AMF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    mod_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: TRUE
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      TLS: TRUE
      PRIORITY: 0
    - NRFINSTANCENAME: 'NRF_Instance_1'
      TLS: TRUE
      PRIORITY: 1
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instance_1'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.26.0.7'
      PORT: 8080
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_Instance_1'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'AMF_Instance_0'
    set_licenseswitch_list_2:
    - LICITEM: 'LKV2NFANR01'
      SWITCH: ENABLE
    add_tokenexp_list:
    - SCFGTYPE: BYNFTYPE
      NFTYPE: AMF
      EXPTIME: 180
      FQDN: ''
    set_tokenalg_list:
    - ALGNAME: RS256
    add_nrfkey_list:
    - KEYNAME: 'key001'
      KEYINFO: '-----BEGIN RSA PRIVATE KEY-----#Proc-Type: 4,ENCRYPTED#DEK-Info: AES-128-CBC,457118CBEC11088677D094CBF5C2019C##pYKnL9rTVK9aESrx+88xwjIHFloq1xanxSz3uV8OEins3rqYiauW/r1AjkNAMowK#RWX/16xNCprf6IzDtTOlsiYP0AGbIf7xHA+Eg+Z8WyGlzGwJd6QqVJugl8VUHrTt#gpYp8XZOExRRsymaWsAZihrRNC+DuU+DY7Y2JBL1xfGzUl2ZLQtXODiYgQiD11ZT#2w8uNFnP8BFA9IvjinaGNFkFrIuQzxKXVK8Jx5H9wTPNAzErpJHhb7PdDrG+xxv0#C3j8wVS8jZ+5mXOLpMkr5bSJgxRP8F7ytK4oB/06TQB7Y1fk7Lb8sJllMCAfArNX#2lvU+6DEMTbSX/0xQBwtv5gh2fyJDrdNFA0OoMPOtAjdvpUhl/iEUEeE3zBK0usO#SE74R/kwmGWT1kbRdAsVJDEVJ27hhpg8M3J67qh+mTGxtulizcmdOet7LRCo9OOg#IPi6k1+RpZ6BEbWLojIDmUdpRKCRF3XSs+4kGS5jV0E8vZNFRIZNZ3oJ9bzYfvKd#wtY101Kr3J8rFZmnt2cdfxZYBaT/kjxk7BqoWCow6M/yBSc0/70QBllDgT1RuJIw#0Scjcb8mVkdjfwPhsjiPv3VsaPTQN8tP4y0hX1+lJOzf3kQzqpMWMd2VAYAfx2d9#YwDhvUE/8yH4XA2HmMD0F+NK0zckU4ZT+vyqO/2mx0lmEzpBEp20hecza7CU4+Xz#U0QWURBeOgBrFOKXgXmAwBphaHH2y8PGtUTdSTxPoWJQm0kN0JI35+vsDStpQuzN#GeDtNXAlwx26PEkQlJRJWwhG8T1+wWi8RNMxck856GWE+dZmiwBC6ALUqDfpySj3#z0HlbUiWUFLaaq0ocOJPuQChH3bBwh4KGzf/jRj3NP+62jowuXNr5A6NCeJ1dAZm#ic4jH65BTy/mUnLUeqAEzEk5jNZO2P70Svpbg/Ep8BPbzZMjPnSdBuXMQt47V62K#JVZJdVuCyRwu8FvRSM1NBMi2RyKErjlmIrCWhZwC6fegOBgBwA9vXDqr/7vSJN+B#M4o9JyHabQrMWTWZ9gFuOhRS94RbNEL0mKfgSPX0hvSBIPgTHnCduwrrHS4cCoOO#Nfdst9Grw0Yf+IqC25Egoy52O02iVK/ASY8gB0w85Va2TaJ5VaGnGpYHGxWtUWQY#y7mSeSlQDEVmCA1nvBpykBgFttLPCqca7SyWjl8gvJnNsKS6ks+tKbQeD73xqd2H#UrYxkLI0PzRLovZRyVVBcXbbg6yCH/1C96SSX+a41NE1Ibh2sDLxWneM8O9LlSWp#m8L+qx7l8fB293gYviq9z3fCQbzO8EQ/wbljdgg2tVAkjDRQwU0LaGk0/0hIcktD#u3mBpfnq7I8Y3ZDGuFqP/nsOOKvPx3VaW2IjKV5FOmNZs8Fbxoai1c63KbIUNuFe#/rBfY2v70TVW3GlGOmtWtx1gJ7gYjMNBQzBZXKnTBvzIlYb9ggWRoi9rOEZ9Gl39#JrIE+bluH8U/s8Np/hm1qo1wyCih+11GUnoVREZVL5PKuyd30IVUdFaPHeBs9FKF#S4GYzrBHed0Tq574mnSpZ08Ra72l3rWj+fWSfpXqhyD12S63rOmDPKOBJnT3oWhy#-----END RSA PRIVATE KEY-----#'
      AUTHPWD: '"*****"，NRFKEYIDSW=FUNC_ON，NRFKEYID=nrfkid001'
      NRFKEYIDSW: FUNC_ON
      NRFKEYID: 'nrfkid001'
    act_nrfkey_list:
    - KEYNAME: 'key001'
    set_licenseswitch_list_3:
    - LICITEM: 'LKV2NFANR01'
      SWITCH: ENABLE
    add_tokenexp_list_1:
    - SCFGTYPE: BYNFTYPE
      NFTYPE: AMF
      EXPTIME: 180
      FQDN: ''
    set_tokenalg_list_1:
    - ALGNAME: RS256
    add_nrfkey_list_1:
    - KEYNAME: 'key001'
      KEYINFO: '-----BEGIN RSA PRIVATE KEY-----#Proc-Type: 4,ENCRYPTED#DEK-Info: AES-128-CBC,457118CBEC11088677D094CBF5C2019C##pYKnL9rTVK9aESrx+88xwjIHFloq1xanxSz3uV8OEins3rqYiauW/r1AjkNAMowK#RWX/16xNCprf6IzDtTOlsiYP0AGbIf7xHA+Eg+Z8WyGlzGwJd6QqVJugl8VUHrTt#gpYp8XZOExRRsymaWsAZihrRNC+DuU+DY7Y2JBL1xfGzUl2ZLQtXODiYgQiD11ZT#2w8uNFnP8BFA9IvjinaGNFkFrIuQzxKXVK8Jx5H9wTPNAzErpJHhb7PdDrG+xxv0#C3j8wVS8jZ+5mXOLpMkr5bSJgxRP8F7ytK4oB/06TQB7Y1fk7Lb8sJllMCAfArNX#2lvU+6DEMTbSX/0xQBwtv5gh2fyJDrdNFA0OoMPOtAjdvpUhl/iEUEeE3zBK0usO#SE74R/kwmGWT1kbRdAsVJDEVJ27hhpg8M3J67qh+mTGxtulizcmdOet7LRCo9OOg#IPi6k1+RpZ6BEbWLojIDmUdpRKCRF3XSs+4kGS5jV0E8vZNFRIZNZ3oJ9bzYfvKd#wtY101Kr3J8rFZmnt2cdfxZYBaT/kjxk7BqoWCow6M/yBSc0/70QBllDgT1RuJIw#0Scjcb8mVkdjfwPhsjiPv3VsaPTQN8tP4y0hX1+lJOzf3kQzqpMWMd2VAYAfx2d9#YwDhvUE/8yH4XA2HmMD0F+NK0zckU4ZT+vyqO/2mx0lmEzpBEp20hecza7CU4+Xz#U0QWURBeOgBrFOKXgXmAwBphaHH2y8PGtUTdSTxPoWJQm0kN0JI35+vsDStpQuzN#GeDtNXAlwx26PEkQlJRJWwhG8T1+wWi8RNMxck856GWE+dZmiwBC6ALUqDfpySj3#z0HlbUiWUFLaaq0ocOJPuQChH3bBwh4KGzf/jRj3NP+62jowuXNr5A6NCeJ1dAZm#ic4jH65BTy/mUnLUeqAEzEk5jNZO2P70Svpbg/Ep8BPbzZMjPnSdBuXMQt47V62K#JVZJdVuCyRwu8FvRSM1NBMi2RyKErjlmIrCWhZwC6fegOBgBwA9vXDqr/7vSJN+B#M4o9JyHabQrMWTWZ9gFuOhRS94RbNEL0mKfgSPX0hvSBIPgTHnCduwrrHS4cCoOO#Nfdst9Grw0Yf+IqC25Egoy52O02iVK/ASY8gB0w85Va2TaJ5VaGnGpYHGxWtUWQY#y7mSeSlQDEVmCA1nvBpykBgFttLPCqca7SyWjl8gvJnNsKS6ks+tKbQeD73xqd2H#UrYxkLI0PzRLovZRyVVBcXbbg6yCH/1C96SSX+a41NE1Ibh2sDLxWneM8O9LlSWp#m8L+qx7l8fB293gYviq9z3fCQbzO8EQ/wbljdgg2tVAkjDRQwU0LaGk0/0hIcktD#u3mBpfnq7I8Y3ZDGuFqP/nsOOKvPx3VaW2IjKV5FOmNZs8Fbxoai1c63KbIUNuFe#/rBfY2v70TVW3GlGOmtWtx1gJ7gYjMNBQzBZXKnTBvzIlYb9ggWRoi9rOEZ9Gl39#JrIE+bluH8U/s8Np/hm1qo1wyCih+11GUnoVREZVL5PKuyd30IVUdFaPHeBs9FKF#S4GYzrBHed0Tq574mnSpZ08Ra72l3rWj+fWSfpXqhyD12S63rOmDPKOBJnT3oWhy#-----END RSA PRIVATE KEY-----#'
      AUTHPWD: '"*****"，NRFKEYIDSW=FUNC_ON，NRFKEYID=nrfkid001'
      NRFKEYIDSW: FUNC_ON
      NRFKEYID: 'nrfkid001'
    act_nrfkey_list_1:
    - KEYNAME: 'key001'
    set_licenseswitch_list_4:
    - LICITEM: 'LKV2NFAAM01'
      SWITCH: ENABLE
    mod_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_0'
      OAUTH2SWITCH: ON
    add_httpoauthkey_list:
    - INDEX: 1
      AUTSCENE: NFSERV_ACCESS
      AUZSVRID: 'bf33a517-7789-4637-b675-b3591b0d706b'
      PUBKEYID: 'sndkey001'
      PUBKEY: '-----BEGIN PUBLIC KEY----- MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7DH95dUBhIMk635HF/Ci SbXYwc2olRFjS6Om5MnXtEtn5GC43Fy05agfVCbEqEGXokf5pZ34XPIydBIADfIo 1UfQ2LPerfHyw5nDXg4Y1Ix84bDt35fpwf9u6nS9PDH8vIWbocY79+JjOGQcpaOu OJqUMFdIJG682ffkt80sZQiLahGYNcFrXSpZ54tOSwZlUIGt4zmEkUd1ps8Yc7cP RmETO//aLGPPwg61lEh2W8pGHfUa7AJ3QUAuU1bMVrl4iz3p1RaVopBRO3GL6LBu 4oCPvM17GWoCULTTMKLTnPKMV79oRzyliwX+IPchBgMwv8dmhII0i4uM+BZjHNik FwIDAQAB -----END PUBLIC KEY-----'
      PUBKEYNAME: 'key001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 任务场景1：FQDN为“huawei1.com.apn.epc.mnc456.mcc123.3gppnetwork.org”的SMF通过在NRF上设置访问授权，设定只允许AMF访问。

#### 1.1 2个NRF均配置，NF侧不需要配置。

##### 1.1.1 **配置NRF1**

###### 1.1.1.1 //打开授权访问开关。

```jinja2
{%- for item in set_nrffuncsw_list -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHSW is not none -%}
        AUTHSW={{item.AUTHSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.1.1.2 //在NRF上配置SMF只允许AMF访问。

```jinja2
{%- for item in add_allowedobjname_list -%}
    ADD ALLOWEDOBJNAME:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_allowedobj_list -%}
    ADD ALLOWEDOBJ:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    FQDN="{{item.FQDN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_allowednftypes_list -%}
    ADD ALLOWEDNFTYPES:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    ALLOWEDNFTYPE={{item.ALLOWEDNFTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in cmt_allowplcy_list -%}
    CMT ALLOWPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.CMTTYPE is not none -%}
        CMTTYPE={{item.CMTTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.1.2 **配置NRF2**

###### 1.1.2.1 //打开授权访问开关。

```jinja2
{%- for item in set_nrffuncsw_list_1 -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHSW is not none -%}
        AUTHSW={{item.AUTHSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 1.1.2.2 //在NRF上配置SMF只允许AMF访问。

```jinja2
{%- for item in add_allowedobjname_list_1 -%}
    ADD ALLOWEDOBJNAME:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_allowedobj_list_1 -%}
    ADD ALLOWEDOBJ:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    FQDN="{{item.FQDN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_allowednftypes_list_1 -%}
    ADD ALLOWEDNFTYPES:
    {#- --- 必选参数 --- -#}
    OBJNAME="{{item.OBJNAME}}",
    ALLOWEDNFTYPE={{item.ALLOWEDNFTYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in cmt_allowplcy_list_1 -%}
    CMT ALLOWPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.CMTTYPE is not none -%}
        CMTTYPE={{item.CMTTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 任务场景2：NF与NRF之间使用TLS证书认证，保证传输层安全。

#### 2.1 NRF侧配置

##### 2.1.1 **配置NRF1**

###### 2.1.1.3 //增加NRF的TLS证书场景。

```jinja2
{%- for item in add_tlsscene_list -%}
    ADD TLSSCENE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    SCENE="{{item.SCENE}}",
    TYPE={{item.TYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TYPE=SCENE_NE 时可选 --- -#}
    {%- if item.TYPE == 'SCENE_NE' -%}
        {%- if item.VERIFYLOCALCERT is not none -%}
            VERIFYLOCALCERT={{item.VERIFYLOCALCERT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.1.5 //增加NRF作为服务器端的TLS参数。

```jinja2
{%- for item in add_tlspara_list -%}
    ADD TLSPARA:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    MODE={{item.MODE}},
    CIPHER={{item.CIPHER}},
    PROTOCAL={{item.PROTOCAL}},
    AUTHMODE={{item.AUTHMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        VERIFY={{item.VERIFY}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        NESCENE={{item.NESCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CASCENE={{item.CASCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CRLFLAG={{item.CRLFLAG}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=PSK 时必选 --- -#}
    {%- if item.AUTHMODE == 'PSK' -%}
        PSKGRPIDX={{item.PSKGRPIDX}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYCN is not none -%}
            VERIFYCN={{item.VERIFYCN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=CERT 时可选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        {%- if item.VDEPTH is not none -%}
            VDEPTH={{item.VDEPTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFYCN=Yes 时可选 --- -#}
    {%- if item.VERIFYCN == 'Yes' -%}
        {%- if item.VERIFYCNFULL is not none -%}
            VERIFYCNFULL={{item.VERIFYCNFULL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYIP is not none -%}
            VERIFYIP={{item.VERIFYIP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYSNI is not none -%}
            VERIFYSNI={{item.VERIFYSNI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.1.7 //增加NRF HTTP本端地址组信息。

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

###### 2.1.1.8 //增加NRF作为服务器端的HTTP本端实体。

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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
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

###### 2.1.1.9 //增加NRF作为客户端的HTTP本端实体。

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

###### 2.1.1.10 //增加NRF服务化接口的接入点信息。

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

##### 2.1.2 **配置NRF2**

###### 2.1.2.3 //增加NRF的TLS证书场景。

```jinja2
{%- for item in add_tlsscene_list_2 -%}
    ADD TLSSCENE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    SCENE="{{item.SCENE}}",
    TYPE={{item.TYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TYPE=SCENE_NE 时可选 --- -#}
    {%- if item.TYPE == 'SCENE_NE' -%}
        {%- if item.VERIFYLOCALCERT is not none -%}
            VERIFYLOCALCERT={{item.VERIFYLOCALCERT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.2.5 //增加NRF作为服务器端的TLS参数。

```jinja2
{%- for item in add_tlspara_list_2 -%}
    ADD TLSPARA:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    MODE={{item.MODE}},
    CIPHER={{item.CIPHER}},
    PROTOCAL={{item.PROTOCAL}},
    AUTHMODE={{item.AUTHMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        VERIFY={{item.VERIFY}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        NESCENE={{item.NESCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CASCENE={{item.CASCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CRLFLAG={{item.CRLFLAG}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=PSK 时必选 --- -#}
    {%- if item.AUTHMODE == 'PSK' -%}
        PSKGRPIDX={{item.PSKGRPIDX}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYCN is not none -%}
            VERIFYCN={{item.VERIFYCN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=CERT 时可选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        {%- if item.VDEPTH is not none -%}
            VDEPTH={{item.VDEPTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFYCN=Yes 时可选 --- -#}
    {%- if item.VERIFYCN == 'Yes' -%}
        {%- if item.VERIFYCNFULL is not none -%}
            VERIFYCNFULL={{item.VERIFYCNFULL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYIP is not none -%}
            VERIFYIP={{item.VERIFYIP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYSNI is not none -%}
            VERIFYSNI={{item.VERIFYSNI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

###### 2.1.2.7 //增加NRF HTTP本端地址组信息。

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

###### 2.1.2.8 //增加NRF作为服务器端的HTTP本端实体。

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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
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

###### 2.1.2.9 //增加NRF作为客户端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_3 -%}
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

###### 2.1.2.10 //增加NRF服务化接口的接入点信息。

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

#### 2.2 AMF侧配置

##### 2.2.3 //增加AMF的TLS证书场景。

```jinja2
{%- for item in add_tlsscene_list_4 -%}
    ADD TLSSCENE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    SCENE="{{item.SCENE}}",
    TYPE={{item.TYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TYPE=SCENE_NE 时可选 --- -#}
    {%- if item.TYPE == 'SCENE_NE' -%}
        {%- if item.VERIFYLOCALCERT is not none -%}
            VERIFYLOCALCERT={{item.VERIFYLOCALCERT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.2.5 //增加AMF作为服务器端的TLS参数。

```jinja2
{%- for item in add_tlspara_list_4 -%}
    ADD TLSPARA:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    MODE={{item.MODE}},
    CIPHER={{item.CIPHER}},
    PROTOCAL={{item.PROTOCAL}},
    AUTHMODE={{item.AUTHMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        VERIFY={{item.VERIFY}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        NESCENE={{item.NESCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CASCENE={{item.CASCENE}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        CRLFLAG={{item.CRLFLAG}},
    {%- endif -%}
    {#- --- 条件必选：AUTHMODE=PSK 时必选 --- -#}
    {%- if item.AUTHMODE == 'PSK' -%}
        PSKGRPIDX={{item.PSKGRPIDX}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYCN is not none -%}
            VERIFYCN={{item.VERIFYCN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：AUTHMODE=CERT 时可选 --- -#}
    {%- if item.AUTHMODE == 'CERT' -%}
        {%- if item.VDEPTH is not none -%}
            VDEPTH={{item.VDEPTH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFYCN=Yes 时可选 --- -#}
    {%- if item.VERIFYCN == 'Yes' -%}
        {%- if item.VERIFYCNFULL is not none -%}
            VERIFYCNFULL={{item.VERIFYCNFULL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYIP is not none -%}
            VERIFYIP={{item.VERIFYIP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：VERIFY=Yes 时可选 --- -#}
    {%- if item.VERIFY == 'Yes' -%}
        {%- if item.VERIFYSNI is not none -%}
            VERIFYSNI={{item.VERIFYSNI}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 2.2.7 //增加AMF HTTP本端地址组信息。

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

##### 2.2.8 //增加AMF作为服务器端的HTTP本端实体。

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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
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

##### 2.2.9 //增加AMF作为客户端的HTTP本端实体。

```jinja2
{%- for item in add_httple_list_5 -%}
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

##### 2.2.10 //增加AMF服务化接口的接入点信息。

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

##### 2.2.12 //场景1：已对接NRF，修改已存在的NRF实例支持TLS。

```jinja2
{%- if is_scenario_existing_nrf -%}
    {%- for item in mod_nrf_list -%}
        MOD NRF:
        {#- --- 必选参数 --- -#}
        NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TLS is not none -%}
            TLS={{item.TLS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.14 //配置NRF1信息。

```jinja2
{%- if is_scenario_new_nrf -%}
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

##### 2.2.15 //配置NRF1的地址信息，对接的NRF地址信息为NRF本端端点作为服务端的IP。

```jinja2
{%- if is_scenario_new_nrf -%}
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

##### 2.2.16 //配置NRF1协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
{%- if is_scenario_new_nrf -%}
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

##### 2.2.20 //打开NF注册/更新/去注册、发现与NRF交互的基本功能开关。

```jinja2
{%- if is_scenario_new_nrf -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.21 //AMF服务就绪后，向NRF注册REGISTERED状态。

```jinja2
{%- if is_scenario_new_nrf -%}
    {%- for item in act_nfonline_list -%}
        ACT NFONLINE:
        {#- --- 必选参数 --- -#}
        NFINSTANCENAME="{{item.NFINSTANCENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 任务场景3：AMF向NRF申请Token，NF间认证，保证应用层安全。公私钥对目前是客户提前准备提供。

#### 3.1 NRF侧配置

##### 3.1.1 **配置NRF1**

###### 3.1.1.1 //打开NF认证的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_2 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 3.1.1.2 //可选：为指定的NF添加Token有效期。

```jinja2
{%- if is_optional_token_expiry -%}
    {%- for item in add_tokenexp_list -%}
        ADD TOKENEXP:
        {#- --- 必选参数 --- -#}
        SCFGTYPE={{item.SCFGTYPE}},
        EXPTIME={{item.EXPTIME}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SCFGTYPE=BYNFTYPE 时必选 --- -#}
        {%- if item.SCFGTYPE == 'BYNFTYPE' -%}
            NFTYPE={{item.NFTYPE}},
        {%- endif -%}
        {#- --- 条件必选：SCFGTYPE=BYFQDN 时必选 --- -#}
        {%- if item.SCFGTYPE == 'BYFQDN' -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.1.1.3 //配置Access Token的签名算法为"RS256(RS256)"，该签名算法用于NF认证过程中校验服务请求方携带的token的数字签名是否合法。

```jinja2
{%- for item in set_tokenalg_list -%}
    SET TOKENALG:
    {#- --- 必选参数 --- -#}
    ALGNAME={{item.ALGNAME}},
    ;
{%- endfor -%}
```

###### 3.1.1.4 //配置NRF生成的Access Token签名的私钥，该私钥为NF认证过程中被校验的内容，需要与NF上的公钥配对。密钥口令请以实际规划为准，此参数输入时界面做了匿名化，务必保证输入参数与规划一致。

```jinja2
{%- for item in add_nrfkey_list -%}
    ADD NRFKEY:
    {#- --- 必选参数 --- -#}
    KEYNAME="{{item.KEYNAME}}",
    KEYINFO="{{item.KEYINFO}}",
    AUTHPWD="{{item.AUTHPWD}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NRFKEYIDSW is not none -%}
        NRFKEYIDSW={{item.NRFKEYIDSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NRFKEYIDSW=FUNC_ON 时必选 --- -#}
    {%- if item.NRFKEYIDSW == 'FUNC_ON' -%}
        NRFKEYID="{{item.NRFKEYID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in act_nrfkey_list -%}
    ACT NRFKEY:
    {#- --- 必选参数 --- -#}
    KEYNAME="{{item.KEYNAME}}",
    ;
{%- endfor -%}
```

##### 3.1.2 **配置NRF2**

###### 3.1.2.1 //打开NF认证的License配置开关，适用于NRF。

```jinja2
{%- for item in set_licenseswitch_list_3 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

###### 3.1.2.2 //可选：为指定的NF添加Token有效期。

```jinja2
{%- if is_optional_token_expiry -%}
    {%- for item in add_tokenexp_list_1 -%}
        ADD TOKENEXP:
        {#- --- 必选参数 --- -#}
        SCFGTYPE={{item.SCFGTYPE}},
        EXPTIME={{item.EXPTIME}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SCFGTYPE=BYNFTYPE 时必选 --- -#}
        {%- if item.SCFGTYPE == 'BYNFTYPE' -%}
            NFTYPE={{item.NFTYPE}},
        {%- endif -%}
        {#- --- 条件必选：SCFGTYPE=BYFQDN 时必选 --- -#}
        {%- if item.SCFGTYPE == 'BYFQDN' -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.1.2.3 //配置Access Token的签名算法为"RS256(RS256)"，该签名算法用于NF认证过程中校验服务请求方携带的token的数字签名是否合法。

```jinja2
{%- for item in set_tokenalg_list_1 -%}
    SET TOKENALG:
    {#- --- 必选参数 --- -#}
    ALGNAME={{item.ALGNAME}},
    ;
{%- endfor -%}
```

###### 3.1.2.4 //配置NRF生成的Access Token签名的私钥，该私钥为NF认证过程中被校验的内容，需要与NF上的公钥配对。密钥口令请以实际规划为准，此参数输入时界面做了匿名化，务必保证输入参数与规划一致。

```jinja2
{%- for item in add_nrfkey_list_1 -%}
    ADD NRFKEY:
    {#- --- 必选参数 --- -#}
    KEYNAME="{{item.KEYNAME}}",
    KEYINFO="{{item.KEYINFO}}",
    AUTHPWD="{{item.AUTHPWD}}",
    {#- --- 可选参数 --- -#}
    {%- if item.NRFKEYIDSW is not none -%}
        NRFKEYIDSW={{item.NRFKEYIDSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NRFKEYIDSW=FUNC_ON 时必选 --- -#}
    {%- if item.NRFKEYIDSW == 'FUNC_ON' -%}
        NRFKEYID="{{item.NRFKEYID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in act_nrfkey_list_1 -%}
    ACT NRFKEY:
    {#- --- 必选参数 --- -#}
    KEYNAME="{{item.KEYNAME}}",
    ;
{%- endfor -%}
```

#### 3.2 AMF侧配置

##### 3.2.1 //打开NF认证的License配置开关，适用于AMF。

```jinja2
{%- for item in set_licenseswitch_list_4 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

##### 3.2.2 //打开AMF的Oauth2 Token鉴权。

```jinja2
{%- for item in mod_nrfpara_list -%}
    MOD NRFPARA:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.OAUTH2SWITCH is not none -%}
        OAUTH2SWITCH={{item.OAUTH2SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.3 //在AMF侧配置公钥信息，该公钥用于NF认证过程中校验服务请求方携带的token的数字签名是否合法，需要与NRF上的私钥配对。

```jinja2
{%- for item in add_httpoauthkey_list -%}
    ADD HTTPOAUTHKEY:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    AUTSCENE={{item.AUTSCENE}},
    AUZSVRID="{{item.AUZSVRID}}",
    PUBKEY="{{item.PUBKEY}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PUBKEYID is not none -%}
        PUBKEYID="{{item.PUBKEYID}}",
    {%- endif -%}
    {%- if item.PUBKEYNAME is not none -%}
        PUBKEYNAME="{{item.PUBKEYNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

