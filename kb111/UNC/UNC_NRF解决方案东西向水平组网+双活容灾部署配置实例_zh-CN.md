---
id: ''
name: NRF解决方案东西向水平组网+双活容灾部署配置实例
ne_type: UNC
type: feature
description: '* NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。 * 双活NRF上的号段信息配置已完成，且配置一致。 * 对于大型运营商网络，为了便于分区域管理，可以建立不同NRF之间的东西向互联，达到全局管理的目标。    如图1所示。    **图1** 东西向+容灾组网举例      在双活容灾部署配置实例中，L-NRF1-A和L-NRF1-S中的A和S不指代Active和Standby,仅做名称上的区分。L-NRF2-A和L-NRF2-S同理。'
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core NRF解决方案","NRF功能部署","5G独立部署","NRF多层容灾组网","NRF解决方案东西向水平组网+双活容灾部署配置实例"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。* 双活NRF上的号段信息配置已完成，且配置一致。* 对于大型运营商网络，为了便于分区域管理，可以建立不同NRF之间的东西向互联，达到全局管理的目标。  如图1所示。  **图1** 东西向+容灾组网举例    在双活容灾部署配置实例中，L-NRF1-A和L-NRF1-S中的A和S不指代Active和Standby,仅做名称上的区分。L-NRF2-A和L-NRF2-S同理。

## 必备事项
前提条件

前提条件

