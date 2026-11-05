---
id: ''
name: 激活SBI接口加密(PSK)
ne_type: UDG
type: feature
description: 为降低网络安全风险，建议开启SBI接口加密特性。  适用于UPF。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","业务安全配置","激活SBI接口加密(PSK)"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为降低网络安全风险，建议开启SBI接口加密特性。适用于UPF。

## 必备事项
前提条件

已规划全网预共享密钥ID和预共享密钥值。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_tlspskgrp_list:
      type: items
      properties:
        PSKGRPIDX:
          name: 'PSK组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tlspsk_list:
      type: items
      properties:
        PSKIDX:
          name: 'PSK索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSKGRPIDX:
          name: 'PSK组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKID:
          name: '预共享密钥ID'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '该参数与“HTTP模式”参数组合，唯一标识一个预共享密钥记录，不能重复配置，而且大小写不敏感。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKTYPE:
          name: 'PSK内容类型'
          type: string
          enum:
          - HEXADECIMAL
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKVALUE:
          name: '预共享密钥值'
          type: string
          minLength: 16
          maxLength: 128
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tlspsk_list_1:
      type: items
      properties:
        PSKIDX:
          name: 'PSK索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSKGRPIDX:
          name: 'PSK组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '-'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKID:
          name: '预共享密钥ID'
          type: string
          minLength: 1
          maxLength: 128
          required: true
          description: '该参数与“HTTP模式”参数组合，唯一标识一个预共享密钥记录，不能重复配置，而且大小写不敏感。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKTYPE:
          name: 'PSK内容类型'
          type: string
          enum:
          - HEXADECIMAL
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PSKVALUE:
          name: '预共享密钥值'
          type: string
          minLength: 16
          maxLength: 128
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
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
          description: '与ADD HTTPLE中配置的TLS参数索引保持一致。'
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
        AUTHMODE:
          name: '身份验证方式'
          type: string
          enum:
          - CERT
          - PSK
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: CERT
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
        PSKGRPIDX:
          name: 'PSK组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '必须与ADD TLSPSKGRP中配置的组索引保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRLFLAG:
          name: 'CRL是否开启'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: integer
          minimum: 1
          maximum: 254
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
        VERIFY:
          name: '是否验证对端证书'
          type: string
          enum:
          - Yes
          - No
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
          description: '与ADD HTTPLE中配置的TLS参数索引保持一致。'
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
        AUTHMODE:
          name: '身份验证方式'
          type: string
          enum:
          - CERT
          - PSK
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: CERT
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
        PSKGRPIDX:
          name: 'PSK组索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: '必须与ADD TLSPSKGRP中配置的组索引保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CASCENE:
          name: 'CA证书场景'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CRLFLAG:
          name: 'CRL是否开启'
          type: string
          enum:
          - CRL_OFF
          - CRL_ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NESCENE:
          name: '设备证书场景'
          type: integer
          minimum: 1
          maximum: 254
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
        VERIFY:
          name: '是否验证对端证书'
          type: string
          enum:
          - Yes
          - No
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
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
  examples:
    add_tlspskgrp_list:
    - PSKGRPIDX: 1
      DESC: 'pskgrp_desc'
    add_tlspsk_list:
    - PSKIDX: 1
      PSKGRPIDX: 1
      MODE: Server
      PSKID: 'psk_01'
      PSKTYPE: HEXADECIMAL
      PSKVALUE: '485750534b56414c554554455354'
      DESC: 'pskgrp_desc'
    add_tlspsk_list_1:
    - PSKIDX: 2
      PSKGRPIDX: 1
      MODE: Client
      PSKID: 'psk_01'
      PSKTYPE: HEXADECIMAL
      PSKVALUE: '485750534b56414c554554455354'
      DESC: 'pskgrp_desc'
    add_tlspara_list:
    - INDEX: 1
      MODE: Server
      AUTHMODE: PSK
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_AES_128_CCM_SHA256-1&TLS_AES_128_CCM_8_SHA256-1&TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_GCM_SHA256-1&TLS_DHE_PSK_WITH_AES_256_GCM_SHA384-1&TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_CCM-1&TLS_DHE_PSK_WITH_AES_256_CCM-1
      PROTOCAL: TLS1_2-0&TLS1_3-1
      PSKGRPIDX: 1
      CASCENE: ''
      CRLFLAG: ''
      NESCENE: ''
      VDEPTH: ''
      VERIFY: ''
    add_tlspara_list_1:
    - INDEX: 2
      MODE: Client
      AUTHMODE: PSK
      CIPHER: TLS_DHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_DHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_DSS_WITH_AES_128_GCM_SHA256-1&TLS_DHE_DSS_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1&TLS_DHE_RSA_WITH_AES_128_CCM-1&TLS_DHE_RSA_WITH_AES_256_CCM-1&TLS_DHE_RSA_WITH_AES_128_CCM_8-1&TLS_DHE_RSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_AES_128_CCM_SHA256-1&TLS_AES_128_CCM_8_SHA256-1&TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_GCM_SHA256-1&TLS_DHE_PSK_WITH_AES_256_GCM_SHA384-1&TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256-1&TLS_DHE_PSK_WITH_AES_128_CCM-1&TLS_DHE_PSK_WITH_AES_256_CCM-1
      PROTOCAL: TLS1_2-0&TLS1_3-1
      PSKGRPIDX: 1
      CASCENE: ''
      CRLFLAG: ''
      NESCENE: ''
      VDEPTH: ''
      VERIFY: ''
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
      PORT: 30116
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

