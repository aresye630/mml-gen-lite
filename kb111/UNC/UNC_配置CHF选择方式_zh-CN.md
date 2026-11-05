---
id: ''
name: 配置CHF选择方式
ne_type: UNC
type: feature
description: UNC支持基于IMSI选择CHF、基于IMSI号段选择CHF、基于PCF下发的FQDN选择CHF、基于用户的计费属性Charging Characteristics（CC）选择CHF，也支持基于标准化服务发现选择CHF。  UNC选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。如果无法通过高优先级的方式选择CHF，则依次向下使用低一级别的方式进行选择。  其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择CHF方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","配置CHF选择方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UNC支持基于IMSI选择CHF、基于IMSI号段选择CHF、基于PCF下发的FQDN选择CHF、基于用户的计费属性Charging Characteristics（CC）选择CHF，也支持基于标准化服务发现选择CHF。UNC选择CHF的优先级从高到低依次是：基于IMSI选择CHF > 基于IMSI号段选择CHF > 基于PCF下发的信息选择CHF > 基于从UDM获取的签约CC选择CHF > 基于标准化服务发现选择CHF > 基于SMF本地配置的CC选择CHF。如果无法通过高优先级的方式选择CHF，则依次向下使用低一级别的方式进行选择。其中，通过**ADD SELCHFGBYIMSI**命令配置基于IMSI选择CHF方式一般用于测试场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_tnfins_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tnfinsip_list:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
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
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置CHF Group。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfbindgrp_list:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '将CHF实例绑定到CHF组上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selchfgbyimsi_list:
      type: items
      properties:
        IMSI:
          name: '用户的IMSI'
          type: string
          minLength: 14
          maxLength: 15
          required: true
          description: '配置IMSI与主备CHF组的绑定关系。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tnfins_list_2:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tnfinsip_list_2:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
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
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list_2:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置CHF Group。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfbindgrp_list_2:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '将CHF实例绑定到CHF组上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selchfgbimsiseg_list:
      type: items
      properties:
        SEGSTART:
          name: '号段起始字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '用于设置绑定的IMSI号段的起始字符串。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '用于设置绑定的IMSI号段的结束字符串。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '主CHF组，使用**ADD TNFGRP**命令配置生成。'
          data_source: '主CHF组'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '备CHF组，使用**ADD TNFGRP**命令配置生成。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tnfins_list_4:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 127
          required: false
          description: '与PCF下发的FQDN名称保持一致。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_tnfinsip_list_4:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
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
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfins_list_6:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TNFINSNAME:
          name: '目标NF实例名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_tnfinsip_list_6:
      type: items
      properties:
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: '增加主备CHF实例的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - NONEIP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4类型地址'
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
        IPV6ADDR:
          name: 'IPV6类型地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfgrp_list_4:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '配置CHF Group。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TNFTYPE:
          name: '目标NF类型'
          type: string
          enum:
          - CHF
          - UPF
          - PCSCF
          - PCF
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNFGRPNAME:
          name: '目标NF组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tnfbindgrp_list_4:
      type: items
      properties:
        TNFGRPINDEX:
          name: '目标NF组索引'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '将CHF实例绑定到CHF组上。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TNFINSINDEX:
          name: '目标NF实例索引'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_selectchfgbycc_list:
      type: items
      properties:
        CCTYPE:
          name: 'Charge Characteristic类型'
          type: string
          enum:
          - DEFAULT
          - VALUE
          required: true
          description: '配置CC和CHF Group的关联关系。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CCVALUE:
          name: 'Charge Characteristic值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: '本地CC时，从已配置数据中获取。  从UDM获取签约CC时，从对端获取。'
          data_source: '已配置数据中获取/从对端获取'
          pattern: ''
          default: ''
        MASK:
          name: 'Charge Characteristic特定值掩码'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'Charge Characteristic优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '数值越小，优先级越高。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIMARYCHFGRP:
          name: '主CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SECONDARYCHFGRP:
          name: '备CHF组'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pnfsupi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfgpsi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATTERN:
          name: '模式'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_tnfins_list:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
    add_tnfinsip_list:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfgrp_list:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    add_selchfgbyimsi_list:
    - IMSI: '123456789012345'
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_tnfins_list_2:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
    add_tnfinsip_list_2:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfgrp_list_2:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list_2:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    add_selchfgbimsiseg_list:
    - SEGSTART: '12345678901'
      SEGEND: '12345678905'
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_tnfins_list_4:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
      FQDN: 'chf1.hw.com'
    add_tnfinsip_list_4:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfins_list_6:
    - TNFINSINDEX: 1
      TNFTYPE: CHF
      TNFINSNAME: 'target_chf_0'
      SCHEMA: http
    add_tnfinsip_list_6:
    - TNFINSINDEX: 1
      IPTYPE: IPV4
      IPV4ADDR: '192.168.94.2'
      PORT: 3220
      IPV6ADDR: ''
    add_tnfgrp_list_4:
    - TNFGRPINDEX: 1
      TNFTYPE: CHF
      TNFGRPNAME: 'ChfGroup1'
    add_tnfbindgrp_list_4:
    - TNFGRPINDEX: 1
      TNFINSINDEX: 1
    add_selectchfgbycc_list:
    - CCTYPE: VALUE
      CCVALUE: '0x1111'
      MASK: '0xffff'
      PRIORITY: 2
      PRIMARYCHFGRP: 'ChfGroup1'
      SECONDARYCHFGRP: 'ChfGroup2'
    add_pnfsupi_list:
    - INDEX: 1
      NFINSTANCEID: 'CHF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100001'
      PATTERN: ''
    add_pnfgpsi_list:
    - INDEX: 1
      NFINSTANCEID: 'CHF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '138100000000000'
      RANGEEND: '138100000000001'
      PATTERN: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置基于IMSI选择CHF组。一般用于拨测场景，将指定IMSI的用户的计费信息发送到指定CHF上，测试CHF的基本功能。