* 各组NRF双活容灾组网的相关配置已完成，详细参考NRF解决方案基本功能配置实例（NRF双活容灾+ NF注册/更新/去注册、NF订阅/通知+NF发现）。
* 各个NRF的基础配置和NF基本功能、NF发现配置已完成，详细参考NRF解决方案基本功能配置实例的NRF侧配置。
* 主备NRF上的号段信息配置已完成，且号段信息配置一致。
* 安全相关配置已完成，访问授权和Token认证只需要在L-NRF层配置（Token分配只可能发生在目标NF注册的NRF上），TLS认证需要在所有NRF上配置，详细参考NRF解决方案安全配置实例（NRF容灾+NF访问授权&NF认证）。
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
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
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
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
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
          name: 'HTTPLE本端实体索引'
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
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
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
    add_nrfgroup_list:
      type: items
      properties:
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPATTR:
          name: '实例组属性'
          type: string
          enum:
          - SNRF
          - HNRF
          - LNRF
          - SNRF_PLMN
          - SELFNRF
          - INRF_PLMN
          required: true
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
          description: '* L-NRF1-A：NRF\_Instancename\_l1\_a * L-NRF1-S：NRF\_Instancenml1\_s * L-NRF2-A：NRF\_Instance\_l2\_a * L-NRF2-S：NRF\_l2\_s'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_nrfaddr_list:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1\_a：172.16.0.7 * NRF\_Instancenml1\_s：172.17.0.7  * NRF\_Instance\_l2\_a：10.10.0.7 * NRF\_l2\_s：10.20.0.7'
          data_source: '全网规划'
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
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
    add_nrfbindgrp_list:
      type: items
      properties:
        NRFINSTNAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPNAME:
          name: '实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISREGED:
          name: '对端NRF是否注册'
          type: string
          enum:
          - FALSE
          - TRUE
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
          default: 100
        NRFINSTID:
          name: 'NRF实例标识'
          type: string
          minLength: 1
          maxLength: 40
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nrfimsirt_list:
      type: items
      properties:
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - AUSF
          - PCF
          - UDM
          - UDR
          - CHF
          - CUSTOM_OCS
          - SMSF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符'
          type: string
          minLength: 5
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NEXTNRFGRPNAME:
          name: '归属NRF实例组名称'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrffuncsw_list:
      type: items
      properties:
        SNRFGRPERRSW:
          name: '东西向NRF实例组分层路由配置错误告警上报开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: false
          description: '该参数为可选配置项。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_nrf_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '* L-NRF1-A：NRF\_Instancename\_l1\_a * L-NRF1-S：NRF\_Instancenml1\_s * L-NRF2-A：NRF\_Instance\_l2\_a * L-NRF2-S：NRF\_l2\_s'
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
          description: '-'
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
          data_source: ''
          pattern: ''
          default: 0
    add_nrfaddr_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '每个NRF和IP的对应关系如下：   * NRF\_Instancename\_l1\_a：172.16.0.7 * NRF\_Instancenml1\_s：172.17.0.7  * NRF\_Instance\_l2\_a：10.10.0.7 * NRF\_l2\_s：10.20.0.7'
          data_source: '全网规划'
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
    add_nrfpara_list_8:
      type: items
      properties:
        NRFINSTANCENAME:
          name: 'NRF实例名称'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: '已通过**ADD NRF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WAITINTERVAL:
          name: '等待时长'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: '当需要改变默认等待时长或最大重传次数时，需要配置此命令。'
          data_source: '与对端协商'
          pattern: ''
          default: 5
        MAXRETRYTIMES:
          name: '最大重传次数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
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
    set_licenseswitch_list_12:
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
  examples:
    add_ngmno_list:
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    - NOID: 0
      FULLNAME: 'Operator A'
      SHORTNAME: 'OA'
    add_nghplmn_list:
    - NOID: 0
      MCC: '123'
      MNC: '03'
    - NOID: 0
      MCC: '123'
      MNC: '03'
    - NOID: 0
      MCC: '123'
      MNC: '03'
    - NOID: 0
      MCC: '123'
      MNC: '03'
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NFBNR01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRLNF01'
      SWITCH: ENABLE
    add_nfuuid_list:
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instancename_l1_a'
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instancenml1_s'
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_Instance_l2_a'
    - NFTYPE: NfNRF
      NFINSTANCENAME: 'NRF_l2_s'
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    - IPVERSION: IPv4
      LOGICIPV4: '172.17.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: ''
      IPV6MTU: ''
      LOGICIPV6: ''
    - IPVERSION: IPv4
      LOGICIPV4: '10.10.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: ''
      IPV6MTU: ''
      LOGICIPV6: ''
    - IPVERSION: IPv4
      LOGICIPV4: '10.20.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR SBI Server'
      IPV4MTU: ''
      IPV6MTU: ''
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NRF'
    - INDEX: 3
      DESC: 'NRF'
    - INDEX: 3
      DESC: 'NRF'
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.17.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.10.0.7'
      PORT: 31000
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '10.20.0.7'
      PORT: 31000
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
      IPV4: '172.16.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: YES
      TLSIDX: ''
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '172.17.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: ''
      TLSIDX: ''
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '10.10.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: ''
      TLSIDX: ''
    - INDEX: 6
      HTTPLEGRPIDX: 3
      LETYPE: CLIENT
      IPTYPE: IPv4
      IPV4: '10.20.0.7'
      VPNNAME: 'VRF_SBI'
      DESC: 'NRF Client'
      IPV6: ''
      PORT: ''
      TLSFLG: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    add_nrfgroup_list:
    - GROUPNAME: 'LGP2'
      GROUPATTR: SNRF
    - GROUPNAME: 'LGP2'
      GROUPATTR: SNRF
    - GROUPNAME: 'LGP1'
      GROUPATTR: SNRF
    - GROUPNAME: 'LGP1'
      GROUPATTR: SNRF
    add_nrf_list:
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_l2_s'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_l2_s'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      TLS: FALSE
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      TLS: FALSE
    add_nrfaddr_list:
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l2_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l2_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list:
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_l2_s'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_l2_s'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      WAITINTERVAL: 60
      MAXRETRYTIMES: 6
    add_nrfbindgrp_list:
    - NRFINSTNAME: 'NRF_Instance_l2_a'
      GROUPNAME: 'LGP2'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    - NRFINSTNAME: 'NRF_Instance_l2_a'
      GROUPNAME: 'LGP2'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    - NRFINSTNAME: 'NRF_Instancename_l1_a'
      GROUPNAME: 'LGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    - NRFINSTNAME: 'NRF_Instancename_l1_a'
      GROUPNAME: 'LGP1'
      ISREGED: FALSE
      PRIORITY: 1
      NRFINSTID: ''
    add_nrfimsirt_list:
    - NFTYPE: UDM
      SEGSTART: '123450000100000'
      SEGEND: '123450000199999'
      NEXTNRFGRPNAME: 'LGP2'
    - NFTYPE: UDM
      SEGSTART: '123450000100000'
      SEGEND: '123450000199999'
      NEXTNRFGRPNAME: 'LGP2'
    - NFTYPE: UDM
      SEGSTART: '123450000300000'
      SEGEND: '123450000499999'
      NEXTNRFGRPNAME: 'LGP1'
    - NFTYPE: UDM
      SEGSTART: '123450000300000'
      SEGEND: '123450000499999'
      NEXTNRFGRPNAME: 'LGP1'
    set_nrffuncsw_list:
    - SNRFGRPERRSW: FUNC_ON
    - SNRFGRPERRSW: FUNC_ON
    - SNRFGRPERRSW: FUNC_ON
    - SNRFGRPERRSW: FUNC_ON
    add_nrf_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      TLS: FALSE
      PRIORITY: 0
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      TLS: FALSE
      PRIORITY: 1
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      TLS: FALSE
      PRIORITY: 0
    - NRFINSTANCENAME: 'NRF_l2_s'
      TLS: FALSE
      PRIORITY: 1
    add_nrfaddr_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.16.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '172.17.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.10.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    - NRFINSTANCENAME: 'NRF_l2_s'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS: '10.20.0.7'
      PORT: 31000
      IPV6ADDRESS: ''
    add_nrfpara_list_8:
    - NRFINSTANCENAME: 'NRF_Instancename_l1_a'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_Instancenml1_s'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_Instance_l2_a'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    - NRFINSTANCENAME: 'NRF_l2_s'
      WAITINTERVAL: 5
      MAXRETRYTIMES: 3
      LOADCARRYINHB: FALSE
      SUBSCRISWITCH: OFF
      OAUTH2SWITCH: OFF
    set_licenseswitch_list_12:
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NFBAM01'
      SWITCH: ENABLE
    act_nfonline_list:
    - NFINSTANCENAME: 'AMF_Instance_1'
    - NFINSTANCENAME: 'AMF_Instance_2'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 NRF分层组网配置

