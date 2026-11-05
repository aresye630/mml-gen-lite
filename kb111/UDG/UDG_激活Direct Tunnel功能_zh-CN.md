---
id: GWFD-020422
name: 激活Direct Tunnel功能
ne_type: UDG
type: feature
description: 适用于PGW-U。  新建网络，需要部署Direct Tunnel时，如果满足如下条件，推荐使用本方案：  接入网与核心网的承载网合一。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","组网功能","GWFD-020422 Direct Tunnel功能","激活Direct Tunnel功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
适用于PGW-U。新建网络，需要部署Direct Tunnel时，如果满足如下条件，推荐使用本方案：接入网与核心网的承载网合一。

## 必备事项
前提条件

* 完成各网元的软件升级。
* 完成各网元的基本配置。
* 完成配置PGW-C到SGSN的数据。
* 完成配置PGW-U到SGSN/RNC的数据。
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5DTTL01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置RNC。

### RNC的Direct Tunnel配置，除需添加到PGW-U和PGW-C的路由外，与Indirect Tunnel模式下的Iu-PS接口配置无异。相关配置请参考RNC相关产品手册。

### 2 配置SGSN。

### SGSN的Direct Tunnel配置，除个别参数外，与Indirect Tunnel配置无异。相关配置请参考“UNC 产品文档 > UNC初始配置与调测 > 配置对接数据 >  配置逻辑接口及业务数据 >  融合网络 >  配置SGSN”。

### 3 打开本特性的License配置开关。

#### 3.1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

