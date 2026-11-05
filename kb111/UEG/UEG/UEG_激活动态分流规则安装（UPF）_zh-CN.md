---
id: ''
name: 激活动态分流规则安装（UPF）
ne_type: UEG
type: feature
description: UPF上的动态规则生效原则受本地配置控制，本地配置支持两种粒度：DNN级别通过**SET APNAPPPARA**命令配置、全局级别通过**SET GLBAPPPARA**命令配置，其中，DNN级别优先级大于全局级别。根据全局/DNN级配置控制UPF上的APP动态规则如何安装生效。  适用于UPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置业务数据（风筝S）","APP集成管理功能","配置UPF","激活动态分流规则安装（UPF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPF上的动态规则生效原则受本地配置控制，本地配置支持两种粒度：DNN级别通过**SET APNAPPPARA**命令配置、全局级别通过**SET GLBAPPPARA**命令配置，其中，DNN级别优先级大于全局级别。根据全局/DNN级配置控制UPF上的APP动态规则如何安装生效。适用于UPF。

## 必备事项
前提条件

请仔细阅读动态分流规则安装（UPF）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_glbapppara_list:
      type: items
      properties:
        APPRVALIDCOND:
          name: 'App规则生效条件'
          type: string
          enum:
          - N4_INDICATION
          - N4_UNRELATED
          required: false
          description: '* “N4\_INDICATION”：APP所有动态规则需要根据PDR携带的Application ID生效。 * “N4\_UNRELATED”：APP动态规则不根据PDR携带的Application ID生效，不论N4接口是否下发Application ID，均进行APP动态规则匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GENERALAPPID:
          name: '通用应用标识'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '全局Application ID，该参数用于和SMF下发的PDR中携带的Application ID进行匹配。   * 如果PDR中Application ID优先匹配上“GENERALAPPID”，则所有动态规则在后续流匹配中均生效。 * 如果PDR中Application ID未匹配上“GENERALAPPID”，但匹配上某一动态规则中对应的Application ID，则后续流匹配仅对某一动态规则生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnapppara_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPRVALIDCOND:
          name: 'App规则生效条件'
          type: string
          enum:
          - INHERIT
          - N4_INDICATION
          - N4_UNRELATED
          required: true
          description: '配置APN的APP动态规则匹配条件。   * “INHERIT”：继承全局配置。表明该生效条件是继承**SET GLBAPPPARA**命令中参数“APPRVALIDCOND”的取值范围。 * “N4\_INDICATION”：根据N4接口下发的Application ID作为APP规则的匹配条件。 * “N4\_UNRELATED”：不论N4接口是否下发Application ID，均进行APP规则匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_glbapppara_list:
    - APPRVALIDCOND: N4_INDICATION
      GENERALAPPID: 'huaweiapp'
    set_apnapppara_list:
    - APN: 'apn1'
      APPRVALIDCOND: N4_INDICATION
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **可选**：配置全局的APP动态分流规则匹配条件。

#### 1.1 //任务一：配置全局的APP动态分流规则匹配条件，添加全局Application ID，UPF收到SMF下发的PDR，优先匹配该Application ID，所有动态规则支持后续的数据流匹配。

```jinja2
{%- if is_optional_global_app_rule_match_condition -%}
    {%- for item in set_glbapppara_list -%}
        SET GLBAPPPARA:
        {#- --- 可选参数 --- -#}
        {%- if item.APPRVALIDCOND is not none -%}
            APPRVALIDCOND={{item.APPRVALIDCOND}},
        {%- endif -%}
        {%- if item.GENERALAPPID is not none -%}
            GENERALAPPID="{{item.GENERALAPPID}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **可选**：配置DNN级的APP动态分流规则匹配条件。

#### 2.1 //任务二：配置DNN级的APP动态分流规则匹配条件，指定DNN的用户访问APP时，根据N4接口下发的Application ID作为APP动态规则的匹配条件。

```jinja2
{%- if is_optional_dnn_app_rule_match_condition -%}
    {%- for item in set_apnapppara_list -%}
        SET APNAPPPARA:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        APPRVALIDCOND={{item.APPRVALIDCOND}},
        ;
    {%- endfor -%}
{%- endif -%}
```

