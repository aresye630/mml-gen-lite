---
id: ''
name: 配置不同区域下发不同APN（方案二）
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员在4G网络中配置不同区域下发不同APN，配置独立开户模板。  * 运营商大网SMF POOL业务不均质，从POOL中选择两台SMF作为智能分流SMF时，UDM使用此章节方式进行配置。 * 配置不同区域下发不同DNN/APN时用户免签约功能（执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数）在UDM 20.11.2.15及之后的版本支持，之前的版本无需关注此功能，之后的版本根据局点实际规划进行设置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UDM","配置4G用户签约","配置不同区域下发不同APN（方案二）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在4G网络中配置不同区域下发不同APN，配置独立开户模板。* 运营商大网SMF POOL业务不均质，从POOL中选择两台SMF作为智能分流SMF时，UDM使用此章节方式进行配置。* 配置不同区域下发不同DNN/APN时用户免签约功能（执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数）在UDM 20.11.2.15及之后的版本支持，之前的版本无需关注此功能，之后的版本根据局点实际规划进行设置。

## 必备事项
前提条件

* 已完成园区专网UDM的基础配置并与周边网元完成对接。

* 操作人员具有PGW Web LMT客户端业务发放权限。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_mapconf_list:
      type: items
      properties:
        OPTGPRSRSISUPP:
          name: '是否支持用户签约的业务下发模板中的优化GPRS业务数据和用户签约的优化GPRS业务数据同时下发'
          type: string
          required: false
          description: '用于标识UDM是否支持用户签约的业务下发模板中的优化GPRS业务数据和用户签约的优化GPRS业务数据同时下发。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPP_RSI_GPRS:
          name: 'LTE业务是否在GPRS模式下支持业务下发模板'
          type: string
          required: false
          description: '用于标识当**SET MAPSERV**命令中的“GPRS管理方式”参数取值为“NotSupportGPRSManager”或“SupportGPRSManager”时，UDM是否支持在4G业务处理流程中根据DIAMETER漫游限制模板或PLMN漫游限制模板中关联的业务下发模板进行APN数据的下发。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mapserv_list:
      type: items
      properties:
        GPRSMANAGER:
          name: 'GPRS管理方式'
          type: string
          required: false
          description: '用于标识是否支持给用户签约多个GPRS模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPC_CHK_5GS_IWK:
          name: 'EPC域是否检查5G域DNN的IWK标识'
          type: string
          required: false
          description: '用于标识在4G注册流程中合并5G SMF注册记录中的PGW-C FQDN时，是否判断5G域DNN的iwkEpsInd标识。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_udmserv_list:
      type: items
      properties:
        SUPP_DUAL_DOMAINS_DNN:
          name: '是否支持双域DNN/APN业务'
          type: string
          required: false
          description: '用于标识UDM是否支持双域DNN/APN业务。   * 在4G网络中，当**SET MAPSERV**命令“GPRS管理方式”参数为“SuppPsEpsSeparateTplManager”时，该参数用于控制UDM是否支持双域APN业务。 * 请勿随意修改该参数，修改前请联系华为技术支持。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SXZW_REPLACE_MODE:
          name: 'DNN/APN替换业务是否免用户签约'
          type: string
          required: false
          description: '用于标识在4G/5G APN/DNN替换业务场景下，UDM是否需要使用**MOD SXZW**命令为用户签约，用户才能使用DNN/APN替换业务。  可选配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: '接入点名称'
          type: string
          required: false
          description: '用于标识接入点名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNGWALLOCTYPE:
          name: 'PDN GW地址分配类型'
          type: string
          required: false
          description: '用于标识PDN GW地址分配类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NONIPDATADELMECH:
          name: 'Non-IP传输模式'
          type: string
          required: false
          description: '用于标识Non-IP PDN类型的APN数据传输给MME时的传输模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_epsqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: 'QoS模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: 'QoS模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSCLASUID:
          name: 'QoS分类ID'
          type: string
          required: false
          description: '用于标识QoS分类ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EXTQCI:
          name: '扩展QoS分类ID'
          type: string
          required: false
          description: '用于标识扩展QoS分类ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRILEVEL:
          name: '分配/保留优先级数据'
          type: string
          required: false
          description: '用于标识用户在网络资源拥塞时的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONCAP:
          name: '业务数据流是否能够占有能力'
          type: string
          required: false
          description: '用于标识是否允许该业务数据流占有优先级相对较低的业务数据流的资源。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PREEMPTIONVUL:
          name: '业务数据流是否能够被占有'
          type: string
          required: false
          description: '用于标识是否允许该业务数据流丢失分配给它的资源，用于接纳一个优先级相对较高的业务数据流。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRMAXREQBWUL:
          name: '最大请求上行带宽'
          type: string
          required: false
          description: '用于标识4G网络最大请求上行带宽，即发送消息的最大带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRMAXREQBWDL:
          name: '最大请求下行带宽'
          type: string
          required: false
          description: '用于标识4G网络最大请求下行带宽，即接受消息的最大带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_optgprstpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待修改模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPLNAME:
          name: '模板名'
          type: string
          required: false
          description: '用于标识模板名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: '用于标识APN类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '用于标识APN模板ID。该参数必须先由**ADD APNTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTCFGFLAG:
          name: '是否是默认APN'
          type: string
          required: false
          description: '用于标识是否将“APN模板ID”对应的APN模板设置为EPS APN的默认APN模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '用于标识EPS QoS模板ID。该参数必须先由**ADD EPSQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '用于标识数据业务的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '用于标识是否允许用户从VPLMN访问PDP/PDN网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '用于标识计费特性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IW5GSINDICATOR:
          name: '是否签约5GS互操作'
          type: string
          required: false
          description: '用于标识用户是否签约5GS互操作业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_optgprstpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待修改模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '用于新增、修改和删除用户PDP/PDN上下文。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        APN_TYPE:
          name: 'APN类型'
          type: string
          required: false
          description: '用于标识APN类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        APNTPLID:
          name: 'APN模板ID'
          type: string
          required: false
          description: '用于标识APN模板ID。该参数必须先由**ADD APNTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTCFGFLAG:
          name: '是否是默认APN'
          type: string
          required: false
          description: '用于标识是否将“APN模板ID”对应的APN模板设置为EPS APN的默认APN模板。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPS_QOSTPLID:
          name: 'EPS QoS模板ID'
          type: string
          required: false
          description: '用于标识EPS QoS模板ID。该参数必须先由**ADD EPSQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDPTYPE:
          name: 'PDP/PDN类型'
          type: string
          required: false
          description: '用于标识数据业务的类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPLMN:
          name: '是否允许用户从VPLMN访问PDP/PDN网络'
          type: string
          required: false
          description: '用于标识是否允许用户从VPLMN访问PDP/PDN网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHARGE:
          name: '计费特性'
          type: string
          required: false
          description: '用于标识计费特性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IW5GSINDICATOR:
          name: '是否签约5GS互操作'
          type: string
          required: false
          description: '用于标识用户是否签约5GS互操作业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_tploptgprs_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供优化GPRS业务'
          type: string
          required: false
          description: '用于标识是否提供优化GPRS/EPS业务。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TPLID:
          name: '优化GPRS模板ID'
          type: string
          required: false
          description: '用于标识优化GPRS模板ID。该参数必须先由**ADD OPTGPRSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DELOLD:
          name: '是否删除已有的APN'
          type: string
          required: false
          description: '用于标识是否删除已有的APN。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rsitpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERCODE:
          name: '下发业务列表'
          type: string
          required: false
          description: '用于标识业务下发列表。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OLDAPNLIST:
          name: '旧APN名称列表'
          type: string
          required: false
          description: '用于标识旧APN名称列表。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NEWAPNLIST:
          name: '新APN名称列表'
          type: string
          required: false
          description: '用于标识新APN名称列表。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_plmntpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTRULE:
          name: '缺省漫游限制状态'
          type: string
          required: false
          description: '用于标识缺省状态下的漫游限制状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RSITPLID:
          name: '业务下发模板ID'
          type: string
          required: false
          description: '用于标识PLMN区域漫游模板关联的业务下发模板序号。该参数必须先通过**ADD RSITPL**命令配置才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家码'
          type: string
          required: false
          description: '用于标识移动国家码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网络码'
          type: string
          required: false
          description: '用于标识移动网络码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISLOCAL:
          name: '是否本地PLMN'
          type: string
          required: false
          description: '用于标识应用于多HPLMN功能中的PLMN是否为本地PLMN。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        RULE:
          name: '漫游限制状态'
          type: string
          required: false
          description: '用于标识该模板PLMN区域漫游限制状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CUSTOMRULE:
          name: '定制规则'
          type: string
          required: false
          description: '用于标识NON-3GPP用户在签约了PLMN区域漫游模板的情况下，当MAR消息未携带VNI（Visitor Network Identifier）时控制是否允许用户注册和限制APN数据的下发。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mapserv_list_1:
      type: items
      properties:
        EPCSXZWPLMNRRID:
          name: 'APN替换业务配置的全局PLMN区域漫游模板ID'
          type: string
          required: false
          description: '用于标识如果用户通过**MOD SXZW**命令签约了APN替换业务，UDM会基于该参数配置的PLMN区域漫游模板与“APN替换业务配置的全局Diameter漫游限制模板ID”参数，根据用户接入的位置匹配到具体的APN替换业务码，再根据配置的APN更名逻辑对下发的APN进行替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diamrrtpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: string
          required: false
          description: '用于标识待增加模板在系统中的序号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTRULE:
          name: '缺省漫游限制状态'
          type: string
          required: false
          description: '用于标识在缺省状态下Diameter漫游限制能力。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RSITPLID:
          name: '业务下发模板ID'
          type: string
          required: false
          description: '用于标识Diameter漫游限制模板关联的业务下发模板ID。该参数必须先由**ADD RSITPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DIAMIDENTITYTYPE:
          name: 'Diameter身份标识类型'
          type: string
          required: false
          description: '用于标识Diameter身份标识类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DIAMIDENTITY:
          name: 'Diameter身份标识'
          type: string
          required: false
          description: '用于标识Diameter的名称，该名称唯一确定一个Diameter服务节点。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULE:
          name: '漫游限制状态'
          type: string
          required: false
          description: '用于标识Diameter漫游的限制能力。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_mapserv_list_2:
      type: items
      properties:
        EPCSXZWDIAMRRID:
          name: 'APN替换业务配置的全局Diameter漫游限制模板ID'
          type: string
          required: false
          description: '用于标识如果用户通过**MOD SXZW**命令签约了APN替换业务，UDM会基于该参数配置的Diameter漫游限制模板与“APN替换业务配置的全局PLMN区域漫游模板ID”参数，根据用户接入的位置匹配到具体的APN替换业务码，再根据配置的APN更名逻辑对下发的APN进行替换。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_sxzw_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识用户的IMSI号码。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLSCHE:
          name: '业务码'
          type: string
          required: false
          description: '用于标识DNN/APN替换业务类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_mapconf_list:
    - OPTGPRSRSISUPP: TRUE
      SUPP_RSI_GPRS: FALSE
    set_mapserv_list:
    - GPRSMANAGER: SuppGprsManageOptimizeon
      EPC_CHK_5GS_IWK: NOTCHECK
    set_udmserv_list:
    - SUPP_DUAL_DOMAINS_DNN: TRUE
      SXZW_REPLACE_MODE: FALSE
    add_apntpl_list:
    - HLRSN: '1'
      TPLID: '111'
      TPLNAME: APN
      APN: common.dnn
      PDNGWALLOCTYPE: DYNAMIC
      NONIPDATADELMECH: SGi_BASED_DATA_DELIVERY
    add_epsqostpl_list:
    - HLRSN: '1'
      TPLID: '111'
      TPLNAME: EPSQOS
      QOSCLASUID: '9'
      EXTQCI: '130'
      PRILEVEL: '6'
      PREEMPTIONCAP: DISABLE
      PREEMPTIONVUL: ENABLE
      AMBRMAXREQBWUL: '104857600'
      AMBRMAXREQBWDL: '1073741824'
    add_optgprstpl_list:
    - HLRSN: '1'
      TPLID: '50'
      TPLNAME: OPTGPRSTPL
      APN_TYPE: EPS_APN
      APNTPLID: '111'
      DEFAULTCFGFLAG: TRUE
      EPS_QOSTPLID: '111'
      PDPTYPE: IPV4_OR_IPV6
      VPLMN: TRUE
      CHARGE: NORMAL
      IW5GSINDICATOR: SUBSCRIBED
    mod_optgprstpl_list:
    - HLRSN: '1'
      TPLID: '50'
      PROV: ADDPDPCNTX
      APN_TYPE: EPS_APN
      APNTPLID: '112'
      DEFAULTCFGFLAG: FALSE
      EPS_QOSTPLID: '111'
      PDPTYPE: IPV4_OR_IPV6
      VPLMN: TRUE
      CHARGE: NORMAL
      IW5GSINDICATOR: NOT-SUBSCRIBED
    mod_tploptgprs_list:
    - IMSI: '46100000912345'
      PROV: TRUE
      TPLID: '50'
      DELOLD: FALSE
    add_rsitpl_list:
    - HLRSN: '1'
      TPLID: '100'
      SERCODE: SXZW
      OLDAPNLIST: common.dnn
      NEWAPNLIST: common2.dnn
    add_plmntpl_list:
    - HLRSN: '1'
      TPLID: '100'
      DEFAULTRULE: PERMISSION
      RSITPLID: '100'
      MCC: '460'
      MNC: '00'
      ISLOCAL: TRUE
      RULE: PERMISSION
      CUSTOMRULE: PERMIT
    set_mapserv_list_1:
    - EPCSXZWPLMNRRID: '100'
    add_diamrrtpl_list:
    - HLRSN: '1'
      TPLID: '100'
      DEFAULTRULE: PERMISSION
      RSITPLID: '100'
      DIAMIDENTITYTYPE: HOSTNAME
      DIAMIDENTITY: test.huawei.com
      RULE: PERMISSION
    set_mapserv_list_2:
    - EPCSXZWDIAMRRID: '100'
    mod_sxzw_list:
    - IMSI: '46100000912345'
      CTRLSCHE: 4GSXZW
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM业务管理”窗口。

