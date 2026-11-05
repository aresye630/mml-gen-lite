---
id: ''
name: 配置HTTP信令数据
ne_type: UEG
type: feature
description: 接入5G SA/5G NSA/4G用户时，HTTP信令数据用于PCF/PCRF和AMF/SMF/PGW-C对接。  园区PCF/PCRF不支持与NRF通信，因此需要手动配置PCF/PCRF和AMF/SMF/PGW-C之间的服务发现。  * N7接口不支持传递PTT业务的策略，因此，部署PTT业务时，需要配置PCRF与PGW-C之间的Gx接口数据。详细配置请参见配置PCF与PCEF（基于Diameter协议）的对接数据。 * 未部署PTT业务的场景，为简化配置，PCF/PCRF与SMF/PGW-C均通过N7接口对接。不需要配置PCRF与PGW-C之间的Gx接口数据。    通过N7接口对接时，需要在SMF/PGW-C上通过**SET POLICYMODE**命令将“FORCED（指定策略接口）”设置为“Npcf（Npcf接口）”。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置PCF/PCRF","配置HTTP信令数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
接入5G SA/5G NSA/4G用户时，HTTP信令数据用于PCF/PCRF和AMF/SMF/PGW-C对接。园区PCF/PCRF不支持与NRF通信，因此需要手动配置PCF/PCRF和AMF/SMF/PGW-C之间的服务发现。* N7接口不支持传递PTT业务的策略，因此，部署PTT业务时，需要配置PCRF与PGW-C之间的Gx接口数据。详细配置请参见配置PCF与PCEF（基于Diameter协议）的对接数据。* 未部署PTT业务的场景，为简化配置，PCF/PCRF与SMF/PGW-C均通过N7接口对接。不需要配置PCRF与PGW-C之间的Gx接口数据。  通过N7接口对接时，需要在SMF/PGW-C上通过**SET POLICYMODE**命令将“FORCED（指定策略接口）”设置为“Npcf（Npcf接口）”。

## 必备事项
前提条件

已完成配置PCF基础数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_hlbdevaddr_list:
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
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '本端服务化接口IP，用于和SMF/AMF互通。   * 双DC场景，两个DC的服务化接口IP地址不能重复，如DC1用样例值，DC2用10.201.200.47等。 * 表格中未特殊说明的参数，两个DC保持一致。'
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
        HTTPSFUNC:
          name: 'HTTPS功能'
          type: string
          enum:
          - ON
          - OFF
          required: false
          description: '* AMF、SMF与PCF均由同一个UEG设备实现，可不开启HTTPS。 * HTTP端口号默认为8080，HTTPS端口号默认为443。'
          data_source: '与对端协商'
          pattern: ''
          default: ON
    set_httpclientcfg_list:
      type: items
      properties:
        LINKCTLMODE:
          name: '链路管理模式'
          type: string
          enum:
          - OLD
          - NEW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NEW
  examples:
    add_hlbdevaddr_list:
    - DEVAID: 2
      VPNNAME: 'VRF_SBI'
      IPVER: IPV4
      IP: '10.200.200.47'
      HTTPSFUNC: OFF
    - DEVAID: 2
      VPNNAME: 'VRF_SBI'
      IPVER: IPV4
      IP: '10.201.200.47'
      HTTPSFUNC: OFF
    set_httpclientcfg_list:
    - LINKCTLMODE: NEW
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“UEG MML命令”界面。

### 2 配置HTTP IP，用于和AMF/SMF/PGW-C通信。如已完成配置PCF基础数据中的HTTP IP数据配置，则不需要重复配置。

#### 2.1 //DC1：

```jinja2
{%- for item in add_hlbdevaddr_list -%}
    ADD HLBDEVADDR:
    {#- --- 必选参数 --- -#}
    DEVAID={{item.DEVAID}},
    VPNNAME="{{item.VPNNAME}}",
    IPVER={{item.IPVER}},
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPSFUNC is not none -%}
        HTTPSFUNC={{item.HTTPSFUNC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置HTTP客户端链路的管理模式。

```jinja2
{%- for item in set_httpclientcfg_list -%}
    SET HTTPCLIENTCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.LINKCTLMODE is not none -%}
        LINKCTLMODE={{item.LINKCTLMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

