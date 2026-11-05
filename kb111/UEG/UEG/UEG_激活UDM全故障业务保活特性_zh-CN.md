---
id: GWFD-021408
name: 激活UDM全故障业务保活特性
ne_type: UEG
type: feature
description: 为提升UDM全故障场景下的业务连续性，可以激活本特性。UDM全故障业务保活特性需要在AMF和SMF侧分别开启UDM全故障业务保活特性。  适用于AMF、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","AMF特性指南","GWFD-021400 可靠性功能","GWFD-021408 UDM全故障业务保活","激活UDM全故障业务保活特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为提升UDM全故障场景下的业务连续性，可以激活本特性。UDM全故障业务保活特性需要在AMF和SMF侧分别开启UDM全故障业务保活特性。适用于AMF、SMF

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-021408 UDM全故障业务保活特性概述。
* 完成加载License。
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
          description: '在AMF侧开启UDM全故障业务保活特性的License开关。'
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
    set_amfudmbypass_list:
      type: items
      properties:
        SWITCH:
          name: 'UDM全故障Bypass开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '在AMF侧开启UDM全故障业务保活功能开关，并设置相关策略。其中：   * “UDM退出Bypass恢复动作（RECOVERYACT）”用于设置用户退出UDM Bypass状态时AMF执行的操作，包括先去注册用户后再标识用户退出UDM Bypass状态、先补齐与UDM的交互流程后再标识用户退出UDM Bypass状态两种方式。 * “部署模式（DEPLOYMENTMODE）”用于指定AUSF和UDM的部署模式，包括合并部署和独立部署两种模式。该部署模式与现网UDM和AUSF的实际部署模式无关，仅用于判断当主备AUSF均故障后是否仍需要与UDM进行交互。合设模式下，主备AUSF均故障后直接标识用户进入UDM Bypass状态，不再尝试与UDM交互。分设模式下，主备AUSF故障后继续尝试与UDM交互，主备UDM均故障后才标识用户进入UDM Bypass状态。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RECOVERYACT:
          name: 'UDM退出Bypass恢复动作'
          type: string
          enum:
          - DEREG
          - SUPPLEMENT_UDM_INTERACT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FAULTDETECTRATE:
          name: '故障探测速率(个/秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCANINTERVAL:
          name: '扫描时间间隔(秒)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RPTFAILCHR:
          name: '上报异常CHR开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEPLOYMENTMODE:
          name: '部署模式'
          type: string
          enum:
          - CO_DEPLOYMENT
          - SEPARATE_DEPLOYMENT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTOEXITSW:
          name: 'UDM Bypass自动退出开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '此处以自动退出UDM Bypass状态举例。如果期望配置不自动退出UDM Bypass状态，则参数值需要配置为“OFF”，后续需要通过手动执行**STR AMFEXITUDMBYPASS**命令触发用户退出UDM Bypass状态。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_udmbypasssub_list:
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
          required: true
          description: '在AMF侧增加UDM Bypass后的最小签约数据。UDM全故障后，AMF无法从UDM侧获取SMF选择签约数据（smfSelData）用以建立PDU会话，因此必须在AMF侧配置SMF选择签约数据。  “SMF选择签约数据”格式：切片1名称:DNN1名称|DNN2名称|...|DNNs名称&切片2名称:DNN1名称|DNN2名称|...|DNNs名称'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAIINFOSSW:
          name: '是否配置SMF选择签约数据'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SNSSAIINFOS:
          name: 'SMF选择签约数据'
          type: string
          minLength: 0
          maxLength: 256
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '可选，设置AMF在匹配用户当前安全上下文时，忽略TSC标识，解决由于手机TSC携带错误导致用户安全检查失败而无法接入的问题。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在AUSF或UDM全故障的场景下应急使用，默认不配置。在AMF侧增加该配置后，当主用AUSF或UDM返回指定状态码时，不再进行重选，立即标识用户进入UDM Bypass状态。当主备AUSF或UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_2:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在AUSF或UDM全故障的场景下应急使用，默认不配置。在AMF侧增加该配置后，当主用AUSF或UDM返回指定状态码时，不再进行重选，立即标识用户进入UDM Bypass状态。当主备AUSF或UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_4:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在AUSF或UDM全故障的场景下应急使用，默认不配置。在AMF侧增加该配置后，当主用AUSF或UDM返回指定状态码时，不再进行重选，立即标识用户进入UDM Bypass状态。当主备AUSF或UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_6:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在AUSF或UDM全故障的场景下应急使用，默认不配置。在AMF侧增加该配置后，当主用AUSF或UDM返回指定状态码时，不再进行重选，立即标识用户进入UDM Bypass状态。当主备AUSF或UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ERRINFO:
          name: '错误信息'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfpeerselfunc_list:
      type: items
      properties:
        AUSFRESELEN:
          name: 'AUSF重选增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_2:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_3:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
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
          description: '配置是否支持通过N26接口向MME传递MSISDN。涉及消息有：Identification Response、Context Response、Forward Relocation Request。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSISDNSW:
          name: '是否传递MSISDN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PVTMSISDNSW:
          name: '是否在Private Extension信元传递MSISDN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_n26mmechar_list:
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
          description: '配置是否支持通过N26接口向MME传递MSISDN。涉及消息有：Identification Response、Context Response、Forward Relocation Request。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSISDNSW:
          name: '是否传递MSISDN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PVTMSISDNSW:
          name: '是否在Private Extension信元传递MSISDN'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_4:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '在SMF侧开启UDM全故障业务保活特性的License开关。'
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
    add_5gcsubqos_list:
      type: items
      properties:
        SUBQOSINDEX:
          name: '用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '在SMF侧增加UDM Bypass后的用户签约QoS属性和指定APN的QoS属性。进入UDM全故障业务保护流程后，SMF需要使用本地通用签约数据完成PDU会话建立。  说明：  用户签约的QoS属性和指定APN的QoS属性请根据用户实际QoS属性进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIVEQI:
          name: '标准5QI'
          type: integer
          minimum: 5
          maximum: 80
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnqosbypass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBQOSINDEX:
          name: '5G用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_commqosbypass_list:
      type: items
      properties:
        DEFSW:
          name: '通用QoS描述开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '配置UDM全故障BYPASS场景下QoS描述的通用信息。未指定APN的QoS描述信息的用户，可使用通用QoS描述信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBQOSINDEX:
          name: '5G用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smfudmbypass_list:
      type: items
      properties:
        UDMBYPASS:
          name: 'UDM全故障Bypass开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '在SMF侧开启UDM全故障Bypass功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FAULTDETECTRATE:
          name: '故障探测速率(个/秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCANINTERVAL:
          name: '扫描时间间隔(秒)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RPTFAILCHR:
          name: '上报异常CHR开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTOEXITSW:
          name: '自动退出Bypass功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '此处以自动退出UDM Bypass状态举例。如果期望配置不自动退出UDM Bypass状态，则参数值需要配置为“OFF”，后续需要通过手动执行**STR SMFEXITUDMBYPASS**命令触发会话退出UDM Bypass状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_edgesmcommfunc_list:
      type: items
      properties:
        UDMSTATICIPSW:
          name: 'UDM静态IP功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启UDM静态IP功能，当UDM全部故障时，静态IP用户可使用本地配置的静态IP激活。当用户请求IPv4v6双栈地址面本地只配置了IPv4或者IPv6单栈地址时，为用户分配本地配置的单栈地址。  说明：  **SET EDGESMCOMMFUNC**的“Radius静态IP功能开关（RDSSTATICIPSW）”参数优先级高于“UDM静态IP功能开关（UDMSTATICIPSW）”参数，“Radius静态IP功能开关（RDSSTATICIPSW）”参数和“UDM静态IP功能开关（UDMSTATICIPSW）”参数两者中有一个开启，静态用户即可使用本地配置的静态IP激活。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UDMIPTYPE:
          name: 'UDM静态IP类型'
          type: string
          enum:
          - SINGLE_STACK
          - DUAL_STACK
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rdsstaticippara_list:
      type: items
      properties:
        IMSI:
          name: '用户IMSI号'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '为静态IP用户配置UDM静态IP信息。  说明：  此处参数取值为举例，请根据用户实际签约情况进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV4V6
          - Ethernet
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rdsstaticippara_list_1:
      type: items
      properties:
        IMSI:
          name: '用户IMSI号'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: '（可选）基于IMSI为5G LAN用户配置5G LAN组。  说明：  * 如果存在5G LAN业务，需要在本地配置5G LAN组。 * 此处参数取值为举例，请根据用户实际签约情况进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV4V6
          - Ethernet
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_edgenglangroup_list:
      type: items
      properties:
        DNN:
          name: 'DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '（可选）基于DNN为5G LAN用户配置5G LAN组。  说明：  * 如果存在5G LAN业务，需要在本地配置5G LAN组。 * 此处参数取值为举例，请根据用户实际签约情况进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDUSESSIONTYPE:
          name: 'PDU会话类型'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPV4V6
          - Ethernet
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '5G LAN组ID'
          type: string
          minLength: 18
          maxLength: 37
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_8:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在UDM全故障的场景下应急使用，默认不配置。在SMF侧增加该配置后，当主用UDM返回指定状态码时，不再进行重选，立即标记会话进入UDM Bypass状态。当主备UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_9:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在UDM全故障的场景下应急使用，默认不配置。在SMF侧增加该配置后，当主用UDM返回指定状态码时，不再进行重选，立即标记会话进入UDM Bypass状态。当主备UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_10:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在UDM全故障的场景下应急使用，默认不配置。在SMF侧增加该配置后，当主用UDM返回指定状态码时，不再进行重选，立即标记会话进入UDM Bypass状态。当主备UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_bypassfaultcode_list_11:
      type: items
      properties:
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - UDM
          - AUSF
          required: true
          description: '可选，仅在已明确存在UDM全故障的场景下应急使用，默认不配置。在SMF侧增加该配置后，当主用UDM返回指定状态码时，不再进行重选，立即标记会话进入UDM Bypass状态。当主备UDM中任何一个网元恢复正常后，需要删除该配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: '网元实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CUSFAULTCODE:
          name: '自定义故障码'
          type: string
          minLength: 1
          maxLength: 64
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ERRINFO:
          name: '错误信息'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置DNN对应的默认切片。  说明：  * 一个DNN可以绑定多个切片，但是默认切片只能配置一个； * 根据网络规划配置DNN对应的唯一默认切片，例如：MOD NSDNN: NSIDX=0, DNN="apn1", DEFIWKIND=YES;'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFIWKIND:
          name: 'EPS互操作默认切片指示'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置DNN对应的默认切片。  说明：  * 一个DNN可以绑定多个切片，但是默认切片只能配置一个； * 根据网络规划配置DNN对应的唯一默认切片，例如：MOD NSDNN: NSIDX=0, DNN="apn1", DEFIWKIND=YES;'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFIWKIND:
          name: 'EPS互操作默认切片指示'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          required: false
          description: '（可选）配置当SMF服务发现UDM失败时，是否支持根据SMF上UDM的缓存信息判断进入UDM BYPASS状态，以及不存在缓存UDM时，是否支持根据NRF返回的NoProfileMatchReason判断用户会话进入UDM BYPASS状态。  说明：  * **DWORD1043 BIT5**仅在**DWORD1059 BIT9**值为0时生效。 * 此处取值为举例，请根据实际业务需要配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    str_amfexitudmbypass_list:
      type: items
      properties:
        QUITTYPE:
          name: '退出方式'
          type: string
          enum:
          - GRACEFUL_DEREG
          - SUPPLEMENT_UDM_INTERACT
          - FORCED_DEREG
          required: true
          description: '配置用户退出UDM Bypass的方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCANRATE:
          name: '扫描速率(个/秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: true
          description: '配置每个DS每秒扫描多少个用户，扫描到处于UDM Bypass的用户后，AMF根据“QUITTYPE”参数设置使用户退出UDM Bypass状态。  说明：  扫描速率 = 整系统5G用户数 ÷ 预期整系统扫描时间(秒) ÷ DS个数  DS个数来源于如下命令输出结果中记录个数：  DSP FRAMEDBG: DBGSTR="UeamCtrlSvc coordinator all";  如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BAMFSW:
          name: '备份用户退出UDM Bypass开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    str_smfexitudmbypass_list:
      type: items
      properties:
        QUITTYPE:
          name: '退出方式'
          type: string
          enum:
          - GRACEFUL_DEACTIVE
          - SUPPLEMENT_UDM_INTERACT
          - FORCED_DEACTIVE
          required: true
          description: '配置会话退出UDM Bypass的方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCANRATE:
          name: '扫描速率(个/秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: true
          description: '每个DS每秒扫描多少个会话，扫描到处于UDM Bypass的会话后，SMF根据QUITTYPE参数设置使会话退出UDM Bypass状态。  说明：  扫描速率 = 整系统5G会话数量 ÷ 预期整系统扫描时间(秒) ÷ DS个数。  “整系统5G会话数量”可以通过DSP SMSESSIONNUM命令查询；  “DS个数”可以通过DSP FRAMEDBG: DBGSTR="SmcCtrlSvc coordinator all";命令查询。  如果结果没有分批显示，则记录个数为回显中“结果个数”字段的值减1；如果结果分批显示，则记录个数为最终的结果个数减1。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2UDMBPMM01'
      SWITCH: ENABLE
    set_amfudmbypass_list:
    - SWITCH: ON
      RECOVERYACT: DEREG
      FAULTDETECTRATE: 3
      SCANINTERVAL: 600
      RPTFAILCHR: ON
      DEPLOYMENTMODE: CO_DEPLOYMENT
      AUTOEXITSW: ON
    add_udmbypasssub_list:
    - SUBRANGE: ALL_USER
      SNSSAIINFOSSW: ON
      SNSSAIINFOS: '1-D143A5:test'
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 14
      VALUE: VALUE_1
      POSITION: 20
    add_bypassfaultcode_list:
    - PEERNFTYPE: UDM
      NFINSTANCEID: '*'
      CUSFAULTCODE: '*'
    add_bypassfaultcode_list_2:
    - PEERNFTYPE: UDM
      NFINSTANCEID: '*'
      CUSFAULTCODE: '403'
    add_bypassfaultcode_list_4:
    - PEERNFTYPE: UDM
      NFINSTANCEID: 'UDM_01'
      CUSFAULTCODE: '*'
    add_bypassfaultcode_list_6:
    - PEERNFTYPE: UDM
      NFINSTANCEID: 'UDM_01'
      CUSFAULTCODE: '504'
      ERRINFO: 'NF_FAILOVER'
    set_amfpeerselfunc_list:
    - AUSFRESELEN: ON
    set_amfsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: 68
      VALUE: VALUE_0
      POSITION: 9
    set_amfsoftparaofbit_list_2:
    - DT: Dw
      DWORDNUM: 68
      VALUE: VALUE_0
      POSITION: 3
    set_amfsoftparaofbit_list_3:
    - DT: Dw
      DWORDNUM: 68
      VALUE: VALUE_0
      POSITION: 5
    add_n26mmechar_list:
    - RANGE: ALL_MME
      MSISDNSW: YES
      PVTMSISDNSW: YES
    mod_n26mmechar_list:
    - RANGE: ALL_MME
      MSISDNSW: YES
      PVTMSISDNSW: YES
    set_amfsoftparaofbit_list_4:
    - DT: Dw
      DWORDNUM: 80
      VALUE: VALUE_1
      POSITION: 20
    set_licenseswitch_list_1:
    - LICITEM: 'LKV2UDMBPSM01'
      SWITCH: ENABLE
    add_5gcsubqos_list:
    - SUBQOSINDEX: 1
      FIVEQI: 5
      AMBRDL: 1000000
      AMBRUL: 1000000
      ARPPL: 1
    add_apnqosbypass_list:
    - APN: 'apn1'
      SUBQOSINDEX: 1
    set_commqosbypass_list:
    - DEFSW: ENABLE
      SUBQOSINDEX: 1
    set_smfudmbypass_list:
    - UDMBYPASS: ON
      FAULTDETECTRATE: 3
      SCANINTERVAL: 600
      RPTFAILCHR: ON
      AUTOEXITSW: ON
    set_edgesmcommfunc_list:
    - UDMSTATICIPSW: ENABLE
      UDMIPTYPE: SINGLE_STACK
    add_rdsstaticippara_list:
    - IMSI: '123000123456789'
      APN: 'apn1'
      ADDRTYPE: IPV4
      IPV4ADDRESS: '192.168.1.10'
    add_rdsstaticippara_list_1:
    - IMSI: '123001123456789'
      APN: 'apn1'
      ADDRTYPE: Ethernet
      GROUPID: 'A0000001-123-003-01'
    add_edgenglangroup_list:
    - DNN: 'apn1'
      SST: 1
      SD: '010101'
      PDUSESSIONTYPE: Ethernet
      GROUPID: 'A0000001-123-003-02'
    add_bypassfaultcode_list_8:
    - PEERNFTYPE: UDM
      NFINSTANCEID: '*'
      CUSFAULTCODE: '*'
    add_bypassfaultcode_list_9:
    - PEERNFTYPE: UDM
      NFINSTANCEID: '*'
      CUSFAULTCODE: '403'
    add_bypassfaultcode_list_10:
    - PEERNFTYPE: UDM
      NFINSTANCEID: 'UDM_01'
      CUSFAULTCODE: '*'
    add_bypassfaultcode_list_11:
    - PEERNFTYPE: UDM
      NFINSTANCEID: 'UDM_01'
      CUSFAULTCODE: '504'
      ERRINFO: 'NF_FAILOVER'
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'apn1'
      DEFIWKIND: YES
    mod_nsdnn_list:
    - NSIDX: 0
      DNN: 'apn1'
      DEFIWKIND: YES
    set_softparaofbit_list:
    - DT: Dw
      DWORDNUM: '1059'
      VALUE: VALUE_0
      POSITION: '9'
    str_amfexitudmbypass_list:
    - QUITTYPE: GRACEFUL_DEREG
      SCANRATE: 3
      BAMFSW: OFF
    str_smfexitudmbypass_list:
    - QUITTYPE: GRACEFUL_DEACTIVE
      SCANRATE: 3
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 AMF侧配置

