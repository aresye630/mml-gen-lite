---
id: ''
name: 配置APN上下行防欺诈
ne_type: UEG
type: feature
description: 为避免用户通过UEG非法访问数据业务，UEG会对指定APN接入的上下行报文进行检查，如果报文中携带的用户IP不是在UEG上合法的IP地址，则判断用户存在欺诈行为，丢弃用户报文。  * 适用于PGW-U、UPF。 * 本功能不适用于GWFD-024101 支持Routing Behind MS特性。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","配置APN上下行防欺诈"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","配置APN上下行防欺诈"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","配置APN上下行防欺诈"]
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置安全数据（风筝L）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","配置APN上下行防欺诈"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为避免用户通过UEG非法访问数据业务，UEG会对指定APN接入的上下行报文进行检查，如果报文中携带的用户IP不是在UEG上合法的IP地址，则判断用户存在欺诈行为，丢弃用户报文。* 适用于PGW-U、UPF。* 本功能不适用于GWFD-024101 支持Routing Behind MS特性。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ANTISPOOFINGUL:
          name: '上行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ANTISPOOFINGDL:
          name: '下行防欺诈'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_apnaddressattr_list:
    - APN: 'apn1.com'
      ANTISPOOFINGUL: ENABLE
      ANTISPOOFINGDL: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置APN上下行防欺诈。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ANTISPOOFINGUL is not none -%}
        ANTISPOOFINGUL={{item.ANTISPOOFINGUL}},
    {%- endif -%}
    {%- if item.ANTISPOOFINGDL is not none -%}
        ANTISPOOFINGDL={{item.ANTISPOOFINGDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

