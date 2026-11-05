---
id: GWFD-026104
name: 配置支持NB-IoT eDRX模式特性
ne_type: UEG
type: feature
description: 该任务旨在指导操作人员签约/修改/去签约PTW寻呼时间窗参数。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","HSS&UDM特性指南","GWFD-026100 NB-IoT基本功能","GWFD-026104 支持NB-IoT eDRX模式","配置支持NB-IoT eDRX模式特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
该任务旨在指导操作人员签约/修改/去签约PTW寻呼时间窗参数。

## 必备事项
前提条件

* 请仔细阅读WHFD-800039 支持NB-IoT eDRX模式特性概述。
* 用户为EPS网络用户。
* 操作人员具有数据配置权限。
* 操作人员具有登录PGW Web LMT的用户名和密码。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_subtpl_list:
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
          description: '用于唯一标识增加的开户模板。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TPLTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: '用于标识用户模板类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用于标识开通卡类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        NAM:
          name: '网络接入模式'
          type: string
          required: false
          description: '用于标识允许用户接入网络的网络类型。  配置为“NONE”，避免占用2G/3G用户License。  说明：  当该参数取值为“MSC”，且**SET MAPCONF**命令中的“用户NAM取值为MSC时，在EPC域鉴权、注册是否按照3GPP协议处理”取值为“TRUE”时，无法在LTE注册成功，不允许自动开户。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '用于标识EPS业务标识。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: string
          required: false
          description: '用于标识4G网络UE最大上行带宽，即UE最大的上传速率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: string
          required: false
          description: '用于标识4G网络UE最大下行带宽，即UE最大的下载速率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_epsusertpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '用于标识EPS用户模板ID。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '用于标识EPS用户最大上行带宽，即发送消息的最大带宽。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '用于标识EPS用户最大下行带宽，即接受消息的最大带宽。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CNTXID:
          name: 'PDN上下文索引值'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: '用于标识PDN上下文索引值，每个PDN上下文的索引值不能相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EPSAPNQOSTPLID:
          name: 'EPSAPNQOS模板ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '用于标识EPSAPNQOS模板ID，该参数必须先由**ADD EPSAPNQOSTPL**命令定义，然后才能在此处引用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_sub_list:
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
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识需要开户的用户的IMSI号码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISDN:
          name: 'ISDN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用于标识需要开户的用户的卡类型。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        NAM:
          name: '网络接入模式'
          type: string
          required: false
          description: '用于标识允许用户接入网络的网络类型。  配置为“NONE”，避免占用2G/3G用户License。  说明：  当该参数取值为“MSC”，且**SET MAPCONF**命令中的“用户NAM取值为MSC时，在EPC域鉴权、注册是否按照3GPP协议处理”取值为“TRUE”时，无法在LTE注册成功，不允许自动开户。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '用于标识为用户提供EPS业务。签约支持SWx接口（Non-3GPP接入）业务的用户该参数必须设置为“TRUE”。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        DEFAULTCALL:
          name: '缺省呼叫类型'
          type: string
          required: false
          description: '用于标识用户缺省呼叫类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXUL:
          name: 'UE最大上行带宽'
          type: string
          required: false
          description: '用于标识UE最大上行带宽，即UE最大的上传速率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMBRMAXDL:
          name: 'UE最大下行带宽'
          type: string
          required: false
          description: '用于标识UE最大下行带宽，即UE最大的下载速率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSISDN:
          name: 'MSISDN'
          type: string
          required: false
          description: '用于标识需要开户的用户的MSISDN号码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_subtpl_list:
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
          description: '用于标识一个待修改的模板ID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: '用于标识用户模板类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用于标识开通卡类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '用于标识EPS业务标识。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_epsusertpl_list:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板 ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '用于标识一个待修改的模板ID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          enum:
          - ADDPDNCNTX
          - MODPDNCNTX
          - RMVPDNCNTX
          - MODEPSINFO
          - MODDEFPDN
          - MODDEFNONIPPDN
          required: false
          description: '用于标识对EPS用户模板的操作类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_eps_list:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识一个待修改的IMSI号码。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供EPS业务'
          type: string
          required: false
          description: '用于标识提供还是撤销EPS业务。   * TRUE：提供。 * FALSE：撤销。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_subtpl_list_1:
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
          description: '用于标识一个待修改的模板ID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLTYPE:
          name: '用户模板类型'
          type: string
          required: false
          description: '用于标识用户模板类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CARDTYPE:
          name: '卡类型'
          type: string
          required: false
          description: '用于标识开通卡类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        EPS:
          name: 'EPS业务标识'
          type: string
          required: false
          description: '用于标识EPS业务标识。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_epsusertpl_list_1:
      type: items
      properties:
        HLRSN:
          name: 'HLR序列号'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '用于标识一个HLR序列号。该参数必须先由**ADD HLRSN**命令定义，然后才能在此处引用。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TPLID:
          name: '模板 ID'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '用于标识一个待修改的模板ID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROV:
          name: '操作类型'
          type: string
          enum:
          - ADDPDNCNTX
          - MODPDNCNTX
          - RMVPDNCNTX
          - MODEPSINFO
          - MODDEFPDN
          - MODDEFNONIPPDN
          required: false
          description: '用于标识对EPS用户模板的操作类型。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_eps_list_1:
      type: items
      properties:
        IMSI:
          name: 'IMSI'
          type: string
          required: false
          description: '用于标识一个待修改的IMSI号码。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROV:
          name: '是否提供EPS业务'
          type: string
          required: false
          description: '用于标识提供还是撤销EPS业务。   * TRUE：提供。 * FALSE：撤销。'
          data_source: '固定配置'
          pattern: ''
          default: ''
        SUPWBPTW:
          name: '是否支持WB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约WB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUPNBPTW:
          name: '是否支持NB模式PTW'
          type: string
          required: false
          description: '用于标识是否支持签约NB模式寻呼时间窗（Paging Time Window）。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WBPTW:
          name: 'WB模式PTW'
          type: string
          required: false
          description: '用于标识WB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NBPTW:
          name: 'NB模式PTW'
          type: string
          required: false
          description: '用于标识NB模式下，终端在eDRX周期中包含的寻呼时间窗。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_subtpl_list:
    - HLRSN: '1'
      TPLID: '1'
      TPLTYPE: NORMAL
      CARDTYPE: USIM
      NAM: NONE
      EPS: TRUE
      AMBRMAXUL: '10000000'
      AMBRMAXDL: '20000000'
      WBPTW: '5'
      NBPTW: '5'
    add_epsusertpl_list:
    - HLRSN: 1
      TPLID: 100
      AMBRMAXUL: 10000000
      AMBRMAXDL: 20000000
      CNTXID: 1
      EPSAPNQOSTPLID: 1
      WBPTW: 5
      NBPTW: 5
    add_sub_list:
    - HLRSN: '1'
      IMSI: '460000009123456'
      ISDN: '8613900001234'
      CARDTYPE: USIM
      NAM: NONE
      EPS: TRUE
      DEFAULTCALL: TS11
      AMBRMAXUL: '10000000'
      AMBRMAXDL: '20000000'
      WBPTW: '5'
      NBPTW: '5'
      MSISDN: '8613900001234'
    mod_subtpl_list:
    - HLRSN: '1'
      TPLID: '1'
      TPLTYPE: NORMAL
      CARDTYPE: USIM
      EPS: TRUE
      SUPWBPTW: TRUE
      WBPTW: '7'
      SUPNBPTW: TRUE
      NBPTW: '7'
    mod_epsusertpl_list:
    - HLRSN: 1
      TPLID: 100
      PROV: MODEPSINFO
      SUPWBPTW: TRUE
      WBPTW: 7
      SUPNBPTW: TRUE
      NBPTW: 7
    mod_eps_list:
    - IMSI: '460000009123456'
      PROV: TRUE
      SUPWBPTW: TRUE
      WBPTW: '7'
      SUPNBPTW: TRUE
      NBPTW: '7'
    mod_subtpl_list_1:
    - HLRSN: '1'
      TPLID: '1'
      TPLTYPE: NORMAL
      CARDTYPE: USIM
      EPS: TRUE
      SUPWBPTW: FALSE
      SUPNBPTW: FALSE
      WBPTW: '7'
      NBPTW: '7'
    mod_epsusertpl_list_1:
    - HLRSN: 1
      TPLID: 100
      PROV: MODEPSINFO
      SUPWBPTW: FALSE
      SUPNBPTW: FALSE
      WBPTW: 7
      NBPTW: 7
    mod_eps_list_1:
    - IMSI: '460000009123456'
      PROV: TRUE
      SUPWBPTW: FALSE
      SUPNBPTW: FALSE
      WBPTW: '7'
      NBPTW: '7'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UDM业务管理”窗口。

