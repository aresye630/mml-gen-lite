---
id: ''
name: 配置Diameter信令数据（与I-CSCF/S-CSCF/ATS对接）
ne_type: UEG
type: feature
description: 接入4G/5G NSA用户并部署语音业务时，Diameter信令数据用于IMS-HSS和I-CSCF/S-CSCF/AS对接。  HSS（UDM）通过Diameter信令与对端网元（如I-CSCF/S-CSCF/AS）互通时，需要配置该页面。  HSS（UDM）和I-CSCF/S-CSCF/AS直联对接，即不通过DRA设备。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置UDM/HSS","配置Diameter信令数据（与I-CSCF/S-CSCF/ATS对接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
接入4G/5G NSA用户并部署语音业务时，Diameter信令数据用于IMS-HSS和I-CSCF/S-CSCF/AS对接。HSS（UDM）通过Diameter信令与对端网元（如I-CSCF/S-CSCF/AS）互通时，需要配置该页面。HSS（UDM）和I-CSCF/S-CSCF/AS直联对接，即不通过DRA设备。

## 必备事项
前提条件

* 已完成配置UDM基础数据。
* HSS（UDM）和I-CSCF/S-CSCF/AS之间外联口通信正常。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_dmle_list:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: 'Diameter本端设备信息。  此处主机名与配置Diameter信令数据（与MME对接）中**ADD DMLE**命令配置的主机名不能相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCTYPE:
          name: '本端设备类型'
          type: string
          enum:
          - IMS-HSS
          - IMS-SLF
          - SAE-HSS
          - UEIR
          - LRF
          - IWF
          - IWF-EIR
          - AAA
          - BSF
          - AP
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_dmpe_list:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: 'Diameter对端设备信息。语音业务中，IMS-HSS需要与I-CSCF/S-CSCF/AS对接。此处以对端主备提供不同的业务IP为例。  对端主备提供不同的业务IP时，可通过“Diameter对端实体优先级（PEPRI）”设置对接设备的优先级。  此处配置的主机名需要与对端一致，否则建链失败。  对接UCN时，可通过**LST ICSCF**/**LST SCSCF**/**LST ATS**分别获取I-CSCF/S-CSCF/AS的主机名。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          enum:
          - OTHER
          - AS
          - S-CSCF
          - I-CSCF
          - GGSN
          - SAE
          - BSF
          - IMS-HSS
          - E-CSCF
          - P-GW
          - ePDG
          - HSGW
          - Non-3GPP
          - AP
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: OTHER
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PEPRI:
          name: 'Diameter对端实体优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '取值越小优先级越高。'
          data_source: '与对端协商'
          pattern: ''
          default: 15
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dmpecap_list:
      type: items
      properties:
        PEERNAME:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMPE**命令中的实体名称。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PEERTYPE:
          name: 'Diameter对端实体类型'
          type: string
          enum:
          - OTHER
          - AS
          - S-CSCF
          - I-CSCF
          - GGSN
          - SAE
          - BSF
          - IMS-HSS
          - E-CSCF
          - P-GW
          - ePDG
          - HSGW
          - Non-3GPP
          - AP
          required: true
          description: '采用**ADD DMPE**命令中的Diameter对端实体类型。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        CSCFFEATURELIST:
          name: 'Cx特性列表'
          type: string
          required: false
          description: '用于设置对端CSCF支持的特性列表。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        HN:
          name: '主机名'
          type: string
          maxLength: 127
          required: false
          description: '采用**ADD DMPE**命令中的主机名。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PR:
          name: '允许Sh-pull的数据类型'
          type: string
          required: false
          description: '该参数用于标识AS从IMS-HSS上获取指定数据的权限。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        UR:
          name: '允许Sh-update的数据类型'
          type: string
          required: false
          description: '该参数用于标识AS从IMS-HSS上更新指定数据的权限。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        NR:
          name: '允许Sh-sub-notify的数据类型'
          type: string
          required: false
          description: '该参数用于标识AS从IMS-HSS上订阅指定数据的权限。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ASFEATURELIST:
          name: 'Sh特性列表'
          type: string
          required: false
          description: '用于设置对端AS支持的特性列表。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        DN:
          name: '域名'
          type: string
          maxLength: 127
          required: false
          description: '采用**ADD DMPE**命令中的域名。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    set_hsystempara_list:
      type: items
      properties:
        ASIDMODE:
          name: 'ASID管理方式'
          type: string
          required: false
          description: '取值为“STORE\_IN\_USCDB”时，使用的是**ADD HASHOST**定义的“ASID”。否则使用系统自动生成的ASID。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_hashost_list:
      type: items
      properties:
        ASID:
          name: 'ASID'
          type: string
          required: false
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          required: false
          description: '对接的AS的主机名和域名。可通过**LST DMPE**命令查询。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        REALMNAME:
          name: '域名'
          type: string
          required: false
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_dmlks_list:
      type: items
      properties:
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALNAM:
          name: 'Diameter本端实体名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLE**定义的实体名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PEERNAM:
          name: 'Diameter对端实体名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMPE**定义的实体名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LNKMOD:
          name: '链路选择模式'
          type: string
          enum:
          - SESSIONIDBASED
          - POLLING
          - AORS
          - ACTIVE
          - ACTIVEWITHPRI
          - POLLINGWITHPRI
          required: true
          description: 'POLLING：对Diameter对端实体下的所有链路轮流选择，即在可用链路之间循环选择。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dmlnk_list:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPNAM2:
          name: 'IP地址名称2'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        SPIPVER:
          name: '对端备用IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SPIPV4:
          name: '对端备用IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    add_dmlnk_list_6:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPNAM2:
          name: 'IP地址名称2'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        SPIPVER:
          name: '对端备用IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SPIPV4:
          name: '对端备用IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    add_dmlnk_list_12:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    add_dmlnk_list_24:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    mod_diampp_list:
      type: items
      properties:
        DIAMPN:
          name: 'Diameter协议参数名称'
          type: string
          enum:
          - MAXPRQLEN
          - MAXDDQLEN
          - PRQTIMERVAL
          - DDQTIMERVAL
          - DDQAPPTIMERVAL
          - INBANDSECURITYID
          - FIRMWAREREVISION
          - CONNDETACHTIMER
          - CONNDETACHNUM
          - DIAMSENDLOWERBUFF
          - LINKPERF
          - USEBSGIP
          - SPTVENDIDINCER
          - TOOBUSYTIMER
          - NOTRELAYMSGTODRA
          - CHECKIMSLINKPORT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIAMPV:
          name: 'Diameter协议参数值'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmlnk_list_36:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    add_dmlnk_list_48:
      type: items
      properties:
        LNKNAME:
          name: '链路名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LINKSNAM:
          name: 'Diameter链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '采用**ADD DMLKS**定义的链路集名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HSFMID:
          name: 'HSF模块号'
          type: integer
          minimum: 1
          maximum: 1023
          required: false
          description: '使用**LST MODULE**命令查询获取FE的HSF模块号。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - SCTP
          - TCP
          - UDP
          required: true
          description: '此处以SCTP方式为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WMODE:
          name: '工作模式'
          type: string
          enum:
          - CLIENT
          - SERVER
          - SERVERMULTPORT
          required: true
          description: '此处以HSS在当前链路中作为服务器端为例。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPNAM1:
          name: 'IP地址名称1'
          type: string
          maxLength: 127
          required: true
          description: '采用表4中的IP地址名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LPT:
          name: '本端端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: '默认是3868，请根据实际规划修改。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIPVER:
          name: '对端IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIPV4:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对接的I-CSCF/S-CSCF/AS的Diamter IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证I-CSCF/S-CSCF/AS的端口号。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        LINKPRI:
          name: 'Diameter对端链路优先级'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '值越小，优先级越高。HSS和对端间发送消息时，优先选择优先级高的。'
          data_source: '本端规划'
          pattern: ''
          default: 15
        CROSSPATHFLAG:
          name: '交叉路径是否可用'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '不使用SCTP交叉路径。'
          data_source: '固定取值'
          pattern: ''
          default: NO
  examples:
    add_dmle_list:
    - EN: 'HSS03'
      LOCTYPE: IMS-HSS
      DN: 'ucn.3gppnetwork.org'
      HN: 'imshss1.ucn.3gppnetwork.org'
    - EN: 'HSS04'
      LOCTYPE: IMS-HSS
      DN: 'ucn.3gppnetwork.org'
      HN: 'imshss2.ucn.3gppnetwork.org'
    add_dmpe_list:
    - EN: 'I-CSCF01'
      PEERTYPE: I-CSCF
      HN: 'icscf01.ucn.3gppnetwork.org'
      PEPRI: 15
      DN: 'ucn.3gppnetwork.org'
    set_dmpecap_list:
    - PEERNAME: 'I-CSCF01'
      PEERTYPE: I-CSCF
      CSCFFEATURELIST: SharedIFC-1&AliasInd-1&CscfDisaster-1
      HN: 'icscf01.ucn.3gppnetwork.org'
      PR: REPOSITORYDATA-1&IMSPUBLICIDENTITY-1&IMSUSERSTATE-1&SCSCFNAME-1&IFC-1&LOCATIONINFORMATION-1&USERSTATE-1&CHARGINGINFORMATION-1&MSISDN-1&PSIACTIVATION-1&ALIASREPOSITORY-1&SMSREGISTRATIONINFO-1&TADSINFORMATION-1&STN_SR-1&UESRVCCCAPABILITY-1&CSRN-1&REFERENSELOCATIONINFORMAION-1&IMSI-1&IPADDRSECUREBINDINGINFOR-1&IMSPRIVATEUSERIDENTITY-1
      UR: REPOSITORYDATA-1&PSIACTIVATION-1&ALIASREPOSITORY-1&SMSREGISTRATIONINFO-1&STN_SR-1
      NR: REPOSITORYDATA-1&IMSUSERSTATE-1&SCSCFNAME-1&IFC-1&PSIACTIVATION-1&ALIASREPOSITORY-1&IMSPUBLICIDENTITY-1&UEREACHABILITYFORIP-1&UESRVCCCAPABILITY-1&CHARGINGINFORMATION-1&IPADDRSECUREBINDINGINFOR-1&IMSPRIVATEUSERIDENTITY-1
      ASFEATURELIST: Notif-Eff-1
      DN: 'ucn.3gppnetwork.org'
    set_hsystempara_list:
    - ASIDMODE: STORE_IN_USCDB
    add_hashost_list:
    - ASID: '0'
      HOSTNAME: as01.ucn.3gppnetwork.org
      REALMNAME: ucn.3gppnetwork.org
    add_dmlks_list:
    - LINKSNAM: 'Diameter10'
      LOCALNAM: 'HSS03'
      PEERNAM: 'I-CSCF01'
      LNKMOD: POLLING
    - LINKSNAM: 'Diameter10'
      LOCALNAM: 'HSS04'
      PEERNAM: 'I-CSCF01'
      LNKMOD: POLLING
    add_dmlnk_list:
    - LNKNAME: 'DMlink05'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.19'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink07'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.21'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink09'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.35'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_6:
    - LNKNAME: 'DMlink05'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.19'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink07'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.21'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink09'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      IPNAM2: 'HSFIP12'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      SPIPVER: IPV4
      SPIPV4: '172.16.100.35'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_12:
    - LNKNAME: 'DMlink105'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink205'
      LINKSNAM: 'Diameter11'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.118'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink107'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink207'
      LINKSNAM: 'Diameter13'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.120'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink109'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink209'
      LINKSNAM: 'Diameter15'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.134'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_24:
    - LNKNAME: 'DMlink105'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink205'
      LINKSNAM: 'Diameter11'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.118'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink107'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink207'
      LINKSNAM: 'Diameter13'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.120'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink109'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink209'
      LINKSNAM: 'Diameter15'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.134'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    mod_diampp_list:
    - DIAMPN: CHECKIMSLINKPORT
      DIAMPV: 0
    - DIAMPN: CHECKIMSLINKPORT
      DIAMPV: 0
    add_dmlnk_list_36:
    - LNKNAME: 'DMlink105'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink205'
      LINKSNAM: 'Diameter11'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.118'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink107'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink207'
      LINKSNAM: 'Diameter13'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.120'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink109'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink209'
      LINKSNAM: 'Diameter15'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.134'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_48:
    - LNKNAME: 'DMlink105'
      LINKSNAM: 'Diameter10'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.18'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink205'
      LINKSNAM: 'Diameter11'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.118'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink107'
      LINKSNAM: 'Diameter12'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.20'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink207'
      LINKSNAM: 'Diameter13'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.120'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink109'
      LINKSNAM: 'Diameter14'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.34'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
    - LNKNAME: 'DMlink209'
      LINKSNAM: 'Diameter15'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP11'
      LPT: 3868
      PIPVER: IPV4
      PIPV4: '172.16.100.134'
      PPT: 3868
      LINKPRI: 15
      CROSSPATHFLAG: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 增加Diameter本端实体。

