---
id: GWFD-020911
name: 激活区域漫游限制特性（适用于SGSN/MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。  区域漫游限制是指UEG可以控制某一类用户可以接入的位置区域，或者控制某一区域不同类别用户的接入策略。  适用于SGSN、MME。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","MME特性指南","GWFD-020900 接入管理","GWFD-020911 区域漫游限制（适用于MME/HSS）","激活区域漫游限制特性（适用于SGSN/MME）"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-020900 接入管理","GWFD-020911 区域漫游限制","GWFD-020911 区域漫游限制（适用于MME/HSS）","激活区域漫游限制特性（适用于SGSN/MME）"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST S1IMEICFG')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活区域漫游限制特性的操作过程。区域漫游限制是指UEG可以控制某一类用户可以接入的位置区域，或者控制某一区域不同类别用户的接入策略。适用于SGSN、MME。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-020911 区域漫游限制特性概述（适用于MME/HSS）。
* 已完成加载License，对应的License项为“82206572 LKV2RRR02 区域漫游限制”。
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
        ZC:
          name: '区域码'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_zc_list:
      type: items
      properties:
        ZC:
          name: '区域码'
          type: string
          maxLength: 6
          required: true
          description: 'ZC配置参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          - SA
          - TA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ZCN:
          name: '区域名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区域码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SAC:
          name: '服务区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACRANGE:
          name: '位置区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RACRANGE:
          name: '路由区域码范围'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SACRANGE:
          name: '服务区域码范围'
          type: string
          maxLength: 6
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
          data_source: ''
          pattern: ''
          default: ''
    add_zcconvert_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: '全网规划'
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
        CONVERTPLCY:
          name: '转换策略'
          type: string
          enum:
          - IGNORE_SUB_ZC
          - OVERWRITE_DIRECTLY
          - OVERWRITE_IF_SUB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ZC:
          name: '区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          - STR
          - STR_EX
          - STR_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list_1:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          - STR
          - STR_EX
          - STR_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_mmfunc_list_1:
      type: items
      properties:
        ZC:
          name: '区域码'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_zc_list_1:
      type: items
      properties:
        ZC:
          name: '区域码'
          type: string
          maxLength: 6
          required: true
          description: 'ZC配置参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          - SA
          - TA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区域码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SAC:
          name: '服务区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ZCN:
          name: '区域名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACRANGE:
          name: '位置区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RACRANGE:
          name: '路由区域码范围'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SACRANGE:
          name: '服务区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_zcconvert_list_1:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: ''
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
        CONVERTPLCY:
          name: '转换策略'
          type: string
          enum:
          - IGNORE_SUB_ZC
          - OVERWRITE_DIRECTLY
          - OVERWRITE_IF_SUB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ZC:
          name: '区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list_2:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          - STR
          - STR_EX
          - STR_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list_3:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          - STR
          - STR_EX
          - STR_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_laragp_list:
      type: items
      properties:
        LARAGPID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LARAGPN:
          name: '区域群名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_laragpmem_list:
      type: items
      properties:
        LARAGPID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RAC:
          name: '路由区域码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RACRANGE:
          name: '路由区域码范围'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tagp_list:
      type: items
      properties:
        TAGPID:
          name: '跟踪区群组标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TANAME:
          name: '跟踪区群组名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 'noname'
    add_tagpmem_list:
      type: items
      properties:
        TAGPID:
          name: '跟踪区群组标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_gbsubrrlst_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '以某一类用户为对象，控制该类用户可以接入的位置区域'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LARAGPID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARMODE:
          name: '区域限制模式'
          type: string
          enum:
          - BLACKLST
          - WHITELST
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_iusubrrlst_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '以某一类用户为对象，控制该类用户可以接入的位置区域'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LARAGPID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARMODE:
          name: '区域限制模式'
          type: string
          enum:
          - BLACKLST
          - WHITELST
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_s1subrrlst_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: '以某一类用户为对象，控制该类用户可以接入的位置区域'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BEGIMSI:
          name: '起始IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDIMSI:
          name: '终止IMSI'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARMODE:
          name: '区域限制模式'
          type: string
          enum:
          - BLACKLST
          - WHITELST
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAGPID:
          name: '跟踪区群标识'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1imeicfg_list:
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
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_areagp_list:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '以位置区域为对象，控制该区域不同用户的接入策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAN:
          name: '区域群名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_areagpmem_list:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '以位置区域为对象，控制该区域不同用户的接入策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          - TA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区域码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imeilib_list:
      type: items
      properties:
        IMEITAC:
          name: '设备型号核准号码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subgp_list:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_subgpmem_list:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbaccarealst_list:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - LA
          - OTHER
          - RA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - GPRS_NONGPRS_SRV_NOT_ALLOWED
          - GPRS_SERVICE_NOT_ALLOWED
          - GPRS_SRV_NOT_ALLOWED_IN_PLMN
          - LA_NOT_ALLOWED
          - NO_SUITABLE_CELLS_IN_LA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_LA
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_LA
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iuaccarealst_list:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - LA
          - OTHER
          - RA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - GPRS_NONGPRS_SRV_NOT_ALLOWED
          - GPRS_SERVICE_NOT_ALLOWED
          - GPRS_SRV_NOT_ALLOWED_IN_PLMN
          - LA_NOT_ALLOWED
          - NO_SUITABLE_CELLS_IN_LA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_LA
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_LA
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1accarealst_list:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
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
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRFSP:
          name: '拒绝特征RFSP用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJCAUSE:
          name: '拒绝原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPECSUB:
          name: '拒绝特征用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJRFSPIDX:
          name: '拒绝特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBCSFB:
          name: '拒绝CSFB用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SRVCCCAP:
          name: 'SRVCC能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSTNSR:
          name: '匹配STN-SR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBIND:
          name: 'eNodeB指示方式'
          type: string
          enum:
          - HORL
          - NO
          - RFSP_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBRFSPIDX:
          name: '指示特征RFSP'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_areagp_list_1:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '以位置区域为对象，控制该区域不同用户的接入策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAN:
          name: '区域群名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_areagpmem_list_1:
      type: items
      properties:
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '以位置区域为对象，控制该区域不同用户的接入策略'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IDTYPE:
          name: '标识类型'
          type: string
          enum:
          - LA
          - RA
          - TA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RAC:
          name: '路由区域码'
          type: string
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_specrfspvalue_list:
      type: items
      properties:
        RFSPIDX:
          name: '特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TYPE:
          name: '特征RFSP索引类型'
          type: string
          enum:
          - ACC_REJECT
          - ENODEB_IND
          - IMS_VOPS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEGRFSP:
          name: '起始RFSP'
          type: integer
          minimum: 1
          maximum: 256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDRFSP:
          name: '终止RFSP'
          type: integer
          minimum: 1
          maximum: 256
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1accarealst_list_3:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
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
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPECSUB:
          name: '拒绝特征用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SUBRFSP:
          name: '拒绝特征RFSP用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJRFSPIDX:
          name: '拒绝特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBCSFB:
          name: '拒绝CSFB用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJCAUSE:
          name: '拒绝原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        ENBIND:
          name: 'eNodeB指示方式'
          type: string
          enum:
          - HORL
          - NO
          - RFSP_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBRFSPIDX:
          name: '指示特征RFSP'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
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
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVCCCAP:
          name: 'SRVCC能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSTNSR:
          name: '匹配STN-SR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
    add_s1accarealst_list_4:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
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
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPECSUB:
          name: '拒绝特征用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SUBRFSP:
          name: '拒绝特征RFSP用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJRFSPIDX:
          name: '拒绝特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBCSFB:
          name: '拒绝CSFB用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SRVCCCAP:
          name: 'SRVCC能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSTNSR:
          name: '匹配STN-SR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBIND:
          name: 'eNodeB指示方式'
          type: string
          enum:
          - HORL
          - NO
          - RFSP_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBRFSPIDX:
          name: '指示特征RFSP'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_s1accarealst_list_5:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
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
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPECSUB:
          name: '拒绝特征用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SUBRFSP:
          name: '拒绝特征RFSP用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJRFSPIDX:
          name: '拒绝特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBCSFB:
          name: '拒绝CSFB用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SRVCCCAP:
          name: 'SRVCC能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSTNSR:
          name: '匹配STN-SR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBIND:
          name: 'eNodeB指示方式'
          type: string
          enum:
          - HORL
          - NO
          - RFSP_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBRFSPIDX:
          name: '指示特征RFSP'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_s1imeicfg_list:
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
          data_source: ''
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_mmfunc_list_2:
      type: items
      properties:
        TALIST:
          name: 'TA List过滤'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FORBIDTA:
          name: 'Forbidden TAs'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1imeicfg_list_1:
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
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    add_imeilib_list_1:
      type: items
      properties:
        IMEITAC:
          name: '设备型号核准号码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subgp_list_1:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_subgpmem_list_1:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_subgp_list_2:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_msisdnsubgpmem_list:
      type: items
      properties:
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gbaccarealst_list_1:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - LA
          - OTHER
          - RA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - GPRS_NONGPRS_SRV_NOT_ALLOWED
          - GPRS_SERVICE_NOT_ALLOWED
          - GPRS_SRV_NOT_ALLOWED_IN_PLMN
          - LA_NOT_ALLOWED
          - NO_SUITABLE_CELLS_IN_LA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_LA
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_LA
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iuaccarealst_list_1:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - LA
          - OTHER
          - RA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - GPRS_NONGPRS_SRV_NOT_ALLOWED
          - GPRS_SERVICE_NOT_ALLOWED
          - GPRS_SRV_NOT_ALLOWED_IN_PLMN
          - LA_NOT_ALLOWED
          - NO_SUITABLE_CELLS_IN_LA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_LA
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_LA
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1accarealst_list_6:
      type: items
      properties:
        AREA:
          name: '区域范围'
          type: string
          enum:
          - AG
          - OTHER
          - TA
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
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
        TAC:
          name: '跟踪区域码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_IMSI_RANGE
          - UE_TYPE
          - USER_GROUP
          required: true
          description: ''
          data_source: ''
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
        CTRLTYPE:
          name: '控制类型'
          type: string
          enum:
          - ALLOW
          - REJECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAUSE:
          name: '原因值'
          type: string
          enum:
          - CUSTOMER_DEFINED
          - EPS_NONEPS_SRV_NOT_ALLOWED
          - EPS_SERVICE_NOT_ALLOWED
          - EPS_SRV_NOT_ALLOWED_IN_PLMN
          - NO_SUITABLE_CELLS_IN_TA
          - PLMN_NOT_ALLOWED
          - ROAMING_NOT_ALLOWED_IN_TA
          - TA_NOT_ALLOWED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO_SUITABLE_CELLS_IN_TA
        AREAID:
          name: '区域群标识'
          type: integer
          minimum: 1
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACRANGE:
          name: '跟踪区域码范围'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBID:
          name: '用户群标识'
          type: integer
          minimum: 1
          maximum: 100
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
        SDCAUSE:
          name: '自定义原因值'
          type: integer
          minimum: 1
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPECSUB:
          name: '拒绝特征用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SUBRFSP:
          name: '拒绝特征RFSP用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        REJRFSPIDX:
          name: '拒绝特征RFSP索引'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBCSFB:
          name: '拒绝CSFB用户接入'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SRVCCCAP:
          name: 'SRVCC能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSTNSR:
          name: '匹配STN-SR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBIND:
          name: 'eNodeB指示方式'
          type: string
          enum:
          - HORL
          - NO
          - RFSP_ID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        ENBRFSPIDX:
          name: '指示特征RFSP'
          type: integer
          minimum: 0
          maximum: 49
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UETYPE:
          name: '终端类型'
          type: string
          enum:
          - ALL_IMEI
          - ANDROID
          - BLACKBERRY
          - CUSTOM_TYPE_1
          - CUSTOM_TYPE_10
          - CUSTOM_TYPE_11
          - CUSTOM_TYPE_12
          - CUSTOM_TYPE_2
          - CUSTOM_TYPE_3
          - CUSTOM_TYPE_4
          - CUSTOM_TYPE_5
          - CUSTOM_TYPE_6
          - CUSTOM_TYPE_7
          - CUSTOM_TYPE_8
          - CUSTOM_TYPE_9
          - IOS
          - WINDOWS
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2RRR02'
      SWITCH: ENABLE
    set_mmfunc_list:
    - ZC: YES
    add_zc_list:
    - ZC: '0x1234'
      IDTYPE: LA
      MCC: '123'
      MNC: '03'
      LAC: '0x1'
      ZCN: 'china-mobile-001'
      RAC: '0x1'
      SAC: '0x1'
      TAC: '0x1'
      LACRANGE: '0x1'
      RACRANGE: '0x1'
      TACRANGE: '0x1'
      SACRANGE: '0x1'
    add_mno_list:
    - MNOID: 128
    add_zcconvert_list:
    - SUBRANGE: 外网用户
      NOID: 128
      CONVERTPLCY: 签约则采用指定ZC
      ZC: '0x1235'
    set_softpara_list:
    - DT: ''
      PARANUM: ''
      VALUE: ''
    set_softpara_list_1:
    - DT: ''
      PARANUM: ''
      VALUE: ''
    set_mmfunc_list_1:
    - ZC: YES
    add_zc_list_1:
    - ZC: '0x3000'
      IDTYPE: TA
      MCC: '123'
      MNC: '03'
      TAC: '0x4203'
      TACRANGE: '0x4204'
      LAC: '0x1'
      RAC: '0x1'
      SAC: '0x1'
      ZCN: 'china-mobile-001'
      LACRANGE: '0x1'
      RACRANGE: '0x1'
      SACRANGE: '0x1'
    add_zcconvert_list_1:
    - SUBRANGE: 外网用户
      IMSIPRE: '1230301'
      CONVERTPLCY: 签约则采用指定ZC
      ZC: '0x1235'
    set_softpara_list_2:
    - DT: ''
      PARANUM: ''
      VALUE: ''
    set_softpara_list_3:
    - DT: ''
      PARANUM: ''
      VALUE: ''
    add_laragp_list:
    - LARAGPID: 1
      LARAGPN: 'shanghai'
    add_laragpmem_list:
    - LARAGPID: 1
      IDTYPE: RA
      MCC: '456'
      MNC: '12'
      LAC: '0x1401'
      RAC: '0x11'
      RACRANGE: '0x20'
    add_tagp_list:
    - TAGPID: 1
      TANAME: 'Shanghai'
    add_tagpmem_list:
    - TAGPID: 1
      MCC: '456'
      MNC: '12'
      TAC: '0x4201'
      TACRANGE: '0x4210'
    add_gbsubrrlst_list:
    - SUBRANGE: IMSI_RANGE
      BEGIMSI: '123003000000000'
      ENDIMSI: '123003666000000'
      LARAGPID: 1
      ARMODE: BLACKLST
    add_iusubrrlst_list:
    - SUBRANGE: IMSI_RANGE
      BEGIMSI: '123004000000000'
      ENDIMSI: '123004666000000'
      LARAGPID: 1
      ARMODE: BLACKLST
    add_s1subrrlst_list:
    - SUBRANGE: IMSI_RANGE
      BEGIMSI: '123003000000000'
      ENDIMSI: '123003666000000'
      ARMODE: BLACKLST
      TAGPID: ''
    add_s1imeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
    add_areagp_list:
    - AREAID: 1
      AREAN: 'L800'
    add_areagpmem_list:
    - AREAID: 1
      IDTYPE: TA
      MCC: '123'
      MNC: '03'
      TAC: '0x7603'
      TACRANGE: '0x7614'
      RAC: '0x1'
      LAC: '0x1'
    add_imeilib_list:
    - IMEITAC: '12345678'
      UETYPE: BLACKBERRY
    add_subgp_list:
    - SUBID: 1
    add_subgpmem_list:
    - SUBID: 1
      IMSIPRE: '1230301'
    add_gbaccarealst_list:
    - AREA: AG
      AREAID: 1
      SUBRANGE: SPECIAL_IMSI_RANGE
      MCC: '123'
      MNC: '03'
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
    add_iuaccarealst_list:
    - AREA: AG
      AREAID: 1
      SUBRANGE: SPECIAL_IMSI_RANGE
      MCC: '123'
      MNC: '03'
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
    add_s1accarealst_list:
    - AREA: AG
      AREAID: 1
      SUBRANGE: HOME_USER
      NOID: 0
      CTRLTYPE: ALLOW
      SUBRFSP: YES
      REJCAUSE: NO_SUITABLE_CELLS_IN_TA
      IMSIPRE: '12303'
      CAUSE: NO_SUITABLE_CELLS_IN_TA
      MCC: '123'
      MNC: '03'
      TAC: '0x4201'
      TACRANGE: '0x1'
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
      SPECSUB: NO
      REJRFSPIDX: 1
      SUBCSFB: NO
      SRVCCCAP: YES
      CHKSTNSR: NO
      ENBIND: NO
      ENBRFSPIDX: 1
    add_areagp_list_1:
    - AREAID: 1
      AREAN: 'shanghai'
    add_areagpmem_list_1:
    - AREAID: 1
      IDTYPE: TA
      MCC: '456'
      MNC: '12'
      TAC: '0x0011'
      TACRANGE: '0x0020'
      RAC: '0x1'
      LAC: '0x1'
    add_specrfspvalue_list:
    - RFSPIDX: 0
      TYPE: ACC_REJECT
      BEGRFSP: 250
      ENDRFSP: 255
    add_s1accarealst_list_3:
    - AREA: AG
      AREAID: 1
      SUBRANGE: HOME_USER
      NOID: 0
      CTRLTYPE: ALLOW
      SPECSUB: YES
      SUBRFSP: YES
      REJRFSPIDX: 1
      SUBCSFB: YES
      REJCAUSE: NO_SUITABLE_CELLS_IN_TA
      ENBIND: RFSP_ID
      ENBRFSPIDX: 2
      MCC: '123'
      MNC: '03'
      TAC: '0x4201'
      TACRANGE: '0x1'
      IMSIPRE: '1230301'
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
      SRVCCCAP: YES
      CHKSTNSR: NO
      CAUSE: NO_SUITABLE_CELLS_IN_TA
    add_s1accarealst_list_4:
    - AREA: AG
      AREAID: 1
      SUBRANGE: SPECIAL_IMSI_RANGE
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      MCC: '123'
      MNC: '03'
      TAC: '0x4201'
      TACRANGE: '0x1'
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
      SPECSUB: NO
      SUBRFSP: NO
      REJRFSPIDX: 1
      SUBCSFB: NO
      SRVCCCAP: YES
      CHKSTNSR: NO
      ENBIND: NO
      ENBRFSPIDX: 1
    add_s1accarealst_list_5:
    - AREA: AG
      MCC: '123'
      MNC: '03'
      TAC: '0x4201'
      SUBRANGE: SPECIAL_IMSI_RANGE
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      AREAID: 1
      TACRANGE: '0x1'
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
      SPECSUB: NO
      SUBRFSP: NO
      REJRFSPIDX: 1
      SUBCSFB: NO
      SRVCCCAP: YES
      CHKSTNSR: NO
      ENBIND: NO
      ENBRFSPIDX: 1
    mod_s1imeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
    set_mmfunc_list_2:
    - TALIST: LOCAL_CFG-1
      FORBIDTA: LOCAL_CFG-1
    add_s1imeicfg_list_1:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEISV
    add_imeilib_list_1:
    - IMEITAC: '12345678'
      UETYPE: BLACKBERRY
    add_subgp_list_1:
    - SUBID: 1
    add_subgpmem_list_1:
    - SUBID: 1
      IMSIPRE: '1230301'
    add_subgp_list_2:
    - SUBID: 1
    add_msisdnsubgpmem_list:
    - SUBID: 1
      MSISDNPRE: '12345678'
    add_gbaccarealst_list_1:
    - AREA: AG
      AREAID: 1
      SUBRANGE: SPECIAL_IMSI_RANGE
      MCC: '123'
      MNC: '03'
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
    add_iuaccarealst_list_1:
    - AREA: AG
      AREAID: 1
      SUBRANGE: SPECIAL_IMSI_RANGE
      MCC: '123'
      MNC: '03'
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
    add_s1accarealst_list_6:
    - AREA: TA
      MCC: '123'
      MNC: '03'
      TAC: '0x4201'
      SUBRANGE: SPECIAL_IMSIPRE
      IMSIPRE: '1230301'
      CTRLTYPE: REJECT
      CAUSE: EPS_SERVICE_NOT_ALLOWED
      AREAID: 1
      TACRANGE: '0x1'
      SUBID: 1
      BEGIMSI: '123'
      ENDIMSI: '456'
      SDCAUSE: 1
      SPECSUB: NO
      SUBRFSP: NO
      REJRFSPIDX: 1
      SUBCSFB: NO
      SRVCCCAP: YES
      CHKSTNSR: NO
      ENBIND: NO
      ENBRFSPIDX: 1
      UETYPE: BLACKBERRY
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 开启本特性的功能控制开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 根据用户签约ZC信息进行漫游限制不受该License控制。

