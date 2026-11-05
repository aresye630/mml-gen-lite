---
id: ''
name: 激活业务节点故障状态管理增强功能
ne_type: UNC
type: feature
description: 根据网络情况需要设置主控与业务节点之间的故障检测方式为HA+ETCD时，需要进行如下配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","Service Fabric特性","Service Fabric可靠性","SFFD-010030 分布式集群防脑裂","激活业务节点故障状态管理增强功能"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST VNFC')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
根据网络情况需要设置主控与业务节点之间的故障检测方式为HA+ETCD时，需要进行如下配置。

## 必备事项
前提条件

请仔细阅读SFFD-010030 分布式集群防脑裂。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_basesubhealth_list:
      type: items
      properties:
        ENABLEFLAG:
          name: 'ENABLEFLAG'
          type: string
          enum:
          - Disable
          - Enable
          required: true
          description: '配置Base链路亚健康信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICEINSTANCE:
          name: 'SERVICEINSTANCE'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_electservice_list:
      type: items
      properties:
        SERVICESWITCH:
          name: '仲裁服务开关配置'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LIGHTHOUSESWITCH:
          name: 'LIGHTHOUSESWITCH'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置主控与业务节点之间的故障检测方式为HA+ETCD。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVICEINSTANCE:
          name: 'SERVICEINSTANCE'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_basesubhealth_list:
    - ENABLEFLAG: Enable
      SERVICEINSTANCE: 'VNRS_VNFC_999'
    set_electservice_list:
    - SERVICESWITCH: ENABLE
      LIGHTHOUSESWITCH: ENABLE
      SERVICEINSTANCE: 'VNRS_VNFC_999'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 已经登录OM Portal，或者已登录U2020，或者登录MAE并进入Access子系统。

### 2 使用**LST VNFC**命令查询系统上部署的所有VNFC。

### 3 在步骤2查询出的所有VNFC上都执行如下两条命令：

#### 3.1 使用**SET BASESUBHEALTH**命令配置Base平面Base链路亚健康信息。

```jinja2
{%- set LST_VNFC=getParameterValue('LST VNFC') -%}
{%- if LST_VNFC -%}
    {%- for item in set_basesubhealth_list -%}
        SET BASESUBHEALTH:
        {#- --- 必选参数 --- -#}
        ENABLEFLAG={{item.ENABLEFLAG}},
        SERVICEINSTANCE="{{item.SERVICEINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 使用命令**SET ELECTSERVICE**配置主控与业务节点之间的故障检测方式为HA+ETCD。

```jinja2
{%- if LST_VNFC -%}
    {%- for item in set_electservice_list -%}
        SET ELECTSERVICE:
        {#- --- 必选参数 --- -#}
        SERVICEINSTANCE="{{item.SERVICEINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SERVICESWITCH is not none -%}
            SERVICESWITCH={{item.SERVICESWITCH}},
        {%- endif -%}
        {%- if item.LIGHTHOUSESWITCH is not none -%}
            LIGHTHOUSESWITCH={{item.LIGHTHOUSESWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