### 如果现网已配置4G用户数据，则可跳过步骤 5~步骤 8。

### 2 执行**SET MAPCONF**命令设置MAP功能流程数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapconf_list的变量区（command: SET MAPCONF） -#}
<!-- MISSING_MACRO: command=SET MAPCONF list_name=set_mapconf_list step_id=2 -->
```

### 3 执行**SET MAPSERV**命令设置MAP业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list step_id=3 -->
```

### 4 执行**SET UDMSERV**命令设置UDM业务数据。

### 该步骤可选配置“DNN/APN替换业务是否免用户签约”参数。

#### 4.1 如果执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数为“TRUE”，则不需要执行步骤 11。

#### 4.2 如果执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数为“FALSE”，则需要执行步骤 11。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=4 -->
```

### 5 执行**ADD APNTPL**命令增加APN模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_apntpl_list的变量区（command: ADD APNTPL） -#}
<!-- MISSING_MACRO: command=ADD APNTPL list_name=add_apntpl_list step_id=5 -->
```

### 6 执行**ADD EPSQOSTPL**命令增加EPS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_epsqostpl_list的变量区（command: ADD EPSQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD EPSQOSTPL list_name=add_epsqostpl_list step_id=6 -->
```

### 7 执行**ADD OPTGPRSTPL**和**MOD OPTGPRSTPL**命令配置优化GPRS/EPS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_optgprstpl_list的变量区（command: ADD OPTGPRSTPL） -#}
<!-- MISSING_MACRO: command=ADD OPTGPRSTPL list_name=add_optgprstpl_list step_id=7 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_optgprstpl_list的变量区（command: MOD OPTGPRSTPL） -#}
<!-- MISSING_MACRO: command=MOD OPTGPRSTPL list_name=mod_optgprstpl_list step_id=7 -->
```

