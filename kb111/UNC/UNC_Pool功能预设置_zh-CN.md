---
id: ''
name: Pool功能预设置
ne_type: UNC
type: feature
description: 新建SGSN Pool时对本Pool的功能和参数按前期规划好的数据进行配置。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","新建部署","激活业务","典型场景：SGSN Pool新建","全网新建","Pool功能预设置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
新建SGSN Pool时对本Pool的功能和参数按前期规划好的数据进行配置。

## 必备事项
前提条件

* 已经申请并加载具有SGSN Iu-flex功能的License和具有用户迁移功能的License。
* SGSN网元已经接入到U2020/MAE的操作维护系统，操作人员已经登录U2020/MAE服务器。
* 网元基础数据配置完成。
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
    - LICITEM: 'LKV2IUFLEX02'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在所有SGSN上打开Iu-flex和Gb-Flex开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 其中，LKV2IUFLEX02为Iu-flex特性的部件编码，LKV2GBFLEX02为Gb-flex特性的部件编码，LKV2SGSNMG02为SGSN Pool用户迁移特性的部件编码。

