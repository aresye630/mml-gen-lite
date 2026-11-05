---
id: GWFD-112002
name: 激活5G-A高通量会话
ne_type: UDG
type: feature
description: 当运营商需要UDG单会话具备大带宽业务流接入能力时，激活此功能。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能转发解决方案","GWFD-112002 5G-A高通量会话","激活5G-A高通量会话"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要UDG单会话具备大带宽业务流接入能力时，激活此功能。适用于PGW-U、UPF。

## 必备事项
前提条件

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
          enum:
          - DISABLE
          - ENABLE
          - FLOWCHK
          required: false
          description: '开启大流优化功能开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CPUBIASDIFF:
          name: '启动优化的线程CPU偏差阈值'
          type: integer
          minimum: 5
          maximum: 50
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPUOVERLOADTHR:
          name: '启动优化的线程CPU阈值'
          type: integer
          minimum: 50
          maximum: 90
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWCHKPPS:
          name: '大流检测速率'
          type: integer
          minimum: 50000
          maximum: 5000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWGUARDPKTNUM:
          name: '大流优化保护报文数'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWGUARDTIME:
          name: '大流优化的保护时间'
          type: integer
          minimum: 5
          maximum: 500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THREADUPDINT:
          name: '线程负载更新间隔'
          type: integer
          minimum: 64
          maximum: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G55GHT01'
      SWITCH: ENABLE
    set_flowletpara_list:
    - FLOWOPTSW: ENABLE
      CPUBIASDIFF: ''
      CPUOVERLOADTHR: ''
      FLOWCHKPPS: ''
      FLOWGUARDPKTNUM: ''
      FLOWGUARDTIME: ''
      THREADUPDINT: ''
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
{%- for item in set_flowletpara_list -%}
    SET FLOWLETPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FLOWOPTSW is not none -%}
        FLOWOPTSW={{item.FLOWOPTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.CPUBIASDIFF is not none -%}
            CPUBIASDIFF={{item.CPUBIASDIFF}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.CPUOVERLOADTHR is not none -%}
            CPUOVERLOADTHR={{item.CPUOVERLOADTHR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.FLOWCHKPPS is not none -%}
            FLOWCHKPPS={{item.FLOWCHKPPS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.FLOWGUARDPKTNUM is not none -%}
            FLOWGUARDPKTNUM={{item.FLOWGUARDPKTNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.FLOWGUARDTIME is not none -%}
            FLOWGUARDTIME={{item.FLOWGUARDTIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：FLOWOPTSW=FLOWCHK/ENABLE 时可选 --- -#}
    {%- if item.FLOWOPTSW in ['FLOWCHK', 'ENABLE'] -%}
        {%- if item.THREADUPDINT is not none -%}
            THREADUPDINT={{item.THREADUPDINT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