### 8 执行**MOD TPLOPTGPRS**命令给用户签约优化GPRS/EPS业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_tploptgprs_list的变量区（command: MOD TPLOPTGPRS） -#}
<!-- MISSING_MACRO: command=MOD TPLOPTGPRS list_name=mod_tploptgprs_list step_id=8 -->
```

### 9 执行**ADD RSITPL**命令增加业务下发模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rsitpl_list的变量区（command: ADD RSITPL） -#}
<!-- MISSING_MACRO: command=ADD RSITPL list_name=add_rsitpl_list step_id=9 -->
```

### 10 配置全局漫游限制模板。

#### 10.1 如果限制区域为本运营商内，则配置PLMN粒度。

##### 10.1.1 执行**ADD PLMNTPL**命令增加PLMN区域漫游模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_plmntpl_list的变量区（command: ADD PLMNTPL） -#}
<!-- MISSING_MACRO: command=ADD PLMNTPL list_name=add_plmntpl_list step_id=10.1.1 -->
```

##### 10.1.2 执行**SET MAPSERV**命令设置PLMN粒度全局APN替换漫游模板ID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list_1的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list_1 step_id=10.1.2 -->
```

#### 10.2 如果限制区域为用户归属省内，则配置Diameter粒度。

##### 10.2.1 执行**ADD DIAMRRTPL**命令增加Diameter漫游限制模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_diamrrtpl_list的变量区（command: ADD DIAMRRTPL） -#}
<!-- MISSING_MACRO: command=ADD DIAMRRTPL list_name=add_diamrrtpl_list step_id=10.2.1 -->
```

##### 10.2.2 执行**SET MAPSERV**命令设置Diameter粒度全局APN替换漫游模板ID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list_2的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list_2 step_id=10.2.2 -->
```

### 11 （可选）执行**MOD SXZW**命令给用户签约APN替换业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_sxzw_list的变量区（command: MOD SXZW） -#}
<!-- MISSING_MACRO: command=MOD SXZW list_name=mod_sxzw_list step_id=11 -->
```

