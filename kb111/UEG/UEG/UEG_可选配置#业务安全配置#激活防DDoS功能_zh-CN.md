---
id: ''
name: 激活防DDoS功能
ne_type: UEG
type: feature
description: 为了防止PDN侧网络设备遭受移动用户的DDoS攻击，运营商可以启用UEG的防范DDoS攻击功能。在UEG上配置报文连接最大速率，当UE向PDN侧网络设备发起TCP连接，如果UE发送的SYN报文连接速率超过配置值，UEG将丢弃报文，以保护PDN侧的网络设备。  * 适用于SGW-U、PGW-U、UPF。 * 当运营商需要通过UEG保护PDN侧指定范围服务器时开启此功能，典型场景下“DDos防护阈值”可使用系统初始值。功能开启后应密切观察KPI指标和DDoS攻击监测指标，例如“1914308686 用户平面上行丢弃报文数(DDoS攻击)”、“1914308724 用户平面上行丢弃IPv6报文数(DDoS攻击)”等性能指标的变化情况，确保网元正常功能不受影响。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","激活防DDoS功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为了防止PDN侧网络设备遭受移动用户的DDoS攻击，运营商可以启用UEG的防范DDoS攻击功能。在UEG上配置报文连接最大速率，当UE向PDN侧网络设备发起TCP连接，如果UE发送的SYN报文连接速率超过配置值，UEG将丢弃报文，以保护PDN侧的网络设备。* 适用于SGW-U、PGW-U、UPF。* 当运营商需要通过UEG保护PDN侧指定范围服务器时开启此功能，典型场景下“DDos防护阈值”可使用系统初始值。功能开启后应密切观察KPI指标和DDoS攻击监测指标，例如“1914308686 用户平面上行丢弃报文数(DDoS攻击)”、“1914308724 用户平面上行丢弃IPv6报文数(DDoS攻击)”等性能指标的变化情况，确保网元正常功能不受影响。

## 必备事项
前提条件

请仔细阅读GWFD-021403 防DDoS功能。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_ddos_list:
      type: items
      properties:
        THRESHOLD:
          name: 'DDos防护阈值'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: '允许发起最大TCP连接数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DDOSCHECK:
          name: '防DDOS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
  examples:
    set_ddos_list:
    - THRESHOLD: 10
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
      DDOSCHECK: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置DDoS攻击防护使用的流控阈值。

```jinja2
{%- for item in set_ddos_list -%}
    SET DDOS:
    {#- --- 必选参数 --- -#}
    THRESHOLD={{item.THRESHOLD}},
    ;
{%- endfor -%}
```

### 2 使能UserProfile的防范DDoS功能。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DDOSCHECK is not none -%}
        DDOSCHECK={{item.DDOSCHECK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

