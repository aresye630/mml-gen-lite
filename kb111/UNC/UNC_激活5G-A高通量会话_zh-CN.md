---
id: ''
name: 激活5G-A高通量会话
ne_type: UNC
type: feature
description: 当运营商需要单会话具备大带宽业务流接入能力时，激活此功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 高通量UPF选择方案","激活5G-A高通量会话"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要单会话具备大带宽业务流接入能力时，激活此功能。适用于PGW-U、UPF。

## 必备事项
前提条件

* SMF已经完成高通量UPF选择的相关配置。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
* 完成userprofile相关配置（与SMF侧规划保持一致）。
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
          description: '打开本特性的License配置开关。'
          data_source: '固定取值'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_flowletpara_list:
      type: items
      properties:
        FLOWOPTSW:
          name: '大流优化功能'
          type: string
          required: false
          description: '开启大流优化功能开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G55GHT01'
      SWITCH: ENABLE
    set_flowletpara_list:
    - FLOWOPTSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关：

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 开启大流优化功能开关。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_flowletpara_list的变量区（command: SET FLOWLETPARA） -#}
<!-- MISSING_MACRO: command=SET FLOWLETPARA list_name=set_flowletpara_list step_id=2 -->
```