### 2 签约PTW寻呼时间窗参数。可以执行**ADD SUB**命令为用户开户时直接进行签约，也可以先在**ADD SUBTPL**/**ADD EPSUSERTPL**开户模板命令中签约后，再执行**ADD SUB**命令为用户进行模板开户。

#### 2.1 执行**ADD SUBTPL**命令，定义“用户模板类型”为“NORMAL”的用户开户模板，在开户模板中设置PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_subtpl_list的变量区（command: ADD SUBTPL） -#}
<!-- MISSING_MACRO: command=ADD SUBTPL list_name=add_subtpl_list step_id=2.1 -->
```

#### 2.2 执行**ADD EPSUSERTPL**命令，定义EPS用户开户模板，在开户模板中设置PTW寻呼时间窗参数。

```jinja2
{%- for item in add_epsusertpl_list -%}
    ADD EPSUSERTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    AMBRMAXUL={{item.AMBRMAXUL}},
    AMBRMAXDL={{item.AMBRMAXDL}},
    CNTXID={{item.CNTXID}},
    EPSAPNQOSTPLID={{item.EPSAPNQOSTPLID}},
    {#- --- 可选参数 --- -#}
    {%- if item.WBPTW is not none -%}
        WBPTW={{item.WBPTW}},
    {%- endif -%}
    {%- if item.NBPTW is not none -%}
        NBPTW={{item.NBPTW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 执行**ADD SUB**命令，为用户开户，设置PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_sub_list的变量区（command: ADD SUB） -#}
<!-- MISSING_MACRO: command=ADD SUB list_name=add_sub_list step_id=2.3 -->
```

### 3 修改PTW寻呼时间窗参数。可以执行**MOD EPS**命令为用户修改PTW参数，也可以执行**MOD SUBTPL**/**MOD EPSUSERTPL**命令修改开户模板中的PTW参数，开户模板中数据修改后，会应用到所有使用模板开户的用户中。

#### 3.1 执行**MOD SUBTPL**命令，修改“用户模板类型”为“NORMAL”的用户开户模板中的PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_subtpl_list的变量区（command: MOD SUBTPL） -#}
<!-- MISSING_MACRO: command=MOD SUBTPL list_name=mod_subtpl_list step_id=3.1 -->
```

#### 3.2 执行**MOD EPSUSERTPL**命令，修改EPS用户开户模板中的PTW寻呼时间窗参数。

```jinja2
{%- for item in mod_epsusertpl_list -%}
    MOD EPSUSERTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    {#- --- 可选参数 --- -#}
    {%- if item.PROV is not none -%}
        PROV={{item.PROV}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROV=MODEPSINFO 时可选 --- -#}
    {%- if item.PROV == 'MODEPSINFO' -%}
        {%- if item.SUPWBPTW is not none -%}
            SUPWBPTW={{item.SUPWBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUPWBPTW=TRUE 时可选 --- -#}
    {%- if item.SUPWBPTW == 'TRUE' -%}
        {%- if item.WBPTW is not none -%}
            WBPTW={{item.WBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROV=MODEPSINFO 时可选 --- -#}
    {%- if item.PROV == 'MODEPSINFO' -%}
        {%- if item.SUPNBPTW is not none -%}
            SUPNBPTW={{item.SUPNBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUPNBPTW=TRUE 时可选 --- -#}
    {%- if item.SUPNBPTW == 'TRUE' -%}
        {%- if item.NBPTW is not none -%}
            NBPTW={{item.NBPTW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 执行**MOD EPS**命令，修改用户的PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_eps_list的变量区（command: MOD EPS） -#}
<!-- MISSING_MACRO: command=MOD EPS list_name=mod_eps_list step_id=3.3 -->
```

### 4 去签约PTW寻呼时间窗参数。可以执行**MOD EPS**命令为用户去签约PTW参数，也可以执行**MOD SUBTPL**/**MOD EPSUSERTPL**命令去签约开户模板中的PTW参数，开户模板中数据去签约后，会应用到所有使用模板开户的用户中。

#### 4.1 执行**MOD SUBTPL**命令，在“用户模板类型”为“NORMAL”的用户开户模板中去签约PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_subtpl_list_1的变量区（command: MOD SUBTPL） -#}
<!-- MISSING_MACRO: command=MOD SUBTPL list_name=mod_subtpl_list_1 step_id=4.1 -->
```

#### 4.2 执行**MOD EPSUSERTPL**命令，在EPS用户开户模板中去签约PTW寻呼时间窗参数。

```jinja2
{%- for item in mod_epsusertpl_list_1 -%}
    MOD EPSUSERTPL:
    {#- --- 必选参数 --- -#}
    HLRSN={{item.HLRSN}},
    TPLID={{item.TPLID}},
    {#- --- 可选参数 --- -#}
    {%- if item.PROV is not none -%}
        PROV={{item.PROV}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PROV=MODEPSINFO 时可选 --- -#}
    {%- if item.PROV == 'MODEPSINFO' -%}
        {%- if item.SUPWBPTW is not none -%}
            SUPWBPTW={{item.SUPWBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PROV=MODEPSINFO 时可选 --- -#}
    {%- if item.PROV == 'MODEPSINFO' -%}
        {%- if item.SUPNBPTW is not none -%}
            SUPNBPTW={{item.SUPNBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUPWBPTW=TRUE 时可选 --- -#}
    {%- if item.SUPWBPTW == 'TRUE' -%}
        {%- if item.WBPTW is not none -%}
            WBPTW={{item.WBPTW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SUPNBPTW=TRUE 时可选 --- -#}
    {%- if item.SUPNBPTW == 'TRUE' -%}
        {%- if item.NBPTW is not none -%}
            NBPTW={{item.NBPTW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 执行**MOD EPS**命令，为用户去签约PTW寻呼时间窗参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_eps_list_1的变量区（command: MOD EPS） -#}
<!-- MISSING_MACRO: command=MOD EPS list_name=mod_eps_list_1 step_id=4.3 -->
```

