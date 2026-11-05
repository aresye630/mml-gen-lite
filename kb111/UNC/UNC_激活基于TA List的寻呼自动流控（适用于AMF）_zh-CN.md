---
id: ''
name: 激活基于TA List的寻呼自动流控（适用于AMF）
ne_type: UNC
type: feature
description: 本操作指导在运行网络中激活基于TA List的寻呼自动流控功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010901 基于TA List的寻呼自动流控","WSFD-010901 基于TA List的寻呼自动流控（适用于AMF）","激活基于TA List的寻呼自动流控（适用于AMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导在运行网络中激活基于TA List的寻呼自动流控功能。

## 必备事项
前提条件

* 请仔细阅读WSFD-010901 基于TA List的寻呼流控特性概述和实现原理（适用于AMF）。
* AMF已对接网管系统，并且在网管上创建5分钟周期的性能测量任务，并勾选如下指标和待监控的测量对象：
  + 1929450177 指定TAI组的N2模式寻呼请求次数
  + 1929449489 指定TAI组的N2模式寻呼成功率
  + 1929447376 指定TAI组的N2模式二次寻呼请求次数
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_perfngtaigroup_list:
      type: items
      properties:
        NGTAIGPN:
          name: 'NG TAI组名'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: '增加NG TAI组性能测量对象。  说明：  NG TAI组测量对象最多可以增加6000个，但仅能监控其中的2000个。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngtaigrpmem_list:
      type: items
      properties:
        NGTAIGPN:
          name: 'NG TAI组名'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '为NG TAI组性能测量对象增加TAI成员。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGNTAI:
          name: '起始TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ngtaipagingmonpara_list:
      type: items
      properties:
        SWITCH:
          name: 'SWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGSUCRATDEFVAL:
          name: 'PAGSUCRATDEFVAL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MINPAGREQTHD:
          name: 'MINPAGREQTHD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGRATEEXPTHD:
          name: 'PAGRATEEXPTHD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGREQEXPTHD:
          name: 'PAGREQEXPTHD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGEXPTIMESTHD:
          name: 'PAGEXPTIMESTHD'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PAGRETRYTIMES:
          name: 'PAGRETRYTIMES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSPAGINGSW:
          name: 'IMSPAGINGSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAIFCALARMSW:
          name: 'TAIFCALARMSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_perfngtaigroup_list:
    - NGTAIGPN: 'NG12300101000'
    add_ngtaigrpmem_list:
    - NGTAIGPN: 'NG12300101000'
      BGNTAI: '12300101000'
      ENDTAI: '12300101000'
    set_ngtaipagingmonpara_list:
    - SWITCH: ON
      PAGSUCRATDEFVAL: '90'
      MINPAGREQTHD: '1000'
      PAGRATEEXPTHD: '5'
      PAGREQEXPTHD: '20'
      PAGEXPTIMESTHD: '1'
      PAGRETRYTIMES: '0'
      IMSPAGINGSW: OFF
      TAIFCALARMSW: ON
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加NG TAI组性能测量对象。

```jinja2
{%- for item in add_perfngtaigroup_list -%}
    ADD PERFNGTAIGROUP:
    {#- --- 可选参数 --- -#}
    {%- if item.NGTAIGPN is not none -%}
        NGTAIGPN="{{item.NGTAIGPN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 为NG TAI组性能测量对象增加TAI成员。

```jinja2
{%- for item in add_ngtaigrpmem_list -%}
    ADD NGTAIGRPMEM:
    {#- --- 必选参数 --- -#}
    NGTAIGPN="{{item.NGTAIGPN}}",
    BGNTAI="{{item.BGNTAI}}",
    ENDTAI="{{item.ENDTAI}}",
    ;
{%- endfor -%}
```

### 3 设置NG TAI组对象寻呼异常监控功能参数。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_ngtaipagingmonpara_list的变量区（command: SET NGTAIPAGINGMONPARA） -#}
<!-- MISSING_MACRO: command=SET NGTAIPAGINGMONPARA list_name=set_ngtaipagingmonpara_list step_id=3 -->
```

