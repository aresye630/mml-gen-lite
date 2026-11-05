---
id: ''
name: 配置PCF与PCEF（基于Diameter协议）的对接数据
ne_type: UEG
type: feature
description: PCF/PCRF通过Gx接口（基于Diameter协议）与SMF/PGW-C对接时，请参考本页面进行配置。  N7接口不支持传递PTT业务的策略，因此，部署PTT业务时，需要配置该页面。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置PCF/PCRF","配置PCF与PCEF（基于Diameter协议）的对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
PCF/PCRF通过Gx接口（基于Diameter协议）与SMF/PGW-C对接时，请参考本页面进行配置。N7接口不支持传递PTT业务的策略，因此，部署PTT业务时，需要配置该页面。

## 必备事项
前提条件

已完成配置PCF基础数据。
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
          description: '-'
          data_source: '固定取值'
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
          description: '本端Diameter IP，用于和PCEF互通。   * 双DC场景，两个DC的Diameter IP地址不能重复，如DC1用样例值，DC2用10.201.200.87等。 * 表格中未特殊说明的参数，两个DC保持一致。'
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
    add_ppcef_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: 'PCRF标识采用**ADD PCRF**定义的PCRF标识。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PCEFID:
          name: '对端PCEF标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '该参数不允许重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PN:
          name: '对端名称'
          type: string
          minLength: 0
          maxLength: 128
          required: false
          description: '-'
          data_source: '本端规划'
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
        DN:
          name: '对端域名'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: '对接PCEF的域名和主机名。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        HN:
          name: '对端主机名'
          type: string
          minLength: 0
          maxLength: 127
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        LSMODE:
          name: '链路选择模式'
          type: string
          enum:
          - SINGLE_LINK
          - LOAD_BALANCE
          required: false
          description: '-'
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: SHARE
        DASWITCH:
          name: '审计开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        DATIME:
          name: '设备间审计时长'
          type: integer
          minimum: 720
          maximum: 1440
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        ABILITYDICTID:
          name: '能力字典ID'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        SKA:
          name: '业务保活时长'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: 90@90
    add_ppcefl_list:
      type: items
      properties:
        PCRFID:
          name: 'PCRF标识'
          type: integer
          minimum: 1
          maximum: 1
          required: true
          description: 'PCRF标识采用**ADD PCRF**定义的PCRF标识。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        PCEFID:
          name: '对端PCEF标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '与**ADD PPCEF**命令中定义的PCEFID一致。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        LNKID:
          name: '对端链路标识'
          type: integer
          minimum: 0
          maximum: 3
          required: true
          description: '-'
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
          - SCTP
          - TCP
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '此处以IPv4为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LIP:
          name: '本端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: '采用表1中规划的IP。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LPT:
          name: '本地侦听端口'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PIP:
          name: '对端IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: 'SMF上的Gx接口IP。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PPT:
          name: '对端端口'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '取值为0，表示不对对端端口做限制。'
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: MultiplePorts
        DUALHOME:
          name: '双归属开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
  examples:
    add_dlbvpn_list:
    - VPNINDEX: 6
      VPNNAME: '_public_'
    - VPNINDEX: 6
      VPNNAME: '_public_'
    add_dlbdevaddr_list:
    - DEVAID: 6
      VPNINDEX: 6
      IPVER: IPV4
      IP: '10.200.200.87'
    - DEVAID: 6
      VPNINDEX: 4
      IPVER: IPV4
      IP: '10.201.200.87'
    add_ppcef_list:
    - PCRFID: 1
      PCEFID: 71
      PN: 'smf01'
      PT: DIAMETER
      DN: 'smf01.huawei.com'
      HN: 'smf01'
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: ON
      DATIME: 720
      ABILITYDICTID: 68
      SKA: 90
    - PCRFID: 1
      PCEFID: 72
      PN: 'smf02'
      PT: DIAMETER
      DN: 'smf02.huawei.com'
      HN: 'smf02'
      LSMODE: LOAD_BALANCE
      SBMODE: SHARE
      DASWITCH: ON
      DATIME: 720
      ABILITYDICTID: 68
      SKA: 90
    add_ppcefl_list:
    - PCRFID: 1
      PCEFID: 71
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: TCP
      IPVER: IPV4
      LIP: '10.200.200.87'
      LPT: 3868
      PIP: '10.200.200.88'
      PPT: 0
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DUALHOME: ''
      DIPVER: ''
    - PCRFID: 1
      PCEFID: 72
      LNKID: 0
      DISPMODE: SpecialQuintuple
      TPTYPE: TCP
      IPVER: IPV4
      LIP: '10.201.200.87'
      LPT: 3868
      PIP: '10.201.200.88'
      PPT: 0
      ADSTS: ENABLE
      LPTMODE: MultiplePorts
      DUALHOME: ''
      DIPVER: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 配置Diameter信令IP，用于和PCEF（基于Diameter协议）通信。如已完成配置PCF基础数据中的和PCEF（基于Diameter协议）互通的Diameter信令IP数据，则不需要重复配置。

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

### 3 增加PCEF实体。

#### 3.1 //DC1：

```jinja2
{%- for item in add_ppcef_list -%}
    ADD PPCEF:
    {#- --- 必选参数 --- -#}
    PCRFID={{item.PCRFID}},
    PCEFID={{item.PCEFID}},
    PT={{item.PT}},
    HN="{{item.HN}}",
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
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PT=DIAMETER 时必选 --- -#}
    {%- if item.PT == 'DIAMETER' -%}
        DN="{{item.DN}}",
    {%- endif -%}
    {#- --- 条件必选：DASWITCH=ON 时必选 --- -#}
    {%- if item.DASWITCH == 'ON' -%}
        DATIME={{item.DATIME}},
    {%- endif -%}
    {#- --- 条件必选：PT=DIAMETER 时必选 --- -#}
    {%- if item.PT == 'DIAMETER' -%}
        ABILITYDICTID={{item.ABILITYDICTID}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：PT=DIAMETER 时可选 --- -#}
    {%- if item.PT == 'DIAMETER' -%}
        {%- if item.DASWITCH is not none -%}
            DASWITCH={{item.DASWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PT=DIAMETER 时可选 --- -#}
    {%- if item.PT == 'DIAMETER' -%}
        {%- if item.SKA is not none -%}
            SKA={{item.SKA}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置Gx链路信息。

#### 4.1 //DC1：

```jinja2
{%- for item in add_ppcefl_list -%}
    ADD PPCEFL:
    {#- --- 必选参数 --- -#}
    PCRFID={{item.PCRFID}},
    PCEFID={{item.PCEFID}},
    LNKID={{item.LNKID}},
    DISPMODE={{item.DISPMODE}},
    TPTYPE={{item.TPTYPE}},
    PPT={{item.PPT}},
    {#- --- 可选参数 --- -#}
    {%- if item.ADSTS is not none -%}
        ADSTS={{item.ADSTS}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
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
```