### 3 根据需要选择合适的漫游策略。

#### 3.1 可以根据不同的需求配置多种策略进行漫游限制。如果配置多种策略，则在用户接入时，需要所有策略都允许用户接入，该用户才能接入网络。否则，该用户不允许接入。

#### 3.2 此种场景下TAU流程的Downlink NAS Transport消息是否携带Handover Restriction List信元，需要判断MME对接的所有eNodeB是否都支持此信元。如果都支持，可以将**SET S1CMPT**命令中的“HRL”设置为“YES”，此时TAU流程中的Downlink NAS Transport消息才会携带Handover Restriction List信元。否则，“HRL”需要设置为“NO”，避免对不支持此信元的eNodeB产生影响，此时TAU流程中的Downlink NAS Transport消息不会携带Handover Restriction List信元。

#### 3.3 * **方法1.1: 通过用户的签约ZC列表进行接入限制。**

#### 该功能需要HLR/HSS支持并配置了用户的签约ZC信息。

##### 3.3.1 打开根据用户ZC信息进行漫游限制的功能开关。

```jinja2
{%- if is_scenario_subscribed_zc_list -%}
    {%- for item in set_mmfunc_list -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.ZC is not none -%}
            ZC={{item.ZC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.2 增加区域码记录。

```jinja2
{%- if is_scenario_subscribed_zc_list -%}
    {%- for item in add_zc_list -%}
        ADD ZC:
        {#- --- 必选参数 --- -#}
        ZC="{{item.ZC}}",
        IDTYPE={{item.IDTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ZCN is not none -%}
            ZCN="{{item.ZCN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IDTYPE=LA/RA/SA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA', 'SA'] -%}
            LAC="{{item.LAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=RA 时必选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            RAC="{{item.RAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=TA 时必选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=SA 时必选 --- -#}
        {%- if item.IDTYPE == 'SA' -%}
            SAC="{{item.SAC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IDTYPE=TA 时可选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=LA 时可选 --- -#}
        {%- if item.IDTYPE == 'LA' -%}
            {%- if item.LACRANGE is not none -%}
                LACRANGE="{{item.LACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=RA 时可选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            {%- if item.RACRANGE is not none -%}
                RACRANGE="{{item.RACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=SA 时可选 --- -#}
        {%- if item.IDTYPE == 'SA' -%}
            {%- if item.SACRANGE is not none -%}
                SACRANGE="{{item.SACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.3 （可选）配置区域码转换策略。当运营商需要忽略来自其它区域或其它运营商的签约ZC时，执行该步骤。

```jinja2
{%- if is_optional_zc_convert_policy and is_scenario_subscribed_zc_list -%}
    {%- for item in add_mno_list -%}
        ADD MNO:
        {#- --- 必选参数 --- -#}
        MNOID={{item.MNOID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_zc_convert_policy and is_scenario_subscribed_zc_list -%}
    {%- for item in add_zcconvert_list -%}
        ADD ZCCONVERT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        CONVERTPLCY={{item.CONVERTPLCY}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=HOME_USER/FOREIGN_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['HOME_USER', 'FOREIGN_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：CONVERTPLCY=OVERWRITE_DIRECTLY/OVERWRITE_IF_SUB 时必选 --- -#}
        {%- if item.CONVERTPLCY in ['OVERWRITE_DIRECTLY', 'OVERWRITE_IF_SUB'] -%}
            ZC="{{item.ZC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.4 （可选）配置用户不允许接入某区域时，UEG下发拒绝接入消息中携带的原因值。

###### 3.3.4.1 2G/3G用户携带的原因值通过软参“BYTE\_EX64 控制ZC接入限制下发的拒绝原因值”进行控制（缺省携带的原因值为#12 Location area not allowed）：

```jinja2
{%- if is_optional_reject_cause_value and is_scenario_subscribed_zc_list -%}
    {%- for item in set_softpara_list -%}
        SET SOFTPARA:
        {#- --- 必选参数 --- -#}
        VALUE="{{item.VALUE}}",
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.3.4.2 4G用户携带的原因值通过软参“BYTE\_EX209 控制下发给4G区域限制用户拒绝消息中携带的原因值”进行控制（缺省携带的原因值为#15 No suitable cells in tracking area）：

```jinja2
{%- if is_optional_reject_cause_value and is_scenario_subscribed_zc_list -%}
    {%- for item in set_softpara_list_1 -%}
        SET SOFTPARA:
        {#- --- 必选参数 --- -#}
        VALUE="{{item.VALUE}}",
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 * **方法1.2: 通过UEG配置的ZC列表进行接入限制。**

##### 3.4.1 打开根据用户ZC信息进行漫游限制的功能开关。

```jinja2
{%- if is_scenario_ueg_configured_zc_list -%}
    {%- for item in set_mmfunc_list_1 -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.ZC is not none -%}
            ZC={{item.ZC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.4.2 定义某一类用户可以接入的区域信息（区域码和区域码对应的位置区域）。

```jinja2
{%- if is_scenario_ueg_configured_zc_list -%}
    {%- for item in add_zc_list_1 -%}
        ADD ZC:
        {#- --- 必选参数 --- -#}
        ZC="{{item.ZC}}",
        IDTYPE={{item.IDTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ZCN is not none -%}
            ZCN="{{item.ZCN}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IDTYPE=TA 时必选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=RA 时必选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            RAC="{{item.RAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=LA/RA/SA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA', 'SA'] -%}
            LAC="{{item.LAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=SA 时必选 --- -#}
        {%- if item.IDTYPE == 'SA' -%}
            SAC="{{item.SAC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IDTYPE=TA 时可选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=LA 时可选 --- -#}
        {%- if item.IDTYPE == 'LA' -%}
            {%- if item.LACRANGE is not none -%}
                LACRANGE="{{item.LACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=RA 时可选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            {%- if item.RACRANGE is not none -%}
                RACRANGE="{{item.RACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IDTYPE=SA 时可选 --- -#}
        {%- if item.IDTYPE == 'SA' -%}
            {%- if item.SACRANGE is not none -%}
                SACRANGE="{{item.SACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.4.3 配置该类用户和3.b定义的区域码绑定。

```jinja2
{%- if is_scenario_ueg_configured_zc_list -%}
    {%- for item in add_zcconvert_list_1 -%}
        ADD ZCCONVERT:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        CONVERTPLCY={{item.CONVERTPLCY}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：CONVERTPLCY=OVERWRITE_DIRECTLY/OVERWRITE_IF_SUB 时必选 --- -#}
        {%- if item.CONVERTPLCY in ['OVERWRITE_DIRECTLY', 'OVERWRITE_IF_SUB'] -%}
            ZC="{{item.ZC}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.4.4 （可选）配置用户不允许接入某区域时，UEG下发拒绝接入消息中携带的原因值。

###### 3.4.4.1 2G/3G用户携带的原因值通过软参“BYTE\_EX64 控制ZC接入限制下发的拒绝原因值”进行控制（缺省携带的原因值为#12 Location area not allowed）：

```jinja2
{%- if is_optional_reject_cause_value and is_scenario_ueg_configured_zc_list -%}
    {%- for item in set_softpara_list_2 -%}
        SET SOFTPARA:
        {#- --- 必选参数 --- -#}
        VALUE="{{item.VALUE}}",
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.4.4.2 4G用户携带的原因值通过软参“BYTE\_EX209 控制下发给4G区域限制用户拒绝消息中携带的原因值”进行控制（缺省携带的原因值为#15 No suitable cells in tracking area）：

```jinja2
{%- if is_optional_reject_cause_value and is_scenario_ueg_configured_zc_list -%}
    {%- for item in set_softpara_list_3 -%}
        SET SOFTPARA:
        {#- --- 必选参数 --- -#}
        VALUE="{{item.VALUE}}",
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.5 * **方法2: 配置以某一类用户为对象，控制该类用户可以接入的位置区域**

##### 3.5.1 配置区域群记录，同一个区域群中的成员具有相同的接入控制策略。

###### 3.5.1.1 配置位置区域群记录。

####### 3.5.1.1.1 配置位置区域群标识和名称。

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_laragp_list -%}
        ADD LARAGP:
        {#- --- 必选参数 --- -#}
        LARAGPID={{item.LARAGPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.LARAGPN is not none -%}
            LARAGPN="{{item.LARAGPN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

####### 3.5.1.1.2 配置区域群的群成员。

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_laragpmem_list -%}
        ADD LARAGPMEM:
        {#- --- 必选参数 --- -#}
        LARAGPID={{item.LARAGPID}},
        IDTYPE={{item.IDTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IDTYPE=LA/RA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA'] -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=LA/RA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA'] -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=LA/RA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA'] -%}
            LAC="{{item.LAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=RA 时必选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            RAC="{{item.RAC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IDTYPE=RA 时可选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            {%- if item.RACRANGE is not none -%}
                RACRANGE="{{item.RACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.5.1.2 配置跟踪区域群记录。

####### 3.5.1.2.1 配置区域群标识和名称。

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_tagp_list -%}
        ADD TAGP:
        {#- --- 必选参数 --- -#}
        TAGPID={{item.TAGPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TANAME is not none -%}
            TANAME="{{item.TANAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

####### 3.5.1.2.2 配置区域群的群成员。

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_tagpmem_list -%}
        ADD TAGPMEM:
        {#- --- 必选参数 --- -#}
        MNC="{{item.MNC}}",
        MCC="{{item.MCC}}",
        TAC="{{item.TAC}}",
        TAGPID={{item.TAGPID}},
        {#- --- 可选参数 --- -#}
        {%- if item.TACRANGE is not none -%}
            TACRANGE="{{item.TACRANGE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.5.2 配置对指定用户范围内用户的区域漫游限制策略。

###### 3.5.2.1 Gb模式下

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_gbsubrrlst_list -%}
        ADD GBSUBRRLST:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        LARAGPID={{item.LARAGPID}},
        ARMODE={{item.ARMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.5.2.2 Iu模式下

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_iusubrrlst_list -%}
        ADD IUSUBRRLST:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        LARAGPID={{item.LARAGPID}},
        ARMODE={{item.ARMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.5.2.3 S1模式下

```jinja2
{%- if is_scenario_user_based_location_restriction -%}
    {%- for item in add_s1subrrlst_list -%}
        ADD S1SUBRRLST:
        {#- --- 必选参数 --- -#}
        ARMODE={{item.ARMODE}},
        SUBRANGE={{item.SUBRANGE}},
        TAGPID={{item.TAGPID}},
        {#- --- 条件必选参数 --- -#}
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

#### 3.6 * **方法3.1: 配置某区域群的用户接入策略。**

#### 在进行策略配置时，该方式不能和“方法3.2: 配置某一特定区域的用户接入策略”同时选择，只能选择其中一种进行配置。

##### 3.6.1 **可选：**配置网络侧的IMEI获取策略为获取IMEI或获取IMEISV。

##### 如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

```jinja2
{%- if is_optional_imei_acquire_policy and is_scenario_area_group_policy -%}
    {%- for item in add_s1imeicfg_list -%}
        ADD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.6.2 将多个区域划分为一个区域群。

###### 3.6.2.1 配置区域群标识和名称。

```jinja2
{%- if is_scenario_area_group_policy -%}
    {%- for item in add_areagp_list -%}
        ADD AREAGP:
        {#- --- 必选参数 --- -#}
        AREAID={{item.AREAID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AREAN is not none -%}
            AREAN="{{item.AREAN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.6.2.2 配置加入区域群的区域信息。

```jinja2
{%- if is_scenario_area_group_policy -%}
    {%- for item in add_areagpmem_list -%}
        ADD AREAGPMEM:
        {#- --- 必选参数 --- -#}
        AREAID={{item.AREAID}},
        IDTYPE={{item.IDTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IDTYPE=TA 时必选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=RA 时必选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            RAC="{{item.RAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=LA/RA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA'] -%}
            LAC="{{item.LAC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IDTYPE=TA 时可选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.6.3 **可选：**配置IMEI TAC与终端类型的映射关系。

##### 如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

```jinja2
{%- if is_optional_imei_tac_mapping and is_scenario_area_group_policy -%}
    {%- for item in add_imeilib_list -%}
        ADD IMEILIB:
        {#- --- 必选参数 --- -#}
        IMEITAC="{{item.IMEITAC}}",
        UETYPE={{item.UETYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.6.4 **可选：**将不同IMSI前缀的用户划分为一个用户群。

##### 如果需要对多个不同IMSI前缀的用户均采用相同的控制策略，则可以通过此步骤将不同IMSI前缀的用户配置为一个用户群。

###### 3.6.4.1 配置用户群标识和名称。

```jinja2
{%- if is_optional_imsi_prefix_user_group and is_scenario_area_group_policy -%}
    {%- for item in add_subgp_list -%}
        ADD SUBGP:
        {#- --- 必选参数 --- -#}
        SUBID={{item.SUBID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.6.4.2 配置加入用户群的IMSI前缀。

```jinja2
{%- if is_optional_imsi_prefix_user_group and is_scenario_area_group_policy -%}
    {%- for item in add_subgpmem_list -%}
        ADD SUBGPMEM:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        SUBID={{item.SUBID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.6.5 配置区域群内不同用户的控制策略。

###### 3.6.5.1 Gb模式下，配置区域群下特定IMSI范围或指定用户群用户的控制策略。

```jinja2
{%- if is_scenario_area_group_policy -%}
    {%- for item in add_gbaccarealst_list -%}
        ADD GBACCAREALST:
        {#- --- 必选参数 --- -#}
        CTRLTYPE={{item.CTRLTYPE}},
        SUBRANGE={{item.SUBRANGE}},
        AREA={{item.AREA}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处以配置区域群下指定用户群用户的控制策略为例。

###### 3.6.5.2 Iu模式下，配置区域群下特定IMSI范围或指定用户群用户的控制策略。

```jinja2
{%- if is_scenario_area_group_policy -%}
    {%- for item in add_iuaccarealst_list -%}
        ADD IUACCAREALST:
        {#- --- 必选参数 --- -#}
        CTRLTYPE={{item.CTRLTYPE}},
        SUBRANGE={{item.SUBRANGE}},
        AREA={{item.AREA}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处以配置区域群下特定IMSI范围用户的控制策略为例。

###### 3.6.5.3 S1模式下，配置区域群下特定IMSI范围、指定终端类型或指定用户群用户进行接入控制。

```jinja2
{%- if is_scenario_area_group_policy -%}
    {%- for item in add_s1accarealst_list -%}
        ADD S1ACCAREALST:
        {#- --- 必选参数 --- -#}
        AREA={{item.AREA}},
        SUBRANGE={{item.SUBRANGE}},
        CTRLTYPE={{item.CTRLTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENBIND is not none -%}
            ENBIND={{item.ENBIND}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：ENBIND=RFSP_ID 时必选 --- -#}
        {%- if item.ENBIND == 'RFSP_ID' -%}
            ENBRFSPIDX={{item.ENBRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：SUBRFSP=YES 时必选 --- -#}
        {%- if item.SUBRFSP == 'YES' -%}
            REJRFSPIDX={{item.REJRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBRFSP is not none -%}
                SUBRFSP={{item.SUBRFSP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.REJCAUSE is not none -%}
                REJCAUSE={{item.REJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.SRVCCCAP is not none -%}
                SRVCCCAP={{item.SRVCCCAP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBCSFB is not none -%}
                SUBCSFB={{item.SUBCSFB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AREA=TA 时可选 --- -#}
        {%- if item.AREA == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.CHKSTNSR is not none -%}
                CHKSTNSR={{item.CHKSTNSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=ALLOW 时可选 --- -#}
        {%- if item.CTRLTYPE == 'ALLOW' -%}
            {%- if item.SPECSUB is not none -%}
                SPECSUB={{item.SPECSUB}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处以配置区域群下指定终端类型用户的控制策略为例。

#### 3.7 * **针对特征用户的接入控制**

##### 3.7.1 在进行策略配置时，该方式不能和“方法3.2: 配置某一特定区域的用户接入策略”同时选择，只能选择其中一种进行配置。

##### 3.7.2 此种场景下TAU流程的Downlink NAS Transport消息中的特征SPID信元是R10协议新增的，需要判断eNodeB是否都支持此信元，如果支持，将**SET S1CMPT**命令中的“SPID”设置为“YES”，此时TAU流程中的Downlink NAS Transport消息才会携带特征RFSP。否则，“SPID”需要设置为“NO”，避免对不支持此信元的eNodeB产生影响，此时TAU流程中的Downlink NAS Transport消息不会携带特征RFSP。

##### 3.7.3 针对特征用户进行接入控制的策略不支持根据MSISDN配置接入策略。

##### 3.7.4 配置特定限制区域群。

###### 3.7.4.1 增加特定限制区域群。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_areagp_list_1 -%}
        ADD AREAGP:
        {#- --- 必选参数 --- -#}
        AREAID={{item.AREAID}},
        {#- --- 可选参数 --- -#}
        {%- if item.AREAN is not none -%}
            AREAN="{{item.AREAN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.7.4.2 增加特定限制区域群成员。

###### 所有特定限制区域需要配置在一个区域群“AREAID”中。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_areagpmem_list_1 -%}
        ADD AREAGPMEM:
        {#- --- 必选参数 --- -#}
        AREAID={{item.AREAID}},
        IDTYPE={{item.IDTYPE}},
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IDTYPE=TA 时必选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=RA 时必选 --- -#}
        {%- if item.IDTYPE == 'RA' -%}
            RAC="{{item.RAC}}",
        {%- endif -%}
        {#- --- 条件必选：IDTYPE=LA/RA 时必选 --- -#}
        {%- if item.IDTYPE in ['LA', 'RA'] -%}
            LAC="{{item.LAC}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IDTYPE=TA 时可选 --- -#}
        {%- if item.IDTYPE == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.7.5 设置特征RFSP取值范围以便于控制用户接入。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_specrfspvalue_list -%}
        ADD SPECRFSPVALUE:
        {#- --- 必选参数 --- -#}
        RFSPIDX={{item.RFSPIDX}},
        TYPE={{item.TYPE}},
        BEGRFSP={{item.BEGRFSP}},
        ENDRFSP={{item.ENDRFSP}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.7.6 设置特征用户的接入控制策略。

###### 3.7.6.1 配置所有本网用户限制策略，以实现用户诉求第一种场景。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_s1accarealst_list_3 -%}
        ADD S1ACCAREALST:
        {#- --- 必选参数 --- -#}
        AREA={{item.AREA}},
        SUBRANGE={{item.SUBRANGE}},
        CTRLTYPE={{item.CTRLTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENBIND is not none -%}
            ENBIND={{item.ENBIND}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=FOREIGN_USER/HOME_USER 时必选 --- -#}
        {%- if item.SUBRANGE in ['FOREIGN_USER', 'HOME_USER'] -%}
            NOID={{item.NOID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRFSP=YES 时必选 --- -#}
        {%- if item.SUBRFSP == 'YES' -%}
            REJRFSPIDX={{item.REJRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：ENBIND=RFSP_ID 时必选 --- -#}
        {%- if item.ENBIND == 'RFSP_ID' -%}
            ENBRFSPIDX={{item.ENBRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=ALLOW 时可选 --- -#}
        {%- if item.CTRLTYPE == 'ALLOW' -%}
            {%- if item.SPECSUB is not none -%}
                SPECSUB={{item.SPECSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBRFSP is not none -%}
                SUBRFSP={{item.SUBRFSP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBCSFB is not none -%}
                SUBCSFB={{item.SUBCSFB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.REJCAUSE is not none -%}
                REJCAUSE={{item.REJCAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.SRVCCCAP is not none -%}
                SRVCCCAP={{item.SRVCCCAP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AREA=TA 时可选 --- -#}
        {%- if item.AREA == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.CHKSTNSR is not none -%}
                CHKSTNSR={{item.CHKSTNSR}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.7.6.2 配置外网用户中特定IMSI前缀用户限制策略，可配置多条，以实现用户诉求第二种场景。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_s1accarealst_list_4 -%}
        ADD S1ACCAREALST:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        CTRLTYPE={{item.CTRLTYPE}},
        AREA={{item.AREA}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENBIND is not none -%}
            ENBIND={{item.ENBIND}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：ENBIND=RFSP_ID 时必选 --- -#}
        {%- if item.ENBIND == 'RFSP_ID' -%}
            ENBRFSPIDX={{item.ENBRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：SUBRFSP=YES 时必选 --- -#}
        {%- if item.SUBRFSP == 'YES' -%}
            REJRFSPIDX={{item.REJRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.SRVCCCAP is not none -%}
                SRVCCCAP={{item.SRVCCCAP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBRFSP is not none -%}
                SUBRFSP={{item.SUBRFSP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AREA=TA 时可选 --- -#}
        {%- if item.AREA == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.CHKSTNSR is not none -%}
                CHKSTNSR={{item.CHKSTNSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=ALLOW 时可选 --- -#}
        {%- if item.CTRLTYPE == 'ALLOW' -%}
            {%- if item.SPECSUB is not none -%}
                SPECSUB={{item.SPECSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBCSFB is not none -%}
                SUBCSFB={{item.SUBCSFB}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.7.6.3 配置其它外网用户限制策略，以实现用户诉求第三种场景。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in add_s1accarealst_list_5 -%}
        ADD S1ACCAREALST:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        CTRLTYPE={{item.CTRLTYPE}},
        AREA={{item.AREA}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENBIND is not none -%}
            ENBIND={{item.ENBIND}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：ENBIND=RFSP_ID 时必选 --- -#}
        {%- if item.ENBIND == 'RFSP_ID' -%}
            ENBRFSPIDX={{item.ENBRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：SUBRFSP=YES 时必选 --- -#}
        {%- if item.SUBRFSP == 'YES' -%}
            REJRFSPIDX={{item.REJRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.SRVCCCAP is not none -%}
                SRVCCCAP={{item.SRVCCCAP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBRFSP is not none -%}
                SUBRFSP={{item.SUBRFSP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AREA=TA 时可选 --- -#}
        {%- if item.AREA == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.CHKSTNSR is not none -%}
                CHKSTNSR={{item.CHKSTNSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=ALLOW 时可选 --- -#}
        {%- if item.CTRLTYPE == 'ALLOW' -%}
            {%- if item.SPECSUB is not none -%}
                SPECSUB={{item.SPECSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBCSFB is not none -%}
                SUBCSFB={{item.SUBCSFB}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.7.7 **可选：**在HSS需要根据IMEI识别特征用户的场景下，配置用户获取IMEI策略。

###### 3.7.7.1 查询用户获取IMEI策略是否配置。

###### 3.7.7.2 + **可选：**如果之前没有配置获取IMEI策略，需要执行此步骤。

```jinja2
{%- set LST_S1IMEICFG=getParameterValue('LST S1IMEICFG') -%}
{%- if is_optional_user_imei_policy and is_scenario_feature_user_access_control and LST_S1IMEICFG=='' -%}
    {%- for item in mod_s1imeicfg_list -%}
        MOD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.7.8 为防止用户在移动或切换时接入特定限制区域，系统下发给UE的TA List中过滤禁止UE接入的TA，且系统向eNodeB发送禁止用户接入的TA列表。

```jinja2
{%- if is_scenario_feature_user_access_control -%}
    {%- for item in set_mmfunc_list_2 -%}
        SET MMFUNC:
        {#- --- 可选参数 --- -#}
        {%- if item.TALIST is not none -%}
            TALIST={{item.TALIST}},
        {%- endif -%}
        {%- if item.FORBIDTA is not none -%}
            FORBIDTA={{item.FORBIDTA}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.8 * **方法3.2: 配置某一特定区域的用户接入策略**

#### 在进行策略配置时，该方式不能和“方法3.1: 配置某区域群的用户接入策略”和“基于特征RFSP值场景下的区域漫游限制”同时选择，只能选择其中一种进行配置。

##### 3.8.1 **可选：**配置网络侧的IMEI获取策略为获取IMEI或获取IMEISV。

##### 如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

```jinja2
{%- if is_optional_imei_acquire_policy and is_scenario_specific_area_policy -%}
    {%- for item in add_s1imeicfg_list_1 -%}
        ADD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.8.2 **可选：**配置IMEI TAC与终端类型的映射关系。

##### 如果需要对指定终端类型用户进行接入控制，需要配置此步骤。

```jinja2
{%- if is_optional_imei_tac_mapping and is_scenario_specific_area_policy -%}
    {%- for item in add_imeilib_list_1 -%}
        ADD IMEILIB:
        {#- --- 必选参数 --- -#}
        IMEITAC="{{item.IMEITAC}}",
        UETYPE={{item.UETYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.8.3 **可选：**将不同IMSI前缀的用户划分为一个用户群。

##### 如果需要对多个不同IMSI前缀的用户均采用相同的控制策略，则可以通过此步骤将不同IMSI前缀的用户配置为一个用户群。

###### 3.8.3.1 配置用户群标识和名称。

```jinja2
{%- if is_optional_imsi_prefix_user_group and is_scenario_specific_area_policy -%}
    {%- for item in add_subgp_list_1 -%}
        ADD SUBGP:
        {#- --- 必选参数 --- -#}
        SUBID={{item.SUBID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.8.3.2 查询IMSI用户群成员。

###### 系统采用最长匹配原则查询对用户的接入限制策略。例如IMSI为1234567890的用户接入时，若系统中同时存在以下3条记录，那该用户只会匹配到SUBID=3对应的接入限制策略。因此在添加IMSI前缀用户群成员前需要先查询当前范围的用户是否已存在配置记录，避免对该用户的部分接入限制策略不生效。

###### - ADD SUBGPMEM: SUBID=1, IMSIPRE="123456";

###### - ADD SUBGPMEM: SUBID=2, IMSIPRE="1234567";

###### - ADD SUBGPMEM: SUBID=3, IMSIPRE="12345678";

###### 3.8.3.3 + **可选：**

###### 配置加入用户群的IMSI前缀。

```jinja2
{%- if is_optional_imsi_prefix_member and is_optional_imsi_prefix_user_group and is_scenario_specific_area_policy -%}
    {%- for item in add_subgpmem_list_1 -%}
        ADD SUBGPMEM:
        {#- --- 必选参数 --- -#}
        IMSIPRE="{{item.IMSIPRE}}",
        SUBID={{item.SUBID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.8.4 **可选：**将不同MSISDN前缀的用户划分为一个用户群。

##### 如果需要对多个不同MSISDN前缀的用户均采用相同的控制策略，则可以通过此步骤将不同MSISDN前缀的用户配置为一个用户群。

###### 3.8.4.1 配置用户群标识和名称。

```jinja2
{%- if is_optional_msisdn_prefix_user_group and is_scenario_specific_area_policy -%}
    {%- for item in add_subgp_list_2 -%}
        ADD SUBGP:
        {#- --- 必选参数 --- -#}
        SUBID={{item.SUBID}},
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.8.4.2 查询MSISDN用户群成员。

###### 系统采用最长匹配原则查询对用户的接入限制策略。例如MSISDN为1234567890的用户接入时，若系统中同时存在以下3条记录，那该用户只会匹配到SUBID=3对应的接入限制策略。因此在添加MSISDN前缀用户群成员前需要先查询当前范围的用户是否已存在配置记录，避免对该用户的部分接入限制策略不生效。

###### - ADD MSISDNSUBGPMEM: SUBID=1, MSISDNPRE="123456";

###### - ADD MSISDNSUBGPMEM: SUBID=2, MSISDNPRE="1234567";

###### - ADD MSISDNSUBGPMEM: SUBID=3, MSISDNPRE="12345678";

###### 3.8.4.3 + **可选：**

###### 配置加入用户群的MSISDN前缀。

```jinja2
{%- if is_optional_msisdn_prefix_member and is_optional_msisdn_prefix_user_group and is_scenario_specific_area_policy -%}
    {%- for item in add_msisdnsubgpmem_list -%}
        ADD MSISDNSUBGPMEM:
        {#- --- 必选参数 --- -#}
        SUBID={{item.SUBID}},
        MSISDNPRE="{{item.MSISDNPRE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### - 对于同一用户如果系统中同时存在基于IMSI前缀和基于MSISDN前缀的接入限制策略，用户接入时，系统将按照基于IMSI前缀对应的策略对其进行接入限制。

###### - 在Inter Handover和Inter Relocation流程中，新侧MME无法从老侧MME获取到MSISDN，因此在这两个流程中新侧MME无法根据MSISDN判断是否允许用户接入该区域，直到后续通过TAU/RAU流程获取到用户签约数据后才能对用户进行接入控制。

##### 3.8.5 配置特定区域内不同用户的控制策略。

###### 3.8.5.1 Gb模式下，配置特定区域下特定IMSI范围或指定用户群用户的控制策略。

```jinja2
{%- if is_scenario_specific_area_policy -%}
    {%- for item in add_gbaccarealst_list_1 -%}
        ADD GBACCAREALST:
        {#- --- 必选参数 --- -#}
        CTRLTYPE={{item.CTRLTYPE}},
        SUBRANGE={{item.SUBRANGE}},
        AREA={{item.AREA}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处特定区域的区域范围以指定路由区为例，并以配置指定用户群用户的控制策略为例。

###### 3.8.5.2 Iu模式下，配置特定区域下特定IMSI范围或指定用户群用户的控制策略。

```jinja2
{%- if is_scenario_specific_area_policy -%}
    {%- for item in add_iuaccarealst_list_1 -%}
        ADD IUACCAREALST:
        {#- --- 必选参数 --- -#}
        CTRLTYPE={{item.CTRLTYPE}},
        SUBRANGE={{item.SUBRANGE}},
        AREA={{item.AREA}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=LA/RA 时必选 --- -#}
        {%- if item.AREA in ['LA', 'RA'] -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处特定区域的区域范围以指定路由区为例，并以配置特定IMSI范围用户的控制策略为例。

###### 3.8.5.3 S1模式下，配置特定区域下特定IMSI范围、指定终端类型或指定用户群用户进行接入控制。

```jinja2
{%- if is_scenario_specific_area_policy -%}
    {%- for item in add_s1accarealst_list_6 -%}
        ADD S1ACCAREALST:
        {#- --- 必选参数 --- -#}
        AREA={{item.AREA}},
        SUBRANGE={{item.SUBRANGE}},
        CTRLTYPE={{item.CTRLTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.ENBIND is not none -%}
            ENBIND={{item.ENBIND}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MCC="{{item.MCC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            MNC="{{item.MNC}}",
        {%- endif -%}
        {#- --- 条件必选：AREA=TA 时必选 --- -#}
        {%- if item.AREA == 'TA' -%}
            TAC="{{item.TAC}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSIPRE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSIPRE' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=UE_TYPE 时必选 --- -#}
        {%- if item.SUBRANGE == 'UE_TYPE' -%}
            UETYPE={{item.UETYPE}},
        {%- endif -%}
        {#- --- 条件必选：AREA=AG 时必选 --- -#}
        {%- if item.AREA == 'AG' -%}
            AREAID={{item.AREAID}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=USER_GROUP 时必选 --- -#}
        {%- if item.SUBRANGE == 'USER_GROUP' -%}
            SUBID={{item.SUBID}},
        {%- endif -%}
        {#- --- 条件必选：CAUSE=CUSTOMER_DEFINED 时必选 --- -#}
        {%- if item.CAUSE == 'CUSTOMER_DEFINED' -%}
            SDCAUSE={{item.SDCAUSE}},
        {%- endif -%}
        {#- --- 条件必选：ENBIND=RFSP_ID 时必选 --- -#}
        {%- if item.ENBIND == 'RFSP_ID' -%}
            ENBRFSPIDX={{item.ENBRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：SUBRFSP=YES 时必选 --- -#}
        {%- if item.SUBRFSP == 'YES' -%}
            REJRFSPIDX={{item.REJRFSPIDX}},
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            ENDIMSI="{{item.ENDIMSI}}",
        {%- endif -%}
        {#- --- 条件必选：SUBRANGE=SPECIAL_IMSI_RANGE 时必选 --- -#}
        {%- if item.SUBRANGE == 'SPECIAL_IMSI_RANGE' -%}
            BEGIMSI="{{item.BEGIMSI}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CTRLTYPE=REJECT 时可选 --- -#}
        {%- if item.CTRLTYPE == 'REJECT' -%}
            {%- if item.CAUSE is not none -%}
                CAUSE={{item.CAUSE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CTRLTYPE=ALLOW 时可选 --- -#}
        {%- if item.CTRLTYPE == 'ALLOW' -%}
            {%- if item.SPECSUB is not none -%}
                SPECSUB={{item.SPECSUB}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.SRVCCCAP is not none -%}
                SRVCCCAP={{item.SRVCCCAP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBRFSP is not none -%}
                SUBRFSP={{item.SUBRFSP}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：AREA=TA 时可选 --- -#}
        {%- if item.AREA == 'TA' -%}
            {%- if item.TACRANGE is not none -%}
                TACRANGE="{{item.TACRANGE}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUBCSFB=YES 时可选 --- -#}
        {%- if item.SUBCSFB == 'YES' -%}
            {%- if item.CHKSTNSR is not none -%}
                CHKSTNSR={{item.CHKSTNSR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPECSUB=YES 时可选 --- -#}
        {%- if item.SPECSUB == 'YES' -%}
            {%- if item.SUBCSFB is not none -%}
                SUBCSFB={{item.SUBCSFB}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 此处特定区域的区域范围以指定跟踪区为例，并以配置指定终端类型用户的控制策略为例。

