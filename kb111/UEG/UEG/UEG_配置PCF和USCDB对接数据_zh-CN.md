---
id: ''
name: 配置PCF和USCDB对接数据
ne_type: UEG
type: feature
description: 开局时，配置PCF与USCDB的对接数据。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置PCF/PCRF","配置PCF和USCDB对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
开局时，配置PCF与USCDB的对接数据。

## 必备事项
前提条件

已经完成PCF、USCDB的基础数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_groupswitch_list:
      type: items
      properties:
        GROUPNAME:
          name: '分组名称'
          type: string
          maxLength: 128
          required: true
          description: 'FE侧支持多应用共存的分组名称。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        GROUPSWITCH:
          name: '分组开关'
          type: string
          enum:
          - OPEN
          - CLOSE
          required: true
          description: 'FE侧支持多应用共存的业务分组开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_rlocation_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '表示远端Location标识，可在PCF侧使用**LST DBSLOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载对应的网元插件包之后才能在此处进行设置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级值'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: 'UEG间FE和BE不交叉互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDUNFLAG:
          name: '是否容灾关系'
          type: string
          enum:
          - No
          - Yes
          required: true
          description: 'BE对接FE时，固定配置为NO。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rlocation_list_2:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '表示远端Location标识，可在PCF侧使用**LST DBSLOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载对应的网元插件包之后才能在此处进行设置。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级值'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: 'UEG间FE和BE不交叉互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDUNFLAG:
          name: '是否容灾关系'
          type: string
          enum:
          - No
          - Yes
          required: true
          description: 'BE对接FE时，固定配置为NO。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rdsg_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '**配置PCF基础数据**页面中，命令**ADD DBSSERVICENO**定义，对应参数“SERVICENO”的取值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: '对接FE时，取值固定为“DBS”。'
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_rdsg_list_4:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '**配置PCF基础数据**页面中，命令**ADD DBSSERVICENO**定义，对应参数“SERVICENO”的取值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: '对接FE时，取值固定为“DBS”。'
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_rdsg_list_6:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '**配置PCF基础数据**页面中，命令**ADD DBSSERVICENO**定义，对应参数“SERVICENO”的取值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: '对接FE时，取值固定为“DBS”。'
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_rdsg_list_10:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '**配置PCF基础数据**页面中，命令**ADD DBSSERVICENO**定义，对应参数“SERVICENO”的取值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: '对接FE时，取值固定为“DBS”。'
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_ripaddr_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过**ADD RLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端DPU模块号/远端IP的VPN索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端PCF上由**ADD DBSIPADDR**先定义。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端PCF中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端PCF中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RDPUST:
          name: '远端IP地址业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_ripaddr_list_2:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端PCF中先定义，然后在本端网元通过**ADD RLOCATION**命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端DPU模块号/远端IP的VPN索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端PCF上由**ADD DBSIPADDR**先定义。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端PCF中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端PCF中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RDPUST:
          name: '远端IP地址业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过**LOD FEPLUG**命令加载PCF插件后在此引用。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_notifycfg_list:
      type: items
      properties:
        FETYPE:
          name: '订阅通知的FE类型'
          type: string
          maxLength: 128
          required: true
          description: '固定配置为UPCF。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FEID:
          name: 'FE标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: '取值范围内不允许重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INFTYPE:
          name: '订阅通知的接口类型'
          type: string
          enum:
          - MCI
          - SOAP
          - FILE
          - THIRDPARTY
          required: true
          description: '在此场景下固定配置为“MCI”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SYNCHROSWITCH:
          name: '同步开关'
          type: string
          enum:
          - ASYNC
          - SYNC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONID:
          name: '订阅通知发送的Location标识'
          type: integer
          minimum: 0
          maximum: 512
          required: false
          description: '表示远端Location标识，可在PCF侧使用**LST LOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        NOTIFYDEST:
          name: '通知目标'
          type: integer
          minimum: 0
          maximum: 2
          required: false
          description: '非混合组网场景下，固定配置为“2”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_notifycfg_list_1:
      type: items
      properties:
        FETYPE:
          name: '订阅通知的FE类型'
          type: string
          maxLength: 128
          required: true
          description: '固定配置为UPCF。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FEID:
          name: 'FE标识'
          type: integer
          minimum: 1
          maximum: 100
          required: true
          description: '取值范围内不允许重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INFTYPE:
          name: '订阅通知的接口类型'
          type: string
          enum:
          - MCI
          - SOAP
          - FILE
          - THIRDPARTY
          required: true
          description: '在此场景下固定配置为“MCI”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SYNCHROSWITCH:
          name: '同步开关'
          type: string
          enum:
          - ASYNC
          - SYNC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONID:
          name: '订阅通知发送的Location标识'
          type: integer
          minimum: 0
          maximum: 512
          required: false
          description: '表示远端Location标识，可在PCF侧使用**LST LOCATION**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        NOTIFYDEST:
          name: '通知目标'
          type: integer
          minimum: 0
          maximum: 2
          required: false
          description: '非混合组网场景下，固定配置为“2”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dbsgrpswitch_list:
      type: items
      properties:
        GROUPNAME:
          name: '分组名称'
          type: string
          minLength: 0
          maxLength: 128
          required: true
          description: 'FE侧支持多应用共存的分组名称。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        GROUPSWITCH:
          name: '分组开关'
          type: string
          enum:
          - OPEN
          - CLOSE
          required: true
          description: 'FE侧支持多应用共存的业务分组开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsrlocation_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          enum:
          - USCDB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '优先级值越小，优先级越高。  UEG间FE和BE不交互互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsrlocation_list_1:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '-'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          enum:
          - USCDB
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '优先级值越小，优先级越高。  UEG间FE和BE不交互互连，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsrdsg_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '可登录“USCDB MML命令”界面，执行“**LST MODULE: MT=DSG;**”查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'PCF（FE）与USCDB对接时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsrdsg_list_4:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '可登录“USCDB MML命令”界面，执行“**LST MODULE: MT=DSG;**”查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'PCF（FE）与USCDB对接时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsripaddr_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端业务IP的索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端USCDB网元由**ADD SRVIPADDR**先定义（“SRVINDEX”参数值）。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RIPST:
          name: '远端IP地址业务类型'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'PCF（FE）与USCDB对接时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dbsripaddr_list_2:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端业务IP的索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端USCDB网元由**ADD SRVIPADDR**先定义（“SRVINDEX”参数值）。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RIPST:
          name: '远端IP地址业务类型'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: 'PCF（FE）与USCDB对接时，使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    act_ipdisp_list:
      type: items
      properties: {}
    act_dbsipdisp_list:
      type: items
      properties: {}
  examples:
    set_groupswitch_list:
    - GROUPNAME: 'UPCF'
      GROUPSWITCH: OPEN
    add_rlocation_list:
    - RLOCID: 13
      RMT: 'UPCF'
      LP: 5
      REDUNFLAG: No
    add_rlocation_list_2:
    - RLOCID: 15
      RMT: 'UPCF'
      LP: 10
      REDUNFLAG: No
    add_rdsg_list:
    - RLOCID: 13
      RDSGMID: 301
      RDSGST: 'UPCF'
      RDSGTYPE: DBS
    add_rdsg_list_4:
    - RLOCID: 13
      RDSGMID: 301
      RDSGST: 'UPCF'
      RDSGTYPE: DBS
    add_rdsg_list_6:
    - RLOCID: 15
      RDSGMID: 301
      RDSGST: 'UPCF'
      RDSGTYPE: DBS
    add_rdsg_list_10:
    - RLOCID: 15
      RDSGMID: 301
      RDSGST: 'UPCF'
      RDSGTYPE: DBS
    add_ripaddr_list:
    - RLOCID: 13
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.200.200.22'
      IPV4IP2: '10.200.200.23'
      RDPUST: 'UPCF'
    add_ripaddr_list_2:
    - RLOCID: 15
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.201.200.22'
      IPV4IP2: '10.201.200.23'
      RDPUST: 'UPCF'
    add_notifycfg_list:
    - FETYPE: 'UPCF'
      FEID: 3
      INFTYPE: MCI
      SYNCHROSWITCH: ASYNC
      LOCATIONID: 13
      NOTIFYDEST: 2
      IPVER: ''
    add_notifycfg_list_1:
    - FETYPE: 'UPCF'
      FEID: 4
      INFTYPE: MCI
      SYNCHROSWITCH: ASYNC
      LOCATIONID: 15
      NOTIFYDEST: 2
      IPVER: ''
    set_dbsgrpswitch_list:
    - GROUPNAME: 'UPCF'
      GROUPSWITCH: OPEN
    add_dbsrlocation_list:
    - RLOCID: 14
      RMT: USCDB
      LP: 5
    add_dbsrlocation_list_1:
    - RLOCID: 16
      RMT: USCDB
      LP: 10
    add_dbsrdsg_list:
    - RLOCID: 14
      RDSGMID: 1017
      RDSGST: 'UPCF'
    add_dbsrdsg_list_4:
    - RLOCID: 16
      RDSGMID: 1017
      RDSGST: 'UPCF'
    add_dbsripaddr_list:
    - RLOCID: 14
      ID: 21
      IPVER: IPV4
      IPV4IP1: '10.200.200.32'
      IPV4IP2: '10.200.200.33'
      RIPST: 'UPCF'
    add_dbsripaddr_list_2:
    - RLOCID: 16
      ID: 21
      IPVER: IPV4
      IPV4IP1: '10.201.200.32'
      IPV4IP2: '10.201.200.33'
      RIPST: 'UPCF'
    act_ipdisp_list:
    - {}
    act_dbsipdisp_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2~6用于配置USCDB与PCF/PCRF对接。容灾组网中，同一UEG内的FE和BE对接，不同UEG内不交叉对接。

