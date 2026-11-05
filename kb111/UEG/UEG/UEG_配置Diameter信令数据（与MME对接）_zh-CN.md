---
id: ''
name: 配置Diameter信令数据（与MME对接）
ne_type: UEG
type: feature
description: 接入4G/5G NSA用户时，Diameter信令数据用于EPC HSS和MME对接。  HSS（UDM）通过Diameter信令与对端网元（如MME）互通时，需要配置该页面。  HSS（UDM）和MME直联对接，即不通过DRA设备。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置UDM/HSS","配置Diameter信令数据（与MME对接）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
接入4G/5G NSA用户时，Diameter信令数据用于EPC HSS和MME对接。HSS（UDM）通过Diameter信令与对端网元（如MME）互通时，需要配置该页面。HSS（UDM）和MME直联对接，即不通过DRA设备。

## 必备事项
前提条件

* 已完成配置UDM基础数据。
* HSS（UDM）和MME之间外联口通信正常。
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
          description: 'Diameter本端设备信息。  双DC场景，两个DC中的主机名不能相同。'
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
          description: 'Diameter对端设备信息。'
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_dmpe_list_1:
      type: items
      properties:
        EN:
          name: '实体名称'
          type: string
          maxLength: 127
          required: true
          description: 'Diameter对端设备信息。'
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
          data_source: '与对端协商'
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
          description: '同一HSS网元上不能重复。  链路集Diameter01用于和MME01互连，链路集Diameter02用于和MME02互连。'
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
          description: 'ACTIVE：从第0条开始选择第一条激活的链路来工作。当该链路不可用时，则向后选择下一条激活链路。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dmlks_list_1:
      type: items
      properties:
        LINKSNAM:
          name: '链路集名称'
          type: string
          maxLength: 127
          required: true
          description: '同一HSS网元上不能重复。  链路集Diameter01用于和MME01互连，链路集Diameter02用于和MME02互连。'
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
          description: 'ACTIVE：从第0条开始选择第一条激活的链路来工作。当该链路不可用时，则向后选择下一条激活链路。'
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_1:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_2:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_3:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_4:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_5:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    add_dmlnk_list_7:
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
          description: '采用表3中的IP地址名称。'
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
          description: 'MME上的S6a接口IP。'
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
          description: 'MME上的S6a接口IP。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '不配置时，HSS不验证MME的端口号。'
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
    - EN: 'HSS01'
      LOCTYPE: SAE-HSS
      DN: 'huawei.com'
      HN: 'HSS01.huawei.com'
    - EN: 'HSS02'
      LOCTYPE: SAE-HSS
      DN: 'huawei.com'
      HN: 'HSS02.huawei.com'
    add_dmpe_list:
    - EN: 'MME01'
      PEERTYPE: OTHER
      HN: 'MME01.huawei.com'
    - EN: 'MME02'
      PEERTYPE: OTHER
      HN: 'MME02.huawei.com'
    add_dmpe_list_1:
    - EN: 'MME02'
      PEERTYPE: OTHER
      HN: 'MME02.huawei.com'
    - EN: 'MME01'
      PEERTYPE: OTHER
      HN: 'MME01.huawei.com'
    add_dmlks_list:
    - LINKSNAM: 'Diameter01'
      LOCALNAM: 'HSS01'
      PEERNAM: 'MME01'
      LNKMOD: ACTIVE
    - LINKSNAM: 'Diameter02'
      LOCALNAM: 'HSS02'
      PEERNAM: 'MME02'
      LNKMOD: ACTIVE
    add_dmlks_list_1:
    - LINKSNAM: 'Diameter02'
      LOCALNAM: 'HSS01'
      PEERNAM: 'MME02'
      LNKMOD: ACTIVE
    - LINKSNAM: 'Diameter01'
      LOCALNAM: 'HSS02'
      PEERNAM: 'MME01'
      LNKMOD: ACTIVE
    add_dmlnk_list:
    - LNKNAME: 'DMlink01'
      LINKSNAM: 'Diameter01'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP1'
      IPNAM2: 'HSFIP2'
      LPT: 5000
      PIPVER: IPV4
      PIPV4: '10.200.200.58'
      SPIPVER: IPV4
      SPIPV4: '10.200.200.59'
      PPT: 5000
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_1:
    - LNKNAME: 'DMlink02'
      LINKSNAM: 'Diameter01'
      HSFMID: 204
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP2'
      IPNAM2: 'HSFIP1'
      LPT: 5001
      PIPVER: IPV4
      PIPV4: '10.200.200.59'
      SPIPVER: IPV4
      SPIPV4: '10.200.200.58'
      PPT: 5001
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_2:
    - LNKNAME: 'DMlink03'
      LINKSNAM: 'Diameter02'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP1'
      IPNAM2: 'HSFIP2'
      LPT: 5000
      PIPVER: IPV4
      PIPV4: '10.201.200.58'
      SPIPVER: IPV4
      SPIPV4: '10.201.200.59'
      PPT: 5000
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_3:
    - LNKNAME: 'DMlink04'
      LINKSNAM: 'Diameter02'
      HSFMID: 204
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP2'
      IPNAM2: 'HSFIP1'
      LPT: 5001
      PIPVER: IPV4
      PIPV4: '10.201.200.59'
      SPIPVER: IPV4
      SPIPV4: '10.201.200.58'
      PPT: 5001
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_4:
    - LNKNAME: 'DMlink03'
      LINKSNAM: 'Diameter02'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP1'
      IPNAM2: 'HSFIP2'
      LPT: 5000
      PIPVER: IPV4
      PIPV4: '10.201.200.58'
      SPIPVER: IPV4
      SPIPV4: '10.201.200.59'
      PPT: 5000
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_5:
    - LNKNAME: 'DMlink04'
      LINKSNAM: 'Diameter02'
      HSFMID: 204
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP2'
      IPNAM2: 'HSFIP1'
      LPT: 5001
      PIPVER: IPV4
      PIPV4: '10.201.200.59'
      SPIPVER: IPV4
      SPIPV4: '10.201.200.58'
      PPT: 5001
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_6:
    - LNKNAME: 'DMlink01'
      LINKSNAM: 'Diameter01'
      HSFMID: 201
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP1'
      IPNAM2: 'HSFIP2'
      LPT: 5000
      PIPVER: IPV4
      PIPV4: '10.200.200.58'
      SPIPVER: IPV4
      SPIPV4: '10.200.200.59'
      PPT: 5000
      LINKPRI: 15
      CROSSPATHFLAG: NO
    add_dmlnk_list_7:
    - LNKNAME: 'DMlink02'
      LINKSNAM: 'Diameter01'
      HSFMID: 204
      PTYPE: SCTP
      WMODE: SERVER
      IPNAM1: 'HSFIP2'
      IPNAM2: 'HSFIP1'
      LPT: 5001
      PIPVER: IPV4
      PIPV4: '10.200.200.59'
      SPIPVER: IPV4
      SPIPV4: '10.200.200.58'
      PPT: 5001
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

