---
id: ''
name: 配置HTTP/RTSP头增强加密策略及防欺诈策略
ne_type: UDG
type: feature
description: 如果需要使用HTTP/RTSP头增强功能，建议使用如下方式进行安全加固，在Web Server/Streaming Server支持加密信息解析的情况下，将用户的IMSI、MSISDN、SGSN-IP等信息加密后添加到报文头传递给Web Server/Streaming Server。同时为了防止用户使用欺诈的头增强信息进行业务，需要配置HTTP/RTSP头增强防欺诈策略。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","业务安全配置","配置HTTP/RTSP头增强加密策略及防欺诈策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
如果需要使用HTTP/RTSP头增强功能，建议使用如下方式进行安全加固，在Web Server/Streaming Server支持加密信息解析的情况下，将用户的IMSI、MSISDN、SGSN-IP等信息加密后添加到报文头传递给Web Server/Streaming Server。同时为了防止用户使用欺诈的头增强信息进行业务，需要配置HTTP/RTSP头增强防欺诈策略。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110261 HTTP头增强、GWFD-110262 RTSP头增强和HTTP头防欺诈。
* 操作员已经获取到运营商对使用头增强特性的插入字段规划、字段前缀名称规划以及需要头增强信息的Web Server/Streaming Server的URL等信息。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_headen_list:
      type: items
      properties:
        HEADERENNAME:
          name: '头增强名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '**ADD HEADEN**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DATATYPE:
          name: '数据类型'
          type: string
          enum:
          - APN
          - BILLINGTYPE
          - CHGCHAR1
          - CHGCHAR2
          - CHGCHAR3
          - CHGID
          - GGSNIP1
          - GGSNIP2
          - GGSNIP3
          - IMEI1
          - IMEI2
          - IMEI3
          - IMSI1
          - IMSI2
          - IMSI3
          - MCC
          - MNC
          - MSIP1
          - MSIP2
          - MSIP3
          - MSISDN1
          - MSISDN2
          - MSISDN3
          - MULTIPARA1
          - MULTIPARA2
          - MULTIPARA3
          - RANDNUM
          - RAT1
          - RAT2
          - RAT3
          - ROAMING1
          - ROAMING2
          - ROAMING3
          - SESSIONID
          - SGSNIP1
          - SGSNIP2
          - SGSNIP3
          - SGSN_MCC_MNC1
          - SGSN_MCC_MNC2
          - SGSN_MCC_MNC3
          - SUBPROFILE1
          - SUBPROFILE2
          - SUBPROFILE3
          - TIMESTAMP1
          - TIMESTAMP2
          - TIMESTAMP3
          - ULI1
          - ULI2
          - ULI3
          - UPIPV4
          - UPIPV6
          - USERDEF1
          - USERDEF2
          - USERDEF3
          - USERDEF4
          - USERPROFALIAS
          - ZONEID
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREFIXNAME:
          name: '前缀名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENCRYALGORI:
          name: '加密算法标识'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - MD5
          - NONE
          - RC4
          - RSA1024
          - RSA2048
          - RSA3072
          - SHA256
          required: false
          description: '推荐使用AES256加密算法。'
          data_source: '与对端协商'
          pattern: ''
          default: AES128_GCM
        PSWDKEY:
          name: '密码'
          type: string
          minLength: 1
          maxLength: 256
          required: false
          description: '对头增强信息进行加密，配置对应的密钥，且密钥建议使用密文显示。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSWDKEYCONFIRM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 256
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ANTIFRAUD:
          name: '防欺诈标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '为了防止用户使用欺诈的头增强信息进行业务，建议开启头增强防欺诈功能。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        CCFORMAT:
          name: 'Charge Characteristic格式'
          type: string
          enum:
          - DECIMAL
          - HEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DECIMAL
        ERRFLAGNAME:
          name: '错误码前缀名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRAYLIST:
          name: '灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADERFLDLEN:
          name: '头域长度'
          type: integer
          minimum: 31
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEITYPE:
          name: 'IMEI类型'
          type: string
          enum:
          - IMEI
          - TAC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMEI
        PARADATATYPE1:
          name: '参数1的数据类型'
          type: string
          enum:
          - MSIP
          - MSISDN
          - NONE
          - SGSNIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        PARADATATYPE2:
          name: '参数2的数据类型'
          type: string
          enum:
          - MSIP
          - MSISDN
          - NONE
          - SGSNIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        PARADATATYPE3:
          name: '参数3的数据类型'
          type: string
          enum:
          - MSIP
          - MSISDN
          - NONE
          - SGSNIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        REMOVEDMCC:
          name: '需去除的移动国家码'
          type: string
          minLength: 0
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEPARATOR:
          name: '多参数拼接分隔符'
          type: string
          minLength: 0
          maxLength: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSPRECISION:
          name: '时间精度'
          type: string
          enum:
          - MILLISECOND
          - SECOND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERDEFINEVAL:
          name: '用户自定义值'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHERTXTENCODE:
          name: '头增强密文编码方式'
          type: string
          enum:
          - ASCII
          - BASE64
          - INHERIT
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        RC4KEYMD5EN:
          name: 'RC4的密钥MD5 Hash使能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        RSA1024METHOD:
          name: 'RSA1024加密方式'
          type: string
          enum:
          - DYNM
          - STAT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STAT
        RSA1024NAME:
          name: 'RSA1024公钥名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSA1024PADDINGTYPE:
          name: 'RSA1024加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。'
          type: string
          enum:
          - RSA_NO_PADDING
          - RSA_PKCS1_OAEP_PADDING
          - RSA_PKCS1_PADDING
          - RSA_SSLV23_PADDING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RSA_PKCS1_OAEP_PADDING
        RSA2048METHOD:
          name: 'RSA2048加密方式'
          type: string
          enum:
          - DYNM
          - STAT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STAT
        RSA2048NAME:
          name: 'RSA2048公钥名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSA2048PADDINGTYPE:
          name: 'RSA2048加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。'
          type: string
          enum:
          - RSA_NO_PADDING
          - RSA_PKCS1_OAEP_PADDING
          - RSA_PKCS1_PADDING
          - RSA_SSLV23_PADDING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RSA_PKCS1_OAEP_PADDING
        RSA3072METHOD:
          name: 'RSA3072加密方式'
          type: string
          enum:
          - DYNM
          - STAT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: STAT
        RSA3072NAME:
          name: 'RSA3072名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSA3072PADDINGTYPE:
          name: 'RSA3072加密明文填充模式，推荐使用RSA_PKCS1_OAEP_PADDING。'
          type: string
          enum:
          - RSA_NO_PADDING
          - RSA_PKCS1_OAEP_PADDING
          - RSA_PKCS1_PADDING
          - RSA_SSLV23_PADDING
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RSA_PKCS1_OAEP_PADDING
        SALTSW:
          name: '是否添加盐值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
  examples:
    add_headen_list:
    - HEADERENNAME: 'header_test'
      DATATYPE: IMSI1
      PREFIXNAME: 'X-imsi'
      ENCRYALGORI: AES256
      PSWDKEY: 'XXXXXX'
      PSWDKEYCONFIRM: 'XXXXXX'
      ANTIFRAUD: ENABLE
      CCFORMAT: DECIMAL
      ERRFLAGNAME: ''
      GRAYLIST: DISABLE
      HEADERFLDLEN: ''
      IMEITYPE: IMEI
      PARADATATYPE1: NONE
      PARADATATYPE2: NONE
      PARADATATYPE3: NONE
      REMOVEDMCC: ''
      SEPARATOR: ''
      TSPRECISION: ''
      USERDEFINEVAL: ''
      CIPHERTXTENCODE: INHERIT
      RC4KEYMD5EN: INHERIT
      RSA1024METHOD: STAT
      RSA1024NAME: ''
      RSA1024PADDINGTYPE: RSA_PKCS1_OAEP_PADDING
      RSA2048METHOD: STAT
      RSA2048NAME: ''
      RSA2048PADDINGTYPE: RSA_PKCS1_OAEP_PADDING
      RSA3072METHOD: STAT
      RSA3072NAME: ''
      RSA3072PADDINGTYPE: RSA_PKCS1_OAEP_PADDING
      SALTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置HTTP/RTSP头增强动作及头防欺诈动作。

