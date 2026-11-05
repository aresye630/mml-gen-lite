---
id: GWFD-023002
name: 激活L2TP VPN
ne_type: UEG
type: feature
description: 利用本地配置部署L2TP组网，在UEG上配置指定APN下是否使能L2TP功能。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-023000 组网接口能力","GWFD-023002 L2TP VPN","GWFD-023002 L2TP VPN特性概述","激活L2TP VPN"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
利用本地配置部署L2TP组网，在UEG上配置指定APN下是否使能L2TP功能。适用于PGW-C、SMF

## 必备事项
前提条件

请仔细阅读GWFD-023002 L2TP VPN特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apnl2tpctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令 ****ADD CPAPN****配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        L2TPSWITCH:
          name: '支持L2TP功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_l2tpkey_list:
      type: items
      properties:
        ENSWITCH:
          name: '加密开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '加密开关在默认情况下设置为DISABLE，即明文携带L2TP私有信元，存在一定安全风险，建议和对端UPF同时开启加密功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_apnl2tpctrl_list:
    - APN: 'huawei.com'
      L2TPSWITCH: ENABLE
    set_l2tpkey_list:
    - ENSWITCH: DISABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置APN L2TP配置。

#### 2.1 //设置APN L2TP配置。

```jinja2
{%- for item in set_apnl2tpctrl_list -%}
    SET APNL2TPCTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.L2TPSWITCH is not none -%}
        L2TPSWITCH={{item.L2TPSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 (可选) 打开L2TP业务加密开关，增强N4接口传输安全。

```jinja2
{%- if is_optional_l2tp_encryption_switch -%}
    {%- for item in set_l2tpkey_list -%}
        SET L2TPKEY:
        {#- --- 可选参数 --- -#}
        {%- if item.ENSWITCH is not none -%}
            ENSWITCH={{item.ENSWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 对端UPF需要同时打开该功能，并且配置相同密钥，否则会导致L2TP业务失败。

