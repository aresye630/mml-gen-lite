---
id: ''
name: 配置PCF与AF（基于Diameter协议）的对接数据
ne_type: UEG
type: feature
description: 当PCF接纳应用层业务请求时，例如应用服务器发起的带宽资源预留请求，PCF需要对接AF（Application Function）实体，以实现应用侧发起的策略控制功能。  * 园区PCF支持语音业务，且PCF与P-CSCF（SBC）之间通过Rx接口对接时，请参考本页面进行配置。 * 园区PCF支持PTT业务，且PCF与PTT Server之间通过Rx接口对接时，请参考本页面进行配置。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置PCF/PCRF","配置PCF与AF（基于Diameter协议）的对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当PCF接纳应用层业务请求时，例如应用服务器发起的带宽资源预留请求，PCF需要对接AF（Application Function）实体，以实现应用侧发起的策略控制功能。* 园区PCF支持语音业务，且PCF与P-CSCF（SBC）之间通过Rx接口对接时，请参考本页面进行配置。* 园区PCF支持PTT业务，且PCF与PTT Server之间通过Rx接口对接时，请参考本页面进行配置。

## 必备事项
前提条件

本端及AF侧已完成基础数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_dlbvpn_list:
      type: items
      properties:
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: 'VPN名称采用**ADD L3VPNINST**定义的VPN实例名称。  如网设规划为VRF\_PS\_Signal，则请将VRF\_SBI替换成VRF\_PS\_Signal。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
    add_dlbdevaddr_list:
      type: items
      properties:
        DEVAID:
          name: '设备地址标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '网元内存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINDEX:
          name: 'VPN索引'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '本端Diameter IP，用于和AF互通。  * 双DC场景，两个DC的Diameter IP地址不能重复，如DC1用样例值，DC2用172.21.100.102等。 * 表格中未特殊说明的参数，两个DC保持一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IP:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_afabidict_list:
      type: items
      properties:
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ABILITYDICTNAME:
          name: '能力字典名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '“能力字典ID+能力字典名”唯一。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_paf_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '采用**ADD PCRF**命令定义的“PCRF标识”参数值。  可通过**LST PCRF**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AFID:
          name: '对端AF标识'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PN:
          name: '对端名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '便于快速识别是哪个AF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DN:
          name: '对端域名'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '对端AF的域名和主机名。  容灾场景两个AF对外提供的业务数据相同时，只需要规划一条数据。  容灾场景两个AF对外提供的业务数据不同时，需要规划两条数据。  此处以容灾场景两个AF对外提供的业务数据不同为例。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        HN:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PT:
          name: '协议类型'
          type: string
          enum:
          - DIAMETER
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LSMODE:
          name: '链路选择模式'
          type: string
          enum:
          - SINGLE_LINK
          - LOAD_BALANCE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOAD_BALANCE
        SBMODE:
          name: '业务绑定模式'
          type: string
          enum:
          - SINGLE
          - SHARE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SHARE
        DASWITCH:
          name: '审计开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '采用表3中定义的能力字典ID值或系统默认的能力字典ID值。可通过**LST AFABIDICT**命令查询。  此处以采用默认的能力字典ID取值“0”为例。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        SKA:
          name: '业务保活时长'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: '可使用样例值。  当对端能力有特殊要求时，需要运营商根据实际的业务场景提供。'
          data_source: '本端规划'
          pattern: ''
          default: 90@0
    add_pafl_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '采用**ADD PCRF**命令定义的“PCRF标识”参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AFID:
          name: '对端AF标识'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '存在多条记录时，该参数不能重复。  此处以一个AF提供两个IP与UEG的两个IP建立独立的SCTP链路为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LNKID:
          name: '对端链路标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISPMODE:
          name: '分发模式'
          type: string
          enum:
          - SpecialQuintuple
          - WellKnownPort
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - TCP
          - SCTP
          required: true
          description: '传输协议类型需要与AF协商，两端使用相同的传输协议类型。  此处以关闭SCTP双归属为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DUALHOME:
          name: '双归属开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIP:
          name: '本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'PCF上的Rx接口IP。  **ADD DLBDEVADDR**命令配置的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LPT:
          name: '本地侦听端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '本端PCF的端口号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIP:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端AF的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '对端AF的端口号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADSTS:
          name: '链路管理状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        LPTMODE:
          name: '本地端口模式'
          type: string
          enum:
          - WellKnownPort
          - MultiplePorts
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: MultiplePorts
        DIPVER:
          name: '双归属地址IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pafl_list_4:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '采用**ADD PCRF**命令定义的“PCRF标识”参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AFID:
          name: '对端AF标识'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '存在多条记录时，该参数不能重复。  此处以一个AF提供两个IP与UEG的两个IP建立独立的SCTP链路为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LNKID:
          name: '对端链路标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISPMODE:
          name: '分发模式'
          type: string
          enum:
          - SpecialQuintuple
          - WellKnownPort
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - TCP
          - SCTP
          required: true
          description: '传输协议类型需要与AF协商，两端使用相同的传输协议类型。  此处以关闭SCTP双归属为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DUALHOME:
          name: '双归属开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIP:
          name: '本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'PCF上的Rx接口IP。  **ADD DLBDEVADDR**命令配置的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LPT:
          name: '本地侦听端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '本端PCF的端口号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIP:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端AF的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '对端AF的端口号。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADSTS:
          name: '链路管理状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        LPTMODE:
          name: '本地端口模式'
          type: string
          enum:
          - WellKnownPort
          - MultiplePorts
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: MultiplePorts
        DIPVER:
          name: '双归属地址IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_paf_list_2:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '采用**ADD PCRF**命令定义的“PCRF标识”参数值。  可通过**LST PCRF**命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AFID:
          name: '对端AF标识'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PN:
          name: '对端名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '便于快速识别是哪个AF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DN:
          name: '对端域名'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: '对端AF的域名和主机名。  AF是P-CSCF（SBC）时，容灾场景两个P-CSCF（SBC）对外提供的业务数据相同。该场景下，只需要规划一条数据。  容灾场景两个AF对外提供的业务数据不同时，需要规划两条数据。  此处以容灾场景两个AF对外提供的业务数据不同为例。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
        HN:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '从对端获取'
          pattern: ''
          default: ''
        PT:
          name: '协议类型'
          type: string
          enum:
          - DIAMETER
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        LSMODE:
          name: '链路选择模式'
          type: string
          enum:
          - SINGLE_LINK
          - LOAD_BALANCE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: LOAD_BALANCE
        SBMODE:
          name: '业务绑定模式'
          type: string
          enum:
          - SINGLE
          - SHARE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SHARE
        DASWITCH:
          name: '审计开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: true
          description: '采用表3中定义的能力字典ID值或系统默认的能力字典ID值。可通过**LST AFABIDICT**命令查询。  此处以采用默认的能力字典ID取值“0”为例。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        SKA:
          name: '业务保活时长'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: '可使用样例值。  当对端能力有特殊要求时，需要运营商根据实际的业务场景提供。'
          data_source: '本端规划'
          pattern: ''
          default: 90@0
    add_pafl_list_8:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: '采用**ADD PCRF**命令定义的“PCRF标识”参数值。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        AFID:
          name: '对端AF标识'
          type: integer
          minimum: 0
          maximum: 15
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LNKID:
          name: '对端链路标识'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '存在多条记录时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DISPMODE:
          name: '分发模式'
          type: string
          enum:
          - SpecialQuintuple
          - WellKnownPort
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TPTYPE:
          name: '传输协议类型'
          type: string
          enum:
          - TCP
          - SCTP
          required: true
          description: '此处以SCTP双归属，不使能交叉路径为例。即：和某一对端AF之间，存在两条平行路径，两条路径的IP地址不重复。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DUALHOME:
          name: '双归属开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CROSSPATH:
          name: '交叉路径'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ON
        DIPVER:
          name: '双归属地址IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DLIP:
          name: '双归属本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '**ADD DLBDEVADDR**命令配置的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIP:
          name: '本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LPT:
          name: '本地侦听端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DPIP:
          name: '双归属对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '对端AF的IP地址。  172.16.100.3和172.16.100.2是af0的IP，172.16.100.103和172.16.100.102是af1的IP。  af0和af1对外提供的IP地址相同时，只需要规划一条数据。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PIP:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADSTS:
          name: '链路管理状态'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        LPTMODE:
          name: '本地端口模式'
          type: string
          enum:
          - WellKnownPort
          - MultiplePorts
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: MultiplePorts
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_dlbvpn_list:
    - VPNINDEX: 4
      VPNNAME: 'VRF_AF'
    - VPNINDEX: 4
      VPNNAME: 'VRF_AF'
    add_dlbdevaddr_list:
    - DEVAID: 4
      VPNINDEX: 4
      IPVER: IPV4
      IP: '172.21.100.2'
    - DEVAID: 4
      VPNINDEX: 4
      IPVER: IPV4
      IP: '172.21.100.102'
    add_afabidict_list:
    - ABILITYDICTID: 88
      ABILITYDICTNAME: 'AF00'
    add_paf_list:
    - PCRFID: 1
      AFID: 0
      PN: 'af0'
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcscf01.ucn.3gppnetwork.org'
      PT: DIAMETER
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: OFF
      ABILITYDICTID: 0
      SKA: 90
    - PCRFID: 1
      AFID: 1
      PN: 'af1'
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcscf03.ucn.3gppnetwork.org'
      PT: DIAMETER
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: OFF
      ABILITYDICTID: 0
      SKA: 90
    add_pafl_list:
    - PCRFID: 1
      AFID: 0
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: OFF
      IPVER: IPV4
      LIP: '172.21.100.2'
      LPT: 3868
      PIP: '172.16.100.2'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DIPVER: ''
    - PCRFID: 1
      AFID: 1
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: OFF
      IPVER: IPV4
      LIP: '172.21.100.2'
      LPT: 3868
      PIP: '172.16.100.102'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DIPVER: ''
    add_pafl_list_4:
    - PCRFID: 1
      AFID: 0
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: OFF
      IPVER: IPV4
      LIP: '172.21.100.102'
      LPT: 3868
      PIP: '172.16.100.2'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DIPVER: ''
    - PCRFID: 1
      AFID: 1
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: OFF
      IPVER: IPV4
      LIP: '172.21.100.102'
      LPT: 3868
      PIP: '172.16.100.102'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DIPVER: ''
    add_paf_list_2:
    - PCRFID: 1
      AFID: 0
      PN: 'af0'
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcscf01.ucn.3gppnetwork.org'
      PT: DIAMETER
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: OFF
      ABILITYDICTID: 0
      SKA: 90
    - PCRFID: 1
      AFID: 0
      PN: 'af0'
      DN: 'ucn.3gppnetwork.org'
      HN: 'pcscf02.ucn.3gppnetwork.org'
      PT: DIAMETER
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: OFF
      ABILITYDICTID: 0
      SKA: 90
    add_pafl_list_8:
    - PCRFID: 1
      AFID: 0
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: ON
      CROSSPATH: OFF
      DIPVER: IPV4
      DLIP: '172.21.100.3'
      LIP: '172.21.100.2'
      LPT: 3868
      DPIP: '172.16.100.3'
      PIP: '172.16.100.2'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      IPVER: ''
    - PCRFID: 1
      AFID: 0
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: SCTP
      DUALHOME: ON
      CROSSPATH: OFF
      DIPVER: IPV4
      DLIP: '172.21.100.103'
      LIP: '172.21.100.102'
      LPT: 3868
      DPIP: '172.16.100.3'
      PIP: '172.16.100.2'
      PPT: 3868
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      IPVER: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 配置Diameter信令IP，用于和AF（基于Diameter协议）通信。如已完成配置PCF基础数据中的和AF（基于Diameter协议）互通的Diameter信令IP数据， 则不需要重复配置。

