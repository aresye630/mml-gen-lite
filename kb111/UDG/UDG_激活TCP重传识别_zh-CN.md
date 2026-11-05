---
id: GWFD-020307
name: 激活TCP重传识别
ne_type: UDG
type: feature
description: UDG通过对用户三四层数据报文进行分析和检测，识别出TCP重传报文，并根据配置对重传报文流量实施灵活的计费策略。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","计费功能","GWFD-020307 TCP重传识别","激活TCP重传识别"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
UDG通过对用户三四层数据报文进行分析和检测，识别出TCP重传报文，并根据配置对重传报文流量实施灵活的计费策略。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读GWFD-020307 TCP重传识别。
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
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '为用户模板添加TCP重传使用量上报规则，并打开TCP重传计费。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TCPCHGPROFLAG:
          name: 'TCP重传计费标识'
          type: string
          enum:
          - CHARGING
          - NOCHARGING
          - NOTCONFIG
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TCPURRGRPNAME:
          name: 'TCP重传URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5TCPR01'
      SWITCH: ENABLE
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'userprofile001'
      TCPCHGPROFLAG: CHARGING
      TCPURRGRPNAME: 'cp_tcp'
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

### 2 请参考部署UPF配置，配置的差异在于UserProfile绑定TCP重传使用量上报规则组，为用户模板添加TCP重传使用量上报规则，并打开TCP重传计费。

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TCPCHGPROFLAG is not none -%}
        TCPCHGPROFLAG={{item.TCPCHGPROFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TCPCHGPROFLAG=CHARGING 时必选 --- -#}
    {%- if item.TCPCHGPROFLAG == 'CHARGING' -%}
        TCPURRGRPNAME="{{item.TCPURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