### NRF单层+东西向组网的L-NRF1和L-NRF2的网络位置及规划如图2所示。

### **图2** NRF的网络位置和东西向NRF组

### 其中，**UDM的号段路由如下：**

### L-NRF1和L-NRF2上分别支持的UDM路由信息：

### 支持的起止号段为"123450000100000"~"123450000299999"的UDM实例组归属LGP2，

### 支持的起止号段为"123450000300000"~"123450000499999"的UDM实例组归属LGP1。

### 所以，例如L-NRF1处管辖的AMF携带号段123450000288888发起UDM请求发现时，路由顺序为：L-NRF1（L-NRF1本身和配置路由都查不到，向L-NRF2查询）→L-NRF2（L-NRF2上查询到符合条件的UDM）。

### 2 NRF侧配置

#### 2.1 /*- - - - - - - - - - - - - - - - L-NRF1-A上的配置- - - - - - - - - - - - - - - - - - - - */

#### //一、配置NRF的基本功能数据，完成NRF作为一个基本的NF的配置。

#### //NRF侧路由配置已完成。

#### //配置NRF基础数据。

#### //配置运营商信息、运营商签约用户的Home PLMN。

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

#### //打开NRF基本功能、NF发现的License。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### //配置NRF实例信息，此步骤配置后系统会为NRF自动分配InstanceID信息。

