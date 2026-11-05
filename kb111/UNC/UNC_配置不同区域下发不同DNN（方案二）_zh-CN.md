---
id: ''
name: 配置不同区域下发不同DNN（方案二）
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员在5G网络中配置不同区域下发不同DNN，配置独立开户模板。  * 运营商大网SMF POOL业务不均质，从POOL中选择两台SMF作为智能分流SMF时，UDM使用此章节方式进行配置。 * 配置不同区域下发不同DNN/APN时用户免签约功能（执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数）在UDM 20.11.2.15及之后的版本支持，之前的版本无需关注此功能，之后的版本根据局点实际规划进行设置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UDM","配置5G用户签约","配置不同区域下发不同DNN（方案二）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员在5G网络中配置不同区域下发不同DNN，配置独立开户模板。* 运营商大网SMF POOL业务不均质，从POOL中选择两台SMF作为智能分流SMF时，UDM使用此章节方式进行配置。* 配置不同区域下发不同DNN/APN时用户免签约功能（执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数）在UDM 20.11.2.15及之后的版本支持，之前的版本无需关注此功能，之后的版本根据局点实际规划进行设置。

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
    set_mapserv_list:
      type: items
      properties:
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
          description: '用于标识UDM是否支持双域DNN/APN业务。   * 在5G网络中，该参数用于控制UDM是否支持双域DNN业务。 * 请勿随意修改该参数，修改前请联系华为技术支持。'
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
    add_ngcqostpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '本端规划'
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
        NGQI:
          name: '5QI'
          type: string
          required: false
          description: '用于标识5G QoS特性的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPPRILEVEL:
          name: 'ARP优先级'
          type: string
          required: false
          description: '用于标识用户在网络资源拥塞时的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dnnqostpl_list:
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
        PDUTYPE:
          name: '默认PDU类型'
          type: string
          required: false
          description: '用于标识默认PDU会话类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SSCMODE:
          name: '默认SSC模式'
          type: string
          required: false
          description: '用于标识默认会话和业务连续性模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ALLOWEDSCCMODE:
          name: '其它允许的SSC模式'
          type: string
          required: false
          description: '用于标识其它允许的会话和业务连续性模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IWKEPSIND:
          name: '是否签约EPS互操作'
          type: string
          required: false
          description: '用于标识是否签约EPS互操作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LADN:
          name: '是否为LADN'
          type: string
          required: false
          description: '用于标识是否支持本地数据网络。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LBO:
          name: '是否允许Local Break Out'
          type: string
          required: false
          description: '用于标识漫游场景下是否允许使用漫游地网关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCQOSTPLID:
          name: '5GC QoS模板ID'
          type: string
          required: false
          description: '用于标识5GC QoS模板ID。该参数必须先由**ADD NGCQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'DNN级别上行速率'
          type: string
          required: false
          description: '用于标识DNN级别上行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'DNN级别上行速率单位'
          type: string
          required: false
          description: '用于标识DNN级别上行速率单位的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'DNN级别下行速率'
          type: string
          required: false
          description: '用于标识DNN级别下行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'DNN级别下行速率单位'
          type: string
          required: false
          description: '用于标识DNN级别下行速率单位的参数。'
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
        UPINTEGR:
          name: '用户面完整性保护策略'
          type: string
          required: false
          description: '用于标识用户面完整性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPCONFID:
          name: '用户面机密性保护策略'
          type: string
          required: false
          description: '用于标识用户面机密性保护策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDARYAUTH:
          name: '是否需要二次认证授权'
          type: string
          required: false
          description: '用于标识SMF在用户PDU会话建立时是否需要二次认证授权。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AAAIPALLOCATION:
          name: 'PDU会话建立是否需要SMF向DN-AAA请求UE的IP地址'
          type: string
          required: false
          description: '用于标识PDU会话建立流程中SMF是否需要向DN-AAA请求UE的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SAMESMFIND:
          name: '到相同DNN和S-NSSAI的多个PDU会话是否需要相同的SMF'
          type: string
          required: false
          description: '用于标识到相同DNN和S-NSSAI的多个PDU会话是否要求SMF相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_smdatatpl_list:
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
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFSNSSAI:
          name: '是否默认S-NSSAI'
          type: string
          required: false
          description: '用于标识签约的S-NSSAI数据是否为默认S-NSSAI数据。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQOS模板ID'
          type: string
          required: false
          description: '用于标识用户待签约的5GS DNNQoS模板ID。该参数必须由**ADD DNNQOSTPL**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_smdatatpl_list:
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
        SNSSAI:
          name: '切片标识'
          type: string
          required: false
          description: '用于标识5G系统中的网络切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          required: false
          description: '用于标识修改5G会话信息模板的操作类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        DNN:
          name: '数据网名称'
          type: string
          required: false
          description: '用于标识数据网名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNQOSTPLID:
          name: '5GS DNNQOS模板ID'
          type: string
          required: false
          description: '用于标识5GS DNNQOS模板ID。该参数必须由**ADD DNNQOSTPL**命令定义后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULT:
          name: '是否为默认DNN'
          type: string
          required: false
          description: '用于标识签约的DNN数据是否为默认DNN数据。'
          data_source: '固定配置'
          pattern: ''
          default: ''
    add_ngsusertpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: string
          required: false
          description: '已配置数据中获取  用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '本端规划'
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
          description: '用于标识5GS用户模板在系统中的名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRUP:
          name: 'UE级别上行速率'
          type: string
          required: false
          description: '用于标识UE级别上行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPUNIT:
          name: 'UE级别上行速率单位'
          type: string
          required: false
          description: '用于标识“UE级别上行速率”的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMBRDW:
          name: 'UE级别下行速率'
          type: string
          required: false
          description: '用于标识UE级别下行速率的参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DWUNIT:
          name: 'UE级别下行速率单位'
          type: string
          required: false
          description: '用于标识“UE级别下行速率”的单位。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RFSPINDEX:
          name: '无线频率选择优先级'
          type: string
          required: false
          description: '用于标识无线频率选择优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBSREGTIMER:
          name: '周期注册定时器'
          type: string
          required: false
          description: '用于标识周期注册定时器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MPS:
          name: '是否支持多媒体优先级服务'
          type: string
          required: false
          description: '用于标识是否提供多媒体优先级服务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACTIVETIME:
          name: '激活时间定时器'
          type: string
          required: false
          description: '用于标识UE在PSM模式开启时，从进入IDLE态开始到进入PSM态的定时器时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DLBUFFERIND:
          name: '提供签约高延迟通信时的下行缓存大小'
          type: string
          required: false
          description: '用于标识当签约高延迟通信时，是否提供下行缓存的大小。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AUTHTYPE:
          name: '鉴权方式'
          type: string
          required: false
          description: '用于标识鉴权方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MICOALLOWED:
          name: '是否支持MICO模式'
          type: string
          required: false
          description: '用于标识是否支持MICO模式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MCS:
          name: '是否支持关键任务优先级服务'
          type: string
          required: false
          description: '用于标识是否提供关键任务优先级服务功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMDATATPLID:
          name: '会话信息模板ID'
          type: string
          required: false
          description: '用于标识会话信息模板ID。该参数必须先由**ADD SMDATATPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SMSSUBSCRIBED:
          name: '是否允许SMS over NAS'
          type: string
          required: false
          description: '用于标识是否允许使用5G NAS短消息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tplngs_list:
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
        NGSUSERTPLID:
          name: '5GS用户数据模板'
          type: string
          required: false
          description: '用于标识5GS用户数据模板号。该参数必须先由**ADD NGSUSERTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    mod_tplngs_list:
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
        NGSUSERTPLID:
          name: '5GS用户数据模板'
          type: string
          required: false
          description: '用于标识5GS用户数据模板号。该参数必须先由**ADD NGSUSERTPL**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ngcrsitpl_list:
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
          description: '用于标识当用户漫游到特定的5G区域后，对哪些业务进行下发。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        OLDDNNLIST:
          name: '旧DNN名称列表'
          type: string
          required: false
          description: '用于标识旧DNN名称列表。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NEWDNNLIST:
          name: '新DNN名称列表'
          type: string
          required: false
          description: '用于标识新DNN名称列表。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngcrrareatpl_list:
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
        AREATYPE:
          name: '区域限制类型'
          type: string
          required: false
          description: '用于标识NGC漫游限制区域模板的AMF限制类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFREGISTER:
          name: '应用到AMF注册流程'
          type: string
          required: false
          description: '用于标识NGC漫游限制是否应用到AMF注册流程。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMN:
          name: 'PLMNID'
          type: string
          required: false
          description: '用于标识PLMN ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMFREGISTER:
          name: '应用到SMF注册流程'
          type: string
          required: false
          description: '用于标识NGC漫游限制是否应用到SMF注册流程。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_ngcrrareatpl_list:
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
        OPTYPE:
          name: '漫游区域操作类型'
          type: string
          required: false
          description: '用于标识对NGC漫游限制区域模板的操作类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: '区域限制类型'
          type: string
          required: false
          description: '用于标识NGC漫游限制区域模板的AMF限制类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PLMN:
          name: 'PLMNID'
          type: string
          required: false
          description: '用于标识PLMN ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFREGION:
          name: 'AMF Region ID'
          type: string
          required: false
          description: '用于标识AMF Region ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFSET:
          name: 'AMF Set ID'
          type: string
          required: false
          description: '用于标识AMF Set ID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ngcrrnodetpl_list:
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
          name: 'AMF注册缺省漫游限制状态'
          type: string
          required: false
          description: '用于标识AMF注册流程中缺省漫游限制状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RRAREATPLID:
          name: '漫游限制区域模板ID'
          type: string
          required: false
          description: '用于标识NGC漫游限制区域模板ID。该参数必须由**ADD NGCRRAREATPL**定义后，才能在此引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULE:
          name: '漫游限制状态'
          type: string
          required: false
          description: '用于标识漫游限制状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGCRSITPLID:
          name: '业务下发模板ID'
          type: string
          required: false
          description: '用于标识NGC漫游限制模板关联的业务下发模板ID。该参数必须先通过**ADD NGCRSITPL**命令配置才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_udmserv_list_1:
      type: items
      properties:
        NGSSXZWRRID:
          name: 'DNN替换业务配置的全局NGC漫游限制模板ID'
          type: string
          required: false
          description: '用于标识DNN替换业务配置的全局NGC漫游限制模板ID。在业务流程中，UDM会基于该参数配置的NGC漫游限制模板，根据用户接入的位置匹配到具体的DNN替换业务码，再根据配置的DNN更名逻辑对下发的DNN进行替换。'
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
    set_mapserv_list:
    - EPC_CHK_5GS_IWK: NOTCHECK
    set_udmserv_list:
    - SUPP_DUAL_DOMAINS_DNN: TRUE
      SXZW_REPLACE_MODE: FALSE
    add_ngcqostpl_list:
    - HLRSN: '1'
      TPLID: '5'
      NGQI: '1'
      ARPPRILEVEL: '1'
    add_dnnqostpl_list:
    - HLRSN: '1'
      TPLID: '5'
      PDUTYPE: IPV4
      SSCMODE: SSC_MODE_1
      ALLOWEDSCCMODE: SSC_MODE_2&SSC_MODE_3
      IWKEPSIND: TRUE
      LADN: FALSE
      LBO: FALSE
      NGCQOSTPLID: '5'
      AMBRUP: '104857600'
      UPUNIT: bps
      AMBRDW: '1073741824'
      DWUNIT: bps
      CHARGE: '0400'
      UPINTEGR: NOT_NEEDED
      UPCONFID: NOT_NEEDED
      SECONDARYAUTH: ABSENT
      AAAIPALLOCATION: ABSENT
      SAMESMFIND: ABSENT
    add_smdatatpl_list:
    - HLRSN: '1'
      TPLID: '5'
      SNSSAI: 1-000000
      DEFSNSSAI: TRUE
      DNN: common.dnn
      DNNQOSTPLID: '5'
    mod_smdatatpl_list:
    - HLRSN: '1'
      TPLID: '5'
      SNSSAI: 1-000000
      PROV: ADD_DNN
      DNN: stjwt.gd
      DNNQOSTPLID: '6'
      DEFAULT: FALSE
    add_ngsusertpl_list:
    - HLRSN: '1'
      TPLID: '6'
      TPLNAME: 5G开通
      AMBRUP: '150'
      UPUNIT: Mbps
      AMBRDW: '2'
      DWUNIT: Gbps
      RFSPINDEX: '0'
      SUBSREGTIMER: '0'
      MPS: FALSE
      ACTIVETIME: '0'
      DLBUFFERIND: NOT_REQUESTED
      AUTHTYPE: 5G-AKA
      MICOALLOWED: FALSE
      MCS: FALSE
      SMDATATPLID: '5'
      SMSSUBSCRIBED: FALSE
    add_tplngs_list:
    - IMSI: '46100000912345'
      NGSUSERTPLID: '6'
    mod_tplngs_list:
    - IMSI: '46100000912345'
      NGSUSERTPLID: '6'
    add_ngcrsitpl_list:
    - HLRSN: '1'
      TPLID: '99'
      SERCODE: SXZW
      OLDDNNLIST: common.dnn
      NEWDNNLIST: common2.dnn
    add_ngcrrareatpl_list:
    - HLRSN: '1'
      TPLID: '12'
      AREATYPE: PLMN
      AMFREGISTER: TRUE
      PLMN: '11111'
      SMFREGISTER: TRUE
    mod_ngcrrareatpl_list:
    - HLRSN: '1'
      TPLID: '12'
      OPTYPE: ADD
      AREATYPE: AMFSET
      PLMN: '11111'
      AMFREGION: '1'
      AMFSET: '1'
    add_ngcrrnodetpl_list:
    - HLRSN: '1'
      TPLID: '12'
      DEFAULTRULE: PERMISSION
      RRAREATPLID: '12'
      RULE: PERMISSION
      NGCRSITPLID: '99'
    set_udmserv_list_1:
    - NGSSXZWRRID: '12'
    mod_sxzw_list:
    - IMSI: '46100000912345'
      CTRLSCHE: 5GSXZW
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录“UDM业务管理”窗口。

