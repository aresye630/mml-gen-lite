---
id: GWFD-111283
name: 激活智能板订阅和采集
ne_type: UDG
type: feature
description: 当运营商想要部署VVIP用户质差监测和保障**、**小区拥塞优化等智能业务时，需要配置本页面，完成智能板业务相关部署。  适用于UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","报表功能","GWFD-111283 智能板订阅和采集","激活智能板订阅和采集"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商想要部署VVIP用户质差监测和保障**、**小区拥塞优化等智能业务时，需要配置本页面，完成智能板业务相关部署。适用于UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-111283 智能板订阅和采集特性概述。
* 已完成业务感知配置。
* 已完成激活报表功能。
* 已完成**软件安装**手册中的**安装SSU服务**。
* 已完成加载License。
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
    set_ssuagingcfg_list:
      type: items
      properties:
        FLOWAGINGTIME:
          name: '业务流老化时间'
          type: integer
          minimum: 5
          maximum: 7200
          required: false
          description: '用于设置业务流老化时间。整数类型，取值范围5~7200，单位为秒，缺省值30。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SESSAGINGTIME:
          name: 'Session表老化时间'
          type: integer
          minimum: 5
          maximum: 7200
          required: false
          description: '用于设置Session表老化时间。整数类型，取值范围5~7200，单位为分钟，缺省值60。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5IBIC01'
      SWITCH: ENABLE
    set_ssuagingcfg_list:
    - FLOWAGINGTIME: 30
      SESSAGINGTIME: 60
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置SSU老化参数。

```jinja2
{%- for item in set_ssuagingcfg_list -%}
    SET SSUAGINGCFG:
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWAGINGTIME is not none -%}
        FLOWAGINGTIME={{item.FLOWAGINGTIME}},
    {%- endif -%}
    {%- if item.SESSAGINGTIME is not none -%}
        SESSAGINGTIME={{item.SESSAGINGTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

