---
id: ''
name: 配置禁止UE互访功能
ne_type: UEG
type: feature
description: 为了防止UE之间的恶意攻击，保证UE的安全，可以在UEG上配置整机APN、指定APN内或APN间禁止UE互访。如果涉及跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","虚机容器模式UEG安全加固","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","裸机容器模式UEG安全加固","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S安全加固配置","安全配置建议","必选配置","业务安全配置","配置禁止UE互访功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为了防止UE之间的恶意攻击，保证UE的安全，可以在UEG上配置整机APN、指定APN内或APN间禁止UE互访。如果涉及跨UPF网元的不同UE会话的互访控制，需要在UPF上配置ACL规则。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_globuemutacc_list:
      type: items
      properties:
        INNERAPNS:
          name: '同APN内的控制开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '整机所有APN内及APN间的UE均不允许互访。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERAPNS:
          name: '不同APN间的控制开关'
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
    set_globuemutacc_list:
    - INNERAPNS: ENABLE
      INTERAPNS: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 开启全局UE互访控制开关。

#### 1.1 //整机粒度APN内UE互访控制开关配置为开启，整机粒度APN间UE互访控制开关配置为开启。

```jinja2
{%- for item in set_globuemutacc_list -%}
    SET GLOBUEMUTACC:
    {#- --- 必选参数 --- -#}
    INNERAPNS={{item.INNERAPNS}},
    INTERAPNS={{item.INTERAPNS}},
    ;
{%- endfor -%}
```

### 需要控制指定APN内或者APN间的UE互访，可以通过**SET APNUEMUTACC**命令控制。

### “不同APN间的控制开关（INTERAPNS）”：用于控制是否允许其他APN向本APN发送报文。如果该参数设置为“ENABLE”，则丢弃其他APN的UE向本APN的UE发送的报文。如果该参数设置为“DISABLE”，则放通其他APN的UE向本APN的UE发送的报文。

### “同APN内的控制开关（INNERAPNS）”：用于控制是否允许APN内的UE之间互访。如果参数设置为“ENABLE”，则丢弃APN内UE发送的报文。如果该参数设置为“DISABLE”，则放通APN内UE发送的报文。