### 如果现网已配置5G用户数据，则可跳过步骤 4~步骤 8。

### 2 执行**SET MAPSERV**命令设置MAP业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_mapserv_list的变量区（command: SET MAPSERV） -#}
<!-- MISSING_MACRO: command=SET MAPSERV list_name=set_mapserv_list step_id=2 -->
```

### 3 执行**SET UDMSERV**命令设置UDM业务数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list step_id=3 -->
```

### 该步骤可选配置“DNN/APN替换业务是否免用户签约”参数。

### 如果执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数为“TRUE”，则不需要执行步骤 13。

### 如果执行**SET UDMSERV**命令设置“DNN/APN替换业务是否免用户签约”参数为“FALSE”，则需要执行步骤 13。

### 4 执行**ADD NGCQOSTPL**命令增加5GS QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcqostpl_list的变量区（command: ADD NGCQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD NGCQOSTPL list_name=add_ngcqostpl_list step_id=4 -->
```

### 5 执行**ADD DNNQOSTPL**命令增加5GS DNN QoS模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_dnnqostpl_list的变量区（command: ADD DNNQOSTPL） -#}
<!-- MISSING_MACRO: command=ADD DNNQOSTPL list_name=add_dnnqostpl_list step_id=5 -->
```

### 6 执行**ADD SMDATATPL**和**MOD SMDATATPL**命令配置5G SMDATA模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_smdatatpl_list的变量区（command: ADD SMDATATPL） -#}
<!-- MISSING_MACRO: command=ADD SMDATATPL list_name=add_smdatatpl_list step_id=6 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_smdatatpl_list的变量区（command: MOD SMDATATPL） -#}
<!-- MISSING_MACRO: command=MOD SMDATATPL list_name=mod_smdatatpl_list step_id=6 -->
```

### 7 执行**ADD NGSUSERTPL**命令增加5GS用户模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngsusertpl_list的变量区（command: ADD NGSUSERTPL） -#}
<!-- MISSING_MACRO: command=ADD NGSUSERTPL list_name=add_ngsusertpl_list step_id=7 -->
```