### 如已完成园区UDM的配置，则不需要重复配置2，请跳转到3。

### 2 设置分组开关。

```jinja2
{%- for item in set_groupswitch_list -%}
    SET GROUPSWITCH:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    GROUPSWITCH={{item.GROUPSWITCH}},
    ;
{%- endfor -%}
```

### 3 增加远端Location信息。

### DC1:

```jinja2
{%- for item in add_rlocation_list -%}
    ADD RLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT="{{item.RMT}}",
    LP={{item.LP}},
    REDUNFLAG={{item.REDUNFLAG}},
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_rlocation_list_2 -%}
    ADD RLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT="{{item.RMT}}",
    LP={{item.LP}},
    REDUNFLAG={{item.REDUNFLAG}},
    ;
{%- endfor -%}
```

### 4 增加远端DBS。

### 参数“RDSGMID”通过在“UEG MML命令”下使用“LST DBSSERVICENO:;”查询。

#### 4.1 DC1:

#### **虚机容器**：

```jinja2
{%- if is_scenario_vm_container -%}
    {%- for item in add_rdsg_list -%}
        ADD RDSG:
        {#- --- 必选参数 --- -#}
        RLOCID={{item.RLOCID}},
        RDSGMID={{item.RDSGMID}},
        RDSGST="{{item.RDSGST}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RDSGTYPE is not none -%}
            RDSGTYPE={{item.RDSGTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### **裸机容器**：

```jinja2
{%- if is_scenario_bare_metal_container -%}
    {%- for item in add_rdsg_list_4 -%}
        ADD RDSG:
        {#- --- 必选参数 --- -#}
        RLOCID={{item.RLOCID}},
        RDSGMID={{item.RDSGMID}},
        RDSGST="{{item.RDSGST}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RDSGTYPE is not none -%}
            RDSGTYPE={{item.RDSGTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 DC2:

#### **虚机容器**：

```jinja2
{%- if is_scenario_vm_container -%}
    {%- for item in add_rdsg_list_6 -%}
        ADD RDSG:
        {#- --- 必选参数 --- -#}
        RLOCID={{item.RLOCID}},
        RDSGMID={{item.RDSGMID}},
        RDSGST="{{item.RDSGST}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RDSGTYPE is not none -%}
            RDSGTYPE={{item.RDSGTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### **裸机容器**：

```jinja2
{%- if is_scenario_bare_metal_container -%}
    {%- for item in add_rdsg_list_10 -%}
        ADD RDSG:
        {#- --- 必选参数 --- -#}
        RLOCID={{item.RLOCID}},
        RDSGMID={{item.RDSGMID}},
        RDSGST="{{item.RDSGST}}",
        {#- --- 可选参数 --- -#}
        {%- if item.RDSGTYPE is not none -%}
            RDSGTYPE={{item.RDSGTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加远端网元IP地址。

### DC1:

```jinja2
{%- for item in add_ripaddr_list -%}
    ADD RIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    RDPUST="{{item.RDPUST}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_ripaddr_list_2 -%}
    ADD RIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    RDPUST="{{item.RDPUST}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加PGW订阅通知配置。操作员通过PGW修改全局数据或用户数据后，PGW负责通知FE相关的修改内容。

### DC1:

```jinja2
{%- for item in add_notifycfg_list -%}
    ADD NOTIFYCFG:
    {#- --- 必选参数 --- -#}
    FETYPE="{{item.FETYPE}}",
    FEID={{item.FEID}},
    INFTYPE={{item.INFTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4/IPV6 时可选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI/THIRDPARTY 时可选 --- -#}
    {%- elif item.INFTYPE in ['MCI', 'THIRDPARTY'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI 时可选 --- -#}
    {%- if item.INFTYPE == 'MCI' -%}
        {%- if item.LOCATIONID is not none -%}
            LOCATIONID={{item.LOCATIONID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI 时可选 --- -#}
    {%- if item.INFTYPE == 'MCI' -%}
        {%- if item.NOTIFYDEST is not none -%}
            NOTIFYDEST={{item.NOTIFYDEST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_notifycfg_list_1 -%}
    ADD NOTIFYCFG:
    {#- --- 必选参数 --- -#}
    FETYPE="{{item.FETYPE}}",
    FEID={{item.FEID}},
    INFTYPE={{item.INFTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4/IPV6 时可选 --- -#}
    {%- if item.IPVER in ['IPV4', 'IPV6'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI/THIRDPARTY 时可选 --- -#}
    {%- elif item.INFTYPE in ['MCI', 'THIRDPARTY'] -%}
        {%- if item.SYNCHROSWITCH is not none -%}
            SYNCHROSWITCH={{item.SYNCHROSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI 时可选 --- -#}
    {%- if item.INFTYPE == 'MCI' -%}
        {%- if item.LOCATIONID is not none -%}
            LOCATIONID={{item.LOCATIONID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INFTYPE=MCI 时可选 --- -#}
    {%- if item.INFTYPE == 'MCI' -%}
        {%- if item.NOTIFYDEST is not none -%}
            NOTIFYDEST={{item.NOTIFYDEST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 登录“UEG MML命令”界面。

### 8~11用于配置PCF/PCRF与USCDB对接。容灾组网中，同一UEG内的FE和BE对接，不同UEG内不交叉对接。

### 如已完成园区UDM的配置，则不需要重复配置8~9，请跳转到10。

### 8 设置DBS分组开关。

```jinja2
{%- for item in set_dbsgrpswitch_list -%}
    SET DBSGRPSWITCH:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    GROUPSWITCH={{item.GROUPSWITCH}},
    ;
{%- endfor -%}
```

### 9 增加远端Location信息。

### DC1:

```jinja2
{%- for item in add_dbsrlocation_list -%}
    ADD DBSRLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT={{item.RMT}},
    LP={{item.LP}},
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_dbsrlocation_list_1 -%}
    ADD DBSRLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT={{item.RMT}},
    LP={{item.LP}},
    ;
{%- endfor -%}
```

### 10 增加远端DSG。

### 在“MML-USCDB”下使用“LST MODULE: MT=DSG;”查询参数“RDSGMID”的值，需要将查询出来的所有DSG模块号配置在此处。如下以查询到DSG模块号为1017、1018、1019和1020为例。

### DC1:

```jinja2
{%- for item in add_dbsrdsg_list -%}
    ADD DBSRDSG:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RDSGMID={{item.RDSGMID}},
    {#- --- 可选参数 --- -#}
    {%- if item.RDSGST is not none -%}
        RDSGST="{{item.RDSGST}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_dbsrdsg_list_4 -%}
    ADD DBSRDSG:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RDSGMID={{item.RDSGMID}},
    {#- --- 可选参数 --- -#}
    {%- if item.RDSGST is not none -%}
        RDSGST="{{item.RDSGST}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 增加远端网元IP地址。

### DC1:

```jinja2
{%- for item in add_dbsripaddr_list -%}
    ADD DBSRIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.RIPST is not none -%}
        RIPST="{{item.RIPST}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### DC2:

```jinja2
{%- for item in add_dbsripaddr_list_2 -%}
    ADD DBSRIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.RIPST is not none -%}
        RIPST="{{item.RIPST}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 12 登录“USCDB MML命令”界面。执行如下命令，激活IP链路。

```jinja2
ACT IPDISP:
;
```

### 13 登录“UEG MML命令”界面。执行如下命令，激活IP链路。

```jinja2
ACT DBSIPDISP:
;
```

