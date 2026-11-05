---
id: ''
name: 配置HTTPS头增强加密策略及防欺诈策略
ne_type: UDG
type: feature
description: 如果需要使用HTTPS头增强功能，建议使用如下方式进行安全加固，在Web Server支持加密信息解析的情况下，将用户的IMSI、MSISDN、SGSN-IP等信息加密后添加到报文头传递给Web Server。同时为了防止用户使用欺诈的头增强信息进行业务，需要配置HTTPS头增强防欺诈策略。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["网络部署","安全配置","UDG安全配置","安全配置建议","可选配置","业务安全配置","配置HTTPS头增强加密策略及防欺诈策略"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
如果需要使用HTTPS头增强功能，建议使用如下方式进行安全加固，在Web Server支持加密信息解析的情况下，将用户的IMSI、MSISDN、SGSN-IP等信息加密后添加到报文头传递给Web Server。同时为了防止用户使用欺诈的头增强信息进行业务，需要配置HTTPS头增强防欺诈策略。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110263 HTTPS头增强和HTTP头防欺诈。
* 操作员已经获取到运营商对使用头增强特性的插入字段规划、字段前缀名称规划以及需要头增强信息的Web Server的URL等信息。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_tlsheaden_list:
      type: items
      properties:
        HEADERENNAME:
          name: '头增强名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '**ADD TLSHEADEN**'
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
        TLSTYPEVAL:
          name: 'TLS报文头域的TLS Type值'
          type: integer
          minimum: 0
          maximum: 65534
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
          maxLength: 255
          required: false
          description: '对头增强信息进行加密，配置对应的密钥，且密钥建议使用密文显示。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PSWDKEYCONFIRM:
          name: '确认密码'
          type: string
          minLength: 1
          maxLength: 255
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
        SALTSW:
          name: '是否添加盐值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '为了保证更好的安全性，MD5和SHA256加密方式建议配置为ENABLE；AES256加密方式不支持盐值添加。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
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
        ERRFGSUBTLSTP:
          name: 'HomeZone功能TLS报文头域的Sub Type值'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ERRFLGTLSTP:
          name: 'HomeZone功能TLS报文头域的TLS Type值'
          type: integer
          minimum: 0
          maximum: 65534
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
        SUBTLSTYPEVAL:
          name: 'TLS报文头域的Sub TLS Type值'
          type: integer
          minimum: 0
          maximum: 254
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
  examples:
    add_tlsheaden_list:
    - HEADERENNAME: 'header_test'
      DATATYPE: IMSI1
      TLSTYPEVAL: 1000
      ENCRYALGORI: AES256
      PSWDKEY: 'XXXXXX'
      PSWDKEYCONFIRM: 'XXXXXX'
      ANTIFRAUD: ENABLE
      SALTSW: DISABLE
      CCFORMAT: DECIMAL
      ERRFGSUBTLSTP: ''
      ERRFLGTLSTP: ''
      GRAYLIST: DISABLE
      HEADERFLDLEN: ''
      IMEITYPE: IMEI
      REMOVEDMCC: ''
      SUBTLSTYPEVAL: ''
      TSPRECISION: ''
      USERDEFINEVAL: ''
      CIPHERTXTENCODE: INHERIT
      RC4KEYMD5EN: INHERIT
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置HTTPS头增强动作及头增强防欺诈动作。

### 头增强的具体配置请参见激活HTTPS头增强；头防欺诈的具体配置请参见激活HTTP头防欺诈。

### 当要在报文头中插入用户的IMSI、MSISDN、SGSN IP等信息时，建议配置为AES256加密方式，配置对应的密钥，且密钥使用密文显示。为了防止用户使用欺诈的头增强信息进行业务，同时开启头增强防欺诈功能。

```jinja2
{%- for item in add_tlsheaden_list -%}
    ADD TLSHEADEN:
    {#- --- 必选参数 --- -#}
    HEADERENNAME="{{item.HEADERENNAME}}",
    DATATYPE={{item.DATATYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DATATYPE=USERDEF1/USERDEF2/USERDEF3/USERDEF4/APN/BILLINGTYPE/CHGCHAR1/CHGCHAR2/CHGCHAR3/CHGID/GGSNIP1/GGSNIP2/GGSNIP3/IMEI1/IMEI2/IMEI3/IMSI1/IMSI2/IMSI3/MCC/MNC/MSIP1/MSISDN1/MSISDN2/MSISDN3/RAT1/RAT2/RAT3/ROAMING1/ROAMING2/ROAMING3/SESSIONID/SGSNIP1/SGSNIP2/SGSNIP3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/ULI1/ULI2/ULI3/USERPROFALIAS/ZONEID/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时必选 --- -#}
    {%- if item.DATATYPE in ['USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'APN', 'BILLINGTYPE', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'CHGID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'IMEI1', 'IMEI2', 'IMEI3', 'IMSI1', 'IMSI2', 'IMSI3', 'MCC', 'MNC', 'MSIP1', 'MSISDN1', 'MSISDN2', 'MSISDN3', 'RAT1', 'RAT2', 'RAT3', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SESSIONID', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'ULI1', 'ULI2', 'ULI3', 'USERPROFALIAS', 'ZONEID', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        TLSTYPEVAL={{item.TLSTYPEVAL}},
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEY="{{item.PSWDKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEYCONFIRM="{{item.PSWDKEYCONFIRM}}",
    {%- endif -%}
    {#- --- 条件必选：DATATYPE=USERDEF1/USERDEF2/USERDEF3/USERDEF4 时必选 --- -#}
    {%- if item.DATATYPE in ['USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4'] -%}
        USERDEFINEVAL="{{item.USERDEFINEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6'] -%}
        {%- if item.ENCRYALGORI is not none -%}
            ENCRYALGORI={{item.ENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        {%- if item.ANTIFRAUD is not none -%}
            ANTIFRAUD={{item.ANTIFRAUD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/SHA256 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'SHA256'] -%}
        {%- if item.SALTSW is not none -%}
            SALTSW={{item.SALTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=CHGCHAR1/CHGCHAR2/CHGCHAR3 时可选 --- -#}
    {%- if item.DATATYPE in ['CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3'] -%}
        {%- if item.CCFORMAT is not none -%}
            CCFORMAT={{item.CCFORMAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        {%- if item.CIPHERTXTENCODE is not none -%}
            CIPHERTXTENCODE={{item.CIPHERTXTENCODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=ZONEID 时可选 --- -#}
    {%- if item.DATATYPE == 'ZONEID' -%}
        {%- if item.ERRFGSUBTLSTP is not none -%}
            ERRFGSUBTLSTP={{item.ERRFGSUBTLSTP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=ZONEID 时可选 --- -#}
    {%- if item.DATATYPE == 'ZONEID' -%}
        {%- if item.ERRFLGTLSTP is not none -%}
            ERRFLGTLSTP={{item.ERRFLGTLSTP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6'] -%}
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
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        {%- if item.SUBTLSTYPEVAL is not none -%}
            SUBTLSTYPEVAL={{item.SUBTLSTYPEVAL}},
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