```jinja2
{%- for item in add_tnfins_list -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfinsip_list -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfgrp_list -%}
    ADD TNFGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFGRPNAME="{{item.TNFGRPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfbindgrp_list -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_selchfgbyimsi_list -%}
    ADD SELCHFGBYIMSI:
    {#- --- 必选参数 --- -#}
    IMSI="{{item.IMSI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置基于IMSI号段选择CHF。针对现网存在多个CHF主备组，为了避免CHF之间业务不均衡，通过将不同IMSI号段范围和CHF主备组的绑定将用户分流到不同CHF。

```jinja2
{%- for item in add_tnfins_list_2 -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfinsip_list_2 -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfgrp_list_2 -%}
    ADD TNFGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFGRPNAME="{{item.TNFGRPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_tnfbindgrp_list_2 -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_selchfgbimsiseg_list -%}
    ADD SELCHFGBIMSISEG:
    {#- --- 必选参数 --- -#}
    SEGSTART="{{item.SEGSTART}}",
    SEGEND="{{item.SEGEND}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置基于PCF下发的FQDN查询CHF。

#### 3.1 进入“MML命令行-UNC”窗口。

#### 3.2 配置目标CHF实例。

```jinja2
{%- for item in add_tnfins_list_4 -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    {%- if item.FQDN is not none -%}
        FQDN="{{item.FQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置目标CHF实例的IP地址信息。

```jinja2
{%- for item in add_tnfinsip_list_4 -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置基于CC值选择CHF。

#### 4.1 配置计费属性。计费属性信息都能从UDM获取时，请跳过该步骤。

#### 请参见配置计费属性CC。

#### 4.2 配置CHF Group。

##### 4.2.1 配置目标CHF实例。

```jinja2
{%- for item in add_tnfins_list_6 -%}
    ADD TNFINS:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFINSNAME="{{item.TNFINSNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SCHEMA is not none -%}
        SCHEMA={{item.SCHEMA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.2.2 配置目标CHF实例的IP地址信息。

```jinja2
{%- for item in add_tnfinsip_list_6 -%}
    ADD TNFINSIP:
    {#- --- 必选参数 --- -#}
    TNFINSINDEX={{item.TNFINSINDEX}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 端口号: 条件必选(IP地址类型=NONEIP) / 条件可选(IP地址类型=IPV4|IPV6) --- -#}
    {%- if (item.IPTYPE == 'NONEIP') -%}
        PORT={{item.PORT}},
    {%- elif (item.IPTYPE in ['IPV4', 'IPV6']) -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 4.2.3 配置CHF组。

```jinja2
{%- for item in add_tnfgrp_list_4 -%}
    ADD TNFGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFTYPE={{item.TNFTYPE}},
    TNFGRPNAME="{{item.TNFGRPNAME}}",
    ;
{%- endfor -%}
```

##### 4.2.4 将目标CHF绑定到CHF组。

```jinja2
{%- for item in add_tnfbindgrp_list_4 -%}
    ADD TNFBINDGRP:
    {#- --- 必选参数 --- -#}
    TNFGRPINDEX={{item.TNFGRPINDEX}},
    TNFINSINDEX={{item.TNFINSINDEX}},
    ;
{%- endfor -%}
```

#### 4.3 配置基于CC选择CHF组。

```jinja2
{%- for item in add_selectchfgbycc_list -%}
    ADD SELECTCHFGBYCC:
    {#- --- 必选参数 --- -#}
    CCTYPE={{item.CCTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIMARYCHFGRP is not none -%}
        PRIMARYCHFGRP="{{item.PRIMARYCHFGRP}}",
    {%- endif -%}
    {%- if item.SECONDARYCHFGRP is not none -%}
        SECONDARYCHFGRP="{{item.SECONDARYCHFGRP}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CCTYPE=VALUE 时必选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CCTYPE=VALUE 时可选 --- -#}
    {%- if item.CCTYPE == 'VALUE' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置基于标准化服务发现选择的CHF。服务化发现CHF存在以下两种方式：

#### 5.1 基于NRF选择CHF，不需要专有配置。

#### 5.2 基本本地配置选择CHF。

#### 选择支持特定SUPI的CHF：**ADD PNFSUPI**

```jinja2
{%- if is_scenario_local_config_selection and is_scenario_supi -%}
    {%- for item in add_pnfsupi_list -%}
        ADD PNFSUPI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 选择支持特定GPSI的CHF：**ADD PNFGPSI**

```jinja2
{%- if is_scenario_local_config_selection and is_scenario_gpsi -%}
    {%- for item in add_pnfgpsi_list -%}
        ADD PNFGPSI:
        {#- --- 必选参数 --- -#}
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        QUERYTYPE={{item.QUERYTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=PATTERN 时必选 --- -#}
        {%- if item.QUERYTYPE == 'PATTERN' -%}
            PATTERN="{{item.PATTERN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

