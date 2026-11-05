---
id: ''
name: 配置IP Spoofing防攻击
ne_type: UEG
type: feature
description: IP Spoofing防攻击配置可以防范用户伪造源地址IP向本端网元以及其他用户发起的恶意攻击。  * 适用于SGW-U、PGW-U、UPF。 * 建议首先通过**SET IPSPOOFALMTHD**开启IP Spoofing攻击检测并观察ALM-81008 IP spoofing告警上报情况评估是否存在攻击者。在评估攻击后确认须开启用户去活保护时通过**SET ANTISPOOFINGTHD**开启防护，功能开启后应密切观察KPI指标和用户会话去活相关性能统计指标变化情况，确保网元正常功能不受影响。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","配置IP Spoofing防攻击"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
IP Spoofing防攻击配置可以防范用户伪造源地址IP向本端网元以及其他用户发起的恶意攻击。* 适用于SGW-U、PGW-U、UPF。* 建议首先通过**SET IPSPOOFALMTHD**开启IP Spoofing攻击检测并观察ALM-81008 IP spoofing告警上报情况评估是否存在攻击者。在评估攻击后确认须开启用户去活保护时通过**SET ANTISPOOFINGTHD**开启防护，功能开启后应密切观察KPI指标和用户会话去活相关性能统计指标变化情况，确保网元正常功能不受影响。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_antispoofingthd_list:
      type: items
      properties:
        THRESHOLD:
          name: '攻击用户去活报文的阈值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '**SET ANTISPOOFINGTHD**  建议根据网络实际情况设置攻击用户去活报文的阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_antispoofingthd_list:
    - THRESHOLD: 1000
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置用户去活报文阈值。

```jinja2
{%- for item in set_antispoofingthd_list -%}
    SET ANTISPOOFINGTHD:
    {#- --- 必选参数 --- -#}
    THRESHOLD={{item.THRESHOLD}},
    ;
{%- endfor -%}
```

