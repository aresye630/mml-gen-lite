---
id: ''
name: 激活设备标识检查特性（适用于5G）
ne_type: UNC
type: feature
description: 本章节指导如何在运行的5G网络中激活设备标识检查特性。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","安全管理功能","WSFD-103004 设备标识检查","设备标识检查（5G）","激活设备标识检查特性（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节指导如何在运行的5G网络中激活设备标识检查特性。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-103004 设备标识检查特性概述（适用于5G）。
* 完成AMF与5G-EIR对接，AMF与5G-EIR的对接配置请参考SBI接口（N8/N11/N12/N14/N15/N17/N20/N22/N50/NLs/NLg/N11mb）配置或配置和NF直连。
* 5G-EIR已激活设备标识检查功能。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ngpeiplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'GETIMEIPLC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHKIMEIPLC:
          name: 'CHKIMEIPLC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTTYPE:
          name: '流程类型'
          type: string
          required: false
          description: '如果希望某个流程开启PEI检查功能，则勾选该流程选项。如果希望某个流程不开启PEI检查功能，则去勾选该流程选项。如果希望系统保持某个流程当前设置值，则灰化该流程选项。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEIACCESS:
          name: 'PEI获取失败是否允许接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTFLAG:
          name: 'PEI检查超时是否允许接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GRALLOW:
          name: '是否允许灰名单用户接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BALLOW:
          name: '是否允许黑名单用户接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EMERGENCYSW:
          name: '是否允许紧急注册用户接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DISCFAIL:
          name: '是否允许EIR发现失败时接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKFAIL:
          name: '是否允许EIR返回失败时接入'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RETRYSW:
          name: '是否重选EIR'
          type: string
          required: false
          description: '如果5G-EIR返回5xx原因值时，AMF选择新的5G-EIR重试业务请求。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        REDIRECTSW:
          name: '是否支持EIR重定向'
          type: string
          required: false
          description: '如果5G-EIR返回307临时重定向或308永久重定向时，AMF支持根据重定向指示选择新的5G-EIR重试业务请求。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPEIPLCY:
          name: 'PEI获取策略'
          type: string
          required: false
          description: 'PEI获取策略和PEI检查策略需配置一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHKPEIPLCY:
          name: 'PEI检查策略'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2EIR02'
      SWITCH: ENABLE
    add_ngpeiplcy_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '12303'
      GETIMEIPLC: IMEISV
      CHKIMEIPLC: IMEISV
      PROTTYPE: INIT_REG-1&MOBL_INTER_REG-1&REG_AFT_INTERHO-1&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-1
      PEIACCESS: YES
      CTFLAG: YES
      GRALLOW: YES
      BALLOW: NO
      EMERGENCYSW: YES
      DISCFAIL: YES
      CHKFAIL: YES
      RETRYSW: YES
      REDIRECTSW: YES
      GETPEIPLCY: GETIMEISV
      CHKPEIPLCY: CHKIMEISV
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置5G网络PEI获取和检查策略。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_ngpeiplcy_list的变量区（command: ADD NGPEIPLCY） -#}
<!-- MISSING_MACRO: command=ADD NGPEIPLCY list_name=add_ngpeiplcy_list step_id=3 -->
```

