---
id: ''
name: 配置大流量防攻击
ne_type: UEG
type: feature
description: 配置大流量防攻击功能，可以防止用户发起大流量报文攻击。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","虚机容器模式UEG安全加固","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","裸机容器模式UEG安全加固","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S安全加固配置","安全配置建议","可选配置","业务安全配置","配置大流量防攻击"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
配置大流量防攻击功能，可以防止用户发起大流量报文攻击。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_trfcdfdswitch_list:
      type: items
      properties:
        UPSWITCH:
          name: '上行大流量攻击检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '**SET TRFCDFDSWITCH**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNSWITCH:
          name: '下行大流量攻击检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_trfcdfdswitch_list:
    - UPSWITCH: ENABLE
      DOWNSWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置大流量防攻击功能。

```jinja2
{%- for item in set_trfcdfdswitch_list -%}
    SET TRFCDFDSWITCH:
    {#- --- 必选参数 --- -#}
    UPSWITCH={{item.UPSWITCH}},
    DOWNSWITCH={{item.DOWNSWITCH}},
    ;
{%- endfor -%}
```