### 1 配置UPF的TLS参数和相关服务化接口参数。

#### 1.1 登录OM Portal。

#### 1.2 增加UPF的PSK组信息。

```jinja2
{%- for item in add_tlspskgrp_list -%}
    ADD TLSPSKGRP:
    {#- --- 必选参数 --- -#}
    PSKGRPIDX={{item.PSKGRPIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 增加UPF作为服务端的PSK参数。其中，“模式”配置为“SERVER”，"**PSK组索引**"与步骤 1.b中的"**PSK组索引**"一致。"**预共享密钥ID**"和"**预共享密钥值**"全网规划。

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_tlspsk_list -%}
        ADD TLSPSK:
        {#- --- 必选参数 --- -#}
        PSKIDX={{item.PSKIDX}},
        PSKGRPIDX={{item.PSKGRPIDX}},
        MODE={{item.MODE}},
        PSKID="{{item.PSKID}}",
        PSKTYPE={{item.PSKTYPE}},
        PSKVALUE="{{item.PSKVALUE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 增加UPF作为客户端的PSK参数。其中，“模式”配置为“CLIENT”，"**PSK组索引**"与步骤 1.b中的"**PSK组索引**"一致。"**预共享密钥ID**"和"**预共享密钥值**"全网规划。

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_tlspsk_list_1 -%}
        ADD TLSPSK:
        {#- --- 必选参数 --- -#}
        PSKIDX={{item.PSKIDX}},
        PSKGRPIDX={{item.PSKGRPIDX}},
        MODE={{item.MODE}},
        PSKID="{{item.PSKID}}",
        PSKTYPE={{item.PSKTYPE}},
        PSKVALUE="{{item.PSKVALUE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.DESC is not none -%}
            DESC="{{item.DESC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 增加UPF作为服务端的TLS参数。其中，“模式”配置为“SERVER”，"**身份验证方式**"配置为"PSK"，"**PSK组索引**"与步骤 1.b中的"**PSK组索引**"一致。"**加密套件集合**"勾选TLS1.2的PSK相关加密套件或TLS1.3的加密套件。

```jinja2
{%- if is_scenario_as_server -%}
    {%- for item in add_tlspara_list -%}
        ADD TLSPARA:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        MODE={{item.MODE}},
        AUTHMODE={{item.AUTHMODE}},
        CIPHER={{item.CIPHER}},
        PROTOCAL={{item.PROTOCAL}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTHMODE=PSK 时必选 --- -#}
        {%- if item.AUTHMODE == 'PSK' -%}
            PSKGRPIDX={{item.PSKGRPIDX}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            CASCENE={{item.CASCENE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            CRLFLAG={{item.CRLFLAG}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            NESCENE={{item.NESCENE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            VERIFY={{item.VERIFY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AUTHMODE=CERT 时可选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            {%- if item.VDEPTH is not none -%}
                VDEPTH={{item.VDEPTH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 增加UPF作为客户端的TLS参数。其中，“模式”配置为“CLIENT”，"**身份验证方式**"配置为"PSK"，"**PSK组索引**"与步骤 1.b中的"**PSK组索引**"一致。"**加密套件集合**"勾选TLS1.2的PSK相关加密套件或TLS1.3的加密套件。

```jinja2
{%- if is_scenario_as_client -%}
    {%- for item in add_tlspara_list_1 -%}
        ADD TLSPARA:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        MODE={{item.MODE}},
        AUTHMODE={{item.AUTHMODE}},
        CIPHER={{item.CIPHER}},
        PROTOCAL={{item.PROTOCAL}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AUTHMODE=PSK 时必选 --- -#}
        {%- if item.AUTHMODE == 'PSK' -%}
            PSKGRPIDX={{item.PSKGRPIDX}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            CASCENE={{item.CASCENE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            CRLFLAG={{item.CRLFLAG}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            NESCENE={{item.NESCENE}},
        {%- endif -%}
        {#- --- 条件必选：AUTHMODE=CERT 时必选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            VERIFY={{item.VERIFY}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：AUTHMODE=CERT 时可选 --- -#}
        {%- if item.AUTHMODE == 'CERT' -%}
            {%- if item.VDEPTH is not none -%}
                VDEPTH={{item.VDEPTH}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.7 增加UPF HTTP本端地址组信息。

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

#### 1.8 增加逻辑IP地址。"**IPv4地址"**、"**IPv6地址**"以及**"VPN实例名称"**全网规划。

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

#### 1.9 增加UPF作为服务端的HTTP本端实体。其中，“本端实体类型”配置为“SERVER”，“TLS索引”需要与步骤 1.e中配置的“索引”相同。"**IPv4地址"**、"**IPv6地址**"以及**"VPN名称"**分别与步骤 1.h。中保持一致。

```jinja2
{%- if is_scenario_as_server -%}
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
{%- endif -%}
```

#### 1.10 增加UPF作为客户端的HTTP本端实体。其中，“本端实体类型”配置为“CLIENT”，“TLS索引”需要与步骤 1.f中配置的“索引”相同。"**IPv4地址"**、"**IPv6地址**"以及**"VPN名称"**分别与步骤 1.h。中保持一致。

```jinja2
{%- if is_scenario_as_client -%}
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
{%- endif -%}
```

#### 1.11 增加UPF服务化接口的接入点信息。

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