### 头增强的具体配置请参见激活HTTP头增强、激活RTSP头增强；头防欺诈的具体配置请参见激活HTTP头防欺诈。

### 当要在报文头中插入用户的IMSI、MSISDN、SGSN IP等信息时，建议配置为AES256加密方式，配置对应的密钥，且密钥使用密文显示。为了防止用户使用欺诈的头增强信息进行业务，同时开启头防欺诈功能。

```jinja2
{%- for item in add_headen_list -%}
    ADD HEADEN:
    {#- --- 必选参数 --- -#}
    HEADERENNAME="{{item.HEADERENNAME}}",
    DATATYPE={{item.DATATYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/MSIP1/MSIP2/MSIP3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/UPIPV4/UPIPV6/RANDNUM/MULTIPARA1/MULTIPARA2/MULTIPARA3 时必选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'MSIP1', 'MSIP2', 'MSIP3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'UPIPV4', 'UPIPV6', 'RANDNUM', 'MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        PREFIXNAME="{{item.PREFIXNAME}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEY="{{item.PSWDKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEYCONFIRM="{{item.PSWDKEYCONFIRM}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=RSA1024 时必选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA1024' -%}
        RSA1024NAME="{{item.RSA1024NAME}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=RSA2048 时必选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA2048' -%}
        RSA2048NAME="{{item.RSA2048NAME}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=RSA3072 时必选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA3072' -%}
        RSA3072NAME="{{item.RSA3072NAME}}",
    {%- endif -%}
    {#- --- 条件必选：DATATYPE=USERDEF1/USERDEF2/USERDEF3/USERDEF4 时必选 --- -#}
    {%- if item.DATATYPE in ['USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4'] -%}
        USERDEFINEVAL="{{item.USERDEFINEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/APN/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/MSIP1/MSIP2/MSIP3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/UPIPV4/UPIPV6/MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'APN', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'MSIP1', 'MSIP2', 'MSIP3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'UPIPV4', 'UPIPV6', 'MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.ENCRYALGORI is not none -%}
            ENCRYALGORI={{item.ENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/MSIP1/MSIP2/MSIP3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/UPIPV4/UPIPV6/RANDNUM/MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'MSIP1', 'MSIP2', 'MSIP3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'UPIPV4', 'UPIPV6', 'RANDNUM', 'MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.ANTIFRAUD is not none -%}
            ANTIFRAUD={{item.ANTIFRAUD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=CHGCHAR1/CHGCHAR2/CHGCHAR3 时可选 --- -#}
    {%- if item.DATATYPE in ['CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3'] -%}
        {%- if item.CCFORMAT is not none -%}
            CCFORMAT={{item.CCFORMAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/RC4/AES128/AES256/RSA1024/RSA2048/SHA256/RSA3072/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'RSA1024', 'RSA2048', 'SHA256', 'RSA3072', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        {%- if item.CIPHERTXTENCODE is not none -%}
            CIPHERTXTENCODE={{item.CIPHERTXTENCODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=ZONEID 时可选 --- -#}
    {%- if item.DATATYPE == 'ZONEID' -%}
        {%- if item.ERRFLAGNAME is not none -%}
            ERRFLAGNAME="{{item.ERRFLAGNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/MSIP1/MSIP2/MSIP3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/UPIPV4/UPIPV6/MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'MSIP1', 'MSIP2', 'MSIP3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'UPIPV4', 'UPIPV6', 'MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.GRAYLIST is not none -%}
            GRAYLIST={{item.GRAYLIST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=USERPROFALIAS 时可选 --- -#}
    {%- if item.DATATYPE == 'USERPROFALIAS' -%}
        {%- if item.HEADERFLDLEN is not none -%}
            HEADERFLDLEN={{item.HEADERFLDLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=IMEI1/IMEI2/IMEI3 时可选 --- -#}
    {%- if item.DATATYPE in ['IMEI1', 'IMEI2', 'IMEI3'] -%}
        {%- if item.IMEITYPE is not none -%}
            IMEITYPE={{item.IMEITYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.PARADATATYPE1 is not none -%}
            PARADATATYPE1={{item.PARADATATYPE1}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.PARADATATYPE2 is not none -%}
            PARADATATYPE2={{item.PARADATATYPE2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.PARADATATYPE3 is not none -%}
            PARADATATYPE3={{item.PARADATATYPE3}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RC4 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RC4' -%}
        {%- if item.RC4KEYMD5EN is not none -%}
            RC4KEYMD5EN={{item.RC4KEYMD5EN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3'] -%}
        {%- if item.REMOVEDMCC is not none -%}
            REMOVEDMCC="{{item.REMOVEDMCC}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA1024 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA1024' -%}
        {%- if item.RSA1024METHOD is not none -%}
            RSA1024METHOD={{item.RSA1024METHOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA1024 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA1024' -%}
        {%- if item.RSA1024PADDINGTYPE is not none -%}
            RSA1024PADDINGTYPE={{item.RSA1024PADDINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA2048 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA2048' -%}
        {%- if item.RSA2048METHOD is not none -%}
            RSA2048METHOD={{item.RSA2048METHOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA2048 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA2048' -%}
        {%- if item.RSA2048PADDINGTYPE is not none -%}
            RSA2048PADDINGTYPE={{item.RSA2048PADDINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA3072 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA3072' -%}
        {%- if item.RSA3072METHOD is not none -%}
            RSA3072METHOD={{item.RSA3072METHOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RSA3072 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RSA3072' -%}
        {%- if item.RSA3072PADDINGTYPE is not none -%}
            RSA3072PADDINGTYPE={{item.RSA3072PADDINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/SHA256 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'SHA256'] -%}
        {%- if item.SALTSW is not none -%}
            SALTSW={{item.SALTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MULTIPARA1/MULTIPARA2/MULTIPARA3 时可选 --- -#}
    {%- if item.DATATYPE in ['MULTIPARA1', 'MULTIPARA2', 'MULTIPARA3'] -%}
        {%- if item.SEPARATOR is not none -%}
            SEPARATOR="{{item.SEPARATOR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=TIMESTAMP1/TIMESTAMP2/TIMESTAMP3 时可选 --- -#}
    {%- if item.DATATYPE in ['TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3'] -%}
        {%- if item.TSPRECISION is not none -%}
            TSPRECISION={{item.TSPRECISION}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

