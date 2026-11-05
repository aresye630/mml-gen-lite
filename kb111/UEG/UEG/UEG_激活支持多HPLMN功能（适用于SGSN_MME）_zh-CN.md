---
id: GWFD-023102
name: 激活支持多HPLMN功能（适用于SGSN/MME）
ne_type: UEG
type: feature
description: 当单一PLMN内的用户号段数量无法满足签约用户数量时，运营商可以选择开启本特性来运营多个PLMN，从而为更多签约用户提供服务。且如果运营商要对不同的PLMN内的签约用户采取不同的计费和策略控制等处理，则运营商可通过本特性在UEG上配置多个HPLMN，保证对签约用户进行精准的计费和业务控制。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-023100 组网能力增强","GWFD-023102 支持多HPLMN功能","激活支持多HPLMN功能（适用于SGSN/MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当单一PLMN内的用户号段数量无法满足签约用户数量时，运营商可以选择开启本特性来运营多个PLMN，从而为更多签约用户提供服务。且如果运营商要对不同的PLMN内的签约用户采取不同的计费和策略控制等处理，则运营商可通过本特性在UEG上配置多个HPLMN，保证对签约用户进行精准的计费和业务控制。适用于SGSN、MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-023102 支持多HPLMN功能特性概述。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    set_mmfunc_list:
      type: items
      properties:
        MMINFO:
          name: '发送网络信息'
          type: string
          required: false
          description: '运营商网络标识相关参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EMMINFOIEPLY:
          name: 'EMM Information消息的信元携带策略'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrmminfo_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNPLCY:
          name: 'PLMN匹配策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: 'HPLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNOID:
          name: 'MNO标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 0
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMSCT:
          name: '纠正后的短消息中心'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCS:
          name: '是否允许LCS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        UEUSGTYPEPLCY:
          name: 'UE USAGE TYPE策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        DCNR:
          name: '支持DCNR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMF:
          name: '融合PGW-C/SMF'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_imsihss_list:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSSRLM:
          name: 'HSS域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务区名称支持的5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabinds1tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1BEGINTAI:
          name: 'UPF服务区名称绑定4G TAI范围起始值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1ENDTAI:
          name: 'UPF服务区名称绑定4G TAI范围结束值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmeshareplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: 'MME的共享PLMN'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '互联PLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsichar_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '本端标识参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCID:
          name: 'RNC标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iupaging_list:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_licenseswitch_list_1:
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
    set_mmfunc_list_1:
      type: items
      properties:
        MMINFO:
          name: '发送网络信息'
          type: string
          required: false
          description: '运营商网络标识相关参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EMMINFOIEPLY:
          name: 'EMM Information消息的信元携带策略'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mno_list:
      type: items
      properties:
        MNOID:
          name: 'MNO标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 0
          - 254
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrmminfo_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMNPLCY:
          name: 'PLMN匹配策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FULLNAME:
          name: '运营商全称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHORTNAME:
          name: '运营商简称'
          type: string
          maxLength: 79
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hplmn_list_2:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: 'HPLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '国家码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNOID:
          name: 'MNO标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 0
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SM:
          name: '是否允许SM业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMS:
          name: '是否允许SMS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        SMSCR:
          name: '是否允许纠正短消息中心'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMSCT:
          name: '纠正后的短消息中心'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCS:
          name: '是否允许LCS业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        S5S8TYPE:
          name: '协议类型'
          type: string
          enum:
          - GTP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        MAXSMNUM:
          name: '最大承载数'
          type: integer
          minimum: 1
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 11
        PLMNN:
          name: '运营商名称'
          type: string
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dnsn_list_2:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        UEUSGTYPEPLCY:
          name: 'UE USAGE TYPE策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        DCNR:
          name: '支持DCNR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        SMF:
          name: '融合PGW-C/SMF'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_imsihss_list_2:
      type: items
      properties:
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSSRLM:
          name: 'HSS域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabindn2tai_list_2:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'UPF服务区名称支持的5G TAI范围的起始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'UPF服务区名称支持的5G TAI范围的结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upareabinds1tai_list_2:
      type: items
      properties:
        AREANAME:
          name: 'UPF服务区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1BEGINTAI:
          name: 'UPF服务区名称绑定4G TAI范围起始值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S1ENDTAI:
          name: 'UPF服务区名称绑定4G TAI范围结束值'
          type: string
          minLength: 9
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mmeshareplmn_list_1:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: 'MME的共享PLMN'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_connectplmn_list_1:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '互联PLMN参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsichar_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '本端标识参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hnoinfo_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: true
          description: '本端标识参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsichar_list_2:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '本端标识参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_hnoinfo_list_1:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: true
          description: '本端标识参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOINDEX:
          name: '本地实体索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rnc_list_1:
      type: items
      properties:
        RNCX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCMNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCID:
          name: 'RNC标识'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NI:
          name: '网络指示语'
          type: string
          enum:
          - INT
          - INTB
          - NAT
          - NATB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPC:
          name: '信令点编码'
          type: string
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iupaging_list_1:
      type: items
      properties:
        LAI:
          name: '位置区标识'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区编码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RNCINDEX:
          name: 'RNC索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2HPLMN02'
      SWITCH: ENABLE
    set_mmfunc_list:
    - MMINFO: S1_MODE-1
      EMMINFOIEPLY: NETWORK_NAME-1
    add_usrmminfo_list:
    - SUBRANGE: IMSI_RANGE
      BEGIMSI: '123002000000000'
      ENDIMSI: '123004000000000'
      PLMNPLCY: YES
      MCC: '401'
      MNC: '01'
      FULLNAME: 'aaa'
      SHORTNAME: 'a'
    add_hplmn_list:
    - MCC: '123'
      MNC: '02'
      CC: '86'
      MNOID: 0
      SM: YES
      SMS: YES
      SMSCR: YES
      SMSCT: '861395678956778'
      LCS: YES
      S5S8TYPE: GTP
      EMCBS: YES
      MAXSMNUM: 11
      PLMNN: 'noname'
    add_dnsn_list:
    - FQDN: 'UEN.APN.EPC.MNC02.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 101
      ENTITY: PGW
      INTYPE: S5
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
      UEUSGTYPEPLCY: NO
      DCNR: YES
      SMF: NO
    add_imsihss_list:
    - IMSIPRE: '12302'
      HSSRLM: 'hss1'
    add_upareabindn2tai_list:
    - AREANAME: '11_uparea_n2_1'
      N2BEGINTAI: '12302000000'
      N2ENDTAI: '12312FFFFFF'
    add_upareabinds1tai_list:
    - AREANAME: '11_uparea_s1_1'
      S1BEGINTAI: '123020000'
      S1ENDTAI: '12312FFFF'
    add_mmeshareplmn_list:
    - MCC: '123'
      MNC: '00'
    add_connectplmn_list:
    - MCC: '123'
      MNC: '003'
      NOID: 128
    add_imsichar_list:
    - SUBRANGE: IMSI_RANGE
      IMSIPRE: '123'
      BEGIMSI: '123001'
      ENDIMSI: '123004'
      LOINDEX: 1
    add_rnc_list:
    - RNCX: ''
      RNCMCC: ''
      RNCMNC: ''
      RNCID: ''
      NI: ''
      SPC: ''
    add_iupaging_list:
    - LAI: ''
      RAC: ''
      RNCINDEX: ''
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2HPLMN02'
      SWITCH: ENABLE
    set_mmfunc_list_1:
    - MMINFO: S1_MODE-1
      EMMINFOIEPLY: NETWORK_NAME-1
    add_mno_list:
    - MNOID: 128
      FULLNAME: 'A'
      SHORTNAME: 'a'
    add_usrmminfo_list_1:
    - SUBRANGE: IMSI_RANGE
      BEGIMSI: '123002000000000'
      ENDIMSI: '123004000000000'
      PLMNPLCY: YES
      MCC: '401'
      MNC: '01'
      FULLNAME: 'aaa'
      SHORTNAME: 'a'
    add_hplmn_list_2:
    - MCC: '123'
      MNC: '02'
      CC: '86'
      MNOID: 0
      SM: YES
      SMS: YES
      SMSCR: YES
      SMSCT: '861395678956778'
      LCS: YES
      S5S8TYPE: GTP
      EMCBS: YES
      MAXSMNUM: 11
      PLMNN: 'noname'
    add_dnsn_list_2:
    - FQDN: 'UEN.APN.EPC.MNC02.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 101
      ENTITY: PGW
      INTYPE: S5
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
      UEUSGTYPEPLCY: NO
      DCNR: YES
      SMF: NO
    add_imsihss_list_2:
    - IMSIPRE: '12302'
      HSSRLM: 'hss1'
    add_upareabindn2tai_list_2:
    - AREANAME: '11_uparea_n2_1'
      N2BEGINTAI: '12302000000'
      N2ENDTAI: '12312FFFFFF'
    add_upareabinds1tai_list_2:
    - AREANAME: '11_uparea_s1_1'
      S1BEGINTAI: '123020000'
      S1ENDTAI: '12312FFFF'
    add_mmeshareplmn_list_1:
    - MCC: '123'
      MNC: '00'
    add_connectplmn_list_1:
    - MCC: '123'
      MNC: '003'
      NOID: 128
    add_imsichar_list_1:
    - SUBRANGE: IMSI_RANGE
      IMSIPRE: '123'
      BEGIMSI: '123001'
      ENDIMSI: '123004'
      LOINDEX: 1
    add_hnoinfo_list:
    - NOID: 128
      LOINDEX: 1
    add_imsichar_list_2:
    - SUBRANGE: IMSI_RANGE
      IMSIPRE: '123'
      BEGIMSI: '123001'
      ENDIMSI: '123004'
      LOINDEX: 1
    add_hnoinfo_list_1:
    - NOID: 128
      LOINDEX: 1
    add_rnc_list_1:
    - RNCX: ''
      RNCMCC: ''
      RNCMNC: ''
      RNCID: ''
      NI: ''
      SPC: ''
    add_iupaging_list_1:
    - LAI: ''
      RAC: ''
      RNCINDEX: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 一个UEG为一个拥有多PLMN ID的MNO服务。

