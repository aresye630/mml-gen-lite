---
id: ''
name: 配置禁止UE向逻辑接口发起PING报文
ne_type: UEG
type: feature
description: UE与UEG不需要通过PING报文调试网络的联通性时，为避免UE通过PING报文非法访问UEG，配置禁止UE向UEG逻辑接口发送PING报文功能。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE向逻辑接口发起PING报文"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE向逻辑接口发起PING报文"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE向逻辑接口发起PING报文"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","配置禁止UE向逻辑接口发起PING报文"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UE与UEG不需要通过PING报文调试网络的联通性时，为避免UE通过PING报文非法访问UEG，配置禁止UE向UEG逻辑接口发送PING报文功能。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_uepinginf_list:
      type: items
      properties:
        PINGSWITCH:
          name: 'Ping开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '仅对通过**ADD LOGICINF**添加的逻辑接口生效。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_uepinginf_list:
    - PINGSWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置禁止UE向逻辑接口发起PING报文。

```jinja2
{%- for item in set_uepinginf_list -%}
    SET UEPINGINF:
    {#- --- 必选参数 --- -#}
    PINGSWITCH={{item.PINGSWITCH}},
    ;
{%- endfor -%}
```