```jinja2
{%- for item in add_nfuuid_list -%}
    ADD NFUUID:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### //配置NRF服务化接口数据，用于跟其他NF对接交互。

#### //增加NRF服务化接口的IP地址。

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

#### //配置Nnrf接口的HTTP信息。

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

#### //增加NRF作为服务器端的HTTP本端实体。

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

#### //增加NRF作为客户器端的HTTP本端实体。

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

#### //二、配置NRF东西向组网。

#### //在NRF上配置打开NRF分层组网的License配置开关。

#### //在L-NRF1-A上配置对应的东西向L-NRF2组信息。

```jinja2
{%- for item in add_nrfgroup_list -%}
    ADD NRFGROUP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    GROUPATTR={{item.GROUPATTR}},
    ;
{%- endfor -%}
```

#### //配置L-NRF1-A互联的主备L-NRF相关信息，为相邻且相连的NRF之间建立联系。（通过LST NFUUID查询出来INSTANCENAME）

```jinja2
{%- for item in add_nrf_list -%}
    ADD NRF:
    {#- --- 必选参数 --- -#}
    NRFINSTANCENAME="{{item.NRFINSTANCENAME}}",
    TLS={{item.TLS}},
    ;
{%- endfor -%}
```

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

```jinja2
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
    ;
{%- endfor -%}
```

#### //新增东西向LGP2组的成员L-NRF2-A和L-NRF2-S。

```jinja2
{%- for item in add_nrfbindgrp_list -%}
    ADD NRFBINDGRP:
    {#- --- 必选参数 --- -#}
    NRFINSTNAME="{{item.NRFINSTNAME}}",
    GROUPNAME="{{item.GROUPNAME}}",
    ISREGED={{item.ISREGED}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- NRF实例标识: 条件必选(对端NRF是否注册=TRUE) / 条件可选(对端NRF是否注册=FALSE) --- -#}
    {%- if (item.ISREGED == 'TRUE') -%}
        NRFINSTID="{{item.NRFINSTID}}",
    {%- elif (item.ISREGED == 'FALSE') -%}
        {%- if item.NRFINSTID is not none -%}
            NRFINSTID="{{item.NRFINSTID}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### //三、配置NRF路由，用于跨NRF查询。

```jinja2
{%- for item in add_nrfimsirt_list -%}
    ADD NRFIMSIRT:
    {#- --- 必选参数 --- -#}
    NFTYPE={{item.NFTYPE}},
    SEGSTART="{{item.SEGSTART}}",
    SEGEND="{{item.SEGEND}}",
    NEXTNRFGRPNAME="{{item.NEXTNRFGRPNAME}}",
    ;
{%- endfor -%}
```

#### //四、支持寻址NRF路由冲突上报告警。

#### //L-NRF东西向寻址时，若SET NRFFUNCSW命令的告警上报开关“SNRFGRPERRSW”打开，支持寻址NRF路由冲突（相同路由配置存在于多个NRF实例组）时上报告警。打开“SNRFGRPERRSW”上报开关配置如下：

```jinja2
{%- for item in set_nrffuncsw_list -%}
    SET NRFFUNCSW:
    {#- --- 可选参数 --- -#}
    {%- if item.SNRFGRPERRSW is not none -%}
        SNRFGRPERRSW={{item.SNRFGRPERRSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 /*- - - - - - - - - - - - - - - - L-NRF1-S上的配置- - - - - - - - - - - - - - - - - - - - */

#### 2.3 /*- - - - - - - - - - - - - - - - L-NRF2-A上的配置- - - - - - - - - - - - - - - - - - - - */

#### 2.4 /*- - - - - - - - - - - - - - - - L-NRF2-S上的配置- - - - - - - - - - - - - - - - - - - - */

### 3 NF侧向L-NRF的注册、更新、去注册、订阅、发现配置。

### 4 AMF侧（不同区域的NF向不同NRF注册，因此以上述2组L-NRF（L-NRF1-A/L-NRF1-S、L-NRF2-A/L-NRF2-S）为例，对应给出2个AMF的配置脚本示例）

#### 4.1 /*- - - - - - - - - - - - - - - - -AMF1上的配置- - - - - - - - - - - - - - - - - - - - */

#### //以下1-4参考NRF解决方案基本功能配置实例中的AMF侧配置。

#### //1.AMF侧路由配置已完成。

#### //2.配置运营商基础数据。

#### ……

#### //3.配置AMF实例信息。

#### ……

#### //4.配置AMF服务化接口数据。

#### ……

#### //配置AMF1向L-NRF1-A的对接数据。

#### //配置L-NRF1-A信息。

```jinja2
{%- for item in add_nrf_list_8 -%}
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

#### //配置L-NRF1-A的地址信息。

```jinja2
{%- for item in add_nrfaddr_list_8 -%}
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

#### //配置L-NRF1-A协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

```jinja2
{%- for item in add_nrfpara_list_8 -%}
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

#### //配置AMF1向L-NRF1-S的对接数据。

#### //配置L-NRF1-S的信息。

#### //配置L-NRF1-S的地址信息。

#### //配置L-NRF1-S协议参数。请提前规划ADD NRFPARA中“WAITINTERVAL”和“MAXRETRYTIMES”的值，确保NF的故障探测时长比NRF探测NF的时长要短，避免因链路故障NF还未来得及倒换就被NRF判定为故障。NF探测时长请参考华为解决方案的NRF实现中“可靠性机制”小节。

#### //打开NF注册/更新/去注册、发现与NRF交互的基本功能开关。

```jinja2
{%- for item in set_licenseswitch_list_12 -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### //激活AMF1向NRF注册。

```jinja2
{%- for item in act_nfonline_list -%}
    ACT NFONLINE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    ;
{%- endfor -%}
```

#### 4.2 /*- - - - - - - - - - - - - - - - -AMF2上的配置- - - - - - - - - - - - - - - - - - - - */

#### ……

#### ……

#### ……