### 系统缺省会增加一条MNO ID为0的MNO记录，当UEG只被一个MNO使用时，无须再增加MNO。

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 打开本特性的License开关。

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 增加运营商网络标识。

##### 1.3.1 打开运营商网络名称下发开关，当4G终端接入时，系统允许将运营商网络名称携带给终端。

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in set_mmfunc_list -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.MMINFO is not none -%}
            MMINFO={{item.MMINFO}},
        {%- endif -%}
        {%- if item.EMMINFOIEPLY is not none -%}
            EMMINFOIEPLY={{item.EMMINFOIEPLY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 若系统中同时存在命令**ADD MNO**和**ADD USRMMINFO**的配置记录，系统会优先将命令**ADD USRMMINFO**配置的运营商网络名称下发给终端。

##### 1.3.2 当需要特性IMSI范围的用户增加特定网络名称时执行以下步骤。

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_usrmminfo_list -%}
        ADD USRMMINFO:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.FULLNAME is not none -%}
            FULLNAME="{{item.FULLNAME}}",
        {%- endif -%}
        {%- if item.PLMNPLCY is not none -%}
            PLMNPLCY={{item.PLMNPLCY}},
        {%- endif -%}
        {%- if item.SHORTNAME is not none -%}
            SHORTNAME="{{item.SHORTNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PLMNPLCY=YES 时必选 --- -#}
        {%- if item.PLMNPLCY == 'YES' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：PLMNPLCY=YES 时必选 --- -#}
        {%- if item.PLMNPLCY == 'YES' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 增加HPLMN记录。

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_hplmn_list -%}
        ADD HPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CC is not none -%}
            CC="{{item.CC}}",
        {%- endif -%}
        {%- if item.MNOID is not none -%}
            MNOID={{item.MNOID}},
        {%- endif -%}
        {%- if item.SM is not none -%}
            SM={{item.SM}},
        {%- endif -%}
        {%- if item.SMS is not none -%}
            SMS={{item.SMS}},
        {%- endif -%}
        {%- if item.LCS is not none -%}
            LCS={{item.LCS}},
        {%- endif -%}
        {%- if item.S5S8TYPE is not none -%}
            S5S8TYPE={{item.S5S8TYPE}},
        {%- endif -%}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        {%- if item.PLMNN is not none -%}
            PLMNN="{{item.PLMNN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SMSCR=YES 时必选 --- -#}
        {%- if item.SMSCR == 'YES' -%}
            SMSCT="{{item.SMSCT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SMS=YES 时可选 --- -#}
        {%- if item.SMS == 'YES' -%}
            {%- if item.SMSCR is not none -%}
                SMSCR={{item.SMSCR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SM=YES 时可选 --- -#}
        {%- if item.SM == 'YES' -%}
            {%- if item.MAXSMNUM is not none -%}
                MAXSMNUM={{item.MAXSMNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.UEUSGTYPEPLCY is not none -%}
            UEUSGTYPEPLCY={{item.UEUSGTYPEPLCY}},
        {%- endif -%}
        {%- if item.DCNR is not none -%}
            DCNR={{item.DCNR}},
        {%- endif -%}
        {%- if item.SMF is not none -%}
            SMF={{item.SMF}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_imsihss_list -%}
        ADD IMSIHSS:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        HSSRLM="{{item.HSSRLM}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_upareabindn2tai_list -%}
        ADD UPAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_upareabinds1tai_list -%}
        ADD UPAREABINDS1TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        S1BEGINTAI="{{item.S1BEGINTAI}}",
        S1ENDTAI="{{item.S1ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置共享MME的PLMN ID。

```jinja2
{%- if is_scenario_single_mno -%}
    {%- for item in add_mmeshareplmn_list -%}
        ADD MMESHAREPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 **可选：**当MNO签订了漫游协议时，增加互联PLMN配置信息。

```jinja2
{%- if is_optional_add_connect_plmn and is_scenario_single_mno -%}
    {%- for item in add_connectplmn_list -%}
        ADD CONNECTPLMN:
        {#- --- 必选参数 --- -#}
        MNC="{{item.MNC}}",
        MCC="{{item.MCC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.NOID is not none -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.7 **可选：**配置本端标识的选择规则。

```jinja2
{%- if is_optional_configure_local_identifier_selection and is_scenario_single_mno -%}
    {%- for item in add_imsichar_list -%}
        ADD IMSICHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 对于只有一个MNO的场景，本端标识依次分为两层配置粒度，即第一层指根据IMSI号段配置，第二层轮选系统中所有的缺省配置。

#### 1.8 **可选：**增加PLMN对应的RNC信息。当MNO拥有多个HPLMN，且这些PLMN都需要在RNC侧进行广播，需要为每个PLMN配置RNC和寻呼信息。

```jinja2
{%- if is_optional_add_rnc_info and is_scenario_single_mno -%}
    {%- for item in add_rnc_list -%}
        ADD RNC:
        {#- --- 必选参数 --- -#}
        NI={{item.NI}},
        RNCX={{item.RNCX}},
        SPC="{{item.SPC}}",
        RNCID={{item.RNCID}},
        RNCMNC="{{item.RNCMNC}}",
        RNCMCC="{{item.RNCMCC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.9 **可选：**增加PLMN对应的寻呼信息。

```jinja2
{%- if is_optional_add_paging_info and is_scenario_single_mno -%}
    {%- for item in add_iupaging_list -%}
        ADD IUPAGING:
        {#- --- 必选参数 --- -#}
        RAC="{{item.RAC}}",
        LAI="{{item.LAI}}",
        RNCINDEX={{item.RNCINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 网络中存在多个MNO，一个UEG为多个MNO服务。

#### 2.1 进入“MML命令行-UEG”窗口。

#### 2.2 打开本特性的License开关。

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in set_licenseswitch_list_1 -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 增加运营商网络标识。

##### 2.3.1 打开运营商网络名称下发开关，当终端接入时，系统允许将运营商网络名称携带给终端。

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in set_mmfunc_list_1 -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.MMINFO is not none -%}
            MMINFO={{item.MMINFO}},
        {%- endif -%}
        {%- if item.EMMINFOIEPLY is not none -%}
            EMMINFOIEPLY={{item.EMMINFOIEPLY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.3.2 增加运营商网络名称。

###### 2.3.2.1 增加MNO信息。

####### 2.3.2.1.1 - 系统缺省已增加一条MNO ID为0的MNO记录，当UEG被多个MNO共享时，需要此步增加多个MNO。

####### 2.3.2.1.2 - 若系统中同时存在命令**ADD MNO**和**ADD USRMMINFO**的配置记录，系统会优先将命令**ADD USRMMINFO**配置的运营商网络名称下发给终端。

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_mno_list -%}
        ADD MNO:
        {#- --- 必选参数 --- -#}
        MNOID={{item.MNOID}},
        {#- --- 可选参数 --- -#}
        {%- if item.SHORTNAME is not none -%}
            SHORTNAME="{{item.SHORTNAME}}",
        {%- endif -%}
        {%- if item.FULLNAME is not none -%}
            FULLNAME="{{item.FULLNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.3.2.2 + **可选：**

###### 当需要特定IMSI范围的用户增加特定网络名称时执行以下步骤。

```jinja2
{%- if is_optional_add_network_name and is_scenario_multi_mno -%}
    {%- for item in add_usrmminfo_list_1 -%}
        ADD USRMMINFO:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.FULLNAME is not none -%}
            FULLNAME="{{item.FULLNAME}}",
        {%- endif -%}
        {%- if item.PLMNPLCY is not none -%}
            PLMNPLCY={{item.PLMNPLCY}},
        {%- endif -%}
        {%- if item.SHORTNAME is not none -%}
            SHORTNAME="{{item.SHORTNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PLMNPLCY=YES 时必选 --- -#}
        {%- if item.PLMNPLCY == 'YES' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：PLMNPLCY=YES 时必选 --- -#}
        {%- if item.PLMNPLCY == 'YES' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 增加HPLMN记录。

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_hplmn_list_2 -%}
        ADD HPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CC is not none -%}
            CC="{{item.CC}}",
        {%- endif -%}
        {%- if item.MNOID is not none -%}
            MNOID={{item.MNOID}},
        {%- endif -%}
        {%- if item.SM is not none -%}
            SM={{item.SM}},
        {%- endif -%}
        {%- if item.SMS is not none -%}
            SMS={{item.SMS}},
        {%- endif -%}
        {%- if item.LCS is not none -%}
            LCS={{item.LCS}},
        {%- endif -%}
        {%- if item.S5S8TYPE is not none -%}
            S5S8TYPE={{item.S5S8TYPE}},
        {%- endif -%}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        {%- if item.PLMNN is not none -%}
            PLMNN="{{item.PLMNN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SMSCR=YES 时必选 --- -#}
        {%- if item.SMSCR == 'YES' -%}
            SMSCT="{{item.SMSCT}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SMS=YES 时可选 --- -#}
        {%- if item.SMS == 'YES' -%}
            {%- if item.SMSCR is not none -%}
                SMSCR={{item.SMSCR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SM=YES 时可选 --- -#}
        {%- if item.SM == 'YES' -%}
            {%- if item.MAXSMNUM is not none -%}
                MAXSMNUM={{item.MAXSMNUM}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_dnsn_list_2 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.UEUSGTYPEPLCY is not none -%}
            UEUSGTYPEPLCY={{item.UEUSGTYPEPLCY}},
        {%- endif -%}
        {%- if item.DCNR is not none -%}
            DCNR={{item.DCNR}},
        {%- endif -%}
        {%- if item.SMF is not none -%}
            SMF={{item.SMF}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_imsihss_list_2 -%}
        ADD IMSIHSS:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        HSSRLM="{{item.HSSRLM}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_upareabindn2tai_list_2 -%}
        ADD UPAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_upareabinds1tai_list_2 -%}
        ADD UPAREABINDS1TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        S1BEGINTAI="{{item.S1BEGINTAI}}",
        S1ENDTAI="{{item.S1ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置共享MME的PLMN ID。

```jinja2
{%- if is_scenario_multi_mno -%}
    {%- for item in add_mmeshareplmn_list_1 -%}
        ADD MMESHAREPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### MME侧必须配置该命令，否则可能导致MME不能识别eNodeB发来的S1 Setup Request消息中携带的PLMN，从而返回S1 Setup Failure。

#### 2.6 **可选：**当MNO签订了漫游协议时，增加互联PLMN配置信息。

```jinja2
{%- if is_optional_add_connect_plmn and is_scenario_multi_mno -%}
    {%- for item in add_connectplmn_list_1 -%}
        ADD CONNECTPLMN:
        {#- --- 必选参数 --- -#}
        MNC="{{item.MNC}}",
        MCC="{{item.MCC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.NOID is not none -%}
            NOID={{item.NOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 **可选：**配置本端标识的选择规则。

#### 对于存在多个MNO的场景，本端标识依次分为三层配置粒度，即第一层指根据IMSI号段配置，第二层根据MNO/MVNO ID配置，第三层轮选系统中所有的缺省配置。

##### 2.7.1 本端标识是SGSN号码

###### 2.7.1.1 - 根据IMSI号段选择本端标识。

```jinja2
{%- if is_optional_configure_local_identifier_selection and is_scenario_multi_mno and is_scenario_sgsn_number -%}
    {%- for item in add_imsichar_list_1 -%}
        ADD IMSICHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.7.1.2 - 根据MNO ID选择本端标识

```jinja2
{%- if is_optional_configure_local_identifier_selection and is_scenario_multi_mno and is_scenario_sgsn_number -%}
    {%- for item in add_hnoinfo_list -%}
        ADD HNOINFO:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.7.2 本端标识是Diameter

###### 2.7.2.1 - 如果系统中配置了多个Diameter本端标识，需要执行如下步骤。

###### 2.7.2.2 - 如果系统中仅配置了一个Diameter本端标识，不需要执行如下步骤。

##### 系统配置的Diameter本端标识可以通过**LST CPDMLE**命令查询。

###### 2.7.2.3 - 根据IMSI号段选择本端标识

```jinja2
{%- if is_optional_configure_local_identifier_selection and is_scenario_multi_mno and is_scenario_diameter -%}
    {%- for item in add_imsichar_list_2 -%}
        ADD IMSICHAR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.7.2.4 - 根据MNO ID选择本端标识

```jinja2
{%- if is_optional_configure_local_identifier_selection and is_scenario_multi_mno and is_scenario_diameter -%}
    {%- for item in add_hnoinfo_list_1 -%}
        ADD HNOINFO:
        {#- --- 必选参数 --- -#}
        NOID={{item.NOID}},
        {#- --- 可选参数 --- -#}
        {%- if item.LOINDEX is not none -%}
            LOINDEX={{item.LOINDEX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.8 **可选：**增加PLMN对应的RNC信息。当一个MNO拥有多个HPLMN，且这些PLMN都需要在RNC侧进行广播，需要为每个PLMN配置RNC和寻呼信息。

```jinja2
{%- if is_optional_add_rnc_info and is_scenario_multi_mno -%}
    {%- for item in add_rnc_list_1 -%}
        ADD RNC:
        {#- --- 必选参数 --- -#}
        NI={{item.NI}},
        RNCX={{item.RNCX}},
        SPC="{{item.SPC}}",
        RNCID={{item.RNCID}},
        RNCMNC="{{item.RNCMNC}}",
        RNCMCC="{{item.RNCMCC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 **可选：**增加PLMN对应的寻呼信息。

```jinja2
{%- if is_optional_add_paging_info and is_scenario_multi_mno -%}
    {%- for item in add_iupaging_list_1 -%}
        ADD IUPAGING:
        {#- --- 必选参数 --- -#}
        RAC="{{item.RAC}}",
        LAI="{{item.LAI}}",
        RNCINDEX={{item.RNCINDEX}},
        ;
    {%- endfor -%}
{%- endif -%}
```