#### 2.1 //DC1：

```jinja2
{%- for item in add_dmle_list -%}
    ADD DMLE:
    {#- --- 必选参数 --- -#}
    EN="{{item.EN}}",
    LOCTYPE={{item.LOCTYPE}},
    DN="{{item.DN}}",
    HN="{{item.HN}}",
    ;
{%- endfor -%}
```

### 3 增加Diameter对端实体。

```jinja2
{%- for item in add_dmpe_list -%}
    ADD DMPE:
    {#- --- 必选参数 --- -#}
    EN="{{item.EN}}",
    HN="{{item.HN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PEERTYPE is not none -%}
        PEERTYPE={{item.PEERTYPE}},
    {%- endif -%}
    {%- if item.PEPRI is not none -%}
        PEPRI={{item.PEPRI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERTYPE=AS/SAE/IMS-HSS 时必选 --- -#}
    {%- if item.PEERTYPE in ['AS', 'SAE', 'IMS-HSS'] -%}
        DN="{{item.DN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置对端实体能力。

```jinja2
{%- for item in set_dmpecap_list -%}
    SET DMPECAP:
    {#- --- 必选参数 --- -#}
    PEERNAME="{{item.PEERNAME}}",
    PEERTYPE={{item.PEERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.HN is not none -%}
        HN="{{item.HN}}",
    {%- endif -%}
    {%- if item.DN is not none -%}
        DN="{{item.DN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PEERTYPE=S-CSCF/I-CSCF 时必选 --- -#}
    {%- if item.PEERTYPE in ['S-CSCF', 'I-CSCF'] -%}
        CSCFFEATURELIST={{item.CSCFFEATURELIST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.PR is not none -%}
            PR={{item.PR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.UR is not none -%}
            UR={{item.UR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.NR is not none -%}
            NR={{item.NR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PEERTYPE=AS 时可选 --- -#}
    {%- if item.PEERTYPE == 'AS' -%}
        {%- if item.ASFEATURELIST is not none -%}
            ASFEATURELIST={{item.ASFEATURELIST}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 与AS对接时，配置“ASID”与对接AS数据的绑定关系。

#### 5.1 登录PGW Web LMT MML命令界面。

#### 5.2 设置“ASID管理方式”为“STORE\_IN\_USCDB”。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_hsystempara_list的变量区（command: SET HSYSTEMPARA） -#}
<!-- MISSING_MACRO: command=SET HSYSTEMPARA list_name=set_hsystempara_list step_id=5.2 -->
```

#### 5.3 配置ASID与对接AS数据的绑定关系。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_hashost_list的变量区（command: ADD HASHOST） -#}
<!-- MISSING_MACRO: command=ADD HASHOST list_name=add_hashost_list step_id=5.3 -->
```

### 6 增加Diameter链路集。

#### 6.1 //DC1：

```jinja2
{%- for item in add_dmlks_list -%}
    ADD DMLKS:
    {#- --- 必选参数 --- -#}
    LINKSNAM="{{item.LINKSNAM}}",
    LOCALNAM="{{item.LOCALNAM}}",
    PEERNAM="{{item.PEERNAM}}",
    LNKMOD={{item.LNKMOD}},
    ;
{%- endfor -%}
```

### 一号通专网煤矿场景，请执行7。

### 一号通专网核电场景，请执行8。

### 一号通专网通用场景，清执行9。

### 7 一号通专网煤矿场景，增加Diameter链路。

#### 7.1 //DC1：

##### 7.1.1 //I-CSCF:

```jinja2
{%- if is_scenario_coal_mine -%}
    {%- for item in add_dmlnk_list -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.IPNAM2 is not none -%}
                IPNAM2="{{item.IPNAM2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.SPIPVER is not none -%}
                SPIPVER={{item.SPIPVER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPIPVER=IPV4 时可选 --- -#}
        {%- if item.SPIPVER == 'IPV4' -%}
            {%- if item.SPIPV4 is not none -%}
                SPIPV4="{{item.SPIPV4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 //DC2：

##### 7.2.1 //I-CSCF:

```jinja2
{%- if is_scenario_coal_mine -%}
    {%- for item in add_dmlnk_list_6 -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.IPNAM2 is not none -%}
                IPNAM2="{{item.IPNAM2}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.SPIPVER is not none -%}
                SPIPVER={{item.SPIPVER}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SPIPVER=IPV4 时可选 --- -#}
        {%- if item.SPIPVER == 'IPV4' -%}
            {%- if item.SPIPV4 is not none -%}
                SPIPV4="{{item.SPIPV4}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 7.2.3 链路增加后会自动激活，但是如果对链路进行了修改，则需要使用**DEA DMLNK**命令去激活链路，再使用**ACT DMLNK**命令激活链路。

### 8 一号通专网核电场景，增加Diameter链路。

#### 8.1 //DC1：

##### 8.1.1 //I-CSCF01:

```jinja2
{%- if is_scenario_nuclear_power -%}
    {%- for item in add_dmlnk_list_12 -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 //DC2：

##### 8.2.1 //I-CSCF01:

```jinja2
{%- if is_scenario_nuclear_power -%}
    {%- for item in add_dmlnk_list_24 -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 8.2.6 链路增加后会自动激活，但是如果对链路进行了修改，则需要使用**DEA DMLNK**命令去激活链路，再使用**ACT DMLNK**命令激活链路。

### 9 一号通专网通用场景，增加Diameter链路。

#### 9.1 //DC1：

```jinja2
{%- if is_scenario_general -%}
    {%- for item in mod_diampp_list -%}
        MOD DIAMPP:
        {#- --- 必选参数 --- -#}
        DIAMPN={{item.DIAMPN}},
        {#- --- 可选参数 --- -#}
        {%- if item.DIAMPV is not none -%}
            DIAMPV={{item.DIAMPV}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.1.1 //I-CSCF01:

```jinja2
{%- if is_scenario_general -%}
    {%- for item in add_dmlnk_list_36 -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 //DC2：

##### 9.2.1 //I-CSCF01:

```jinja2
{%- if is_scenario_general -%}
    {%- for item in add_dmlnk_list_48 -%}
        ADD DMLNK:
        {#- --- 必选参数 --- -#}
        LNKNAME="{{item.LNKNAME}}",
        LINKSNAM="{{item.LINKSNAM}}",
        PTYPE={{item.PTYPE}},
        WMODE={{item.WMODE}},
        IPNAM1="{{item.IPNAM1}}",
        PIPVER={{item.PIPVER}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.HSFMID is not none -%}
            HSFMID={{item.HSFMID}},
        {%- endif -%}
        {%- if item.LINKPRI is not none -%}
            LINKPRI={{item.LINKPRI}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PIPVER=IPV4 时必选 --- -#}
        {%- if item.PIPVER == 'IPV4' -%}
            PIPV4="{{item.PIPV4}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：PTYPE=SCTP 时可选 --- -#}
        {%- if item.PTYPE == 'SCTP' -%}
            {%- if item.CROSSPATHFLAG is not none -%}
                CROSSPATHFLAG={{item.CROSSPATHFLAG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件必选/可选参数 --- -#}
        {#- --- 本端端口号: 条件必选(工作模式=CLIENT|SERVERMULTPORT) / 条件可选(工作模式=SERVER) --- -#}
        {%- if (item.WMODE in ['CLIENT', 'SERVERMULTPORT']) -%}
            LPT={{item.LPT}},
        {%- elif (item.WMODE == 'SERVER') -%}
            {%- if item.LPT is not none -%}
                LPT={{item.LPT}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 9.2.6 链路增加后会自动激活，但是如果对链路进行了修改，则需要使用**DEA DMLNK**命令去激活链路，再使用**ACT DMLNK**命令激活链路。

