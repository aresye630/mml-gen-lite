---
id: ''
name: 激活Mp2接口链路探测
ne_type: UEG
type: feature
description: MPF通过Mp2接口向UPF推送动态DNS Rule和动态Traffic Rule，可以在推送过程中根据消息处理确认Mp2接口链路是否正常。当没有Traffic Rule、DNS Rule消息时，为了避免MPF无法及时感知Mp2链路状态，MPF通过****SET MPFMP2ATTR****命令支持在无Traffic Rule、DNS Rule相关消息时的Mp2链路状态检测处理。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC APP业务访问控制（公共）","动态分流（MPF/UPF）","配置动态分流","激活动态分流规则下发（MPF）","激活Mp2接口链路探测"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
MPF通过Mp2接口向UPF推送动态DNS Rule和动态Traffic Rule，可以在推送过程中根据消息处理确认Mp2接口链路是否正常。当没有Traffic Rule、DNS Rule消息时，为了避免MPF无法及时感知Mp2链路状态，MPF通过****SET MPFMP2ATTR****命令支持在无Traffic Rule、DNS Rule相关消息时的Mp2链路状态检测处理。

## 必备事项
前提条件

请仔细阅读Mp2接口链路探测。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_mpfmp2attr_list:
      type: items
      properties:
        MP2DETECTSW:
          name: 'Mp2链路探测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置是否开启Mp2链路探测功能。   * 配置为“ENABLE”时，Mp2链路正常情况下，无论Mp2接口是否有动态规则推送消息，MPF按照MP2DETECTTIME设置的探测周期发送探测消息，MPF连续发送3条检测消息无响应时认为链路故障，上报ALM-81259 Mp2链路故障告警。 * 配置为“DISABLE”时，Mp2链路正常情况下，MPF不发送探测消息，当MPF根据动态规则推送时触发的ALM-81259 Mp2链路故障告警判断Mp2接口链路故障，主动发起链路探测消息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MP2DETECTTIME:
          name: 'Mp2链路探测周期'
          type: integer
          minimum: 30
          maximum: 1800
          required: false
          description: '设置Mp2链路探测的周期。修改探测周期后，先按照原探测周期进行探测，下一次探测消息按照修改后的探测周期发送。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_mpfmp2attr_list:
    - MP2DETECTSW: DISABLE
      MP2DETECTTIME: 60
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置MPF上Mp2链路探测开关和链路探测周期。

#### 1.1 //设置MPF上Mp2链路探测开关和链路探测周期。

```jinja2
{%- for item in set_mpfmp2attr_list -%}
    SET MPFMP2ATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.MP2DETECTSW is not none -%}
        MP2DETECTSW={{item.MP2DETECTSW}},
    {%- endif -%}
    {%- if item.MP2DETECTTIME is not none -%}
        MP2DETECTTIME={{item.MP2DETECTTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

