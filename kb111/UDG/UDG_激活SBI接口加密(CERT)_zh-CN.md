---
id: ''
name: 激活SBI接口加密(CERT)
ne_type: UDG
type: feature
description: 为降低网络安全风险，建议开启SBI接口加密功能。  适用于UPF。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","业务安全配置","激活SBI接口加密(CERT)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为降低网络安全风险，建议开启SBI接口加密功能。适用于UPF。

## 必备事项
前提条件

已获取证书：商用证书，由客户申请。

* 如需开启证书域名校验功能，则证书中的域名必须与实际域名保持一致。否则将导致域名校验失败，从而导致NF间建链失败。
* 华为建议客户通过部署PKI系统对现网设备、软件签发证书并做好证书的生命周期管理（为保证安全性推荐使用短有效期的证书）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCENE:
          name: '证书使用场景名称'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: ''
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: '模式'
          type: string
          enum:
          - Client
          - Server
          required: true
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCAL:
          name: '协议版本'
          type: string
          required: true
          description: ''
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
    add_tlspara_list_1:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MODE:
          name: '模式'
          type: string
          enum:
          - Client
          - Server
          required: true
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROTOCAL:
          name: '协议版本'
          type: string
          required: true
          description: ''
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
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
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSPARA**中配置的“索引”匹配。'
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
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '用于指定关联的TLSPARA的索引，需要与**ADD TLSPARA**中配置的“索引”匹配。'
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
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
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
          description: ''
          data_source: ''
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HttpLEGRP索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
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
  examples:
    add_tlsscene_list:
    - INDEX: 1
      SCENE: 'NESCENE'
      TYPE: SCENE_NE
      DESC: 'UPFNESCENE'
      VERIFYLOCALCERT: ''
    add_tlspara_list:
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
    add_tlspara_list_1:
    - INDEX: 2
      MODE: Client
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
    add_httplegrp_list:
    - INDEX: 1
      DESC: 'UPF'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.16.1.5'
      VPNINSTNAME: '_public_'
      DESC: 'test'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      LETYPE: SERVER
      PORT: 443
      TLSFLG: YES
      TLSIDX: 1
      IPTYPE: IPv4
      IPV4: '10.16.1.5'
      VPNNAME: '_public_'
      IPV6: ''
    add_httple_list_1:
    - INDEX: 2
      HTTPLEGRPIDX: 1
      LETYPE: CLIENT
      TLSIDX: 2
      IPTYPE: IPv4
      IPV4: '10.16.1.6'
      VPNNAME: '_public_'
      TLSFLG: YES
      IPV6: ''
      PORT: ''
    add_sbiaple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      NFTYPE: NFTypeUPF
      DESCRIPTION: 'UPF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 上传证书文件。

#### 1.1 登录OM Portal。

#### 1.2 选择“安全 > 证书管理>证书与证书集管理”，单击“上传证书”，分别上传CA证书和设备证书文件（包含设备证书私钥文件）。

#### 1.3 （可选）如果存在CA证书对应的证书吊销列表（CRL文件），则根据需要上传CRL文件。

#### 选择“安全 > 证书管理>上传证书吊销列表”，单击“上传证书吊销列表”，上传CRL文件。

#### CA证书与CRL文件一一对应，如果存在多个CA证书，则需要分别上传其对应的CRL文件。

#### 为了提升系统安全性，避免使用已被吊销的证书，建议开启证书吊销列表（CRL）功能。

### 2 增加TLS证书场景。

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

### 3 关联证书业务场景。

#### 3.1 选择“安全 > 证书管理 > 证书应用场景关联”，在证书场景列表中选择步骤 2中增加的证书场景，单击“关联证书”。

#### 3.2 选择需要与该场景关联的证书，比如设备证书场景则选择对应的设备证书进行关联，CA证书场景则选择对应的CA证书和CRL文件进行关联。

#### CA证书与CRL文件一一对应。当一个证书场景关联了多个CA证书时，如果需要启用CRL功能，那么还需要一一关联这些CA证书所对应的CRL文件。

### 4 配置UPF的TLS参数和相关服务化接口参数。

#### 4.1 进入“MML命令行-UDG”窗口。

#### 4.2 增加UPF作为服务器端的TLS参数。其中，“模式”配置为“SERVER”，“设备证书场景”和“CA证书场景”与步骤 2中配置的对应证书场景“索引”一致。

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

#### 4.3 增加UPF作为客户端的TLS参数。其中，“模式”配置为“CLIENT”，“设备证书场景”和“CA证书场景”与步骤 2中配置的对应证书场景“索引”一致。

```jinja2
{%- for item in add_tlspara_list_1 -%}
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

#### 4.4 增加UPF HTTP本端地址组信息。

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

#### 4.5 增加逻辑IP地址。"**IPv4地址"**、"**IPv6地址**"以及**"VPN实例名称"**全网规划。

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

#### 4.6 增加UPF作为服务器端的HTTP本端实体。其中，“本端实体类型”配置为“SERVER”，“TLS索引”需要与步骤 4.b中配置的“索引”相同。

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

#### 4.7 增加UPF作为客户端的HTTP本端实体。其中，“本端实体类型”配置为“CLIENT”，“TLS索引”需要与步骤 4.c中配置的“索引”相同。

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

#### 4.8 增加UPF服务化接口的接入点信息。

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