#### 3.1 //DC1：

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
    ;
{%- endfor -%}
```

#### 3.2 //UEG负荷分担模式容灾组网时需要配置：

```jinja2
{%- if is_scenario_ueg_load_sharing -%}
    {%- for item in add_dmpe_list_1 -%}
        ADD DMPE:
        {#- --- 必选参数 --- -#}
        EN="{{item.EN}}",
        HN="{{item.HN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PEERTYPE is not none -%}
            PEERTYPE={{item.PEERTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 增加Diameter链路集。

#### 4.1 //DC1：

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

#### 4.2 //UEG负荷分担模式容灾组网时需要配置：

```jinja2
{%- if is_scenario_ueg_load_sharing -%}
    {%- for item in add_dmlks_list_1 -%}
        ADD DMLKS:
        {#- --- 必选参数 --- -#}
        LINKSNAM="{{item.LINKSNAM}}",
        LOCALNAM="{{item.LOCALNAM}}",
        PEERNAM="{{item.PEERNAM}}",
        LNKMOD={{item.LNKMOD}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加Diameter链路。

### 当UEG在煤矿等场景下使用2U1选型时，无需配置以下“DMlink02”和“DMlink04”链路。

#### 5.1 //DC1：

##### 5.1.1 //MME01:

```jinja2
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
```

```jinja2
{%- if is_scenario_non_2u1 -%}
    {%- for item in add_dmlnk_list_1 -%}
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

#### 5.2 //UEG负荷分担模式容灾组网时需要配置：

##### 5.2.1 //MME02:

```jinja2
{%- if is_scenario_ueg_load_sharing -%}
    {%- for item in add_dmlnk_list_2 -%}
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

```jinja2
{%- if is_scenario_ueg_load_sharing and is_scenario_non_2u1 -%}
    {%- for item in add_dmlnk_list_3 -%}
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

#### 5.3 //DC2：

##### 5.3.1 //MME02:

```jinja2
{%- for item in add_dmlnk_list_4 -%}
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
```

```jinja2
{%- if is_scenario_non_2u1 -%}
    {%- for item in add_dmlnk_list_5 -%}
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

#### 5.4 //UEG负荷分担模式容灾组网时需要配置：

##### 5.4.1 //MME01:

```jinja2
{%- if is_scenario_ueg_load_sharing -%}
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

```jinja2
{%- if is_scenario_ueg_load_sharing and is_scenario_non_2u1 -%}
    {%- for item in add_dmlnk_list_7 -%}
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

##### 链路增加后会自动激活，但是如果对链路进行了修改，则需要使用**DEA DMLNK**命令去激活链路，再使用**ACT DMLNK**命令激活链路。

