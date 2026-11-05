---
id: ''
name: 激活网络侧发起专有PDP/承载建立
ne_type: UNC
type: feature
description: PS核心网的会话管理对用户的每一个PDN连接最多支持11条承载。  为了满足运营商对网络资源越来越精细化的管理需求，3GPP R8标准引入了网络侧发起专有承载创建的过程。IMS呼叫控制和PCC机制则利用PS核心网具备的这种由网络操作承载的机制，实现网络侧发起的IMS会话资源预留，为多媒体业务分配适合的承载。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109301 网络侧发起专有PDP/承载建立","激活网络侧发起专有PDP/承载建立"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
PS核心网的会话管理对用户的每一个PDN连接最多支持11条承载。为了满足运营商对网络资源越来越精细化的管理需求，3GPP R8标准引入了网络侧发起专有承载创建的过程。IMS呼叫控制和PCC机制则利用PS核心网具备的这种由网络操作承载的机制，实现网络侧发起的IMS会话资源预留，为多媒体业务分配适合的承载。

## 必备事项
前提条件

* 请仔细阅读WSFD-109301 网络侧发起专有PDP/承载建立。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
* 已完成配置与P-CSCF的对接数据（适用于SGW-C/PGW-C）和激活VoLTE基础语音业务（适用于SGW-C/PGW-C）。
* 已完成配置与PCRF对接数据。
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
    - LICITEM: ''
      SWITCH: ''
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