#### 1.1 打开本特性的License配置开关。

#### **SET LICENSESWITCH**

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.2 开启AMF的UDM全故障Bypass功能。

#### **SET AMFUDMBYPASS**

```jinja2
{%- for item in set_amfudmbypass_list -%}
    SET AMFUDMBYPASS:
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    {%- if item.RECOVERYACT is not none -%}
        RECOVERYACT={{item.RECOVERYACT}},
    {%- endif -%}
    {%- if item.FAULTDETECTRATE is not none -%}
        FAULTDETECTRATE={{item.FAULTDETECTRATE}},
    {%- endif -%}
    {%- if item.SCANINTERVAL is not none -%}
        SCANINTERVAL={{item.SCANINTERVAL}},
    {%- endif -%}
    {%- if item.RPTFAILCHR is not none -%}
        RPTFAILCHR={{item.RPTFAILCHR}},
    {%- endif -%}
    {%- if item.DEPLOYMENTMODE is not none -%}
        DEPLOYMENTMODE={{item.DEPLOYMENTMODE}},
    {%- endif -%}
    {%- if item.AUTOEXITSW is not none -%}
        AUTOEXITSW={{item.AUTOEXITSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 增加UDM Bypass后的最小签约数据配置。

#### **ADD UDMBYPASSSUB**

```jinja2
{%- for item in add_udmbypasssub_list -%}
    ADD UDMBYPASSSUB:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SNSSAIINFOSSW is not none -%}
        SNSSAIINFOSSW={{item.SNSSAIINFOSSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SNSSAIINFOSSW=ON 时必选 --- -#}
    {%- if item.SNSSAIINFOSSW == 'ON' -%}
        SNSSAIINFOS="{{item.SNSSAIINFOS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 （可选）设置AMF在匹配用户当前安全上下文时，忽略TSC标识，解决由于手机TSC携带错误导致用户安全检查失败而无法接入的问题。

#### **SET AMFSOFTPARAOFBIT**

```jinja2
{%- if is_optional_ignore_tsc -%}
    {%- for item in set_amfsoftparaofbit_list -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 （可选）配置故障设备的网元实例标识和故障码。

#### **ADD BYPASSFAULTCODE**

#### AMF收到UDM/AUSF返回的5xx故障码允许用户进入UDM Bypass状态，如果需要增加其他故障码作为进入UDM Bypass状态的原因值，或者应急场景下配置指定的故障码进入UDM Bypass状态，可以通过**ADD BYPASSFAULTCODE**命令配置。

#### **ADD BYPASSFAULTCODE**命令仅在已明确存在AUSF或UDM全故障的场景下应急使用，默认不配置。配置前需要先收集故障码信息，根据实际情况可进行如下四种配置：

##### 1.5.1 基于全局设备的所有故障码：“网元实例标识”和“自定义故障码”配置为“\*”,不配置“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_global_all_faultcode -%}
    {%- for item in add_bypassfaultcode_list -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.2 基于全局设备的指定故障码：“网元实例标识”配置为“\*”，“自定义故障码”配置为具体的故障码，不配置“错误信息”或者配置具体的“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_global_specific_faultcode -%}
    {%- for item in add_bypassfaultcode_list_2 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.3 基于具体UDM/AUSF网元实例所有故障码：“网元实例标识”配置为具体的某些网元实例，“自定义故障码”配置为“\*”,不配置“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_instance_all_faultcode -%}
    {%- for item in add_bypassfaultcode_list_4 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.5.4 基于具体UDM/AUSF网元实例、具体的故障码和错误信息组合：“网元实例标识”配置为具体的某些网元实例，“自定义故障码”配置为具体的故障码，不配置“错误信息”或者配置具体的“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_instance_specific_faultcode -%}
    {%- for item in add_bypassfaultcode_list_6 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ERRINFO is not none -%}
            ERRINFO="{{item.ERRINFO}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.6 配置对端AUSF返回5xx错误码时，AMF在对ProblemDetails校验失败后是否重选AUSF以及重选后的AUSF响应消息携带ProblemDetails再次校验失败是否进入UDM Bypass状态。

#### **SET AMFPEERSELFUNC**

```jinja2
{%- for item in set_amfpeerselfunc_list -%}
    SET AMFPEERSELFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.AUSFRESELEN is not none -%}
        AUSFRESELEN={{item.AUSFRESELEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 **可选：**如果是Model D组网，将软参DWORD68 BIT9设置为0，配置AMF在Model D模式下向AUSF及UDM发送的首消息头域中不携带3gpp-Sbi-Target-apiRoot。

#### **SET AMFSOFTPARAOFBIT**

```jinja2
{%- if is_optional_model_d_no_apiroot -%}
    {%- for item in set_amfsoftparaofbit_list_1 -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.8 **可选：**通过软参DWORD68 BIT3配置AMF服务发现AUSF或UDM失败且本地没有AUSF或UDM的缓存信息时，是否支持根据NRF返回的NoProfileMatchReason判断用户进入UDM BYPASS状态。

#### **SET AMFSOFTPARAOFBIT**

```jinja2
{%- if is_optional_noprofilematch_amf_bypass -%}
    {%- for item in set_amfsoftparaofbit_list_2 -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.9 **可选：**通过软参DWORD68 BIT5配置AMF与AUSF或UDM交互时是否使用对端原始响应信息。

#### **SET AMFSOFTPARAOFBIT**

```jinja2
{%- if is_optional_peer_raw_response -%}
    {%- for item in set_amfsoftparaofbit_list_3 -%}
        SET AMFSOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.10 配置是否支持通过N26接口向MME传递MSISDN。涉及消息有：Identification Response、Context Response、Forward Relocation Request。

#### **ADD N26MMECHAR**

#### **MOD N26MMECHAR**

```jinja2
{%- for item in add_n26mmechar_list -%}
    ADD N26MMECHAR:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PVTMSISDNSW is not none -%}
        PVTMSISDNSW={{item.PVTMSISDNSW}},
    {%- endif -%}
    {%- if item.MSISDNSW is not none -%}
        MSISDNSW={{item.MSISDNSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_n26mmechar_list -%}
    MOD N26MMECHAR:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSISDNSW is not none -%}
        MSISDNSW={{item.MSISDNSW}},
    {%- endif -%}
    {%- if item.PVTMSISDNSW is not none -%}
        PVTMSISDNSW={{item.PVTMSISDNSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.11 若N26接口支持携带MSISDN信元（参考配置**ADD MMECHARACT**/**MOD MMECHARACT**/**ADD N26MMECHAR**/**MOD N26MMECHAR**），建议将软参DWORD80 BIT20配置为1。

#### **SET AMFSOFTPARAOFBIT**

```jinja2
{%- for item in set_amfsoftparaofbit_list_4 -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 SMF侧配置

#### 2.1 打开本特性的License配置开关。

#### **SET LICENSESWITCH**

```jinja2
{%- for item in set_licenseswitch_list_1 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.2 增加UDM Bypass后的用户签约QoS属性。

#### **ADD 5GCSUBQOS**

```jinja2
{%- for item in add_5gcsubqos_list -%}
    ADD 5GCSUBQOS:
    {#- --- 必选参数 --- -#}
    SUBQOSINDEX={{item.SUBQOSINDEX}},
    FIVEQI={{item.FIVEQI}},
    AMBRDL={{item.AMBRDL}},
    AMBRUL={{item.AMBRUL}},
    ARPPL={{item.ARPPL}},
    ;
{%- endfor -%}
```

#### 2.3 设置UDM Bypass后指定APN的QoS属性。

#### **ADD APNQOSBYPASS**

```jinja2
{%- for item in add_apnqosbypass_list -%}
    ADD APNQOSBYPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SUBQOSINDEX={{item.SUBQOSINDEX}},
    ;
{%- endfor -%}
```

#### 2.4 **可选：**配置UDM Bypass后通用的QoS属性。

#### **SET COMMQOSBYPASS**

```jinja2
{%- if is_optional_common_qos -%}
    {%- for item in set_commqosbypass_list -%}
        SET COMMQOSBYPASS:
        {#- --- 必选参数 --- -#}
        DEFSW={{item.DEFSW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DEFSW=ENABLE 时必选 --- -#}
        {%- if item.DEFSW == 'ENABLE' -%}
            SUBQOSINDEX={{item.SUBQOSINDEX}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 开启SMF的UDM全故障Bypass功能。

#### **SET SMFUDMBYPASS**

```jinja2
{%- for item in set_smfudmbypass_list -%}
    SET SMFUDMBYPASS:
    {#- --- 可选参数 --- -#}
    {%- if item.UDMBYPASS is not none -%}
        UDMBYPASS={{item.UDMBYPASS}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UDMBYPASS=ON 时可选 --- -#}
    {%- if item.UDMBYPASS == 'ON' -%}
        {%- if item.FAULTDETECTRATE is not none -%}
            FAULTDETECTRATE={{item.FAULTDETECTRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UDMBYPASS=ON 时可选 --- -#}
    {%- if item.UDMBYPASS == 'ON' -%}
        {%- if item.SCANINTERVAL is not none -%}
            SCANINTERVAL={{item.SCANINTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UDMBYPASS=ON 时可选 --- -#}
    {%- if item.UDMBYPASS == 'ON' -%}
        {%- if item.RPTFAILCHR is not none -%}
            RPTFAILCHR={{item.RPTFAILCHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：UDMBYPASS=ON 时可选 --- -#}
    {%- if item.UDMBYPASS == 'ON' -%}
        {%- if item.AUTOEXITSW is not none -%}
            AUTOEXITSW={{item.AUTOEXITSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 开启UDM静态IP功能。

#### **SET EDGESMCOMMFUNC**

```jinja2
{%- for item in set_edgesmcommfunc_list -%}
    SET EDGESMCOMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.UDMSTATICIPSW is not none -%}
        UDMSTATICIPSW={{item.UDMSTATICIPSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UDMSTATICIPSW=ENABLE 时可选 --- -#}
    {%- if item.UDMSTATICIPSW == 'ENABLE' -%}
        {%- if item.UDMIPTYPE is not none -%}
            UDMIPTYPE={{item.UDMIPTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 为静态IP用户配置UDM静态IP信息。

#### **ADD RDSSTATICIPPARA**

```jinja2
{%- for item in add_rdsstaticippara_list -%}
    ADD RDSSTATICIPPARA:
    {#- --- 必选参数 --- -#}
    IMSI="{{item.IMSI}}",
    APN="{{item.APN}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPV4/IPV4V6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPV4', 'IPV4V6'] -%}
        {%- if item.IPV4ADDRESS is not none -%}
            IPV4ADDRESS="{{item.IPV4ADDRESS}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.8 （可选）基于IMSI为5G LAN用户配置5G LAN组。

#### **ADD RDSSTATICIPPARA**

```jinja2
{%- if is_optional_lan_group_by_imsi -%}
    {%- for item in add_rdsstaticippara_list_1 -%}
        ADD RDSSTATICIPPARA:
        {#- --- 必选参数 --- -#}
        IMSI="{{item.IMSI}}",
        APN="{{item.APN}}",
        ADDRTYPE={{item.ADDRTYPE}},
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 5G LAN组ID: 条件必选(地址类型=Ethernet) / 条件可选(地址类型=IPV4|IPV6|IPV4V6) --- -#}
        {%- if (item.ADDRTYPE == 'Ethernet') -%}
            GROUPID="{{item.GROUPID}}",
        {%- elif (item.ADDRTYPE in ['IPV4', 'IPV6', 'IPV4V6']) -%}
            {%- if item.GROUPID is not none -%}
                GROUPID="{{item.GROUPID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 （可选）基于DNN为5G LAN用户配置5G LAN组。

#### **ADD EDGENGLANGROUP**

```jinja2
{%- if is_optional_lan_group_by_dnn -%}
    {%- for item in add_edgenglangroup_list -%}
        ADD EDGENGLANGROUP:
        {#- --- 必选参数 --- -#}
        DNN="{{item.DNN}}",
        SST={{item.SST}},
        SD="{{item.SD}}",
        PDUSESSIONTYPE={{item.PDUSESSIONTYPE}},
        GROUPID="{{item.GROUPID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.10 （可选）配置故障设备的网元实例标识和故障码。

#### **ADD BYPASSFAULTCODE**

#### SMF收到UDM返回的5xx故障码允许会话进入UDM Bypass状态，如果需要增加其他故障码作为进入UDM Bypass状态的原因值，或者应急场景下配置指定的故障码进入UDM Bypass状态，可以通过**ADD BYPASSFAULTCODE**命令配置。

#### **ADD BYPASSFAULTCODE**命令仅在已明确存在UDM全故障的场景下应急使用，默认不配置。配置前需要先收集故障码信息，根据实际情况可进行如下四种配置：

##### 2.10.1 基于全局设备的所有故障码：“网元实例标识”和“自定义故障码”配置为“\*”,不配置“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_global_all_faultcode -%}
    {%- for item in add_bypassfaultcode_list_8 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.2 基于全局设备的指定故障码：“网元实例标识”配置为“\*”，“自定义故障码”配置为具体的故障码，不配置“错误信息”或者配置具体的“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_global_specific_faultcode -%}
    {%- for item in add_bypassfaultcode_list_9 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.3 基于具体UDM网元实例所有故障码：“网元实例标识”配置为具体的某些网元实例，“自定义故障码”配置为“\*”,不配置“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_instance_all_faultcode -%}
    {%- for item in add_bypassfaultcode_list_10 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.10.4 基于具体UDM网元实例、具体的故障码和错误信息组合：“网元实例标识”配置为具体的某些网元实例，“自定义故障码”配置为具体的故障码，不配置“错误信息”或者配置具体的“错误信息”。

```jinja2
{%- if is_optional_config_fault_udm and is_scenario_instance_specific_faultcode -%}
    {%- for item in add_bypassfaultcode_list_11 -%}
        ADD BYPASSFAULTCODE:
        {#- --- 必选参数 --- -#}
        PEERNFTYPE={{item.PEERNFTYPE}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        CUSFAULTCODE="{{item.CUSFAULTCODE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ERRINFO is not none -%}
            ERRINFO="{{item.ERRINFO}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.11 配置DNN对应的默认切片。

#### **ADD NSDNN**

#### **MOD NSDNN**

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    DNN="{{item.DNN}}",
    NSIDX={{item.NSIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DEFIWKIND is not none -%}
        DEFIWKIND={{item.DEFIWKIND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_nsdnn_list -%}
    MOD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DEFIWKIND is not none -%}
        DEFIWKIND={{item.DEFIWKIND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.12 **可选：**配置当SMF服务发现UDM失败时，是否支持根据SMF上UDM的缓存信息判断进入UDM BYPASS状态，以及不存在缓存UDM时，是否支持根据NRF返回的NoProfileMatchReason判断用户会话进入UDM BYPASS状态。

#### **SET SOFTPARAOFBIT**

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_softparaofbit_list的变量区（command: SET SOFTPARAOFBIT） -#}
<!-- MISSING_MACRO: command=SET SOFTPARAOFBIT list_name=set_softparaofbit_list step_id=2.12 -->
```

### 3 手动触发AMF上用户退出UDM Bypass状态。

```jinja2
{%- for item in str_amfexitudmbypass_list -%}
    STR AMFEXITUDMBYPASS:
    {#- --- 必选参数 --- -#}
    QUITTYPE={{item.QUITTYPE}},
    SCANRATE={{item.SCANRATE}},
    {#- --- 可选参数 --- -#}
    {%- if item.BAMFSW is not none -%}
        BAMFSW={{item.BAMFSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 手动触发SMF上会话退出UDM Bypass状态。

```jinja2
{%- for item in str_smfexitudmbypass_list -%}
    STR SMFEXITUDMBYPASS:
    {#- --- 必选参数 --- -#}
    QUITTYPE={{item.QUITTYPE}},
    SCANRATE={{item.SCANRATE}},
    ;
{%- endfor -%}
```