#### 2.1 //DC1：

```jinja2
{%- for item in add_dlbvpn_list -%}
    ADD DLBVPN:
    {#- --- 必选参数 --- -#}
    VPNINDEX={{item.VPNINDEX}},
    VPNNAME="{{item.VPNNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_dlbdevaddr_list -%}
    ADD DLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNINDEX={{item.VPNINDEX}},
    IPVER={{item.IPVER}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 默认的能力字典不满足要求时，配置对端AF能力字典。

```jinja2
{%- for item in add_afabidict_list -%}
    ADD AFABIDICT:
    {#- --- 必选参数 --- -#}
    ABILITYDICTID={{item.ABILITYDICTID}},
    ABILITYDICTNAME="{{item.ABILITYDICTNAME}}",
    ;
{%- endfor -%}
```

#### 3.1 规划关闭SCTP双归属时，执行4和5。

#### 如下以容灾的两个AF对外提供的业务数据不同为例。

#### 3.2 规划开启SCTP双归属时，请执行6和7。

#### 如下以容灾的两个AF对外提供的业务数据不同为例。

### 4 增加对端AF实体。关闭SCTP双归属时需要执行本步骤。

#### 4.1 //af0

```jinja2
{%- if is_scenario_sctp_dual_home_off -%}
    {%- for item in add_paf_list -%}
        ADD PAF:
        {#- --- 必选参数 --- -#}
        PCRFID={{item.PCRFID}},
        AFID={{item.AFID}},
        DN="{{item.DN}}",
        HN="{{item.HN}}",
        PT={{item.PT}},
        ABILITYDICTID={{item.ABILITYDICTID}},
        {#- --- 可选参数 --- -#}
        {%- if item.PN is not none -%}
            PN="{{item.PN}}",
        {%- endif -%}
        {%- if item.LSMODE is not none -%}
            LSMODE={{item.LSMODE}},
        {%- endif -%}
        {%- if item.SBMODE is not none -%}
            SBMODE={{item.SBMODE}},
        {%- endif -%}
        {%- if item.SKA is not none -%}
            SKA={{item.SKA}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PT=DIAMETER 时必选 --- -#}
        {%- if item.PT == 'DIAMETER' -%}
            DASWITCH={{item.DASWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加PCF与对端AF的链路。关闭SCTP双归属时需要执行本步骤。

#### 5.1 //DC1：

##### 5.1.1 //af0

```jinja2
{%- if is_scenario_sctp_dual_home_off -%}
    {%- for item in add_pafl_list -%}
        ADD PAFL:
        {#- --- 必选参数 --- -#}
        PCRFID={{item.PCRFID}},
        AFID={{item.AFID}},
        LNKID={{item.LNKID}},
        DISPMODE={{item.DISPMODE}},
        TPTYPE={{item.TPTYPE}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADSTS is not none -%}
            ADSTS={{item.ADSTS}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TPTYPE=SCTP 时必选 --- -#}
        {%- if item.TPTYPE == 'SCTP' -%}
            DUALHOME={{item.DUALHOME}},
        {%- endif -%}
        {#- --- 条件必选：TPTYPE=TCP 时必选 --- -#}
        {%- if item.TPTYPE == 'TCP' -%}
            IPVER={{item.IPVER}},
        {#- --- 条件必选：DUALHOME=OFF 时必选 --- -#}
        {%- elif item.DUALHOME == 'OFF' -%}
            IPVER={{item.IPVER}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {%- endif -%}
        {#- --- 条件必选：DISPMODE=SpecialQuintuple 时必选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            LPT={{item.LPT}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DISPMODE=SpecialQuintuple 时可选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            {%- if item.LPTMODE is not none -%}
                LPTMODE={{item.LPTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 //DC2：

##### 5.2.1 //af0

```jinja2
{%- if is_scenario_sctp_dual_home_off -%}
    {%- for item in add_pafl_list_4 -%}
        ADD PAFL:
        {#- --- 必选参数 --- -#}
        PCRFID={{item.PCRFID}},
        AFID={{item.AFID}},
        LNKID={{item.LNKID}},
        DISPMODE={{item.DISPMODE}},
        TPTYPE={{item.TPTYPE}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADSTS is not none -%}
            ADSTS={{item.ADSTS}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TPTYPE=SCTP 时必选 --- -#}
        {%- if item.TPTYPE == 'SCTP' -%}
            DUALHOME={{item.DUALHOME}},
        {%- endif -%}
        {#- --- 条件必选：TPTYPE=TCP 时必选 --- -#}
        {%- if item.TPTYPE == 'TCP' -%}
            IPVER={{item.IPVER}},
        {#- --- 条件必选：DUALHOME=OFF 时必选 --- -#}
        {%- elif item.DUALHOME == 'OFF' -%}
            IPVER={{item.IPVER}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {%- endif -%}
        {#- --- 条件必选：DISPMODE=SpecialQuintuple 时必选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            LPT={{item.LPT}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DISPMODE=SpecialQuintuple 时可选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            {%- if item.LPTMODE is not none -%}
                LPTMODE={{item.LPTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 增加对端AF实体。开启SCTP双归属时需要执行本步骤。

#### 6.1 //DC1：

```jinja2
{%- if is_scenario_sctp_dual_home_on -%}
    {%- for item in add_paf_list_2 -%}
        ADD PAF:
        {#- --- 必选参数 --- -#}
        PCRFID={{item.PCRFID}},
        AFID={{item.AFID}},
        DN="{{item.DN}}",
        HN="{{item.HN}}",
        PT={{item.PT}},
        ABILITYDICTID={{item.ABILITYDICTID}},
        {#- --- 可选参数 --- -#}
        {%- if item.PN is not none -%}
            PN="{{item.PN}}",
        {%- endif -%}
        {%- if item.LSMODE is not none -%}
            LSMODE={{item.LSMODE}},
        {%- endif -%}
        {%- if item.SBMODE is not none -%}
            SBMODE={{item.SBMODE}},
        {%- endif -%}
        {%- if item.SKA is not none -%}
            SKA={{item.SKA}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PT=DIAMETER 时必选 --- -#}
        {%- if item.PT == 'DIAMETER' -%}
            DASWITCH={{item.DASWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 增加PCF与对端AF的链路。开启SCTP双归属时需要执行本步骤。

#### 7.1 //DC1：

```jinja2
{%- if is_scenario_sctp_dual_home_on -%}
    {%- for item in add_pafl_list_8 -%}
        ADD PAFL:
        {#- --- 必选参数 --- -#}
        PCRFID={{item.PCRFID}},
        AFID={{item.AFID}},
        LNKID={{item.LNKID}},
        DISPMODE={{item.DISPMODE}},
        TPTYPE={{item.TPTYPE}},
        PPT={{item.PPT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ADSTS is not none -%}
            ADSTS={{item.ADSTS}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TPTYPE=SCTP 时必选 --- -#}
        {%- if item.TPTYPE == 'SCTP' -%}
            DUALHOME={{item.DUALHOME}},
        {%- endif -%}
        {#- --- 条件必选：DUALHOME=ON 时必选 --- -#}
        {%- if item.DUALHOME == 'ON' -%}
            DIPVER={{item.DIPVER}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            DLIP="{{item.DLIP}}",
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            LIP="{{item.LIP}}",
        {%- endif -%}
        {#- --- 条件必选：DISPMODE=SpecialQuintuple 时必选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            LPT={{item.LPT}},
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            DPIP="{{item.DPIP}}",
        {%- endif -%}
        {#- --- 条件必选：DIPVER=IPV4 时必选 --- -#}
        {%- if item.DIPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
        {%- elif item.IPVER == 'IPV4' -%}
            PIP="{{item.PIP}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DUALHOME=ON 时可选 --- -#}
        {%- if item.DUALHOME == 'ON' -%}
            {%- if item.CROSSPATH is not none -%}
                CROSSPATH={{item.CROSSPATH}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：DISPMODE=SpecialQuintuple 时可选 --- -#}
        {%- if item.DISPMODE == 'SpecialQuintuple' -%}
            {%- if item.LPTMODE is not none -%}
                LPTMODE={{item.LPTMODE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