### 8 给用户签约会话管理数据。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_tplngs_list的变量区（command: ADD TPLNGS） -#}
<!-- MISSING_MACRO: command=ADD TPLNGS list_name=add_tplngs_list step_id=8 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_tplngs_list的变量区（command: MOD TPLNGS） -#}
<!-- MISSING_MACRO: command=MOD TPLNGS list_name=mod_tplngs_list step_id=8 -->
```

### 对于新用户，需要开户后再执行**ADD TPLNGS**命令签约5G数据。

### 如果用户已签约5G数据且在网，则使用**MOD TPLNGS**命令签约。

### 9 执行**ADD NGCRSITPL**命令增加5G业务下发模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcrsitpl_list的变量区（command: ADD NGCRSITPL） -#}
<!-- MISSING_MACRO: command=ADD NGCRSITPL list_name=add_ngcrsitpl_list step_id=9 -->
```

### 10 执行**ADD NGCRRAREATPL**和**MOD NGCRRAREATPL**命令配置NGC漫游限制区域模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcrrareatpl_list的变量区（command: ADD NGCRRAREATPL） -#}
<!-- MISSING_MACRO: command=ADD NGCRRAREATPL list_name=add_ngcrrareatpl_list step_id=10 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_ngcrrareatpl_list的变量区（command: MOD NGCRRAREATPL） -#}
<!-- MISSING_MACRO: command=MOD NGCRRAREATPL list_name=mod_ngcrrareatpl_list step_id=10 -->
```

### 11 执行**ADD NGCRRNODETPL**命令增加NGC漫游限制模板。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngcrrnodetpl_list的变量区（command: ADD NGCRRNODETPL） -#}
<!-- MISSING_MACRO: command=ADD NGCRRNODETPL list_name=add_ngcrrnodetpl_list step_id=11 -->
```

### 12 执行**SET UDMSERV**命令设置全局DNN替换漫游模板ID。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_udmserv_list_1的变量区（command: SET UDMSERV） -#}
<!-- MISSING_MACRO: command=SET UDMSERV list_name=set_udmserv_list_1 step_id=12 -->
```

### 13 （可选）执行**MOD SXZW**命令给用户签约DNN替换业务。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_sxzw_list的变量区（command: MOD SXZW） -#}
<!-- MISSING_MACRO: command=MOD SXZW list_name=mod_sxzw_list step_id=13 -->
```

